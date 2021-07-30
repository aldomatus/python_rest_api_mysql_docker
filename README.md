<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
-->

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="https://i.imgur.com/19coMSB.png" alt="Header" >
  </a>
   <div align="center">
   <a href="https://www.facebook.com/aldo.matusmartinez" ><img src="https://github.com/edent/SuperTinyIcons/blob/master/images/svg/facebook.svg" title="Facebook" width="60"  margin="30px"/></a><a href="https://github.com/aldomatus/" ><img src="https://github.com/edent/SuperTinyIcons/blob/master/images/svg/github.svg" title="Github" width="60"/></a><a href="https://www.instagram.com/aldomatus1/" ><img src="https://github.com/edent/SuperTinyIcons/blob/master/images/svg/instagram.svg" title="Instagram" width="60"  /></a><a href="https://www.linkedin.com/in/aldomatus/" ><img src="https://github.com/edent/SuperTinyIcons/blob/master/images/svg/linkedin.svg" title="Linkedin" width="60"  /></a>

  </div>

  <h3 align="center">Learn REST API with Flask, Mysql and Docker</h3>

  <p align="center">
    A project for you to learn to work a flask REST api with docker and the mysql database manager!
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This project is made with the intention of teaching how to use Docker with the backend technologies Flask and Mysql in the project we are going to take into account the following points:

* Create the dockerfile that will have the necessary instructions to create a Python image that will later be converted into a single application.
* Docker Compose allows you through YAML files to instruct the Docker Engine to perform tasks, programmatically. Here we will install the mysql image, declare the environment variables for both mysql and Flask, and also declare the volumes.
* We will add the list of requirements in a requirements.txt file that will be executed automatically within the Dockerfile

### Built With

This section should list any major frameworks that you built your project using. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.
* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [Mysql](https://www.mysql.com/)
* [Docker](https://www.docker.com/)

### Libraries

#### SQLAlchemy (Offers an ORM along with a Core)
The Python SQL Toolkit and Object Relational Mapper
SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.

#### Flask-Marshmallow (Serializer)
Flask-Marshmallow is a thin integration layer for Flask (a Python web framework) and marshmallow (an object serialization/deserialization library) that adds additional features to marshmallow, including URL and Hyperlinks fields for HATEOAS-ready APIs. It also (optionally) integrates with Flask-SQLAlchemy.

#### Flask-SQLAlchemy 
Flask-SQLAlchemy is an extension for Flask that adds support for SQLAlchemy to your application. It aims to simplify using SQLAlchemy with Flask by providing useful defaults and extra helpers that make it easier to accomplish common tasks.

<!-- GETTING STARTED -->
## Getting Started



### Prerequisites

For this project you need to have Docker and Docker compose installed


<ol>
<li>Link to install Docker engine:</li>
<a href="https://docs.docker.com/engine/install/ubuntu/">Linux</a>
<a href="https://docs.docker.com/engine/install/">  -  Windows or Mac</a>

<li>After installing docker engine install docker compose</li>
<a href="https://docs.docker.com/compose/install/">Linux Windows Mac</a>
</li>



### Installation

1. To obtain my repository you must create a folder in a desired directory and within this folder open a terminal or use cmd in the case of windows.
2. Clone the repo
   ```
   git remote add origin git@github.com:aldomatus/flask_rest_api.git
   
   ```
3. In the folder where docker-compose.yml is located, open a terminal (the same address where you ran the previous line) and write the following command to build the image.
   ```
   docker-compose build
   ```
4. Once the previous execution is finished, you must run the services made in the build.
   ```
   docker-compose up
   ```
5. If all goes well, our application should already be executing the app.py file with python using the mysql database, now we just have to check by entering the following link in our browser:

   ```
   http://localhost:5000/
   ```
6. You should have a response like this:
   ```
   {"message": "Welcome to my API"}
   ```


<!-- USAGE EXAMPLES -->
## Usage

With this base you can make any flask code, modify the API and adapt it to your projects. It is important that you study the docker code to understand what is behind each file in both the Docker and the docker-compose.yml.



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/aldomatus/flask_rest_api/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Aldo Matus - [Linkedin](https://www.linkedin.com/in/aldomatus/) [Facebook](https://www.facebook.com/aldo.matusmartinez/)

Project Link: [Repository](https://github.com/aldomatus/flask_rest_api/)






