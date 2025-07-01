from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Đọc email đã đăng ký từ file
with open("test_email.txt", "r") as f:
    test_email = f.read().strip()

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 20)

def login():
    driver.get("http://localhost:8000/login")
    wait.until(EC.presence_of_element_located((By.NAME, "email"))).send_keys(test_email)
    driver.find_element(By.NAME, "password").send_keys("Password123")
    driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)
    time.sleep(2)
    print("🔐 Đã login.")

def test_search_product(keyword):
    driver.get("http://localhost:8000")
    try:
        wait.until(EC.presence_of_element_located((By.NAME, "keyword")))
        search_input = driver.find_element(By.NAME, "keyword")
        search_input.clear()

        # Gõ từng ký tự để mô phỏng người dùng
        for char in keyword:
            search_input.send_keys(char)
            time.sleep(0.15)

        print(f"🔎 Đã nhập: '{keyword}'")
        search_input.send_keys(Keys.RETURN)
        time.sleep(2)

        page_text = driver.page_source.lower()
        if "không tìm thấy" in page_text or "không có sản phẩm" in page_text:
            print(f"❌ Không tìm thấy sản phẩm với từ khóa '{keyword}'")
        elif "sản phẩm" in page_text or "giỏ hàng" in page_text:
            print(f"✅ Có kết quả với từ khóa '{keyword}'")
        else:
            print(f"⚠️ Kết quả không rõ ràng với từ khóa '{keyword}'")
    except Exception as e:
        print(f"❌ Lỗi khi tìm kiếm với từ khóa '{keyword}':", e)

try:
    login()

    print("\n🔎 TC1: Tìm kiếm với từ khóa chính xác")
    test_search_product("Bản nâng cấp")

    print("\n🔎 TC2: Tìm kiếm với từ khóa gần đúng (không dấu)")
    test_search_product("ban nang cap")

    print("\n🔎 TC3: Tìm kiếm với từ khóa không tồn tại")
    test_search_product("xyzabc123")

    print("\n🔎 TC4: Tìm kiếm khi không nhập từ khóa")
    test_search_product("")

finally:
    driver.quit()
