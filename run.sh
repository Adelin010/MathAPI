#/bin/bash
sudo docker build --tag "adelin" .
sudo docker run -it --rm -p 8000:8000 adelin
sudo docker ps -a
