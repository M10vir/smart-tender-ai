# 🧠 Smart Tender AI - RFP Automation Platform

Smart Tender AI is a full-stack, containerized application designed to automate RFP processing, budget analysis, and vendor scoring for public and enterprise procurement. Built with modern open-source technologies, it delivers an AI-powered solution from resume-like tender analysis to final dashboard visibility.

---

## 🧰 Built With

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?logo=streamlit)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-336791?logo=postgresql)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI/CD-2088FF?logo=githubactions)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-blue)
![GHCR](https://img.shields.io/badge/GitHub_Container_Registry-GHCR-0D1117?logo=github)


![Backend CI](https://github.com/M10vir/smart-tender-ai/actions/workflows/backend-ci.yml/badge.svg)
![Frontend CI](https://github.com/M10vir/smart-tender-ai/actions/workflows/frontend-ci.yml/badge.svg)
![GHCR Backend Image](https://ghcr-badge.dev/M10vir/smart-tender-ai/smart-tender-backend/latest)
![GHCR Frontend Image](https://ghcr-badge.dev/M10vir/smart-tender-ai/smart-tender-frontend/latest)

---

## 📐 Architecture Overview

![Architecture Diagram](docs/architecture.png)

---

## 📂 Project Structure

```
smart-tender-ai/
├── backend/                  # FastAPI application
│   ├── app/
│   │   ├── api/              # API route definitions
│   │   ├── models/           # Pydantic models
│   │   ├── services/         # Business logic
│   │   └── main.py           # FastAPI app entrypoint
│   ├── pyproject.toml        # Poetry project file
│   ├── requirements.txt      # Optional fallback
│   └── Dockerfile            # Backend Docker image
│
├── frontend/                 # Streamlit frontend
│   ├── streamlit_app.py      # Main Streamlit app
│   ├── requirements.txt      # Python packages
│   └── Dockerfile            # Frontend Docker image
│
├── docker/
│   └── docker-compose.yml    # Full-stack integration
│
├── .github/workflows/        # CI/CD pipelines
│
├── docs/
│   └── architecture.png      # Architecture diagram
│
└── README.md                 # This file
```

---

## 🚀 Getting Started

### Prerequisites

- Docker & Docker Compose
- GitHub account with GHCR access
- Python 3.11+ (for local dev)

### Run Full Stack Locally

```bash
git clone https://github.com/M10vir/smart-tender-ai.git
cd smart-tender-ai
docker-compose -f docker/docker-compose.yml up --build
```

- 📍 Visit frontend: [http://localhost:8501](http://localhost:8501)
- 📍 API docs: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🧪 Testing CI/CD & GHCR

### Manual Image Build + Push

```bash
# Backend
docker build -t ghcr.io/M10vir/smart-tender-backend:latest ./backend
docker push ghcr.io/M10vir/smart-tender-backend:latest

# Frontend
docker build -t ghcr.io/M10vir/smart-tender-frontend:latest ./frontend
docker push ghcr.io/M10vir/smart-tender-frontend:latest
```

### GitHub Actions

- Auto-publish triggered on push to `main` for `/frontend` or `/backend`
- Images published to [https://github.com/M10vir?tab=packages](https://github.com/M10vir?tab=packages)

---

## 🔒 Secrets and Git Ignore

Make sure `.env`, `.env-safe`, and other credentials are excluded and handled securely.
`.gitignore` is configured for Python, Streamlit, venvs, and CI artifacts.

---

## 📘 License

MIT License. Built with ❤️ by [M10vir](https://github.com/M10vir)
