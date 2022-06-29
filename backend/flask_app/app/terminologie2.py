from flask import Blueprint, jsonify
from model import app, Terminologie
import random

app.config["JSON_AS_ASCII"] = False

terminologie_module = Blueprint("terminologie_module", __name__)
terminologie_module2 = Blueprint("terminologie_module2", __name__)
# create_module = Blueprint("create_module", __name__, template_folder="templates")
# update_module = Blueprint("update_module", __name__, template_folder="templates")
# delete_module = Blueprint("delete_module", __name__)

# 用語全てからランダムで問題をJSONで取得
@terminologie_module2.route("/terminologie2", methods=["GET"])
def terms():
    terms = Terminologie.query.all()
    data = [
        {
            "terminologie_id": i.terminologie_id,
            "genre_id": i.genre_id,
            "theme_jp": i.theme_jp,
            "theme_ro": i.theme_ro,
            "description_ja": i.description_ja,
            "description_ro": i.description_ro
        }
        for i in terms
    ]
    return(random.choice(data))
        

