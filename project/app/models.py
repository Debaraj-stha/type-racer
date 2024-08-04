from enum import Enum
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group, Permission
from django.db import models
from django.core.validators import RegexValidator


from .manager import User_Manager
# Create your models here.

name_Validator = RegexValidator(
    regex=r"[a-zA-Z]", message="Invalid field value,only string is allowed"
)
phone_regex = RegexValidator(
    regex=r"^\+?1?\d{9,15}$",
    message="Phone number must be entered in the format: '+999999999'. Up to 13 digits allowed.",
)


class Customuser(AbstractBaseUser, PermissionsMixin):
    phone = models.CharField(max_length=13, validators=[phone_regex], unique=True)
    lastname = models.CharField(max_length=10, null=True, blank=True, validators=[name_Validator])
    firstname = models.CharField(max_length=10, null=True, blank=True, validators=[name_Validator])
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateField(auto_now_add=True)
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_permissions_set',
        blank=True
    )

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = User_Manager()

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'


    def __str__(self) -> str:
        return ("Name : " + self.name if self.firstname  else "Phone : " + self.phone)
class Category(Enum):
    SIMPLE="simple"
    MEDIUM="medium"
    COMPLEX="complex"

category=[
    (Category.SIMPLE.value,"simple"),
    (Category.MEDIUM.value,"medium"),
    (Category.COMPLEX.value,"complex"),
    ]

class Quote(models.Model):
    text = models.TextField()
    difficulty = models.CharField(choices=category,default=Category.SIMPLE.value,max_length=10)


    def __str__(self) -> str:
        words=self.text.split()
        sort_text="".join(words[:15])
        if len(words)>15:
            sort_text+="..."
        return sort_text
    def to_dict(self):
        return {"id":self.id,"text":self.text,"difficulty":self.difficulty}
    

class Rank(models.Model):
    user = models.ForeignKey(Customuser, on_delete=models.CASCADE)
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE,null=True)
    score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)

    def __str__(self) -> str:
        return  ("Score %s by user %s" ) % (self.score,self.user.phone)
