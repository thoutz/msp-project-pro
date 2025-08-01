
# MSP Project Management App

A streamlined project management platform designed for MSP (Managed Service Provider) workflows.

---

## 🚀 Quickstart (Local + Docker)

### **1. Clone & Navigate**
```bash
git clone <repo-url>
cd msp_pm_app
```

---

### **2. Environment Variables**
Copy `.env.example` to `.env` in `backend`:
```bash
cp backend/.env.example backend/.env
```
Edit the values for:
- `DATABASE_URL`
- `SECRET_KEY`
- `AUTOTASK_API_KEY`
- Email credentials if using email ingestion

---

### **3. Run with Docker**
```bash
docker-compose up --build
```

This starts:
- Backend API (FastAPI) on `http://localhost:8000`
- Frontend React app on `http://localhost:3000`
- Postgres DB
- Redis worker

---

### **4. Access**
- API Docs: `http://localhost:8000/docs`
- Frontend UI: `http://localhost:3000`

---

## 🛠 Development Setup (Cursor / Local Dev)

### **Backend**
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

---

### **Frontend**
```bash
cd frontend
npm install
npm run dev
```

---

## 📂 Project Structure

### Backend
```
backend/app/
  main.py            # API entrypoint
  config.py          # Env config
  database.py        # DB connection
  models/            # SQLAlchemy models
  routers/           # API routes
  services/          # Business logic (Autotask, Email, SLA, Billing)
```

### Frontend
```
frontend/src/
  components/        # React components (Dashboard, SLAWidget, AutomationBuilder)
  pages/             # Page layouts
  api/               # Axios API calls
```

---

## 🔄 Phase Overview
- **Phase 1**: Core API, DB models, Auth
- **Phase 2**: Autotask API, Email ingestion
- **Phase 3**: SLA Dashboard
- **Phase 4**: Automation Builder
- **Phase 5**: Billing + Invoices
- **Phase 6**: UI Polish + Deployment

---

## 📌 Notes
- SLA, Automation, and Billing have placeholder stubs to expand
- Ready for Cursor import
- Autotask integration requires API credentials
