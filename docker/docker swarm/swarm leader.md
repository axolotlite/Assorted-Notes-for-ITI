RAFT Algo: uses random timers to initiate requests, the first one to finish the timers requests permission to be the leader, if a leader is elected it sends notification to other managers to tell it that it is assuming the role of the leader.
if it fails a new election starts until a leader is found.

all the manager nodes have synced data of all the worker nodes.
every decision taken by a manager node must be agreed upon by the majority of the manager nodes.

so 2 agree to add but the 3rd fails to reply, meaning that the addition is successful.
Qorum: the agreement of a mojority of managers
the formula $Qorum\ of\ N = floor(\frac{N}{2}) + 1$ for a successful command running.

it is recommended to pick an odd number of managers in case a network segmentation occurs, since an odd number of nodes increases a chance of a successful Qorum decision taking after seperation of networks.

## On Qorum failure
the swarm won't be able to perform anymore management tasks, but the current swarm will work as it is, with all its existing services.
but if a node fails, they won't automatically start back up.
the only way to recover the Qorum is by bringing back the clusters online.

if we've only a single node working without the other two leaders, then we must force create a new cluster.
`docker swarm init --force-new-cluster`