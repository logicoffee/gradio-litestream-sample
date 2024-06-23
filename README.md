# Gradio Litestream Sample

Todo application sample built with Gradio and Litestream.

## Prerequisites

- Create a GCS Bucket.
- Rewrite the replica url in `litestream.yml`.

## Runnig locally

- Authenticate gcloud with `gcloud auth application-default login`.
- Run `docker compose up --build`
- Access localhost:7860

## Deploy to Cloud Run

```bash
gcloud run deploy your-service-name \
    --port 7860 \
    --allow-unauthenticated \
    --region your-region \
    --source .
```
