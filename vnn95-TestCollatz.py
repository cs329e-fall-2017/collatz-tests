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
        self.assertEqual(i, 1)
        self.assertEqual(j, 10)

    def test_read_2(self):
        s = "100 200\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 100)
        self.assertEqual(j, 200)

    def test_read_3(self):
        s = "201 210\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 201)
        self.assertEqual(j, 210)
  
        
    def test_read_4(self):
        s = "900 1000\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 900)
        self.assertEqual(j, 1000)

    def test_read_5(self):
        s = "9000 900\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 9000)
        self.assertEqual(j, 900)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20)

    def test_eval_2(self):
        v = collatz_eval(100, 200)
        self.assertEqual(v,125)

    def test_eval_3(self):
        v = collatz_eval(201, 210)
        self.assertEqual(v, 89)

    def test_eval_4(self):
        v = collatz_eval(900, 1000)
        self.assertEqual(v, 174)
        
    def test_eval_5(self):
        v = collatz_eval(1000, 900)
        self.assertEqual(v, 174)
    
    def test_eval_6(self):
        v = collatz_eval(1000, 1000)
        self.assertEqual(v, 112)

    # -----
    # print
    # -----

    def test_print_1(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")
        
    def test_print_2(self):
        w = StringIO()
        collatz_print(w, 100, 200, 125)
        self.assertEqual(w.getvalue(), "100 200 125\n")

    def test_print_3(self):
        w = StringIO()
        collatz_print(w, 201, 210, 89)
        self.assertEqual(w.getvalue(), "201 210 89\n")

    def test_print_4(self):
        w = StringIO()
        collatz_print(w, 1000, 1000, 112)
        self.assertEqual(w.getvalue(), "1000 1000 112\n")

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
        r = StringIO("13 17\n780 699\n99 98\n450 140\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "13 17 18\n780 699 171\n99 98 26\n450 140 144\n")
        
    def test_solve_3(self):
        r = StringIO("13 13\n7777 7777\n1234 1\n34587 2\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "13 13 10\n7777 7777 84\n1234 1 182\n34587 2 311\n")




# ----
# main
# ----

if __name__ == "__main__":
    main()

""" #pragma: no cover
% coverage-3.5 run --branch TestCollatz.py >  TestCollatz.out 2>&1


% cat TestCollatz.out
..................
----------------------------------------------------------------------
Ran 18 tests in 4.957s

OK


% coverage-3.5 report -m                   >> TestCollatz.out



% cat TestCollatz.out
..................
----------------------------------------------------------------------
Ran 18 tests in 4.957s

OK
Name             Stmts   Miss Branch BrPart  Cover   Missing
------------------------------------------------------------
Collatz.py          34      0     14      0   100%
TestCollatz.py      80      0      0      0   100%
------------------------------------------------------------
TOTAL              114      0     14      0   100%
"""
