import secrets

def generate_secret_key(length=64):
    return secrets.token_urlsafe(length)

secret_key = generate_secret_key()
print(secret_key)