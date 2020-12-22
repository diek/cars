import random
import string

from car import models as car_models
# from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, Group, User
from django.contrib.contenttypes.models import ContentType


def random_string(length=10):
    # Create a random string of length length
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


def create_User(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_AbstractUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractUser.objects.create(**defaults)


def create_AbstractBaseUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractBaseUser.objects.create(**defaults)


def create_Group(**kwargs):
    defaults = {
        "name": "%s_group" % random_string(5),
    }
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_ContentType(**kwargs):
    defaults = {
    }
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_car_Car(**kwargs):
    defaults = {}
    defaults["year"] = ""
    defaults["model"] = ""
    defaults["base_color"] = ""
    defaults["size"] = ""
    defaults.update(**kwargs)
    return car_models.Car.objects.create(**defaults)
def create_car_Make(**kwargs):
    defaults = {}
    defaults["make"] = ""
    defaults.update(**kwargs)
    return car_models.Make.objects.create(**defaults)
