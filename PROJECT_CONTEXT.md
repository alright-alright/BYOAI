# Build Your Own AI (BYOAI)

<img src="./assets/logo.png" alt="BYOAI Logo" width="200" />

## Overview

BYOAI is a modular and customizable AI system inspired by Gentoo, allowing users to build and integrate various AI models efficiently. This project aims to democratize AI by making it accessible and easy to use for all.

## Vision and Goal

Our vision for BYOAI is to create a platform that enables users to easily manage, customize, and deploy AI models. Inspired by the modularity and flexibility of Gentoo Linux, BYOAI aims to provide a robust and user-friendly environment for AI enthusiasts and developers.

### Key Features

- **Dynamic Model Installation:** Browse, select, and install models through a CLI interface.
- **User-Friendly CLI:** Commands for searching, listing, installing, and updating models.
- **Model Repository and Index:** A centralized repository with an index of available models and their metadata.
- **Modular Architecture:** Support for bundling multiple models together and optimizing them for different hardware configurations.
- **Community Contributions:** A system where users can contribute new models to the repository, ensuring quality and compatibility.

## Current Status

We have created a proof of concept that can quickly and easily install and run a wide variety of AI models from external sources like Hugging Face. The CLI tool now supports:

- Listing available models
- Searching for specific models
- Installing models dynamically
- Enhanced formatting for better user experience

## Usage

### List all Available Models

To list all available models:

python byoai-core/byoai-cli.py list

### Search for a Specific Model

To search for a specific model:

python byoai-core/byoai-cli.py search <query>

### Install a Specific Model

To install a specific model:

python byoai-core/byoai-cli.py install <model_name>

### Interactive CLI Usage

You can now use the interactive CLI tool to browse, select, and install models with enhanced formatting:

1. List all available models: 

python byoai-core/byoai-cli.py list

2. Search for a specific model:

python byoai-core/byoai-cli.py search <query>

3. Install a specific model:

python byoai-core/byoai-cli.py install <model_name>

## Repository Structure

BYOAI/
│
├── byoai-core/
│   ├── byoai-cli.py
│   ├── byoai-pm.py
│   ├── index.json
│   └── update_index.py
│
├── modules/
│   ├── huggingface/
│   └── tensorflow/
│
├── assets/
│   └── logo.png
│
├── fetch_tf_models.py
├── PROJECT_CONTEXT.md
└── README.md

## Next Steps

### Expand Model Library

- Identify and integrate more interesting AI models to showcase the versatility of BYOAI.
- Index TensorFlow libraries and ensure compatibility with our CLI tool.

### Modular Model Bundling

- Develop a method to bundle multiple models together into new modular models.

### Optimization and Recompilation

- Investigate ways to optimize and recompile models for different hardware configurations, enhancing performance and compatibility.

### Interactive and User-Friendly Interface

- Beautify the output and add interactive features to enhance user experience.

## Contributions

We welcome contributions! Please see our CONTRIBUTING.md for details.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
