#!/bin/env python
import sys
import importlib
from random import randrange

test_array = [randrange(0, 100) for x in xrange(0, 20)]

if len(sys.argv) != 2:
    print "Usage: ./test.py <sort algorithm name>"
    sys.exit(1)

func_name = sys.argv[1] + "_sort"
mod = importlib.import_module(func_name)
func = getattr(mod, func_name)

print("Before sort: %s" % test_array)
func(test_array)
print("After sort: %s" % test_array)
