FROM python:3.12

COPY . /api
WORKDIR /api

RUN pip install -r requirements.txt

EXPOSE 1777

#
CMD ["uvicorn", "main:app",  "--host", "0.0.0.0", "--port", "1777"]