FROM python:3.9.2-slim-buster

WORKDIR /usr/src/app

LABEL description="Development image for peatdash tutorial"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get -y install netcat gcc postgresql \
    && apt-get clean

RUN apt-get update \
    && apt-get install -y binutils libproj-dev gdal-bin python-gdal python3-gdal   

# RUN apt-get install xz-utils
# RUN apt-get -y install curl

# RUN curl https://nodejs.org/dist/v14.15.4/node-v14.15.4-linux-x64.tar.xz -O

# Extract & install
# RUN tar -xf node-v14.15.4-linux-x64.tar.xz
# RUN ln -s /node-v14.15.4-linux-x64/bin/node /usr/local/bin/node
# RUN ln -s /node-v14.15.4-linux-x64/bin/npm /usr/local/bin/npm
# RUN ln -s /node-v14.15.4-linux-x64/bin/npx /usr/local/bin/npx
# RUN apt-get install -y npm

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt


COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["sh", "/usr/src/app/entrypoint.sh"]