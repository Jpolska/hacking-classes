""" This method is based on Floyd's cycle detection algorithm also
    known as tortoise and hare, which represents graphs vertexes. At each
    iteration of the main loop tortoise moves forward by one vertex (one
    hash) and hare moves two times faster. At some point they'll meet. That's
    the position where collision occours. Then we set up another tortoise from
    the beginning. We need to remember the previous value to get the collision.
"""

from f import get_f

SIZE = 18  # Difficulty of the hash
f = get_f(SIZE)

starting_point = ""
tortoise = f(starting_point)
last_hare = starting_point
hare = f(f(last_hare))

hash_calculations = 3
while hare != tortoise:
    tortoise = f(tortoise)
    last_hare = hare
    hare = f(f(hare))

    hash_calculations += 3

# We found one colliding vertex
y = f(last_hare)
collision = f(y)

print "Found colliding point in {0} steps".format(hash_calculations)

# We need to get the second
last_x = starting_point
x = f(last_x)
while x != collision:
    last_x = x
    x = f(x)
    hash_calculations += 1

print "Found collision in {0} steps in total".format(hash_calculations)
print "f('{0}') == f('{1}')".format(x, y)
