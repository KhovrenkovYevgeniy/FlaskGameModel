from sqlalchemy import *

meta = MetaData()

Users = Table("Users", meta,
              Column("name", String(250), nullable=False),
              Column("age", Integer, nullable=False),
              Column("email", String(250), nullable=False)
              )

Games = Table("Games", meta,
              Column("Games_id", Integer, primary_key=True),
              Column("name", String(250), nullable=False),
              Column("User_id", Integer,ForeignKey("users.User_id"))
              )
print(Users)


engine = create_engine("mysql+mysqlconnector://Evghene:77009988h@localhost/GameModel", echo=True)
meta.create_all(engine)

