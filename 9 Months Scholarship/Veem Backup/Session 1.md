### Backup Architecture:
these are the components in a back up environment
#### Client backup methods:
These are the 2 main methods
- **Image Based**: 
	saving the entire client as an img / VM file, this is agentless, so no agent is pushed onto the client, so the backup is taken by a proxy.
	this is not effective when backing up a database, because this type of backup will corrupt it.
	vCenter Example:
	We have a guest VM on a vCenter host, to make an image backup of the VM, we'll have to install a specialized VM called "proxy vm" which acts as a middle-man between the host and the backup server (because the VM doesn't have an agent to communicate directly with the backup server).
	First of all the backup server sends to the proxy requesting to backup the guest vm, which causes the proxy to tell the vCenter host takes a snapshot of the guest VM then mount this snapshot in the proxy vm to allow it to transfer the snapshot to the backup server.
- **Agent Based**: 
	This pushes a specialized tool or set of tools, installs them on the client to do backups, depending on the agent function it could allow us to backup specific parts, or the whole client if needed.
	for example: we can install a special agent to backup the databases.
	Linux Example using a database backup agent (like oracles RMan agent):
	First, we start by downloading the linux specific agent on the machine to install it.
	After install, the agent will start discovering the files and directories inside the machine, this also applies to database systems.
	Then whenver a backup is requested by the server, the agent handles it by transferring the requested data to the backup server.
#### Back up Servers:
They can either be a specialized physical device (Physical Appliance) that takes the backup, or a virtual device (Virtual Appliance) that does the same.
both of them are capable of taking a backup or restoring it.
The following products are currently used in the market, with each having their special selling point
DELL EMC has the largest market share with these:
	Networker: wasn't an option until recently
	Avamar: allows for backup as a service
There are also:
Veeam: allows for backup as a service
CommVault: this is the most expensive one and has the most features.
NetBackup: allows for backup as a service

#### Backup Target:
This is where the backups are stored on, it's mostly placed on storage boxes but it also allows for usage of Cloud providers, NAS Devices, Tape Devices, etc...
The most famous backup target used in the middle east is `DELL EMC's Data Domain` now rebranded as `PowerProtect Data Domain` as of 2019.
Because it gives the best de-duplication ratio which may reach 99%.
#### Backup Types:
These are the 3 main types of backup
- **Full Backup**: we take a full backup of the data every backup run.
- **Incremental Backup**:
	needs at least 1 full back up, then any subsequent backup run will backup the changes from the previous taken backup.
	Full backup -> backup difference between this run and the Full backup -> backup the difference between this run and the previous run -> repeat until latest Full Backup
- **Cumulative Backup**:
	also needs 1 full back up, then each back up run backs up the different data from the last full backup, unlike the incremental which backs up the difference from the previous incremental back up run.
#### Important Terminologies:
Backup Window:
	This is the duration in which a backup is taken.
	for example:
	a  `backup window` of 2AM to 6AM means that backups are allowed to run during any time within this window, if the backup exceeds the window for example if the time reaches `6:01 AM`, the backup task is killed.
Retention Policy:
	The duration we keep the backup file for.
	for example a `retention policy` of 1 week means that each backup is kept for an entire week.
	unless specified otherwise.
Protection Group:
	This is the group of clients (hosts/VMs to be backed up) on which a specific set of Policies are applied to.
	This works with Backup Policies.
Backup Policies:
	These are the rules that include a backup window (to know when to schedule the backup or kill it once it exceeds the window), its retention policy (for how long this backup will be kept) and the backup type (full, incremental, cumulative).
	This works with Protection Groups.
On Demand Backup:
	This is a backup that is manually set, it doesn't follow the backup window, it's done by the user.
