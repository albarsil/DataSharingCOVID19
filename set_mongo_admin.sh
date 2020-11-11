# Log into mongodb and execute script:
mongo admin -u admin -p admin --host localhost --port 27017 < mongo_admin.js

# Use this command out of the container to get the IP:
MONGOHOST=$(docker ps | grep 'tutum' | awk '{ print $1 }')
MONGOHOST=$(docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $MONGOHOST)

echo "Mongo is running on: ${MONGOHOST}"