# Autonomous Mathematical Research Programme

This directory is the persistent coordination and memory layer for autonomous attempts on the repository's 100 open problems. It initializes problem 001 but contains no research attempt or claimed solution.

## Scope guard

Every writer operating under this programme may create or modify files only beneath `research/automated_attempts/` unless a later prompt explicitly expands that scope. In particular, `problems/`, the repository's main `README.md`, and other existing research files are read-only inputs.

## Layout

| Path | Purpose |
| --- | --- |
| `STATE.md` | Machine-readable coordination state, counters, bottleneck, and revision. |
| `QUEUE.md` | Canonical 001–100 queue derived from the repository problem index. |
| `NNN/PROGRESS.md` | Compact cumulative mathematical memory for problem `NNN`. |
| `NNN/attempts/` | Timestamped immutable research-attempt records. |
| `NNN/reviews/` | Timestamped immutable independent-review records. |
| `NNN/artifacts/` | Reproducible code, certificates, data, and supporting outputs. |

Use UTC names of the form `YYYYMMDDTHHMMSSZ-sol-NNN.md` for attempts and `YYYYMMDDTHHMMSSZ-astra-NNN.md` for reviews. Once committed, a run record is immutable: corrections go in a new record that cites the superseded one. Artifacts should use timestamped or content-addressed names and must be reproducible from documented commands.

## Evidence discipline

`PROGRESS.md` must keep the following categories separate:

1. VERIFIED RESULTS
2. PROMISING BUT UNPROVED CLAIMS
3. COMPUTATIONAL EVIDENCE
4. FAILED / EXHAUSTED ROUTES
5. CURRENT BOTTLENECK
6. NEXT HIGH-VALUE ATTACKS

A numerical experiment is never a proof. A plausible lemma remains unproved until every hypothesis and inference has been checked. A problem may move to `solved` or `counterexample` only after an independent review has verified a complete argument and its reproducible artifacts.

## Run and concurrency protocol

At the start of every run:

1. Read the current problem file, `QUEUE.md`, `STATE.md`, and that problem's `PROGRESS.md`.
2. Record the starting `revision`.
3. Perform one bounded role: a Sol research attempt or an Astra independent review.
4. Preserve the full run in a new immutable timestamped record and place reproducible outputs in `artifacts/`.
5. Compress only durable conclusions into `PROGRESS.md`; update `STATE.md` and, when appropriate, `QUEUE.md`.

Immediately before the final GitHub write, every writer must reread `STATE.md` from the target branch. If its `revision` differs from the starting value, the writer must incorporate the newer state and cumulative memory, recompute counters and next actions, and must not overwrite newer work. Prefer one atomic commit for the run. Every successful research or review run increments `revision` by exactly one; a failed or abandoned run does not advance it. The bootstrap state begins at revision 0.

## Programme status vocabulary

- `queued`: not yet started.
- `research`: active mathematical attack.
- `review`: independent verification in progress.
- `paused`: deliberately deferred with a recorded reason.
- `exhausted`: current high-value routes are exhausted; requires a new campaign.
- `solved`: a complete proof has passed independent verification.
- `counterexample`: a rigorous counterexample has passed independent verification.
