FROM python:3.7-slim

RUN apt-get update
# set work directory
WORKDIR /usr/src/wedding_shop


# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt


ADD tws /usr/src/wedding_shop/tws
ADD The_Wedding_Shop /usr/src/wedding_shop/The_Wedding_Shop
COPY ./manage.py .
COPY ./product.json /usr/src/wedding_shop/product.json
#COPY ./data /usr/src/wedding_shop/data
# copy entrypoint.sh
COPY entrypoint.sh /usr/src/wedding_shop/entrypoint.sh
RUN chmod +x /usr/src/wedding_shop/entrypoint.sh
# run entrypoint.sh
ENTRYPOINT ["/usr/src/wedding_shop/entrypoint.sh"]
