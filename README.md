# botchat
A script to generate a conversation between two ChatGPT instances

## Requirements

- 1 OpenAI API key
- create a Python virtual environment and `pip install -r requirements.txt`

## Usage

To use this script you need an OpenAI API key and you must set it as an environment variable:

```bash
export OPENAI_API_KEY=your-api-key
```

At this point, just run:

```bash
python botchat.py
```

You will be required to provide system messages for both bots:

```bash
BOT 1: Start a conversation about pizza
BOT 2: Continue discussing pizza
```

The script will generate and display a conversation between the two bots.

## Limits

It seems that after a little bit, especially if the response from the previous request is truncated (due to the limit of tokens), the other bot doesn't continue the "conversation" but it just tries to "complete" the previous sentence.
