Finding hash collisions
=======================

I prepared 3 scripts that find hash collision i.e. for a given hash function f find two distinct values x != y that satisfies f(x) == f(y)

1) Brute force - for a given x generetes randon y until f(x)  == f(y)

2) Birthday Paradox - we keep every calculated hash in memory and with every new x we check if we haven't calculated the same hash

3) Floyd'd cycle detection algorithm (tortoise and hare) - we don't keep every hash in memory, just two of them. More info: https://en.wikipedia.org/wiki/Cycle_detection#Tortoise_and_hare
