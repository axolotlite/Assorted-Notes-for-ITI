## [What are roles?](https://docs.ansible.com/ansible/latest/user_guide/playbooks_reuse_roles.html)
Roles let you automatically load related vars, files, tasks, handlers, and other Ansible artifacts based on a known file structure
### the roles directory exists within the main directory of the project
ansible looks for the **main.yml** file inside each role directory.
```
└── roles
       ├── role_1
       │   └── tasks
       │   │   └── main.yml
       │   └── files
       │       └── data
       └── role_2
              └── tasks
                  └── main.yml
```
each role can contain its relevant data
```
role_X
      └── tasks
      │   └── main.yml
      └── files
            └── data.html
						 └── data.txt
						 └── data.data
```
You can define variables in an external variables file.
```
role_X
      └── tasks
      │   └── main.yml
      └── vars
            └── main.yml
```
## Examples of roles:
Basic hello world role
```
---
  - name: echoes hello world 
    shell: echo "Hello, World!"
```
gets kernel name.
```
---
  - name: test
    shell: uname -a
```
updates an apt based distro
```
---
  - name: update repos, or apt-get update
    become: true
    become_method: sudo
    apt:
      update_cache: yes
  - name: remove unwanted dependencies
    become: true
    become_method: sudo
    apt:
      autoremove: yes
```
install apache and moves file from local to the server
role hierarchy:
```
apache
      └── tasks
          └── main.yml
          └── index.html
```
corresponding code
```
---
  - name: install apache
    become: true
    become_method: sudo
    apt:
      name: apache2
      state: latest
      update_cache: yes
  - name: copy index page
    copy:
      src:  index.html
      dest: /var/www/html/index.html
      backup: yes
```
alternative role hierarchy:
```
apache
      └── tasks
          └── main.yml
		  └── files
          └── index.html
```
alternative code:
```
    copy:
      src:  files/index.html
      dest: /var/www/html/index.html
      backup: yes
```
update packages,  copy files, then install and run a nodejs server.
```
---
  - name: update packages
    become: yes
    apt:
      update_cache: yes
  - name: upgrade packages
    become: yes
    apt:
      upgrade: yes
  - name: install nodejs
    become: yes
    apt:
      name: nodejs
      state: latest
  - name: install npm
    become: yes
    apt:
      name: npm
      state: latest
  - name: install pm2
    become: yes
    shell: npm install pm2 -g
  - name: create web directory at home
    file:
      path: ~/web
      state: directory
  - name: copy index
    copy:
      src: files/index.js
      dest: ~/web/index.js
  - name: start server
    shell: pm2 start ~/web/index.js -f
```