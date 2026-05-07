"""
Agent with tool usage (advanced feature)
"""

from langchain.agents import initialize_agent, Tool
from langchain.chat_models import ChatOpenAI


def calculator_tool(input_str: str) -> str:
    """Simple calculator tool"""
    try:
        return str(eval(input_str))
    except Exception:
        return "Invalid calculation"


def load_agent(api_key):
    llm = ChatOpenAI(
        temperature=0,
        openai_api_key=api_key
    )

    tools = [
        Tool(
            name="Calculator",
            func=calculator_tool,
            description="Useful for math calculations"
        )
    ]

    agent = initialize_agent(
        tools,
        llm,
        agent="zero-shot-react-description",
        verbose=True
    )

    return agent
