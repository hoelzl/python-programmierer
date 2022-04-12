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
# <div style="text-align:center; font-size:200%;"><b>Katzen vs. Hunde mit FastAI</b></div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "en"}
# <img src="img/python-logo-notext.svg"
#      style="display:block;margin:auto;width:10%"/>
# <br>
# <div style="text-align:center; font-size:200%;"><b>Cats vs. Dogs with FastAI</b></div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>

# %% {"tags": ["code-along"]}
from fastai.vision.all import *

# %% {"tags": ["code-along"]}
path = untar_data(URLs.PETS) / "images"
path

# %% {"tags": ["code-along"]}
def is_cat(x):
    return x[0].isupper()

# %% {"tags": ["code-along"]}
def create_dls():
     return ImageDataLoaders.from_name_func(
        path, get_image_files(path), valid_pct=0.2, seed=42,
        label_func=is_cat, item_tfms=Resize(224))

# %% {"tags": ["code-along"]}
dls = create_dls()
dls.show_batch()

# %% {"tags": ["code-along"]}
learn = cnn_learner(dls, resnet34, metrics=error_rate)
learn.dls = create_dls()

# %% {"tags": ["code-along"]}
learn.fine_tune(1)

# %% {"tags": ["code-along"]}
learn.show_results()

# %%



