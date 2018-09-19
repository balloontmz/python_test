from sqlalchemy import Column, String, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+pymysql://test:123456@localhost:3306/test')
# 创建对象的基类：
Base = declarative_base()


# 定义一对多对象
class User(Base):
    __tablename__ = 'user'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # 一对象：
    books = relationship('Book')


class Book(Base):
    __tablename__ = 'book'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # 多的一方通过外链链接到user
    user_id = Column(String(20), ForeignKey('user.id'))


Base.metadata.create_all(engine)

DBSession = sessionmaker(bind=engine)
session = DBSession()
session.close()
