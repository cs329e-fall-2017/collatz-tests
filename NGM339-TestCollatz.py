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

    # ----
    # my unit tests of eval
    # ----
    def test_eval_m1(self):
        v = collatz_eval(525, 620)
        self.assertEqual(v, 137)

    def test_eval_m2(self):
        v = collatz_eval(8, 50000)
        self.assertEqual(v, 324)

    def test_eval_m3(self):
        v = collatz_eval(1002, 2000)
        self.assertEqual(v, 182)

    def test_eval_m4(self):
        v = collatz_eval(3000, 4200)
        self.assertEqual(v, 238)
    # -----
    # print
    # -----

    def test_print(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    # -----
    # my print tests
    # -----
    def test_print_m1(self):
        w = StringIO()
        collatz_print(w, 525, 620, 137)
        self.assertEqual(w.getvalue(), "525 620 137\n")

    def test_print_m2(self):
        w = StringIO()
        collatz_print(w, 8, 50000, 324)
        self.assertEqual(w.getvalue(), "8 50000 324\n")

    def test_print_m3(self):
        w = StringIO()
        collatz_print(w, 1002, 2000, 182)
        self.assertEqual(w.getvalue(), "1002 2000 182\n")

    def test_print_m4(self):
        w = StringIO()
        collatz_print(w, 99001, 98999, 116)
        self.assertEqual(w.getvalue(), "99001 98999 116\n")
    # -----
    # solve
    # -----

    def test_solve(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
    # -----
    # my solve tests
    # -----

    def test_solve_m1(self):
        r = StringIO("4666 6666\n200 20000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "4666 6666 262\n200 20000 279\n")

    def test_solve_m2(self):
        r = StringIO("68555 43222\n339 51999\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "68555 43222 340\n339 51999 324\n")

    def test_solve_m3(self):
        r = StringIO("3000 2001\n99999 99001\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "3000 2001 217\n99999 99001 328\n")


# ----
# main
# ----

if __name__ == "__main__":
    main()
