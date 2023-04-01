FROM python
ENV PYTHONUNBUFFERED 1
WORKDIR .
COPY . /
EXPOSE 8000
RUN pip install -r requirements.txt