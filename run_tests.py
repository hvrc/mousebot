import pytest
import os
import importlib

test_files = [
    "tests/test_login_001.py",
    "tests/test_import_001.py",
    "tests/test_mating_003.py",
    "tests/test_mating_004.py",
    "tests/test_litter_001.py",
    "tests/test_pups_001.py",
    "tests/test_pups_004.py",
    "tests/test_reset_001.py",
]

def print_test_suite(selected=None):
    print("\nTest suite:")
    for idx, test in enumerate(test_files):
        name = os.path.splitext(os.path.basename(test))[0]
        mark = " [X]" if selected and idx in selected else ""
        print(f"{idx}. {name}{mark}")

def main():
    print_test_suite()
    print("\nSelect test numbers to run separated by commas or 'a' for all:")
    user_input = input("user: ").strip()
    if user_input.lower() == 'a':
        selected = list(range(len(test_files)))
    else:
        try:
            selected = [int(x) for x in user_input.split(',') if x.strip().isdigit() and 0 <= int(x) < len(test_files)]
        except Exception:
            print("Invalid input. Exiting.")
            return
    if not selected:
        print("No valid tests selected. Exiting.")
        return
    print("\nRunning selected tests:")
    for idx in selected:
        print(f"- {os.path.splitext(os.path.basename(test_files[idx]))[0]}")
    # Build pytest args
    html_report = "reports/report_selected.html" if len(selected) > 1 else f"reports/report_{os.path.splitext(os.path.basename(test_files[selected[0]]))[0]}.html"
    pytest_args = [
        "-s",
        f"--html={html_report}",
        "--no-header",
        "--tb=no",
        "-q",
    ] + [test_files[idx] for idx in selected]
    print("\nStarting pytest session...")
    pytest.main(pytest_args)
    print("\nAll selected tests have been run. Report:", html_report)
    input("\nPress [Enter] to exit suite.\n")
    # After Enter, quit the browser
    try:
        conftest = importlib.import_module("tests.conftest")
        driver = conftest.get_global_driver()
        if driver:
            driver.quit()
            print("Browser closed.")
    except Exception as e:
        print(f"Could not close browser automatically: {e}")

if __name__ == "__main__":
    main()