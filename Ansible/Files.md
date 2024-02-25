Files are a directory and part of the hierarchy of ansible.
data that is meant to be copied and moved are placed in files.
```
role_X
      └── tasks
      │   └── main.yml
      └── files
            └── file_name.html
						 └── file_name.txt
						 └── file_name.data
```
and it can be copied from host to guest using copy module.
```
- name: copy index page
    copy:
      src:  file_name.html
      dest: /anywhere/on/guest/file_name.html
```