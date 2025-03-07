## Dockerized Airflow for dbt

### Inspired by 
https://medium.com/@aminesnoussi7/orchestrating-dbt-on-snowflake-using-apache-airflow-a-comprehensive-guide-9ca100eb6391

### Prerequisite
Docker

### Usage
#### Setting the right Airflow user
You can also manually create an .env file in the same folder as docker-compose.yaml with this content to get rid of the warning
```
AIRFLOW_UID=50000
```

#### Initialize the database
```bash
docker compose up airflow-init
```

#### start
```bash
docker compose -f docker-compose.yml --build up
```
