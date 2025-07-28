from flask_limiter.errors import RateLimitExceeded
from flask import Blueprint, jsonify


bp_erro_handler = Blueprint("erro_handler", __name__)


@bp_erro_handler.errorhandler(RateLimitExceeded)
def ratelimit_handler(e):
    return jsonify({'message': 'Rate limit exceeded. Try again later.'}), 429
