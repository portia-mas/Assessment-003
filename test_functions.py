# import pytest
from functions import *

# -------------------------
# recursive_sum (4 tests)
# -------------------------

def test_recursive_sum_simple():
    assert recursive_sum([1, 2, 3]) == 6

def test_recursive_sum_nested():
    assert recursive_sum([1, [2, [3, 4]], 5]) == 15

def test_recursive_sum_empty():
    assert recursive_sum([]) == 0

def test_recursive_sum_deep():
    assert recursive_sum([[[1]], [2, [3]]]) == 6


# -------------------------
# count_items (4 tests)
# -------------------------

def test_count_items_flat():
    assert count_items([1, 2, 3]) == 3

def test_count_items_nested():
    assert count_items([1, [2, 3], [4, [5]]]) == 5

def test_count_items_empty():
    assert count_items([]) == 0

def test_count_items_deep():
    assert count_items([[[1], 2], 3]) == 3


# -------------------------
# factorial (3 tests)
# -------------------------

def test_factorial_zero():
    assert factorial(0) == 1

def test_factorial_small():
    assert factorial(5) == 120

def test_factorial_medium():
    assert factorial(7) == 5040


# -------------------------
# fibonacci (3 tests)
# -------------------------

def test_fibonacci_zero():
    assert fibonacci(0) == 0

def test_fibonacci_one():
    assert fibonacci(1) == 1

def test_fibonacci_seven():
    assert fibonacci(7) == 13


# -------------------------
# flatten_dict (4 tests)
# -------------------------

def test_flatten_simple():
    assert flatten_dict({"a": 1}) == {"a": 1}

def test_flatten_nested():
    assert flatten_dict({"a": {"b": 2}}) == {"a.b": 2}

def test_flatten_deep():
    d = {"a": {"b": {"c": 3}}}
    assert flatten_dict(d) == {"a.b.c": 3}

def test_flatten_multiple():
    d = {"a": 1, "b": {"c": 2}}
    assert flatten_dict(d) == {"a": 1, "b.c": 2}


# -------------------------
# group_by_length (3 tests)
# -------------------------

def test_group_basic():
    words = ["hi", "cat", "dog"]
    assert group_by_length(words) == {2: ["hi"], 3: ["cat", "dog"]}

def test_group_empty():
    assert group_by_length([]) == {}

def test_group_varied():
    words = ["a", "bb", "ccc", "dd"]
    assert group_by_length(words) == {1: ["a"], 2: ["bb", "dd"], 3: ["ccc"]}


# -------------------------
# is_palindrome_recursive (3 tests)
# -------------------------

def test_palindrome_true():
    assert is_palindrome_recursive("racecar") is True

def test_palindrome_false():
    assert is_palindrome_recursive("python") is False

def test_palindrome_single():
    assert is_palindrome_recursive("a") is True


# -------------------------
# format_name (2 tests)
# -------------------------

def test_format_name_basic():
    assert format_name("john", "doe") == "John Doe"

def test_format_name_caps():
    assert format_name("ALICE", "smith") == "Alice Smith"


# -------------------------
# snake_to_camel (2 tests)
# -------------------------

def test_snake_to_camel_basic():
    assert snake_to_camel("hello_world") == "helloWorld"

def test_snake_to_camel_long():
    assert snake_to_camel("convert_this_string") == "convertThisString"


# -------------------------
# word_frequency 
# -------------------------

def test_word_frequency_simple():
    sentence = "hello world hello"
    assert word_frequency(sentence) == {"hello": 2, "world": 1}

def test_word_frequency_case():
    sentence = "Hello hello"
    assert word_frequency(sentence) == {"hello": 2}
