import pytest
from src.baggage import validate_baggage 

def test_hazardous_item_prohibited():
    assert validate_baggage(5, "carry-on", "economy", "domestic", hazardous_item=True, passport_valid=True) == False

def test_international_flight_invalid_passport():
    assert validate_baggage(5, "carry-on", "economy", "international", hazardous_item=False, passport_valid=False) == False

def test_carry_on_economy_max_weight():
    assert validate_baggage(7, "carry-on", "economy", "domestic", hazardous_item=False, passport_valid=True) == True
    assert validate_baggage(8, "carry-on", "economy", "domestic", hazardous_item=False, passport_valid=True) == False

def test_checked_business_allowance():
    assert validate_baggage(40, "checked", "business", "domestic", hazardous_item=False, passport_valid=True) == True
    assert validate_baggage(41, "checked", "business", "domestic", hazardous_item=False, passport_valid=True) == False