import sys
import primes

h = 0
b = 105700
c = b + 17000

for n in range(b, c+1, 17):
    if not primes.is_prime(n):
        h += 1
print(h)

# while True:
#     f = 1
#     d = 2
#     while True:
#         e = 2
#         while True:
#             if d * e == b:
#                 f = 0
#             e += 1
#             if e == b:
#                 break
#         d += 1
#         if d == b:
#             break
#     if f == 0:
#         h += 1
#     if b == c:
#         print(h)
#         sys.exit()
#     b += 17