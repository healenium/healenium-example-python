# healenium
Python 3.9.5 + Pytest project with healenium usage example 

## How to start
### 1.Start Healenium backend from 'infra' folder

```cd infra```

```docker-compose up -d```

To download this file into your project use this command:

```$ curl https://raw.githubusercontent.com/healenium/healenium-example-python/master/infra/docker-compose.yml -o docker-compose.yml```

Create /db/sql folder on the same level in your project. Add init.sql file into ```./db/sql/init.sql``` folder in your project via command:

```$ curl https://raw.githubusercontent.com/healenium/healenium-client/master/example/init.sql -o init.sql```

Verify that images ```healenium/hlm-backend:3.2.0```, ```postgres:11-alpine```, ```healenium/hlm-selector-imitator```, ```healenium/hlm-selenium-4-standalone-xpra``` and ```healenium/hlm-proxy:0.2.1``` are up and running

### 2. Project structure
```
|__healenium-example-python (root)
	|__src
        |__main
            |__locators
            |__pages
    |__tests
        |__selenium tests
   |__infra
      |__docker-compose.yml

``` 
			   
### 3.Run test
To run tests in terminal with pytest you need to go to ```cd healenium_selenium\tests``` project folder

> If you want to execute tests from test_callback.py file, please use the command: ```pytest test_callback.py```
> And appropriate command for test_markup.py file: ```pytest test_markup.py```
>> In case you want to run all tests in project use ```pytest``` command

### 4. Monitoring tests running
You can monitor tests running. To do this go to ```http://<remote webdriver host>:8086```
