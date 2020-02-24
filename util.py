# encoding: utf-8

import re
import unicodedata


def strip_punct(string):
    return re.sub(r"(^[^\w]+|[^\w]+$)", "", string)


def remove_accents(string):
    return "".join([char for char in unicodedata.normalize("NFD", string)
                    if unicodedata.category(char) != "Mn"])
