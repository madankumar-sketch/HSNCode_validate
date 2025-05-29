import pandas as pd
from difflib import get_close_matches
from google.adk.tools import Tool
from google.adk.agents import Agent

# Load HSN codes
hsn_df = pd.read_excel("hsn_codes.xlsx")

def validate_hsn_code(hsn_code: str) -> str:
    hsn_code = hsn_code.strip()
    if hsn_code in hsn_df['HSN_Code'].astype(str).values:
        desc = hsn_df.loc[hsn_df['HSN_Code'].astype(str) == hsn_code, 'Description'].values[0]
        return f"HSN code {hsn_code} is valid. Description: {desc}"
    else:
        all_codes = hsn_df['HSN_Code'].astype(str).tolist()
        suggestions = get_close_matches(hsn_code, all_codes, n=3, cutoff=0.6)
        if suggestions:
            return f"HSN code {hsn_code} is invalid. Did you mean: {', '.join(suggestions)}?"
        else:
            return f"HSN code {hsn_code} is invalid and no close matches were found."

hsn_validation_tool = Tool(
    name="hsn_validation",
    description="Validates an HSN code and provides description or suggestions.",
    func=validate_hsn_code
)

hsn_agent = Agent(
    name="hsn_code_validator",
    model="gemini-2.0-flash",
    instruction="You validate HSN codes and provide descriptions or suggestions.",
    description="An agent that validates HSN codes from a predefined Excel database.",
    tools=[hsn_validation_tool]
)

# Direct function call (recommended for fast validation)
print(validate_hsn_code("0101"))

# Or invoke the agent for a natural language query
response = hsn_agent.invoke("Is HSN code 0101 valid?")
print(response.text)
