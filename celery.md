## Asynchronous Tasks in Python - Getting Started With Celery

Celery is a powerful and flexible distributed task queue for Python, allowing you to manage asynchronous tasks and perform background processing. 

### Prerequisites
Before getting started, ensure you have the following installed:
- Python 3.x
- pip (Python package manager)
- A message broker like RabbitMQ or Redis (Celery requires a message broker to send and receive messages between workers).

#### Installing Celery
- Install Celery using pip:
```bash
pip install celery
```
- Install Redis (or RabbitMQ). If you're using Redis, you can install the Python client for Redis:
```bash
pip install redis
```
N.B: Make sure Redis is running on your local machine or use a hosted Redis service.

### Step-by-Step Example of Using Celery

Let's go through the process of setting up a simple Celery task to get familiar with it.

#### Step 1: Setting Up a Celery App

First, you need to create a Celery app. This will be the central point of your application to handle the task distribution.

1. Create a Python file (e.g., `celery_app.py`) and define the Celery application.
```python
# celery_app.py
from celery import Celery

# Create a Celery instance, and configure the broker (in this case Redis)
app = Celery('tasks', broker='redis://localhost:6379/0')

@app.task
def add(x, y):
    return x + y
```

- The `Celery` object needs two parameters:
  - The name of the app (you can use any name).
  - The broker URL (in this case, we’re using Redis running locally on the default port `6379`).
- The `@app.task` decorator marks the `add` function as an asynchronous task.

#### Step 2: Running the Celery Worker

To execute the tasks, you’ll need to run the Celery worker. The worker is a process that continuously listens for tasks and executes them.

Run the worker in your terminal:

```bash
celery -A celery_app worker --loglevel=info
```

- `celery_app`: This tells Celery to look for the Celery instance in the `celery_app.py` file.
- `worker`: This tells Celery to start the worker process.
- `--loglevel=info`: This sets the logging level to `info`, which will show logs as tasks are processed.

You should see output like this:

```
[celery] Starting worker with pid 12345
```

#### Step 3: Sending Tasks to the Worker

Now that the worker is running, you can send tasks to it.

1. In a new Python file (e.g., `main.py`), import the Celery app and call the `add` task asynchronously.

```python
# main.py
from celery_app import add

# Call the task asynchronously
result = add.apply_async((4, 6))

# Check the result (this is just to show how to access it later)
print(f'Task result: {result.get(timeout=10)}')
```

- `apply_async()` is the method used to send a task to the worker asynchronously.
- `result.get(timeout=10)` waits for the result and gives it back once the worker finishes the task.

When you run `main.py`, the Celery worker processes the task in the background, and the result is returned.

#### Step 4: Running the Example

- Start the Celery worker:
  
  ```bash
  celery -A celery_app worker --loglevel=info
  ```

- Run the `main.py` script:

  ```bash
  python main.py
  ```

If everything is set up correctly, you should see the task result printed in the terminal like so:

```
Task result: 10
```

This means that Celery successfully processed the task in the background.

### Advanced Configuration

Celery offers a wide range of advanced configuration options, such as:

- **Scheduling tasks**: You can schedule tasks to run at a particular time or periodically using **Celery Beat**.
- **Task retries**: Celery allows you to configure task retries in case of failure.
- **Result backends**: You can configure Celery to store results in a database (e.g., Redis, SQLAlchemy, MongoDB) for later retrieval.

For example, to set a retry policy, you can modify the task as follows:

```python
@app.task(bind=True, max_retries=3, default_retry_delay=30)
def add(self, x, y):
    try:
        # Simulate task execution (you could raise an exception here to test retries)
        return x + y
    except Exception as exc:
        raise self.retry(exc=exc)
```

### Common Use Cases for Celery

Celery is great for tasks that are:
- Time-consuming (e.g., sending emails, generating reports, etc.).
- Need to run periodically (e.g., backups, data synchronization).
- Need to scale across multiple machines (distributed systems).

## Link
- https://www.youtube.com/watch?v=THxCy-6EnQM&t=453s
- https://medium.com/@mohammed.farmaan.k/setting-up-celery-with-rabbitmq-in-docker-a-step-by-step-guide-dfcdbcb4658e
  
