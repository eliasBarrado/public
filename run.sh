sudo docker build -t public .
sudo docker run --name app_container -p 8080:8080 --rm -it public 
