# Use an official Python runtime as a parent image
FROM python:3.6.0

# Install Node and yarn
RUN apt-get update
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - \
	&& apt-get install -y nodejs

RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \
  && echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list \
  && apt-get update \
  && apt-get install -y yarn

RUN mkdir /code
WORKDIR /code

# Install app dependencies 
ADD requirements.txt ./
RUN pip install -r requirements.txt

COPY package.json yarn.lock ./
RUN yarn install && yarn global add nodemon

# Copy app code
ADD . /code
CMD ./run