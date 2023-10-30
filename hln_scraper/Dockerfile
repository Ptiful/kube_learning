FROM python:3.11
RUN mkdir /hln_scraper
COPY . /hln_scrape
WORKDIR /hln_scrape
RUN pip install -r requirements.txt
CMD [ "python", "hln_articles.py"]