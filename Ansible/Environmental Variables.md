[How does Ansible handle environmental variables?](https://www.educba.com/ansible-environment-variables/)
There are syntax, each syntax has a different way to set, remove and retrieve the environment variables on the remote host.

`env` is a default ansible module used to deal with enviornmantal variables.
`lookup` method searches local environmental variables and it can be replaced by `ansible_env.HOME` if we want data from ssh host
```
- name: Ansible playbook to retrieve environment variables on linux servers.
hosts: linuxservers
tasks:
- debug:
msg: "{{ lookup('env','HOME') }}"
```

we can set environment variables on the ssh host using
```
environment:
	-	VARAIBLE_NAME: "VARIABLE VALUE"
	-	OTHER_VARIABLE: "{{ lookup('env', 'LOCAL_VARIABLE')}}"
```