## [What is Ansible?](https://www.redhat.com/en/technologies/management/ansible/what-is-ansible)
it's an open source IT tool made to automate, provision, configure and deploy applications, using only SSH.
it runs on "playbooks"
you can run a playbook. but, you will need the SSH key for the host
`ansible-playbook playbook_name.yml --private-key=key_location`
you won't need to specify the key location if you added the key to your keychain.

## anatomy of an ansible playbook:
ansible uses directory based hierarchy.
```
Parent_folder
│
├── main_playbook.yml
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
