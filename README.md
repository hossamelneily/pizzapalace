# PizzaPalace Django Project

PizzaPalace is a Django-based web application for managing orders, menus, and statistics for a pizza restaurant.

## Setup Instructions

Follow these steps to set up the PizzaPalace project:

### 1. Clone the Repository

Clone the PizzaPalace repository to your local machine:

```bash
git clone https://github.com/hossamelneily/pizzapalace.git
```
### 2. Setting Up a Virtual Environment

To set up a virtual environment for the PizzaPalace project, follow these steps:

1. First, make sure you have Python installed on your system. You can download and install Python from the [official website](https://www.python.org/).

2. Once Python is installed, navigate to the root directory of the project.

3. Run the following command to create a new virtual environment named `venv`:

    ```
    python -m venv venv
    ```

4. Activate the virtual environment. On Windows, you can activate it with:

    ```
    venv\Scripts\activate
    ```

   On macOS and Linux, you can activate it with:

    ```
    source venv/bin/activate
    ```




### 3. Install Dependencies

Navigate to the project directory and install the required dependencies using pip:

```bash
cd PizzaPalace
pip install -r requirements.txt
```

### 4. Configure Database

Configure the database settings in settings.py. By default, PizzaPalace uses SQLite as the database backend.

### 5. Run Migrations

Run database migrations to create the necessary tables:

```bash 
python manage.py migrate
```

### 6. Run Celery Worker
Start a Celery worker to process asynchronous tasks:

```bash
celery -A PizzaPalace worker -l info
 ```

### 7. Run Celery Beat
Start Celery Beat to schedule periodic tasks such as updating statistics:

```bash
celery -A PizzaPalace beat -l info
```

### 8. Run Django Server
Start the Django development server:

```bash
python manage.py runserver
```

The PizzaPalace application should now be accessible at http://localhost:8000.

## Usage

### Accessing APIs
You can access the PizzaPalace APIs using the following endpoints:
- http://127.0.0.1:8000/swagger/
- http://127.0.0.1:8000/redoc/

### Celery Tasks

#### Cook Pizza Task

The cook_pizza task is responsible for cooking pizzas asynchronously. It is triggered when an order containing pizzas is placed.

#### Beat Task for Statistics

A Celery Beat task is scheduled to update order statistics at regular intervals, such as the end of each month.


