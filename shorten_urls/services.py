import random
from utilis.logger import logger
from models.shorten_services_model import ShortenURL
import datetime
from flask_sqlalchemy import SQLAlchemy
from app import db


class ShortenServices:
 
    
# TASK --> Shortly
# 1. A form where we can post any URL and obtain a short version of the URL.
# 2. Accessing the short URL should redirect to the random URL.
# 3. Design and code models/views/forms in your choice of framework.
# 4. Bonus: Code to handle all edge cases, optimize for space/time, etc.

    def __init__(self, original_url,redirect_options,link_length) -> None:
        self.original_url = original_url
        self.redirect_options = redirect_options
        self.link_length = link_length
        self.logs_path = 'logs/shorten-urls.log'
        self.random_links = ["https://www.google.com","https://www.openai.com","https://github.com","https://stackoverflow.com","https://docs.python.org","https://flask.palletsprojects.com","https://developer.mozilla.org","https://www.w3schools.com","https://www.reddit.com","https://www.youtube.com"]
        logger(self.logs_path, 'info', 'Object initialized with ShortenServices class')

    def shorten_url(self):
        logger(self.logs_path, 'info', 'shorten_url method called')
        try:
            shorten_url_map = {}
            short_url = ''.join(random.choices(self.original_url, k=self.link_length))
            shorten_url_map[short_url] = self.original_url if self.redirect_options == 'same' else random.choices(self.random_links,k=1)[0]
            shorten_model = ShortenURL(original_url=self.original_url, shortened_url=short_url, redirect_options=shorten_url_map[short_url], link_length= self.link_length, data_time= datetime.datetime.now())
            db.session.add(shorten_model)
            db.session.commit()
            logger(self.logs_path, 'info', 'Shortened URL is created successfully')
            return {'message': 'Shortened URL is created successfully', 'short_url': short_url,'shorten_url_map':shorten_url_map}
        except Exception as error:
            logger(self.logs_path, 'error',f'There is an error saying {error}')
            return {'error_message': f'There is an error saying {error}'}
