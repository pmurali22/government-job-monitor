from typing import List, Optional
from fastapi import APIRouter, Query
from app.db.base import SessionLocal
from app.db.models import Job

router = APIRouter()

@router.get('/')
def list_jobs(q: Optional[str] = Query(None), limit: int = 20, offset: int = 0):
    db = SessionLocal()
    query = db.query(Job)
    if q:
        query = query.filter(Job.title.ilike(f'%{q}%') | Job.company.ilike(f'%{q}%') | Job.location.ilike(f'%{q}%'))
    jobs = query.order_by(Job.scraped_at.desc()).limit(limit).offset(offset).all()
    return jobs

@router.get('/{job_id}')
def get_job(job_id: int):
    db = SessionLocal()
    job = db.query(Job).filter(Job.id == job_id).first()
    if not job:
        return {'detail': 'Not found'}
    return job
