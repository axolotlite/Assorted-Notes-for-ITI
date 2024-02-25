## [why does ansible use variables?](https://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html)
Ansible uses variables to manage differences between systems. With Ansible, you can execute tasks and playbooks on multiple different systems with a single command. 

Variables can be defined both locally(inside the playbook or role) and externally(inside a file relative to the hierarchy).
### example of local definition of a variable
```
vars:
	var_name: some text
```
### examples of externally defined variables
```
role_X
      └── tasks
      │   └── main.yml
      └── vars
            └── main.yml
```
the main.yml from `vars`:
```
	test_var: Hello World!
```
which can be referenced inside `role_X` by just calling `{{ test_var }}`
the content of `role_X` main.yml:
```
---
  - name: echoes hello world 
    vars:
      test_var: "Hello, World!"
    shell: echo {{vars.test_var}}

  - name: echoes hello world from external vars
    shell: echo {{ test_var }}
```