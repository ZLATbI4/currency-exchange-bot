FROM python:3.8

ENV TELEGRAM_API_TOKEN=""

RUN mkdir -p usr/src/app/
WORKDIR /usr/src/app/
COPY . /usr/src/app/
ENV TZ=Europe/Kiev
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "bot.py"]