import pytest

def main():
    pytest.main([
        "-s",                                   # don't capture output
        "--html=reports/report.html",           # generate HTML report
        "--no-header",                          # remove pytest header
        "--tb=no",                             # disable traceback
        "-q",                                   # quiet mode
        "tests/test_login_001.py",              # login test
        "tests/test_reset_001.py"               # reset test
    ])

if __name__ == "__main__":
    main()