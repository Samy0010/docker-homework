

# Homework1

- Make server1 have an endpoint that recieves POST requests and then saves the data passed in the body of the request in a file
- Make another endpint that returns the data in the file as json. (The file can also be json, practice loading, reading, and parsing json files)
- Make server3 that is a web server and exposes a simplle HTML application that has a form where you can type an word and submit the form and the app sends that word to server1 to be added in the list
- Reaserch nginx container to make server3 with https conection in docker. (add ngnix contaner that acts as a reverse proxy ffor the webapp running on server3)
- Deploy ngix to add https connection to the webapp on server3 with self siigned certificate.
