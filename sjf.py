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
        
        if int(t) in processes.keys(): processes[int(t)].append(f'P{total_processes}')
        else: processes[int(t)] = [f'P{total_processes}']

        arrival = int(time.time() - time_counter)
        table_data[f'P{total_processes}'] = {
            'Arrival Time': arrival,
            'Burst Time': int(t)
        }
        print(f'P{total_processes} arrived at time {arrival}')
        total_processes += 1
 
def finishProcess():
    global processes, time_counter, beautify, table_data
    if len(processes) == 0: return

    sjt = min(processes.keys())
    if len(processes[sjt]) == 1: name = processes.pop(sjt).pop(0)
    else: name = processes[sjt].pop(0)

    time.sleep(sjt)
    finish = int(time.time() - time_counter)

    table_data[name].update({
        'Completion Time': finish,
        'Waiting Time': finish - table_data[name].get('Burst Time'),
        'Turnaround Time': finish - table_data[name].get('Arrival Time')
    })

    if beautify:
        print('\n')
        beautify = False
    print(f'{name}:({sjt}) finished at time {finish}')

processes = dict()
go_on, beautify = True, True
time_counter = time.time()
table_data = dict()

print("Enter 'exit' to stop the program if there are no processes running.")
print("If a process was running, the program will exit after it finishes.")
Thread(target = newProcess).start()
while go_on or len(processes) > 0: 
    finishProcess()

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