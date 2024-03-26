from datetime import datetime
from pydantic import BaseModel
from typing import Annotated

class User(BaseModel):
    id: int
    name: str = "John Doe"
    signup_ts: datetime | None = None
    friends: list[int] = []

external_data = {
    "id": 1,
    "signup_ts": "2017-06-01 12:22:01",
    "friends": [1, "2", b"3"]
}

user = User(**external_data)
print(user)
print(user.friends)

class Person:
    def __init__(self, name: str):
        self.name = name

def get_person_name(one_person: Person):
    return one_person.name

def get_full_name(first_name: str, last_name: str):
    full_name = first_name.title() + " " + last_name.title()
    return full_name

def get_name_with_age(name: str, age: int):
    name_with_age = name.title() + " is this old: " + str(age)
    return name_with_age

def process_items(items: list[int]):
    return list(filter(lambda x: x >0, items))

def process_records(record_t: tuple[int, int, str], item_s: set[bytes]):
    return record_t, item_s

def process_prices(prices: dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name, item_price)

def say_hello(name: Annotated[str, "this is just metadata"]) -> str:
    return "Hello %s"%name

print(get_full_name("john", "doe"))
print(get_name_with_age("john", 33))
print(process_items([-1, 0]))
process_prices({"television": 50.0, "dvd": 12.5})
print(get_person_name(Person(name = "John")))
print(say_hello("John Doe"))