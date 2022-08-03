# Python Example with Healenium

[![Docker Pulls](https://img.shields.io/docker/pulls/healenium/hlm-backend.svg?maxAge=25920)](https://hub.docker.com/u/healenium)
[![License](https://img.shields.io/badge/license-Apache-brightgreen.svg)](https://www.apache.org/licenses/LICENSE-2.0)

Python 3.9.5 + Pytest project with healenium usage example 

[1. Start Healenium components](#1-start-healenium-components)
* [Healenium with Selenoid](#run-healenium-with-selenoid)
* [Healenium with Selenium-Grid](#run-healenium-with-selenium-grid)

[2. Run test](#2-run-test)

[3. Monitoring tests running](#3-monitoring-tests-running)

## How to start

### 1. Start Healenium components

Go into healenium folder

```cd healenium``` 

#### Run Healenium with Selenoid:

> Note: `browsers.json` consists of target browsers and appropriate versions.
> Before run healenium you have to manually pull selenoid browser docker images with version specified in browsers.json

Example pull selenoid chrome image:
```sh
docker pull selenoid/vnc:chrome_102.0
```
Full list of browser images you can find [here](https://hub.docker.com/u/selenoid)

Run healenium with Selenoid:
```sh
docker-compose up -d
```

#### Run Healenium with Selenium-Grid:
```sh
docker-compose -f docker-compose-selenium-grid.yaml up -d
```

<b>ATTENTION</b>

Verify the next images are <b>Up</b> and <b>Running</b>
- `postgres-db` (PostgreSQL database to store etalon selector / healing / report)
- `hlm-proxy` (Proxy client request to Selenium server)
- `hlm-bacand` (CRUD service)
- `selector imitator` (Convert healed locator to convenient format)
- `selenoid`/`selenium-grid` (Selenium server)

### 2. Run test
To run tests in terminal with pytest you need to go to execute next commands:

``python3 -m venv env``

``source ./env/bin/activate``

``python -m pip install -U pytest``

``python -m pip install -U selenium``

``python -m pytest ./tests/``

> If you want to execute tests from specified file, please use the command: ```python -m pytest ./tests/test_css.py```
>> In case you want to run all tests in project use ```python -m pytest ./tests/``` command

### 3. Monitoring tests running
You can monitor tests running if you using Healenium with Selenoid plus Selenoid Ui, go to:</br>
```http://localhost:8080```
