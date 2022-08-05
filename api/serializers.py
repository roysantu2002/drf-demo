from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        # The default result (access/refresh tokens)

        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)
        print(data['access'])
        # Custom data you want to include
        data.update({'user': self.user.user_name})
        data.update({'id': self.user.id})
        # and everything else you want to send in the response
        return data
