# Writing a program to count the number of bits that are set to 1 in a positive integer.
import sys

def count_bits(x):
    num_bits = 0
    while x:
        num_bits += x & 1
        x >>= 1
    return num_bits

print(count_bits(21))

# print(sys.maxsize)
# print(sys.float_info)


# The time complexity isO(n), where n is the word size
def parity(x):
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result

print(parity(3)) # 011 -> 0
print(parity(4)) # 100 -> 1


# time complexity of the algorithm below is O(k), k be the number of bits set to 1 in a particular word
def parity_improved(x):
    result = 0
    while x:
        result ^= 1
        x &= x - 1 # Drops the -lowest set bit of x
    return result


x = 20 & ~19 # 10100 and ~10011 == 01100 
print(x)