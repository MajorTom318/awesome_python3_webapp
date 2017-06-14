#test.py

#初始化数据库表
import mysql.connector
conn = mysql.connector.connect(user='root', password='8225265921023', database='awesome')
cursor = conn.cursor()
cursor.execute('create table users (id varchar(50) primary key, email varchar(50), passwd varchar(50), name varchar(50), image varchar(500), admin boolean, created_at real)')
cursor.execute('create table blogs (id varchar(50) primary key, user_id varchar(50), user_name varchar(50), user_image varchar(500), name varchar(50), summary varchar(50), content text, created_at real)')
cursor.execute('create table comments (id varchar(50) primary key, blog_id varchar(50), user_id varchar(50), user_name varchar(50), user_image varchar(500), content text, create_at real)')
cursor.close()
conn.commit()
conn.close()


import orm, asyncio
from models import User, Blog, Comment

async def test():
    await orm.create_pool(loop, user='root', password='8225265921023', db='awesome')

    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
    await u.save()
    a = await u.findAll()
    print(a)

loop = asyncio.get_event_loop()
loop.run_until_complete(test())
orm.__pool.close()
loop.run_until_complete(orm.__pool.wait_closed())
loop.close()



