from rest_framework import serializers
from .models import *
from .validators import *


class AcademicSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicInformation
        exclude = ("student",)


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseInterest
        exclude = ("student",)


class FutureSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuturePlan
        exclude = ("student",)

    def validate(self, data):
        validate_preferred_country(data)
        return data


class AdditionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalInformation
        exclude = ("student",)


class StudentSerializer(serializers.ModelSerializer):
    academic_information = AcademicSerializer()
    course_interest = CourseSerializer()
    future_plan = FutureSerializer()
    additional_information = AdditionalSerializer()

    class Meta:
        model = Student
        fields = "__all__"

    def validate_mobile_number(self, value):
        validate_mobile(value)
        return value

    def create(self, validated_data):
        academic = validated_data.pop("academic_information")
        course = validated_data.pop("course_interest")
        future = validated_data.pop("future_plan")
        additional = validated_data.pop("additional_information")

        student = Student.objects.create(**validated_data)

        AcademicInformation.objects.create(student=student, **academic)
        CourseInterest.objects.create(student=student, **course)
        FuturePlan.objects.create(student=student, **future)
        AdditionalInformation.objects.create(student=student, **additional)

        return student