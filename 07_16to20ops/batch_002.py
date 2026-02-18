"""Batch 002 - passing/07_16to20ops
33 models bundled from Fusion360 Gallery reconstructions.
"""

from build123d import *


def model_24372_03b260fe_0009():
    """Model: construction3 v8"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 64, perimeter: 32
            with BuildLine():
                Line((5, -5), (-3, -5))
                Line((5, 3), (5, -5))
                Line((-3, 3), (5, 3))
                Line((-3, -5), (-3, 3))
            make_face()
        # OneSide extrude, distance=130
        extrude(amount=130)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 48, perimeter: 28
            with BuildLine():
                Line((122, -5), (122, -11))
                Line((122, -11), (130, -11))
                Line((130, -11), (130, -5))
                Line((122, -5), (130, -5))
            make_face()
            # Profile area: 64, perimeter: 32
            with BuildLine():
                Line((122, -5), (130, -5))
                Line((130, -5), (130, 3))
                Line((130, 3), (122, 3))
                Line((122, 3), (122, -5))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -5), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 64, perimeter: 32
            with BuildLine():
                Line((-122, 3), (-122, -5))
                Line((-130, 3), (-122, 3))
                Line((-130, -5), (-130, 3))
                Line((-130, -5), (-122, -5))
            make_face()
            # Profile area: 48, perimeter: 28
            with BuildLine():
                Line((-130, -5), (-122, -5))
                Line((-130, -11), (-130, -5))
                Line((-122, -11), (-130, -11))
                Line((-122, -5), (-122, -11))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(130, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 14, perimeter: 30
            with BuildLine():
                Line((5, 3), (5, -5))
                Line((5, -5), (5, -11))
                Line((5, -11), (6, -11))
                Line((6, -11), (6, 3))
                Line((6, 3), (5, 3))
            make_face()
            # Profile area: 14, perimeter: 30
            with BuildLine():
                Line((-3, -5), (-3, -11))
                Line((-3, 3), (-3, -5))
                Line((-4, 3), (-3, 3))
                Line((-4, -11), (-4, 3))
                Line((-3, -11), (-4, -11))
            make_face()
        # OneSide extrude, distance=8
        extrude(amount=8, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 64, perimeter: 32
            with BuildLine():
                Line((-8, -5), (-8, 3))
                Line((0, -5), (-8, -5))
                Line((0, 3), (0, -5))
                Line((0, 3), (-8, 3))
            make_face()
            # Profile area: 48, perimeter: 28
            with BuildLine():
                Line((0, 3), (-8, 3))
                Line((0, 9), (0, 3))
                Line((-8, 9), (0, 9))
                Line((-8, 3), (-8, 9))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch6 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -5, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 64, perimeter: 32
            with BuildLine():
                Line((0, -5), (0, 3))
                Line((8, -5), (0, -5))
                Line((8, 3), (8, -5))
                Line((8, 3), (0, 3))
            make_face()
            # Profile area: 48, perimeter: 28
            with BuildLine():
                Line((0, 3), (0, 9))
                Line((8, 3), (0, 3))
                Line((8, 9), (8, 3))
                Line((0, 9), (8, 9))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch7 -> Extrude7 (Join)
        # Sketch on BRepFace
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 8, perimeter: 18
            with BuildLine():
                Line((3, 3), (-5, 3))
                Line((3, 4), (3, 3))
                Line((-5, 4), (3, 4))
                Line((-5, 3), (-5, 4))
            make_face()
            # Profile area: 8, perimeter: 18
            with BuildLine():
                Line((3, -6), (3, -5))
                Line((3, -5), (-5, -5))
                Line((-5, -5), (-5, -6))
                Line((-5, -6), (3, -6))
            make_face()
        # OneSide extrude, distance=8
        extrude(amount=8, mode=Mode.ADD)

        # Sketch8 -> Extrude8 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -6, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 48, perimeter: 28
            with BuildLine():
                Line((0, 9), (0, 3))
                Line((0, 3), (8, 3))
                Line((8, 3), (8, 9))
                Line((8, 9), (0, 9))
            make_face()
        # OneSide extrude, distance=-10
        extrude(amount=-10, mode=Mode.SUBTRACT)

        # Sketch10 -> Extrude9 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((59.6697989167, -1.1852345329)):
                Circle(1)
        # OneSide extrude, distance=-8
        extrude(amount=-8, mode=Mode.SUBTRACT)
    return part.part


def model_24907_c72322ea_0000():
    """Model: Handle_Second element v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2733971007, perimeter: 1.8535396656
            Circle(0.295)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.8575762546, perimeter: 5.6234508499
            with BuildLine():
                CenterArc((0, 0), 0.6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.295, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2733971007, perimeter: 1.8535396656
            Circle(0.295)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.6), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.9503317777, perimeter: 3.4557519189
            Circle(0.55)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.8), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 3.5735616435, perimeter: 10.9955742876
            with BuildLine():
                CenterArc((0, 0), 1.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.55, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.9503317777, perimeter: 3.4557519189
            Circle(0.55)
        # OneSide extrude, distance=1.05
        extrude(amount=1.05, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -1.85), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 3.4636059006, perimeter: 6.5973445725
            Circle(1.05)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -1.65), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # OneSide extrude, distance=-0.6
        extrude(amount=-0.6, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -1.05), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=-0.25
        extrude(amount=-0.25, mode=Mode.SUBTRACT)

        # Sketch8 -> Extrude8 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.8), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=-1.6
        extrude(amount=-1.6, mode=Mode.SUBTRACT)
    return part.part


def model_25199_39e3c0d3_0000():
    """Model: Part 41 - Main Shaft v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 12 constraints, 21 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.1343159949, perimeter: 8.8145269952
            with BuildLine():
                Line((0.9, 0.7), (1.55, 0.7))
                Line((1.55, 0.7), (1.55, 1.13))
                Line((1.55, 1.13), (0.7265022236, 1.8209966804))
                Line((0.7265022236, 1.8209966804), (0.0765022236, 1.8209966804))
                Line((0.0765022236, 1.8209966804), (-0.4597288865, 1.3710453536))
                Line((-0.4597288865, 1.3710453536), (-0.8847288865, 1.3710453536))
                Line((-0.8847288865, 1.3710453536), (-1.4909466692, 1.0210453536))
                Line((-1.4909466692, 1.0210453536), (-1.4909466692, 0.5710453536))
                Line((-1.4909466692, 0.5710453536), (-1.1, 0))
                Line((0, 0), (-1.1, 0))
                Line((0, 0), (0, 0.7))
                CenterArc((0.3, 0.7), 0.3, 90, 90)
                Line((0.3, 1), (0.6, 1))
                CenterArc((0.6, 0.7), 0.3, 0, 90)
            make_face()
        # OneSide extrude, distance=0.615
        extrude(amount=0.615)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0981747704, perimeter: 1.2853981634
            with BuildLine():
                CenterArc((-0.25, 0.3075), 0.25, 0, 180)
                Line((0, 0.3075), (-0.5, 0.3075))
            make_face()
            # Profile area: 0.0981747704, perimeter: 1.2853981634
            with BuildLine():
                Line((0, 0.3075), (-0.5, 0.3075))
                CenterArc((-0.25, 0.3075), 0.25, -180, 180)
            make_face()
        # OneSide extrude, distance=9.8
        extrude(amount=9.8, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 22 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.615), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with BuildLine():
                CenterArc((-0.8303926968, 1.067312652), 0.2, 90, 180)
                CenterArc((-0.8303926968, 1.067312652), 0.2, -90, 180)
            make_face()
            # Profile area: 0.4199156545, perimeter: 4.1404664614
            with BuildLine():
                CenterArc((-0.8303926968, 1.067312652), 0.2, -90, 180)
                Line((-0.8303926968, 0.867312652), (-0.1668846172, 0.867312652))
                Line((0.3501494231, 1.2930363677), (-0.1668846172, 0.867312652))
                Line((0.4723380379, 1.2930363677), (0.3501494231, 1.2930363677))
                CenterArc((0.4723417051, 1.4930363677), 0.2, 94.1709485119, 175.8280009096)
                Line((0.457795204, 1.6925066645), (0.286946561, 1.6925066645))
                Line((0.286946561, 1.6925066645), (-0.2197799309, 1.267312652))
                Line((-0.2197799309, 1.267312652), (-0.8303926968, 1.267312652))
            make_face()
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with BuildLine():
                CenterArc((0.4723417051, 1.4930363677), 0.2, 94.1709485119, 175.8280009096)
                CenterArc((0.4723417051, 1.4930363677), 0.2, -90.0010505785, 184.1719990904)
            make_face()
        # OneSide extrude, distance=-0.33
        extrude(amount=-0.33, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 2.6452697306, perimeter: 8.6411684907
            with BuildLine():
                Line((-0.6, 1), (-0.3, 1))
                CenterArc((-0.3, 0.7), 0.3, 0, 90)
                Line((0.5173528466, 0.7000000104), (0, 0.7))
                Line((0.5173528466, 0), (0.5173528466, 0.7000000104))
                Line((0.5173528466, 0), (1.1, 0))
                Line((1.1, 0), (1.2954733346, 0.2855226768))
                Line((1.2954733346, 0.2855226768), (1.2954733175, 1.1339019459))
                Line((1.2954733175, 1.1339019459), (0.8847288865, 1.3710453536))
                Line((0.8847288865, 1.3710453536), (0.4597288865, 1.3710453536))
                Line((0.4597288865, 1.3710453536), (-0.0765022236, 1.8209966804))
                Line((-0.0765022236, 1.8209966804), (-0.7265022236, 1.8209966804))
                Line((-0.7265022236, 1.8209966804), (-1.55, 1.13))
                Line((-1.55, 1.13), (-1.55, 0.7))
                Line((-1.55, 0.7), (-0.9, 0.7))
                CenterArc((-0.6, 0.7), 0.3, 90, 90)
            make_face()
        # OneSide extrude, distance=-0.06
        extrude(amount=-0.06, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.06), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 2.295822068, perimeter: 8.4909136164
            with BuildLine():
                Line((1.2954733346, 0.2855226768), (1.2954733175, 1.1339019459))
                Line((1.2954733175, 1.1339019459), (0.8847288865, 1.3710453536))
                Line((0.8847288865, 1.3710453536), (0.4597288865, 1.3710453536))
                Line((0.4597288865, 1.3710453536), (-0.0765022236, 1.8209966804))
                Line((-0.0765022236, 1.8209966804), (-0.7265022236, 1.8209966804))
                Line((-0.7265022236, 1.8209966804), (-1.55, 1.13))
                Line((-1.55, 1.13), (-1.55, 0.7))
                Line((-1.55, 0.7), (-0.9, 0.7))
                CenterArc((-0.6, 0.7), 0.3, 90, 90)
                Line((-0.6, 1), (-0.3, 1))
                CenterArc((-0.3, 0.7), 0.3, 0, 90)
                Line((0, 0.7), (0.5173528466, 0.7000000104))
                Line((0.5173528466, 0.542708871), (0.5173528466, 0.7000000104))
                Line((0.5173528466, 0.542708871), (1.1673528466, 0.542708871))
                Line((1.1673528466, 0.542708871), (1.1673528466, 0.0983805034))
                Line((1.1673528466, 0.0983805034), (1.2954733346, 0.2855226768))
            make_face()
        # OneSide extrude, distance=-0.05
        extrude(amount=-0.05, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.11), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.4613292176, perimeter: 3.4581476799
            with BuildLine():
                Line((-1.55, 0.7), (-0.9, 0.7))
                CenterArc((-0.6, 0.7), 0.3, 90, 90)
                CenterArc((-0.5762739932, 1.4104084448), 0.4110936815, 130.0002682306, 136.6911042509)
                Line((-1.55, 1.13), (-0.8405213924, 1.725323238))
                Line((-1.55, 1.13), (-1.55, 0.7))
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.06), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0449391933, perimeter: 1.0564324266
            with BuildLine():
                Line((1.1673528466, 0.542708871), (1.2954733294, 0.542708871))
                Line((1.1673528466, 0.2121280161), (1.1673528466, 0.542708871))
                Line((1.1673528466, 0.0983805034), (1.1673528466, 0.2121280161))
                Line((1.2954733346, 0.2855226768), (1.1673528466, 0.0983805034))
                Line((1.2954733294, 0.542708871), (1.2954733346, 0.2855226768))
            make_face()
            # Profile area: 0.0536615145, perimeter: 1.6151829975
            with BuildLine():
                Line((1.077285516, 0.0783873633), (1.1673528466, 0.2121280161))
                Line((0.5173528466, 0.0783873633), (1.077285516, 0.0783873633))
                Line((0.5173528466, 0.0783873633), (0.5173528466, 0))
                Line((1.1, 0), (0.5173528466, 0))
                Line((1.1673528466, 0.0983805034), (1.1, 0))
                Line((1.1673528466, 0.0983805034), (1.1673528466, 0.2121280161))
            make_face()
        # OneSide extrude, distance=-0.45
        extrude(amount=-0.45, mode=Mode.SUBTRACT)

        # Sketch8 -> Extrude8 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -9.8, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0706858347, perimeter: 2.8274333882
            with BuildLine():
                CenterArc((-0.25, 0.3075), 0.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-0.25, 0.3075), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-3.35
        extrude(amount=-3.35, mode=Mode.SUBTRACT)

        # Sketch10 -> Extrude10 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -6.45, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0226739875, perimeter: 1.0246231384
            with BuildLine():
                CenterArc((-0.25, 0.3075), 0.2, 126.8698976458, 106.2602047083)
                Line((-0.37, 0.526817122), (-0.37, 0.4675))
                CenterArc((-0.25, 0.3075), 0.25, 118.6854020141, 122.6291959718)
                Line((-0.37, 0.1475), (-0.37, 0.088182878))
            make_face()
            # Profile area: 0.0178918087, perimeter: 0.6909180872
            with BuildLine():
                Line((-0.13, 0.1475), (-0.13, 0.4675))
                CenterArc((-0.25, 0.3075), 0.2, -53.1301023542, 106.2602047083)
            make_face()
            # Profile area: 0.0226739875, perimeter: 1.0246231384
            with BuildLine():
                CenterArc((-0.25, 0.3075), 0.2, -53.1301023542, 106.2602047083)
                Line((-0.13, 0.088182878), (-0.13, 0.1475))
                CenterArc((-0.25, 0.3075), 0.25, -61.3145979859, 122.6291959718)
                Line((-0.13, 0.4675), (-0.13, 0.526817122))
            make_face()
            # Profile area: 0.0178918087, perimeter: 0.6909180872
            with BuildLine():
                CenterArc((-0.25, 0.3075), 0.2, 126.8698976458, 106.2602047083)
                Line((-0.37, 0.4675), (-0.37, 0.1475))
            make_face()
        # OneSide extrude, distance=4
        extrude(amount=4, mode=Mode.SUBTRACT)
    return part.part


def model_25199_b2422c18_0009():
    """Model: Part 1 - Drag knob v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            Circle(1.5)
        # OneSide extrude, distance=1.8
        extrude(amount=1.8)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 5.6159110276, perimeter: 13.6973439697
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.68, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.72
        extrude(amount=-0.72, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.72), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.4771293843, perimeter: 12.723450247
            with BuildLine():
                CenterArc((0, 0), 1.05, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.975, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.08
        extrude(amount=0.08, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.72), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 3.60497757, perimeter: 16.0221225333
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.05, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.55
        extrude(amount=-0.55, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.8), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 2.5941294033, perimeter: 7.2089649545
            with BuildLine():
                Line((-0.45, 0), (-0.25, 0.9682458366))
                Line((-0.25, 1.4790199458), (-0.25, 0.9682458366))
                CenterArc((0, 0), 1.5, 99.5940682269, 160.8118635463)
                Line((-0.25, -0.9682458366), (-0.25, -1.4790199458))
                Line((-0.45, 0), (-0.25, -0.9682458366))
            make_face()
            # Profile area: 2.5941294033, perimeter: 7.2089649545
            with BuildLine():
                CenterArc((0, 0), 1.5, -80.4059317731, 160.8118635463)
                Line((0.25, 1.4790199458), (0.25, 0.9682458366))
                Line((0.45, 0), (0.25, 0.9682458366))
                Line((0.45, 0), (0.25, -0.9682458366))
                Line((0.25, -0.9682458366), (0.25, -1.4790199458))
            make_face()
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.8), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1936491673, perimeter: 3.9138636664
            with BuildLine():
                Line((-0.25, 0.9682458366), (-0.25, -0.9682458366))
                Line((-0.25, 0.9682458366), (-0.45, 0))
                Line((-0.45, 0), (-0.25, -0.9682458366))
            make_face()
            # Profile area: 0.1936491673, perimeter: 3.9138636664
            with BuildLine():
                Line((0.45, 0), (0.25, 0.9682458366))
                Line((0.25, 0.9682458366), (0.25, -0.9682458366))
                Line((0.25, -0.9682458366), (0.45, 0))
            make_face()
        # OneSide extrude, distance=-0.05
        extrude(amount=-0.05, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.4), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.8824054452, perimeter: 4.6136041366
            with BuildLine():
                Line((-0.45, 0), (-0.25, -0.9682458366))
                Line((-0.25, 0.9682458366), (-0.45, 0))
                CenterArc((0, 0), 1, 104.4775121859, 151.0449756281)
            make_face()
            # Profile area: 0.8824054452, perimeter: 4.6136041366
            with BuildLine():
                CenterArc((0, 0), 1, -75.5224878141, 151.0449756281)
                Line((0.25, 0.9682458366), (0.45, 0))
                Line((0.45, 0), (0.25, -0.9682458366))
            make_face()
        # OneSide extrude, distance=-0.05
        extrude(amount=-0.05, mode=Mode.SUBTRACT)

        # Sketch8 -> Extrude8 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.104, perimeter: 1.32
            with BuildLine():
                Line((0.13, -0.2), (0.13, 0.2))
                Line((0.13, 0.2), (-0.13, 0.2))
                Line((-0.13, 0.2), (-0.13, -0.2))
                Line((-0.13, -0.2), (0.13, -0.2))
            make_face()
        # OneSide extrude, distance=-1.6
        extrude(amount=-1.6, mode=Mode.SUBTRACT)

        # Sketch9 -> Extrude9 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.8), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((0, 1.1000000164)):
                Circle(0.05)
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((0, 0.9000000134)):
                Circle(0.05)
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((0, 0.7000000104)):
                Circle(0.05)
        # OneSide extrude, distance=-0.05
        extrude(amount=-0.05, mode=Mode.SUBTRACT)
    return part.part


def model_25199_d7aff7a5_0023():
    """Model: Part 14 - Bail Trip Lever v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.18688, perimeter: 6.9949611571
            with BuildLine():
                Line((0, 0), (3.1, 0))
                Line((3.1, 0), (3.1, 0.482))
                Line((3.1, 0.482), (1.9, 0.482))
                Line((1.22, 0.285), (1.9, 0.482))
                Line((0, 0.285), (1.22, 0.285))
                Line((0, 0), (0, 0.285))
            make_face()
        # OneSide extrude, distance=0.345
        extrude(amount=0.345)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 17 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.482, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1055606223, perimeter: 1.611382384
            with BuildLine():
                Line((-3.6000003928, 0.845), (-3.7750003928, 0.845))
                Line((-3.7750003928, 0.845), (-3.7750003928, 0.3366693989))
                CenterArc((-3.1000003928, 0.845), 0.845, -143.0172410636, 16.7383671887)
                Line((-3.6000003928, 0.845), (-3.6000003928, 0.163806195))
            make_face()
            # Profile area: 0.0875, perimeter: 1.35
            with BuildLine():
                Line((-3.7750003928, 1.345), (-3.7750003928, 0.845))
                Line((-3.6000003928, 0.845), (-3.7750003928, 0.845))
                Line((-3.6000003928, 0.845), (-3.6000003928, 1.345))
                Line((-3.6000003928, 1.345), (-3.7750003928, 1.345))
            make_face()
            # Profile area: 0.2000042906, perimeter: 2.3466347533
            with BuildLine():
                Line((-3.6000003928, 0.845), (-3.6000003928, 0.163806195))
                CenterArc((-3.1000003928, 0.845), 0.845, -126.2788738749, 36.2789005078)
                Line((-3.1, 0.345), (-3.1, 0))
                CenterArc((-3.1000003928, 0.845), 0.5, 180, 90.0000450097)
            make_face()
        # OneSide extrude, distance=-0.481
        extrude(amount=-0.481, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.345), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0146705, perimeter: 1.0268525549
            with BuildLine():
                Line((3.7750003928, 0.001), (3.8360003928, 0.001))
                Line((3.8360003928, 0.001), (3.7750003928, 0.482))
                Line((3.7750003928, 0.001), (3.7750003928, 0.482))
            make_face()
        # OneSide extrude, distance=-1.01
        extrude(amount=-1.01, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 9 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0120025704, perimeter: 0.7992269618
            with BuildLine():
                Line((-0.3, 0.285), (-0.0665582432, 0.2274570057))
                CenterArc((-0.0875, 0.1425), 0.0875, 0, 76.1527427158)
                Line((0, 0.1425), (0, 0.285))
                Line((0, 0.285), (-0.3, 0.285))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 9 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0240528188, perimeter: 0.5497787144
            with BuildLine():
                CenterArc((-0.0875, 0.1425), 0.0875, 0, 76.1527427158)
                CenterArc((-0.0875, 0.1425), 0.0875, 76.1527427158, 207.6945145684)
                CenterArc((-0.0875, 0.1425), 0.0875, -76.1527427158, 76.1527427158)
            make_face()
            # Profile area: 0.0374420404, perimeter: 1.0830420049
            with BuildLine():
                Line((-0.3, 0), (-0.3, 0.285))
                Line((-0.3, 0), (-0.0665582432, 0.0575429943))
                CenterArc((-0.0875, 0.1425), 0.0875, 76.1527427158, 207.6945145684)
                Line((-0.3, 0.285), (-0.0665582432, 0.2274570057))
            make_face()
        # OneSide extrude, distance=0.25
        extrude(amount=0.25, mode=Mode.ADD)

        # Sketch4 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 9 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0120025704, perimeter: 0.7992269618
            with BuildLine():
                CenterArc((-0.0875, 0.1425), 0.0875, -76.1527427158, 76.1527427158)
                Line((-0.3, 0), (-0.0665582432, 0.0575429943))
                Line((0, 0), (-0.3, 0))
                Line((0, 0), (0, 0.1425))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude7 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.25), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0240528188, perimeter: 0.5497787144
            with BuildLine():
                CenterArc((-0.0875, 0.1425), 0.0875, 76.1527427158, 207.6945145684)
                CenterArc((-0.0875, 0.1425), 0.0875, -76.1527427158, 152.3054854316)
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch8 -> Extrude8 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.352981504, perimeter: 3.2394847417
            with BuildLine():
                Line((-2.3, 0.482), (-2.3, 0.132))
                Line((-2.3, 0.132), (-0.945, 0.132))
                Line((-0.945, 0.132), (-0.9464836084, 0.285))
                Line((-0.9464836084, 0.285), (-1.22, 0.285))
                Line((-1.22, 0.285), (-1.9, 0.482))
                Line((-1.9, 0.482), (-2.3, 0.482))
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)

        # Sketch9 -> Extrude9 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0.285, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0513864871, perimeter: 0.8035805137
            with Locations((-0.5984553172, 0.177884483)):
                Circle(0.1278938109)
        # OneSide extrude, distance=-0.02
        extrude(amount=-0.02, mode=Mode.SUBTRACT)

        # Sketch10 -> Extrude10 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0.482, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0485530112, perimeter: 0.7811114727
            with Locations((-2.7448914639, 0.148182248)):
                Circle(0.124317752)
        # OneSide extrude, distance=-0.02
        extrude(amount=-0.02, mode=Mode.SUBTRACT)
    return part.part


def model_26086_bf892d7f_0014():
    """Model: Tractor_Lift_Arm v17 (1)"""
    with BuildPart() as part:
        # Sketch5 -> Extrude44 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 71.2441443234, perimeter: 100.4436479354
            with BuildLine():
                Line((-8.2, 0), (-8.2, -1.5))
                Line((-8.2, -1.5), (-0.0660470564, -1.5))
                Line((-0.0660470564, -1.5), (31.5, 5.7875961849))
                Line((31.5, 5.7875961849), (39.7, 5.7875961849))
                Line((39.7, 5.7875961849), (39.7, 7.2723480205))
                Line((31.5, 7.2723480205), (39.7, 7.2723480205))
                Line((0, 0), (31.5, 7.2723480205))
                Line((-8.2, 0), (0, 0))
            make_face()
        # Symmetric extrude, each_side=3.25
        extrude(amount=3.25, both=True)

        # Sketch36 -> Extrude45 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 10.0584568641, perimeter: 24.9101782567
            with BuildLine():
                CenterArc((4.1000010668, 0), 3.25, -90.0000188069, 180.0000376048)
                Line((4.1, -3.25), (8.2, -3.25))
                Line((8.2, -3.25), (8.2, 3.25))
                Line((8.2, 3.25), (4.1000000005, 3.25))
            make_face()
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((4.1000010668, 0)):
                Circle(1)
        # OneSide extrude, distance=-12.5
        extrude(amount=-12.5, mode=Mode.SUBTRACT)

        # Sketch37 -> Extrude46 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 7.2723480205, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 10.0584601338, perimeter: 24.9101772516
            with BuildLine():
                CenterArc((-35.6000005638, 0), 3.25, 89.9999900611, 180.0000198766)
                Line((-35.6, 3.25), (-39.7, 3.25))
                Line((-39.7, 3.25), (-39.7, -3.25))
                Line((-39.7, -3.25), (-35.6000000001, -3.25))
            make_face()
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)

        # Sketch38 -> Extrude47 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 7.2723480205, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((-35.6000005638, 0)):
                Circle(1)
        # OneSide extrude, distance=-6
        extrude(amount=-6, mode=Mode.SUBTRACT)

        # Sketch38 -> Extrude48 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 7.2723480205, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((-17, 0)):
                Circle(1)
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((-35.6000005638, 0)):
                Circle(1)
        # OneSide extrude, distance=-10
        extrude(amount=-10, mode=Mode.SUBTRACT)

        # Sketch39 -> Extrude49 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 6.479534848, perimeter: 17.2787595947
            with BuildLine():
                CenterArc((4.1000010668, 0), 1.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((4.1000010668, 0), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides extrude, along=0.5, against=-2
        extrude(amount=0.5, mode=Mode.ADD)
        extrude(sk.sketch, amount=-2, mode=Mode.ADD)

        # Sketch40 -> Extrude50 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 7.2723480205, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 6.479534848, perimeter: 17.2787595947
            with BuildLine():
                CenterArc((-35.6000005638, 0), 1.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-35.6000005638, 0), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides extrude, along=0.5, against=-2
        extrude(amount=0.5, mode=Mode.ADD)
        extrude(sk.sketch, amount=-2, mode=Mode.ADD)

        # Sketch41 -> Extrude51 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3.25), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 4.6951414815, perimeter: 9.4603432494
            with BuildLine():
                Line((16.4954302136, 2.3235182997), (16.4954302136, 3.8082701353))
                Line((16.4954302136, 3.8082701353), (13.3331903234, 3.0782095319))
                Line((13.3331903234, 3.0782095319), (13.3331903234, 1.5934576963))
                Line((13.3331903234, 1.5934576963), (16.4954302136, 2.3235182997))
            make_face()
        # OneSide extrude, distance=-11
        extrude(amount=-11, mode=Mode.SUBTRACT)

        # Sketch42 -> Extrude52 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3.25), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 2.9065580576, perimeter: 6.989447033
            with BuildLine():
                Line((18.4567774883, 4.2610828327), (18.4492935325, 2.7746031898))
                Line((16.4954302136, 3.8082701353), (18.4567774883, 4.2610828327))
                Line((16.4954302136, 2.3235182997), (16.4954302136, 3.8082701353))
                Line((18.4492935325, 2.7746031898), (16.4954302136, 2.3235182997))
            make_face()
        # OneSide extrude, distance=-13
        extrude(amount=-13, mode=Mode.SUBTRACT)
    return part.part


def model_28929_50621ea1_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            Circle(0.75)
        # OneSide extrude, distance=-1.7
        extrude(amount=-1.7, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((3.5, 0)):
                Circle(0.5)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-3.5, 0)):
                Circle(0.25)
        # OneSide extrude, distance=-1.1
        extrude(amount=-1.1, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.2841990145, perimeter: 10.6100914535
            with BuildLine():
                CenterArc((0, 0), 1, -72.3945681129, 146.059670617)
                Line((0.302460256, -0.9531619975), (3.5192810758, -0.4996281018))
                CenterArc((3.5, 0), 0.5, 91.6862115676, 180.5237849214)
                Line((0.2812512514, 0.9596341665), (3.4852871522, 0.4997834852))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.3647855113, perimeter: 4.7045425516
            with BuildLine():
                Line((-1.5000000224, -0.5000000075), (-2.9000000432, -0.3000000045))
                CenterArc((-1.6750315283, -0.011087277), 0.5192992259, -70.3025548636, 146.3478546208)
                Line((-2.9000000432, 0.3000000045), (-1.5498000921, 0.4928857118))
                Line((-2.9000000432, -0.3000000045), (-2.9000000432, 0.3000000045))
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude7 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.36, perimeter: 3
            with BuildLine():
                Line((-0.5743037147, -1.0096647743), (-0.5743037147, -1.3096647743))
                Line((-0.5743037147, -1.3096647743), (0.6256962853, -1.3096647743))
                Line((0.6256962853, -1.3096647743), (0.6256962853, -1.0096647743))
                Line((0.6256962853, -1.0096647743), (-0.5743037147, -1.0096647743))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch8 -> Extrude8 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.36, perimeter: 3
            with BuildLine():
                Line((-0.6000000089, 1.3000000149), (-0.6000000089, 1.0000000149))
                Line((-0.6000000089, 1.0000000149), (0.5999999911, 1.0000000149))
                Line((0.5999999911, 1.0000000149), (0.5999999911, 1.3000000149))
                Line((0.5999999911, 1.3000000149), (-0.6000000089, 1.3000000149))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch9 -> Extrude9 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.6000000089, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0176714587, perimeter: 0.471238898
            with Locations((-1.1572159529, 0.25)):
                Circle(0.075)
        # OneSide extrude, distance=-2.5
        extrude(amount=-2.5, mode=Mode.SUBTRACT)

        # Sketch10 -> Extrude10 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.5743037147, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0176714587, perimeter: 0.471238898
            with Locations((1.1591074884, 0.25)):
                Circle(0.075)
        # OneSide extrude, distance=-4.1
        extrude(amount=-4.1, mode=Mode.SUBTRACT)
    return part.part


def model_30426_2cde26de_0028():
    """Model: PortaTavolaSX"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 15 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 7.96, perimeter: 80
            with BuildLine():
                Line((-0.1, 10), (0.1, 10))
                Line((-0.1, -9.8), (-0.1, 10))
                Line((-19.9, -9.8), (-0.1, -9.8))
                Line((-19.9, -10), (-19.9, -9.8))
                Line((0.1, -10), (-19.9, -10))
                Line((0.1, 10), (0.1, -10))
            make_face()
        # Symmetric extrude, each_side=2
        extrude(amount=2, both=True)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -9.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((17.4, 0)):
                Circle(0.2)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((14.9, 0)):
                Circle(0.2)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((12.4, 0)):
                Circle(0.2)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((9.9, 0)):
                Circle(0.2)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((7.4, 0)):
                Circle(0.2)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((4.9, 0)):
                Circle(0.2)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((2.4, 0)):
                Circle(0.2)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 13 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.1, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 6, perimeter: 40.6
            with BuildLine():
                Line((-0.95, 10), (-0.95, -10))
                Line((-1.25, 10), (-0.95, 10))
                Line((-1.25, -10), (-1.25, 10))
                Line((-0.95, -10), (-1.25, -10))
            make_face()
            # Profile area: 6, perimeter: 40.6
            with BuildLine():
                Line((1.25, -10), (1.25, 10))
                Line((1.25, 10), (0.95, 10))
                Line((0.95, 10), (0.95, -10))
                Line((0.95, -10), (1.25, -10))
            make_face()
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.ADD)

        # Sketch3 -> Extrude4 (NewBody)
        # Sketch on BRepFace
        # Sketch has 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -9.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((17.4, 0)):
                Circle(0.2)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((14.9, 0)):
                Circle(0.2)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((12.4, 0)):
                Circle(0.2)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((9.9, 0)):
                Circle(0.2)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((7.4, 0)):
                Circle(0.2)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((4.9, 0)):
                Circle(0.2)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((2.4, 0)):
                Circle(0.2)
        # Symmetric extrude, each_side=1.5
        extrude(amount=1.5, both=True)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -8.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2900284877, perimeter: 3.6566370614
            with BuildLine():
                Line((17.0535898385, -0.2), (17.4, -0.4))
                Line((17.4, -0.4), (17.7464101615, -0.2))
                Line((17.7464101615, -0.2), (17.7464101615, 0.2))
                Line((17.7464101615, 0.2), (17.4, 0.4))
                Line((17.4, 0.4), (17.0535898385, 0.2))
                Line((17.0535898385, 0.2), (17.0535898385, -0.2))
            make_face()
            with BuildLine():
                CenterArc((17.4, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((17.4, 0)):
                Circle(0.2)

        # Sketch6 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.0000002245, -8.3, 0.0000000011), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2900284877, perimeter: 3.6566370614
            with BuildLine():
                Line((14.553590063, -0.2000000011), (14.9000002245, -0.4000000011))
                Line((14.9000002245, -0.4000000011), (15.246410386, -0.2000000011))
                Line((15.246410386, -0.2000000011), (15.246410386, 0.1999999989))
                Line((15.246410386, 0.1999999989), (14.9000002245, 0.3999999989))
                Line((14.9000002245, 0.3999999989), (14.553590063, 0.1999999989))
                Line((14.553590063, 0.1999999989), (14.553590063, -0.2000000011))
            make_face()
            with BuildLine():
                CenterArc((14.9000002245, -0.0000000011), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((14.9000002245, -0.0000000011)):
                Circle(0.2)

        # Sketch7 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.0000002245, -8.3, 0.0000000011), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2900284877, perimeter: 3.6566370614
            with BuildLine():
                Line((12.053590063, -0.2000000011), (12.4000002245, -0.4000000011))
                Line((12.4000002245, -0.4000000011), (12.746410386, -0.2000000011))
                Line((12.746410386, -0.2000000011), (12.746410386, 0.1999999989))
                Line((12.746410386, 0.1999999989), (12.4000002245, 0.3999999989))
                Line((12.4000002245, 0.3999999989), (12.053590063, 0.1999999989))
                Line((12.053590063, 0.1999999989), (12.053590063, -0.2000000011))
            make_face()
            with BuildLine():
                CenterArc((12.4000002245, -0.0000000011), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((12.4000002245, -0.0000000011)):
                Circle(0.2)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch10 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.0000002245, -8.3, 0.0000000011), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2900284877, perimeter: 3.6566370614
            with BuildLine():
                Line((4.553590063, -0.2000000011), (4.9000002245, -0.4000000011))
                Line((4.9000002245, -0.4000000011), (5.246410386, -0.2000000011))
                Line((5.246410386, -0.2000000011), (5.246410386, 0.1999999989))
                Line((5.246410386, 0.1999999989), (4.9000002245, 0.3999999989))
                Line((4.9000002245, 0.3999999989), (4.553590063, 0.1999999989))
                Line((4.553590063, 0.1999999989), (4.553590063, -0.2000000011))
            make_face()
            with BuildLine():
                CenterArc((4.9000002245, -0.0000000011), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((4.9000002245, -0.0000000011)):
                Circle(0.2)

        # Sketch11 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -8.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2900284877, perimeter: 3.6566370614
            with BuildLine():
                Line((2.0535898385, -0.2), (2.4, -0.4))
                Line((2.4, -0.4), (2.7464101615, -0.2))
                Line((2.7464101615, -0.2), (2.7464101615, 0.2))
                Line((2.7464101615, 0.2), (2.4, 0.4))
                Line((2.4, 0.4), (2.0535898385, 0.2))
                Line((2.0535898385, 0.2), (2.0535898385, -0.2))
            make_face()
            with BuildLine():
                CenterArc((2.4, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((2.4, 0)):
                Circle(0.2)

        # Sketch8 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -8.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2900284877, perimeter: 3.6566370614
            with BuildLine():
                Line((9.5535898385, -0.2), (9.9, -0.4))
                Line((9.9, -0.4), (10.2464101615, -0.2))
                Line((10.2464101615, -0.2), (10.2464101615, 0.2))
                Line((10.2464101615, 0.2), (9.9, 0.4))
                Line((9.9, 0.4), (9.5535898385, 0.2))
                Line((9.5535898385, 0.2), (9.5535898385, -0.2))
            make_face()
            with BuildLine():
                CenterArc((9.9, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((9.9, 0)):
                Circle(0.2)

        # Sketch9 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -8.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2900284877, perimeter: 3.6566370614
            with BuildLine():
                Line((7.0535898385, -0.2), (7.4, -0.4))
                Line((7.4, -0.4), (7.7464101615, -0.2))
                Line((7.7464101615, -0.2), (7.7464101615, 0.2))
                Line((7.7464101615, 0.2), (7.4, 0.4))
                Line((7.4, 0.4), (7.0535898385, 0.2))
                Line((7.0535898385, 0.2), (7.0535898385, -0.2))
            make_face()
            with BuildLine():
                CenterArc((7.4, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((7.4, 0)):
                Circle(0.2)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)
    return part.part


def model_31136_987852a4_0004():
    """Model: Component7"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 7.65, perimeter: 12.1
            with BuildLine():
                Line((-20.9499701907, 6.7012464495), (-22.7499701907, 6.7012464495))
                Line((-22.7499701907, 6.7012464495), (-22.7499701907, 2.4512464495))
                Line((-22.7499701907, 2.4512464495), (-20.9499701907, 2.4512464495))
                Line((-20.9499701907, 2.4512464495), (-20.9499701907, 6.7012464495))
            make_face()
        # OneSide extrude, distance=4.25
        extrude(amount=4.25)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 17 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-22.7499701907, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 3.4649086959, perimeter: 8.0909803882
            with BuildLine():
                CenterArc((1.14, 4.5762464495), 0.2676, 90, 180)
                Line((1.24, 4.3086464495), (1.14, 4.3086464495))
                Line((1.24, 3.6912464495), (1.24, 4.3086464495))
                Line((3.01, 3.6912464495), (1.24, 3.6912464495))
                Line((3.01, 4.3086464495), (3.01, 3.6912464495))
                Line((3.01, 4.3086464495), (3.11, 4.3086464495))
                CenterArc((3.11, 4.5762464495), 0.2676, -90, 180)
                Line((3.01, 4.8438464495), (3.11, 4.8438464495))
                Line((3.01, 5.4612464495), (3.01, 4.8438464495))
                Line((1.24, 5.4612464495), (3.01, 5.4612464495))
                Line((1.24, 4.8438464495), (1.24, 5.4612464495))
                Line((1.24, 4.8438464495), (1.14, 4.8438464495))
            make_face()
        # OneSide extrude, distance=-3.2
        extrude(amount=-3.2, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-20.9499701907, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 11.3575913041, perimeter: 23.4909803882
            with BuildLine():
                Line((-4.05, 6.5012464495), (-4.05, 2.6512464495))
                Line((-4.05, 2.6512464495), (-0.2, 2.6512464495))
                Line((-0.2, 2.6512464495), (-0.2, 6.5012464495))
                Line((-0.2, 6.5012464495), (-4.05, 6.5012464495))
            make_face()
            with BuildLine():
                Line((-1.24, 4.3086464495), (-1.24, 3.6912464495))
                Line((-1.24, 3.6912464495), (-3.01, 3.6912464495))
                Line((-3.01, 3.6912464495), (-3.01, 4.3086464495))
                Line((-3.01, 4.3086464495), (-3.11, 4.3086464495))
                CenterArc((-3.11, 4.5762464495), 0.2676, 90, 180)
                Line((-3.11, 4.8438464495), (-3.01, 4.8438464495))
                Line((-3.01, 4.8438464495), (-3.01, 5.4612464495))
                Line((-3.01, 5.4612464495), (-1.24, 5.4612464495))
                Line((-1.24, 5.4612464495), (-1.24, 4.8438464495))
                Line((-1.24, 4.8438464495), (-1.14, 4.8438464495))
                CenterArc((-1.14, 4.5762464495), 0.2676, -90, 180)
                Line((-1.14, 4.3086464495), (-1.24, 4.3086464495))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 14 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-21.9499701907, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.49, perimeter: 2.8
            with BuildLine():
                Line((-4.05, 6.5012464495), (-4.05, 5.8012464495))
                Line((-3.35, 5.8012464495), (-4.05, 5.8012464495))
                Line((-3.35, 6.5012464495), (-3.35, 5.8012464495))
                Line((-4.05, 6.5012464495), (-3.35, 6.5012464495))
            make_face()
            # Profile area: 0.49, perimeter: 2.8
            with BuildLine():
                Line((-3.35, 2.6512464495), (-3.35, 3.3512464495))
                Line((-3.35, 3.3512464495), (-4.05, 3.3512464495))
                Line((-4.05, 3.3512464495), (-4.05, 2.6512464495))
                Line((-4.05, 2.6512464495), (-3.35, 2.6512464495))
            make_face()
            # Profile area: 0.49, perimeter: 2.8
            with BuildLine():
                Line((-0.9, 6.5012464495), (-0.9, 5.8012464495))
                Line((-0.9, 5.8012464495), (-0.2, 5.8012464495))
                Line((-0.2, 5.8012464495), (-0.2, 6.5012464495))
                Line((-0.2, 6.5012464495), (-0.9, 6.5012464495))
            make_face()
            # Profile area: 0.49, perimeter: 2.8
            with BuildLine():
                Line((-0.9, 3.3512464495), (-0.2, 3.3512464495))
                Line((-0.9, 2.6512464495), (-0.9, 3.3512464495))
                Line((-0.9, 2.6512464495), (-0.2, 2.6512464495))
                Line((-0.2, 2.6512464495), (-0.2, 3.3512464495))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 6.7012464495, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.26, perimeter: 5
            with BuildLine():
                Line((22.7499701907, 3.1425), (20.9499701907, 3.1425))
                Line((20.9499701907, 3.1425), (20.9499701907, 2.4425))
                Line((22.7499701907, 2.4425), (20.9499701907, 2.4425))
                Line((22.7499701907, 2.4425), (22.7499701907, 3.1425))
            make_face()
            # Profile area: 1.26, perimeter: 5
            with BuildLine():
                Line((20.9499701907, 1.8075), (22.7499701907, 1.8075))
                Line((20.9499701907, 1.8075), (20.9499701907, 1.1075))
                Line((20.9499701907, 1.1075), (22.7499701907, 1.1075))
                Line((22.7499701907, 1.1075), (22.7499701907, 1.8075))
            make_face()
        # OneSide extrude, distance=0.8
        extrude(amount=0.8, mode=Mode.ADD)

        # Sketch6 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.4512464495, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 1.26, perimeter: 5
            with BuildLine():
                Line((-22.7499701907, 1.1075), (-20.9499701907, 1.1075))
                Line((-20.9499701907, 1.1075), (-20.9499701907, 1.8075))
                Line((-22.7499701907, 1.8075), (-20.9499701907, 1.8075))
                Line((-22.7499701907, 1.8075), (-22.7499701907, 1.1075))
            make_face()
            # Profile area: 1.26, perimeter: 5
            with BuildLine():
                Line((-20.9499701907, 2.4425), (-22.7499701907, 2.4425))
                Line((-20.9499701907, 2.4425), (-20.9499701907, 3.1425))
                Line((-20.9499701907, 3.1425), (-22.7499701907, 3.1425))
                Line((-22.7499701907, 3.1425), (-22.7499701907, 2.4425))
            make_face()
        # OneSide extrude, distance=0.8
        extrude(amount=0.8, mode=Mode.ADD)

        # Sketch7 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3.1425), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-21.8499701907, 7.1012464495)):
                Circle(0.25)
        # OneSide extrude, distance=-3.8
        extrude(amount=-3.8, mode=Mode.SUBTRACT)

        # Sketch8 -> Extrude8 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3.1425), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-21.8499701907, 2.0512464495)):
                Circle(0.25)
        # OneSide extrude, distance=-2.6
        extrude(amount=-2.6, mode=Mode.SUBTRACT)
    return part.part


def model_33655_f8991a06_0005():
    """Model: pieza 1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.9374792479, perimeter: 3.8909477023
            with BuildLine():
                CenterArc((0, 0), 0.7, 150, 30)
                CenterArc((0, 0), 0.7, -180, 30)
                Line((-0.6062177826, -0.35), (0.6062177826, -0.35))
                CenterArc((0, 0), 0.7, -30, 30)
                CenterArc((0, 0), 0.7, 0, 30)
                Line((0.6062177826, 0.35), (-0.6062177826, 0.35))
            make_face()
        # OneSide extrude, distance=1.9
        extrude(amount=1.9)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.026288725, perimeter: 1.2497787144
            with BuildLine():
                CenterArc((0, 0.35), 0.35, -90, 90)
                Line((0.35, 0), (0, 0))
                Line((0.35, 0.35), (0.35, 0))
            make_face()
            # Profile area: 0.026288725, perimeter: 1.2497787144
            with BuildLine():
                CenterArc((0, 0.35), 0.35, -180, 90)
                Line((-0.35, 0), (-0.35, 0.35))
                Line((0, 0), (-0.35, 0))
            make_face()
        # OneSide extrude, distance=0.85
        extrude(amount=0.85, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.026288725, perimeter: 1.2497787144
            with BuildLine():
                CenterArc((0, 0.35), 0.35, -90, 90)
                Line((0.35, 0), (0, 0))
                Line((0.35, 0.35), (0.35, 0))
            make_face()
            # Profile area: 0.026288725, perimeter: 1.2497787144
            with BuildLine():
                CenterArc((0, 0.35), 0.35, -180, 90)
                Line((-0.35, 0), (-0.35, 0.35))
                Line((0, 0), (-0.35, 0))
            make_face()
        # OneSide extrude, distance=-0.85
        extrude(amount=-0.85, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude4 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0628318531, perimeter: 1.0283185307
            with BuildLine():
                Line((0.2, 0.35), (-0.2, 0.35))
                CenterArc((0, 0.35), 0.2, 180, 180)
            make_face()
            # Profile area: 0.0628318531, perimeter: 1.0283185307
            with BuildLine():
                CenterArc((0, 0.35), 0.2, 0, 180)
                Line((0.2, 0.35), (-0.2, 0.35))
            make_face()
        # OneSide extrude, distance=0.85
        extrude(amount=0.85, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude5 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0628318531, perimeter: 1.0283185307
            with BuildLine():
                Line((0.2, 0.35), (-0.2, 0.35))
                CenterArc((0, 0.35), 0.2, 180, 180)
            make_face()
            # Profile area: 0.0628318531, perimeter: 1.0283185307
            with BuildLine():
                CenterArc((0, 0.35), 0.2, 0, 180)
                Line((0.2, 0.35), (-0.2, 0.35))
            make_face()
        # OneSide extrude, distance=-0.85
        extrude(amount=-0.85, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.35), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.28, perimeter: 2.3
            with BuildLine():
                Line((-0.4, 0.35), (0.4, 0.35))
                Line((-0.4, 0.35), (-0.4, 0))
                Line((0.4, 0), (-0.4, 0))
                Line((0.4, 0.35), (0.4, 0))
            make_face()
            # Profile area: 0.6913274123, perimeter: 3.1566370614
            with BuildLine():
                Line((0.4, 0.9), (0.4, 0.35))
                CenterArc((0, 0.9), 0.4, 0, 90)
                CenterArc((0, 0.9), 0.4, 90, 90)
                Line((-0.4, 0.9), (-0.4, 0.35))
                Line((-0.4, 0.35), (0.4, 0.35))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude7 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.9, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=0.22
        extrude(amount=0.22, mode=Mode.ADD)

        # Sketch5 -> Extrude8 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.12, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1590431281, perimeter: 1.4137166941
            Circle(0.225)
        # OneSide extrude, distance=0.08
        extrude(amount=0.08, mode=Mode.ADD)

        # Sketch6 -> Extrude9 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1237002107, perimeter: 3.2986722863
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.225, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1590431281, perimeter: 1.4137166941
            Circle(0.225)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)

        # Sketch7 -> Extrude10 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0590251792, perimeter: 1.5574276068
            with BuildLine():
                CenterArc((0, 0), 0.3, 41.8103148958, 96.3793702084)
                Line((0.2236067977, 0.2), (0.3, 0.2))
                Line((0.3, 0.2), (0.3, 0.35))
                Line((0.3, 0.35), (-0.3, 0.35))
                Line((-0.3, 0.35), (-0.3, 0.2))
                Line((-0.3, 0.2), (-0.2236067977, 0.2))
            make_face()
            # Profile area: 0.0309748208, perimeter: 0.9518547978
            with BuildLine():
                Line((0, 0.2), (0.2236067977, 0.2))
                CenterArc((0, 0), 0.3, 41.8103148958, 96.3793702084)
                Line((-0.2236067977, 0.2), (0, 0.2))
            make_face()
        # OneSide extrude, distance=-0.3175
        extrude(amount=-0.3175, mode=Mode.SUBTRACT)
    return part.part


def model_34317_e9c65aa6_0001():
    """Model: Basis v18 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 576, perimeter: 104
            with BuildLine():
                Line((29.5, -11), (-6.5, -11))
                Line((29.5, 5), (29.5, -11))
                Line((-6.5, 5), (29.5, 5))
                Line((-6.5, -11), (-6.5, 5))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 54, perimeter: 75
            with BuildLine():
                Line((-6.5, -2.25), (29.5, -2.25))
                Line((-6.5, -2.25), (-6.5, -3.75))
                Line((29.5, -3.75), (-6.5, -3.75))
                Line((29.5, -2.25), (29.5, -3.75))
            make_face()
        # OneSide extrude, distance=28
        extrude(amount=28, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -3.75, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 123.0931914395, perimeter: 82.9533286251
            with BuildLine():
                Line((1.5, 6.5), (24.9213855594, -0.0511346755))
                CenterArc((12.8966990027, -11.5), 16.6033009973, 0, 43.594779724)
                Line((29.5, -11.5), (29.5, 6.5))
                Line((29.5, 6.5), (1.5, 6.5))
            make_face()
            # Profile area: 123.0931914395, perimeter: 82.9533286251
            with BuildLine():
                CenterArc((12.8966990027, -11.5), 16.6033009973, -43.594779724, 43.594779724)
                Line((1.5, -29.5), (24.9213855594, -22.9488653245))
                Line((1.5, -29.5), (29.5, -29.5))
                Line((29.5, -29.5), (29.5, -11.5))
            make_face()
        # OneSide extrude, distance=-5
        extrude(amount=-5, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -3.75, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 35.1912416832, perimeter: 49.923728398
            with BuildLine():
                Line((24.9213855594, -22.9488653245), (25.0002700182, -21.4488653245))
                Line((25.0002700182, -21.4488653245), (1.5, -21.4488653245))
                Line((1.5, -22.9488653245), (1.5, -21.4488653245))
                Line((24.9213855594, -22.9488653245), (1.5, -22.9488653245))
            make_face()
        # OneSide extrude, distance=9
        extrude(amount=9, mode=Mode.ADD)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -22.9488653245), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 110.8086049303, perimeter: 57.4197895312
            with BuildLine():
                Line((-1.5, -11), (-2.5, -11))
                Line((-24.9213855594, -4.7719120867), (-2.5, -11))
                Line((-24.9213855594, -4.7719120867), (-24.9213855594, -12.75))
                Line((-24.9213855594, -12.75), (-1.5, -12.75))
                Line((-1.5, -12.75), (-1.5, -11))
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -22.9488653245), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 10.9219783133, perimeter: 19.8776008312
            with BuildLine():
                Line((-25.3937270446, -4.6407076932), (-25.3937270446, -13.3587321221))
                Line((-25.3937270446, -13.3587321221), (-23.5767252393, -13.3587321221))
                Line((-23.5767252393, -13.3587321221), (-24.6628046593, -4.8437392525))
                Line((-24.6628046593, -4.8437392525), (-24.9213855594, -4.7719120867))
                Line((-24.9213855594, -4.7719120867), (-25.3937270446, -4.6407076932))
            make_face()
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.SUBTRACT)

        # Sketch10 -> Extrude8 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -3.75, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 50.2654824574, perimeter: 25.1327412287
            with Locations((15.7, -11.5)):
                Circle(4)
        # OneSide extrude, distance=-5
        extrude(amount=-5, mode=Mode.SUBTRACT)

        # Sketch11 -> Extrude9 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -3.75, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((22.2000083754, -4.9999916246)):
                Circle(1)
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((9.1999916246, -4.9999916246)):
                Circle(1)
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((22.2000083754, -18.0000083754)):
                Circle(1)
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((9.1999916246, -18.0000083754)):
                Circle(1)
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)

        # Sketch12 -> Extrude10 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -3.75, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 6.479534848, perimeter: 51.8362787842
            with BuildLine():
                CenterArc((15.7, -11.5), 4.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((15.7, -11.5), 4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 50.2654824574, perimeter: 25.1327412287
            with Locations((15.7, -11.5)):
                Circle(4)
        # OneSide extrude, distance=-4
        extrude(amount=-4, mode=Mode.SUBTRACT)
    return part.part


def model_40145_9854f000_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4, perimeter: 8
            with BuildLine():
                Line((0.3000000045, 2.1000000015), (0.3000000045, 0.1000000015))
                Line((0.3000000045, 0.1000000015), (2.3000000045, 0.1000000015))
                Line((2.3000000045, 0.1000000015), (2.3000000045, 2.1000000015))
                Line((2.3000000045, 2.1000000015), (0.3000000045, 2.1000000015))
            make_face()
        # OneSide extrude, distance=50
        extrude(amount=50)

        # Sketch4 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 13 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4, perimeter: 8
            with BuildLine():
                Line((54.3000000045, 0.1000000015), (54.3000000045, 2.1000000015))
                Line((54.3000000045, 2.1000000015), (52.3000000045, 2.1000000015))
                Line((52.3000000045, 2.1000000015), (52.3000000045, 0.1000000015))
                Line((52.3000000045, 0.1000000015), (54.3000000045, 0.1000000015))
            make_face()
            # Profile area: 4, perimeter: 8
            with BuildLine():
                Line((54.3000000045, -29.8999999985), (52.3000000045, -29.8999999985))
                Line((52.3000000045, -29.8999999985), (52.3000000045, -31.8999999985))
                Line((54.3000000045, -31.8999999985), (52.3000000045, -31.8999999985))
                Line((54.3000000045, -31.8999999985), (54.3000000045, -29.8999999985))
            make_face()
            # Profile area: 4, perimeter: 8
            with BuildLine():
                Line((2.3000000045, -29.8999999985), (2.3000000045, -31.8999999985))
                Line((0.3000000045, -29.8999999985), (2.3000000045, -29.8999999985))
                Line((0.3000000045, -31.8999999985), (0.3000000045, -29.8999999985))
                Line((2.3000000045, -31.8999999985), (0.3000000045, -31.8999999985))
            make_face()
        # OneSide extrude, distance=50
        extrude(amount=50)

        # Sketch5 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 50, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2012, perimeter: 192
            with BuildLine():
                Line((0.6999999955, -3.1000000015), (0.6999999955, 32.8999999985))
                Line((0.6999999955, 32.8999999985), (-55.3000000045, 32.8999999985))
                Line((-55.3000000045, 32.8999999985), (-55.3000000045, -3.1000000015))
                Line((-55.3000000045, -3.1000000015), (0.6999999955, -3.1000000015))
            make_face()
            with BuildLine():
                Line((-0.3000000045, 31.8999999985), (-0.3000000045, 29.8999999985))
                Line((-0.3000000045, 29.8999999985), (-2.3000000045, 29.8999999985))
                Line((-2.3000000045, 29.8999999985), (-2.3000000045, 31.8999999985))
                Line((-2.3000000045, 31.8999999985), (-0.3000000045, 31.8999999985))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 4, perimeter: 8
            with BuildLine():
                Line((-2.3000000045, 31.8999999985), (-0.3000000045, 31.8999999985))
                Line((-2.3000000045, 29.8999999985), (-2.3000000045, 31.8999999985))
                Line((-0.3000000045, 29.8999999985), (-2.3000000045, 29.8999999985))
                Line((-0.3000000045, 31.8999999985), (-0.3000000045, 29.8999999985))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)

        # Sketch7 -> Extrude4 (NewBody)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 31.8999999985), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 21, perimeter: 38
            with BuildLine():
                Line((14.3000000045, 50), (12.8000000045, 50))
                Line((12.8000000045, 50), (12.8000000045, 44))
                Line((12.8000000045, 44), (2.3000000045, 44))
                Line((2.3000000045, 43), (2.3000000045, 44))
                Line((14.3000000045, 43), (2.3000000045, 43))
                Line((14.3000000045, 50), (14.3000000045, 43))
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2)

        # Sketch13 -> Extrude9 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 167.44, perimeter: 53
            with BuildLine():
                Line((-15, -18.6), (-25.4, -18.6))
                Line((-15, -2.5), (-15, -18.6))
                Line((-25.4, -2.5), (-15, -2.5))
                Line((-25.4, -18.6), (-25.4, -2.5))
            make_face()
        # OneSide extrude, distance=5.9
        extrude(amount=5.9)

        # Sketch14 -> Extrude10 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5.9, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 141.94, perimeter: 49
            with BuildLine():
                Line((15.5, 18.1), (24.9, 18.1))
                Line((15.5, 3), (15.5, 18.1))
                Line((24.9, 3), (15.5, 3))
                Line((24.9, 18.1), (24.9, 3))
            make_face()
        # OneSide extrude, distance=-5.5
        extrude(amount=-5.5, mode=Mode.SUBTRACT)

        # Sketch15 -> Extrude11 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 18.6), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-20, 3)):
                Circle(0.5)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch16 -> Extrude12 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 19.6), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.5393797299, perimeter: 8.5465922468
            with BuildLine():
                CenterArc((-20, 3), 0.8602324027, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-20, 3), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-20, 3)):
                Circle(0.5)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


def model_40693_d1d9ff4a_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 41 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 31.4256449886, perimeter: 23.7204443642
            with BuildLine():
                Line((0.4740113146, -0.8599999808), (0.4740113146, -1.7000000253))
                Line((-0.579999987, -0.8599999808), (0.4740113146, -0.8599999808))
                Line((-0.9599999785, -0.8799999803), (-0.579999987, -0.8599999808))
                Line((-1.1699999738, -0.9199999794), (-0.9599999785, -0.8799999803))
                Line((-1.3199999705, -0.9699999783), (-1.1699999738, -0.9199999794))
                Line((-1.4799999669, -1.0599999763), (-1.3199999705, -0.9699999783))
                Line((-1.5999999642, -1.1399999745), (-1.4799999669, -1.0599999763))
                Line((-1.7099999618, -1.2399999723), (-1.5999999642, -1.1399999745))
                Line((-1.9499999564, -1.5399999656), (-1.7099999618, -1.2399999723))
                Line((-2.0199999548, -1.7299999613), (-1.9499999564, -1.5399999656))
                Line((-2.0499999542, -1.9599999562), (-2.0199999548, -1.7299999613))
                Line((-2.0499999542, -2.0999999531), (-2.0499999542, -1.9599999562))
                Line((-2.0199999548, -2.279999949), (-2.0499999542, -2.0999999531))
                Line((-1.9899999555, -2.3999999464), (-2.0199999548, -2.279999949))
                Line((-1.9499999564, -2.4999999441), (-1.9899999555, -2.3999999464))
                Line((-1.879999958, -2.6499999408), (-1.9499999564, -2.4999999441))
                Line((-1.8099269326, -2.7929491087), (-1.879999958, -2.6499999408))
                Line((-1.6641727348, -3.0674816153), (-1.8099269326, -2.7929491087))
                Line((-1.5899999645, -3.2899999265), (-1.6641727348, -3.0674816153))
                Line((-1.5672919339, -3.4099999238), (-1.5899999645, -3.2899999265))
                Line((-1.5672919339, -3.499627331), (-1.5672919339, -3.4099999238))
                Line((-1.6591553719, -3.8096186484), (-1.5672919339, -3.499627331))
                Line((-1.7199999616, -3.9399999119), (-1.6591553719, -3.8096186484))
                Line((-1.8017047577, -4.0465108721), (-1.7199999616, -3.9399999119))
                Line((-2.2299999502, -4.4999998994), (-1.8017047577, -4.0465108721))
                Line((-2.3999999464, -4.7399998941), (-2.2299999502, -4.4999998994))
                Line((-2.5399999432, -4.9799998887), (-2.3999999464, -4.7399998941))
                Line((-2.6799999401, -5.279999882), (-2.5399999432, -4.9799998887))
                Line((-2.7799999379, -5.5699998755), (-2.6799999401, -5.279999882))
                Line((-2.8499999363, -5.859999869), (-2.7799999379, -5.5699998755))
                Line((-2.8499999363, -6.4699998554), (-2.8499999363, -5.859999869))
                Line((-2.7799999379, -6.8199998476), (-2.8499999363, -6.4699998554))
                Line((-2.7099999394, -7.0399998426), (-2.7799999379, -6.8199998476))
                Line((-2.6099999417, -7.2699998375), (-2.7099999394, -7.0399998426))
                Line((-2.4699999448, -7.5099998321), (-2.6099999417, -7.2699998375))
                Line((-2.2999999486, -7.7199998274), (-2.4699999448, -7.5099998321))
                Line((-2.0799999535, -7.9399998225), (-2.2999999486, -7.7199998274))
                Line((-1.8199999593, -8.1099998187), (-2.0799999535, -7.9399998225))
                Line((-1.6499999631, -8.2099998165), (-1.8199999593, -8.1099998187))
                Line((-1.3199999705, -8.3499998134), (-1.6499999631, -8.2099998165))
                Line((-1.0799999759, -8.4199998118), (-1.3199999705, -8.3499998134))
                Line((-0.7099999841, -8.4899998102), (-1.0799999759, -8.4199998118))
                Line((-0.2999999933, -8.5199998096), (-0.7099999841, -8.4899998102))
                Line((0.1999999955, -8.5199998096), (-0.2999999933, -8.5199998096))
                Line((0.5599999875, -8.49999981), (0.1999999955, -8.5199998096))
                Line((0.8699999806, -8.4499998111), (0.5599999875, -8.49999981))
                Line((1.1399999745, -8.3899998125), (0.8699999806, -8.4499998111))
                Line((1.3499999698, -8.3099998143), (1.1399999745, -8.3899998125))
                Line((1.5599999651, -8.2199998163), (1.3499999698, -8.3099998143))
                Line((1.7868519472, -8.089838296), (1.5599999651, -8.2199998163))
                Line((2.0607429017, -7.8900590116), (1.7868519472, -8.089838296))
                Line((2.2879112816, -7.6677240015), (2.0607429017, -7.8900590116))
                Line((2.5000000373, -7.4000001103), (2.2879112816, -7.6677240015))
                Line((2.6683162393, -7.1230653498), (2.5000000373, -7.4000001103))
                Line((2.7819000873, -6.8421027104), (2.6683162393, -7.1230653498))
                Line((2.8434885654, -6.4500000961), (2.7819000873, -6.8421027104))
                Line((2.8434885654, -5.981980835), (2.8434885654, -6.4500000961))
                Line((2.7203116092, -5.4488047466), (2.8434885654, -5.981980835))
                Line((2.6168147299, -5.1751129991), (2.7203116092, -5.4488047466))
                Line((2.508149589, -4.9670468853), (2.6168147299, -5.1751129991))
                Line((2.4163022768, -4.7785135014), (2.508149589, -4.9670468853))
                Line((2.2220107341, -4.4916169317), (2.4163022768, -4.7785135014))
                Line((1.6013434921, -3.7287387586), (2.2220107341, -4.4916169317))
                Line((1.5277598134, -3.5500000529), (1.6013434921, -3.7287387586))
                Line((1.5277598134, -3.2028810866), (1.5277598134, -3.5500000529))
                Line((1.5553657674, -3.0941316037), (1.5277598134, -3.2028810866))
                Line((1.8552701333, -2.4857541757), (1.5553657674, -3.0941316037))
                Line((1.9500000291, -2.150000032), (1.8552701333, -2.4857541757))
                Line((1.969999956, -1.929559835), (1.9500000291, -2.150000032))
                Line((1.9619014628, -1.8746627003), (1.969999956, -1.929559835))
                Line((1.913121735, -1.6868607482), (1.9619014628, -1.8746627003))
                Line((1.9027714303, -1.665621906), (1.913121735, -1.6868607482))
                Line((1.8918786211, -1.6523796672), (1.9027714303, -1.665621906))
                Line((1.8699999582, -1.6399999633), (1.8918786211, -1.6523796672))
                Line((1.8249999592, -1.6349999635), (1.8699999582, -1.6399999633))
                Line((1.7942705067, -1.6376423371), (1.8249999592, -1.6349999635))
                Line((1.7756886556, -1.6425547805), (1.7942705067, -1.6376423371))
                Line((1.7635625308, -1.6473345149), (1.7756886556, -1.6425547805))
                Line((1.7499999609, -1.6599999629), (1.7635625308, -1.6473345149))
                Line((1.72901454, -1.6970788305), (1.7499999609, -1.6599999629))
                Line((1.6408755383, -1.8239867699), (1.72901454, -1.6970788305))
                Line((1.5589524629, -1.9206982919), (1.6408755383, -1.8239867699))
                Line((1.4399999678, -1.9999999553), (1.5589524629, -1.9206982919))
                Line((1.3599999696, -2.0299999546), (1.4399999678, -1.9999999553))
                Line((1.2699999716, -2.0562163838), (1.3599999696, -2.0299999546))
                Line((0.9189869464, -2.0562163838), (1.2699999716, -2.0562163838))
                Line((0.7699999828, -1.9899999555), (0.9189869464, -2.0562163838))
                Line((0.6799999848, -1.9399999566), (0.7699999828, -1.9899999555))
                Line((0.6099999864, -1.8899999578), (0.6799999848, -1.9399999566))
                Line((0.5599999875, -1.8399999589), (0.6099999864, -1.8899999578))
                Line((0.4740113146, -1.7000000253), (0.5599999875, -1.8399999589))
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.2581414382, perimeter: 4.5356022126
            with BuildLine():
                Line((0.5411305074, 0.8599999808), (0.5411305074, 2.1599999808))
                Line((-0.4266705989, 2.1599999808), (0.5411305074, 2.1599999808))
                Line((-0.4266705989, 0.8599999808), (-0.4266705989, 2.1599999808))
                Line((0.5411305074, 0.8599999808), (-0.4266705989, 0.8599999808))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 15 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6600000197, perimeter: 3.4000000507
            with BuildLine():
                Line((-0.5000000075, 2.8000000417), (0.6000000089, 2.8000000417))
                Line((-0.5000000075, 2.2000000328), (-0.5000000075, 2.8000000417))
                Line((0.6000000089, 2.2000000328), (-0.5000000075, 2.2000000328))
                Line((0.6000000089, 2.8000000417), (0.6000000089, 2.2000000328))
            make_face()
            # Profile area: 0.6600000197, perimeter: 3.4000000507
            with BuildLine():
                Line((-0.5000000075, 5.100000076), (0.6000000089, 5.100000076))
                Line((-0.5000000075, 4.5000000671), (-0.5000000075, 5.100000076))
                Line((0.6000000089, 4.5000000671), (-0.5000000075, 4.5000000671))
                Line((0.6000000089, 5.100000076), (0.6000000089, 4.5000000671))
            make_face()
        # OneSide extrude, distance=0.05
        extrude(amount=0.05, mode=Mode.ADD)

        # Sketch8 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2200000066, perimeter: 2.6090722423
            with BuildLine():
                Line((-0.5000000075, 5.4000000805), (0.6000000089, 5.500000082))
                Line((0.6000000089, 5.500000082), (0.6000000089, 5.7000000849))
                Line((0.6000000089, 5.7000000849), (-0.5000000075, 5.6000000834))
                Line((-0.5000000075, 5.6000000834), (-0.5000000075, 5.4000000805))
            make_face()
        # OneSide extrude, distance=0.05
        extrude(amount=0.05, mode=Mode.ADD)

        # Sketch9 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4500000134, perimeter: 3.6000000536
            with BuildLine():
                Line((0.8000000119, 6.1000000909), (-0.7000000104, 6.1000000909))
                Line((0.8000000119, 6.1000000909), (0.8000000119, 6.4000000954))
                Line((-0.7000000104, 6.4000000954), (0.8000000119, 6.4000000954))
                Line((-0.7000000104, 6.1000000909), (-0.7000000104, 6.4000000954))
            make_face()
        # OneSide extrude, distance=0.03
        extrude(amount=0.03, mode=Mode.ADD)

        # Sketch10 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.63, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2999358762, perimeter: 2.5995725528
            with BuildLine():
                Line((0.5499898445, 6.1000000909), (0.5497843313, 6.4000000954))
                Line((-0.4498991511, 6.4000000909), (0.5497843313, 6.4000000954))
                Line((-0.4498991511, 6.1000000909), (-0.4498991511, 6.4000000909))
                Line((0.5499898445, 6.1000000909), (-0.4498991511, 6.1000000909))
            make_face()
        # OneSide extrude, distance=0.075
        extrude(amount=0.075, mode=Mode.ADD)

        # Sketch11 -> Extrude7 (Join)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.63, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((-0.5749495807, 6.2502261747)):
                Circle(0.1)
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((0.6748921716, 6.2503872691)):
                Circle(0.1)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05, mode=Mode.ADD)

        # Sketch12 -> Extrude8 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.2581414382, perimeter: 4.5356022126
            with BuildLine():
                Line((-0.4266705989, 2.1599999808), (-0.4266705989, 0.8599999808))
                Line((-0.4266705989, 0.8599999808), (0.5411305074, 0.8599999808))
                Line((0.5411305074, 2.1599999808), (0.5411305074, 0.8599999808))
                Line((-0.4266705989, 2.1599999808), (0.5411305074, 2.1599999808))
            make_face()
            # Profile area: 0.4839005532, perimeter: 2.9356022126
            with BuildLine():
                Line((-0.4266705989, 0.8599999808), (0.5411305074, 0.8599999808))
                Line((-0.4266705989, 0.8599999808), (-0.4266705989, 0.3599999808))
                Line((0.5411305074, 0.3599999808), (-0.4266705989, 0.3599999808))
                Line((0.5411305074, 0.8599999808), (0.5411305074, 0.3599999808))
            make_face()
        # OneSide extrude, distance=0.575
        extrude(amount=0.575, mode=Mode.ADD)
    return part.part


def model_40800_7fa2d7a5_0001():
    """Model: Camera"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 15, perimeter: 17
            with BuildLine():
                Line((3, -1.25), (3, 1.25))
                Line((3, 1.25), (-3, 1.25))
                Line((-3, 1.25), (-3, -1.25))
                Line((-3, -1.25), (3, -1.25))
            make_face()
        # OneSide extrude, distance=-4.3
        extrude(amount=-4.3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 11 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.25, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.8013271108, perimeter: 6.9115038379
            with Locations((2.8, -1.5)):
                Circle(1.1)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 11 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.25, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.2672563597, perimeter: 16.3362817987
            with BuildLine():
                CenterArc((2.8, -1.5), 1.5, 0, 270)
                CenterArc((2.8, -1.5), 1.5, -90, 90)
            make_face()
            with BuildLine():
                CenterArc((2.8, -1.5), 1.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch3 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.05, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.5446900494, perimeter: 5.6548667765
            with Locations((2.8, -1.5)):
                Circle(0.9)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 11 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.25, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.9225388353, perimeter: 6.8360147517
            with BuildLine():
                CenterArc((2.9894683032, 1.6773703687), 0.55, 0, 360)
            make_face()
            with BuildLine():
                Line((3.1875070277, 1.4861518581), (3.1875070277, 1.4662155183))
                CenterArc((2.9894683032, 1.6773703687), 0.2894921541, 46.8359072362, 266.3281855276)
                Line((3.1875070277, 1.8685888793), (3.1875070277, 1.8885252192))
                CenterArc((2.9894683032, 1.6773703687), 0.2752886761, 43.9962177737, 272.0075644527)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((3.049848678, 1.6584034248), (3.049848678, 1.6867900022))
                Line((3.049848678, 1.6867900022), (3.3653769194, 1.6867900022))
                Line((3.3653769194, 1.6867900022), (3.3653769194, 1.6584034248))
                Line((3.3653769194, 1.6584034248), (3.049848678, 1.6584034248))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch5 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 16 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.25, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0569603966, perimeter: 1.6367536349
            with BuildLine():
                Line((1.4500000209, 0.5994150434), (1.4500000209, 1.2999821363))
                CenterArc((1.4125000209, 1.2999821363), 0.0375, 0, 180)
                Line((1.3750000209, 1.2999821363), (1.3750000209, 0.5994150434))
                CenterArc((1.4125000209, 0.5994150434), 0.0375, 180, 180)
            make_face()
            # Profile area: 0.0569603966, perimeter: 1.6367536349
            with BuildLine():
                Line((1.2000000209, 0.5994150434), (1.2000000209, 1.2999821363))
                CenterArc((1.1625000209, 1.2999821363), 0.0375, 0, 180)
                Line((1.1250000209, 1.2999821363), (1.1250000209, 0.5994150434))
                CenterArc((1.1625000209, 0.5994150434), 0.0375, 180, 180)
            make_face()
        # OneSide extrude, distance=-0.025
        extrude(amount=-0.025, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude8 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-4.3, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 1.130973389, perimeter: 3.7699112405
            with Locations((1.8000000268, 0)):
                Circle(0.6000000089)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05, mode=Mode.ADD)

        # Sketch7 -> Extrude9 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-4.35, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0863938064, perimeter: 3.455751947
            with BuildLine():
                CenterArc((1.8000000268, 0), 0.3000000045, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((1.8000000268, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.025
        extrude(amount=-0.025, mode=Mode.SUBTRACT)

        # Sketch8 -> Extrude10 (Join)
        # Sketch on BRepFace
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.2628318609, perimeter: 2.0283185609
            with BuildLine():
                Line((-2.5000000373, 0), (-2.0000000298, 0))
                CenterArc((-2.5000000373, -0.200000003), 0.200000003, 90, 180)
                Line((-2.0000000298, -0.400000006), (-2.5000000373, -0.400000006))
                Line((-2.0000000298, 0), (-2.0000000298, -0.400000006))
            make_face()
            # Profile area: 0.2628318609, perimeter: 2.0283185609
            with BuildLine():
                Line((-1.8000000268, 0), (-1.8000000268, -0.400000006))
                Line((-1.8000000268, -0.400000006), (-1.3000000194, -0.400000006))
                CenterArc((-1.3000000194, -0.200000003), 0.200000003, -90, 180)
                Line((-1.3000000194, 0), (-1.8000000268, 0))
            make_face()
        # OneSide extrude, distance=0.05
        extrude(amount=0.05, mode=Mode.ADD)
    return part.part


def model_41125_711db4bf_0002():
    """Model: main_frame v16"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 13 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.417294641, perimeter: 8.3455062474
            with BuildLine():
                CenterArc((-1.8, 0.2000000148), 0.5999999972, 33.5573090964, 112.8853818073)
                Line((-2.3000000015, 0.5316624864), (-2.3000000015, -0.531662472))
                CenterArc((-1.8, -0.1999999913), 0.6000000022, -146.4426901857, 112.8853803714)
                Line((-1.2999999985, -0.531662472), (-1.2999999985, 0.5316624864))
            make_face()
            with BuildLine():
                Line((-2.2, 0.5000000075), (-2.2, -0.4999999925))
                CenterArc((-1.8, 0.2000000148), 0.4999999957, 36.869896985, 106.26020603)
                Line((-1.4, -0.4999999925), (-1.4, 0.5000000075))
                CenterArc((-1.8, -0.1999999913), 0.5000000007, -143.130102253, 106.2602045061)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1256637061, perimeter: 2.5132741229
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.6
        extrude(amount=1.6)

        # Sketch5 -> Extrude4 (Join)
        # Sketch on XZ construction plane
        # Sketch has 13 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0314159275, perimeter: 0.6283185401
            with Locations((-2.3, 0)):
                Circle(0.1000000015)
            # Profile area: 0.1150000034, perimeter: 2.5000000373
            with BuildLine():
                Line((-0.200000003, -0.0500000007), (-1.3500000201, -0.0500000007))
                Line((-0.200000003, 0.0500000007), (-0.200000003, -0.0500000007))
                Line((-1.3500000201, 0.0500000007), (-0.200000003, 0.0500000007))
                Line((-1.3500000201, -0.0500000007), (-1.3500000201, 0.0500000007))
            make_face()
            # Profile area: 0.0218498116, perimeter: 0.7968038553
            with BuildLine():
                Line((1.2133974601, 0.0500000007), (1.3, 0.0500000007))
                Line((1.3, 0.0500000007), (1.3, -0.0500000007))
                Line((1.3, -0.0500000007), (1.2133974601, -0.0500000007))
                CenterArc((1.3, 0), 0.1, -149.9999995071, 299.9999990141)
            make_face()
            # Profile area: 0.0095661149, perimeter: 0.3779248382
            with BuildLine():
                CenterArc((1.3, 0), 0.1, 149.9999995071, 60.0000009859)
                Line((1.3, -0.0500000007), (1.2133974601, -0.0500000007))
                Line((1.3, 0.0500000007), (1.3, -0.0500000007))
                Line((1.2133974601, 0.0500000007), (1.3, 0.0500000007))
            make_face()
            # Profile area: 0.1004338864, perimeter: 2.2315146725
            with BuildLine():
                CenterArc((1.3, 0), 0.1, 149.9999995071, 60.0000009859)
                Line((0.200000003, 0.0500000007), (1.2133974601, 0.0500000007))
                Line((0.200000003, -0.0500000007), (0.200000003, 0.0500000007))
                Line((1.2133974601, -0.0500000007), (0.200000003, -0.0500000007))
            make_face()
        # OneSide extrude, distance=1.6
        extrude(amount=1.6, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on XZ construction plane
        # Sketch has 13 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0314159275, perimeter: 0.6283185401
            with Locations((-2.3, 0)):
                Circle(0.1000000015)
            # Profile area: 0.0218498116, perimeter: 0.7968038553
            with BuildLine():
                Line((1.2133974601, 0.0500000007), (1.3, 0.0500000007))
                Line((1.3, 0.0500000007), (1.3, -0.0500000007))
                Line((1.3, -0.0500000007), (1.2133974601, -0.0500000007))
                CenterArc((1.3, 0), 0.1, -149.9999995071, 299.9999990141)
            make_face()
            # Profile area: 0.0095661149, perimeter: 0.3779248382
            with BuildLine():
                CenterArc((1.3, 0), 0.1, 149.9999995071, 60.0000009859)
                Line((1.3, -0.0500000007), (1.2133974601, -0.0500000007))
                Line((1.3, 0.0500000007), (1.3, -0.0500000007))
                Line((1.2133974601, 0.0500000007), (1.3, 0.0500000007))
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.ADD)

        # Sketch12 -> Extrude12 (Join)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.48, perimeter: 10.8
            with BuildLine():
                Line((1.2999999657, -0.9), (-2.3000000343, -0.9))
                Line((1.2999999657, 0.9), (1.2999999657, -0.9))
                Line((-2.3000000343, 0.9), (1.2999999657, 0.9))
                Line((-2.3000000343, -0.9), (-2.3000000343, 0.9))
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.ADD)

        # Sketch13 -> Extrude13 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.425783177, perimeter: 2.610102083
            with BuildLine():
                Line((0.4449489741, 0.8), (1.1000000164, 0.8))
                Line((0.4449489741, 0.1500000007), (0.4449489741, 0.8))
                Line((1.1000000164, 0.1500000007), (0.4449489741, 0.1500000007))
                Line((1.1000000164, 0.8), (1.1000000164, 0.1500000007))
            make_face()
            # Profile area: 0.4257831441, perimeter: 2.6101019817
            with BuildLine():
                Line((-1.0999999657, 0.8), (-0.4449489741, 0.8))
                Line((-1.0999999657, 0.1500000007), (-1.0999999657, 0.8))
                Line((-0.4449489741, 0.1500000007), (-1.0999999657, 0.1500000007))
                Line((-0.4449489741, 0.8), (-0.4449489741, 0.1500000007))
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)

        # Sketch14 -> Extrude14 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -0.1, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)

        # Sketch14 -> Extrude15 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -0.1, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.1884955592, perimeter: 3.7699111843
            with BuildLine():
                CenterArc((0, 0), 0.35, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides extrude (symmetric), distance=0.2
        extrude(amount=0.2, both=True, mode=Mode.ADD)

        # Sketch15 -> Extrude16 (NewBody)
        # Sketch on BRepFace
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0047356381, perimeter: 0.3021401507
            with BuildLine():
                Line((0.2449489741, -0.0500000007), (0.2956795678, -0.0500000007))
                Line((0.2956795678, 0.0500000007), (0.2956795678, -0.0500000007))
                Line((0.2956795678, 0.0500000007), (0.2449489741, 0.0500000007))
                CenterArc((0, 0), 0.25, -11.5369592071, 23.0739184142)
            make_face()
            # Profile area: 0.0855514615, perimeter: 1.9161638876
            with BuildLine():
                Line((0.3464101614, -0.0500000007), (1.2043204546, -0.0500000007))
                Line((1.2043204546, -0.0500000007), (1.2043204546, 0.0500000007))
                Line((1.2043204546, 0.0500000007), (0.3464101614, 0.0500000007))
                CenterArc((0, 0), 0.35, -8.213210825, 16.4264216499)
            make_face()
            # Profile area: 0.084199513, perimeter: 1.8868557051
            with BuildLine():
                Line((0.3464101614, 0.0500000007), (0.2956795678, 0.0500000007))
                CenterArc((0, 0), 0.35, 8.213210825, 163.5735783501)
                Line((-0.2449489741, 0.0500000007), (-0.3464101614, 0.0500000007))
                CenterArc((0, 0), 0.25, 11.5369592071, 156.9260815858)
                Line((0.2956795678, 0.0500000007), (0.2449489741, 0.0500000007))
            make_face()
            # Profile area: 0.0053126286, perimeter: 0.3018044885
            with BuildLine():
                Line((0.2956795678, -0.0500000007), (0.3464101614, -0.0500000007))
                CenterArc((0, 0), 0.35, -8.213210825, 16.4264216499)
                Line((0.3464101614, 0.0500000007), (0.2956795678, 0.0500000007))
                Line((0.2956795678, 0.0500000007), (0.2956795678, -0.0500000007))
            make_face()
            # Profile area: 0.0100482667, perimeter: 0.4039446362
            with BuildLine():
                CenterArc((0, 0), 0.25, 168.4630407929, 23.0739184142)
                Line((-0.2449489741, 0.0500000007), (-0.3464101614, 0.0500000007))
                CenterArc((0, 0), 0.35, 171.786789175, 16.4264216499)
                Line((-0.3464101614, -0.0500000007), (-0.2449489741, -0.0500000007))
            make_face()
            # Profile area: 0.084199513, perimeter: 1.8868557051
            with BuildLine():
                CenterArc((0, 0), 0.25, -168.4630407929, 156.9260815858)
                Line((-0.3464101614, -0.0500000007), (-0.2449489741, -0.0500000007))
                CenterArc((0, 0), 0.35, -171.786789175, 163.5735783501)
                Line((0.2956795678, -0.0500000007), (0.3464101614, -0.0500000007))
                Line((0.2449489741, -0.0500000007), (0.2956795678, -0.0500000007))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch23 -> Extrude28 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((1.8000000268, 0)):
                Circle(0.3)
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((1.8000000268, 0.5000000075)):
                Circle(0.05)
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((1.8000000268, -0.5000000075)):
                Circle(0.05)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)
    return part.part


def model_41303_b8f7bdf2_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 387.096, perimeter: 81.28
            with BuildLine():
                Line((-12.7, 7.62), (12.7, 7.62))
                Line((-12.7, -7.62), (-12.7, 7.62))
                Line((12.7, -7.62), (-12.7, -7.62))
                Line((12.7, 7.62), (12.7, -7.62))
            make_face()
        # OneSide extrude, distance=57.15
        extrude(amount=57.15)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 7.62, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1348.3844, perimeter: 160.02
            with BuildLine():
                Line((12.065, 0.635), (12.065, 56.515))
                Line((12.065, 56.515), (-12.065, 56.515))
                Line((-12.065, 56.515), (-12.065, 0.635))
                Line((-12.065, 0.635), (12.065, 0.635))
            make_face()
        # OneSide extrude, distance=-14.605
        extrude(amount=-14.605, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude3 (Join)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 545.1602, perimeter: 99.06
            with BuildLine():
                Line((16.51, -8.255), (-16.51, -8.255))
                Line((16.51, 8.255), (16.51, -8.255))
                Line((-16.51, 8.255), (16.51, 8.255))
                Line((-16.51, -8.255), (-16.51, 8.255))
            make_face()
        # OneSide extrude, distance=-2.54
        extrude(amount=-2.54, mode=Mode.ADD)

        # Sketch6 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 57.15), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 3.2258, perimeter: 7.62
            with BuildLine():
                Line((15.24, -7.62), (15.24, -6.35))
                Line((15.24, -6.35), (12.7, -6.35))
                Line((12.7, -6.35), (12.7, -7.62))
                Line((12.7, -7.62), (15.24, -7.62))
            make_face()
        # OneSide extrude, distance=-27.94
        extrude(amount=-27.94, mode=Mode.ADD)

        # Sketch7 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 57.15), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 3.2258, perimeter: 7.62
            with BuildLine():
                Line((-12.7, -6.35), (-12.7, -7.62))
                Line((-15.24, -6.35), (-12.7, -6.35))
                Line((-15.24, -7.62), (-15.24, -6.35))
                Line((-12.7, -7.62), (-15.24, -7.62))
            make_face()
        # OneSide extrude, distance=-27.94
        extrude(amount=-27.94, mode=Mode.ADD)

        # Sketch8 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -2.54), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            Circle(0.635)
        # OneSide extrude, distance=1.27
        extrude(amount=1.27, mode=Mode.ADD)

        # Sketch9 -> Extrude7 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -3.81), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 11.4009182797, perimeter: 11.9694680102
            Circle(1.905)
        # OneSide extrude, distance=1.27
        extrude(amount=1.27, mode=Mode.ADD)
    return part.part


def model_41714_1d49f4d1_0011():
    """Model: bird_sitting_stick"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0967740062, perimeter: 1.2700000405
            with BuildLine():
                Line((-3.4290001094, -0.3810000122), (-3.8100001216, -0.3810000122))
                Line((-3.8100001216, -0.3810000122), (-3.8100001216, -0.6350000203))
                Line((-3.8100001216, -0.6350000203), (-3.4290001094, -0.6350000203))
                Line((-3.4290001094, -0.6350000203), (-3.4290001094, -0.3810000122))
            make_face()
        # OneSide extrude, distance=3.81
        extrude(amount=3.81)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-3.4290001094, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.00064516, perimeter: 0.1015999988
            with BuildLine():
                Line((-0.495299994, 3.4035999589), (-0.5206999937, 3.4035999589))
                Line((-0.5206999937, 3.4035999589), (-0.5206999937, 3.3781999592))
                Line((-0.5206999937, 3.3781999592), (-0.495299994, 3.3781999592))
                Line((-0.495299994, 3.3781999592), (-0.495299994, 3.4035999589))
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-3.8100001216, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0007215713, perimeter: 0.107616636
            with BuildLine():
                Line((0.5237083123, 3.0352999633), (0.495299994, 3.0352999633))
                Line((0.495299994, 3.0352999633), (0.495299994, 3.0098999636))
                Line((0.495299994, 3.0098999636), (0.5237083123, 3.0098999636))
                Line((0.5237083123, 3.0098999636), (0.5237083123, 3.0352999633))
            make_face()
        # OneSide extrude, distance=1.27
        extrude(amount=1.27, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.3810000122), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.00064516, perimeter: 0.1015999988
            with BuildLine():
                Line((3.6067999564, 2.5399999693), (3.5813999567, 2.5399999693))
                Line((3.5813999567, 2.5399999693), (3.5813999567, 2.5145999696))
                Line((3.5813999567, 2.5145999696), (3.6067999564, 2.5145999696))
                Line((3.6067999564, 2.5145999696), (3.6067999564, 2.5399999693))
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635, mode=Mode.ADD)

        # Sketch6 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-3.4290001094, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0025806399, perimeter: 0.2031999975
            with BuildLine():
                Line((-0.4063999951, 2.9209999647), (-0.4571999945, 2.9209999647))
                Line((-0.4571999945, 2.9209999647), (-0.4571999945, 2.8701999653))
                Line((-0.4571999945, 2.8701999653), (-0.4063999951, 2.8701999653))
                Line((-0.4063999951, 2.8701999653), (-0.4063999951, 2.9209999647))
            make_face()
        # OneSide extrude, distance=0.762
        extrude(amount=0.762, mode=Mode.ADD)

        # Sketch7 -> Extrude7 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.3810000122), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.00016129, perimeter: 0.0508000003
            with BuildLine():
                Line((3.6068000225, 3.683000023), (3.5941000225, 3.683000023))
                Line((3.5941000225, 3.683000023), (3.5941000225, 3.6703000229))
                Line((3.5941000225, 3.6703000229), (3.6068000225, 3.6703000229))
                Line((3.6068000225, 3.6703000229), (3.6068000225, 3.683000023))
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635, mode=Mode.ADD)

        # Sketch8 -> Extrude8 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.6350000203), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0058064399, perimeter: 0.3047999963
            with BuildLine():
                Line((-3.5813999567, 1.9811999761), (-3.6575999558, 1.9811999761))
                Line((-3.6575999558, 1.9811999761), (-3.6575999558, 1.904999977))
                Line((-3.6575999558, 1.904999977), (-3.5813999567, 1.904999977))
                Line((-3.5813999567, 1.904999977), (-3.5813999567, 1.9811999761))
            make_face()
        # OneSide extrude, distance=0.762
        extrude(amount=0.762, mode=Mode.ADD)

        # Sketch9 -> Extrude9 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-3.4290001094, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0025806399, perimeter: 0.2031999975
            with BuildLine():
                Line((-0.4825999942, 0.6349999923), (-0.5333999936, 0.6349999923))
                Line((-0.5333999936, 0.6349999923), (-0.5333999936, 0.5841999929))
                Line((-0.5333999936, 0.5841999929), (-0.4825999942, 0.5841999929))
                Line((-0.4825999942, 0.5841999929), (-0.4825999942, 0.6349999923))
            make_face()
        # OneSide extrude, distance=0.381
        extrude(amount=0.381, mode=Mode.ADD)

        # Sketch10 -> Extrude10 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.3810000122), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0038709599, perimeter: 0.2539999969
            with BuildLine():
                Line((3.6575999558, 1.2699999847), (3.5813999567, 1.2699999847))
                Line((3.5813999567, 1.2699999847), (3.5813999567, 1.2191999853))
                Line((3.5813999567, 1.2191999853), (3.6575999558, 1.2191999853))
                Line((3.6575999558, 1.2191999853), (3.6575999558, 1.2699999847))
            make_face()
        # OneSide extrude, distance=0.508
        extrude(amount=0.508, mode=Mode.ADD)

        # Sketch11 -> Extrude11 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-3.8100001216, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0025806399, perimeter: 0.2031999975
            with BuildLine():
                Line((0.5333999936, 1.6763999797), (0.4825999942, 1.6763999797))
                Line((0.4825999942, 1.6763999797), (0.4825999942, 1.6255999804))
                Line((0.4825999942, 1.6255999804), (0.5333999936, 1.6255999804))
                Line((0.5333999936, 1.6255999804), (0.5333999936, 1.6763999797))
            make_face()
        # OneSide extrude, distance=0.254
        extrude(amount=0.254, mode=Mode.ADD)
    return part.part


def model_41759_f47f0249_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.1109998915, perimeter: 7.780142752
            with BuildLine():
                Line((0.4999999888, 0), (0.9899999779, 0.4999999888))
                Line((0.9899999779, 0.4999999888), (0.9899999779, 2.1999999888))
                Line((-0.9899999779, 2.1999999888), (0.9899999779, 2.1999999888))
                Line((-0.9899999779, 0.4999999888), (-0.9899999779, 2.1999999888))
                Line((-0.4999999888, 0), (-0.9899999779, 0.4999999888))
                Line((-0.4999999888, 0), (0.4999999888, 0))
            make_face()
        # OneSide extrude, distance=0.75
        extrude(amount=0.75)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.75, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.22, perimeter: 1.88
            with BuildLine():
                Line((0.22, 0), (0.22, -0.5))
                Line((0.22, 0), (-0.22, 0))
                Line((-0.22, 0), (-0.22, -0.5))
                Line((-0.22, -0.5), (0.22, -0.5))
            make_face()
        # OneSide extrude, distance=-0.55
        extrude(amount=-0.55, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.75, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.25, perimeter: 2
            with BuildLine():
                Line((0.25, -1.4000000171), (-0.25, -1.4000000171))
                Line((0.25, -0.9000000171), (0.25, -1.4000000171))
                Line((-0.25, -0.9000000171), (0.25, -0.9000000171))
                Line((-0.25, -1.4000000171), (-0.25, -0.9000000171))
            make_face()
        # OneSide extrude, distance=-0.02
        extrude(amount=-0.02, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.75, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2100000063, perimeter: 2.0000000298
            with BuildLine():
                Line((0.6000000089, -1.8500000276), (0.3000000045, -1.8500000276))
                Line((0.6000000089, -1.1500000171), (0.6000000089, -1.8500000276))
                Line((0.3000000045, -1.1500000171), (0.6000000089, -1.1500000171))
                Line((0.3000000045, -1.8500000276), (0.3000000045, -1.1500000171))
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.75, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0503999977, perimeter: 1.0799999759
            with BuildLine():
                Line((-0.6499999855, -0.6399999857), (-0.6499999855, -0.759999983))
                Line((-0.6499999855, -0.759999983), (-0.2299999949, -0.759999983))
                Line((-0.2299999949, -0.759999983), (-0.2299999949, -0.6399999857))
                Line((-0.2299999949, -0.6399999857), (-0.6499999855, -0.6399999857))
            make_face()
        # OneSide extrude, distance=-0.02
        extrude(amount=-0.02, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.22, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.096211275, perimeter: 1.0995574288
            with Locations((0.1899999958, 0.4599999897)):
                Circle(0.175)
        # OneSide extrude, distance=-0.06
        extrude(amount=-0.06, mode=Mode.SUBTRACT)

        # Sketch8 -> Extrude8 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.22, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.096211275, perimeter: 1.0995574288
            with Locations((0.1899999958, 0.4599999897)):
                Circle(0.175)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.SUBTRACT)

        # Sketch9 -> Extrude9 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 2.2698006922, perimeter: 5.3407075111
            with Locations((0, -1.2000000179)):
                Circle(0.85)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)
    return part.part


def model_41787_7d41b65c_0000():
    """Model: Arm v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.0342917353, perimeter: 10.7123889804
            with BuildLine():
                CenterArc((0, 0), 1.5, 90, 180)
                Line((0, -1.5), (1.5, -1.5))
                Line((1.5, -1.5), (1.5, 1.5))
                Line((0, 1.5), (1.5, 1.5))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 10.5, perimeter: 13
            with BuildLine():
                Line((5, -1.5), (1.5, -1.5))
                Line((5, 1.5), (5, -1.5))
                Line((1.5, 1.5), (5, 1.5))
                Line((1.5, -1.5), (1.5, 1.5))
            make_face()
        # OneSide extrude, distance=6
        extrude(amount=6, mode=Mode.ADD)

        # Sketch5 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.0342917348, perimeter: 10.7123897277
            with BuildLine():
                Line((-1.5, -1.5), (-1.5, 1.5))
                Line((-0.0000007475, -1.5), (-1.5, -1.5))
                CenterArc((0, 0), 1.5, -90.0000285531, 180.0000285472)
                Line((-1.5, 1.5), (0.0000000002, 1.5))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.ADD)

        # Sketch6 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch9 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4828541324, perimeter: 5.3561944902
            with BuildLine():
                Line((-1.5, 0), (-1.5, 1.5))
                CenterArc((0, 0), 1.5, 90, 90)
                Line((-1.5, 1.5), (0, 1.5))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch9 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4828541324, perimeter: 5.3561937427
            with BuildLine():
                Line((-1.5, -1.5), (-1.5, 0))
                Line((0, -1.5), (-1.5, -1.5))
                CenterArc((0, 0), 1.5, 180, 90)
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch9 -> Extrude8 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4828541324, perimeter: 5.3561944902
            with BuildLine():
                Line((-1.5, 0), (-1.5, 1.5))
                CenterArc((0, 0), 1.5, 90, 90)
                Line((-1.5, 1.5), (0, 1.5))
            make_face()
        # OneSide extrude, distance=4.5
        extrude(amount=4.5, mode=Mode.SUBTRACT)

        # Sketch9 -> Extrude9 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4828541324, perimeter: 5.3561937427
            with BuildLine():
                Line((-1.5, -1.5), (-1.5, 0))
                Line((0, -1.5), (-1.5, -1.5))
                CenterArc((0, 0), 1.5, 180, 90)
            make_face()
        # OneSide extrude, distance=4.5
        extrude(amount=4.5, mode=Mode.SUBTRACT)

        # Sketch10 -> Extrude10 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(1.5, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 15, perimeter: 16
            with BuildLine():
                Line((-1.5, 0.5), (1.5, 0.5))
                Line((1.5, 0.5), (1.5, 5.5))
                Line((-1.5, 5.5), (1.5, 5.5))
                Line((-1.5, 5.5), (-1.5, 0.5))
            make_face()
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)

        # Sketch11 -> Extrude11 (Join)
        # Sketch on BRepFace
        # Sketch has 13 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 5, perimeter: 20
            with BuildLine():
                Line((-1.5, 1.5), (1.5, 1.5))
                Line((1.5, 1.5), (1.5, 4.5))
                Line((1.5, 4.5), (-1.5, 4.5))
                Line((-1.5, 4.5), (-1.5, 1.5))
            make_face()
            with BuildLine():
                Line((-1, 2), (1, 2))
                Line((-1, 4), (-1, 2))
                Line((1, 4), (-1, 4))
                Line((1, 2), (1, 4))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


def model_41896_7d8659e6_0007():
    """Model: Front Wheel Pin v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.4417864669, perimeter: 2.3561944902
            Circle(0.375)
        # OneSide extrude, distance=3.8
        extrude(amount=3.8)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3.8), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.0975939333, perimeter: 6.7544242052
            with BuildLine():
                CenterArc((0, 0), 0.7, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.375, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch4 -> Extrude3 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 1.0975939333, perimeter: 6.7544242052
            with BuildLine():
                CenterArc((0, 0), 0.7, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.375, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch5 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 4.8), x_dir=(1, 0, 0), z_dir=(0, 0, 1))) as sk:
            # Profile area: 0.502777543, perimeter: 9.4640478689
            with BuildLine():
                CenterArc((0, 0), 0.80625, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.7, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides offset extrude, full=-0.4, trim=-0.3
        extrude(amount=-0.4, mode=Mode.ADD)
        extrude(sk.sketch, amount=-0.3, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 4.8), x_dir=(1, 0, 0), z_dir=(0, 0, 1))) as sk:
            # Profile area: 0.502777543, perimeter: 9.4640478689
            with BuildLine():
                CenterArc((0, 0), 0.80625, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.7, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides offset extrude, full=-0.2, trim=-0.1
        extrude(amount=-0.2, mode=Mode.ADD)
        extrude(sk.sketch, amount=-0.1, mode=Mode.SUBTRACT)

        # Sketch8 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -1), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))) as sk:
            # Profile area: 0.502777543, perimeter: 9.4640478689
            with BuildLine():
                CenterArc((0, 0), 0.80625, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.7, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides offset extrude, full=-0.4, trim=-0.3
        extrude(amount=-0.4, mode=Mode.ADD)
        extrude(sk.sketch, amount=-0.3, mode=Mode.SUBTRACT)

        # Sketch9 -> Extrude7 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -1), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))) as sk:
            # Profile area: 0.502777543, perimeter: 9.4640478689
            with BuildLine():
                CenterArc((0, 0), 0.80625, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.7, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides offset extrude, full=-0.2, trim=-0.1
        extrude(amount=-0.2, mode=Mode.ADD)
        extrude(sk.sketch, amount=-0.1, mode=Mode.SUBTRACT)
    return part.part


def model_43467_eb9b64c2_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 15 constraints, 20 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1065.915257439, perimeter: 144.5407373538
            with BuildLine():
                Line((0, 28.09875), (0, 0))
                Line((0, 0), (38.1, 0))
                Line((38.1, 0), (38.1, 28.09875))
                Line((38.1, 28.09875), (0, 28.09875))
            make_face()
            with BuildLine():
                CenterArc((2.54, 2.54), 0.61515625, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.35, 1.031875), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.35, 2.54), 0.3175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.201566528, perimeter: 7.3874060375
            with BuildLine():
                CenterArc((2.54, 2.54), 0.61515625, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((2.54, 2.54), 0.5605859375, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1828557111, perimeter: 6.7016552661
            with BuildLine():
                CenterArc((2.54, 2.54), 0.5605859375, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((2.54, 2.54), 0.506015625, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1641448941, perimeter: 6.0159044947
            with BuildLine():
                CenterArc((2.54, 2.54), 0.506015625, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((2.54, 2.54), 0.4514453125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1454340772, perimeter: 5.3301537233
            with BuildLine():
                CenterArc((2.54, 2.54), 0.4514453125, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((2.54, 2.54), 0.396875, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0244323064, perimeter: 4.9249373584
            with BuildLine():
                CenterArc((2.54, 2.54), 0.396875, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((2.54, 2.54), 0.386953125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.023813767, perimeter: 4.8002553999
            with BuildLine():
                CenterArc((2.54, 2.54), 0.386953125, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((2.54, 2.54), 0.37703125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0231952276, perimeter: 4.6755734415
            with BuildLine():
                CenterArc((2.54, 2.54), 0.37703125, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((2.54, 2.54), 0.367109375, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0225766882, perimeter: 4.550891483
            with BuildLine():
                CenterArc((2.54, 2.54), 0.367109375, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((2.54, 2.54), 0.3571875, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.4008135333, perimeter: 2.2442752519
            with Locations((2.54, 2.54)):
                Circle(0.3571875)
            # Profile area: 2.8249004792, perimeter: 8.2780966422
            with BuildLine():
                CenterArc((6.35, 1.031875), 1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((6.35, 1.031875), 0.3175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with Locations((6.35, 1.031875)):
                Circle(0.3175)
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with Locations((6.35, 2.54)):
                Circle(0.3175)
        # OneSide extrude, distance=-1.905
        extrude(amount=-1.905)

        # Sketch1 -> Extrude2 (Cut)
        # Sketch on XY construction plane
        # Sketch has 15 constraints, 20 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.201566528, perimeter: 7.3874060375
            with BuildLine():
                CenterArc((2.54, 2.54), 0.61515625, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((2.54, 2.54), 0.5605859375, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.635
        extrude(amount=-0.635, mode=Mode.SUBTRACT)

        # Sketch1 -> Extrude3 (Cut)
        # Sketch on XY construction plane
        # Sketch has 15 constraints, 20 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1828557111, perimeter: 6.7016552661
            with BuildLine():
                CenterArc((2.54, 2.54), 0.5605859375, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((2.54, 2.54), 0.506015625, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.6895703125
        extrude(amount=-0.6895703125, mode=Mode.SUBTRACT)

        # Sketch1 -> Extrude4 (Cut)
        # Sketch on XY construction plane
        # Sketch has 15 constraints, 20 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1641448941, perimeter: 6.0159044947
            with BuildLine():
                CenterArc((2.54, 2.54), 0.506015625, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((2.54, 2.54), 0.4514453125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.744140625
        extrude(amount=-0.744140625, mode=Mode.SUBTRACT)

        # Sketch1 -> Extrude5 (Cut)
        # Sketch on XY construction plane
        # Sketch has 15 constraints, 20 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1454340772, perimeter: 5.3301537233
            with BuildLine():
                CenterArc((2.54, 2.54), 0.4514453125, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((2.54, 2.54), 0.396875, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.7987109375
        extrude(amount=-0.7987109375, mode=Mode.SUBTRACT)

        # Sketch1 -> Extrude6 (Cut)
        # Sketch on XY construction plane
        # Sketch has 15 constraints, 20 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0244323064, perimeter: 4.9249373584
            with BuildLine():
                CenterArc((2.54, 2.54), 0.396875, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((2.54, 2.54), 0.386953125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.85328125
        extrude(amount=-0.85328125, mode=Mode.SUBTRACT)

        # Sketch1 -> Extrude7 (Cut)
        # Sketch on XY construction plane
        # Sketch has 15 constraints, 20 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.023813767, perimeter: 4.8002553999
            with BuildLine():
                CenterArc((2.54, 2.54), 0.386953125, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((2.54, 2.54), 0.37703125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-1.27396875
        extrude(amount=-1.27396875, mode=Mode.SUBTRACT)

        # Sketch1 -> Extrude8 (Cut)
        # Sketch on XY construction plane
        # Sketch has 15 constraints, 20 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0231952276, perimeter: 4.6755734415
            with BuildLine():
                CenterArc((2.54, 2.54), 0.37703125, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((2.54, 2.54), 0.367109375, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-1.4843125
        extrude(amount=-1.4843125, mode=Mode.SUBTRACT)

        # Sketch1 -> Extrude9 (Cut)
        # Sketch on XY construction plane
        # Sketch has 15 constraints, 20 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0225766882, perimeter: 4.550891483
            with BuildLine():
                CenterArc((2.54, 2.54), 0.367109375, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((2.54, 2.54), 0.3571875, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-1.69465625
        extrude(amount=-1.69465625, mode=Mode.SUBTRACT)

        # Sketch1 -> Extrude10 (Cut)
        # Sketch on XY construction plane
        # Sketch has 15 constraints, 20 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.4008135333, perimeter: 2.2442752519
            with Locations((2.54, 2.54)):
                Circle(0.3571875)
        # OneSide extrude, distance=-1.905
        extrude(amount=-1.905, mode=Mode.SUBTRACT)

        # Sketch1 -> Extrude11 (Cut)
        # Sketch on XY construction plane
        # Sketch has 15 constraints, 20 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with Locations((6.35, 1.031875)):
                Circle(0.3175)
        # OneSide extrude, distance=-1.905
        extrude(amount=-1.905, mode=Mode.SUBTRACT)

        # Sketch1 -> Extrude12 (Cut)
        # Sketch on XY construction plane
        # Sketch has 15 constraints, 20 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.8249004792, perimeter: 8.2780966422
            with BuildLine():
                CenterArc((6.35, 1.031875), 1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((6.35, 1.031875), 0.3175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-1.27
        extrude(amount=-1.27, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude13 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with Locations((-2.54, -6.35)):
                Circle(0.3175)
        # OneSide extrude, distance=-1.5875
        extrude(amount=-1.5875, mode=Mode.SUBTRACT)

        # Sketch1 -> Extrude14 (Cut)
        # Sketch on XY construction plane
        # Sketch has 15 constraints, 20 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with Locations((6.35, 2.54)):
                Circle(0.3175)
        # OneSide extrude, distance=-1.5875
        extrude(amount=-1.5875, mode=Mode.SUBTRACT)
    return part.part


def model_43529_4804941b_0056():
    """Model: Solid53_Torno triple"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.6376619848, perimeter: 4.5364597918
            Circle(0.722)
        # OneSide extrude, distance=0.18
        extrude(amount=0.18)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.18, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0826741523, perimeter: 9.1860169191
            with BuildLine():
                CenterArc((0, 0), 0.74, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.722, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.6376619848, perimeter: 4.5364597918
            Circle(0.722)
        # OneSide extrude, distance=0.305
        extrude(amount=0.305, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.485, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.8824733764, perimeter: 3.3300882128
            Circle(0.53)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.885, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4448495197, perimeter: 7.4141586625
            with BuildLine():
                CenterArc((0, 0), 0.65, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.53, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.8824733764, perimeter: 3.3300882128
            Circle(0.53)
        # OneSide extrude, distance=0.675
        extrude(amount=0.675, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.56, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4536459792, perimeter: 2.3876104167
            Circle(0.38)
        # OneSide extrude, distance=0.22
        extrude(amount=0.22, mode=Mode.ADD)

        # Sketch6 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.78, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.873676917, perimeter: 6.4716808664
            with BuildLine():
                CenterArc((0, 0), 0.65, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.38, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.4536459792, perimeter: 2.3876104167
            Circle(0.38)
        # OneSide extrude, distance=0.11
        extrude(amount=0.11, mode=Mode.ADD)

        # Sketch7 -> Extrude7 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.89, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.2154319322, perimeter: 3.9081412611
            Circle(0.622)
        # OneSide extrude, distance=1.31
        extrude(amount=1.31, mode=Mode.ADD)

        # Sketch8 -> Extrude8 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            Circle(0.6)
        # OneSide extrude, distance=0.115
        extrude(amount=0.115, mode=Mode.ADD)

        # Sketch9 -> Extrude9 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3.315, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.08552986, perimeter: 1.0367255757
            Circle(0.165)
        # OneSide extrude, distance=0.28
        extrude(amount=0.28, mode=Mode.ADD)
    return part.part


def model_43928_6ca53538_0015():
    """Model: spindle crossmember v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0113097336, perimeter: 0.3769911184
            Circle(0.06)
        # OneSide extrude, distance=0.23
        extrude(amount=0.23)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.23), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0018095574, perimeter: 0.1507964474
            Circle(0.024)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.43), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0095001762, perimeter: 0.5277875658
            with BuildLine():
                CenterArc((0, 0), 0.06, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.024, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0018095574, perimeter: 0.1507964474
            Circle(0.024)
        # OneSide extrude, distance=0.295
        extrude(amount=0.295, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.725), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0018095574, perimeter: 0.1507964474
            Circle(0.024)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.825), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0158619013, perimeter: 0.6220353454
            with BuildLine():
                CenterArc((0, 0), 0.075, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.024, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0018095574, perimeter: 0.1507964474
            Circle(0.024)
        # OneSide extrude, distance=0.45
        extrude(amount=0.45, mode=Mode.ADD)

        # Sketch6 -> Extrude6 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 1.275), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0018095574, perimeter: 0.1507964474
            Circle(0.024)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch7 -> Extrude7 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 1.375), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0095001762, perimeter: 0.5277875658
            with BuildLine():
                CenterArc((0, 0), 0.06, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.024, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0018095574, perimeter: 0.1507964474
            Circle(0.024)
        # OneSide extrude, distance=0.295
        extrude(amount=0.295, mode=Mode.ADD)

        # Sketch8 -> Extrude8 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 1.67), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0018095574, perimeter: 0.1507964474
            Circle(0.024)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch9 -> Extrude9 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 1.87), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0095001762, perimeter: 0.5277875658
            with BuildLine():
                CenterArc((0, 0), 0.06, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.024, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0018095574, perimeter: 0.1507964474
            Circle(0.024)
        # OneSide extrude, distance=0.23
        extrude(amount=0.23, mode=Mode.ADD)
    return part.part


def model_43928_6ca53538_0025():
    """Model: Spool Drive Spindle v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0683492752, perimeter: 0.9267698328
            Circle(0.1475)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.8), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0660519855, perimeter: 0.9110618695
            Circle(0.145)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.9), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0274300309, perimeter: 1.994911335
            with BuildLine():
                CenterArc((0, 0), 0.1725, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.145, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0660519855, perimeter: 0.9110618695
            Circle(0.145)
        # OneSide extrude, distance=1.3
        extrude(amount=1.3, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0660519855, perimeter: 0.9110618695
            Circle(0.145)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1263901994, perimeter: 2.4661502331
            with BuildLine():
                CenterArc((0, 0), 0.2475, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.145, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0660519855, perimeter: 0.9110618695
            Circle(0.145)
        # OneSide extrude, distance=0.375
        extrude(amount=0.375, mode=Mode.ADD)

        # Sketch6 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.675), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.139388539, perimeter: 3.5971235884
            with BuildLine():
                CenterArc((0, 0), 0.325, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2475, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.192442185, perimeter: 1.5550883635
            Circle(0.2475)
        # OneSide extrude, distance=3.1
        extrude(amount=3.1, mode=Mode.ADD)

        # Sketch7 -> Extrude7 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 5.775), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.2248005893, perimeter: 1.6807520697
            Circle(0.2675)
        # OneSide extrude, distance=0.54
        extrude(amount=0.54, mode=Mode.ADD)

        # Sketch8 -> Extrude8 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 6.315), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0683492752, perimeter: 0.9267698328
            Circle(0.1475)
        # OneSide extrude, distance=1.8
        extrude(amount=1.8, mode=Mode.ADD)

        # Sketch9 -> Extrude10 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 17 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0833998788, perimeter: 1.2454201896
            with BuildLine():
                Line((-5.8677756814, -0.2675), (-6.015, -0.1825))
                Line((-6.015, -0.1825), (-6.315, -0.1825))
                Line((-6.3943357144, -0.3574457213), (-6.315, -0.1825))
                Line((-6.1021255751, -0.3867967018), (-6.3943357144, -0.3574457213))
                Line((-5.907190094, -0.349770766), (-6.1021255751, -0.3867967018))
                Line((-5.8677756814, -0.2675), (-5.907190094, -0.349770766))
            make_face()
            # Profile area: 0.0833998788, perimeter: 1.2454201896
            with BuildLine():
                Line((-6.015, 0.1825), (-6.315, 0.1825))
                Line((-5.8677756814, 0.2675), (-6.015, 0.1825))
                Line((-5.8677756814, 0.2675), (-5.907190094, 0.349770766))
                Line((-5.907190094, 0.349770766), (-6.1021255751, 0.3867967018))
                Line((-6.1021255751, 0.3867967018), (-6.3943357144, 0.3574457213))
                Line((-6.3943357144, 0.3574457213), (-6.315, 0.1825))
            make_face()
        # Symmetric extrude, each_side=-0.8
        extrude(amount=-0.8, both=True, mode=Mode.SUBTRACT)

        # Sketch11 -> Extrude11 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0176714587, perimeter: 0.471238898
            with Locations((0, -2.45)):
                Circle(0.075)
        # Symmetric extrude, each_side=1.3
        extrude(amount=1.3, both=True, mode=Mode.SUBTRACT)
    return part.part


def model_45303_48d14b32_0001():
    """Model: central profile"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 25, perimeter: 20
            with BuildLine():
                Line((2.5, -2.5), (-2.5, -2.5))
                Line((2.5, 2.5), (2.5, -2.5))
                Line((-2.5, 2.5), (2.5, 2.5))
                Line((-2.5, -2.5), (-2.5, 2.5))
            make_face()
        # OneSide extrude, distance=190
        extrude(amount=190)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 190, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 13.69, perimeter: 14.8
            with BuildLine():
                Line((1.85, -1.85), (1.85, 1.85))
                Line((1.85, 1.85), (-1.85, 1.85))
                Line((-1.85, 1.85), (-1.85, -1.85))
                Line((-1.85, -1.85), (1.85, -1.85))
            make_face()
        # OneSide extrude, distance=-190
        extrude(amount=-190, mode=Mode.SUBTRACT)

        # Sketch14 -> Extrude11 (Join)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 5, perimeter: 12
            with BuildLine():
                Line((-2.05, 19.9785715186), (-2.05, 14.9785715186))
                Line((-2.05, 14.9785715186), (-1.05, 14.9785715186))
                Line((-1.05, 14.9785715186), (-1.05, 19.9785715186))
                Line((-1.05, 19.9785715186), (-2.05, 19.9785715186))
            make_face()
            # Profile area: 5, perimeter: 12
            with BuildLine():
                Line((2.0500018045, 14.9785715186), (1.0500018045, 14.9785715186))
                Line((2.0500018045, 19.9785715186), (2.0500018045, 14.9785715186))
                Line((1.0500018045, 19.9785715186), (2.0500018045, 19.9785715186))
                Line((1.0500018045, 14.9785715186), (1.0500018045, 19.9785715186))
            make_face()
        # OneSide extrude, distance=10
        extrude(amount=10, mode=Mode.ADD)

        # Sketch16 -> Extrude12 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-1.05, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 9.6211275016, perimeter: 10.9955742876
            with Locations((-10, 17.4785715186)):
                Circle(1.75)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch17 -> Extrude13 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1.0500018045, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 9.6211275016, perimeter: 10.9955742876
            with Locations((10, 17.4785715186)):
                Circle(1.75)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch18 -> Extrude14 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.5500018045, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 1.3273228961, perimeter: 4.0840704497
            with Locations((10, 17.4785715186)):
                Circle(0.65)
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.SUBTRACT)

        # Sketch20 -> Extrude16 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-2.05, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 1.3273228961, perimeter: 4.0840704497
            with Locations((10, 17.4785715186)):
                Circle(0.65)
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.SUBTRACT)
    return part.part


def model_45359_1768ab3f_0028():
    """Model: Valve"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.703647609, perimeter: 3.054590436
            with BuildLine():
                Line((-0.4, -0.3), (-0.4, 0.3))
                CenterArc((0, 0), 0.5, -143.1301023542, 106.2602047083)
                Line((0.4, -0.3), (0.4, 0.3))
                CenterArc((0, 0), 0.5, 36.8698976458, 106.2602047083)
            make_face()
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.4, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0628318531, perimeter: 1.0283185307
            with BuildLine():
                CenterArc((0, 0.4), 0.2, 90, 180)
                Line((0, 0.2), (0, 0.6))
            make_face()
            # Profile area: 0.0628318531, perimeter: 1.0283185307
            with BuildLine():
                Line((0, 0.2), (0, 0.6))
                CenterArc((0, 0.4), 0.2, -90, 180)
            make_face()
        # OneSide extrude, distance=-2.1
        extrude(amount=-2.1, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=1.8
        extrude(amount=1.8, mode=Mode.ADD)

        # Sketch7 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -1.8, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.2120575041, perimeter: 2.8274333882
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8, mode=Mode.ADD)

        # Sketch8 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -2.6, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=3.4
        extrude(amount=3.4, mode=Mode.ADD)

        # Sketch9 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -6, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.2120575041, perimeter: 2.8274333882
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8, mode=Mode.ADD)
    return part.part


def model_48526_d1248549_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 72.3822947387, perimeter: 90.4778684234
            with BuildLine():
                CenterArc((0, 0), 8, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 6.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3.5
        extrude(amount=3.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 3.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 128.679635091, perimeter: 40.2123859659
            Circle(6.4)
        # OneSide extrude, distance=-3.5
        extrude(amount=-3.5, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 3.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 128.679635091, perimeter: 40.2123859659
            Circle(6.4)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude4 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 45.3645979178, perimeter: 23.8761041673
            Circle(3.8)
        # OneSide extrude, distance=4
        extrude(amount=4, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 60.3185789489, perimeter: 60.3185789489
            with BuildLine():
                CenterArc((0, 0), 5.8, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-4
        extrude(amount=-4, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 60.3185789489, perimeter: 60.3185789489
            with BuildLine():
                CenterArc((0, 0), 5.8, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-3.3
        extrude(amount=-3.3, mode=Mode.ADD)

        # Sketch6 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 60.3185789489, perimeter: 60.3185789489
            with BuildLine():
                CenterArc((0, 0), 5.8, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-3.3
        extrude(amount=-3.3, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude8 (Join)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 60.3185789489, perimeter: 60.3185789489
            with BuildLine():
                CenterArc((0, 0), 5.8, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch9 -> Extrude9 (Join)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 22.4623874732, perimeter: 40.8407044967
            with BuildLine():
                CenterArc((0, 0), 3.8, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.7, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


def model_48907_25974aa4_0010():
    """Model: left frame v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 13.5, perimeter: 22
            with BuildLine():
                Line((0, 0), (-3, 0))
                Line((-3, 0), (-3, -8))
                Line((-1.5, -8), (-3, -8))
                Line((-1.5, -1), (-1.5, -8))
                Line((0, -1), (-1.5, -1))
                Line((0, 0), (0, -1))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.75, perimeter: 3.5
            with BuildLine():
                Line((0, 0), (0, 1))
                Line((0, 1), (-0.75, 1))
                Line((-0.75, 1), (-0.75, 0))
                Line((-0.75, 0), (0, 0))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.5, perimeter: 3
            with BuildLine():
                Line((0.75, -0.75), (0.25, -0.75))
                Line((0.75, 0), (0.75, -0.75))
                Line((0.75, 0.25), (0.75, 0))
                Line((0.25, 0.25), (0.75, 0.25))
                Line((0.25, -0.75), (0.25, 0.25))
            make_face()
        # OneSide extrude, distance=1.25
        extrude(amount=1.25, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.25, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.2042820623, perimeter: 1.6022122533
            with Locations((0.75, -0.2514944591)):
                Circle(0.255)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1963495467, perimeter: 1.5707963502
            with Locations((-0.5000000075, -0.5000000075)):
                Circle(0.2500000037)
        # OneSide extrude, distance=-0.6
        extrude(amount=-0.6, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.8, perimeter: 3.6
            with BuildLine():
                Line((-1.5, 2.9), (-2.5, 2.9))
                Line((-2.5, 2.9), (-2.5, 2.1))
                Line((-2.5, 2.1), (-1.5, 2.1))
                Line((-1.5, 2.9), (-1.5, 2.1))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)

        # Sketch7 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-1.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-2.5000000373, -0.2)):
                Circle(0.15)
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.SUBTRACT)

        # Sketch8 -> Extrude8 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-1.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.08, perimeter: 1.3656854249
            with BuildLine():
                Line((-3.3, 0), (-2.9, -0.4))
                Line((-2.9, -0.4), (-2.9, 0))
                Line((-2.9, 0), (-3.3, 0))
            make_face()
            # Profile area: 0.08, perimeter: 1.3656854249
            with BuildLine():
                Line((-2.1, -0.4), (-2.1, 0))
                Line((-1.7, 0), (-2.1, -0.4))
                Line((-2.1, 0), (-1.7, 0))
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.ADD)

        # Sketch9 -> Extrude9 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 8), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.14, perimeter: 1.8
            with BuildLine():
                Line((-1.5, 0.35), (-2.2, 0.35))
                Line((-2.2, 0.35), (-2.2, 0.15))
                Line((-2.2, 0.15), (-1.5, 0.15))
                Line((-1.5, 0.15), (-1.5, 0.35))
            make_face()
        # OneSide extrude, distance=-5
        extrude(amount=-5, mode=Mode.SUBTRACT)

        # Sketch10 -> Extrude10 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 1.5150000452, perimeter: 6.3000000939
            with BuildLine():
                Line((-2.7000000402, 0.2500000037), (-1.0000000149, 0.2500000037))
                Line((-1.0000000149, 0.2500000037), (-1.0000000149, 0.7500000112))
                Line((-1.0000000149, 0.7500000112), (-2.0000000298, 0.7500000112))
                Line((-2.0000000298, 0.7500000112), (-2.0000000298, 1.7000000253))
                Line((-2.0000000298, 1.7000000253), (-2.7000000402, 1.7000000253))
                Line((-2.7000000402, 1.7000000253), (-2.7000000402, 0.2500000037))
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)
    return part.part


def model_49019_748c9a9f_0002():
    """Model: do kulki v7"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.7629328468, perimeter: 5.8923711811
            Circle(0.9378)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.7, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.0721996351, perimeter: 8.8385567716
            with BuildLine():
                CenterArc((0, 0), 0.9378, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.4689, -180, 180)
                CenterArc((0, 0), 0.4689, 0, 180)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-4.6
        extrude(amount=-4.6, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.7, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.3198861465, perimeter: 7.9727339112
            with BuildLine():
                CenterArc((0, 0), 0.8000000119, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.4689, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.9
        extrude(amount=0.9)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.7, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433472, perimeter: 1.8849556202
            Circle(0.3000000045)
        # OneSide extrude, distance=-1.1
        extrude(amount=-1.1, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.3198861465, perimeter: 7.9727339112
            with BuildLine():
                CenterArc((0, 0), 0.8000000119, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.4689, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.6907332117, perimeter: 2.9461855905
            Circle(0.4689)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on YZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1260334005, perimeter: 1.2584841759
            with Locations((0, 1.1108478821)):
                Circle(0.2002939774)
        # Symmetric extrude, each_side=2.2
        extrude(amount=2.2, both=True, mode=Mode.SUBTRACT)

        # Sketch8 -> Extrude7 (Cut)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.1256637099, perimeter: 1.2566370802
            with Locations((0, 1.1000000164)):
                Circle(0.200000003)
        # Symmetric extrude, each_side=6.7
        extrude(amount=6.7, both=True, mode=Mode.SUBTRACT)
    return part.part


def model_51559_4293c0e0_0005():
    """Model: Piston v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            Circle(2)
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 15.7079632679, perimeter: 31.4159265359
            with BuildLine():
                CenterArc((0, 0), 3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            Circle(2)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -0.5, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 8, perimeter: 12
            with BuildLine():
                Line((1, -2), (1, 2))
                Line((1, 2), (-1, 2))
                Line((-1, 2), (-1, -2))
                Line((-1, -2), (1, -2))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -2.5, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 5.2134278601, perimeter: 10.6067139301
            with BuildLine():
                Line((0.6516784825, -2), (0.6516784825, 2))
                Line((0.6516784825, 2), (-0.6516784825, 2))
                Line((-0.6516784825, 2), (-0.6516784825, -2))
                Line((-0.6516784825, -2), (0.6516784825, -2))
            make_face()
        # OneSide extrude, distance=-1.8
        extrude(amount=-1.8, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((0, -1.6335286541)):
                Circle(0.25)
        # OneSide extrude, distance=-7
        extrude(amount=-7, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=13
        extrude(amount=13, mode=Mode.ADD)

        # Sketch7 -> Extrude7 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3455752106, perimeter: 4.6948815264
            with BuildLine():
                CenterArc((0, 0), 0.4472136022, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=12
        extrude(amount=12, mode=Mode.ADD)

        # Sketch8 -> Extrude8 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0078539629, perimeter: 5.6373593225
            with BuildLine():
                CenterArc((0, 0), 0.45, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.4472136022, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=12
        extrude(amount=12, mode=Mode.ADD)
    return part.part


def model_52230_60438ea5_0008():
    """Model: seat mounting"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 137.5, perimeter: 65
            with BuildLine():
                Line((-85, 10), (-90, 10))
                Line((-85, 37.5), (-85, 10))
                Line((-90, 37.5), (-85, 37.5))
                Line((-90, 10), (-90, 37.5))
            make_face()
            # Profile area: 137.5, perimeter: 65
            with BuildLine():
                Line((-60, 10), (-60, 37.5))
                Line((-60, 37.5), (-65, 37.5))
                Line((-65, 37.5), (-65, 10))
                Line((-65, 10), (-60, 10))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 26.2805667191, perimeter: 56.9113139432
            with BuildLine():
                Line((-85.9556569716, 10), (-85.9556569716, 37.5))
                Line((-85, 10), (-85.9556569716, 10))
                Line((-85, 10), (-85, 37.5))
                Line((-85.9556569716, 37.5), (-85, 37.5))
            make_face()
            # Profile area: 577.5, perimeter: 97
            with BuildLine():
                Line((-85, 10), (-85, 37.5))
                Line((-64, 10), (-85, 10))
                Line((-64, 37.5), (-64, 10))
                Line((-85, 37.5), (-64, 37.5))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((-75, 24)):
                Circle(1)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-88, 30)):
                Circle(0.25)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-62, 17.5)):
                Circle(0.25)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-62, 30)):
                Circle(0.25)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-88, 17.5)):
                Circle(0.25)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 3.0784464758, perimeter: 6.762038648
            with BuildLine():
                CenterArc((-68.8556393965, 24.0000003576), 1, 135.5729951623, 88.8540096753)
                Line((-69.5697822291, 23.3000003472), (-67.7000010088, 23.3000003472))
                CenterArc((-68.8556393965, 24.0000003576), 1.3511106904, -31.2043718124, 62.4087436247)
                Line((-69.5697822291, 24.7000003681), (-67.7000010088, 24.7000003681))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0600000018, perimeter: 1.4000000209
            with BuildLine():
                Line((70.9000010565, 23.9000003561), (70.3000010476, 23.9000003561))
                Line((70.9000010565, 24.0000003576), (70.9000010565, 23.9000003561))
                Line((70.3000010476, 24.0000003576), (70.9000010565, 24.0000003576))
                Line((70.3000010476, 23.9000003561), (70.3000010476, 24.0000003576))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)

        # Sketch6 -> Extrude7 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 23.9000003561, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0314159275, perimeter: 0.6283185401
            with Locations((-70.600001052, 0.8000000119)):
                Circle(0.1000000015)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch11 -> Extrude10 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-72.4911722892, 14.9856660524)):
                Circle(0.25)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-77.9910702515, 14.9521637479)):
                Circle(0.25)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)
    return part.part


def model_52543_3ad80ce5_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4500, perimeter: 280
            with BuildLine():
                Line((45, -25), (45, 25))
                Line((45, 25), (-45, 25))
                Line((-45, 25), (-45, -25))
                Line((-45, -25), (45, -25))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 3825, perimeter: 260
            with BuildLine():
                Line((42.5, -22.5), (42.5, 22.5))
                Line((42.5, 22.5), (-42.5, 22.5))
                Line((-42.5, 22.5), (-42.5, -22.5))
                Line((-42.5, -22.5), (42.5, -22.5))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 15, perimeter: 23
            with BuildLine():
                Line((5, -25), (5, -23.5))
                Line((5, -23.5), (-5, -23.5))
                Line((-5, -23.5), (-5, -25))
                Line((-5, -25), (5, -25))
            make_face()
            # Profile area: 15, perimeter: 23
            with BuildLine():
                Line((-5, -25), (5, -25))
                Line((-5, -25), (-5, -26.5))
                Line((-5, -26.5), (5, -26.5))
                Line((5, -26.5), (5, -25))
            make_face()
        # OneSide extrude, distance=1.2
        extrude(amount=1.2, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 75, perimeter: 40
            with BuildLine():
                Line((-7.5, -12.5), (7.5, -12.5))
                Line((-7.5, -17.5), (-7.5, -12.5))
                Line((7.5, -17.5), (-7.5, -17.5))
                Line((7.5, -12.5), (7.5, -17.5))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.5399612373, perimeter: 8.6393797974
            with BuildLine():
                CenterArc((25, 0), 0.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((25, 0), 0.625, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.5399612373, perimeter: 8.6393797974
            with BuildLine():
                CenterArc((28, 0), 0.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((28, 0), 0.625, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.5399612373, perimeter: 8.6393797974
            with BuildLine():
                CenterArc((31, 0), 0.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((31, 0), 0.625, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.5399612373, perimeter: 8.6393797974
            with BuildLine():
                CenterArc((31, -2), 0.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((31, -2), 0.625, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.5399612373, perimeter: 8.6393797974
            with BuildLine():
                CenterArc((28, -2), 0.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((28, -2), 0.625, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.5399612373, perimeter: 8.6393797974
            with BuildLine():
                CenterArc((25, -2), 0.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((25, -2), 0.625, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 6.2831853072, perimeter: 12.5663706144
            with BuildLine():
                CenterArc((32, -8), 1.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((32, -8), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.SUBTRACT)

        # Sketch8 -> Extrude8 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 100, perimeter: 50
            with BuildLine():
                Line((10, -25), (10, -20))
                Line((10, -20), (-10, -20))
                Line((-10, -20), (-10, -25))
                Line((-10, -25), (10, -25))
            make_face()
            # Profile area: 100, perimeter: 50
            with BuildLine():
                Line((-10, -25), (10, -25))
                Line((-10, -25), (-10, -30))
                Line((-10, -30), (10, -30))
                Line((10, -30), (10, -25))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)

        # Sketch9 -> Extrude9 (NewBody)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -30, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 1085, perimeter: 184
            with BuildLine():
                Line((22.5, -7.5), (22.5, 17.5))
                Line((22.5, 17.5), (-22.5, 17.5))
                Line((-22.5, 17.5), (-22.5, -7.5))
                Line((-22.5, -7.5), (22.5, -7.5))
            make_face()
            with BuildLine():
                Line((10, 7), (-10, 7))
                Line((10, 5), (10, 7))
                Line((-10, 5), (10, 5))
                Line((-10, 7), (-10, 5))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)
    return part.part


def model_54034_b4473013_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 13 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 79.3561944902, perimeter: 40.7123889804
            with BuildLine():
                CenterArc((-2.5, 4), 1, 90, 90)
                Line((-3.5, 1), (-3.5, 4))
                CenterArc((-2.5, 1), 1, -180, 90)
                Line((12.5, 0), (-2.5, 0))
                Line((12.5, 4), (12.5, 0))
                CenterArc((11.5, 4), 1, 0, 90)
                Line((-2.5, 5), (11.5, 5))
            make_face()
        # Symmetric extrude, each_side=3
        extrude(amount=3, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 9 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -3), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 3.0002050945, perimeter: 6.6548068662
            with BuildLine():
                Line((-8.900762377, 0.4590531057), (-8.900762377, 0))
                CenterArc((-10, 0.5), 1.1, -2.1332967079, 181.0656937346)
                Line((-11.0998090479, 0.5204953197), (-11.0998090479, 0.4795046803))
                Line((-11.0998090479, 0.4795046803), (-11.0998090479, 0))
                Line((-11.0998090479, 0), (-8.900762377, 0))
            make_face()
            # Profile area: 0.0000052183, perimeter: 0.0819836507
            with BuildLine():
                Line((-11.0998090479, 0.5204953197), (-11.0998090479, 0.4795046803))
                CenterArc((-10, 0.5), 1.1, 178.9323970266, 2.1352059468)
            make_face()
            # Profile area: 2.9933128989, perimeter: 6.6251345894
            with BuildLine():
                Line((-0.099952775, 0), (2.0683790907, 0))
                Line((2.0683790907, 0), (2.0974373481, 0.4249582321))
                CenterArc((1, 0.5), 1.1, -3.9117441704, 184.4426636129)
                Line((-0.099952775, 0.4898072243), (-0.099952775, 0))
            make_face()
        # OneSide extrude, distance=-14.5
        extrude(amount=-14.5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 15, perimeter: 23
            with BuildLine():
                Line((11.7891273393, 2.5649970701), (1.7891273393, 2.5649970701))
                Line((11.7891273393, 4.0649970701), (11.7891273393, 2.5649970701))
                Line((1.7891273393, 4.0649970701), (11.7891273393, 4.0649970701))
                Line((1.7891273393, 2.5649970701), (1.7891273393, 4.0649970701))
            make_face()
            # Profile area: 2.6463495408, perimeter: 6.3853981634
            with BuildLine():
                Line((-1.8, 4.0447552802), (-0.5, 4.0447552802))
                CenterArc((-1.8, 3.5447552802), 0.5, 90, 90)
                Line((-2.3, 2.5447552802), (-2.3, 3.5447552802))
                Line((-0.5, 2.5447552802), (-2.3, 2.5447552802))
                Line((-0.5, 4.0447552802), (-0.5, 2.5447552802))
            make_face()
        # OneSide extrude, distance=-22
        extrude(amount=-22, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude5 (NewBody)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -3), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.4073855856, perimeter: 2.2625998878
            with Locations((-10, 0.5)):
                Circle(0.3601039564)
            # Profile area: 0.3769818828, perimeter: 2.1765325758
            with Locations((1, 0.5)):
                Circle(0.3464059182)
        # Symmetric extrude, each_side=0.2
        extrude(amount=0.2, both=True)

        # Sketch5 -> Extrude8 (NewBody)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 15, perimeter: 23
            with BuildLine():
                Line((1.7891273393, 4.0649970701), (11.7891273393, 4.0649970701))
                Line((1.7891273393, 2.5649970701), (1.7891273393, 4.0649970701))
                Line((11.7891273393, 2.5649970701), (1.7891273393, 2.5649970701))
                Line((11.7891273393, 4.0649970701), (11.7891273393, 2.5649970701))
            make_face()
            # Profile area: 2.6463495408, perimeter: 6.3853981634
            with BuildLine():
                CenterArc((-1.8, 3.5447552802), 0.5, 90, 90)
                Line((-2.3, 2.5447552802), (-2.3, 3.5447552802))
                Line((-0.5, 2.5447552802), (-2.3, 2.5447552802))
                Line((-0.5, 4.0447552802), (-0.5, 2.5447552802))
                Line((-1.8, 4.0447552802), (-0.5, 4.0447552802))
            make_face()
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)

        # Sketch12 -> Extrude12 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0700000021, perimeter: 1.6000000238
            with BuildLine():
                Line((-2.9000000432, 3.4000000507), (-3.0000000447, 3.4000000507))
                Line((-2.9000000432, 4.1000000611), (-2.9000000432, 3.4000000507))
                Line((-3.0000000447, 4.1000000611), (-2.9000000432, 4.1000000611))
                Line((-3.0000000447, 3.4000000507), (-3.0000000447, 4.1000000611))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)

        # Sketch13 -> Extrude13 (Join)
        # Sketch on BRepFace
        # Sketch has 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-3.5, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((-2, 1.5)):
                Circle(0.4)
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((2, 1.5)):
                Circle(0.4)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch14 -> Extrude14 (Join)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-3.5, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0799999973, perimeter: 1.1999999732
            with BuildLine():
                Line((-2.6, 1.4000000268), (-2.8, 1.4000000268))
                Line((-2.6, 1.8), (-2.6, 1.4000000268))
                Line((-2.8, 1.8000000268), (-2.6, 1.8))
                Line((-2.8, 1.4000000268), (-2.8, 1.8000000268))
            make_face()
            # Profile area: 0.0800000024, perimeter: 1.2000000179
            with BuildLine():
                Line((2.8000000417, 1.4000000209), (2.6000000387, 1.4000000209))
                Line((2.8000000417, 1.8000000268), (2.8000000417, 1.4000000209))
                Line((2.6000000387, 1.8000000268), (2.8000000417, 1.8000000268))
                Line((2.6000000387, 1.4000000209), (2.6000000387, 1.8000000268))
            make_face()
        # OneSide extrude, distance=0.15
        extrude(amount=0.15, mode=Mode.ADD)

        # Sketch17 -> Extrude17 (Join)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(12.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.5, perimeter: 3
            with BuildLine():
                Line((-1.7, 0.55), (-2.7, 0.55))
                Line((-1.7, 1.05), (-1.7, 0.55))
                Line((-2.7, 1.05), (-1.7, 1.05))
                Line((-2.7, 0.55), (-2.7, 1.05))
            make_face()
            # Profile area: 0.5, perimeter: 3
            with BuildLine():
                Line((1.7000000402, 1.05), (2.7000000402, 1.05))
                Line((1.7000000402, 0.55), (1.7000000402, 1.05))
                Line((2.7000000402, 0.55), (1.7000000402, 0.55))
                Line((2.7000000402, 1.05), (2.7000000402, 0.55))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch18 -> Extrude18 (Join)
        # Sketch on BRepFace
        # Sketch has 20 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(12.6, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-2.0000000298, 0.8000000119)):
                Circle(0.2)
            # Profile area: 0.0402389801, perimeter: 0.842237899
            with BuildLine():
                Line((-2.5846735043, 0.9465570353), (-2.5846735043, 0.8))
                Line((-2.5846735043, 0.8), (-2.3101115901, 0.8))
                Line((-2.3101115901, 0.8), (-2.3101115901, 0.9465570353))
                Line((-2.3101115901, 0.9465570353), (-2.5846735043, 0.9465570353))
            make_face()
            # Profile area: 0.0275032453, perimeter: 0.7695274405
            with BuildLine():
                Line((-2.3101115901, 0.6000000089), (-2.3101115901, 0.6948752805))
                Line((-2.3101115901, 0.6948752805), (-2.6000000387, 0.6948752805))
                Line((-2.6000000387, 0.6948752805), (-2.6000000387, 0.6000000089))
                Line((-2.6000000387, 0.6000000089), (-2.3101115901, 0.6000000089))
            make_face()
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((2.0000000298, 0.8000000119)):
                Circle(0.2)
            # Profile area: 0.0402389801, perimeter: 0.842237899
            with BuildLine():
                Line((2.5846735043, 0.8), (2.3101115901, 0.8))
                Line((2.5846735043, 0.9465570353), (2.5846735043, 0.8))
                Line((2.3101115901, 0.9465570353), (2.5846735043, 0.9465570353))
                Line((2.3101115901, 0.8), (2.3101115901, 0.9465570353))
            make_face()
            # Profile area: 0.0275032453, perimeter: 0.7695274405
            with BuildLine():
                Line((2.6000000387, 0.6000000089), (2.3101115901, 0.6000000089))
                Line((2.6000000387, 0.6948752805), (2.6000000387, 0.6000000089))
                Line((2.3101115901, 0.6948752805), (2.6000000387, 0.6948752805))
                Line((2.3101115901, 0.6000000089), (2.3101115901, 0.6948752805))
            make_face()
        # OneSide extrude, distance=0.05
        extrude(amount=0.05, mode=Mode.ADD)
    return part.part


MODELS = {
    "model_24372_03b260fe_0009": {"func": model_24372_03b260fe_0009, "volume": 8998.8672587713, "area": 5443.9822971503},
    "model_24907_c72322ea_0000": {"func": model_24907_c72322ea_0000, "volume": 2.8296403571, "area": 27.061679118},
    "model_25199_39e3c0d3_0000": {"func": model_25199_39e3c0d3_0000, "volume": 2.8657504709, "area": 26.5669364035},
    "model_25199_b2422c18_0009": {"func": model_25199_b2422c18_0009, "volume": 4.3849399133, "area": 28.5024589681},
    "model_25199_d7aff7a5_0023": {"func": model_25199_d7aff7a5_0023, "volume": 0.5526624423, "area": 7.4465825842},
    "model_26086_bf892d7f_0014": {"func": model_26086_bf892d7f_0014, "volume": 387.3348849249, "area": 718.546519106},
    "model_28929_50621ea1_0000": {"func": model_28929_50621ea1_0000, "volume": 2.340058707, "area": 25.734931597},
    "model_30426_2cde26de_0028": {"func": model_30426_2cde26de_0028, "volume": 68.4399622474, "area": 594.9290690036},
    "model_31136_987852a4_0004": {"func": model_31136_987852a4_0004, "volume": 18.7922943289, "area": 100.4954003069},
    "model_33655_f8991a06_0005": {"func": model_33655_f8991a06_0005, "volume": 1.1805179599, "area": 10.3000675874},
    "model_34317_e9c65aa6_0001": {"func": model_34317_e9c65aa6_0001, "volume": 2052.7891690644, "area": 3019.5855068017},
    "model_40145_9854f000_0000": {"func": model_40145_9854f000_0000, "volume": 5082.476353742, "area": 7042.381352032},
    "model_40693_d1d9ff4a_0000": {"func": model_40693_d1d9ff4a_0000, "volume": 19.3441272051, "area": 79.8027812785},
    "model_40800_7fa2d7a5_0001": {"func": model_40800_7fa2d7a5_0001, "volume": 67.5289271888, "area": 111.2546642116},
    "model_41125_711db4bf_0002": {"func": model_41125_711db4bf_0002, "volume": 1.9397418895, "area": 40.7092131161},
    "model_41303_b8f7bdf2_0000": {"func": model_41303_b8f7bdf2_0000, "volume": 4010.4348124613, "area": 8661.4870983278},
    "model_41714_1d49f4d1_0011": {"func": model_41714_1d49f4d1_0011, "volume": 0.3805432402, "area": 5.9753712854},
    "model_41759_f47f0249_0000": {"func": model_41759_f47f0249_0000, "volume": 3.1296766336, "area": 15.7347244949},
    "model_41787_7d41b65c_0000": {"func": model_41787_7d41b65c_0000, "volume": 32.4612825523, "area": 149.5575195632},
    "model_41896_7d8659e6_0007": {"func": model_41896_7d8659e6_0007, "volume": 4.0750874582, "area": 32.0255918602},
    "model_43467_eb9b64c2_0000": {"func": model_43467_eb9b64c2_0000, "volume": 2032.8450871361, "area": 2413.0765412203},
    "model_43529_4804941b_0056": {"func": model_43529_4804941b_0056, "volume": 4.0604477464, "area": 19.2191957132},
    "model_43928_6ca53538_0015": {"func": model_43928_6ca53538_0015, "volume": 0.0209131111, "area": 0.8097203737},
    "model_43928_6ca53538_0025": {"func": model_43928_6ca53538_0025, "volume": 1.5094965577, "area": 12.6693953437},
    "model_45303_48d14b32_0001": {"func": model_45303_48d14b32_0001, "volume": 2254.5391588132, "area": 6892.558494052},
    "model_45359_1768ab3f_0028": {"func": model_45359_1768ab3f_0028, "volume": 1.2823428049, "area": 13.3699933072},
    "model_48526_d1248549_0000": {"func": model_48526_d1248549_0000, "volume": 345.78253701, "area": 656.6556964533},
    "model_48907_25974aa4_0010": {"func": model_48907_25974aa4_0010, "volume": 7.197500564, "area": 57.2652762378},
    "model_49019_748c9a9f_0002": {"func": model_49019_748c9a9f_0002, "volume": 2.1087347145, "area": 18.0950749115},
    "model_51559_4293c0e0_0005": {"func": model_51559_4293c0e0_0005, "volume": 53.6657659687, "area": 160.9371442879},
    "model_52230_60438ea5_0008": {"func": model_52230_60438ea5_0008, "volume": 435.7120735802, "area": 1761.4543851889},
    "model_52543_3ad80ce5_0000": {"func": model_52543_3ad80ce5_0000, "volume": 23798.3354546152, "area": 13651.8858347058},
    "model_54034_b4473013_0000": {"func": model_54034_b4473013_0000, "volume": 335.8663974142, "area": 602.2889936738},
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
