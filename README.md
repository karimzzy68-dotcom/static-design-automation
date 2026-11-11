# Static Design Automation

**An agent-driven production pipeline for static ads. It turns a brand brief and product photos into batches of 100–150 reviewed ad creatives, with saved prompts, quality-check records and runs that can be resumed if interrupted.**

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Pillow](https://img.shields.io/badge/Pillow-12-blue)
![Whisper](https://img.shields.io/badge/faster--whisper-video%20lessons-FF6F00)
![Agents](https://img.shields.io/badge/Agents-Codex%20%7C%20Antigravity%20%7C%20Claude-black)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![CI](https://github.com/karimzzy68-dotcom/static-design-automation/actions/workflows/ci.yml/badge.svg)

---

## Key Architecture & Features

- **Batch state machine** (`tools/design_system.py`, about 330 lines, no outside dependencies): a CLI covers `init-product → add-asset → new-batch → prepare → start → record-output → qa → handoff → gallery`. Every batch has a JSON manifest with an event log, so any agent can pick up exactly where the last one stopped.
- **Multi-agent safety:** a batch is locked while one agent works on it (`claim` / `release`), and locks belong to their owner. Different batches can run in parallel without colliding.
- **Reference isolation:** product photos and inspiration images are content-hashed (SHA-256) and indexed per product, so references for one brand never mix with another's.
- **Copy quality checks** (`tools/creative_standards.py`): before a concept can move on, it must state its direct or indirect marketing angle, name at least five distinct hooks, fill in fields for audience insight, objection and proof, and include a concrete design spec. Fields left as template placeholders are rejected.
- **Plan audit** (`tools/audit_plan.py`): finds missing strategy fields and repeated scenes across a batch before any image is generated.
- **Concept counting:** "N designs" counts distinct concepts. Resizes and format exports are tracked separately, so totals aren't inflated.
- **Review gallery:** each batch builds its own HTML gallery of finished work for client review.
- **Video learning library** (`tools/ingest_videos.py`, `tools/video_library.py`): turns training videos into timestamped transcripts (faster-whisper), screenshots every 30 seconds and contact sheets. Lessons are linked back to their source timestamps.
- **Works across agents:** shared instructions (`WORKFLOW.md`, `CREATIVE-STANDARDS.md`) and a reusable skill (`.agents/skills/static-design-system/SKILL.md`) let Codex, Antigravity and Claude Code all run the same workflow.
- **Self-verification** (`tools/verify_system.py`): checks reference isolation, resumability, lock ownership and final-file integrity in a temporary workspace.

## Tech Stack

| Area | Technology |
| --- | --- |
| Core | Python 3.10+ standard library (argparse, json, hashlib, pathlib) |
| Imaging | Pillow |
| Video ingest | faster-whisper, OpenCV, imageio-ffmpeg |
| Generation | Whatever image tool the active agent has (no vendor lock-in) |
| Output | Static HTML galleries, PNG/WebP exports, ZIP bundles |

## Quickstart

```bash
git clone https://github.com/karimzzy68-dotcom/static-design-automation.git
cd static-design-automation
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install pillow                                  # core
pip install -r requirements-video.txt               # optional: video lessons

python tools/design_system.py --help
python tools/verify_system.py                       # self-test
```

A typical run:

```bash
python tools/design_system.py init-product --brand acme --product hydration-mix --url https://acme.example
python tools/design_system.py add-asset    --brand acme --product hydration-mix --file pack.png --kind product
python tools/design_system.py new-batch    --brand acme --product hydration-mix --batch launch-01 --count 20
python tools/audit_plan.py brands/acme/products/hydration-mix/batches/launch-01/manifest.json
python tools/design_system.py next         --brand acme --product hydration-mix --batch launch-01
python tools/design_system.py gallery      --brand acme --product hydration-mix --batch launch-01
```

Or open the folder in a coding agent and ask: *"Make 10 premium static ads for Acme Hydration Mix using the saved references."*

> Brand assets, client deliverables and third-party reference images are deliberately left out of this repo. `brands/` is created locally when you run the tools.

## License

MIT. See [LICENSE](LICENSE).
