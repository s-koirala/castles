# Claude Code for Polymarket Bots

A comprehensive Claude Code configuration for building Polymarket prediction market trading bots. This project provides specialized agents, skills, and commands that enable Claude Code to research, scaffold, and audit trading bots with deep knowledge of Polymarket's APIs.

## What This Project Does

This is a **Claude Code configuration project** - it enhances Claude Code with:

- **Specialized Agents**: Research and implementation agents with Polymarket domain expertise
- **Skills**: On-demand knowledge modules (fee calculations, crypto market mechanics)
- **Commands**: Workflow automation for bot creation, auditing, and verification

When you use Claude Code in this directory, it gains the ability to build complete, working Polymarket trading bots through a structured research → scaffold → audit pipeline.

## Quick Start

1. **Install Claude Code** if you haven't already:
   ```bash
   npm install -g @anthropic-ai/claude-code
   ```

2. **Clone this repository**:
   ```bash
   git clone https://github.com/your-username/claude-for-polymarket-bots.git
   cd claude-for-polymarket-bots
   ```

3. **Start Claude Code**:
   ```bash
   claude
   ```

4. **Create your first bot**:
   ```
   /create_single_strategy_bot market_maker
   ```

## Available Commands

| Command | Description |
|---------|-------------|
| `/create_single_strategy_bot` | Create a complete trading bot (market_maker, arbitrage, spike_detector, or custom) |
| `/verify_changes` | Verify code changes work by creating and running test scripts |
| `/audit_logic` | Deep, skeptical audit of code paths and logic |
| `/check_concern` | Evaluate whether a specific concern about code behavior is valid |
| `/create_implementation_plan` | Create detailed implementation plans through interactive research |
| `/execute_plan` | Execute a pre-written implementation plan using coordinated subagents |
| `/research_codebase` | Research codebase comprehensively using parallel sub-agents |

## Supported Trading Strategies

### Preset Strategies

| Strategy | Description |
|----------|-------------|
| `market_maker` | Two-sided quotes around midpoint to capture spread |
| `arbitrage` | Exploit YES + NO pricing inefficiencies (when sum ≠ $1.00) |
| `spike_detector` | React to sudden price movements |

### Custom Strategies

Describe any strategy in natural language:
```
/create_single_strategy_bot "buy when price drops 10% in 5 minutes"
/create_single_strategy_bot custom
```

Claude will interrogate you to fully understand your strategy before implementation.

## Skills

Skills provide specialized knowledge that Claude can invoke on-demand:

| Skill | When It's Used |
|-------|----------------|
| `crypto-short-term-markets` | Research BTC/ETH/SOL 15-minute and 1-hour prediction markets |
| `polymarket-fee-knowledge` | Fee calculations, maker rebates, break-even analysis for 15-min crypto markets |
| `context-optimizer` | Optimize context window before compaction |

### Fee Knowledge Highlights

15-minute crypto markets (BTC, ETH, SOL, XRP) are the **only** Polymarket markets with fees:

| Role | Fee |
|------|-----|
| Maker | 0% + rebates |
| Taker | Up to ~3% at 50% price |

Fee formulas:
- **Selling**: `feeQuote = baseRate × min(price, 1-price) × size` (USDC)
- **Buying**: `feeBase = baseRate × min(price, 1-price) × (size/price)` (tokens)

## Specialized Agents

This configuration includes 30+ specialized agents for research and implementation:

### Research Agents
- `polymarket-researcher` - Polymarket APIs, trading strategies, best practices
- `news-researcher` / `news-researcher-lite` - Current news and developments
- `financial-markets-researcher` - Market indicators, asset prices, derivatives
- `social-media-researcher` - Sentiment analysis, viral discussions
- `expert-opinion-researcher` - Think tank reports, analyst opinions
- `contrarian-researcher` - Devil's advocate finding counter-arguments
- `historical-precedent-researcher` - Past events and base rates
- `data-researcher` - Statistics, polls, prediction market odds
- `technical-researcher` - Code snippets, official documentation

### Implementation Agents
- `polymarket-bot-scaffolder` - Creates complete bot project structures
- `polymarket-bot-auditor` - Comprehensive bot auditing against specifications
- `codebase-analyzer` - Analyzes implementation details
- `logic-auditor` - Deep, skeptical audit of code logic
- `change-verifier` - Creates and runs verification scripts
- `plan-executor` - Executes implementation phases

## How Bot Creation Works

The `/create_single_strategy_bot` command follows a structured pipeline:

```
1. Parse Strategy Input
   ↓
2. Interrogate (custom strategies only)
   ↓
3. Confirm Understanding with User
   ↓
4. Write Strategy Spec to thoughts/
   ↓
5. Invoke Crypto Markets Skill (if applicable)
   ↓
6. Spawn Research Agent → writes findings
   ↓
7. Spawn Scaffolder Agent → creates bot files
   ↓
8. Spawn Auditor Agent → verifies implementation
   ↓
9. Present Results
```

All context passes through markdown files in `thoughts/shared/polymarket-bot-specs/`.

## Project Structure

```
.claude/
├── agents/           # 30+ specialized agent configurations
│   ├── polymarket-researcher.md
│   ├── polymarket-bot-scaffolder.md
│   ├── polymarket-bot-auditor.md
│   └── ...
├── commands/         # Slash command definitions
│   ├── create_single_strategy_bot.md
│   ├── verify_changes.md
│   └── ...
├── skills/           # On-demand knowledge modules
│   ├── crypto-short-term-markets/
│   ├── polymarket-fee-knowledge/
│   └── context-optimizer/
└── settings.local.json

thoughts/             # Working directory for agent context
└── shared/
    └── polymarket-bot-specs/
        ├── {timestamp}-{strategy}.md
        └── {timestamp}-{strategy}-research.md

polymarket-bots/      # Generated bots are created here
└── {strategy-slug}/
    ├── bot.py
    ├── config.py
    ├── requirements.txt
    └── .env.example
```

## Polymarket API Knowledge

The configuration includes deep knowledge of Polymarket's APIs:

| API | Purpose | Auth |
|-----|---------|------|
| **Gamma API** (`gamma-api.polymarket.com`) | Market discovery, metadata | None |
| **CLOB API** (`clob.polymarket.com`) | Trading, orderbooks, prices | L1/L2 |
| **Data API** (`data-api.polymarket.com`) | Positions, trade history | Required |

### Rate Limits

| Endpoint | Limit (per 10s) |
|----------|-----------------|
| POST /order | 3,500 burst |
| DELETE /order | 3,000 burst |
| Market data | 1,500 |
| General | 9,000 |

## Requirements

- [Claude Code](https://docs.claude.ai/claude-code) CLI
- Python 3.9+ (for generated bots)
- Polymarket account with API credentials

## Generated Bot Dependencies

Bots created by this configuration use:
- `py-clob-client` - Official Polymarket Python SDK
- `python-dotenv` - Environment configuration
- Standard libraries for logging, scheduling, etc.

## Safety Notes

- Generated bots include `.env.example` files - never commit real credentials
- All strategies include risk management parameters
- Test with small amounts before production use
- The auditor agent verifies implementation matches specification

## License

MIT