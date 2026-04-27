from build123d import Box, BuildPart, Cylinder, Mode


def gen_step():
    with BuildPart() as part:
        Box(50, 30, 20)
        # Circular hole through Y axis, diameter 8 mm, centered in the face
        Cylinder(radius=4, height=30, rotation=(90, 0, 0), mode=Mode.SUBTRACT)

    return {
        "shape": part.part,
        "step_output": "wedge-demo.step",
        "export_stl": True,
        "stl_output": "wedge-demo.stl",
    }
