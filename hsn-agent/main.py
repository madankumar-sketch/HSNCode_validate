from handlers.agent import agent

if __name__ == "__main__":
    print(agent.handle_intent("validate_hsn_code", {"hsn_code": "1234"}))
