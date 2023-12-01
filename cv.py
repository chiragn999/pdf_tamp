import fitz
doc1 = fitz.open(r"C:\Users\chira\Downloads\cv1.pdf")
doc2 = fitz.open(r"C:\Users\chira\Downloads\cv1.pdf")

from pprint import pprint
pprint(doc1.metadata)
pprint(doc2.metadata)