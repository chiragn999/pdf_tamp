import fitz

# Define paths to the PDF files
cv1_path = r"C:\Users\chira\Downloads\cv1.pdf"  # Path to the first CV
cv2_path = r"C:\Users\chira\Downloads\cv2.pdf"  # Path to the second CV

# Attempt to open both documents
try:
    doc1 = fitz.open(cv1_path)
    doc2 = fitz.open(cv2_path)
except Exception as e:
    print(f"An error occurred while opening the files: {e}")
    exit(1)

from pprint import pprint

# Print the metadata of both documents
pprint(doc1.metadata)
pprint(doc2.metadata)