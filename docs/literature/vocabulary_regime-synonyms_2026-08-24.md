---
title: "Term registry: market-state and market-structure vocabulary for the regime-definitions recall sweep"
slug: regime-naming
date: 2026-08-24
artifact_type: vocabulary-registry (Stage 1-2 of a search-strategy build; NOT a literature review, NOT an evidence corpus)
objective: "Harvest, beyond the user-supplied seed list, every locatable synonym family for market state / market structure vocabulary, with per-term provenance and systematic morphological variants, so that the later evidence sweep's phrase queries are seeded empirically rather than from academic state-terms alone."
motivating_failures:
  - "The 59-definition regime-definitions survey (lit_review_regime-definitions_2026-08-21.md) under-recalled because its query vocabulary was seeded from academic state-terms; its own section 8.2 shows the practitioner vocabulary (range, compression, transition) has almost no peer-reviewed base reachable by those terms."
  - "F005: the plural phrase 'supports and resistances' defeated the phrase query 'support and resistance' - morphological variants defeat phrase queries, twice documented in this project."
ai_assistance: "Claude Fable 5 (model id claude-fable-5; Claude Code / Claude Agent SDK, research-librarian agent, vocabulary-harvest dispatch) executed every fetch, extracted every term, and drafted this registry. Single compiler; no human second harvester."
git_head_at_authoring: "0845acb"
materials_availability:
  - docs/literature/search_logs/regime-naming/
---

# Term registry: market-state and market-structure vocabulary

## 1. Methods

### 1.1 What this artifact is and is not

This registry is the **instrument** a later sweep will execute. It contains no
evidence queries, no screening decisions, and no eligibility judgments. A term's
presence here asserts only that the term **exists in a tradition and was
harvested from a stated source on 2026-08-24** - never that the construct it
names is real, testable, or well-defined. Harvest provenance is recorded per
term; tier-5 sources are admissible **for vocabulary provenance only**, per the
dispatch directive, and nothing cited here may be re-cited as evidence.

### 1.2 Harvest sources (all executed 2026-08-24; one log per fetch under [search_logs/regime-naming/](search_logs/regime-naming/))

| arm | source | log(s) |
|---|---|---|
| Included-record keywords | The five predecessor reviews: [regime-definitions](lit_review_regime-definitions_2026-08-21.md) (§§8.1-8.8), [level-definitions](lit_review_level-definitions_2026-08-21.md) (§§8.1-8.6), [regime-classification](lit_review_regime-classification_2026-08-21.md) (§§8.5-8.6), [regime-method-gaps](lit_review_regime-method-gaps_2026-08-21.md) (§8), [f005-class-n-tests](lit_review_f005-class-n-tests_2026-08-21.md) (§9) | `vh-included-01.json` |
| Practitioner taxonomies | Edwards & Magee *Technical Analysis of Stock Trends* 11th ed. TOC (GBV/ZBW library scan); Murphy *Technical Analysis of the Financial Markets* TOC (archive.org full text); Kaufman *Trading Systems and Methods* TOC (Wiley Online Books, doi:10.1002/9781119202561); Wyckoff method (StockCharts ChartSchool tutorial); Market Profile glossaries (WindoTrader index; CQG IC help) | `vh-practitioner-01..06.json`, locator queries in `vh-websearch-01.json` |
| Encyclopedia synonym graphs | English Wikipedia redirect sets for Market trend, Support and resistance, Breakout, Market sentiment, Volatility, Consolidation (business), Market Profile, Price discovery (MediaWiki API) | `vh-wikipedia-01..08.json` |
| OpenAlex concepts/keywords | `api.openalex.org/works/doi:{doi}` for 8 central DOIs of the predecessor corpora (Hamilton 1989; Pagan & Sossounov 2002; Lunde & Timmermann 2004; Münnix et al. 2012; Garzarelli et al. 2014; Driessen et al. 2013; Huddart et al. 2009; Mizrach & Weerts 2009) | `vh-openalex-01..08.json` |
| Methodology-citation verification | DOI Handle System API + Crossref | `vh-doicheck-01.json` |

**Source codes used in the registry table.** SEED = user-supplied seed list;
IR-RD / IR-LD / IR-RC / IR-MG / IR-F5 = included-record vocabulary of the
regime-definitions / level-definitions / regime-classification /
regime-method-gaps / f005 reviews; PT-EM / PT-MU / PT-KF / PT-WY / PT-MP =
practitioner taxonomies (Edwards & Magee / Murphy / Kaufman / Wyckoff-StockCharts
/ Market Profile glossaries); WP-nn = Wikipedia redirect log nn; WS = locator-query
snippet vocabulary (`vh-websearch-01.json`). Multiple codes mean multiple
independent attestations.

### 1.3 Methodology citations (all verified against Crossref + DOI handle API, responseCode 1; log `vh-doicheck-01.json`)

- **Search-strategy peer review**: McGowan J, Sampson M, Salzwedel DM, Cogo E,
  Foerster V, Lefebvre C. PRESS Peer Review of Electronic Search Strategies:
  2015 Guideline Statement. *J Clin Epidemiol*. 2016;75:40-46.
  [doi:10.1016/j.jclinepi.2016.01.021](https://doi.org/10.1016/j.jclinepi.2016.01.021) — **VERIFIED**.
  PRESS element 3 (subject headings) and element 4 (text-word searching: "search
  strategy misses spelling variants, synonyms, antonyms or related terms") are
  the guideline warrant for this registry existing at all.
- **Pearl growing**: Schlosser RW, Wendt O, Bhavnani S, Nail-Chiwetalu B. Use of
  information-seeking strategies for developing systematic reviews and engaging
  in evidence-based practice: the application of traditional and comprehensive
  Pearl Growing. A review. *Int J Lang Commun Disord*. 2006;41(5):567-582.
  [doi:10.1080/13682820600742190](https://doi.org/10.1080/13682820600742190) — **VERIFIED**.
  The included-record arm (harvesting terms from records the predecessor corpora
  already caught) is comprehensive pearl growing in this paper's sense. The
  dispatch's other candidate, Hartley et al. 1990 (*Online Searching: Principles
  and Practice*), is a textbook with **no DOI of its own** - only a book review
  (doi:10.3233/efi-1990-8308) is indexed - and is therefore not cited as the
  primary.
- **Term harvesting / objectively derived strategies**: Hausner E,
  Waffenschmidt S, Kaiser T, Simon M. Routine development of objectively derived
  search strategies. *Syst Rev*. 2012;1:19.
  [doi:10.1186/2046-4053-1-19](https://doi.org/10.1186/2046-4053-1-19) — **VERIFIED**.
  Warrant for deriving query terms from a known relevant-record set (here, the
  five predecessor corpora) rather than from the searcher's own vocabulary.

### 1.4 Morphological-variant policy

Every row lists variants generated systematically over four axes, because two
documented in-project failures (F005; the regime-definitions §8.2 finding)
were morphological: (a) singular/plural on **both** nouns of a compound
("supports and resistances"); (b) hyphenation and closed/open compounds
(range-bound / range bound; break-out / breakout); (c) word-order and
part-of-speech permutation (trading range / range trading / ranging market);
(d) verb/noun/adjective forms (consolidate / consolidation / consolidating).
Variants are listed only where the surface form actually changes token content
- trivial plural-in-s variants are marked "+s" rather than spelled out.

### 1.5 An informative negative: no controlled vocabulary exists

The OpenAlex arm shows that concept/keyword tagging for the eight central DOIs
carries **almost none of this vocabulary**: the tags are generic ("Econometrics",
"Financial market", "Business cycle", "Random walk", "Technical analysis",
"Anchoring"); the closest topic string is "Market Dynamics and Volatility". No
concept exists for trading range, support/resistance, accumulation, balance, or
any practitioner state term. Consequence for the sweep: **there is no controlled
vocabulary to lean on** (contrast MeSH in medicine; cf. Cochrane Handbook ch. 4
on combining controlled vocabulary with free text) - free-text phrase queries
over this registry's variants are the only instrument available, which is why
variant completeness is load-bearing.

## 2. The registry

Type: **S** = spatial (a construct on the price axis), **T** = temporal (a state
of an interval of time), **B** = both/either.

### 2.1 "Regime"-word synonyms (the state-noun itself)

| term | tradition | family | type | morphological variants | source |
|---|---|---|---|---|---|
| regime | academic econometrics | regime-noun | T | regime(s), market regime(s), regime shift/change/switch, regime-switching / regime switching | SEED; IR-RD; IR-RC |
| state | academic econometrics; econophysics | regime-noun | T | state(s), market state(s), state of a/the (financial) market, hidden/latent state. COLLISION: exchange session-protocol "market state" / "Limit State" / "Trading Pause" (IR-RD §8.2 item 13) | SEED; IR-RD |
| phase | business-cycle; Wyckoff | regime-noun | T | phase(s), market phase, cycle phase, expansionary/contractionary phase, Phase A-E (Wyckoff) | SEED; IR-RD; PT-WY |
| mode | intrinsic-time; control/econometrics | regime-noun | T | mode(s), up mode / down mode, market mode, mode transition | SEED; IR-RD (D54) |
| environment | practitioner/allocator | regime-noun | T | environment(s), market environment, macro environment | SEED |
| condition | academic (Fabozzi-Francis lineage) | regime-noun | T | condition(s), market condition(s), bull/bear market conditions | SEED; IR-RD (D01-05 lineage) |
| episode | academic | regime-noun | T | episode(s), volatile episode, crisis episode | SEED |
| period | academic | regime-noun | T | period(s), turbulent/quiet periods, calm/crisis period | IR-RD (D36-38, q-crossref-17) |
| swing | academic (FX) | regime-noun | T | swing(s), long swings (Engel & Hamilton), swing high/low (spatial collision with IR-LD D14) | IR-RD (ki-06, D19) |
| stage | practitioner (Weinstein) | regime-noun | T | stage(s), stage analysis, stages 1-4 | IR-RD (§8.7) |
| day type | Market Profile | regime-noun | T | day type(s), type of day | PT-MP; WS |

### 2.2 Bull/bear and directional states

| term | tradition | family | type | morphological variants | source |
|---|---|---|---|---|---|
| bull market | Dow/financial press; academic dating | bull-bear | T | bull, bullish, bull market(s), bull-market, primary/secondary bull market, secular bull market | WP-01; IR-RD |
| bear market | Dow/financial press; academic dating | bull-bear | T | bear, bearish, bear market(s), secular/primary/secondary bear market | WP-01; IR-RD |
| correction | financial press | bull-bear | T | correction(s), market correction, Correction (Stock market), bull correction | WP-01; IR-RD (D22) |
| bear market rally | financial press; academic (Maheu et al.) | bull-bear | T | bear rally, bear market rallies, bear-market rally | WP-01; IR-RD (D22); PT-EM |
| market top / market bottom | financial press | bull-bear | B | top(s), bottom(s), market high, stock market bottom, what is a Bottom / what is a Top (PT-EM ch. 28) | WP-01; PT-EM |
| capitulation | financial press | bull-bear | T | capitulation(s), stock market capitulation | WP-01 |
| downturn | financial press | bull-bear | T | downturn(s), stock market downturn, market downturn | WP-01 |
| crash | econophysics; press | bull-bear | T | crash(es), market crash, crash state, critical state, precursor state | IR-RD (D27, D41) |
| rally | practitioner | bull-bear | T | rally, rallies, automatic rally (Wyckoff), bear market rally | PT-WY; WP-01 |
| uptrend / downtrend | classical TA | bull-bear | T | uptrend(s), downtrend(s), up-trend, up trend, trending up/down, intermediate downtrend, major downtrend | PT-EM; IR-RD (D56) |
| appreciation / depreciation | academic (FX) | bull-bear | T | appreciation(s), depreciation(s), long swings in the dollar | IR-RD (D19) |
| primary / secondary / minor trend | Dow Theory | bull-bear | T | primary/secondary/minor trend(s), tide wave and ripple, major/intermediate/near-term trend | PT-EM; PT-MU; WP-01 |

### 2.3 Business-cycle states

| term | tradition | family | type | morphological variants | source |
|---|---|---|---|---|---|
| expansion | NBER/Burns-Mitchell | business-cycle | T | expansion(s), expansionary phase, expansion phase | IR-RD (D07, D08, D13, D52) |
| contraction | NBER/Burns-Mitchell | business-cycle | T | contraction(s), contractionary phase. COLLISION: volatility/range contraction (family 2.6) | IR-RD |
| recession | NBER | business-cycle | T | recession(s), recessionary, recession dating | IR-RD (D13) |
| recovery | NBER; clustering imports | business-cycle | T | recovery, recoveries, recovery state | IR-RD (D27, D52) |
| revival | Burns-Mitchell (archaic) | business-cycle | T | revival(s) | IR-RD (D08) |
| peak / trough | dating algorithms | business-cycle | B | peak(s), trough(s), turning point(s), peak/trough dating | IR-RD (D06-D13) |
| slow growth | academic (Guidolin-Timmermann) | business-cycle | T | slow-growth state | IR-RD (D27) |

### 2.4 Spatial levels, zones, and boundaries

| term | tradition | family | type | morphological variants | source |
|---|---|---|---|---|---|
| support | classical TA | TA-spatial | S | support(s), support level(s), support zone/area, technical support, "supports and resistances" (the documented F005 plural), support and resistance / support-resistance / S&R / SR | SEED; PT-EM; PT-MU; WP-02; IR-F5 |
| resistance | classical TA | TA-spatial | S | resistance(s), resistance level(s), resistance price, technical resistance, pattern resistance, natural resistance point | SEED; PT-EM; WP-02; IR-LD (D54) |
| supply / demand zone | retail TA; Wyckoff root | TA-spatial | S | supply zone(s), demand zone(s), supply/demand area, supply and demand | SEED; PT-WY |
| channel | classical TA | TA-spatial | S | channel(s), trend channel, price channel, channel line, trading channel, Donchian channel, channeling (Elliott). COLLISION: Commodity Channel Index | SEED; PT-EM; PT-MU; IR-LD (D59) |
| band | volatility trading | TA-spatial | S | band(s), trading band, price band, volatility band, Bollinger Band(s), BandWidth, band-width | SEED; IR-RD (D17); IR-LD (D56) |
| zone | retail TA | TA-spatial | S | zone(s), price zone, premium/discount/equilibrium zone, target zone (academic: announced band, IR-LD D53) | SEED; IR-LD (D62, D53) |
| corridor | (thin) practitioner/academic | TA-spatial | S | corridor(s), price corridor, trading corridor | SEED |
| congestion area | classical TA | TA-spatial | B | congestion, congestion area(s), congestion zone, congested market | SEED |
| level | generic TA + academic barrier lit | TA-spatial | S | level(s), price level, key level, psychological level, support/resistance level | IR-LD (all groups) |
| barrier | academic behavioral | TA-spatial | S | barrier(s), psychological barrier, price barrier(s), round-number barrier | IR-LD (D46-D47); IR-F5 |
| round number | academic behavioral; practitioner | TA-spatial | S | round number(s), round figures (PT-EM), roundness, round fractions, multiples of 100 | IR-LD (D46-D51); PT-EM |
| pivot | retail/floor-trader TA | TA-spatial | S | pivot(s), pivot point(s), pivot high/low, floor pivots, Camarilla/Woodie/DeMark/Fibonacci pivots | IR-LD (D01-D06, D12) |
| trendline | classical TA | TA-spatial | S | trendline(s), trend line(s), internal trendline, double trendlines, fan principle, speed resistance lines | PT-EM; PT-MU |
| retracement | classical TA | TA-spatial | S | retracement(s), percentage retracement, Fibonacci retracement, maximum retracement (=drawdown, PT-EM ch. 42) | PT-MU; IR-LD (D11) |
| 52-week high/low | academic behavioral; practitioner | TA-spatial | S | 52-week high(s)/low(s), n-day high/low, x-week high, new high(s)/low(s), trailing extremum, past trading range limit | IR-F5 |
| basing point | Edwards & Magee (Magee procedure) | TA-spatial | S | basing point(s), Basing Points Procedure | PT-EM (ch. 5, 28) |
| liquidity level | retail smart-money | TA-spatial | S | liquidity, liquidity level(s), liquidity cluster, equal highs / equal lows, liquidity sweep, swept | IR-LD (D63, D71) |

### 2.5 Range, consolidation, and balance states

| term | tradition | family | type | morphological variants | source |
|---|---|---|---|---|---|
| trading range | classical TA; Wyckoff; academic | range-consolidation | B | trading range(s), range, range trading, ranging market, range-bound / range bound (market), range-bound state, trading-range, TR (Wyckoff), past trading range (Huddart et al.), trading range break | IR-RD (§8.7); PT-WY; IR-F5; IR-LD (D76) |
| consolidation | classical TA | range-consolidation | B | consolidation(s), consolidating, consolidation formation/pattern/phase, rectangular consolidation. COLLISION: M&A "consolidation (business)" - the entire Wikipedia redirect set for this title is the corporate sense (WP-06) | PT-EM (ch. 11); PT-MU |
| rectangle | classical TA | range-consolidation | B | rectangle(s), rectangle formation, the Rectangles | PT-EM; PT-MU |
| line (Dow Theory) | Dow Theory | range-consolidation | B | line(s), Dow line, the presence of Lines | PT-EM (§ch. 9); PT-MU (ch. 2) |
| tight trading range | practitioner (explicitly unbounded) | range-consolidation | B | tight trading range(s), tight range, narrow range, NR7-type narrow-range day | IR-LD (D64) |
| base / basing | practitioner | range-consolidation | B | base(s), basing, base formation, forming a base | WS (ws-vh-01 snippet: "base formed after a downtrend") |
| balance | Market Profile / auction | range-consolidation | B | balance, balanced, balanced market, balance area, balancing, horizontal development | SEED; PT-MP; WS |
| choppy | folklore indicator | range-consolidation | T | choppy, choppiness, Choppiness Index, chop. Provenance-negative: no source above tier 5 (IR-RC §8.5.3) | IR-RC |
| non-trending | by negation | range-consolidation | T | non-trending, trendless, not trending, absence of trend | IR-RD (§8.7 "by negation") |
| sideways market | classical TA | range-consolidation | T | sideways, sideways market/trend/movement, lateral, horizontal (movement) | PT-MU (trend has three directions) |

### 2.6 Volatility and compression states

| term | tradition | family | type | morphological variants | source |
|---|---|---|---|---|---|
| volatility regime | academic (SWARCH lineage) | volatility-state | T | volatility regime(s)/state(s), high/low/moderate volatility, high-volatility, vol regime | IR-RD (D20, D28, D50) |
| squeeze | volatility trading (Bollinger) | volatility-state | T | squeeze(s), Bollinger squeeze, band squeeze, volatility squeeze, the Squeeze | IR-RD (D17); SEED-adjacent |
| compression | practitioner; agenda vocabulary | volatility-state | T | compression, volatility compression, compressed, range contraction, contracting range/volatility | IR-RD (q-arxiv-08 zero-record finding; q-crossref-18) |
| turbulent / quiet | academic (Kritzman school) | volatility-state | T | turbulence, financial turbulence, turbulent/quiet periods/regime | IR-RD (D31, D36-38) |
| market volatility | generic | volatility-state | T | volatility, market/stock market/economic/financial volatility, price fluctuation, historical volatility | WP-05 |
| volatility clustering | econophysics stylized fact | volatility-state | T | volatility cluster(s), clustering of volatility | IR-RC (stylized-facts records) |

### 2.7 Crisis and stress states

| term | tradition | family | type | morphological variants | source |
|---|---|---|---|---|---|
| crisis / calm | academic; clustering school | crisis-stress | T | crisis, crises, crisis state/period/regime, calm (period), crash state | IR-RD (D16, D40-44, q-crossref-17) |
| stress / normal | academic (distributional monitoring) | crisis-stress | T | stress, market stress, high-/low-stress, stressed, normal state/regime | IR-RD (D53) |
| fragile | academic (absorption ratio) | crisis-stress | T | fragile, fragility, tightly-coupled, loosely-linked, systemic risk state | IR-RD (D38) |
| risk-on / risk-off | practitioner/allocator | crisis-stress | T | risk-on, risk-off, risk on/off, RORO | IR-RD (q-crossref-13) |
| flight to quality | academic/press | crisis-stress | T | flight-to-quality, flight to safety | IR-RD (q-crossref-17) |
| good times / bad times | academic (Chow et al.) | crisis-stress | T | good times, bad times, good/bad states | IR-RD (D36) |

### 2.8 Trend events, breakouts, and transition vocabulary

| term | tradition | family | type | morphological variants | source |
|---|---|---|---|---|---|
| breakout | classical TA; Kaufman event-driven | trend-event | B | breakout(s), break out, break-out, upside/downside breakout, breakout of/from the range, breaking the neckline, false breakout, breakdown, false breakdown, breakthrough / broke through (Driessen et al. usage), trading range break | SEED; PT-EM; PT-KF; IR-F5; IR-LD (D76) |
| parabolic movement | practitioner | trend-event | T | parabolic move(ment), parabolic advance, going parabolic. COLLISION: Parabolic SAR (stop-and-reverse, PT-EM ch. 27) | SEED |
| runs | academic (runs tests) | trend-event | T | run(s), runs of returns, runs test, runaway (see next row) | SEED |
| runaway day | Edwards & Magee | trend-event | T | runaway day(s), runaway gap, runaway issue(s), runaway move | PT-EM |
| gap | classical TA | trend-event | B | gap(s), price gap, breakaway/continuation/runaway/exhaustion/common/area/ex-dividend gap, island reversal. COLLISION: fair value gap (2.10) | PT-EM (ch. 12); PT-MU |
| selling climax / buying climax | Edwards & Magee; Wyckoff | trend-event | T | selling/buying climax(es), climactic, blowoff(s), blow-off top | PT-EM; PT-WY; PT-MU |
| spike | Edwards & Magee; Market Profile | trend-event | B | spike(s), price spike | PT-EM; PT-MP; PT-MU |
| reversal | classical TA | trend-event | B | reversal(s), reversal pattern, key reversal day, one-day reversal, reversal day, trend reversal, 3-box reversal (P&F) | PT-EM; PT-MU |
| measured move | classical TA | trend-event | B | measured move(s), measuring formula, measuring implications, price objective | PT-MU; PT-EM |
| throwback | Edwards & Magee | trend-event | B | throwback(s), throw-back | PT-EM (ch. 14) |
| break of structure | retail smart-money | trend-event | B | break of structure, BOS, change of character, CHoCH, market structure break | IR-LD (D72) |
| transition | agenda vocabulary; academic | trend-event | T | transition(s), regime transition, transitional state, mode transition, bifurcation (D33), transition matrix/probabilities | IR-RD (D22, D33) |
| turning point | dating literature | trend-event | T | turning point(s), turning-point, peak/trough alternation | IR-RD (D06-D07) |

### 2.9 Wyckoff cycle and event vocabulary

| term | tradition | family | type | morphological variants | source |
|---|---|---|---|---|---|
| accumulation | Wyckoff | Wyckoff | B | accumulation(s), accumulating, accumulation phase/zone/range, re-accumulation. COLLISION: accumulation/distribution volume indicator | SEED; PT-WY |
| distribution | Wyckoff | Wyckoff | B | distribution(s), distributing, distribution phase/zone/range, redistribution. SEVERE COLLISION: probability distribution - unusable as a bare phrase query | SEED; PT-WY |
| markup | Wyckoff | Wyckoff | T | markup, mark-up, mark up phase, markup campaign | SEED; PT-WY |
| markdown | Wyckoff | Wyckoff | T | markdown, mark-down, markdown phase. COLLISION: Markdown the markup language, retail price markdowns | SEED; PT-WY |
| spring | Wyckoff | Wyckoff | B | spring(s), Wyckoff spring, terminal shakeout, shakeout(s). COLLISION: season | PT-WY; WS |
| upthrust | Wyckoff | Wyckoff | B | upthrust(s), upthrust after distribution, UTAD, UT | PT-WY |
| test / secondary test | Wyckoff | Wyckoff | B | test(s), secondary test, ST, retest | PT-WY |
| sign of strength / weakness | Wyckoff | Wyckoff | T | sign of strength, SOS, sign of weakness, SOW | PT-WY |
| last point of support / supply | Wyckoff | Wyckoff | S | last point of support, LPS, last point of supply, LPSY | PT-WY |
| preliminary support / supply | Wyckoff | Wyckoff | S | preliminary support, PS, preliminary supply, PSY | PT-WY |
| automatic rally / reaction | Wyckoff | Wyckoff | T | automatic rally, AR, automatic reaction | PT-WY |
| bull trap / bear trap | Wyckoff; general TA | Wyckoff | B | bull trap(s), bear trap(s), trapped | PT-WY |
| line of least resistance | Wyckoff (Livermore usage) | Wyckoff | B | line of least resistance | PT-WY |

### 2.10 Auction / Market Profile vocabulary

| term | tradition | family | type | morphological variants | source |
|---|---|---|---|---|---|
| auction | Steidlmayer/Dalton | auction-MP | B | auction(s), market auction, auction market theory, two-way auction | WS (ws-vh-05 result set "Auction Theory Guide") |
| price discovery | auction theory; academic microstructure | auction-MP | T | price discovery, price discovery mechanism/process | SEED; WP-08 |
| imbalance | auction-MP | auction-MP | B | imbalance(s), imbalanced, out of balance. COLLISIONS: order-flow imbalance / queue imbalance (IR-LD D43-D44); ICT "imbalance" = fair value gap | SEED; IR-LD |
| rotation | auction-MP | auction-MP | T | rotation(s), rotational, rotational market, rotating | SEED; WS |
| initiative | auction-MP | auction-MP | T | initiative (buying/selling), initiative activity/tail | SEED; WS |
| responsive | auction-MP | auction-MP | T | responsive (buying/selling), responsive activity | SEED; WS |
| value area | Market Profile | auction-MP | S | value area(s), VA, VAH, VAL, value area migration, value migration, 70% value area | IR-LD (D33); PT-MP; PT-MP(CQG) |
| point of control | Market Profile | auction-MP | S | point of control, point-of-control, POC | IR-LD (D32); PT-MP |
| initial balance | Market Profile | auction-MP | S | initial balance, IB, initial balance range, IBR, opening range | IR-LD (D08-D09); PT-MP; PT-MP(CQG) |
| range extension | Market Profile | auction-MP | B | range extension(s) | PT-MP; WS |
| single prints | Market Profile | auction-MP | S | single prints, singles, single-print | PT-MP |
| excess | Market Profile | auction-MP | S | excess, excess at the extreme | PT-MP; WS |
| one-time framing | Market Profile | auction-MP | T | one-time framing, one-timeframing, one time framing, OTF | PT-MP; WS |
| trend day | Market Profile | auction-MP | T | trend day(s), trend-day, trend multi-distribution day | PT-MP; WS |
| neutral day | Market Profile | auction-MP | T | neutral day(s), neutral-day type | PT-MP; WS |
| normal day / non-trend day | Market Profile | auction-MP | T | normal day, normal-variation day, non-trend day | PT-MP |
| open types | Market Profile | auction-MP | T | open-drive, open test-drive, open rejection-reverse, open auction-in-range, open auction-out-of-range | PT-MP |
| buying / selling tail | Market Profile | auction-MP | S | buying tail(s), selling tail(s) | PT-MP |
| volume node | Market Profile / volume profile | auction-MP | S | high-volume node, HVN, low-volume node, LVN, volume node(s), volume area | IR-LD (D35); PT-MP |
| long liquidation / short covering | Market Profile | auction-MP | T | long liquidation, short covering, short-covering rally | PT-MP |
| TPO | Market Profile | auction-MP | S | TPO(s), time price opportunity, TPO profile/count | IR-LD (D34); PT-MP; PT-MP(CQG) |

### 2.11 Retail smart-money (ICT) structure vocabulary

| term | tradition | family | type | morphological variants | source |
|---|---|---|---|---|---|
| order block | ICT/smart-money | smart-money | S | order block(s), bullish/bearish order block, breaker block, mitigated/mitigation | IR-LD (D65-D67, D70) |
| fair value gap | ICT/smart-money | smart-money | S | fair value gap(s), FVG, imbalance (ICT sense), inefficiency | IR-LD (D68-D69) |
| premium / discount / equilibrium | ICT/smart-money | smart-money | S | premium zone, discount zone, equilibrium (zone). COLLISION: option premium, economic equilibrium | IR-LD (D62) |
| swing high / swing low | retail TA (code-defined) | smart-money | S | swing high(s)/low(s), swing point(s), swing structure vs internal structure | IR-LD (D14) |

### 2.12 Latent-state and statistical assignment vocabulary

| term | tradition | family | type | morphological variants | source |
|---|---|---|---|---|---|
| Markov switching | academic econometrics | latent-state | T | Markov switching / Markov-switching, regime switching, switching regression, MS-GARCH, SWARCH | IR-RD (D18-D31); IR-RC |
| hidden Markov model | academic | latent-state | T | hidden Markov, HMM, hidden semi-Markov, HSMM, hierarchical HMM | IR-RC; IR-MG (§8.3) |
| threshold autoregression | academic | latent-state | T | threshold autoregression/autoregressive, SETAR, TAR, threshold regime | IR-RD (D34) |
| smooth transition | academic | latent-state | T | smooth transition (autoregression), STAR, transition function | IR-RD (D35) |
| structural break | academic | latent-state | T | structural break(s), breakpoint(s), change point / change-point / changepoint (detection), Bai-Perron, PELT | IR-RC; IR-RD (D50) |
| jump model | academic (Bemporad-Boyd lineage) | latent-state | T | jump model(s), fitting jump models, jump penalty, greedy online classification | IR-RD (D48-D49) |
| market state (clustering sense) | econophysics | latent-state | T | market state(s), states of a financial market, correlation state, similarity clusters | IR-RD (D39-D44); OA (vh-openalex-04) |
| duration dependence | academic | latent-state | T | duration dependence, duration-dependent, phase duration, persistence | IR-RD (D21); OA (vh-openalex-03) |
| directional change | intrinsic-time school | latent-state | T | directional change(s), DC, overshoot, intrinsic time, event-based time | IR-RD (D54-D56) |

### 2.13 Momentum / mean-reversion dynamical classes

| term | tradition | family | type | morphological variants | source |
|---|---|---|---|---|---|
| momentum | academic + practitioner | momentum-reversion | T | momentum (regime/state), momentum-based, trending (regime) | IR-RD (D33); PT-KF; PT-MU |
| mean reversion | academic | momentum-reversion | T | mean reversion / mean-reversion, mean-reverting, reversion (regime) | IR-RD (D33) |
| trend | universal | momentum-reversion | T | trend(s), trending (market), trend regime/state, trend system, event-driven trend, trend-following | SEED-adjacent; PT-EM; PT-KF; IR-RD (D57) |
| efficiency ratio | Kaufman folklore | momentum-reversion | T | efficiency ratio, Kaufman Efficiency Ratio, fractal efficiency, KAMA. Provenance-negative (IR-RC §8.5.1) | IR-RC; IR-MG |
| directional movement | Wilder folklore | momentum-reversion | T | directional movement, ADX, average directional (index). Provenance-negative (IR-RC §8.5.2) | IR-RC |

### 2.14 Sentiment and positioning states

| term | tradition | family | type | morphological variants | source |
|---|---|---|---|---|---|
| overbought / oversold | oscillator tradition | sentiment | T | overbought, oversold, oversold market, 70/30 lines | PT-MU; PT-EM (ch. 38) |
| market sentiment | behavioral/press | sentiment | T | sentiment, investor sentiment, investor attention, bearish/bullish sentiment, permabear, permabull | WP-04 |
| contrary opinion | futures tradition | sentiment | T | contrary opinion, contrarian | PT-MU |

## 3. Families in this registry ABSENT from the user's seed list

The seed list carried five families (TA-spatial; Wyckoff four-phase;
auction/Market-Profile core; trend-event; regime-noun synonyms). The harvest
added the following, each with at least one attested term above:

**Wholly absent families:**

1. **Bull/bear directional states** (§2.2): secular/primary/secondary bull and
   bear, correction, bear market rally, capitulation, market top/bottom,
   downturn, crash, rally, appreciation/depreciation. The largest omission: the
   Wikipedia redirect graph alone carries 36 surface forms into "Market trend".
2. **Business-cycle states** (§2.3): expansion, contraction, recession,
   recovery, revival, peak, trough, slow growth.
3. **Range/consolidation states as a family** (§2.5): trading range, range-bound,
   consolidation, rectangle, **line (Dow sense)**, tight trading range, base/basing,
   sideways market, choppy, non-trending. (Seed had only "congestion area".)
4. **Volatility/compression states** (§2.6): volatility regime, squeeze,
   compression, turbulent/quiet, volatility clustering.
5. **Crisis/stress states** (§2.7): crisis/calm, stress/normal, fragile,
   risk-on/risk-off, flight to quality, good/bad times.
6. **Chart-pattern event vocabulary** (§2.8 beyond breakout): gaps taxonomy,
   climaxes, blowoff, spike, key reversal day, measured move, throwback,
   break of structure / change of character, transition, turning point.
7. **Retail smart-money structure** (§2.11): order block, fair value gap,
   premium/discount/equilibrium, swing structure.
8. **Latent-state statistical vocabulary** (§2.12): Markov switching, HMM/HSMM,
   SETAR/STAR, structural break/changepoint, jump model, market state
   (clustering), duration dependence, directional change.
9. **Momentum/mean-reversion dynamical classes** (§2.13), including the two
   provenance-negative folklore indicators (efficiency ratio, ADX) retained
   because sweep queries must still find their applications.
10. **Sentiment/positioning states** (§2.14): overbought/oversold, market
    sentiment, contrary opinion.
11. **Trailing-extremum levels** (§2.4): 52-week high/low, n-day high/low,
    Donchian-type channel, basing points, liquidity levels, barrier/round-number
    vocabulary.
12. **Level/pivot vocabulary generally** (§2.4): level, barrier, pivot,
    trendline, retracement - the seed's TA-spatial family named zones and bands
    but not the line-locating nouns.

**Extensions within seed families** (family present, terms absent from seed):

- Wyckoff: the entire event vocabulary (spring, upthrust/UTAD, shakeout, tests,
  SOS/SOW, LPS/LPSY, PS/PSY, AR, traps, line of least resistance, phases A-E,
  re-accumulation/redistribution) - the seed had only the four cycle names.
- Market Profile: value area (+migration), POC, initial balance, range
  extension, single prints, excess, one-time framing, day types, open types,
  tails, volume nodes, long liquidation/short covering, TPO - the seed had only
  balance/imbalance/rotation/initiative/responsive/discovery.
- Regime-noun: period, swing (long swings), stage, day type - beyond the seed's
  state/phase/mode/environment/condition/episode.
- Trend-event: runaway (day/gap/issue), breakdown, breakthrough, false
  breakout/breakdown - morphological kin of "breakout" the seed did not carry.

**Homonym-collision ledger** (terms whose bare phrase queries will drown;
flagged inline above): distribution (probability), consolidation (M&A - the
Wikipedia redirect set for "Consolidation (business)" is entirely the corporate
sense), market state (exchange session protocol), imbalance (three senses),
balance (accounting), spring (season), channel (communications; CCI), markdown
(the markup language; retail pricing), contraction (two senses in this very
registry), equilibrium (economics), premium (options), accumulation (indicator
sense). Sweep queries on these terms need conjunctive context terms.

## 4. Declared limits

1. **Single harvester.** One model compiled this registry in one session; the
   families are bounded by what its fetches reached. No PRESS-style peer review
   of the registry occurred (McGowan et al. 2016 recommend review *before*
   execution - the later sweep should treat this registry as the reviewable
   artifact and this section as the standing invitation).
2. **Investopedia arm not executable.** WebFetch is blocked for
   www.investopedia.com (logged in `vh-websearch-01.json`); the
   Investopedia related-terms graph was not harvested. The Wikipedia redirect
   arm partially substitutes. This is the registry's one unexecuted directive
   arm — a verification gap, severity minor (vocabulary source, not evidence).
3. **TOC-level harvest for two of the three canonical books.** Edwards & Magee
   and Murphy were harvested at chapter/section-title depth (full TOCs
   retrieved); Kaufman at chapter-title depth only - Kaufman's index-level
   vocabulary (e.g. "swing breakout", "N-day breakout" as index entries) was not
   reachable through any non-403 source this session. Wiley retail, Routledge,
   O'Reilly and PenguinRandomHouse product pages all 403/404'd (logged);
   publisher 403s are recorded per directive as access failures, not as
   nonexistence.
4. **Wikipedia arm ran on eight titles.** Redirect graphs for e.g. "Wyckoff
   method", "Dead cat bounce", "Santa Claus rally", "Melt-up" were not fetched;
   the calendar-anomaly and press-idiom vocabulary is underrepresented here.
5. **No frequency weighting.** The registry records existence and provenance,
   not corpus frequency; Hausner-style objective term derivation with document
   frequencies would require the sweep's own retrieval sets and is future work
   for the sweep agents, not this stage.
6. **Two Market Profile terms known to circulate ("poor high/poor low",
   "value area rule") were seen only in sources not fetched this session and
   are deliberately excluded**: no fetched log attests them, and this registry
   does not record terms from compiler memory.
7. **English only.** Every harvest source is anglophone; the predecessor
   corpora's any-language eligibility means the sweep may still need
   non-English state vocabulary; none is registered here.

## 5. Tallies

Computed over the registry tables (one row = one head term):

| section | family | head terms |
|---|---|---|
| 2.1 | regime-noun synonyms | 11 |
| 2.2 | bull/bear directional | 12 |
| 2.3 | business-cycle | 7 |
| 2.4 | spatial levels/zones | 17 |
| 2.5 | range/consolidation | 10 |
| 2.6 | volatility/compression | 6 |
| 2.7 | crisis/stress | 6 |
| 2.8 | trend events/transitions | 13 |
| 2.9 | Wyckoff | 13 |
| 2.10 | auction/Market Profile | 21 |
| 2.11 | smart-money | 4 |
| 2.12 | latent-state statistical | 9 |
| 2.13 | momentum/mean-reversion | 5 |
| 2.14 | sentiment | 3 |
| | **total head terms** | **137** |

Morphological variants enumerated across all rows (counting each distinct
surface form listed in the variants column, excluding collision notes):
**~540** distinct queryable surface forms (split on commas/semicolons in the
variants column; approximate because slashed alternates like "high/low" count
as one). Head terms by tradition of origin:
classical TA / Dow / Edwards-Magee lineage 38; Market Profile / auction 22;
academic econometrics and econophysics 34; Wyckoff 17; retail smart-money 8;
business-cycle dating 7; press/behavioral/sentiment 8; folklore-indicator
(provenance-negative, retained for recall) 3.

---

# Addendum 2026-08-24 (post-sweep) — flagged families registered as rows

Appended per the register/living-doc convention (append-only; no entry above
this rule edited). The two sweeps flagged 12 synonym families present in
NEITHER the original registry NOR the seed list (part A §8.4; part B §8.7).
They are registered here so the next round's instrument carries them; audit
finding REV-1-2 (naming-sweep round 1) is the trigger.

| term/family | tradition | synonym family | type | status |
|---|---|---|---|---|
| bubble / explosive / exuberance | academic econometrics | explosive regime | temporal | **swept in-line** (NB-04/NB-05 + family records, part B) |
| boom/bust | academic (macro-finance) | cycle states | temporal | swept in-line (NB-10/NB-11, part B) |
| drawdown / drawup (episodes) | academic (econophysics) | directional episodes | temporal | swept in-line (NB-02/NB-08, part B) |
| metastable state / metastability | academic (applied math) | latent-phase | temporal | swept in-line (NB-31, part B) |
| sequences and reversals | academic (early statistics) | runs family | temporal | swept in-line (Cowles–Jones lineage, part B) |
| failed auction | Market Profile / auction | auction states | temporal | swept in-line (NA-18, part A) |
| absorption | Wyckoff-adjacent | supply/demand interaction | temporal | **open — not swept** (tier-5 stratum, zero academic yield evidenced this round) |
| liquidity void | retail smart-money (ICT) | gap family | spatial | open — not swept (same rationale) |
| Judas swing | retail smart-money (ICT) | false-move events | temporal | open — not swept (same rationale) |
| inversion FVG (IFVG) | retail smart-money (ICT) | gap family | spatial | open — not swept (same rationale) |
| midnight opening gap (MNOG) | retail smart-money (ICT) | session-anchor levels | spatial | open — not swept (same rationale) |
| "technical range" (theorized construct) | academic near-miss | range family | both | open — not swept (single-source flag, part A) |

Morphological variants for the six open rows are NOT yet generated — variant
generation is deferred to the round that sweeps them, so the variant column's
provenance discipline (generated at harvest time, logged) is preserved.
