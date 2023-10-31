# Initial setup: configure doctl
```
doctl auth init
doctl registry login
```

# Build the app
The images are built automatically when pushed to master, but they can be
pushed manually as well:
```
docker build -t registry.digitalocean.com/rs-general/ai-prod-demo .
docker push registry.digitalocean.com/rs-general/fastapi

docker build -f streamlit.Dockerfile -t registry.digitalocean.com/rs-general/prod-demo-ui .
docker push registry.digitalocean.com/rs-general/prod-demo-ui
```

Deploy the backend and the UI
```
# Backend: FastAPI, Huggingface
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

# UI: Streamlit
kubectl apply -f ui-deployment.yaml
kubectl apply -f ui-service.yaml
```

