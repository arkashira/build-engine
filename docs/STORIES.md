# STORIES.md – build‑engine

## Overview

**build‑engine** is a hybrid AI tool that blends high‑level strategic reasoning with low‑level code generation to help developers and organizations tackle complex software tasks.  
The product will expose a web UI, a CLI, and a REST API, and will be powered by a fine‑tuned LLM (vLLM) and a structured generation engine (SGLang).  

The following backlog is organized into epics that reflect the core value‑propositions of the product.  Stories are written in the classic *As a <role>, I want <goal>, so that <benefit>* format and include acceptance criteria.  The order reflects the MVP delivery sequence.

---

## Epics

| Epic | Description |
|------|-------------|
| **E1 – Core AI Engine** | Build the inference engine that can answer high‑level design questions and generate low‑level code snippets. |
| **E2 – Interaction Layer** | Provide UI, CLI, and API for developers to interact with the engine. |
| **E3 – Context Management** | Enable the engine to remember project context, user preferences, and previous interactions. |
| **E4 – Quality & Safety** | Ensure generated code is safe, linted, and meets basic quality standards. |
| **E5 – Deployment & Ops** | Package the tool for easy deployment, monitoring, and scaling. |
| **E6 – Feedback Loop** | Capture user feedback and usage data to improve the model and product. |

---

## User Story Backlog

### Epic E1 – Core AI Engine

| # | Story | Acceptance Criteria |
|---|-------|---------------------|
| **E1‑S1** | *As a developer, I want the engine to answer design‑level questions, so that I can quickly evaluate architectural options.* | • The engine returns a concise, well‑structured answer within 3 s.<br>• Answers reference at least one external source or code example.<br>• The answer is marked with a confidence score. |
| **E1‑S2** | *As a developer, I want the engine to generate a code snippet for a given function signature, so that I can bootstrap implementation.* | • Input: function signature + brief description.<br>• Output: compilable code in the target language (Python/TypeScript).<br>• Code passes a basic unit test (provided in the prompt). |
| **E1‑S3** | *As a product owner, I want the engine to explain the generated code, so that stakeholders can understand the solution.* | • Engine outputs a short explanation (≤ 150 words) describing the algorithm and key decisions.<br>• Explanation is linked to the code block. |
| **E1‑S4** | *As a developer, I want the engine to suggest improvements to my existing code, so that I can refactor efficiently.* | • Input: code snippet + optional comment.<br>• Output: refactored code + list of suggested improvements.<br>• Refactored code compiles and passes the original unit tests. |

### Epic E2 – Interaction Layer

| # | Story | Acceptance Criteria |
|---|-------|---------------------|
| **E2‑S1** | *As a developer, I want a web UI where I can type prompts and see generated code, so that I can interact without a terminal.* | • UI has a prompt box, submit button, and output panel.<br>• Generated code is syntax‑highlighted.<br>• UI loads within 2 s on a standard laptop. |
| **E2‑S2** | *As a developer, I want a CLI tool that accepts prompts via arguments, so that I can integrate it into scripts.* | • `build-engine prompt "..."` returns the generated code.<br>• Supports `--lang` flag to specify target language.<br>• Exit code 0 on success, 1 on failure. |
| **E2‑S3** | *As a developer, I want a REST API that accepts JSON prompts, so that I can embed the engine in my services.* | • POST `/v1/generate` with `{prompt, lang}` returns `{code, explanation}`.<br>• API is documented via OpenAPI spec. |
| **E2‑S4** | *As a product owner, I want the UI to display a usage counter, so that I can monitor API consumption.* | • Counter shows number of requests per day.<br>• Counter updates in real time. |

### Epic E3 – Context Management

| # | Story | Acceptance Criteria |
|---|-------|---------------------|
| **E3‑S1** | *As a developer, I want the engine to remember my project name and language, so that I don’t have to re‑specify them each time.* | • Context is stored per session.<br>• Subsequent prompts automatically include the stored context. |
| **E3‑S2** | *As a developer, I want to reset the context, so that I can start a new project.* | • UI button “Reset Context” clears stored data.<br>• CLI flag `--reset-context` clears context. |
| **E3‑S3** | *As a developer, I want to view my context history, so that I can review past interactions.* | • UI tab “History” lists prompts and responses.<br>• History is searchable by keyword. |

### Epic E4 – Quality & Safety

| # | Story | Acceptance Criteria |
|---|-------|---------------------|
| **E4‑S1** | *As a developer, I want the engine to lint generated code, so that I can avoid syntax errors.* | • Generated code is passed through a language‑specific linter (e.g., flake8 for Python).<br>• Linter errors are reported back to the user. |
| **E4‑S2** | *As a developer, I want the engine to flag potentially unsafe code (e.g., `eval`, `exec`), so that I can avoid security risks.* | • Engine scans for unsafe patterns.<br>• Unsafe patterns are highlighted and a warning is shown. |
| **E4‑S3** | *As a product owner, I want a safety score for each response, so that I can gauge overall risk.* | • Safety score (0–1) is returned with each response.<br>• Score is based on predefined heuristics. |

### Epic E5 – Deployment & Ops

| # | Story | Acceptance Criteria |
|---|-------|---------------------|
| **E5‑S1** | *As an ops engineer, I want a Docker image that runs the engine, so that I can deploy it easily.* | • Dockerfile builds in < 5 min.<br>• Container exposes port 8000 for the API. |
| **E5‑S2** | *As an ops engineer, I want health‑check endpoints, so that I can monitor uptime.* | • GET `/health` returns 200 OK with JSON `{status:"ok"}`.<br>• Health check includes model load status. |
| **E5‑S3** | *As a product owner, I want metrics (latency, request count) exposed via Prometheus, so that I can monitor performance.* | • `/metrics` endpoint follows Prometheus format.<br>• Metrics include `build_engine_request_latency_seconds` and `build_engine_request_count`. |

### Epic E6 – Feedback Loop

| # | Story | Acceptance Criteria |
|---|-------|---------------------|
| **E6‑S1** | *As a developer, I want to flag incorrect or low‑quality responses, so that the model can improve.* | • UI button “Flag” next to each response.<br>• Flagged data is stored in a feedback table with timestamp. |
| **E6‑S2** | *As a data scientist, I want to export feedback logs, so that I can retrain the model.* | • CLI command `build-engine export-feedback --output path.csv` exports all flags.<br>• CSV contains columns: prompt, response, flag, timestamp. |
| **E6‑S3** | *As a product owner, I want a dashboard showing aggregate feedback trends, so that I can prioritize improvements.* | • Dashboard displays number of flags per day, top flagged categories.<br>• Dashboard is accessible at `/dashboard`. |

---

## MVP Order

1. **E1‑S1, E1‑S2, E1‑S3** – Core generation capabilities.  
2. **E2‑S1, E2‑S2, E2‑S3** – Interaction channels.  
3. **E3‑S1, E3‑S2** – Basic context handling.  
4. **E4‑S1, E4‑S2** – Linting and safety.  
5. **E5‑S1, E5‑S2** – Docker & health checks.  
6. **E6‑S1, E6‑S2** – Feedback capture and export.  
7. **E3‑S3, E4‑S3, E5‑S3, E6‑S3** – Advanced UI/history, safety score, metrics, dashboard.

---

## Notes

- All stories assume the use of the existing **vLLM** inference engine and **SGLang** structured generation framework.  
- The product must respect the company’s data‑privacy policies; no user prompts are stored beyond the session unless explicitly flagged.  
- The backlog is intentionally focused on deliverables that can be shipped quickly while providing clear value to developers and stakeholders.
