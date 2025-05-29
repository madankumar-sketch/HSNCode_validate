# handlers/agent.py
from google.adk.agents.llm_agent import Agent
from handlers.hsn_handlers import (
    validate_hsn_code_handler,
    suggest_hsn_code_handler,
    get_hsn_description_handler,
)

agent = Agent(
    name="hsn_validation_agent",
    description="Agent that validates and describes HSN codes.",
    intent_handlers={
        "validate_hsn_code": validate_hsn_code_handler,
        "suggest_hsn_code": suggest_hsn_code_handler,
        "get_hsn_description": get_hsn_description_handler,
    }
)
