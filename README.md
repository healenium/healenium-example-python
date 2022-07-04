# healenium
Python 3.9.5 + Pytest project with healenium usage example 

## How to start
### 1.Start Healenium backend from 'root' folder
```cd infra``` </br></br>
To work with Healenium and Selenoid plus Selenoid Ui, use:</br>
<pre>
    <b>docker-compose up -d</b>

    To download docker-compose.yaml file into your project use this command:

    <b>$ curl https://raw.githubusercontent.com/healenium/healenium-example-python/master/infra/docker-compose.yaml -o docker-compose.yaml</b>

    Additionally downlod browsers.json file into you project use this command:

    <b>curl https://raw.githubusercontent.com/healenium/healenium-example-python/master/infra/browsers.json -o browsers.json</b>

    Manually pull docker images with specific versions from browsers.json:

    <b>docker pull selenoid/vnc:chrome_102.0</b>
    <b>docker pull selenoid/vnc:chrome_101.0</b>
    <b>docker pull selenoid/vnc:firefox_101.0</b>
    <b>docker pull selenoid/vnc:chrome_100.0</b>
</pre>
To work with Healenium and standard Selenium hub with nodes, use:</br>
<pre>
    <b>docker-compose -f docker-compose-selenium-v3.yaml up -d</b>

    To download docker-compose-selenium-v3.yaml file into your project use this command:

    <b>$ curl https://raw.githubusercontent.com/healenium/healenium-example-python/master/infra/docker-compose-selenium-v3.yaml -o docker-compose-selenium-v3.yaml</b>
</pre>

Create <b>/db/sql</b> folder on the same level in your project.</br>
<pre>
    Add init.sql file into ./db/sql/init.sql folder in your project via command:

    <b>$ curl https://raw.githubusercontent.com/healenium/healenium/master/db/sql/init.sql -o init.sql</b>
</pre>
Verify the next images are <b>Up</b> and <b>Running</b>
<pre>
    * postgres:14.2-bullseye
    * healenium/hlm-backend:3.2.3
    * healenium/hlm-selector-imitator:1.1
    * healenium/hlm-proxy:1.0.0
    * healenium/hlm-selenoid:0.1.0
    * aerokube/selenoid-ui:1.10.5
</pre>

### 2. Project structure
```
|__healenium-example-python (root)
    |__infra
        |__db
            |__sql
                |__init.sql
        |__docker-compose.yaml
        |__docker-compose-selenium-v3.yaml
	|__src
            |__main
                |__constants
                |__pages
                |__search
    |__tests
        |__test_css.py
        |__test_general.py
        |__test_parent_child.py
        |__test_semantic.py
        |__test_wait.py
        |__test_xpath.py

```
			   
### 3.Run test
To run tests in terminal with pytest you need to go to execute next commands:

``python3 -m venv env``

``source ./env/bin/activate``

``python -m pip install -U pytest``

``python -m pip install -U selenium``

``python -m pytest ./tests/``

> If you want to execute tests from specified file, please use the command: ```python -m pytest ./tests/test_css.py```
>> In case you want to run all tests in project use ```python -m pytest ./tests/``` command

### 4. Monitoring tests running
You can monitor tests running if you using Healenium with Selenoid plus Selenoid Ui, use:</br>
<pre>
    go to <b>http://localhost:8080</b>
</pre>
