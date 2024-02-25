we can set DTP(Dynamic trunking protocol) to allow the switch to detect whether the port connection mode should be set as access or trunk.
we can check the state of dtp through
`show dtp`
we can manually enable dynamic through selecting the port
then
`switchpirt mode dynamic auto/desirable`
auto: will depend on the other side if both auto then it'll pick trunking
desirable: desires trunking.
we can disable negotiation through:
`switchport nonegotiate`

from the terminal configuration we pick the ports and configure them all as trunks.
this will cause looping which will block one of the ports.
to fix this, we'll  need to enable the spanning tree.
`show spanning-tree`
we can modify the spanning tree modes through
`spanning-tree mode pvst/rapid-pvst`
now we can create a vlan and assign each vlan their own spanning tree mode.
we'll have to create these vlans on each switch after changing the spanning-tree mode.

this will prevent blocking within switches but the blocking will move onto the vlan, blocking connection between them.
then we can configure the vlan position in the spanning tree
`spanning-tree vlan n priority/root`
if we make it a root then
`spanning-tree vlan n root primary/secondary`
the primary root is the current working root, if it fails or shuts down, the secondary will take its place.
we can specify more than one secondary root.

we'll configure this in each switch, like before.


then we can block the bpdus request from non-switch ports after selecting them, by using:
`spanning-tree bpduguard enable`
this won't accept spanning-tree data from these ports.

now, we can change the spanning-tree mode to send packets without trying to find data from the other switches, this assumes all priorities and links were already mapped, so it'll just forward packets directly.
this can be achieved through:
`spanning-tree portfast`

first we select the ports we want:
`int f 0/1-4`
then we group them using `channel-group` then select a number from 1 to 6 then specify the mode
`channel-group {1-6} active/auto/desired
in this case
`channel-group 1 active`
then we can take this ether channel and use it for trunking
`int port-channel n`
then make it trunk
`switchport mode trunk`
then we do the same thing on the other switch, since the ether channel will require configuration on both sides.

we can enable vtp(vlan trunking protocol) to allow transfer of vlan configs accross routers.
first we create a vtp domain:
`vtp domain name.domain`
then set a password
`vtp password pass`

any change inside the vlan will increment the config revision in vtp status.

now to configure the other switches to use the vtp of another. by changing the mode from server into client.
`vtp mode client`
after which we create the same domain on the client
`vtp domain name.domain`
with the same password
`vtp password pass`
then we must enable trunking on the port.
`switchport mode trunk`

after finishing our configuration we change vtp mode
`vtp mode transparent`
so that any changes we do remain on this specific switch.
anything done in transparent mode won't be transported through vtp.
upon returning to client mode, the transparent configs are removed.
