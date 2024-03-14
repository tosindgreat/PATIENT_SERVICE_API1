from sqlalchemy import Column
from lib.models.model_base import ModelBase
from lib.models.model_base import ModelBase
import sqlalchemy.dialects.postgresql as pg

class depatment(ModelBase):
    __tablename__ = "department"
    departmentID = Column(
        pg.BIGINT,
        primary_key=True,
        autoincrement=True,
        nullable=False
    )
    departmentname = Column(pg.VARCHAR)
    managerID = mapped_column(pg.BIGINT,  ForeignKey(manager.managerID), nullable=False)
    
    # relationships
    manager = relationship("manager", foreign_keys=[managerID]


