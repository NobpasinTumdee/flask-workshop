from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")  # เมื่อเปิดเว็บที่ /
def home():
    return render_template("index.html")  # แสดงหน้า index.html

if __name__ == "__main__":
    app.run(debug=True)
