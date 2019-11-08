current_count = 0
admin_server_is_running = 'false'

while ((admin_server_is_running=='false') and (current_count < 60)):
    try:
        connect("weblogic", 'weblogic1', 't3://localhost:7001')
        admin_server_is_running = 'true'
    except Exception, e:
        java.lang.Thread.sleep(30000)
        current_count = current_count +1

deploy("camunda-engine-rest", 
    "/home/camunda/distro/webapps/camunda-engine-rest.war", 
    deploymentOrder=80, 
    createPlan='true', 
    remote='true', 
    upload='true', 
    targets='AdminServer', 
    timeout=(60 * 1000))
    
deploy("camunda-webapp", 
    "/home/camunda/distro/webapps/camunda-webapp.war", 
    deploymentOrder=80, 
    createPlan='true', 
    remote='true', 
    upload='true', 
    targets='AdminServer', 
    timeout=(60 * 1000))

deploy("camunda-example-invoice", 
    "/home/camunda/distro/webapps/camunda-example-invoice.war", 
    deploymentOrder=80, 
    createPlan='true', 
    remote='true', 
    upload='true', 
    targets='AdminServer', 
    timeout=(60 * 1000))

disconnect()