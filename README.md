<!-- README For Playcenter API -->

# Playcenter API

## Introduction

This is a REST API for the Playcenter application. It is built using the Django REST Framework.
This API is used to manage and provide data for the Playcenter application.Also, it is used to manage the users and their roles.

## Installation

### Requirements

Refer to the requirements.txt file for the list of dependencies.

### Setup

1. Clone the repository

2. Create a virtual environment

3. Install the dependencies

4. Run the migrations

5. Create a superuser

6. Run the server

## Usage

### Endpoints

#### Authentication

##### Register

`POST /api/v1/auth/register/`

##### Login

`POST /api/v1/auth/login/`

##### Logout

`POST /api/v1/auth/logout/`

##### Refresh Token

`POST /api/v1/auth/refresh/`

#### Users

##### List Users

`GET /api/v1/users/`

##### Create User

`POST /api/v1/users/`

##### Retrieve User

`GET /api/v1/users/{id}/`

##### Update User

`PUT /api/v1/users/{id}/`

##### Delete User

`DELETE /api/v1/users/{id}/`
