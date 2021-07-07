from flask import Flask, render_template, request, url_for
import os
import string



application = Flask(__name__)

@application.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    application.run()