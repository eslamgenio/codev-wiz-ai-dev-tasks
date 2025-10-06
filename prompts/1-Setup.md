You are my AI pair-developer and project orchestrator.

Your job: 
1. Create and configure the full **ai-dev-tasks × Codev hybrid repository** on my local workspace.  
2. Explain commands as comments inside the files.  
3. Ensure everything works on **Windows PowerShell**.

Codev repo: @https://github.com/ansari-project/codev
ai-dev-tasks repo: @https://github.com/snarktank/ai-dev-tasks


---

## 🧭 Objective
Combine:
- **ai-dev-tasks** → lightweight prompt templates (create-prd.md, generate-tasks.md, process-task-list.md)
- **Codev (SP(IDE)R)** → context-first structure (Specify, Plan, Implement, Defend, Evaluate, Review)

I want:
✅ complete folder structure  
✅ all markdown templates  
✅ a helper CLI (`devflow.py`)  
✅ a diagram (Mermaid) in README.md  
✅ step-by-step PowerShell usage instructions  

---

## 🏗️ Folder Layout
```

project-root/
│
├── README.md
├── manifest.yaml
├── devflow.py
├── ai-dev-tasks/
│   ├── create-prd.md
│   ├── generate-tasks.md
│   └── process-task-list.md
└── codev/
├── specs/
│   └── sample-feature/prd.md
├── plans/
│   └── sample-feature/tasks.md
├── impl/sample-feature/.keep
├── defend/sample-feature/test_plan.md
├── evaluate/sample-feature/results.md
└── review/sample-feature/retrospective.md

```

---

## 🧩 Behavior Expected
- **create-prd.md** → generate Product Requirement Doc (PRD)
- **generate-tasks.md** → produce task list (`tasks.md`)
- **process-task-list.md** → run one task loop: plan → implement → test → evaluate → summarize
- **devflow.py**:
  - `--list` → show tasks
  - `--next` → create scratch file for next pending task
  - `--done <ID>` → mark a task done in `tasks.md`

---

## ⚙️ Steps Claude should perform
1. **Create folders and files** above with correct content.  
2. Add detailed **PowerShell guide** to README:  
   - how to create a new feature (`New-Feature` PowerShell function)  
   - how to use the CLI (`--list`, `--next`, `--done`)  
3. Include **Mermaid diagram** showing ai-dev-tasks ↔ Codev flow.  
4. Ensure all Markdown uses Git-friendly line endings (LF).  
5. Write clear comments at top of every script file.  
6. Configure `.gitignore` for `__pycache__`, `.venv`, and scratch files.  

---

## 🧠 Usage Flow (Claude must include this in README)
1. `python -m venv .venv; .\.venv\Scripts\Activate.ps1`
2. `python devflow.py --feature login --list`
3. `python devflow.py --feature login --next`
4. Run `process-task-list.md` prompt in AI chat using that Task ID  
5. Save results to `codev/impl/...` and mark done:  
   `python devflow.py --feature login --done T1`
6. Add tests → evaluate → review.  

---

## 🔒 Rules
- No external dependencies (pure Python + Markdown).  
- All templates must use Markdown headings (### etc.).  
- Make filenames and task IDs human-readable.  
- Add inline comments explaining what each file does.  
- Make sure `devflow.py` runs fine on Windows PowerShell.

---

## 🧭 Deliverable
When done, I expect:
- a working local repo ready to commit  
- a README.md containing:
  - usage guide
  - PowerShell commands
  - Mermaid diagram
  - workflow summary table
  - contribution notes