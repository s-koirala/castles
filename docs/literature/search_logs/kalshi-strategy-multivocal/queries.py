# -*- coding: utf-8 -*-
"""Import shim. `queries` is the module name the ACADEMIC-arm scripts import.

The query table was archived as ks-academic-query-table.py, a hyphenated filename that is
not a legal Python module name, so `from queries import QUERIES` in ks-academic-runner.py,
ks-academic-recovery-pass.py and ks-academic-query-table-supplementary.py had no module to
bind to and every one of them failed at import. This shim restores the binding WITHOUT
renaming the archived file, whose name is cited elsewhere in the corpus record.

It loads the archived source and re-exports exactly the four names its importers use. It
adds nothing, computes nothing, and reads no data: the query table remains the single
source of truth for what was executed.

No PYTHONHASHSEED assert: this shim, like the table it loads, has no hash-order dependence.
The scripts that import it assert the seed at their own entry.
"""
import importlib.util
import os

_SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ks-academic-query-table.py")

_spec = importlib.util.spec_from_file_location(__name__ + "._archived_source", _SRC)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)

# The four names ks-academic-runner.py and ks-academic-query-table-supplementary.py import.
QUERIES = _mod.QUERIES              # the frozen query table, protocol section 3.1
CR = _mod.CR                        # Crossref endpoint prefix
CROSSREF_SEL = _mod.CROSSREF_SEL    # Crossref rows= and select= suffix
OA_MAIL = _mod.OA_MAIL              # OpenAlex polite-pool mailto suffix

__all__ = ["QUERIES", "CR", "CROSSREF_SEL", "OA_MAIL"]
