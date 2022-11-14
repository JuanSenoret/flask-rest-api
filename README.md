# service-gateway-showcase
Service to route traffic to internal solution.

Table of contents
=================
  * [Development](#development)
    * [Run locally](#run-locally)
    * [Run as container](#run-as-container)
    * [Build](#build)
    * [Deploy](#deploy)
  * [Configuration](#configuration)
  * [Contributing](#contributing)
  * [References](#references)



## Development    
### Run locally

1. Starting service locally with pipenv and python.
```
pipenv run python -m uvicorn main:app --reload
```

### Run as container
1. Build the container image:
```
podman build -t service-gateway . 
```

2. Check that the contaier image has been created:
```
podman images
```
3. Run the container image (for mounting ca file and setting env variables):
```
podman run --name service-gateway -p 8001:8000 service-gateway:latest
```

### Build
Build final container image:
```

```
### Deploy
1. Build docker image with a specific versioning tag (e.g. 'v0.5.5-beta')
2. Push docker image to the registry
3. Update versioning tag in Helm Config files 
4. When deploying it as new service use helm install, when an older version already exists use helm upgrade to deploy the image. 
```

```
The ./service-gateway should point to the config directory of the service in local config repo.

## Configuration

Note: ensure that no single quotes are used for the values.

## Contributing
1. Create your Feature Branch (`git checkout -b feature/<...>`)
2. Install packages from Pipfile (`pipenv install`)
3. Commit your Changes (`git commit -m 'Added xyz.'`)
4. Ensure that your pylint score is 10 (`python -m pylint src.main.py`)
5. Push to the Branch (`git push`)
6. Open a Merge Request
## References
* [Uvicorn](https://www.uvicorn.org)
