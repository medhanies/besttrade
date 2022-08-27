# this the entry point of the application
# this file will create a new web application and if executed directly (i.e, the interpreter assigns __main__ value to __name__)) the application will start
# this where we would register all the blueprints for the resources that we'll be creating:
# 1) investor resource, 2) account resource, 3) portfolio resource
from crypt import methods
from http import HTTPStatus
from flask import Flask, render_template
from app.src.api.blueprints.investor_bp import investor_bp
from app.src.api.blueprints.portfolio_bp import portfolio_bp
from app.src.api.blueprints.account_bp import account_bp
from app.src.api.blueprints.ui_bp import ui_bp

app = Flask(__name__) # special variable that is assigned to every module (imported or executed)

app.register_blueprint(investor_bp)
app.register_blueprint(portfolio_bp)
app.register_blueprint(account_bp)
app.register_blueprint(ui_bp)

@app.route('/healthcheck', methods=['GET'])
def health_check():
    return render_template('healthcheck.html')


if __name__ == '__main__': # this module was used as an entry point (execution module)
    app.run(host='0.0.0.0', port= 8080, debug = True)
