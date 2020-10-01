# Build and Run Docker image locally

## Docker build

```
docker build -t streamlit-webapp1 .
```

## Docker run

```
docker run -p 8080:8080 streamlit-webapp1
```

# Deploy to GCP App Engine

### Create Project:

```
gcloud projects create <project_id>

```

### Set default project:
```
gcloud config set project <project_id>

```

Initialize App engine App:
```
gcloud app create --project=<project_id>

```

Deploy:
```
gcloud app deploy

```

# Access control with `Identity-Aware Proxy`

https://cloud.google.com/iap/docs/app-engine-quickstart




