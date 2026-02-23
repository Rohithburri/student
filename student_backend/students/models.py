from django.db import models


class Student(models.Model):
    full_name = models.CharField(max_length=150)
    father_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=10)


class AcademicInformation(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name="academic_information")
    college_code = models.CharField(max_length=50)
    department_course = models.CharField(max_length=100)
    academic_year = models.CharField(max_length=20)
    year_of_study = models.CharField(max_length=20)
    cgpa_percentage_range = models.CharField(max_length=20)


class CourseInterest(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name="course_interest")
    reason_for_course = models.JSONField()
    area_of_interest = models.JSONField()
    skills_to_develop = models.JSONField()


class FuturePlan(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name="future_plan")
    plan_after_graduation = models.CharField(max_length=100)
    going_abroad = models.BooleanField()
    preferred_country = models.CharField(max_length=100, null=True, blank=True)
    career_goal_type = models.CharField(max_length=100)


class AdditionalInformation(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name="additional_information")
    internship_completed = models.BooleanField()
    interested_in_internship = models.BooleanField()
    have_certifications = models.BooleanField()
