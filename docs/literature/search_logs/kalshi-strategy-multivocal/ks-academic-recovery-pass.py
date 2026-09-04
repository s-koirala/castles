# -*- coding: utf-8 -*-
"""Recovery pass: (a) retry-until-200 on the Semantic Scholar queries that returned 429
   (predecessor -b/-c retry convention), (b) log the RePEc alternate-interface probes.
   Every attempt is logged as its own section-3.0 entry with retry_of set."""
import os, sys, json, time
assert os.environ.get("PYTHONHASHSEED") == "0"
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import run_arm
from queries import QUERIES

BY = {q["qid"]: q for q in QUERIES}

# (a) Semantic Scholar recovery -------------------------------------------------
S2 = ["ks-s2-01", "ks-s2-02", "ks-s2-03", "ks-s2-04", "ks-s2-05"]
SUFFIX = "efghijklmnopqrstuvwxyz"
for qid in S2:
    q = BY[qid]
    got = False
    for i, wait in enumerate([30, 45, 60, 90, 120, 150, 180]):
        time.sleep(wait)
        sub = "%s-%s" % (qid, SUFFIX[i])
        e = run_arm.execute(dict(q, qid=sub), attempt=0, retry_of=qid)
        print("%-16s status=%-6s n=%-4s tot=%s" % (sub, e["http_status"], e["n_returned"], e["n_total_reported"]))
        sys.stdout.flush()
        if e["http_status"] == 200:
            got = True
            break
    print("  -> %s %s" % (qid, "RECOVERED" if got else "STILL FAILING"))
    sys.stdout.flush()

# (b) RePEc alternate-interface probes ------------------------------------------
REPEC_ALT = [
 dict(qid="ks-repec-01-b", platform="repec", stratum="S1-venue-and-contract-families",
      instrument="event contract", strategy="market making", venue="Kalshi",
      cap="platform offers no cap parameter; platform default page size in force",
      note=("Alternate-interface probe. The IDEAS htsearch endpoint answered ks-repec-01 with HTTP 200 carrying its "
            "search FORM and zero result rows, and the page states 'IDEAS is struggling with massive bot traffic'. "
            "This retry adds the cmd=Search! submit parameter to test whether the query executes at all."),
      url="https://ideas.repec.org/cgi-bin/htsearch?q=Kalshi+event+contract+market+making&cmd=Search%21&form=extended&wm=wrd&wf=4BFF&s=R"),
 dict(qid="ks-repec-01-c", platform="repec", stratum="S1-venue-and-contract-families",
      instrument="event contract", strategy="market making", venue="Kalshi",
      cap="platform offers no cap parameter; platform default page size in force",
      note=("Alternate-interface probe against EconPapers, a RePEc service, after the IDEAS interface failed to "
            "execute the query. Recorded as a within-source interface substitution, not a new platform."),
      url="https://econpapers.repec.org/scripts/search.pf?ft=Kalshi+event+contract+market+making&adv=true&wp=on&art=on&bkchp=on&soft=on"),
 dict(qid="ks-repec-02-b", platform="repec", stratum="S2-sports-and-sportsbook-vs-exchange",
      instrument="event contract", strategy="arbitrage", venue="sportsbook betting exchange",
      cap="platform offers no cap parameter; platform default page size in force",
      note="Alternate-interface probe; see ks-repec-01-c.",
      url="https://econpapers.repec.org/scripts/search.pf?ft=sportsbook+betting+exchange+arbitrage+event+contract&adv=true&wp=on&art=on&bkchp=on&soft=on"),
 dict(qid="ks-repec-03-b", platform="repec", stratum="S4-macro-event-contracts",
      instrument="macroeconomic event contract", strategy="hedging", venue=None,
      cap="platform offers no cap parameter; platform default page size in force",
      note="Alternate-interface probe; see ks-repec-01-c.",
      url="https://econpapers.repec.org/scripts/search.pf?ft=macroeconomic+event+contract+prediction+market+hedging&adv=true&wp=on&art=on&bkchp=on&soft=on"),
 dict(qid="ks-repec-04-b", platform="repec", stratum="S3-weather-and-climate-event-contracts",
      instrument="weather event contract", strategy="hedging", venue=None,
      cap="platform offers no cap parameter; platform default page size in force",
      note="Alternate-interface probe; see ks-repec-01-c.",
      url="https://econpapers.repec.org/scripts/search.pf?ft=weather+event+contract+temperature+hedging+prediction+market&adv=true&wp=on&art=on&bkchp=on&soft=on"),
]
for q in REPEC_ALT:
    e = run_arm.execute(q, attempt=0, retry_of=q["qid"].rsplit("-", 1)[0])
    print("%-16s status=%-6s n=%-4s bytes=%s" % (e["query_id"], e["http_status"], e["n_returned"], e["payload_bytes"]))
    sys.stdout.flush()
    time.sleep(3)
print("recovery pass complete")
