from ineuron_college_management_system.utils.mongohandlers import MongoHandler
from ineuron_college_management_system import config


class CollegeDetails:
    def __int__(self):
        self.mongo_handler = MongoHandler()

    def college_profile(self, data):
        college_id = MongoHandler().find_data(config.MONGO_DBNAME, config.MONGO_COLLEGEDETAILS, data)
        if college_id:
            return {"status_id": 0}
        else:
            MongoHandler().insert_data(config.MONGO_DBNAME, config.MONGO_COLLEGEDETAILS, data)
            return {"status_id": 1}

    def find_details_by_id(self, data):
        _id = data["_id"]
        print(_id)
        find_college = MongoHandler().get_document_by_id(config.MONGO_DBNAME, config.MONGO_COLLEGEDETAILS, _id)
        if find_college:
            return {"status_id": 1}
        else:
            return {"status_id": 0}

