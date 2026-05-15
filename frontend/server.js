const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
const path = require('path');
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 3000;
const BACKEND_URL = process.env.BACKEND_URL || 'http://localhost:5000';

// Middleware
app.use(cors());
app.use(bodyParser.json({ limit: '50mb' }));
app.use(bodyParser.urlencoded({ limit: '50mb', extended: true }));
app.use(express.static(path.join(__dirname, 'public')));

// Routes
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.get('/health', (req, res) => {
    res.json({
        status: 'healthy',
        version: '0.1',
        frontend: 'Scan-It'
    });
});

// Proxy requests to backend
const axios = require('axios');

app.post('/api/*', async (req, res) => {
    try {
        const apiPath = req.params[0];
        const response = await axios.post(
            `${BACKEND_URL}/api/${apiPath}`,
            req.body,
            { timeout: 30000 }
        );
        res.json(response.data);
    } catch (error) {
        console.error('Backend error:', error.message);
        res.status(error.response?.status || 500).json({
            error: 'Backend request failed',
            message: error.message
        });
    }
});

// Start server
app.listen(PORT, () => {
    console.log(`\n✅ Scan-It Frontend running on http://localhost:${PORT}`);
    console.log(`📡 Backend URL: ${BACKEND_URL}\n`);
});
