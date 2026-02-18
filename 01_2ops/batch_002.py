"""Batch 002 - passing/01_2ops
132 models bundled from Fusion360 Gallery reconstructions.
"""

from build123d import *


# Description: This is a lightweight carabiner with an elongated oval shape, featuring textured grip surfaces on the sides and a hinged gate mechanism with locking teeth on one side for secure rope or equipment attachment.
def model_118269_fa4b08d7_0002():
    """Model: Rack_11 v1"""
    with BuildPart() as part:
        # Gear_13.995_14x20_250 -> Extrude2 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 16 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.9034578382, perimeter: 26.5815564415
            with BuildLine():
                CenterArc((0, -1.7), 1, 180, 180)
                Line((1, -1.7), (1, 1.5))
                CenterArc((0, 1.5), 1, 0, 180)
                Line((-1, -1.7), (-1, 1.5))
            make_face()
            with BuildLine():
                Line((0.7819734786, 0.7255694372), (0.626237, 0.6689152572))
                Line((0.626237, 0.6689152572), (0.626237, 0.5756733743))
                Line((0.626237, 0.5756733743), (0.780088, 0.5196753743))
                Line((0.780088, 0.5196753743), (0.780088, 0.4111353743))
                Line((0.780088, 0.4111353743), (0.626237, 0.3551373743))
                Line((0.626237, 0.3551373743), (0.626237, 0.2616263743))
                Line((0.626237, 0.2616263743), (0.780088, 0.2056293743))
                Line((0.780088, 0.2056293743), (0.780088, 0.0970883743))
                Line((0.780088, 0.0970883743), (0.626237, 0.0410913743))
                Line((0.626237, 0.0410913743), (0.626237, -0.0524196257))
                Line((0.626237, -0.0524196257), (0.780088, -0.1084166257))
                Line((0.780088, -0.1084166257), (0.780088, -0.2169576257))
                Line((0.780088, -0.2169576257), (0.626237, -0.2729546257))
                Line((0.626237, -0.2729546257), (0.626237, -0.3664656257))
                Line((0.626237, -0.3664656257), (0.780088, -0.4224626257))
                Line((0.780088, -0.4224626257), (0.780088, -0.5310036257))
                Line((0.780088, -0.5310036257), (0.626237, -0.5870006257))
                Line((0.626237, -0.5870006257), (0.626237, -0.6805116257))
                Line((0.626237, -0.6805116257), (0.780088, -0.7365096257))
                Line((0.780088, -0.7365096257), (0.780088, -0.8450496257))
                Line((0.780088, -0.8450496257), (0.626237, -0.9010466257))
                Line((0.626237, -0.9010466257), (0.626237, -0.99446395))
                Line((0.626237, -0.99446395), (0.7807169121, -1.0506812068))
                Line((0.7807172774, -1.7), (0.7807169121, -1.0506812068))
                CenterArc((0, -1.7), 0.7807172774, -180, 180)
                Line((-0.7807172774, -1.7), (-0.7807172774, -0.8860514799))
                Line((-0.626237, -0.829834124), (-0.7807172774, -0.8860514799))
                Line((-0.626237, -0.73641495), (-0.626237, -0.829834124))
                Line((-0.780088, -0.68041795), (-0.626237, -0.73641495))
                Line((-0.780088, -0.57187795), (-0.780088, -0.68041795))
                Line((-0.626237, -0.51587995), (-0.780088, -0.57187795))
                Line((-0.626237, -0.42236895), (-0.626237, -0.51587995))
                Line((-0.780088, -0.36637195), (-0.626237, -0.42236895))
                Line((-0.780088, -0.25783095), (-0.780088, -0.36637195))
                Line((-0.626237, -0.20183395), (-0.780088, -0.25783095))
                Line((-0.626237, -0.10832295), (-0.626237, -0.20183395))
                Line((-0.780088, -0.05232595), (-0.626237, -0.10832295))
                Line((-0.780088, 0.05621505), (-0.780088, -0.05232595))
                Line((-0.626237, 0.11221205), (-0.780088, 0.05621505))
                Line((-0.626237, 0.20572305), (-0.626237, 0.11221205))
                Line((-0.780088, 0.26172005), (-0.626237, 0.20572305))
                Line((-0.780088, 0.37026105), (-0.780088, 0.26172005))
                Line((-0.626237, 0.42625805), (-0.780088, 0.37026105))
                Line((-0.626237, 0.51976905), (-0.626237, 0.42625805))
                Line((-0.780088, 0.57576705), (-0.626237, 0.51976905))
                Line((-0.780088, 0.68430705), (-0.780088, 0.57576705))
                Line((-0.626237, 0.74030505), (-0.780088, 0.68430705))
                Line((-0.626237, 0.8335409109), (-0.626237, 0.74030505))
                Line((-0.7819734786, 0.8901948926), (-0.626237, 0.8335409109))
                Line((-0.7819734786, 1.5), (-0.7819734786, 0.8901948926))
                CenterArc((0, 1.5), 0.7819734786, 0, 180)
                Line((0.7819734786, 1.5), (0.7819734786, 0.7255694372))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: This is a dark gray parallelogram or skewed rectangular plate with a uniform thickness, featuring a simple flat geometric shape with no holes, slots, or additional features.
def model_118427_e6d67c63_0001():
    """Model: FRONT DOOR2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 8500, perimeter: 440
            with BuildLine():
                Line((45, 170), (45, 0))
                Line((45, 0), (95, 0))
                Line((95, 0), (95, 170))
                Line((95, 170), (45, 170))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


# Description: This is a flat parallelogram-shaped plate or panel with a slanted rectangular form and no additional features such as holes, slots, or flanges.
def model_118427_e6d67c63_0002():
    """Model: FRONT DOOR"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 13600, perimeter: 500
            with BuildLine():
                Line((-40, 170), (40, 170))
                Line((-40, 0), (-40, 170))
                Line((40, 0), (-40, 0))
                Line((40, 170), (40, 0))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


# Description: This is a dark gray composite or plastic housing component with an elongated, tapered shape featuring internal blue-highlighted cavities or channels, angular cutouts, and a streamlined aerodynamic profile designed for airflow or cable management.
def model_118437_904c2ed5_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 13 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 28.4049677865, perimeter: 35.3370189252
            with BuildLine():
                CenterArc((6.3500002027, -2.2352), 2.2352, -90, 180)
                Line((0, 0), (6.3500002027, 0))
                Line((0, 0), (0, -4.4704))
                Line((6.3500002027, -4.4704), (0, -4.4704))
            make_face()
            with BuildLine():
                Line((3.8100001216, -3.2004), (6.3500002027, -3.2004))
                CenterArc((3.8100001216, -2.2352), 0.9652, 90, 180)
                Line((6.3500002027, -1.27), (3.8100001216, -1.27))
                CenterArc((6.3500002027, -2.2352), 0.9652, -90, 180)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.9652
        extrude(amount=-0.9652)
    return part.part


# Description: This is a cylindrical roller or shaft with three evenly-spaced mounting holes along its length and rounded end caps on both sides.
def model_118440_90bbb605_0003():
    """Model: 3hole-link"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 12 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 7.1696044979, perimeter: 18.6982205139
            with BuildLine():
                CenterArc((-2.54, 0), 0.635, 90, 180)
                Line((-2.54, -0.635), (2.54, -0.635))
                CenterArc((2.54, 0), 0.635, -90, 180)
                Line((2.54, 0.635), (-2.54, 0.635))
            make_face()
            with BuildLine():
                CenterArc((-2.54, 0), 0.2413, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0), 0.2413, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.54, 0), 0.2413, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=0.254
        extrude(amount=0.127, both=True)
    return part.part


# Description: This is a elongated channel or trough with rounded ends, featuring two parallel internal ridges or guides that runs the length of the part, designed for linear motion or material guidance applications.
def model_118618_1255e091_0000():
    """Model: LINK"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 11 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.1073009183, perimeter: 6.5707963268
            with BuildLine():
                Line((0, 0.5), (3, 0.5))
                CenterArc((0, 0), 0.5, 0, 90)
                Line((2.5, 0), (0.5, 0))
                CenterArc((3, 0), 0.5, 90, 90)
            make_face()
            # Profile area: 0.3298672286, perimeter: 2.7991148575
            with BuildLine():
                CenterArc((0, 0), 0.5, 90, 90)
                Line((-0.2, 0), (-0.5, 0))
                CenterArc((0, 0), 0.2, 0, 180)
                Line((0.5, 0), (0.2, 0))
                CenterArc((0, 0), 0.5, 0, 90)
            make_face()
            # Profile area: 1.1073009183, perimeter: 6.5707963268
            with BuildLine():
                CenterArc((0, 0), 0.5, -90, 90)
                Line((0, -0.5), (3, -0.5))
                CenterArc((3, 0), 0.5, -180, 90)
                Line((2.5, 0), (0.5, 0))
            make_face()
            # Profile area: 0.3298672286, perimeter: 2.7991148575
            with BuildLine():
                CenterArc((3, 0), 0.5, 90, 90)
                Line((2.8, 0), (2.5, 0))
                CenterArc((3, 0), 0.2, 0, 180)
                Line((3.5, 0), (3.2, 0))
                CenterArc((3, 0), 0.5, 0, 90)
            make_face()
            # Profile area: 0.3298672286, perimeter: 2.7991148575
            with BuildLine():
                Line((0.5, 0), (0.2, 0))
                CenterArc((0, 0), 0.2, -180, 180)
                Line((-0.2, 0), (-0.5, 0))
                CenterArc((0, 0), 0.5, -180, 90)
                CenterArc((0, 0), 0.5, -90, 90)
            make_face()
            # Profile area: 0.3298672286, perimeter: 2.7991148575
            with BuildLine():
                CenterArc((3, 0), 0.5, -180, 90)
                CenterArc((3, 0), 0.5, -90, 90)
                Line((3.5, 0), (3.2, 0))
                CenterArc((3, 0), 0.2, -180, 180)
                Line((2.8, 0), (2.5, 0))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is a cylindrical rod or shaft with rounded ends, featuring a smooth, uniform diameter throughout its length and a slight tapered or beveled edge at each end.
def model_118626_c1782d20_0000():
    """Model: AXLE"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1829214, perimeter: 1.5161326146
            Circle(0.2413)
        # OneSide extrude, distance=3.81
        extrude(amount=3.81)
    return part.part


# Description: This is a cylindrical housing or barrel component with a rounded, capsule-like overall shape, featuring a large central axial hole running through its length and smaller perforated or slotted openings on the sides.
def model_118626_c1782d20_0001():
    """Model: COLLAR"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.7539807289, perimeter: 4.9473801109
            with BuildLine():
                CenterArc((0, 0), 0.5461, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2413, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=0.762
        extrude(amount=0.381, both=True)
    return part.part


# Description: This is a hexagonal or polygonal container/enclosure with angled faceted walls, internal ribbing or structural supports, and mesh or perforated panels that appears to be designed for structural rigidity while allowing airflow or visibility through certain sections.
def model_118626_c1782d20_0003():
    """Model: BASE"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 3.0428786, perimeter: 9.1361326146
            with BuildLine():
                Line((0.635, -1.778), (-0.635, -1.778))
                Line((0.635, 0.762), (0.635, -1.778))
                Line((-0.635, 0.762), (0.635, 0.762))
                Line((-0.635, -1.778), (-0.635, 0.762))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2413, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=1.27
        extrude(amount=0.635, both=True)
    return part.part


# Description: This is a mounting bracket or fastening plate with an elongated, narrow rectangular shape featuring three evenly-spaced circular holes along its length for bolted attachment.
def model_118626_c1782d20_0004():
    """Model: 3 HOLE LINK"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 11 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 5.0019099023, perimeter: 15.6659552847
            with BuildLine():
                CenterArc((5.08, 0), 0.635, 90, 180)
                Line((0, 0.635), (5.08, 0.635))
                CenterArc((0, 0), 0.635, -90, 180)
                Line((0, -0.635), (5.08, -0.635))
            make_face()
            with BuildLine():
                CenterArc((2.54, 0), 0.2413, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.0838472978, perimeter: 5.5059552847
            with BuildLine():
                CenterArc((5.08, 0), 0.635, 90, 180)
                CenterArc((5.08, 0), 0.635, -90, 180)
            make_face()
            with BuildLine():
                CenterArc((5.08, 0), 0.2413, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.0838472978, perimeter: 5.5059552847
            with BuildLine():
                CenterArc((0, 0), 0.635, 90, 180)
                CenterArc((0, 0), 0.635, -90, 180)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2413, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=0.254
        extrude(amount=0.127, both=True)
    return part.part


# Description: This is a cylindrical rod or pin with a smooth, tapered or slightly conical shape, featuring rounded ends and a uniform diameter along its length.
def model_119054_4e1076ec_0000():
    """Model: Middle stand v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 70.1380194868, perimeter: 29.6880505764
            Circle(4.725)
        # OneSide extrude, distance=92.5
        extrude(amount=92.5)
    return part.part


# Description: This is a ring or washer-like component with an oval/elliptical outer profile and a large central opening, featuring a radially-grooved or ridged surface texture across its entire body.
def model_119054_4e1076ec_0022():
    """Model: Washer v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 14.944163554, perimeter: 27.8030949843
            with BuildLine():
                CenterArc((0, 0), 2.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.675, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.15
        extrude(amount=0.15)
    return part.part


# Description: This is a long, rectangular prism or bar with a slightly tapered profile, featuring clean edges and a uniform dark finish, appearing to be a structural beam or extrusion with no holes or slots.
def model_119054_4e1076ec_0027():
    """Model: Reflector's mirror v1 (3)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 973, perimeter: 167
            with BuildLine():
                Line((-7, 34.75), (7, 34.75))
                Line((-7, -34.75), (-7, 34.75))
                Line((7, -34.75), (-7, -34.75))
                Line((7, 34.75), (7, -34.75))
            make_face()
        # OneSide extrude, distance=0.35
        extrude(amount=0.35)
    return part.part


# Description: A horizontal cylindrical rod or shaft with rounded ends and two small holes or slots positioned symmetrically near each end on the top surface.
def model_119054_4e1076ec_0029():
    """Model: Stand v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 25.5175863288, perimeter: 17.9070781255
            Circle(2.85)
        # OneSide extrude, distance=50
        extrude(amount=50)
    return part.part


# Description: This is a hexagonal frame or ring structure with a large central oval opening, featuring curved inward-facing surfaces and geometric faceting throughout its body.
def model_119054_4e1076ec_0039():
    """Model: Nut v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 7.4251566035, perimeter: 25.5249409814
            with BuildLine():
                Line((-1.2305448584, -2.1762959407), (1.2694551416, -2.1538310782))
                Line((1.2694551416, -2.1538310782), (2.5, 0.0224648624))
                Line((2.5, 0.0224648624), (1.2305448584, 2.1762959407))
                Line((1.2305448584, 2.1762959407), (-1.2694551416, 2.1538310782))
                Line((-1.2694551416, 2.1538310782), (-2.5, -0.0224648624))
                Line((-2.5, -0.0224648624), (-1.2305448584, -2.1762959407))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.675, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-1
        extrude(amount=-1)
    return part.part


# Description: This is a flat rectangular plate or panel with a diagonal crease or fold line running across its surface, giving it a slightly bent or folded appearance.
def model_119054_4e1076ec_0040():
    """Model: Mirror v1 (6)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 472, perimeter: 91
            with BuildLine():
                Line((-8, 14.75), (8, 14.75))
                Line((-8, -14.75), (-8, 14.75))
                Line((8, -14.75), (-8, -14.75))
                Line((8, 14.75), (8, -14.75))
            make_face()
        # OneSide extrude, distance=0.39
        extrude(amount=0.39)
    return part.part


# Description: This is a rounded rectangular bar or shaft with a long, slender cylindrical body featuring hemispherical or rounded end caps.
def model_119465_4fad1b4f_0001():
    """Model: Component28"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with Locations((9.6077055265, 11.0952601064)):
                Circle(0.75)
        # OneSide extrude, distance=15
        extrude(amount=15)
    return part.part


# Description: This is a rectangular prism or block-shaped part with a tall, narrow elongated form featuring beveled or angled edges on its faces, giving it a slightly tapered appearance.
def model_119465_4fad1b4f_0002():
    """Model: Component34"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.8609922608, perimeter: 6.3399484053
            with BuildLine():
                Line((8.7, 12.8699742027), (9, 12.8699742027))
                Line((8.7, 10), (8.7, 12.8699742027))
                Line((9, 10), (8.7, 10))
                Line((9, 12.8699742027), (9, 10))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a cylindrical mesh or perforated filter housing with an open top and bottom, featuring a solid base section and a mesh-textured upper section with a central rectangular slot or opening.
def model_119553_c436b288_0009():
    """Model: separador v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4319689899, perimeter: 3.4557519189
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: This is a tapered cylindrical tool or stylus with a gradually narrowing shaft that transitions from a thicker rounded grip end to a sharp pointed tip, featuring a subtle curved profile along its length.
def model_119553_c436b288_0011():
    """Model: Pata reducida Carnage v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 32 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.8752010486, perimeter: 22.5470990904
            with BuildLine():
                Line((0.45, 0), (0.45, 5))
                CenterArc((0, 5), 0.45, -179.7142934876, 179.7142934876)
                Line((-0.4499944053, 4.9977560756), (-0.45, 0.0000005037))
                CenterArc((0, 0), 0.45, 179.9999358607, 30.0065227429)
                Line((2.2950900018, -4.2741192873), (-0.3896860664, -0.2250439284))
                CenterArc((2.4249853572, -4.1991046445), 0.15, 30.0064586036, 180)
                Line((2.5548807127, -4.1240900018), (0.45, 0))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.5654866776, perimeter: 3.7699111843
            with BuildLine():
                CenterArc((0, 5), 0.45, -179.7142934876, 179.7142934876)
                CenterArc((0, 5), 0.45, 0, 180.2857065124)
            make_face()
            with BuildLine():
                CenterArc((0, 5), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with BuildLine():
                CenterArc((2.4249853572, -4.1991046445), 0.15, 30.0064586036, 180)
                CenterArc((2.4249853572, -4.1991046445), 0.15, -149.9935413964, 180)
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: This is a elongated rectangular tray or channel with rounded end flanges and two parallel slot openings running along the top surface.
def model_119553_c436b288_0012():
    """Model: Biela 1 v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 11 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.0940008429, perimeter: 10.4883889804
            with BuildLine():
                CenterArc((-1.444, 0), 0.45, 90, 180)
                Line((-1.444, -0.45), (1.444, -0.45))
                CenterArc((1.444, 0), 0.45, -90, 180)
                Line((1.444, 0.45), (-1.444, 0.45))
            make_face()
            with BuildLine():
                CenterArc((-1.444, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.444, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: This is a rectangular duct or channel component with a elongated box-like shape featuring dark flanged ends, a recessed central cavity with blue-highlighted interior surfaces, and mesh or perforated side sections for ventilation or airflow.
def model_119553_c436b288_0013():
    """Model: Biela 2 v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.3308008429, perimeter: 8.7923889804
            with BuildLine():
                CenterArc((-1.02, 0), 0.45, 90, 180)
                Line((-1.02, -0.45), (1.02, -0.45))
                CenterArc((1.02, 0), 0.45, -90, 180)
                Line((1.02, 0.45), (-1.02, 0.45))
            make_face()
            with BuildLine():
                CenterArc((-1.02, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.02, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: This is a flat parallelogram-shaped plate or panel with a slanted rectangular form, featuring clean edges and a uniform thickness, commonly used as a structural component or mounting bracket.
def model_119787_9a55dfa9_0001():
    """Model: Component1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 216, perimeter: 60
            with BuildLine():
                Line((0, 0), (12, 0))
                Line((12, 0), (12, 18))
                Line((12, 18), (0, 18))
                Line((0, 0), (0, 18))
            make_face()
        # OneSide extrude, distance=0.35
        extrude(amount=0.35)
    return part.part


# Description: This is a bent or folded sheet metal bracket with a parallelogram-like shape, featuring two primary flat faces connected at an angle, internal structural reinforcement ribs or gussets, and sharp edges characteristic of stamped or laser-cut metal components.
def model_119787_9a55dfa9_0003():
    """Model: 1-7"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 15 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 17.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.69, perimeter: 3.5
            with BuildLine():
                Line((0, 1.5), (0, 0.35))
                Line((-0.6, 1.5), (0, 1.5))
                Line((-0.6, 1.5), (-0.6, 0.35))
                Line((-0.6, 0.35), (0, 0.35))
            make_face()
            # Profile area: 1.54, perimeter: 9.5
            with BuildLine():
                Line((-0.6, 0.35), (-0.6, 0))
                Line((-5, 0.35), (-0.6, 0.35))
                Line((-5, 0), (-5, 0.35))
                Line((-0.6, 0), (-5, 0))
            make_face()
            # Profile area: 0.21, perimeter: 1.9
            with BuildLine():
                Line((0, 0), (-0.6, 0))
                Line((0, 0.35), (0, 0))
                Line((-0.6, 0.35), (0, 0.35))
                Line((-0.6, 0.35), (-0.6, 0))
            make_face()
            # Profile area: 0.69, perimeter: 3.5
            with BuildLine():
                Line((-12, 0.35), (-11.4, 0.35))
                Line((-11.4, 1.5), (-11.4, 0.35))
                Line((-12, 1.5), (-11.4, 1.5))
                Line((-12, 0.35), (-12, 1.5))
            make_face()
            # Profile area: 0.9, perimeter: 4.2
            with BuildLine():
                Line((-0.6, 3), (-0.6, 1.5))
                Line((-0.6, 1.5), (0, 1.5))
                Line((0, 3), (0, 1.5))
                Line((-0.6, 3), (0, 3))
            make_face()
            # Profile area: 0.9, perimeter: 4.2
            with BuildLine():
                Line((-12, 1.5), (-11.4, 1.5))
                Line((-11.4, 3), (-11.4, 1.5))
                Line((-12, 3), (-11.4, 3))
                Line((-12, 1.5), (-12, 3))
            make_face()
            # Profile area: 1.54, perimeter: 9.5
            with BuildLine():
                Line((-7, 0), (-7, 0.35))
                Line((-11.4, 0.35), (-7, 0.35))
                Line((-11.4, 0.35), (-11.4, 0))
                Line((-7, 0), (-11.4, 0))
            make_face()
            # Profile area: 0.21, perimeter: 1.9
            with BuildLine():
                Line((-11.4, 0.35), (-11.4, 0))
                Line((-12, 0.35), (-11.4, 0.35))
                Line((-12, 0), (-12, 0.35))
                Line((-11.4, 0), (-12, 0))
            make_face()
        # OneSide extrude, distance=-6
        extrude(amount=-6)
    return part.part


# Description: This is a toroidal (doughnut-shaped) ring or washer with a smooth circular cross-section and a central hole, featuring textured or patterned surfaces on portions of its outer and inner edges.
def model_119790_1ed376f0_0005():
    """Model: Aluslevy 8 mm v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.1528859641, perimeter: 7.3199108829
            with BuildLine():
                CenterArc((0, 0), 0.74, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.425, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.22
        extrude(amount=0.22)
    return part.part


# Description: This is a simple elongated rectangular bar or rod with a uniform cross-section, oriented at an oblique angle, featuring clean edges and a solid, tapered appearance typical of a basic structural or support component.
def model_119870_fcffae11_0000():
    """Model: Component4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 9.1584831099, perimeter: 21.8316966505
            with BuildLine():
                Line((3.9158484509, 15), (3.0000001413, 15))
                Line((3.9158484509, 25.0000000314), (3.9158484509, 15))
                Line((3.0000001413, 25), (3.9158484509, 25.0000000314))
                Line((3.0000001413, 15), (3.0000001413, 25))
            make_face()
            # Profile area: 0.9010766103, perimeter: 3.7994386588
            with BuildLine():
                Line((3.9158484509, 10), (3.9158484509, 9.0161289802))
                Line((3.0000001413, 10), (3.9158484509, 10))
                Line((3.0000001413, 9.0161289802), (3.0000001413, 10))
                Line((3.9158484509, 9.0161289802), (3.0000001413, 9.0161289802))
            make_face()
            # Profile area: 0.2747544929, perimeter: 2.4316966191
            with BuildLine():
                Line((3.9158484509, 9.0161289802), (3.9158484509, 8.7161289802))
                Line((3.9158484509, 9.0161289802), (3.0000001413, 9.0161289802))
                Line((3.0000001413, 8.7161289802), (3.0000001413, 9.0161289802))
                Line((3.9158484509, 8.7161289802), (3.0000001413, 8.7161289802))
            make_face()
            # Profile area: 4.5792415478, perimeter: 11.8316966191
            with BuildLine():
                Line((3.0000001413, 10), (3.9158484509, 10))
                Line((3.9158484509, 15), (3.9158484509, 10))
                Line((3.9158484509, 15), (3.0000001413, 15))
                Line((3.0000001413, 10), (3.0000001413, 15))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is a blue plastic trim or deflector component with an elongated horizontal body, a curved right end, and a vertical mounting flange on the left side, designed for automotive or appliance applications.
def model_119915_a858f82a_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 25 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 55.72860322, perimeter: 55.6381376267
            with BuildLine():
                Line((-8.5, -2), (-8.5, -6))
                CenterArc((-6.5, -6), 2, -180, 180)
                Line((-4.5, -6), (-4.5, -2))
                CenterArc((-4, -2), 0.5, 90, 90)
                Line((0, -1.5), (-4, -1.5))
                Line((0, 0), (0, -1.5))
                Line((0, 0), (-14.6109127035, 0))
                CenterArc((-14.6109127035, -3.5), 3.5, 90, 45)
                Line((-20, -3.9393398282), (-17.0857864376, -1.0251262658))
                Line((-18.9393398282, -5), (-20, -3.9393398282))
                Line((-16.0251262658, -2.0857864376), (-18.9393398282, -5))
                CenterArc((-14.6109127035, -3.5), 2, 90, 45)
                Line((-9, -1.5), (-14.6109127035, -1.5))
                CenterArc((-9, -2), 0.5, 0, 90)
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a cylindrical barrel or drum with a slightly tapered body that curves outward toward the middle, featuring two flat circular end faces and a mesh or wireframe surface pattern visible on the curved sides.
def model_119921_5621fcb4_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 38.4845100065, perimeter: 21.9911485751
            Circle(3.5)
        # OneSide extrude, distance=8
        extrude(amount=8)
    return part.part


# Description: This is a dumbbell with a symmetrical design featuring two dark rounded weight plates on either end connected by a central blue grip bar with horizontal ribbing for ergonomic handling.
def model_120371_433ba1ca_0001():
    """Model: gear connector v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.7051863544, perimeter: 8.4150842609
            with BuildLine():
                CenterArc((0, 0), 1.27, -44.4240655643, 88.8481311286)
                Line((0.9070070019, -0.888953485), (3.2409059592, -0.888953485))
                Line((3.2409059592, 0.888953485), (3.2409059592, -0.888953485))
                Line((3.2409059592, 0.888953485), (0.9070070019, 0.888953485))
            make_face()
            # Profile area: 1.7687979638, perimeter: 10.6171561538
            with BuildLine():
                Line((6.4727178776, 0.888953485), (5.5748049164, 0.888953485))
                CenterArc((6.4818119184, 0), 0.889, 89.4138816144, 1.1722367713)
                CenterArc((6.4818119184, 0), 0.889, -89.4138816144, 178.8277632287)
                CenterArc((6.4818119184, 0), 0.889, -90.5861183856, 1.1722367712)
                Line((5.5748049164, -0.888953485), (6.4727178776, -0.888953485))
                CenterArc((6.4818119184, 0), 1.27, -135.5759344357, 271.1518688714)
            make_face()
            # Profile area: 3.7051863544, perimeter: 8.4150842609
            with BuildLine():
                Line((3.2409059592, 0.888953485), (3.2409059592, -0.888953485))
                Line((3.2409059592, -0.888953485), (5.5748049164, -0.888953485))
                CenterArc((6.4818119184, 0), 1.27, 135.5759344357, 88.8481311286)
                Line((5.5748049164, 0.888953485), (3.2409059592, 0.888953485))
            make_face()
            # Profile area: 1.7687979638, perimeter: 10.6171561538
            with BuildLine():
                CenterArc((0, 0), 1.27, 44.4240655643, 271.1518688714)
                Line((0.0090940408, -0.888953485), (0.9070070019, -0.888953485))
                CenterArc((0, 0), 0.889, -90.5861183856, 1.1722367713)
                CenterArc((0, 0), 0.889, 90.5861183856, 178.8277632287)
                CenterArc((0, 0), 0.889, 89.4138816143, 1.1722367713)
                Line((0.9070070019, 0.888953485), (0.0090940408, 0.888953485))
            make_face()
            # Profile area: 0.8154101796, perimeter: 6.539892769
            with BuildLine():
                CenterArc((6.4818119184, 0), 1.27, 135.5759344357, 88.8481311286)
                Line((5.5748049164, -0.888953485), (6.4727178776, -0.888953485))
                CenterArc((6.4818119184, 0), 0.889, 90.5861183856, 178.8277632288)
                Line((6.4727178776, 0.888953485), (5.5748049164, 0.888953485))
            make_face()
            # Profile area: 0.8154101796, perimeter: 6.539892769
            with BuildLine():
                Line((0.9070070019, 0.888953485), (0.0090940408, 0.888953485))
                CenterArc((0, 0), 0.889, -89.4138816144, 178.8277632287)
                Line((0.0090940408, -0.888953485), (0.9070070019, -0.888953485))
                CenterArc((0, 0), 1.27, -44.4240655643, 88.8481311286)
            make_face()
        # OneSide extrude, distance=0.7112
        extrude(amount=0.7112)
    return part.part


# Description: This is a roof rack cross bar with an elongated rectangular tube profile featuring black rubberized end caps on both sides and a blue metallic finish on the central beam section.
def model_120371_433ba1ca_0002():
    """Model: Short Extension v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.8150474778, perimeter: 6.4917675505
            with BuildLine():
                CenterArc((19.9578366273, 0), 1.27, 135.5887872008, 88.8224255983)
                Line((19.0506302354, -0.88875), (19.9367549409, -0.88875))
                CenterArc((19.9578366273, 0), 0.889, 91.3588356493, 177.2823287016)
                Line((19.9367549409, 0.88875), (19.0506302354, 0.88875))
            make_face()
            # Profile area: 0.8150474778, perimeter: 6.4917675505
            with BuildLine():
                Line((0.9072063919, 0.88875), (0.0210816864, 0.88875))
                CenterArc((0, 0), 0.889, -88.6411643508, 177.2823287015)
                Line((0.0210816864, -0.88875), (0.9072063919, -0.88875))
                CenterArc((0, 0), 1.27, -44.4112127992, 88.8224255983)
            make_face()
            # Profile area: 1.7691606656, perimeter: 10.6181283498
            with BuildLine():
                Line((19.9367549409, 0.88875), (19.0506302354, 0.88875))
                CenterArc((19.9578366273, 0), 0.889, 88.6411643508, 2.7176712985)
                CenterArc((19.9578366273, 0), 0.889, -88.6411643508, 177.2823287015)
                CenterArc((19.9578366273, 0), 0.889, -91.3588356492, 2.7176712984)
                Line((19.0506302354, -0.88875), (19.9367549409, -0.88875))
                CenterArc((19.9578366273, 0), 1.27, -135.5887872008, 271.1775744017)
            make_face()
            # Profile area: 1.7691606656, perimeter: 10.6181283498
            with BuildLine():
                CenterArc((0, 0), 1.27, 44.4112127992, 271.1775744017)
                Line((0.0210816864, -0.88875), (0.9072063919, -0.88875))
                CenterArc((0, 0), 0.889, -91.3588356492, 2.7176712985)
                CenterArc((0, 0), 0.889, 91.3588356492, 177.2823287015)
                CenterArc((0, 0), 0.889, 88.6411643508, 2.7176712985)
                Line((0.9072063919, 0.88875), (0.0210816864, 0.88875))
            make_face()
            # Profile area: 15.6810535283, perimeter: 21.8897334394
            with BuildLine():
                Line((9.9789183136, 0.88875), (9.9789183136, -0.88875))
                Line((9.9789183136, -0.88875), (19.0506302354, -0.88875))
                CenterArc((19.9578366273, 0), 1.27, 135.5887872008, 88.8224255983)
                Line((19.0506302354, 0.88875), (9.9789183136, 0.88875))
            make_face()
            # Profile area: 15.6810535283, perimeter: 21.8897334394
            with BuildLine():
                CenterArc((0, 0), 1.27, -44.4112127992, 88.8224255983)
                Line((0.9072063919, -0.88875), (9.9789183136, -0.88875))
                Line((9.9789183136, 0.88875), (9.9789183136, -0.88875))
                Line((9.9789183136, 0.88875), (0.9072063919, 0.88875))
            make_face()
        # OneSide extrude, distance=0.7112
        extrude(amount=0.7112)
    return part.part


# Description: This is a tapered needle or cone-shaped cylindrical pin with a smooth, gradually narrowing profile from one end to the other, featuring no holes or surface features.
def model_120454_c30d2e80_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Airfoil NACA 0012 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0816686726, perimeter: 2.0394212676
            with BuildLine():
                Line((0.9993147674, -0.0000995542), (1, 0))
                Line((1, 0), (0.9993147674, 0.0000995542))
                Line((0.9993147674, 0.0000995542), (0.9972609477, 0.000397414))
                Line((0.9972609477, 0.000397414), (0.9938441703, 0.0008911863))
                Line((0.9938441703, 0.0008911863), (0.9890738004, 0.0015769341))
                Line((0.9890738004, 0.0015769341), (0.9829629131, 0.0024492512))
                Line((0.9829629131, 0.0024492512), (0.9755282581, 0.0035013623))
                Line((0.9755282581, 0.0035013623), (0.9667902132, 0.0047252443))
                Line((0.9667902132, 0.0047252443), (0.9567727288, 0.0061117634))
                Line((0.9567727288, 0.0061117634), (0.9455032621, 0.0076508216))
                Line((0.9455032621, 0.0076508216), (0.9330127019, 0.0093315085))
                Line((0.9330127019, 0.0093315085), (0.919335284, 0.0111422492))
                Line((0.919335284, 0.0111422492), (0.9045084972, 0.0130709457))
                Line((0.9045084972, 0.0130709457), (0.8885729807, 0.0151051033))
                Line((0.8885729807, 0.0151051033), (0.8715724127, 0.0172319406))
                Line((0.8715724127, 0.0172319406), (0.8535533906, 0.0194384764))
                Line((0.8535533906, 0.0194384764), (0.8345653032, 0.0217115946))
                Line((0.8345653032, 0.0217115946), (0.8146601955, 0.0240380832))
                Line((0.8146601955, 0.0240380832), (0.7938926261, 0.02640465))
                Line((0.7938926261, 0.02640465), (0.7723195175, 0.0287979161))
                Line((0.7723195175, 0.0287979161), (0.75, 0.0312043904))
                Line((0.75, 0.0312043904), (0.7269952499, 0.03361043))
                Line((0.7269952499, 0.03361043), (0.7033683215, 0.0360021906))
                Line((0.7033683215, 0.0360021906), (0.6791839748, 0.0383655749))
                Line((0.6791839748, 0.0383655749), (0.6545084972, 0.0406861839))
                Line((0.6545084972, 0.0406861839), (0.6294095226, 0.042949278))
                Line((0.6294095226, 0.042949278), (0.6039558454, 0.0451397549))
                Line((0.6039558454, 0.0451397549), (0.5782172325, 0.0472421489))
                Line((0.5782172325, 0.0472421489), (0.5522642316, 0.0492406577))
                Line((0.5522642316, 0.0492406577), (0.5261679781, 0.0511191993))
                Line((0.5261679781, 0.0511191993), (0.5, 0.052861502))
                Line((0.5, 0.052861502), (0.4738320219, 0.0544512277))
                Line((0.4738320219, 0.0544512277), (0.4477357684, 0.0558721285))
                Line((0.4477357684, 0.0558721285), (0.4217827675, 0.0571082323))
                Line((0.4217827675, 0.0571082323), (0.3960441546, 0.0581440552))
                Line((0.3960441546, 0.0581440552), (0.3705904774, 0.0589648327))
                Line((0.3705904774, 0.0589648327), (0.3454915028, 0.0595567645))
                Line((0.3454915028, 0.0595567645), (0.3208160252, 0.0599072632))
                Line((0.3208160252, 0.0599072632), (0.2966316785, 0.0600051983))
                Line((0.2966316785, 0.0600051983), (0.2730047501, 0.059841127))
                Line((0.2730047501, 0.059841127), (0.25, 0.0594075))
                Line((0.25, 0.0594075), (0.2276804825, 0.0586988364))
                Line((0.2276804825, 0.0586988364), (0.2061073739, 0.0577118565))
                Line((0.2061073739, 0.0577118565), (0.1853398045, 0.0564455671))
                Line((0.1853398045, 0.0564455671), (0.1654346968, 0.0549012929))
                Line((0.1654346968, 0.0549012929), (0.1464466094, 0.0530826501))
                Line((0.1464466094, 0.0530826501), (0.1284275873, 0.0509954607))
                Line((0.1284275873, 0.0509954607), (0.1114270193, 0.0486476069))
                Line((0.1114270193, 0.0486476069), (0.0954915028, 0.0460488284))
                Line((0.0954915028, 0.0460488284), (0.080664716, 0.0432104676))
                Line((0.080664716, 0.0432104676), (0.0669872981, 0.0401451679))
                Line((0.0669872981, 0.0401451679), (0.0544967379, 0.0368665348))
                Line((0.0544967379, 0.0368665348), (0.0432272712, 0.0333887691))
                Line((0.0432272712, 0.0333887691), (0.0332097868, 0.0297262832))
                Line((0.0332097868, 0.0297262832), (0.0244717419, 0.0258933127))
                Line((0.0244717419, 0.0258933127), (0.0170370869, 0.0219035367))
                Line((0.0170370869, 0.0219035367), (0.0109261996, 0.0177697166))
                Line((0.0109261996, 0.0177697166), (0.0061558297, 0.0135033681))
                Line((0.0061558297, 0.0135033681), (0.0027390523, 0.0091144757))
                Line((0.0027390523, 0.0091144757), (0.0006852326, 0.004611259))
                Line((0.0006852326, 0.004611259), (0, 0))
                Line((0, 0), (0.0006852326, -0.004611259))
                Line((0.0006852326, -0.004611259), (0.0027390523, -0.0091144757))
                Line((0.0027390523, -0.0091144757), (0.0061558297, -0.0135033681))
                Line((0.0061558297, -0.0135033681), (0.0109261996, -0.0177697166))
                Line((0.0109261996, -0.0177697166), (0.0170370869, -0.0219035367))
                Line((0.0170370869, -0.0219035367), (0.0244717419, -0.0258933127))
                Line((0.0244717419, -0.0258933127), (0.0332097868, -0.0297262832))
                Line((0.0332097868, -0.0297262832), (0.0432272712, -0.0333887691))
                Line((0.0432272712, -0.0333887691), (0.0544967379, -0.0368665348))
                Line((0.0544967379, -0.0368665348), (0.0669872981, -0.0401451679))
                Line((0.0669872981, -0.0401451679), (0.080664716, -0.0432104676))
                Line((0.080664716, -0.0432104676), (0.0954915028, -0.0460488284))
                Line((0.0954915028, -0.0460488284), (0.1114270193, -0.0486476069))
                Line((0.1114270193, -0.0486476069), (0.1284275873, -0.0509954607))
                Line((0.1284275873, -0.0509954607), (0.1464466094, -0.0530826501))
                Line((0.1464466094, -0.0530826501), (0.1654346968, -0.0549012929))
                Line((0.1654346968, -0.0549012929), (0.1853398045, -0.0564455671))
                Line((0.1853398045, -0.0564455671), (0.2061073739, -0.0577118565))
                Line((0.2061073739, -0.0577118565), (0.2276804825, -0.0586988364))
                Line((0.2276804825, -0.0586988364), (0.25, -0.0594075))
                Line((0.25, -0.0594075), (0.2730047501, -0.059841127))
                Line((0.2730047501, -0.059841127), (0.2966316785, -0.0600051983))
                Line((0.2966316785, -0.0600051983), (0.3208160252, -0.0599072632))
                Line((0.3208160252, -0.0599072632), (0.3454915028, -0.0595567645))
                Line((0.3454915028, -0.0595567645), (0.3705904774, -0.0589648327))
                Line((0.3705904774, -0.0589648327), (0.3960441546, -0.0581440552))
                Line((0.3960441546, -0.0581440552), (0.4217827675, -0.0571082323))
                Line((0.4217827675, -0.0571082323), (0.4477357684, -0.0558721285))
                Line((0.4477357684, -0.0558721285), (0.4738320219, -0.0544512277))
                Line((0.4738320219, -0.0544512277), (0.5, -0.052861502))
                Line((0.5, -0.052861502), (0.5261679781, -0.0511191993))
                Line((0.5261679781, -0.0511191993), (0.5522642316, -0.0492406577))
                Line((0.5522642316, -0.0492406577), (0.5782172325, -0.0472421489))
                Line((0.5782172325, -0.0472421489), (0.6039558454, -0.0451397549))
                Line((0.6039558454, -0.0451397549), (0.6294095226, -0.042949278))
                Line((0.6294095226, -0.042949278), (0.6545084972, -0.0406861839))
                Line((0.6545084972, -0.0406861839), (0.6791839748, -0.0383655749))
                Line((0.6791839748, -0.0383655749), (0.7033683215, -0.0360021906))
                Line((0.7033683215, -0.0360021906), (0.7269952499, -0.03361043))
                Line((0.7269952499, -0.03361043), (0.75, -0.0312043904))
                Line((0.75, -0.0312043904), (0.7723195175, -0.0287979161))
                Line((0.7723195175, -0.0287979161), (0.7938926261, -0.02640465))
                Line((0.7938926261, -0.02640465), (0.8146601955, -0.0240380832))
                Line((0.8146601955, -0.0240380832), (0.8345653032, -0.0217115946))
                Line((0.8345653032, -0.0217115946), (0.8535533906, -0.0194384764))
                Line((0.8535533906, -0.0194384764), (0.8715724127, -0.0172319406))
                Line((0.8715724127, -0.0172319406), (0.8885729807, -0.0151051033))
                Line((0.8885729807, -0.0151051033), (0.9045084972, -0.0130709457))
                Line((0.9045084972, -0.0130709457), (0.919335284, -0.0111422492))
                Line((0.919335284, -0.0111422492), (0.9330127019, -0.0093315085))
                Line((0.9330127019, -0.0093315085), (0.9455032621, -0.0076508216))
                Line((0.9455032621, -0.0076508216), (0.9567727288, -0.0061117634))
                Line((0.9567727288, -0.0061117634), (0.9667902132, -0.0047252443))
                Line((0.9667902132, -0.0047252443), (0.9755282581, -0.0035013623))
                Line((0.9755282581, -0.0035013623), (0.9829629131, -0.0024492512))
                Line((0.9829629131, -0.0024492512), (0.9890738004, -0.0015769341))
                Line((0.9890738004, -0.0015769341), (0.9938441703, -0.0008911863))
                Line((0.9938441703, -0.0008911863), (0.9972609477, -0.000397414))
                Line((0.9972609477, -0.000397414), (0.9993147674, -0.0000995542))
            make_face()
        # OneSide extrude, distance=20
        extrude(amount=20)
    return part.part


# Description: This is a shoe sole or heel component with a rounded, arched profile featuring a textured top surface and a curved bottom surface, with a recessed slot or channel running along one side.
def model_120535_e304dfca_0002():
    """Model: component C tutorial v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 54 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 7.4039676261, perimeter: 10.6834948714
            with BuildLine():
                Line((2.2961925006, 7.6), (0, 7.6))
                Line((0, 7.6), (0, 4.85))
                Line((0, 4.85), (2.1524779535, 4.85))
                Line((2.1524779535, 4.85), (2.7319912487, 4.85))
                Line((2.7319912487, 4.85), (2.7319912487, 7.0603192373))
                CenterArc((0, 5.3), 3.25, 32.7951249663, 12.2523390147)
            make_face()
            # Profile area: 27.0236557736, perimeter: 26.1011322848
            with BuildLine():
                Line((0, 0.5), (0, 0))
                Line((0, 1.2), (0, 0.5))
                Line((0, 1.85), (0, 1.2))
                Line((0, 2.55), (0, 1.85))
                Line((0, 3.2), (0, 2.55))
                Line((0, 3.7), (0, 3.2))
                Line((0, 4.35), (0, 3.7))
                Line((0, 4.85), (0, 4.35))
                Line((0, 7.6), (0, 4.85))
                Line((2.2961925006, 7.6), (0, 7.6))
                CenterArc((0, 5.3), 3.25, 45.0474639811, 134.9525360189)
                Line((-3.25, 5.3), (-3.25, 0))
                Line((-3.25, 0), (0, 0))
            make_face()
            # Profile area: 1.3797935599, perimeter: 6.5191742398
            with BuildLine():
                Line((2.7595871199, 0), (2.7595871199, 0.5))
                Line((2.7595871199, 0.5), (2.1524779535, 0.5))
                Line((0, 0.5), (2.1524779535, 0.5))
                Line((0, 0.5), (0, 0))
                Line((0, 0), (2.7595871199, 0))
            make_face()
            # Profile area: 4.7228519025, perimeter: 19.4298705475
            with BuildLine():
                Line((2.7595871199, 0), (3.25, 0))
                Line((3.25, 0), (3.25, 5.3))
                CenterArc((0, 5.3), 3.25, 0, 32.7951249663)
                Line((2.7319912487, 4.85), (2.7319912487, 7.0603192373))
                Line((2.1524779535, 4.85), (2.7319912487, 4.85))
                Line((2.1524779535, 4.35), (2.1524779535, 4.85))
                Line((2.7319912487, 4.35), (2.1524779535, 4.35))
                Line((2.7319912487, 3.7), (2.7319912487, 4.35))
                Line((2.1524779535, 3.7), (2.7319912487, 3.7))
                Line((2.1524779535, 3.2), (2.1524779535, 3.7))
                Line((2.7319912487, 3.2), (2.1524779535, 3.2))
                Line((2.7319912487, 2.55), (2.7319912487, 3.2))
                Line((2.1524779535, 2.55), (2.7319912487, 2.55))
                Line((2.1524779535, 1.85), (2.1524779535, 2.55))
                Line((2.7595871199, 1.85), (2.1524779535, 1.85))
                Line((2.7595871199, 1.2), (2.7595871199, 1.85))
                Line((2.1524779535, 1.2), (2.7595871199, 1.2))
                Line((2.1524779535, 0.5), (2.1524779535, 1.2))
                Line((2.7595871199, 0.5), (2.1524779535, 0.5))
                Line((2.7595871199, 0), (2.7595871199, 0.5))
            make_face()
            # Profile area: 1.0762389768, perimeter: 5.304955907
            with BuildLine():
                Line((0, 4.85), (2.1524779535, 4.85))
                Line((0, 4.85), (0, 4.35))
                Line((0, 4.35), (2.1524779535, 4.35))
                Line((2.1524779535, 4.35), (2.1524779535, 4.85))
            make_face()
            # Profile area: 1.7757943117, perimeter: 6.7639824974
            with BuildLine():
                Line((0, 4.35), (2.1524779535, 4.35))
                Line((0, 4.35), (0, 3.7))
                Line((0, 3.7), (2.1524779535, 3.7))
                Line((2.1524779535, 3.7), (2.7319912487, 3.7))
                Line((2.7319912487, 3.7), (2.7319912487, 4.35))
                Line((2.7319912487, 4.35), (2.1524779535, 4.35))
            make_face()
            # Profile area: 1.0762389768, perimeter: 5.304955907
            with BuildLine():
                Line((0, 3.7), (2.1524779535, 3.7))
                Line((0, 3.7), (0, 3.2))
                Line((0, 3.2), (2.1524779535, 3.2))
                Line((2.1524779535, 3.2), (2.1524779535, 3.7))
            make_face()
            # Profile area: 1.7757943117, perimeter: 6.7639824974
            with BuildLine():
                Line((0, 3.2), (2.1524779535, 3.2))
                Line((0, 3.2), (0, 2.55))
                Line((0, 2.55), (2.1524779535, 2.55))
                Line((2.1524779535, 2.55), (2.7319912487, 2.55))
                Line((2.7319912487, 2.55), (2.7319912487, 3.2))
                Line((2.7319912487, 3.2), (2.1524779535, 3.2))
            make_face()
            # Profile area: 1.5067345675, perimeter: 5.704955907
            with BuildLine():
                Line((0, 2.55), (2.1524779535, 2.55))
                Line((0, 2.55), (0, 1.85))
                Line((0, 1.85), (2.1524779535, 1.85))
                Line((2.1524779535, 1.85), (2.1524779535, 2.55))
            make_face()
            # Profile area: 1.7937316279, perimeter: 6.8191742398
            with BuildLine():
                Line((0, 1.85), (2.1524779535, 1.85))
                Line((0, 1.85), (0, 1.2))
                Line((0, 1.2), (2.1524779535, 1.2))
                Line((2.1524779535, 1.2), (2.7595871199, 1.2))
                Line((2.7595871199, 1.2), (2.7595871199, 1.85))
                Line((2.7595871199, 1.85), (2.1524779535, 1.85))
            make_face()
            # Profile area: 1.5067345675, perimeter: 5.704955907
            with BuildLine():
                Line((2.1524779535, 0.5), (2.1524779535, 1.2))
                Line((0, 1.2), (2.1524779535, 1.2))
                Line((0, 1.2), (0, 0.5))
                Line((0, 0.5), (2.1524779535, 0.5))
            make_face()
        # OneSide extrude, distance=-1.4
        extrude(amount=-1.4)
    return part.part


# Description: This is a long, flat, elongated metal tray or channel with a trapezoidal profile, featuring a shallow rectangular basin and angled side walls that taper slightly toward the ends.
def model_120539_4492fbcd_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0342636892, perimeter: 1.5428097245
            with BuildLine():
                Line((0.7, 0), (0.7, -0.05))
                Line((0, 0), (0.7, 0))
                Line((0, -0.05), (0, 0))
                Line((0, -0.05), (0.0375, -0.05))
                CenterArc((0.05, -0.05), 0.0125, 0, 180)
                Line((0.0625, -0.05), (0.4371081208, -0.05))
                CenterArc((0.4496081208, -0.05), 0.0125, 0, 180)
                Line((0.4621081208, -0.05), (0.6378006311, -0.05))
                CenterArc((0.6503006311, -0.05), 0.0125, 0, 180)
                Line((0.6628006311, -0.05), (0.7, -0.05))
            make_face()
            # Profile area: 0.0342636892, perimeter: 1.5428097245
            with BuildLine():
                Line((0.7, -0.05), (0.7, -0.1))
                Line((0.6628006311, -0.05), (0.7, -0.05))
                CenterArc((0.6503006311, -0.05), 0.0125, 180, 180)
                Line((0.4621081208, -0.05), (0.6378006311, -0.05))
                CenterArc((0.4496081208, -0.05), 0.0125, 180, 180)
                Line((0.0625, -0.05), (0.4371081208, -0.05))
                CenterArc((0.05, -0.05), 0.0125, 180, 180)
                Line((0, -0.05), (0.0375, -0.05))
                Line((0, -0.1), (0, -0.05))
                Line((0.7, -0.1), (0, -0.1))
            make_face()
        # OneSide extrude, distance=0.0125
        extrude(amount=0.0125)
    return part.part


# Description: This is a flat parallelogram plate with a uniform rectangular shape, slightly skewed or angled, featuring clean edges and a simple geometric form with no holes, slots, or additional features.
def model_120700_d818883a_0005():
    """Model: стенка"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 57 constraints, 20 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0875, perimeter: 1.2
            with BuildLine():
                Line((0.6, 0.25), (0.6, 0))
                Line((0.6, 0.25), (0.25, 0.25))
                Line((0.25, 0.25), (0.25, 0))
                Line((0.25, 0), (0.6, 0))
            make_face()
            # Profile area: 0.0625, perimeter: 1
            with BuildLine():
                Line((11.75, 18), (11.75, 17.75))
                Line((12, 17.75), (11.75, 17.75))
                Line((12, 17.75), (12, 18))
                Line((12, 18), (11.75, 18))
            make_face()
            # Profile area: 0.0875, perimeter: 1.2
            with BuildLine():
                Line((1.2, 0.25), (1.2, 0))
                Line((1.2, 0.25), (0.85, 0.25))
                Line((0.85, 0.25), (0.85, 0))
                Line((0.85, 0), (1.2, 0))
            make_face()
            # Profile area: 1.2625, perimeter: 10.6
            with BuildLine():
                Line((6.35, 18), (6.35, 17.75))
                Line((11.4, 17.75), (6.35, 17.75))
                Line((11.4, 18), (11.4, 17.75))
                Line((11.4, 18), (6.35, 18))
            make_face()
            # Profile area: 1.2, perimeter: 10.1
            with BuildLine():
                Line((1.2, 18), (1.2, 17.75))
                Line((6, 17.75), (1.2, 17.75))
                Line((6, 18), (6, 17.75))
                Line((6, 18), (1.2, 18))
            make_face()
            # Profile area: 4.2, perimeter: 34.1
            with BuildLine():
                Line((12, 17.4), (11.75, 17.4))
                Line((11.75, 17.4), (11.75, 0.6))
                Line((12, 0.6), (11.75, 0.6))
                Line((12, 0.6), (12, 17.4))
            make_face()
            # Profile area: 0.0875, perimeter: 1.2
            with BuildLine():
                Line((6.35, 0.25), (6, 0.25))
                Line((6, 0.25), (6, 0))
                Line((6, 0), (6.35, 0))
                Line((6.35, 0.25), (6.35, 0))
            make_face()
            # Profile area: 0.0625, perimeter: 1
            with BuildLine():
                Line((0.6, 18), (0.6, 17.75))
                Line((0.85, 17.75), (0.6, 17.75))
                Line((0.85, 18), (0.85, 17.75))
                Line((0.85, 18), (0.6, 18))
            make_face()
            # Profile area: 1.2625, perimeter: 10.6
            with BuildLine():
                Line((11.4, 0.25), (11.4, 0))
                Line((11.4, 0.25), (6.35, 0.25))
                Line((6.35, 0.25), (6.35, 0))
                Line((6.35, 0), (11.4, 0))
            make_face()
            # Profile area: 0.0875, perimeter: 1.2
            with BuildLine():
                Line((12, 0.25), (11.75, 0.25))
                Line((12, 0.25), (12, 0.6))
                Line((12, 0.6), (11.75, 0.6))
                Line((11.75, 0.6), (11.75, 0.25))
            make_face()
            # Profile area: 0.0625, perimeter: 1
            with BuildLine():
                Line((0.25, 17.75), (0, 17.75))
                Line((0.25, 18), (0.25, 17.75))
                Line((0.25, 18), (0, 18))
                Line((0, 18), (0, 17.75))
            make_face()
            # Profile area: 0.0875, perimeter: 1.2
            with BuildLine():
                Line((11.4, 0), (11.75, 0))
                Line((11.75, 0.25), (11.75, 0))
                Line((11.75, 0.25), (11.4, 0.25))
                Line((11.4, 0.25), (11.4, 0))
            make_face()
            # Profile area: 0.0625, perimeter: 1
            with BuildLine():
                Line((0.25, 0.25), (0.25, 0))
                Line((0.25, 0.25), (0, 0.25))
                Line((0, 0.25), (0, 0))
                Line((0, 0), (0.25, 0))
            make_face()
            # Profile area: 0.0625, perimeter: 1
            with BuildLine():
                Line((0.85, 0.25), (0.85, 0))
                Line((0.85, 0.25), (0.6, 0.25))
                Line((0.6, 0.25), (0.6, 0))
                Line((0.6, 0), (0.85, 0))
            make_face()
            # Profile area: 1.2, perimeter: 10.1
            with BuildLine():
                Line((6, 0.25), (6, 0))
                Line((6, 0.25), (1.2, 0.25))
                Line((1.2, 0.25), (1.2, 0))
                Line((1.2, 0), (6, 0))
            make_face()
            # Profile area: 0.0625, perimeter: 1
            with BuildLine():
                Line((11.75, 0), (12, 0))
                Line((12, 0), (12, 0.25))
                Line((12, 0.25), (11.75, 0.25))
                Line((11.75, 0.25), (11.75, 0))
            make_face()
            # Profile area: 0.0875, perimeter: 1.2
            with BuildLine():
                Line((6, 18), (6, 17.75))
                Line((6.35, 17.75), (6, 17.75))
                Line((6.35, 18), (6.35, 17.75))
                Line((6.35, 18), (6, 18))
            make_face()
            # Profile area: 0.0875, perimeter: 1.2
            with BuildLine():
                Line((11.4, 18), (11.4, 17.75))
                Line((11.75, 17.75), (11.4, 17.75))
                Line((11.75, 18), (11.75, 17.75))
                Line((11.75, 18), (11.4, 18))
            make_face()
            # Profile area: 0.0875, perimeter: 1.2
            with BuildLine():
                Line((0.85, 18), (0.85, 17.75))
                Line((1.2, 17.75), (0.85, 17.75))
                Line((1.2, 18), (1.2, 17.75))
                Line((1.2, 18), (0.85, 18))
            make_face()
            # Profile area: 4.2, perimeter: 34.1
            with BuildLine():
                Line((0.25, 0.6), (0, 0.6))
                Line((0.25, 9.45), (0.25, 0.6))
                Line((0.25, 9.8), (0.25, 9.45))
                Line((0.25, 17.4), (0.25, 9.8))
                Line((0.25, 17.4), (0, 17.4))
                Line((0, 17.4), (0, 0.6))
            make_face()
            # Profile area: 0.0875, perimeter: 1.2
            with BuildLine():
                Line((0.25, 18), (0.25, 17.75))
                Line((0.6, 17.75), (0.25, 17.75))
                Line((0.6, 18), (0.6, 17.75))
                Line((0.6, 18), (0.25, 18))
            make_face()
            # Profile area: 0.0875, perimeter: 1.2
            with BuildLine():
                Line((12, 17.75), (11.75, 17.75))
                Line((11.75, 17.75), (11.75, 17.4))
                Line((12, 17.4), (11.75, 17.4))
                Line((12, 17.4), (12, 17.75))
            make_face()
            # Profile area: 0.0875, perimeter: 1.2
            with BuildLine():
                Line((0.25, 0.25), (0, 0.25))
                Line((0.25, 0.6), (0.25, 0.25))
                Line((0.25, 0.6), (0, 0.6))
                Line((0, 0.6), (0, 0.25))
            make_face()
            # Profile area: 0.0875, perimeter: 1.2
            with BuildLine():
                Line((0.25, 17.4), (0, 17.4))
                Line((0.25, 17.75), (0.25, 17.4))
                Line((0.25, 17.75), (0, 17.75))
                Line((0, 17.75), (0, 17.4))
            make_face()
            # Profile area: 0.1225, perimeter: 1.4
            with BuildLine():
                Line((0.6, 0.6), (0.6, 0.25))
                Line((0.6, 0.6), (0.25, 0.6))
                Line((0.25, 0.6), (0.25, 0.25))
                Line((0.6, 0.25), (0.25, 0.25))
            make_face()
            # Profile area: 0.0875, perimeter: 1.2
            with BuildLine():
                Line((0.85, 0.6), (0.85, 0.25))
                Line((0.85, 0.6), (0.6, 0.6))
                Line((0.6, 0.6), (0.6, 0.25))
                Line((0.85, 0.25), (0.6, 0.25))
            make_face()
            # Profile area: 0.1225, perimeter: 1.4
            with BuildLine():
                Line((1.2, 0.6), (1.2, 0.25))
                Line((1.2, 0.6), (0.85, 0.6))
                Line((0.85, 0.6), (0.85, 0.25))
                Line((1.2, 0.25), (0.85, 0.25))
            make_face()
            # Profile area: 1.68, perimeter: 10.3
            with BuildLine():
                Line((6, 0.6), (1.2, 0.6))
                Line((1.2, 0.6), (1.2, 0.25))
                Line((6, 0.25), (1.2, 0.25))
                Line((6, 0.6), (6, 0.25))
            make_face()
            # Profile area: 11.04, perimeter: 14.2
            with BuildLine():
                Line((6, 2.9), (6, 0.6))
                Line((6, 2.9), (1.2, 2.9))
                Line((1.2, 2.9), (1.2, 0.6))
                Line((6, 0.6), (1.2, 0.6))
            make_face()
            # Profile area: 0.805, perimeter: 5.3
            with BuildLine():
                Line((6.35, 2.9), (6.35, 0.6))
                Line((6.35, 2.9), (6, 2.9))
                Line((6, 2.9), (6, 0.6))
                Line((6.35, 0.6), (6, 0.6))
            make_face()
            # Profile area: 84.84, perimeter: 43.7
            with BuildLine():
                Line((11.4, 17.4), (11.4, 0.6))
                Line((11.4, 17.4), (6.35, 17.4))
                Line((6.35, 17.4), (6.35, 9.8))
                Line((6.35, 9.8), (6.35, 9.45))
                Line((6.35, 9.45), (6.35, 7.5))
                Line((6.35, 7.5), (6.35, 7.15))
                Line((6.35, 7.15), (6.35, 5.2))
                Line((6.35, 5.2), (6.35, 2.9))
                Line((6.35, 2.9), (6.35, 0.6))
                Line((11.4, 0.6), (6.35, 0.6))
            make_face()
            # Profile area: 5.88, perimeter: 34.3
            with BuildLine():
                Line((11.75, 0.6), (11.4, 0.6))
                Line((11.75, 17.4), (11.75, 0.6))
                Line((11.75, 17.4), (11.4, 17.4))
                Line((11.4, 17.4), (11.4, 0.6))
            make_face()
            # Profile area: 0.1225, perimeter: 1.4
            with BuildLine():
                Line((11.75, 0.25), (11.4, 0.25))
                Line((11.75, 0.6), (11.75, 0.25))
                Line((11.75, 0.6), (11.4, 0.6))
                Line((11.4, 0.6), (11.4, 0.25))
            make_face()
            # Profile area: 1.7675, perimeter: 10.8
            with BuildLine():
                Line((11.4, 0.6), (11.4, 0.25))
                Line((11.4, 0.6), (6.35, 0.6))
                Line((6.35, 0.6), (6.35, 0.25))
                Line((11.4, 0.25), (6.35, 0.25))
            make_face()
            # Profile area: 0.1225, perimeter: 1.4
            with BuildLine():
                Line((6.35, 0.6), (6.35, 0.25))
                Line((6.35, 0.6), (6, 0.6))
                Line((6, 0.6), (6, 0.25))
                Line((6.35, 0.25), (6, 0.25))
            make_face()
            # Profile area: 0.1225, perimeter: 1.4
            with BuildLine():
                Line((11.4, 17.75), (11.4, 17.4))
                Line((11.75, 17.4), (11.4, 17.4))
                Line((11.75, 17.75), (11.75, 17.4))
                Line((11.75, 17.75), (11.4, 17.75))
            make_face()
            # Profile area: 1.7675, perimeter: 10.8
            with BuildLine():
                Line((6.35, 17.75), (6.35, 17.4))
                Line((11.4, 17.4), (6.35, 17.4))
                Line((11.4, 17.75), (11.4, 17.4))
                Line((11.4, 17.75), (6.35, 17.75))
            make_face()
            # Profile area: 0.1225, perimeter: 1.4
            with BuildLine():
                Line((6, 17.75), (6, 17.4))
                Line((6.35, 17.4), (6, 17.4))
                Line((6.35, 17.75), (6.35, 17.4))
                Line((6.35, 17.75), (6, 17.75))
            make_face()
            # Profile area: 1.68, perimeter: 10.3
            with BuildLine():
                Line((1.2, 17.75), (1.2, 17.4))
                Line((6, 17.4), (1.2, 17.4))
                Line((6, 17.75), (6, 17.4))
                Line((6, 17.75), (1.2, 17.75))
            make_face()
            # Profile area: 0.1225, perimeter: 1.4
            with BuildLine():
                Line((0.85, 17.75), (0.85, 17.4))
                Line((1.2, 17.4), (0.85, 17.4))
                Line((1.2, 17.75), (1.2, 17.4))
                Line((1.2, 17.75), (0.85, 17.75))
            make_face()
            # Profile area: 0.0875, perimeter: 1.2
            with BuildLine():
                Line((0.6, 17.75), (0.6, 17.4))
                Line((0.85, 17.4), (0.6, 17.4))
                Line((0.85, 17.75), (0.85, 17.4))
                Line((0.85, 17.75), (0.6, 17.75))
            make_face()
            # Profile area: 0.1225, perimeter: 1.4
            with BuildLine():
                Line((0.6, 17.4), (0.25, 17.4))
                Line((0.6, 17.75), (0.6, 17.4))
                Line((0.6, 17.75), (0.25, 17.75))
                Line((0.25, 17.75), (0.25, 17.4))
            make_face()
            # Profile area: 2.66, perimeter: 15.9
            with BuildLine():
                Line((0.6, 9.8), (0.25, 9.8))
                Line((0.6, 17.4), (0.6, 9.8))
                Line((0.6, 17.4), (0.25, 17.4))
                Line((0.25, 17.4), (0.25, 9.8))
            make_face()
            # Profile area: 0.1225, perimeter: 1.4
            with BuildLine():
                Line((0.25, 9.45), (0.6, 9.45))
                Line((0.6, 9.8), (0.6, 9.45))
                Line((0.6, 9.8), (0.25, 9.8))
                Line((0.25, 9.8), (0.25, 9.45))
            make_face()
            # Profile area: 3.0975, perimeter: 18.4
            with BuildLine():
                Line((0.6, 0.6), (0.25, 0.6))
                Line((0.6, 9.45), (0.6, 0.6))
                Line((0.25, 9.45), (0.6, 9.45))
                Line((0.25, 9.45), (0.25, 0.6))
            make_face()
            # Profile area: 2.2125, perimeter: 18.2
            with BuildLine():
                Line((0.85, 2.9), (0.85, 0.6))
                Line((0.85, 5.2), (0.85, 2.9))
                Line((0.85, 7.15), (0.85, 5.2))
                Line((0.85, 7.5), (0.85, 7.15))
                Line((0.85, 9.45), (0.85, 7.5))
                Line((0.6, 9.45), (0.85, 9.45))
                Line((0.6, 9.45), (0.6, 0.6))
                Line((0.85, 0.6), (0.6, 0.6))
            make_face()
            # Profile area: 0.805, perimeter: 5.3
            with BuildLine():
                Line((1.2, 2.9), (1.2, 0.6))
                Line((1.2, 2.9), (0.85, 2.9))
                Line((0.85, 2.9), (0.85, 0.6))
                Line((1.2, 0.6), (0.85, 0.6))
            make_face()
            # Profile area: 0.805, perimeter: 5.3
            with BuildLine():
                Line((1.2, 5.2), (1.2, 2.9))
                Line((1.2, 5.2), (0.85, 5.2))
                Line((0.85, 5.2), (0.85, 2.9))
                Line((1.2, 2.9), (0.85, 2.9))
            make_face()
            # Profile area: 11.04, perimeter: 14.2
            with BuildLine():
                Line((6, 5.2), (6, 2.9))
                Line((6, 5.2), (1.2, 5.2))
                Line((1.2, 5.2), (1.2, 2.9))
                Line((6, 2.9), (1.2, 2.9))
            make_face()
            # Profile area: 0.805, perimeter: 5.3
            with BuildLine():
                Line((6.35, 5.2), (6, 5.2))
                Line((6, 5.2), (6, 2.9))
                Line((6.35, 2.9), (6, 2.9))
                Line((6.35, 5.2), (6.35, 2.9))
            make_face()
            # Profile area: 0.6825, perimeter: 4.6
            with BuildLine():
                Line((6.35, 7.15), (6, 7.15))
                Line((6, 7.15), (6, 5.2))
                Line((6.35, 5.2), (6, 5.2))
                Line((6.35, 7.15), (6.35, 5.2))
            make_face()
            # Profile area: 0.1225, perimeter: 1.4
            with BuildLine():
                Line((6.35, 7.5), (6, 7.5))
                Line((6, 7.5), (6, 7.15))
                Line((6.35, 7.15), (6, 7.15))
                Line((6.35, 7.5), (6.35, 7.15))
            make_face()
            # Profile area: 0.6825, perimeter: 4.6
            with BuildLine():
                Line((6, 9.45), (6.35, 9.45))
                Line((6, 9.45), (6, 7.5))
                Line((6.35, 7.5), (6, 7.5))
                Line((6.35, 9.45), (6.35, 7.5))
            make_face()
            # Profile area: 0.1225, perimeter: 1.4
            with BuildLine():
                Line((6.35, 9.8), (6, 9.8))
                Line((6, 9.8), (6, 9.45))
                Line((6, 9.45), (6.35, 9.45))
                Line((6.35, 9.8), (6.35, 9.45))
            make_face()
            # Profile area: 2.66, perimeter: 15.9
            with BuildLine():
                Line((6.35, 17.4), (6, 17.4))
                Line((6, 17.4), (6, 9.8))
                Line((6.35, 9.8), (6, 9.8))
                Line((6.35, 17.4), (6.35, 9.8))
            make_face()
            # Profile area: 36.48, perimeter: 24.8
            with BuildLine():
                Line((1.2, 17.4), (1.2, 9.8))
                Line((6, 9.8), (1.2, 9.8))
                Line((6, 17.4), (6, 9.8))
                Line((6, 17.4), (1.2, 17.4))
            make_face()
            # Profile area: 2.66, perimeter: 15.9
            with BuildLine():
                Line((0.85, 17.4), (0.85, 9.8))
                Line((1.2, 9.8), (0.85, 9.8))
                Line((1.2, 17.4), (1.2, 9.8))
                Line((1.2, 17.4), (0.85, 17.4))
            make_face()
            # Profile area: 1.9, perimeter: 15.7
            with BuildLine():
                Line((0.85, 9.8), (0.6, 9.8))
                Line((0.85, 17.4), (0.85, 9.8))
                Line((0.85, 17.4), (0.6, 17.4))
                Line((0.6, 17.4), (0.6, 9.8))
            make_face()
            # Profile area: 0.0875, perimeter: 1.2
            with BuildLine():
                Line((0.6, 9.45), (0.85, 9.45))
                Line((0.85, 9.8), (0.85, 9.45))
                Line((0.85, 9.8), (0.6, 9.8))
                Line((0.6, 9.8), (0.6, 9.45))
            make_face()
            # Profile area: 0.1225, perimeter: 1.4
            with BuildLine():
                Line((0.85, 9.45), (1.2, 9.45))
                Line((1.2, 9.8), (1.2, 9.45))
                Line((1.2, 9.8), (0.85, 9.8))
                Line((0.85, 9.8), (0.85, 9.45))
            make_face()
            # Profile area: 0.6825, perimeter: 4.6
            with BuildLine():
                Line((1.2, 7.5), (0.85, 7.5))
                Line((1.2, 9.45), (1.2, 7.5))
                Line((0.85, 9.45), (1.2, 9.45))
                Line((0.85, 9.45), (0.85, 7.5))
            make_face()
            # Profile area: 0.1225, perimeter: 1.4
            with BuildLine():
                Line((1.2, 7.15), (0.85, 7.15))
                Line((1.2, 7.5), (1.2, 7.15))
                Line((1.2, 7.5), (0.85, 7.5))
                Line((0.85, 7.5), (0.85, 7.15))
            make_face()
            # Profile area: 0.6825, perimeter: 4.6
            with BuildLine():
                Line((1.2, 7.15), (1.2, 5.2))
                Line((1.2, 7.15), (0.85, 7.15))
                Line((0.85, 7.15), (0.85, 5.2))
                Line((1.2, 5.2), (0.85, 5.2))
            make_face()
            # Profile area: 9.36, perimeter: 13.5
            with BuildLine():
                Line((6, 7.15), (1.2, 7.15))
                Line((1.2, 7.15), (1.2, 5.2))
                Line((6, 5.2), (1.2, 5.2))
                Line((6, 7.15), (6, 5.2))
            make_face()
            # Profile area: 1.68, perimeter: 10.3
            with BuildLine():
                Line((6, 7.5), (1.2, 7.5))
                Line((1.2, 7.5), (1.2, 7.15))
                Line((6, 7.15), (1.2, 7.15))
                Line((6, 7.5), (6, 7.15))
            make_face()
            # Profile area: 9.36, perimeter: 13.5
            with BuildLine():
                Line((1.2, 9.45), (6, 9.45))
                Line((1.2, 9.45), (1.2, 7.5))
                Line((6, 7.5), (1.2, 7.5))
                Line((6, 9.45), (6, 7.5))
            make_face()
            # Profile area: 1.68, perimeter: 10.3
            with BuildLine():
                Line((6, 9.8), (1.2, 9.8))
                Line((1.2, 9.8), (1.2, 9.45))
                Line((1.2, 9.45), (6, 9.45))
                Line((6, 9.8), (6, 9.45))
            make_face()
        # OneSide extrude, distance=0.35
        extrude(amount=0.35)
    return part.part


# Description: This is a U-shaped bracket or clamp with a hollow rectangular opening in the center, featuring curved outer edges, reinforced flanges on the sides, and mounting holes for fastening applications.
def model_120700_d818883a_0007():
    """Model: Ручки_Эскиз"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 41 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 7), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.3889048562, perimeter: 7.3561945591
            with BuildLine():
                Line((-5.6500000894, 0.2500000149), (-5.6000000834, 0.2500000149))
                CenterArc((-5.2500000834, 0.2500000149), 0.35, 90, 90)
                Line((-4.5500000566, 0.6000000417), (-5.2500000834, 0.6000000149))
                CenterArc((-4.5500000566, 0.2500000149), 0.3500000268, 0, 90)
                Line((-4.2000000298, 0.2500000149), (-4.1500000566, 0.2500000149))
                Line((-4.1500000566, 0.2500000149), (-4.1500000566, -0.0999999851))
                Line((-3.8000000566, -0.0999999851), (-4.1500000566, -0.0999999851))
                Line((-3.8000000566, 0.6000000149), (-3.8000000566, -0.0999999851))
                CenterArc((-4.2000000566, 0.6000000149), 0.4, 0, 90)
                Line((-5.6000000894, 1.0000000149), (-4.2000000566, 1.0000000149))
                CenterArc((-5.6000000834, 0.6000000149), 0.4, 90.0000008538, 89.9999991462)
                Line((-6.0000000834, -0.0999999851), (-6.0000000834, 0.6000000149))
                Line((-5.6500000894, -0.0999999851), (-6.0000000834, -0.0999999851))
                Line((-5.6500000894, 0.2500000149), (-5.6500000894, -0.0999999851))
            make_face()
        # OneSide extrude, distance=0.35
        extrude(amount=0.35)
    return part.part


# Description: This is a tapered cone or pointed wedge with a grooved or fluted surface pattern running along its length, featuring a broad flat top and sharp pointed bottom.
def model_120800_6ee246cf_0001():
    """Model: Mid Tri Base"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 703.0354489211, perimeter: 237.1758232816
            with BuildLine():
                Line((32.0538487874, -110.8975554293), (101.5658987153, -21.9261887876))
                CenterArc((64.9969851475, -64.9954882998), 56.5, -125.6663633249, 0.3746363238)
                Line((109.9461800585, -30.7636335902), (32.3546878385, -111.1119758762))
                CenterArc((64.9969851475, -64.9954882998), 56.5, 37.2917270011, 12.3746363238)
            make_face()
            # Profile area: 0.6449323923, perimeter: 7.3955506271
            with BuildLine():
                CenterArc((64.9969851475, -64.9954882998), 56.5, -125.6663633249, 0.3746363238)
                Line((29.9019500647, -113.6518601928), (32.0538487874, -110.8975554293))
                Line((32.3546878385, -111.1119758762), (29.9019500647, -113.6518601928))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


# Description: This is a dark blue/black composite or plastic boat-shaped housing with an elongated, streamlined hull form, featuring a central longitudinal slot and curved side flanges.
def model_120806_77995027_0001():
    """Model: Component1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.9755036715, perimeter: 7.3778312737
            with BuildLine():
                CenterArc((14.1630136663, 0), 1.65, 8.0219633133, 53.260651549)
                CenterArc((16.5630136663, 0), 0.8, 0, 163.2720680856)
                Line((17.3630136663, 0), (17.5030136663, 0))
                Line((17.5030136663, 0), (17.5030136663, 0.795))
                Line((17.5030136663, 0.795), (14.9558215491, 1.4470506767))
            make_face()
            # Profile area: 0.9755036715, perimeter: 7.3778312737
            with BuildLine():
                Line((17.3630136663, 0), (17.5030136663, 0))
                CenterArc((16.5630136663, 0), 0.8, -163.2720680856, 163.2720680856)
                CenterArc((14.1630136663, 0), 1.65, -61.2826148623, 53.260651549)
                Line((17.5030136663, -0.795), (14.9558215491, -1.4470506767))
                Line((17.5030136663, 0), (17.5030136663, -0.795))
            make_face()
            # Profile area: 8.4811663583, perimeter: 10.3550972186
            with BuildLine():
                CenterArc((14.1630136663, 0), 1.65, 90, 180)
                Line((14.9558215491, -1.4470506767), (14.1630136663, -1.65))
                CenterArc((14.1630136663, 0), 1.65, -61.2826148623, 53.260651549)
                CenterArc((16.5630136663, 0), 0.8, -180, 16.7279319144)
                CenterArc((16.5630136663, 0), 0.8, 163.2720680856, 16.7279319144)
                CenterArc((14.1630136663, 0), 1.65, 8.0219633133, 53.260651549)
                Line((14.9558215491, 1.4470506767), (14.1630136663, 1.65))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: This is a cylindrical rod or shaft with a simple, uniform circular cross-section and a straight, tapered or pointed end, commonly used as a fastener, pin, or structural component in mechanical assemblies.
def model_120806_77995027_0002():
    """Model: Component3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7137698509, perimeter: 8.9221231362
            with BuildLine():
                CenterArc((14.5773713986, 0), 0.79, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((14.5773713986, 0), 0.63, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=50
        extrude(amount=50)
    return part.part


# Description: This is a cylindrical extruded plastic or metal component with a long, slender rectangular profile featuring two parallel slots or channels running along its length and a mounting flange or connector at the top.
def model_121184_3075d4dc_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.0228549059, perimeter: 7.2089519276
            with BuildLine():
                Line((0.9525, 1.27), (0.9525, 0.7112))
                Line((0.9525, 0.7112), (0.6350000203, 0.7112))
                Line((0.6350000203, 0.7112), (0.635, 1.27))
                CenterArc((0.635, 0.635), 0.635, 90, 90)
                Line((0, 0.635), (0.5588, 0.635))
                Line((0.5588, 0.635), (0.5588, 0.3175))
                Line((0, 0.3175), (0.5588, 0.3175))
                Line((0, 0.3175), (0, 0.15875))
                Line((0, 0.15875), (0, 0))
                Line((0, 0), (0.5588772204, 0))
                CenterArc((0.4825154743, 0.7874762835), 0.7911700281, -84.4613329496, 78.9288840136)
                Line((1.27, 1.27), (1.2700000405, 0.7112))
                Line((1.27, 1.27), (0.9525, 1.27))
            make_face()
            with BuildLine():
                CenterArc((0.8350443152, 0.434975), 0.079375, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=6.35
        extrude(amount=6.35)
    return part.part


# Description: This is a rectangular sheet metal box or duct component with a parallelogram-like 3D shape, featuring open ends, flat side panels, and angled edges that suggest it's designed for airflow or structural containment purposes.
def model_121467_899f0850_0002():
    """Model: base"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 46.4292036732, perimeter: 38.2831853072
            with BuildLine():
                Line((6, -2), (6, 2))
                Line((6, 2), (-6, 2))
                Line((-6, 2), (-6, -2))
                Line((-6, -2), (6, -2))
            make_face()
            with BuildLine():
                CenterArc((-4, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=1.5
        extrude(amount=0.75, both=True)
    return part.part


# Description: This is a blue plastic or composite bracket assembly featuring two perpendicular box-shaped arms connected by a flat base plate, with the right arm containing ventilation slots or mesh panels and both arms designed for mounting or attachment purposes.
def model_121469_bb776055_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 15 constraints, 15 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 55.7987967673, perimeter: 56.131884742
            with BuildLine():
                Line((-18.9393398282, 5), (-20, 3.9393398282))
                Line((-20, 3.9393398282), (-16.6464466094, 0.5857864376))
                CenterArc((-15.232233047, 2), 2, -135, 45)
                Line((-15.232233047, 0), (0, 0))
                Line((0, 0), (0, 1.5))
                Line((-4.5, 1.5), (0, 1.5))
                Line((-4.5, 6), (-4.5, 1.5))
                CenterArc((-6.5, 6), 2, 0, 180)
                Line((-8.5, 1.5), (-8.5, 6))
                Line((-14.6109127035, 1.5), (-8.5, 1.5))
                CenterArc((-14.6109127035, 3.5), 2, -135, 45)
                Line((-18.9393398282, 5), (-16.0251262658, 2.0857864376))
            make_face()
        # Symmetric extrude, each_side=2
        extrude(amount=2, both=True)
    return part.part


# Description: This is a cylindrical container or sleeve with an open top, featuring a curved/tapered upper rim and a flat or recessed bottom, with a smooth lateral surface and mesh-textured end caps.
def model_121620_4a6e845d_0001():
    """Model: Head"""
    with BuildPart() as part:
        # Head -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2642079422, perimeter: 1.8221237391
            Circle(0.29)
        # OneSide extrude, distance=-0.37
        extrude(amount=-0.37)
    return part.part


# Description: This is an elongated rectangular prism or flat bar with a tapered wedge shape, featuring a sloped top surface and a dark edge bevel, commonly used as a structural support, spacer, or shim component.
def model_121703_69c4a5ac_0000():
    """Model: table"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 225, perimeter: 100
            with BuildLine():
                Line((20, -7), (20, -2))
                Line((20, -2), (-25, -2))
                Line((-25, -2), (-25, -7))
                Line((-25, -7), (20, -7))
            make_face()
        # Symmetric extrude, each_side=50
        extrude(amount=50, both=True)
    return part.part


# Description: This is a parallelogram-shaped flat plate or panel with a uniform thickness and slight beveled edges at the top, featuring a simple geometric form without holes or complex features.
def model_121869_67b34d49_0002():
    """Model: Battery v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 9.36, perimeter: 12.4
            with BuildLine():
                Line((1.3, -1.8), (-1.3, -1.8))
                Line((1.3, 1.8), (1.3, -1.8))
                Line((-1.3, 1.8), (1.3, 1.8))
                Line((-1.3, -1.8), (-1.3, 1.8))
            make_face()
        # OneSide extrude, distance=0.575
        extrude(amount=0.575)
    return part.part


# Description: This is a curved duct or airflow channel component with an overall L-shaped or serpentine form, featuring internal ribbing for structural reinforcement, a rectangular inlet opening on the left, and a curved elbow section on the right that transitions the flow direction.
def model_122100_a32b6fdf_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 26 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 22.098401951, perimeter: 47.5717983916
            with BuildLine():
                Line((3.5148396995, -1.846307153), (2.2122515541, -1.846307153))
                CenterArc((1.5315280664, -0.1226184184), 2.6276658631, -40.9937833838, 129.0125792768)
                Line((-0.3929247367, 0.6141371217), (1.6223707964, 2.5034766839))
                Line((-1.8981377048, 0.6141371217), (-0.3929247367, 0.6141371217))
                Line((-1.8981377048, 1.3956900089), (-1.8981377048, 0.6141371217))
                Line((-0.1324071077, 1.3956900089), (-1.8981377048, 1.3956900089))
                Line((0.9386098119, 2.4956533317), (-0.1324071077, 1.3956900089))
                Line((-3.4901898825, 2.4956533317), (0.9386098119, 2.4956533317))
                Line((-3.4901898825, 1.3956900089), (-3.4901898825, 2.4956533317))
                Line((-3.2007258502, 1.3956900089), (-3.4901898825, 1.3956900089))
                Line((-3.2007258502, -1.4121111045), (-3.2007258502, 1.3956900089))
                Line((-3.4901898825, -1.4121111045), (-3.2007258502, -1.4121111045))
                Line((-3.4901898825, -2.5410208306), (-3.4901898825, -1.4121111045))
                Line((-1.5218344628, -2.5410208306), (-3.4901898825, -2.5410208306))
                Line((-1.5218344628, -1.4121111045), (-1.5218344628, -2.5410208306))
                Line((-1.7823520919, -1.4121111045), (-1.5218344628, -1.4121111045))
                Line((-1.7823520919, -0.6305582173), (-1.7823520919, -1.4121111045))
                Line((-1.2613168337, -0.6305582173), (-1.7823520919, -0.6305582173))
                CenterArc((0.9548552423, -0.4221244226), 2.2259522271, -174.6270644197, 66.7851686484)
                Line((0.2728425376, -1.846307153), (0.2728425376, -2.5410208306))
                Line((2.2990907638, -0.0516301526), (0.2728425376, -1.846307153))
                Line((2.2990907638, 0.3101998877), (2.2990907638, -0.0516301526))
                CenterArc((1.9372607234, 0.3101998877), 0.3618300404, 0, 180)
                Line((1.575430683, -0.1674157656), (1.575430683, 0.3101998877))
                Line((0.2265282924, -0.1674157656), (1.575430683, -0.1674157656))
                Line((0.2265282924, 0.7878155411), (0.2265282924, -0.1674157656))
                Line((0.9675562151, 1.4825292186), (0.2265282924, 0.7878155411))
                Line((2.8635456268, 1.4825292186), (0.9675562151, 1.4825292186))
                Line((3.5148396995, 0.7878155411), (2.8635456268, 1.4825292186))
                Line((3.5148396995, -0.4858262011), (3.5148396995, 0.7878155411))
                Line((2.2122515541, -1.846307153), (3.5148396995, -0.4858262011))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a trapezoidal or wedge-shaped plate with a slanted top face and a reinforcing vertical flange or lip along one edge, featuring a hollow or open interior structure.
def model_122105_21cb0a9e_0000():
    """Model: Corredera Guia v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.258, perimeter: 9.5
            with BuildLine():
                Line((3.15, 1.05), (0.55, 1.05))
                Line((0.55, 1.05), (0.55, 0.48))
                Line((0.55, 0.48), (0, 0.48))
                Line((0, 0.48), (0, 0))
                Line((0, 0), (3.7, 0))
                Line((3.7, 0), (3.7, 0.48))
                Line((3.15, 0.48), (3.7, 0.48))
                Line((3.15, 1.05), (3.15, 0.48))
            make_face()
        # OneSide extrude, distance=4
        extrude(amount=4)
    return part.part


# Description: This is a linear shaft or rail with a hexagonal or multi-faceted cross-section, featuring a tapered or chamfered end on one side and a flat end on the other, designed for use in mechanical assemblies or machinery.
def model_122105_21cb0a9e_0004():
    """Model: Listones Guia v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.43, perimeter: 5.4
            with BuildLine():
                Line((1, 1.1), (0, 1.1))
                Line((0, 1.1), (0, 0))
                Line((0, 0), (1.6, 0))
                Line((1.6, 0), (1.6, 0.55))
                Line((1, 0.55), (1.6, 0.55))
                Line((1, 1.1), (1, 0.55))
            make_face()
        # OneSide extrude, distance=10
        extrude(amount=10)
    return part.part


# Description: This is an elliptical dish or shallow pan with a flat base, gently curved sides, a reinforced rim flange, and internal radial ribbing for structural stiffening.
def model_122258_c3076cb0_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 22.901834478, perimeter: 16.964530687
            with BuildLine():
                CenterArc((0, 0), 2.7, 95.1334813432, 355.1167430581)
                Line((-0.2415860853, 2.6891701626), (-0.0117915096, 2.6999742518))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: This is a flat, trapezoidal metal plate or panel with a parallelogram shape, featuring a slightly beveled edge on the left side and a clean, minimalist design with no holes or cutouts.
def model_122260_c9bddd6a_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.0449168805, perimeter: 4.0604792923
            with BuildLine():
                Line((1.23, 0.2989001251), (0.9791930153, 0))
                Line((1.23, 0.88), (1.23, 0.2989001251))
                Line((0, 0.88), (1.23, 0.88))
                Line((0, 0), (0, 0.88))
                Line((0.9791930153, 0), (0, 0))
            make_face()
        # OneSide extrude, distance=0.062
        extrude(amount=0.062)
    return part.part


# Description: This is a hexagonal or polygonal prism-shaped structural component with flat faces and angular edges, appearing to be a solid geometric form without notable holes, slots, or protrusions.
def model_122328_4d8636de_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 145.1609956398, perimeter: 48.2599992752
            with BuildLine():
                Line((19.0499997139, 3.8099999428), (6.3499999046, 3.8099999428))
                Line((19.0499997139, 15.2399997711), (19.0499997139, 3.8099999428))
                Line((6.3499999046, 15.2399997711), (19.0499997139, 15.2399997711))
                Line((6.3499999046, 3.8099999428), (6.3499999046, 15.2399997711))
            make_face()
        # OneSide extrude, distance=5.08
        extrude(amount=5.08)
    return part.part


# Description: This is a shoe last or foot form with an elongated, rounded capsule shape featuring a mesh-textured curved surface on one side and a solid smooth surface on the other, used as a mold for shoe manufacturing or fitting.
def model_122423_9ab69fbb_0001():
    """Model: PT4 Cam"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.8660780083, perimeter: 7.1887920006
            with BuildLine():
                CenterArc((0, -1), 0.6, -156.4218215218, 132.8436430436)
                Line((0.5499090834, -1.24), (0.916515139, -0.4))
                CenterArc((0, 0), 1, -23.5781784782, 227.1563569564)
                Line((-0.5499090834, -1.24), (-0.916515139, -0.4))
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)
    return part.part


# Description: This is a cable management clip or duct connector with an elongated oval base, featuring a cylindrical barrel on one end and a slot or channel running along its length for routing and securing cables or tubing.
def model_122423_9ab69fbb_0002():
    """Model: PT5 Handle"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 14 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.1726548246, perimeter: 8.1132741229
            with BuildLine():
                CenterArc((0, 0), 0.4, -90, 180)
                Line((0, 0.4), (-2.2, 0.4))
                CenterArc((-2.2, 0), 0.4, 90, 180)
                Line((-2.2, -0.4), (0, -0.4))
            make_face()
            with BuildLine():
                Line((-2.05, 0.15), (-2.05, -0.15))
                Line((-2.05, -0.15), (-2.35, -0.15))
                Line((-2.35, -0.15), (-2.35, 0.15))
                Line((-2.35, 0.15), (-2.05, 0.15))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5)
    return part.part


# Description: This is a triangular bracket or mounting plate with rounded corners, featuring three circular mounting holes and a hollow triangular interior cavity.
def model_122424_d612248e_0000():
    """Model: PT1 Side Plate"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 16 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2147.9354217093, perimeter: 246.3242787607
            with BuildLine():
                CenterArc((-20.32, 0), 9.525, 90, 118.4742036101)
                Line((-8.3727784255, -42.0061679596), (-28.6927784255, -4.5411679596))
                CenterArc((0, -37.465), 9.525, -151.5257963899, 123.0515927799)
                Line((8.3727784255, -42.0061679596), (28.6927784255, -4.5411679596))
                CenterArc((20.32, 0), 9.525, -28.4742036101, 118.4742036101)
                Line((-20.32, 9.525), (20.32, 9.525))
            make_face()
            with BuildLine():
                CenterArc((-20.32, 0), 3.2146875, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, -37.465), 3.2146875, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((20.32, 0), 3.2146875, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3.175
        extrude(amount=3.175)
    return part.part


# Description: This is a toroidal (donut-shaped) component with a large central hole, featuring a smooth, rounded profile and a wireframe mesh surface finish.
def model_122425_248c57e8_0001():
    """Model: PT4 Collar"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 10.2965699221, perimeter: 21.6769893098
            with BuildLine():
                CenterArc((0, 0), 2.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.6
        extrude(amount=1.6)
    return part.part


# Description: This is a hexagonal prism or elongated hexagonal block with a beveled or chamfered top surface, featuring angled facets across its upper edges and a hollow or recessed interior section.
def model_122491_52380ecd_0000():
    """Model: part3 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.7442932324, perimeter: 7.9923909766
            with BuildLine():
                Line((1.5, -2.4961954883), (0, -2.4961954883))
                Line((1.5, 0), (1.5, -2.4961954883))
                Line((0, 0), (1.5, 0))
                Line((0, -2.4961954883), (0, 0))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a hexagonal prism or wedge-shaped connector block with a tapered profile, featuring angled end faces and a hollow or recessed central cavity running along its length.
def model_122491_52380ecd_0001():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.0000000075, perimeter: 10.0000000149
            with BuildLine():
                Line((4.0000000075, -1), (0, -1))
                Line((4.0000000075, 0), (4.0000000075, -1))
                Line((0, 0), (4.0000000075, 0))
                Line((0, -1), (0, 0))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is an elongated hexagonal prism or wedge-shaped structural component with a tapered profile, featuring a beveled or angled end on the left side and a flat rectangular body extending to the right.
def model_122491_52380ecd_0002():
    """Model: part2 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5, perimeter: 12
            with BuildLine():
                Line((5, -1), (0, -1))
                Line((5, 0), (5, -1))
                Line((0, 0), (5, 0))
                Line((0, -1), (0, 0))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a triangular prism or wedge-shaped bracket with a tapered profile, featuring a narrow top edge and a wider base, with a dark blue finish and what appears to be a mounting flange or support surface along one edge.
def model_122515_758d8b70_0002():
    """Model: SUPPORTING RIB (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 103.125, perimeter: 44.5773797371
            with BuildLine():
                Line((10, 2.5), (10, 0))
                Line((2.5, 15), (10, 2.5))
                Line((0, 15), (2.5, 15))
                Line((0, 0), (0, 15))
                Line((10, 0), (0, 0))
            make_face()
        # Symmetric extrude, full_length=True, total=1
        extrude(amount=0.5, both=True)
    return part.part


# Description: This is a flat parallelogram or wedge-shaped plate with a trapezoidal profile, featuring a sloped top surface and a thin, beveled edge on one side, commonly used as a shim, spacer, or structural component.
def model_122515_758d8b70_0004():
    """Model: COLUMN BASE PLATE"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3.75, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 760, perimeter: 380
            with BuildLine():
                Line((-20, 24.25), (-20, 28.25))
                Line((20, 24.25), (-20, 24.25))
                Line((20, 28.25), (20, 24.25))
                Line((20, 83.25), (20, 28.25))
                Line((20, 87.25), (20, 83.25))
                Line((-20, 87.25), (20, 87.25))
                Line((-20, 83.25), (-20, 87.25))
                Line((-20, 28.25), (-20, 83.25))
            make_face()
            with BuildLine():
                Line((16, 28.25), (-16, 28.25))
                Line((-16, 28.25), (-16, 83.25))
                Line((-16, 83.25), (16, 83.25))
                Line((16, 83.25), (16, 28.25))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1760, perimeter: 174
            with BuildLine():
                Line((16, 83.25), (16, 28.25))
                Line((-16, 83.25), (16, 83.25))
                Line((-16, 28.25), (-16, 83.25))
                Line((16, 28.25), (-16, 28.25))
            make_face()
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)
    return part.part


# Description: This is a cylindrical heat exchanger vessel with a tubular core, featuring rounded end caps, internal tube bundles visible through the semi-transparent shell, and inlet/outlet ports along the length for fluid circulation.
def model_122515_758d8b70_0009():
    """Model: Pin-1_Working Arm v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4.9087385212, perimeter: 7.853981634
            Circle(1.25)
        # Symmetric extrude, full_length=True, total=9
        extrude(amount=4.5, both=True)
    return part.part


# Description: A cylindrical hollow tube or pipe with rounded ends (capsule shape) featuring a central longitudinal slot or groove running along its length and circular openings at both ends.
def model_122515_758d8b70_0011():
    """Model: Bush_Working Arm v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.638937829, perimeter: 17.5929188601
            with BuildLine():
                CenterArc((0, 0), 1.55, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=6
        extrude(amount=3, both=True)
    return part.part


# Description: This is a toroidal (donut-shaped) rubber or elastic ring with a smooth inner and outer surface, featuring a mesh or textured pattern on the outer perimeter and a solid cross-section designed for use as a seal, gasket, or compression ring.
def model_122587_febb5971_0000():
    """Model: 13 Washer - Copper"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.0106192983, perimeter: 10.0530964915
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: This is a toroidal (donut-shaped) ring or sleeve with a smooth outer surface and a hollow central opening, featuring a textured or mesh-patterned upper section that contrasts with the solid lower band.
def model_122587_febb5971_0002():
    """Model: 10 Washer - Fiber"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.8246680716, perimeter: 6.5973445725
            with BuildLine():
                CenterArc((0, 0), 0.65, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is a black plastic bracket or clamp with a U-shaped channel design, featuring a curved top mount and two flat flanged feet at the base for fastening.
def model_122750_8f5f5638_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 22 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 55.0723723526, perimeter: 55.4595970928
            with BuildLine():
                CenterArc((0, 6), 2, 0, 180)
                Line((-2, 6), (-2, 2))
                CenterArc((-2.5, 2), 0.5, -90, 90)
                Line((-2.5, 1.5), (-8.4389606877, 1.5))
                CenterArc((-8.4389606877, 2.5), 1, -135, 45)
                Line((-12.2059457643, 4.8527715142), (-9.1460674689, 1.7928932188))
                Line((-12.2059457643, 4.8527715142), (-12.3617117006, 5.0085374505))
                Line((-12.3617117006, 5.0085374505), (-13.3318927229, 4.0383564282))
                Line((-13.3318927229, 4.0383564282), (-10.7935362947, 1.5))
                Line((-10.7935362947, 1.5), (-9.5864295135, 0.2928932188))
                CenterArc((-8.8793227323, 1), 1, -135, 45)
                Line((0, 0), (-8.8793227323, 0))
                Line((6.5, 0), (0, 0))
                Line((6.5, 0), (6.5, 1.5))
                Line((6.5, 1.5), (2.5, 1.5))
                CenterArc((2.5, 2), 0.5, 180, 90)
                Line((2, 6), (2, 2))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a polyhedron or geometric solid with an irregular, faceted form featuring multiple angular faces in varying shades of blue and dark gray, with visible edge lines defining its complex geometric structure.
def model_122895_39b17a39_0000():
    """Model: Part v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 225, perimeter: 60
            with BuildLine():
                Line((7.5, -7.5), (7.5, 7.5))
                Line((7.5, 7.5), (-7.5, 7.5))
                Line((-7.5, 7.5), (-7.5, -7.5))
                Line((-7.5, -7.5), (7.5, -7.5))
            make_face()
        # Symmetric extrude, each_side=7.5
        extrude(amount=7.5, both=True)
    return part.part


# Description: This is a complex geometric bracket or structural component with an organic, asymmetrical shape featuring multiple internal voids, triangulated mesh surfaces, curved edges, and angular faceted elements that suggest a lightweight, optimized design for aerospace or industrial applications.
def model_122904_9ac95090_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 45 constraints, 14 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4.2933934885, perimeter: 10.0643261234
            with BuildLine():
                CenterArc((0, -11), 3, 61.0449756281, 57.9100487437)
                CenterArc((0, -7), 2, -43.4325365578, 43.4325365578)
                Line((2, -7), (-2, -7))
                CenterArc((0, -7), 2, 180, 43.4325365578)
            make_face()
            # Profile area: 113.1358176171, perimeter: 91.996787438
            with BuildLine():
                CenterArc((0, 0), 1.5, -180, 180)
                Line((-1.5, 0), (-11, 0))
                CenterArc((0, 0), 11, -180, 74.3250404738)
                CenterArc((0, -11), 3, 118.9550243719, 53.2074958651)
                CenterArc((0, -7), 2, 180, 43.4325365578)
                Line((-2, -7), (-6.5, -7))
                CenterArc((-6.5, -6.5), 0.5, 180, 90)
                Line((-7, -6.5), (-7, -3.5))
                CenterArc((-6.5, -3.5), 0.5, 90, 90)
                Line((-6.5, -3), (6.5, -3))
                CenterArc((6.5, -3.5), 0.5, 0, 90)
                Line((7, -3.5), (7, -6.5))
                CenterArc((6.5, -6.5), 0.5, -90, 90)
                Line((6.5, -7), (2, -7))
                CenterArc((0, -7), 2, -43.4325365578, 43.4325365578)
                CenterArc((0, -11), 3, 7.8374797631, 53.2074958651)
                CenterArc((0, 0), 11, -74.3250404738, 74.3250404738)
                Line((1.5, 0), (11, 0))
            make_face()
            # Profile area: 27.2328541324, perimeter: 26.2648765125
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 90)
                Line((1.5, 0), (11, 0))
                Line((11, 0), (8, 2))
                Line((8, 2), (4, 3.5))
                Line((4, 3.5), (0, 4))
                Line((0, 4), (0, 1.5))
            make_face()
            # Profile area: 6.2831853072, perimeter: 10.2831853072
            with BuildLine():
                Line((2, -7), (-2, -7))
                CenterArc((0, -7), 2, 0, 180)
            make_face()
            # Profile area: 27.2328541324, perimeter: 26.2648765125
            with BuildLine():
                Line((0, 4), (0, 1.5))
                Line((-4, 3.5), (0, 4))
                Line((-8, 2), (-4, 3.5))
                Line((-11, 0), (-8, 2))
                Line((-1.5, 0), (-11, 0))
                CenterArc((0, 0), 1.5, 90, 90)
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


# Description: This is a bent metal channel or bracket with a U-shaped profile, featuring two vertical flanges at each end and a horizontal base, commonly used as a structural support or mounting component.
def model_123016_29f35476_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 13 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 330.88, perimeter: 416.8
            with BuildLine():
                Line((88.4, -58.4), (1.6, -58.4))
                Line((1.6, 0), (1.6, -58.4))
                Line((0, 0), (1.6, 0))
                Line((0, -58.4), (0, 0))
                Line((0, -58.4), (0, -60))
                Line((0, -60), (1.6, -60))
                Line((1.6, -60), (88.4, -60))
                Line((90, -60), (88.4, -60))
                Line((90, -58.4), (90, -60))
                Line((90, 0), (90, -58.4))
                Line((88.4, 0), (90, 0))
                Line((88.4, -58.4), (88.4, 0))
            make_face()
        # OneSide extrude, distance=10
        extrude(amount=10)
    return part.part


# Description: This is a curved structural component with a toroidal (doughnut-like) overall shape, featuring a hollow center opening, triangulated mesh panel reinforcements on the upper surface, and multiple rectangular slots or cutouts along the sides.
def model_123331_28a27457_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 59 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 178.1529062758, perimeter: 106.8718336459
            with BuildLine():
                CenterArc((3.3402132856, -9.9545454545), 0.5, -162.6203831922, 91.1693828056)
                CenterArc((0, 0), 11, -71.4510003866, 70.0028663949)
                CenterArc((10.496646422, -0.2653561606), 0.5, -1.4481339917, 57.7580664657)
                Line((10.7739965201, 0.1506689866), (8.047893029, 1.968071314))
                CenterArc((7.7705429309, 1.5520461668), 0.5, 56.309932474, 13.1340223064)
                Line((7.9461046517, 2.0202107556), (4.0266654738, 3.4900004473))
                CenterArc((3.851103753, 3.0218358586), 0.5, 69.4439547804, 13.4782591484)
                Line((3.9127121201, 3.5180257507), (0.0616083671, 3.9961898922))
                CenterArc((0, 3.5), 0.5, 82.9222139288, 14.1555721423)
                Line((-3.9127121201, 3.5180257507), (-0.0616083671, 3.9961898922))
                CenterArc((-3.851103753, 3.0218358586), 0.5, 97.0777860712, 13.4782591484)
                Line((-7.9461046517, 2.0202107556), (-4.0266654738, 3.4900004473))
                CenterArc((-7.7705429309, 1.5520461668), 0.5, 110.5560452196, 13.1340223064)
                Line((-10.7739965201, 0.1506689866), (-8.047893029, 1.968071314))
                CenterArc((-10.496646422, -0.2653561606), 0.5, 123.690067526, 57.7580664657)
                CenterArc((0, 0), 11, -178.5518660083, 70.0028663949)
                CenterArc((-3.3402132856, -9.9545454545), 0.5, -108.5489996134, 91.1693828056)
                CenterArc((0, -11), 3, 17.3796168078, 145.2407663844)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, -7), 2, 11.5369590328, 156.9260819344)
                CenterArc((-2.4494897428, -6.5), 0.5, -90, 78.4630409672)
                Line((-6.5, -7), (-2.4494897428, -7))
                CenterArc((-6.5, -6.5), 0.5, 180, 90)
                Line((-7, -3.5), (-7, -6.5))
                CenterArc((-6.5, -3.5), 0.5, 90, 90)
                Line((6.5, -3), (-6.5, -3))
                CenterArc((6.5, -3.5), 0.5, 0, 90)
                Line((7, -6.5), (7, -3.5))
                CenterArc((6.5, -6.5), 0.5, -90, 90)
                Line((2.4494897428, -7), (6.5, -7))
                CenterArc((2.4494897428, -6.5), 0.5, -168.4630409672, 78.4630409672)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=4
        extrude(amount=4)
    return part.part


# Description: This is a dark blue plastic or composite bracket or mounting clip with an angular, geometric shape featuring two upright flanges and a curved central support structure, designed to hold or clamp components together.
def model_123332_eb7b0c9a_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 14 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 55.9060976856, perimeter: 55.8747969141
            with BuildLine():
                CenterArc((13.5, 6), 2, 0, 180)
                Line((11.5, 6), (11.5, 2))
                CenterArc((11, 2), 0.5, -90, 90)
                Line((11, 1.5), (4.5606601718, 1.5))
                Line((4.5606601718, 1.5), (1.0606601718, 5))
                Line((1.0606601718, 5), (0, 3.9393398282))
                Line((0, 3.9393398282), (3.9393398282, 0))
                Line((3.9393398282, 0), (20, 0))
                Line((20, 0), (20, 1.5))
                Line((20, 1.5), (16, 1.5))
                CenterArc((16, 2), 0.5, 180, 90)
                Line((15.5, 6), (15.5, 2))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


# Description: This is a complex polyhedron or faceted geometric solid with an irregular, box-like shape featuring multiple triangular and quadrilateral faces, rendered in shades of blue and dark gray, with no apparent holes, slots, or flanges.
def model_123495_0999be98_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 20, perimeter: 18
            with BuildLine():
                Line((5, -4), (0, -4))
                Line((5, 0), (5, -4))
                Line((0, 0), (5, 0))
                Line((0, -4), (0, 0))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a metal bracket or corner brace with an L-shaped profile featuring mounting holes and angular cutouts along its surfaces for weight reduction and structural optimization.
def model_123496_74cb10dc_0015():
    """Model: ???? v2 (3)"""
    with BuildPart() as part:
        # Sketch1 -> 押し出し1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.8752501107, perimeter: 13.6774910385
            with BuildLine():
                Line((-3.0045762864, 2.2320508076), (-3.8706016902, 2.7320508076))
                Line((-3.8706016902, 2.7320508076), (-5.0045762864, 0.7679491924))
                Line((-5.0045762864, 0.7679491924), (-5.0045762864, -1.5))
                Line((-5.0045762864, -1.5), (-4.0045762864, -1.5))
                Line((-4.0045762864, -1.5), (-4.0045762864, 0.5))
                Line((-4.0045762864, 0.5), (-3.0045762864, 2.2320508076))
            make_face()
            with BuildLine():
                CenterArc((-3.7000000551, 2.0000000298), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-4.5045762864, -1), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a hexagonal or elongated polyhedron with a complex geometric form, featuring multiple faceted surfaces in varying shades, a concave indentation on the left side, and an overall prismatic shape with angular edges and planar faces.
def model_123754_6d71ab4f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 42.9966565729, perimeter: 27.2941968123
            with BuildLine():
                Line((3.7114494, -2.9356490061), (-5, -2.9356490061))
                Line((3.7114494, 2), (3.7114494, -2.9356490061))
                Line((-5, 2), (3.7114494, 2))
                Line((-5, -2.9356490061), (-5, 2))
            make_face()
        # OneSide extrude, distance=4
        extrude(amount=4)
    return part.part


# Description: This is a dark blue hexagonal or polygonal housing/enclosure with a wireframe mesh panel on one side and a rectangular slot or window opening on the front face.
def model_123770_de9989d1_0000():
    """Model: BODY (6)"""
    with BuildPart() as part:
        # Sketch1 -> 押し出し1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 16 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.059275, perimeter: 1.268
            with BuildLine():
                Line((0.127, -0.125), (-0.127, -0.125))
                Line((0.127, 0.125), (0.127, -0.125))
                Line((-0.127, 0.125), (0.127, 0.125))
                Line((-0.127, -0.125), (-0.127, 0.125))
            make_face()
            with BuildLine():
                Line((-0.0325, -0.0325), (-0.0325, 0.0325))
                Line((-0.0325, 0.0325), (0.0325, 0.0325))
                Line((0.0325, 0.0325), (0.0325, -0.0325))
                Line((0.0325, -0.0325), (-0.0325, -0.0325))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.25
        extrude(amount=0.25)
    return part.part


# Description: This is a rectangular steel bar or rod with a hexagonal cross-section, featuring a tapered or beveled end on one side.
def model_123770_de9989d1_0001():
    """Model: PIN (2)"""
    with BuildPart() as part:
        # Sketch1 -> 押し出し1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY) as sk:
            # Profile area: 0.004096, perimeter: 0.256
            with BuildLine():
                Line((0.032, -0.032), (-0.032, -0.032))
                Line((0.032, 0.032), (0.032, -0.032))
                Line((-0.032, 0.032), (0.032, 0.032))
                Line((-0.032, -0.032), (-0.032, 0.032))
            make_face()
        # TwoSides extrude, along=0.86, against=-0.3
        extrude(amount=0.86)
        extrude(sk.sketch, amount=-0.3)
    return part.part


# Description: This is a long, narrow tapered wedge or shim with a flat top surface and angled sides that gradually narrow toward the right end, featuring a subtle curved profile along its length.
def model_123865_f6dff61e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 31 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.8228318531, perimeter: 34.8283185307
            with BuildLine():
                Line((1.25, -15.4), (1.25, -15))
                Line((1.25, -15), (0.4, -15))
                Line((0.4, -15), (0.4, -0.4))
                Line((0.4, -0.4), (1.25, -0.4))
                Line((1.25, 0), (1.25, -0.4))
                Line((0.2, 0), (1.25, 0))
                CenterArc((0.2, -0.2), 0.2, 90, 90)
                Line((0, -15.2), (0, -0.2))
                CenterArc((0.2, -15.2), 0.2, 180, 90)
                Line((1.25, -15.4), (0.2, -15.4))
            make_face()
            # Profile area: 6.8228318531, perimeter: 34.8283185307
            with BuildLine():
                CenterArc((2.3, -15.2), 0.2, -90, 90)
                Line((2.5, -0.2), (2.5, -15.2))
                CenterArc((2.3, -0.2), 0.2, 0, 90)
                Line((1.25, 0), (2.3, 0))
                Line((1.25, 0), (1.25, -0.4))
                Line((1.25, -0.4), (2.1, -0.4))
                Line((2.1, -0.4), (2.1, -15))
                Line((2.1, -15), (1.25, -15))
                Line((1.25, -15.4), (1.25, -15))
                Line((2.3, -15.4), (1.25, -15.4))
            make_face()
            # Profile area: 24.22, perimeter: 39
            with BuildLine():
                Line((0.4, -0.4), (1.25, -0.4))
                Line((0.4, -15), (0.4, -0.4))
                Line((1.25, -15), (0.4, -15))
                Line((2.1, -15), (1.25, -15))
                Line((2.1, -0.4), (2.1, -15))
                Line((1.25, -0.4), (2.1, -0.4))
            make_face()
            with BuildLine():
                Line((1.35, -6.2), (1.35, -9.2))
                Line((1.35, -9.2), (1.15, -9.2))
                Line((1.15, -9.2), (1.15, -6.2))
                Line((1.15, -6.2), (1.35, -6.2))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.6, perimeter: 6.4
            with BuildLine():
                Line((1.15, -6.2), (1.35, -6.2))
                Line((1.15, -9.2), (1.15, -6.2))
                Line((1.35, -9.2), (1.15, -9.2))
                Line((1.35, -6.2), (1.35, -9.2))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is a parallelepiped or skewed rectangular box with a trapezoidal profile, featuring flat faces and sharp edges, appearing to be a structural bracket or support component with an angular, asymmetrical geometry.
def model_123944_ccfed065_0001():
    """Model: seissseitenstück v1 (3)"""
    with BuildPart() as part:
        # Sketch1 -> Extrusion1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4, perimeter: 8
            with BuildLine():
                Line((0, 2), (0, 0))
                Line((0, 0), (2, 0))
                Line((2, 0), (2, 2))
                Line((2, 2), (0, 2))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a curved, dome-like enclosure or housing with an organic, kidney-bean shape featuring a hollow interior cavity, mesh/lattice structural elements on the upper surface, and flanged or ribbed sections on the sides for structural reinforcement and assembly.
def model_124415_4db8a722_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 19 constraints, 15 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 184.9098302902, perimeter: 98.7317586363
            with BuildLine():
                CenterArc((0, 0), 11, 180, 71.4510003866)
                CenterArc((-3.3402132856, -9.9545454545), 0.5, -108.5489996134, 91.1693828056)
                CenterArc((0, -11), 3, 17.3796168078, 145.2407663844)
                CenterArc((3.3402132856, -9.9545454545), 0.5, -162.6203831922, 91.1693828056)
                CenterArc((0, 0), 11, -71.4510003866, 71.4510003866)
                Line((11, 0), (8, 2))
                Line((8, 2), (4, 3.5))
                Line((4, 3.5), (0, 4))
                Line((-4, 3.5), (0, 4))
                Line((-8, 2), (-4, 3.5))
                Line((-11, 0), (-8, 2))
            make_face()
            with BuildLine():
                CenterArc((0, -7), 2, 0, 180)
                Line((-2, -7), (-7, -7))
                Line((-7, -7), (-7, -3))
                Line((-7, -3), (7, -3))
                Line((7, -3), (7, -7))
                Line((2, -7), (7, -7))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=7
        extrude(amount=7)
    return part.part


# Description: This is a flat, annular (ring-shaped) washer with a large central hole and a circular outer diameter, featuring a beveled or chamfered edge around the inner and outer perimeters.
def model_124497_5c00f42d_0003():
    """Model: Washer v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 5.5421130526, perimeter: 13.9643793452
            with BuildLine():
                CenterArc((0, 0), 1.508125, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.714375, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.15875
        extrude(amount=0.15875)
    return part.part


# Description: This is a thick annular (ring-shaped) washer or thrust bearing component with a large central hole, featuring a textured or knurled outer edge and a tapered or beveled inner bore.
def model_124497_5c00f42d_0011():
    """Model: Washer Hinge v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 6.6454635213, perimeter: 13.9723589905
            with BuildLine():
                CenterArc((0, 0), 1.5875, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.63627, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.47625
        extrude(amount=0.47625)
    return part.part


# Description: This is a hexagonal or polygonal shaped connector block with a faceted geometric design, featuring multiple planar surfaces and angular faces that suggest it may serve as a junction point, mounting bracket, or structural link component with chamfered or beveled edges throughout.
def model_124804_18e77ffd_0001():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 67.5, perimeter: 33
            with BuildLine():
                Line((-5, -4.5), (-5, 3))
                Line((4, -4.5), (-5, -4.5))
                Line((4, 3), (4, -4.5))
                Line((-4.5, 3), (4, 3))
                Line((-5, 3), (-4.5, 3))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


# Description: This is a pair of cylindrical rubber or elastomer bushings with slightly rounded ends and visible surface texture, commonly used as vibration dampeners or mechanical isolators.
def model_125153_a3c60b19_0001():
    """Model: Component2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 11.6), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 11.1447997517, perimeter: 13.5088483612
            with BuildLine():
                CenterArc((8.3500172946, 20.0044802978), 1.9, 0.244464566, 359.511070868)
                Line((10.25, 20.0125870252), (10.25, 19.9963735704))
            make_face()
            with BuildLine():
                CenterArc((8.3500172946, 20.0044802978), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 11.1447997517, perimeter: 13.5088483612
            with BuildLine():
                Line((11.75, 19.9963735704), (11.75, 20.0125870252))
                CenterArc((13.6499827054, 20.0044802978), 1.9, -179.755535434, 359.511070868)
            make_face()
            with BuildLine():
                CenterArc((13.6499827054, 20.0044802978), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-1.2
        extrude(amount=-1.2)
    return part.part


# Description: This is a modular robotic arm or mechanical linkage assembly consisting of four dark gray articulated segments connected in series, with the leftmost segment featuring a blue rectangular mounting pad or interface plate.
def model_125416_ab456bc3_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 472 constraints, 16 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 63.2499999776, perimeter: 82.0000000596
            with BuildLine():
                Line((26.5, -15.5), (18, -15.5))
                Line((26.5, -7), (26.5, -15.5))
                Line((18, -7), (26.5, -7))
                Line((18, -15.5), (18, -7))
            make_face()
            with BuildLine():
                Line((20, -8), (20, -7.5))
                Line((20, -7.5), (21.5, -7.5))
                Line((21.5, -7.5), (21.5, -8))
                Line((21.5, -8), (20, -8))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((23, -8), (23, -7.5))
                Line((23, -7.5), (24.5, -7.5))
                Line((24.5, -7.5), (24.5, -8))
                Line((24.5, -8), (23, -8))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((25.5, -10.5), (26, -10.5))
                Line((25.5, -9), (25.5, -10.5))
                Line((26, -9), (25.5, -9))
                Line((26, -10.5), (26, -9))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((26, -12), (26, -13.5))
                Line((26, -13.5), (25.5, -13.5))
                Line((25.5, -13.5), (25.5, -12))
                Line((25.5, -12), (26, -12))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((24.5, -14.5), (24.5, -15))
                Line((24.5, -15), (23, -15))
                Line((23, -15), (23, -14.5))
                Line((23, -14.5), (24.5, -14.5))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((21.5, -14.5), (20, -14.5))
                Line((21.5, -15), (21.5, -14.5))
                Line((20, -15), (21.5, -15))
                Line((20, -14.5), (20, -15))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((19, -12), (18.5, -12))
                Line((19, -13.5), (19, -12))
                Line((18.5, -13.5), (19, -13.5))
                Line((18.5, -12), (18.5, -13.5))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((19, -9), (19, -10.5))
                Line((19, -10.5), (18.5, -10.5))
                Line((18.5, -10.5), (18.5, -9))
                Line((18.5, -9), (19, -9))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((18.5000005215, -8.5000003576), (18.5000005215, -8.0000003502))
                Line((18.5000005215, -8.0000003502), (18.5000005215, -7.5000003427))
                Line((18.5000005215, -7.5000003427), (19.5000005364, -7.5000003427))
                Line((19.5000005364, -7.5000003427), (19.5000005364, -8.0000003502))
                Line((19.5000005364, -8.0000003502), (19.000000529, -8.0000003502))
                Line((19.000000529, -8.0000003502), (19.000000529, -8.5000003576))
                Line((19.000000529, -8.5000003576), (18.5000005215, -8.5000003576))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((25.5, -8), (25, -8))
                Line((25, -8), (25, -7.5))
                Line((25, -7.5), (26, -7.5))
                Line((26, -7.5), (26, -8))
                Line((26, -8.5), (26, -8))
                Line((25.5, -8.5), (26, -8.5))
                Line((25.5, -8), (25.5, -8.5))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((25, -14.5), (25.5, -14.5))
                Line((25.5, -14.5), (25.5, -14))
                Line((25.5, -14), (26, -14))
                Line((26, -14), (26, -15))
                Line((26, -15), (25.5, -15))
                Line((25.5, -15), (25, -15))
                Line((25, -15), (25, -14.5))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((19, -14.5), (19.5, -14.5))
                Line((19.5, -14.5), (19.5, -15))
                Line((19.5, -15), (18.5, -15))
                Line((18.5, -15), (18.5, -14.5))
                Line((18.5, -14), (18.5, -14.5))
                Line((19, -14), (18.5, -14))
                Line((19, -14.5), (19, -14))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 28.5681135836, perimeter: 40.5990247631
            with BuildLine():
                Line((34.3013000787, -18.0000002608), (33.6026002685, -19.5000002831))
                Line((33.6026002685, -19.5000002831), (34.0134569034, -19.6913772488))
                Line((34.0134569034, -19.6913772488), (33.5476570299, -20.6913772637))
                Line((33.136800395, -20.500000298), (33.5476570299, -20.6913772637))
                Line((33.136800395, -20.500000298), (32.6710005215, -21.5000003129))
                Line((35.0000005215, -21.5000003129), (32.6710005215, -21.5000003129))
                CenterArc((38.7500002608, -21.5012576094), 3.74999995, -0.0192100762, 180)
                Line((44.8290307339, -21.5025149059), (42.5, -21.5025149059))
                Line((44.3622880301, -20.500000298), (44.8290307339, -21.5025149059))
                Line((44.3622880301, -20.500000298), (44.7732163357, -20.3086835961))
                Line((44.7732163357, -20.3086835961), (44.307644356, -19.3086835812))
                Line((43.8967160503, -19.5000002831), (44.307644356, -19.3086835812))
                Line((43.1983580807, -18.0000002608), (43.8967160503, -19.5000002831))
                Line((43.1983580807, -18.0000002608), (43.6092863863, -17.8086835588))
                Line((43.6092863863, -17.8086835588), (43.1437144065, -16.8086835439))
                Line((42.7327861009, -17.0000002459), (43.1437144065, -16.8086835439))
                Line((42.5, -16.5), (42.7327861009, -17.0000002459))
                Line((41, -16.5), (42.5, -16.5))
                Line((41, -16.5), (41, -16))
                Line((41, -16), (40.5, -16))
                Line((39.5, -16), (40.5, -16))
                Line((39.5, -16.5), (39.5, -16))
                Line((38, -16.5), (39.5, -16.5))
                Line((38, -16.5), (38, -16))
                Line((37, -16), (38, -16))
                Line((37, -16), (36.5000005439, -16))
                Line((36.5000005439, -16), (36.5000005439, -16.5))
                Line((35, -16.5), (36.5000005439, -16.5))
                Line((35, -16.5), (34.7670999522, -17.0000002459))
                Line((34.7670999522, -17.0000002459), (35.1779565871, -17.1913772116))
                Line((34.8013000787, -18.0000002608), (35.1779565871, -17.1913772116))
                Line((34.7121567136, -18.1913772265), (34.8013000787, -18.0000002608))
                Line((34.3013000787, -18.0000002608), (34.7121567136, -18.1913772265))
            make_face()
            # Profile area: 20.3998471034, perimeter: 38.4517183521
            with BuildLine():
                Line((32.5000006153, -8.9999998172), (32.5000006388, -9.4999999299))
                Line((32.5000006153, -8.9999998172), (31.5000006004, -8.9999998642))
                Line((31.5000006004, -8.9999998642), (31.5000006239, -9.499999977))
                Line((30.0000005662, -9.5000000475), (31.5000006239, -9.499999977))
                Line((30.0000005662, -9.5000000475), (30.0000005662, -9.0000001341))
                Line((29.0271821067, -8.9999999859), (30.0000005662, -9.0000001341))
                Line((29.0000005631, -8.9999999818), (29.0271821067, -8.9999999859))
                Line((29.0000005631, -8.9999999818), (29.0000005858, -9.4825933536))
                Line((29.0000005866, -9.5000000945), (29.0000005858, -9.4825933536))
                Line((28.478018238, -9.5000001191), (29.0000005866, -9.5000000945))
                Line((28.2092876334, -10.5000001565), (28.478018238, -9.5000001191))
                Line((28.2092876334, -10.5000001565), (27.7092876334, -10.3656348592))
                Line((27.4405570348, -11.3656348741), (27.7092876334, -10.3656348592))
                Line((27.9405570348, -11.5000001714), (27.4405570348, -11.3656348741))
                Line((27.537461137, -13.0000001937), (27.9405570348, -11.5000001714))
                Line((27.537461137, -13.0000001937), (27.037461137, -12.8656348964))
                Line((26.7687305385, -13.8656349113), (27.037461137, -12.8656348964))
                Line((27.2687305385, -14.0000002086), (26.7687305385, -13.8656349113))
                Line((27, -15), (27.2687305385, -14.0000002086))
                Line((27, -15), (27, -15.5))
                Line((27, -15.5), (28, -15.5))
                Line((28, -15.5), (28, -15))
                Line((28, -15), (28.5000005439, -15))
                Line((28.5000005439, -15), (29.7272732784, -10.5000001565))
                Line((29.7272732784, -10.5000001565), (31.7727278654, -10.5000001565))
                Line((31.7727278654, -10.5000001565), (33.0000006109, -15.0000002235))
                Line((33.0000006109, -15.0000002235), (33.5, -15.000000149))
                Line((33.5000000745, -15.500000149), (33.5, -15.000000149))
                Line((34.5000000745, -15.5), (33.5000000745, -15.500000149))
                Line((34.5, -15), (34.5000000745, -15.5))
                Line((34.5, -15), (34.2316665793, -14.0000002086))
                Line((34.2316665793, -14.0000002086), (33.7316665793, -14.1341669469))
                Line((33.4633330987, -13.134166932), (33.7316665793, -14.1341669469))
                Line((33.9633330987, -13.0000001937), (33.4633330987, -13.134166932))
                Line((33.9633330987, -13.0000001937), (33.5608328777, -11.5000001714))
                Line((33.5608328777, -11.5000001714), (33.0608328777, -11.6341669097))
                Line((32.7924993933, -10.634166859), (33.0608328777, -11.6341669097))
                Line((33.292499387, -10.5000001192), (32.7924993933, -10.634166859))
                Line((33.292499387, -10.5000001192), (33.0241658529, -9.4999999053))
                Line((32.5000006388, -9.4999999299), (33.0241658529, -9.4999999053))
            make_face()
            # Profile area: 28.5681135836, perimeter: 40.5990247631
            with BuildLine():
                Line((46.8013000787, -18.0000002608), (46.1026002685, -19.5000002831))
                Line((46.1026002685, -19.5000002831), (46.5134569034, -19.6913772488))
                Line((46.5134569034, -19.6913772488), (46.0476570299, -20.6913772637))
                Line((45.636800395, -20.500000298), (46.0476570299, -20.6913772637))
                Line((45.636800395, -20.500000298), (45.1710005215, -21.5000003129))
                Line((47.5000005215, -21.5000003129), (45.1710005215, -21.5000003129))
                CenterArc((51.2500002608, -21.5012576094), 3.74999995, -0.0192100762, 180)
                Line((57.3290307339, -21.5025149059), (55, -21.5025149059))
                Line((56.8622880301, -20.500000298), (57.3290307339, -21.5025149059))
                Line((56.8622880301, -20.500000298), (57.2732163357, -20.3086835961))
                Line((57.2732163357, -20.3086835961), (56.807644356, -19.3086835812))
                Line((56.3967160503, -19.5000002831), (56.807644356, -19.3086835812))
                Line((55.6983580807, -18.0000002608), (56.3967160503, -19.5000002831))
                Line((55.6983580807, -18.0000002608), (56.1092863863, -17.8086835588))
                Line((56.1092863863, -17.8086835588), (55.6437144065, -16.8086835439))
                Line((55.2327861009, -17.0000002459), (55.6437144065, -16.8086835439))
                Line((55, -16.5), (55.2327861009, -17.0000002459))
                Line((53.5, -16.5), (55, -16.5))
                Line((53.5, -16.5), (53.5, -16))
                Line((53.5, -16), (53, -16))
                Line((52, -16), (53, -16))
                Line((52, -16.5), (52, -16))
                Line((50.5, -16.5), (52, -16.5))
                Line((50.5, -16.5), (50.5, -16))
                Line((49.5, -16), (50.5, -16))
                Line((49.5, -16), (49.0000005439, -16))
                Line((49.0000005439, -16), (49.0000005439, -16.5))
                Line((47.5, -16.5), (49.0000005439, -16.5))
                Line((47.5, -16.5), (47.2670999522, -17.0000002459))
                Line((47.2670999522, -17.0000002459), (47.6779565871, -17.1913772116))
                Line((47.3013000787, -18.0000002608), (47.6779565871, -17.1913772116))
                Line((47.2121567136, -18.1913772265), (47.3013000787, -18.0000002608))
                Line((46.8013000787, -18.0000002608), (47.2121567136, -18.1913772265))
            make_face()
            # Profile area: 20.3998471034, perimeter: 38.4517183521
            with BuildLine():
                Line((48.5000006153, -8.9999998172), (48.5000006388, -9.4999999299))
                Line((48.5000006153, -8.9999998172), (47.5000006004, -8.9999998642))
                Line((47.5000006004, -8.9999998642), (47.5000006239, -9.499999977))
                Line((46.0000005662, -9.5000000475), (47.5000006239, -9.499999977))
                Line((46.0000005662, -9.5000000475), (46.0000005662, -9.0000001341))
                Line((45.0271821067, -8.9999999859), (46.0000005662, -9.0000001341))
                Line((45.0000005631, -8.9999999818), (45.0271821067, -8.9999999859))
                Line((45.0000005631, -8.9999999818), (45.0000005858, -9.4825933536))
                Line((45.0000005866, -9.5000000945), (45.0000005858, -9.4825933536))
                Line((44.478018238, -9.5000001191), (45.0000005866, -9.5000000945))
                Line((44.2092876334, -10.5000001565), (44.478018238, -9.5000001191))
                Line((44.2092876334, -10.5000001565), (43.7092876334, -10.3656348592))
                Line((43.4405570348, -11.3656348741), (43.7092876334, -10.3656348592))
                Line((43.9405570348, -11.5000001714), (43.4405570348, -11.3656348741))
                Line((43.537461137, -13.0000001937), (43.9405570348, -11.5000001714))
                Line((43.537461137, -13.0000001937), (43.037461137, -12.8656348964))
                Line((42.7687305385, -13.8656349113), (43.037461137, -12.8656348964))
                Line((43.2687305385, -14.0000002086), (42.7687305385, -13.8656349113))
                Line((43, -15), (43.2687305385, -14.0000002086))
                Line((43, -15), (43, -15.5))
                Line((43, -15.5), (44, -15.5))
                Line((44, -15.5), (44, -15))
                Line((44, -15), (44.5000005439, -15))
                Line((44.5000005439, -15), (45.7272732784, -10.5000001565))
                Line((45.7272732784, -10.5000001565), (47.7727278654, -10.5000001565))
                Line((47.7727278654, -10.5000001565), (49.0000006109, -15.0000002235))
                Line((49.0000006109, -15.0000002235), (49.5, -15.000000149))
                Line((49.5000000745, -15.500000149), (49.5, -15.000000149))
                Line((50.5000000745, -15.5), (49.5000000745, -15.500000149))
                Line((50.5, -15), (50.5000000745, -15.5))
                Line((50.5, -15), (50.2316665793, -14.0000002086))
                Line((50.2316665793, -14.0000002086), (49.7316665793, -14.1341669469))
                Line((49.4633330987, -13.134166932), (49.7316665793, -14.1341669469))
                Line((49.9633330987, -13.0000001937), (49.4633330987, -13.134166932))
                Line((49.9633330987, -13.0000001937), (49.5608328777, -11.5000001714))
                Line((49.5608328777, -11.5000001714), (49.0608328777, -11.6341669097))
                Line((48.7924993933, -10.634166859), (49.0608328777, -11.6341669097))
                Line((49.292499387, -10.5000001192), (48.7924993933, -10.634166859))
                Line((49.292499387, -10.5000001192), (49.0241658529, -9.4999999053))
                Line((48.5000006388, -9.4999999299), (49.0241658529, -9.4999999053))
            make_face()
            # Profile area: 28.5681135836, perimeter: 40.5990247631
            with BuildLine():
                Line((21.8013000787, -18.0000002608), (21.1026002685, -19.5000002831))
                Line((21.1026002685, -19.5000002831), (21.5134569034, -19.6913772488))
                Line((21.5134569034, -19.6913772488), (21.0476570299, -20.6913772637))
                Line((20.636800395, -20.500000298), (21.0476570299, -20.6913772637))
                Line((20.636800395, -20.500000298), (20.1710005215, -21.5000003129))
                Line((22.5000005215, -21.5000003129), (20.1710005215, -21.5000003129))
                CenterArc((26.2500002608, -21.5012576094), 3.74999995, -0.0192100762, 180)
                Line((32.3290307339, -21.5025149059), (30, -21.5025149059))
                Line((31.8622880301, -20.500000298), (32.3290307339, -21.5025149059))
                Line((31.8622880301, -20.500000298), (32.2732163357, -20.3086835961))
                Line((32.2732163357, -20.3086835961), (31.807644356, -19.3086835812))
                Line((31.3967160503, -19.5000002831), (31.807644356, -19.3086835812))
                Line((30.6983580807, -18.0000002608), (31.3967160503, -19.5000002831))
                Line((30.6983580807, -18.0000002608), (31.1092863863, -17.8086835588))
                Line((31.1092863863, -17.8086835588), (30.6437144065, -16.8086835439))
                Line((30.2327861009, -17.0000002459), (30.6437144065, -16.8086835439))
                Line((30, -16.5), (30.2327861009, -17.0000002459))
                Line((28.5, -16.5), (30, -16.5))
                Line((28.5, -16.5), (28.5, -16))
                Line((28.5, -16), (28, -16))
                Line((27, -16), (28, -16))
                Line((27, -16.5), (27, -16))
                Line((25.5, -16.5), (27, -16.5))
                Line((25.5, -16.5), (25.5, -16))
                Line((24.5, -16), (25.5, -16))
                Line((24.5, -16), (24.0000005439, -16))
                Line((24.0000005439, -16), (24.0000005439, -16.5))
                Line((22.5, -16.5), (24.0000005439, -16.5))
                Line((22.5, -16.5), (22.2670999522, -17.0000002459))
                Line((22.2670999522, -17.0000002459), (22.6779565871, -17.1913772116))
                Line((22.3013000787, -18.0000002608), (22.6779565871, -17.1913772116))
                Line((22.2121567136, -18.1913772265), (22.3013000787, -18.0000002608))
                Line((21.8013000787, -18.0000002608), (22.2121567136, -18.1913772265))
            make_face()
            # Profile area: 26.2499998063, perimeter: 29.9999989271
            with BuildLine():
                Line((37.0000005513, -8.0000001192), (38.0000005662, -8.0000001192))
                Line((38.0000005662, -8.0000001192), (38.0000005662, -8.5))
                Line((38.0000005662, -8.5), (39.5000005886, -8.5))
                Line((39.5000005886, -8.0000001192), (39.5000005886, -8.5))
                Line((39.5000005886, -8.0000001192), (40.5000006035, -8.0000001192))
                Line((40.5000006035, -8.0000001192), (40.5000006035, -8.5))
                Line((40.5000006035, -8.5), (41.5, -8.5))
                Line((41.5, -8.5), (41.5, -7.5000001118))
                Line((41.0000006109, -7.5000001118), (41.5, -7.5000001118))
                Line((41.0000006109, -7.5000001118), (41.0000006109, -6.5000000969))
                Line((41.0000006109, -6.5000000969), (41.5, -6.5000000969))
                Line((41.5, -6.5000000969), (41.5, -5.0000000745))
                Line((41.0000006109, -5.0000000745), (41.5, -5.0000000745))
                Line((41.0000006109, -4.0000000596), (41.0000006109, -5.0000000745))
                Line((41.0000006109, -4.0000000596), (41.5, -4.0000000596))
                Line((41.5, -4.0000000596), (41.5, -3))
                Line((41.5, -3), (40.5000006035, -3))
                Line((40.5000006035, -3.5000000522), (40.5000006035, -3))
                Line((40.5000006035, -3.5000000522), (39.5000005886, -3.5000000522))
                Line((39.5000005886, -3.5000000522), (39.5000005886, -3))
                Line((39.5000005886, -3), (38.0000005662, -3))
                Line((38.0000005662, -3.5000000522), (38.0000005662, -3))
                Line((37.0000005513, -3.5000000522), (38.0000005662, -3.5000000522))
                Line((37.0000005513, -3.5000000522), (37.0000005513, -3))
                Line((37.0000005513, -3), (36, -3))
                Line((36, -3), (36, -4.0000000596))
                Line((36.5000005439, -4.0000000596), (36, -4.0000000596))
                Line((36.5000005439, -4.0000000596), (36.5000005439, -5.0000000745))
                Line((36.0000005364, -5.0000000745), (36.5000005439, -5.0000000745))
                Line((36.0000005364, -5.0000000745), (36, -6.5000000969))
                Line((36.5000005439, -6.5000000969), (36, -6.5000000969))
                Line((36.5000005439, -7.5000001118), (36.5000005439, -6.5000000969))
                Line((36.5000005439, -7.5000001118), (36, -7.5000001118))
                Line((36, -7.5000001118), (36, -8.5))
                Line((36, -8.5), (37.0000005513, -8.5))
                Line((37.0000005513, -8.0000001192), (37.0000005513, -8.5))
            make_face()
            # Profile area: 28.5681135836, perimeter: 40.5990247631
            with BuildLine():
                Line((46.3013000787, -5.0000002608), (45.6026002685, -6.5000002831))
                Line((45.6026002685, -6.5000002831), (46.0134569034, -6.6913772488))
                Line((46.0134569034, -6.6913772488), (45.5476570299, -7.6913772637))
                Line((45.136800395, -7.500000298), (45.5476570299, -7.6913772637))
                Line((45.136800395, -7.500000298), (44.6710005215, -8.5000003129))
                Line((47.0000005215, -8.5000003129), (44.6710005215, -8.5000003129))
                CenterArc((50.7500002608, -8.5012576094), 3.74999995, -0.0192100762, 180)
                Line((56.8290307339, -8.5025149059), (54.5, -8.5025149059))
                Line((56.3622880301, -7.500000298), (56.8290307339, -8.5025149059))
                Line((56.3622880301, -7.500000298), (56.7732163357, -7.3086835961))
                Line((56.7732163357, -7.3086835961), (56.307644356, -6.3086835812))
                Line((55.8967160503, -6.5000002831), (56.307644356, -6.3086835812))
                Line((55.1983580807, -5.0000002608), (55.8967160503, -6.5000002831))
                Line((55.1983580807, -5.0000002608), (55.6092863863, -4.8086835588))
                Line((55.6092863863, -4.8086835588), (55.1437144065, -3.8086835439))
                Line((54.7327861009, -4.0000002459), (55.1437144065, -3.8086835439))
                Line((54.5, -3.5), (54.7327861009, -4.0000002459))
                Line((53, -3.5), (54.5, -3.5))
                Line((53, -3.5), (53, -3))
                Line((53, -3), (52.5, -3))
                Line((51.5, -3), (52.5, -3))
                Line((51.5, -3.5), (51.5, -3))
                Line((50, -3.5), (51.5, -3.5))
                Line((50, -3.5), (50, -3))
                Line((49, -3), (50, -3))
                Line((49, -3), (48.5000005439, -3))
                Line((48.5000005439, -3), (48.5000005439, -3.5))
                Line((47, -3.5), (48.5000005439, -3.5))
                Line((47, -3.5), (46.7670999522, -4.0000002459))
                Line((46.7670999522, -4.0000002459), (47.1779565871, -4.1913772116))
                Line((46.8013000787, -5.0000002608), (47.1779565871, -4.1913772116))
                Line((46.7121567136, -5.1913772265), (46.8013000787, -5.0000002608))
                Line((46.3013000787, -5.0000002608), (46.7121567136, -5.1913772265))
            make_face()
            # Profile area: 20.3998471034, perimeter: 38.4517183521
            with BuildLine():
                Line((36.2092876334, -10.5000001565), (35.7092876334, -10.3656348592))
                Line((35.4405570348, -11.3656348741), (35.7092876334, -10.3656348592))
                Line((35.9405570348, -11.5000001714), (35.4405570348, -11.3656348741))
                Line((35.537461137, -13.0000001937), (35.9405570348, -11.5000001714))
                Line((35.537461137, -13.0000001937), (35.037461137, -12.8656348964))
                Line((34.7687305385, -13.8656349113), (35.037461137, -12.8656348964))
                Line((35.2687305385, -14.0000002086), (34.7687305385, -13.8656349113))
                Line((35, -15), (35.2687305385, -14.0000002086))
                Line((35, -15), (35, -15.5))
                Line((35, -15.5), (36, -15.5))
                Line((36, -15.5), (36, -15))
                Line((36, -15), (36.5000005439, -15))
                Line((36.5000005439, -15), (37.7272732784, -10.5000001565))
                Line((37.7272732784, -10.5000001565), (39.7727278654, -10.5000001565))
                Line((39.7727278654, -10.5000001565), (41.0000006109, -15.0000002235))
                Line((41.0000006109, -15.0000002235), (41.5, -15.000000149))
                Line((41.5000000745, -15.500000149), (41.5, -15.000000149))
                Line((42.5000000745, -15.5), (41.5000000745, -15.500000149))
                Line((42.5, -15), (42.5000000745, -15.5))
                Line((42.5, -15), (42.2316665793, -14.0000002086))
                Line((42.2316665793, -14.0000002086), (41.7316665793, -14.1341669469))
                Line((41.4633330987, -13.134166932), (41.7316665793, -14.1341669469))
                Line((41.9633330987, -13.0000001937), (41.4633330987, -13.134166932))
                Line((41.9633330987, -13.0000001937), (41.5608328777, -11.5000001714))
                Line((41.5608328777, -11.5000001714), (41.0608328777, -11.6341669097))
                Line((40.7924993933, -10.634166859), (41.0608328777, -11.6341669097))
                Line((41.292499387, -10.5000001192), (40.7924993933, -10.634166859))
                Line((41.292499387, -10.5000001192), (41.0241658529, -9.4999999053))
                Line((40.5000006388, -9.4999999299), (41.0241658529, -9.4999999053))
                Line((40.5000006153, -8.9999998172), (40.5000006388, -9.4999999299))
                Line((40.5000006153, -8.9999998172), (39.5000006004, -8.9999998642))
                Line((39.5000006004, -8.9999998642), (39.5000006239, -9.499999977))
                Line((38.0000005662, -9.5000000475), (39.5000006239, -9.499999977))
                Line((38.0000005662, -9.5000000475), (38.0000005662, -9.0000001341))
                Line((37.0271821067, -8.9999999859), (38.0000005662, -9.0000001341))
                Line((37.0000005631, -8.9999999818), (37.0271821067, -8.9999999859))
                Line((37.0000005631, -8.9999999818), (37.0000005858, -9.4825933536))
                Line((37.0000005866, -9.5000000945), (37.0000005858, -9.4825933536))
                Line((36.478018238, -9.5000001191), (37.0000005866, -9.5000000945))
                Line((36.2092876334, -10.5000001565), (36.478018238, -9.5000001191))
            make_face()
            # Profile area: 20.3998471034, perimeter: 38.4517183521
            with BuildLine():
                Line((56.5000006153, -8.9999998172), (56.5000006388, -9.4999999299))
                Line((56.5000006153, -8.9999998172), (55.5000006004, -8.9999998642))
                Line((55.5000006004, -8.9999998642), (55.5000006239, -9.499999977))
                Line((54.0000005662, -9.5000000475), (55.5000006239, -9.499999977))
                Line((54.0000005662, -9.5000000475), (54.0000005662, -9.0000001341))
                Line((53.0271821067, -8.9999999859), (54.0000005662, -9.0000001341))
                Line((53.0000005631, -8.9999999818), (53.0271821067, -8.9999999859))
                Line((53.0000005631, -8.9999999818), (53.0000005858, -9.4825933536))
                Line((53.0000005866, -9.5000000945), (53.0000005858, -9.4825933536))
                Line((52.478018238, -9.5000001191), (53.0000005866, -9.5000000945))
                Line((52.2092876334, -10.5000001565), (52.478018238, -9.5000001191))
                Line((52.2092876334, -10.5000001565), (51.7092876334, -10.3656348592))
                Line((51.4405570348, -11.3656348741), (51.7092876334, -10.3656348592))
                Line((51.9405570348, -11.5000001714), (51.4405570348, -11.3656348741))
                Line((51.537461137, -13.0000001937), (51.9405570348, -11.5000001714))
                Line((51.537461137, -13.0000001937), (51.037461137, -12.8656348964))
                Line((50.7687305385, -13.8656349113), (51.037461137, -12.8656348964))
                Line((51.2687305385, -14.0000002086), (50.7687305385, -13.8656349113))
                Line((51, -15), (51.2687305385, -14.0000002086))
                Line((51, -15), (51, -15.5))
                Line((51, -15.5), (52, -15.5))
                Line((52, -15.5), (52, -15))
                Line((52, -15), (52.5000005439, -15))
                Line((52.5000005439, -15), (53.7272732784, -10.5000001565))
                Line((53.7272732784, -10.5000001565), (55.7727278654, -10.5000001565))
                Line((55.7727278654, -10.5000001565), (57.0000006109, -15.0000002235))
                Line((57.0000006109, -15.0000002235), (57.5, -15.000000149))
                Line((57.5000000745, -15.500000149), (57.5, -15.000000149))
                Line((58.5000000745, -15.5), (57.5000000745, -15.500000149))
                Line((58.5, -15), (58.5000000745, -15.5))
                Line((58.5, -15), (58.2316665793, -14.0000002086))
                Line((58.2316665793, -14.0000002086), (57.7316665793, -14.1341669469))
                Line((57.4633330987, -13.134166932), (57.7316665793, -14.1341669469))
                Line((57.9633330987, -13.0000001937), (57.4633330987, -13.134166932))
                Line((57.9633330987, -13.0000001937), (57.5608328777, -11.5000001714))
                Line((57.5608328777, -11.5000001714), (57.0608328777, -11.6341669097))
                Line((56.7924993933, -10.634166859), (57.0608328777, -11.6341669097))
                Line((57.292499387, -10.5000001192), (56.7924993933, -10.634166859))
                Line((57.292499387, -10.5000001192), (57.0241658529, -9.4999999053))
                Line((56.5000006388, -9.4999999299), (57.0241658529, -9.4999999053))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is an elliptical or oval-shaped plate or diaphragm with a curved, bowl-like profile featuring radial reinforcing ribs or supports that extend from the center to the perimeter edge.
def model_125428_e6d291da_0002():
    """Model: Central Disk"""
    with BuildPart() as part:
        # Central Disk -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 23 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 660.5198554173, perimeter: 91.1061869541
            Circle(14.5)
        # OneSide extrude, distance=0.9
        extrude(amount=0.9)
    return part.part


# Description: This is a cylindrical rod or shaft with a uniform circular cross-section, featuring rounded ends and a smooth, tapered surface along its length.
def model_125428_e6d291da_0003():
    """Model: Tube Assembly v1"""
    with BuildPart() as part:
        # Tube -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 5.2477163686, perimeter: 29.1539798253
            with BuildLine():
                CenterArc((0, 1.5000000224), 2.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 1.5000000224), 2.14, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=40
        extrude(amount=20, both=True)
    return part.part


# Description: This is a hexagonal prism or wedge-shaped structural component with a trapezoidal profile, featuring angled faces and internal triangular divisions that suggest reinforcing ribs or internal bracing geometry.
def model_125591_12eac82b_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 100, perimeter: 40
            with BuildLine():
                Line((5, -5), (-5, -5))
                Line((5, 5), (5, -5))
                Line((-5, 5), (5, 5))
                Line((-5, -5), (-5, 5))
            make_face()
        # OneSide extrude, distance=20
        extrude(amount=20)
    return part.part


# Description: This is a streamlined, boat-shaped or wedge-like structural component with an asymmetrical polygonal profile featuring a tapered body, angular faceted surfaces, and a hollow or recessed underside, designed for aerodynamic or hydrodynamic efficiency.
def model_125594_799c122a_0005():
    """Model: 701176 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.825, perimeter: 10.9
            with BuildLine():
                Line((3.5, -1.95), (0, -1.95))
                Line((3.5, 0), (3.5, -1.95))
                Line((0, 0), (3.5, 0))
                Line((0, -1.95), (0, 0))
            make_face()
        # OneSide extrude, distance=0.65
        extrude(amount=0.65)
    return part.part


# Description: This is a rectangular plastic or composite mounting bracket with a long, narrow elongated shape featuring multiple regularly-spaced rectangular slots or openings along its length and raised flanges on the sides for structural support and fastening.
def model_125745_cf468448_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 126 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0267051109, perimeter: 0.8043129568
            with BuildLine():
                Line((-5.2677500612, 3.0382838829), (-5.2677500612, 2.7939999662))
                Line((-5.2677500612, 2.7939999662), (-5.2577999365, 2.7939999662))
                CenterArc((-4.03142088, 1.9337214124), 1.4980269625, 132.494273735, 12.4568915801)
                Line((-5.0433628393, 3.0382838829), (-5.2677500612, 3.0382838829))
            make_face()
            # Profile area: 0.0911614662, perimeter: 1.1747212315
            with BuildLine():
                Line((-4.9783999398, 2.6161999684), (-4.7497999426, 2.7685999665))
                CenterArc((-4.8691784393, 2.8524214674), 0.1458673009, -35.0745762898, 160.1491525795)
                Line((-5.130799938, 2.7431999668), (-4.9529999401, 2.9717999641))
                CenterArc((-5.2248953914, 2.4753454246), 0.2839014092, 29.7448812969, 40.8990952216)
            make_face()
            # Profile area: 0.0348386392, perimeter: 0.8542860041
            with BuildLine():
                Line((-4.7497999426, 2.3367999718), (-4.9783999398, 2.4891999699))
                Line((-4.7497999426, 2.6415999681), (-4.7497999426, 2.3367999718))
                Line((-4.9783999398, 2.4891999699), (-4.7497999426, 2.6415999681))
            make_face()
            # Profile area: 0.0887183793, perimeter: 1.207667512
            with BuildLine():
                Line((-5.1435960835, 2.2732708506), (-4.9021999408, 1.9811999761))
                CenterArc((-4.8823750012, 2.1250812695), 0.145240679, -97.8452020441, 121.9506087965)
                Line((-5.0136515749, 2.3961641068), (-4.7497999426, 2.1843999736))
                CenterArc((-5.2885286254, 2.5566659927), 0.3183052753, -62.9141138544, 32.6332753142)
            make_face()
            # Profile area: 0.0223072666, perimeter: 0.7846007588
            with BuildLine():
                Line((-5.2577999365, 1.9811999761), (-5.0545999389, 1.9811999761))
                CenterArc((-4.5211999454, 2.6161999684), 0.829301238, -152.6501242199, 22.619864948)
                Line((-5.2577999365, 2.235199973), (-5.2577999365, 1.9811999761))
            make_face()
            # Profile area: 0.0455454846, perimeter: 0.8231429304
            with BuildLine():
                CenterArc((-5.2157160115, 2.5018999698), 0.1459011524, -106.7646647502, 213.5293295004)
                Line((-5.2577999365, 2.6415999681), (-5.2577999365, 2.3621999715))
            make_face()
            # Profile area: 7.0331131569, perimeter: 81.1637267483
            with BuildLine():
                Line((3.2387780228, 1.2700000405), (3.2387780228, 2.286000073))
                Line((3.2387780228, 2.286000073), (3.8100001216, 2.286000073))
                Line((3.8100001216, 2.286000073), (3.8100001216, 1.9050000608))
                Line((3.8100001216, 1.9050000608), (4.0209650912, 1.9050000608))
                Line((4.0209650912, 1.9050000608), (4.0209650912, 3.1169514502))
                Line((4.0209650912, 3.1169514502), (5.2070001662, 3.1169514502))
                Line((5.2070001662, 3.1169514502), (5.2070001662, 3.3020001054))
                Line((5.2070001662, 3.3020001054), (-5.2577999365, 3.3020001054))
                Line((-5.2577999365, 3.0987999626), (-5.2577999365, 3.3020001054))
                Line((-4.6735999435, 3.0987999626), (-5.2577999365, 3.0987999626))
                Line((-4.6735999435, 1.904999977), (-4.6735999435, 3.0987999626))
                Line((-5.2577999365, 1.904999977), (-4.6735999435, 1.904999977))
                Line((-5.2577999365, 1.8287999779), (-5.2577999365, 1.904999977))
                Line((-4.5949737005, 1.8287999779), (-5.2577999365, 1.8287999779))
                Line((-4.5949737005, 3.1134066608), (-4.5949737005, 1.8287999779))
                Line((-3.1926587027, 3.1134066608), (-4.5949737005, 3.1134066608))
                Line((-3.1926587027, 3.1134066608), (-3.1926587027, 2.4938500569))
                Line((-3.1926587027, 2.4938500569), (-3.9831501498, 2.4938500569))
                Line((-3.9831501498, 2.4938500569), (-3.9831501498, 1.2700000405))
                Line((-3.9831501498, 1.2700000405), (-5.2416126843, 1.2700000405))
                Line((-5.2416126843, 1.2700000405), (-5.2416126843, 1.0630774742))
                Line((-5.2416126843, 1.0630774742), (5.2070001662, 1.0630774742))
                Line((5.2070001662, 1.0630774742), (5.2070001662, 1.2700000405))
                Line((4.6481999438, 1.2699999847), (5.2070001662, 1.2700000405))
                Line((4.6481999438, 2.4637999702), (4.6481999438, 1.2699999847))
                Line((5.2069999371, 2.4637999702), (4.6481999438, 2.4637999702))
                Line((5.2069999371, 2.5145999696), (5.2069999371, 2.4637999702))
                Line((4.5719999447, 2.5145999696), (5.2069999371, 2.5145999696))
                Line((4.5719999447, 1.2700000405), (4.5719999447, 2.5145999696))
                Line((3.2387780228, 1.2700000405), (4.5719999447, 1.2700000405))
            make_face()
            with BuildLine():
                Line((-2.328542148, 2.4637999702), (-2.328542148, 1.2700000405))
                Line((-2.328542148, 2.4637999702), (-1.1430000365, 2.4637999702))
                Line((-1.1430000365, 1.2700000405), (-1.1430000365, 2.4637999702))
                Line((-2.328542148, 1.2700000405), (-1.1430000365, 1.2700000405))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-0.5587999932, 1.8795999773), (-0.3047999963, 1.8795999773))
                Line((-0.3047999963, 1.8795999773), (-0.3047999963, 2.235199973))
                Line((-0.3047999963, 2.235199973), (0.2285999972, 2.235199973))
                Line((0.2285999972, 2.235199973), (0.2285999972, 1.2700000405))
                Line((0.2285999972, 1.2700000405), (-1.0696942956, 1.2700000405))
                Line((-1.0696942956, 1.2700000405), (-1.0696942956, 2.5400000811))
                Line((-1.0696942956, 2.5400000811), (-2.413000077, 2.5400000811))
                Line((-2.413000077, 2.5400000811), (-2.413000077, 1.2700000405))
                Line((-2.413000077, 1.2700000405), (-3.7337999549, 1.2699999847))
                Line((-3.7337999549, 1.2699999847), (-3.7337999549, 2.235199973))
                Line((-3.7337999549, 2.235199973), (-3.225799961, 2.235199973))
                Line((-3.225799961, 2.235199973), (-3.225799961, 1.8795999773))
                Line((-3.225799961, 1.8795999773), (-2.9717999641, 1.8795999773))
                Line((-2.9717999641, 1.8795999773), (-2.9717999641, 3.1114999624))
                Line((-2.9717999641, 3.1114999624), (-0.5587999932, 3.1114999624))
                Line((-0.5587999932, 3.1114999624), (-0.5587999932, 1.8795999773))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((1.1429999862, 3.1241999622), (1.1429999862, 1.904999977))
                Line((1.1429999862, 3.1241999622), (2.3367999718, 3.1241999622))
                Line((2.3367999718, 1.904999977), (2.3367999718, 3.1241999622))
                Line((1.1429999862, 1.904999977), (2.3367999718, 1.904999977))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-0.2982142019, 2.4940549456), (0.4407467237, 2.4940549456))
                Line((-0.2982142019, 2.4940549456), (-0.304379943, 3.1241999622))
                Line((1.0605883997, 3.1241999622), (-0.304379943, 3.1241999622))
                Line((1.0605883997, 1.8512247689), (1.0605883997, 3.1241999622))
                Line((2.4129999708, 1.8512247689), (1.0605883997, 1.8512247689))
                Line((2.4129999708, 3.1241999622), (2.4129999708, 1.8512247689))
                Line((3.809999954, 3.1241999622), (2.4129999708, 3.1241999622))
                Line((3.809999954, 2.5145999696), (3.809999954, 3.1241999622))
                Line((3.0225999635, 2.5145999696), (3.809999954, 2.5145999696))
                Line((3.0225999635, 1.2699999847), (3.0225999635, 2.5145999696))
                Line((0.4571999945, 1.2699999847), (3.0225999635, 1.2699999847))
                Line((0.4407467237, 2.4940549456), (0.4571999945, 1.2699999847))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.6221355271, perimeter: 6.4443497974
            with BuildLine():
                Line((-4.4449999463, 1.7017999794), (-5.2548772759, 1.7003940896))
                Line((-5.2548772759, 1.7003940896), (-5.2548772759, 1.5240000486))
                Line((-5.2548772759, 1.5240000486), (-4.216399949, 1.5240000486))
                Line((-4.216399949, 1.5240000486), (-4.216399949, 2.6923999675))
                Line((-4.216399949, 2.6923999675), (-3.4035999589, 2.6923999675))
                Line((-3.4035999589, 2.6923999675), (-3.4035999589, 2.895599965))
                Line((-3.4035999589, 2.895599965), (-4.4449999463, 2.895599965))
                Line((-4.4449999463, 2.895599965), (-4.4449999463, 1.7017999794))
            make_face()
            # Profile area: 1.5393143466, perimeter: 14.3313113957
            with BuildLine():
                Line((-2.515983625, 1.4552162361), (-3.57784284, 1.4505688828))
                Line((-2.521522131, 2.7206921322), (-2.515983625, 1.4552162361))
                Line((-0.9641150798, 2.7275083098), (-2.521522131, 2.7206921322))
                Line((-0.9585370313, 1.4529974844), (-0.9641150798, 2.7275083098))
                Line((0.0553742365, 1.4574349879), (-0.9585370313, 1.4529974844))
                Line((0.0525883199, 2.0939803482), (0.0553742365, 1.4574349879))
                Line((-0.1288124372, 2.0931864262), (0.0525883199, 2.0939803482))
                Line((-0.1269999984, 1.6790679667), (-0.1288124372, 2.0931864262))
                Line((-0.7365999911, 1.6763999797), (-0.1269999984, 1.6790679667))
                Line((-0.7420471312, 2.9209999647), (-0.7365999911, 1.6763999797))
                Line((-2.7685999665, 2.9209999647), (-0.7420471312, 2.9209999647))
                Line((-2.7685999665, 1.7017999794), (-2.7685999665, 2.9209999647))
                Line((-3.3527999595, 1.7017999794), (-2.7685999665, 1.7017999794))
                Line((-3.3527999595, 2.0827999748), (-3.3527999595, 1.7017999794))
                Line((-3.5813999567, 2.0827999748), (-3.3527999595, 2.0827999748))
                Line((-3.57784284, 1.4505688828), (-3.5813999567, 2.0827999748))
            make_face()
            # Profile area: 0.0348386392, perimeter: 0.8542860041
            with BuildLine():
                Line((-2.0319999754, 1.8795999773), (-2.2605999727, 2.0319999754))
                Line((-2.2605999727, 2.0319999754), (-2.2605999727, 1.7271999791))
                Line((-2.2605999727, 1.7271999791), (-2.0319999754, 1.8795999773))
            make_face()
            # Profile area: 0.0506707467, perimeter: 0.7979645244
            with Locations((-1.7525999788, 1.8795999773)):
                Circle(0.1269999985)
            # Profile area: 0.0605878317, perimeter: 1.1474669472
            with BuildLine():
                Line((-1.7921658724, 2.121484874), (-1.7326068417, 2.121484874))
                CenterArc((-0.9101412299, 1.7098967364), 0.9197034727, 131.8707872329, 21.5443621078)
                Line((-1.94982213, 2.3947557207), (-1.5240000486, 2.3947557207))
                CenterArc((-2.9946329886, 1.6098670354), 1.3067822996, 23.0484648903, 13.866348957)
            make_face()
            # Profile area: 0.0387095991, perimeter: 0.8972247017
            with BuildLine():
                Line((-1.2191999853, 1.7271999791), (-1.4731999822, 1.8795999773))
                Line((-1.2191999853, 2.0319999754), (-1.2191999853, 1.7271999791))
                Line((-1.4731999822, 1.8795999773), (-1.2191999853, 2.0319999754))
            make_face()
            # Profile area: 0.0457760433, perimeter: 1.0032687079
            with BuildLine():
                Line((-1.7779999785, 1.6001999807), (-1.7271999791, 1.6001999807))
                CenterArc((-2.8701999653, 2.0827999748), 1.1940701678, -38.088772881, 14.2500326978)
                Line((-1.574799981, 1.3461999837), (-1.9303999767, 1.3461999837))
                CenterArc((-1.1953321068, 1.7466007061), 0.5516489881, -164.6100228154, 31.147558695)
            make_face()
            # Profile area: 1.1865898962, perimeter: 12.5696198899
            with BuildLine():
                Line((0.9315212528, 2.895777432), (-0.0891579195, 2.8915175186))
                Line((-0.0891579195, 2.8915175186), (-0.0891579195, 2.6670000851))
                Line((-0.0891579195, 2.6670000851), (0.7176835318, 2.6670000851))
                Line((0.7176835318, 2.6670000851), (0.7176835318, 1.5240000486))
                Line((0.7176835318, 1.5240000486), (2.757408883, 1.5240000486))
                Line((2.757408883, 1.5240000486), (2.757408883, 2.6670000851))
                Line((2.757408883, 2.6670000851), (3.5560001135, 2.6670000851))
                Line((3.5560001135, 2.6670000851), (3.5560001135, 2.9210000932))
                Line((3.5560001135, 2.9210000932), (2.5400000811, 2.9210000932))
                Line((2.5400000811, 2.9210000932), (2.5400000811, 1.6510000527))
                Line((2.5400000811, 1.6510000527), (0.9315212528, 1.6510000527))
                Line((0.9315212528, 1.6510000527), (0.9315212528, 2.895777432))
            make_face()
            # Profile area: 0.0862037686, perimeter: 1.1694300858
            with BuildLine():
                Line((1.4223999828, 2.9717999641), (1.6255999804, 2.7431999668))
                CenterArc((1.3588999836, 2.8574999655), 0.1307545012, 60.9453959009, 148.1092081982)
                Line((1.244599985, 2.7939999662), (1.4731999822, 2.5907999687))
                CenterArc((1.7652999787, 2.4510999704), 0.3237877352, 115.5599651718, 38.8800696564)
            make_face()
            # Profile area: 0.0917673048, perimeter: 1.2255463936
            with BuildLine():
                Line((2.0111773306, 2.5844499688), (2.2398367172, 2.8057439516))
                CenterArc((2.1271403052, 2.8776083303), 0.1336599049, -32.5248902878, 161.0753555839)
                Line((1.860915448, 2.7469458237), (2.0438429572, 2.9821383356))
                CenterArc((1.8083441185, 2.5476100618), 0.2061516205, 10.2942206326, 64.931427869)
            make_face()
            # Profile area: 0.037792762, perimeter: 0.8946715192
            with BuildLine():
                Line((1.904999977, 2.9971999638), (1.739899979, 2.7682916507))
                Line((1.574799981, 2.9971999638), (1.904999977, 2.9971999638))
                Line((1.739899979, 2.7682916507), (1.574799981, 2.9971999638))
            make_face()
            # Profile area: 0.0668431665, perimeter: 0.9165020473
            with Locations((1.7302529413, 2.4954204984)):
                Circle(0.1458658312)
            # Profile area: 0.0356089062, perimeter: 0.8607357853
            with BuildLine():
                Line((1.4740955232, 2.5018999698), (1.2191999853, 2.6415999681))
                Line((1.2191999853, 2.6415999681), (1.2191999853, 2.3621999715))
                Line((1.2191999853, 2.3621999715), (1.4740955232, 2.5018999698))
            make_face()
            # Profile area: 0.0810996121, perimeter: 1.1401009257
            with BuildLine():
                Line((1.2696676055, 2.2275623598), (1.4740955232, 2.3908904931))
                CenterArc((1.3471038531, 2.1306401056), 0.1240576311, 128.6231828981, 183.1377262778)
                Line((1.4297291761, 2.0381017252), (1.6093901227, 2.2536948612))
                CenterArc((1.6646312914, 2.4434783584), 0.197659714, -164.5704968378, 58.3415567993)
            make_face()
            # Profile area: 0.0567740786, perimeter: 1.0973546886
            with BuildLine():
                Line((1.7525999788, 2.2605999727), (1.5493999813, 1.9811999761))
                Line((1.5493999813, 1.9811999761), (1.9557999764, 1.9811999761))
                Line((1.9557999764, 1.9811999761), (1.7525999788, 2.2605999727))
            make_face()
            # Profile area: 0.0797847409, perimeter: 1.1960879565
            with BuildLine():
                Line((1.862337066, 2.2856196402), (2.0667088959, 2.0119692239))
                CenterArc((2.1051502325, 2.1543697056), 0.1474979103, -105.1070274364, 129.1638478852)
                Line((1.9801764999, 2.3979893294), (2.2398367172, 2.2144961092))
                CenterArc((1.8952695266, 2.3690567055), 0.0897011195, -111.5390609778, 130.355950728)
            make_face()
            # Profile area: 0.0396019263, perimeter: 0.9125876779
            with BuildLine():
                Line((2.0207336689, 2.5018999698), (2.2605999727, 2.3367999718))
                Line((2.2605999727, 2.3367999718), (2.2605999727, 2.6669999678))
                Line((2.2605999727, 2.6669999678), (2.0207336689, 2.5018999698))
            make_face()
            # Profile area: 0.6992429015, perimeter: 7.2186770943
            with BuildLine():
                Line((4.4450001419, 1.4862985209), (3.4290001094, 1.4862985209))
                Line((4.4450001419, 2.7157557786), (4.4450001419, 1.4862985209))
                Line((5.2070001662, 2.7157557786), (4.4450001419, 2.7157557786))
                Line((5.2070001662, 2.9210000932), (5.2070001662, 2.7157557786))
                Line((4.232839385, 2.9210000932), (5.2070001662, 2.9210000932))
                Line((4.232839385, 1.6986964525), (4.232839385, 2.9210000932))
                Line((3.6038147415, 1.6986964525), (4.232839385, 1.6986964525))
                Line((3.6038147415, 2.098984862), (3.6038147415, 1.6986964525))
                Line((3.4363471416, 2.098984862), (3.6038147415, 2.098984862))
                Line((3.4290001094, 1.4862985209), (3.4363471416, 2.098984862))
            make_face()
            # Profile area: 0.0159564809, perimeter: 0.8620828823
            with BuildLine():
                Line((5.2069999371, 2.3875999711), (5.2069999371, 2.0915480064))
                Line((5.0144721485, 2.3875999711), (5.2069999371, 2.3875999711))
                CenterArc((4.8831149642, 2.0915480064), 0.3238849729, 0, 66.0733121721)
            make_face()
            # Profile area: 0.0767543625, perimeter: 1.1795334076
            with BuildLine():
                CenterArc((4.8314924729, 2.2468206603), 0.1239562508, 68.5609189518, 141.6755728064)
                Line((5.0037999395, 1.9811999761), (4.7243999429, 2.1843999736))
                CenterArc((5.0926999385, 1.9938999759), 0.0898025601, 81.8698976458, 106.2602047083)
                Line((5.1053999383, 2.0827999748), (4.8767999411, 2.3621999715))
            make_face()
            # Profile area: 0.0316147841, perimeter: 0.8112294491
            with BuildLine():
                Line((4.9686470968, 1.8754054598), (4.7243999429, 2.0065999757))
                Line((4.7243999429, 2.0065999757), (4.7309414215, 1.7442109438))
                Line((4.7309414215, 1.7442109438), (4.9686470968, 1.8754054598))
            make_face()
            # Profile area: 0.0273510165, perimeter: 0.6946554814
            with BuildLine():
                CenterArc((5.2196999369, 1.8668999774), 0.1402760832, 95.1944289077, 169.6111421845)
                Line((5.2069999371, 2.0065999757), (5.2069999371, 1.7271999791))
            make_face()
            # Profile area: 0.0869497428, perimeter: 1.1927420495
            with BuildLine():
                Line((4.9783999398, 1.7525999788), (4.7243999429, 1.5493999813))
                CenterArc((4.873064647, 1.514288217), 0.1527548043, 166.7113458652, 124.2054579381)
                Line((5.130799938, 1.6255999804), (4.9275999404, 1.3715999834))
                CenterArc((5.14632216, 1.7991666449), 0.1742593654, -164.5007246235, 69.3903070625)
            make_face()
            # Profile area: 0.0174332393, perimeter: 0.7470997677
            with BuildLine():
                Line((5.2069999371, 1.3461999837), (5.0291999392, 1.3461999837))
                Line((5.2069999371, 1.6001999807), (5.2069999371, 1.3461999837))
                CenterArc((4.7309414215, 1.7442109438), 0.4973639188, -53.1531147085, 36.3221890199)
            make_face()
        # OneSide extrude, distance=0.508
        extrude(amount=0.508)
    return part.part


# Description: This is a rectangular box or container with an open top, featuring a trapezoidal or angled cross-section with beveled/chamfered edges on the front left corner and a flat base design.
def model_126068_f94ff813_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 18 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 66.9453978405, perimeter: 32.9553746421
            with BuildLine():
                CenterArc((-4.768554635, -2.3671119832), 0.7, 180, 90)
                Line((-4.768554635, -3.0671119832), (4.727295177, -3.0671119832))
                CenterArc((4.727295177, -2.3671119832), 0.7, -90, 90)
                Line((5.427295177, -2.3671119832), (5.427295177, 2.4156106684))
                CenterArc((4.727295177, 2.4156106684), 0.7, 0, 90)
                Line((4.727295177, 3.1156106684), (-4.768554635, 3.1156106684))
                CenterArc((-4.768554635, 2.4156106684), 0.7, 90, 90)
                Line((-5.468554635, 2.4156106684), (-5.468554635, -2.3671119832))
            make_face()
        # Symmetric extrude, each_side=11
        extrude(amount=11, both=True)
    return part.part


# Description: This is a rectangular base plate or platform with a stepped/tiered perimeter, featuring a curved or domed upper surface with multiple internal ribs and a segmented bottom profile with protruding rectangular pads or feet.
def model_126165_6f6c3719_0002():
    """Model: project v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 23 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 54.6, perimeter: 36
            with BuildLine():
                Line((5.6, 0), (5.6, 0.5))
                Line((5.6, 0.5), (4.2, 0.5))
                Line((4.2, 0.5), (4.2, 0))
                Line((2.8, 0), (4.2, 0))
                Line((2.8, 0.5), (2.8, 0))
                Line((1.4, 0.5), (2.8, 0.5))
                Line((1.4, 0), (1.4, 0.5))
                Line((0, 0), (1.4, 0))
                Line((0, -1.4), (0, 0))
                Line((0, -1.4), (-0.5, -1.4))
                Line((-0.5, -1.4), (-0.5, -2.8))
                Line((-0.5, -2.8), (0, -2.8))
                Line((0, -4.2), (0, -2.8))
                Line((-0.5, -4.2), (0, -4.2))
                Line((-0.5, -5.6), (-0.5, -4.2))
                Line((0, -5.6), (-0.5, -5.6))
                Line((0, -7), (0, -5.6))
                Line((1.4, -7), (0, -7))
                Line((1.4, -7.5), (1.4, -7))
                Line((2.8, -7.5), (1.4, -7.5))
                Line((2.8, -7), (2.8, -7.5))
                Line((4.2, -7), (2.8, -7))
                Line((4.2, -7.5), (4.2, -7))
                Line((5.6, -7.5), (4.2, -7.5))
                Line((5.6, -7), (5.6, -7.5))
                Line((7, -7), (5.6, -7))
                Line((7, -5.6), (7, -7))
                Line((7.5, -5.6), (7, -5.6))
                Line((7.5, -4.2), (7.5, -5.6))
                Line((7, -4.2), (7.5, -4.2))
                Line((7, -2.8), (7, -4.2))
                Line((7.5, -2.8), (7, -2.8))
                Line((7.5, -1.4), (7.5, -2.8))
                Line((7, -1.4), (7.5, -1.4))
                Line((7, 0), (7, -1.4))
                Line((5.6, 0), (7, 0))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a sheet metal or composite structural component with an elongated, wedge-like profile featuring a large flat top surface, tapered ends, integral ribbing/reinforcement webbing, and a recessed or stepped underside for lightweight structural support.
def model_126165_6f6c3719_0003():
    """Model: project v5 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 14 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 119.5999816666, perimeter: 53.9999971926
            with BuildLine():
                Line((0, 0), (0.0000005776, -1.3999970037))
                Line((0.5000012159, -1.3999971557), (0.0000005776, -1.3999970037))
                Line((0.5000007904, -2.7999971557), (0.5000012159, -1.3999971557))
                Line((0.0000007904, -2.7999970037), (0.5000007904, -2.7999971557))
                Line((0.0000003648, -4.1999970037), (0.0000007904, -2.7999970037))
                Line((0.5000010031, -4.1999971557), (0.0000003648, -4.1999970037))
                Line((0.5000005776, -5.5999971557), (0.5000010031, -4.1999971557))
                Line((0.0000005776, -5.5999970037), (0.5000005776, -5.5999971557))
                Line((0.000000152, -6.9999970037), (0.0000005776, -5.5999970037))
                Line((10.200000152, -7.0000001043), (0.000000152, -6.9999970037))
                Line((10.200000152, -7.0000001043), (10.2, -7.5))
                Line((13.6, -7.5), (10.2, -7.5))
                Line((13.6, -7), (13.6, -7.5))
                Line((17, -7), (13.6, -7))
                Line((17, -7), (17, -6.1000000909))
                Line((17, -5.6), (17, -6.1000000909))
                Line((16.5000002459, -5.6), (17, -5.6))
                Line((16.5000002459, -4.2), (16.5000002459, -5.6))
                Line((17, -4.2), (16.5000002459, -4.2))
                Line((17, -2.8), (17, -4.2))
                Line((16.5000002459, -2.8), (17, -2.8))
                Line((16.5000002459, -1.4), (16.5000002459, -2.8))
                Line((17, -1.4), (16.5000002459, -1.4))
                Line((17, 0), (17, -1.4))
                Line((6.8, 0), (17, 0))
                Line((6.8, 0.5), (6.8, 0))
                Line((3.4, 0.5), (6.8, 0.5))
                Line((3.4, 0), (3.4, 0.5))
                Line((0, 0), (3.4, 0))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is an elliptical disc or membrane structure with a curved, bowl-like profile featuring radial internal ribs or reinforcement struts that extend from the center to the perimeter, and a thickened outer rim or flange for structural support.
def model_126770_0f5a87bf_0001():
    """Model: Sword v6_Medallion v5"""
    with BuildPart() as part:
        # Sketch3 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.4009182797, perimeter: 11.9694680102
            Circle(1.905)
        # OneSide extrude, distance=-0.3175
        extrude(amount=-0.3175)
    return part.part


# Description: This is a blue plastic bracket or mount assembly with an angular, asymmetrical design featuring two upright wings/flanges and a central base platform with cutouts and slots for fastening or component integration.
def model_126913_541882ae_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 17 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 56.1351925148, perimeter: 55.724185268
            with BuildLine():
                Line((15.8197603583, 6.9436578518), (15.8197603583, 2.9436578518))
                CenterArc((13.8197603583, 6.9436578518), 2, 0, 180)
                Line((11.8197603583, 2.9436578518), (11.8197603583, 6.9436578518))
                CenterArc((11.3197603583, 2.9436578518), 0.5, -90, 90)
                Line((11.3197603583, 2.4436578518), (5.7254250535, 2.4436578518))
                CenterArc((5.7254277387, 4.4436578518), 2, -135, 44.9999230755)
                Line((4.3112141763, 3.0294442894), (1.3970006139, 5.9436578518))
                Line((1.3970006139, 5.9436578518), (0.3197603583, 4.8998410903))
                Line((0.3197603583, 4.8998410903), (3.5638228999, 1.5519021698))
                CenterArc((5.0001432408, 2.9436578518), 2, -135.9027888698, 45.9027888698)
                Line((20.3197603583, 0.9436578518), (5.0001432408, 0.9436578518))
                Line((20.3197603583, 2.4436578518), (20.3197603583, 0.9436578518))
                Line((20.3197603583, 2.4436578518), (16.3197603583, 2.4436578518))
                CenterArc((16.3197603583, 2.9436578518), 0.5, 180, 90)
            make_face()
        # Symmetric extrude, each_side=2
        extrude(amount=2, both=True)
    return part.part


# Description: This is a complex organic-shaped bracket or connector with a curved, asymmetrical form featuring multiple triangulated surface panels, internal voids/cutouts, and ribbed reinforcement structures along its edges.
def model_126913_54ffe782_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 44 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 178.1328022429, perimeter: 106.9631564879
            with BuildLine():
                CenterArc((0, 0), 11, 180, 71.4510003866)
                CenterArc((-3.3402132856, -9.9545454545), 0.5, -108.5489996134, 91.1693828056)
                CenterArc((0, -11), 3, 17.3796168078, 145.2407663844)
                CenterArc((3.3402132856, -9.9545454545), 0.5, -162.6203831922, 91.1693828056)
                CenterArc((0, 0), 11, -71.4510003866, 71.4510003866)
                Line((11, 0), (8, 2))
                Line((8, 2), (4, 3.5))
                Line((4, 3.5), (0, 4))
                Line((-4, 3.5), (0, 4))
                Line((-8, 2), (-4, 3.5))
                Line((-11, 0), (-8, 2))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.0002724783, -6.3560983), 2, 11.5369590328, 156.9260819344)
                CenterArc((-2.4492172645, -5.8560983), 0.5, -90, 78.4630409672)
                Line((-6.4997275217, -6.3560983), (-2.4492172645, -6.3560983))
                CenterArc((-6.4997275217, -5.8560983), 0.5, 180, 90)
                Line((-6.9997275217, -2.8560983), (-6.9997275217, -5.8560983))
                CenterArc((-6.4997275217, -2.8560983), 0.5, 90, 90)
                Line((6.5002724783, -2.3560983), (-6.4997275217, -2.3560983))
                CenterArc((6.5002724783, -2.8560983), 0.5, 0, 90)
                Line((7.0002724783, -5.8560983), (7.0002724783, -2.8560983))
                CenterArc((6.5002724783, -5.8560983), 0.5, -90, 90)
                Line((2.4497622211, -6.3560983), (6.5002724783, -6.3560983))
                CenterArc((2.4497622211, -5.8560983), 0.5, -168.4630409672, 78.4630409672)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3
        extrude(amount=3)
    return part.part


# Description: This is a rectangular flat tray or pan with a shallow depth, featuring a slightly beveled or tapered perimeter edge and a recessed interior surface with subtle ribbing or reinforcement features.
def model_127024_3b28566f_0002():
    """Model: Wall"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 18 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 20.23, perimeter: 36.8
            with BuildLine():
                Line((-8.6, 0.19), (-8.6, -0.19))
                Line((-8.6, -0.19), (-8.35, -0.19))
                Line((-8.35, -0.6), (-8.35, -0.19))
                Line((8.35, -0.6), (-8.35, -0.6))
                Line((8.35, -0.19), (8.35, -0.6))
                Line((8.6, -0.19), (8.35, -0.19))
                Line((8.6, 0.19), (8.6, -0.19))
                Line((8.35, 0.19), (8.6, 0.19))
                Line((8.35, 0.6), (8.35, 0.19))
                Line((-8.35, 0.6), (8.35, 0.6))
                Line((-8.35, 0.19), (-8.35, 0.6))
                Line((-8.35, 0.19), (-8.6, 0.19))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


# Description: This is a pen or stylus tool with an elongated cylindrical shaft and a circular loop or eye at the base, featuring a tapered pointed tip at the opposite end.
def model_127094_e79e6db8_0001():
    """Model: 短針"""
    with BuildPart() as part:
        # Sketch1 -> 押し出し1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 15 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1535462123, perimeter: 1.913222955
            with BuildLine():
                Line((0.25, -0.0000000033), (0.25, -0.4330127019))
                CenterArc((0, 0), 0.5, -60, 120)
                Line((0.25, 0.4330127019), (0.25, -0.0000000033))
            make_face()
            # Profile area: 1.8686789837, perimeter: 8.4858919025
            with BuildLine():
                Line((0.25, 4.05), (0.25, 0.4330127019))
                CenterArc((0.05, 4.05), 0.2, 0, 90)
                Line((-0.05, 4.25), (0.05, 4.25))
                CenterArc((-0.05, 4.05), 0.2, 90, 90)
                Line((-0.25, 0.4330127019), (-0.25, 4.05))
                CenterArc((0, 0), 0.5, 60, 60)
            make_face()
            # Profile area: 0.1535462123, perimeter: 1.913222955
            with BuildLine():
                Line((-0.25, -0.000000002), (-0.25, 0.4330127019))
                CenterArc((0, 0), 0.5, 120, 120)
                Line((-0.25, -0.4330127019), (-0.25, -0.000000002))
            make_face()
            # Profile area: 0.1358471306, perimeter: 1.6575733718
            with BuildLine():
                Line((-0.25, -0.75), (-0.25, -0.4330127019))
                Line((-0.25, -0.75), (0.25, -0.75))
                Line((0.25, -0.4330127019), (0.25, -0.75))
                CenterArc((0, 0), 0.5, -120, 60)
            make_face()
            # Profile area: 0.1409780989, perimeter: 2.1750223512
            with BuildLine():
                CenterArc((0, 0), 0.25, -0.000000746, 180.000000746)
                Line((0.25, 0.4330127019), (0.25, -0.0000000033))
                CenterArc((0, 0), 0.5, 60, 60)
                Line((-0.25, -0.000000002), (-0.25, 0.4330127019))
            make_face()
            # Profile area: 0.1409780989, perimeter: 2.1750223324
            with BuildLine():
                Line((-0.25, -0.4330127019), (-0.25, -0.000000002))
                CenterArc((0, 0), 0.5, -120, 60)
                Line((0.25, -0.0000000033), (0.25, -0.4330127019))
                CenterArc((0, 0), 0.25, -179.9999995511, 179.9999988051)
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a stylus or pen tool featuring a long, tapered cylindrical shaft with a narrow, pointed tip and a circular hole or opening near the base for attachment or mounting purposes.
def model_127094_e79e6db8_0002():
    """Model: 長針"""
    with BuildPart() as part:
        # Sketch1 -> 押し出し1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 13 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1647673042, perimeter: 1.9667408167
            with BuildLine():
                Line((-0.2335484253, 0.0891915525), (-0.2265589104, 0.4457253191))
                CenterArc((0, 0), 0.5, 116.9438967513, 123.8660326247)
                Line((-0.2438541871, -0.4365033052), (-0.2368646721, -0.0799695385))
                CenterArc((0, 0), 0.25, 159.0982698034, 39.5572865204)
            make_face()
            # Profile area: 0.1338991037, perimeter: 1.6365767023
            with BuildLine():
                CenterArc((0, 0), 0.5, -119.190070624, 58.3801412481)
                Line((-0.25, -0.75), (-0.2438541871, -0.4365033052))
                Line((-0.25, -0.75), (0.25, -0.75))
                Line((0.25, -0.75), (0.2438541871, -0.4365033052))
            make_face()
            # Profile area: 1.7798190189, perimeter: 11.2332998717
            with BuildLine():
                Line((0.2265589104, 0.4457253191), (0.1249759869, 5.6274500387))
                CenterArc((0, 5.625), 0.125, 178.8769130636, 182.2461738727)
                Line((-0.2265589104, 0.4457253191), (-0.1249759869, 5.6274500387))
                CenterArc((0, 0), 0.5, 63.0561032487, 53.8877935026)
            make_face()
            # Profile area: 0.1647673042, perimeter: 1.9667408167
            with BuildLine():
                CenterArc((0, 0), 0.25, -18.6555563239, 39.5572865204)
                Line((0.2438541871, -0.4365033052), (0.2368646721, -0.0799695385))
                CenterArc((0, 0), 0.5, -60.809929376, 123.8660326247)
                Line((0.2335484253, 0.0891915525), (0.2265589104, 0.4457253191))
            make_face()
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            with BuildLine():
                CenterArc((0, 5.625), 0.125, 178.8769130636, 182.2461738727)
                CenterArc((0, 5.625), 0.125, 1.1230869364, 177.7538261273)
            make_face()
            # Profile area: 0.1260817137, perimeter: 1.7864604125
            with BuildLine():
                Line((0.2335484253, 0.0891915525), (0.2265589104, 0.4457253191))
                CenterArc((0, 0), 0.5, 63.0561032487, 53.8877935026)
                Line((-0.2335484253, 0.0891915525), (-0.2265589104, 0.4457253191))
                CenterArc((0, 0), 0.25, 20.9017301966, 138.1965396068)
            make_face()
            # Profile area: 0.1334323005, perimeter: 1.845265107
            with BuildLine():
                CenterArc((0, 0), 0.25, -161.3444436761, 142.6888873523)
                Line((-0.2438541871, -0.4365033052), (-0.2368646721, -0.0799695385))
                CenterArc((0, 0), 0.5, -119.190070624, 58.3801412481)
                Line((0.2438541871, -0.4365033052), (0.2368646721, -0.0799695385))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a stylus or pointer tool with an elongated, tapered cylindrical shaft and a small rounded knob or grip feature at the base.
def model_127094_e79e6db8_0003():
    """Model: 秒針"""
    with BuildPart() as part:
        # Sketch1 -> 押し出し1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.3083491182, perimeter: 13.0325165118
            with BuildLine():
                CenterArc((0, 0), 0.5, 65.1814937384, 49.6370125233)
                Line((0, 6.75), (0.2098726342, 0.4538209751))
                Line((-0.2098726342, 0.4538209751), (0, 6.75))
            make_face()
            # Profile area: 0.1288160418, perimeter: 1.7504739423
            with BuildLine():
                Line((-0.2396279208, -0.4388376233), (-0.2283892556, -0.1016776669))
                CenterArc((0, 0), 0.5, -118.6368111276, 57.2736222553)
                Line((0.2283892556, -0.1016776669), (0.2396279208, -0.4388376233))
                CenterArc((0, 0), 0.25, -156.001629124, 132.0032582481)
            make_face()
            # Profile area: 0.1719559562, perimeter: 2.0050909035
            with BuildLine():
                Line((-0.2211112994, 0.1166610187), (-0.2098726342, 0.4538209751))
                CenterArc((0, 0), 0.5, 114.8185062616, 126.5446826107)
                Line((-0.2396279208, -0.4388376233), (-0.2283892556, -0.1016776669))
                CenterArc((0, 0), 0.25, 152.183324258, 51.8150466179)
            make_face()
            # Profile area: 0.1719559562, perimeter: 2.0050909035
            with BuildLine():
                Line((0.2283892556, -0.1016776669), (0.2396279208, -0.4388376233))
                CenterArc((0, 0), 0.5, -61.3631888724, 126.5446826107)
                Line((0.2098726342, 0.4538209751), (0.2211112994, 0.1166610187))
                CenterArc((0, 0), 0.25, -23.998370876, 51.8150466179)
            make_face()
            # Profile area: 0.1163206683, perimeter: 1.6505109547
            with BuildLine():
                CenterArc((0, 0), 0.25, 27.816675742, 124.3666485161)
                Line((0.2098726342, 0.4538209751), (0.2211112994, 0.1166610187))
                CenterArc((0, 0), 0.5, 65.1814937384, 49.6370125233)
                Line((-0.2211112994, 0.1166610187), (-0.2098726342, 0.4538209751))
            make_face()
            # Profile area: 0.1325598744, perimeter: 1.6224770349
            with BuildLine():
                Line((-0.25, -0.75), (-0.2396279208, -0.4388376233))
                Line((-0.25, -0.75), (0.25, -0.75))
                Line((0.2396279208, -0.4388376233), (0.25, -0.75))
                CenterArc((0, 0), 0.5, -118.6368111276, 57.2736222553)
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a hexagonal or elongated prismatic solid with a faceted, angular geometry featuring multiple planar surfaces in varying shades, representing a compact geometric block with no apparent holes, slots, or curved surfaces.
def model_127181_c2f406bf_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> 押し出し1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4.2963583722, perimeter: 8.3093365422
            with BuildLine():
                Line((2.1791055485, -2.2150248708), (0.2394621482, -2.2150248708))
                Line((2.1791055485, 0), (2.1791055485, -2.2150248708))
                Line((0.2394621482, 0), (2.1791055485, 0))
                Line((0.2394621482, -2.2150248708), (0.2394621482, 0))
            make_face()
        # OneSide extrude, distance=4
        extrude(amount=4)
    return part.part


# Description: This is a flat parallelogram-shaped plate or panel with a trapezoidal appearance, featuring a simple planar geometry with no holes, slots, or additional features—just a basic four-sided flat component.
def model_127291_07a17648_0000():
    """Model: Kundenkarten_Vorlage v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 46.17, perimeter: 27.9
            with BuildLine():
                Line((-4.275, 2.7), (4.275, 2.7))
                Line((-4.275, -2.7), (-4.275, 2.7))
                Line((4.275, -2.7), (-4.275, -2.7))
                Line((4.275, 2.7), (4.275, -2.7))
            make_face()
        # OneSide extrude, distance=0.09
        extrude(amount=0.09)
    return part.part


# Description: This is a flat, thin-walled parallelogram or trapezoidal plate with a slightly beveled or chamfered edge along one side, featuring a simple geometric form with no holes or complex features.
def model_127453_23b625e6_0001():
    """Model: Table Top"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 122.4418082134, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 31.048325, perimeter: 22.86
            with BuildLine():
                Line((-55.3194806753, 57.15), (-55.3194806753, 52.705))
                Line((-55.3194806753, 52.705), (-48.3344806753, 52.705))
                Line((-48.3344806753, 52.705), (-48.3344806753, 57.15))
                Line((-48.3344806753, 57.15), (-55.3194806753, 57.15))
            make_face()
            # Profile area: 3307.654675, perimeter: 231.14
            with BuildLine():
                Line((-55.3194806753, 57.15), (-106.7544806753, 57.15))
                Line((-106.7544806753, 57.15), (-106.7544806753, 0))
                Line((-106.7544806753, 0), (-48.3344806753, 0))
                Line((-48.3344806753, 0), (-48.3344806753, 52.705))
                Line((-55.3194806753, 52.705), (-48.3344806753, 52.705))
                Line((-55.3194806753, 57.15), (-55.3194806753, 52.705))
            make_face()
        # OneSide extrude, distance=3.81
        extrude(amount=3.81)
    return part.part


# Description: This is a rectangular prism or beam with a long, slender cylindrical or prismatic shape, featuring a smooth exterior surface and what appears to be a subtle central groove or seam running along its length.
def model_127453_23b625e6_0003():
    """Model: rIGHTlEG"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1185.4815, perimeter: 267.97
            with BuildLine():
                Line((-56.776473782, 2.796252251), (-66.301473782, 2.796252251))
                Line((-56.776473782, 127.256252251), (-56.776473782, 2.796252251))
                Line((-66.301473782, 127.256252251), (-56.776473782, 127.256252251))
                Line((-66.301473782, 2.796252251), (-66.301473782, 127.256252251))
            make_face()
        # OneSide extrude, distance=9.525
        extrude(amount=9.525)
    return part.part


# Description: This is a cylindrical rod or shaft with a tapered end, featuring a smooth, elongated body with a slightly beveled or pointed tip at one end.
def model_127453_23b625e6_0005():
    """Model: TopRail"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 9.525), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 36.29025, perimeter: 26.67
            with BuildLine():
                Line((-59.6591470648, 117.731252251), (-63.4691470648, 117.731252251))
                Line((-59.6591470648, 127.256252251), (-59.6591470648, 117.731252251))
                Line((-63.4691470648, 127.256252251), (-59.6591470648, 127.256252251))
                Line((-63.4691470648, 117.731252251), (-63.4691470648, 127.256252251))
            make_face()
        # OneSide extrude, distance=203.2
        extrude(amount=203.2)
    return part.part


# Description: This is a tapered cylindrical pin or punch with a pointed tip, featuring a smooth conical surface that gradually reduces in diameter from a thicker end to a sharp point.
def model_127453_23b625e6_0006():
    """Model: TopHB"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 127.256252251, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1599.9968, perimeter: 901.7
            with BuildLine():
                Line((56.3873534524, 226.695), (56.3873534524, -6.985))
                Line((56.3873534524, -6.985), (66.5473534524, -6.985))
                Line((66.5473534524, -6.985), (66.5473534524, 226.695))
                Line((66.5473534524, 226.695), (56.3873534524, 226.695))
            make_face()
            with BuildLine():
                Line((63.4691470648, 212.725), (59.6591470648, 212.725))
                Line((63.4691470648, 9.525), (63.4691470648, 212.725))
                Line((59.6591470648, 9.525), (63.4691470648, 9.525))
                Line((59.6591470648, 212.725), (59.6591470648, 9.525))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 774.192, perimeter: 414.02
            with BuildLine():
                Line((59.6591470648, 212.725), (59.6591470648, 9.525))
                Line((59.6591470648, 9.525), (63.4691470648, 9.525))
                Line((63.4691470648, 9.525), (63.4691470648, 212.725))
                Line((63.4691470648, 212.725), (59.6591470648, 212.725))
            make_face()
        # OneSide extrude, distance=3.81
        extrude(amount=3.81)
    return part.part


# Description: This is a hexagonal metal rod or shaft with a tapered, pointed tip, featuring a uniform cross-section along its length and a conical end.
def model_127453_23b625e6_0009():
    """Model: LeftFront"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 57.15), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 488.8031732407, perimeter: 158.2060366651
            with BuildLine():
                Line((51.8269806753, 48.7818082134), (55.3194806753, 63.5058893927))
                Line((55.3194806753, 122.4418082134), (55.3194806753, 63.5058893927))
                Line((48.3344806753, 122.4418082134), (55.3194806753, 122.4418082134))
                Line((48.3344806753, 48.7818082134), (48.3344806753, 122.4418082134))
                Line((51.8269806753, 48.7818082134), (48.3344806753, 48.7818082134))
            make_face()
        # OneSide extrude, distance=4.445
        extrude(amount=4.445)
    return part.part


# Description: This is a cylindrical shaft or rod with a tapered end, featuring a uniform diameter body that gradually narrows to a pointed tip, commonly used as a drill bit, punch, or similar precision tool.
def model_127453_75e818dd_0002():
    """Model: TopRail"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 9.525), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 36.29025, perimeter: 26.67
            with BuildLine():
                Line((-59.6591470648, 117.731252251), (-63.4691470648, 117.731252251))
                Line((-59.6591470648, 127.256252251), (-59.6591470648, 117.731252251))
                Line((-63.4691470648, 127.256252251), (-59.6591470648, 127.256252251))
                Line((-63.4691470648, 117.731252251), (-63.4691470648, 127.256252251))
            make_face()
        # OneSide extrude, distance=185.42
        extrude(amount=185.42)
    return part.part


# Description: This is a tapered cylindrical pin or punch with a pointed end, featuring a slightly conical shape that gradually narrows from a larger diameter at one end to a sharp point at the opposite end.
def model_127453_75e818dd_0003():
    """Model: TopHB"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 127.256252251, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1512.9002, perimeter: 835.66
            with BuildLine():
                Line((56.3873534524, 211.455), (56.3873534524, -6.985))
                Line((56.3873534524, -6.985), (66.5473534524, -6.985))
                Line((66.5473534524, -6.985), (66.5473534524, 211.455))
                Line((66.5473534524, 211.455), (56.3873534524, 211.455))
            make_face()
            with BuildLine():
                Line((63.4691470648, 194.945), (59.6591470648, 194.945))
                Line((63.4691470648, 9.525), (63.4691470648, 194.945))
                Line((59.6591470648, 9.525), (63.4691470648, 9.525))
                Line((59.6591470648, 194.945), (59.6591470648, 9.525))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 706.4502, perimeter: 378.46
            with BuildLine():
                Line((59.6591470648, 194.945), (59.6591470648, 9.525))
                Line((59.6591470648, 9.525), (63.4691470648, 9.525))
                Line((63.4691470648, 9.525), (63.4691470648, 194.945))
                Line((63.4691470648, 194.945), (59.6591470648, 194.945))
            make_face()
        # OneSide extrude, distance=3.81
        extrude(amount=3.81)
    return part.part


# Description: This is a curved composite housing or shroud with an organic, rounded shape featuring a flat rectangular top opening, a dark curved body, and an integrated internal web or partition structure visible through the translucent top section.
def model_127552_761bd9bf_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 8.64, perimeter: 12
            with BuildLine():
                Line((-1.2, 1.8), (-1.2, -1.8))
                Line((-1.2, -1.8), (1.2, -1.8))
                Line((1.2, -1.8), (1.2, 1.8))
                Line((1.2, 1.8), (-1.2, 1.8))
            make_face()
            # Profile area: 5.0893800988, perimeter: 9.2548667765
            with BuildLine():
                Line((1.2, -1.8), (1.2, 1.8))
                CenterArc((1.2, 0), 1.8, -90, 180)
            make_face()
        # OneSide extrude, distance=1.4
        extrude(amount=1.4)
    return part.part


# Description: This is a jet ski or personal watercraft hull featuring a streamlined, hydrodynamic design with curved sides, a central operator seating area, dual intake vents, and a tapered rear section for water propulsion.
def model_127552_bf0db7a9_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 40 constraints, 14 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 175.3666687816, perimeter: 108.3657936853
            with BuildLine():
                CenterArc((0, 0), 11, 105.6749595262, 72.0206991642)
                CenterArc((-10.4915091903, 0.422178766), 0.5, 177.6956586904, 58.6142737837)
                Line((-10.7688592884, 0.0061536188), (-8.0467369311, -1.8085946193))
                CenterArc((-7.769386833, -1.3925694722), 0.5, -123.690067526, 13.1340223064)
                Line((-7.9449485538, -1.860734061), (-4.053960679, -3.319854514))
                CenterArc((-3.8783989582, -2.8516899252), 0.5, -110.5560452196, 13.4289901512)
                Line((-3.9404339793, -3.3478266565), (0, -3.8405233053))
                Line((3.8585438501, -3.4028942434), (0, -3.8405233053))
                CenterArc((3.8021960172, -2.9060794674), 0.5, -83.5292676395, 12.4062791404)
                Line((7.9411094753, -2.0192886935), (3.9639649167, -3.3791870906))
                CenterArc((7.7793405758, -1.5461810702), 0.5, -71.1229884991, 14.8130560251)
                Line((10.7739965201, -0.1506689866), (8.0566906739, -1.9622062174))
                CenterArc((10.496646422, 0.2653561606), 0.5, -56.309932474, 57.7580664657)
                CenterArc((0, 0), 11, 1.4481339917, 72.8769064821)
                CenterArc((0, 11), 3, -172.1625202369, 164.3250404738)
            make_face()
            with BuildLine():
                CenterArc((0, 7), 2, 180, 180)
                Line((2, 7), (7, 7))
                Line((7, 7), (7, 3))
                Line((7, 3), (-7, 3))
                Line((-7, 3), (-7, 7))
                Line((-7, 7), (-2, 7))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a rectangular prism or box-shaped structural component with a long, slender profile featuring parallel top and bottom faces and four vertical sides, appearing to be a solid extrusion without any visible holes, slots, or curved features.
def model_127559_7042a2ea_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 16, perimeter: 16
            with BuildLine():
                Line((0, 4), (0, 0))
                Line((0, 0), (4, 0))
                Line((4, 0), (4, 4))
                Line((4, 4), (0, 4))
            make_face()
        # OneSide extrude, distance=12
        extrude(amount=12)
    return part.part


# Description: This is a rectangular enclosure or housing with a trapezoidal profile, featuring an angled top surface, ventilation slots or mesh patterns on the interior surfaces, and a tapered geometric design that narrows toward one end.
def model_128043_287dadde_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6696758629, perimeter: 5.0348979419
            with BuildLine():
                Line((0.0690598923, -0.5732050808), (0.5309401077, -0.2267949192))
                Line((0.5309401077, -0.2267949192), (0.4618802154, 0.3464101615))
                Line((0.4618802154, 0.3464101615), (-0.0690598923, 0.5732050808))
                Line((-0.0690598923, 0.5732050808), (-0.5309401077, 0.2267949192))
                Line((-0.5309401077, 0.2267949192), (-0.4618802154, -0.3464101615))
                Line((-0.4618802154, -0.3464101615), (0.0690598923, -0.5732050808))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is a toroidal (doughnut-shaped) component featuring a smooth, curved surface with a central hollow opening and a fine mesh or textured finish on the outer surface.
def model_128043_9f2ba9d9_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2120575041, perimeter: 2.8274333882
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)
    return part.part


# Description: This is a toroidal (doughnut-shaped) ring or torus with a hollow center, featuring a textured or mesh-patterned surface on the outer portion and a smooth dark band running along the inner equator.
def model_128043_e5d0f07d_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1884955592, perimeter: 3.7699111843
            with BuildLine():
                CenterArc((0, 0), 0.35, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)
    return part.part


# Description: This is a cylindrical barrel or sleeve with a curved, tapered body, an open top with a beveled or angled edge, and vertical ribbing or fluting along its outer surface for structural reinforcement.
def model_128125_374010e8_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.3747577333, perimeter: 21.5984494934
            with BuildLine():
                CenterArc((0, 0), 1.875, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.5625, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3.5
        extrude(amount=3.5)
    return part.part


# Description: This is a flat parallelogram or skewed rectangular plate with a simple planar form and beveled or chamfered edges, featuring no holes, slots, or other cutouts.
def model_128355_739c5ce0_0002():
    """Model: TV"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 12 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 76), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 8575, perimeter: 432
            with BuildLine():
                Line((152, 100), (28, 100))
                Line((152, 170), (152, 100))
                Line((28, 170), (152, 170))
                Line((28, 100), (28, 170))
            make_face()
            with BuildLine():
                Line((97.5, 117), (82.5, 117))
                Line((97.5, 110), (97.5, 117))
                Line((82.5, 110), (97.5, 110))
                Line((82.5, 117), (82.5, 110))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 105, perimeter: 44
            with BuildLine():
                Line((82.5, 117), (82.5, 110))
                Line((82.5, 110), (97.5, 110))
                Line((97.5, 110), (97.5, 117))
                Line((97.5, 117), (82.5, 117))
            make_face()
        # OneSide extrude, distance=-5
        extrude(amount=-5)
    return part.part


# Description: This is a flat parallelogram-shaped plate or panel with a slight 3D depth, featuring clean edges and a simple geometric form typical of a spacer, shim, or structural bracket component.
def model_128441_b3d88d7a_0004():
    """Model: Component1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 160, perimeter: 56
            with BuildLine():
                Line((20, -8), (0, -8))
                Line((20, 0), (20, -8))
                Line((0, 0), (20, 0))
                Line((0, -8), (0, 0))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a hexagonal prism or box-shaped component with an irregular polygonal base, featuring triangulated faceted surfaces on the top and sides, suggesting a complex geometric form with multiple angled planes and internal structural geometry.
def model_128644_1d6d3ec5_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 20.2846707977, perimeter: 18.5912404558
            with BuildLine():
                Line((0.2043797721, 3.5), (0.2043797721, 0))
                Line((0.2043797721, 0), (6, 0))
                Line((6, 0), (6, 3.5))
                Line((6, 3.5), (0.2043797721, 3.5))
            make_face()
        # OneSide extrude, distance=3.5
        extrude(amount=3.5)
    return part.part


# Description: This is a cylindrical sleeve or tube with an elliptical or oval-shaped opening at the top and vertical ribbing or fluting along its outer surface.
def model_128656_22e204c6_0003():
    """Model: gasket v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 32.9174421312, perimeter: 46.0529130176
            with BuildLine():
                CenterArc((0, 0), 4.3795487505, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.95, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=8.5
        extrude(amount=8.5)
    return part.part


# Description: This is a cylindrical rod or shaft with a uniform circular cross-section, featuring a smooth, tapered or slightly beveled end and a straight elongated body.
def model_128996_1eb0ac1b_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=14
        extrude(amount=14)
    return part.part


# Description: This is a cylindrical rod or shaft with a simple, uniform circular cross-section and a straight, slightly tapered or rounded end, commonly used as a mechanical component or fastener.
def model_128996_2777de76_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=10.65
        extrude(amount=10.65)
    return part.part


# Description: This is a cylindrical tube or pipe with a uniform hollow circular cross-section, featuring slightly rounded edges at both ends and a smooth, tapered finish.
def model_128996_2c8d17d0_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            Circle(0.35)
        # OneSide extrude, distance=5.3
        extrude(amount=5.3)
    return part.part


# Description: This is a cylindrical band or ring with a meshed or perforated upper half and a solid lower half, featuring an oval or elliptical cross-section with a hollow center.
def model_128996_33b0bbe4_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.8246680716, perimeter: 6.5973445725
            with BuildLine():
                CenterArc((0, 0), 0.65, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)
    return part.part


# Description: This is a cylindrical shaft or axle with rounded ends (capsule shape) featuring two circular flanges or enlarged sections on opposite sides and a central longitudinal slot or groove running along its length.
def model_128996_36204ae8_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.9738937226, perimeter: 19.4778744523
            with BuildLine():
                CenterArc((0, 0), 1.6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=7.6
        extrude(amount=7.6)
    return part.part


# Description: This is a long, tapered structural beam or duct with a rectangular cross-section that angles downward from left to right, featuring a flange or mounting bracket at the upper left end and a reinforced corner joint at the lower right terminus.
def model_128996_4317ea15_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.1599999718, perimeter: 10.2
            with BuildLine():
                Line((0, 0), (0, -3.3))
                Line((0, -3.3), (1.2, -3.3))
                Line((1.2, -3.3), (1.2, -3.1500000469))
                Line((1.2, -3.1500000469), (0.6, -3.1500000469))
                Line((0.6, -3.1500000469), (0.6, -0.15))
                Line((1.2, -0.15), (0.6, -0.15))
                Line((1.2, 0), (1.2, -0.15))
                Line((0, 0), (1.2, 0))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: This is a cylindrical sleeve or tube with a closed top end, open bottom end, and a vertical slot or seam running along its length, designed as a container or housing component.
def model_128996_59392a72_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7461282552, perimeter: 5.9690260418
            with BuildLine():
                CenterArc((0, 0), 0.6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.35, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.9
        extrude(amount=2.9)
    return part.part


# Description: This is a cylindrical tube or pipe with a slightly tapered or beveled top edge and a smooth, uniform dark gray finish throughout its length.
def model_128996_5ded6c77_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6361725124, perimeter: 2.8274333882
            Circle(0.45)
        # OneSide extrude, distance=3.9
        extrude(amount=3.9)
    return part.part


# Description: This is a simple cylindrical rod or shaft with a uniform circular cross-section, tapered or rounded ends, and a slight diagonal orientation.
def model_128996_60143a1e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.5393804003, perimeter: 4.398229715
            Circle(0.7)
        # OneSide extrude, distance=15.2
        extrude(amount=15.2)
    return part.part


# Description: This is a toroidal (doughnut-shaped) rubber or elastomer ring with a uniform cross-section, featuring a smooth outer surface and an open central hole, commonly used as a seal, gasket, or drive belt.
def model_128996_724a7354_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 115.4535300194, perimeter: 153.9380400259
            with BuildLine():
                CenterArc((0, 0), 13, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 11.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a cylindrical rod or shaft with a slightly tapered or rounded end, appearing to be a solid, elongated component with uniform diameter along most of its length.
def model_128996_77b982d9_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            Circle(0.35)
        # OneSide extrude, distance=8.1
        extrude(amount=8.1)
    return part.part


# Description: This is a dark gray cylindrical tube or sleeve with a slightly tapered or rounded end cap, featuring a smooth, uniform bore along its length and a subtle textured surface finish.
def model_128996_7a37ea05_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            Circle(0.35)
        # OneSide extrude, distance=4
        extrude(amount=4)
    return part.part


# Description: This is a timing belt or drive belt with a circular ring shape, featuring regularly-spaced parallel teeth or ridges on its inner and outer surfaces for grip and power transmission.
def model_128996_85889997_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.8613936473, perimeter: 24.8185819634
            with BuildLine():
                CenterArc((0, 0), 2.05, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.9, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)
    return part.part


# Description: This is a cylindrical mesh or perforated sleeve with an open top and bottom, featuring a solid outer wall and a latticed or grid-patterned upper rim.
def model_128996_8f2877c4_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.9032078879, perimeter: 7.2256631033
            with BuildLine():
                CenterArc((0, 0), 0.7, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.45, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.9
        extrude(amount=1.9)
    return part.part


# Description: This is a cylindrical pipe or tube with a uniform hollow core, featuring a slightly tapered or rounded top end and a clean cylindrical body, commonly used as a connector or spacer component in mechanical assemblies.
def model_128996_a58117a3_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=2.9
        extrude(amount=2.9)
    return part.part


MODELS = {
    "model_118269_fa4b08d7_0002": {"func": model_118269_fa4b08d7_0002, "volume": 0.8710373515, "area": 13.7813826089},
    "model_118427_e6d67c63_0001": {"func": model_118427_e6d67c63_0001, "volume": 12750, "area": 17660},
    "model_118427_e6d67c63_0002": {"func": model_118427_e6d67c63_0002, "volume": 20400, "area": 27950},
    "model_118437_904c2ed5_0000": {"func": model_118437_904c2ed5_0000, "volume": 27.4164749075, "area": 90.9172262396},
    "model_118440_90bbb605_0003": {"func": model_118440_90bbb605_0003, "volume": 1.8210795425, "area": 19.0885570063},
    "model_118618_1255e091_0000": {"func": model_118618_1255e091_0000, "volume": 0.7068141502, "area": 9.3991148575},
    "model_118626_c1782d20_0000": {"func": model_118626_c1782d20_0000, "volume": 0.6969305338, "area": 6.1423080616},
    "model_118626_c1782d20_0001": {"func": model_118626_c1782d20_0001, "volume": 0.5745333154, "area": 5.2778651023},
    "model_118626_c1782d20_0003": {"func": model_118626_c1782d20_0003, "volume": 3.8644558221, "area": 17.6886456207},
    "model_118626_c1782d20_0004": {"func": model_118626_c1782d20_0004, "volume": 1.8210795425, "area": 19.0885570063},
    "model_119054_4e1076ec_0000": {"func": model_119054_4e1076ec_0000, "volume": 6487.7668025291, "area": 2886.4207172928},
    "model_119054_4e1076ec_0022": {"func": model_119054_4e1076ec_0022, "volume": 2.2416245331, "area": 34.0587913557},
    "model_119054_4e1076ec_0027": {"func": model_119054_4e1076ec_0027, "volume": 340.55, "area": 2004.45},
    "model_119054_4e1076ec_0029": {"func": model_119054_4e1076ec_0029, "volume": 1275.8793164392, "area": 946.3890789307},
    "model_119054_4e1076ec_0039": {"func": model_119054_4e1076ec_0039, "volume": 7.4251566035, "area": 40.3752541883},
    "model_119054_4e1076ec_0040": {"func": model_119054_4e1076ec_0040, "volume": 184.08, "area": 979.49},
    "model_119465_4fad1b4f_0001": {"func": model_119465_4fad1b4f_0001, "volume": 26.5071880147, "area": 74.2201264411},
    "model_119465_4fad1b4f_0002": {"func": model_119465_4fad1b4f_0002, "volume": 0.8609922608, "area": 8.0619329269},
    "model_119553_c436b288_0009": {"func": model_119553_c436b288_0009, "volume": 0.129590697, "area": 1.9006635554},
    "model_119553_c436b288_0011": {"func": model_119553_c436b288_0011, "volume": 2.2534120683, "area": 22.0709665481},
    "model_119553_c436b288_0012": {"func": model_119553_c436b288_0012, "volume": 0.9282002529, "area": 9.33451838},
    "model_119553_c436b288_0013": {"func": model_119553_c436b288_0013, "volume": 0.6992402529, "area": 7.29931838},
    "model_119787_9a55dfa9_0001": {"func": model_119787_9a55dfa9_0001, "volume": 75.6, "area": 453},
    "model_119787_9a55dfa9_0003": {"func": model_119787_9a55dfa9_0003, "volume": 40.08, "area": 205.36},
    "model_119790_1ed376f0_0005": {"func": model_119790_1ed376f0_0005, "volume": 0.2536349121, "area": 3.9161523223},
    "model_119870_fcffae11_0000": {"func": model_119870_fcffae11_0000, "volume": 2.9827111522, "area": 36.7069992598},
    "model_119915_a858f82a_0000": {"func": model_119915_a858f82a_0000, "volume": 27.86430161, "area": 139.2762752535},
    "model_119921_5621fcb4_0000": {"func": model_119921_5621fcb4_0000, "volume": 307.8760800518, "area": 252.898208614},
    "model_120371_433ba1ca_0001": {"func": model_120371_433ba1ca_0001, "volume": 8.9460347336, "area": 48.2912293235},
    "model_120371_433ba1ca_0002": {"func": model_120371_433ba1ca_0002, "volume": 25.9805082018, "area": 115.3632387965},
    "model_120454_c30d2e80_0000": {"func": model_120454_c30d2e80_0000, "volume": 1.6333734521, "area": 40.9517626975},
    "model_120535_e304dfca_0002": {"func": model_120535_e304dfca_0002, "volume": 71.4581506825, "area": 140.3173189774},
    "model_120539_4492fbcd_0000": {"func": model_120539_4492fbcd_0000, "volume": 0.0008565922, "area": 0.16},
    "model_120700_d818883a_0005": {"func": model_120700_d818883a_0005, "volume": 75.6, "area": 453},
    "model_120700_d818883a_0007": {"func": model_120700_d818883a_0007, "volume": 0.4861166964, "area": 5.352477808},
    "model_120800_6ee246cf_0001": {"func": model_120800_6ee246cf_0001, "volume": 3518.4019065672, "area": 2626.5233020692},
    "model_120806_77995027_0001": {"func": model_120806_77995027_0001, "volume": 3.1296521104, "area": 26.4730193447},
    "model_120806_77995027_0002": {"func": model_120806_77995027_0002, "volume": 35.6884925448, "area": 447.5336965115},
    "model_121184_3075d4dc_0000": {"func": model_121184_3075d4dc_0000, "volume": 6.4951286523, "area": 47.8225545518},
    "model_121467_899f0850_0002": {"func": model_121467_899f0850_0002, "volume": 69.6438055098, "area": 150.2831853072},
    "model_121469_bb776055_0000": {"func": model_121469_bb776055_0000, "volume": 223.1951870692, "area": 336.1251325024},
    "model_121620_4a6e845d_0001": {"func": model_121620_4a6e845d_0001, "volume": 0.0977569386, "area": 1.2026016678},
    "model_121703_69c4a5ac_0000": {"func": model_121703_69c4a5ac_0000, "volume": 22500, "area": 10450},
    "model_121869_67b34d49_0002": {"func": model_121869_67b34d49_0002, "volume": 5.382, "area": 25.85},
    "model_122100_a32b6fdf_0000": {"func": model_122100_a32b6fdf_0000, "volume": 11.0492009755, "area": 67.9827030978},
    "model_122105_21cb0a9e_0000": {"func": model_122105_21cb0a9e_0000, "volume": 13.032, "area": 44.516},
    "model_122105_21cb0a9e_0004": {"func": model_122105_21cb0a9e_0004, "volume": 14.3, "area": 56.86},
    "model_122258_c3076cb0_0000": {"func": model_122258_c3076cb0_0000, "volume": 6.8705503434, "area": 50.893028162},
    "model_122260_c9bddd6a_0000": {"func": model_122260_c9bddd6a_0000, "volume": 0.0647848466, "area": 2.341583477},
    "model_122328_4d8636de_0000": {"func": model_122328_4d8636de_0000, "volume": 737.4178578502, "area": 535.4827875977},
    "model_122423_9ab69fbb_0001": {"func": model_122423_9ab69fbb_0001, "volume": 2.319646805, "area": 12.045431217},
    "model_122423_9ab69fbb_0002": {"func": model_122423_9ab69fbb_0002, "volume": 1.0863274123, "area": 8.4019467106},
    "model_122424_d612248e_0000": {"func": model_122424_d612248e_0000, "volume": 6819.694963927, "area": 5077.9504284839},
    "model_122425_248c57e8_0001": {"func": model_122425_248c57e8_0001, "volume": 16.4745118754, "area": 55.2763227399},
    "model_122491_52380ecd_0000": {"func": model_122491_52380ecd_0000, "volume": 3.7442932324, "area": 15.4809774414},
    "model_122491_52380ecd_0001": {"func": model_122491_52380ecd_0001, "volume": 4.0000000075, "area": 18.0000000298},
    "model_122491_52380ecd_0002": {"func": model_122491_52380ecd_0002, "volume": 5, "area": 22},
    "model_122515_758d8b70_0002": {"func": model_122515_758d8b70_0002, "volume": 103.125, "area": 250.8273797371},
    "model_122515_758d8b70_0004": {"func": model_122515_758d8b70_0004, "volume": 6300, "area": 5555},
    "model_122515_758d8b70_0009": {"func": model_122515_758d8b70_0009, "volume": 44.1786466911, "area": 80.5033117482},
    "model_122515_758d8b70_0011": {"func": model_122515_758d8b70_0011, "volume": 15.8336269741, "area": 110.8353888186},
    "model_122587_febb5971_0000": {"func": model_122587_febb5971_0000, "volume": 0.6031857895, "area": 7.037167544},
    "model_122587_febb5971_0002": {"func": model_122587_febb5971_0002, "volume": 0.1649336143, "area": 2.9688050576},
    "model_122750_8f5f5638_0000": {"func": model_122750_8f5f5638_0000, "volume": 55.0723723526, "area": 165.6043417981},
    "model_122895_39b17a39_0000": {"func": model_122895_39b17a39_0000, "volume": 3375, "area": 1350},
    "model_122904_9ac95090_0000": {"func": model_122904_9ac95090_0000, "volume": 890.8905233872, "area": 895.4048382055},
    "model_123016_29f35476_0000": {"func": model_123016_29f35476_0000, "volume": 3308.8, "area": 4829.76},
    "model_123331_28a27457_0000": {"func": model_123331_28a27457_0000, "volume": 712.6116251033, "area": 783.7931471351},
    "model_123332_eb7b0c9a_0000": {"func": model_123332_eb7b0c9a_0000, "volume": 279.530488428, "area": 391.1861799419},
    "model_123495_0999be98_0000": {"func": model_123495_0999be98_0000, "volume": 40, "area": 76},
    "model_123496_74cb10dc_0015": {"func": model_123496_74cb10dc_0015, "volume": 1.9376250554, "area": 14.5892457407},
    "model_123754_6d71ab4f_0000": {"func": model_123754_6d71ab4f_0000, "volume": 171.9866262918, "area": 195.1701003949},
    "model_123770_de9989d1_0000": {"func": model_123770_de9989d1_0000, "volume": 0.01481875, "area": 0.43555},
    "model_123770_de9989d1_0001": {"func": model_123770_de9989d1_0001, "volume": 0.00475136, "area": 0.305152},
    "model_123865_f6dff61e_0000": {"func": model_123865_f6dff61e_0000, "volume": 7.6931327412, "area": 84.0226548246},
    "model_123944_ccfed065_0001": {"func": model_123944_ccfed065_0001, "volume": 2, "area": 12},
    "model_124415_4db8a722_0000": {"func": model_124415_4db8a722_0000, "volume": 1294.3688120313, "area": 1060.9419710342},
    "model_124497_5c00f42d_0003": {"func": model_124497_5c00f42d_0003, "volume": 0.8798104471, "area": 13.3010713263},
    "model_124497_5c00f42d_0011": {"func": model_124497_5c00f42d_0011, "volume": 3.164902002, "area": 19.9452630118},
    "model_124804_18e77ffd_0001": {"func": model_124804_18e77ffd_0001, "volume": 337.5, "area": 300},
    "model_125153_a3c60b19_0001": {"func": model_125153_a3c60b19_0001, "volume": 26.747519404, "area": 77.0004350737},
    "model_125416_ab456bc3_0000": {"func": model_125416_ab456bc3_0000, "volume": 142.6859212659, "area": 784.8451707874},
    "model_125428_e6d291da_0002": {"func": model_125428_e6d291da_0002, "volume": 594.4678698755, "area": 1403.0352790932},
    "model_125428_e6d291da_0003": {"func": model_125428_e6d291da_0003, "volume": 209.9086547423, "area": 1176.6546257496},
    "model_125591_12eac82b_0000": {"func": model_125591_12eac82b_0000, "volume": 2000, "area": 1000},
    "model_125594_799c122a_0005": {"func": model_125594_799c122a_0005, "volume": 4.43625, "area": 20.735},
    "model_125745_cf468448_0000": {"func": model_125745_cf468448_0000, "volume": 6.325509791, "area": 99.5678914137},
    "model_126068_f94ff813_0000": {"func": model_126068_f94ff813_0000, "volume": 1472.7987524918, "area": 858.9090378071},
    "model_126165_6f6c3719_0002": {"func": model_126165_6f6c3719_0002, "volume": 27.3, "area": 127.2},
    "model_126165_6f6c3719_0003": {"func": model_126165_6f6c3719_0003, "volume": 59.7999908333, "area": 266.1999619296},
    "model_126770_0f5a87bf_0001": {"func": model_126770_0f5a87bf_0001, "volume": 3.6197915538, "area": 26.6021426526},
    "model_126913_541882ae_0000": {"func": model_126913_541882ae_0000, "volume": 224.5407700593, "area": 335.1671261015},
    "model_126913_54ffe782_0000": {"func": model_126913_54ffe782_0000, "volume": 534.3984067288, "area": 677.1550739496},
    "model_127024_3b28566f_0002": {"func": model_127024_3b28566f_0002, "volume": 101.15, "area": 224.46},
    "model_127094_e79e6db8_0001": {"func": model_127094_e79e6db8_0001, "volume": 0.2593574737, "area": 6.463295389},
    "model_127094_e79e6db8_0002": {"func": model_127094_e79e6db8_0002, "volume": 0.255185413, "area": 6.6650102272},
    "model_127094_e79e6db8_0003": {"func": model_127094_e79e6db8_0003, "volume": 0.2029957615, "area": 5.8100592248},
    "model_127181_c2f406bf_0000": {"func": model_127181_c2f406bf_0000, "volume": 17.1854334887, "area": 41.8300629132},
    "model_127291_07a17648_0000": {"func": model_127291_07a17648_0000, "volume": 4.1553, "area": 94.851},
    "model_127453_23b625e6_0001": {"func": model_127453_23b625e6_0001, "volume": 12720.45843, "area": 7558.0494},
    "model_127453_23b625e6_0003": {"func": model_127453_23b625e6_0003, "volume": 11291.7112875, "area": 4923.37725},
    "model_127453_23b625e6_0005": {"func": model_127453_23b625e6_0005, "volume": 7374.1788, "area": 5491.9245},
    "model_127453_23b625e6_0006": {"func": model_127453_23b625e6_0006, "volume": 9045.659328, "area": 6606.4384},
    "model_127453_23b625e6_0009": {"func": model_127453_23b625e6_0009, "volume": 2172.730105055, "area": 1680.8321794578},
    "model_127453_75e818dd_0002": {"func": model_127453_75e818dd_0002, "volume": 6728.938155, "area": 5017.7319},
    "model_127453_75e818dd_0003": {"func": model_127453_75e818dd_0003, "volume": 8455.725024, "area": 6180.6328},
    "model_127552_761bd9bf_0000": {"func": model_127552_761bd9bf_0000, "volume": 19.2211321383, "area": 47.1355736847},
    "model_127552_bf0db7a9_0000": {"func": model_127552_bf0db7a9_0000, "volume": 87.6833343908, "area": 404.9162344057},
    "model_127559_7042a2ea_0000": {"func": model_127559_7042a2ea_0000, "volume": 192, "area": 224},
    "model_128043_287dadde_0000": {"func": model_128043_287dadde_0000, "volume": 0.1339351726, "area": 2.3463313143},
    "model_128043_9f2ba9d9_0000": {"func": model_128043_9f2ba9d9_0000, "volume": 0.0106028752, "area": 0.5654866776},
    "model_128043_e5d0f07d_0000": {"func": model_128043_e5d0f07d_0000, "volume": 0.009424778, "area": 0.5654866776},
    "model_128125_374010e8_0000": {"func": model_128125_374010e8_0000, "volume": 11.8116520667, "area": 82.3440886937},
    "model_128355_739c5ce0_0002": {"func": model_128355_739c5ce0_0002, "volume": 43400, "area": 19300},
    "model_128441_b3d88d7a_0004": {"func": model_128441_b3d88d7a_0004, "volume": 80, "area": 348},
    "model_128644_1d6d3ec5_0000": {"func": model_128644_1d6d3ec5_0000, "volume": 70.996347792, "area": 105.6386831909},
    "model_128656_22e204c6_0003": {"func": model_128656_22e204c6_0003, "volume": 279.7982581154, "area": 457.2846449118},
    "model_128996_1eb0ac1b_0000": {"func": model_128996_1eb0ac1b_0000, "volume": 1.759291886, "area": 17.8442462724},
    "model_128996_2777de76_0000": {"func": model_128996_2777de76_0000, "volume": 1.3383184704, "area": 13.6345121166},
    "model_128996_2c8d17d0_0000": {"func": model_128996_2c8d17d0_0000, "volume": 2.0396790303, "area": 12.4249989449},
    "model_128996_33b0bbe4_0000": {"func": model_128996_33b0bbe4_0000, "volume": 0.3298672286, "area": 4.2882739722},
    "model_128996_36204ae8_0000": {"func": model_128996_36204ae8_0000, "volume": 7.4015922919, "area": 149.9796332824},
    "model_128996_4317ea15_0000": {"func": model_128996_4317ea15_0000, "volume": 0.6479999916, "area": 7.3799999437},
    "model_128996_59392a72_0000": {"func": model_128996_59392a72_0000, "volume": 2.1637719402, "area": 18.8024320317},
    "model_128996_5ded6c77_0000": {"func": model_128996_5ded6c77_0000, "volume": 2.4810727982, "area": 12.2993352388},
    "model_128996_60143a1e_0000": {"func": model_128996_60143a1e_0000, "volume": 23.3985820839, "area": 69.9318524689},
    "model_128996_724a7354_0000": {"func": model_128996_724a7354_0000, "volume": 230.9070600388, "area": 538.7831400906},
    "model_128996_77b982d9_0000": {"func": model_128996_77b982d9_0000, "volume": 3.1172453105, "area": 18.582520546},
    "model_128996_7a37ea05_0000": {"func": model_128996_7a37ea05_0000, "volume": 1.5393804003, "area": 9.5661496302},
    "model_128996_85889997_0000": {"func": model_128996_85889997_0000, "volume": 1.4891149178, "area": 23.5776528652},
    "model_128996_8f2877c4_0000": {"func": model_128996_8f2877c4_0000, "volume": 1.716094987, "area": 15.535175672},
    "model_128996_a58117a3_0000": {"func": model_128996_a58117a3_0000, "volume": 0.3644247478, "area": 3.8955748905},
}

if __name__ == "__main__":
    import time
    from build123d import export_step
    
    passed = 0
    failed = 0
    errors = []
    
    for name, info in MODELS.items():
        t0 = time.time()
        try:
            result = info["func"]()
            vol_err = abs(result.volume - info["volume"]) / max(info["volume"], 1e-10)
            area_err = abs(result.area - info["area"]) / max(info["area"], 1e-10)
            dt = time.time() - t0
            if vol_err < 0.01 and area_err < 0.01:
                print(f"  PASS  {name} ({dt:.1f}s)")
                passed += 1
            else:
                print(f"  FAIL  {name} vol_err={vol_err:.4%} area_err={area_err:.4%} ({dt:.1f}s)")
                failed += 1
                errors.append(name)
        except Exception as e:
            dt = time.time() - t0
            print(f"  ERROR {name}: {e} ({dt:.1f}s)")
            failed += 1
            errors.append(name)
    
    print(f"\nResults: {passed} passed, {failed} failed out of {len(MODELS)}")
    if errors:
        print(f"Failed: {errors}")
