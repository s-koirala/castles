# WTI Kalshi Backtest

A backtesting tool for evaluating a **NO-side betting strategy** on Kalshi's WTI crude oil range markets. The strategy identifies range brackets that are far from the current WTI spot price and have a high implied NO probability, then tracks whether those bets would have resolved in your favor.

---

## How It Works

At **2:20 PM ET** (just before Kalshi's WTI markets close), the script:

1. Reads the live WTI spot price
2. Looks at all active **"between" (range) markets** for that event
3. Filters to markets where the implied **NO probability ≥ threshold** (default: 97%)
4. Among qualifying markets, picks the one whose **midpoint is furthest from the current WTI price**
5. Records whether that bet resolved as NO (a win) or YES (a loss)

---

## Project Structure

```
.
├── wti_backtest.py       # Main backtest script
└── backtest_cache.json   # Input data (markets, candlesticks, WTI prices)
```

### `backtest_cache.json` Schema

```json
{
  "markets": [...],        // Kalshi market objects with strike_type, floor/cap, result, etc.
  "candlesticks": {...},   // Keyed as "TICKER_UNIXTIMESTAMP" → OHLC data in dollars
  "wti_prices": {...}      // ISO timestamp → WTI spot price
}
```

---

## Installation

No external dependencies — uses only the Python standard library.

```bash
git clone https://github.com/AjwaZainab/wti-kalshi-backtest.git
cd wti-kalshi-backtest
```

Requires **Python 3.7+**.

---

## Usage

```bash
# Basic run (uses backtest_cache.json in current directory)
python wti_backtest.py

# Custom data file
python wti_backtest.py --file path/to/your_cache.json

# Adjust NO probability threshold (e.g., 97%)
python wti_backtest.py --threshold 0.97

# Output raw JSON (useful for further analysis)
python wti_backtest.py --json
```

### Arguments

| Flag | Default | Description |
|------|---------|-------------|
| `--file` | `backtest_cache.json` | Path to the input cache JSON |
| `--threshold` | `0.97` | Minimum NO probability to qualify a market (0.0–1.0) |
| `--json` | `false` | Output results as JSON instead of formatted text |

---

## Sample Output

```
              WTI KALSHI BACKTEST — RESULTS
────────────────────────────────────────────────────────────────────────
  NO Probability Threshold : 97%
  Total Event Dates        : 42
  Events Bet               : 38
  Events Skipped (no bet)  : 4
────────────────────────────────────────────────────────────────────────
  Wins                     : 36
  Losses                   : 2
  WIN RATE                 : 94.7%
────────────────────────────────────────────────────────────────────────

Event                WTI @2:20  Bet Range        NO%   Dist  Result   Win?
────────────────────────────────────────────────────────────────────────
KXWTICMMAX-...       $  72.45   $65.00–$67.00    98%    6.5  no       ✓ WIN
...
```

---

## Strategy Logic

- **Market type:** Only `strike_type == "between"` (range) markets are considered.
- **NO probability:** Derived as `1 - yes_ask_close` from the candlestick's closing ask price.
- **Selection:** Among all qualifying ranges, the one **furthest from spot** is chosen — the assumption being that further-out ranges carry less risk of the price touching them before expiry.
- **Win condition:** The selected market resolves as `"no"`.

---

## Skipped Events

Events are skipped (no bet placed) when:
- No candlestick data is available for any market in the event
- No WTI spot price is available for the event's timestamp
- No market meets the minimum NO probability threshold

Skipped events are reported in the output with reasons.

