#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import random
import sympy

if __name__ == "__main__":
    try:
        mother = int(sys.argv[1])
        father = int(sys.argv[2])
        env    = [] if len(sys.argv) <= 3 else map(int, sys.argv[3].split(","))
    except Exception:
        print "usage: python my_number.py {mother's number} {father's number} {env}"
        sys.exit(0)
    
    print "mother: %s, father: %s, env: %s" % (mother, father, env)

    p = sympy.nextprime(max(mother, father))
    my_number = 0
    while True:
        my_number = 2 * mother * father * p + 1
        if p not in env and sympy.isprime(my_number):
            break
        else:
            p = sympy.nextprime(p)

    print "prime: %s, number: %s" % (p, my_number)
