from rest_framework import serializers

from .models import Appraisal


class AppraisalSerializer(serializers.ModelSerializer):
   class Meta:
      model = Appraisal
      fields = '__all__'
      depth = 1
