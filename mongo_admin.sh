# Log into mongodb with:
mongo admin -u admin -p admin --host localhost --port 27017

# Run these commands:
use admin;
db.grantRolesToUser('admin', [{ role: 'root', db: 'admin' }]);

# Use this command out of the container to get the IP:
docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' container_name_or_id