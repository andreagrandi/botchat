import openai
import time
import os


OPENAI_API_KEY_1 = os.environ.get("OPENAI_API_KEY_1")
OPENAI_API_KEY_2 = os.environ.get("OPENAI_API_KEY_2")
CONVERSATION_ITERATIONS = 10
MAX_TOKENS = 120


def conversation(input_text):
    bot_1_response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "assistant", "content": input_text}
        ],
        max_tokens=MAX_TOKENS,
        presence_penalty=0.5,
        api_key=OPENAI_API_KEY_1,
    )

    print(f"BOT 1: {bot_1_response.choices[0].message.content}\n")

    bot_2_response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": bot_1_response.choices[0].message.content}
        ],
        max_tokens=MAX_TOKENS,
        presence_penalty=0.5,
        api_key=OPENAI_API_KEY_2,
    )

    print(f"BOT 2: {bot_2_response.choices[0].message.content}\n")
    
    return bot_2_response.choices[0].message.content


def main():
    # Start the conversation
    input_text = input("Please enter your message: ")
    for i in range(CONVERSATION_ITERATIONS):
        input_text = conversation(input_text)
        # There seems to be a limit of 3 requests/minute so with a delay of 12 seconds
        # each API call from different keys should be allowed.
        time.sleep(12)


if __name__ == '__main__':
    main()
