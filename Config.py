
class Config():
    def __init__(self) -> None:
        self.db_url = "mysql+pymysql://root:xxxxx@localhost:3306/test?charset=utf8"
        self.sqlalchemy_track_modifications = True
