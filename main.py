import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()

from lesson.models import User

# User(
#     name = "piter",
#     bio = "",
#     email = "testgmail.com",
#     birthday = "1990-01-01"
# ).save()

# user  = User.objects.filter(id=1).all()
# print(user)
# print(user[0].email)

# user = User.objects.get(id=1)

# user  = User.objects.filter(id=1).first()
# print(user)
# print(user.email)

# user = User.objects.filter(id=4).first()
# print(user)

# not_needed_user = User.objects.get(id=2)
# not_needed_user.delete()

# user_to_upadate = User.objects.get(id=2)
# user_to_upadate.name =  "first_name2"
# user_to_upadate.bio = "bio2"
# user_to_upadate.email = "test2@gmail.com"
# user_to_upadate.save(

# users = User.objects.all()
# for user in users:
#     print(user.name)

