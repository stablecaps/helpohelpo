
from helpo.hstrops import get_lines_between_tags


class TestGetLinesBetweenTags:
    def test_correct_input_output(self):
        filetext = "Hello\n@@@\nWorld\n@@@\nGoodbye"
        expected_output = ["@@@", "World", "@@@"]
        assert (
            get_lines_between_tags(filetext, start_tag="@@@", end_tag="@@@")
            == expected_output
        ), "Failed on Correct input and output"

    def test_incorrect_input_output(self):
        filetext = "Hello\n@@@\nWorld\n@@@\nGoodbye"
        expected_output = ["@@@", "World"]
        assert (
            get_lines_between_tags(filetext, start_tag="@@@", end_tag="@@@")
            != expected_output
        ), "Failed on: Incorrect input and output"

    def test_start_tag_not_found(self):
        filetext = "Hello\nWorld\n@@@\nGoodbye"
        expected_output = []
        assert (
            get_lines_between_tags(filetext, start_tag="@@@", end_tag="@@@")
            == expected_output
        ), "Failed on: Edge case: start tag not found"

    def test_start_end_tags_only_lines(self):
        filetext = "@@@\n@@@"
        expected_output = ["@@@", "@@@"]
        assert (
            get_lines_between_tags(filetext, start_tag="@@@", end_tag="@@@")
            == expected_output
        ), "Failed on: Edge case: start and end tags are the only lines"

    def test_end_tag_not_found(self):
        filetext = "Hello\n@@@\nWorld\nGoodbye"
        expected_output = []
        assert (
            get_lines_between_tags(filetext, start_tag="@@@", end_tag="@@@")
            == expected_output
        ), "Failed on: Edge case: end tag not found"

    def test_start_tag_found_end_tag_not_found(self):
        filetext = "Hello\n@@@\nWorld\nGoodbye"
        expected_output = []
        assert (
            get_lines_between_tags(filetext, start_tag="@@@", end_tag="@@@")
            == expected_output
        ), "Failed on: Edge case: start tag found but end tag not found"

    def test_start_end_tags_same(self):
        filetext = "Hello\n@@@\nWorld\n@@@"
        expected_output = ["@@@", "World", "@@@"]
        assert (
            get_lines_between_tags(filetext, start_tag="@@@", end_tag="@@@")
            == expected_output
        ), "Failed on: Edge case: start tag and end tag are the same"

    def test_general_case(self):
        filetext = "Hello\n@@@\nWorld\n@@@"
        expected_output = ["@@@", "World", "@@@"]
        assert (
            get_lines_between_tags(filetext, start_tag="@@@", end_tag="@@@")
            == expected_output
        ), "Incorrect output"
