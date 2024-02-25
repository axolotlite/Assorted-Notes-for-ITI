by default docker limits the capabilities of a container, we can use commands to add or remove these capabilities
using these parameters we can add or remove capabilities from the root account of a docker container:
`--cap-add`
`--cap-drop`

these are the available capabilities
|Capability Key| Capability Description|
|----------|-----|
|AUDIT_WRITE| 	Write records to kernel auditing log.|
|CHOWN| 	Make arbitrary changes to file UIDs and GIDs (see chown(2)).|
|DAC_OVERRIDE| 	Bypass file read, write, and execute permission checks.|
|FOWNER| 	Bypass permission checks on operations that normally require the file system ||UID| of the process to match the UID of the file.|
|FSETID| 	Don’t clear set-user-ID and set-group-ID permission bits when a file is modified.|
|KILL| 	Bypass permission checks for sending signals.|
|MKNOD| 	Create special files using mknod(2).|
|NET_BIND_SERVICE| 	Bind a socket to internet domain privileged ports (port numbers less |than 1024).
|NET_RAW| 	Use RAW and PACKET sockets.|
|SETFCAP| 	Set file capabilities.|
|SETGID| 	Make arbitrary manipulations of process GIDs and supplementary GID list.|
|SETPCAP| 	Modify process capabilities.|
|SETUID| 	Make arbitrary manipulations of process UIDs.|
|SYS_CHROOT| 	Use chroot(2), change root directory.|

The next table shows the capabilities which are not granted by default and may be added.
|Capability Key | 	Capability Description|
|--------------|----------------|
|AUDIT_CONTROL| 	Enable and disable kernel auditing; change auditing filter rules; retrieve auditing status and filtering rules.|
|AUDIT_READ| 	Allow reading the audit log via multicast netlink socket.|
|BLOCK_SUSPEND| 	Allow preventing system suspends.|
|BPF| 	Allow creating BPF maps, loading BPF Type Format (BTF) data, retrieve JITed code of |BPF| programs, and more.|
|CHECKPOINT_RESTORE| 	Allow checkpoint/restore related operations. Introduced in kernel 5.9.|
|DAC_READ_SEARCH| 	Bypass file read permission checks and directory read and execute permission checks.|
|IPC_LOCK| 	Lock memory (mlock(2), mlockall(2), mmap(2), shmctl(2)).|
|IPC_OWNER| 	Bypass permission checks for operations on System V IPC objects.|
|LEASE| 	Establish leases on arbitrary files (see fcntl(2)).|
|LINUX_IMMUTABLE| 	Set the FS_APPEND_FL and FS_IMMUTABLE_FL i-node flags.|
|MAC_ADMIN| 	Allow MAC configuration or state changes. Implemented for the Smack LSM.|
|MAC_OVERRIDE| 	Override Mandatory Access Control (MAC). Implemented for the Smack Linux Security Module (LSM).|
|NET_ADMIN| 	Perform various network-related operations.|
|NET_BROADCAST| 	Make socket broadcasts, and listen to multicasts.|
|PERFMON| 	Allow system performance and observability privileged operations using perf_events, i915_perf and other kernel subsystems|
|SYS_ADMIN| 	Perform a range of system administration operations.|
|SYS_BOOT| 	Use reboot(2) and kexec_load(2), reboot and load a new kernel for later execution.|
|SYS_MODULE| 	Load and unload kernel modules.|
|SYS_NICE| 	Raise process nice value (nice(2), setpriority(2)) and change the nice value for arbitrary processes.|
|SYS_PACCT| 	Use acct(2), switch process accounting on or off.|
|SYS_PTRACE| 	Trace arbitrary processes using ptrace(2).|
|SYS_RAWIO| 	Perform I/O port operations (iopl(2) and ioperm(2)).|
|SYS_RESOURCE| 	Override resource Limits.|
|SYS_TIME| 	Set system clock (settimeofday(2), stime(2), adjtimex(2)); set real-time (hardware) clock.|
|SYS_TTY_CONFIG| 	Use vhangup(2); employ various privileged ioctl(2) operations on virtual terminals.|
|SYSLOG| 	Perform privileged syslog(2) operations.|
|WAKE_ALARM| 	Trigger something that will wake up the system.|

Further reference information is available on the capabilities(7) - Linux man page, and in the Linux kernel source code.

Both flags support the value ALL, so to allow a container to use all capabilities except for MKNOD:

 `docker run --cap-add=ALL --cap-drop=MKNOD`

The --cap-add and --cap-drop flags accept capabilities to be specified with a CAP_ prefix. The following examples are therefore equivalent:

 `docker run --cap-add=SYS_ADMIN ...`

 `docker run --cap-add=CAP_SYS_ADMIN ...`