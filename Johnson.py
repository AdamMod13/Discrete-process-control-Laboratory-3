from RandomNumberGenerator import RandomNumberGenerator
import random
import random

rng = RandomNumberGenerator(1)
def Johnson(tasks):
    n = len(tasks)
    p1 = [task[0] for task in tasks]
    p2 = [task[1] for task in tasks]

    pi = [0] * n
    l = 0  # pi[0] is the dummy task
    k = n - 1
    N = list(range(n))

    while N:
        min_p1 = min(p1)
        min_p2 = min(p2)
        if min_p1 >= min_p2:
            j_star = p2.index(min_p2)
        else:
            j_star = p1.index(min_p1)
        pi[l] = N.pop(j_star)
        l += 1
        p1.pop(j_star)
        p2.pop(j_star)
    return pi

random = random.Random(42)
n = 4
tasks = [[rng.nextInt(1, 29), rng.nextInt(1, 29)] for _ in range(n)]
print(tasks)

pi = Johnson(tasks)
print(pi)
