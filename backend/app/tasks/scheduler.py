from apscheduler.schedulers.background import BackgroundScheduler
from app.services.scraper import ScraperService

scheduler = BackgroundScheduler()

@scheduler.scheduled_job('interval', hours=6)
def scheduled_scrape():
    ScraperService().run_all()

scheduler.start()
