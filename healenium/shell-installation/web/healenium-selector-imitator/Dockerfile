FROM python:3.7-slim-stretch

COPY ./requirements.txt ./requirements.txt
COPY ./dist ./

RUN pip install -r requirements.txt

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]