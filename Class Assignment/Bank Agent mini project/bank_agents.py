accounts_db = {
    "Asiya": {"pin": "1234", "balance": 5000},
}

def is_authenticated(name, pin):
    return name in accounts_db and accounts_db[name]["pin"] == pin

def bank_agent(name, pin, user_input):
    if "balance" in user_input.lower():
        balance = accounts_db[name]["balance"]
        return f"[Bank Agent] Your account balance is: Rs. {balance}"
    else:
        return "[Bank Agent] Sorry, I didn't understand your request."
