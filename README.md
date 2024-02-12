# Rag

```python
python3.11 -m venv env
source menv/bin/activate
```

## Build and push image

```command
docker build --tag username/image:tag .

docker push username/image:tag
```

<!--
export PLATFORM=linux/amd64
-->

## Test server

```command
python3 src/handler.py --rp_serve_api
```

## Test locally

```command
python3 src/handler.py --test_input '{"input": {"prompt": "What is RunPod"}}'
```