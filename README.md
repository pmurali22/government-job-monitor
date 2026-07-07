# Government Job Monitor System

A full-stack monitoring platform for government job postings with scraping, summarization, notifications, and analytics.

## Stack
- Backend: FastAPI + SQLAlchemy + PostgreSQL
- Frontend: React + TypeScript + Vite
- Notifications: Email + Telegram
- AI: Google Gemini API
- Deployment: Render (backend), Vercel (frontend)

## Local Setup
1. Create a Python virtual environment in backend
2. Install backend dependencies
3. Install frontend dependencies
4. Configure environment variables in backend/.env.example and frontend/.env.example

## Project Structure
- `backend/` - FastAPI backend, database models, scrapers, notification services
- `frontend/` - React dashboard and auth UI
- `docker-compose.yml` - local development environment
