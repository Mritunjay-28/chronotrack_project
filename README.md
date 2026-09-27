# ChronoTrack

A command-line daily routine and habit tracker written in pure Python.

## Overview
ChronoTrack helps users plan and execute their day through structured time blocks. It validates schedule slots against time conflicts, tracks active windows, and audits completed tasks with color-coded feedback.

## Features
- Modular multi-file architecture.
- 24-hour time format validation and collision detection.
- ANSI-coded terminal schedule display.
- Post-slot completion audit.
- Daily adherence metrics and summary reporting.
- Automated unit test suite.

## Technologies Used
- Python 3 standard libraries: `json`, `datetime`, `unittest`, `sys`, `os`

## How to Run
1. Open terminal inside the project folder.
2. Run:
   ```bash
   python main.py