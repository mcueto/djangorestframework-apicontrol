# djangorestframework-apicontrol

This is an App intended to control Clients Apps access over REST APIs.

## NOTICE
```
This software is in an early stage of development, please be carefull with the use of it, and remember to backup your database before apply each migration.
```

***

[*] permissions to control Client Apps in views
[ ] quota management per Client

If you want to contribute with this software you can code or donate in http://paypal.me/mcuetodeveloper


## Permission Usage
you only has to import the permission and use it in your rest_framework views, or in your settings.py file, as you prefer. e.g:

``` python
"""Contact views."""
from rest_framework import viewsets
from rest_framework_apicontrol.permissions import HasApiKeyPermission
from .models import (
    ContactInfo
)
from .serializers import (
    ContactInfoSerializer
)


class ContactInfoViewSet(viewsets.ModelViewSet):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer
    permission_classes = [HasApiKeyPermission]
    authentication_classes = []

```

All the calls to this endpoint **MUST HAVE** a header called **Api-Key** with the value of an App(App model in Django admin site)

## Donate
My Paypal - http://paypal.me/mcuetodeveloper
