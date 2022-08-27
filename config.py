core = {
    "x": 44.6,
    "y": 25.5,
    "z": 15,
    "cone": {
        "edge-offset": 4,
        "outer-diameter": 0.75,
        "length": 10,
    },
    "clip": {
        "width": 6,
        "min-depth": 0.56,
        "max-depth": 1.4,
        "midpoint": 0.6,
    },
}

frame = {
    "length": False,  # was frameDims.width
    "height": False,  # when set space around the front plate is the same on all sides
    "marginX": 6,  # margin can be used instead of width, to scale based on the core size.
    "marginY": 6,  # margin can be used instead of width, to scale based on the core size.
    "wall": 3.5,
    "cutout": {
        "paddingX": 3,
        "paddingY": 3,
        "z": 12,
        "fillet": 2,
    },
}
