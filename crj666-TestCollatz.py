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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_parse

# -----------
# TestCollatz
# -----------


class TestCollatz (TestCase):
    # ----
    # read
    # ----

    def test_read_1(self):
        s = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    def test_read_2(self):
        s = "42 1023\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  42)
        self.assertEqual(j, 1023)

    def test_read_3(self):
        s = "111 999999\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  111)
        self.assertEqual(j, 999999)

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

    def test_eval_5(self):
        v = collatz_eval(10, 1)
        self.assertEqual(v, 20)

    def test_eval_6(self):
        v = collatz_eval(12345, 999999)
        self.assertEqual(v, 525)

    def test_eval_7(self):
        v = collatz_eval(100, 15000)
        self.assertEqual(v, 276)

    # -----
    # print
    # -----

    def test_print_1(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2(self):
        w = StringIO()
        collatz_print(w, 10, 100, 119)
        self.assertEqual(w.getvalue(), "10 100 119\n")

    def test_print_3(self):
        w = StringIO()
        collatz_print(w, 1900, 2000, 175)
        self.assertEqual(w.getvalue(), "1900 2000 175\n")

    # -----
    # solve
    # -----

    def test_solve_1(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2(self):
        r = StringIO("10 100\n210 900\n301 301\n302 303\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "10 100 119\n210 900 179\n301 301 17\n302 303 43\n")

    def test_solve_3(self):
        r = StringIO("1001 1023\n1010 1200\n1201 1210\n1900 2000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1001 1023 156\n1010 1200 182\n1201 1210 71\n1900 2000 175\n")

    # -----
    # parse
    # -----

    def test_parse_1(self):
        v = collatz_parse(400, 2600)
        self.assertEqual(v, [[400, 1000], [1001, 2000], [2001, 2600]])

    def test_parse_2(self):
        v = collatz_parse(5, 4200)
        self.assertEqual(v, [[5, 1000], [1001, 2000], [2001, 3000], [3001, 4000], [4001, 4200]])

    def test_parse_3(self):
        v = collatz_parse(15001, 16000)
        self.assertEqual(v, [[15001, 16000]])

    def test_parse_4(self):
        v = collatz_parse(1, 1000)
        self.assertEqual(v, [[1, 1000]])

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
