# Python Example with Healenium

[![Docker Pulls](https://img.shields.io/docker/pulls/healenium/hlm-backend.svg?maxAge=25920)](https://hub.docker.com/u/healenium)
[![License](https://img.shields.io/badge/license-Apache-brightgreen.svg)](https://www.apache.org/licenses/LICENSE-2.0)

Python 3.9.5 + Pytest project with healenium usage example 

[1. Start Healenium components](#1-start-healenium-components)
* [Healenium with Selenium-Grid](#run-healenium-with-selenium-grid)
* [Healenium with Selenoid](#run-healenium-with-selenoid)


[2. Configuration RemoteWebDriver for Healenium](#2-configuration-remotewebdriver-for-healenium)

[3. Run test](#3-run-test)

[4. Monitoring tests running](#4-monitoring-tests-running)

## How to start

### 1. Start Healenium components

Go into healenium folder

```sh
cd healenium
```

#### Run Healenium with Selenium-Grid:
```sh
docker-compose up -d
```

#### Run Healenium with Selenoid

> Note: `browsers.json` consists of target browsers and appropriate versions.
> Before run healenium you have to manually pull selenoid browser docker images with version specified in browsers.json

Example pull selenoid chrome image:
```sh
docker pull selenoid/vnc:chrome_111.0
```
Full list of browser images you can find [here](https://hub.docker.com/u/selenoid)


Run healenium with Selenoid:
```sh
docker-compose -f docker-compose-selenoid.yaml up -d
```

<b>ATTENTION</b>

Verify the next images are <b>Up</b> and <b>Running</b>
- `postgres-db` (PostgreSQL database to store etalon selector / healing / report)
- `hlm-proxy` (Proxy client request to Selenium server)
- `hlm-backend` (CRUD service)
- `selector imitator` (Convert healed locator to convenient format)
- `selenoid`/`selenium-grid` (Selenium server)

### 2. Configuration RemoteWebDriver for Healenium

To run using Healenium create RemoteWebDriver with URL ```http://<remote webdriver host>:8085```:

```py
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Remote('http://localhost:8085', options=options)
```

To temporarily disable the healing mechanism for certain sections of your code, use the following syntax:

```py
        self.driver.execute_script("disable_healing_true")
        ... // Your code that does not require healing
        self.driver.execute_script("disable_healing_false")
```

### 3. Run test
To run tests in terminal with pytest you need to go to execute next commands:

```sh
python3 -m venv env
```

```sh
source ./env/bin/activate
```

```sh
python -m pip install -U pytest
```

```sh
python -m pip install -U selenium
```

```sh
pytest
```

> If you want to execute tests from specified file, please use the command: ```python -m pytest ./tests/test_css.py```
>> In case you want to run all tests in project use ```python -m pytest ./tests/``` command

### 4. Monitoring tests running
You can monitor tests running if you using Healenium with Selenoid plus Selenoid Ui, go to:</br>
```sh
http://localhost:8080
```

## Community / Support

* [Telegram chat](https://t.me/healenium)
* [YouTube Channel](https://www.youtube.com/channel/UCsZJ0ri-Hp7IA1A6Fgi4Hvg)

