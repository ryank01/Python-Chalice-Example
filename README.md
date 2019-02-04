# Python-Chalice-Example
A simple publishing service utilizing Python-chalice

## Run application
```
   git clone git@github.com:ryank01/Python-Chalice-Example.git
   cd into adx-research/adx
   source bin/activate
   pip install -r requirements.txt
   chalice local
```

## Endpoints and Interface
This application consists of three endpoints one of which has a simple UI \

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
This endpoint renders a time series graph in the browser \
Example: \
Visit ```http://127.0.0.1:8000/index/AAPL```  in any browser \
AAPL can be replaced with any valid stock ticker \
Response: \
   https://github.com/ryank01/Python-Chalice-Example/issues/1#issue-405874557
  
### /upload
This endpoint allows an upload of a png image to s3 and \
generates a url. You can then visit the genrated url to \
view the uploaded image. \
Example:
```
   curl -X POST \
-H 'Content-Type: application/x-www-form-urlencoded' \
--data-binary @'</absolute/path/to/file>' \
localhost:8000/upload

```
Response:
```
   https://s3-us-west-2.amazonaws.com/chalice-app/BBDL8CW56L.png
```
Open the generated url in any browser to see the png image 

### /response-status
This endpoint returns a simple json object 

Example: \
Visit in browser or use curl
```
   http://127.0.0.1:8000/response-status
```
Response:
```
   {
"message": "success",
"status_code": 200
}
```

# NOTES
If you do not want to run this application locally, there's an option to \
go directly to the prod REST API url. \
The url is 
```
`https://87xysrymzi.execute-api.us-west-2.amazonaws.com/api/<insert-any-one-of-the-three-endpoints>

```
