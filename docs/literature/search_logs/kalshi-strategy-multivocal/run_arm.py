# -*- coding: utf-8 -*-
"""Import shim. `run_arm` is the module name the ACADEMIC-arm scripts import.

The arm executor was archived as ks-academic-runner.py, a hyphenated filename that is not a
legal Python module name, so `import run_arm` in ks-academic-recovery-pass.py and
ks-academic-query-table-supplementary.py had no module to bind to and both failed at import.
This shim restores the binding WITHOUT renaming the archived file, whose name is cited
elsewhere in the corpus record.

It loads the archived source and re-exports its public surface. It adds nothing and changes
no behaviour: ks-academic-runner.py remains the single source of truth for how a query is
executed and logged.

Loading this module runs the archived module body, which asserts PYTHONHASHSEED=0 at entry
(protocol section 3.0). It does NOT issue any request: the executor's network work is behind
execute(), and its main() is behind an `if __name__ == "__main__"` guard.
"""
import importlib.util
import os

_SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ks-academic-runner.py")

_spec = importlib.util.spec_from_file_location(__name__ + "._archived_source", _SRC)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)

# execute() is the only name ks-academic-recovery-pass.py and
# ks-academic-query-table-supplementary.py call; the rest are re-exported so that this shim
# is a faithful stand-in for the module the run imported.
execute = _mod.execute
main = _mod.main
fetch = _mod.fetch
now = _mod.now
ext_for = _mod.ext_for
count_records = _mod.count_records
QUERIES = _mod.QUERIES
LOGDIR = _mod.LOGDIR
PAYDIR = _mod.PAYDIR
RELLOG = _mod.RELLOG
PAUSE = _mod.PAUSE
RETRY_WAITS = _mod.RETRY_WAITS
REGISTRATION_COMMIT = _mod.REGISTRATION_COMMIT
PROTOCOL_SHA256 = _mod.PROTOCOL_SHA256

__all__ = ["execute", "main", "fetch", "now", "ext_for", "count_records", "QUERIES",
           "LOGDIR", "PAYDIR", "RELLOG", "PAUSE", "RETRY_WAITS",
           "REGISTRATION_COMMIT", "PROTOCOL_SHA256"]
