from sqlalchemy import Column, Integer, String, ForeignKey, Uuid
from sqlalchemy.orm import relationship

from app.conect_with_db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    user_name = Column(String, unique=True)
    email = Column(String, nullable=True)
    phone = Column(String, nullable=True)


class Computer(Base):
    __tablename__ = "computers"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    status = Column(String, default="ACTIVE")
    activated_at = Column(String, nullable=True)
    expiration_at = Column(String, nullable=True)
    host_v4 = Column(String, nullable=True)
    host_v6 = Column(String, nullable=True)
    detailed_info_id = Column(Integer, ForeignKey(column="detailed_info.id", ondelete="CASCADE"),
                              nullable=True)

    detailed_info = relationship("DetailedInfo", back_populates="computer", passive_deletes=True)


class DetailedInfoOwners(Base):
    __tablename__ = "detailedinfo_owners"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    detailed_info_id = Column(Integer, ForeignKey(column="detailed_info.id", ondelete="CASCADE"), nullable=True)
    owner_id = Column(Integer, ForeignKey(column="owners.id", ondelete="CASCADE"), nullable=True)


class DetailedInfo(Base):
    __tablename__ = "detailed_info"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    physical_id = Column(Integer, ForeignKey(column="physical.id", ondelete="CASCADE"), nullable=True)

    computer = relationship("Computer", back_populates="detailed_info")
    physical = relationship("Physical", back_populates="detailed_info")

    owners = relationship("Owners", secondary="detailedinfo_owners", back_populates="detailed_info")


class Physical(Base):
    __tablename__ = "physical"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    color = Column(String, nullable=True)
    photo = Column(String, nullable=True)
    uuid = Column(Uuid, nullable=True)

    detailed_info = relationship("DetailedInfo", back_populates="physical")


class Owners(Base):
    __tablename__ = "owners"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String, nullable=True, unique=True)
    card_number = Column(String, nullable=True, unique=True)
    email = Column(String, nullable=True, unique=True)

    detailed_info = relationship("DetailedInfo", secondary="detailedinfo_owners", back_populates="owners")


class DbTables:
    DB_TABLES = {"users": User, "computer": Computer, "physical": Physical,
                 "owners": Owners, "detailed_info": DetailedInfo}

    @classmethod
    def get_models(cls):
        return cls.DB_TABLES
