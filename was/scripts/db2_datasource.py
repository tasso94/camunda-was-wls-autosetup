import sys

host=sys.argv[0]
port=sys.argv[1]
database_name=sys.argv[2]

jdbcProvider = AdminConfig.create('JDBCProvider', u'localhostNode01Cell(cells/localhostNode01Cell|cell.xml#Cell_1)', [
  ['name', 'DB2 Universal JDBC Driver Provider (XA)'],
  ['classpath', '/home/camunda/db2jcc4-11.1.1.1.jar'],
  ['nativepath', ''],
  ['implementationClassName', 'com.ibm.db2.jcc.DB2XADataSource'],
  ['description', 'DB2 Universal JDBC Driver Provider (XA)'],
  ['providerType', 'DB2 Universal JDBC Driver Provider (XA)']
])

AdminTask.createAuthDataEntry([
	'-alias', 'camunda-bpm-db2-JAAS',
	'-user', 'camunda',
	'-password', 'camunda',
	'-description', 'Camunda database user'
])

dataSource = AdminConfig.create('DataSource', jdbcProvider, [
  ['name', 'camunda-bpm-db2-DS'],
  ['description', 'camunda-bpm-db2-DS'],
  ['jndiName', 'jdbc/ProcessEngine'],
  ['statementCacheSize', 10],
  ['datasourceHelperClassname', 'com.ibm.websphere.rsadapter.DB2DataStoreHelper'],
  ['authDataAlias', 'localhostNode01/camunda-bpm-db2-JAAS'],
  ['mapping', [
    ['authDataAlias', 'localhostNode01/camunda-bpm-db2-JAAS'],
    ['mappingConfigAlias', 'DefaultPrincipalMapping']
  ]],
  ['xaRecoveryAuthAlias', 'localhostNode01/camunda-bpm-db2-JAAS']
])

resourcePropertySet = AdminConfig.create('J2EEResourcePropertySet', dataSource, [], 'propertySet')

AdminConfig.create('J2EEResourceProperty', resourcePropertySet, [
  ['name', 'databaseName'],
  ['type', 'java.lang.String'],
  ['value', database_name],
  ['description', '']
])

AdminConfig.create('J2EEResourceProperty', resourcePropertySet, [
  ['name', 'serverName'],
  ['type', 'java.lang.String'],
  ['value', host],
  ['description', '']
])

AdminConfig.create('J2EEResourceProperty', resourcePropertySet, [
  ['name', 'portNumber'],
  ['type', 'java.lang.Integer'],
  ['value', port],
  ['description', '']
])

AdminConfig.create('J2EEResourceProperty', resourcePropertySet, [
  ['name', 'driverType'],
  ['type', 'java.lang.Integer'],
  ['value', '4'],
  ['description', '']
])

AdminConfig.save()

