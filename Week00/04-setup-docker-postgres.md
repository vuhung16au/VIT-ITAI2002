# Activity 4: Setup Docker and PostgreSQL

**Objective:** Install Docker and use Docker Compose to run a local PostgreSQL 18.4 database.

## Step 1: Install Docker

- **Windows and macOS:** Download and install [Docker Desktop](https://www.docker.com/products/docker-desktop/).
- **Linux:** Install [Docker Engine](https://docs.docker.com/engine/install/) and [Docker Compose](https://docs.docker.com/compose/install/).

*Note for Windows users:* Ensure you have WSL 2 (Windows Subsystem for Linux) installed and enabled, as Docker Desktop relies on it.

## Step 2: Create a Docker Compose File

Instead of installing PostgreSQL directly on your computer, we will use Docker to run it in a container. This ensures everyone has the exact same version and configuration.

1. In your `ITAI2002-Projects` folder, create a new file named `docker-compose.yml`.
2. Open it in VS Code and paste the following working sample:

```yaml
version: '3.8'

services:
  db:
    image: postgres:18.4-alpine
    container_name: itai2002-postgres
    restart: always
    environment:
      POSTGRES_USER: admin
      POSTGRES_PASSWORD: secretpassword
      POSTGRES_DB: itaidb
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

## Step 3: Run PostgreSQL

1. Open your terminal (or VS Code terminal) and navigate to the folder containing `docker-compose.yml`.
2. Run the following command to start the database in the background:
   ```bash
   docker compose up -d
   ```
3. Docker will download the PostgreSQL 18.4 image and start it. You can see running containers using:
   ```bash
   docker ps
   ```

*To stop the database later, you can run `docker compose down`.*
