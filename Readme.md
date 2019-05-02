### Backend
Dockerized Flask Backend api.  Serves data to Vue frontend.

### Frontend
Dockerized Vue Frontend app.  Makes api calls to Flask backend.

### Docker
Both apps maintain their own docker images, which requires both to be build and ran individually.  Commands must be run from their respective root directories `cafe-flask` and `cafe-vue`.

#### Docker Commands
Build Vue docker image => `$ docker build cafe-vue .`
Build Flask docker image => `$ docker build cafe-flask .`

Run Vue Docker container => `$ docker run -d -p 5000:5000 cafe-flask `
Run Flask docker container => `$ docker run -d -p 8080:8080 cafe-vue `