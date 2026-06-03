from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.main import app, get_db
from src.models import Base
from tests.factories import TodoFactory

# Testler için geçici veritabanı
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_gorev_ekleme():
    response = client.post("/todos/?title=Test Gorevi 1")
    assert response.status_code == 200

def test_gorev_listeleme():
    response = client.get("/todos/")
    assert response.status_code == 200

def test_factory_boy_ile_veri_uretme():
    sahte_gorev = TodoFactory()
    response = client.post(f"/todos/?title={sahte_gorev.title}")
    assert response.status_code == 200

def test_gorev_tamamlama():
    # 1. Görevi oluştur
    client.post("/todos/?title=Tamamlanacak Gorev")
    
    # 2. Tüm görevleri listele ve listeye eklenen EN SON görevin ID'sini yakala
    gorevler = client.get("/todos/").json()
    gorev_id = gorevler[-1]["id"]
    
    # 3. O dinamik ID'yi kullanarak tamamlama işlemini yap
    response = client.put(f"/todos/{gorev_id}/complete")
    assert response.status_code == 200

def test_gorev_silme():
    # 1. Görevi oluştur
    client.post("/todos/?title=Silinecek Gorev")
    
    # 2. Tüm görevleri listele ve listeye eklenen EN SON görevin ID'sini yakala
    gorevler = client.get("/todos/").json()
    gorev_id = gorevler[-1]["id"]
    
    # 3. O dinamik ID'yi kullanarak silme işlemini yap
    response = client.delete(f"/todos/{gorev_id}")
    assert response.status_code == 200