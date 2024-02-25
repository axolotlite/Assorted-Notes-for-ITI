to create our first docker compose app
we can do it using docker run first:

`docker run -d --name=redis redis`

`docker run -d --name=db postgres`
we link both the voting app front end and redis through the network.
`docker run -d --name=vote -p 5000:80 --link redis:redist voting-app`
now we link the result app to the database
`docker run -d --name=result -p 5001:80 --link db:db result-app`

`docker run -d --name=worker --link redis:redis worker`

we can build the images inside the docker-compose file.
we can do this is a dockercompose file:
```yaml
version: '3.8'
services:
	vote:
		image: voting-app
		# if we want to build it, we can do this
		build: ./vote
		ports:
			- "81:80"
		networks:
			- front-end
			- back-end
	redis:
		image: redis
		networks:
			- back-end
	db:
		image: postgres:9.4
		networks:
			- back-end
	worker:
		image: worker
		networks:
			- appnet
	result:
		image: result
		ports:
			- "82:80"
		networks:
			- front-end
			- back-end
networks:
	front-end:
	back-end:
		driver: bridge
```
