from flask import Flask
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration


def create_app():
    app = Flask(__name__)
    app.config['JSON_AS_ASCII'] = False

    # sentry_sdk.init(dsn="https://225751dc0e8e4a2095a83abccc18b3f0@o415817.ingest.sentry.io/5307474",integrations=[FlaskIntegration()])


    return app

app = create_app()