# Python To-Do List API — CI/CD Assignment 2

A small Flask API packaged with Docker and checked by GitHub Actions.

## Endpoints
- `GET /` — API information
- `GET /health` — health check
- `GET /tasks` — list tasks
- `POST /tasks` — create a task with JSON such as `{"title": "Read notes"}`

## Run locally without Docker
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements-dev.txt
pytest -v
python app.py
```
Open `http://127.0.0.1:5000/health`.

## Build and run with Docker
```bash
docker build -t todo-list-python .
docker run --rm -p 5000:5000 todo-list-python
```
Then open `http://127.0.0.1:5000/health`.

## CI/CD workflow
`.github/workflows/ci-cd.yml` runs Build → Test → Deploy on pushes to `main`, pull requests targeting `main`, and manual dispatch.
- **Build:** builds the Docker image.
- **Test:** installs dependencies and runs pytest.
- **Deploy:** builds and runs the container on the GitHub Actions runner and checks `/health`.

**Deployment note:** The Deploy stage is a temporary runner demonstration. The container is removed when the job finishes; it is not permanent public hosting. To deploy publicly, configure a target service and credentials/secrets.
