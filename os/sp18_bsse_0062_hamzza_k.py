
class PrioritySchedulingWithAging(object):

    def algorithm(self, data):
        starting = list()
        ending = list()
        state = 0
        sequence = list()
        data.sort(key=lambda x: x[1], reverse=False)
        while True:
            ready_q = list()
            normal_q = list()
            t = list()
            for i in range(len(data)):
                # pid, arrival, burst, priority, 0, burst
                if data[i][1] <= state and data[i][4] == 0:
                    t.extend([data[i][0], data[i][1], data[i][2], data[i][3],
                                 data[i][5]])
                    ready_q.append(t)
                    t = list()
                elif data[i][4] == 0:
                    t.extend([data[i][0], data[i][1], data[i][2], data[i][4],
                                 data[i][5]])
                    normal_q.append(t)
                    t = list()
            if len(ready_q) == 0 and len(normal_q) == 0:
                break
            if len(ready_q) != 0:
                if state != 0:
                    ready_q.sort(key=lambda x: x[3], reverse=True)
                starting.append(state)
                state += 1
                e = state
                ending.append(e)
                sequence.append(ready_q[0][0])
                for k in range(len(data)):
                    if data[k][0] == ready_q[0][0]:
                        break
                data[k][2] = data[k][2] - 1
                age = state - data[k][1]
                data[k][3] = data[k][2] + age
                if data[k][2] == 0: 
                    data[k][4] = 1
                    data[k].append(e)
            if len(ready_q) == 0:
                normal_q.sort(key=lambda x: x[1])
                if state < normal_q[0][1]:
                    state = normal_q[0][1]
                starting.append(state)
                state += 1
                e = state
                ending.append(e)
                sequence.append(normal_q[0][0])
                for k in range(len(data)):
                    if data[k][0] == normal_q[0][0]:
                        break
                data[k][2] = data[k][2] - 1
                age = state - data[k][1]
                data[k][3] = data[k][2] + age
                if data[k][2] == 0: 
                    data[k][4] = 1
                    data[k].append(e)
        tat = PrioritySchedulingWithAging.calculating_turnaround_time(self, data)
        wt = PrioritySchedulingWithAging.calculating_waiting_time(self, data)
        PrioritySchedulingWithAging.show(self, data, tat, wt, sequence, ending)

    def getting_data(self, n):
        data = list()
        for i in range(n):
            t = list()
            pid = int(input("Enter Process ID: "))
            arrival = int(input(f"Enter Arrival Time for Process {pid}: "))
            burst = int(input(f"Enter Burst Time for Process {pid}: "))
            priority = 20 - burst
            t.extend([pid, arrival, burst, priority, 0, burst])
            data.append(t)
        PrioritySchedulingWithAging.algorithm(self, data)


    def calculating_turnaround_time(self, data):
        total = 0
        for i in range(len(data)):
            tat_time = data[i][6] - data[i][5]
            total += tat_time
            data[i].append(total)
        average = total / len(data)
        '''
        average_turnaround_time = total_turnaround_time / n
        '''
        return average

    def calculating_waiting_time(self, data):
        total = 0
        for i in range(len(data)):
            wt_time = data[i][6] - data[i][2]
            total += wt_time
            data[i].append(wt_time)
        average = total / len(data)
        return average

    def show(self, data, average_turnaround_time, average_waiting_time, sequence, ending):
        data.sort(key=lambda x: x[0])
        '''
        Sort processes according to the Process ID
        '''
        print("pid\t    arrival\t     priority\t  burst time\t       tat\t        wt")
        print('+'+'-'*105+'+')
        for i in range(len(data)):
            for j in range(len(data[i])):
                if j not in [2, 4, 6]:
                    print(data[i][j], end="\t\t")
            print()


        data.sort(key=lambda x: x[1])

        f = data[0][1]

        cpu = (len(sequence) - f)/len(sequence) * 100
        throughput = len(data) / sum(ending) * 100

        print(f'Average Turnaround Time: {average_turnaround_time}')
        print(f'Average Waiting Time: {average_waiting_time}')
        print(f'CPU utilization {cpu:.2f}')
        print(f'throughput {throughput:.2f}')
        print(f'Sequence of Process: {sequence}')


if __name__ == "__main__":
    n = int(input("Enter number of processes: "))
    p = PrioritySchedulingWithAging()
    p.getting_data(n)