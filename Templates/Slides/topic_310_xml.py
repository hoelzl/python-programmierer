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
# <div style="text-align:center; font-size:200%;"><b>Strukturierte Daten und XML</b></div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "en"}
# <img src="img/python-logo-notext.svg"
#      style="display:block;margin:auto;width:10%"/>
# <br>
# <div style="text-align:center; font-size:200%;"><b>Structured Data and XML</b></div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "de"}
# ## Das XML Package
#
# Siehe [Python Dokumentation](https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree)

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "lang": "en"}
# ## The XML Package
#
# See the [Python documentation](https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree)

# %% {"tags": ["code-along"]}
from xml.etree import ElementTree
from tempfile import NamedTemporaryFile
import os

# %% {"tags": ["code-along"]}
xml_data = """\
<?xml version="1.0"?>
<data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank>4</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
        <rank>68</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country>
</data>
"""

# %% {"tags": ["code-along"]}
xml_file = NamedTemporaryFile(mode="w", delete=False)
xml_file.write(xml_data)
xml_file.close()

# %% {"tags": ["code-along"]}
tree = ElementTree.parse(xml_file.name)

# %%
os.remove(xml_file.name)

# %% {"tags": ["code-along"]}
tree

# %% {"tags": ["code-along"]}
root = tree.getroot()
root

# %% {"tags": ["code-along"]}
root.tag

# %% {"tags": ["code-along"]}
root.attrib

# %% {"tags": ["code-along"]}
for child in root:
    print(child.tag, child.attrib)

# %% {"tags": ["code-along"]}
root[0]

# %% {"tags": ["code-along"]}
root[0][1]

# %% {"tags": ["code-along"]}
root[0][1].text

# %% [markdown] {"lang": "de"}
# ## LXML
#
# [LXML](https://lxml.de/index.html) ist eine Alternative mit (möglicherweise) höherer Performanz.

# %% [markdown] {"lang": "en"}
# ## LXML
#
# [LXML](https://lxml.de/index.html) is an alternative with (possibly) higher performance.

# %%
