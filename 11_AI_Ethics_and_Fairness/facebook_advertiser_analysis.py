#!/usr/bin/env python3
# Example usage (PowerShell or Terminal):
#
# 1) Extract advertisers, sample, and create labeling CSV:
# python path/to/ads_information/nanyanwu3_random_advertisers.py extract --in "path/to/facebook-export-root" --out "path/to/output/fb_out" --seed 6603
#
# 2) After you edit labeled_advertisers.csv (fill Category & Bucket):
# python path/to/ads_information/nanyanwu3_random_advertisers.py stats --in "path/to/output/fb_out" --out "path/to/output/fb_out"

import os, re, json, argparse, random, csv, sys
from html.parser import HTMLParser
from typing import List, Dict, Any
import pandas as pd

TARGETS = {
    "advertisers_using_your_activity_or_information",
    "advertisers_you've_interacted_with",
    "advertisers_who_uploaded_a_contact_list_with_your_information",
}
BUCKETS = {"Relevant", "Not Relevant", "Way Off"}
REG_KEYS = {
    "Credit": ["bank","credit","loan","lender","mortgage","financ","card","union"],
    "Education": ["university","college","academy","school","learning","edx","coursera","bootcamp"],
    "Employment": ["recruit","hiring","careers","jobs","indeed","talent"],
    "Housing & Public Accommodation": ["apartments","realty","realtor","homes","hotel","inn","resort"],
}

def mkdir(p): os.makedirs(p, exist_ok=True)
def stem(s): return re.sub(r'[^a-z0-9]+', ' ', str(s).lower()).strip()

def write_csv(path: str, rows: List[Dict[str, Any]], header: List[str]):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=header); w.writeheader(); w.writerows(rows)

class LIParser(HTMLParser):
    def __init__(self): super().__init__(); self.in_li=False; self.buf=[]; self.items=[]
    def handle_starttag(self, tag, attrs): 
        if tag.lower()=="li": self.in_li=True; self.buf=[]
    def handle_endtag(self, tag):
        if tag.lower()=="li" and self.in_li:
            t="".join(self.buf).strip()
            if t: self.items.append(t)
            self.in_li=False
    def handle_data(self, data): 
        if self.in_li: self.buf.append(data)

def find_files(root: str) -> List[str]:
    out=[]
    for d,_,fs in os.walk(root):
        for fn in fs:
            base=os.path.splitext(fn)[0].lower()
            if (fn.lower().endswith((".json",".html")) and any(base.startswith(t) for t in TARGETS)):
                out.append(os.path.join(d, fn))
    return out

def pull_from_json(obj: Any) -> List[str]:
    out=[]
    def walk(x):
        if isinstance(x, dict):
            for k in ("advertiser_name","name","title"):
                v=x.get(k); 
                if isinstance(v,str) and v.strip(): out.append(v.strip())
            for v in x.values(): walk(v)
        elif isinstance(x, list): 
            for v in x: walk(v)
        elif isinstance(x,str) and x.strip(): out.append(x.strip())
    walk(obj); return out

def load_names(path: str) -> List[str]:
    try:
        if path.lower().endswith(".json"):
            with open(path, "r", encoding="utf-8") as f: data=json.load(f)
            names=pull_from_json(data)
        else:
            p=LIParser(); 
            with open(path,"r",encoding="utf-8") as f: p.feed(f.read())
            names=p.items
    except Exception as e:
        print(f"⚠️ Parse failed {os.path.basename(path)}: {e}", file=sys.stderr); names=[]
    # clean
    out=[]
    for n in names:
        n=re.sub(r"\s+"," ",str(n)).strip().strip("'\"[]()")
        if n: out.append(n)
    # dedupe
    seen=set(); uniq=[]
    for s in out:
        k=s.lower()
        if k not in seen: seen.add(k); uniq.append(s)
    return uniq

def detect_reg(names: List[str]) -> List[Dict[str, Any]]:
    rows=[]
    for nm in names:
        st=stem(nm); hit=[]
        for dom,keys in REG_KEYS.items():
            if any(k in st for k in keys): hit.append(dom)
        rows.append({"Advertiser": nm, "Domains": "; ".join(sorted(set(hit))) if hit else ""})
    return rows

# -------- commands --------
def do_extract(a):
    mkdir(a.out)
    files=find_files(a.input)
    if not files:
        raise SystemExit(f"No advertiser files under: {a.input}")

    print("Discovered files:"); [print("  -", f) for f in files]

    all_names=[]
    for f in files: all_names+=load_names(f)
    # final dedupe
    seen=set(); names=[]
    for s in all_names:
        k=s.lower()
        if k not in seen: seen.add(k); names.append(s)

    write_csv(os.path.join(a.out,"all_advertisers.csv"), [{"Advertiser":n} for n in names], ["Advertiser"])
    total=len(names); print(f"\nTotal unique advertisers found: {total}")
    if total==0: raise SystemExit("No advertisers parsed.")

    sample = int(round(total*(a.percent/100.0))) if a.percent is not None else int(round(total*0.10))
    sample = max(50, min(200, sample))
    if total < 50: print("⚠️ <50 total; using all."); sample=total
    sample=min(sample,total)

    random.seed(a.seed)
    picked=random.sample(names, sample)

    write_csv(os.path.join(a.out,"sampled_advertisers.csv"), [{"Advertiser":x} for x in picked], ["Advertiser"])
    write_csv(os.path.join(a.out,"labeled_advertisers.csv"), [{"Advertiser":x,"Category":"MISC","Bucket":""} for x in picked], ["Advertiser","Category","Bucket"])
    write_csv(os.path.join(a.out,"regulated_domains.csv"), detect_reg(names), ["Advertiser","Domains"])

    print("\nWrote:")
    print(" ", os.path.join(a.out,"all_advertisers.csv"))
    print(" ", os.path.join(a.out,"sampled_advertisers.csv"))
    print(" ", os.path.join(a.out,"labeled_advertisers.csv"), " <-- EDIT Category & Bucket")
    print(" ", os.path.join(a.out,"regulated_domains.csv"))

def do_stats(a):
    mkdir(a.out)
    path=os.path.join(a.input,"labeled_advertisers.csv")
    if not os.path.isfile(path): 
        raise SystemExit(f"Missing: {path}")

    df=pd.read_csv(path)
    need={"Advertiser","Category","Bucket"}
    if not need.issubset(df.columns): raise SystemExit("CSV needs: Advertiser, Category, Bucket")

    df["Category"]=df["Category"].fillna("MISC").astype(str).str.strip()
    df["Bucket"]=df["Bucket"].fillna("").astype(str).str.strip()

    bad=df.loc[~df["Bucket"].isin(list(BUCKETS)+[""]),"Bucket"].unique().tolist()
    if len(bad): print("⚠️ Invalid Bucket values:", bad, "Allowed:", sorted(BUCKETS))

    rows=[]; sankey=[]; catstats=[]
    counts=df.groupby("Category")["Advertiser"].count().to_dict()
    for c,n in counts.items(): sankey.append(f"FB Advertisers [{n}] {c}")

    for c, sub in df.groupby("Category"):
        t=len(sub); r=int((sub["Bucket"]=="Relevant").sum()); nr=int((sub["Bucket"]=="Not Relevant").sum()); w=int((sub["Bucket"]=="Way Off").sum())
        acc=round(r/t*100,2) if t else 0.0; rub=round(w/t*100,2) if t else 0.0
        rows += [
            {"Category":c,"Data Bucket":"Relevant","Count":r,"Accuracy (%)":acc,"Rubbish (%)":rub},
            {"Category":c,"Data Bucket":"Not Relevant","Count":nr,"Accuracy (%)":"","Rubbish (%)":""},
            {"Category":c,"Data Bucket":"Way Off","Count":w,"Accuracy (%)":"","Rubbish (%)":""},
            {"Category":c,"Data Bucket":"Total","Count":t,"Accuracy (%)":acc,"Rubbish (%)":rub},
        ]
        if r:  sankey.append(f"{c} [{r}] Relevant")
        if nr: sankey.append(f"{c} [{nr}] Not Relevant")
        if w:  sankey.append(f"{c} [{w}] Way Off")
        catstats.append((c,acc,rub))

    most = max(catstats, key=lambda x:x[1]) if catstats else None
    worst = max(catstats, key=lambda x:x[2]) if catstats else None

    stats_p=os.path.join(a.out,"stats_by_category.csv")
    sankey_p=os.path.join(a.out,"sankeymatic_input.txt")
    pd.DataFrame(rows).to_csv(stats_p, index=False)
    with open(sankey_p,"w",encoding="utf-8") as f: f.write("\n".join(sankey))

    print("Wrote:\n ", stats_p, "\n ", sankey_p)
    if most:  print(f"Most accurate: {most[0]} ({most[1]:.2f}%)")
    if worst: print(f"Least accurate: {worst[0]} ({worst[2]:.2f}%)")

def main():
    ap=argparse.ArgumentParser(description="CS6603 Facebook Assignment Helper (extract + stats)")
    sub=ap.add_subparsers(dest="cmd")

    p1=sub.add_parser("extract", help="Find files, sample, make labeling CSV")
    p1.add_argument("--in",  dest="input", required=True, help="Export root (folder that contains 'ads_information', etc.)")
    p1.add_argument("--out", dest="out", default="./out", help="Output folder")
    p1.add_argument("--percent", type=int, default=None, help="% of total to sample (50–200 cap). Default 10%")
    p1.add_argument("--seed", type=int, default=6603, help="RNG seed")
    p1.set_defaults(func=do_extract)

    p2=sub.add_parser("stats", help="Compute Accuracy/Rubbish and Sankey input")
    p2.add_argument("--in",  dest="input", default="./out", help="Folder with labeled_advertisers.csv")
    p2.add_argument("--out", dest="out", default="./out", help="Output folder")
    p2.set_defaults(func=do_stats)

    args=ap.parse_args()
    if not args.cmd: ap.print_help(); return
    args.func(args)

if __name__ == "__main__":
    main()
