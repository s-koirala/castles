# @nusantara-ventures/dino-markets

> **Renamed.** This package was previously published as `dino-markets`. That name is deprecated and will not receive updates — install `@nusantara-ventures/dino-markets` instead. No API changes came with the move.

Official TypeScript SDK for [dino.markets](https://dino.markets): related Kalshi and Polymarket prediction markets across sports, crypto, weather, and economics, plus confirmed cross-venue arbitrage and a real-time stream.

Zero runtime dependencies. Built on the native `fetch` API, so it runs in Node 18+, Deno, Bun, and the browser without a bundler polyfill.

## Install

```bash
npm install @nusantara-ventures/dino-markets
```

## Auth

Get a free API key from the dashboard at https://dino.markets. Sign in and open the keys page, then mint a key with the `sk_live_` prefix.

Pass the key directly, or set it as an environment variable and let the client pick it up:

```bash
export DINO_API_KEY=sk_live_...
```

```ts
import { Dino } from "@nusantara-ventures/dino-markets";

const dino = new Dino(); // reads DINO_API_KEY
// or: new Dino({ apiKey: "sk_live_..." });
```

## Quickstart

```ts
import { Dino } from "@nusantara-ventures/dino-markets";

const dino = new Dino({ apiKey: "sk_live_..." });

const { markets } = await dino.markets({ category: "sports", sport: "baseball", competition: "MLB" });
console.log(markets.length, "markets");

const { markets: crypto } = await dino.markets({ category: "crypto", asset: "btc", market_type: "crypto_above" });

const arbs = await dino.findArbitrage({ sport: "soccer" });
for (const opportunity of arbs.opportunities) {
  console.log(opportunity.title, opportunity.roi_pct, opportunity.fee_model, opportunity.max_wager_usd);
}

const market = await dino.market(markets[0].id);
const history = await dino.history(markets[0].id);
const { categories } = await dino.categories();

await dino.reportBadArb({ opp_id: arbs.opportunities[0]?.id, reason: "stale price on one leg" });
```

Market catalog methods return the canonical `Market` type. `findArbitrage()` returns the separate `Opportunity` type with exact snapshot selected legs, conservative modeled ROI after fees, `fee_model`, and a USD capital estimate.

REST reads are priced roughly two minutes behind live on every plan. If you need the current price when it changes, use the WebSocket stream.

## Streaming

Every plan gets a real-time WebSocket feed over [Centrifugo](https://centrifugal.dev): Free is scoped to a curated `sample` channel, while Basic, Premium, and Pro plans get the full market stream. Streaming needs the optional `centrifuge` peer dependency:

```bash
npm install centrifuge
```

```ts
import { Dino, watch } from "@nusantara-ventures/dino-markets";

const dino = new Dino({ apiKey: "sk_live_..." });

const handle = await watch(dino, {
  onFrame: (frame, channel) => console.log(channel, frame),
  onError: (err) => console.error(err),
  onRecoveryFailed: (channel) => bootstrapFromRest(channel),
});

// later
handle.close();
```

`watch` mints one short-lived ticket per connection attempt, including automatic reconnects. At connect time the server re-reads current account state, selects the active plan's channels, and forwards their publications. Initial admission is fenced to about 15 seconds; the first successful plan-matching refresh then grants the normal 15-minute renewal. If the five-minute recovery history cannot fill a reconnect gap, `onRecoveryFailed` receives the channel that must be loaded again from REST.

## Error handling

Every non-2xx response is thrown as a typed error, all extending `DinoError`:

```ts
import { AuthenticationError, PlanError, RateLimitError, ServerError } from "@nusantara-ventures/dino-markets";

try {
  await dino.markets();
} catch (err) {
  if (err instanceof RateLimitError) {
    console.log("retry after", err.retryAfter, "seconds");
  } else if (err instanceof AuthenticationError) {
    console.log("check your API key");
  } else if (err instanceof PlanError) {
    console.log("subscription inactive or plan not recognized:", err.body);
  } else if (err instanceof ServerError) {
    console.log("dino.markets had a server error, try again shortly");
  }
}
```

The client retries a 429 or 5xx automatically (`maxRetries`, default 2), honoring the server's `Retry-After` when present and backing off otherwise. A 4xx other than 429 is never retried.

## Rate limits

REST requests are metered per API key:

| Plan | Requests/month | Requests/sec | WebSocket |
| --- | ---: | ---: | --- |
| Free | 10,000 | 10 | Curated `sample`, 1 connection |
| Basic ($30/month) | 1,000,000 | 10 | Full market stream, 3 connections |
| Premium ($100/month) | 5,000,000 | 25 | Full market stream, 10 connections |
| Pro ($200/month) | 5,000,000 | 25 | Full stream plus raw quotes and early candidates, 10 connections |

## Disclaimer

Informational data. Not investment advice. You trade on your own venue accounts at your own risk.

## Support

Reach us at support@dino.markets with questions, or report a bad signal directly from your code with `dino.reportBadArb(...)`.

## Localized documentation

| Language | Docs | MCP server |
|---|---|---|
| 日本語 | [Docs](https://dino.markets/ja/docs) | [MCP](https://dino.markets/ja/docs/mcp) |
| 한국어 | [Docs](https://dino.markets/ko/docs) | [MCP](https://dino.markets/ko/docs/mcp) |
| 简体中文 | [Docs](https://dino.markets/zh/docs) | [MCP](https://dino.markets/zh/docs/mcp) |
| Español | [Docs](https://dino.markets/es/docs) | [MCP](https://dino.markets/es/docs/mcp) |
