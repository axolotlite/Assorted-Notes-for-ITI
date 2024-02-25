[What are ansible modules](https://docs.ansible.com/ansible/latest/user_guide/modules_intro.html)
some modules i've come across:
```
apt:
      update_cache: yes 
```
```
apt:
      upgrade: yes
```
```
apt:
      name: [package1,package2...packagename]
      state: latest
```

there is also `unarchive`
```
  - name: unarchive files to remote host
    unarchive:
      src: local_archive.tar.gz
      dest: ~/remote_location/
      remote_src: no
```
```
  - name: unarchive files from remote host
    unarchive:
      src: remote_archive.tar.gz
      dest: ~/remote_location/
      remote_src: yes
```