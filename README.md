# AI-Dev-Tasks × Codev — Hybrid Template

This repository gives you the **best of both worlds**:
- **ai-dev-tasks**: lightweight, prompt-first task scaffolding ([GitHub](https://github.com/snarktank/ai-dev-tasks))
- **codev (SP(IDE)R)**: context-first methodology with explicit phases ([GitHub](https://github.com/ansari-project/codev))

Use this template to kickstart AI-assisted development with **clarity, traceability, and speed**.

Follow **HowTo.md** For immediate usage.

---

## 📁 Repository Structure

```
.
├── README.md                      # This file
├── HowTo.md                       # Step-by-step setup guide
├── 0-FeatureDescription.md        # Template for new features
├── manifest.yaml                  # Project conventions
├── devflow.py                     # CLI task manager
│
├── prompts/                       # Setup prompts
│   ├── 1-Setup.md                # Repository setup
│   ├── 2-apply_SPIDER.md         # SP(IDE)R integration
│   ├── 3-Verify.md               # Usage verification
│   └── 4-Add_feature.md          # Feature workflow
│
├── ai-dev-tasks/                  # Prompt templates
│   ├── create-prd.md             # PRD generation
│   ├── generate-tasks.md         # Task list generation
│   └── process-task-list.md      # Task execution
│
└── codev/                         # SP(IDE)R phases
    ├── specs/                     # (S)pecify
    ├── plans/                     # (P)lan
    ├── impl/                      # (I)mplement
    ├── defend/                    # (D)efend
    ├── evaluate/                  # (E)valuate
    └── review/                    # (R)eview
```

---

## 🚀 Usage

### Step 1 — Setup (one-time)

```powershell
# Create virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Verify installation
python devflow.py --feature sample-feature --list
```

### Step 2 — Create a New Feature

```powershell
$Feature = "your-feature-name"

# Create folder structure
New-Item -ItemType Directory -Force -Path `
  ".\codev\specs\$Feature",`
  ".\codev\plans\$Feature",`
  ".\codev\impl\$Feature",`
  ".\codev\defend\$Feature",`
  ".\codev\evaluate\$Feature",`
  ".\codev\review\$Feature" | Out-Null

# Copy templates
Copy-Item ".\codev\specs\sample-feature\*" ".\codev\specs\$Feature\" -Force
Copy-Item ".\codev\plans\sample-feature\*" ".\codev\plans\$Feature\" -Force
Copy-Item ".\codev\defend\sample-feature\*" ".\codev\defend\$Feature\" -Force
Copy-Item ".\codev\evaluate\sample-feature\*" ".\codev\evaluate\$Feature\" -Force
Copy-Item ".\codev\review\sample-feature\*" ".\codev\review\$Feature\" -Force
```

### Step 3 — (S)pecify: Write PRD

**PROMPT:** Use `ai-dev-tasks/create-prd.md` with your AI assistant

Save output to: `codev/specs/<feature>/prd.md`

### Step 4 — (P)lan: Generate Tasks

**PROMPT:** Use `ai-dev-tasks/generate-tasks.md` with your PRD

Save output to: `codev/plans/<feature>/tasks.md`

**Required format:**
```markdown
- [ ] T1: Task title (phase: implement)
  - deps: <none or T0>
  - rationale: Brief explanation
```

### Step 5 — (I)mplement: Build Feature

```powershell
# See all tasks
python devflow.py --feature $Feature --list

# Pick next task (creates scratch file)
python devflow.py --feature $Feature --next
```

**PROMPT:** Use `ai-dev-tasks/process-task-list.md` for the task

```powershell
# Mark task complete
python devflow.py --feature $Feature --done T1
```

**Repeat** until all tasks are `[x]`

### Step 6 — (D)efend: Add Tests

Update: `codev/defend/<feature>/test_plan.md`
- Add test cases (valid, invalid, edge cases)
- Specify test framework (pytest, jest, etc.)
- Target >= 80% coverage

### Step 7 — (E)valuate: Run Tests

Record in: `codev/evaluate/<feature>/results.md`
- Date, commit, environment
- Pass/fail summary
- Decision: ✅ Accept / ❌ Rework

### Step 8 — (R)eview: Retrospective

Fill: `codev/review/<feature>/retrospective.md`
- What went well
- What to improve
- Action items
- Update `ai-dev-tasks/*.md` with lessons learned

---

## 🛠️ CLI Commands

```powershell
python devflow.py --feature <name> --list     # List tasks
python devflow.py --feature <name> --next     # Next task
python devflow.py --feature <name> --done T1  # Mark done
```

---

## 📦 Commit Convention

| Phase | Prefix | Example |
|-------|--------|---------|
| Specify | `spec:` | `spec(login): add PRD` |
| Plan | `plan:` | `plan(login): 8 tasks` |
| Implement | `impl:` | `impl(login): T2 auth` |
| Defend | `test:` | `test(login): unit tests` |
| Evaluate | `eval:` | `eval(login): all pass` |
| Review | `review:` | `review(login): retro` |

---

## 💡 Tips

- Keep tasks **atomic** (1-2 hours max)
- Write **tests before "done"**
- Commit **often** with clear messages
- Update **retrospectives** with actionable items

---

## 📚 Learn More

- **HowTo.md**: Complete workflow guide
- **prompts/**: Multi-stage setup instructions
- **manifest.yaml**: Customize conventions

---

## 📄 License

MIT
