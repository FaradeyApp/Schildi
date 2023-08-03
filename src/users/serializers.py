from rest_framework import serializers

from users.services import entries


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=33)
    password = serializers.CharField(max_length=128, write_only=True)
    first_name = serializers.CharField(max_length=32, required=False, allow_null=True, allow_blank=True)
    last_name = serializers.CharField(max_length=32, required=False, allow_null=True, allow_blank=True)
    avatar = serializers.ImageField(required=False, allow_null=True, default=None)

    def to_entry(self) -> entries.UserEntry:
        return entries.UserEntry(
            **self.validated_data
        )


class EditUserSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=32, required=False, allow_null=True, allow_blank=True)
    last_name = serializers.CharField(max_length=32, required=False, allow_null=True, allow_blank=True)
    avatar = serializers.ImageField(required=False, allow_null=True, default=None)

    def to_entry(self) -> entries.UserEntry:
        return entries.EditUserEntry(
            **self.validated_data
        )


class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class TokenSerializer(serializers.Serializer):
    access = serializers.CharField()
    refresh = serializers.CharField()


class RefreshTokenSerializer(serializers.Serializer):
    refresh = serializers.CharField()
