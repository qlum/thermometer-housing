from cadquery import exporters
from parts.cutout import core
from parts.frame import base

exporters.export(base - core, "output/thermometerHousing.stl")
exporters.export(base - core, "output/thermometerHousing.step")