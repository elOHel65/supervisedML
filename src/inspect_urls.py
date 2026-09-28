import csv
from collections import Counter, defaultdict

filename = "data/PhiUSIIL_Phishing_URL_Dataset.csv"

total = 0
blank_urls = 0
blank_labels = 0
url_counts = Counter()
url_labels = defaultdict(set)

with open(filename, encoding="utf-8-sig", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        total += 1
        url = row["URL"].strip()
        label = row["label"].strip()

        if not url:
            blank_urls += 1
        if not label:
            blank_labels += 1

        if url and label:
            url_counts[url] += 1
            url_labels[url].add(label)

repeated_urls = sum(count > 1 for count in url_counts.values())
extra_rows = sum(count - 1 for count in url_counts.values())
conflicting_urls = sum(len(labels) > 1 for labels in url_labels.values())

print("Total rows:", total)
print("Blank URLs:", blank_urls)
print("Blank labels:", blank_labels)
print("URLs appearing more than once:", repeated_urls)
print("Extra rows from repeats:", extra_rows)
print("URLs with conflicting labels:", conflicting_urls)