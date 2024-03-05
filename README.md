# Test project

Hello, this project is an exercise project in which it is connected to its Postgres database in Docker using the Python code in the folder and creates three tables with the following specifications.

> The first table named "user" whose fields are "username", "first-name", "last-name", "password", "email"
> The second table with the name of the "product", which has the "name","price", and "color" fields
> The third table is named "Organizations" and has "username","password" and "email" fields
> There is a primary key field in all fields

After creating the tables in the database, it values them randomly using the [Faker](https://faker.readthedocs.io/en/master/) library

In the docker-compose.yml file, which is related to Docker, we first created the Postgres database using the Postgres image, and then we created the PGadmin using its image in another container, and then these two containers using a We connected the network and using volume we were able to save the values in the database

## Installation

First, note that Docker, Python and Docker Compose are installed in your system

Follow the steps below to install Docker Compose on Linux
```sh
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```
Then
```sh
sudo chmod +x /usr/local/bin/docker-compose
```
Run the following command to test the correct installation
```sh
docker-compose --version
```
In the next step, we need to install the libraries available in Python

First, install the psycopg2 library with the following command
```sh
pip install psycopg2-binary selenium
```
Then install the facker library using the following command
```sh
pip install faker
```
Now, after adding the folders to our system, execute the following command to create the containers
```sh
docker-compose up -d
```
Now run the Python code using the following command
```sh
python test.py
```
If you are done and want to delete the containers, execute the following command
```sh
docker-compose down
```

