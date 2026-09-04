# -*- coding: utf-8 -*-
"""Supplementary ACADEMIC-arm block, same frozen construction rule (section 3.1).

Motive, recorded rather than buried: the first block's weather (stratum 3) and macro
(stratum 4) queries returned near-zero, and a near-zero return is only evidence of
absence if the vocabulary was given a fair test. This block gives those two strata a
second surface form. The instrument slot carries CONTRACT-FAMILY-QUALIFIED phrases
("weather derivative", "economic derivative", "macroeconomic derivative"), on the
reading that section 3.1's instrument vocabulary is "the terms naming binary event
contracts, EVENT DERIVATIVES, prediction markets, or the named venues" and that these
phrases name event-derivative families. Two of them are also counterparty legs under
section 2.2's stated extension. The construal is reported, not assumed silent.
"""
import os, sys, time
assert os.environ.get("PYTHONHASHSEED") == "0"
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import run_arm
from queries import CR, CROSSREF_SEL, OA_MAIL

SUPP = [
 dict(qid="ks-crossref-16", platform="crossref", stratum="S4-macro-event-contracts", cap="rows=20",
      instrument="economic derivative (binary auction contract on CPI/payrolls)", strategy="arbitrage", venue=None,
      note="Contract-family-qualified instrument phrase; see module docstring.",
      url=CR+"economic+derivatives+auction+binary+option+payrolls+CPI+arbitrage"+CROSSREF_SEL),
 dict(qid="ks-crossref-17", platform="crossref", stratum="S3-weather-and-climate-event-contracts", cap="rows=20",
      instrument="weather derivative", strategy="hedging", venue=None,
      note="Contract-family-qualified instrument phrase; also a section 2.2 counterparty leg.",
      url=CR+"weather+derivative+temperature+binary+option+hedging"+CROSSREF_SEL),
 dict(qid="ks-crossref-18", platform="crossref", stratum="S1-venue-and-contract-families,S4-macro-event-contracts", cap="rows=20",
      instrument="event contract", strategy="hedging", venue="Kalshi", url=CR+"Kalshi+event+contract+hedging"+CROSSREF_SEL),
 dict(qid="ks-crossref-19", platform="crossref", stratum="S6-regulated-DCM-microstructure", cap="rows=20",
      instrument="binary event contract", strategy="inventory", venue="fully collateralised exchange",
      url=CR+"fully+collateralized+binary+payoff+event+contract+exchange+inventory+capital"+CROSSREF_SEL),
 dict(qid="ks-openalex-09", platform="openalex", stratum="S3-weather-and-climate-event-contracts", cap="per-page=25",
      instrument="weather derivative", strategy="hedging", venue=None,
      url='https://api.openalex.org/works?filter=title_and_abstract.search:%22weather%20derivative%22%20AND%20%22hedging%22&per-page=25'+OA_MAIL),
 dict(qid="ks-openalex-10", platform="openalex", stratum="S4-macro-event-contracts", cap="per-page=25",
      instrument="economic derivative", strategy="arbitrage", venue=None,
      url='https://api.openalex.org/works?filter=title_and_abstract.search:%22economic%20derivatives%22%20AND%20%22arbitrage%22&per-page=25'+OA_MAIL),
 dict(qid="ks-openalex-11", platform="openalex", stratum="S4-macro-event-contracts", cap="per-page=25",
      instrument="macroeconomic derivative", strategy="forecasting-driven trading", venue=None,
      url='https://api.openalex.org/works?filter=title_and_abstract.search:%22macroeconomic%20derivatives%22%20AND%20%22forecast%22&per-page=25'+OA_MAIL),
 dict(qid="ks-openalex-12", platform="openalex", stratum="S1-venue-and-contract-families", cap="per-page=25",
      instrument="event contract", strategy="hedging", venue="Kalshi", url='https://api.openalex.org/works?filter=title_and_abstract.search:%22event%20contract%22%20AND%20%22hedging%22&per-page=25'+OA_MAIL),
 dict(qid="ks-openalex-13", platform="openalex", stratum="S6-regulated-DCM-microstructure", cap="per-page=25",
      instrument="event contract", strategy="inventory", venue=None,
      url='https://api.openalex.org/works?filter=title_and_abstract.search:%22event%20contract%22%20AND%20%22inventory%22&per-page=25'+OA_MAIL),
 dict(qid="ks-openalex-14", platform="openalex", stratum="S2-sports-and-sportsbook-vs-exchange", cap="per-page=25",
      instrument="sportsbook", strategy="market making", venue="betting exchange",
      url='https://api.openalex.org/works?filter=title_and_abstract.search:%22sportsbook%22%20AND%20%22market%20making%22&per-page=25'+OA_MAIL),
 dict(qid="ks-arxiv-09", platform="arxiv", stratum="S3-weather-and-climate-event-contracts", cap="max_results=50",
      instrument="weather derivative", strategy="hedging", venue=None,
      url='https://export.arxiv.org/api/query?search_query=abs:%22weather%20derivative%22%20AND%20abs:%22hedging%22&max_results=50'),
 dict(qid="ks-arxiv-10", platform="arxiv", stratum="S4-macro-event-contracts", cap="max_results=50",
      instrument="economic derivative", strategy="arbitrage", venue=None,
      url='https://export.arxiv.org/api/query?search_query=abs:%22economic%20derivatives%22%20AND%20abs:%22arbitrage%22&max_results=50'),
 dict(qid="ks-arxiv-11", platform="arxiv", stratum="S1-venue-and-contract-families", cap="max_results=50",
      instrument="Kalshi", strategy="market making", venue=None,
      url='https://export.arxiv.org/api/query?search_query=abs:%22Kalshi%22%20AND%20abs:%22market%20making%22&max_results=50'),
 dict(qid="ks-arxiv-12", platform="arxiv", stratum="S6-regulated-DCM-microstructure", cap="max_results=50",
      instrument="binary contract", strategy="spread", venue=None,
      url='https://export.arxiv.org/api/query?search_query=abs:%22binary%20contract%22%20AND%20abs:%22spread%22&max_results=50'),
 dict(qid="ks-arxiv-13", platform="arxiv", stratum="S7-LLM-and-forecasting-driven-trading", cap="max_results=50",
      instrument="prediction market", strategy="trading (agentic execution)", venue=None,
      url='https://export.arxiv.org/api/query?search_query=abs:%22prediction%20market%22%20AND%20abs:%22trading%20agent%22&max_results=50'),
]

for q in SUPP:
    e = run_arm.execute(q)
    print("%-18s %-14s status=%-6s n=%-4s tot=%s" % (e["query_id"], q["platform"], e["http_status"], e["n_returned"], e["n_total_reported"]))
    sys.stdout.flush()
    if e["http_status"] != 200:
        for i, w in enumerate([30, 60, 90]):
            time.sleep(w)
            r = run_arm.execute(q, attempt=i + 1, retry_of=q["qid"])
            print("  retry %-14s status=%-6s n=%s" % (r["query_id"], r["http_status"], r["n_returned"]))
            sys.stdout.flush()
            if r["http_status"] == 200:
                break
    time.sleep({"crossref": 2.0, "openalex": 4.0, "arxiv": 4.0}.get(q["platform"], 3.0))
print("supplementary block complete")
