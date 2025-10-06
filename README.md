# AI-Dev-Tasks × Codev — Hybrid Template

This repository gives you the **best of both worlds**:
- **ai-dev-tasks**: lightweight, prompt-first task scaffolding (https://github.com/snarktank/ai-dev-tasks)
- **codev (SP(IDE)R)**: context-first methodology with explicit phases (https://github.com/ansari-project/codev)

Use this template to kickstart AI-assisted development with **clarity, traceability, and speed**.

---

## Structure

```
.
├── README.md
├── manifest.yaml
├── devflow.py
├── ai-dev-tasks/
│   ├── create-prd.md
│   ├── generate-tasks.md
│   └── process-task-list.md
└── codev/
    ├── specs/
    │   └── sample-feature/
    │       └── prd.md
    ├── plans/
    │   └── sample-feature/
    │       └── tasks.md
    ├── impl/
    │   └── sample-feature/
    │       └── .keep
    ├── defend/
    │   └── sample-feature/
    │       └── test_plan.md
    ├── evaluate/
    │   └── sample-feature/
    │       └── results.md
    └── review/
        └── sample-feature/
            └── retrospective.md
```

### How to use
1. **Specify** → Edit `codev/specs/<feature>/prd.md` (use `ai-dev-tasks/create-prd.md` as the prompt).
2. **Plan** → Generate and refine `codev/plans/<feature>/tasks.md` (using `ai-dev-tasks/generate-tasks.md`).
3. **Implement** → Work through tasks with `ai-dev-tasks/process-task-list.md`. Commit code & notes under `codev/impl/<feature>/`.
4. **Defend** → Add tests & defensive checks to `codev/defend/<feature>/test_plan.md`.
5. **Evaluate** → Record results in `codev/evaluate/<feature>/results.md`.
6. **Review** → Summarize lessons in `codev/review/<feature>/retrospective.md` and update `manifest.yaml`.

### Quick Start (recommended flow with an LLM IDE)
- Open `ai-dev-tasks/create-prd.md`, copy the template into your IDE (Cursor/VS Code + ChatGPT/Claude).
- Paste your feature idea → generate PRD → save into `codev/specs/<feature>/prd.md`.
- Open `ai-dev-tasks/generate-tasks.md`, feed it your PRD → produce a task list → save under `codev/plans/<feature>/tasks.md`.
- Use `devflow.py` to pick and log the next pending task and create a scratch file.
  ```bash
  python devflow.py --feature sample-feature --next
  ```

---

## Tips
- Keep PRDs concise but **explicit** (requirements, done rules, constraints).
- Treat tasks as **atomic**. If too big, split them before implementation.
- Enforce **tests before done** in the Defend/Evaluate phases.
- After Review, **improve the prompts** in `ai-dev-tasks/*` with lessons learned.

## License
MIT
