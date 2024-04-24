# README.md

## Event Service

This Flask application provides an API endpoint to fetch events within a specified time range. It respects the OpenAPI specification and follows PEP8 guidelines for code formatting.

### Installation

1. Clone the repository:
git clone

2. Install dependencies:
pip install -r requirements.txt


3. Run migrations:
flask db upgrade 

4. Start the application:
python run.py


### API Endpoint

- `/events`: GET endpoint to fetch events within a specified time range. Parameters `starts_at` and `ends_at` must be provided.

### Makefile

This repository includes a Makefile with the following targets:

- `run`: Installs dependencies, runs migrations, and starts the application.

```makefile
# Makefile

.PHONY: run

run:
 pip install -r requirements.txt
 flask db upgrade
 python run.py


To run the application, simply use the make run command.


