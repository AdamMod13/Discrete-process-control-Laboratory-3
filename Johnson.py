from Classes import Task
from RandomNumberGenerator import RandomNumberGenerator

rng = RandomNumberGenerator(1)
p = []
for _ in range(0,10):
    p.append(rng.nextInt(1,29))

A = sum(p)

r = []
for _ in range(0,10):
    r.append(rng.nextInt(1,A))

X = A

q = []
for _ in range(0,10):
    q.append(rng.nextInt(1,X))

print(r)
print(p)
print(q)