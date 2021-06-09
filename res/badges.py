from flask import jsonify, request
from flask_restful import  Resource,  abort
from flask_pymongo import pymongo
from bson.json_util import  ObjectId
import db_config as database


class Badges(Resource):
    """ Get all badges """

    def get(self):
        response =list(database.db.Badges.find())
        
        for doc in response:
            doc['_id'] = str(doc['_id'])

        return jsonify(response)

    def delete(self):
        return database.db.Delete.delete_many({}).deleted_count