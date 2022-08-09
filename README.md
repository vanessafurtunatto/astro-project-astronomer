# astro-project-astronomer

Airflow

What is?
Apache Airflow is a open source platform to programmatically AUTHOR, SCHEDULE, and MONITOR workflows.

What a benefit? 
Dinamic
Scalable
Interactive
Extensible

Core Components

Web sever 
Scheduler
Metadata Database
Executor - How 
Worker - Where 

Common Architectures
Single node Architecture (same machine)

Multi node (celery) 

Core Concepts

DAGs - Directed acyclic graph 
Operators - creating task in your DAG
Three types of operator: Action Operators, Transfer Operators, Sensor Operators;
Task - Intense of an operator 
Task Instance - Represents a specific run of a task: DAG + TASK + Point in time
Dependencies - Specified the relationships

Workflows 
Combination of all concepts 

Task Lifecycle 

Extras or Providers:

Extras - All dependencies
Providers - Operators or hooks


Three ways interactions: 

UI, CLI, Rest API

DAGs View:

Dag; 
Toggle; Owner; Runs; Schedule; Last Run; Recent Tasks; Actions; Links.

Tree view - check status
Graph view - check dependencies status
Gantt view - check how time is spent

CLI Commands:   docker ps

Docker exec -it “” /bin/bash 

Airflow db init 
Airflow db upgrade
Airflow db reset
Airflow webserver
Airflow schedule 
Airflow celery worker
Airflow dags pause
Airflow dags unpause
Airflow dags trigger
Airflow dags trigger -e
Airflow dags list
Airflow tasks list
Airflow tasks test
Airflow dags backfill

 DAG Scheduling

Start date - date os Dags starter scheduling 
Scheduling - interval  - Parameter of interval
End date - define finish of scheduling Dags 
