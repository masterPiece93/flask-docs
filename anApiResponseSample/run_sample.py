"""Denonstration
This is a demonstration of using `JsonApiResponse` in Flask
"""
from flask import Flask, request
from response import JsonApiResponse

app = Flask(__name__)

def api_controller(request_obj, **path_params):
    response = JsonApiResponse()

    # ... API logic ...

    response.http_status_code = 400
    response.message = "some readable text"
    response.code = "SOME_SECRET_CLIENT_DEFINED_CODE"
    response.data = [
        {
            "key": "value"
        },
        {
            "key": "value"
        },
        {
            "key": "value"
        },
    ]

    return response

def pagination_logic(request, response):
    page = response.page
    page.current = 1
    page.next = 2
    page.total = ...
    page.link["next"] = None


@app.route('/test-api/<path_param_1>/', methods=['GET','PUT', 'POST'])
def api_name(path_param_1: str):
    response = api_controller(request, **{"path_param_1":path_param_1})
    pagination_logic(request, response)
    return response.make(paginated=True)
    
if __name__ == '__main__':
    app.run()