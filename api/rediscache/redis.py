import datetime
from typing import AnyStr, Optional, Union

import aioredis
from aioredis import Redis

from .util import BackendBaseCache

DEFAULT_ENCODING = 'utf-8'
CACHE_KEY = 'REDIS'

RedisKey = Union[AnyStr, float, int]
RedisValue = Union[AnyStr, float, int]
RedisExpiry = Union[AnyStr, float, int]
RedisAbsExpiry = Union[AnyStr, float, int]

class BackendRedisCache(BackendBaseCache([RedisKey, RedisValue])):
    def __init__(
        self,
        address: str,
        encoding: Optional[str] = DEFAULT_ENCODING,

    ) -> None:
        self._redis_address = address
        self._encoding = encoding
        self._pool: Optional[Redis] = None

        print(self._redis_address)


    @property
    async def _client(self) -> Redis:
        if self._pool is None:
            self._pool = await self._create_connection()
        return self._pool

    async def _create_connection(self) -> Redis:
        return aioredis.from_url(self._redis_address)

    async def add(
        self,
        key: RedisKey,
        value: RedisValue,
        **kwargs
    ) -> bool:
        """
        Not a perfect solution.

        #TODO: Implement Lua

        if redis.call("GET", KEYS[1]) then
            return 0
        else
            return 1
        """

        client = await self._client
        in_cache = await client.get(key)

        if in_cache is not None:
            return False

        return await client.set(key, value, **kwargs)

    async def get(
        self,
        key: RedisKey,
        default: RedisValue = None,
        **kwargs,
    ) -> AnyStr:
        encoding = kwargs.pop("encoding", self._encoding)

        client = await self._client
        cache_value = await client.get(key, **kwargs)
        if encoding is not None and isinstance(cache_value, bytes):
            cached_value = cached_value.decode(encoding)

        return cached_value if cached_value is not None else default

    async def exists(self, *keys: RedisKey) -> bool:
        client = await self._client
        exists = await client.exists(*keys)

        return bool(exists)

    async def delete(self, key: RedisKey) -> bool:
        client = await self._client

        return await client.delete(key)

    async def flush(self) -> None:
        client = await self._client
        await client.flushdb()

    async def expire(
        self,
        key: RedisKey,
        time: RedisExpiry
    ) -> bool:
        client = await self._client

        return await client.expire(key, time)

    async def expireat(
        self,
        key: RedisKey,
        when: RedisAbsExpiry
    ) -> bool:
        client = await client.expireat(key, when)

    async def close(self) -> None:
        client = await self._client
        await client.connection_pool.disconnect()
        await client.close()








