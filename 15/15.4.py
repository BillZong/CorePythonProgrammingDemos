#!/usr/bin/env python
# encoding: UTF-8

"""Exercise answer 15.4 for chapter 15."""

# 匹配所有合法的Python标识符

import re
# import keyword

# Python 2.x
# patternFor2 = r'\b(?P<var>[a-zA-Z_]\w*)\b'
patternFor2 = r'\b([a-zA-Z_]\w*)\b'

# Pyone 3.x
flag = re.UNICODE | re.IGNORECASE
patternFor3 = r'\b(\w*)\b'
