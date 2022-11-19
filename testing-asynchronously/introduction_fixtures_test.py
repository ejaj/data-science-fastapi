import pytest

from introduction_fixtures import Address, Gender, Person


@pytest.fixture
def address():
    return Address(
        street_address="12 Squirell Street",
        postal_code="424242",
        city="Woodtown",
        country="US",
    )


@pytest.fixture
def person(address):
    return Person(
        first_name="Kazi",
        last_name="Ejaj",
        gender=Gender.MALE,
        birthdate="1991-01-01",
        interests=["travel", "sports"],
        address=address,
    )


def test_address_country(address):
    assert address.country == "US"


def test_person_first_name(person):
    assert person.first_name == "Kazi"


def test_person_address_city(person):
    assert person.address.city == "Woodtown"
