from flask import Blueprint, request, jsonify
from model import Result, app

import datetime

JST = datetime.timezone(datetime.timedelta(hours=+9))

app.config['JSON_AS_ASCII'] = False

record_module = Blueprint("record_module", __name__,url_prefix="/record")


#直近の5日分出力
@record_module.route("/<user_id>",methods=["POST"])
def get_my_result(user_id):
        payload = request.json
        insert_data = Result(
            user_id = payload.get("user_id"),
            accuracy_value = payload.get("accuracy_value"),
            wpm = payload.get("wpm"),
            played_at_date = payload.get("played_at_date"))
        
        users = Result.query.filter_by(user_id=insert_data.user_id).all()
        my_data = [
            {
                "user_name":i.users.user_name,
                "user_id":i.user_id,
                "accuracy_value":i.accuracy_value,
                "wpm":i.wpm,
                "played_at_date":i.played_at_date
            }
            for i in users
        ]
        return jsonify(sorted(my_data, key=lambda x: x['played_at_date'],reverse=True)[0:5])