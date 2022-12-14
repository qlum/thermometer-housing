import cadquery as cq
from config import core

# defining all the parts

# central cuboid
box = (
    cq.Workplane()
    .box(core["x"], core["y"], core["z"], )
)


# 4 cones on the top / bottom
def cone():
    sketch = (
        cq.Sketch()
        .segment((0, 0), (0, core["cone"]["length"]))
        .segment((core["cone"]["outer-diameter"], 0))
        .close()
        .assemble()
    )
    result = (
        cq.Workplane()
        .placeSketch(sketch)
        .revolve(360, (0, 0, 0), (0, 1, 0))
        .translate([
            0,
            -core["cone"]["length"] / 4,
            (core["z"] / 2) - core["cone"]["length"] / 4
        ])
        .rotateAboutCenter([1, 0, 0], 270)
    )
    return result


# clips on the left and right
def clip():
    sketch = (
        cq.Sketch()
        .segment((0, 0), (core["clip"]["max-depth"], core["z"] * core["clip"]["midpoint"]))
        .segment((core["clip"]["min-depth"], core["z"]))
        .segment((0, core["z"]))
        .close()
        .assemble()
    )

    result = (
        cq.Workplane("XZ")
        .placeSketch(sketch)
        .extrude(core["clip"]["width"] / 2, both=True)
        .translate([0, 0, -core["z"] / 2])
    )
    return result


# combine all the parts into one object
core = (
    box +
    cone().translate([
        core["x"] / 2 - core["cone"]["edge-offset"],
        core["y"] / 2
    ]) +
    cone().translate([
        core["x"] / 2 - core["cone"]["edge-offset"],
        -(core["y"] / 2)
    ]) +
    cone().translate([
        -(core["x"] / 2 - core["cone"]["edge-offset"]),
        core["y"] / 2
    ]) +
    cone().translate([
        -(core["x"] / 2 - core["cone"]["edge-offset"]),
        -(core["y"] / 2)
    ]) +
    clip().translate([core["x"] / 2, 0]) +
    clip().translate([core["x"] / 2, 0]).mirror([1, 0, 0])
).mirror([0, 0, 1]).translate([0, 0, core["z"] / 2])
