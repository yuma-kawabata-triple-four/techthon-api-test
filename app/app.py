import time
from http import HTTPStatus
from typing import Optional

from flask import *

app = Flask(__name__)


# =========================== function ===========================
def create_response_base(status_code: int, method_name: str) -> dict:
    return {
        "status_code": status_code,
        "method": method_name,
    }

def create_http_response(status_code: int):
    HTTP_STAUTS = HTTPStatus(status_code)
    return Response(
        f"{status_code} {HTTP_STAUTS.phrase}",
        status=status_code,
    )


# =========================== hello world ===========================
@app.route("/", methods=['GET'])
def hello():
    return "Hello World!"


# =========================== Check Methods ===========================
@app.route("/check", methods=['GET'])
def check_get():
    return create_response_base(200, "GET")

@app.route("/check", methods=['POST'])
def check_post():
    return create_response_base(200, "POST")

@app.route("/check", methods=['PUT'])
def check_put():
    return create_response_base(200, "PUT")

@app.route("/check", methods=['DELETE'])
def check_delete():
    return create_response_base(200, "DELETE")
    
    
# =========================== Check Https ===========================
@app.route("/check/http/<int:status_code>", methods=['GET'])
def ret_http_status(status_code):
    return create_http_response(status_code)


# =========================== Check huge response ===========================
@app.route("/check/huge", methods=['GET'])
def ret_huge_str():
    return "10万文字返却します" * 10000

# =========================== Check req case ===========================
@app.route("/check/req/<int:case>", methods=['GET'])
def check_req_case(case):
    print(f"case {case}: start!")
    response = create_response_base(200, "GET")
    response['case'] = case
    response['exec_time'] = 0
    print(f"case {case}: finished!")
    return response

@app.route("/check/req/<int:case>/sleep/<int:second>", methods=['GET'])
def check_req_case_with_sleep(case, second):
    print(f"case {case}")
    print(f"case {case}: {second} seconds sleeping...")
    time.sleep(second)

    response = create_response_base(200, "GET")
    response['case'] = case
    response['exec_time'] = second
    print(f"case {case}: finished!")
    return response


if __name__ == '__main__':
    app.run(host="0.0.0.0")
