from sqlalchemy import Column
from lib.models.model_base import ModelBase
from lib.models.model_base import ModelBase
import sqlalchemy.dialects.postgresql as pg

class maanager(ModelBase):
    __tablename__ = "manager"
    managerID = Column(
        pg.BIGINT,
        primary_key=True,
        autoincrement=True,
        nullable=False
    )
    Firstname = Column(pg.VARCHAR)
    Lastname = Column(pg.VARCHAR)
    SSN = Column(pg.VARCHAR, nullable=False)
    employeeID = mapped_column(pg.BIGINT,  ForeignKey(employee.employeID), nullable=False)
     # relationships
    employee = relationship("employee", foreign_keys=[employeeID]

