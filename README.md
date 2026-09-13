# System Configuration Comparison Tool

A Python and Flask-based web application for detecting, comparing, and displaying system configurations from two computers.

## Project Overview

The System Configuration Comparison Tool automatically detects the specifications of the computer running the application (System A) and compares them with the specifications of another computer provided through a JSON configuration file (System B).

The project was developed as a hands-on project for the CSE111 EDU-Revolution initiative.

## Features

* Detects operating system and OS version
* Detects system architecture
* Detects CPU model
* Detects CPU frequency
* Detects physical and logical CPU cores
* Detects total RAM
* Detects total storage
* Detects GPU where possible
* Generates a portable JSON configuration for another computer
* Loads System B configuration through a web upload
* Compares System A and System B specifications
* Identifies matching and mismatching specifications
* Calculates numerical differences where applicable
* Handles invalid JSON files without crashing
* Provides a responsive web interface
* Uses separate CSS classes for comparison results

## Project Structure

```text
Spec Comparison/
├── README.md
├── app.py
├── main.py
├── generate_config.py
├── example_system_B.json
├── .gitignore
├── templates/
│   └── index.html
└── static/
    └── style.css
```

## File Description

* `app.py` — Flask application and web interface logic
* `main.py` — System information detection and comparison logic
* `generate_config.py` — Generates a JSON configuration containing the specifications of another computer
* `example_system_B.json` — Example System B configuration
* `templates/index.html` — HTML structure of the web interface
* `static/style.css` — Styling for the web interface
* `.gitignore` — Prevents generated Python files such as `__pycache__` from being tracked
* `README.md` — Project documentation

## How It Works

The application uses two systems for comparison.

### System A

System A is the computer that runs `app.py`.

The application automatically detects its specifications using Python libraries and operating-system information.

### System B

System B is represented by a JSON file generated from another computer.

`generate_config.py` detects the specifications of that computer and saves them in a JSON format. The JSON file can then be transferred to the computer running the application and uploaded through the web interface.

### Comparison

After the System B JSON file is uploaded, the application compares the available specifications between System A and System B.

* **Match** — Both systems have the same value.
* **Mismatch** — The values are different for non-numerical specifications.
* **Difference** — A numerical difference is calculated for numerical specifications.

The application displays the results directly on the web page.

## How to Run This App

### 1. Clone the repository

Run the following command in PowerShell or a terminal:

```bash
git clone https://github.com/notrudra15-sing/system-configuration-comparison-tool.git
```

Wait for the repository to finish cloning.

Then enter the project directory using:

```bash
cd system-configuration-comparison-tool
```

### 2. Install dependencies

The application requires Flask and psutil.

#### Linux / Arch Linux

```bash
sudo pacman -S python-flask python-psutil
```

#### Windows

```bash
python -m pip install flask psutil
```

### 3. Start the application

```bash
python app.py
```

The Flask application runs on port `5001`.

Open the following address in a web browser:

```text
http://127.0.0.1:5001
```

The computer running `app.py` becomes System A automatically.

### 4. Generate a System B configuration

On another computer, run:

```bash
python generate_config.py
```
