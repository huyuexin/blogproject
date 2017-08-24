#!/usr/bin/python3
# -*- coding: utf-8 -*-
#blog/templatetags/blog_tags.py
from ..models import Post, Category
from django import template
register = template.Library()

#最近
@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]
#归档


@register.simple_tag
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')



@register.simple_tag
def get_categories():
    # 别忘了在顶部引入 Category 类
    return Category.objects.all()