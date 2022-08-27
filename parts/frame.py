import cadquery as cq
import math
from config import core, frame

paddedCore = {
    "x": core["x"] + 2 * frame["cutout"]["paddingX"],
    "y": core["y"] + 2 * frame["cutout"]["paddingY"],
}

# when some variables are not given, calculate the rest
if not frame["length"] and not frame["height"]:  # neither height nor length given
    frame["width"] = paddedCore["y"] + frame["wall"] + frame["marginY"] * 2
    frame["length"] = paddedCore["x"] + frame["wall"] + frame["marginX"] * 2
    frame["height"] = math.sqrt(0.75) * frame["width"]
elif not frame["length"]:  # height given but not length
    frame["width"] = frame["height"] / math.sqrt(0.75)
    frame["length"] = paddedCore["x"] + (frame["width"] - paddedCore["y"])
elif not frame["height"]:  # length given but not height
    frame["width"] = paddedCore["y"] + (frame["length"] - paddedCore["x"])
    frame["height"] = math.sqrt(0.75) * frame["width"]
else:
    frame["width"] = frame["height"] / math.sqrt(0.75)

frame["diagonal"] = math.sqrt(math.pow(frame["length"], 2) + math.pow(frame["width"], 2))

# angle of the diagonal is rounded because it gives errors otherwise
frame["diagonalAngle"] = math.degrees(math.atan2(frame["width"], frame["length"]))

# area the thermometer gets clipped in
cutoutPlate = (
    cq.Workplane()
    .rect(paddedCore["x"], paddedCore["y"])
    .extrude(frame["cutout"]["z"])
    .edges("not(<Z)")
    .fillet(frame["cutout"]["fillet"])
)

# bars along the length of the housing
linearBar = (
    cq.Workplane()
    .cylinder(frame["length"], frame["wall"] / 2)
    .rotateAboutCenter([0, 1, 0], 90)
    .translate([0, 0, frame["wall"] / 2])
)


# diagonal braces
crossBar = (
    cq.Workplane()
    .cylinder(frame["diagonal"], frame["wall"] / 2)
    .rotateAboutCenter([0, 1, 0], 90)
    .rotateAboutCenter([0, 0, 1], frame["diagonalAngle"])
    .translate([0, 0, frame["wall"] / 2])
)
cross = crossBar + crossBar.mirror([0, 1, 0])
cross = cq.Workplane().union(cross)  # union because nested objects fail otherwise


# 2d sketch for the triangular frame on the edges
def triangleSketch():
    p = frame["wall"]
    w = frame["width"] + p * 1.73
    h = frame["height"] + p * 1.5

    return (
        cq.Sketch()
        .polygon([
            (-w / 2, 0),
            (w / 2, 0),
            (0, h),
            (-w / 2, 0)
        ], tag="outer")
        .polygon([
            (-w / 2 + 1.73 * p, p),
            (w / 2 - 1.73 * p, p),
            (0, h - p * 2),
            (-w / 2 + 1.73 * p, p)
        ], tag="inner", mode="s")
        .vertices(tag="outer")
        .fillet(p / 2)
    )


# extruded triangular frame
triangle = (
    cq.Workplane()
    .placeSketch(triangleSketch())
    .extrude(frame["wall"])
    .faces("|Z")
    .fillet(frame["wall"] / 2 - 0.002 * frame["wall"])
    .rotate([0, 0, 0], [1, 0, 0], 90)
    .rotate([0, 0, 0], [0, 0, 1], 90)
    .translate([-frame["wall"] / 2, 0, 0])
)

# combine all the parts
base = (
    linearBar.translate([0, frame["width"] / 2, 0]) +  # front cylinder
    linearBar.translate([0, -frame["width"] / 2, 0]) +  # rear cylinder
    linearBar.translate([0, 0, frame["height"]]) +  # top cylinder
    cross +  # bottom cross brace
    cross.rotate(
        [0, -frame["width"] / 2, frame["wall"] / 2],
        [1, -frame["width"] / 2, frame["wall"] / 2],
        60
    ) +  # front cross brace
    cross.rotate(
        [0, frame["width"] / 2, frame["wall"] / 2],
        [1, frame["width"] / 2, frame["wall"] / 2],
        -60
    ) +  # rear cross brace
    cutoutPlate +  # space around the thermometer
    triangle.translate([frame["length"] / 2, 0, 0]) +  # right side of the frame
    triangle.translate([-frame["length"] / 2, 0, 0])  # left side of the frame
)