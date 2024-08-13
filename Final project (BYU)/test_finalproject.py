# Created by: Tomas Contreras, student from BYU Idaho

import pytest
from io import StringIO
import sys
from unittest.mock import patch
from finalproject import main, random_number


def test_random_number():
    secret_number = random_number()

    assert secret_number  == secret_number
    assert secret_number != random_number()
    assert secret_number != 21

def test_main():

    # For testing purposes, set a known secret number
    secret_number = 5
    with patch('finalproject.random_number', return_value=secret_number):
        # Simulate user input '5'
        with patch('builtins.input', side_effect=['5']):  
            captured_output = StringIO()
            sys.stdout = captured_output
            main()
            sys.stdout = sys.__stdout__
            output = captured_output.getvalue().strip()
            assert "Congratulations! you guess the number in 1 attempts." in output


    # For testing purposes, set a known secret number
    secret_number = 11
    with patch('finalproject.random_number', return_value=secret_number):
         # Simulate 10 incorrect guesses
        with patch('builtins.input', side_effect=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']): 
            captured_output = StringIO()
            sys.stdout = captured_output
            main()
            sys.stdout = sys.__stdout__
            output = captured_output.getvalue().strip()
            assert f"Sorry! the secret number was {secret_number}. You lose your 10 attempts." in output


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])