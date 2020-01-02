from flask import Blueprint

account = Blueprint("account", __name__)


@account.route("/page")
def load_page():
    return "load account page"


@account.route("/list")
def load_list():
    # query_property = dBSession.query(StatementStatementAccount).all()
    # print(query_property)
    return "load account list"


@account.route("/detail")
def load_detail():
    return "load account detail"
