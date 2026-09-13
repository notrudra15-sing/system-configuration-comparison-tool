# System Configuration Comparison Tool

A Python + Flask web application that detects the configuration of the
computer running the application (System A), accepts a JSON
configuration from another computer (System B), and compares the two
systems.

## Features

-   Automatic System A detection
-   CPU, RAM, storage, OS, architecture, GPU, and CPU-frequency
    detection
-   System B JSON generation
-   JSON upload through a Flask dashboard
-   Match, mismatch, numeric-difference, and missing-field results
-   Detailed malformed-JSON error messages
-   Responsive dark-themed dashboard

## Project Structure

``` text
Spec Comparison/
├── app.py
├── main.py
├── generate_config.py
├── system_b.json
├── README.md
├── templates/
│   └── index.html
└── static/
    └── style.css
```

## How It Works

**System A:** The computer running Flask is detected automatically using
Python libraries and OS-specific methods.

**System B:** Another computer's configuration is stored in JSON and
uploaded through the dashboard.

**Comparison:** Shared fields are compared. Equal values produce
`Match`, different numeric values produce a rounded numerical
difference, different non-numeric values produce a `Mismatch`, and
missing System B fields produce `Not found in System B`.

## Problems Faced and Solutions

### 1. Installing `psutil` on Arch/Omarchy

**Problem:** `pip install psutil` produced the PEP 668
`externally-managed-environment` error.

**Solution:** The Arch package manager was used:

``` bash
sudo pacman -S python-psutil
```

### 2. Flask port 5000 was already in use

**Problem:** Flask's default port was occupied.

**Solution:** The application was moved to port 5001:

``` python
app.run(port=5001)
```

### 3. `system_b.json` FileNotFoundError

**Problem:** The application initially tried to read `system_b.json`
from the local project directory, causing a `FileNotFoundError` when it
was not at the expected path.

**Solution:** System B was changed to a browser-uploaded JSON file
rather than a file automatically read from the same machine.

### 4. System B needed to represent another computer

**Problem:** Reading a local JSON file did not properly demonstrate
comparison between two computers.

**Solution:** `generate_config.py` was created so another computer can
generate its configuration as a portable JSON file.

### 5. CPU frequency is dynamic

**Problem:** CPU frequency can change between measurements.

**Solution:** CPU frequency is treated as a numeric snapshot and its
difference is rounded to two decimal places.

### 6. Floating-point output was unnecessarily long

**Problem:** Calculated values sometimes contained excessive decimal
digits.

**Solution:** Relevant values and comparison differences use
`round(value, 2)`.

### 7. Malformed JSON could crash the app

**Problem:** Invalid JSON caused `json.load()` to raise
`JSONDecodeError`.

**Solution:** JSON loading was placed inside `try/except`, allowing the
application to continue running and report the error.

### 8. The JSON error message was too generic

**Problem:** The initial message only said `Invalid JSON file.`

**Solution:** The final message includes the parser's description, line
number, and column number, for example:

``` text
Invalid JSON file: ... (line 5, column 12)
```

### 9. No file selected

**Problem:** The upload form needed to prevent submission without a
file.

**Solution:** The HTML file input uses `required`, so the browser
handles this before the request reaches Flask.

### 10. Empty JSON file

**Problem:** An empty System B configuration contains no fields.

**Observed behavior:** The app stayed alive and reported
`Not found in System B` for System A fields.

**Decision:** This was accepted as reasonable prototype behavior because
the application did not crash and clearly showed that System B contained
no matching fields.

### 11. Wrong data type in a JSON value

**Problem:** A JSON value could have an unexpected type, such as:

``` json
"Physical Cores": "potato"
```

**Solution:** The comparison logic checks that both values are numeric
before subtraction. The example is therefore reported as a mismatch
rather than causing a calculation error.

### 12. Comparison colors were initially inline

**Problem:** Match, difference, and mismatch colors were temporarily
written directly in the HTML.

**Solution:** They were moved into `.match`, `.difference`, and
`.mismatch` CSS classes, keeping HTML structure separate from
presentation.

### 13. CSS changes appeared not to work

**Problem:** Updated CSS did not immediately appear in the browser.

**Solution:** Browser caching was identified as the cause; refreshing
the page loaded the updated stylesheet.

### 14. Dashboard needed smaller-screen support

**Problem:** Side-by-side system cards could become cramped on small
screens.

**Solution:** A media query stacks the cards vertically below 700px.

## Technologies Used

-   Python
-   Flask
-   psutil
-   platform
-   subprocess
-   HTML
-   CSS
-   JSON
-   Jinja

## Running the Project

On Arch/Omarchy, install the required packages:

``` bash
sudo pacman -S python-psutil python-flask
```

Run:

``` bash
python app.py
```

Open:

``` text
http://127.0.0.1:5001
```

To compare another computer, run `generate_config.py` on that computer,
transfer the generated JSON file, and upload it through the dashboard.

## Future Improvements

-   Improve GPU detection across operating systems
-   Replace deprecated Windows WMIC commands with modern methods
-   Support multiple storage drives
-   Add richer comparison summaries
-   Export comparison results
-   Add stronger JSON schema validation
-   Add automated tests

## Project Status

**Working Prototype**

The main detection, JSON generation, upload, comparison, error handling,
responsive dashboard, and edge-case testing workflows are implemented
and working.
