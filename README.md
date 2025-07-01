# MouseBot for SoftMouse

This repo contains an automated selenium based test framework for SoftMouse.NET, that automates common workflows like logging in, importing data, creating matings, litters, pups, weaning pups and resetting colony data. These instructions are primarily for Windows based systems.

## Project Structure
```
mousebot/
  config/           # config and credentials files
  data/             # test data files (e.g. .xlsx, .csv files)
  pages/            # page object model classes
  reports/          # logs and screenshots
  tests/            # test scripts
  utilities/        # logger, screenshoter, runner, config reader
  requirements.txt  # python dependencies
  run.bat           # Windows batch script to run tests
  README.md         # This file
```

## Setup Instructions

**Clone the repository**

**Install Python 3.8+**

**Create and activate a virtual environment:**
   ```cmd
   python -m venv venv
   venv\Scripts\activate
   ```

**Install dependencies:**
   ```cmd
   pip install -r requirements.txt
   ```

**Configure your environment:**

Edit `config/config.ini` to match your environment variables.

Edit `config/credentials.ini` for your credentials.

Edit `tests/tests.txt` to control which tests run and in what order.

Place test data files in the `data/` directory.

## Running the Tests

### Interactive

Run the batch script:
```cmd
run.bat
```

You will be prompted to select a config file (e.g. dev, staging).

You will be prompted to select which tests to run (all or specific).

Test artifacts like logs, screenshots will be saved in a new folder under `reports/`.

### Manual

You can also run the runner directly:
```cmd
python utilities/run.py
```

Or run pytest directly:
```cmd
pytest -c config/pytest.ini tests/
```