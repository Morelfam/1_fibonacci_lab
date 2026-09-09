"""Fibonacci lab — run this to see which functions work.

Fix the bugs in fibonacci.py, then re-run.
"""

from fibonacci import fib, fib_sequence, golden_ratio_approx
import numpy


PASS = 0
TOTAL = 0


def check(label, actual, expected):
    """Compare actual to expected. Print PASS or FAIL. Update counters."""
    global PASS, TOTAL
    TOTAL += 1
    passed = actual == expected
    if passed:
        PASS += 1
    status = "PASS" if passed else "FAIL"
    print(f"  [{status}]  {label}")
    print(f"          got:      {actual!r}")
    print(f"          expected: {expected!r}")


def check_approx(label, actual, expected, tol=0.001):
    """Same as check() but allows a small numerical tolerance."""
    global PASS, TOTAL
    TOTAL += 1
    passed = abs(actual - expected) < tol
    if passed:
        PASS += 1
    status = "PASS" if passed else "FAIL"
    print(f"  [{status}]  {label}")
    print(f"          got:      {actual:.6f}")
    print(f"          expected: ~{expected:.6f}")


def main():
    global TOTAL
    print()
    print("=" * 60)
    print(" Fibonacci lab")
    print("=" * 60)

    print("\n [ Task 1 ]  fib(n)")
    check("fib(0)", fib(0), 0)
    check("fib(1)", fib(1), 1)
    check("fib(7)", fib(7), 13)
    check("fib(10)", fib(10), 55)

    print("\n [ Task 2 ]  fib_sequence(n)")
    check("fib_sequence(0)", fib_sequence(0), [])
    check("fib_sequence(1)", fib_sequence(1), [0])
    check("fib_sequence(8)", fib_sequence(8), [0, 1, 1, 2, 3, 5, 8, 13])

    print("\n [ Task 3 ]  golden_ratio_approx(n)")
    phi = (1 + 5 ** 0.5) / 2
    check_approx("golden_ratio_approx(20)", golden_ratio_approx(20), phi)

    print("\n [ Task 4 - Extension ]  Negative Fibonacci")
    print("  Formula:  F(-n) = (-1)^(n+1) * F(n)")
    print("  Examples: fib(-1) = 1,  fib(-6) = -8,  fib(-7) = 13")
    print()
    for arg, expected in [(-1, 1), (-6, -8), (-7, 13)]:
        try:
            actual = fib(arg)
            check(f"fib({arg})", actual, expected)
        except (ValueError, RecursionError):
            TOTAL += 1
            print(f"  [SKIP]  fib({arg}): not yet implemented")

    print()
    print("=" * 60)
    print(f" Summary: {PASS}/{TOTAL} checks passing")
    print("=" * 60)
    print()


if __name__ == "__main__":
    main()
