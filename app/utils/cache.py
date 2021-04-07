import logging

from typing import Any

from django.core.cache import cache
from django_redis import get_redis_connection
from redis.exceptions import ConnectionError, TimeoutError

from app.utils.exceptions import CacheGetException, CacheSetException


logger = logging.getLogger(__name__)


def cache_data(data: Any, cache_name: str):
    """Выполняет кэширование данных. В качестве кэш-хранилища используется Redis"""

    try:
        conn = get_redis_connection()
        conn.ping()
    except (TimeoutError, ConnectionError):
        logger.warning('Failed to connect to redis')
        return data

    try:
        cached_data = cache.get(f'{cache_name}')
        logger.info('Get value from Redis cache')
    except CacheGetException:
        logger.warning('Failed to get value from cache')
        return data

    if not cached_data:
        data_to_cache = data
        try:
            cache.set(f'{cache_name}', data_to_cache)
            logger.info('Set value to Redis cache')
            return data_to_cache
        except CacheSetException:
            logger.warning('Failed to set value to cache')
            return data

    return cached_data
