from redis import Redis
from os import getenv
from redis.exceptions import ConnectionError

def get_redis_client():
    """
    Obtiene y retorna una instancia de Redis con la configuración basada en las variables de entorno.

    Returns:
        Redis: Instancia de Redis.
    """
    redis_host = getenv('REDIS_HOST')
    redis_port = getenv('REDIS_PORT')
    redis_password = getenv('REDIS_PASSWORD')
    redis_ssl = bool(getenv('REDIS_SSL'))

    if not all([redis_host, redis_port, redis_password]):
        raise ValueError("Faltan variables de entorno requeridas para la conexión a Redis")

    redis_client = Redis(
        host=redis_host,
        port=redis_port,
        password=redis_password,
        ssl=redis_ssl
    )

    return redis_client

try:
    redis_client = get_redis_client()
    print("Redis client connected successfully")
except ConnectionError as e:
    print(e)