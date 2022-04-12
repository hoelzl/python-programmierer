# ---
# jupyter:
#   jupytext:
#     cell_metadata_json: true
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.7
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

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"} Running
# Sub-Prozesse
#
# *Hinweis:* Zur Ausführung dieses Notebooks müssen muss das `ext_sample_app`
# Package (in `Examples/ExternalSampleApplication`) installiert sein.

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "en"}
# Subprocesses
#
# *Note:* You need to have the `ext_sample_app` package (in
# `Examples/ExternalSampleApplication`) installed to run the following examples.

# %% {"tags": ["code-along"]}
from subprocess import TimeoutExpired, run

# %% {"tags": ["code-along"]}
# This may not work if `python` is not in your path...
run(["python", "--version"])

# %% {"tags": ["code-along"]}
import shutil

shutil.which("python")

# %%
cp = run([shutil.which("python"), "--version"])

# %% {"tags": ["code-along"]}
def print_completed_process(cp):
    print("return code:", cp.returncode)
    print("captured stdout:", repr(cp.stdout))
    print("captured stderr:", repr(cp.stderr))


# %% {"tags": ["code-along"]}
print_completed_process(cp)

# %%
cp = run([shutil.which("python"), "--version"], capture_output=True, text=True)

# %% {"tags": ["code-along"]}
print_completed_process(cp)

# %% {"tags": ["code-along"]}
import sys

cp = run([sys.executable, "--version"], capture_output=True, text=True)

# %% {"tags": ["code-along"]}
print_completed_process(cp)

# %% {"tags": ["code-along"]}
import sys

cp = run([sys.executable, "-m", "ext_sample_app"], capture_output=True, text=True)

# %% {"tags": ["code-along"]}
print_completed_process(cp)

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

# %% {"tags": ["code-along"]}
proc.communicate("work")

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

# %%
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
