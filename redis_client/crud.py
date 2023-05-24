from .connection import get_redis_client
from redis.exceptions import ConnectionError

def save_hash(key: str, data: dict):
    """
    Guarda un hash en el servidor Redis bajo la clave especificada.

    Args:
        key (str): La clave bajo la cual se guardará el hash.
        data (dict): El diccionario de datos que se guardará en el hash.

    Raises:
        ConnectionError: Si ocurre un error de conexión con el servidor Redis.
    """
    redis_client = get_redis_client()

    try:
        redis_client.hset(key, mapping=data)
    except ConnectionError as e:
        raise ConnectionError("Error de conexión con el servidor Redis") from e