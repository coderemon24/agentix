"""
Backward-compatibility alias for scripts/agx.py
"""
import sys
from pathlib import Path

# Redirect directly to agx
agx_path = Path(__file__).parent / "agx.py"
if agx_path.exists():
    with open(agx_path, "r", encoding="utf-8") as f:
        code = compile(f.read(), str(agx_path), "exec")
        exec(code, {"__name__": "__main__"})
