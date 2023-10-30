```
uvicorn prod_demo.main:app --reload

curl --get "http://127.0.0.1:8000/complete_text/" --data-urlencode "prompt=Python is "

docker build -t prod-demo .
docker tag prod-demo registry.digitalocean.com/ai-prod-demo/fastapi
docker push registry.digitalocean.com/ai-prod-demo/fastapi

kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

curl --get "164.90.243.52:80/complete_text/" --data-urlencode "prompt=Hi, my name is"
```
