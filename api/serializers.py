from hashlib import md5

import jwt
from django.conf import settings
from django.core.cache import cache
from django_redis import get_redis_connection
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# import redis
# from django.conf import settings



# Connect to our Redis instance
# redis_instance = redis.StrictRedis(host=settings.REDIS_HOST,
#                                   port=settings.REDIS_PORT, db=0)




# import arioredis

# con = get_redis_connection("default")
#


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):


    def validate(self, attrs):

        # redi = BackendRedisCache()

        # The default result (access/refresh tokens)
#
#         redis = redis_instance.Redis.from_url
        # r=redis.StrictRedis(host=settings.REDIS_HOST,port=settings.REDIS_PORT,db=settings.REDIS_DB)

        result = cache.keys("*")
        print(result)
        r = get_redis_connection("default")
        connection_pool = r.connection_pool
        print("Created connections so far: %d" % connection_pool._created_connections)


        for key in r.scan_iter("user:*"):
            print(f'{key}')


        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)

        # jwt.decode(token,settings.SECRET_KEY, algorithms=['HS256'])
        # Custom data you want to include
        data.update({'user': self.user.user_name})
        data.update({'id': self.user.id})
        hashed = md5(f"{self.user.user_name}{self.user.password}".encode('utf-8')).hexdigest()
        print(f"{hashed}_token")
        cache.set(f"{hashed}_token", data["access"], settings.CACHE_TTL)
        # and everything else you want to send in the response
        # print(cache.get(f'{hashed}'))
        return data
