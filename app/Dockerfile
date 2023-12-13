FROM docker.io/midnighter/fastapi-base:3.10-slim-bullseye_2023-06-27_f263ffa 

COPY ./ /app/

WORKDIR /app/
ENTRYPOINT ["uvicorn", "main:app"]
CMD ["--port=80", "--host=0.0.0.0" ,"--reload"]

