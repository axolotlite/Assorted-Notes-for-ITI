given a host with a single cpu core.
if there are processes running in parallel needing the same CPU resource.
we can't allow one to wait til the other finish, and of course can't split the single core in half?

so, each process gets an equal amount of time of the cpu. 
so, one process does a number of cycles and it alternates with the second process till both finish.
it takes ms and the switch is fast and unnoticable for the user.


prioritizing processes gives them more time of the cpu share.

the default scheduler is called: CFS (completely fair schedule)

cpus are number from 0 index