# FRONT - MEDICAL INFORMATION MANAGEMENT

## About the solution

We divided our solution into **4 stages**:

**In stage 1**, we are collecting data from reports sent from the battlefield by rescuers, soldiers and, in the future, intelligent measuring devices.

**In stage 2**, with the use of an appropriate decision tree and machine learning, we are estimating the best allocation of the patient to the hospital.

**In stage 3**, we are determining the optimal soldier transport paths using graph algorithms. There are 2 paths - the safest and the fastest.

**In stage 4**, we are notifying a selected hospital to prepare for patient treatment,  mission commander about the loss/injury of a soldier and a rescuer about transport routes.

## Project structure

`hackathonbackend` - part of backend services based on **python**, **django**, **DRF**, **celery**, **scikit-learn (_naive bayes classifier_)**, **sqlite**. <br />
`neo4j` - **graph** database; used to store geodata of battlefield/situation map objects.<br />
`hackathonfrontend` - part of visual/frontend services based on **react**; this image can be seen, for example, by the commander.

## Project run

We use docker containers so you can easily setup and run environment on any devices.<br />
All you have to do is to start console and run containers with the following command:
```python
docker-compose up
```
After that you should load some map data to neo4j (_see section Load data to neo4j_).



### Load data to neo4j

- Log in to the database management system under `localhost:7474` using credentials:
```python
L: neo4j
T: test
```
- In neo4j console run following scripts: 
a) `neo4j/script/script_create_populate_init` 
b) `neo4j/script/script_create_graph`

## Admin

Here you can add and manage data using import tools.

Credentials for `localhost:8000/admin`:
```python
L: hackathon_admin
H: zgfIdjXxNFVEyrua9cjI
```

## REST API

We also created REST API for faster integration of our solution with another NATO services.<br />
You can find a list of available endpoints at: `localhost:8000`

