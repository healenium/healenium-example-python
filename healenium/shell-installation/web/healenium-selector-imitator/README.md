# Healenium selector imitator

Selector imitator tries to reconstruct a user selector, changing only fields that the user modified in HTML. It works with the original selector (and its type) and target node (so it should be applied after the best node is already found). It proposes possible healed selectors or raises an error.  
Proposed selectors are not guaranteed to find a unique web element. Uniqueness must be checked outside of the service with a selenium driver.  

1. [Example request and response](#example)
2. [Image and container resources consumption](#resources)
3. [Installation with Docker](#installation)
4. [Creating your own image from Dockerfile](#image)
5. [Local testing](#testing)

### <a name="example">Example request and response</a>

Here is an example request. You can try out different requests with Swagger after the [installation](#installation).
![image](https://user-images.githubusercontent.com/40484210/127833016-10da747f-ae4d-480f-9624-ec1266cbbb25.png)
![image](https://user-images.githubusercontent.com/40484210/127833088-59eeced9-17c3-4b60-b1ee-f97d4421ff33.png)


### <a name="resources">Image and container resources consumption</a>
![image](https://user-images.githubusercontent.com/40484210/123598005-b7c7ff00-d7fc-11eb-9be6-fa20c181bb47.png)  
![image](https://user-images.githubusercontent.com/40484210/123598058-c3b3c100-d7fc-11eb-85d9-380bacd53d6a.png)


### <a name="installation">Installation with Docker</a>
Run the following command to install and use Healenium selector imitator as a stand-alone service (you'll need docker installed):
```
docker compose up
```
Now you can access an API at http://localhost:8000/  
Check http://localhost:8000/docs for Swagger documentation.

### <a name="image">Creating your own image from Dockerfile</a>
If you wish to make some changes to the code and test them in Docker environment, you will need to create an image.
Run these commands from the repository directory, change the version if needed (you'll need docker and pyarmor installed):
```
pyarmor obfuscate --platform linux.x86_64.7 --recursive --output dist/src src/__init__.py
pyarmor obfuscate --platform linux.x86_64.7 --exact app.py
docker build -t healenium/hlm-selector-imitator:1 .
docker run -d -p 8000:8000 healenium/hlm-selector-imitator:1
```

### <a name="testing">Local testing</a>
To test or lint locally, create a virtual environment with Pyhton 3.7 and install packages from requirements_dev.txt  

Test with [pytest](https://docs.pytest.org/en/6.2.x/):
```
pytest
```

Get [coverage](https://coverage.readthedocs.io/en/coverage-5.5/#) report:
```
coverage run -m pytest
coverage report -m
coverage html
```

Check types with [mypy](https://mypy.readthedocs.io/en/stable/):
```
mypy src app.py
```

Lint with [flake8](https://flake8.pycqa.org/en/latest/):
```
flake8
```

Format code with [black](https://github.com/psf/black):
```
black .
```
