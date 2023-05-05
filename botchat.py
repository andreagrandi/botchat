import openai
import os
import copy
import sys

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
CONVERSATION_ITERATIONS = 20
OPEN_AI_MODEL = "gpt-4"

format = {
    "green": "\033[32m",
    "cyan": "\033[96m",
    "yellow": "\033[93m",
    "bold": "\033[01m",
    "reset": "\033[0m",
}

def conversation(bot_1_system_message, bot_2_system_message, messages):
    input = copy.deepcopy(messages)
    role = ""
    COL_COUNTER_START = 7
    SOFT_MAX_COLS = 80
    col_counter = COL_COUNTER_START

    if len(messages) == 0 or messages[-1]["role"] == "user":
        role = "assistant"

        sys.stdout.write(
            format["green"]
            + format["bold"]
            + "BOT 1: "
            + format["reset"]
            + format["green"]
        )
        sys.stdout.flush()

        input.insert(0, {"role": "system", "content": bot_1_system_message})

    elif len(messages) > 0 and messages[-1]["role"] == "assistant":
        role = "user"

        sys.stdout.write(
            format["cyan"]
            + format["bold"]
            + "BOT 2: "
            + format["reset"]
            + format["cyan"]
        )
        sys.stdout.flush()

        input.insert(0, {"role": "system", "content": bot_2_system_message})

        for message in input:
            if message["role"] == "user":
                message["role"] = "assistant"
            elif message["role"] == "assistant":
                message["role"] = "user"

    response_content = ""

    for response in openai.ChatCompletion.create(
        model=OPEN_AI_MODEL,
        messages=input,
        presence_penalty=0.5,
        api_key=OPENAI_API_KEY,
        stream=True,
    ):
        if hasattr(response.choices[0].delta, "content"):
            delta = response.choices[0].delta.content
            response_content += delta
            sys.stdout.write(delta)
            sys.stdout.flush()

            col_counter += len(delta)
            if col_counter >= SOFT_MAX_COLS:
                sys.stdout.write("\n")
                col_counter = 0

    sys.stdout.write(format["reset"] + "\n\n")
    sys.stdout.flush()

    messages.append({"role": role, "content": response_content})

    return messages


def main():
    print(
        format["yellow"]
        + "\n~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~\n"
        + format["reset"]
    )

    print(format["yellow"] +
        """
        ██████╗░░█████╗░████████╗  ░█████╗░██╗░░██╗░█████╗░████████╗
        ██╔══██╗██╔══██╗╚══██╔══╝  ██╔══██╗██║░░██║██╔══██╗╚══██╔══╝
        ██████╦╝██║░░██║░░░██║░░░  ██║░░╚═╝███████║███████║░░░██║░░░
        ██╔══██╗██║░░██║░░░██║░░░  ██║░░██╗██╔══██║██╔══██║░░░██║░░░
        ██████╦╝╚█████╔╝░░░██║░░░  ╚█████╔╝██║░░██║██║░░██║░░░██║░░░
        ╚═════╝░░╚════╝░░░░╚═╝░░░  ░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░
""" + format["reset"]
    )

    print(
        format["yellow"]
        + "\n~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~\n"
        + format["reset"]
    )

    print("Please enter system messages for the bots.\n")
    bot_1_system_message = input(
        format["green"] + format["bold"] + "BOT 1" + format["reset"] + ": "
    )
    bot_2_system_message = input(
        format["cyan"] + format["bold"] + "BOT 2" + format["reset"] + ": "
    )

    if bot_2_system_message == "":
        bot_2_system_message = bot_1_system_message
        print("(Using the same system message for both)")

    print(
        format["yellow"]
        + "\n~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~\n\n"
        + format["reset"]
    )

    messages = []
    for i in range(CONVERSATION_ITERATIONS):
        messages = conversation(bot_1_system_message, bot_2_system_message, messages)


if __name__ == "__main__":
    main()
