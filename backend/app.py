from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
import logging
from config import config
from utils.logger import setup_logger
from api.routes import api_bp

load_dotenv()

def create_app(config_name=None):
    """Application factory"""
    if config_name is None:
        config_name = os.getenv('FLASK_ENV', 'development')
    
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Setup CORS
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    
    # Setup logging
    setup_logger(app.config['LOG_LEVEL'], app.config['LOG_FILE'])
    logger = logging.getLogger(__name__)
    
    # Register blueprints
    app.register_blueprint(api_bp, url_prefix='/api')
    
    # Error handlers
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({'error': 'Bad request', 'message': str(error)}), 400
    
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({'error': 'Not found', 'message': 'Resource not found'}), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        logger.error(f'Internal error: {str(error)}')
        return jsonify({'error': 'Internal server error'}), 500
    
    # Health check endpoint
    @app.route('/health', methods=['GET'])
    def health_check():
        return jsonify({
            'status': 'healthy',
            'version': '0.1',
            'app': 'Scan-It'
        }), 200
    
    logger.info(f'Application started in {config_name} mode')
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)
