from sqlalchemy import Column
from lib.models.model_base import ModelBase
from lib.models.model_base import ModelBase
import sqlalchemy.dialects.postgresql as pg

class hospital(ModelBase):
    __tablename__ = "hospital"
    hospitalID = Column(
        pg.BIGINT,
        primary_key=True,
        autoincrement=True,
        nullable=False
    )
    HospitalName= Column(pg.VARCHAR)
    HospitalAddress = Column(pg.VARCHAR)
    