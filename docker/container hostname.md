creating a named container doesn't change the hostname of the container, if you call the `hostname` command you'll realized that container uses the short version of the container id.

since applications use the name of the container, this is disadvantagous, so we set the hostname of the container to be some specific we can set it during starttime