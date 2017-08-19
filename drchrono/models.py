from django.db import models
from django.contrib.auth.models import User
from social_django.utils import load_strategy

import datetime, requests

class ArrivedPatient(models.Model):
  first_name = models.CharField(max_length=200)
  last_name = models.CharField(max_length=200)
  ssn = models.CharField(max_length=50)
  created_at = models.DateField(auto_now_add=True)
  patient_id = models.IntegerField(null=False, blank=False)
  doctor_id = models.IntegerField(null=False, blank=False)
  chart_id = models.CharField(max_length=200)
  appointment_id = models.CharField(max_length=200)
  time_waiting = models.DurationField(default=datetime.timedelta(seconds=0))
  seen_by_doctor = models.BooleanField(default=False)

class Profile(models.Model):
  user = models.OneToOneField(User)
  is_doctor = models.BooleanField(default=False)
  doctor_id = models.IntegerField(null=False, blank=False)

  def __str__(self):
    return self.user.username

  def social(self):
    return self.user.social_auth.first()

  def patients(self):
    social = self.social()
    # Access Token for Current User
    headers = {'Authorization': 'Bearer {}'.format(social.get_access_token(load_strategy()))}
    patients = []
    patients_url = 'https://drchrono.com/api/patients'
    while patients_url:
      response = requests.get(patients_url, headers=headers)
      data = response.json()
      patients.extend(data['results'])
      patients_url = data['next'] # A JSON null on the last page
    return patients