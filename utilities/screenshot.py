import os
import time

# take a fullscreen screenshot of all tabs in the browser
def take_screenshot(driver, output_dir, name=None):
    os.makedirs(output_dir, exist_ok=True)
    timestamp = time.strftime('%Y%m%d_%H%M%S')
    if not name: name = f'screenshot_{timestamp}'
    else: name = f'{name}_{timestamp}'
    screenshots = []
    original_window = driver.current_window_handle
    window_handles = driver.window_handles

    for index, handle in enumerate(window_handles):
        driver.switch_to.window(handle)
        time.sleep(0.5)
        tab_name = f"{name}_screenshot_{index + 1}.png"
        filepath = os.path.join(output_dir, tab_name)
        driver.save_screenshot(filepath)
        screenshots.append(filepath)

    driver.switch_to.window(original_window)
    return screenshots