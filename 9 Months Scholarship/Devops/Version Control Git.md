
What is meant by a repository?
definition changes depending on the field, but in the computer field it means a placeholder for data alongside its metadata, usually for the source code.

Repositories are handled as if they were linux directories, and are language agnostic (are not limited to one programming language).

### Version Control Systems
They are used to create and maintain repositories that contains the source code saved in different forms taken from different stages during development.
#### Distributed Version Control Systems:
allows for different users to push their code and for the reviewers to asynchronously merge their code to the repositories.
This allows for the reviewer to ensure the committed code is both up to standards and doesn't break the existing code base, and in case a problem occurs, they can always undo it and return to an older version of the code.

Git is platform agnostic (works on any platform, like: github, gitlab, bitbucket, etc...)

#### Git Configurations
git has several levels for its configurations:
- System: for specific users on the machine
- Global: the default settings for all users on the machine
- Local: for a specific git repo on the machine
These configurations include the user, email, info, etc...

Whats the difference between git reset and revert?
they both return you to a previous commit, but reset deletes the commits after it, unlike revert which just returns you back to the commit.
