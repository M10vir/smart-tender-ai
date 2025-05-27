import os
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
from docx import Document
from fastapi import UploadFile
# import textract  # for .pdf and other formats
import tempfile

load_dotenv()

def extract_text_from_file(file: UploadFile) -> str:
    suffix = os.path.splitext(file.filename)[1].lower()

    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(file.file.read())
        tmp_path = tmp.name

    if suffix == ".docx":
        text = "\n".join([para.text for para in Document(tmp_path).paragraphs])
    else:
        # text = textract.process(tmp_path).decode("utf-8")
        raise ValueError("Only .docx files are supported in the MVP.")

    os.unlink(tmp_path)
    return text

def score_vendor_proposal(file: UploadFile) -> str:
    proposal_text = extract_text_from_file(file)

    llm = ChatOpenAI(model="gpt-4", temperature=0.3)

    messages = [
        SystemMessage(content="You are a proposal evaluator for public tenders."),
        HumanMessage(content=f"""
Evaluate the following vendor proposal and assign scores based on:

1. Understanding of Requirements (0–10)
2. Relevant Experience (0–10)
3. Timeline Feasibility (0–10)
4. Cost Competitiveness (0–10)

Proposal:
---
{proposal_text[:3000]}
---

Output the total score, score breakdown, and a brief justification.
""")
    ]

    response = llm(messages)
    return response.content.strip()
