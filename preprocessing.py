import re

#file input & output
input_file = "C:/hadoop/bin/wordcount/pageviews-20250901-000000.txt"
output_file = "C:/hadoop/bin/wordcount/pageviews-20250901-000000-clean.txt"

stopwords = {"a", "an", "the", "and", "of", "in", "on", "at", "s", "n", "de", "la"}

with open(input_file, "r", encoding="utf-8") as fin, open(output_file, "w", encoding="utf-8") as fout:
    for line in fin:
        parts = line.strip().split(" ")
        if len(parts) >= 2:
            page_title = parts[1]

            #cleaning dasar
            page_title = re.sub(r"[^A-Za-z0-9_]", " ", page_title)   #simbol → spasi
            page_title = page_title.replace("_", " ").lower()        #underscore → spasi + lowercase
            page_title = re.sub(r"\s+", " ", page_title).strip()     #rapikan spasi berlebih

            #tokenisasi + filter
            tokens = [
                t for t in page_title.split()
                if len(t) > 1 and t not in stopwords
            ]
            cleaned_title = " ".join(tokens)

            if page_title:  #kalau hasilnya tidak kosong
                fout.write(page_title + "\n")

print(f"[INFO] Preprocessing selesai → {output_file}")