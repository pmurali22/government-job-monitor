from app.config import settings

class AISummarizer:
    def summarize(self, text: str) -> str:
        if not settings.GEMINI_API_KEY:
            return text[:400] + '...'
        return 'Summarized job description.'
