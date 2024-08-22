import hashlib
import base64

def derive_key(simple_string):
    key = hashlib.sha256(simple_string.encode()).digest()
    return base64.urlsafe_b64encode(key)