#Linux/theory
#Linux/commands
we can send different kinds of signals to a process, to either pause, resume or terminate the process.

pause can be done through:
`kill -SIGSTOP pid`
this preserves the state of the process, allowing us to resume the process without any damage using:
`kill -SIGCONT pid`
this allows it to continue where it left off.
to complete terminate the command we can send the terminate command.
`kill -SIGTERM pid`
this allows the process to perform cleanup before shutting down, but the process can ignore the signal and continue its own work.
if that happens we can force it to kill the process using 
`kill -SIGKILL pid`
this kills the process, it can't be caught by the process. it's executed by the OS.
we can find the pid of a process using `pgrep process_name`