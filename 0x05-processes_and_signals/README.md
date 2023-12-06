# 0x05 Processes and Signals

## Overview

This projct covers a set of Bash scripts and a C program focused on processes and signals. The tasks involve creating scripts to display process information, managing processes, and handling signals. Additionally, a C program is provided to demonstrate the creation of zombie processes.

## Tasks

### Task 0: What is my PID

#### Script: 0-what-is-my-pid

This Bash script displays its own PID.

```bash
sylvain@ubuntu$ ./0-what-is-my-pid
4120
sylvain@ubuntu$
```

### Task 1: List your processes

#### Script: 1-list_your_processes

This Bash script displays a list of currently running processes, showing all processes for all users, including those without a TTY.

```bash
sylvain@ubuntu$ ./1-list_your_processes | head -50
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         2  0.0  0.0      0     0 ?        S    Feb13   0:00 [kthreadd]
...
```

### Task 2: Show your Bash PID

#### Script: 2-show_your_bash_pid

This Bash script displays lines containing the word "bash" and allows easy retrieval of the PID of the Bash process.

```bash
sylvain@ubuntu$ ./2-show_your_bash_pid
sylvain   4404  0.0  0.7  21432  4000 pts/0    Ss   03:32   0:00          \_ -bash
...
```

### Task 3: Show your Bash PID made easy

#### Script: 3-show_your_bash_pid_made_easy

This Bash script displays the PID and process name of processes containing the word "bash."

```bash
sylvain@ubuntu$ ./3-show_your_bash_pid_made_easy
4404 bash
4555 bash
...
```

### Task 4: To infinity and beyond

#### Script: 4-to_infinity_and_beyond

This Bash script displays "To infinity and beyond" indefinitely with a sleep of 2 seconds between each iteration.

```bash
sylvain@ubuntu$ ./4-to_infinity_and_beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
...
```

### Task 5: Don't stop me now!

#### Script: 5-dont_stop_me_now

This Bash script stops the process created by the script in Task 4.

```bash
sylvain@ubuntu$ ./5-dont_stop_me_now
sylvain@ubuntu$
```

### Task 6: Stop me if you can

#### Script: 6-stop_me_if_you_can

This Bash script stops the process created by the script in Task 4 without using `kill` or `killall`.

```bash
sylvain@ubuntu$ ./6-stop_me_if_you_can
sylvain@ubuntu$
```

### Task 7: Highlander

#### Scripts: 7-highlander and 67-stop_me_if_you_can

The 7-highlander script displays "To infinity and beyond" and "I am invincible!!!" when receiving a SIGTERM signal. The 67-stop_me_if_you_can script kills the 7-highlander process.

```bash
sylvain@ubuntu$ ./7-highlander
To infinity and beyond
I am invincible!!!
...
sylvain@ubuntu$ ./67-stop_me_if_you_can
sylvain@ubuntu$
```

### Task 8: Beheaded process

#### Script: 8-beheaded_process

This Bash script kills the process created by the script in Task 7.

```bash
sylvain@ubuntu$ ./8-beheaded_process
sylvain@ubuntu$
```

### Task 9: Process and PID file

#### Script: 100-process_and_pid_file

This Bash script creates the file `/var/run/myscript.pid` containing its PID, displays messages, and terminates itself on receiving specific signals.

```bash
sylvain@ubuntu$ sudo ./100-process_and_pid_file
To infinity and beyond
I hate the kill command
...
```

### Task 10: Manage my process

#### Scripts: manage_my_process and 101-manage_my_process

The `manage_my_process` Bash script writes "I am alive!" to the file `/tmp/my_process`. The `101-manage_my_process` init script manages the `manage_my_process` script, providing start, stop, and restart functionalities.

```bash
sylvain@ubuntu$ sudo ./101-manage_my_process start
manage_my_process started
...
sylvain@ubuntu$ sudo ./101-manage_my_process stop
manage_my_process stopped
...
sylvain@ubuntu$ sudo ./101-manage_my_process restart
manage_my_process restarted
...
```

### Task 11: Zombie

#### C Program: 102-zombie.c

This C program creates 5 zombie processes, displaying messages with their PIDs.

```bash
sylvain@ubuntu$ gcc 102-zombie.c -o zombie
sylvain@ubuntu$ ./zombie
Zombie process created, PID: 13527
Zombie process created, PID: 13528
...
```

## Conclusion

This project covers a variety of tasks related to processes and signals, including process management, signal handling, and creating zombie processes. The Bash scripts and C program provide practical examples and demonstrate the handling of different scenarios.

This project is powered by ALX Africa 2023
