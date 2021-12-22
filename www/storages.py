from storages.backends.s3boto3 import S3Boto3Storage

class MediaStorage(S3Boto3Storage):
    bucket_name = 'eyolfson.com'
    default_acl = 'public-read'
    location = 'media'
    querystring_auth = False

class StaticStorage(S3Boto3Storage):
    bucket_name = 'eyolfson.com'
    default_acl = 'public-read'
    location = 'static'
    querystring_auth = False
