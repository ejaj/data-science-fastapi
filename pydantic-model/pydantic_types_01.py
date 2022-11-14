from pydantic import BaseModel, EmailStr, HttpUrl, ValidationError


class User(BaseModel):
    email: EmailStr
    website: HttpUrl


# Invalid email
try:
    User(email="kazi", website="https://www.example.com")
except ValidationError as e:
    print(str(e))


# Invalid URL
try:
    User(email="kazi@example.com", website="kazi")
except ValidationError as e:
    print(str(e))


# Valid
user = User(email="kazi@example.com", website="https://www.example.com")
# email='kazi@example.com' website=HttpUrl('https://www.example.com', scheme='https', host='www.example.com', tld='com', host_type='domain')
print(user)