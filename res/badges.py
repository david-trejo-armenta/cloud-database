from flask import jsonify, request
from flask_restful import  Resource,  abort
from flask_pymongo import pymongo
from bson.json_util import  ObjectId
import db_config as database


class AllBadge(Resource):
    """ Get all badges """

    def get(self):
        pass