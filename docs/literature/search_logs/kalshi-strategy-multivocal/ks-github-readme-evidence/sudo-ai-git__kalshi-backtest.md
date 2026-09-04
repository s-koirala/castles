# Kalshi Backtest — independent, honest prediction-market analysis

Rigorous backtester and data-pullers for Kalshi (the US CFTC-regulated
prediction-market exchange). Fully independent: pure Python + the public
Kalshi API. No paid keys, no LLM, no dependency on any trading-bot codebase.

The deliberate posture here is **honest statistics** — the point is to
test whether an edge actually exists, and to refuse to claim one when the
data can't support it. This is the discipline the code is written around:
every strategy is compared against correct baselines, every "edge" has a
confidence interval, and the headline finding is a negative one.

## The headline finding (from ~92,000 real settled markets)

Pulled and analyzed ~92,000 settled/closed Kalshi markets across the public
historical and live endpoints:

| Finding | Value |
|---|---|
| Direct single-event binary markets found | **136 (0.15% of sampled)** |
| Of those, clean YES/NO settlements | 61 |
| NO-tilt across a 30k settled sample | **97.1% settle NO** |
| Best candidate strategy (BUY_NO @ high-NO-prob) | +1.37% ROI, CI [1.13, 1.61], n=23 |

Three structural realities:

1. **Kalshi's settlement feed is ~99.9% multivariate/combo markets** right
   now. Direct single-event markets — the class most retail strategies
   target — are a vanishing fraction.
2. **The NO-tilt is massive** (97%) but it is an *artifact of multi-outcome
   event structure* (one YES, many NOs), not a signal. The correct null for
   any strategy is the **always-NO baseline**, and every candidate must beat
   it.
3. **No price-based strategy clears the honest bar.** The best candidate
   beats always-NO on point estimate but is statistically indistinguishable
   from it (n=23, CI overlaps). Favorites >> longshots (the classic
   favorite-longshot bias), but that bias is already priced in and eaten by
   fees/spread.

**Conclusion: there is no demostrable price-based edge in the public
settled-market data.** Any "guaranteed profit" claim on Kalshi is
fraud. A defensible model-based edge (forecast beats market) requires
forecast history and out-of-sample proof — which this public-data backtest
cannot fabricate.

## Files

- `pull_markets.py` — pull settled markets from the historical archive
- `pull_direct.py` — historical puller that filters direct markets as it goes
- `pull_large.py` — resume-safe incremental settled-market puller (JSONL)
- `pull_live_direct.py` — pull live `/markets` settled+closed, filter direct
- `backtest.py` — rigorous backtester (JSON input, baselines, bootstrap CIs)
- `backtest_jsonl.py` — rigorous backtester (JSONL input, price bands, verdict)
- `consolidate.py` — merge all pulls, structural finding, run backtest

## Methodology notes

- **Semantics (flat-bet, $1 face value per contract):** BUY YES @ p pays p,
  wins (1-p) on YES / loses p on NO; capital at risk = p. BUY NO @ p pays
  (1-p), wins p on NO / loses (1-p) on YES; capital at risk = 1-p.
- **Baselines:** always-YES and always-NO on the *same* universe. Because of
  the structural NO-tilt, always-NO is the meaningful null — beating it is
  required before any "edge" claim.
- **Confidence intervals:** bootstrap (resample with replacement) on per-bet
  ROI, so the verdict reports whether the CI excludes the baseline — not the
  point-estimate delta.
- **Favorite-longshot decomposition:** capital-weighted ROI by entry-price
  band, so a strategy that only "wins" at deep-longshot prices is exposed.
- **Wash/quote-artifact filter:** near-zero-price rows (`last_price < 1c`)
  dropped as they don't represent tradeable economics.

## Reproduce

```bash
# pull a fresh sample (takes a while; direct markets are sparse)
python3 pull_large.py 150000 400

# consolidate + backtest whatever has accumulated
python3 consolidate.py

# or run the backtester directly on a JSONL of markets
python3 backtest_jsonl.py <markets.jsonl>
```

Data artifacts (`*.json`, `*.jsonl`, `*.mftk`) are gitignored — the repo is
code + methodology, not a data dump.
