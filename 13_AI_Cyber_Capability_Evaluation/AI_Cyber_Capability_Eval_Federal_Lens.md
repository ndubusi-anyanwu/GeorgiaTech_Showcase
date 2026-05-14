# AI Cyber Capability Evaluation: A Federal RMF Lens on Frontier Model Risk

*Independent research write-up. Ndubusi Anyanwu. May 2026.*

## Why I wrote this

I work as a security engineer in federal cyber, where most of my time goes to the risk paragraphs and control narratives that move federal programs toward Authority to Operate decisions. The closer federal programs come to using frontier language models, the more I notice the same uncomfortable thing. There is no clean way to translate "this model is dangerous in a cyber context" into the language an RMF reviewer actually reads.

There are good public benchmarks now. CyberSecEval from Meta. Cybench from Berkeley and Stanford. NYU CTF Bench. METR's autonomous task evaluations. Anthropic publishes Frontier Red Team reports under its Responsible Scaling Policy. There is also a clear and well structured framework in NIST AI RMF, with a Map function designed to characterize risk before a deployment decision is made. What I cannot find, at least not in any consolidated form, is the bridge. Take the published cyber capability evidence, map it to AI RMF Map categories, and produce something a federal reviewer can use during ATO style review of a frontier LLM deployment.

This write-up is my first cut at that bridge. It is a synthesis paper, not an experimental one. I do not have a GPU cluster sitting in my living room, and I would rather give an honest reading of work already in the public record than invent numbers. What I will do is survey the public benchmarks, classify what each one actually measures, propose where each maps into the AI RMF Map function, identify the gaps that a federal use case exposes, and sketch a reference evaluation pattern an agency could apply during ATO style review.

## The decision problem facing a federal AI assessor

The question that lands on the assessor's desk is not philosophical. A program office says they want to use a specific frontier model for a specific task. Maybe the task is summarizing analyst reporting. Maybe it is drafting code that will be merged into operational tooling. Maybe it is an agent calling other tools across a mission enclave. The job is to figure out whether this is safe to authorize.

The first ATO instinct is to ask what the model can do, then ask what it can do that nobody approved. For most of the existing 800-53 control families this is familiar territory. Access control, audit logging, supply chain risk, configuration management. With a frontier LLM the surface widens in ways the old controls were not written for. The model is the supply chain. It can exhibit capability that was not in any product datasheet. It can respond differently to different inputs from different users. The worst case for a cyber focused review is that the model lowers the operational cost of an attack to the point where an adversary who was not previously a credible threat becomes one.

NIST published the AI Risk Management Framework specifically to give risk professionals a structure for thinking about questions like these. The Map function is where the framing work happens. Who uses the system. What risks its use creates. What the magnitude of those risks looks like. The problem from where I sit is that AI RMF tells the reviewer what categories of question to ask. It does not tell the reviewer what evidence answers those questions for a model that might be writing working exploit code on the side.

That is the gap this write-up is trying to fill. Public cyber capability benchmarks are the evidence. AI RMF is the question structure. Connecting them is the missing step before a federal program can sign an ATO with confidence.

## What the public benchmarks actually measure

The benchmark landscape has matured rapidly. The ones below are the most relevant for a cyber focused review.

**CyberSecEval (Meta, Purple Llama).** First released late 2023, currently at v3. The suite mixes capability tests with refusal rate tests. The insecure code subtest asks the model to complete coding tasks and measures how often the completed code contains a known vulnerability class. The cyber attack helpfulness subtest scores whether the model complies with prompts that ask for direct offensive assistance. Later versions added prompt injection susceptibility, code interpreter abuse, spear phishing capability, and an autonomous offensive cyber operations evaluation that scores end to end agent runs. All artifacts are public on GitHub.

**Cybench (Berkeley and Stanford, 2024).** A focused benchmark of forty CTF tasks drawn from real competitions across cryptography, web, reverse engineering, forensics, and pwn. Cybench scores agent capability end to end, meaning the model has to operate in a Linux shell, use tools, and submit a flag rather than just answer multiple choice. Frontier models like Claude 3.5 Sonnet and GPT-4o solve a non-trivial share of the easier challenges. The harder ones still resist most models.

**NYU CTF Bench.** Roughly two hundred CTF challenges sourced from real events. Larger and more diverse than Cybench. Useful for studying capability variance across challenge types.

**InterCode-CTF.** An interactive shell environment built for agentic CTF play. Less about scoring than about giving researchers a reproducible scaffold for letting a model take iterative actions against a target.

**AutoAdvExBench.** Less classically "cyber" and more adversarial ML, but worth including. Tests whether a model can automatically generate adversarial inputs against another model. Relevant for adversarial robustness reviews in deployed ML pipelines.

**METR autonomous task evaluations.** Time horizon evaluations on agentic tasks, including cyber operations as a task family. METR's results are widely cited in the responsible scaling community and are referenced in the system cards of multiple frontier labs.

**Anthropic Frontier Red Team public reports.** Anthropic publishes specific capability claims with each major model release under its Responsible Scaling Policy. These reports are not a benchmark in the academic sense, but they are the most operationally useful public artifacts for understanding what one frontier lab's red team thinks the current generation can do.

It is worth saying out loud what these benchmarks do not do. None of them measure the model under your deployment configuration. None of them measure capability in your specific mission context. None of them quantify uplift over your specific baseline attacker. They measure the model in isolation, with research prompts, in research conditions. They are necessary inputs to a risk review. They are not the review itself.

## Mapping to NIST AI RMF Map function

The Map function in AI RMF 1.0 has five categories. The ones most relevant for a cyber capability review are MAP 1 (context), MAP 3 (capabilities and goals against benchmarks), and MAP 5 (impacts).

A first pass mapping looks like this.

| Benchmark or evaluation source | Primary signal it provides | AI RMF Map subcategory it informs |
|---|---|---|
| CyberSecEval insecure code rate | Likelihood the model writes vulnerable code in normal use | MAP 5.1 |
| CyberSecEval cyber attack helpfulness | Likelihood the model complies with offensive requests | MAP 3.2, MAP 5.1 |
| CyberSecEval prompt injection susceptibility | Likelihood of system compromise via input | MAP 2.3 |
| Cybench, NYU CTF Bench | Offensive capability ceiling on representative tasks | MAP 3.1, MAP 3.2 |
| InterCode-CTF | Capability under agentic conditions | MAP 3.2, MAP 5.1 |
| METR autonomous cyber task evals | Risk of unsupervised offensive activity | MAP 5.1, MAP 5.2 |
| Vendor Frontier Red Team reports | Vendor attested capability ceiling | MAP 3.1, MAP 4.1 |

Two things to read off this table. First, no public benchmark cleanly lands in MAP 1 (context). That is by design. The context of a deployment is something the program office documents, not something a benchmark can answer. Second, MAP 5.2, which is where AI RMF asks about test, evaluation, validation, and verification, is the natural home for evaluation results. A federal review that does not produce a MAP 5.2 artifact has not really completed the Map function for a frontier LLM.

## Where the federal specific gaps show up

When I work through this mapping against a representative ATO scenario, four gaps come into focus.

The first gap is mission specificity. Public benchmarks measure capability on representative tasks. Federal missions have specific threat surfaces, some of which cannot be characterized openly. A score on CyberSecEval tells me the model is generally willing to help with offensive code. It does not tell me whether the model knows enough about a specific platform or a specific operational workflow to be useful to an adversary who already has internal access. That is not a flaw in the benchmark. It is a gap in what is possible to publish openly. The federal version of this evaluation has to be done inside the deployment environment, by appropriately cleared personnel, on representative mission data.

The second gap is uplift. RMF reviewers care about delta. The right question is not "can this model write exploit code" but "how much faster, cheaper, or better can a specific adversary class operate with this model than without it." The public benchmark landscape mostly answers the first question, not the second. METR's time horizon evaluations and Anthropic's RSP reports start to gesture toward uplift modeling, but the field is early. A federal reviewer doing this today has to build their own uplift estimate, and the eval results are an input, not a deliverable.

The third gap is configuration drift. Public benchmarks measure the model. Federal deployments measure the model plus a system prompt plus an API safety filter plus a wrapper application plus a logging layer. The behavior of the deployed system can diverge significantly from the behavior of the bare model. An RMF review for a frontier LLM that cites only vendor benchmark scores has skipped a step. The right evaluation is on the deployed configuration, not on the model card.

The fourth gap is reauthorization. Most ATOs reauthorize on a calendar cadence. LLMs update on a vendor cadence. The current AI RMF Map function does not have a strong story for "the model was reauthorized in January and silently improved at exploit synthesis in March." A federal program needs a trigger event tied to model version changes that automatically reopens the relevant MAP categories, separate from the calendar driven reauthorization clock.

## A reference evaluation pattern for federal use

Pulling the threads together, the rough pattern a federal program could apply when reviewing a frontier LLM deployment looks like this.

First, document the deployment in MAP 1. Intended task, user population, data classifications touched, system prompt, safety configuration, telemetry. This is the part RMF reviewers already know how to do well. The only addition is to capture the exact model version and the exact wrapper code at the time of review.

Second, ingest the available vendor evidence. Vendor system cards. Vendor Frontier Red Team reports. Any published evaluations the vendor cites. This becomes MAP 3.1 (intended benefits) and MAP 4.1 (third party risk) input.

Third, run a curated subset of the public benchmarks against the deployed configuration, not the bare model. The most useful starting set is CyberSecEval insecure code, CyberSecEval cyber attack helpfulness, CyberSecEval prompt injection, and a small slice of Cybench in the categories most relevant to the mission. These produce MAP 5.1 evidence directly.

Fourth, compare the deployed configuration results to the vendor reported bare model results. Any delta is the value the deployment configuration is adding or removing in terms of risk. Most of the time the deployment will reduce raw scores because the system prompt and filters do useful work. Sometimes it will not, and that surprise is exactly what MAP 5 was written to surface.

Fifth, write a MAP 5.2 artifact. The artifact does not need to be long. It needs to say what was evaluated, on what configuration, with what results, against what thresholds, and what the residual risk is after compensating controls. The format can be a short technical report attached to the accreditation package.

Sixth, register a reauthorization trigger. When the model version changes, when the system prompt changes, or when a new public benchmark in a relevant category is released, the MAP 3 and MAP 5 categories reopen and steps three through five run again. Calendar cadence is not enough.

This pattern is not original in its components. Each step has analogs in current RMF practice or in published AI risk guidance. What it does is sequence them in a way that produces an actionable record an ATO reviewer can sign against.

## Honest limitations

A few things to keep in mind about what this write-up is and is not.

I am one security engineer with a graduate ML specialization, not a national lab. The benchmark survey above is current to my knowledge as of May 2026. The cyber evaluation landscape is moving fast enough that any cited benchmark could be deprecated or superseded by next quarter. The reader should treat the survey as a starting point, not a definitive list.

The mapping table is a first cut. Different reviewers will land different evidence in different MAP subcategories depending on context. The point of the table is to make the choices explicit so they can be argued about, not to be the final answer.

I did not run any of the benchmarks for this write-up. Doing so honestly requires either licensed access to frontier API endpoints with a documented evaluation budget, or local infrastructure to host open weights at the scale where the cyber evaluations make sense. Both are doable. Neither was in scope for this particular artifact.

The reference evaluation pattern in the preceding section assumes a cooperative vendor and a deployment that lives behind a stable API. Federal deployments that fine tune a model, or that wrap an open weights model behind a custom inference stack, will need a heavier evaluation lift than what is sketched here.

Finally, the obvious point. None of this replaces a real adversarial test by a qualified red team on the deployed system. The evaluation pattern above is the structured paperwork side of an ATO. The red team is what tells you whether the paperwork is right.

## References

CyberSecEval suite, Purple Llama, Meta. https://github.com/meta-llama/PurpleLlama

Cybench: A Framework for Evaluating Cybersecurity Capabilities and Risk of Language Models. Zhang et al., 2024.

NYU CTF Bench. New York University CTF benchmark suite.

InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback. Yang et al., 2023.

NIST AI Risk Management Framework 1.0. National Institute of Standards and Technology, 2023.

NIST AI RMF Generative AI Profile (NIST AI 600-1). National Institute of Standards and Technology, 2024.

METR (Model Evaluation and Threat Research). https://metr.org

Anthropic Responsible Scaling Policy and Frontier Red Team reports. https://www.anthropic.com/rsp

Microsoft AI Red Team lessons (Bullwinkel et al., 2024).
