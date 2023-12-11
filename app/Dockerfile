FROM midnighter/fastapi-base:3.10-slim-bullseye_2023-06-27_f263ffa 

COPY ./ ./

WORKDIR ./

CMD ["uvicorn", "main:app --port 80 --host 0.0.0.0 --reload"]

