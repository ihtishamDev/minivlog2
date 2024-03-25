import datetime
from flask import Flask, render_template , request
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    clint = MongoClient(os.getenv("MONGODB_URI"))
    app.db = clint.miniblog

    # entries = []

    @app.route("/", methods = ["GET" , "POST"])
    def hello_world():
        # print([e for e in app.db.entries.find({})])
        if request.method == "POST":
            entry_content = request.form.get("content")
            formatted_date =  datetime.datetime.today().strftime("%y-%m-%d")
            # entry_content = (entry_content , formatted_date)
            # entries.append((entry_content , formatted_date))
            app.db.entries.insert_one({"content": entry_content , "date": formatted_date})
            # print(entries )

        entries_with_date =[ 
        (
            entry["content"],
            entry["date"],
            datetime.datetime.strptime(entry["date"], "%y-%m-%d").strftime("%b %d")
        )
        for entry in app.db.entries.find({})
        ]

        return render_template("home.html", entries=entries_with_date)

    if __name__ == "__main__":""
    app.run(debug=True) 
 
    return app