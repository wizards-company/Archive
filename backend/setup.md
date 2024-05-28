# Setup Guide

## Prerequisites

- **Python 3.10+**: Make sure you have Python installed. You can download it from [python.org](https://www.python.org/).
- **PostgreSQL**: Ensure PostgreSQL is installed and running. You can download it from [postgresql.org](https://www.postgresql.org/).
- **Docker and Docker Compose**: These tools are required to manage the database containers. You can download them from [docker.com](https://www.docker.com/).

## Clone the Repository

1. Clone the repository from GitHub:
   ```sh
   git clone https://github.com/lfqcamargo/web_book_trade.git
   cd web_book_trade
   ```

## Set Up Virtual Environment and Install Dependencies

2. Set up a Python virtual environment and activate it:
   ```sh
   python -m venv .venv
   source .venv/bin/activate
   ```

3. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Configure Environment Variables

4. Create environment variable files for different environments:

   - **.env.dev**
     ```
    DATABASE_USER=root
    DATABASE_PASSWORD=you_user
    DATABASE_DB=you_db
    DATABASE_PORT=you_port
    DATABASE_VOLUME=you_volume
    DATABASE_CONTAINER_NAME=you_name
    DATABASE_URL=postgresql+asyncpg://root:you_user@localhost:5434/you_db

     ```

   - **.env.test**
     ```
    DATABASE_USER=root
    DATABASE_PASSWORD=you_user
    DATABASE_DB=you_db
    DATABASE_PORT=you_port
    DATABASE_VOLUME=you_volume
    DATABASE_CONTAINER_NAME=you_name
    DATABASE_URL=postgresql+asyncpg://root:you_user@localhost:5434/you_db

     ```

   - **.env.prod**
     ```
    DATABASE_USER=root
    DATABASE_PASSWORD=you_user
    DATABASE_DB=you_db
    DATABASE_PORT=you_port
    DATABASE_VOLUME=you_volume
    DATABASE_CONTAINER_NAME=you_name
    DATABASE_URL=postgresql+asyncpg://root:you_user@localhost:5434/you_db
     ```

access the .env.example file to see an example

## Set Up and Run PostgreSQL with Docker

5. Use Docker Compose to set up PostgreSQL containers for development, testing, and production:

   Create a `docker-compose.yml`:
   
    make updatabase_test

    make updatabase_dev

    make updatabase_prod


## Apply Database Migrations

6. Run Alembic migrations to set up the database schema:

   - For development:
     ```sh
     make upgrade_head_test
     ```

   - For testing:
     ```sh
     make upgrade_head_dev
     ```

   - For production:
     ```sh
     make upgrade_head_prod
     ```

## Run the Application

8. Start the FastAPI application:

   - For development:
     ```sh
     run_dev
     ```

   - For production:
     ```sh
     run_prod
     ```
   - For test:
     ```sh
     run_test
     ```

## Running Tests

9. To run the tests, use the following command:
    ```sh
    pytest
    ```

## Additional Resources

- **API Documentation**: For detailed API documentation, refer to [API.md](API.md).