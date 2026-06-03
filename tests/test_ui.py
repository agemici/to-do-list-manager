from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def test_swagger_ui_loads():
    # Tarayıcıyı ekranda görünmeden arka planda çalıştırıyoruz (Headless)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    
    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        # API'mizin dokümantasyon sayfasına gidiyoruz
        driver.get("http://127.0.0.1:8000/docs")
        
        # Sayfa başlığında FastAPI/Swagger kelimelerinin geçtiğini doğruluyoruz
        assert "FastAPI" in driver.title or "Swagger" in driver.title
    finally:
        driver.quit()