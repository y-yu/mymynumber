#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import random
import sympy

if __name__ == "__main__":
    try:
        mother = int(sys.argv[1])
        father = int(sys.argv[2])
    except Exception:
        print "usage: python my_number.py {mother's number} {father's number}"
        sys.exit(0)
    
    print "mother: %s, father %s" % (mother, father)

    p = sympy.nextprime(max(mother, father))
    my_number = 0
    while True:
        my_number = 2 * mother * father * p + 1
        if (p > father) and sympy.isprime(my_number):
            break
        else:
            p = sympy.nextprime(p)

    print "prime: %s, number: %s" % (p, my_number)
