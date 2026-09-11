import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.accounts.models import User

admin_email = os.environ.get('ADMIN_EMAIL', 'admin@example.com')
admin_password = os.environ.get('ADMIN_PASSWORD', 'Admin@123456')

if admin_email and admin_password:
    user = User.objects.filter(email=admin_email).first()
    if not user:
        User.objects.create_superuser(email=admin_email, password=admin_password)
        print(f"==> Successfully created superuser: {admin_email}")
    else:
        user.set_password(admin_password)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save()
        print(f"==> Superuser already exists. Credentials updated for: {admin_email}")
else:
    print("==> ADMIN_EMAIL or ADMIN_PASSWORD missing. Skipping superuser creation.")
