from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Đọc email hợp lệ đã đăng ký từ file
with open("test_email.txt", "r") as f:
    valid_email = f.read().strip()

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 20)

def run_login_case(email, password, expect_success):
    driver.get("http://localhost:8000/login")
    try:
        email_field = wait.until(EC.presence_of_element_located((By.NAME, "email")))
        password_field = driver.find_element(By.NAME, "password")

        # Clear và nhập lại thông tin
        email_field.clear()
        password_field.clear()

        if email:
            email_field.send_keys(email)
        if password:
            password_field.send_keys(password)

        password_field.send_keys(Keys.RETURN)
        time.sleep(2)

        current_url = driver.current_url.lower()
        page_source = driver.page_source.lower()

        success_keywords = ["dashboard", "logout", "đăng xuất"]
        is_success = any(k in current_url or k in page_source for k in success_keywords)

        if is_success == expect_success:
            print(f"✅ Test {'THÀNH CÔNG' if expect_success else 'LỖI hợp lệ'} (email={email}, password={'***' if password else ''})")
        else:
            print(f"❌ Sai kết quả mong đợi (email={email}, password={'***' if password else ''})")
            print(driver.page_source[:500])
    except Exception as e:
        print("❌ Lỗi khi thực hiện login:", e)

# === TEST CASE ===
print("🚫 [TC1] Email không tồn tại:")
run_login_case("khongton@abc.com", "Password123", expect_success=False)

print("🚫 [TC2] Mật khẩu sai với email hợp lệ:")
run_login_case(valid_email, "WrongPass123", expect_success=False)

print("🚫 [TC3] Bỏ trống email:")
run_login_case("", "Password123", expect_success=False)

print("🚫 [TC4] Bỏ trống mật khẩu:")
run_login_case(valid_email, "", expect_success=False)

print("🚫 [TC5] Bỏ trống cả email và mật khẩu:")
run_login_case("", "", expect_success=False)

print("🚫 [TC6] Email sai định dạng:")
run_login_case("abc@@@", "Password123", expect_success=False)

print("✅ [TC7] Email và mật khẩu hợp lệ:")
run_login_case(valid_email, "Password123", expect_success=True)

print("📌 Hoàn tất toàn bộ test case đăng nhập.")

driver.quit()
