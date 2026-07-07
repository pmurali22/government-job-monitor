from fastapi import FastAPI
from app.api.routes import auth, jobs, scrape
import app.tasks  # noqa: F401

app = FastAPI(title='Job Monitor API')
app.include_router(auth.router, prefix='/api/auth', tags=['auth'])
app.include_router(jobs.router, prefix='/api/jobs', tags=['jobs'])
app.include_router(scrape.router, prefix='/api/scrape', tags=['scrape'])

@app.get('/')
def root():
    return {'status': 'Job Monitor API is running'}
