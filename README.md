## Dockerized Airflow for dbt

### Inspired by 
https://medium.com/@aminesnoussi7/orchestrating-dbt-on-snowflake-using-apache-airflow-a-comprehensive-guide-9ca100eb6391

### Prerequisite
Docker

### Usage
#### Build image
```bash
docker compose build
```

#### Initialize the database
```bash
docker compose up airflow-init
```

#### Run Airflow
```bash
docker compose up --build
```

#### Stop Airflow
```bash
docker stop $(docker ps -qa) && sudo chown nxydx dags/*.* && sudo rm -rf logs && mkdir logs
```

#### Web Interface link
```
localhost:8080
```
More [methods](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html#accessing-the-web-interface)

###
General Details on [Dockerize Airflow](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html#accessing-the-web-interface)