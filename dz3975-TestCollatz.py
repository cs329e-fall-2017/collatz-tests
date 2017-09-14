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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, round_down, simple_collatz_eval

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

    def test_read2(self):
        s = "0 098\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 0)
        self.assertEqual(j, 98)

    def test_read3(self):
        s = "failure case \n"
        self.assertRaises(ValueError, collatz_read, s)

    # ----
    # round_down
    # ----
    def test_round_1(self):
        v = round_down(50, 500)
        self.assertEqual(v, 0)
    
    def test_round_2(self):
        v = round_down(999, 1000)
        self.assertEqual(v, 0)

    def test_round_3(self):
        v = round_down(500, 1000)
        self.assertEqual(v, 0)
    
    def test_round_4(self):
        v = round_down(8987, 1000)
        self.assertEqual(v, 8000)

    # ----
    # eval 
    # ----
    def test_eval_1(self):
        v = simple_collatz_eval(999, 99999)
        self.assertEqual(v, 351)

    def test_eval_2(self):
        v = simple_collatz_eval(898, 101010)
        self.assertEqual(v, 351)

    def test_eval_3(self):
        v = simple_collatz_eval(89, 130)
        self.assertEqual(v, 122)

    def test_eval_4(self):
        v = simple_collatz_eval(29, 32)
        self.assertEqual(v, 107)
    
    def test_eval_5(self):
        v = simple_collatz_eval(90, 8765)
        self.assertEqual(v, 262)

    # ----
    # eval simple
    # ----

    def test_seval_1(self):
        v = simple_collatz_eval(1, 10)
        self.assertEqual(v, 20)

    def test_seval_2(self):
        v = simple_collatz_eval(100, 200)
        self.assertEqual(v, 125)

    def test_seval_3(self):
        v = simple_collatz_eval(201, 210)
        self.assertEqual(v, 89)

    def test_seval_4(self):
        v = simple_collatz_eval(900, 1000)
        self.assertEqual(v, 174)
    
    def test_seval_5(self):
        v = simple_collatz_eval(3, 3)
        self.assertEqual(v, 8)



    # -----
    # print
    # -----

    def test_print(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print2(self):
        w = StringIO()
        collatz_print(w, '', '', '')
        self.assertEqual(w.getvalue(), "  \n")

    def test_print3(self):
        w = StringIO()
        t = True
        f = False
        i = 0.00000
        collatz_print(w, t, f, i)
        self.assertEqual(w.getvalue(), "True False 0.0\n")
    # -----
    # solve
    # -----

    def test_solve(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve2(self):
        r = StringIO(" ")
        w = StringIO()
        self.assertRaises(IndexError, collatz_solve, r , w)

    def test_solve3(self):
        r = StringIO("String Index \n Another String !!!!")
        w = StringIO()
        self.assertRaises(ValueError, collatz_solve, r, w)

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
