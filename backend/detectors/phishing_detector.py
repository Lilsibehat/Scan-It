import requests
import logging
from urllib.parse import urlparse
import re

logger = logging.getLogger(__name__)

class PhishingDetector:
    """Detects phishing URLs using URLhaus API and pattern matching"""
    
    def __init__(self, api_key=None):
        self.api_key = api_key
        self.urlhaus_api = 'https://urlhaus-api.abuse.ch/v1/url/'
        self.suspicious_patterns = [
            r'bit\.ly',
            r'tinyurl',
            r'goo\.gl',
            r'short\.link',
            r'login',
            r'verify',
            r'confirm',
            r'update',
            r'suspend',
        ]
    
    def detect(self, url):
        """Detect if URL is phishing"""
        try:
            # Check URLhaus database
            urlhaus_result = self._check_urlhaus(url)
            
            # Check URL patterns
            pattern_score = self._check_patterns(url)
            
            # Analyze domain
            domain_score = self._analyze_domain(url)
            
            # Calculate overall risk
            risk_score = (urlhaus_result.get('risk', 0) + pattern_score + domain_score) / 3
            
            return {
                'url': url,
                'is_phishing': risk_score > 0.6,
                'confidence': min(risk_score, 1.0),
                'risk_score': round(risk_score, 2),
                'details': {
                    'urlhaus_detection': urlhaus_result,
                    'pattern_score': pattern_score,
                    'domain_analysis': domain_score
                }
            }
        
        except Exception as e:
            logger.error(f'Error in phishing detection: {str(e)}')
            return {
                'url': url,
                'is_phishing': False,
                'confidence': 0.0,
                'error': str(e)
            }
    
    def _check_urlhaus(self, url):
        """Check URL against URLhaus database"""
        try:
            response = requests.post(
                self.urlhaus_api,
                data={'url': url},
                timeout=10
            )
            
            if response.status_code == 200:
                data = response.json()
                query_status = data.get('query_status')
                
                if query_status == 'ok':
                    threat = data.get('threat', 'unknown')
                    return {
                        'detected': True,
                        'threat': threat,
                        'risk': 0.8 if threat != 'unknown' else 0.2
                    }
            
            return {'detected': False, 'risk': 0.0}
        
        except Exception as e:
            logger.warning(f'URLhaus check failed: {str(e)}')
            return {'detected': False, 'risk': 0.0, 'error': str(e)}
    
    def _check_patterns(self, url):
        """Check URL for suspicious patterns"""
        score = 0.0
        
        for pattern in self.suspicious_patterns:
            if re.search(pattern, url, re.IGNORECASE):
                score += 0.15
        
        return min(score, 1.0)
    
    def _analyze_domain(self, url):
        """Analyze domain for suspicious characteristics"""
        score = 0.0
        
        try:
            parsed = urlparse(url)
            domain = parsed.netloc.lower()
            
            # Check for IP address instead of domain
            if re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', domain):
                score += 0.3
            
            # Check for excessive subdomains
            if domain.count('.') > 3:
                score += 0.2
            
            # Check for typosquatting patterns
            common_domains = ['google', 'amazon', 'facebook', 'microsoft', 'apple']
            for dom in common_domains:
                if dom in domain and not domain.startswith(dom):
                    score += 0.3
            
            # Check for non-standard TLDs
            if domain.endswith(('.tk', '.ml', '.ga', '.cf')):
                score += 0.2
        
        except Exception as e:
            logger.warning(f'Domain analysis error: {str(e)}')
        
        return min(score, 1.0)
