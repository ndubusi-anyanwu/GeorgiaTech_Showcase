# Network Security — ML-Based Threat Detection and Firewall Engineering

**Subject Area:** Network Security · Machine Learning for Security · Intrusion Detection · Firewall Policy

---

## What It Does

This project covers two complementary network security problems: applying machine learning to detect phishing and classify network threats (ML for Security), and implementing a firewall rule engine that models packet filtering decisions from connection logs (Firewall Rules). Together they demonstrate the intersection of data-driven security and traditional network defense engineering.

### Components

**`ML_for_Security/`** — Machine learning applied to network threat classification:
- `ML_for_Security_writeup.docx` — Technical analysis of ML models applied to phishing and network intrusion datasets; covers feature engineering, model selection, performance evaluation, and limitations
- `Go_Phish_Project_slides.pptx` — Presentation deck covering threat modeling, ML approach, and results

**`Firewall_Rules/`** — Programmatic firewall policy analysis:
- `rules_helper.py` — Python utility for parsing and evaluating firewall rule sets against connection logs
- `connections.txt` — Sample network connection data used to test rule evaluation logic

## Problem Addressed

Security operations teams face two persistent challenges: keeping signature-based defenses current against novel threats (where ML classifiers can supplement static rules), and maintaining firewall rule sets that are auditable, correctly ordered, and free of conflicts. This project addresses both: it benchmarks ML classifiers on real threat datasets and implements the logic needed to programmatically validate whether firewall rules match expected outcomes for a given connection profile.

## Practical Relevance

ML-augmented threat detection is increasingly deployed in commercial security products (EDR, SIEM, UEBA platforms). Understanding how these classifiers are built, evaluated, and fooled is essential for security engineers responsible for tuning or procuring such tools. Similarly, firewall rule analysis and automation is a core skill for network security engineers and cloud security architects working across multi-tier environments.

## Tools, Languages, and Libraries

Python · scikit-learn · pandas · network security datasets · firewall rule logic · PowerPoint

## Skills Demonstrated

- Applying supervised ML to security classification problems (phishing, intrusion detection)
- Feature engineering from raw network telemetry
- Firewall rule modeling: parsing, ordering, and conflict detection in access control lists
- Technical communication: presenting ML-based security findings to a mixed technical/executive audience
- Security tool evaluation: understanding model performance metrics in adversarial contexts (precision, recall, false positive rate)

## Extension Ideas

- Implement a SHAP-based explainability layer for the ML classifier to make detection decisions auditable
- Build a firewall rule optimizer that detects shadowed, redundant, or conflicting rules in large ACL sets
- Apply adversarial ML techniques (evasion attacks) against the phishing classifier to test robustness
- Extend the firewall rule engine to parse and validate cloud security group rules (AWS/GCP/Azure)

---

*Georgia Institute of Technology — MS Cybersecurity · CS 6262: Network Security*
