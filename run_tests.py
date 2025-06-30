import pytest

def main():
    pytest.main([
        "-s",
        "--html=reports/report.html",
        "--no-header",
        "--tb=no",
        "-q",
        "tests/test_login_001.py",
        # "tests/test_reset_001.py",
        # "tests/test_import_001.py",
        "tests/test_mating_004.py",
        # "tests/test_mating_003.py",
        # "tests/test_reset_001.py",
    ])

if __name__ == "__main__":
    main()