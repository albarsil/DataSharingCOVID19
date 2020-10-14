# Comands to start mongo instance

Run `run_mongo.sh` script and will start MongoDB at port 27017.

Then, log into mongodb and run:

`mongo admin -u admin -p admin --host localhost --port 27017`

Once you're inside it, run these commands:

```
use admin;
db.grantRolesToUser('admin', ["root"]);
db.grantRolesToUser('admin', roles=[{role:'dbAdminAnyDatabase', db:'admin'},{role:'readWriteAnyDatabase', db:'admin'},{role:'userAdminAnyDatabase', db:'admin'},{role:'root', db:'admin'}, {role: 'read', db:'admin'}, {role:'dbOwner', db:'admin'},{role:'readWrite', db:'admin'}]);
```

Disconnect from mongo and use this command out of the container to get the running MongoDB IP:

```docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <container_name_or_id>```
