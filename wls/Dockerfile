FROM registry.camunda.com/camunda-ci-weblogic:12R2-oracle-12

COPY ./scripts/ /home/camunda

RUN chmod +x /home/camunda/start_container.sh

CMD ["/home/camunda/start_container.sh"]

EXPOSE 7001/tcp