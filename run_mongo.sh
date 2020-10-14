docker pull tutum/mongodb

# docker run -p 27017:27017 -p 28017:28017 -e AUTH=yes -e JOURNALING=no -v mongodb:/data/ tutum/mongodb mongod --repair
docker run -p 27017:27017 -p 28017:28017 -e AUTH=yes -e MONGODB_PASS="admin" -e JOURNALING=no -v mongodb:/data/ tutum/mongodb 
# docker run -p 27017:27017 -p 28017:28017 -e AUTH=yes -e MONGODB_PASS="admin" -e JOURNALING=no tutum/mongodb 