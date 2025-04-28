from flask import Blueprint, jsonify, request

events_link_route_bp = Blueprint("event_link_route", __name__)

from src.http_types.http_request import HttpRequest

from src.controllers.events_link.events_link_creator import EventLinkCreator
from src.model.repositories.eventos_link_repository import EventosLinkRepository

@events_link_route_bp.route("/events_link", methods=["POST"])
def create_new_link():
    eventos_link_repo = EventosLinkRepository()
    events_link_creator = EventLinkCreator(eventos_link_repo)

    http_request = HttpRequest(body=request.json)

    htttp_response = events_link_creator.create(http_request)

    # retorna um body e um status code
    return jsonify(htttp_response.body), htttp_response.status_code