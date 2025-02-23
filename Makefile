PYTHON = python3
PIP = pip3
PYTEST = pytest
SRC_DIR = src
TESTS_DIR = $(SRC_DIR)
REQUIREMENTS = requirements.txt
VENV_DIR = dsa_venv
VENV_ACTIVATE = $(VENV_DIR)/bin/activate


.DEFAULT_GOAL := help

help:
	@echo "Available commands:"
	@echo "  make venv          - Create a virtual environment"
	@echo "  make install       - Install dependencies in the virtual environment"
	@echo "  make test          - Run all tests"
	@echo "  make test-algorithms - Run tests for algorithms"
	@echo "  make test-data-structures - Run tests for data structures"
	@echo "  make clean         - Clean up temporary files"
	@echo "  make help          - Show this help message"

# Creating virtual environment
venv:
	@echo "Creating virtual environment..."
	$(PYTHON) -m venv $(VENV_DIR)
	@echo "Virtual environment created at $(VENV_DIR). Run 'source $(VENV_ACTIVATE)' to activate it."

# Install dependencies in the virtual environment
install: venv
	@echo "Installing dependencies..."
	. $(VENV_ACTIVATE) && $(PIP) install -r $(REQUIREMENTS)
	@echo "Dependencies installed."


# Run all tests
test:
	. $(VENV_ACTIVATE) && $(PYTEST) $(TESTS_DIR)

# Run tests for algorithms
test-algorithms:
	. $(VENV_ACTIVATE) && $(PYTEST) $(SRC_DIR)/algorithms

# Run tests for data structures
test-data-structures:
	. $(VENV_ACTIVATE) && $(PYTEST) $(SRC_DIR)/data_structures

# Clean up temporary files
clean:
	@echo "Cleaning up temporary files..."
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type d -name ".pytest_cache" -exec rm -r {} +
	find . -type d -name ".mypy_cache" -exec rm -r {} +
	@echo "Cleanup complete."


.PHONY: help install test test-algorithms test-data-structures clean