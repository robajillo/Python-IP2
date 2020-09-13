import os

class Config:
    NEWS_API_BASE_URL='https://newsapi.org/v2/sources?country=us&category={}&apiKey={}'
    NEWS_API_KEY=os.environ.get("NEWS_API_KEY")
    SECRET_KEY = os.environ.get('SECRET_KEY')