# Scan-It 0.1

A comprehensive cybersecurity threat detection tool that identifies scams, phishing attacks, malware, and fake AI-generated content across emails and applications.

## Features

✅ **Phishing Detection** - Detect suspicious URLs and phishing emails using URLhaus API
✅ **Malware Scanning** - Identify malicious files using VirusTotal API
✅ **AI-Generated Content Detection** - Detect fake AI-generated content using ML models
✅ **Scam Detection** - Identify common scam patterns and suspicious emails
✅ **Custom Rules Engine** - Define custom detection rules for specific threats
✅ **Web Interface** - User-friendly dashboard for threat analysis
✅ **CLI Tool** - Command-line interface for automated scanning
✅ **REST API** - Integrate threat detection into other applications

## Tech Stack

- **Backend**: Python (Flask/FastAPI)
- **Frontend**: Node.js/Express + HTML/CSS/JavaScript
- **ML Models**: TensorFlow, scikit-learn
- **APIs**: VirusTotal, URLhaus
- **Database**: SQLite/PostgreSQL
- **Task Queue**: Celery (for async scanning)

## Project Structure

```
Scan-It/
├── backend/                 # Python backend
│   ├── app.py              # Main Flask/FastAPI application
│   ├── requirements.txt    # Python dependencies
│   ├── config.py           # Configuration settings
│   ├── detectors/
│   │   ├── malware_detector.py       # VirusTotal integration
│   │   ├── phishing_detector.py      # URLhaus + URL analysis
│   │   ├── ai_content_detector.py    # ML-based AI detection
│   │   ├── scam_detector.py          # Scam pattern detection
│   │   └── rules_engine.py           # Custom rules engine
│   ├── models/
│   │   ├── ai_model.pkl              # Pre-trained ML model
│   │   └── training_scripts/         # Model training scripts
│   ├── api/
│   │   ├── routes.py                 # API endpoints
│   │   └── middleware.py             # API middleware
│   ├── utils/
│   │   ├── validators.py             # Input validation
│   │   ├── helpers.py                # Helper functions
│   │   └── logger.py                 # Logging setup
│   ├── database/
│   │   ├── models.py                 # Database models
│   │   └── init_db.py                # Database initialization
│   └── cli.py                         # CLI interface
├── frontend/                # Node.js/Express frontend
│   ├── server.js           # Express server
│   ├── package.json        # Node dependencies
│   ├── public/
│   │   ├── index.html      # Main dashboard
│   │   ├── css/
│   │   │   └── style.css
│   │   └── js/
│   │       └── app.js
│   └── routes/
│       └── index.js        # Express routes
├── tests/                   # Unit & integration tests
├── docs/                    # Documentation
├── .env.example            # Environment variables template
├── docker-compose.yml      # Docker setup
├── Dockerfile              # Docker configuration
└── .gitignore
```

## Quick Start

### Prerequisites
- Python 3.8+
- Node.js 14+
- API Keys: VirusTotal, URLhaus

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Lilsibehat/Scan-It.git
   cd Scan-It
   ```

2. **Setup Backend**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Setup Frontend**
   ```bash
   cd ../frontend
   npm install
   ```

4. **Configure Environment**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

5. **Run the Application**
   ```bash
   # Terminal 1: Backend
   cd backend
   python app.py

   # Terminal 2: Frontend
   cd frontend
   npm start
   ```

## API Endpoints

### Scan Endpoints
- `POST /api/scan/url` - Scan a URL for threats
- `POST /api/scan/email` - Analyze an email
- `POST /api/scan/file` - Scan a file for malware
- `POST /api/scan/content` - Check if content is AI-generated

### Results Endpoints
- `GET /api/results/<scan_id>` - Get scan results
- `GET /api/history` - Get scanning history

## CLI Usage

```bash
python cli.py scan-url https://example.com
python cli.py scan-email email.txt
python cli.py scan-file malware.exe
python cli.py scan-content "This is AI generated text"
```

## Configuration

Edit `backend/config.py` to configure:
- API keys (VirusTotal, URLhaus)
- Detection sensitivity levels
- Custom rules
- Database settings

## Custom Rules Engine

Define custom detection rules in `rules.json`:

```json
{
  "rules": [
    {
      "name": "Suspicious Keywords",
      "type": "keyword",
      "patterns": ["urgent", "verify", "confirm"],
      "severity": "high"
    }
  ]
}
```

## Testing

```bash
pytest tests/
```

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT License - See LICENSE file for details

## Support

For issues, questions, or suggestions, please create an issue on GitHub.

## Roadmap

- [ ] Machine learning model improvements
- [ ] Additional threat intelligence APIs
- [ ] Mobile app version
- [ ] Real-time threat monitoring
- [ ] Advanced analytics dashboard
- [ ] Community threat database

---

**Version**: 0.1  
**Status**: Active Development  
**Last Updated**: May 2026
