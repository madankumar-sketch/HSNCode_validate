# tools/hsn_tool.py
import pandas as pd

class HSNCodeTool:
    def __init__(self, excel_path="hsn_codes.xlsx"):
        self.df = pd.read_excel(excel_path)

    def validate_code(self, code):
        return str(code) in self.df["HSN Code"].astype(str).values

    def suggest_codes(self, partial_code):
        return self.df[self.df["HSN Code"].astype(str).str.startswith(str(partial_code))]["HSN Code"].tolist()

    def get_description(self, code):
        match = self.df[self.df["HSN Code"].astype(str) == str(code)]
        if not match.empty:
            return match["Description"].values[0]
        return "No description found for this HSN code."
