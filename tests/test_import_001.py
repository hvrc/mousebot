import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

def test_import_workflow(driver, config):
    wait = WebDriverWait(driver, 20)

    assert "homepage" in driver.current_url.lower() or "home" in driver.current_url.lower()

    import_card = wait.until(
        EC.element_to_be_clickable((
            By.XPATH,
            "//p[text()='Import']/ancestor::div[contains(@class, 'MuiPaper-root')]"
        ))
    )
    import_card.click()

    wait.until(
        lambda driver: "import" in driver.current_url.lower() or driver.current_url.lower() != driver.current_url.lower()
    )
    time.sleep(2)

    assert "import" in driver.current_url.lower() or "import" in driver.title.lower()

    check_errors_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'process')]"))
    )
    check_errors_btn.click()
    time.sleep(2)