import os
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
from dotenv import load_dotenv

load_dotenv()

def generate_rfp_from_objectives(title: str, objectives: str) -> str:
    llm = ChatOpenAI(model="gpt-4", temperature=0.5)

    messages = [
        SystemMessage(content="You are a procurement specialist generating government RFPs."),
        HumanMessage(content=f"""Create a formal Request for Proposal (RFP) for the following:
        
Tender Title: {title}

Project Objectives:
{objectives}

The RFP should include sections such as:
1. Introduction
2. Scope of Work
3. Deliverables
4. Timeline
5. Evaluation Criteria
6. Proposal Submission Instructions

Output in clear professional English (or Arabic if user input is in Arabic).
""")
    ]

    response = llm(messages)
    return response.content.strip()
