from hsn_validation_tool import agent, handle_intent

if __name__ == "__main__":
    print(handle_intent("validate_hsn_code", {"hsn_code": "0101"}))
