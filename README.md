<h1 align="center"> Pop-up Café Mini Project </h1>

A Dockerized Python CLI application for a fictional pop-up café in a busy business district, designed to log and track customer orders. The application allows users to create, modify, and manage orders while supporting multiple data formats (text files, JSON, CSV). Data is persisted in a MySQL database to enable full CRUD (Create, Read, Update, Delete) operations. 

--- 

<h1 align="center"> Repository Structure </h1>

This repository contains the following files: 

1. **Code.py** - A file containing the main code for the application.
2. **Couriers.csv** - A CSV file detailing information about the couriers the café uses. 
3. **Orders.csv** - A CSV file containing all order information.
4. **Products.csv** - A CSV file with information relating to all products offered. 
5. **docker-compose.yml**, **.env**, and **requirements.txt** - 3 files (YAML, env, and text) used to launch a MySQL database locally using Docker.
6. **db_setup.py** - A Python file used to create the tables and load data from the CSV files.
7. **db_connection.py** - A Python file used to establish a connection with the MySQL database.
8. **App.py** - The Python executable that must be run to start the application.

--- 

<h1 align="center"> How to Run the Application </h1>

To run the most updated version of the application, follow these steps:

1. Set up your MySQL database locally using Docker by running the **docker-compose.yml** file or by installing MySQL on your machine.
2. Run the **App.py** file.

--- 

<h1 align="center"> Usage Instructions </h1>

Once the application is running, you can interact with it via the Visual Studio Code terminal. Simply follow the on-screen prompts to log and track orders as needed.

---
