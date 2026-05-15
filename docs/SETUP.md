# Scan-It Setup Guide

## Prerequisites

- Python 3.8 or higher
- Node.js 14 or higher
- pip and npm package managers
- API Keys:
  - VirusTotal API Key (get from https://virustotal.com)
  - URLhaus API Key (optional, but recommended)

## Installation Steps

### 1. Clone Repository

```bash
git clone https://github.com/Lilsibehat/Scan-It.git
cd Scan-It
```

### 2. Setup Backend

#### Create Virtual Environment
```bash
cd backend
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

#### Install Dependencies
```bash
pip install -r requirements.txt
```

#### Configure Environment Variables
```bash
cp ../.env.example ../.env
```

Edit `.env` and add your API keys:
```
VIRUSTOTAL_API_KEY=your_key_here
URLHAUS_API_KEY=your_key_here
```

### 3. Setup Frontend

```bash
cd ../frontend
npm install
```

### 4. Run Application

#### Terminal 1 - Backend
```bash
cd backend
source venv/bin/activate  # or venv\Scripts\activate on Windows
python app.py
```

Backend will run on `http://localhost:5000`

#### Terminal 2 - Frontend
```bash
cd frontend
npm start
```

Frontend will run on `http://localhost:3000`

### 5. Access Application

Open your browser and navigate to: `http://localhost:3000`

## Docker Setup (Optional)

### Prerequisites
- Docker
- Docker Compose

### Build and Run

```bash
# Create .env file with your API keys
cp .env.example .env

# Build and start containers
docker-compose up --build
```

Application will be available at:
- Frontend: `http://localhost:3000`
- Backend: `http://localhost:5000`
- Database: `localhost:5432`

## Troubleshooting

### Port Already in Use

If ports 3000 or 5000 are in use:

```bash
# Find process using port 3000
lsof -i :3000

# Kill process
kill -9 <PID>
```

### Missing Dependencies

Ensure all requirements are installed:

```bash
# Backend
pip install -r backend/requirements.txt

# Frontend
cd frontend
npm install
```

### API Key Errors

1. Verify API keys are correctly set in `.env`
2. Check VirusTotal account status
3. Test API connection with curl

### Database Issues

```bash
# Reset database
rm backend/scan_it.db

# Or with PostgreSQL
psql -U scan_it -d scan_it -c "DROP SCHEMA public CASCADE; CREATE SCHEMA public;"
```

## Next Steps

1. Read the [API Documentation](API.md)
2. Review [Custom Rules](RULES.md)
3. Check [Development Guide](DEVELOPMENT.md)
