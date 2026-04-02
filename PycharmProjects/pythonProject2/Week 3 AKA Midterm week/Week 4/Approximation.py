def sqrt(n):
    approx = n/2.0     # Start with some or other guess at the answer
    while True:
        next_approx = (approx + n/approx)/2.0
        if abs(approx - next_approx) < 0.001:
            return next_approx
        approx = next_approx

# Test cases
print(sqrt(9.0))