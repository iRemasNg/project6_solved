docker stop brevets-app
docker rm brevets-app
docker build -t brevets:latest .
docker run -d --name brevets-app -p 5000:5000 brevets
