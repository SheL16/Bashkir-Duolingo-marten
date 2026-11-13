from sqlalchemy import BigInteger, Text
from sqlalchemy.orm import Mapped, mapped_column
from database.database import Base

class Dictionary(Base):
    __tablename__ = "dictionary"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    russian: Mapped[str] = mapped_column(Text, nullable=False)
    bashkir: Mapped[str] = mapped_column(Text, nullable=False)