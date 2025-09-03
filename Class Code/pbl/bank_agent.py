from agents import Agent, Runner, function_tool, RunContextWrapper, input_guardrail, GuardrailFunctionOutput
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

class Account(BaseModel):
    name:str
    pin:int

# class My_Output(BaseModel):
#     name:str
#     balance:str

class Guardrail_Output(BaseModel):
    is_not_bank_related:bool

guardrail_agent = Agent(
    name="Gaurdrail Agent",
    instructions="You are a guardrail agent. You check if the user is asking you bank related quiries",
    output_type=Guardrail_Output,
)

@input_guardrail
async def check_bank_related(ctx:RunContextWrapper[None],agent:Agent,input:str)->GuardrailFunctionOutput:
    
    result= await Runner.run(guardrail_agent,input,context=ctx.context)
    guardrail_instence=GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=result.final_output.is_not_bank_related
    )

def check_user(ctx:RunContextWrapper[Account],agent:Agent)->bool:
    if ctx.context.name == "Asiya" and ctx.context.pin == 1234:
        return True
    else:
        return False

@function_tool(is_enabled=check_user)
def check_balance(account_number: str) -> str:
    return f"The balance of acount is $10000"

bank_agent = Agent(
    name='Bank Agent',
    instructions='you are bank agent. You help customer with their question related to bank accounts and there blanace information but to sure the user authenticated.',
    tools=[check_balance],
    input_guardrails=[check_bank_related]

)

user_context= Account(name="Asiya", pin=1234)

result= Runner.run_sync(bank_agent, "I want to my balance my account number is 09876567", context=user_context)
print(result.final_output)