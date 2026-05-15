// Scan-It Frontend Application
const BACKEND_URL = 'http://localhost:5000';

// Tab Navigation
document.querySelectorAll('.nav-btn').forEach(btn => {
    btn.addEventListener('click', () => {
        const tabName = btn.dataset.tab;
        switchTab(tabName);
    });
});

function switchTab(tabName) {
    // Hide all tabs
    document.querySelectorAll('.tab-content').forEach(tab => {
        tab.classList.remove('active');
    });
    
    // Remove active state from all buttons
    document.querySelectorAll('.nav-btn').forEach(btn => {
        btn.classList.remove('active');
    });
    
    // Show selected tab
    document.getElementById(tabName).classList.add('active');
    document.querySelector(`[data-tab="${tabName}"]`).classList.add('active');
}

// URL Scan Form
document.getElementById('url-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const url = document.getElementById('url-input').value;
    await scanUrl(url);
});

async function scanUrl(url) {
    const resultsDiv = document.getElementById('url-results');
    resultsDiv.innerHTML = '<div class="loading"><div class="spinner"></div> Scanning URL...</div>';
    
    try {
        const response = await fetch('/api/scan/url', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ url })
        });
        
        const data = await response.json();
        displayUrlResults(data);
    } catch (error) {
        resultsDiv.innerHTML = `<div class="error">Error: ${error.message}</div>`;
    }
}

function displayUrlResults(data) {
    const resultsDiv = document.getElementById('url-results');
    
    let html = '<div class="result-item threat">';
    html += `<div class="result-label">🔍 URL: ${data.url}</div>`;
    html += `<div class="result-value">Risk Score: ${data.threats?.phishing?.confidence || 0}</div>`;
    html += '</div>';
    
    resultsDiv.innerHTML = html;
}

// Email Scan Form
document.getElementById('email-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const content = document.getElementById('email-input').value;
    await scanEmail(content);
});

async function scanEmail(content) {
    const resultsDiv = document.getElementById('email-results');
    resultsDiv.innerHTML = '<div class="loading"><div class="spinner"></div> Analyzing email...</div>';
    
    try {
        const response = await fetch('/api/scan/email', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ content })
        });
        
        const data = await response.json();
        displayEmailResults(data);
    } catch (error) {
        resultsDiv.innerHTML = `<div class="error">Error: ${error.message}</div>`;
    }
}

function displayEmailResults(data) {
    const resultsDiv = document.getElementById('email-results');
    
    let html = '<div class="result-item threat">';
    html += `<div class="result-label">📧 Email Analysis</div>`;
    html += `<div class="result-value">Phishing Risk: ${data.email_analysis?.phishing || 'N/A'}</div>`;
    html += '</div>';
    
    resultsDiv.innerHTML = html;
}

// File Scan Form
document.getElementById('file-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const fileInput = document.getElementById('file-input');
    const file = fileInput.files[0];
    
    if (file) {
        await scanFile(file);
    }
});

async function scanFile(file) {
    const resultsDiv = document.getElementById('file-results');
    resultsDiv.innerHTML = '<div class="loading"><div class="spinner"></div> Scanning file...</div>';
    
    const formData = new FormData();
    formData.append('file', file);
    
    try {
        const response = await fetch('/api/scan/file', {
            method: 'POST',
            body: formData
        });
        
        const data = await response.json();
        displayFileResults(data);
    } catch (error) {
        resultsDiv.innerHTML = `<div class="error">Error: ${error.message}</div>`;
    }
}

function displayFileResults(data) {
    const resultsDiv = document.getElementById('file-results');
    
    let html = '<div class="result-item threat">';
    html += `<div class="result-label">📁 File: ${data.filename}</div>`;
    html += `<div class="result-value">Malware Detected: ${data.is_malicious ? 'YES' : 'NO'}</div>`;
    html += '</div>';
    
    resultsDiv.innerHTML = html;
}

// Content Analysis Form
document.getElementById('content-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const content = document.getElementById('content-input').value;
    await analyzeContent(content);
});

async function analyzeContent(content) {
    const resultsDiv = document.getElementById('content-results');
    resultsDiv.innerHTML = '<div class="loading"><div class="spinner"></div> Analyzing content...</div>';
    
    try {
        const response = await fetch('/api/scan/content', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ content })
        });
        
        const data = await response.json();
        displayContentResults(data);
    } catch (error) {
        resultsDiv.innerHTML = `<div class="error">Error: ${error.message}</div>`;
    }
}

function displayContentResults(data) {
    const resultsDiv = document.getElementById('content-results');
    
    const riskClass = data.is_ai_generated ? 'threat' : 'safe';
    let html = `<div class="result-item ${riskClass}">`;
    html += `<div class="result-label">🤖 AI Content Detection</div>`;
    html += `<div class="result-value">AI Generated: ${data.is_ai_generated ? 'YES' : 'NO'}</div>`;
    html += `<div class="result-value">Confidence: ${(data.confidence * 100).toFixed(1)}%</div>`;
    html += `<div class="confidence-bar"><div class="confidence-fill" style="width: ${data.confidence * 100}%"></div></div>`;
    html += `<span class="risk-badge ${data.risk_level}">${data.risk_level.toUpperCase()}</span>`;
    html += '</div>';
    
    resultsDiv.innerHTML = html;
}

console.log('Scan-It v0.1 initialized');
