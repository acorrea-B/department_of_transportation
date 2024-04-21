# Traffic Violations Registration System

## Description
This project is a comprehensive system designed to manage the registration of traffic violations. It is developed in Python and structured according to the hexagonal architecture, ensuring a separation between business logic and infrastructure. The system can be deployed as both an AWS Lambda service and a microservices environment using Flask.

## Features
- **Administrative Interface**: Allows for the management of person, vehicle, and officer records. Supports creation, viewing, modification, and deletion of records, ensuring referential integrity.
- **Police Officer API**: Includes methods for real-time infringement loading and generating reports of violations associated with a specific person.
- **Secure Authentication**: Implements access token authentication (Bearer Token) to secure API interactions.

## Technologies Used
- **Python 3.8+**: Programming language.
- **Flask**: Web framework used for developing the administrative interface and API.
- **SQLAlchemy**: ORM for database interaction.
- **Docker**: Used for packaging and deploying the application consistently across different environments.
- **AWS Lambda and API Gateway**: Allow serverless deployment to handle API requests in a scalable way.

## Project Structure
The repository is organized into the following main folders:
- `domain/`: Contains the models and business logic.
- `application/`: Defines the necessary ports and adapters for the application.
- `infrastructure/`: Houses specific configurations for Flask and AWS Lambda.
- `tests/`: Includes tests to ensure the correct functionality of the components.
