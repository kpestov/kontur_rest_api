"""
ASGI config for storage project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import dotenv
from django.core.asgi import get_asgi_application


dotenv.load_dotenv()
application = get_asgi_application()
