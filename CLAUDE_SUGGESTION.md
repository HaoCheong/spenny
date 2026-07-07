# Claude Suggestions

---

## [2026-05-27] `run_update` in `backend/app/operations.py`

### Structural

**1. Move operation dispatch into the `Operation` class hierarchy**
`run_update` imports `TranferMoneyOperation` just to decide how `apply` is called. Every new operation type requires a change here. Each `Operation` subclass should know how to apply itself — ideally `op.apply(db, db_event)` handles its own bucket fetching internally.

**2. Add an `advance()` method to `TimedTrigger`**
Advancing the trigger date is trigger domain logic and shouldn't live in a standalone helper. A `TimedTrigger.advance()` method that returns a `model_copy` with the updated date would replace `event_freq_adder`, the `model_copy` call, and the associated PFIX comment.

### Readability

**3. Use `res.data` instead of `res["data"]`**
`get_events_by_date_range` returns an `EventAllRead` Pydantic model — dict-style access is fragile and non-obvious.

**4. Move sort outside the loop**
`to_process.sort(...)` runs every iteration even when nothing was re-appended. Sort once before the loop and only re-sort after an append.

**5. Remove the redundant `db.add(db_event)`**
`db_event` is already tracked by the session since it was fetched from it. The call is misleading.

**6. Clean up dead code and noise**
- Remove commented-out debug prints (lines 60–61)
- Resolve or remove `# PFIX` comments
- Remove unused imports: `true` from sqlalchemy, `Event`, `EventReadNR`, `TimedTrigger`
