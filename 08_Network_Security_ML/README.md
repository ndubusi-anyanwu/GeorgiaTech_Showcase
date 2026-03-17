# Network Security — Intrusion Detection Rules and ML-Based Threat Detection

**Subject Area:** Network Security · Intrusion Detection · Snort IDS · Machine Learning for Security

---

## What It Does

This project covers two complementary network security problem sets: engineering Snort IDS rules to detect real labeled attack traffic, and applying machine learning techniques to network threat classification and phishing detection.

### Components

**`Firewall_Rules/`** — Snort IDS rule engineering against real attack traffic:
- `rules_helper.py` — Snort rule set engineered to detect four labeled attack types (DoS, brute force, web attack, botnet C2) against a provided PCAP and labeled connection dataset
- `connections.txt` — Labeled network connection data (brute force, DoS, web attack, botnet categories) used to validate rule detection logic

**`ML_for_Security/`** — ML-based threat detection:
- `Go_Phish_Project_slides.pptx` — Presentation covering ML approach to phishing and network intrusion detection: threat modeling, feature engineering, model selection, results, and limitations

## Problem Addressed

Traditional network defenses rely on signature-based detection that must be kept current against evolving attack patterns. This project addresses two dimensions: writing precise, performant Snort IDS rules that correctly detect attack categories in labeled traffic without excessive false positives, and evaluating machine learning classifiers as a complementary detection layer for phishing and intrusion scenarios where signatures alone are insufficient.

## Practical Relevance

Snort rule writing and IDS tuning are core operational security skills — directly applicable to SOC engineering, network security architecture, and penetration testing. Understanding the mechanics of rule-based detection is foundational for anyone evaluating or deploying commercial IDS/IPS products. The ML for Security work connects to the growing market for AI-augmented threat detection in SIEM and EDR platforms.

## Tools, Languages, and Libraries

Python · Snort IDS · PCAP analysis · network connection classification · PowerPoint

## Skills Demonstrated

- Snort IDS rule engineering: crafting precise detection rules for DoS, brute force, web attack, and botnet traffic
- Network traffic pattern analysis: mapping labeled attack categories to specific packet-level signatures
- ML-based security: applying classifiers to phishing and intrusion detection datasets
- Security tool evaluation: understanding detection tradeoffs (false positive rate, performance impact)
- Technical communication: presenting ML-based security findings to mixed audiences

## Extension Ideas

- Convert the Snort rules to Suricata format and benchmark detection performance against the same PCAP
- Build a SHAP-based explainability wrapper for the ML classifier to make detection decisions auditable
- Extend the rule set to cover MITRE ATT&CK technique-level detections (T1046 Network Scanning, T1110 Brute Force)
- Apply adversarial ML evasion techniques to test classifier robustness against polymorphic attack traffic

---

*Georgia Institute of Technology — MS Cybersecurity · CS 6262: Network Security*
