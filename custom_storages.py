from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

# custom_storages.py tells django where to save
# the css, media and user uploaded images


class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
