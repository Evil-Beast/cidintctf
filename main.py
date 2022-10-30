from flask import Flask, render_template
app = Flask(__name__)

#uvicorn main:app --host 192.168.18.244

@app.route("/VjFod1QxUXlUak5RVkRBOQ==/<p>")
def login(p):
    return render_template('k.html')

@app.route("/L1ZqRm9kMVF4VVhsVWFrNVJWa1JCT1E9PS97cGFzc3dvcmR9/")
def closeDoor():
    return render_template('look.html')

#pip freeze > to-uninstall.txt
#pip uninstall -r to-uninstall.txt

if __name__ == '__main__':
    app.run()
