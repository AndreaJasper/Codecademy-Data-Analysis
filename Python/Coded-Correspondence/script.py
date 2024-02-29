alphabet = "abcdefghijklmnopqrstuvwxyz"
message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"

translated_message = ""

for char in message:
    if char in alphabet:
        char_value = alphabet.find(char)
        translated_message += alphabet[(char_value + 10) % 26]
    else:
        translated_message += char

print(translated_message)

message_for_v = "Hey, thanks for showing me this. I can't wait to try it out myself"
translated_message_for_v = ""

for char in message:
    if char in alphabet:
        char_value = alphabet.find(char)
        translated_message_for_v += alphabet[(char_value - 10) % 26]
    else:
        translated_message_for_v += char

print(translated_message_for_v)

def caesar_decode(message, offset):
    decoded_message = ""

    for char in message:
        if char in alphabet:
            char_value = alphabet.find(char)
            decoded_message += alphabet[(char_value + offset) % 26]
        else:
            decoded_message += char

    return decoded_message

def caesar_encode(message, offset):
    encoded_message = ""

    for char in message:
        if char in alphabet:
            char_value = alphabet.find(char)
            encoded_message += alphabet[(char_value - offset) % 26]
        else:
            encoded_message += char

    return encoded_message

message_one = "jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud"
print(caesar_decode(message_one, 10))

message_two = "bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!"
print(caesar_decode(message_two, 14))

brute_force_message = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."

for i in range(1, 26):
  print("Offset: {}".format(i))
  print("\t {}".format(caesar_decode(brute_force_message, i)))

def vigenere_decode(message, keyword):
  keyword_phrase = ""
  keyword_index = 0

  for character in message:
    if keyword_index >= len(keyword):
      keyword_index = 0
    if character in alphabet:
      keyword_phrase += keyword[keyword_index]
      keyword_index += 1
    else:
      keyword_phrase += character

  decoded_message = ""

  for i in range(len(message)):
    if message[i] in alphabet:
      old_character_index = alphabet.find(message[i])
      offset_index = alphabet.find(keyword_phrase[i])
      new_character = alphabet[(old_character_index + offset_index) % 26]
      decoded_message += new_character
    else:
      decoded_message += message[i]

  return decoded_message

vigenere_message = "txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztcgcexxch!"
vigenere_keyword = "friends"

print(vigenere_decode(vigenere_message, vigenere_keyword))

def vigenere_encode(message, keyword):
  keyword_phrase = ""
  keyword_index = 0

  for character in message:
    if keyword_index >= len(keyword):
      keyword_index = 0
    if character in alphabet:
      keyword_phrase += keyword[keyword_index]
      keyword_index += 1
    else:
      keyword_phrase += character

  encoded_message = ""

  for i in range(len(message)):
    if message[i] in alphabet:
      old_character_index = alphabet.find(message[i])
      offset_index = alphabet.find(keyword_phrase[i])
      new_character = alphabet[(old_character_index - offset_index) % 26]
      encoded_message += new_character
    else:
      encoded_message += message[i]

  return encoded_message

vigenere_message_for_v = "thanks for teaching me all these cool ciphers! you really are the best!"
keyword_for_v = "besties"

print(vigenere_encode(vigenere_message_for_v, keyword_for_v))
print(vigenere_decode(vigenere_encode(vigenere_message_for_v, keyword_for_v), keyword_for_v))