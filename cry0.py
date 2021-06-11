from cryptography.fernet import Fernet
# Put this somewhere safe!
key = Fernet.generate_key()
print(key)
f = Fernet(key)
print(f)
token = f.encrypt(b"A really secret message. Not for prying eyes.")
print(token)
f.decrypt(token)