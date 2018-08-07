from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 初始化数据库连接：
engine = create_engine('mysql+pymysql://test:123456@localhost:3306/test') # mysql下root用户不可用，猜测为软件在tomtiddler用户下无权限
# 创建对象的基类
Base = declarative_base()


# 定义User对象：
class User(Base):
    # 表的名字：
    __tablename__ = 'user'

    # 表的结构：
    id = Column(String(20), primary_key=True)
    name = Column(String(20))


# Base.metadata.create_all(engine) 在engine连接下 创建继承Base的所有表

# 创建DBSession类型：
DBSession = sessionmaker(bind=engine)
# 创建session对象：
# session = DBSession()
# 创建新User对象：
# new_user = User(id='5', name='bob') 已操作
# 添加到session
# session.add(new_user)
# 提交即保存到数据库
# session.commit()
# 关闭session
# session.close()

session2 = DBSession()
user = session2.query(User).filter(User.id=='5').one()
# 打印类型和对象的name属性
print('type:', type(user))
print('name:', user.name)
# 关闭session
session2.close()