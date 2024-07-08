# BYOAI

## Overview
BYOAI is a modular and customizable AI system inspired by Gentoo, allowing users to build and integrate various AI models efficiently. This project aims to democratize AI by making it accessible and easy to use.

## Usage

### Install and Run GPT-2 Text Generation Script

1. Install the GPT-2 Text Generation Module:
   `python byoai-core/byoai-pm.py install gpt2_text_generation`
2. Run the GPT-2 Text Generation Script:
   `python modules/gpt2_text_generation.py 'Once upon a time'`

### Install and Run BERT NER Script

1. Install the BERT NER Module:
   `python byoai-core/byoai-pm.py install bert_ner`
2. Run the BERT NER Script:
   `python modules/bert_ner.py 'Albert Einstein was a theoretical physicist.'`

### Install and Run MobileNet Image Classification Script

1. Install the MobileNet Image Classification Module:
   `python byoai-core/byoai-pm.py install mobilenet_image_classification`
2. Run the MobileNet Image Classification Script:
   `python modules/mobilenet_image_classification.py path_to_your_image.jpg`

### Install and Run Text Classification Script

1. Install the Text Classification Module:
   `python byoai-core/byoai-pm.py install text_classification`
2. Run the Text Classification Script:
   `python modules/text_classification.py 'I really enjoyed this film'`

## Repository Structure
- `byoai-core/`: Core scripts and tools
- `modules/`: Directory for installed AI modules
- `repository/`: Directory for available AI modules

## Contributions
We welcome contributions! Please see our CONTRIBUTING.md for details.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.
