from re import findall

file = open("other/examinf/24/986.txt").read()

print(len(max(findall(r"(?:[CDF][ACDFO][AO])+", file), key=len)) // 3)
