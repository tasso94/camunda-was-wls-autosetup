# Setup Camunda BPM on IBM & Oracle Java Application Servers

## IBM Websphere 9.0 + DB2 11.1

```sh
docker run \
    -e CAM_LDAP_USERNAME=my.username \
    -e CAM_LDAP_PASSWORD=S3CRE7!PASSWD \
    -p 9080:9080 -p 9060:9060 -ti was
```

### Optional Variables
CAMUNDA_VERSION (7.12.0-alpha5) \
DATABASE_HOST (localhost) \
DATABASE_PORT (50000) \
DATABASE_NAME (engine)

## Setup Camunda BPM on Oracle WebLogic Server 12R2 + Oracle 18c

```sh
docker run \
    -e CAM_LDAP_USERNAME=my.username \
    -e CAM_LDAP_PASSWORD=S3CRE7!PASSWD \
    -p 7001:7001 -ti wls
```

## Optional Variables
CAMUNDA_VERSION (7.12.0-alpha5) \
DATABASE_HOST (localhost) \
DATABASE_PORT (1521) \
DATABASE_NAME (XE)