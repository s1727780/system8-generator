# System 8 Testflow Generator

A simple mouse and keyboard macro app built with Python. <br> 
Designed to simplify and standardize the generation of testflows using ABI System 8 Ulitmate.

## Features (MVP)
- Parse an excel file to obtain the desired testflow steps
- Perform mouse and keyboard macros to setup the steps
- Each step has:
    - Step number
	- Step name
	- Test type
	- Probe / pin count
	- Voltage
	- Probe +/- notes
	- General notes / description
- Allow for appending steps to an existing testflow.

---

## Tech Stack

| Layer       | Tech                     |
|------------|---------------------------|
| Language    | Python |
| Automation  | pyautogui |
| File parsing| openpyxl |
| Frontend    | tkinter |
| Packaging   | Inno |
| Deployment  | Windows 10/11 executable |

---

## Data Model

### Step

| Parameter		| Type                     |
|---------------|---------------------------|
| id (primary)	| int |
| name			| string |
| test_type		| enum (see below) |
| probe_pins	| enum (see below) |
| voltage		| enum (see below) |
| probe_plus	| string |
| probe_minus   | string |
| notes			| string |
| create_step	| bool	|

#### Enum - test_type 
- RESERVED: Reserved for steps included in the template <br>
- AMS-VI: Performing a VI test with the AMS module <br>
- AMS-Matrix: Performing a Matrix test with the AMS module <br>

#### Enum - probe_pins 
- N/A: Ignore the probe/pin count <br>
- 1 to 4 Probe: When using manual probes <br>
- 2 to 64 Clip: When using an IC clip (pin counts are multiples of two <br>

#### Enum - voltage 
- 2V
- 5V
- 10V
- 20V
- 50V

---

## Project Structure

system8-generator/ <br>
├── / <br>
├── src/ <br>
├── assets/ <br>
├── data/ <br>
├── scripts/ <br>
├── build/ <br>
├── venv/ <br>
├── installer/ <br>
└── README.md <br>

| Folder       | Contents                              | Notes                        |
| ------------ | ------------------------------------- | ---------------------------- |
| `src/`       | Main Python logic                     | Entry point in `__main__.py` |
| `assets/`    | Images/icons/static files             | Input only                   |
| `data/`      | Runtime-generated or downloaded files | Don't version-control        |
| `build/`     | PyInstaller or other build outputs    | Don't version-control        |
| `installer/` | `.iss` config, icons                  | Tied to Inno Setup builds    |
| `tests/`     | Unit tests                            | Optional but recommended     |
| `venv/`      | Virtual env                           | Ignore from git and VS       |


---

## Milestones

* [ ] Define MVP features (macro from CSV, mouse/keyboard actions, delays, logging)
* [ ] Set up project structure and initialize Git
* [ ] Implement CSV parser module
* [ ] Implement macro executor (using `pyautogui` or `pynput`)
* [ ] Add logging and fail-safe system (e.g., escape via mouse corner)
* [ ] Add CLI interface for selecting and running macros
* [ ] Add support for extended actions (e.g., hotkeys, scroll, key up/down)
* [ ] Add support for delays and repeat actions
* [ ] Add JSON/YAML macro format support (optional)
* [ ] Build GUI using Tkinter or PySimpleGUI
* [ ] Integrate GUI with macro engine
* [ ] Add error handling and user feedback in GUI
* [ ] Add basic unit tests (parser, macro engine)
* [ ] Package app using PyInstaller
* [ ] Test executable on Windows 10/11
* [ ] (Optional) Add config saving/history using SQLite
* [ ] (Optional) Add FastAPI backend for future remote/API control
* [ ] (Optional) Add scheduling or automation profiles
* [ ] (Optional) Digitally sign the executable for distribution


---

## Testing (TBD)

- Unit tests for task logic and validation
- Integration tests for API endpoints
- (Planned): CI with GitHub Actions

---

## Running the Project

### Prerequisites

- Python 3.13

### Instructions

```bash
# Clone the repo
git clone https://github.com/s1727780/system8-generator.git
cd system8-generator

# Setup environment
py -m venv .venv
.\.venv\Scripts\activate
py -m pip install -r requirements.txt

# Run project
py src\system8-macro.py
