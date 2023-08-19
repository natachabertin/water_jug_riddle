# Water Jug Riddle
CLI and API to interact with a Water Jug Riddle app


## Executing the app

#### Run the backend server dockerized
##### First time set up
1. Ensure you have Docker daemon/desktop running.
2. Clone this repo and cd into `water-jug-riddle`.
3. Build the repo with
    ```bash
    docker-compose up -d --build
    ```
4. In [OpenAPI docs, in your local](http://localhost:8000/docs) you'll see OpenAPI docs from the app.

##### Resume
1. Execute `docker-compose up`.
2. You'll see app docs in [http://localhost:8000/docs](http://localhost:8000/docs).


#### Testing and debugging backend locally (without Docker)
##### Setup
1. After cloning the repo, create a virtual environment
2. `cd` into `water-jug-riddle` and install the requirements in it.

##### Resume
3. Run the tests with `pytest .`
4. Debugging and local running
    * CLI: `uvicorn app.main:app --reload --workers 1 --host 0.0.0.0 --port 8000`
    * IDE (PyCharm):
        1. In the running selector, click _Edit configurations_ and add a new one.
        2. Change _Script path_ selector to Module name, and type in with `uvicorn`.
        3. In parameters, type `app.main:app --reload --port 8000` (given the working directory below is `water-jug-riddle/app`)

## Main commands for recurrent actions

### Pre-commit
#### Running
```bash
pre-commit run --all-files --show-diff-on-failure
```
#### Updating pre-commit repos
```bash
pre-commit autoupdate
```
