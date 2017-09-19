#!/usr/bin/env python

import os
import random
import json
from codenames import codenames

class pallet:
    WIN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ENDC = '\033[0m'

def colored(text, color):
	print color+text+'\033[0m'

size = len(codenames)

codename_index = random.randint(0, size)
codename = codenames[codename_index]

colored(codename['name'], pallet.WIN)
print codename['description']
print codename['year']

