from sqlalchemy import Column, BIGINT, String, ForeignKey
from src.models.sqlite.settings.base import Base

class PeopleTable(Base):
    __tablename__ = "people"
    id = Column(BIGINT, primary_key=True, autoincrement=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    age = Column(BIGINT, nullable=False)
    pet_id = Column(BIGINT, ForeignKey("pets.id"))

    def __repr__(self):
        return f"<Person(id={self.id}, first_name={self.first_name}, last_name={self.last_name}, age={self.age}, pet_id={self.pet_id})>"

       