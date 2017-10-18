# -*- coding: utf-8 -*-
"""Pyrseas YAML utilities"""

from yaml import add_representer, dump

from pyrseas.lib.pycompat import PY2
import re


if PY2:
    from yaml import safe_dump as dump

    class MultiLineStr(unicode):
        """ Marker for multiline strings"""
else:
    class MultiLineStr(str):
        """ Marker for multiline strings"""


def pretty(self):
    return re.sub(r"\s*(?:\r|\n|\r\n)","\n", self.replace("\t","  ").strip())


MultiLineStr.pretty = pretty


def MultiLineStr_presenter(dumper, data):
    """

    :param yaml.Dumper dumper:
    :param MultiLineStr data:
    """
    data_pretty = re.sub(r"\s*(?:\r|\n|\r\n)","\n", data.replace("\t","  ").strip())
    return dumper.represent_scalar('tag:yaml.org,2002:str', data_pretty, style='|')
add_representer(MultiLineStr, MultiLineStr_presenter)


def yamldump(objmap):
    """Dump an object map using yaml.dump with certain defaults

    :param objmap: dictionary
    :return: dumped object map
    """
    return dump(objmap, default_flow_style=False, allow_unicode=True)
