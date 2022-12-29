from src.dividas import models


def create_response_dividas_devedor(devedor_dividas):
    devedor = models.DevedorResponse(
        id=devedor_dividas[0][""]["id"],
        name=devedor_dividas[0]["name"]
    )
    dividas = []

    for debt in devedor_dividas:
