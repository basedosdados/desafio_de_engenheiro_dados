# Pull official base image
FROM python:3.9-buster

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN apt update -y
RUN apt install ftp -y
# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Set working directory and copy python scripts
RUN mkdir /scripts
WORKDIR /scripts
COPY . ./

CMD ["prefect", "run", "-p", "flows.py"]
