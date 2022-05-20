# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.8
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown] lang="de"
# ## Cäsar-Verschlüsselung
#
# Bei der Cäsar-Verschlüsselung werden die Buchstaben des zu verschlüsselnden
# Wortes im Alphabet um 3 Stellen verschoben, z.B. wird aus der Zeichenkette
# `ABC` die Zeichenkette `DEF`. Die letzten drei Buchstaben des Alphabets
# werden durch die ersten ersetzt, d.h. aus `XYZA` wird `ABCD`.
#
# Typischerweise wurden bei historischen Verschlüsselungsverfahren alle
# Buchstaben in Großbuchstaben umgewandelt. Leer- und Sonderzeichen werden
# ignoriert. So wird aus "Ich kam, sah und siegte." der verschlüsselte Text
#
# ```
# LFKNDPVDKXQGVLHJWH
# ```

# %% [markdown] lang="en"
# ## Caesar encryption
#
# Caesar encryption shifts each letter of the to-be-encrypted word
# in the alphabet by 3 places, e.g. the character string
# `ABC` becomes the string `DEF`. The last three letters of the alphabet
# are replaced by the first ones, i.e. `XYZA` becomes `ABCD`.
#
# Typically, in historical encryption methods, all
# letters are converted to uppercase, spaces and special characters are
# ignored. So after encrypting, the text "I came, saw and conquered." becomes
#
# ```
# LFKNDPVDKXQGVLHJWH
# ```

# %% [markdown] lang="de"
#
# Schreiben Sie eine Funktion `encode_char(c: str)`, die einen String `c`,
# der nur aus einem einzigen Zeichen besteht, folgendermaßen verschlüsselt:
#
# - ist `c` einer der Buchstaben `a` bis `z` oder `A` bis `Z` so wird er, falls
#   nötig, in einen Großbuchstaben umgewandelt und mit der Cäsar-Verschlüsselung
#   verschlüsselt;
# - ist `c` eine Ziffer, so wird sie unverändert zurückgegeben;
# - andernfalls wird der leere String `""` zurückgegeben.
#
# *Hinweis:* Die folgenden beiden Strings sind dabei hilfreich:

# %% [markdown] lang="en"
# Write a function `encode_char(c: str)` that takes a string `c`
# consisting of a single character and encodes it as follows:
#
# - if `c` is one of the letters `a` to `z` or `A` to `Z` then it is, if
#   necessary, converted to a capital letter and encrypted using the Caesar
#   cipher;
# - if `c` is a digit, it is returned unchanged;
# - otherwise the empty string `""` is returned.
#
# *Note:* The following two strings are helpful:

# %% tags=["solution"]
letters_in_alphabetical_order = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
letters_in_encoded_order = "DEFGHIJKLMNOPQRSTUVWXYZABC1234567890"


# %% tags=["solution"]
def encode_char(c: str):
    c_upper = c.upper()
    if c_upper in letters_in_alphabetical_order:
        index = letters_in_alphabetical_order.index(c_upper)
        return letters_in_encoded_order[index]
    else:
        return ""


# %% [markdown] lang="de"
# Testen Sie Ihre Implementierung mit einigen Werten

# %% [markdown] lang="en"
# Test your implementation with some values

# %% tags=["solution"]
encode_char("a")

# %% tags=["solution"]
encode_char("x")

# %% tags=["solution"]
encode_char("3")

# %% tags=["solution"]
encode_char("!")


# %% [markdown] lang="de"
#
# Schreiben Sie eine Funktion `encode_caesar(text: str)`, die einen String
# `text` mittels der Cäsar-Verschlüsselung verschlüsselt.

# %% [markdown] lang="en"
# Write a function `encode_caesar(text: str)` that takes a string
# `text` and encrypts it using Caesar encryption.

# %% tags=["solution"]
def encode_caesar(text: str):
    return "".join(encode_char(c) for c in text)


# %% [markdown] lang="de"
# Überprüfen Sie Ihr Programm mit den folgenden Beispielen:

# %% [markdown] lang="en"
# Check your program with the following examples:

# %% tags=["solution"]
pangram = "Sphinx of black quartz, judge my vow!"

# %% tags=["solution"]
encoded_pangram = encode_caesar(pangram)
encoded_pangram

# %% tags=["solution"]
verlaine = """\
1. Les sanglots longs
2. Des violons
3. De l'automne
4. Blessent mon cœur
5. D'une langueur
6. Monotone.

(Verlaine, 1866)
Gesendet vom BBC 1944-06-01 um Operation Overlord anzukündigen
"""

# %% tags=["solution"]
encoded_verlaine = encode_caesar(verlaine)
encoded_verlaine


# %% [markdown] lang="de"
# Schreiben Sie jetzt Funktionen `decode_char(c: str)`
# und `decode_caesar(text: str)`, die einen mit der Cäsar-Verschlüsselung
# verschlüsselten Text entschlüsseln. Um robust zu sein sollen diese
# Funktionen Zeichen, die keine Buchstaben oder Ziffern sind, unverändert zurückgeben.

# %% [markdown] lang="en"
# Now write functions `decode_char(c: str)` and `decode_caesar(text: str)`
# that decrypt a text encrypted with the Caesar cipher. To be robust, these functions should return characters, that aren't letters or digits, unchanged.

# %% tags=["solution"]
def decode_char(c: str):
    if c in letters_in_encoded_order:
        index = letters_in_encoded_order.index(c)
        return letters_in_alphabetical_order[index]
    else:
        return c


# %% tags=["solution"]
def decode_caesar(text: str):
    return "".join(decode_char(c) for c in text)


# %% tags=["solution"]
def decode_caesar2(text: str):
    result = ""
    for c in text:
        result += decode_char(c)
    return result


# %% [markdown] lang="de"
# Testen Sie `decode_caesar()` mit `pangram` und `verlaine`.

# %% [markdown] lang="en"
# Test `decode_caesar()` with `pangram` and `verlaine`.

# %% tags=["solution"]
decoded_pangram = decode_caesar(encoded_pangram)
decoded_pangram

# %% tags=["solution"]
decoded_verlaine = decode_caesar(encoded_verlaine)
print(decoded_verlaine)

# %% tags=["solution"]
assert decoded_pangram == decode_caesar2(encoded_pangram)

# %% tags=["solution"]
assert decoded_verlaine == decode_caesar2(encoded_verlaine)

# %% [markdown] lang="de"
# Entschlüsseln Sie den folgenden Text:
# ```
# SDFN PB ERA ZLWK ILYH GRCHQ OLTXRU MXJV
# (SDQJUDP IURP QDVD'V VSDFH VKXWWOH SURJUDP)
# ```

# %% [markdown] lang="en"
# Decrypt the following text:
# ```
# SDFN PB ERA ZLWK ILYH GRCHQ OLTXRU MXJV
# (SDQJUDP IURP QDVD'V VSDFH VKXWWOH SURJUDP)
# ```

# %% tags=["solution"]
secret_text = """\
SDFN PB ERA ZLWK ILYH GRCHQ OLTXRU MXJV
(SDQJUDP IURP QDVD'V VSDFH VKXWWOH SURJUDP)\
"""
print(decode_caesar(secret_text))


# %% [markdown] pycharm={"is_executing": false, "name": "#%% md\n"} lang="de"
# Die Funktionen `encode_char()` und `decode_char()` enthalten viel duplizierten
# Code. Können Sie eine Funktion `rot_n_char(...)` schreiben, die die
# Funktionalität beider Funktionen verallgemeinert?

# %% [markdown] lang="en"
# The functions `encode_char()` and `decode_char()` contain a lot of duplicated
# code. Can you write a function `rot_n_char(...)` that generalizes the
# functionality of both functions?

# %% tags=["solution"]
def rot_n_char(c: str, n: int, keep_non_letters=False):
    c_upper = c.upper()
    if c_upper in letters_in_alphabetical_order:
        source_index = letters_in_alphabetical_order.index(c_upper)
        target_index = (source_index + n) % len(letters_in_alphabetical_order)
        return letters_in_alphabetical_order[target_index]
    elif keep_non_letters:
        return c_upper
    else:
        return ""


# %% [markdown] lang="de"
#
# Wie würden Sie `encode_caesar_2()` und `decode_caesar_2()` unter
# Zuhilfenahme dieser Funktion implementieren?

# %% [markdown] lang="en"
# How can you implement `encode_caesar_2()` and `decode_caesar_2()` 
# using `rot_n_char()`?

# %% tags=["solution"]
def encode_caesar_2(text: str, keep_non_letters=False):
    return "".join(rot_n_char(c, 3, keep_non_letters=keep_non_letters) for c in text)


# %% tags=["solution"]
def decode_caesar_2(text: str):
    return "".join(rot_n_char(c, -3, keep_non_letters=True) for c in text)


# %% [markdown] lang="de"
# Testen Sie die neue Funktion mittels `secret_text` und `verlaine`.
# Sind alte und neue Implementierung kompatibel?

# %% [markdown] lang="en"
# Test the new function using `secret_text` and `verlaine`.
# Are the old and new implementations compatible?

# %% tags=["solution"]
print(decode_caesar_2(secret_text))

# %% tags=["solution"]
encoded_verlaine_2 = encode_caesar_2(verlaine, keep_non_letters=True)
print(encoded_verlaine_2)

# %% tags=["solution"]
print(decode_caesar_2(encoded_verlaine_2))

# %% tags=["solution"]
print(decode_caesar(encoded_verlaine_2))

# %% [markdown] lang="de"
# Möglicherweise zeigt die Decodierung mit dem ursprünglichen Cäsar-Code, dass Ihre neue
# Implementierung einen Fehler hat, der bei der Verallgemeinerung häufig passiert: Es kann sein, dass der generalisierte Code Zahlen und Buchstaben vermischt. 
#
# Gratulation, falls Sie diesen Fehler vermieden haben!
# Wie können wir den Fehler beseitigen, falls er bei Ihnen auftritt?

# %% [markdown] lang="en"
# Decoding with the original code for the Caesar cipher may reveal a
# bug that frequently appears in the generalized implementation:
# it may mix numbers and letters. 
#
# Congratulations if you managed to avoid this error!
# How can you fix this bug if it appears in your code?

# %% tags=["solution"]
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letters


# %% tags=["solution"]
def rot_n_char(c: str, n: int, keep_non_letters=False):
    c_upper = c.upper()
    if c_upper in letters:
        source_index = letters.index(c_upper)
        target_index = (source_index + n) % len(letters)
        return letters[target_index]
    elif c.isnumeric() or keep_non_letters:
        return c_upper
    else:
        return ""


def encode_caesar_2(text: str, keep_non_letters=False):
    return "".join(rot_n_char(c, 3, keep_non_letters=keep_non_letters) for c in text)


def decode_caesar_2(text: str):
    return "".join(rot_n_char(c, -3, keep_non_letters=True) for c in text)


# %% [markdown] lang="de"
# Testen Sie die neue Implementierung indem Sie `secret_text` decodieren.

# %% [markdown] lang="en"
# Test the new implementation by decoding `secret_text`.

# %% tags=["solution"]
print(decode_caesar_2(secret_text))

# %% [markdown] lang="de"
# Testen Sie die neue Implementierung mit `verlaine`.

# %% [markdown] lang="en"
# Test the new implementation with `verlaine`.

# %% tags=["solution"]
encoded_verlaine_2 = encode_caesar_2(verlaine, keep_non_letters=True)
print(encoded_verlaine_2)

# %% tags=["solution"]
print(decode_caesar_2(encoded_verlaine_2))

# %% tags=["solution"]
print(decode_caesar(encoded_verlaine_2))

# %% tags=["solution"]
decode_caesar(encoded_verlaine_2) == decode_caesar_2(encoded_verlaine_2)

# %%
