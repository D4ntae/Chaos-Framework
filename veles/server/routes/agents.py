from flask import Blueprint, request, jsonify, abort
import json

from server.db import get_db

agents_blueprint = Blueprint("agents", __name__, url_prefix="/agents")

def get_null_index(req_body):
    i = 0
    while req_body[i] != 0:
        i += 1
    return i

def dict_from_row_single(row):
    return dict(zip(row.keys(), row))

def dict_from_row(row_list):
    l = []
    for row in row_list:
        l.append(dict(zip(row.keys(), row)))
    return l 

@agents_blueprint.route("/register", methods=("GET", "POST"))
def register():
    if request.method == "POST":
        req = request.data[0:get_null_index(request.data)].decode("utf8")
        print(req)
        print(request.data[0:get_null_index(request.data)])
        data = json.loads(req[0:len(req)])
        hostname = data["hostname"]
        os = data["os"]
        arch = data["arch"]
        proc_name = data["procName"]
        pid = data["pid"]
        agent_type = data["type"]
        db = get_db()

        try:
            db.execute("INSERT INTO agents(agentType, arch, os, hostname, pid, procName) VALUES (?, ?, ?, ?, ?, ?)", (agent_type, arch, os, hostname, pid, proc_name))
            db.commit()
        except db.IntegrityError:
            print("Host already exists")

        return "Success"

    else:
        return "Use POST on this route"

@agents_blueprint.route("/getall")
def getall():
    db = get_db()
    agents = db.execute("SELECT * FROM agents").fetchall()
    response = jsonify(dict_from_row(agents))
    response.headers.add("Access-Control-Allow-Origin", "*") 
    return response

@agents_blueprint.route("/agent/<int:id>")
def agentById(id):
    db = get_db()
    try:
        agent = db.execute("SELECT * FROM agents WHERE id = ?", (id,)).fetchall()[0]
    except Exception:
        return abort(404) 
    response = jsonify(dict_from_row_single(agent))
    response.headers.add("Access-Control-Allow-Origin", "*") 
    return response
