# cutout for the thermometer
core = {
    "x": 45,  # width
    "y": 26,  # height
    "z": 15,  # depth
    "cone": {  # cutout for small ridges on the casing, note not all of them have them
        "edge-offset": 4,
        "outer-diameter": 0.75,
        "length": 10,
    },
    "clip": {  # cutout for the clip on the sides
        "width": 6,
        "min-depth": 0.56,
        "max-depth": 1.4,
        "midpoint": 0.6,
    },
}

# actual frame of the housing
frame = {
    "length": False,  # when set a fixed width is used
    "height": False,  # when set space around the front plate is the same on all sides
    "marginX": 6,  # when length and height are not used, a margin is used for spacing instead
    "marginY": 6,  # when length and height are not used, a margin is used for spacing instead
    "wall": 3.5,  # the thickness of the frame bars round the housing
    "cutout": {
        "paddingX": 3,  # thickness of the walls around the cutout
        "paddingY": 3,  # thickness of the walls around the cutout

        # How deep the cutout frame is, generally set this lower than the depth of the cutout.
        # As having a closed back makes it harder to remove the thermometer to replace batteries
        "z": 13,
        "fillet": 2,
    },
}
