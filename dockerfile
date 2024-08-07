FROM python:3.11

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

EXPOSE 8501

CMD ["streamlit" , "run", "app/main.py", "--server.port=8501", "--server.address=0.0.0.0"]