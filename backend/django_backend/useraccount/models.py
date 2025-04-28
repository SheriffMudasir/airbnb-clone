# useraccount/models.py
import uuid
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _



class User(AbstractUser):

    first_name = None
    last_name = None

    # --- Define your custom fields ---
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(_('email address'), unique=True) # Ensure email is still required
    avatar = models.ImageField(_('avatar'), upload_to='uploads/avatars/', blank=True, null=True)

    # --- Authentication Fields ---
    # 'objects' will now default to AbstractUser's UserManager
    USERNAME_FIELD = 'username' # Use username to log in
    EMAIL_FIELD = 'email'       # Specify email field for Django's use
    REQUIRED_FIELDS = ['email'] # Email is required for createsuperuser

    def __str__(self):
        return self.username