from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text


engine = create_engine("mysql+pymysql://root:123456andy@127.0.0.1:3306/threatreport")

session = sessionmaker(engine)

Model = declarative_base()




class AquankeModel(Model):
    __tablename__ = "anquanke"

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    title = Column('title', String(64), index=True)
    cve = Column('cve', String(24), index=True)
    publish = Column('publish', String(24))
    update = Column('update', String(24))
    type = Column('type', String(24))
    cnnvd_id = Column('cnnvd-id', String(32), index=True)
    cubes = Column('cubes', String(32), index=True)
    cvss = Column('cvss', String(32))
    vul_from = Column('vul_from', String(258))
    info = Column('info', Text())



    def __str__(self):
        return self.title





if __name__ == "__main__":

    # 创建表
    Model.metadata.create_all(engine)

    





    ...


