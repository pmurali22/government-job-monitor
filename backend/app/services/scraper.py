from app.db.base import SessionLocal, Base, engine
from app.db.models import Job
from datetime import datetime

class ScraperService:
    def __init__(self):
        Base.metadata.create_all(bind=engine)

    def run_all(self):
        db = SessionLocal()
        job = Job(
            title='Sample Government Job',
            company='Official Agency',
            location='Remote',
            url='https://example.com/job/1',
            source='example',
            description='This is a sample government job posting.',
            summary='Summary pending',
            scraped_at=datetime.utcnow(),
        )
        if not db.query(Job).filter(Job.url == job.url).first():
            db.add(job)
            db.commit()
        db.close()
