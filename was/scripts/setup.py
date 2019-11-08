AdminResources.createSharedLibraryAtScope("localhostNode01(cells/localhostNode01Cell/nodes/localhostNode01|node.xml#Node_1)", "Camunda",
  "/home/camunda/distro/modules/lib/", [
  ['description', 'Camunda BPM Shared Libraries'],
  ['isolatedClassLoader', 'true']
])

AdminResources.createWorkManagerAtScope("localhostNode01(cells/localhostNode01Cell/nodes/localhostNode01|node.xml#Node_1)",
  "camunda-platform-jobexecutor-WM",
  "wm/camunda-bpm-workmanager", "2", "2", "5", "5",
  "WorkManagerProvider(cells/localhostNode01Cell|resources-pme.xml#WorkManagerProvider_1)", [
    ['description', 'Camunda BPM Platform Workmanager'],
    ['isGrowable', 'false'],
    ['workReqQFullAction', '1'],
    ['workReqQSize', '5']
])

# EAR
AdminApp.install("/home/camunda/distro/modules/camunda-ibm-websphere-ear.ear",
['-target', u'WebSphere:cell=localhostNode01Cell,node=localhostNode01,server=server1'])

# Webapps
AdminApp.install("/home/camunda/distro/webapps/camunda-engine-rest.war",
['-target', u'WebSphere:cell=localhostNode01Cell,node=localhostNode01,server=server1', '-MapWebModToVH', [
  ['.*', '.*', 'default_host']
], '-appname', 'camunda-engine-rest', '-MapSharedLibForMod', [
  ['.*', '.*', 'Camunda']
]])

AdminApp.install("/home/camunda/distro/webapps/camunda-webapp.war",
['-target', u'WebSphere:cell=localhostNode01Cell,node=localhostNode01,server=server1', '-MapWebModToVH', [
  ['.*', '.*', 'default_host']
], '-appname', 'camunda-webapp-ee-was9', '-MapSharedLibForMod', [
  ['.*', '.*', 'Camunda']
]])

AdminApp.install("/home/camunda/distro/webapps/camunda-example-invoice.war",
['-target', u'WebSphere:cell=localhostNode01Cell,node=localhostNode01,server=server1', '-MapWebModToVH', [
  ['.*', '.*', 'default_host']
], '-appname', 'camunda-example-invoice', '-MapSharedLibForMod', [
  ['.*', '.*', 'Camunda']
]])

AdminConfig.save()