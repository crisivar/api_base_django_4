from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.db import models


class User(AbstractBaseUser):

    username = models.CharField(max_length=50, unique=True, db_column='usuario')
    password = models.CharField(max_length=60, db_column='clave')
    nivel_acceso = models.CharField(max_length=30, blank=True, null=True)
    tpo_prsna = models.CharField(max_length=10, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True, db_column='nm_prsna')
    last_name = models.CharField(max_length=50, blank=True, null=True, db_column='ap_prsna')
    nm_emprsa = models.CharField(max_length=60, blank=True, null=True)
    cc_nit = models.CharField(max_length=15, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    tlfno = models.CharField(max_length=10, blank=True, null=True)
    ciudad = models.CharField(max_length=30, blank=True, null=True)
    pais = models.CharField(max_length=20, blank=True, null=True)
    role = models.CharField(max_length=17, blank=True, null=True)
    token_password = models.CharField(max_length=100, blank=True, null=True)
    password_updated = models.BooleanField(blank=True, null=True)
    date_password_updated = models.DateTimeField(blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField(blank=True, null=True)
    is_staff = models.BooleanField(blank=True, null=True)

    USERNAME_FIELD = 'username'

    objects = UserManager()

    class Meta:
        managed = False
        db_table = 'usuarios'
