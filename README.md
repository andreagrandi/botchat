# botchat
A script to generate a conversation between two ChatGPT instances

## Requirements

- 2 OpenAI API keys
- create a Python virtual environment and `pip install -r requirements.txt`

## Usage

To use this script you need two (possibly from two different OpenAI accounts) OpenAI API keys and you must set them
as environment variables:

```bash
export OPENAI_API_KEY_1=your-api-key-1
export OPENAI_API_KEY_2=your-api-key-2
```

at this point just run

```bash
python botchat.py
```

you will be required to start a conversation like this:

```bash
Please enter your message: Start a conversation about pizza
```

# Limits

It seems that after a little bit, especially if the response from the previous request is truncated (due to the limit of tokens)
the other bot doesn't continue the "conversation" but it just tries to "complete" the previous sentence.
