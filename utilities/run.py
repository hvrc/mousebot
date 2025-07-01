import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

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
    user_input = input()
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
    # Run all selected tests in a single pytest session, stop on first failure
    pytest_args = ['-c', 'config/pytest.ini', '--maxfail=1', '--exitfirst'] + [test_files[idx] for idx in selected]
    print("\nStarting test session...")
    result = pytest.main(pytest_args)
    print("\nTest session ended.")
    # Print the report folder location
    try:
        # Dynamically find the latest test_report_n folder in reports/
        reports_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'reports'))
        all_reports = [d for d in os.listdir(reports_dir) if d.startswith('test_report_')]
        if all_reports:
            latest = max(all_reports, key=lambda d: int(d.split('_')[-1]))
            report_folder = os.path.abspath(os.path.join(reports_dir, latest))
            print(f"\nReport generated at: {report_folder}")
        else:
            print("\nReport folder location could not be determined.")
    except Exception as e:
        print(f"\nReport folder location could not be determined. ({e})")
    input("\nPress [Enter] to exit.\n")
    # Browser will be closed by pytest fixture finalizer. No manual shutdown here.

if __name__ == "__main__":
    main()