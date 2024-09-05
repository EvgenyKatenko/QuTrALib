import pytest
from datetime import date
import VanillaOption as VO
#from VanillaOption import VanillaOption, EuropeanCallOption, EuropeanPutOption

def test_european_call_option_creation():
    strike = 100.0
    expiry = date(2023, 12, 31)
    call_option = VO.EuropeanCallOption(strike, expiry)
    
    assert call_option.get_strike() == strike
    assert call_option.get_expiry_date() == expiry

def test_european_put_option_creation():
    strike = 50.0
    expiry = date(2024, 6, 30)
    put_option = VO.EuropeanPutOption(strike, expiry)
    
    assert put_option.get_strike() == strike
    assert put_option.get_expiry_date() == expiry

def test_option_attributes_are_private():
    option = VO.EuropeanCallOption(100.0, date(2023, 12, 31))
    
    with pytest.raises(AttributeError):
        option._strike
    
    with pytest.raises(AttributeError):
        option._expiry_date

if __name__ == "__main__":
    pytest.main()
