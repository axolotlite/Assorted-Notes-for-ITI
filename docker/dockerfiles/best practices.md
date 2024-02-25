do not build images combining multiple applications

build modular images, solving only 1 problem. to avoid lib and dep issues.

do not store data or states inside containers, because containers are ephemerial in nature.
only stare data in external volumes.

keep image size as small as possible. to allow faster pulling and more efficient dealing.
- use official minimal packages
- only install necesary pacakges
- maintain different images for different environments
	- dev env
	- prod env
- use mult stage builds to create lean images
- avoid unwanted files using dockerignore