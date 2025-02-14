DATABASES = {
    'default': {
      'ENGINE': 'django.db.backends.postgresql',
      'NAME': 'venture_villas',
      'USER': os.environ['DB_USER'],
      'PASSWORD': os.environ['DB_PW'],
      'HOST': os.environ['DB_HOST'],
      'PORT': '5432',
    }
}