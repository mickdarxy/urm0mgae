

from_morsecode = {".-": "a", "-...": "b", "-.-.": "c", "-..": "d", ".": "e", "..-.": "f", "--.": "g", "....": "h",
                        "..": "i", ".---": "j", "-.-": "k", ".-..": "l", "--": "m", "-.": "n", "---": "o", ".--.": "p",
                        "--.-": "q", ".-.": "r", "...": "s", "-": "t", "..-": "u", ".--": "w", "...-": "v", "-..-": "x",
                        "-.--": "y", "--..": "z", "--..--": ",", ".-.-.-": ".", "..--..": "?", "-.-.--": "!"}
to_morsecode = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....",
                      "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.",
                      "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "w": ".--", "v": "...-", "x": "-..-",
                      "y": "-.--", "z": "--..", ",": "--..--", ".": ".-.-.-", "?": "..--..", "!": "-.-.--"}


def message_to_morse(message):
    character_list = list()
    translated_message= []
for char in message.upper():
    character_list += char.lower

    morse_code = ""
    for char in character_list:
        if char == " ":
            translated_message.append('    ')
        elif char in to_morsecode:
            translated_message.append(morse
            if morse_code == "":
                morse_code += translated_char
            else:
                morse_code += f"{translated_char}"
        else:
            morse_code = f"Can't convert {char} to morse code"
            break
return morse_code


def morse_to_message(morse):
    splitted_morse = morse.split()
    empty_code = 0
    message = ""
    for part in splitted_morse:
        if part == "":
            empty_code += 1
            if empty_code == 3:
                message += " "
                empty_code = 0
        if part in to_morsecode:
            to_morsecode[char]
