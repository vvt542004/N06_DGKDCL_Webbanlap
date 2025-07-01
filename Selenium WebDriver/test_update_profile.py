from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# Đọc email đã đăng ký từ file
with open("test_email.txt", "r") as f:
    test_email = f.read().strip()

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 20)

def slow_type(element, text, delay=0.15):
    for char in text:
        element.send_keys(char)
        time.sleep(delay)

def login():
    driver.get("http://localhost:8000/login")
    wait.until(EC.presence_of_element_located((By.NAME, "email"))).send_keys(test_email)
    driver.find_element(By.NAME, "password").send_keys("Password123")
    driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)
    time.sleep(2)
    print("🔐 Đã login.")

def update_profile(name, address, phone, upload_image=True, test_name=""):
    print(f"\n🧪 {test_name}")
    driver.get("http://localhost:8000/profile/edit")
    wait.until(EC.presence_of_element_located((By.ID, "name")))
    time.sleep(2)

    name_input = driver.find_element(By.ID, "name")
    email_input = driver.find_element(By.NAME, "email")
    address_input = driver.find_element(By.ID, "address")
    phone_input = driver.find_element(By.ID, "phone")

    # Xóa và nhập lại
    name_input.clear()
    address_input.clear()
    phone_input.clear()

    if name is not None:
        slow_type(name_input, name)
    if address is not None:
        slow_type(address_input, address)
    if phone is not None:
        slow_type(phone_input, phone)

    # Ảnh đại diện
    if upload_image:
        avatar_input = driver.find_element(By.ID, "avatar")
        avatar_path = os.path.abspath("Selenium WebDriver/ima/dd.webp")
        if os.path.exists(avatar_path):
            avatar_input.send_keys(avatar_path)
            print("🖼️ Đã upload ảnh.")
            time.sleep(1)

    # Gửi form
    driver.find_element(By.XPATH, "//button[contains(text(), 'Lưu thay đổi')]").click()
    time.sleep(2)

    # Kết quả
    errors = driver.find_elements(By.CLASS_NAME, "text-danger")
    if errors:
        print("❌ Có lỗi:")
        for e in errors:
            if e.text.strip():
                print("   ⚠️", e.text.strip())
    else:
        text = driver.page_source.lower()
        if "cập nhật thành công" in text or "hồ sơ" in text:
            print("✅ Cập nhật thành công.")
        else:
            print("⚠️ Không rõ kết quả.")
            print(driver.page_source[:500])

try:
    login()

    # TC1: Không nhập họ tên
    update_profile(name="", address="123 Đường ABC", phone="0900000000", test_name="TC1: Không nhập họ tên")

    # TC2: Không nhập địa chỉ
    update_profile(name="Test User", address="", phone="0900000000", test_name="TC3: Không nhập địa chỉ")

    # TC3: Không nhập số điện thoại
    update_profile(name="Test User", address="123 Đường ABC", phone="", test_name="TC4: Không nhập số điện thoại")

    # TC4: Nhập đầy đủ hợp lệ
    update_profile(name="Nguyễn Selenium", address="456 Đường Tự Động", phone="0909999999", test_name="TC5: Nhập đầy đủ thông tin hợp lệ")

finally:
    driver.quit()
