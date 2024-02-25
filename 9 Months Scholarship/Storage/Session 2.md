## RAID (Redundant Array of Independent Disks):
it can be implemented either in hardware (raid box in the disk controller) or in software (os module)
There are 3 types of raid:
- striping(RAID-0): we distribute the data across disks, each disk has a strip(piece) of the data. this increases read and write speeds with risk of data loss if any of the striped disks are damaged.
- mirroring(RAID-1): you write data to several disks, mirroring(duplicating) the data across several disks. this adds redundancy.
- parity(RAID-5): uses xor-ing to save the results on a separate disk, if corruption occurs on the data it'll retrieve it from the xor'd disk. if a single disk fails, it can be recovered. in a three disk configuration, if any 2 disks fail data is lost.
both RAID 1 and 0 require a minimum of 2 disks while RAID-5 requires at minimum of 2 disks, storage and for xor of the data.

we can combine raid levels to mix them
### RAID-10 (striping and mirroring):
this stripes two disks and duplicates them, providing redundancy and a performance speed with a minimum number of 4 disks.

### RAID-3 (Striping with dedicated parity):
we stripe two disks and then xor them for a third disk, in case any of the stripes are damaged.
#### Write penalty:
Although this increases the read speed but takes a massive cost to writing.
since it reads the previous data in both disks and parity before writing the new data in each disk and their XOR result in the new disk. 
#### Wasted resources
This wastes a third of the storage resource, leaving an entire disk dedicated for parity.

### RAID-5 (Striping with random parity):
the result of the XORing is distributed between all the disks present within the array.
this is faster raid-3 since reversing the operation is much more processing intensive than creating the parity data, this randomization increases the restoration speed by having parity pieces saved in other disks, meaning each disk may have 67% data and 33% parity, increasing the recovery speed of the 67% while ignoring the much shorter time to recreate the damaged 33% parity.

### RAID-6 (striping with double parity):
minimum of 4 disks, with double parity for each equivalent piece of data.
it also allows for 2 disk failures unlike previous method.

### RAID Application
We configure raid on a disk array, through 'Raid set' we place a group of disks in an array into a set, to apply a specific raid technique on it. 
for example:
set A having (Raid-5 5+1): this means we'll apply 1 part parity to each 5 parts of data. This saves a lot of disk space for data.
the most common used configuration is (7+1).

#### Hot spare:
when a disk fails, we've a prepared set of disks ready to replace it. this applies to each array, these hot spare disks are usually empty to replaceany failing disk in the RAID.

## Block based storage
This is the distribution of block storage (unpartitioned disks) for hosts to use and partition.
they have 2 components:
- Controllers: They define the cost of the storage box, it has several components.
- Disk: they basically follow the controller for reading and writing, it's a dummy component

### Controller:
contains a front-end filled with ports to connect with hosts, it's connected with the HPA controller, it's responsible for encapsulating /decapsulating the data received before sending it to the cache.

the most important and costly part of the controller is the cache:
it determines the speed of the storage box, as the increase in cache size and intelligence, it offloads parts of the disk work onto itself nullifying the slow speed of disks by acting as a faster middle man.

#### cache hit: 
the requested data exists in the cache, it returns it to the requester.
this is of course faster than a cache miss, as the data already exists within the cache.

#### cache miss:
the requested data doesn't exist in the cache, search for it inside the disks before returning it.
then it will consider -according to an algorithm- saving a copy of it in cache, so once another host requests it, it'll cause a cache hit.

#### Write through:
data is written into the cache, then it's written on the disk, the disk then sends the acknowledgement to the host confirming the write.

#### Write back:
data is written onto the cache, then it sends an acknowledgement to the host that its data is written, the cache then collects a group of operations (similar writes) before writing it to the disk at once.
this could cause data loss if the cache is damaged or suffers a power loss, the host has already been told that a write operation happened although the cache didn't actually commit.

this was solved through:
##### cache volting:
we add a battery to the cache, keeping it powered even during unexpected power failures. allowing it to resume operations once power returns.
however if a cache fails, the solution will be:
##### cache mirroring:
add another cache that has a copy of the running cache.

### Caching algorithms:
the goal of these algorithms is maximizing cache hits while minimizing misses.
these algorithms may worth together, so: a cache may use several algorithms together.
#### pre-fetch algorithm:
it predicts the data that will be requested and retrieves before hand, so once it's requested it returns it.
so for example:
'abc' is requested, the algorithm predicts that the closest block to the requested data will be needed.
so, it retrieves 'abcd' into the cache, returning 'abc' for the first request and while keeping 'd' in case it's requested later.

#### LRU (least recently used)
it removes any unrequested data according to a time limit, if a piece of data is not requested during that time, it's removed from the cache.

#### MRU(most recently used)
keep the most used data, it acts like queue, the most recent piece of data remains in the cache.

## Storage provisioning:
we assign chunks from the storage to give it to a host, this is called LUN(Logical Unit)
there are two types of storage:
thin: this is a new way of provisioning, we fill the provisioned space as it's being used, this allows for over provisioning.
thick: this is the traditional way of provisioning, we reserve the entire provisioned space for use. this writes 0's to the unused spaces.

LUN is mapped as a block file, meaning it's up to the host to install a filesystem and partition it as if it was a normal physical volume.

in case the LUNs thin provisions actual data threshold reach the physical threshold data will start being deleted. to avoid this, a threshold is set (85% of the actual physical storage) if it's surpassed an alert is issued to the administrator to either move the upcoming provisions onto another storage box or if available storage exists, add it to the existing LUN Pool.

### Storage box
a storage box containing disks can turn them into one or more LUN Pools, they allow us to be scale them with ease.
#### Scaling Up:
increasing capabilities of an existing system, for example increases the number of disk arrays within a storage box.
#### Scaling Out:
increasing the number of systems, for example buying another storage box.

however any added disks don't automatically join the pool, we will have to add them to the pool.
### LUN Masking / Mapping:
This determines which host can see which LUNs, it allows us to control who has access to which LUN pool.
this prevents unauthorized access to LUNS.
### Storage tiering:
we can create several pools inside a storage box, each pool may contain hard drives, ssds or mixed.
Then we can specify the tiers inside the pool, to allow the customers to select whichever tier within the pool that suits their needs.
#### LUN tiering:
moves an entire LUN pool into another heigher tier pool because this LUN has a lot of read and write, this moves it from normal performance to higher performance tier.
this is a problem if a single LUN has 20 Vms, and the increased read and write belongs to 3 VMs which means they all move because of a few
#### sub LUN Tiering (fast VP)
This method locates the part of the LUN responsible for high IO, then moves it into the higher tier to increase its performance.

### Cache Tiering:
we can increase the size of the cache, by taking a disk from the storage box, for example an SSD and use it as a virtual cache.
it's the same principle as swap, we move data from the actual cache into the SSD and anything that isn't used there, remains in the disk drives.

### Storage > Pool > LUN
one or more pools can be created inside a storage box
one or more LUN can be created inside a Pool
LUN Tiering allows us to select which pools within a storage to be used.

## SAN
it's created by a storage box, switches and cables (mostly fiber).
the speed of a network is determined by the
- server NIC
- switch bandwidth
- cables
- receiver
the traffic is limited by the speed of the network, like a tunnel or a bottleneck.

The server -> device (hub, SAN switch, director) -> Storage box
If it's a hub: it floods the network, so it's never used
San Switch, San Director: these are similar, the only difference is that a director is more scalable, you can add ports to it.
for a server to be able to connect to a SAN switch or director, it'll need an HBA, which en/decapsulates SCSI commands(read/write operations) for transferal to the SAN.
The SAN will also have it's own HBA to do the same.

In any production environment, you will have two SAN switches at minimum, the cables can either be copper or fiber. 
There are several protocols used with SAN:
### FC(fiber channel) Layers:
despite what the name says, the cables can be either copper or fiber glass.
its speed is commonly run as a multiple of 2: 2,4,8,16... 128 Gb/s etc...

| layers | function                                                                                           | features                                                                                                                                |
| ------ | -------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| fc-4   | mapping                                                                                            | this is the equivalent to the application layer, it is responsible for scsi commands                                                    |
| fc-3   | common services                                                                                    | this technology is not yet mature, so they've decided to make a buffer layer for later use and configuration as of now, it does nothing |
| fc-2   | we use frames in this layer, like in the osi model and uses something called WWN(world wide Name ) |                                                                                                                                         |
| fc-1   | encode/decode                                                                                      | the equivalent to the data link layer                                                                                                   |
| fc-0   | physical layer                                                                                     | uses either fiber or special copper cables                                                                                                                                        |

### WWN(world wide name): the mac-address equivalent
it's unique, so it's used in SAN, it's also used in zoning.
we use it to double check devices since it's non-modifiable.
again, it's mac adress for storage, both the LUNs and ports have their own WWN.
LUNs receive WWN like drives get UUIDs on partitioning.
### Fabric Login Types:
any node connected to a SAN environment does something called flogi, it identifies itself by broadcasting its WNN.

Block level storage:
- Fiber Channel Protocol
	Advantages:
	- we use FC (fiber channel) layers because it's lossless, basically no packet drops.
	- also FC protocol avoids network congestion because it isn't in it's own network, the SAN network.
	Disadvantage:
	- Extra Costs: buying fiber is expensive
	- Complex environment: we now have another set of switches and another network to manage
- Fiber Channel Over Ethernet Protocol
- IP-SAN
	- ISCSI Protocol
	- FCIP (this is also a protocol)

## Zoning
all connected devices in a SAN cannot connect to anything, you have to manually set it up.
this is done through zoning, you place all devices in a zone so that they could connect.
### WWN Zoning:
we create the zone between the servers (called initiators) and the storage box (called target) WWNs.

### Port Zoning:
we have a switch with ports, some ports are connected to servers, others are connected to storage boxes. this type of zoning selects a port for example port 1 and port 8 and tells the switch that they can access each other.
if the HBA breaks, this method won't require any reconfiguration as the ports are already mapped. however you'll have to deal with broken cables and moving / replacing them.

configuring a SAN:
1) Zoning: to give the server access to the storage box (SAN Switch)
2) add host to the storage box (Storage Box)
3) create the LUN (Storage Box)
4) LUN Masking (Storage Box)
5) Discover LUN & format a file system into it (Host)

## Virtual Layer atop the storage boxes
we have a layer atop the storage boxes that allow us to control all the available virtual boxes through abstracting them.
this means only the admin will be able to know the sources of the LUN drives while the host cannot know which storage box is responsible.

### VSANs
we can distribute SAN into several VSANs, similar to VLANs in normal networking.
this means only devices in a specific VSAN are capable of contacting eachother, this is an additional security layer added on top of zoning which is the main security layer.
and each device in a VSAN has its own tag, which allows it to communicate with other devices tagged similarly.

we can use trunking to allow several VSANs through switches according to their tags.

