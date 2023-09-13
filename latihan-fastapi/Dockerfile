# 
FROM python:3.8

#
USER root

#
ENV PYTHONUNBUFFERED 1

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# #
RUN apt-get update

# # 
RUN pip install -r /code/requirements.txt

# # 
RUN apt-get install python3-tk -y

# # 
COPY ./api /code/app

# # 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]