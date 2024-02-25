[what is ansible inventory?](https://docs.ansible.com/ansible/2.3/intro_inventory.html)
its a file containing a list of hosts, ips or domains ansible targets to.
to invoke it you call 
`ansible-playbook -i /location/of/inventory_file`

an example of an inventory file:
```
mail.example.com

[webservers]
foo.example.com
bar.example.com

[dbservers]
one.example.com
two.example.com
three.example.com
```