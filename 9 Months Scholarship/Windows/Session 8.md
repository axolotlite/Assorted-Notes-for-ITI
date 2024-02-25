
### Storage Pooling
we collect several hard drives together and create a pool from which we can create virtual disks / drives.

### Organizational Unit
each group of employees will be assigned to an OU.
to control who can access which devices and what data.
this is part of `administrative control` 
#### Group Policy
a policy can be configured to users or groups.
and the policies are applied on login.
##### Local Group Policy
- user specific configurations
- computer specific configurations
an example of policies:
password complexity: this is applied on the level of a computer device.

we can check our local policies by searching for `edit group policy` in the taskbar
you can modify the password policies through
windows settings -> security settings -> account policies -> password policies
you can hide the control panel through
user configurations -> administration -> control panal -> prohibit access to control panel and pc settings

you can check each users configurations or settings through the `All Settings` directory in root directories such as `User Configuration` and 

## Setting up:
we can configure new Organizational Units through the Active directory users and computers.
right clicking on our domain (iti.local) and selecting `new` to create a new Organizational Unit
### Group Policy Management
Inside our forest we can find `Group Policy Objects` we'll find all our OUs here with their policies.
from here we can configure our policies and on which domain and objects they fall.
by editing it, we can find all the relevant policies within the group policy management.
it's similar to what we can find locally.

#### Filteration
in All Settings by right clicking you can filter policies by selection Filter ON then Filter Options.
alternatively, search google for the desired policies and their effects.

### Applying Group Policies
in Group Policy manager we can specify which policies apply to which groups by right clicking the group and selecting `Link an Existing GPO`
we can manually update the policy from the CMD through `gpupdate /force` this forces the updates.

## VPN
we open a service within the firewall called VPN Connection, it requires a username and a password or a token for the user/client to pass through the firewall.
this creates an encrypted tunnel between the client device and the network behind the firewall, this enables the device to virtually become a device inside that network.
meaning that the DHCP server will give it an address and the gateway will forward through this tunnel.
The devices within the network will deal with the machine as if it is within the same network, but in reality the traffic is securely routed through the internet.

There is another form between different corporate networks that is called site-to-site VPN.

