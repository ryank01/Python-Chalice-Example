from chalice import Chalice, Response, IAMAuthorizer
import requests
import os
import jinja2
import boto3
import random
import string

app = Chalice(app_name='adx')

def render(tpl_path, context):
    path, filename = os.path.split(tpl_path)
    return jinja2.Environment(loader=jinja2.FileSystemLoader(path or "./")).get_template(filename).render(context)

@app.route('/index/{params}', methods=['GET'], cors=True)
def index(params):
    response = requests.get("https://www.alphavantage.co/query?function=ADX&symbol={}&interval=daily&time_period=10&apikey=K87BB8H31SVY3OBA".format(params))
    data = response.json()
    time_interval = []
    index_rating = []
    my_dict = {}
    legend = "ADX graph"

    for k, v in data['Technical Analysis: ADX'].items():
        time_interval.append(k)
        index_rating.append(float(v['ADX']))
        my_dict[k] = v['ADX']

    current_adx = index_rating[0]
    max_adx = max(index_rating)
    min_adx = min(index_rating)


    context = {
            "time_interval":time_interval,
            "index_rating":index_rating,
            "legend":legend,
            "current_adx":current_adx,
            "max_adx":max_adx,
            "min_adx":min_adx
        }
    template = render("chalicelib/templates/chart.html", context)
    return Response(template, status_code=200, headers={
        "Content-Type": "text/html",
        "Access-Control-Allow-Origin": "*"
    })


@app.route('/upload', methods=['POST'], content_types=['application/x-www-form-urlencoded'])
def upload():
    image_data = app.current_request.raw_body

    s3 = boto3.client('s3')
    s3_bucket = 'chalice-app'

    file_name = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(10))+'.png'

    
    s3.put_object(
            ACL = 'public-read',
            Body = image_data,
            Bucket = s3_bucket,
            Key = file_name,
            ContentType = 'image/png'
        )

    image_location = 'https://s3-us-west-2.amazonaws.com/{}/{}'.format(s3_bucket, file_name)

    return {'image-location': image_location}



# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
