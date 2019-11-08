import sys

host=sys.argv[1]
port=sys.argv[2]
database_name=sys.argv[3]
url="jdbc:oracle:thin:@" + host + ":" + port + ":" + database_name
username="camunda"
password="camunda"

domain_name="base_domain"
ds_name="ProcessEngineDS"
jndi_name="jdbc/ProcessEngine"
driver="oracle.jdbc.pool.OracleConnectionPoolDataSource"

deploy_target="AdminServer"

readTemplate('/home/camunda/oracle/wlserver/common/templates/wls/wls.jar')

cd('/')
cd('Security/base_domain/User/weblogic')
cmo.setPassword('weblogic1')

cd('/Servers/AdminServer')
set('ListenAddress', '')
set('ListenPort', 7001)

setOption('OverwriteDomain', 'true')
setOption('ServerStartMode','dev')

writeDomain(domain_name)
closeTemplate()

readDomain(domain_name)

cd('/')
sysRes = create(ds_name, 'JDBCSystemResource')

cd('/JDBCSystemResource/' + ds_name + '/JdbcResource/' + ds_name)
data_source_params = create('dataSourceParams', 'JDBCDataSourceParams')
data_source_params.setGlobalTransactionsProtocol('TwoPhaseCommit')
cd('JDBCDataSourceParams/NO_NAME_0')
set('JNDIName', java.lang.String(jndi_name))

cd('/JDBCSystemResource/' + ds_name + '/JdbcResource/' + ds_name)
conn_pool_params = create('connPoolParams', 'JDBCConnectionPoolParams')
conn_pool_params.setInitialCapacity(10)
conn_pool_params.setMinCapacity(10)
conn_pool_params.setMaxCapacity(30)

cd('/JDBCSystemResource/' + ds_name + '/JdbcResource/' + ds_name)
driver_params = create('driverParams', 'JDBCDriverParams')
driver_params.setUrl(url)
driver_params.setDriverName(driver)
driver_params.setUseXaDataSourceInterface(True)
driver_params.setPasswordEncrypted(password)
cd('JDBCDriverParams/NO_NAME_0')

create(ds_name, 'Properties')
cd('Properties/NO_NAME_0')

db_user = create('user', 'Property')
db_user.setValue(username)

db_password = create('password', 'Property')
db_password.setValue(password)

db_name = create('databaseName', 'Property')
db_name.setValue(database_name)

server_name = create('serverName', 'Property')
server_name.setValue(host)

port_number = create('portNumber', 'Property')
port_number.setValue(port)

driver_type = create('driverType', 'Property')
driver_type.setValue('4')

cd('/')
assign('JDBCSystemResource', ds_name, 'Target', deploy_target)

updateDomain()
closeDomain()