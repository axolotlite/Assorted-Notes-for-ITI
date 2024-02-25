#git/directories
github [repo](https://github.com/thoughtworks/talisman)
This tool can hook your repo and ensures that no potential secrets of sensitive info leaves the developers workstation.

it can both a pre-push and pre-commit hook

it can even detect suspicious changes to sshkeys, auth tokens or priv keys by scanning the repo.

it can be globally installed or confined to a single project

single project installation:
```sh
# Download the talisman installer script
curl https://thoughtworks.github.io/talisman/install.sh > ~/install-talisman.sh
chmod +x ~/install-talisman.sh

# Install to a single project
cd my-git-project
# as a pre-push hook
~/install-talisman.sh
# or as a pre-commit hook
~/install-talisman.sh pre-commit
```
this installs it as a pre-push hook, it runs before a push command in git.
you can view all hooks in `.git/hooks`

ofcourse, you can ignore specific files through a `.talismanrc` this will cause talisman to skip the file during its pre-push scan.
