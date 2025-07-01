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

def count_cart_items():
    driver.get("http://localhost:8000/cart")
    time.sleep(3)
    items = driver.find_elements(By.CLASS_NAME, "shoping__cart__item")
    return len(items)

def test_cart():
    # TC1: Không thêm sản phẩm → giỏ hàng trống
    print("\n🧪 TC1: Không chọn sản phẩm → giỏ hàng phải trống")
    driver.get("http://localhost:8000/cart")
    time.sleep(2)
    items = count_cart_items()
    if items == 0:
        print("✅ Giỏ hàng đang trống.")
    else:
        print(f"❌ Giỏ hàng KHÔNG trống (có {items} sản phẩm).")

    # TC2: Thêm 1 sản phẩm
    print("\n🧪 TC2: Thêm 1 sản phẩm hợp lệ vào giỏ")
    driver.get("http://localhost:8000/shop")
    time.sleep(2)
    try:
        cart_icons = driver.find_elements(By.CLASS_NAME, "fa-shopping-cart")
        if not cart_icons:
            print("❌ Không tìm thấy biểu tượng giỏ hàng.")
            return

        first_link = cart_icons[0].find_element(By.XPATH, "./parent::a")
        driver.execute_script("arguments[0].click();", first_link)
        print("🛒 Đã thêm sản phẩm thứ 1 vào giỏ.")
        time.sleep(2)
    except Exception as e:
        print("⚠️ Lỗi khi thêm sản phẩm thứ 1:", e)

    driver.get("http://localhost:8000/cart")
    time.sleep(3)
    items = count_cart_items()
    if items >= 1:
        print("✅ Giỏ hàng có ít nhất 1 sản phẩm.")
    else:
        print(f"❌ Giỏ hàng chỉ có {items} sản phẩm (mong đợi: ≥1).")

    # TC3: Thêm nhiều sản phẩm
    print("\n🧪 TC3: Thêm nhiều sản phẩm khác nhau (3 sản phẩm bất kỳ)")
    for i in range(1, 4):
        driver.get("http://localhost:8000/shop")
        time.sleep(2)
        try:
            cart_icons = driver.find_elements(By.CLASS_NAME, "fa-shopping-cart")
            if len(cart_icons) <= i:
                print(f"⚠️ Không đủ sản phẩm tại vị trí thứ {i+1}")
                continue

            product_link = cart_icons[i].find_element(By.XPATH, "./parent::a")
            driver.execute_script("arguments[0].click();", product_link)
            print(f"🛒 Đã thêm sản phẩm thứ {i+1} vào giỏ.")
            time.sleep(2)
        except Exception as e:
            print(f"⚠️ Lỗi khi thêm sản phẩm thứ {i+1}: {e}")

    driver.get("http://localhost:8000/cart")
    time.sleep(4)
    items = count_cart_items()
    expected = 4
    if items >= expected:
        print(f"✅ Giỏ hàng có đủ sản phẩm (mong đợi: {expected})")
    else:
        print(f"❌ Giỏ hàng chỉ có {items} sản phẩm (mong đợi: {expected})")

try:
    login()
    test_cart()
finally:
    driver.quit()
