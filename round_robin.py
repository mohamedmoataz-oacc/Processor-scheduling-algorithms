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
        processes.append([f'P{total_processes}', int(t)])
        print(f'P{total_processes} arrived at time {int(time.time() - time_counter)}')
        total_processes += 1
 
def finishProcess(quantum):
    global processes, time_counter, beautify
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
        if beautify:
            print('\n')
            beautify = False
        print(f'{name} finished at time {int(time.time() - time_counter)}')
 
processes = list()
go_on, beautify = True, True
time_counter = time.time()

Thread(target = newProcess).start()
print("Enter 'exit' to stop the program")
while go_on:
    finishProcess(4)