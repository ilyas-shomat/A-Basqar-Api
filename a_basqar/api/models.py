from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.


class MyAccountManager(BaseUserManager):
    def create_user(self, username, full_name, password, status):
        if not username:
            raise ValueError("User must have username")

        user = self.model(
            # email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, full_name, password, status):
        user = self.create_user(
            # email=self.normalize_email(email),
            password=password,
            username=username,
            full_name=full_name,
            status=status,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=255)
    company_bin = models.CharField(max_length=12)

    def __str__(self):
        return self.company_name


class Store(models.Model):
    store_id = models.AutoField(primary_key=True)
    store_name = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='store_company', null=True)

    def __str__(self):
        return self.store_name


class Account(AbstractBaseUser):
    # email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    account_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    status = models.CharField(max_length=255)

    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='store', null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='user_company', null=True)

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['full_name', 'password', 'status']

    objects = MyAccountManager()

    def __str__(self):
        return self.full_name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
