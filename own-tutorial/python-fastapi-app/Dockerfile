FROM python:3.9

WORKDIR /code


RUN pip install --no-cache-dir --upgrade poetry


COPY ./app /code/app

WORKDIR /code/app

RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-root 

CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0"]
