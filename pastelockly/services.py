from utilis.logger import logger
from cryptography.fernet import Fernet
from utilis.derive_key import derive_key
from models.pastelockly import PasteLockly_
import datetime
from app import db

# 1. A form where we can enter text and create a shareable URL.
# 2. Shareable URL should lead to the view-only snippet.
# 3. Optionally, the creator of the snippet URL can add a secret key which will be used
# to encrypt the content in the database.
# 4. The viewer must supply the key to decrypt the content.

class PasteLockly:
    def __init__(self, text=None, encrypt_key=None) -> None:
        self.text = text
        self.log_path = 'logs/paste-lockly.log'
        self.encrypt_key = encrypt_key
        logger(self.logs_path, 'info', 'Object initialized with PasteLockly class')
    
    def create_sharable_link(self):
        logger(self.logs_path, 'info', 'create_sharable_link method called')
        try:
            key = derive_key(self.encrypt_key)
            text = self.text.encode()
            cipher_suite = Fernet(key)
            cipher_text = cipher_suite.encrypt(text)
            paste_lockly_obj = PasteLockly_(cipher_text, key, datetime.datetime.now())
            db.session.add(paste_lockly_obj)
            db.session.commit()
            logger(self.logs_path, 'info', 'create_sharable_link method ran successfully')
            return paste_lockly_obj.id
        
        except Exception as error:
            logger(self.logs_path, 'error', f'create_sharable_link end up with an error saying {error}')
            raise RuntimeError("An error occurred while processing your request.") from error
    
    def get_snippet(self,id):
        try:
            logger(self.logs_path, 'info', 'get_snippet method called')
            paste_lockly_obj = PasteLockly_.query.get(id)
            cipher_suite = Fernet(paste_lockly_obj.encrypt_key)
            text = cipher_suite.decrypt(paste_lockly_obj.text).decode()
            return text
        except Exception as error:
            logger(self.logs_path, 'error', f'get_snippet end up with an error saying {error}')
            raise RuntimeError("An error occurred while processing your request.") from error
        
        
