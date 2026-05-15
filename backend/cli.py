#!/usr/bin/env python
"""Command-line interface for Scan-It"""

import click
import json
from detectors.phishing_detector import PhishingDetector
from detectors.malware_detector import MalwareDetector
from detectors.ai_content_detector import AIContentDetector
from detectors.scam_detector import ScamDetector

phishing_detector = PhishingDetector()
malware_detector = MalwareDetector()
ai_content_detector = AIContentDetector()
scam_detector = ScamDetector()

@click.group()
def cli():
    """Scan-It: Multi-threat Detection Tool"""
    pass

@cli.command()
@click.argument('url')
def scan_url(url):
    """Scan a URL for threats"""
    click.echo(f'🔍 Scanning URL: {url}\n')
    result = phishing_detector.detect(url)
    click.echo(json.dumps(result, indent=2))

@cli.command()
@click.argument('email_file', type=click.File('r'))
def scan_email(email_file):
    """Scan an email for threats"""
    content = email_file.read()
    click.echo(f'🔍 Scanning email...\n')
    result = scam_detector.detect_email(content)
    click.echo(json.dumps(result, indent=2))

@cli.command()
@click.argument('file_path', type=click.File('rb'))
def scan_file(file_path):
    """Scan a file for malware"""
    click.echo(f'🔍 Scanning file: {file_path.name}\n')
    result = malware_detector.scan_file(file_path)
    click.echo(json.dumps(result, indent=2))

@cli.command()
@click.argument('content')
def scan_content(content):
    """Check if content is AI-generated"""
    click.echo(f'🔍 Analyzing content...\n')
    result = ai_content_detector.detect(content)
    click.echo(json.dumps(result, indent=2))

@cli.command()
@click.argument('url')
def analyze_url(url):
    """Comprehensive URL analysis"""
    click.echo(f'🔍 Comprehensive analysis of: {url}\n')
    
    phishing_result = phishing_detector.detect(url)
    malware_result = malware_detector.scan_url(url)
    scam_result = scam_detector.detect_url(url)
    
    results = {
        'url': url,
        'analysis': {
            'phishing': phishing_result,
            'malware': malware_result,
            'scam': scam_result
        }
    }
    
    click.echo(json.dumps(results, indent=2))

if __name__ == '__main__':
    cli()
