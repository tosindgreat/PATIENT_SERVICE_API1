import datetime
import uuid
from sqlalchemy import Column, ForeignKey
from lib.models.model_base import ModelBase
from lib.models.physician import Physician
from sqlalchemy.orm import mapped_column, relationship
import sqlalchemy.dialects.postgresql as pg

class employee(ModelBase):
    __tablename__ = "employee"
    employeeID = Column(
        pg.BIGINT,
        primary_key=True,
        autoincrement=True,
        nullable=False
    )
    Firstname = Column(pg.VARCHAR)
    Lastname = Column(pg.VARCHAR)
    SSN = Column(pg.VARCHAR, nullable=False)
    DOB = Column(pg.DATE)
    Gender = Column(pg.VARCHAR)
    Address = Column(pg.VARCHAR)
    Hospital = mapped_column(pg.BIGINT,  ForeignKey(Hospital.HospitalID), nullable=False)
    
# relationships
    Hospital = relationship("Hospital", foreign_keys=[HospitalID]

