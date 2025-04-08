from flask import Blueprint, jsonify, request
from src.http_types.http_response import HttpResponse
from src.http_types.http_request import HttpRequest

event_route_bp = Blueprint("event_route", __name__)

@event_route_bp.route("/event", methods=["POST"])

def create_new_event():
    http_request = HttpRequest(body=request.json)

    htttp_response = HttpResponse(body={"estou": "aqui"}, status_code=201)
    # retorna um body e um status code
    return jsonify(htttp_response.body), htttp_response.status_code