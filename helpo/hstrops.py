"""String Ops Helpers module."""

import logging

from rich import print as print

LOG = logging.getLogger(__name__)


def get_lines_between_tags(filetext, start_tag="```{toctree}", end_tag="```"):
    """
    Extracts lines of text between specified start and end tags.

    Args:
        filetext (str): The text to search within.
        start_tag (str, optional): The tag marking the start of the text to extract. Defaults to "```{toctree}".
        end_tag (str, optional): The tag marking the end of the text to extract. Defaults to "```".

    Returns:
        list: A list of lines between the start and end tags.

    Example:
        >>> text = "Hello\n```{toctree}\nWorld\n```\nGoodbye"
        >>> get_lines_between_tags(text)
        ['```{toctree}', 'World', '```']
    """

    line_holder = []
    inRecordingMode = False
    tags_found = 0
    for line in filetext.split("\n"):
        if not inRecordingMode:
            if start_tag in line:
                print("TRUE: found toctree")
                inRecordingMode = True
                tags_found += 1
                line_holder.append(line)
        elif end_tag in line:
            inRecordingMode = False
            tags_found += 1
            line_holder.append(line)
        else:
            line_holder.append(line)

    if tags_found != 2:
        return []
    return line_holder


def get_lines_between_tag_and_blank_line(filetext, start_tag="```{toctree}"):
    """
    Extracts lines of text between a specified start tag and the next blank line.

    Args:
        filetext (str): The text to search within.
        start_tag (str, optional): The tag marking the start of the text to extract. Defaults to "```{toctree}".

    Returns:
        list: A list of lines between the start tag and the next blank line.

    Example:
        >>> text = "Hello\n```{toctree}\nWorld\n\nGoodbye"
        >>> get_lines_between_tag_and_blank_line(text)
        ['```{toctree}', 'World', '']
    """
    line_holder = []
    inRecordingMode = False
    for line in filetext.split("\n"):
        if not inRecordingMode:
            if start_tag in line:
                print("TRUE: found toctree")
                inRecordingMode = True
                line_holder.append(line)
        elif len(line) == 0:
            inRecordingMode = False
            line_holder.append(line)
        else:
            line_holder.append(line)

    return line_holder


def get_multiblocks_between_tags(filetext, start_tag=":::", end_tag=":::"):
    """
    Extracts blocks of text between specified start and end tags.

    Args:
        filetext (str): The text to search within.
        start_tag (str, optional): The tag marking the start of the text to extract. Defaults to ":::".
        end_tag (str, optional): The tag marking the end of the text to extract. Defaults to ":::".

    Returns:
        list: A list of blocks (each block is a list of lines) between the start and end tags.

    Example:
        >>> text = "Hello\n:::\nWorld\n:::\nGoodbye"
        >>> get_multiblocks_between_tags(text)
        [[':::', 'World', ':::']]
    """
    block_holder = []
    inRecordingMode = False
    for line in filetext.split("\n"):
        if not inRecordingMode:
            if start_tag in line:
                inRecordingMode = True
                line_holder = []
                line_holder.append(line)
        elif end_tag in line:
            inRecordingMode = False
            line_holder.append(line)
            block_holder.append(line_holder)
        else:
            line_holder.append(line)
    return block_holder


def norm_key(instr):
    """
    Normalizes a string by converting it to lowercase and removing spaces, hyphens, and underscores.

    Args:
        instr (str): The string to normalize.

    Returns:
        str: The normalized string.

    Example:
        >>> norm_key("Hello_World-Test")
        'helloworldtest'
    """
    return instr.lower().replace(" ", "").replace("-", "").replace("_", "").strip()


def rreplace(instr, match_str, replace_str, times):
    """
    Replaces the last occurrences of a substring in a string with another substring.

    Args:
        instr (str): The string to modify.
        match_str (str): The substring to replace.
        replace_str (str): The substring to replace with.
        times (int): The number of occurrences to replace.

    Returns:
        str: The modified string.

    Example:
        >>> rreplace("Hello, World, Hello, World", "World", "Everyone", 1)
        'Hello, World, Hello, Everyone'
    """
    rsplit_li = instr.rsplit(match_str, times)
    return replace_str.join(rsplit_li)


def clean_list_via_rm_patts(input_list, rm_patts, rm_empty_instrs=True):
    """
    Cleans a list by removing elements that are empty or contain any of the specified patterns.

    Args:
        input_list (list): The list to be cleaned.
        rm_patts (list): The patterns to remove.
        rm_empty_instrs (bool, optional): Whether to remove empty strings. Defaults to True.

    Returns:
        list: The cleaned list.

    Example:
        >>> clean_list_via_rm_patts(["Hello", "World", "", "Hello, World"], ["World"])
        ['Hello', '']
    """
    clean_list = []
    for instr in input_list:
        instr_is_empty = len(instr.strip()) == 0
        instr_contains_rm_patts = any(rm_patt in instr for rm_patt in rm_patts)

        if instr_is_empty and rm_empty_instrs:
            continue
        if instr_contains_rm_patts:
            continue

        clean_list.append(instr)
    return clean_list


def does_str_contain_pattern(instr, match_patts):
    """
    Checks if a string contains any of the specified patterns.

    Args:
        instr (str): The string to check.
        match_patts (list): The patterns to check for.

    Returns:
        bool: True if the string contains any of the patterns, False otherwise.

    Example:
        >>> does_str_contain_pattern("Hello, World", ["World"])
        True
    """
    instr_clean = instr.strip()
    for input_patt in match_patts:
        if input_patt.strip() in instr_clean:
            return True
    return False


def does_str_start_with_pattern(instr, match_patts):
    """
    Checks if a string starts with any of the specified patterns.

    Args:
        instr (str): The string to check.
        match_patts (list): The patterns to check for.

    Returns:
        bool: True if the string starts with any of the patterns, False otherwise.

    Example:
        >>> does_str_start_with_pattern("Hello, World", ["Hello"])
        True
    """
    for idx in range(len(match_patts)):
        clean_patt = match_patts[idx].strip()
        match_patts[idx] = clean_patt

    instr_clean = instr.strip()
    for patt in match_patts:
        if instr_clean.startswith(patt):
            return True
    return False


# TODO: use this function more
def multiline_str_2list(multiline_str, delimiter="\n"):
    """
    Converts a multiline string into a list of strings, using a specified delimiter.

    Args:
        multiline_str (str): The multiline string to convert.
        delimiter (str, optional): The delimiter to split the string by. Defaults to "\n".

    Returns:
        list: The list of strings.

    Example:
        >>> multiline_str_2list("Hello\nWorld")
        ['Hello', 'World']
    """
    mstr = multiline_str.split(delimiter)
    mstr_clean = [line.strip() for line in mstr if line.strip() != ""]
    return mstr_clean


def rm_lines_starting_with(multiline_str, rm_patts):
    """
    Removes lines from a multiline string that start with any of the specified patterns.

    Args:
        multiline_str (str): The multiline string to process.
        rm_patts (list): The patterns to check for at the start of each line.

    Returns:
        str: The processed string with matching lines removed.

    Example:
        >>> rm_lines_starting_with("Hello\nWorld", ["Hello"])
        'World'
    """
    lines = multiline_str_2list(multiline_str=multiline_str, delimiter="\n")
    print("lines", lines)
    filtered_lines = [
        line for line in lines if not does_str_start_with_pattern(line, rm_patts)
    ]

    print("filtered_lines", filtered_lines)

    multiline_outstr = "\n".join(filtered_lines)
    print("multiline_outstr", multiline_outstr)

    return multiline_outstr


def clean_str_pline(instr, rm_patts):
    """
    Cleans a string by removing specified patterns and leading/trailing whitespace.

    Args:
        instr (str): The string to clean.
        rm_patts (list): The patterns to remove.

    Returns:
        str: The cleaned string.

    Example:
        >>> clean_str_pline("Hello, World", ["World"])
        'Hello, '
    """
    for patt in rm_patts:
        instr = instr.replace(patt, "")

    return instr.strip()


def replace_str_pline(instr, sub_tups):
    """
    Replaces multiple substrings in a string with specified replacements.

    Args:
        instr (str): The string to modify.
        sub_tups (list): A list of tuples, each containing a target substring and its replacement.
            e.g. [("Hello", "Goodbye"), ("World", "Everyone")]

    Returns:
        str: The modified string.

    Example:
        >>> replace_str_pline("Hello, World", [("Hello", "Goodbye"), ("World", "Everyone")])
        'Goodbye, Everyone'
    """
    for sub in sub_tups:
        instr = instr.replace(sub[0], sub[1])

    return instr.strip()


# TODO: remove all instances of this function - use replace_str_pline instead
def str_multi_replace(instr, rm_patts, replace_str):
    """
    Replaces multiple substrings in a string with a specified replacement.

    Args:
        instr (str): The string to modify.
        rm_patts (list): A list of target substrings to replace.
        replace_str (str): The replacement string.

    Returns:
        str: The modified string.

    Example:
        >>> str_multi_replace("Hello, World", ["Hello", "World"], "Everyone")
        'Everyone, Everyone'
    """
    for patt in rm_patts:
        patt_clean = patt.replace("*.", ".")
        print("patt_clean", patt_clean)
        instr = instr.replace(patt_clean, replace_str)
    return instr
