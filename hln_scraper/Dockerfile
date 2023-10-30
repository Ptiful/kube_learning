FROM python:3.11
RUN mkdir /hln_scraper
COPY . /hln_scraper
WORKDIR /hln_scraper
RUN pip install -r requirements.txt
CMD [ "python", "hln_articles.py"]