devops allows faster development of application through combining the dev and sec team.
however security is not encorporated.
but devsecops is incorporating security in the devops cycle.

they both use automatited building, continuis integration, etc...

the devops process:
developer writing code -> push to repo -> CI/CD server pulls code -> package the code -> push artifacts -> deploy artifacts on servers using k8s or docker -> monitor service

in devsecops security is added at the end of the cycle.

normally, the entire pipeline is rerun to fix a single risk, so in order to avoid this devsecops hopoes to add security to the pipeline at an early stage.

by adding automated security we can 