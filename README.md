# Flask Application for Text-to-Speech and Query Response

This Flask application integrates ElevenLabs for text-to-speech (TTS) capabilities and LangChain's `Ollama` model to handle and respond to user queries. The application provides endpoints to generate audio responses from text queries and play generated audio.

## Features

- Generate and stream audio responses from text queries.
- Play custom text using specified voices and models.
- Use the `Ollama` model from LangChain for processing and responding to text queries.

## Requirements

- Python 3.9 or higher
- `mpv` media player for streaming audio

## Installation

### Step 1: Clone the Repository

```sh
git clone https://github.com/ELFAHIM96/RAG_Ollama_API.git
cd RAG_Ollama_API
```

### Step 2: Create a Virtual Environment

```sh
python -m venv envrag
source envrag/bin/activate  # On Windows use `envrag\Scripts\activate`
```
### Step 3: Install Dependencies

```sh
pip install -r requirements.txt
```

### Step 4: Install mpv Media Player
On Linux (Ubuntu/Debian)

```sh
sudo apt update
sudo apt install mpv
```

