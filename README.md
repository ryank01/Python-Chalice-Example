# Python-Chalice-Example
A simple publishing service utilizing Python-chalice

## Run application
```
   clone repo
   cd into adx-research/adx
   source bin/activate
   pip install -r requirements.txt
   chalice local
```

## Endpoints and Interface
This application consists of three endpoints one of which has a simple UI \
NOTE: ```/index``` renders a time series graph \
These endpoints are:
```
  /index 
  /upload
  /response-status
```

### Requesting Endpoints
Request ```/upload and /response-status``` using curl \
```/index``` can be requested through any browser since it renders a ui

### /index
Example: \
```http://127.0.0.1:8000/index/AAPL``` \
AAPL can be replaced with any valid stock ticker \
Response: \
   https://github.com/ryank01/Python-Chalice-Example/issues/1#issue-405874557
  
