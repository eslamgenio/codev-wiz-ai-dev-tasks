Once the repo is generated , here’s a crisp, no-fluff plan to start using it.

# 1) Verify it runs (once)

```powershell
# from repo root
python -m venv .venv
. .\.venv\Scripts\Activate.ps1

python devflow.py --feature sample-feature --list
python devflow.py --feature sample-feature --next
python devflow.py --feature sample-feature --done T1
```

If those three work, the scaffold is good.

# 2) Create your real feature

```powershell
$Feature = "login"   # change me
# quick scaffold (copy from sample)
New-Item -ItemType Directory -Force -Path ".\codev\specs\$Feature",".\codev\plans\$Feature",".\codev\impl\$Feature",".\codev\defend\$Feature",".\codev\evaluate\$Feature",".\codev\review\$Feature" | Out-Null
Copy-Item ".\codev\specs\sample-feature\prd.md" ".\codev\specs\$Feature\prd.md" -Force
Copy-Item ".\codev\plans\sample-feature\tasks.md" ".\codev\plans\$Feature\tasks.md" -Force
Copy-Item ".\codev\defend\sample-feature\test_plan.md" ".\codev\defend\$Feature\test_plan.md" -Force
Copy-Item ".\codev\evaluate\sample-feature\results.md" ".\codev\evaluate\$Feature\results.md" -Force
Copy-Item ".\codev\review\sample-feature\retrospective.md" ".\codev\review\$Feature\retrospective.md" -Force
```

# 3) Write the PRD (Specify)

* Open `codev/specs/<feature>/prd.md`.
* Use the prompt in `ai-dev-tasks/create-prd.md` with your AI IDE to fill it.
* Keep acceptance criteria concrete (Given/When/Then).

# 4) Generate the task list (Plan)

* Use `ai-dev-tasks/generate-tasks.md` on your PRD.
* Paste the result into `codev/plans/<feature>/tasks.md`.
* Ensure each line follows this format (the CLI depends on it):

  ```
  - [ ] T1: Short title (phase: implement)
  ```

# 5) Work in small loops (Implement → Defend → Evaluate)

```powershell
# show backlog
python devflow.py --feature $Feature --list

# create scratch file for the next unchecked task
python devflow.py --feature $Feature --next
```

* Open the created file in `codev/impl/<feature>/T<ID>_<timestamp>.md`.
* In your AI chat, paste `ai-dev-tasks/process-task-list.md` and the Task ID.
* Do ONLY that task:

  * Implement the minimal code
  * Add/adjust tests (update `codev/defend/<feature>/test_plan.md`)
  * Run tests and log outcomes in `codev/evaluate/<feature>/results.md`
* When done:

```powershell
python devflow.py --feature $Feature --done T<ID>
```

Repeat `--next` → implement/test/evaluate → `--done` until the list is finished.

# 6) Review (Retro)

* Fill `codev/review/<feature>/retrospective.md` (what went well, improvements).
* If prompts need tweaks, improve `ai-dev-tasks/*.md`.

# 7) Commit in meaningful slices

```powershell
git init
git checkout -b feat/$Feature
git add .
git commit -m "spec($Feature): PRD + initial tasks"
# during loops
git commit -m "impl($Feature): T2 core logic + unit tests"
git commit -m "eval($Feature): test results + notes"
git commit -m "review($Feature): retro + prompt improvements"
```

# 8) (Optional) Push and PR

```powershell
git remote add origin https://github.com/<you>/<repo>.git
git push -u origin feat/$Feature
# open a PR when the feature cycle is green
```

# 9) Plug in your real test runner

Pick what matches your stack and reference it in `defend/test_plan.md`:

* Python: `pytest`
* Node: `vitest`/`jest`
* Android/Kotlin: `JUnit` + `Robolectric`, instrumented tests via Gradle

Record how to run them in `evaluate/results.md` (exact commands + pass/fail summary).

# 10) Definition of Done (for each feature)

* PRD matches implemented behavior
* All tasks in `plans/<feature>/tasks.md` are `[x]`
* Tests exist and pass locally
* `evaluate/results.md` shows green results
* Retro written, prompts improved if needed

# Pitfalls to avoid

* **Task sprawl:** if a task is >2h, split it before coding.
* **Skipping tests:** “Done” requires tests + results.
* **Breaking format:** keep `- [ ] T<ID>:` lines exact; the CLI relies on it.
