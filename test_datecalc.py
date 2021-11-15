# import datetime library to assign test variables
import datetime
# import functions from datecalc we with to test
from datecalc import when, duration

# validation test to ensure test file is working correctly
def test_tautology():
    assert 1 == 1

def test_datediff():    
    # define start and end dates
    start = datetime.datetime(2021,1,1)
    end = datetime.datetime(2021,1,31)
    # set known number of days between both period for validation
    datesdiff = 30
    # use when() function to determind date after adding 31 days to 01/01/2021
    final = when(start,datesdiff)
    # test that end variable is equal to output from when() function
    assert final == end

def test_leapyear():
    # Wish to check that the function accounts for additional day in leap years
    ## 2024 is a leap year, hence its use.
    # define start and end dates
    start = datetime.datetime(2024,1,1)
    end = datetime.datetime(2024,3,31)
    # set known number of days between start and end varialbe
    datesdiff = 90
    # run when() function for above parametres
    final = when(start,datesdiff)
    # Test when() function output is equal to end variable.
    assert final == end

def test_postiveints():
    # Want to ensure duration() function only returns positive integers
    # define start and end variables so that difference would be negative days
    start = datetime.datetime(2021,1,1)
    end = datetime.datetime(2020,1,1)
    # test that duration function output is greater than 0 (positive)
    assert duration(start,end) >=0
    # test that duration function output is integer (whole number)
    assert isinstance(duration(start,end),int)