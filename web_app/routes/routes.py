from flask import Blueprint, render_template, redirect, request, flash
routes = Blueprint("routes", __name__)


@routes.route("/")
def home():
    print("VISITED THE HOME PAGE")
    return render_template("home.html")