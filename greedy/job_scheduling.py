jobs = [
    (3, 1), # job 1, profit 3, deadline 1
    (5, 3), # job 2, profit 5, deadline 3
    (20, 4),
    (18, 3),
    (1, 2),
    (6, 1),
    (30, 2),
]

# (Optional) set array with fixed size
scheduled_jobs = [None] * len(jobs)

# 1. Sort all jobs in desceding order of profit
sorted_jobs = sorted(jobs, key=lambda x: x[0], reverse=True)

units = 0

# loop through all jobs with index
for i, job in enumerate(sorted_jobs):
    profit, deadline = job
    if scheduled_jobs[deadline - 1] == None:
        scheduled_jobs[deadline - 1] = job
        units += profit

print(scheduled_jobs)
print(units)