import logging
import re
from textblob import TextBlob

logger = logging.getLogger(__name__)

class ScamDetector:
    """Detects scam and fraudulent content"""
    
    def __init__(self):
        self.scam_keywords = [
            'click here', 'urgent action', 'verify account', 'confirm identity',
            'limited time', 'act now', 'congratulations won', 'claim prize',
            'update payment', 'confirm password', 'reset account', 'unusual activity',
            'suspended', 'locked', 'authenticate', 're-confirm', 'validate',
        ]
        
        self.urgency_words = [
            'urgent', 'immediately', 'asap', 'right now', 'today', 'limited',
            'expire', 'deadline', 'now', 'hurry', 'quick', 'act fast',
        ]
        
        self.phishing_phrases = [
            'dear customer',
            'valued customer',
            'dear sir',
            'dear madam',
            'dear member',
        ]
    
    def detect_url(self, url):
        """Detect scam characteristics in URL"""
        try:
            score = 0.0
            
            # Check for suspicious URL patterns
            if any(keyword in url.lower() for keyword in ['login', 'signin', 'verify', 'confirm']):
                score += 0.2
            
            # Check for URL shorteners
            if any(short in url for short in ['bit.ly', 'tinyurl', 'goo.gl', 'short.link']):
                score += 0.15
            
            # Check for suspicious TLDs
            if any(tld in url for tld in ['.tk', '.ml', '.ga', '.cf', '.top', '.download']):
                score += 0.2
            
            return {
                'url': url,
                'is_scam': score > 0.5,
                'confidence': min(score, 1.0),
                'score': round(score * 100, 2)
            }
        
        except Exception as e:
            logger.error(f'URL scam detection error: {str(e)}')
            return {'url': url, 'is_scam': False, 'confidence': 0.0}
    
    def detect_email(self, content):
        """Detect scam characteristics in email"""
        try:
            score = 0.0
            content_lower = content.lower()
            
            # Check for scam keywords
            keyword_count = sum(1 for keyword in self.scam_keywords if keyword in content_lower)
            score += min(keyword_count * 0.1, 0.3)
            
            # Check for urgency language
            urgency_count = sum(1 for word in self.urgency_words if word in content_lower)
            score += min(urgency_count * 0.1, 0.3)
            
            # Check for generic greetings (phishing indicator)
            greeting_count = sum(1 for phrase in self.phishing_phrases if phrase in content_lower)
            score += min(greeting_count * 0.15, 0.3)
            
            # Check for requests for personal information
            personal_info_requests = ['password', 'ssn', 'credit card', 'bank account', 'pin']
            if any(request in content_lower for request in personal_info_requests):
                score += 0.3
            
            # Sentiment analysis (scams often have mixed/suspicious sentiment)
            try:
                sentiment = TextBlob(content).sentiment.polarity
                if sentiment < 0.2 or sentiment > 0.9:  # Very negative or very positive
                    score += 0.1
            except:
                pass
            
            return {
                'content_preview': content[:100],
                'is_scam': score > 0.5,
                'confidence': min(score, 1.0),
                'score': round(score * 100, 2),
                'red_flags': self._get_red_flags(content)
            }
        
        except Exception as e:
            logger.error(f'Email scam detection error: {str(e)}')
            return {
                'is_scam': False,
                'confidence': 0.0,
                'error': str(e)
            }
    
    def _get_red_flags(self, content):
        """Identify specific red flags in content"""
        flags = []
        content_lower = content.lower()
        
        if any(keyword in content_lower for keyword in self.scam_keywords):
            flags.append('Suspicious keywords detected')
        
        if any(word in content_lower for word in self.urgency_words):
            flags.append('High urgency language detected')
        
        if any(phrase in content_lower for phrase in self.phishing_phrases):
            flags.append('Generic greeting detected')
        
        if any(req in content_lower for req in ['password', 'ssn', 'credit card']):
            flags.append('Requests for sensitive information')
        
        if 'http://' in content and 'https://' not in content:
            flags.append('Unencrypted links detected')
        
        return flags
