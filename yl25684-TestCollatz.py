#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2016
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------


class TestCollatz (TestCase):
    # ----
    # read 
   # ----

    def test_read(self):
        s = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    #
    def test_read_1(self):
        s = "1 1\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 1)
        self.assertEqual(j, 1)

    #
    def test_read_2(self):
        s = "10 1\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 10)
        self.assertEqual(j, 1)
        
    #
    # ----
    # eval
    # ----

    def test_eval_1(self):
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20)

    def test_eval_2(self):
        v = collatz_eval(100, 200)
        self.assertEqual(v, 125)

    def test_eval_3(self):
        v = collatz_eval(201, 210)
        self.assertEqual(v, 89)

    def test_eval_4(self):
        v = collatz_eval(900, 1000)
        self.assertEqual(v, 174)

    #
    def test_eval_corner1(self):
        v = collatz_eval(1,1)
        self.assertEqual(v, 1)

    #
    def test_eval_corner2(self):
        v = collatz_eval(10, 1)
        self.assertEqual(v, 20)

    #
    def test_eval_corner3(self):
        v = collatz_eval(1, 5000)
        self.assertEqual(v, 238)

    #
    def test_eval_corner4(self):
        v = collatz_eval(1, 10000)
        self.assertEqual(v, 262)

    #
    def test_eval_corner5(self):
        v = collatz_eval(1, 6000)
        self.assertEqual(v, 238)

    #
    def test_eval_corner6(self):
        v = collatz_eval(4000, 10000)
        self.assertEqual(v, 262)

    #
    def test_eval_corner7(self):
        v = collatz_eval(4000, 5500)
        self.assertEqual(v, 215)
    #
    def test_eval_corner8(self):
        v = collatz_eval(5001, 25000)
        self.assertEqual(v, 282)
    #
    def test_eval_corner9(self):
        v = collatz_eval(5001, 22000)
        self.assertEqual(v, 279)

    #
    def test_eval_corner10(self):
        v = collatz_eval(7001, 25000)
        self.assertEqual(v, 282)

    #
    def test_eval_corner11(self):
        v = collatz_eval(7001, 22000)
        self.assertEqual(v, 279)

    #
    def test_eval_corner12(self):
        v = collatz_eval(1100000, 1100000)
        self.assertEqual(v, 135)
    # -----
    # print
    # -----

    def test_print(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    # -----
    # solve
    # -----

    def test_solve(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            #w.getvalue(), "1 10 1\n100 200 1\n201 210 1\n900 1000 1\n")
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")


# ----
# main
# ----

if __name__ == "__main__":
    main()

""" #pragma: no cover
% coverage-3.5 run --branch TestCollatz.py >  TestCollatz.out 2>&1


% cat TestCollatz.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.000s
OK


% coverage-3.5 report -m                   >> TestCollatz.out



% cat TestCollatz.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.000s
OK
Name             Stmts   Miss Branch BrPart  Cover   Missing
------------------------------------------------------------
Collatz.py          12      0      2      0   100%
TestCollatz.py      32      0      0      0   100%
------------------------------------------------------------
TOTAL               44      0      2      0   100%
"""
