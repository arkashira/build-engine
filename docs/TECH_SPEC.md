# TECH_SPEC.md – build‑engine

---

## 1. Overview

**build‑engine** is a hybrid AI platform that blends high‑level reasoning (e.g., design, architecture) with low‑level code generation (e.g., snippets, refactoring). It serves as a developer assistant, providing end‑to‑end support for complex software tasks such as:

- **Design‑time**: generate architectural diagrams, component contracts, and design patterns.
- **Implementation‑time**: auto‑generate boilerplate, refactor code, and produce unit tests.
- **Review‑time**: static analysis, code quality scoring, and compliance checks.

The engine is built on top of the **vLLM** inference engine and **SGLang** structured generation framework, leveraging the company’s shared knowledge base (pgvector) for contextual embeddings.

---

## 2. Architecture

```
┌───────────────────────┐
│  Client (IDE/CLI/API) │
└─────────────┬─────────┘
              │
              ▼
┌───────────────────────┐
│  API Gateway (FastAPI)│
└───────┬───────┬───────┘
        │       │
        ▼       ▼
┌───────────────┐ ┌───────────────────────┐
│  Orchestration │ │  Knowledge‑Store (pgvector) │
│  Service (Celery) │ └───────────────────────┘
└───────┬───────┘
        │
        ▼
┌───────────────────────┐
│  vLLM Inference Engine│
└───────┬───────┬───────┘
        │       │
        ▼       ▼
┌───────────────┐ ┌───────────────────────┐
│  SGLang Engine │ │  Static‑Analysis Tool │
└───────┬───────┘ └───────────────────────┘
        │
        ▼
┌───────────────────────┐
│  Response Formatter   │
└───────────────────────┘
```

### 2.1 Components

| Component | Responsibility | Tech |
|-----------|----------------|------|
| **Client** | IDE plugin, CLI, or REST client | VSCode extension, Python CLI, HTTP |
| **API Gateway** | Auth, rate‑limit, request routing | FastAPI, Uvicorn |
| **Orchestration Service** | Task queue, workflow orchestration | Celery + Redis |
| **Knowledge‑Store** | Vector embeddings, context retrieval | pgvector + PostgreSQL |
| **vLLM Engine** | Large‑model inference | vLLM (CUDA, TensorRT) |
| **SGLang Engine** | Structured generation, prompt templates | SGLang |
| **Static‑Analysis Tool** | Linting, type‑checking, security | `pylint`, `mypy`, `bandit` |
| **Response Formatter** | Convert raw model output to user‑friendly format | Jinja2 templates |

---

## 3. Data Model

### 3.1 Core Tables

| Table | Columns | Notes |
|-------|---------|-------|
| `projects` | `id`, `name`, `owner_id`, `created_at` | Tracks user projects |
| `tasks` | `id`, `project_id`, `type`, `status`, `payload`, `result`, `created_at`, `updated_at` | Generic task queue |
| `embeddings` | `id`, `project_id`, `vector` (pgvector) | Stores contextual embeddings |
| `model_runs` | `id`, `task_id`, `model_name`, `prompt`, `output`, `latency_ms` | Audit trail |

### 3.2 Embedding Generation

- **Source**: Project source code, design docs, and user prompts.
- **Model**: `sentence-transformers/all-MiniLM-L6-v2` (or company‑trained variant).
- **Storage**: `pgvector` column type in PostgreSQL.

---

## 4. Key APIs / Interfaces

| Endpoint | Method | Description | Request | Response |
|----------|--------|-------------|---------|----------|
| `/v1/projects` | POST | Create a new project | `{ "name": "myproj" }` | `{ "id": "...", "name": "..."}`
| `/v1/projects/{id}/tasks` | POST | Submit a task (design, code, review) | `{ "type": "design", "payload": { ... } }` | `{ "task_id": "...", "status": "queued" }`
| `/v1/tasks/{id}` | GET | Poll task status | N/A | `{ "status": "...", "result": "..." }`
| `/v1/embeddings/{project_id}` | GET | Retrieve relevant embeddings | N/A | `[ { "id": "...", "vector": [...] } ]`
| `/v1/health` | GET | Health check | N/A | `{ "status": "ok" }`

### 4.1 Task Payloads

- **Design**: `{ "language": "python", "components": ["auth", "db"], "style": "clean" }`
- **Code**: `{ "source_file": "app.py", "changes": "add logging" }`
- **Review**: `{ "source_file": "app.py", "analysis": ["lint", "security"] }`

---

## 5. Tech Stack

| Layer | Technology | Rationale |
|-------|------------|-----------|
| **API** | FastAPI | Async, OpenAPI, lightweight |
| **Worker** | Celery + Redis | Decoupled task processing |
| **Inference** | vLLM (CUDA) | High‑throughput, low‑latency |
| **Structured Gen** | SGLang | Predictable output, schema enforcement |
| **Static Analysis** | `pylint`, `mypy`, `bandit` | Industry‑standard tools |
| **Vector DB** | PostgreSQL + pgvector | Relational + vector search |
| **Container** | Docker, Docker‑Compose | Reproducible builds |
| **CI/CD** | GitHub Actions | Automated tests, lint, deployment |
| **Monitoring** | Prometheus + Grafana | Metrics, alerts |
| **Auth** | OAuth2 / JWT | Secure API access |

---

## 6. Dependencies

| Dependency | Version | Purpose |
|------------|---------|---------|
| `fastapi` | `>=0.110.0` | Web framework |
| `uvicorn` | `>=0.29.0` | ASGI server |
| `celery` | `>=5.3.0` | Task queue |
| `redis` | `>=5.0.0` | Message broker |
| `vllm` | `>=0.5.0` | Inference engine |
| `sglang` | `>=0.3.0` | Structured generation |
| `psycopg2-binary` | `>=2.9.0` | PostgreSQL driver |
| `pgvector` | `>=0.3.0` | Vector extension |
| `pylint` | `>=3.0.0` | Linting |
| `mypy` | `>=1.10.0` | Type‑checking |
| `bandit` | `>=1.7.0` | Security scanning |
| `jinja2` | `>=3.1.0` | Template rendering |
| `python-dotenv` | `>=1.0.0` | Env var loading |

---

## 7. Deployment

### 7.1 Local Development

```bash
# Clone repo
git clone https://github.com/arkashira/build-engine.git
cd build-engine

# Create env
cp .env.example .env
# Edit .env with DB credentials, Redis URL, etc.

# Build containers
docker compose up --build
```

### 7.2 Production

- **Kubernetes** (recommended)
  - Deploy API, Celery workers, Redis, PostgreSQL, and vLLM pods.
  - Use Helm chart (`helm install build-engine ./helm/build-engine`).
- **Autoscaling**:
  - Scale Celery workers based on task queue depth.
  - Scale vLLM pods based on GPU availability.

### 7.3 CI/CD Pipeline

1. **Lint & Test** – `pytest`, `pylint`, `mypy`.
2. **Build Docker Image** – `docker build -t axentx/build-engine:latest .`
3. **Push to Registry** – Docker Hub / GitHub Packages.
4. **Deploy** – Helm upgrade or `kubectl apply`.

---

## 8. Security & Compliance

- **Authentication**: OAuth2 with JWT; scopes per endpoint.
- **Data Encryption**: TLS for all external traffic; data-at-rest encrypted in PostgreSQL.
- **Audit Logging**: All API calls logged with request/response payloads (excluding PII).
- **Rate Limiting**: 100 requests/min per user.

---

## 9. Extensibility

- **Model Plug‑in**: Replace vLLM model by updating `MODEL_NAME` env var.
- **Prompt Templates**: Stored in `templates/` directory; can be overridden per project.
- **Static Analysis Rules**: Configurable via `analysis_rules.yaml`.

---

## 10. Future Enhancements

- **Multi‑model fallback** (e.g., GPT‑4, Claude) for fallback or higher‑quality outputs.
- **Real‑time collaboration** via WebSocket API for live code editing.
- **Marketplace** for third‑party prompt templates and analysis plugins.

---

**Prepared by:**  
Senior Product/Engineering Lead – Axentx  
Date: 2026‑06‑21

---
