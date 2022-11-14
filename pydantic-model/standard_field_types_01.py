from pydantic import BaseModel


class Person(BaseModel):
    first_name: str
    last_name: str
    age: int


person = Person(first_name="Kazi", last_name="Ejajul", age=30)
print(person)
