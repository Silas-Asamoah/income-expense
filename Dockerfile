# Using lightweight alpine image
FROM python:3.6-alpine

# Installing packages
RUN apk update

# Defining working directory and adding source code
WORKDIR /usr/src/app
COPY bootstrap.sh ./
COPY cashman ./cashman

# Install API dependencies
RUN pip install flask --user
RUN pip install marshmallow --user

# Start app
EXPOSE 5000
ENTRYPOINT ["/usr/src/app/bootstrap.sh"]