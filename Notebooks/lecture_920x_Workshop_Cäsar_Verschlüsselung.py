# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.0
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown] pycharm={"name": "#%% md\n"}
# ## Cäsar-Verschlüsselung
#
# Bei der Cäsar-Verschlüsselung werden die Buchstaben des zu verschlüsselnden
# Wortes im Alphabet um 3 Stellen verschoben, z.B. wird aus der Zeichenkette `ABC`
# die Zeichenkette `DEF`. Die letzten drei Buchstaben des Alphabets werden durch
# die ersten ersetzt, d.h. aus `XYZA` wird `ABCD`.
#
# Typischerweise wurden bei historischen Verschlüsselungsverfahren alle Buchstaben
# in Großbuchstaben umgewandelt. Leer- und Sonderzeichen werden ignoriert. So wird
# aus "Ich kam, sah und siegte." der verschlüsselte Text
#
# ```
# LFKNDPVDKXQGVLHJWH
# ```

# %% [markdown] pycharm={"name": "#%% md\n"}
# Schreiben Sie eine Funktion `encode_char(c: str)`, die einen String `c`, der nur
# aus einem einzigen Zeichen besteht, folgendermaßen verschlüsselt:
#
# - ist `c` einer der Buchstaben `a` bis `z` oder `A` bis `Z` so wird er, falls
#   nötig, in einen Großbuchstaben umgewandelt und mit der Cäsar-Verschlüsselung
#   verschlüsselt;
# - ist `c` eine Ziffer, so wird sie unverändert zurückgegeben;
# - andernfalls wird der leere String `""` zurückgegeben.
#
# *Hinweis:* Die folgenden beiden Strings sind dabei hilfreich:

# %% pycharm={"is_executing": false, "name": "#%%\n"}
letters_in_alphabetical_order = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
letters_in_encoded_order = "DEFGHIJKLMNOPQRSTUVWXYZABC1234567890"

# %% [markdown]
# *Hinweis:* Mit dem Operator `in` und der Funktion `index` können Sie testen, ob und an welcher Stelle eine Zeichen in einem String vorkommt.

# %% pycharm={"is_executing": false, "name": "#%%\n"}

# %% [markdown] pycharm={"is_executing": false, "name": "#%%\n"}
# Testen Sie Ihre Implementierung mit einigen Werten

# %%

# %% [markdown] pycharm={"name": "#%% md\n"}
# Schreiben Sie eine Funktion `encode_caesar(text: str)`, die einen String `text`
# mittels der Cäsar-Verschlüsselung verschlüsselt.

# %% pycharm={"is_executing": false, "name": "#%%\n"}

# %% [markdown] pycharm={"name": "#%% md\n"}
# Überprüfen Sie Ihr Programm mit den folgenden Beispielen:

# %% pycharm={"is_executing": false, "name": "#%%\n"}
pangram = "Sphinx of black quartz, judge my vow!"

# %%

# %% pycharm={"is_executing": false, "name": "#%%\n"}
verlaine = """\
1. Les sanglots longs
2. Des violons
3. De l'automne
4. Blessent mon cœur
5. D'une langueur
6. Monotone.

(Verlaine, 1866)
Gesendet vom BBC 1944-06-01 um Operation Overlord anzukuendigen
"""

# %%

# %% [markdown] pycharm={"name": "#%% md\n"}
# Schreiben Sie jetzt Funktionen `decode_char(c: str)` und `decode_caesar(text: str)`, die einen mit der Cäsar-Verschlüsselung verschlüsselten Text entschlüsseln. Um robust zu sein sollen diese Funktionen Zeichen, die nicht Buchstaben oder Ziffern sind unverändert zurückgeben.

# %% pycharm={"is_executing": false, "name": "#%%\n"}

# %% pycharm={"is_executing": false, "name": "#%%\n"}

# %% [markdown]
# Testen Sie mit `pangram` und `verlaine`.

# %% pycharm={"is_executing": false, "name": "#%%\n"}

# %% pycharm={"is_executing": false, "name": "#%%\n"}

# %% [markdown] pycharm={"name": "#%% md\n"}
# Entschlüsseln Sie den folgenden Text:
# ```
# SDFN PB ERA ZLWK ILYH GRCHQ OLTXRU MXJV
# (SDQJUDP IURP QDVD'V VSDFH VKXWWOH SURJUDP)
# ```

# %% pycharm={"is_executing": false, "name": "#%%\n"}

# %% [markdown] pycharm={"is_executing": false, "name": "#%% md\n"}
# Die Funktionen `encode_char()` und `decode_char()` enthalten (wahrscheinlich) viel duplizierten
# Code. Können Sie eine Funktion `rot_n_char(...)` schreiben, die die
# Funktionalität beider Funktionen verallgemeinert?

# %% pycharm={"is_executing": false, "name": "#%%\n"}

# %% [markdown] pycharm={"is_executing": false, "name": "#%% md\n"}
# Wie würden Sie `encode_caesar()` und `decode_caesar()` unter Zuhilfenahme dieser
# Funktion implementieren?

# %% pycharm={"is_executing": false, "name": "#%%\n"}

# %% pycharm={"is_executing": false, "name": "#%%\n"}

# %% [markdown] pycharm={"name": "#%% md\n"}
# Testen Sie die neue Funktion mittels `secret_text` und `verlaine`. Sind alte und neue Implementierung kompatibel?

# %% pycharm={"is_executing": false, "name": "#%%\n"}

# %% pycharm={"is_executing": false, "name": "#%%\n"}

# %% [markdown] pycharm={"name": "#%% md\n"}
# Die Decodierung mit dem ursprünglichen Cäsar-Code im Lösungsvorschlag zeigt, dass die neue
# Implementierung im Lösungsvorschlag einen Fehler hat: sie vermischt Zahlen und Buchstaben. 
#
# ```
# (VERLAINE, 4X99)
# GESENDET VOM BBC 4Y77-Z9-Z4 UM OPERATION OVERLORD AN3UKUENDIGEN
# ```
#
# Falls Ihre Implementierung den gleichen Fehler hat: Wie können wir den Fehler beseitigen?
#
# Falls Ihre Implementierung den Fehler nicht hat: Warum tritt bei Ihnen dieses Problem nicht auf?
#
# (Die nachfolgenden Zellen sind nur relevant, falls Ihre Implementierung den gleichen Fehler hat wie der Lösungsvorschlag.)

# %% pycharm={"is_executing": false, "name": "#%%\n"}

# %% [markdown]
# Testen Sie die neue Implementierung indem Sie `secret_text` decodieren.

# %%

# %% [markdown]
# Testen Sie die neue Implementierung mit `verlaine`.

# %% pycharm={"is_executing": false, "name": "#%%\n"}
