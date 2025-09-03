from bank_agents import bank_agent, is_authenticated
from typing import Dict

# Input Guardrails
def validate_pin(pin: str) -> bool:
    return pin.isdigit() and len(pin) == 4

def validate_name(name: str) -> bool:
    return name.isalpha()

# Agent 1: Balance Inquiry
def balance_agent(account_number: str, context: Dict):
    if context.get("pin") == "1234" and account_number == "12345678":
        return f"Hello {context['name']}, your balance is Rs. 50,000."
    else:
        return "Invalid account details or PIN."

# Agent 2: Transfer Money
def transfer_agent(account_number: str, amount: int, context: Dict):
    if context.get("pin") == "1234" and account_number == "12345678":
        return f"Successfully transferred Rs. {amount} from account {account_number}."
    else:
        return "Transfer failed. Invalid account details or PIN."

def main():
    name = input("Enter your name: ").strip()
    pin = input("Enter your 4-digit PIN: ").strip()

    # Input Guardrail Checks
    if not validate_name(name):
        print("❌ Invalid name. Use alphabetic characters only.")
        return

    if not validate_pin(pin):
        print("❌ Invalid PIN. Enter exactly 4 digits.")
        return

    context = {
        "name": name,
        "pin": pin
    }

    question = input("💬 Ask your bank question: ").lower().strip()

    # Agent Handoff Logic
    if "balance" in question:
        result = balance_agent("12345678", context)
    elif "transfer" in question:
        result = transfer_agent("12345678", 1000, context)
    else:
        result = "❓ Sorry, I couldn't understand your request."

    # Output Guardrail
    print("\n🤖 Bank Agent:\n", result)

if __name__ == "__main__":
    main()