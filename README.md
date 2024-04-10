# fastapi-learn

## Build && Run

### Build

```bash
bash ./run.sh build
```

### Run

```bash
bash ./run.sh dev
bash ./run.sh stage
bash ./run.sh prod
```

## Docker

### Docker build

```bash
docker build -t fastapi-learn .
```

### Docker start

```bash
docker run -d -p 3000:3000 --name fastapi-learn fastapi-learn
```
