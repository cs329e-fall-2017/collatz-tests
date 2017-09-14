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

    def test_read_1(self):
        s = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    def test_read_2(self):
        s = "10 1\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 10)
        self.assertEqual(j, 1)
        
    def test_read_3(self):
        s = "300 500\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 300)
        self.assertEqual(j, 500)
##        
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
        v = collatz_eval(600, 600)
        self.assertEqual(v, 18)
                         
    def test_eval_5(self):
        v = collatz_eval(8, 1)
        self.assertEqual(v, 17)

    def test_eval_6(self):
        v = collatz_eval(300, 50)
        self.assertEqual(v, 128)
                         
    # -----
    # print
    # -----

    def test_print_1(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")
        
    def test_print_2(self):
        w = StringIO()
        collatz_print(w, 50, 40, 30)
        self.assertEqual(w.getvalue(), "50 40 30\n")

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
        r = StringIO("10 20\n50 100\n1 2\n1000 900\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(),"10 20 21\n50 100 119\n1 2 2\n1000 900 174\n")
        
    def test_solve_3(self):
        r = StringIO("1 1\n4 80\n80 4\n1000 1001\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(),"1 1 1\n4 80 116\n80 4 116\n1000 1001 143\n")

# ----
# main
# ----

if __name__ == "__main__":
    main()

""" #pragma: no cover
$ coverage-3.5 run TestCollatz.py
..............
----------------------------------------------------------------------
Ran 14 tests in 0.024s

OK

Acer@DESKTOP-CM1G772 MINGW64 ~/cs329e-collatz (dev)
$ coverage-3.5 report
Name             Stmts   Miss  Cover
------------------------------------
Collatz.py          32      0   100%
TestCollatz.py      62      0   100%
------------------------------------
TOTAL               94      0   100% """
