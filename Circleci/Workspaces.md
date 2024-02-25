[what is circleci workspace?](https://circleci.com/docs/workspaces)
the palce where all the magic happens, it contains the job, the cache and can output to artifacts.

you can persist data in a job using 
```
	- persist_to_workspace:
		  root: ~/
		  paths:
			- filename_at_root.txt
			- other_filename.txt
			-	another_filename_same_directory.txt
```
then call it in another job using
```
		steps:
      - attach_workspace:
          at: ~/
      - run: cat ~/filename_at_root.txt
```