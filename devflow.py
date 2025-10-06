#!/usr/bin/env python3
# A tiny helper to move through the hybrid flow.
# - Lists tasks for a feature
# - Picks the next pending task
# - Creates a scratch file for the task under impl/

import argparse, sys, pathlib, re, datetime

ROOT = pathlib.Path(__file__).parent
CODEV = ROOT / "codev"

def read_tasks(feature: str):
    path = CODEV / "plans" / feature / "tasks.md"
    if not path.exists():
        print(f"[!] tasks file not found: {path}")
        sys.exit(1)
    text = path.read_text(encoding="utf-8")
    # Simple task format: "- [ ] TID: Title"
    items = []
    for m in re.finditer(r"^- \[( |x)\]\s*(?P<id>[A-Za-z0-9_-]+):\s*(?P<title>.+)$", text, flags=re.M):
        items.append({
            "done": (m.group(1) == "x"),
            "id": m.group("id").strip(),
            "title": m.group("title").strip()
        })
    return text, items, path

def pick_next_pending(items):
    for it in items:
        if not it["done"]:
            return it
    return None

def create_scratch(feature: str, task):
    scratch_dir = CODEV / "impl" / feature
    scratch_dir.mkdir(parents=True, exist_ok=True)
    ts = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    fname = f"{task['id']}_{ts}.md"
    path = scratch_dir / fname
    path.write_text(f'''# Scratch: {task['id']} — {task['title']}

## Context
- Feature: {feature}
- Created: {ts}

## Plan for this task
- [ ] Approach
- [ ] Edge cases
- [ ] Dependencies

## Work log
- Notes here...

## Checklist
- [ ] Code implemented
- [ ] Tests added/updated
- [ ] Docs updated
- [ ] PR created
''', encoding="utf-8")
    return path

def mark_done(tasks_text, path, task_id):
    new = re.sub(rf"^- \[ \]\s*{re.escape(task_id)}:", f"- [x] {task_id}:", tasks_text, count=1, flags=re.M)
    path.write_text(new, encoding="utf-8")
    print(f"[+] Marked done: {task_id}")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--feature", required=True, help="Feature name (e.g., sample-feature)")
    ap.add_argument("--list", action="store_true", help="List tasks")
    ap.add_argument("--next", action="store_true", help="Create scratch for next pending task")
    ap.add_argument("--done", help="Mark a task id as done")
    args = ap.parse_args()

    tasks_text, items, path = read_tasks(args.feature)

    if args.list:
        for it in items:
            mark = "x" if it["done"] else " "
            print(f"- [{mark}] {it['id']}: {it['title']}")
        return

    if args.next:
        nx = pick_next_pending(items)
        if not nx:
            print("[i] No pending tasks 🎉")
            return
        sp = create_scratch(args.feature, nx)
        print(f"[+] Created scratch: {sp}")
        print("   Use this file to plan/implement, then run --done <id> when finished.")
        return

    if args.done:
        mark_done(tasks_text, path, args.done)
        return

    ap.print_help()

if __name__ == "__main__":
    main()
