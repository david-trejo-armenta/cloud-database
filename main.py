from flask import Flask, jsonify, request
from flask_restful import Api
from flask_pymongo import pymongo
import db_config as database

#Resources

from res.badge import Badge
from res.badges import Badges

app=Flask(__name__)

api=Api(app)



api.add_resource(Badge,'/new','/<string:by>=<string:data>/')
api.add_resource(Badges, '/all/')

if __name__ == '__main__':
    app.run(load_dotenv=True,)