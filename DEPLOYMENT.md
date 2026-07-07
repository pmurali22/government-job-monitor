# Backend Deployment Guide

This guide explains how to deploy the government-job-monitor API backend to various cloud platforms.

## Deployment Platforms

### Option 1: Google Cloud Run (Recommended - Free Tier)

**Best for:** Serverless, auto-scaling, pay-per-use model, generous free tier

**Setup:**
1. Create a Google Cloud project: https://console.cloud.google.com/
2. Enable these APIs:
   - Cloud Run
   - Container Registry
   - Cloud Build

3. Create a service account:
   ```bash
   gcloud iam service-accounts create github-deployer
   gcloud projects add-iam-policy-binding PROJECT_ID \
     --member=serviceAccount:github-deployer@PROJECT_ID.iam.gserviceaccount.com \
     --role=roles/run.admin
   gcloud iam service-accounts add-iam-policy-binding \
     github-deployer@PROJECT_ID.iam.gserviceaccount.com \
     --role=roles/iam.serviceAccountUser \
     --member=serviceAccount:github-deployer@PROJECT_ID.iam.gserviceaccount.com
   ```

4. Set up Workload Identity:
   - Follow: https://github.com/google-github-actions/auth#setup

5. Add these GitHub Secrets:
   - `GCP_PROJECT_ID` - Your GCP project ID
   - `GCP_WORKLOAD_IDENTITY_PROVIDER` - From Workload Identity setup
   - `GCP_SERVICE_ACCOUNT` - github-deployer@PROJECT_ID.iam.gserviceaccount.com
   - `DATABASE_URL` - PostgreSQL connection string
   - `SECRET_KEY` - Random secret key for FastAPI
   - `GEMINI_API_KEY` - (optional) Google Gemini API key
   - `EMAIL_FROM` - Email address for notifications
   - `TELEGRAM_BOT_TOKEN` - (optional) Telegram bot token
   - `TELEGRAM_CHAT_ID` - (optional) Telegram chat ID

6. Push to main branch - GitHub Actions will automatically deploy

### Option 2: Render.com (Easy - Free Tier Available)

**Best for:** Simple deployment, GitHub integration, UI-based configuration

**Setup:**
1. Sign up: https://dashboard.render.com
2. Connect your GitHub repository
3. Create a new "Web Service"
4. Select the repository and branch (main)
5. Set the Build command: `pip install -r backend/requirements.txt`
6. Set the Start command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
7. Set environment variables in Render dashboard
8. Deploy!

### Option 3: Fly.io (Modern - Free Tier)

**Best for:** Global deployment, minimal latency, modern infrastructure

**Setup:**
1. Sign up: https://fly.io
2. Install flyctl: `curl -L https://fly.io/install.sh | sh`
3. Authenticate: `fly auth login`
4. Run from backend directory: `fly launch`
5. Configure environment variables:
   ```bash
   fly secrets set DATABASE_URL="..."
   fly secrets set SECRET_KEY="..."
   # ... set other secrets
   ```
6. Deploy: `fly deploy`

**Manual deployment commands:**
```bash
cd backend
fly launch --name government-job-monitor-api
fly deploy
```

### Option 4: DigitalOcean App Platform ($7/month minimum)

**Best for:** Reliable hosting, good documentation

**Setup:**
1. Create account: https://www.digitalocean.com/
2. Create App Platform deployment
3. Connect GitHub repository
4. Select backend directory as root
5. Set environment variables
6. Deploy

### Option 5: Self-Hosted with Docker

If you prefer to host yourself:
1. Build the image: `docker build -f backend/Dockerfile -t job-monitor-api .`
2. Run: `docker run -e DATABASE_URL="..." -p 8000:8000 job-monitor-api`

## Environment Variables Required

All deployments need these variables:
- `DATABASE_URL` - PostgreSQL connection string (e.g., `postgresql://user:pass@host:5432/dbname`)
- `SECRET_KEY` - Random string for JWT signing
- `GEMINI_API_KEY` - (optional) For AI summarization features
- `EMAIL_FROM` - Email address for notifications
- `TELEGRAM_BOT_TOKEN` - (optional) For Telegram notifications
- `TELEGRAM_CHAT_ID` - (optional) Telegram channel ID

## Database Setup

For production, use a managed PostgreSQL database:
- **Google Cloud SQL** (with GCP)
- **Render PostgreSQL** (with Render)
- **DigitalOcean Managed Database**
- **Heroku Postgres** (legacy)
- **AWS RDS**

## Verify Deployment

After deployment, test the API:
```bash
curl https://your-deployed-url/health
curl https://your-deployed-url/docs  # API documentation
```

## Frontend Configuration

Once backend is deployed, update the frontend environment variable:

For Vercel, set `VITE_API_URL` to your backend URL (e.g., `https://government-job-monitor-api.onrender.com`)

Then redeploy the frontend:
```bash
cd frontend
VITE_API_URL=https://your-backend-url npm run build
npx vercel --prod
```

## Troubleshooting

### Port Issues
- Railway, Render, Fly.io all use the `PORT` environment variable
- Our Docker image uses `${PORT:-8000}` so it defaults to 8000 locally
- Platform assigns `PORT` dynamically at runtime

### Database Connection
- Ensure database firewall allows incoming connections from your deployment region
- Test connection string locally before deploying
- Check logs: Most platforms provide log viewers in their dashboards

### Environment Variables Not Loading
- Ensure all secrets are properly set in the platform's dashboard
- Restart the service after adding/updating secrets
- Check that variable names match exactly (case-sensitive)

## Next Steps

1. Choose your preferred deployment platform
2. Follow that platform's setup instructions
3. Add required GitHub Secrets (or platform dashboard variables)
4. Push code or manually trigger deployment
5. Test the live API endpoint
6. Update frontend API URL and redeploy
7. Monitor logs and performance in the platform dashboard
