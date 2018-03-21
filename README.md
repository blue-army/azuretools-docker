# azuretools-docker
A docker image with with the Azure libraries

`pip install azure-storage-blob && pip freeze > requirements.txt`

## Build / Publish

```bash
docker build -t nullreference/azuretools .

docker run -it --rm nullreference/azuretools
```

`docker run --mount type=bind,source="$(pwd)",target=/work nullreference/azuretools junk.py`