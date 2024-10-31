from flask import Flask

app = Flask(__name__)


@app.route('/imagedottxt')
def main_site():
    return "*SITE WHERE USER WILL PASS IMAGE (all formats) TO CONVERT*"


@app.route('/imagedottxt/success')
def success_site():
    return "*SITE WHERE USER COULD READ, SAVE (.docx) OR COPY CONVERTED IMAGE TO TEXT*"


@app.route('/imagedottxt/fail')
def fail_site():
    return "*SITE WHERE USER WILL SEE FAILED ATTEMPT TO CONVERT IMAGE TO TEXT (REASON)*"
