# extract.py
import pandas as pd

input_path = "data/raw/customers.csv"

extracted_data = pd.read_csv(input_path)

extracted_data.to_csv("data/stage/extracted.csv", index=False)

print("✅ Extracted data saved to data/stage/extracted.csv")