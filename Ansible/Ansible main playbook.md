# Main Playbook
it references the roles, and calls them to execute their functionalities, it also has other capabilities.
`main_playbook` contains the "hosts" that the "roles" target.

```
---
  - name: (whatever you want)
    hosts: (a yaml list of ips or a filename)
    user: (username on the target machine)
    become: (bool, checks if you want to become another user)
    become_method: (how it becomes root, ex: sudo)
    become_user: (who you want to sudo into)
    roles: (a yaml list of roles that exist in /roles)
```

# example main playbooks:
my_first_playbook
```
---
- name: Exercise one
  hosts: localhost
  roles:
    - print
    - kernel_info
```
this two reference an inventory file containing a group called "all"
they both elevate privilidge to root, then execute their roles.
remote-control-using-ansible
```
---
  - name: setting up a web server
    hosts: all
    user: ubuntu
    become: true
    become_method: sudo
    become_user: root
    roles:
      - setup
```
ubuntu_apache_playbook
```
---
  - name: apache hello world
    hosts: all
    user: ubuntu
    become: true
    become_method: sudo
    become_user: root
    roles:
      - update
      - apache
```