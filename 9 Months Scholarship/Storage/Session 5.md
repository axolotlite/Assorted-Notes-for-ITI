## Backup and Recovery:
### Backup VS Replication:
the main difference between them is their RTO, backups take longer to restore them, unlike replication which is faster.

### Types of backups:
- Full Backups:
	takes a full copy of the data at a set interval.

| advantages                                      | disadvantages          |
| ----------------------------------------------- | ---------------------- |
| Faster Recovery(recovering from a single point) | uses a lot of storage  |
|    -                                             | large backup windows |
|     -                                            |      large load on backed up client                  |

- Incremental Backups:
	Takes the changes from each backup, for example the day after a full backup, it takes the changes of the next day on top of the previous day and this repeats everyday until the next full backup.
	it's also faster than cumulative backups.

| advantages            | disadvantages                              |
| --------------------- | ------------------------------------------ |
| fastest backup option | longest restore time(multiple restore points) (largest RTO)|
| least storage usage   |                                            |
| least load on backed up client                      |                                            |
- Cumulative Backups:
	Takes a full backup, then takes changes from the last full backup. the next day, the backup is also taken from the changes from the last full backup.

| advantages | disadvantages |
| ---------- | ------------- |
| medium back up speed       | medium restore time(multiple restore points)|
The difference between Incremental and Cumulative backups is that incremental compares between the **previous backup**(whether it's full or incremental) and current data, but Cumulative only compares between the **last full backup** and the current data.

#### We choose which backup method depending on:
- RTO
- Budget
#### Retention policy:
the time you keep backups in storage, after this time ends you delete the backup.
### Backup Methods:
- Agent Based:
	We push an agent (software program) onto the VM to discover it, then takes backup from a specific file, directory or data store inside the operating system. we restore the specific file or directories selected.
- Image Based:
	we take the whole VM as a backup, when restoring it we restore the entire VM as a new VM

### Recovery in place:
This recovers the VM on the backup target. so, if the main server fails, we start the new VM on the storage box responsible for the backup data storage the moment the main server fails, until we recover (move the data to) the main host, then reroute traffic to that host. This is done to reduce RTO as much as possible, regardless of the performance hit caused by the storage box.
### NDMP Based Backup
This takes a backup from NAS devices, the directories inside it, through the network NAS protocol.

### Business Terms
##### Capitol Expenses:
asses belonging to a corporation for example:
servers, deks, data center and all their content
##### Operation Expenses:
the money spent maintaining and operating the infrastructure and employees.

## Data Deduplication:
The process of finding similar chunks(pieces of data) in a dataset and creating a pointer to one of them after discarding the rest.
replaces similar data with pointers to one of them.

### file-level deduplication:
this deals with files, it looks for the same file across different places and then deletes redundancies and replaces them with a pointer to only one.
### sub-file level deduplication:
this deals with two files containing similar content, instead of being the same. this will look for similar data inside files and remove all except one, then replace all instances with a pointer to the remaining one.
it uses two methods:
- fixed length block: sets a length to check the data inside files
- variable length block: it looks for any data similar at different lengths to check.
### Deduplication in Source:
This reduces the network overhead of transferring data, but this requires a lot of CPU time and resources, which reduce the available resources for the running of apps.
### Target based Deduplication:
This does the the deduplication on the storage box, this offloads all the processing onto the storage box, but increases transfer overhead on the network, this is used a lot in production to allow maximum resource availability for hosts.

## Data Archiving:
the process of saving data on an external source from its origin, this helps us retain data for a very very long time. they use tape drives to store them in data archives.
unlike backups, the whole point of archiving is insurance, it's being kept as a history log which means it's RTO is slow, it may even takes days to recover from it.

| Data Backup                                   | Data Archive                               |
| --------------------------------------------- | ------------------------------------------ |
| secondary copy of working data                | a primary copy of the data for later study |
| used to recover operation and ensure business | used for data retrieval                    |
| retained in months                            | retained in decades                                           |

## Migration
The transfer of data from one place to another, this can apply from server level to host level.
we have VM migration, this moves data from a server to another, in order to do this, we'll need both servers to access a shared storage / data.
in case one of them fails, we can migrate(move) the data to the next vm.
### Types of VM Migration:
- hot migration:
	occurs to a running VM, it doesn't stop nor shutdown during migration
- cold migration:
	This occurs only when the VM is shutdown, we transfer it while shutdown.

### Storage Migration:
we move the VM disk from one data store into another, like from one LUN to another LUN. this may happen if we want to shutdown a storage box or if its almost full and requires us to migrate its LUNs into another box.
### Storage Based Migration:
we move storage disk from one storage box into another, this requires special software and hardware to allow both storage boxes to communicate through a SAN.

