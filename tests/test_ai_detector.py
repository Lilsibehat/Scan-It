import pytest
from backend.detectors.ai_content_detector import AIContentDetector

class TestAIContentDetector:
    @pytest.fixture
    def detector(self):
        return AIContentDetector()
    
    def test_detect_ai_content(self, detector):
        """Test AI content detection"""
        content = "As an AI language model, I can assist you with..."
        result = detector.detect(content)
        assert 'is_ai_generated' in result
        assert 'confidence' in result
    
    def test_pattern_detection(self, detector):
        """Test pattern-based detection"""
        result = detector.detect("I am an AI model")
        assert result['confidence'] > 0
    
    def test_human_content(self, detector):
        """Test human-written content"""
        content = "I went to the store today and bought some groceries."
        result = detector.detect(content)
        assert result['is_ai_generated'] == False or result['confidence'] < 0.5
