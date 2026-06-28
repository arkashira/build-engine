## partner-targets.md  
*Hybrid AI “build‑engine” – Partner Integration Roadmap*  

| # | SaaS / API | Core Capability (why it matters for build‑engine) | Free‑Tier / Limits* | Integration Effort | Value‑Add (User Job Solved) | Revenue‑Share / Affiliate Potential |
|---|------------|---------------------------------------------------|----------------------|--------------------|----------------------------|--------------------------------------|
| 1 | **GitHub (REST & GraphQL)** | Source‑code hosting, PR creation, CI status, repo‑level metadata. Enables the engine to **read, modify and push code** in the developer’s own org. | 5 k API calls / hr, unlimited public repo access, private repo access for GitHub Apps (free for orgs ≤ 3 users) | **M** – OAuth app + webhook registration, PR/commit diff parsing | *“Generate production‑ready PRs from high‑level specs”* | GitHub Marketplace revenue‑share (20 % on paid app upgrades). |
| 2 | **OpenAI / Azure OpenAI** | State‑of‑the‑art LLM for high‑level reasoning, prompt‑engineering, code generation. Provides the **cognitive layer** of build‑engine. | 5 M tokens / month (free trial) | **M** – API wrapper, token‑budget manager, safety filters | *“Translate business requirements into design docs & skeleton code”* | Affiliate via Azure CSP program (up‑sell to Azure OpenAI credits). |
| 3 | **Docker Hub / GitHub Container Registry** | Container image build, storage, and scanning. Allows the engine to **produce runnable artifacts** and run security scans automatically. | 100 GB storage, 100 GB data transfer per month (Docker Hub free) | **S** – Docker SDK integration, image tagging workflow | *“Deliver ready‑to‑run containers from generated code”* | Potential revenue‑share on paid storage tiers (Docker Hub Partner Program). |
| 4 | **HashiCorp Terraform Cloud (API)** | IaC plan/apply execution, state storage. Lets build‑engine **provision infra** as part of end‑to‑end delivery. | 5 runs / workspace / month (free) | **L** – Terraform provider wrapper, state‑sync, secret handling | *“Spin up cloud resources automatically from generated infra code”* | Referral fee for Terraform Cloud Enterprise upgrades. |
| 5 | **Zapier / Make (Integromat) API** | Low‑code workflow automation across 5 k+ SaaS apps. Enables **cross‑tool orchestration** (e.g., create JIRA tickets, Slack alerts) after a build completes. | 100 tasks / month (Zapier Free) | **S** – Webhook endpoint, task template library | *“Notify teams & trigger downstream processes without manual steps”* | Affiliate per‑user revenue share (Zapier Partner Program). |
| 6 | **Snyk (or GitHub Advanced Security)** | Static/Dynamic code analysis, dependency scanning, license compliance. Guarantees **security & compliance** of generated code before merge. | 100 tests / month (Snyk Free) | **M** – API token flow, results parsing, remediation suggestions | *“Auto‑fix vulnerabilities in AI‑generated code”* | Referral bonus on paid Snyk plans. |
| 7 | **Jira Cloud (Atlassian REST API)** | Issue tracking, sprint planning, backlog grooming. Allows the engine to **create tickets** for generated features, bugs, or tech‑debt. | 10 000 API calls / day (free tier) | **S** – OAuth, issue‑type mapping, webhook sync | *“Turn AI‑generated specs into actionable backlog items”* | Atlassian Marketplace revenue‑share on paid add‑ons. |
| 8 | **Stripe Billing API** | Subscription management, usage‑based billing. Enables **pay‑as‑you‑go pricing** for build‑engine compute minutes or generated artifacts. | $0.5 M processed / month (no fee for test mode) | **M** – webhook handling, metered usage tracking | *“Charge per generated PR, container, or infra run”* | Direct revenue (no share) but opens cross‑sell to Stripe partner ecosystem. |

\*Free‑tier limits are as of 2024‑12‑01; they are sufficient for early‑adopter pilots and for validating the integration before scaling to paid tiers.

### Prioritisation Rationale
1. **GitHub** – Core to any developer workflow; high affiliate upside; low‑effort for read/write access.  
2. **OpenAI / Azure OpenAI** – The brain of the product; essential for high‑level reasoning; free token quota for MVP.  
3. **Docker Hub** – Turns code into deployable artifacts; modest effort, immediate value for CI/CD pipelines.  
4. **Zapier** – Provides “glue” to thousands of SaaS tools; quick win for workflow automation; affiliate revenue.  
5. **Snyk** – Security is a non‑negotiable differentiator; free tier covers early testing; referral fees.  
6. **Terraform Cloud** – Extends product from code generation to infra provisioning; larger effort but opens enterprise TAM.  
7. **Jira** – Aligns generated work with PM processes; low effort, strong Atlassian partner program.  
8. **Stripe** – Enables monetisation model; medium effort; direct revenue rather than share but critical for go‑to‑market.  

### Integration Timeline (Quarterly)

| Quarter | Milestones | Integrated Partners |
|---------|------------|---------------------|
| **Q1 2026** | MVP core loop (spec → PR) | GitHub, OpenAI, Docker Hub |
| **Q2 2026** | Secure delivery & feedback loop | Snyk, Stripe Billing |
| **Q3 2026** | Automation & orchestration layer | Zapier, Jira |
| **Q4 2026** | Full‑stack provisioning | Terraform Cloud |
| **2027 H1** | Expansion & revenue‑share optimisation | Additional SaaS (e.g., Notion, Asana) based on user demand |

---  

*Prepared by Business‑Synthesis – Axentx OS*  