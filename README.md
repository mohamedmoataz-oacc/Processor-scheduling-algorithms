# Processor-scheduling-algorithms
<h4>Here you can find the implementation of some algorithms used in processor scheduling, implemented in Python.</h4>

<h3>SJF (Shortest Job First):</h3>
A scheduling policy that selects the waiting process with the smallest execution time to execute next.

<img style="display: block;-webkit-user-select: none;margin: auto;cursor: zoom-in;background-color: hsl(0, 0%, 90%);transition: background-color 300ms;" src="https://i.ibb.co/4Pt2dw7/sjf.jpg" width="522" height="393">

<h3>RR (Round Robin):</h3>
To schedule processes fairly, a round-robin scheduler generally employs time-sharing, giving each job a time slot or quantum (its allowance of CPU time), and interrupting the job if it is not completed by then. The job is resumed next time a time slot is assigned to that process. If the process terminates or changes its state to waiting during its attributed time quantum, the scheduler selects the first process in the ready queue to execute.

<img style="display: block;-webkit-user-select: none;margin: auto;cursor: zoom-in;background-color: hsl(0, 0%, 90%);transition: background-color 300ms;" src="https://i.ibb.co/jzgPbPV/rr.jpg" width="406" height="393">
