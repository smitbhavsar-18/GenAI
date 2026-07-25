#Task 1
import math_utils
from math_utils import square

print(math_utils.add(5, 3))
print(math_utils.subtract(10, 4))
print(square(6))

#Task 2
import string_utils

print(string_utils.capitalize_words("hello world"))
print(string_utils.reverse_string("Python"))
print(string_utils.word_count("This is a sample sentence."))

#Task 3
import shop_package.discount as disc
from shop_package.billing import calculate_total, apply_tax

print(disc.apply_discount(100, 10))
print(disc.flat_discount(100, 15))
print(calculate_total([100, 200, 300]))
print(apply_tax(600))