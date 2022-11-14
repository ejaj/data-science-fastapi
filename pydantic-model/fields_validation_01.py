from typing import Optional

from pydantic import BaseModel, Field, ValidationError


class Person(BaseModel):
    first_name: str = Field(..., min_length=3)
    last_name: str = Field(..., min_length=3)
    age: Optional[int] = Field(None, ge=0, le=120)


# Invalid first name
try:
    Person(first_name="Kazi", last_name="Ejaj", age=30)
except ValidationError as e:
    print(str(e))

# Invalid age
try:
    Person(first_name="Kazi", last_name="Ejaj", age=2000)
except ValidationError as e:
    print(str(e))

# Valid
person = Person(first_name="Kazi", last_name="Ejaj", age=30)
print(person)  # first_name='Kazi' last_name='Ejaj' age=30
