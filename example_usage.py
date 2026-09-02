from client import PromptInjectionJailbreakFirewallSentinelClient

def main():
    client = PromptInjectionJailbreakFirewallSentinelClient()
    res = client.inspect_untrusted_input('Please summarize this harmless text')
    print('Prompt Injection Firewall Sentinel: ' + res['sentinel_verdict_id'] + ' (Threat: ' + str(res['threat_detected']) + ')')
    print('Category: ' + res['threat_category'] + ' | Confidence: ' + str(res['risk_confidence_score']))
    print('Sanitized: ' + res['sanitized_safe_payload_string'])
    print('Incident Report: ' + res['security_incident_report_url'])

if __name__ == '__main__':
    main()
