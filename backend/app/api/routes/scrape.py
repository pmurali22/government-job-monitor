from fastapi import APIRouter
from app.services.scraper import ScraperService

router = APIRouter()

@router.post('/')
def trigger_scrape():
    ScraperService().run_all()
    return {'status': 'Scrape started'}
