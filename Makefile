run:
	docker build -t myimage .
	docker run -d --name mycontainer -p 80:80 myimage
	docker ps

stop:
	docker stop mycontainer
	docker rm mycontainer
	docker rmi myimage

