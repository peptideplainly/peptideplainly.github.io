#!/usr/bin/env python3
"""Fetch recent peptide papers from PubMed E-utilities. Usage: python fetch_papers.py [days] > papers.json"""
import json, sys, time, urllib.parse, urllib.request, xml.etree.ElementTree as ET
BASE="https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
TOPICS={"BPC-157":'"BPC-157" OR "BPC 157" OR "body protection compound"',
"GLP-1 agonists":'semaglutide OR tirzepatide OR retatrutide',
"TB-500 / thymosin":'"thymosin beta-4" OR "TB-500"',
"Collagen peptides":'"collagen peptides" OR "collagen hydrolysate"',
"Antimicrobial peptides":'"antimicrobial peptides"[Title]',
"GHK-Cu":'"GHK-Cu" OR "copper peptide"'}
def get(ep,**p):
    p.update(tool="peptideplainly",email="none@example.com")
    with urllib.request.urlopen(BASE+ep+"?"+urllib.parse.urlencode(p),timeout=30) as r: return r.read()
def search(q,days,n=8):
    d=json.loads(get("esearch.fcgi",db="pubmed",term=f"({q}) AND hasabstract",reldate=days,datetype="edat",retmax=n,retmode="json",sort="relevance"))
    return d["esearchresult"]["idlist"]
def fetch(ids):
    root=ET.fromstring(get("efetch.fcgi",db="pubmed",id=",".join(ids),retmode="xml"));out=[]
    for a in root.iter("PubmedArticle"):
        t=lambda x:"".join(a.find(x).itertext()) if a.find(x) is not None else ""
        abs_=[((e.get("Label")+": ") if e.get("Label") else "")+"".join(e.itertext()) for e in a.iter("AbstractText")]
        pmid=t(".//PMID")
        out.append(dict(pmid=pmid,title=t(".//ArticleTitle"),journal=t(".//Journal/Title"),
          types=[ "".join(x.itertext()) for x in a.iter("PublicationType")],abstract="\n".join(abs_),
          url=f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"))
    return out
if __name__=="__main__":
    days=int(sys.argv[1]) if len(sys.argv)>1 else 14;res={}
    for k,q in TOPICS.items():
        ids=search(q,days);time.sleep(0.4)
        res[k]=fetch(ids) if ids else [];time.sleep(0.4)
    json.dump(res,sys.stdout,indent=1)
