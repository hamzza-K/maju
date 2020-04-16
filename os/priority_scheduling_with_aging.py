

n = int(input("Enter the number of processes: "))

burst_time = list()
arrival_time = list()
priority = list()

processes = {}

for i in range(n):
	print(f"Enter the arrival time of P{i+1}: ")
	inp = int(input())
	if inp < 0:
		inp = 0
	arrival_time.append(inp)

for i in range(n):
	print(f"Enter the burst time of P{i+1}: ")
	inp = int(input())
	if inp < 1:
		inp = 1
	burst_time.append(inp)

for i in range(n):
	results = 20 - burst_time[i]
	priority.append(results)


for i in range(n):
	processes[f"P{i+1}"] = [arrival_time[i], burst_time[i], priority[i], 0]


# for keys, values in processes.items():
# 	print(keys, processes[keys])



k = {k: v for k, v in sorted(processes.items(), key=lambda item: item[1][0])}
# print(k)

t = 0
idle_time = 0

first_process = list(k.keys())[0]

idle_time = processes[first_process][0] - t

t = processes[first_process][0]



def print_processes(processes):
	statement = "Process\t  Arrival Time\t Burst Time\t Priority\t Aging"
	print(statement)
	print('+'+'-'*65+'+')
	for k, v in processes.items():
		print(f"{k}\t    {v[0]}\t\t    {v[1]}\t\t    {v[2]}\t\t    {v[3]}")
		print('+'+'-'*65+'+')

print_processes(k)
l = list(k.keys())
if idle_time != 0:
	print(f"The CPU is idle for unit time {idle_time}")
print(f"The process {first_process} begins at time unit {t}..")
print(f"The process {first_process} preempts back to ready queue at time unit {k[l[1]][0]}")








