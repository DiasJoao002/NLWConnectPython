from flask import Blueprint, jsonify, request
from src.http_types.http_request import HttpRequest
from src.validators.subscribers_creator_validator import subscribers_creator_validator
from src.controllers.subscribers.subscribers_creator import SubscribersCreator
from src.model.repositories.subscribers_repository import SubscribersRepository

subs_route_bp = Blueprint("subs_route", __name__)

@subs_route_bp.route("/subscriber", methods=["POST"])

def create_new_subscriber():
    subscribers_creator_validator(request)
    http_request = HttpRequest(body=request.json)

    subs_repo = SubscribersRepository()
    subs_creator = SubscribersCreator(subs_repo)

    htttp_response = subs_creator.create(http_request)

    # retorna um body e um status code
    return jsonify(htttp_response.body), htttp_response.status_code
