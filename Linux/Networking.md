The linux host has its own routing tables and arp tables.
each within its own namespace, we can apply the same namespace logic

we can create a new network namespace by using the following command.
`ip netns add ns_name`

we can list the network namespaces using
`ip netns`

we can list all the interfaces using
`ip link`

we do list all interfaces in a namespace using
`ip netns exec ns_name ip link`
`ip -n ns_name ip link`

we can inspect the namespace arp and route tables using the same command
`up -n ns_name route`
`up -n ns_name arp`

we can connect two namespaces using
`ip link add ns_link_name_first type veth peer name ns_link_name_second`
then we connect both links to their respective namespace
`ip link set ns_link_name_first netns ns_first`
`ip link set ns_link_name_second netns ns_second`
to delete both links we can use, since both of them are a pair, they're both deleted
`ip -n ns_first del ns_link_name_first`

we can create a linux bridge using:
`ip link add v_bridge_name type bridge`
then we can connect the name spaces to this bridge network through:
`ip link add veth_first type veth peer name veth_first_br`
then the second namespace
`ip link add veth_second type veth peer name veth_second_br`
then
`ip link set veth_first netns ns_first`
`ip link set veth_second netns ns_second`
then define its master using:
`ip link set veth_first_br master v_bridge_name`
`ip link set veth_second_br master v_bridge_name`

then assign the ip address for gateway:
`ip -n ns_first addr add 192.168.15.1 dev veth_first`
`ip -n ns_second addr add 192.168.15.2 dev veth_second`

then we set them up:
`ip -n ns_first link set veth_first up`
`ip -n ns_second link set veth_second up`

finally we add a range to the bridge network:
`ip add add 192.168.15.5/24 dev v_bridge_name`
