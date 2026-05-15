import logging
import json
import re
from pathlib import Path

logger = logging.getLogger(__name__)

class RulesEngine:
    """Custom rules engine for threat detection"""
    
    def __init__(self, rules_file='rules.json'):
        self.rules = []
        self.load_rules(rules_file)
    
    def load_rules(self, rules_file):
        """Load rules from JSON file"""
        try:
            if Path(rules_file).exists():
                with open(rules_file, 'r') as f:
                    data = json.load(f)
                    self.rules = data.get('rules', [])
                logger.info(f'Loaded {len(self.rules)} custom rules')
            else:
                logger.warning(f'Rules file not found: {rules_file}')
        
        except Exception as e:
            logger.error(f'Error loading rules: {str(e)}')
    
    def apply_rules(self, content, content_type='email'):
        """Apply all rules to content"""
        matches = []
        
        for rule in self.rules:
            if self._check_rule(content, rule, content_type):
                matches.append({
                    'rule_name': rule.get('name'),
                    'severity': rule.get('severity', 'medium'),
                    'type': rule.get('type')
                })
        
        return {
            'matches': matches,
            'rule_count': len(matches),
            'threat_level': self._calculate_threat_level(matches)
        }
    
    def _check_rule(self, content, rule, content_type):
        """Check if content matches a rule"""
        rule_type = rule.get('type', 'keyword')
        
        if rule_type == 'keyword':
            patterns = rule.get('patterns', [])
            return any(pattern in content.lower() for pattern in patterns)
        
        elif rule_type == 'regex':
            pattern = rule.get('pattern')
            try:
                return bool(re.search(pattern, content, re.IGNORECASE))
            except:
                return False
        
        elif rule_type == 'domain':
            domains = rule.get('domains', [])
            return any(domain in content for domain in domains)
        
        return False
    
    def _calculate_threat_level(self, matches):
        """Calculate overall threat level from matches"""
        if not matches:
            return 'low'
        
        severity_scores = {'critical': 1.0, 'high': 0.8, 'medium': 0.5, 'low': 0.2}
        avg_score = sum(severity_scores.get(m['severity'], 0.5) for m in matches) / len(matches)
        
        if avg_score >= 0.8:
            return 'critical'
        elif avg_score >= 0.6:
            return 'high'
        elif avg_score >= 0.4:
            return 'medium'
        else:
            return 'low'
