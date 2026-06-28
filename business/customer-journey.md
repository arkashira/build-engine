# Customer Journey – **build‑engine**  

| Phase | Trigger Event | Friction Points | User Emotions | Opportunities to Delight | Success Metric |
|-------|---------------|----------------|---------------|--------------------------|----------------|
| **Aware** | • Reads a dev‑blog post about “AI that can *design* and *code* together”. <br>• Sees a LinkedIn ad: “Turn architecture sketches into production code in seconds”. <br>• Hears a teammate mention a bottleneck when moving from design to implementation. | • Information overload – many AI‑coding tools claim similar benefits. <br>• Unclear whether the tool works on the organization’s stack (e.g., .NET, Go, Kubernetes). <br>• Fear of hidden costs / licensing. | Curiosity → Skepticism | • Publish a **one‑page “What‑If” calculator** that quantifies time saved (e.g., 30 % faster design‑to‑code). <br>• Release a **short demo video** (≤90 s) showing a real‑world architecture diagram turned into a working micro‑service. <br>• Offer a **free “AI‑Design‑Audit”** (email‑based) for the first 100 sign‑ups. | **Impression‑to‑Click Rate** – target **≥5 %** of impressions generate a click to the product landing page. |
| **Consider** | • Visits the landing page, reads the value‑prop and case studies. <br>• Downloads the “Technical Deep‑Dive” PDF. <br>• Joins a live webinar where a senior engineer demos the tool on a real ticket. | • Lack of concrete integration examples for the user’s CI/CD pipeline. <br>• Concern about data privacy when feeding proprietary designs to the AI. <br>• Uncertainty about pricing model (pay‑per‑run vs subscription). | Analytical → Cautious optimism | • Provide **interactive integration wizard** that auto‑generates a minimal Dockerfile / GitHub Action for the user’s stack. <br>• Publish a **security white‑paper** (SOC‑2, ISO‑27001 compliance) and a **data‑ownership FAQ**. <br>• Offer a **transparent pricing calculator** (e.g., $0.02 per generated line, with a $199/mo “unlimited” tier). | **Qualified‑Lead Rate** – **≥30 %** of visitors download the PDF or register for the webinar. |
| **Try** | • Signs up for a 14‑day free trial (no credit card). <br>• Uploads a high‑level system diagram (UML, ArchiMate, or simple markdown). | • Initial latency while the hybrid model loads the high‑level context. <br>• Learning curve for the “prompt‑engineering” UI (how to ask for low‑level implementation). <br>• Limited sandbox resources (CPU/GPU) causing slower generation on large models. | Excitement → Frustration (if performance lags) | • Offer a **“First‑Run Boost”** – dedicated GPU node for the first 5 generations. <br>• Provide **in‑app guided tours** with example prompts and a “Prompt‑Suggest” AI that rewrites user intent into optimal syntax. <br>• Deploy a **real‑time progress dashboard** showing token usage, cost estimate, and ETA. | **Trial Activation** – **≥70 %** of sign‑ups run at least one generation within the first 48 h. |
| **Adopt** | • Converts to a paid plan after trial (or after a “pay‑as‑you‑go” pilot). <br>• Integrates build‑engine into the organization’s CI pipeline. | • Governance: need for role‑based access control (RBAC) and audit logs. <br>• Scaling: handling concurrent requests across multiple teams. <br>• Support: response time for critical failures. | Confidence → Empowerment | • Ship **Enterprise‑Ready RBAC** and **audit‑log export** out‑of‑the‑box. <br>• Provide a **dedicated Customer Success Manager** for the first 90 days. <br>• Release **“Team Templates”** (pre‑built prompt libraries) that map to common internal standards (e.g., security hardening, logging). | **Conversion Rate** – **≥25 %** of trial users become paying customers; **NPS ≥ 55** after 30 days of paid usage. |
| **Expand** | • Teams start using build‑engine for more than just code generation (e.g., automated test scaffolding, infra‑as‑code). <br>• Organization evaluates additional seats or higher‑tier plans. | • Feature gaps: need for multi‑modal inputs (e.g., voice, design‑tool plugins). <br>• Pricing friction for large‑scale usage (volume discounts). | Satisfaction → Advocacy | • Launch **Marketplace Plugins** (e.g., Figma → build‑engine, VS Code extension). <br>• Offer **volume‑discount contracts** and **annual‑commitment rebates**. <br>• Run a **“Customer Innovation Showcase”** where power users present their workflows; winners receive free premium seats. | **Expansion Revenue** – **≥20 %** of existing accounts upgrade or add seats within 6 months; **Referral Rate** – **≥10 %** of users refer a new organization. |

---

### Narrative Flow (for internal alignment)

1. **Aware** – Capture attention with concise, data‑driven content that quantifies the problem (time spent translating design → code).  
2. **Consider** – Reduce ambiguity through hands‑on, security‑focused assets and transparent pricing.  
3. **Try** – Lower the activation barrier with resource‑boosts and guided prompting, ensuring the first experience is fast and successful.  
4. **Adopt** – Cement trust via enterprise‑grade governance, dedicated support, and reusable team templates.  
5. **Expand** – Turn satisfied users into advocates by extending the product’s modality, rewarding scale, and showcasing community success.

---  

**Key KPI Targets (Quarterly)**  

| KPI | Target |
|-----|--------|
| Impressions → Clicks (Aware) | 5 % |
| Qualified Leads (Consider) | 30 % |
| Trial Activation (Try) | 70 % |
| Trial → Paid Conversion (Adopt) | 25 % |
| Expansion Revenue (Expand) | +20 % YoY |
| NPS (Adopt) | ≥55 |
| Referral Rate (Expand) | ≥10 % |

These metrics will be tracked in the **Customer Success Dashboard** and fed back to product, engineering, and marketing for continuous improvement.