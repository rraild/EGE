import re

from docx import Document

doc = Document("mar/task10-02.03/3.docx")
full_text = []

for para in doc.paragraphs:
    full_text.append(para.text)

text = "\n".join(full_text)

words = re.findall(r"[a-zA-Z]+", text)

print(len(words))
