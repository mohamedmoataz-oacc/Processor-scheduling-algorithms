from threading import Thread
import time
 
def newProcess():
    global processes, go_on, time_counter, beautify
    t = ''
    total_processes = 0
    while True:
        t = input("Enter burst time of process: ")
        beautify = True
        if t == 'exit':
            go_on = False
            break
        if int(t) in processes.keys(): processes[int(t)].append(f'P{total_processes}')
        else: processes[int(t)] = [f'P{total_processes}']
        print(f'P{total_processes} arrived at time {time_counter}')
        total_processes += 1
 
def finishProcess():
    global processes, time_counter, beautify
    if len(processes) == 0: return
    sjt = min(processes.keys())
    if len(processes[sjt]) == 1: name = processes.pop(sjt).pop(0)
    else: name = processes[sjt].pop(0)
    time.sleep(sjt)
    if beautify:
        print('\n')
        beautify = False
    print(f'{name}:({sjt}) finished at time {time_counter}')
 
def countTime():
    global time_counter
    while True:
        time.sleep(1)
        time_counter += 1

processes = dict()
go_on, beautify = True, True
time_counter = 0
 
Thread(target = countTime).start()
Thread(target = newProcess).start()
print("Enter 'exit' to stop the program")
while go_on:
    finishProcess()