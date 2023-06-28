to run this project:

# type in CLI (in project folder)
    docker-compose up --build
    (if error)
    docker start mysql
    then reapet 
    docker-compose up --build

# URLS
add student
http://localhost:5000/test
get students
http://localhost:5000/students

# result
[
  {
    "age": 20, 
    "id": 1, 
    "name": "John Doe"
  }, 
  {
    "age": 20, 
    "id": 2, 
    "name": "John Doe"
  }, 
  {
    "age": 20, 
    "id": 3, 
    "name": "John Doe"
  }
]

# deploy to dockerhub
docker build -t narnavg/back:latest .
docker push narnavg/back:latest