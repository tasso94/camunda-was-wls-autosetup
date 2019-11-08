#!/bin/bash

DATABASE_HOST=${DATABASE_HOST:-"localhost"}
DATABASE_PORT=${DATABASE_PORT:-"1521"}
DATABASE_NAME=${DATABASE_NAME:-"XE"}
CAMUNDA_VERSION=${CAMUNDA_VERSION:-"7.12.0-alpha5"}

DISTRO_URL=https://app.camunda.com/nexus/repository/camunda-bpm-ee/org/camunda/bpm/weblogic/camunda-bpm-weblogic/${CAMUNDA_VERSION}-ee/camunda-bpm-weblogic-${CAMUNDA_VERSION}-ee.zip

cd /home/camunda
wget --user=${CAM_LDAP_USERNAME} --password=${CAM_LDAP_PASSWORD} ${DISTRO_URL}

mkdir /home/camunda/distro
cd /home/camunda/distro
unzip ../camunda-bpm-weblogic-${CAMUNDA_VERSION}-ee.zip
rm ../camunda-bpm-weblogic-${CAMUNDA_VERSION}-ee.zip

mv /home/camunda/distro/modules/camunda-oracle-weblogic-ear-${CAMUNDA_VERSION}-ee.ear  /home/camunda/distro/modules/camunda-oracle-weblogic-ear.ear
mv /home/camunda/distro/webapps/camunda-engine-rest-${CAMUNDA_VERSION}-ee-wls.war  /home/camunda/distro/webapps/camunda-engine-rest.war
mv /home/camunda/distro/webapps/camunda-webapp-ee-wls-${CAMUNDA_VERSION}-ee.war /home/camunda/distro/webapps/camunda-webapp.war
mv /home/camunda/distro/webapps/camunda-example-invoice-${CAMUNDA_VERSION}-ee.war /home/camunda/distro/webapps/camunda-example-invoice.war

mv /home/camunda/distro/modules/lib/* /home/camunda/oracle/domains/base_domain/lib/

mv /home/camunda/distro/modules/camunda-oracle-weblogic-ear.ear /home/camunda/oracle/domains/base_domain/autodeploy/

cd /home/camunda/oracle/domains # wlst creates server domain in this folder

/home/camunda/oracle/oracle_common/common/bin/wlst.sh \
    /home/camunda/oracle_datasource.py ${DATABASE_HOST} ${DATABASE_PORT} ${DATABASE_NAME}

/home/camunda/oracle/domains/base_domain/bin/startWebLogic.sh &

/home/camunda/oracle/oracle_common/common/bin/wlst.sh /home/camunda/deploy.py

tail -F /home/camunda/oracle/domains/base_domain/servers/AdminServer/logs/AdminServer.log