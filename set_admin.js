use admin;
db.grantRolesToUser('admin', [{ role: 'root', db: 'admin' }]);
exit;