# BYOAI Dependencies

<img src="./assets/logo.png" alt="BYOAI Logo" width="200" />

## Overview
This document lists all the dependencies required to run the BYOAI project and provides instructions on how to set up the environment.

## Dependencies

### Python
- **Python 3.12** or higher

### Python Packages
- **transformers**: For Hugging Face models
- **tensorflow**: For TensorFlow models
- **pillow**: For image processing
- **numpy**: For numerical operations
- **keras**: For using Keras with TensorFlow

### Other Tools
- **Git**: For version control

## Installation Instructions

### 1. Install Python
Make sure you have Python 3.12 or higher installed. You can download Python from [python.org](https://www.python.org/downloads/).

### 2. Set Up a Virtual Environment
It’s recommended to use a virtual environment to manage your dependencies.

Create a virtual environment:
`python3 -m venv venv`

Activate the virtual environment:
On Windows:
`venv\Scripts\activate`

On macOS/Linux:
`source venv/bin/activate`

### 3. Install Python Packages
Install the required Python packages using pip:
`pip install transformers tensorflow pillow numpy keras`

### 4. Install Git
Make sure Git is installed on your system. You can download Git from [git-scm.com](https://git-scm.com/).

## Additional Information

### Verifying the Installation
You can verify that the packages are installed correctly by running the following commands:
`python -c "import transformers; print(transformers.__version__)"`
`python -c "import tensorflow as tf; print(tf.__version__)"`
`python -c "import PIL; print(PIL.__version__)"`
`python -c "import numpy as np; print(np.__version__)"`
`python -c "import keras; print(keras.__version__)"`

### Updating Dependencies
To update the dependencies to their latest versions, you can use pip:
`pip install --upgrade transformers tensorflow pillow numpy keras`

### Managing Dependencies
You can export the list of dependencies to a `requirements.txt` file:
`pip freeze > requirements.txt`

To install dependencies from a `requirements.txt` file, use:
`pip install -r requirements.txt`

## Contribution Guidelines
Please see the CONTRIBUTING.md file for details on how to contribute to this project.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.
