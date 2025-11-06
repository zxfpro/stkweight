import uuid
from typing import Optional

from sqlalchemy import String, Boolean, Column
from sqlalchemy.dialects.mysql import (
    CHAR,
)  # Use CHAR for UUID to store as fixed length string
from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from pydantic import BaseModel, Field
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from sqlalchemy import Column, Integer, String, Text, DateTime, text, UniqueConstraint,Float
from sqlalchemy.orm import declarative_base


class Base(DeclarativeBase):
    pass


# SQLAlchemy 用户模型
# 使用 SQLAlchemyBaseUserTableUUID 来自动处理 UUID 主键
class User(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = "users"  # 表名

    # 可以在这里添加额外的用户属性
    first_name: str = Column(String(255), nullable=True)
    last_name: str = Column(String(255), nullable=True)
    is_admin: bool = Column(Boolean, default=False)


class Weight(Base):
    __tablename__ = 'weight_data' # 数据库中的表名，你可以改成你希望的名字

    # id (int, primary_key=True, autoincrement=True)
    # 你的属性表中 id 为 int, true (not null), true (primary key), 0 (length), ASC (key order), true (auto increment)
    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True, # 自动递增
        nullable=False,     # 不能为空
        comment="Primary key ID"
    )

    # prompt_id (varchar 255, not null, unique)
    # 你的属性表中 prompt_id 为 varchar, 255 (length), true (not null)
    user = Column(
        String(255),        # VARCHAR 类型，长度 255
        nullable=True,     # 不能为空    # 必须是唯一的，这会创建唯一索引
        comment="用户"
    )

    Date = Column(
        DateTime,
        nullable=False,      # 不能为空
        server_default=text('CURRENT_TIMESTAMP'),
        onupdate=text('CURRENT_TIMESTAMP'),
        comment="时间戳"
    )

    Mon_Weight = Column(
        Float,               # TEXT 类型，适用于长文本
        nullable=False,     # 不能为空
        comment="早晨的体重"
    )


    Eve_Weight = Column(
        Float,               # TEXT 类型，适用于长文本
        nullable=False,     # 不能为空
        comment="晚上的体重"
    )

    Max_Weight = Column(
        Float,               # TEXT 类型，适用于长文本
        nullable=False,     # 不能为空
        comment="最高的体重"
    )

    Min_Weight = Column(
        Float,               # TEXT 类型，适用于长文本
        nullable=False,     # 不能为空
        comment="最低的体重"
    )

    KCal_Input = Column(
        Float,               # TEXT 类型，适用于长文本
        nullable=False,     # 不能为空
        comment="卡路里输入"
    )    
    KCal_Output = Column(
        Float,               # TEXT 类型，适用于长文本
        nullable=False,     # 不能为空
        comment="卡路里输出"
    )


    # 定义 __repr__ 方法以便打印对象时有清晰的表示
    def __repr__(self):
        return (f"<Weight(id={self.id}, user='{self.user}', "
                f"Date='{self.Date})>")





# Pydantic 模型 (用于请求和响应)
class UserRead(BaseModel):
    id: uuid.UUID
    email: str
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    is_admin: bool = False

    class Config:
        from_attributes = True  # updated from orm_mode = True


class UserCreate(BaseModel):
    email: str
    password: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None


class UserUpdate(UserCreate):
    is_active: Optional[bool] = None
    is_superuser: Optional[bool] = None
    is_verified: Optional[bool] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    is_admin: Optional[bool] = None
