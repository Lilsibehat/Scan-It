# Scan-It API Documentation

## Base URL
`http://localhost:5000/api`

## Authentication
Currently, no authentication is required. API keys will be implemented in future versions.

## Endpoints

### 1. Scan URL

**Endpoint:** `POST /scan/url`

**Request Body:**
```json
{
  "url": "https://example.com"
}
```

**Response:**
```json
{
  "url": "https://example.com",
  "is_phishing": false,
  "confidence": 0.15,
  "risk_score": 0.15,
  "details": {
    "urlhaus_detection": {...},
    "pattern_score": 0,
    "domain_analysis": 0.15
  }
}
```

### 2. Scan Email

**Endpoint:** `POST /scan/email`

**Request Body:**
```json
{
  "content": "email content here",
  "headers": {}
}
```

**Response:**
```json
{
  "email_analysis": {
    "phishing": {...},
    "scam": {...},
    "urls_found": 2,
    "suspicious_urls": [...]
  }
}
```

### 3. Scan File

**Endpoint:** `POST /scan/file`

**Request:** Multipart form data with file

**Response:**
```json
{
  "filename": "document.exe",
  "is_malicious": true,
  "malicious_vendors": 5,
  "total_vendors": 60,
  "confidence": 0.083
}
```

### 4. Analyze Content

**Endpoint:** `POST /scan/content`

**Request Body:**
```json
{
  "content": "text content to analyze"
}
```

**Response:**
```json
{
  "is_ai_generated": true,
  "confidence": 0.85,
  "score": 85,
  "risk_level": "high",
  "analysis": {
    "pattern_indicators": 0.2,
    "entropy_score": 0.3,
    "style_analysis": 0.35
  }
}
```

### 5. Get Results

**Endpoint:** `GET /results/<scan_id>`

**Response:**
```json
{
  "scan_id": "scan_12345",
  "timestamp": "2026-05-15T10:30:00Z",
  "results": {...}
}
```

### 6. Get History

**Endpoint:** `GET /history`

**Query Parameters:**
- `limit` (optional, default: 50)
- `offset` (optional, default: 0)

**Response:**
```json
{
  "total": 100,
  "scans": [
    {
      "scan_id": "scan_12345",
      "type": "url",
      "timestamp": "2026-05-15T10:30:00Z",
      "result": "safe"
    }
  ]
}
```

## Error Responses

All errors return a JSON response with an error message:

```json
{
  "error": "Error type",
  "message": "Detailed error message"
}
```

### Common Error Codes
- `400` - Bad Request
- `404` - Not Found
- `500` - Internal Server Error

## Rate Limiting

- Rate limit: 100 requests per hour
- Rate limit window: 3600 seconds

## Examples

### Scan a URL using cURL
```bash
curl -X POST http://localhost:5000/api/scan/url \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com"}'
```

### Scan a File
```bash
curl -X POST http://localhost:5000/api/scan/file \
  -F "file=@malware.exe"
```

### Analyze Content
```bash
curl -X POST http://localhost:5000/api/scan/content \
  -H "Content-Type: application/json" \
  -d '{"content": "This is AI generated content"}'
```
