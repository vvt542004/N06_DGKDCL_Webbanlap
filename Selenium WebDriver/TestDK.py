from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, random

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 20)

def run_test_case(name, email, password, confirm_password, expect_success):
    driver.get("http://localhost:8000/register")
    wait.until(EC.presence_of_element_located((By.NAME, "name"))).clear()
    driver.find_element(By.NAME, "email").clear()
    driver.find_element(By.NAME, "password").clear()
    driver.find_element(By.NAME, "password_confirmation").clear()

    # Điền dữ liệu
    if name:
        driver.find_element(By.NAME, "name").send_keys(name)
    if email:
        driver.find_element(By.NAME, "email").send_keys(email)
    if password:
        driver.find_element(By.NAME, "password").send_keys(password)
    if confirm_password:
        driver.find_element(By.NAME, "password_confirmation").send_keys(confirm_password)

    driver.find_element(By.NAME, "password_confirmation").send_keys(Keys.RETURN)
    time.sleep(2)

    page_source = driver.page_source.lower()
    current_url = driver.current_url.lower()

    # Xác định thành công
    success_keywords = ["dashboard", "verify", "xác minh", "logout", "đăng xuất"]
    is_success = any(k in page_source or k in current_url for k in success_keywords)

    if is_success == expect_success:
        print(f"✅ Test {'PASS' if expect_success else 'FAIL hợp lý'}")
    else:
        print(f"❌ Test {'không đúng mong đợi' if expect_success else 'FAIL không đúng'}")
        print("   Trang hiện tại:", current_url)
        print(driver.page_source[:500])

# === Các TEST CASE không hợp lệ ===
print("🚫 [TC1] Email không hợp lệ:")
run_test_case("User A", "email_sai", "Password123", "Password123", expect_success=False)

print("🚫 [TC2] Mật khẩu < 8 kí tự:")
run_test_case("User B", f"test{random.randint(1000,9999)}@mail.com", "12345", "12345", expect_success=False)

print("🚫 [TC3] Mật khẩu không khớp:")
run_test_case("User C", f"test{random.randint(1000,9999)}@mail.com", "Password123", "Password321", expect_success=False)

print("🚫 [TC4] Không nhập tên:")
run_test_case("", f"test{random.randint(1000,9999)}@mail.com", "Password123", "Password123", expect_success=False)

print("🚫 [TC5] Không nhập email:")
run_test_case("User E", "", "Password123", "Password123", expect_success=False)

print("🚫 [TC6] Không nhập mật khẩu:")
run_test_case("User F", f"test{random.randint(1000,9999)}@mail.com", "", "", expect_success=False)

# === Test hợp lệ ===
valid_email = f"testuser{random.randint(1000,9999)}@example.com"
print("✅ [TC7] Đăng ký hợp lệ:")
run_test_case("Test User", valid_email, "Password123", "Password123", expect_success=True)

# Nếu thành công thì lưu email lại để test sau dùng
with open("test_email.txt", "w") as f:
    f.write(valid_email)

print("📌 Đã hoàn tất tất cả test case.")

driver.quit()
