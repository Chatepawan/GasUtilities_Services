# Gas Utility Service Requests Django Application

A Django-based web application that allows customers to submit and track their service requests for a gas utility company. The application also provides customer support representatives with tools to manage service requests and provide support.

## Features

- **Customer-facing features**:
  - Submit service requests online.
  - Track the status of service requests.
  - View account details and request history.
  
- **Admin-facing features**:
  - Manage service requests (view, update status).
  - Provide support to customers.
  - Access and update service request details.

## Setup and Installation

Follow these steps to get the project up and running on your local machine:

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/gas-utility-service.git
cd gas-utility-service
Run below commands on the terminal
pip install django
python manage.py migrate
python manage.py createsuperuser (Create the username, email, & password)
After that login using the created username and password.
python manage.py runserver
You will see the server is running on http://127.0.0.1:8000/

