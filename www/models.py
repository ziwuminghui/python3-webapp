# -*- coding: utf-8 -*-
import time,uuid
from orm import Model,StringField,BooleanField,FloatField,TextField

def next_id():
    return '%015d%s000'%(int(time.time()*1000),uuid.uuid4().hex)

class User(Model):
    """完善User表的映射"""
    __table__ = 'users'

    id = StringField(primary_key=True,default=next_id,ddl='varchar(50)')
    email = StringField(ddl='varchar(50)')
    passwd = StringField(ddl='varchar(50)')
    admin = BooleanField(default=False)
    name = StringField(ddl='varchar(50)')
    image = StringField(ddl='varchar(500)')
    created_at = FloatField(default=time.time)

class Blog(Model):
    """创建Blog表的映射"""
    __table__ = 'blogs'

    id = StringField(primary_key=True,default=next_id,ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    name = StringField(ddl='varchar(50)')
    summary = StringField(ddl='varchar(200)')
    content = TextField()
    created_at = FloatField(default=time.time)

class Comment(Model):
    """创建Comment表映射"""
    __table__ = 'comments'

    id = StringField(primary_key=True,default=next_id,ddl='varchar(50)')
    blog_id = StringField(ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    content = TextField()    
    created_at = FloatField(default=time.time)