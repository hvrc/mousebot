import os
import time

def take_screenshot(driver, name=None):
    """Take a full-page screenshot of all open tabs and save to screenshots/ directory."""
    screenshots_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'screenshots')
    os.makedirs(screenshots_dir, exist_ok=True)
    timestamp = time.strftime('%Y%m%d_%H%M%S')
    if not name:
        name = f'screenshot_{timestamp}'
    else:
        name = f'{name}_{timestamp}'

    screenshots = []
    original_window = driver.current_window_handle
    window_handles = driver.window_handles

    for index, handle in enumerate(window_handles):
        driver.switch_to.window(handle)
        # Ensure the page is fully loaded
        time.sleep(0.5)
        # Append tab index to filename to differentiate screenshots
        tab_name = f"{name}_tab_{index + 1}.png"
        filepath = os.path.join(screenshots_dir, tab_name)
        driver.save_screenshot(filepath)
        screenshots.append(filepath)

    # Switch back to the original window
    driver.switch_to.window(original_window)
    return screenshots