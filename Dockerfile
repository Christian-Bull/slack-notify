# use official python as parent image
FROM python:3.7-alpine

# sets working directory
WORKDIR /usr/src/app

COPY requirements.txt ./

# installs requirements
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python","./main.py"]
