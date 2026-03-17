# AI Ethics and Algorithmic Fairness Analysis

**Subject Area:** AI Ethics · Algorithmic Fairness · Data Analysis · Policy Research · Bias Auditing

---

## What It Does

This project investigates algorithmic fairness and bias in AI/ML systems through two complementary lenses: empirical analysis of real-world advertising targeting data, and a policy-oriented examination of how protected classes under U.S. law interact with machine learning classification systems. The Python scripts perform statistical analysis and produce Sankey diagram visualizations of audience targeting flows, while the accompanying report synthesizes findings into policy-relevant recommendations.

### Contents

| File | Description |
|------|-------------|
| `facebook_advertiser_analysis.py` | Parses and statistically analyzes Facebook advertiser audience targeting data to surface demographic targeting patterns |
| `stats_and_sankey_visualization.py` | Produces Sankey flow diagrams and summary statistics visualizing how demographic segments are targeted across ad campaigns |
| `AI_ML_Protected_Classes_Report.docx` | Analysis of how ML systems trained on protected class correlates can produce discriminatory outcomes in lending, hiring, and criminal justice — with policy recommendations |

## Problem Addressed

Machine learning systems that optimize for engagement or outcome prediction can inadvertently encode and amplify demographic bias — even when explicitly protected attributes are excluded from model inputs. Correlated proxy features (zip code, browsing behavior, purchase history) can serve as effective substitutes for race, gender, or religion, producing discriminatory outcomes while maintaining technical compliance with anti-discrimination law. This project quantifies this dynamic in an advertising context and examines the policy frameworks available to address it.

## Practical Relevance

AI fairness is no longer an academic concern — it is a regulatory and litigation risk. The EU AI Act, CFPB guidance on algorithmic lending, and EEOC enforcement actions around AI hiring tools all create organizational accountability for discriminatory algorithmic outcomes. Security engineers working in regulated industries (financial services, healthcare, federal contracting) need to understand bias auditing as part of AI risk management and responsible AI adoption frameworks.

## Tools, Languages, and Libraries

Python · pandas · Matplotlib · Plotly (Sankey diagrams) · statistical analysis · policy research methodology

## Skills Demonstrated

- Bias auditing: quantifying demographic disparities in algorithmic targeting data
- Data visualization: Sankey diagrams for flow analysis of audience segmentation
- Fairness frameworks: applying Disparate Impact, Equal Opportunity, and Individual Fairness concepts
- Policy analysis: translating technical findings into compliance and risk recommendations
- Technical writing: communicating algorithmic fairness issues to legal and policy audiences

## Extension Ideas

- Apply the fairness analysis pipeline to a public ML dataset (COMPAS, Adult Income) and benchmark multiple fairness metrics
- Build a bias audit tool that accepts a trained classifier and produces a standardized disparate impact report
- Extend the policy analysis to cover the EU AI Act's requirements for high-risk AI system documentation
- Integrate the Sankey visualization into an interactive dashboard for non-technical stakeholders

---

*Georgia Institute of Technology — MS Computer Science · CS 6603: AI, Ethics, and Society*
