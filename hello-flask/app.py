import logging

from flask import Flask, escape, request

logger = logging.getLogger(__name__)
logging.basicConfig(level="DEBUG", format=logging.BASIC_FORMAT)

app = Flask(__name__)


@app.route('/')
def hello():
    name = request.args.get("name", "World")
    logger.info(f"Say hello to {name}!")
    return f'Hello, {escape(name)}!'
