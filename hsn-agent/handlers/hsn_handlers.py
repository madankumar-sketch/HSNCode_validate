# handlers/hsn_handlers.py
from tools.hsn_tool import HSNCodeTool

tool = HSNCodeTool()

def validate_hsn_code_handler(inputs):
    code = inputs.get("hsn_code")
    is_valid = tool.validate_code(code)
    return {"valid": is_valid}

def suggest_hsn_code_handler(inputs):
    partial = inputs.get("partial_code", "")
    suggestions = tool.suggest_codes(partial)
    return {"suggestions": suggestions}

def get_hsn_description_handler(inputs):
    code = inputs.get("hsn_code")
    description = tool.get_description(code)
    return {"description": description}
