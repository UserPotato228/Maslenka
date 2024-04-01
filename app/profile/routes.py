# import blueprint
from app.profile import bp
# flask modules
from flask import render_template


@bp.route("/profile")
def profile():
    return "profile"
