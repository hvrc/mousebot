import sys
import os
import pytest

# set the path to include the parent directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# loads which tests to run from tests.txt
def load_test_files():
    tests_txt = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'tests', 'tests.txt'))
    test_files = []
    if os.path.exists(tests_txt):
        with open(tests_txt, 'r', encoding='utf-8') as f:
            for line in f:
                name = line.strip()
                if name and not name.startswith('#'):
                    if not name.endswith('.py'):
                        name = f"tests/{name}.py"
                    else:
                        name = f"tests/{name}"
                    test_files.append(name)
    else:
        print(f"tests.txt not found at {tests_txt}. Exiting.")
        sys.exit(1)
    return test_files

# print all tests
def print_test_suite(test_files, selected=None):
    print("\nTest suite:")
    for idx, test in enumerate(test_files):
        name = os.path.splitext(os.path.basename(test))[0]
        mark = " [X]" if selected and idx in selected else ""
        print(f"{idx}. {name}{mark}")

# select tests to run
# run tests using pytest
# set pytest arguments to exit if any test fails
# generate reports
# requires user input to fully exit session
def main():
    test_files = load_test_files()
    print_test_suite(test_files)
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

    pytest_args = ['-c', 'config/pytest.ini', '--maxfail=1', '--exitfirst'] + [test_files[idx] for idx in selected]
    print("\nStarting test session...")
    result = pytest.main(pytest_args)
    print("\nTest session ended.")
    try:
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

if __name__ == "__main__":
    main()