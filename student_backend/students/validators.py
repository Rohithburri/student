import re
from rest_framework import serializers


def validate_mobile(value):
    if not re.match(r"^[0-9]{10}$", value):
        raise serializers.ValidationError("Mobile must be 10 digits")


def validate_preferred_country(data):
    if data.get("going_abroad") and not data.get("preferred_country"):
        raise serializers.ValidationError("Preferred country required if going abroad")