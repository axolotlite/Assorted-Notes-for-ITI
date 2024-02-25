you can restart prometheus configs using

`kill -HUP $(pgrep prometheus)`

you can get active memory metrics using:
`(node_memory_CommitLimit_bytes - node_memory_Active_bytes ) / 1024 / 1024 / 100`