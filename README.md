# foodhub
Website created using python's flask tailwindcss and mongoDb

# Preview


# Initialize
To host website in your server pull docker file from dockerhub repo:
<pre>https://hub.docker.com/repository/docker/jaimit2002/jenkinsfoodapp/general</pre>

# Running Docker File
After pulling the docker file use this command to use the docker image
(You will need admin privilege)
<pre>docker run -d -p 8080:8080 5000:5000 --name <chose a name> jaimit2002/jenkinsfoodapp:v1</pre>

# Steps to Deploy Website
1. go to localhost:8080
2. Enter UserName: Jason
3. Enter Password: kali
4. Go to Python Integrated CI/CD Pipeline
5. Click Build to deploy website
6. To see the website type: localhost:5000
