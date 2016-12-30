""" The approach based on birtday paradox. The main idea is to store
    all calculated hashes in memory and check if we hadn't generated
    the same hash before.
"""

from f import get_f

SIZE = 12  # Difficulty of the hash
f = get_f(SIZE)

x = 0  # We'll generate new x's just by adding one
curr_hash = f(str(x))
saved_hashes = {}
hash_calculations = 1
while curr_hash not in saved_hashes:
    saved_hashes[curr_hash] = x
    x += 1
    curr_hash = f(str(x))
    hash_calculations += 1

print "Found collision in {0} steps".format(hash_calculations)
print "f('{0}') == f('{1}')".format(str(x), saved_hashes[curr_hash])
