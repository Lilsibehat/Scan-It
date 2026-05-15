import pytest
from backend.detectors.phishing_detector import PhishingDetector

class TestPhishingDetector:
    @pytest.fixture
    def detector(self):
        return PhishingDetector()
    
    def test_detect_url(self, detector):
        """Test URL detection"""
        result = detector.detect('https://example.com')
        assert 'url' in result
        assert 'is_phishing' in result
        assert 'confidence' in result
    
    def test_suspicious_patterns(self, detector):
        """Test detection of suspicious patterns"""
        result = detector.detect('https://bit.ly/verify-account')
        assert result['risk_score'] > 0
    
    def test_domain_analysis(self, detector):
        """Test domain analysis"""
        result = detector.detect('https://192.168.1.1')
        assert result is not None
