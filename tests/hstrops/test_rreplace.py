# Generated by CodiumAI
import pytest

from helpo.hstrops import rreplace


class TestRreplace:
    # Should replace the last occurrence of a substring in a string with another substring
    def test_replace_last_occurrence(self):
        instr = "Hello, World, Hello, World"
        match_str = "World"
        replace_str = "Everyone"
        times = 1
        expected_output = "Hello, World, Hello, Everyone"
        assert (
            rreplace(instr, match_str, replace_str, times) == expected_output
        ), "Replacement of last occurrence failed"

    # Should replace the last n occurrences of a substring in a string with another substring
    def test_replace_last_n_occurrences(self):
        instr = "Hello, World, Hello, World"
        match_str = "World"
        replace_str = "Everyone"
        times = 2
        expected_output = "Hello, Everyone, Hello, Everyone"
        assert (
            rreplace(instr, match_str, replace_str, times) == expected_output
        ), "Replacement of last n occurrences failed"

    # Should return the original string if the substring is not found
    def test_substring_not_found(self):
        instr = "Hello, World, Hello, World"
        match_str = "Everyone"
        replace_str = "World"
        times = 1
        expected_output = instr
        assert (
            rreplace(instr, match_str, replace_str, times) == expected_output
        ), "Substring not found, original string should be returned"

    # Should return the original string if times is 0
    def test_times_zero(self):
        instr = "Hello, World, Hello, World"
        match_str = "World"
        replace_str = "Everyone"
        times = 0
        expected_output = instr
        assert (
            rreplace(instr, match_str, replace_str, times) == expected_output
        ), "Times is 0, original string should be returned"

    # Should replace all occurrences of the substring if times is greater than the number of occurrences
    def test_times_greater_than_occurrences(self):
        instr = "Hello, World, Hello, World"
        match_str = "World"
        replace_str = "Everyone"
        times = 3
        expected_output = "Hello, Everyone, Hello, Everyone"
        assert (
            rreplace(instr, match_str, replace_str, times) == expected_output
        ), "Times is greater than occurrences, all occurrences should be replaced"

    # Should replace all occurrences of the substring if times is negative
    def test_times_negative(self):
        instr = "Hello, World, Hello, World"
        match_str = "World"
        replace_str = "Everyone"
        times = -1
        expected_output = "Hello, Everyone, Hello, Everyone"
        assert (
            rreplace(instr, match_str, replace_str, times) == expected_output
        ), "Times is negative, all occurrences should be replaced"
