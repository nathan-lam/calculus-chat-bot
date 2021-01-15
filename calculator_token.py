from nltk_utils import tokenize
from base_calculator import *
import string

_NUMERAL_STARTS = set(string.digits) | set('+-.')
_SYMBOL_CHARS = (set('!$%&*/:<=>?@^_~') | set(string.ascii_lowercase) |
                 set(string.ascii_uppercase) | _NUMERAL_STARTS)
_STRING_DELIMS = set('"')
_WHITESPACE = set(' \t\n\r')
_SINGLE_CHAR_TOKENS = set("()[]'`")
_TOKEN_END = _WHITESPACE | _SINGLE_CHAR_TOKENS | _STRING_DELIMS | {',', ',@'}
DELIMITERS = _SINGLE_CHAR_TOKENS | {'.', ',', ',@'}


def valid_symbol(s):
    if len(s) == 0:
        return False
    for c in s:
        if c not in _SYMBOL_CHARS:
            return False
    return True


def link_token(line):
    line = tokenize(line)
    math_link = Link(None)

    for i in line:
        math_link.rest = Link(i)
    math_link.rest = Link(None)
    return math_link





