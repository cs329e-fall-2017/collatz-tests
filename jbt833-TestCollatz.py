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

    def test_read_1(self):
        s = "1234 1000\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1234)
        self.assertEqual(j, 1000)

    def test_read_2(self):
        s = "888775 98756\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  888775)
        self.assertEqual(j, 98756)

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
        v = collatz_eval(10,1)
        self.assertEqual(v,20)

    def test_eval_6(self):
        v = collatz_eval(2,2)
        self.assertEqual(v,2)

    def test_eval_7(self):
        v = collatz_eval(500,999)
        self.assertEqual(v,179)

    def test_eval_8(self):
        v = collatz_eval(1000,2000)
        self.assertEqual(v,182)

    def test_eval_9(self):
        v = collatz_eval(2001,2222)
        self.assertEqual(v,170)

    def test_eval_10(self):
        v = collatz_eval(500,2222)
        self.assertEqual(v,182)


    # -----
    # print
    # -----

    def test_print(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2(self):
        w = StringIO()
        collatz_print(w, 12, 130, 24)
        self.assertEqual(w.getvalue(), "12 130 24\n")

    def test_print_3(self):
        w = StringIO()
        collatz_print(w, 145, 9990, 576)
        self.assertEqual(w.getvalue(), "145 9990 576\n")

    # -----
    # solve
    # -----

    def test_solve(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
             w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
    def test_solve_2(self):
        r = StringIO("5 10\n100 200\n13 10\n972 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "5 10 20\n100 200 125\n13 10 15\n972 1000 143\n")
    def test_solve_3(self):
        r = StringIO("2657 877790\n432 476\n7895 678345\n344 5674\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "2657 877790 525\n432 476 129\n7895 678345 509\n344 5674 238\n")


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
