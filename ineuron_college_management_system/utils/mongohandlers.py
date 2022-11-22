
from datetime import datetime

from bson import ObjectId
from pymongo import MongoClient
# from flask import session as flask_session, current_app


class MongoHandler:
    """
    This class is a Middleware between app and Database Operations.
    """

    def __init__(self):
        try:
            self.client = MongoClient('localhost:27017')

        except Exception as e:
            print(
                "MongoDbHandler : Exception while connecting to MongoDB.." + e)
    def get_client(self):
        """
        Get the Mongodb client.
        :return:
        """
        return self.client

    def close_client(self):
        """
        Releases any valuable MongoDb Resources
        :return:
        """
        self.client.close()

    def get_db(self, db_name: str):
        """
        Gets the Mongodb database specified by db_name
        :param db_name:
        :return:
        """
        return self.client[db_name]

    def drop_db(self, db_name: str):
        """
        Drops the Mongodb database specified by db_name
        :param db_name:
        :return:
        """
        return self.client.drop_database(self.client[db_name])

    def create_collection(self, db_name: str, collection_name: str):
        """
        Creates the collection specified by collection_name inside db_name Database
        :param db_name:
        :param collection_name:
        :return:
        """
        db = self.get_db(db_name)
        return db.createCollection[collection_name]

    def get_collection(self, db_name: str, collection_name: str):
        """
        Gets the collection specified by collection_name in db_name Database
        :param db_name:
        :param collection_name:
        :return:
        """
        db = self.get_db(db_name)
        return db[collection_name]

    def delete_collection(self, db_name: str, collection_name: str):
        """
        Deletes the collection specified by collection_name in db_name Database
        :param db_name:
        :param collection_name:
        :return:
        """
        db = self.get_db(db_name)
        return db.drop_collection(collection_name)

    def insert_data(self, db_name, coll_name, insert_json):
        """
        this function returns particular data inserted from
        """
        db = self.client[db_name]
        mycoll = db[coll_name]
        return mycoll.insert_one(insert_json)

    def find_data(self, db_name, coll_name, find_json):
        """
        this function returns particular data inserted from
        """
        db = self.client[db_name]
        mycoll = db[coll_name]
        return mycoll.find(find_json)

    def aggregate_data(self, db_name, coll_name, pipeline):
        db = self.client[db_name]
        mycoll = db[coll_name]
        return mycoll.aggregate(pipeline)

    def update_data(self, db_name, coll_name, filter_json, update_json):
        db = self.client[db_name]
        coll = db[coll_name]
        return coll.update_data(filter_json, update_json)

    def get_document_by_id(self, db_name: str, collection_name: str, object_id: str):
        """
        Get Specified ObjectId document
        :param db_name:
        :param collection_name:
        :param object_id:
        :return:
        """
        db = self.get_db(db_name)
        collection = db[collection_name]
        return collection.find_one({'_id': ObjectId(object_id)})


