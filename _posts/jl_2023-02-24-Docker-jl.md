### Docker 

1. under the program folder, create a Dockerfile, it will copy program code and create a image

'''
FROM node:19
# Create app directory
WORKDIR /app
COPY package.json ./

RUN npm install --force
# If you are building your code for production
# RUN npm ci --only=production

# Bundle app source
COPY public .
COPY src .
COPY next.config.js ./
COPY  README.md ./


EXPOSE 3000
CMD [ "npm","run","dev" ]

'''

2. Build image
'''
docker build -t getting-app .
'''

3. start program and show  program website
'''
docker run -dp 3000:3000 getting-app
curl http://qzdocker:3000/

docker run -p 127.0.0.1:8080:8080
'''

4. delete container
'''
 1526  docker ps
 1527  docker stop b3d6720ef1fa
 1528  docker rm  b3d6720ef1fa
 1529  docker run -dp 127.0.0.1:3000:3000 getting-app
'''


* general
'''
docker images               # show all images

docker container ls        #show all comtainers

sudo docker container inspect b3d6720ef1fa | grep -i IPAddress        # check container ip address

'''
