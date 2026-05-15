# Development Guide

## Project Structure

```
Scan-It/
├── backend/          # Python Flask backend
├── frontend/         # Node.js Express frontend
├── tests/            # Unit and integration tests
├── docs/             # Documentation
└── docker-compose.yml
```

## Code Style

### Python (Backend)
- Follow PEP 8 guidelines
- Use black for code formatting
- Use flake8 for linting

```bash
black backend/
flake8 backend/
```

### JavaScript (Frontend)
- Use ES6+ syntax
- Follow Airbnb style guide
- Use ESLint for linting

## Testing

### Backend Tests

```bash
cd backend
pytest
pytest --cov  # With coverage
```

### Frontend Tests

```bash
cd frontend
npm test
```

## Adding New Detectors

### Step 1: Create Detector Class

```python
# backend/detectors/new_detector.py
class NewDetector:
    def __init__(self):
        pass
    
    def detect(self, content):
        # Implementation
        return result
```

### Step 2: Register in API Routes

```python
# backend/api/routes.py
from detectors.new_detector import NewDetector

detector = NewDetector()

@api_bp.route('/scan/new', methods=['POST'])
def scan_new():
    # Implementation
    pass
```

### Step 3: Add Frontend Tab

```html
<!-- frontend/public/index.html -->
<section id="new-scan" class="tab-content">
    <!-- Form and results -->
</section>
```

## Database Models

Use SQLAlchemy ORM for database operations:

```python
from database.models import ScanResult

# Create
scan = ScanResult(url='https://example.com', risk_level='high')
db.session.add(scan)
db.session.commit()

# Query
results = ScanResult.query.filter_by(url='https://example.com').all()
```

## API Rate Limiting

Configure in `config.py`:

```python
RATE_LIMIT = 100  # requests
RATE_LIMIT_WINDOW = 3600  # seconds
```

## Logging

Logging is configured in `utils/logger.py`. Logs are written to `logs/scan_it.log`.

```python
import logging

logger = logging.getLogger(__name__)
logger.info('Message')
logger.error('Error message')
```

## Git Workflow

1. Create feature branch
   ```bash
   git checkout -b feature/new-detector
   ```

2. Make changes and commit
   ```bash
   git add .
   git commit -m "Add new detector"
   ```

3. Push to GitHub
   ```bash
   git push origin feature/new-detector
   ```

4. Create Pull Request

## Performance Optimization

- Use caching for API responses
- Implement async processing with Celery
- Optimize database queries
- Use connection pooling

## Security Best Practices

- Always validate user input
- Use environment variables for secrets
- Implement rate limiting
- Use HTTPS in production
- Keep dependencies updated

## Deployment

See deployment guides:
- [Heroku](HEROKU_DEPLOYMENT.md)
- [AWS](AWS_DEPLOYMENT.md)
- [Docker](DOCKER_DEPLOYMENT.md)
