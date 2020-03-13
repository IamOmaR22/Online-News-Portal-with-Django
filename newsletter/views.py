from django.shortcuts import render, get_object_or_404, redirect
from .models import Newsletter
from news.models import News
from cat.models import Cat  # for showing categories in footer
from subcat.models import SubCat  ## for SubMenu in the menu bar
from django.contrib.auth import authenticate, login, logout  # for authentication
from django.core.files.storage import FileSystemStorage  # for upload image
from trending.models import Trending  ### Trending app's model
import random                   ## Random Object (For Trending now)
from random import randint      ## Random Object (For Trending now)
from django.contrib.auth.models import User, Group, Permission ## For User Group Permission
from django.contrib.contenttypes.models import ContentType  ## To add Permissions

# Create your views here.
