# README

deploy command

```shell
gcloud functions deploy yaogin-daily --gen2 --runtime=python310 --region=asia-northeast1 --source=. --entry-point=main --trigger-topic=yaogin --allow-unauthenticated --env-vars-file .env.yaml  
```
