# 0X08 Networking basics #1

## Project Overview

Welcome to the 0x08. Networking basics #1 project! In this module, we embark on a journey through essential networking concepts. Unraveling the mysteries behind localhost, 0.0.0.0, and /etc/hosts, the project provides a solid understanding of these foundational elements in computer networking. Additionally, you'll learn how to display active network interfaces on your machine using tools like ifconfig, telnet, nc, and cut.

Each task is carefully designed to build your expertise, offering hands-on experience with practical scripts and real-world scenarios. By the end of this project, you'll have a solid foundation in networking basics, empowering you to navigate and troubleshoot networking issues effectively. Dive in, explore, and enjoy the journey through the intricacies of computer networking!

## Tasks

### 0. Change your home IP

Write a Bash script that configures an Ubuntu server with the below requirements.

**Requirements:**
- localhost resolves to 127.0.0.2
- facebook.com resolves to 8.8.8.8.

**Example:**

```bash
sylvain@ubuntu$ ping localhost
# Output truncated for brevity
sylvain@ubuntu$ sudo ./0-change_your_home_IP
# Output truncated for brevity
sylvain@ubuntu$ ping localhost
# Output truncated for brevity
```

**In this example, we can see that:**
- before running the script, localhost resolves to 127.0.0.1 and facebook.com resolves to 157.240.11.35
- after running the script, localhost resolves to 127.0.0.2 and facebook.com resolves to 8.8.8.8

If you’re running this script on a machine that you’ll continue to use, be sure to revert localhost to 127.0.0.1. Otherwise, a lot of things will stop working!

- **Repo:** alx-system_engineering-devops
- **Directory:** 0x08-networking_basics_2
- **File:** [0-change_your_home_IP](./0-change_your_home_IP)

### 1. Show attached IPs

Write a Bash script that displays all active IPv4 IPs on the machine it’s executed on.

**Example:**

```bash
sylvain@ubuntu$ ./1-show_attached_IPs | cat -e
# Output truncated for brevity
```

Obviously, the IPs displayed may be different depending on which machine you are running the script on.

Note that we can see our localhost IP :)

- **Repo:** alx-system_engineering-devops
- **Directory:** 0x08-networking_basics_2
- **File:** [1-show_attached_IPs](./1-show_attached_IPs)

### 2. Port listening on localhost

Write a Bash script that listens on port 98 on localhost.


Starting my script.

```bash
sylvain@ubuntu$ sudo ./100-port_listening_on_localhost
```

**Terminal 1:**

Connecting to localhost on port 98 using telnet and typing some text.

```bash
sylvain@ubuntu$ telnet localhost 98
# Output truncated for brevity
```

**Terminal 0:**

Receiving the text on the other side.

```bash
sylvain@ubuntu$ sudo ./100-port_listening_on_localhost
# Output truncated for brevity
```

For the sake of the exercise, this connection is made entirely within localhost. This isn’t really exciting as is, but we can use this script across networks as well. Try running it between your local PC and your remote server for fun!

As you can see, this can come in very handy in a multitude of situations. Maybe you’re debugging socket connection issues, or you’re trying to connect to a software and you are unsure if the issue is the software or the network, or you’re working on firewall rules… Another tool to add to your debugging toolbox!

- **Repo:** alx-system_engineering-devops
- **Directory:** 0x08-networking_basics_2
- **File:** [100-port_listening_on_localhost](./100-port_listening_on_localhost)

## Conclusion

The Networking Basics #1 project (0x08) covers essential topics to deepen understanding of network configurations and functionalities. Tasks involve configuring IP addresses, displaying active IPs, and creating a script for port listening on localhost. By exploring these tasks, users gain valuable insights into manipulating network settings, troubleshooting connectivity issues, and debugging socket connections. The completion of these tasks not only enhances technical proficiency but also provides practical tools for network-related problem-solving.
