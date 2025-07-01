import os
import time

def take_screenshot(driver, output_dir, name=None):
    """Take a full-page screenshot of all open tabs and save to the specified output_dir."""
    os.makedirs(output_dir, exist_ok=True)
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
        # Name screenshots as <testname>_screenshot_1.png, ...
        tab_name = f"{name}_screenshot_{index + 1}.png"
        filepath = os.path.join(output_dir, tab_name)
        driver.save_screenshot(filepath)
        screenshots.append(filepath)

    # Switch back to the original window
    driver.switch_to.window(original_window)
    return screenshots