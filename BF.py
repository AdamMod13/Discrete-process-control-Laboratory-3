from RandomNumberGenerator import RandomNumberGenerator
from itertools import permutations

def brute_force_cmax(jobs, machines):
    job_permutations = permutations(jobs)
    
    min_cmax = float('inf')
    for permutation in job_permutations:
        machine_times = [0] * machines
        for job in permutation:
            machine_times[0] += job[0]
            for i in range(1, machines):
                machine_times[i] = max(machine_times[i], machine_times[i-1]) + job[i]
        cmax = machine_times[-1]
        
        if cmax < min_cmax:
            min_cmax = cmax
            
    return min_cmax

rng = RandomNumberGenerator(1)
machines = 4

n = 4
tasks = [[rng.nextInt(1, 29), rng.nextInt(1, 29), rng.nextInt(1, 29), rng.nextInt(1, 29)] for _ in range(n)]
print(tasks)

cmax = brute_force_cmax(tasks, machines)
print(cmax) 