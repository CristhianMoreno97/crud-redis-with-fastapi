from .connection import get_redis_client
from redis.exceptions import ConnectionError

def get_hash(key: str):
    """
    Obtiene un hash del servidor Redis bajo la clave especificada.

    Args:
        key (str): La clave bajo la cual se encuentra el hash.

    Returns:
        dict: El diccionario de datos del hash.

    Raises:
        ConnectionError: Si ocurre un error de conexión con el servidor Redis.
    """
    redis_client = get_redis_client()

    try:
        data = redis_client.hgetall(key)
        return data
    except ConnectionError as e:
        raise ConnectionError("Error de conexión con el servidor Redis") from e

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
    
def delete_hash(key: str, keys: list):
    """
    Elimina uno o más campos de un hash en el servidor Redis bajo la clave especificada.

    Args:
        key (str): La clave bajo la cual se encuentra el hash.
        keys (list): La lista de campos que se eliminarán del hash.

    Raises:
        ConnectionError: Si ocurre un error de conexión con el servidor Redis.
    """
    redis_client = get_redis_client()

    try:
        redis_client.hdel(key, *keys)
    except ConnectionError as e:
        raise ConnectionError("Error de conexión con el servidor Redis") from e
    