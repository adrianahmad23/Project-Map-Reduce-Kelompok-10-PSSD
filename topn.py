#!/usr/bin/env python3
import sys
import pandas as pd

#baca hasil reducer
data = []
for line in sys.stdin:
    word, count = line.strip().split("\t")
    data.append((word, int(count)))

df = pd.DataFrame(data, columns=["word", "count"])
df_sorted = df.sort_values(by="count", ascending=False)

#tampilkan Top 20 kata
print(df_sorted.head(20).to_csv(index=False))

#simpan Top 20 ke CSV
df_sorted.head(20).to_csv("top20_output.csv", index=False)
