[why debug your playbooks?](https://www.educba.com/ansible-debug/)
when we create and run playbooks, it’s very common that we run into an error due to some issues with our playbook. This can be a syntax error, a logical error or some mandatory parameter is missing.

Debug is an ansible module. it prints to the host data such as ansible variables, output masseges and has a verbosity option for further debugging capabilities.

you can place variables directly beneath it.
Examples:
if no specific value is given debug outputs "Hello World!"
```
---
	name: default debug output task
	tasks:
		name: outputs hello world
		debug:
```
it can print variables defined in the playbook or its corresponding vars folder
```
---
	-	name: print the variables task
		vars:
			some_var: data in var
	-	name: this will return the value of some_var
    debug:
			var:	some_var
```
it can also print a "fact" from the remote host
I can also customize the messages using "msg"
```
- name: echoes hello world from external vars
  debug: 
    msg: "hello my name is {{ ansible_hostname }} "
```
register task output and `debug msg` it to host
you can't register a value and output it in the same task
```
  - name: returns hello world to host
    shell: echo "hello world!"
    register: output_echo
  - name: print output from a register
    debug: 
      msg: {{ output_echo.stdout_lines }}
```
you can change verbosity level by running the following playbook using `ansible-playbook playbook-name.yml -v`
```
  - name: echoes a string
    shell: echo " some text "
    register: output_echo
  - name: print output from a register
    debug: 
      var: output_echo
      verbosity: 1
```