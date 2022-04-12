# ---
# jupyter:
#   jupytext:
#     cell_metadata_json: true
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

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# <img src="img/python-logo-notext.svg"
#      style="display:block;margin:auto;width:10%"/>
# <br>
# <div style="text-align:center; font-size:200%;"><b>Externe Programme</b></div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "en"}
# <img src="img/python-logo-notext.svg"
#      style="display:block;margin:auto;width:10%"/>
# <br>
# <div style="text-align:center; font-size:200%;"><b>External Programs</b></div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>

# %% [markdown] {"incorrectly_encoded_metadata": "{\"slideshow\": {\"slide_type\": \"slide\"}, \"lang\": \"de\"} Running"}
# ## Sub-Prozesse
#
# *Hinweis:* Zur Ausführung dieses Notebooks müssen muss das `ext_sample_app`
# Package (in `Examples/ExternalSampleApplication`) installiert sein.
#
# `subprocess.run` ist die bevorzugte Methode um externe Applikationen zu starten.

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "en"}
# ## Subprocesses
#
# *Note:* You need to have the `ext_sample_app` package (in
# `Examples/ExternalSampleApplication`) installed to run the following examples.
#
# `subprocess.run()` is the preferred way of running external applications.

# %% {"tags": ["code-along"]}
from subprocess import TimeoutExpired, run

# %% {"tags": ["code-along"]}
# This may not work if `python` is not in your path...
run(["python", "--version"])

# %% [markdown] {"lang": "de"}
# Mit `shutil.which()` kann man den vollständigen Pfad eines Programms herausfinden.

# %% [markdown] {"lang": "en"}
# With `shutil.which()` you can determine the full path of a program.

# %% {"tags": ["code-along"]}
import shutil

shutil.which("python")

# %% {"tags": ["code-along"]}
cp = run([shutil.which("python"), "--version"])

# %% {"tags": ["code-along"]}
def print_completed_process(cp):
    print("return code:", cp.returncode)
    print("captured stdout:", repr(cp.stdout))
    print("captured stderr:", repr(cp.stderr))


# %% {"tags": ["code-along"]}
print_completed_process(cp)

# %% {"tags": ["code-along"]}
cp = run([shutil.which("python"), "--version"], capture_output=True, text=True)

# %% {"tags": ["code-along"]}
print_completed_process(cp)

# %% [markdown] {"lang": "de"}
# Mit `sys.executable` kann man den Pfad des gerade aktiven Python Interpreters herausfinden. Das ist die bevorzugte Methode um einen Python Prozess zu starten.

# %% [markdown] {"lang": "en"}
# With `sys.executable` you can find out the path of the currently active Python interpreter. This is the preferred way to start a Python process.

# %% {"tags": ["code-along"]}
import sys

cp = run([sys.executable, "--version"], capture_output=True, text=True)

# %% {"tags": ["code-along"]}
print_completed_process(cp)

# %% {"tags": ["code-along"]}
cp = run([sys.executable, "-m", "ext_sample_app"], capture_output=True, text=True)

# %% {"tags": ["code-along"]}
print_completed_process(cp)

# %% {"tags": ["code-along"]}
cp = run(
    [sys.executable, "-m", "ext_sample_app", "--help"], capture_output=True, text=True
)

# %% {"tags": ["code-along"]}
print_completed_process(cp)

# %% {"tags": ["code-along"]}
cp = run(
    [sys.executable, "-m", "ext_sample_app", "say-hi"], capture_output=True, text=True
)

# %% {"tags": ["code-along"]}
print_completed_process(cp)

# %% {"tags": ["code-along"]}
cp = run(
    [sys.executable, "-m", "ext_sample_app", "error"], capture_output=True, text=True
)

# %% {"tags": ["code-along"]}
print_completed_process(cp)

# %% {"tags": ["code-along"]}
# THIS DOES NOT WORK!
# cp = run(
#     [sys.executable, "-m", "ext_sample_app", "interact"], capture_output=True, text=True
# )

# %% [markdown] {"lang": "de"}
# ## Popen: Nebenläufige Ausführung von Programmen
#
# Wenn man nicht warten kann, bis das gestartete Programm beendet wird muss man die `subprocess.Popen` Klasse verwenden:

# %% [markdown] {"lang": "en"}
# ## Popen: Concurrent execution of programs
#
# If you can't wait for the launched program to finish, you have to use the `subprocess.Popen` class:

# %% {"tags": ["code-along"]}
from subprocess import Popen, PIPE
import sys

# %% {"tags": ["code-along"]}
proc = Popen(
    [sys.executable, "-m", "ext_sample_app", "interact"],
    stdin=PIPE,
    stderr=PIPE,
    stdout=PIPE,
    encoding="utf-8",
    universal_newlines=True,
    bufsize=0,
)

# %% {"tags": ["code-along"]}
type(proc)

# %% [markdown] {"lang": "de"}
# `proc.communicate()` sendet eine Nachricht and `proc`, schließt die Ein- und Ausgabeströme und beendet den Prozess.

# %% [markdown] {"lang": "en"}
# `proc.communicate()` sends a message to `proc`, closes the input and output streams and ends the process.

# %% {"tags": ["code-along"]}
proc.communicate("work")

# %% [markdown] {"lang": "de"}
# Mit `proc.poll()` kann man feststellen, ob der Prozess schon beendet wurde und was der Rückgabewert war. Falls das Ergebniss `None` ist, ist der Prozess noch aktiv. `proc.wait()` wartet eine bestimmte Zeit und gibt den Rückgabewert des Prozesses zurück. Falls der Prozess nicht in der vorgegebenen Zeit beendet wurde, wird eine `TimeoutExpired` Exception ausgelöst.

# %% [markdown] {"lang": "en"}
# With `proc.poll()` you can determine whether the process has already ended and what its return value was. If the result is `None`, the process is still active. `proc.wait()` waits a certain amount of time and returns the status of the process. If the process hasn't finished in the allotted time, a `TimeoutExpired` exception is thrown.

# %% {"tags": ["code-along"]}
proc.poll()

# %% {"tags": ["code-along"]}
def run_and_communicate(command):
    proc = Popen(
        [sys.executable, "-m", "ext_sample_app", "interact"],
        stdin=PIPE,
        stderr=PIPE,
        stdout=PIPE,
        encoding="utf-8",
        universal_newlines=True,
        bufsize=0,
    )
    result = proc.communicate(command)
    try:
        wait_result = proc.wait(5)
    except TimeoutExpired:
        print("Process did not terminate!")
        proc.terminate()
        wait_result = proc.wait(5)
    return result, wait_result


# %% {"tags": ["code-along"]}
run_and_communicate("work")

# %% {"tags": ["code-along"]}
run_and_communicate("exit")

# %% {"tags": ["code-along"]}
run_and_communicate("error")

# %% [markdown] {"lang": "de"}
# ## Kommunikation mit Sockets
#
# Das folgende Beispiel zeigt, wie man einen Prozess starten und dann über Sockets mit ihm kommunizieren kann.

# %% [markdown] {"lang": "en"}
# ## Communication with sockets
#
# The following example shows how to start a process and then communicate with it using sockets.

# %% {"tags": ["code-along"]}
from subprocess import Popen, PIPE
import sys

HOST = "localhost"
PORT = 12345

# %% {"tags": ["code-along"]}
from socket import socket, AF_INET, SOCK_STREAM
import sys


def send_message(msg: str):
    with socket(AF_INET, SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        sock.sendall(bytes(msg + "\n", "utf-8"))
        return str(sock.recv(1024), "utf-8")


# %% {"tags": ["code-along"]}
proc = Popen(
    [
        sys.executable,
        "-m",
        "ext_sample_app",
        "serve",
        "--host",
        HOST,
        "--port",
        str(PORT),
    ],
    stdin=PIPE,
    stderr=PIPE,
    stdout=PIPE,
    encoding="utf-8",
    universal_newlines=True,
    bufsize=0,
)

# %% {"tags": ["code-along"]}
proc.poll()

# %% {"tags": ["code-along"]}
send_message("Hello, world!")

# %% {"tags": ["code-along"]}
send_message("Are you running?")

# %% {"tags": ["code-along"]}
proc.poll()

# %% {"tags": ["code-along"]}
proc.terminate()

# %% {"tags": ["code-along"]}
proc.poll()

# %% {"tags": ["code-along"]}
try:
    send_message("Are you still running?")
except ConnectionRefusedError as err:
    print("Could not connect to server.")
    print(err)

# %% {"tags": ["code-along"]}
proc.poll()

# %% {"tags": ["code-along"]}
