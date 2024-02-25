## Business Continuity
it's the process / steps taken to ensure that the business / services remains available despite any disasters or problems.

This is done to retain your reputation which impacts your customers and acquiring newer ones.

Information availability measurement methods:
### mtbf (mean time between failures)
average between failures between specific duration
total uptime / number of failures = mtbf

mtbr (mean time to recover)
this is the average time between recovering from failure

rpo(recover point objective):
we have specific data which we specifically want to back up, we say every hour, so the next back up is within an hour.
so, the RPO is the data lost during the time between backups.
this means that the business can recover in a time frame that is within an hour.

rto(recovery time objective):
this is the time taken to recover data from a point of failure.
the more recoverable a system has, the better it is.

there are several techiniques for business continuity
backups
snapshots
double components

you do an analysis to find the best solutions and implement them.
then we can test this, for 

disaster recovery:
you have a sole site, this is a single point of failure. 
you need more, you need to, at the least replicate the critical functionalities of the original site in another location.

avoid single points of failure

fault tolerance: 
the ability of your infrastructure to remain operational even if it fails

shadow vm:
a backup VM that is launches in case the original provisioned vm fails, this shadow vm automatically replaced the original vm before another shadow vm is provisioned.

clustering:
using more than one server to do the same function, for example windows active directories, sql databases are clusters.
- active active: two nodes, up and running any incoming traffic is distributed between those two nodes. this will require a shared disk to allow them to do the same function on the same data.
- active passive: you have two servers, passing traffic only to one, while the other waits for the other to fail, this also uses a shared disk between them. they listen to failure through a heartbeat(message interval, once stopped the device is assumed down). if the passive fails, you'll need to manually intervene.

link aggregation / nic teaming:
if a server has more than one nic, we can make them all work as a single logical link, adding their speeds together.
the same logic applies to links.

testing environments:
you create an environment to test your changes before applying them to production.

vmware ha (high availability)
this is a technique that takes a number of hosts, where the vms of a failing host are transferred to another host on the vsphere cluster.
this prevents any downtime as long as there are enough resources in the cluster.

vmware fault tolerance:
this uses shadow vms to compensate the failure of any provisioned vm, replacing them once they fail.

these techniques work through network heartbeats, but since if a network error happens, the other hosts assume that it's failed, which may cause errors.
to solve this, they decided to use storage heart beat.
storage heartbeat: a host writes to its dedicated file, if it stops writing, the storage heart beat fails.
once both heartbeats stop, the host is presumed down and a replacement takes its place.

replicas: an exact copy of the original
you create a copy of an existing resource, like shadow vms.
there is also replica vms, creating a copy of a vm in case the other fails.
there are two types of replicas:
- point in time: this means we create a replica according to time, one each hour
- continues data protection: this replica is continuesly updated with the original data.

multi-site replication:
we replicate the data across more than one site, using both synchronous and asynchronous methods.

we can do replication between remote sites.

right splitter sends data into two places, the main disk and to another storage box, this appliance sends data to the journal log, recording the changes.
