#!/bin/bash

DATABASE_HOST=${DATABASE_HOST:-"localhost"}
DATABASE_PORT=${DATABASE_PORT:-"50000"}
DATABASE_NAME=${DATABASE_NAME:-"engine"}
CAMUNDA_VERSION=${CAMUNDA_VERSION:-"7.12.0-alpha5"}

JDBC_DRIVER_URL=https://app.camunda.com/nexus/repository/thirdparty/com/ibm/db2/jcc/db2jcc4/11.1.1.1/db2jcc4-11.1.1.1.jar
DISTRO_URL=https://app.camunda.com/nexus/repository/camunda-bpm-ee/org/camunda/bpm/websphere/camunda-bpm-websphere9/${CAMUNDA_VERSION}-ee/camunda-bpm-websphere9-${CAMUNDA_VERSION}-ee.zip

cd /home/camunda
wget --user=$CAM_LDAP_USERNAME --password=$CAM_LDAP_PASSWORD $JDBC_DRIVER_URL
wget --user=$CAM_LDAP_USERNAME --password=$CAM_LDAP_PASSWORD $DISTRO_URL

mkdir /home/camunda/distro
cd /home/camunda/distro 
unzip ../camunda-bpm-websphere9-${CAMUNDA_VERSION}-ee.zip
rm ../camunda-bpm-websphere9-${CAMUNDA_VERSION}-ee.zip

mv /home/camunda/distro/modules/camunda-ibm-websphere-ear-${CAMUNDA_VERSION}-ee.ear /home/camunda/distro/modules/camunda-ibm-websphere-ear.ear
mv /home/camunda/distro/webapps/camunda-engine-rest-${CAMUNDA_VERSION}-ee-was9.war /home/camunda/distro/webapps/camunda-engine-rest.war
mv /home/camunda/distro/webapps/camunda-webapp-ee-was9-${CAMUNDA_VERSION}-ee.war /home/camunda/distro/webapps/camunda-webapp.war
mv /home/camunda/distro/webapps/camunda-example-invoice-${CAMUNDA_VERSION}-ee.war /home/camunda/distro/webapps/camunda-example-invoice.war

/home/camunda/IBM/WebSphere/AppServer/profiles/AppSrv01/bin/wsadmin.sh -conntype NONE -f \
    /home/camunda/db2_datasource.py ${DATABASE_HOST} ${DATABASE_PORT} ${DATABASE_NAME}

/home/camunda/IBM/WebSphere/AppServer/profiles/AppSrv01/bin/wsadmin.sh -conntype NONE -f /home/camunda/setup.py

/home/camunda/IBM/WebSphere/AppServer/profiles/AppSrv01/bin/startServer.sh server1

tail -F /home/camunda/IBM/WebSphere/AppServer/profiles/AppSrv01/logs/server1/SystemOut.log