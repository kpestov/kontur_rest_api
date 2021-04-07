import logging

from typing import Any

from django.core.cache import cache
from django_redis import get_redis_connection
from django.conf import settings
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
        max_requests = cache.get('max_requests')

        # проверка на доступность ключа max_requests, который определяет максимальное количество запросов,
        # после которых кэш устаревает
        if max_requests is not None:
            # если счетчик max_requests израсходован, то чистим кэш
            if not int(max_requests):
                cache.clear()
            else:
                # уменьшаем счетчик max_requests на 1
                cache.decr('max_requests', delta=1)

            logger.info('Get values from Redis cache')
    except CacheGetException:
        logger.warning('Failed to get values from cache')
        return data

    if not cached_data:
        data_to_cache = data
        try:
            cache.set(f'{cache_name}', data_to_cache)
            cache.set('max_requests', settings.CACHE_MAX_REQUESTS)
            logger.info('Set values to Redis cache')
            return data_to_cache
        except CacheSetException:
            logger.warning('Failed to set values to cache')
            return data

    return cached_data
