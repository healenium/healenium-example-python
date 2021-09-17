# healenium
Python 3.9.5 + Pytest project with healenium usage example 

## How to start
### 1.Start Healenium backend from 'infra' folder

```cd infra```

```docker-compose up -d```

Verify that images ```healenium/hlm-backend:3.1.2```, ```postgres:11-alpine```, ```healenium/hlm-selector-imitator:1```, ```healenium/hlm-selenium-4-standalone-xpra``` and ```healenium/hlm-proxy``` are up and running

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