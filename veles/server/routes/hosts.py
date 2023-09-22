from flask import Blueprint, request

from server.db import get_db

hosts_blueprint = Blueprint("hosts", __name__, url_prefix="/hosts")

def dict_from_row(row_list):
    l = []
    for row in row_list:
        l.append(dict(zip(row.keys(), row)))
    return l 

@hosts_blueprint.route("/getall")
def getall():
    db = get_db()
    hosts = db.execute("SELECT * FROM hosts").fetchall()
    return dict_from_row(hosts)
