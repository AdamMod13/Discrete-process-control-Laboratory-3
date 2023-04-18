from RandomNumberGenerator import RandomNumberGenerator
import random

rng = RandomNumberGenerator(1)

def calculate(pi, times):
    return sum(times[pi[i]][pi[j]] for i in range(len(pi)) for j in range(i + 1, len(pi)))

n = 5 
J = list(range(n))
times = [[rng.nextInt(1, 29) for _ in range(n)] for _ in range(n)]  # Czasy wykonania operacji

print("Times:", times)

UB = float('inf')
init_pi = []
result_pi = []

def BnB(j_star, N, pi):
    pi.append(j_star)
    N.remove(j_star)

    global UB

    if not N:
        global Cmax 
        Cmax = calculate(pi, times)  
        if Cmax < UB:
            UB = Cmax
            result_pi.clear()
            result_pi.extend(pi)
    else:
        LB = calculate(pi, times)
        if LB < UB:
            for j in N:
                BnB(j, N.copy(), pi.copy())

for j in J:
    BnB(j, J.copy(), init_pi.copy())

print("Optimal Cmax:", Cmax)
print("Optimal permutation:", result_pi)
