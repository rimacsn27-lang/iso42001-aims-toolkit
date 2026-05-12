# ISO 42001 AIMS Toolkit for UK AI Companies
[![EU AI Act](https://img.shields.io/badge/EU%20AI%20Act-Ready%20for%202%20Aug%202026-red)](https://artificial-intelligence-act.com/)
[![ISO 42001](https://img.shields.io/badge/ISO%2042001-AIMS%20Toolkit-blue)](https://www.iso.org/standard/81230.html)
[![Python](https://img.shields.io/badge/Python-3.8%2B-green)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)
[![UK](https://img.shields.io/badge/Made%20for-UK%20AI%20Companies-purple)](https://www.gov.uk/government/publications/ai-regulation-a-pro-innovation-approach)

&gt; The first open-source AI Management System (AIMS) implementation framework built specifically for UK AI companies navigating the **EU AI Act August 2, 2026 high-risk obligations deadline**.

## Why This Exists

UK AI companies with EU customers face fines of up to **€35 million or 7% of global turnover** under the EU AI Act. ISO 42001 is the operational standard that maps directly to those obligations — but until now, there was no open-source implementation toolkit.

This repository contains:
- **Risk Classification Engine**: CLI tool to determine your EU AI Act risk tier and required ISO 42001 controls
- **Gap Assessment Suite**: Automated maturity scoring across 10 AIMS dimensions
- **Audit Trail Generator**: Tamper-evident logging for AI system decisions
- **Implementation Templates**: FRIA, Risk Management System, Technical Documentation, AI Policy
- **EU AI Act → ISO 42001 Mapping**: Complete control correlation for engineering teams

## Who This Is For

- **Series A/B UK AI companies** deploying high-risk AI systems (recruitment, fintech, healthtech)
- **Engineering teams** who need to build compliance into their MLOps pipeline, not bolt it on afterward
- **Compliance officers** who need technical documentation that auditors and regulators will accept
- **Startups with EU customers** who need to demonstrate conformity by August 2, 2026

## Quick Start

### 1. Classify Your AI System (60 seconds)
```bash
python tools/risk-classifier.py
