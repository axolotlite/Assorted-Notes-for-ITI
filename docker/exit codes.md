#docker/flags 
0: correctly exited
if a container is gracefully killed it usually yields a 0 exit code

1: failure to exit safely
a non-graceful exit of a container can result in a 1 exit code.

however we can configure docker to restart container depending on the exit codes, if it's 1 it can restart container.
this only occurs if the container successfully starts for at least 10 seconds otherwise it won't attempt to resart it.
using the `--restart` flags
`=no`
`=on-failure`
`=always`
`=unless_stopped`
