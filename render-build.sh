#!/usr/bin/env bash

# Install Python dependencies
pip install -r requirements.txt

# Install Playwright and Chromium
playwright install chromium
