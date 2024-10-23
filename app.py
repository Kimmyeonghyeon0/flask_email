from flask import Flask, render_template, url_for, request, redirect #url_for 추가
from flask_mail import Mail, Message

app = Flask(__name__)

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = "audguss00915@gmail.com"
app.config["MAIL_PASSWORD"] = "ncygpmupdvyraabs"
app.config["MAIL_DEFAULT_SENDER"] = "audguss00915@gmail.com"

mail = Mail(app)

@app.route("/")
def hello():
    return print("oz hello")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/contact/complete", methods=("GET", "POST"))
def contact_complete():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        send_email(email, "문의해주셔서 감사합니다.", "contact_mail", name=name, message=message)

        return redirect(url_for("contact_complete"))    #url_for("contact_complete")->/contact/complete
    
    return render_template("contact_complete.html")


def send_email(to, subject, template, **kwargs):

    msg = Message(subject, recipients=[to])
    msg.body = render_template(template + ".txt", **kwargs)
    msg.html = render_template(template + ".html", **kwargs)
    msg.charset = 'utf-8'
    mail.send(msg)
