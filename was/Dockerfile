FROM registry.camunda.com/camunda-ci-websphere:9.0-db2-10.5-port

COPY ./scripts/ /home/camunda

RUN chmod +x /home/camunda/start_container.sh

CMD ["/home/camunda/start_container.sh"]

EXPOSE 9060/tcp 9080/tcp