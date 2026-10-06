# Project guidance

Write 3–5 concrete bullets of your own and save as `AGENTS.md`. Combine related points where useful.
The instructions below are example ideas. Keep them relatively short and specific.

- Project and context: Implement `move_booking` in `service.py`. `Booking` is a reservation record. Records are held in a list in memory. Use `SPEC.md` for the agreed requirements.
- Preservation and scope: Preserve creation behaviour, the existing model and public function signatures. Keep `models.py`, `test_baseline.py`, `test_move_smoke.py`, `SPEC.md` and the fallback example unchanged. Do not weaken supplied checks. Preserve existing callers and behaviour. An optional parameter is acceptable if current calls still work.
- Checks: Run `uv run --python 3.12 python -m unittest -v test_baseline`, and `uv run --python 3.12 python -m unittest -v test_move_smoke` after changes.
- Review: Stop after the agreed implementation and show the changed files for review.
