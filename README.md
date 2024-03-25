

# Homework1

- Make server1 have an endpoint that recieves POST requests and then saves the data passed in the body of the request in a file. The file should be inside a container but use a volumeMount to store it on the host as well.
- Make another endpoint that returns the data in the file as json. (The file can also be json, practice loading, reading, and parsing json files)
- Make server3 that is a web server and exposes a simplle HTML application that has a form where you can type an word and submit the form and the app sends that word to server1 to be added in the list (Flask web app!!) 
- Reaserch nginx container to make server3 with https conection in docker. (add ngnix contaner that acts as a reverse proxy ffor the webapp running on server3) (https://www.nginx.com/)
  - OR Reaaserch Traefiik (https://traefik.io/traefik/)
  - https://www.kubecost.com/kubernetes-devops-tools/traefik-vs-nginx/
  - https://medium.com/@miladev95/nginx-with-self-signed-certificate-on-docker-a514bb1a4061
- Deploy ngix to add https connection to the webapp on server3 with self siigned certificate.
- Commit the changes to giithub with a meaningfull commit name! )
```
git add .
git commit -m "ceva"
git push origin
```
In folderul de docker unde vezi folderul .git
