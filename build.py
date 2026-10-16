"""Render issues/*.md to HTML with shared layout. Usage: .venv/bin/python build.py"""
import markdown,pathlib,sys
sys.path.insert(0,str(pathlib.Path(__file__).parent)); import make_site as S
for md in sorted((S.P/"issues").glob("issue-*.md")):
    n=md.stem.split("-")[1].lstrip("0"); rel=f"issues/{md.name[:-3]}.html"
    body='<article class="issue">'+markdown.markdown(md.read_text(),extensions=["extra","nl2br"])+"</article>"
    (S.P/rel).write_text(S.page(rel,f"Peptide Plainly Issue #{n}: new peptide research, explained","Plain-language summaries of new peptide studies, with PubMed links and honest limitations.",body,[S.ORG,{"@type":"Article","headline":f"Peptide Plainly Issue #{n}","url":f"{S.BASE}/{rel}","datePublished":"2026-10-16","author":{"@id":S.BASE+"/#org"},"publisher":{"@id":S.BASE+"/#org"}}]))
