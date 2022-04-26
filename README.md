# healenium
Python 3.9.5 + Pytest project with healenium usage example 

## How to start
### 1.Start Healenium backend from 'root' folder

```docker-compose up -d```

To download this file into your project use this command:

```$ curl https://raw.githubusercontent.com/healenium/healenium-example-python/master/infra/docker-compose.yml -o docker-compose.yml```

Create /db/sql folder on the same level in your project. Add init.sql file into ```./db/sql/init.sql``` folder in your project via command:

```$ curl https://raw.githubusercontent.com/healenium/healenium-client/master/example/init.sql -o init.sql```

Verify that images ```healenium/hlm-backend:3.2.1```, ```postgres:11-alpine```, ```healenium/hlm-selector-imitator:1.1```, ```healenium/hlm-proxy``` are up and running

### 2. Project structure
```
|__healenium-example-python (root)
	|__src
        |__main
            |__constants
            |__pages
            |__search
    |__tests
        |__selenium tests
    |__docker-compose.yml

``` 
			   
### 3.Run test
To run tests in terminal with pytest you need to go to execute next comands:

``python3 -m venv env``

``source ./env/bin/activate``

``python -m pip install -U pytest``

``python -m pip install -U selenium``

``python -m pytest ./tests/``

> If you want to execute tests from specified file, please use the command: ```python -m pytest ./tests/test_css.py```
>> In case you want to run all tests in project use ```python -m pytest ./tests/``` command

### 4. Monitoring tests running
You can monitor tests running. To do this go to ```http://<remote webdriver host>:8086```
