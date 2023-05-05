import openai
import time
import os


OPENAI_API_KEY_1 = os.environ.get("OPENAI_API_KEY_1")
OPENAI_API_KEY_2 = os.environ.get("OPENAI_API_KEY_2")
CONVERSATION_ITERATIONS = 10
OPEN_AI_MODEL = "gpt-4"


def conversation(input_text, original_context):
    if input_text != original_context:
        message = original_context + " " + input_text
    else:
        message = input_text

    bot_1_response = openai.ChatCompletion.create(
        model=OPEN_AI_MODEL,
        messages=[
            {"role": "assistant", "content": message}
        ],
        presence_penalty=0.5,
        api_key=OPENAI_API_KEY_1,
    )

    print(f"BOT 1: {bot_1_response.choices[0].message.content}\n")

    message = original_context + bot_1_response.choices[0].message.content

    bot_2_response = openai.ChatCompletion.create(
        model=OPEN_AI_MODEL,
        messages=[
            {"role": "user", "content": message}
        ],
        presence_penalty=0.5,
        api_key=OPENAI_API_KEY_2,
    )

    print(f"BOT 2: {bot_2_response.choices[0].message.content}\n")

    return bot_2_response.choices[0].message.content


def main():
    # Start the conversation
    input_text = input("Please enter your message: ")
    original_input = input_text

    for i in range(CONVERSATION_ITERATIONS):
        input_text = conversation(input_text=input_text, original_context=original_input)
        # There seems to be a limit of 3 requests/minute so with a delay of 10 seconds
        # each API call from different keys should be allowed.
        time.sleep(10)


if __name__ == '__main__':
    main()
