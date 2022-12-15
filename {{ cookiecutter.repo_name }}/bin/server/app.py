#!/usr/local/bin/python3
from os import environ
import threading
import enum
from typing import Any, Dict, Tuple
from dotenv import load_dotenv
import datetime as dt
import pandas as pd
import numpy as np

from wsgiref import validate
from flask import Flask, request
from flask_cors import CORS
from flask_restx import Api, Resource, fields
from dotenv import load_dotenv
from {{ cookiecutter.python_package }}.helper import {{ cookiecutter.ApplicationHelper }}

load_dotenv()


today = dt.date.today()

api = Api()
app = Flask(__name__)

CORS(app)
api.init_app(app)

helper = {{ cookiecutter.ApplicationHelper }}()

""" NB:
    app.py is responsible only for:
    1. getting parameters from the request body/path
    2. call the controller functions
    3. return responses
"""


class ReturnCode(enum.Enum):
    OK = 200
    BAD_REQUEST = 400
    INTERNAL_SERVER_ERROR = 500


responses = {200: "Success", 400: "Bad Request", 500: "Internal Server Error"}


def init(req: request) -> Tuple[Dict, ReturnCode, Dict]:
    data = req.get_json() if request.method == "POST" else {}
    return {}, ReturnCode.INTERNAL_SERVER_ERROR, data


def out(res: Any, code: ReturnCode):
    if code == ReturnCode.INTERNAL_SERVER_ERROR:
        print(res)
    return res, code.value


prj_ns = api.namespace(
    "Project", description="Project miscellaneous APIs", ordered=True
)


@prj_ns.route("/GetProjectDetails")
class ProjectDetails(Resource):
    @prj_ns.doc(responses=responses)
    def get(self):
        res, code, _ = init(request)
        res = helper.get_project_tree(project=helper._prj)
        if res != {}:
            code = ReturnCode.OK
        return out(res, code)


@prj_ns.route("/CreateUpdateData")
class CreateUpdateData(Resource):
    request_model = api.model(
        "CreateUpdateDataRequest",
        {
            "resource_keys": fields.List(fields.String),
            "main_action": fields.String(
                default="create", description="'create' or 'update'"
            ),
        },
    )

    @prj_ns.expect(request_model)
    @prj_ns.doc(responses=responses)
    def post(self):
        res, code, data = init(request)
        try:
            res = helper.create_update_data("ts", data)
            if res:
                code = ReturnCode.OK
        except Exception as e:
            res = str(e)
        return out(res, code)


resource_key_opt_args = {
    "required": True,
    "description": "Name of the resource on which build the model",
}

if __name__ == "__main__":
    host = environ["HOST"]
    port = environ["PORT"]
    print(f"Host: {host}")
    print(f"port: {port}")
    app.run(host, port)
