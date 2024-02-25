[register](https://linuxhint.com/ansible_register_module/``)
they're used to store output of shell codes.
debug on the other hand, outputs to the host terminal
you can't register a value and output it in the same task
## example:
output kernel info 
```
---
  - name: test
    shell: uname -a
    register: hello_register
  - name: print test
    debug:
      msg: "{{hello_register.stdout_lines}}"
```

print several info related to the environment
```
---
  - name: Print env variable
    shell:  echo $PATH
    register: print_result
  - name: greet world
    shell: echo "Hello World!"
    register: hello_register
  - name: get ip address
    shell: ip addr | grep 'state UP' -A2 | tail -n1 | awk '{print $2}' | cut -f1  -d'/'
    register: ip_address
  - name: print message
    debug:
      msg:  "{{print_result.stdout_lines}}"
  - name: print hello
    debug:
      msg: "{{hello_register.stdout_lines}}"
  - name: ip address
    debug:
      msg: "ipv4 address: {{ip_address.stdout_lines}}"
```