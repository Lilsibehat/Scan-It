import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Base configuration"""
    # Flask
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key')
    DEBUG = False
    TESTING = False
    
    # Database
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///scan_it.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # API Keys
    VIRUSTOTAL_API_KEY = os.getenv('VIRUSTOTAL_API_KEY')
    URLHAUS_API_KEY = os.getenv('URLHAUS_API_KEY')
    
    # ML Model Settings
    AI_DETECTION_THRESHOLD = float(os.getenv('AI_DETECTION_THRESHOLD', 0.7))
    CONFIDENCE_THRESHOLD = float(os.getenv('CONFIDENCE_THRESHOLD', 0.8))
    
    # Rate Limiting
    RATE_LIMIT = int(os.getenv('RATE_LIMIT', 100))
    RATE_LIMIT_WINDOW = int(os.getenv('RATE_LIMIT_WINDOW', 3600))
    
    # Logging
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    LOG_FILE = os.getenv('LOG_FILE', 'logs/scan_it.log')
    
    # Detection Sensitivity (0-100)
    DETECTION_SENSITIVITY = int(os.getenv('DETECTION_SENSITIVITY', 75))
    
    # Timeouts (seconds)
    API_TIMEOUT = 30
    SCAN_TIMEOUT = 300

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    TESTING = False

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    TESTING = False

class TestingConfig(Config):
    """Testing configuration"""
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
