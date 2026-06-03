from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from src.models import Base, TodoItem
from prometheus_fastapi_instrumentator import Instrumentator

# Veritabanını kuruyoruz
engine = create_engine("sqlite:///./sql_app.db", connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

app = FastAPI()
Instrumentator().instrument(app).expose(app)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 1. Görev Ekleme (POST)
@app.post("/todos/")
def create_todo(title: str, db: Session = Depends(get_db)):
    yeni_gorev = TodoItem(title=title)
    db.add(yeni_gorev)
    db.commit()
    return {"mesaj": "Görev başarıyla eklendi!", "gorev": title}

# 2. Görevleri Listeleme (GET)
@app.get("/todos/")
def list_todos(db: Session = Depends(get_db)):
    gorevler = db.query(TodoItem).all()
    return gorevler

# 3. Görevi Tamamlandı İşaretleme (PUT)
@app.put("/todos/{todo_id}/complete")
def complete_todo(todo_id: int, db: Session = Depends(get_db)):
    gorev = db.query(TodoItem).filter(TodoItem.id == todo_id).first()
    if not gorev:
        raise HTTPException(status_code=404, detail="Görev bulunamadı")
    gorev.completed = True
    db.commit()
    return {"mesaj": "Görev tamamlandı!", "gorev_id": todo_id}

# 4. Görevi Silme (DELETE)
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    gorev = db.query(TodoItem).filter(TodoItem.id == todo_id).first()
    if not gorev:
        raise HTTPException(status_code=404, detail="Görev bulunamadı")
    db.delete(gorev)
    db.commit()
    return {"mesaj": "Görev silindi!"}

import boto3

@app.get("/aws-health")
def check_aws_s3():
    # LocalStack üzerindeki sahte S3 servisine bağlanıyoruz
    s3 = boto3.client('s3', endpoint_url='http://localstack:4566', 
                      aws_access_key_id='test', aws_secret_access_key='test', region_name='us-east-1')
    try:
        s3.list_buckets()
        return {"status": "success", "message": "AWS S3 (LocalStack) bağlantısı başarılı!"}
    except Exception as e:
        return {"status": "error", "message": str(e)}