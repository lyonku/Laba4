import math

if __name__ == '__main__':
    n = int(input("Value of n? "))
    x = float(input("Value of x? "))
    S = 0.0
for k in range(1, n + 1):
    a = math.log(k * n) / (n * n)
    S += a
print(f"S = {S}")
