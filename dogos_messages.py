import numpy as np
import pandas as pd
import regex as re

def main():
    txts = [ 
        ("chapter4/chats/WhatsApp Chat with ✨ マン　カリーン　チンゲ.txt", "Pedro"),
        ("chapter4/chats/WhatsApp Chat with Fellow King Dio Brando.txt", "Brandon"),
        ("chapter4/chats/WhatsApp Chat with バラリア.txt", "Valeria")
        ]
    my_message = "Luis ドゴ: "
    messages = []
    days = []
    people = []
    for txt in txts:
        with open(txt[0], 'r', encoding='utf-8') as file:
            for line in file:
                if my_message in line:
                    pattern = f'{my_message}(.*)'
                    message = re.search(pattern, my_message)
                    day = line[:7]
                    messages.append(message)
                    days.append(day)
                    people.append(txt[1])
    df = pd.DataFrame(
        {
        "content" : messages,
        "day" : days,
        "person" : people,
        }
    )
    return df

if __name__ == "__main__":
    df = main()
    print(df.describe())

