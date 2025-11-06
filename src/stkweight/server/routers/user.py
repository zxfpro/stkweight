# app/routers/admin.py
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi import FastAPI, Header


import time
from contextlib import contextmanager
from sqlalchemy.orm import sessionmaker


@contextmanager
def create_session(engine):
    # 5. 创建会话 (Session)
    # Session 是与数据库交互的主要接口，它管理着你的对象和数据库之间的持久化操作
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        yield session

    except Exception as e:
        print(f"An error occurred: {e}")
        session.rollback() # 发生错误时回滚事务
    finally:
        session.close() # 关闭会话，释放资源


# 模拟获取当前用户的依赖项
async def get_current_user(x_token: str = Header(...)):
    if x_token not in ["1234", "5678"]:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid X-Token header"
        )
    return {"username": "admin", "roles": ["user", "admin"]}


router = APIRouter(
    tags=["users"], dependencies=[Depends(get_current_user)]  # 统一的依赖项列表
)


@router.get("/dashboard")
async def get_user(user_info: dict = Depends(get_current_user)):
    pass
    return {"message": "Welcome to the admin dashboard!"}


@router.get("/get_dash")
async def get_dash(user_info: dict = Depends(get_current_user)):
    # 查询uer 的先关数据
    

    # 然后返回html信息
    return {"message": "Welcome to the admin dashboard!"}
