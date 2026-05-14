# AI Cyber Capability Evaluation: A Federal RMF Lens on Frontier Model Risk

**Subject Area:** AI Security · NIST AI RMF · Frontier Model Evaluation · Federal Risk Management · ATO Decision Support

---

## What It Does

This is an independent research write-up that bridges two bodies of work that do not currently talk to each other: the rapidly maturing public benchmark literature on frontier model cyber capability, and the NIST AI Risk Management Framework that federal programs use to make AI adoption decisions. It surveys the relevant public benchmarks (CyberSecEval, Cybench, NYU CTF Bench, InterCode-CTF, AutoAdvExBench, METR autonomous task evaluations, and the Frontier Red Team reports published by frontier labs), proposes a mapping from those benchmark signals into specific AI RMF Map function subcategories, identifies four gaps that a federal use case exposes in the current public eval landscape, and sketches a reference evaluation pattern an agency could apply during ATO style review of a deployed LLM.

## Problem Addressed

Federal AI deployment decisions today land in front of RMF assessors who are fluent in 800-53 control families and accreditation lifecycles but who do not have a structured way to interpret published cyber capability benchmark scores into ATO grade risk language. Vendor system cards quote eval results. NIST AI RMF tells reviewers what categories of risk to characterize. The connecting layer, where a specific benchmark signal informs a specific Map subcategory in a specific deployment context, is missing in any consolidated form. That gap is where this work sits.

## Practical Relevance

This work is built for the audience I work with daily and for the audience I want to be writing for in five years. It is directly usable by:

- ISSEs, ISSOs, and assessors writing the AI portion of an RMF package for a frontier LLM deployment
- AI governance and risk leads in regulated industry adapting NIST AI RMF to operational decision making
- AI red teams looking for the federal language to wrap around their technical findings so the results land with policy and authorization audiences
- Cleared cyber engineers transitioning into AI security roles and needing a portfolio artifact that demonstrates fluency in both domains

## Tools, Languages, and Libraries

Markdown · Public benchmark literature synthesis · NIST AI RMF 1.0 (Map function) · NIST AI 600-1 (Generative AI Profile, 2024) · Cross domain analysis methodology

## Skills Demonstrated

- Translating frontier AI capability evidence into federal RMF risk language
- Synthesis of fast moving published research across multiple labs and venues
- Building a mapping table that is honest about its first cut nature and the disagreements it invites
- Identifying gaps in a published framework against a real operational use case
- Sequencing a reference evaluation pattern that an ATO reviewer could actually apply
- Writing with deliberate intellectual honesty about what was done, what was not done, and why

## Extension Ideas

- Build a Python harness that runs CyberSecEval insecure code and prompt injection subtests against a small set of open weights models hosted locally, and publish raw numbers as a follow-up
- Extend the mapping table to AI RMF Govern and Manage functions, not just Map
- Pilot the reference evaluation pattern against a hypothetical agency LLM deployment scenario and produce a sample MAP 5.2 artifact as a template
- Track NIST AI RMF Generative AI Profile control updates and refresh the mapping as new guidance lands
- Add a controlled environment variant of the pattern that addresses sensitive context evaluations that cannot be done with public benchmarks

---

*Independent research, May 2026. Not associated with any current employer or program.*
