#!/usr/bin/env python3
# Example:
# python stats_and_sankey.py --in "path/to/labeled_advertisers.csv" --out "path/to/fb_out" --coerce-not-reviewed

import os, argparse, sys
import pandas as pd

ALLOWED = {"Relevant", "Not Relevant", "Way Off"}

def main():
    ap = argparse.ArgumentParser(description="Per-category stats + Sankey input")
    ap.add_argument("--in",  dest="in_csv",  required=True, help="Path to labeled_advertisers.csv")
    ap.add_argument("--out", dest="out_dir", default=".",   help="Output folder")
    ap.add_argument("--coerce-not-reviewed", action="store_true",
                    help="Coerce non-allowed bucket values to 'Not Relevant'")
    args = ap.parse_args()

    os.makedirs(args.out_dir, exist_ok=True)
    rpt_path = os.path.join(args.out_dir, "bucket_value_report.txt")

    # load
    try:
        df = pd.read_csv(args.in_csv)
    except Exception as e:
        sys.exit(f"Couldn't read CSV: {e}")

    need = {"Advertiser","Category","Bucket"}
    if not need.issubset(df.columns):
        sys.exit("CSV must have columns: Advertiser, Category, Bucket")

    df["Advertiser"] = df["Advertiser"].astype(str).str.strip()
    df["Category"]   = df["Category"].astype(str).str.strip().replace({"": "MISC"})
    df["Bucket"]     = df["Bucket"].astype(str).str.strip()

    # bucket check / coerce
    uniq = sorted(df["Bucket"].unique())
    bad  = [b for b in uniq if b not in ALLOWED]
    notes = []
    if bad:
        if args.coerce_not_reviewed:
            df.loc[~df["Bucket"].isin(ALLOWED), "Bucket"] = "Not Relevant"
            notes.append("Coerced invalid bucket values -> 'Not Relevant': " + ", ".join(bad))
        else:
            notes += [
                "Found invalid bucket values (not in {Relevant, Not Relevant, Way Off}): " + ", ".join(bad),
                "Re-run with --coerce-not-reviewed or fix the CSV."
            ]
            with open(rpt_path, "w", encoding="utf-8") as f: f.write("\n".join(notes) + "\n")
            print("\n".join(notes)); sys.exit(1)

    # stats
    rows, sankey, cat_summ = [], [], []
    cat_cts = df.groupby("Category")["Advertiser"].count().to_dict()
    for cat, ct in sorted(cat_cts.items(), key=lambda x: x[0].lower()):
        sankey.append(f"FB Advertisers [{ct}] {cat}")

    for cat, sub in df.groupby("Category"):
        tot   = len(sub)
        rel   = int((sub["Bucket"] == "Relevant").sum())
        nrel  = int((sub["Bucket"] == "Not Relevant").sum())
        woff  = int((sub["Bucket"] == "Way Off").sum())
        acc   = round((rel/tot*100), 2) if tot else 0.0
        rub   = round((woff/tot*100), 2) if tot else 0.0

        rows += [
            {"Category": cat, "Data Bucket": "Relevant",     "Count": rel,  "Accuracy (%)": acc, "Rubbish (%)": rub},
            {"Category": cat, "Data Bucket": "Not Relevant", "Count": nrel, "Accuracy (%)": "",  "Rubbish (%)": ""},
            {"Category": cat, "Data Bucket": "Way Off",      "Count": woff, "Accuracy (%)": "",  "Rubbish (%)": ""},
            {"Category": cat, "Data Bucket": "Total",        "Count": tot,  "Accuracy (%)": acc, "Rubbish (%)": rub},
        ]
        if rel:  sankey.append(f"{cat} [{rel}] Relevant")
        if nrel: sankey.append(f"{cat} [{nrel}] Not Relevant")
        if woff: sankey.append(f"{cat} [{woff}] Way Off")

        cat_summ.append((cat, acc, rub))

    # winners
    m_acc = max(cat_summ, key=lambda x: x[1]) if cat_summ else None
    m_rub = max(cat_summ, key=lambda x: x[2]) if cat_summ else None

    # write
    stats_csv = os.path.join(args.out_dir, "stats_by_category.csv")
    sankey_txt = os.path.join(args.out_dir, "sankeymatic_input.txt")
    pd.DataFrame(rows).to_csv(stats_csv, index=False)
    with open(sankey_txt, "w", encoding="utf-8") as f: f.write("\n".join(sankey))

    if args.coerce_not_reviewed:
        notes.append("Bucket coercion enabled.")

    if m_acc: notes.append(f"Most accurate category: {m_acc[0]} ({m_acc[1]:.2f}%)")
    if m_rub: notes.append(f"Least accurate (highest rubbish): {m_rub[0]} ({m_rub[2]:.2f}%)")

    with open(rpt_path, "w", encoding="utf-8") as f:
        f.write("\n".join(notes) + ("\n" if notes else "No issues.\n"))

    print(f"Wrote:\n  - {stats_csv}\n  - {sankey_txt}\n  - {rpt_path}")
    if m_acc: print(f"Most accurate: {m_acc[0]} ({m_acc[1]:.2f}%)")
    if m_rub: print(f"Highest rubbish: {m_rub[0]} ({m_rub[2]:.2f}%)")

if __name__ == "__main__":
    main()
