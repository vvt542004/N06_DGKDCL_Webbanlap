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

def login():
    driver.get("http://localhost:8000/login")
    wait.until(EC.presence_of_element_located((By.NAME, "email"))).send_keys(test_email)
    driver.find_element(By.NAME, "password").send_keys("Password123")
    driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)
    time.sleep(2)
    print("🔐 Đã login.")

def add_product_to_cart():
    driver.get("http://localhost:8000/shop")
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "fa-shopping-cart")))
    cart_icons = driver.find_elements(By.CLASS_NAME, "fa-shopping-cart")
    if not cart_icons:
        print("❌ Không tìm thấy sản phẩm để thêm vào giỏ.")
        return False
    cart_link = cart_icons[0].find_element(By.XPATH, "./parent::a")
    driver.execute_script("arguments[0].click();", cart_link)
    print("🛒 Đã thêm sản phẩm vào giỏ.")
    time.sleep(2)
    return True

def proceed_to_checkout():
    driver.get("http://localhost:8000/cart")
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".shoping__checkout")))
    checkout_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.primary-btn[href*='checkout']")))
    driver.execute_script("arguments[0].click();", checkout_btn)
    print("➡️ Đã vào trang thanh toán.")
    time.sleep(2)

def run_checkout_test(address, email, phone, note="Giao hàng giờ hành chính"):
    print(f"🧪 BẮT ĐẦU TEST: {address=}, {email=}, {phone=}")
    wait.until(EC.presence_of_element_located((By.NAME, "address")))

    # Điền thông tin form
    driver.find_element(By.NAME, "address").clear()
    driver.find_element(By.NAME, "address").send_keys(address)

    driver.find_element(By.NAME, "email").clear()
    driver.find_element(By.NAME, "email").send_keys(email)

    driver.find_element(By.NAME, "phone").clear()
    driver.find_element(By.NAME, "phone").send_keys(phone)

    driver.find_element(By.NAME, "note").clear()
    driver.find_element(By.NAME, "note").send_keys(note)

    # Submit
    submit = driver.find_element(By.CSS_SELECTOR, "button[type='submit'][name='checkout']")
    driver.execute_script("arguments[0].scrollIntoView();", submit)
    time.sleep(1)
    submit.click()
    time.sleep(2)

    # Kiểm tra kết quả
    body = driver.page_source.lower()
    if (
        "đặt hàng thành công" in body
        or "cảm ơn" in body
        or "đơn hàng của bạn" in body
        or "thanh toán thành công" in body
        or "đã nhận được đơn hàng" in body
    ):
        print("✅ Đặt hàng thành công.")
    elif "text-danger" in body:
        print("❌ Có lỗi xảy ra khi thanh toán.")
        errors = driver.find_elements(By.CLASS_NAME, "text-danger")
        for e in errors:
            if e.text.strip():
                print("   ⚠️", e.text.strip())
    else:
        print("⚠️ Không rõ trạng thái thanh toán.")
        print(driver.page_source[:500])

# Thực thi các test case
try:
    login()
    if add_product_to_cart():
        proceed_to_checkout()

        # TC1: Không nhập địa chỉ
        run_checkout_test("", test_email, "0909999999")

        # TC2: Không nhập email
        proceed_to_checkout()
        run_checkout_test("123 Đường ABC", "", "0909999999")

        # TC3: Không nhập số điện thoại
        proceed_to_checkout()
        run_checkout_test("123 Đường ABC", test_email, "")

        # TC4: Nhập đầy đủ hợp lệ
        proceed_to_checkout()
        run_checkout_test("123 Đường ABC", test_email, "0909999999")

finally:
    driver.quit()
