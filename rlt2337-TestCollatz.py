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

from Collatz import collatz_read, cycle_length, largest_cycle, get_full_interval, get_part_intervals, get_interval_range, find_largest_cached_cycle, collatz_eval, collatz_print, collatz_solve

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
        s = "29 55\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  29)
        self.assertEqual(j, 55)

    def test_read_3(self):
        s = "60 14\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  60)
        self.assertEqual(j, 14)

    def test_read_4(self):
        s = "10 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  10)
        self.assertEqual(j, 10)



    # ------------
    # cycle_length
    # ------------
    
    def test_cycle_1(self):
        c = cycle_length (1)
        self.assertEqual(c, 1)

    def test_cycle_2(self):
        c = cycle_length (21)
        self.assertEqual(c, 8)

    def test_cycle_1(self):
        c = cycle_length (6)
        self.assertEqual(c, 9)



    # ------------
    # largest_cycle
    # ------------

    def test_largest_cycle_1(self):
        v = largest_cycle(1, 10)
        self.assertEqual(v, 20)

    def test_largest_cycle_2(self):
        v = largest_cycle(100, 200)
        self.assertEqual(v, 125)

    def test_largest_cycle_3(self):
        v = largest_cycle(201, 210)
        self.assertEqual(v, 89)

    def test_largest_cycle_4(self):
        v = largest_cycle(1000, 1000)
        self.assertEqual(v, 112)

    def test_largest_cycle_5(self):
        v = largest_cycle(3001, 3001)
        self.assertEqual(v, 41)



    # -----------------
    # get_full_interval
    # -----------------
    
    def test_get_full_interval_1(self):
        intr = get_full_interval(889)
        val = (1, 1000)
        self.assertEqual(intr, val)

    def test_get_full_interval_2(self):
        intr = get_full_interval(98032)
        val = (98001, 99000)
        self.assertEqual(intr, val)

    def test_get_full_interval_3(self):
        intr = get_full_interval(1)
        val = (1, 1000)
        self.assertEqual(intr, val)

    def test_get_full_interval_4(self):
        intr = get_full_interval(722312)
        val = (722001, 723000)
        self.assertEqual(intr, val)

    def test_get_full_interval_5(self):
        intr = get_full_interval(1000)
        val = (1, 1000)
        self.assertEqual(intr, val)

    def test_get_full_interval_6(self):
        intr = get_full_interval(3001)
        val = (3001, 4000)
        self.assertEqual(intr, val)




    # ------------------
    # get_part_intervals
    # ------------------

    def test_get_part_intervals_1(self):
        intrs = get_part_intervals (2, 88723)
        val = (2, 1000), (88001, 88723)
        self.assertEqual(intrs, val)

    def test_get_part_intervals_2(self):
        intrs = get_part_intervals (3500, 7500)
        val = (3500, 4000), (7001, 7500)
        self.assertEqual(intrs, val)

    def test_get_part_intervals_3(self):
        intrs = get_part_intervals (77999, 78001)
        val = (77999, 78000), (78001, 78001)
        self.assertEqual(intrs, val)

    def test_get_part_intervals_3(self):
        intrs = get_part_intervals (1000, 3001)
        val = (1000, 1000), (3001, 3001)
        self.assertEqual(intrs, val)



    # ------------------
    # get_interval_range
    # ------------------

    def test_get_interval_range_1(self):
        intrs = get_interval_range((1,1000), (5001,6000))
        val = [(1,1000), (1001,2000), (2001,3000), (3001,4000), (4001,5000), (5001,6000)]
        self.assertEqual(intrs,val)

    def test_get_interval_range_2(self):
        intrs = get_interval_range((778001,779000), (782001,783000))
        val = [(778001, 779000), (779001, 780000), (780001, 781000), (781001, 782000), (782001, 783000)]
        self.assertEqual(intrs,val)

    def test_get_interval_range_3(self):
        intrs = get_interval_range((1,1000), (3001,4000))
        val = [(1,1000), (1001,2000), (2001,3000), (3001,4000)]
        self.assertEqual(intrs,val)        

    # -------------------------
    # find_largest_cached_cycle
    # -------------------------

    def test_find_largest_cached_cycle_1(self):
        v = find_largest_cached_cycle (1, 99900)
        self.assertEqual(v, 351)

    def test_find_largest_cached_cycle_2(self):
        v = find_largest_cached_cycle (88234, 99991)
        self.assertEqual(v, 333)

    def test_find_largest_cached_cycle_3(self):
        v = find_largest_cached_cycle (123, 239234)
        self.assertEqual(v, 443)

    def test_find_largest_cached_cycle_4(self):
        v = find_largest_cached_cycle (124234, 992304)
        self.assertEqual(v, 525)

    def test_find_largest_cached_cycle_5(self):
        v = find_largest_cached_cycle (1000, 3001)
        self.assertEqual(v, 217)

    def test_find_largest_cached_cycle_6(self):
        v = find_largest_cached_cycle (1001, 3000)
        self.assertEqual(v, 217)

    def test_find_largest_cached_cycle_7(self):
        v = find_largest_cached_cycle (1002, 2001)
        self.assertEqual(v, 182)

    def test_find_largest_cached_cycle_8(self):
        v = find_largest_cached_cycle (1001, 3800)
        self.assertEqual(v, 238)


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
        v = collatz_eval(1000, 900)
        self.assertEqual(v, 174)

    def test_eval_6(self):
        v = collatz_eval(21, 21)
        self.assertEqual(v, 8)

    def test_eval_7(self):
        v = collatz_eval(1001, 2000)
        self.assertEqual(v, 182)

    def test_eval_8(self):
        v = collatz_eval(1002, 2001)
        self.assertEqual(v, 182)

    def test_eval_9(self):
        v = collatz_eval(1002, 322400)
        self.assertEqual(v, 443)



    # -----
    # print
    # -----

    def test_print_1(self):
        w = StringIO()
        collatz_print(w, 100, 200, 125)
        self.assertEqual(w.getvalue(), "100 200 125\n")
    
    def test_print_2(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_3(self):
        w = StringIO()
        collatz_print(w, 21, 21, 8)
        self.assertEqual(w.getvalue(), "21 21 8\n")
    


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
        r = StringIO("1 10\n1 10\n1 10\n1 10\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n1 10 20\n1 10 20\n1 10 20\n")

    def test_solve_3(self):
        r = StringIO("1 1\n21 21\n1000 900\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 1 1\n21 21 8\n1000 900 174\n900 1000 174\n")

    def test_solve_4(self):
        r = StringIO("\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "")

    


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
