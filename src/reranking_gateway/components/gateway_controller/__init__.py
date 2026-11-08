"""Gateway Controller.

Validates, normalises, de-duplicates, and bounds the incoming candidate set.
"""

from reranking_gateway.components.gateway_controller.adapter import ROLE, build
from reranking_gateway.components.gateway_controller.config import CONFIG, GatewayControllerConfig
from reranking_gateway.components.gateway_controller.errors import GatewayControllerError
from reranking_gateway.components.gateway_controller.service import GatewayControllerService

__all__ = ["CONFIG", "ROLE", "build", "GatewayControllerConfig", "GatewayControllerError", "GatewayControllerService"]
