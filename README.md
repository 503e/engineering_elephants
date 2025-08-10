# FIRST LEGO League Pybricks Spike Prime Project

This project contains Python code for a LEGO Spike Prime hub running [Pybricks](https://pybricks.com/).

## Prerequisites

Before starting, make sure you have:

- Python 3.8 or later installed
- [pip](https://pip.pypa.io/) package manager
- A LEGO Spike Prime hub with Pybricks firmware installed
- [pybricksdev](https://github.com/pybricks/pybricksdev) installed in your Python environment
- (Optional) [Visual Studio Code](https://code.visualstudio.com/) with the Python extension

---

## 1. Create a Virtual Environment

It’s recommended to run this project in a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 2. Install Requirements

Once the virtual environment is active, install dependencies:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## 3. Running the Project

In order to run PyBrick programs, Pybrick firmware must first be installed (see below), and the Spike hub must be turned on. The following two methods can be used to connect and run the program using bluetooth. Once the program is run on the hub, you can re-run by short-pressing the hub button. 

### A. From the Command Line

```bash
pybricksdev run ble hello_world.py
```

### B. From VS Code

You can run a program from within VS Code by pressing `F5` or the green play button on the debug tab.

## 4. Helpful Tips

- List connected hubs:

```bash
pybricksdev devices
```

- Install Pybricks firmware:
Follow the official [Pybricks firmware guide](https://pybricks.com/install/).