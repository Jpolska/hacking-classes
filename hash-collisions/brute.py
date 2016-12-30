""" Brute force solution. At the beggining calculate starting_hash = f("").
    Each time generate new x and check if f(x) == starting_hash
"""

from f import get_f

SIZE = 4  # Difficulty of the hash
f = get_f(SIZE)

y = ""
starting_hash = f(y)
x = 0  # We'll generate new x's just by adding one
hash_calculations = 1
while f(str(x)) != starting_hash:
    hash_calculations += 1
    x += 1

print "Found collision in {0} steps".format(hash_calculations)
print "f('{0}') == f('{1}')".format(y, x)
