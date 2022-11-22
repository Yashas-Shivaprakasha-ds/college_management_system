from flask import jsonify, request, Blueprint

from .handlers import CollegeDetails

bp = Blueprint('admin', __name__)


class CollegeDetail:

    @bp.route('/insert_college_data', methods=['POST'])
    def insert_college_data():
        """
        :return: function inserts admin details
        """
        data = request.json
        return jsonify(CollegeDetails().college_profile(data))

    @bp.route('/find_college_data', methods=['POST'])
    def find_college_data():
        """
        :return: function inserts admin details
        """
        data = request.json
        return jsonify(CollegeDetails().find_details_by_id(data))

