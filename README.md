#### First, install Docker

#### To build the Docker image
- `docker build -t myapplication:v1.0.0 .`

#### To run the image
- `docker run -d -p 80:8080 myapplication:v1.0.0`

#### To see the running containers
- run `docker ps` to see the name of the container

#### To see the app working
- navigate to a new browser tab and type in the following in the address bar and press Enter `http://localhost:80/info`

#### To see the logs from the running container
- `docker logs -f <containerName>`

#### To stop the running container
- `docker stop <containerName>`

#### To start the container back again
- `docker start <containerName>`
