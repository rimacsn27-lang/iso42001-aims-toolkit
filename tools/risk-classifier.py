#!/usr/bin/env python3
"""
EU AI Act Risk Classifier + ISO 42001 Control Mapper
For UK AI companies preparing for August 2, 2026 deadline.
Usage: python risk-classifier.py
"""

import json
import sys
from datetime import datetime

# EU AI Act Annex III High-Risk Categories
HIGH_RISK_CATEGORIES = {
    "biometric": {
        "name": "Biometric identification and categorization",
        "article": "Annex III.1",
        "iso_controls": ["A.6", "A.8", "A.9", "A.10"],
        "description": "Remote biometric identification, biometric categorization, emotion recognition"
    },
    "critical_infrastructure": {
        "name": "Management of critical infrastructure",
        "article": "Annex III.2",
        "iso_controls": ["A.4", "A.7", "A.10", "A.12"],
        "description": "Road traffic, water/gas/electricity supply, safety components"
    },
    "education": {
        "name": "Education and vocational training",
        "article": "Annex III.3",
        "iso_controls": ["A.6", "A.8", "A.9", "A.10"],
        "description": "Admissions, evaluations, proctoring, learning outcomes assessment"
    },
    "employment": {
        "name": "Employment and workers management",
        "article": "Annex III.4",
        "iso_controls": ["A.6", "A.8", "A.9", "A.10", "A.11"],
        "description": "Recruitment, selection, promotion, termination, task allocation, performance evaluation"
    },
    "essential_services": {
        "name": "Access to essential services",
        "article": "Annex III.5",
        "iso_controls": ["A.6", "A.9", "A.10"],
        "description": "Credit scoring, insurance pricing, benefits, emergency services dispatch"
    },
    "law_enforcement": {
        "name": "Law enforcement",
        "article": "Annex III.6",
        "iso_controls": ["A.6", "A.7", "A.8", "A.9", "A.10"],
        "description": "Risk assessment, polygraphs, evidence evaluation, crime analytics"
    },
    "migration": {
        "name": "Migration, asylum and border control",
        "article": "Annex III.7",
        "iso_controls": ["A.6", "A.8", "A.9", "A.10"],
        "description": "Visa/asylum decisions, border control risk assessment, document verification"
    },
    "justice": {
        "name": "Administration of justice and democratic processes",
        "article": "Annex III.8",
        "iso_controls": ["A.6", "A.7", "A.9", "A.10"],
        "description": "Case prioritization, evidence analysis, election/voting influence"
    }
}

ISO_42001_CONTROL_DETAILS = {
    "A.2": "Policy for AI — Establish AI policy aligned with organizational objectives and EU AI Act obligations.",
    "A.3": "Internal organization — Roles, responsibilities, and authorities for AI system lifecycle governance.",
    "A.4": "Resources for AI systems — Competence, awareness, and communication for AI development/operation.",
    "A.5": "Assessing and treating AI risks — Systematic risk identification, analysis, and treatment.",
    "A.6": "AI system impact assessment — Evaluate impacts on individuals, groups, and society (FRIA alignment).",
    "A.7": "AI system lifecycle — Planning, development, testing, deployment, and decommissioning controls.",
    "A.8": "Data for AI systems — Data governance, quality, bias mitigation, and training data documentation.",
    "A.9": "Information for interested parties — Transparency, explainability, and communication to users/deployers.",
    "A.10": "Use of AI systems — Operational monitoring, human oversight, and incident response.",
    "A.11": "Third-party and customer relationships — Supplier management and customer agreement compliance.",
    "A.12": "Acquisition, development and maintenance — Secure development, change control, and technical documentation."
}

def ask_yes_no(question):
    while True:
        answer = input(f"\n[?] {question} (yes/no): ").strip().lower()
        if answer in ('yes', 'y'):
            return True
        elif answer in ('no', 'n'):
            return False
        print("Please answer 'yes' or 'no'.")

def classify_system():
    print("=" * 60)
    print("EU AI ACT RISK CLASSIFIER + ISO 42001 CONTROL MAPPER")
    print("For UK AI Companies | August 2, 2026 Deadline Ready")
    print("=" * 60)
    
    print("\n[!] Answer the following about your AI system...")
    
    prohibited = []
    if ask_yes_no("Does your system perform social scoring of individuals or groups by government or public authorities?"):
        prohibited.append("social_scoring")
    if ask_yes_no("Does your system use real-time remote biometric identification in publicly accessible spaces?"):
        prohibited.append("realtime_biometric_public")
    if ask_yes_no("Does your system infer emotions in workplace or educational settings (except for medical/safety reasons)?"):
        prohibited.append("emotion_recognition_workplace_school")
    if ask_yes_no("Does your system use subliminal techniques or manipulative design to distort behavior?"):
        prohibited.append("manipulative_subliminal")
    if ask_yes_no("Does your system exploit vulnerabilities of specific groups (age, disability, social/economic situation)?"):
        prohibited.append("exploitation_vulnerability")
    
    if prohibited:
        print("\n" + "!" * 60)
        print("CRITICAL: PROHIBITED PRACTICE DETECTED")
        print("!" * 60)
        print("Your AI system falls under Article 5 (Prohibited AI Practices).")
        print("This system cannot be deployed in the EU.")
        print(f"Prohibited indicators triggered: {', '.join(prohibited)}")
        print("\nISO 42001 Recommendation: Immediate legal review required.")
        return {"risk_class": "PROHIBITED", "prohibited": prohibited, "iso_controls": []}
    
    triggered_categories = []
    
    if ask_yes_no("Is your system used for biometric identification, categorization, or emotion recognition?"):
        triggered_categories.append("biometric")
    if ask_yes_no("Is your system used to manage critical infrastructure or safety components?"):
        triggered_categories.append("critical_infrastructure")
    if ask_yes_no("Is your system used for educational admissions, evaluation, or vocational training assessment?"):
        triggered_categories.append("education")
    if ask_yes_no("Is your system used for recruitment, selection, promotion, termination, task allocation, or performance evaluation?"):
        triggered_categories.append("employment")
    if ask_yes_no("Is your system used for credit scoring, insurance pricing, benefits eligibility, or emergency services dispatch?"):
        triggered_categories.append("essential_services")
    if ask_yes_no("Is your system used by law enforcement for risk assessment or evidence evaluation?"):
        triggered_categories.append("law_enforcement")
    if ask_yes_no("Is your system used for visa/asylum decisions, border control, or document verification?"):
        triggered_categories.append("migration")
    if ask_yes_no("Is your system used to assist judicial decisions, case prioritization, or influence voting/election processes?"):
        triggered_categories.append("justice")
    
    annex_ii = ask_yes_no("Is your AI system a safety component of a product already regulated under EU harmonization legislation (toys, aviation, vehicles, medical devices, lifts, etc.)?")
    
    if triggered_categories or annex_ii:
        risk_class = "HIGH-RISK"
        articles = []
        iso_controls = set()
        
        for cat in triggered_categories:
            info = HIGH_RISK_CATEGORIES[cat]
            articles.append(f"{info['article']} ({info['name']})")
            iso_controls.update(info['iso_controls'])
        
        if annex_ii:
            articles.append("Annex II (Safety component in regulated product)")
            iso_controls.update(["A.7", "A.10", "A.12"])
            
        iso_controls = sorted(list(iso_controls))
        
        result = {
            "risk_class": risk_class,
            "eu_ai_act_articles": articles,
            "iso_42001_controls": iso_controls,
            "iso_control_details": {k: ISO_42001_CONTROL_DETAILS[k] for k in iso_controls if k in ISO_42001_CONTROL_DETAILS},
            "deadline": "2026-08-02",
            "days_remaining": (datetime(2026, 8, 2) - datetime.now()).days,
            "required_actions": [
                "Complete Fundamental Rights Impact Assessment (FRIA)",
                "Implement full ISO 42001 AIMS (Clauses 4-10)",
                "Create technical documentation package (Article 11)",
                "Establish risk management system (Article 9)",
                "Implement data governance and training data controls (Article 10)",
                "Deploy human oversight measures (Article 14)",
                "Ensure transparency and information provision (Article 13)",
                "Validate accuracy, robustness, cybersecurity (Article 15)",
                "Register in EU database (Article 71)",
                "Affix CE marking and EU declaration of conformity"
            ]
        }
    else:
        limited_risk = ask_yes_no("Is your system a chatbot, deepfake/synthetic media generator, or AI system that interacts directly with humans?")
        if limited_risk:
            risk_class = "LIMITED RISK"
            result = {
                "risk_class": risk_class,
                "eu_ai_act_articles": ["Article 52 (Transparency obligations)"],
                "iso_42001_controls": ["A.3", "A.9", "A.10"],
                "iso_control_details": {
                    "A.3": "Internal organization for transparency governance",
                    "A.9": "Information provision to users (disclosure requirements)",
                    "A.10": "Operational controls for transparent AI use"
                },
                "required_actions": [
                    "Ensure users are informed they are interacting with AI",
                    "For deepfakes: disclose synthetic origin",
                    "Document transparency measures in AIMS"
                ]
            }
        else:
            risk_class = "MINIMAL RISK"
            result = {
                "risk_class": risk_class,
                "eu_ai_act_articles": ["No specific obligations under EU AI Act"],
                "iso_42001_controls": ["A.2", "A.3", "A.5"],
                "iso_control_details": {
                    "A.2": "Voluntary AI policy and governance",
                    "A.3": "Basic internal organization",
                    "A.5": "Fundamental risk assessment"
                },
                "required_actions": [
                    "No mandatory EU AI Act compliance required",
                    "Recommended: Establish basic AIMS for future readiness",
                    "Monitor for changes in risk classification if use case evolves"
                ]
            }
    
    return result

def print_report(result):
    print("\n" + "=" * 60)
    print("RISK CLASSIFICATION REPORT")
    print("=" * 60)
    print(f"Risk Classification: {result['risk_class']}")
    print(f"Assessment Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    
    if result['risk_class'] == "PROHIBITED":
        print("\n[LEGAL STATUS] This system is PROHIBITED under EU AI Act Article 5.")
        print("Deployment in the EU is illegal. Seek immediate legal counsel.")
        return
    
    print(f"\n[EU AI ACT ARTICLES APPLICABLE]")
    for article in result.get('eu_ai_act_articles', []):
        print(f"  • {article}")
    
    print(f"\n[ISO 42001 CONTROLS REQUIRED]")
    for control, detail in result.get('iso_control_details', {}).items():
        print(f"  • {control}: {detail}")
    
    print(f"\n[REQUIRED ACTIONS]")
    for i, action in enumerate(result.get('required_actions', []), 1):
        print(f"  {i}. {action}")
    
    if 'days_remaining' in result:
        print(f"\n[DEADLINE] EU AI Act high-risk obligations: {result['deadline']}")
        print(f"[DAYS REMAINING] {result['days_remaining']} days")
        if result['days_remaining'] < 90:
            print("[URGENT] Less than 90 days remaining. Immediate action required.")
    
    filename = f"risk-classification-report-{datetime.now().strftime('%Y%m%d-%H%M%S')}.json"
    with open(filename, 'w') as f:
        json.dump(result, f, indent=2)
    print(f"\n[OUTPUT] Detailed report saved to: {filename}")

def main():
    try:
        result = classify_system()
        print_report(result)
    except KeyboardInterrupt:
        print("\n\nAssessment cancelled.")
        sys.exit(0)

if __name__ == "__main__":
    main()
