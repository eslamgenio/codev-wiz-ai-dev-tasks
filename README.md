# 🤖 AI-Dev-Tasks × Codev Hybrid Framework

> A unified AI-assisted development system that combines the lightweight prompt-driven workflow of **[ai-dev-tasks](https://github.com/snarktank/ai-dev-tasks)** with the structured, context-first **SP(IDE)R methodology** from **[Codev](https://github.com/ansari-project/codev)**.

---

## 🧠 Overview

This hybrid framework helps human + AI teams collaborate efficiently on software projects by combining:
- 🧩 **ai-dev-tasks:** task-oriented prompts for generating PRDs, breaking work down, and executing step-by-step.
- 🕸 **Codev:** a structured development lifecycle (Specify → Plan → Implement → Defend → Evaluate → Review) that keeps your project context, code, and reasoning synchronized.

Together they create a repeatable, traceable, and scalable AI-assisted development system.

---

## 🧱 Repository Structure
project-root/

│

├── README.md               # This documentation

├── manifest.yaml           # Project conventions and metadata

├── devflow.py              # CLI to manage tasks (--list, --next, --done)

├── ai-dev-tasks/           # Prompt templates for AI guidance

│   ├── create-prd.md

│   ├── generate-tasks.md

│   └── process-task-list.md

└── codev/                  # Codev SP(IDE)R structure

├── specs//prd.md

├── plans//tasks.md

├── impl//

├── defend//test_plan.md

├── evaluate//results.md

└── review//retrospective.md
