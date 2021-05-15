from django import template

register = template.Library()

from ..models import Post
from django.contrib.auth.models import User


@register.simple_tag
def get_bool(post, user):
    return post.get_bool(user)

