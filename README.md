# Printable stand standard Chinese thermometers

![Render of thermometer](./Images/render.png)

---



## Basics
For basic use you can grab either the `stl` or `step` file and slice these in your favorite slicer.  
These are found in the rendered directory.

---

## Adjusting the model

### Dependencies
CadQuery 2, please refer to the CadQuery instructions how to use it: https://cadquery.readthedocs.io/en/latest/installation.html
Optionally also install cq-editor to use the `render.py` for easier previewing of changes.


### Changing basic dimensions
The dimensions of the model can be changed to your liking using the provider config file: `config.py`.  
The config is in the form of a python dictionary.  

After modifications you can generate a new model by running `python export.py`, inside a conda environment with CadQuery installed.  
Alternatively you can preview the model by running `cq-editor render.py`  
For the later, please note that cq-editor will not auto track changes made in included files.  
You may need to re-render manually after changes.  

---

## Caveats

- These cheap Chinese thermometers are cloned all over, so I cannot guarantee all of them fit with the default values.
- The model has some overhangs which results in some artifacts and requires a bit of manual touch-up at the end of the print.

---

## Known issues
Slicers such as Prusa Slicer may complain about 8 open faces. This should not impact the actual print.


Certain specific values in the config file may result in errors.
In such a case adding / removing 0.001mm generally fixes things.
