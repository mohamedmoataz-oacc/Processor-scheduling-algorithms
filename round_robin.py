from threading import Thread
import time
 
def newProcess():
    global processes, go_on, time_counter, beautify, table_data
    total_processes = 0

    while True:
        t = input("Enter burst time of process: ")
        beautify = True

        if t == 'exit':
            print("Exiting...")
            go_on = False
            break

        processes.append([f'P{total_processes}', int(t)])
        arrival = int(time.time() - time_counter)
        table_data[f'P{total_processes}'] = {
            'Arrival Time': arrival,
            'Burst Time': int(t)
        }

        print(f'P{total_processes} arrived at time {arrival}')
        total_processes += 1
 
def finishProcess(quantum):
    global processes, time_counter, beautify, table_data
    if len(processes) == 0: return

    p = processes.pop(0)
    name = p[0]
    t = p[1]

    time.sleep(t if t <= quantum else quantum)
    t -= quantum
    if t > 0:
        p[1] = t
        processes.append(p)
    else:
        finish = int(time.time() - time_counter)
        table_data[name].update({
            'Completion Time': finish,
            'Waiting Time': finish - table_data[name].get('Burst Time'),
            'Turnaround Time': finish - table_data[name].get('Arrival Time')
        })

        if beautify:
            print('\n')
            beautify = False
        print(f'{name} finished at time {finish}')
 
processes = list()
table_data = dict()
go_on, beautify = True, True
time_counter = time.time()

print("Enter 'exit' to stop the program if there are no processes running.")
print("If a process was running, the program will exit after it finishes.")
quantum = int(input('Enter quantum time: '))
Thread(target = newProcess).start()
while go_on or len(processes) > 0:
    finishProcess(quantum)

print_head = True
for k, v in table_data.items():
    if print_head:
        print_head = False
        print(f"{' ' * 4}\t", end='')
        for i in v.keys():
            print(i, end='   ')
        print('\n')
    print(f'{k}:\t', end='')
    for j, i in v.items():
        print('   ', i, end = f"{' ' * (len(j) - len(str(i)) - 3)}  ")
    print('\n\n')

awt = 0
att = 0
for k, v in table_data.items():
    awt += v['Waiting Time']
    att += v['Turnaround Time']
print('Average waiting time:', round(awt / len(table_data), 3))
print('Average turnaround time:', round(att / len(table_data), 3))