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
        self.assertEqual(j,  1)

    def test_read_3(self):
        s = "999 999"
        i, j = collatz_read(s)
        self.assertEqual(i, 999)
        self.assertEqual(j, 999)


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
        v = collatz_eval(129, 129)
        self.assertEqual(v, 122)

    def test_eval_6(self):
        v = collatz_eval(654321, 123456)
        self.assertEqual(v, 509)
    # -----
    # print
    # -----

    def test_print_1(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2(self):
        w = StringIO()
        collatz_print(w, 129, 129, 129)
        self.assertEqual(w.getvalue(), "129 129 129\n")

    def test_print_3(self):
        w = StringIO()
        collatz_print(w, 3, 1, 67)
        self.assertEqual(w.getvalue(), "3 1 67\n")

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
        r = StringIO("129 129\n150 100\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "129 129 122\n150 100 122\n")

    def test_solve_3(self):
        r = StringIO("10 1\n1 1\n 2 1\n 13 10\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "10 1 20\n1 1 1\n2 1 2\n13 10 15\n")

# ----
# main
# ----

if __name__ == "__main__":
    main()

