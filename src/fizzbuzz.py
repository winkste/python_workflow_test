#!/usr/bin/env python
""" Test Driven Development Kata: fizzBuzz.

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.
"""

__author__ = "Stephan Wink"
__copyright__ = "Copyright $2022, $WShield"
__credits__ = ["MArtin C. Roberts"]
__date__ = "2022/11/19"
__deprecated__ = False
__license__ = "GPLv3"
__maintainer__ = "developer"
__status__ = "Production"
__version__ = "0.0.1"

def calculate_fizzbuzz(val):
    """Calculates the fizzBuzz from val.

    """
    if isinstance(val, int):
        return calc(val)
    raise ValueError

def calc(val):
    """This function does the calculation of the fizzBuzz.

    """
    if is_value_a_fizz(val) and is_value_a_buzz(val):
        return "FizzBuzzz"
    elif is_value_a_fizz(val):
        return "Fizz"
    elif is_value_a_buzz(val):
        return "Buzz"

    return f"{val}"

def is_value_a_fizz(val):
    """Checks if val is a multiple of 3.

    """
    if val % 3 == 0 and val != 0:
        return True
    return False

def is_value_a_buzz(val):
    """Checks if the val is a multiple of 5.

    """
    if val % 5 == 0 and val != 0:
        return True
    return False
