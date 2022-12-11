# README

deploy command

```shell
gcloud functions deploy function --gen2 --runtime=python310 --region=asia-northeast1 --source=. --entry-point=main --trigger-topic=event-name --allow-unauthenticated --env-vars-file .env.yaml
```
