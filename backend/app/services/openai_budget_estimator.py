import os
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
from dotenv import load_dotenv

load_dotenv()

def estimate_budget_items(project_title: str, items: list) -> str:
    llm = ChatOpenAI(model="gpt-4", temperature=0.3)

    item_list = "\n".join([f"- {item.quantity} x {item.item}" for item in items])

    messages = [
        SystemMessage(content="You are a cost estimation expert for public sector projects."),
        HumanMessage(content=f"""Estimate the itemized budget for this project:

Project: {project_title}
Requested Items:
{item_list}

Provide estimated cost per item and total cost. Respond in a clean, readable format (like a table or bullet list).
""")
    ]

    response = llm(messages)
    return response.content.strip()
