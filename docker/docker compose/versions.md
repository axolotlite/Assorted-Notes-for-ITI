version: 1
you can't deploy networks on any network other than the default bridge.
then uses links to allow communication between containers
dependencies between containers and defining which container starts first

version: 2
change in format:
you encapsulate all containers in a `services` section
creates a dedicated bridge network between containers in the compose file, to allow intercommunications.
introduces `depends_on` property: which allows startup order between containers.

version: 3
similar in structure to version 2.
supports docker swarm