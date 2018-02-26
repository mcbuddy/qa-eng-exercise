# -*- coding: utf-8 -*-
"""
    server
    ~~~~~~

    A simple HTTP API service
"""

import logging
import os
import time
import MySQLdb

import sqlalchemy.event
import wtforms_json

from flask import Flask, request, json, jsonify, g
from flask_sqlalchemy import SQLAlchemy
from wtforms import Form
from wtforms.fields import TextField
from wtforms.validators import InputRequired, Email

debug = os.getenv('DEBUG', '0').lower() in ['true', 'yes', '1']
log_level = os.getenv('LOG_LEVEL', 'INFO').upper() if not debug else 'DEBUG'

logging.basicConfig(level=log_level)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.debug = debug

# using mysql localhost with root user no password.
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/exercise'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
wtforms_json.init()


def before_exec(conn, clause, multiparams, params):
    g.sql_alchemy_start_time = time.time()


def after_exec(conn, clause, multiparams, params, results):
    if not hasattr(g, 'sql_alchemy_start_time'):
        return

    duration = time.time() - g.sql_alchemy_start_time

    print(json.dumps({
        'name': 'query',
        'fields': {
            'duration': duration
        }
    }))


sqlalchemy.event.listen(db.engine, "before_execute", before_exec)
sqlalchemy.event.listen(db.engine, "after_execute", after_exec)


class UserForm(Form):
    username = TextField('username', [InputRequired()])
    email = TextField('email', [InputRequired(), Email()])


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)


with app.app_context():
    logger.debug('Creating database tables')
    db.create_all()


def user_to_dict(user):
    return {
        'id': user.id,
        'username': user.username,
        'email': user.email
    }


@app.route('/users')
def users_index():
    return jsonify({
        'items': [
            user_to_dict(user)
            for user in User.query.all()
        ]
    })


@app.route('/users', methods=['POST'])
def users_post():
    form = UserForm.from_json(request.get_json())
    if not form.validate():
        return jsonify({
            'message': 'Bad request',
            'errors': form.errors
        }), 400
    user = User(**form.data)
    db.session.add(user)
    db.session.commit()
    rv = user_to_dict(user)
    print(json.dumps({'name': 'user.created', 'entity': rv}))
    return jsonify(rv)


@app.route('/users/<user_id>')
def user(user_id):
    rv = User.query.filter_by(id=user_id).first_or_404()
    return jsonify(user_to_dict(rv))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
