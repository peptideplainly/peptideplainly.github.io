"""Issues are built by make_site.py now: only the newest issue marked `sent: true` is published, at /newsletter.html.
Kept so existing routines still work. Usage: .venv/bin/python build.py"""
import pathlib,sys
sys.path.insert(0,str(pathlib.Path(__file__).parent)); import make_site  # noqa: F401  (building happens on import)
