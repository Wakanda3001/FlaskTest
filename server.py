import config
from flask import render_template

# connexion setup
connex_app = config.connex_app
connex_app.add_api("swagger.yml")


@connex_app.route("/")
def home():
    return render_template("home.html")


connex_app.run(debug=True)