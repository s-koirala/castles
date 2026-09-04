# Kalshi (kalshi)

<!-- API-EVANGELIST-PROVENANCE:BEGIN -->
> ### About this repository
>
> **This is not our API.** This repository is an independent, third-party profile of a company's
> **publicly available** API surface, maintained by [API Evangelist](https://apievangelist.com).
> API Evangelist does not operate, host, resell, or support this company's APIs, and is not
> affiliated with or endorsed by the company unless stated on the profile.
>
> **Where the information came from.** Everything here is assembled from material a member of the
> public can reach with a browser and no credentials — the company's own website, developer portal
> and documentation, the specifications it publishes for public use (OpenAPI, AsyncAPI, JSON Schema,
> `apis.json`, `llms.txt` and similar), its public repositories, and its public status, pricing and
> changelog pages. **Nothing here is obtained by breaching a system, defeating an access control, or
> using credentials of any kind.**
>
> **The rating is an independent assessment.** The Kin Score and Agent Readiness rating are
> independently calculated scores of a company's *public* API artifacts, produced by API Evangelist
> against a published rubric. They are not certifications, endorsements, security assessments, or
> audits, and they score published artifacts — not the quality, safety, or security of the software.
>
> **Corrections, re-scores, and removal are free.** No partnership, contract, or purchase is
> required, and you do not need to justify the request.
>
> - **Something wrong?** Open an issue on this repository, or email
>   [info@apievangelist.com](mailto:info@apievangelist.com).
> - **Published something new?** Ask for a re-score and we will re-run the rating.
> - **Want the listing taken down?** Say so and we will honor it. The profile is reduced to your
>   company name, a factual description, and a link to your own site, and the company is recorded as
>   **unrated** — never scored zero for having asked.
>
> **Response times.** Acknowledgement within **one business day**; removal or restriction within
> **two business days**; corrections and re-scores within **five business days**.
>
> **Not from the company, and here with a question?** You are welcome here — we would rather be the
> front line and point you the right way than have a good report go nowhere. What this repository
> can answer is narrow, though, so it is worth knowing who you are actually looking for:
>
> - **A question about how the API works, an account, billing, or a bug in the service** — that is
>   the company's own support, not us. We profile this API; we do not operate it and cannot see
>   your account.
> - **A bug in an open-source project we only catalog** — file it on that project's own repository.
>   This has happened with a real and correct bug report that reached us instead of the people who
>   could fix it, which helped nobody.
> - **Anything about this listing itself** — the description, the tags, the rating, a missing or
>   wrong artifact — is ours. Open an issue here.
> - **Not sure, or something general about API Evangelist or APIs.io** — open an issue on the
>   [APIs.io Inbox](https://github.com/api-search/inbox) and we will route it.
>
> **This repository contains no software, and we will never ask you to download anything.** There is
> no build, release, installer, or binary here — only text and machine-readable API descriptions, so
> there is nothing here that can be "corrupt" or need "repairing". Any issue, comment, or email
> claiming otherwise and offering a download link is not from us and is hostile. Do not follow the
> link; it is a lure. Report it to GitHub and, if you like, tell us at
> [info@apievangelist.com](mailto:info@apievangelist.com) so we can take it down.
>
> **On a security or compliance team?** Email
> [info@apievangelist.com](mailto:info@apievangelist.com) with *security* in the subject line and
> you will get a person, not a form. We will tell you exactly which public URLs this profile was
> built from so your team can see the same surface we did, and we will take the listing down on
> request while you work through it.
>
> Full detail: **[Where this data comes from](https://apievangelist.com/about/where-our-data-comes-from)**
<!-- API-EVANGELIST-PROVENANCE:END -->

Kalshi is a CFTC-regulated US exchange for binary event contracts on real-world outcomes - elections, economics, weather, sports, and more. The platform exposes a public REST trading API and WebSocket streams for market data, orders, positions, and portfolio actions, with a published OpenAPI 3 specification and AsyncAPI definition for the streaming surface. A demo environment mirrors production for safe development. Official Python and community SDKs are provided.

**APIs.json:** [https://raw.githubusercontent.com/api-evangelist/kalshi/refs/heads/main/apis.yml](https://raw.githubusercontent.com/api-evangelist/kalshi/refs/heads/main/apis.yml)

## Tags

- Prediction Markets
- Event Contracts
- Exchange
- CFTC
- Trading
- Markets

## Timestamps

- **Created:** 2026-05-23
- **Modified:** 2026-05-29

## APIs

### Kalshi Trade API (REST)

Public REST API for trading on Kalshi - browse markets, events, and series, place and cancel orders, manage portfolio and positions, fund and withdraw, and pull historical trades. Authenticated with API keys and Ed25519 request signatures.

- **Human URL:** [https://docs.kalshi.com/api-reference](https://docs.kalshi.com/api-reference)
- **Base URL:** `https://api.elections.kalshi.com/trade-api/v2`

#### Tags

- REST
- Trading
- Markets
- Orders

#### Properties

- [Documentation](https://docs.kalshi.com/api-reference)
- [OpenAPI](https://docs.kalshi.com/openapi.yaml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/kalshi.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/kalshi.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### Kalshi Trade API (external-api host)

Alternate production host for the Kalshi Trade API, used by external integrators. Same API surface and authentication as the primary host.

- **Human URL:** [https://docs.kalshi.com/api-reference](https://docs.kalshi.com/api-reference)
- **Base URL:** `https://external-api.kalshi.com/trade-api/v2`

#### Tags

- REST
- Trading
- External

#### Properties

- [Documentation](https://docs.kalshi.com/api-reference)
- [OpenAPI](https://docs.kalshi.com/openapi.yaml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/kalshi.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/kalshi.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### Kalshi Trade API (Demo)

Demo / sandbox environment for the Kalshi Trade API - mirrors production semantics with simulated balances and markets for safe development and automated testing.

- **Human URL:** [https://docs.kalshi.com/api-reference](https://docs.kalshi.com/api-reference)
- **Base URL:** `https://demo-api.kalshi.co/trade-api/v2`

#### Tags

- REST
- Demo
- Sandbox
- Testing

#### Properties

- [Documentation](https://docs.kalshi.com/api-reference)
- [Postman Collection](collections/kalshi.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/kalshi.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### Kalshi WebSocket Streaming API

Real-time streaming feed for market data, order book updates, fills, and portfolio events on Kalshi. Documented as an AsyncAPI spec alongside the OpenAPI REST surface.

- **Human URL:** [https://docs.kalshi.com/api-reference](https://docs.kalshi.com/api-reference)
- **Base URL:** `wss://api.elections.kalshi.com/trade-api/ws/v2`

#### Tags

- WebSocket
- Streaming
- Market Data

#### Properties

- [Documentation](https://docs.kalshi.com/api-reference)
- [AsyncAPI](https://docs.kalshi.com/asyncapi.yaml) — [AsyncAPI Specification](https://www.asyncapi.com/docs/reference/specification/latest)
- [AsyncAPI](https://raw.githubusercontent.com/api-evangelist/kalshi/refs/heads/main/asyncapi/kalshi-asyncapi.yml) — [AsyncAPI Specification](https://www.asyncapi.com/docs/reference/specification/latest)
- [Postman Collection](collections/kalshi.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/kalshi.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### Kalshi OpenAPI Specification

Machine-readable OpenAPI 3 description of the Kalshi Trade REST API. Suitable for generating clients, mocks, and contract tests.

- **Human URL:** [https://docs.kalshi.com/](https://docs.kalshi.com/)
- **Base URL:** `https://docs.kalshi.com/openapi.yaml`

#### Tags

- OpenAPI
- Specification

#### Properties

- [OpenAPI](https://docs.kalshi.com/openapi.yaml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/kalshi.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/kalshi.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### Kalshi AsyncAPI Specification

Machine-readable AsyncAPI description of the Kalshi WebSocket streaming API. Suitable for generating async clients and documenting message schemas.

- **Human URL:** [https://docs.kalshi.com/](https://docs.kalshi.com/)
- **Base URL:** `https://docs.kalshi.com/asyncapi.yaml`

#### Tags

- AsyncAPI
- Specification
- WebSocket

#### Properties

- [AsyncAPI](https://docs.kalshi.com/asyncapi.yaml) — [AsyncAPI Specification](https://www.asyncapi.com/docs/reference/specification/latest)
- [Postman Collection](collections/kalshi.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/kalshi.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### Kalshi Python Starter Kit

Official Python starter / SDK published by Kalshi for connecting to the Trade REST API and WebSocket streams. Includes request signing, authentication helpers, and example trading flows.

- **Human URL:** [https://github.com/Kalshi/kalshi-starter-code-python](https://github.com/Kalshi/kalshi-starter-code-python)
- **Base URL:** `https://github.com/Kalshi/kalshi-starter-code-python`

#### Tags

- SDK
- Python
- Starter

#### Properties

- [Repository](https://github.com/Kalshi/kalshi-starter-code-python)
- [Postman Collection](collections/kalshi.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/kalshi.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

## Common Properties

- [Website](https://kalshi.com/)
- [Documentation](https://docs.kalshi.com/)
- [A P I  Reference](https://docs.kalshi.com/api-reference)
- [Help](https://help.kalshi.com/)
- [Git Hub](https://github.com/Kalshi)
- [Developer  Agreement](https://kalshi.com/developer-agreement)
- [LinkedIn](https://www.linkedin.com/company/kalshi/)
- [L L Ms Txt](https://docs.kalshi.com/llms.txt)

## Maintainers

**FN:** Kin Lane
**Email:** kin@apievangelist.com
