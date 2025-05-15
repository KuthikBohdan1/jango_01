import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()

from lesson.models import User, Category, Product, Student, Course

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


# new_category = Category(name = "Diary products")
# new_category.save()

# new_product = Product(
#     name = "Milk",
#     price = 22.5,
#     description = "Milk is a white liquid produced by the mammary glands of mammals.",
#     Category = new_category

# ).save()
        

# product = Product.objects.filter(id=1).first()
# print(product.name)
# print(product.Category.name)


# catategory = Category.objects.get(id=2)
# print(catategory.product_set)

# Student(name="Some Student").save()


Course(title="some_course").save() 