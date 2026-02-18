"""Batch 004 - passing/06_11to15ops
49 models bundled from Fusion360 Gallery reconstructions.
"""

from build123d import *
from build123d import Edge, BuildLine
from collections import Counter
from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
from OCP.Geom import Geom_BSplineCurve
from OCP.TColStd import TColStd_Array1OfReal, TColStd_Array1OfInteger
from OCP.TColgp import TColgp_Array1OfPnt
from OCP.gp import gp_Pnt


# Description: This is a hinged dual-compartment tray or container with a Z-shaped folded profile, featuring two rectangular box sections connected by a central hinge mechanism, translucent blue panel inserts, and dark gray structural frames with internal ribbing for reinforcement.
def model_39953_02c01de9_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 31 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 95.7853981634, perimeter: 39.1415926536
            with BuildLine():
                CenterArc((-5.5000000745, -1.8000001013), 0.5, 90, 90)
                Line((-6.0000000745, -8.8000001013), (-6.0000000745, -1.8000001013))
                CenterArc((-5.5000000745, -8.8000001013), 0.5, 180, 90)
                Line((5.4999999255, -9.3000001013), (-5.5000000745, -9.3000001013))
                CenterArc((5.4999999255, -8.8000001013), 0.5, -90, 90)
                Line((5.9999999255, -1.8000001013), (5.9999999255, -8.8000001013))
                CenterArc((5.4999999255, -1.8000001013), 0.5, 0, 90)
                Line((-5.5000000745, -1.3000001013), (5.4999999255, -1.3000001013))
            make_face()
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)

        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 31 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 95.7853981634, perimeter: 39.1415926536
            with BuildLine():
                CenterArc((-5.5, 7.5), 0.5, 90, 90)
                Line((-6, 0.5), (-6, 7.5))
                CenterArc((-5.5, 0.5), 0.5, 180, 90)
                Line((5.5, 0), (-5.5, 0))
                CenterArc((5.5, 0.5), 0.5, -90, 90)
                Line((6, 7.5), (6, 0.5))
                CenterArc((5.5, 7.5), 0.5, 0, 90)
                Line((-5.5, 8), (5.5, 8))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch3 -> Extrude3 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((-0.6500000097, 1.7500000261)):
                Circle(0.6)
        # Symmetric extrude, each_side=5.5
        extrude(amount=5.5, both=True)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 15 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 89.6031641007, perimeter: 38.136282139
            with BuildLine():
                CenterArc((-5.4999998695, -0.4999999964), 0.34, 90, 90)
                Line((-5.8399998695, -0.4999999964), (-5.8399998695, -7.4999998248))
                CenterArc((-5.4999998695, -7.4999998248), 0.34, 180, 90)
                Line((-5.4999998695, -7.8399998248), (5.4999998695, -7.8399998248))
                CenterArc((5.4999998695, -7.4999998248), 0.34, -90, 90)
                Line((5.8399998695, -7.4999998248), (5.8399998695, -0.4999999964))
                CenterArc((5.4999998695, -0.4999999964), 0.34, 0, 90)
                Line((5.4999998695, -0.1599999964), (-5.4999998695, -0.1599999964))
            make_face()
        # OneSide extrude, distance=0.15
        extrude(amount=0.15, mode=Mode.ADD)

        # Sketch42 -> Extrude40 (NewBody)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -8), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.2250000067, perimeter: 3.3000000492
            with BuildLine():
                Line((0.7500000112, 1.5500000231), (0.7500000112, 1.7000000253))
                Line((0.7500000112, 1.7000000253), (-0.7500000112, 1.7000000253))
                Line((-0.7500000112, 1.7000000253), (-0.7500000112, 1.5500000231))
                Line((0.7500000112, 1.5500000231), (-0.7500000112, 1.5500000231))
            make_face()
        # OneSide extrude, distance=-0.08
        extrude(amount=-0.08)
    return part.part


# Description: This is a streamlined aerodynamic fairing or cowling with a smooth, curved teardrop-like profile featuring a rounded upper surface, tapered nose, and flat bottom base, designed to reduce drag or house internal components.
def model_40070_be9c502b_0015():
    """Model: ogon v10"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 11.3411494795, perimeter: 11.9380520836
            Circle(1.9)
        # OneSide extrude, distance=10
        extrude(amount=10)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 27.3724675012, perimeter: 26.677049038
            with BuildLine():
                Line((-1.9399600302, 0), (-6.3819772911, -10.2503249434))
                Line((-6.3819772911, -10.2503249434), (-0.9326980702, -10))
                Line((-1.9399600302, 0), (-0.9326980702, -10))
            make_face()
            # Profile area: 15.674881162, perimeter: 28.4465323256
            with BuildLine():
                Line((-0.2621496567, -12.9567029012), (0.9326980702, -10))
                Line((3.1025364531, -11.4694141136), (-0.2621496567, -12.9567029012))
                Line((1.9399600302, 0), (3.1025364531, -11.4694141136))
                Line((1.9399600302, 0), (0.9326980702, -10))
            make_face()
        # Symmetric extrude, each_side=4
        extrude(amount=4, both=True, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude4 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.4545142005, perimeter: 5.9257100063
            with BuildLine():
                Line((-5.1723194909, 1.1032523802), (-5.1723194909, 2.5))
                Line((-5.1723194909, 2.5), (-7.2550353372, 2.3797556408))
                Line((-5.1723194909, 1.1032523802), (-7.2550353372, 2.3797556408))
            make_face()
            # Profile area: 14.6843547847, perimeter: 18.0543824156
            with BuildLine():
                Line((-5.1723194909, 0.4654514926), (-5.1723194909, 1.1032523802))
                Line((-5.6929984525, 0.2536498811), (-5.1723194909, 0.4654514926))
                Line((-4.6516405294, -2.3063550132), (-5.6929984525, 0.2536498811))
                Line((-5.5233336068, -2.5601083296), (-4.6516405294, -2.3063550132))
                Line((-3.1763834716, -3.9985616383), (-5.5233336068, -2.5601083296))
                Line((0.3671261279, -2.2918917087), (-3.1763834716, -3.9985616383))
                Line((0.3671261279, -2.2918917087), (-5.1723194909, 1.1032523802))
            make_face()
            # Profile area: 36.8935972073, perimeter: 27.7786765316
            with BuildLine():
                Line((-5.1723194909, 1.1032523802), (-7.2550353372, 2.3797556408))
                Line((-7.2550353372, 2.3797556408), (-10.8274715456, 2.148342769))
                Line((-10.8274715456, 2.148342769), (-10.3821306659, -4.7266070623))
                Line((-10.3821306659, -4.7266070623), (-3.1763834716, -3.9985616383))
                Line((-3.1763834716, -3.9985616383), (-5.5233336068, -2.5601083296))
                Line((-5.5233336068, -2.5601083296), (-4.6516405294, -2.3063550132))
                Line((-4.6516405294, -2.3063550132), (-5.6929984525, 0.2536498811))
                Line((-5.6929984525, 0.2536498811), (-5.1723194909, 0.4654514926))
                Line((-5.1723194909, 0.4654514926), (-5.1723194909, 1.1032523802))
            make_face()
        # Symmetric extrude, each_side=2.5
        extrude(amount=2.5, both=True, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 5.1723194909), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((0.3310500752, 1.5629090385)):
                Circle(0.2)
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 5.1723194909), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-0.3310500752, 1.5629090385)):
                Circle(0.2)
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical connector or coupling with a central tubular body, featuring a larger flanged head at the top and a smaller rectangular mounting flange or bracket protruding from the middle section.
def model_40072_b44084ae_0017():
    """Model: koncowka metalowa v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2199115007, perimeter: 4.3982297525
            with BuildLine():
                CenterArc((0, 0), 0.400000006, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8, mode=Mode.ADD)

        # Sketch5 -> Extrude4 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 1.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2199115007, perimeter: 4.3982297525
            with BuildLine():
                CenterArc((0, 0), 0.400000006, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch6 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a hexagonal box or enclosure with a large circular opening or viewing window on one face, internal ribbing and structural supports, and triangular mounting flanges or fins extending from the top edges.
def model_40417_b8d98f73_0015():
    """Model: Component21"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 132.25, perimeter: 46
            with BuildLine():
                Line((5.75, -9.25), (-5.75, -9.25))
                Line((5.75, 2.25), (5.75, -9.25))
                Line((-5.75, 2.25), (5.75, 2.25))
                Line((-5.75, -9.25), (-5.75, 2.25))
            make_face()
        # OneSide extrude, distance=-5.5
        extrude(amount=-5.5)

        # Sketch4 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 80.1184666482, perimeter: 31.7300858013
            with Locations((0, -3.4999999776)):
                Circle(5.05)
        # OneSide extrude, distance=-1.6
        extrude(amount=-1.6, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -1.6), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            with Locations((0, -3.4999999776)):
                Circle(2)
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -3.1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 5.3092915846, perimeter: 8.1681408993
            with Locations((0, -3.4999999776)):
                Circle(1.3)
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -4.6), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((0, -3.4999999776)):
                Circle(1)
        # OneSide extrude, distance=-3.5
        extrude(amount=-3.5, mode=Mode.SUBTRACT)

        # Sketch8 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.25, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.0773781422, perimeter: 6.4064157758
            with BuildLine():
                Line((0, 0), (-1.6263455967, -1.6263455967))
                Line((0, 0), (-2.3, 0))
                CenterArc((0, 0), 2.3, -180, 45)
            make_face()
            # Profile area: 2.0773781422, perimeter: 6.4064157758
            with BuildLine():
                Line((2.3, 0), (0, 0))
                Line((0, 0), (1.6263455967, -1.6263455967))
                CenterArc((0, 0), 2.3, -45, 45)
            make_face()
            # Profile area: 4.1547562844, perimeter: 8.2128315516
            with BuildLine():
                CenterArc((0, 0), 2.3, -135, 90)
                Line((0, 0), (1.6263455967, -1.6263455967))
                Line((0, 0), (-1.6263455967, -1.6263455967))
            make_face()
        # OneSide extrude, distance=-0.7
        extrude(amount=-0.7, mode=Mode.SUBTRACT)

        # Sketch9 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-5.0428932188, 1.5428932188)):
                Circle(0.25)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch8 -> Extrude8 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.25, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((1.8384776311, -1.8384776311)):
                Circle(0.1)
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((-1.8384776311, -1.8384776311)):
                Circle(0.1)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a T-shaped connector or fastener featuring a cylindrical stem with a large, flat, oval-shaped head on top, with mesh-patterned cutouts or perforations visible throughout the design.
def model_40514_bb61631d_0025():
    """Model: flange"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.0522985122, perimeter: 20.1986058092
            with BuildLine():
                CenterArc((0, 0), 1.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, -1.3), 0.2, 175.5882742142, 188.8234515715)
                CenterArc((0, 0), 1.3, -171.1765484285, 72.3530968569)
                CenterArc((-1.3, 0), 0.2, 85.5882742142, 188.8234515715)
                CenterArc((0, 0), 1.3, 98.8234515715, 72.3530968569)
                CenterArc((0, 1.3), 0.2, -4.4117257858, 188.8234515715)
                CenterArc((0, 0), 1.3, 8.8234515715, 72.3530968569)
                CenterArc((1.3, 0), 0.2, -94.4117257858, 188.8234515715)
                CenterArc((0, 0), 1.3, -81.1765484285, 72.3530968569)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 5.0661741648, perimeter: 8.9566342715
            with BuildLine():
                CenterArc((0, -1.3), 0.2, 4.4117257858, 171.1765484285)
                CenterArc((0, 0), 1.3, -81.1765484285, 72.3530968569)
                CenterArc((1.3, 0), 0.2, 94.4117257858, 171.1765484285)
                CenterArc((0, 0), 1.3, 8.8234515715, 72.3530968569)
                CenterArc((0, 1.3), 0.2, -175.5882742142, 171.1765484285)
                CenterArc((0, 0), 1.3, 98.8234515715, 72.3530968569)
                CenterArc((-1.3, 0), 0.2, -85.5882742142, 171.1765484285)
                CenterArc((0, 0), 1.3, -171.1765484285, 72.3530968569)
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 2.0106192983, perimeter: 5.0265482457
            Circle(0.8)
        # OneSide extrude, distance=1.7
        extrude(amount=1.7, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.9503317777, perimeter: 3.4557519189
            Circle(0.55)
        # OneSide extrude, distance=-1.2
        extrude(amount=-1.2, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -0.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.9503317777, perimeter: 3.4557519189
            Circle(0.55)
        # OneSide extrude, distance=0.11
        extrude(amount=0.11, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -0.69, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.9503317777, perimeter: 3.4557519189
            Circle(0.55)
        # OneSide extrude, distance=-0.29
        extrude(amount=-0.29, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -1.7, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.2375829444, perimeter: 1.7278759595
            Circle(0.275)
        # OneSide extrude, distance=-0.55
        extrude(amount=-0.55, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a shaft-mounted component featuring a central cylindrical shaft with two large circular flanges on either end and angular mounting brackets, designed for rotational power transmission or coupling applications.
def model_40688_effe215a_0001():
    """Model: Crankshaft"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 20.2683004576, perimeter: 15.9592911896
            Circle(2.5400000811)
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1.27, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 7.9173043609, perimeter: 9.9745566751
            Circle(1.5875)
        # OneSide extrude, distance=7.62
        extrude(amount=7.62, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(8.89, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 49.0649892731, perimeter: 27.5691142301
            with BuildLine():
                Line((3.8100001216, 1.2700000405), (2.5400000811, 1.2700000405))
                Line((2.5400000811, 1.2700000405), (2.5400000811, 2.5400000811))
                CenterArc((0, 2.5400000811), 2.5400000811, 0, 180)
                Line((-2.5400000811, 1.2700000405), (-2.5400000811, 2.5400000811))
                Line((-3.8100001216, 1.2700000405), (-2.5400000811, 1.2700000405))
                Line((-3.8100001216, 0), (-3.8100001216, 1.2700000405))
                CenterArc((0, 0), 3.8100001216, 180, 180)
                Line((3.8100001216, 1.2700000405), (3.8100001216, 0))
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635, mode=Mode.ADD)

        # Sketch5 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(9.525, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 7.9173043609, perimeter: 9.9745566751
            with Locations((0, 2.5400000811)):
                Circle(1.5875)
        # OneSide extrude, distance=2.54
        extrude(amount=2.54, mode=Mode.ADD)

        # Sketch11 -> Extrude10 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 20.2683004576, perimeter: 15.9592911896
            Circle(2.5400000811)
        # OneSide extrude, distance=-1.27
        extrude(amount=-1.27, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a dual-cylinder mounting bracket featuring two parallel cylindrical bosses mounted on a rectangular base with an angled support surface and internal channels or slots connecting the cylinders.
def model_41229_16283ae1_0004():
    """Model: Side audio v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.8, perimeter: 5.8
            with BuildLine():
                Line((0, 2), (0, 0))
                Line((0, 0), (0.9, 0))
                Line((0.9, 0), (0.9, 2))
                Line((0.9, 2), (0, 2))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((-0.45, -1.5000000224)):
                Circle(0.4)
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((-0.45, -0.5000000075)):
                Circle(0.4)
        # OneSide extrude, distance=0.025
        extrude(amount=0.025, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.525, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-0.45, -1.5000000224)):
                Circle(0.3)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.525, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-0.45, -0.5000000075)):
                Circle(0.3)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.125, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-0.45, -0.5000000075)):
                Circle(0.25)
        # OneSide extrude, distance=-0.6
        extrude(amount=-0.6, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.125, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-0.45, -1.5000000224)):
                Circle(0.25)
        # OneSide extrude, distance=-0.6
        extrude(amount=-0.6, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a hexagonal or polygonal duct/pipe connector with an irregular geometric shape, featuring multiple flat faces, internal ribbing or structural bracing, and what appears to be a flanged opening on one end for ductwork or fluid conveyance.
def model_41303_e063f288_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 806.45, perimeter: 114.3
            with BuildLine():
                Line((-12.7, 15.875), (12.7, 15.875))
                Line((-12.7, -15.875), (-12.7, 15.875))
                Line((12.7, -15.875), (-12.7, -15.875))
                Line((12.7, 15.875), (12.7, -15.875))
            make_face()
        # OneSide extrude, distance=57.15
        extrude(amount=57.15)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 15.875, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1348.3844, perimeter: 160.02
            with BuildLine():
                Line((12.065, 0.635), (12.065, 56.515))
                Line((12.065, 56.515), (-12.065, 56.515))
                Line((-12.065, 56.515), (-12.065, 0.635))
                Line((-12.065, 0.635), (12.065, 0.635))
            make_face()
        # OneSide extrude, distance=-31.115
        extrude(amount=-31.115, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 57.15), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1132.2558, perimeter: 134.62
            with BuildLine():
                Line((-17.145, 16.51), (17.145, 16.51))
                Line((-17.145, -16.51), (-17.145, 16.51))
                Line((17.145, -16.51), (-17.145, -16.51))
                Line((17.145, 16.51), (17.145, -16.51))
            make_face()
        # OneSide extrude, distance=1.905
        extrude(amount=1.905, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 3.2258, perimeter: 7.62
            with BuildLine():
                Line((15.24, -15.875), (15.24, -14.605))
                Line((15.24, -14.605), (12.7, -14.605))
                Line((12.7, -14.605), (12.7, -15.875))
                Line((12.7, -15.875), (15.24, -15.875))
            make_face()
        # OneSide extrude, distance=-29.21
        extrude(amount=-29.21, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 3.2258, perimeter: 7.62
            with BuildLine():
                Line((-12.7, -14.605), (-12.7, -15.875))
                Line((-15.24, -14.605), (-12.7, -14.605))
                Line((-15.24, -15.875), (-15.24, -14.605))
                Line((-12.7, -15.875), (-15.24, -15.875))
            make_face()
        # OneSide extrude, distance=-29.21
        extrude(amount=-29.21, mode=Mode.ADD)

        # Sketch6 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 59.055), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 2.8502295699, perimeter: 5.9847340051
            Circle(0.9525)
        # OneSide extrude, distance=1.905
        extrude(amount=1.905, mode=Mode.ADD)

        # Sketch7 -> Extrude7 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 60.96), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 20.2682991639, perimeter: 15.9592906802
            Circle(2.54)
        # OneSide extrude, distance=1.27
        extrude(amount=1.27, mode=Mode.ADD)
    return part.part


# Description: This is a pulley wheel with a circular rim, four equally-spaced radial spokes, and a central hub with a mounting hole, designed to guide and support a belt or rope.
def model_41650_9417da80_0009():
    """Model: Wheel v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            Circle(2)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.1, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.0106193582, perimeter: 5.713274208
            with BuildLine():
                Line((0.200000003, 0.200000003), (1.8000000268, 0.200000003))
                CenterArc((0.200000003, 0.200000003), 1.6000000238, 0, 90)
                Line((0.200000003, 0.200000003), (0.200000003, 1.8000000268))
            make_face()
        # OneSide extrude, distance=-1.1
        extrude(amount=-1.1, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.1, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.0106193582, perimeter: 5.713274208
            with BuildLine():
                Line((-0.200000003, 0.200000003), (-0.200000003, 1.8000000268))
                CenterArc((-0.200000003, 0.200000003), 1.6000000238, 90, 90)
                Line((-0.200000003, 0.200000003), (-1.8000000268, 0.200000003))
            make_face()
        # OneSide extrude, distance=-0.7
        extrude(amount=-0.7, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.1, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.0106193582, perimeter: 5.713274208
            with BuildLine():
                Line((-0.200000003, -1.8000000268), (-0.200000003, -0.200000003))
                Line((-0.200000003, -0.200000003), (-1.8000000268, -0.200000003))
                CenterArc((-0.200000003, -0.200000003), 1.6000000238, 180, 90)
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.1, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.0106193582, perimeter: 5.713274208
            with BuildLine():
                Line((0.200000003, -0.200000003), (0.200000003, -1.8000000268))
                CenterArc((0.200000003, -0.200000003), 1.6000000238, -90, 90)
                Line((0.200000003, -0.200000003), (1.8000000268, -0.200000003))
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.1, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=-1.3
        extrude(amount=-1.3, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical connector or coupling with threaded ends on both the top and bottom, featuring a long tubular body with hexagonal or knurled sections at each end for gripping or mounting purposes.
def model_41685_df8ac866_0003():
    """Model: Base Shaft (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.0681415022, perimeter: 21.3628300444
            with BuildLine():
                CenterArc((0, 0), 1.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.65, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.2332961007, perimeter: 24.1902634326
            with BuildLine():
                CenterArc((0, 0), 2.1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.0681415022, perimeter: 21.3628300444
            with BuildLine():
                CenterArc((0, 0), 1.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.65, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.0681415022, perimeter: 21.3628300444
            with BuildLine():
                CenterArc((0, 0), 1.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.65, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=9
        extrude(amount=9, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 11.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.2332961007, perimeter: 24.1902634326
            with BuildLine():
                CenterArc((0, 0), 2.1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.0681415022, perimeter: 21.3628300444
            with BuildLine():
                CenterArc((0, 0), 1.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.65, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 12.6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.0681415022, perimeter: 21.3628300444
            with BuildLine():
                CenterArc((0, 0), 1.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.65, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2, mode=Mode.ADD)
    return part.part


# Description: This is a dust pan with a trapezoidal scoop shape, featuring a flat bottom collection surface, angled sides, and an attached handle protruding from the upper back edge.
def model_41698_900d863d_0004():
    """Model: Chassis"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 19 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 16, perimeter: 20
            with BuildLine():
                Line((0.5, 3.5), (0.5, 1))
                Line((-0.5, 3.5), (0.5, 3.5))
                Line((-0.5, 3.5), (-0.5, 1))
                Line((-0.5, 1), (-1.5, 1))
                Line((-1.5, 1), (-1.5, -3.5))
                Line((-1.5, -3.5), (1.5, -3.5))
                Line((1.5, 1), (1.5, -3.5))
                Line((0.5, 1), (1.5, 1))
            make_face()
            # Profile area: 2.5, perimeter: 7
            with BuildLine():
                Line((0.5, 1), (1.5, 1))
                Line((1.5, 1), (1.5, 3.5))
                Line((1.5, 3.5), (0.5, 3.5))
                Line((0.5, 3.5), (0.5, 1))
            make_face()
            # Profile area: 2.5, perimeter: 7
            with BuildLine():
                Line((-1.5, 3.5), (-0.5, 3.5))
                Line((-1.5, 1), (-1.5, 3.5))
                Line((-0.5, 1), (-1.5, 1))
                Line((-0.5, 3.5), (-0.5, 1))
            make_face()
        # OneSide extrude, distance=4
        extrude(amount=4)

        # Sketch1 -> Extrude3 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 19 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.5, perimeter: 7
            with BuildLine():
                Line((0.5, 1), (1.5, 1))
                Line((1.5, 1), (1.5, 3.5))
                Line((1.5, 3.5), (0.5, 3.5))
                Line((0.5, 3.5), (0.5, 1))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.SUBTRACT)

        # Sketch1 -> Extrude4 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 19 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.5, perimeter: 7
            with BuildLine():
                Line((-1.5, 3.5), (-0.5, 3.5))
                Line((-1.5, 1), (-1.5, 3.5))
                Line((-0.5, 1), (-1.5, 1))
                Line((-0.5, 3.5), (-0.5, 1))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude5 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((0, 2.5000000373)):
                Circle(0.3)
        # OneSide extrude, distance=4
        extrude(amount=4, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude6 (Join)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((0, 2.5000000373)):
                Circle(0.3)
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.ADD)

        # Sketch4 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -3.5), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((0, 3.2000000477)):
                Circle(0.25)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude8 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((0, -2.5000000373)):
                Circle(0.3)
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical gear or pulley hub with a wide circular flange base, featuring a tall central bore with internal ribbing/teeth patterns visible on the sides, designed for power transmission or mechanical coupling applications.
def model_41717_3bb49f29_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            Circle(1.5)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.5446900494, perimeter: 5.6548667765
            Circle(0.9)
        # OneSide extrude, distance=0.9359535196
        extrude(amount=0.9359535196, mode=Mode.ADD)

        # Sketch6 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 2.0106192983, perimeter: 5.0265482457
            Circle(0.8)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.2, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 2.0106192983, perimeter: 5.0265482457
            Circle(0.8)
        # OneSide extrude, distance=-0.9359535196
        extrude(amount=-0.9359535196, mode=Mode.SUBTRACT)

        # Sketch8 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((0, 1.2)):
                Circle(0.15)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((0, -1.2)):
                Circle(0.15)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-1.2, 0)):
                Circle(0.15)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((1.2, 0)):
                Circle(0.15)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical mesh or perforated filter component with a flat base and a curved, open-mesh top section, designed for filtering or ventilation applications.
def model_41780_da6cd1db_0014():
    """Model: Cap"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.0106192983, perimeter: 5.0265482457
            Circle(0.8)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2591813939, perimeter: 10.3672557568
            with BuildLine():
                CenterArc((0, 0), 0.85, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0669715593, perimeter: 0.9398186744
            with Locations((0, -0.2500000037)):
                Ellipse(0.1748915342, 0.1218910311)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.SUBTRACT)
    return part.part


# Description: A dumbbell consisting of a horizontal cylindrical bar connecting two spherical weights at each end, designed for strength training exercises.
def model_41896_7d8659e6_0019():
    """Model: Wheel Pin v5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.4417864669, perimeter: 2.3561944902
            Circle(0.375)
        # OneSide extrude, distance=7.5
        extrude(amount=7.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(7.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.1290098599, perimeter: 6.7990774284
            with BuildLine():
                CenterArc((0, 0), 0.7071067812, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.375, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.5
        extrude(amount=0.5, both=True, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(8, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))) as sk:
            # Profile area: 0.4712389589, perimeter: 9.5085489563
            with BuildLine():
                CenterArc((0, 0), 0.8062257868, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.7071067812, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides offset extrude, full=-0.4, trim=-0.3
        extrude(amount=-0.4, mode=Mode.ADD)
        extrude(sk.sketch, amount=-0.3, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(8, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))) as sk:
            # Profile area: 0.4712389589, perimeter: 9.5085489563
            with BuildLine():
                CenterArc((0, 0), 0.8062257868, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.7071067812, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides offset extrude, full=-0.2, trim=-0.1
        extrude(amount=-0.2, mode=Mode.ADD)
        extrude(sk.sketch, amount=-0.1, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 1.1290098599, perimeter: 6.7990774284
            with BuildLine():
                CenterArc((0, 0), 0.7071067812, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.375, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.5
        extrude(amount=0.5, both=True, mode=Mode.ADD)

        # Sketch6 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.5, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))) as sk:
            # Profile area: 0.4712389589, perimeter: 9.5085489563
            with BuildLine():
                CenterArc((0, 0), 0.8062257868, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.7071067812, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides offset extrude, full=-0.4, trim=-0.3
        extrude(amount=-0.4, mode=Mode.ADD)
        extrude(sk.sketch, amount=-0.3, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude7 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.5, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))) as sk:
            # Profile area: 0.4712389589, perimeter: 9.5085489563
            with BuildLine():
                CenterArc((0, 0), 0.8062257868, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.7071067812, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides offset extrude, full=-0.2, trim=-0.1
        extrude(amount=-0.2, mode=Mode.ADD)
        extrude(sk.sketch, amount=-0.1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a bracket or mounting component with a complex angular, faceted geometry featuring a protruding arm or flange extending to the right, internal ribbing or cross-bracing for structural reinforcement, and multiple planar surfaces that suggest it is designed for assembly and attachment purposes.
def model_41920_d3c8f833_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1209.9054250795, perimeter: 160.331089324
            with BuildLine():
                Line((20, -60), (-0.330180836, -60))
                Line((20, 0), (20, -60))
                Line((0, 0), (20, 0))
                Line((-0.330180836, -60), (0, 0))
            make_face()
        # OneSide extrude, distance=50
        extrude(amount=50)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(20, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 600.6908245761, perimeter: 111.370175603
            with BuildLine():
                Line((0, 40.1381649152), (-10, 40))
                Line((-20, 0), (-10, 40))
                Line((0, 0), (-20, 0))
                Line((0, 40.1381649152), (0, 0))
            make_face()
            # Profile area: 603.7993435103, perimeter: 111.5770432968
            with BuildLine():
                Line((-50, 40.1061696458), (-39.8899521524, 0))
                Line((-60, 40.1061696458), (-50, 40.1061696458))
                Line((-60, 0), (-60, 40.1061696458))
                Line((-39.8899521524, 0), (-60, 0))
            make_face()
        # OneSide extrude, distance=-25
        extrude(amount=-25, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(20, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 78.5398163397, perimeter: 31.4159265359
            with Locations((-30.1153137785, 20.2669248476)):
                Circle(5)
        # OneSide extrude, distance=-31
        extrude(amount=-31, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 40.1061696458, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            with Locations((10, 55)):
                Circle(1.5)
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 40.130504185, 0.5544627709), x_dir=(-1, 0, 0), z_dir=(0, -0.9999045659, -0.013815173))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            with Locations((-10, -4)):
                Circle(1.5)
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a hexagonal or octagonal structural enclosure or frame with internal cross-bracing and lattice reinforcement, featuring multiple rectangular openings or windows and a hollow interior design for lightweight strength.
def model_41941_79d46bb4_0004():
    """Model: Die"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.4515998062, perimeter: 10.1599998474
            with BuildLine():
                Line((-6.3499999046, -19.0499997139), (-8.8899998665, -19.0499997139))
                Line((-6.3499999046, -16.509999752), (-6.3499999046, -19.0499997139))
                Line((-8.8899998665, -16.509999752), (-6.3499999046, -16.509999752))
                Line((-8.8899998665, -19.0499997139), (-8.8899998665, -16.509999752))
            make_face()
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(-8.8899998665, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.1489140899, perimeter: 1.3679582022
            with Locations((17.7800005674, 1.2700000405)):
                Circle(0.2177173098)
        # OneSide extrude, distance=-0.127
        extrude(amount=-0.127, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 19.0499997139), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1466590044, perimeter: 1.3575608284
            with Locations((-8.3820002675, 2.0320000648)):
                Circle(0.2160625164)
            # Profile area: 0.1464384615, perimeter: 1.3565397078
            with Locations((-6.8580002189, 0.5080000162)):
                Circle(0.2159)
        # OneSide extrude, distance=-0.127
        extrude(amount=-0.127, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-6.3499999046, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1464384615, perimeter: 1.3565397078
            with Locations((-18.5420005918, 2.0320000648)):
                Circle(0.2159)
            # Profile area: 0.1464384615, perimeter: 1.3565397078
            with Locations((-17.7800005674, 1.2700000405)):
                Circle(0.2159)
            # Profile area: 0.1464384615, perimeter: 1.3565397078
            with Locations((-17.0180005431, 0.5080000162)):
                Circle(0.2159)
        # OneSide extrude, distance=-0.127
        extrude(amount=-0.127, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 16.509999752), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.1464384615, perimeter: 1.3565397078
            with Locations((6.8580002189, 0.5080000162)):
                Circle(0.2159)
            # Profile area: 0.1461247996, perimeter: 1.3550861182
            with Locations((6.8580002189, 2.0320000648)):
                Circle(0.215668654)
            # Profile area: 0.1466590044, perimeter: 1.3575608284
            with Locations((8.3820002675, 2.0320000648)):
                Circle(0.2160625164)
            # Profile area: 0.1464384615, perimeter: 1.3565397078
            with Locations((8.3820002675, 0.5080000162)):
                Circle(0.2159)
        # OneSide extrude, distance=-0.127
        extrude(amount=-0.127, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.54, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1464384615, perimeter: 1.3565397078
            with Locations((8.3820002675, 17.0180005431)):
                Circle(0.2159)
            # Profile area: 0.1464384615, perimeter: 1.3565397078
            with Locations((6.8580002189, 17.0180005431)):
                Circle(0.2159)
            # Profile area: 0.1464384615, perimeter: 1.3565397078
            with Locations((7.6200002432, 17.7800005674)):
                Circle(0.2159)
            # Profile area: 0.1464384615, perimeter: 1.3565397078
            with Locations((8.3820002675, 18.5420005918)):
                Circle(0.2159)
            # Profile area: 0.1464384615, perimeter: 1.3565397078
            with Locations((6.8580002189, 18.5420005918)):
                Circle(0.2159)
        # OneSide extrude, distance=-0.127
        extrude(amount=-0.127, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.1464384615, perimeter: 1.3565397078
            with Locations((-8.3820002675, 18.5420005918)):
                Circle(0.2159)
            # Profile area: 0.1464384615, perimeter: 1.3565397078
            with Locations((-6.8580002189, 18.5420005918)):
                Circle(0.2159)
            # Profile area: 0.1464384615, perimeter: 1.3565397078
            with Locations((-8.3820002675, 17.7800005674)):
                Circle(0.2159)
            # Profile area: 0.1464384615, perimeter: 1.3565397078
            with Locations((-6.8580002189, 17.7800005674)):
                Circle(0.2159)
            # Profile area: 0.1464384615, perimeter: 1.3565397078
            with Locations((-8.3820002675, 17.0180005431)):
                Circle(0.2159)
            # Profile area: 0.1464384615, perimeter: 1.3565397078
            with Locations((-6.8580002189, 17.0180005431)):
                Circle(0.2159)
        # OneSide extrude, distance=-0.127
        extrude(amount=-0.127, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a dual-wheel caster or cart wheel assembly featuring a dark blue rectangular mounting plate with two black rubber wheels attached to a shared axle at the top.
def model_41982_f75ceb8f_0014():
    """Model: HINGE v2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.25, perimeter: 6
            with BuildLine():
                Line((-1.5, 1.5), (0, 1.5))
                Line((-1.5, 0), (-1.5, 1.5))
                Line((0, 0), (-1.5, 0))
                Line((0, 1.5), (0, 0))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1963495724, perimeter: 3.7922378852
            with BuildLine():
                CenterArc((0.4500000052, 1.7500000149), 0.3535534048, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0.4500000052, 1.7500000149), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3)

        # Sketch4 -> Extrude3 (NewBody)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.196349549, perimeter: 3.792237819
            with BuildLine():
                CenterArc((-0.4500000052, 1.75), 0.3535533943, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-0.4500000052, 1.75), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.6
        extrude(amount=-0.6)

        # Sketch5 -> Extrude4 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.196349549, perimeter: 3.792237819
            with BuildLine():
                CenterArc((-0.4500000052, 1.75), 0.3535533943, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-0.4500000052, 1.75), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0076070291, perimeter: 0.6076075167
            with BuildLine():
                Line((0.0965894156, 1.7399522249), (0.1, 1.5))
                Line((0.2, 1.5), (0.1, 1.5))
                CenterArc((0.4500000052, 1.75), 0.3535533943, -178.371469095, 43.3714684974)
            make_face()
            # Profile area: 0.0080320384, perimeter: 0.6306535949
            with BuildLine():
                Line((0.2, 1.5), (0.2, 1.3965980666))
                Line((0.2, 1.3965980666), (0.4497857153, 1.3964466707))
                CenterArc((0.4500000052, 1.75), 0.3535533943, -135.0000005976, 44.9652734327)
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.ADD)

        # Sketch7 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.007611283, perimeter: 0.617552712
            with BuildLine():
                Line((-0.1, 1.5), (-0.2, 1.5))
                Line((-0.1, 1.5), (-0.096483055, 1.7449237272))
                CenterArc((-0.4500000052, 1.75), 0.3535533943, -44.9999994024, 44.1773259215)
            make_face()
            # Profile area: 0.0080320384, perimeter: 0.6306535949
            with BuildLine():
                CenterArc((-0.4500000052, 1.75), 0.3535533943, -89.965272835, 44.9652734327)
                Line((-0.2, 1.3965980666), (-0.4497857153, 1.3964466707))
                Line((-0.2, 1.5), (-0.2, 1.3965980666))
            make_face()
        # OneSide extrude, distance=-0.6
        extrude(amount=-0.6, mode=Mode.ADD)

        # Sketch8 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0080320384, perimeter: 0.6306535949
            with BuildLine():
                Line((-0.2, 1.3965980666), (-0.2, 1.5))
                CenterArc((-0.4500000052, 1.75), 0.3535533943, -89.965272835, 44.9652734327)
                Line((-0.2, 1.3965980666), (-0.4497857153, 1.3964466707))
            make_face()
            # Profile area: 0.007611283, perimeter: 0.617552712
            with BuildLine():
                CenterArc((-0.4500000052, 1.75), 0.3535533943, -44.9999994024, 44.1773259215)
                Line((-0.1, 1.5), (-0.2, 1.5))
                Line((-0.1, 1.5), (-0.096483055, 1.7449237272))
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a hexagonal or octagonal box-shaped enclosure with an open top frame structure, featuring internal cross-bracing and support ribs, designed as a structural container or framework component.
def model_41985_e9d6af98_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0950000091, perimeter: 1.3236068474
            with BuildLine():
                Line((0.2999999933, 0.2999999933), (0.1999999955, 0.3499999922))
                Line((0.5999999866, 0.2999999933), (0.2999999933, 0.2999999933))
                Line((0.7000000104, 0.3499999922), (0.5999999866, 0.2999999933))
                Line((0.7000000104, 0.5000000075), (0.7000000104, 0.3499999922))
                Line((0.200000003, 0.5000000075), (0.7000000104, 0.5000000075))
                Line((0.1999999955, 0.3499999922), (0.200000003, 0.5000000075))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.4), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0643999971, perimeter: 1.8188853975
            with BuildLine():
                Line((0.6799999848, 0.4799999893), (0.2199999951, 0.4799999893))
                Line((0.2199999951, 0.4799999893), (0.2199999951, 0.359999992))
                Line((0.2199999951, 0.359999992), (0.2999999933, 0.3199999928))
                Line((0.2999999933, 0.3199999928), (0.5999999866, 0.3199999928))
                Line((0.5999999866, 0.3199999928), (0.6799999848, 0.359999992))
                Line((0.6799999848, 0.359999992), (0.6799999848, 0.4799999893))
            make_face()
            with BuildLine():
                Line((0.5999999866, 0.4399999902), (0.5999999866, 0.4599999897))
                Line((0.2999999933, 0.4399999902), (0.5999999866, 0.4399999902))
                Line((0.2999999933, 0.4599999897), (0.2999999933, 0.4399999902))
                Line((0.5999999866, 0.4599999897), (0.2999999933, 0.4599999897))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.35
        extrude(amount=-0.35, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 20 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5000000075, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0045161722, perimeter: 0.2985398092
            with BuildLine():
                CenterArc((-0.2599999944, 0.3399999922), 0.01, 0, 90)
                Line((-0.2599999944, 0.3499999922), (-0.2999999931, 0.3499999922))
                CenterArc((-0.2999999931, 0.3399999922), 0.01, 90, 90)
                Line((-0.3099999931, 0.3399999922), (-0.3099999931, 0.3220132828))
                CenterArc((-0.3079999931, 0.3220132828), 0.002, 180, 90)
                Line((-0.3029999933, 0.3200132828), (-0.3079999931, 0.3200132828))
                CenterArc((-0.3029999933, 0.3170132828), 0.003, 0, 90)
                Line((-0.2999999933, 0.2599999944), (-0.2999999933, 0.3170132828))
                CenterArc((-0.2899999933, 0.2599999944), 0.01, -180, 90)
                Line((-0.2699999942, 0.2499999944), (-0.2899999933, 0.2499999944))
                CenterArc((-0.2699999942, 0.2599999944), 0.01, -90, 90)
                Line((-0.2599999942, 0.3169999928), (-0.2599999942, 0.2599999944))
                CenterArc((-0.2569999942, 0.3169999928), 0.003, 90, 90)
                Line((-0.2519999944, 0.3199999928), (-0.2569999942, 0.3199999928))
                CenterArc((-0.2519999944, 0.3219999928), 0.002, -90, 90)
                Line((-0.2499999944, 0.3399999922), (-0.2499999944, 0.3219999928))
            make_face()
        # OneSide extrude, distance=-0.02
        extrude(amount=-0.02, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 23 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5000000075, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0045163051, perimeter: 0.2985398092
            with BuildLine():
                Line((-0.5969999866, 0.3199999944), (-0.5919999868, 0.3199999944))
                CenterArc((-0.5919999868, 0.3219999944), 0.002, -90, 90)
                Line((-0.5899999868, 0.3219999944), (-0.5899999868, 0.3399999922))
                CenterArc((-0.5999999868, 0.3399999922), 0.01, 0, 90)
                Line((-0.5999999868, 0.3499999922), (-0.6399999855, 0.3499999922))
                CenterArc((-0.6399999855, 0.3399999922), 0.01, 90, 90)
                Line((-0.6499999855, 0.3399999922), (-0.6499999855, 0.3219999928))
                CenterArc((-0.6479999855, 0.3219999928), 0.002, 180, 90)
                Line((-0.6479999855, 0.3199999928), (-0.6429999857, 0.3199999928))
                CenterArc((-0.6429999857, 0.3169999928), 0.003, 0, 90)
                Line((-0.6399999857, 0.3169999928), (-0.6399999857, 0.2599999944))
                CenterArc((-0.6299999857, 0.2599999944), 0.01, 180, 90)
                Line((-0.6299999857, 0.2499999944), (-0.6099999866, 0.2499999944))
                CenterArc((-0.6099999866, 0.2599999944), 0.01, -90, 90)
                Line((-0.5999999866, 0.2599999944), (-0.5999999866, 0.3169999944))
                CenterArc((-0.5969999866, 0.3169999944), 0.003, 90, 90)
            make_face()
        # OneSide extrude, distance=-0.02
        extrude(amount=-0.02, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 24 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5000000075, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0038463731, perimeter: 0.2401204071
            with BuildLine():
                CenterArc((-0.2513557136, 0.0899999978), 0.01, 0, 90)
                Line((-0.3099999928, 0.0999999978), (-0.2513557136, 0.0999999978))
                CenterArc((-0.3099999928, 0.0899999978), 0.01, 90, 90)
                Line((-0.3199999928, 0.06), (-0.3199999928, 0.0899999978))
                CenterArc((-0.3099999928, 0.06), 0.01, 180, 90)
                Line((-0.3099999928, 0.05), (-0.2513557136, 0.05))
                CenterArc((-0.2513557136, 0.06), 0.01, -90, 90)
                Line((-0.2413557136, 0.0899999978), (-0.2413557136, 0.06))
            make_face()
        # OneSide extrude, distance=-0.02
        extrude(amount=-0.02, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 12 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5000000075, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0038944072, perimeter: 0.2420417738
            with BuildLine():
                CenterArc((-0.589999987, 0.06), 0.01, -90, 90)
                Line((-0.579999987, 0.06), (-0.579999987, 0.0899999978))
                CenterArc((-0.589999987, 0.0899999978), 0.01, 0, 90)
                Line((-0.589999987, 0.0999999978), (-0.6496049496, 0.0999999978))
                CenterArc((-0.6496049496, 0.0899999978), 0.01, 90, 90)
                Line((-0.6596049496, 0.0899999978), (-0.6596049496, 0.06))
                CenterArc((-0.6496049496, 0.06), 0.01, 180, 90)
                Line((-0.589999987, 0.05), (-0.6496049496, 0.05))
            make_face()
        # OneSide extrude, distance=-0.02
        extrude(amount=-0.02, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical dowel or pin with a rounded end, featuring a straight tubular body and a slightly tapered or rounded tip at one end.
def model_42329_df7f540f_0060():
    """Model: Hydraulic Body"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0333794219, perimeter: 2.6703537556
            with BuildLine():
                CenterArc((0, 0), 0.225, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.1
        extrude(amount=2.1)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0333794219, perimeter: 2.6703537556
            with BuildLine():
                CenterArc((0, 0), 0.225, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 14 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -0.2, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.03, perimeter: 0.8
            with BuildLine():
                Line((-0.15, -0.05), (-0.15, -0.15))
                Line((0.15, -0.15), (-0.15, -0.15))
                Line((0.15, -0.05), (0.15, -0.15))
                Line((0.15, -0.05), (-0.15, -0.05))
            make_face()
            # Profile area: 0.015, perimeter: 0.5
            with BuildLine():
                Line((0, 0.05), (0, 0.15))
                Line((0, 0.15), (-0.15, 0.15))
                Line((-0.15, 0.05), (-0.15, 0.15))
                Line((0, 0.05), (-0.15, 0.05))
            make_face()
            # Profile area: 0.015, perimeter: 0.5
            with BuildLine():
                Line((0.15, 0.05), (0.15, 0.15))
                Line((0, 0.15), (0.15, 0.15))
                Line((0, 0.05), (0, 0.15))
                Line((0, 0.05), (0.15, 0.05))
            make_face()
        # OneSide extrude, distance=0.25
        extrude(amount=0.25, mode=Mode.ADD)

        # Sketch3 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.15), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0252898209, perimeter: 0.8625663103
            with BuildLine():
                Line((0.15, -0.45), (0.08, -0.45))
                CenterArc((0, -0.45), 0.08, 180, 180)
                Line((-0.15, -0.45), (-0.08, -0.45))
                CenterArc((0, -0.45), 0.15, 180, 180)
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.ADD)

        # Sketch3 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.15), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0100530965, perimeter: 0.4113274123
            with BuildLine():
                Line((-0.08, -0.45), (0.08, -0.45))
                CenterArc((0, -0.45), 0.08, 0, 180)
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.15), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0252898209, perimeter: 0.8625663103
            with BuildLine():
                Line((0.08, -0.45), (0.15, -0.45))
                CenterArc((0, -0.45), 0.08, 180, 180)
                Line((-0.15, -0.45), (-0.08, -0.45))
                CenterArc((0, -0.45), 0.15, 180, 180)
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.ADD)

        # Sketch4 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.15), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0100530965, perimeter: 0.4113274123
            with BuildLine():
                CenterArc((0, -0.45), 0.08, 0, 180)
                Line((-0.08, -0.45), (0.08, -0.45))
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude8 (Cut)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((0, -0.05)):
                Circle(0.05)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude9 (Join)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((0, -0.05)):
                Circle(0.05)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)
    return part.part


# Description: This is a wireless router or network device enclosure featuring an angular, wedge-shaped housing with two external antenna posts, a front-facing ventilation panel with mesh grilles, and a dark navy blue color scheme with lighter blue accent panels.
def model_42559_aff60eae_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 55.6018824006, perimeter: 36.3140405352
            with BuildLine():
                Line((6, 0), (8, 0))
                Line((8, 0), (8, 4))
                Line((3, 6.5), (8, 4))
                Line((3, 6.5), (2.4316348886, 8.2814167995))
                Line((-2, 7.5), (2.4316348886, 8.2814167995))
                Line((-2, 7.5), (-2, 0))
                Line((-2, 0), (1, 0))
                CenterArc((3.5, 0), 2.5, 0, 180)
            make_face()
        # Symmetric extrude, each_side=7
        extrude(amount=7, both=True)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 7), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 8.9118365096, perimeter: 19.8390996312
            with BuildLine():
                Line((-1, 7.6763269807), (-2, 7.5))
                Line((-1, 16.5), (-1, 7.6763269807))
                Line((-2, 16.5), (-1, 16.5))
                Line((-2, 7.5), (-2, 16.5))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -7), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 8.9118365096, perimeter: 19.8390996312
            with BuildLine():
                Line((2, 7.5), (1, 7.6763269807))
                Line((2, 7.5), (2, 16.5))
                Line((1, 16.5), (2, 16.5))
                Line((1, 16.5), (1, 7.6763269807))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 7), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 15.0835803308, perimeter: 32.0111481838
            with BuildLine():
                Line((-2, 1.0111440441), (-2, 0))
                Line((-17, 1), (-2, 1.0111440441))
                Line((-17, 0), (-17, 1))
                Line((-2, 0), (-17, 0))
            make_face()
        # OneSide extrude, distance=-14
        extrude(amount=-14, mode=Mode.ADD)

        # Sketch6 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 7), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 14.9996285319, perimeter: 31.9992573397
            with BuildLine():
                Line((-16, 1.0007429363), (-17, 1))
                Line((-16, 16), (-16, 1.0007429363))
                Line((-17, 16), (-16, 16))
                Line((-17, 1), (-17, 16))
            make_face()
        # OneSide extrude, distance=-14
        extrude(amount=-14, mode=Mode.ADD)

        # Sketch7 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-17, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 96.1762781082, perimeter: 40.0294156499
            with BuildLine():
                Line((-6, 15), (-6, 7))
                Line((-6, 7), (6, 7))
                Line((6, 7), (6, 15.0293796847))
                Line((-6, 15), (6, 15.0293796847))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a blue geometric origami-style or folded sheet metal part featuring a symmetrical wave-like shape with pointed end flanges on both sides and a central ribbed or faceted channel running lengthwise.
def model_42572_2c23210e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 26.8644574375, perimeter: 108.45782975
            with BuildLine():
                Line((2.5, 10), (12.5, 0))
                Line((2.5, 10), (2.1464466094, 9.6464466094))
                Line((2.1464466094, 9.6464466094), (12.2928932188, -0.5))
                Line((12.2928932188, -0.5), (25.1384919825, -0.5))
                Line((25.1384919825, -0.5), (37.4689593996, 6.8982804503))
                Line((37.4689593996, 6.8982804503), (47.2, -0.4))
                Line((47.5, 0), (47.2, -0.4))
                Line((37.5, 7.5), (47.5, 0))
                Line((25, 0), (37.5, 7.5))
                Line((12.5, 0), (25, 0))
            make_face()
        # OneSide extrude, distance=13.5
        extrude(amount=13.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 114.8076866053, perimeter: 42.9506058421
            with BuildLine():
                Line((-23.4555819759, 0.9732437997), (-13.4107680113, 1.1676595539))
                Line((-13.4107680113, 1.1676595539), (-13.4107680113, 12.5))
                Line((-13.4107680113, 12.5), (-23.4555819759, 12.5))
                Line((-23.4555819759, 12.5), (-23.4555819759, 0.9732437997))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(6.6176470588, -11.0294117647, 0), x_dir=(0, 0, 1), z_dir=(-0.5144957554, 0.8574929257, 0))):
            # Profile area: 96.6905442602, perimeter: 39.7063844778
            with BuildLine():
                Line((2.5, 35), (11.0676383355, 35))
                Line((2.5, 23.7144460966), (2.5, 35))
                Line((11.0676383355, 23.7144460966), (2.5, 23.7144460966))
                Line((11.0676383355, 35), (11.0676383355, 23.7144460966))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(17.1, 22.8, 0), x_dir=(0, 0, -1), z_dir=(0.6, 0.8, 0))):
            # Profile area: 73.9341713204, perimeter: 34.3947237528
            with BuildLine():
                Line((-2.3452605503, -35.5426224267), (-11, -35.5426224267))
                Line((-2.3452605503, -27), (-2.3452605503, -35.5426224267))
                Line((-11, -27), (-2.3452605503, -27))
                Line((-11, -35.5426224267), (-11, -27))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)

        # Sketch6 -> Extrude6 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(6.25, 6.25, 0), x_dir=(0, 0, -1), z_dir=(0.7071067812, 0.7071067812, 0))):
            # Profile area: 0.8214463779, perimeter: 3.2128802692
            with Locations((-6.75, 4.4644434022)):
                Circle(0.5113457764)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6, mode=Mode.ADD)

        # Sketch8 -> Extrude7 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(16.8, 22.4, 0), x_dir=(0, 0, 1), z_dir=(-0.6, -0.8, 0))):
            # Profile area: 1.5654095459, perimeter: 4.4352583371
            with Locations((6.6726302752, -36.7253786173)):
                Circle(0.7058932882)
        # OneSide extrude, distance=-0.6
        extrude(amount=-0.6, mode=Mode.SUBTRACT)

        # Sketch10 -> Extrude9 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.027613323, 0, 1.4266883543), x_dir=(-0.9998127477, 0, 0.0193512145), z_dir=(-0.0193512145, 0, -0.9998127477))):
            # Profile area: 0.199766662, perimeter: 4.5145810211
            with BuildLine():
                Line((-16.5500002466, 0.0500000007), (-17.6000002623, 0.0500000007))
                Line((-16.5500002466, 0.3500000052), (-16.5500002466, 0.0500000007))
                Line((-17.6000002623, 0.3500000052), (-16.5500002466, 0.3500000052))
                Line((-17.6000002623, 0.0500000007), (-17.6000002623, 0.3500000052))
            make_face()
            with BuildLine():
                Line((-17.430071413, 0.119501601), (-17.430071413, 0.2722138618))
                Line((-17.430071413, 0.2722138618), (-16.6754931833, 0.2722138618))
                Line((-16.6754931833, 0.2722138618), (-16.6754931833, 0.119501601))
                Line((-16.6754931833, 0.119501601), (-17.430071413, 0.119501601))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a shoulder bolt or carriage bolt consisting of a cylindrical shaft with a squared or hexagonal head base, featuring a smooth cylindrical body and a distinct shoulder transition between the shaft and head for load distribution.
def model_43529_4804941b_0058():
    """Model: Solid77_tornillo mas chico (1) (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.022710006, perimeter: 1.431241773
            with BuildLine():
                Line((-0.3249965295, 0.5629185161), (-0.65, 0.375277675))
                Line((-0.65, 0.375277675), (-0.65, 0))
                CenterArc((0, 0), 0.65, 119.9996467615, 60.0003532385)
            make_face()
            # Profile area: 0.022710006, perimeter: 1.431233728
            with BuildLine():
                Line((0.3250000058, -0.5629165091), (0.65, -0.375277675))
                Line((0.65, -0.375277675), (0.65, -0.0000000085))
                CenterArc((0, 0), 0.65, -59.9999994145, 59.9999986657)
            make_face()
            # Profile area: 0.022710006, perimeter: 1.4312393053
            with BuildLine():
                CenterArc((0, 0), 0.65, -120.0002438954, 60.0002444809)
                Line((-0.3250023962, -0.562915129), (0, -0.7505553499))
                Line((0, -0.7505553499), (0.3250000058, -0.5629165091))
            make_face()
            # Profile area: 0.022710006, perimeter: 1.4312337824
            with BuildLine():
                Line((0.65, -0.0000000085), (0.65, 0.375277675))
                Line((0.65, 0.375277675), (0.3249999969, 0.5629165143))
                CenterArc((0, 0), 0.65, -0.0000007488, 60.000001066)
            make_face()
            # Profile area: 0.022710006, perimeter: 1.4312257363
            with BuildLine():
                Line((0.3249999969, 0.5629165143), (0, 0.7505553499))
                Line((0, 0.7505553499), (-0.3249965295, 0.5629185161))
                CenterArc((0, 0), 0.65, 60.0000003172, 59.9996464442)
            make_face()
            # Profile area: 0.022710006, perimeter: 1.4312282244
            with BuildLine():
                CenterArc((0, 0), 0.65, -180, 59.9997561046)
                Line((-0.65, 0), (-0.65, -0.375277675))
                Line((-0.65, -0.375277675), (-0.3250023962, -0.562915129))
            make_face()
            # Profile area: 1.3273228961, perimeter: 4.0840704497
            with BuildLine():
                CenterArc((0, 0), 0.65, -59.9999994145, 59.9999986657)
                CenterArc((0, 0), 0.65, -0.0000007488, 60.000001066)
                CenterArc((0, 0), 0.65, 60.0000003172, 59.9996464442)
                CenterArc((0, 0), 0.65, 119.9996467615, 60.0003532385)
                CenterArc((0, 0), 0.65, -180, 59.9997561046)
                CenterArc((0, 0), 0.65, -120.0002438954, 60.0002444809)
            make_face()
        # OneSide extrude, distance=0.53
        extrude(amount=0.53)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.53, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=2.5
        extrude(amount=2.5, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.325, 0, -0.5629165125), x_dir=(-0.8660254038, 0, 0.5), z_dir=(-0.5, 0, -0.8660254038))):
            # Profile area: 0.0157079633, perimeter: 0.5141592654
            with BuildLine():
                Line((0, 0.365), (0, 0.165))
                CenterArc((0, 0.265), 0.1, -90, 180)
            make_face()
            # Profile area: 0.0157079633, perimeter: 0.5141592654
            with BuildLine():
                CenterArc((0, 0.265), 0.1, 90, 180)
                Line((0, 0.365), (0, 0.165))
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.325, 0, -0.5629165125), x_dir=(-0.8660254038, 0, -0.5), z_dir=(0.5, 0, -0.8660254038))):
            # Profile area: 0.0157079633, perimeter: 0.5141592654
            with BuildLine():
                CenterArc((0, 0.265), 0.1, 90, 180)
                Line((0, 0.365), (0, 0.165))
            make_face()
            # Profile area: 0.0157079633, perimeter: 0.5141592654
            with BuildLine():
                Line((0, 0.365), (0, 0.165))
                CenterArc((0, 0.265), 0.1, -90, 180)
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.325, 0, -0.5629165125), x_dir=(-0.8660254038, 0, -0.5), z_dir=(0.5, 0, -0.8660254038))):
            # Profile area: 0.0157079633, perimeter: 0.5141592654
            with BuildLine():
                CenterArc((0, 0.265), 0.1, 90, 180)
                Line((0, 0.365), (0, 0.165))
            make_face()
            # Profile area: 0.0157079633, perimeter: 0.5141592654
            with BuildLine():
                Line((0, 0.365), (0, 0.165))
                CenterArc((0, 0.265), 0.1, -90, 180)
            make_face()
        # OneSide extrude, distance=-1.3
        extrude(amount=-1.3, mode=Mode.ADD)

        # Sketch4 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.325, 0, -0.5629165125), x_dir=(-0.8660254038, 0, 0.5), z_dir=(-0.5, 0, -0.8660254038))):
            # Profile area: 0.0157079633, perimeter: 0.5141592654
            with BuildLine():
                Line((0, 0.365), (0, 0.165))
                CenterArc((0, 0.265), 0.1, -90, 180)
            make_face()
            # Profile area: 0.0157079633, perimeter: 0.5141592654
            with BuildLine():
                CenterArc((0, 0.265), 0.1, 90, 180)
                Line((0, 0.365), (0, 0.165))
            make_face()
        # OneSide extrude, distance=-1.3
        extrude(amount=-1.3, mode=Mode.ADD)

        # Sketch3 -> Extrude7 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.53, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch3 -> Extrude8 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.53, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.ADD)
    return part.part


# Description: This is a tapered cylindrical pin or shaft with a pointed tip at one end and a slightly larger diameter at the other end, commonly used as a dowel pin, alignment pin, or conical fastener.
def model_43928_6ca53538_0028():
    """Model: Threaded Strut v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            Circle(0.125)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0215984495, perimeter: 1.7278759595
            with BuildLine():
                CenterArc((0, 0), 0.15, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            Circle(0.125)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0487732259, perimeter: 2.167698931
            with BuildLine():
                CenterArc((0, 0), 0.195, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=0.18
        extrude(amount=0.18, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.38), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0691150384, perimeter: 2.7646015352
            with BuildLine():
                CenterArc((0, 0), 0.245, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.195, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1194590607, perimeter: 1.2252211349
            Circle(0.195)
        # OneSide extrude, distance=3.68
        extrude(amount=3.68, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 5.06), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1194590607, perimeter: 1.2252211349
            Circle(0.195)
        # OneSide extrude, distance=0.19
        extrude(amount=0.19, mode=Mode.ADD)

        # Sketch6 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 5.25), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0804247719, perimeter: 1.0053096491
            Circle(0.16)
        # OneSide extrude, distance=0.9
        extrude(amount=0.9, mode=Mode.ADD)
    return part.part


# Description: This is a tapered shaft or spindle with a cylindrical body that gradually narrows toward both ends, featuring a wider central section and pointed or reduced diameter tips on each end.
def model_43928_6ca53538_0030():
    """Model: slotted strut v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            Circle(0.125)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0215984495, perimeter: 1.7278759595
            with BuildLine():
                CenterArc((0, 0), 0.15, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            Circle(0.125)
        # OneSide extrude, distance=0.78
        extrude(amount=0.78, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.28), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0745342857, perimeter: 2.2933626371
            with BuildLine():
                CenterArc((0, 0), 0.215, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=0.18
        extrude(amount=0.18, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.46), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1189878218, perimeter: 3.1730085801
            with BuildLine():
                CenterArc((0, 0), 0.29, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.215, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1452201204, perimeter: 1.350884841
            Circle(0.215)
        # OneSide extrude, distance=3.69
        extrude(amount=3.69, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 5.15), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0490088454, perimeter: 2.4504422698
            with BuildLine():
                CenterArc((0, 0), 0.215, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.096211275, perimeter: 1.0995574288
            Circle(0.175)
        # OneSide extrude, distance=0.18
        extrude(amount=0.18, mode=Mode.ADD)

        # Sketch6 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 5.33), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0754767635, perimeter: 0.9738937226
            Circle(0.155)
        # OneSide extrude, distance=0.9
        extrude(amount=0.9, mode=Mode.ADD)

        # Sketch7 -> Extrude8 (Cut)
        # Sketch on BRepFace
        # Sketch has 9 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 6.23), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0013438464, perimeter: 0.270547679
            with BuildLine():
                CenterArc((0, 0), 0.155, 154.5853790848, 50.8292418303)
                Line((-0.14, -0.0665206735), (-0.14, 0.0665206735))
            make_face()
            # Profile area: 0.0721874195, perimeter: 1.243605809
            with BuildLine():
                Line((-0.14, 0.0665206735), (-0.14, 0.08))
                Line((-0.14, 0.08), (-0.5995704119, 0.08))
                Line((-0.5995704119, 0.08), (-0.5995704119, -0.08))
                Line((-0.5995704119, -0.08), (-0.14, -0.08))
                Line((-0.14, -0.08), (-0.14, -0.0665206735))
                CenterArc((0, 0), 0.155, 154.5853790848, 50.8292418303)
            make_face()
        # OneSide extrude, distance=-5.323
        extrude(amount=-5.323, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cubic or box-shaped enclosure with multiple rectangular openings/windows on its faces, mounting holes distributed around the perimeter, and internal structural ribbing or reinforcement, designed as a modular housing or junction box component.
def model_43933_3b763a09_0000():
    """Model: center v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 70 constraints, 20 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 9.5355654894, perimeter: 14.905569664
            with BuildLine():
                Line((-2.7838366306, 1.6599999991), (-2.7838366705, 0.9))
                Line((-2.7838366705, 0.9), (-2, 0.9))
                Line((-2, 0.9), (-2, 0.3))
                Line((-2, 0.3), (-1.7, 0.3))
                Line((-1.7, 0.3), (-1.7, 0.55))
                Line((-1.7, 0.55), (-1.4, 0.55))
                Line((-1.4, 0.55), (-1.4, 0.3000000045))
                Line((-1.4, 0.3000000045), (0.626794927, 0.3000000045))
                Line((0.626794927, 0.3000000045), (0.8, 0.4))
                Line((0.8, 0.4), (0.8, 0.7))
                Line((0.8, 0.7), (2.7838367177, 0.7))
                Line((2.7838367177, 1.66), (2.7838367177, 0.7))
                CenterArc((2, 1.5), 0.8, 11.5369590328, 78.4630409672)
                Line((-1.9999999122, 2.3), (2, 2.3))
                CenterArc((-1.9999999127, 1.5), 0.8, 89.9999999648, 78.4630410666)
            make_face()
            # Profile area: 9.5355654896, perimeter: 14.9055696643
            with BuildLine():
                Line((2.7838367177, -1.66), (2.7838367177, -0.7))
                Line((0.8, -0.7), (2.7838367177, -0.7))
                Line((0.8, -0.4), (0.8, -0.7))
                Line((0.626794927, -0.3000000045), (0.8, -0.4))
                Line((-1.4, -0.3000000045), (0.626794927, -0.3000000045))
                Line((-1.4, -0.55), (-1.4, -0.3000000045))
                Line((-1.7, -0.55), (-1.4, -0.55))
                Line((-1.7, -0.3), (-1.7, -0.55))
                Line((-2, -0.3), (-1.7, -0.3))
                Line((-2, -0.9), (-2, -0.3))
                Line((-2.7838366707, -0.9), (-2, -0.9))
                Line((-2.783836631, -1.6599999972), (-2.7838366707, -0.9))
                CenterArc((-1.9999999127, -1.5), 0.8, -168.4630411691, 78.4630412043)
                Line((-1.9999999122, -2.3), (2, -2.3))
                CenterArc((2, -1.5), 0.8, -90, 78.4630409672)
            make_face()
            # Profile area: 3.0177989902, perimeter: 14.1621417373
            with BuildLine():
                Line((-2.7838366707, -0.9), (-2, -0.9))
                Line((-2, -0.9), (-2, -0.3))
                Line((-2, -0.3), (-1.7, -0.3))
                Line((-1.7, -0.3), (-1.7, -0.55))
                Line((-1.7, -0.55), (-1.4, -0.55))
                Line((-1.4, -0.55), (-1.4, -0.3000000045))
                Line((-1.4, -0.3000000045), (0.626794927, -0.3000000045))
                Line((0.626794927, -0.3000000045), (0.8, -0.4))
                Line((0.8, -0.4), (0.8, -0.7))
                Line((0.8, -0.7), (2.7838367177, -0.7))
                Line((2.7838367177, -0.7), (2.7838367177, 0))
                Line((2.7838367177, 0), (-2.7838367177, 0))
                Line((-2.7838366707, -0.9), (-2.7838367177, 0))
            make_face()
            # Profile area: 3.0177989901, perimeter: 14.1621417371
            with BuildLine():
                Line((2.7838367177, 0), (-2.7838367177, 0))
                Line((2.7838367177, 0.7), (2.7838367177, 0))
                Line((0.8, 0.7), (2.7838367177, 0.7))
                Line((0.8, 0.4), (0.8, 0.7))
                Line((0.626794927, 0.3000000045), (0.8, 0.4))
                Line((-1.4, 0.3000000045), (0.626794927, 0.3000000045))
                Line((-1.4, 0.55), (-1.4, 0.3000000045))
                Line((-1.7, 0.55), (-1.4, 0.55))
                Line((-1.7, 0.3), (-1.7, 0.55))
                Line((-2, 0.3), (-1.7, 0.3))
                Line((-2, 0.9), (-2, 0.3))
                Line((-2.7838366705, 0.9), (-2, 0.9))
                Line((-2.7838366705, 0.9), (-2.7838367177, 0))
            make_face()
        # Symmetric extrude, each_side=2.4
        extrude(amount=2.4, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.4), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 2.0941443878, perimeter: 5.1368433013
            with BuildLine():
                CenterArc((-2, -1.5), 0.825, -75.8588897661, 237.6833002752)
                Line((-2.7838366528, -1.2426576176), (-2.783836631, -1.6599999972))
                CenterArc((-1.9999999127, -1.5), 0.8, -168.4630411691, 78.4630412043)
                Line((-1.9999999122, -2.3), (-1.7984435563, -2.3))
            make_face()
            # Profile area: 2.0941444754, perimeter: 5.1368433989
            with BuildLine():
                CenterArc((2, -1.5), 0.825, 18.175575034, 237.6833147321)
                Line((1.7984435563, -2.3), (2, -2.3))
                CenterArc((2, -1.5), 0.8, -90, 78.4630409672)
                Line((2.7838367177, -1.66), (2.7838367177, -1.2426578154))
            make_face()
            # Profile area: 2.0941444754, perimeter: 5.1368433989
            with BuildLine():
                CenterArc((2, 1.5), 0.825, 104.1411102339, 237.6833147321)
                Line((2.7838367177, 1.2426578154), (2.7838367177, 1.66))
                CenterArc((2, 1.5), 0.8, 11.5369590328, 78.4630409672)
                Line((2, 2.3), (1.7984435563, 2.3))
            make_face()
            # Profile area: 2.0941443877, perimeter: 5.1368433012
            with BuildLine():
                CenterArc((-2, 1.5), 0.825, -161.824410445, 237.6833002111)
                Line((-1.7984435563, 2.3), (-1.9999999122, 2.3))
                CenterArc((-1.9999999127, 1.5), 0.8, 89.9999999648, 78.4630410666)
                Line((-2.7838366306, 1.6599999991), (-2.7838366525, 1.2426576167))
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((-2, -1.5)):
                Circle(0.4)
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((2, -1.5)):
                Circle(0.4)
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((2, 1.5)):
                Circle(0.4)
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((-2, 1.5)):
                Circle(0.4)
        # OneSide extrude, distance=-10
        extrude(amount=-10, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            Circle(0.6)
        # OneSide extrude, distance=-1.2
        extrude(amount=-1.2, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=-5.8
        extrude(amount=-5.8, mode=Mode.SUBTRACT)

        # Sketch8 -> Extrude8 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -2.3, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.9346238144, perimeter: 5.3407075111
            with BuildLine():
                CenterArc((0, 0), 0.6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-1.2
        extrude(amount=-1.2, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a 3D printer enclosure or housing unit with a cubic frame structure featuring an open front face, a circular mounting flange on the left side, internal cross-bracing for structural support, and a hinged or removable top panel.
def model_43934_912ff891_0025():
    """Model: Steam Chest v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 14.4, perimeter: 15.2
            with BuildLine():
                Line((2, -1.8), (2, 1.8))
                Line((2, 1.8), (-2, 1.8))
                Line((-2, 1.8), (-2, -1.8))
                Line((-2, -1.8), (2, -1.8))
            make_face()
        # Symmetric extrude, each_side=0.8
        extrude(amount=0.8, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 18 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.8), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 5.1656637061, perimeter: 8.8566370614
            with BuildLine():
                CenterArc((-1.1, 0.8), 0.2, 90, 90)
                Line((-1.3, 0.8), (-1.3, -0.799999625))
                CenterArc((-1.1, -0.8), 0.2, 179.9998925747, 90.0002148271)
                Line((-1.0999996251, -1), (1.0999996251, -1))
                CenterArc((1.1, -0.8), 0.2, -90.0001074023, 90.0002148039)
                Line((1.3, -0.7999996251), (1.3, 0.7999996251))
                CenterArc((1.1, 0.8), 0.2, -0.0001074022, 90.000214804)
                Line((1.0999996251, 1), (-1.1, 1))
            make_face()
        # OneSide extrude, distance=-2.3
        extrude(amount=-2.3, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-2, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 1.8849555922, perimeter: 5.105399773
            Ellipse(1, 0.6, rotation=90)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8, mode=Mode.ADD)

        # Sketch6 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-2.8, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a three-fingered robotic gripper or clamping hand featuring three parallel horizontal arms with a central pyramidal palm section, designed to grip objects between the opposing fingers with integrated slot features along each arm.
def model_44207_cb5191a8_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 35 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 170.3601289007, perimeter: 88.8430934696
            with BuildLine():
                Line((9.079338988, 5.1314343794), (9.079338988, -5.1314343794))
                Line((-9.079338988, 5.1314343794), (9.079338988, 5.1314343794))
                Line((-9.079338988, -5.1314343794), (-9.079338988, 5.1314343794))
                Line((9.079338988, -5.1314343794), (-9.079338988, -5.1314343794))
            make_face()
            with BuildLine():
                Line((8.1946605223, -2.6314343794), (8.1946605223, -4.6314343794))
                Line((8.1946605223, -4.6314343794), (6.1946605223, -4.6314343794))
                Line((6.1946605223, -4.6314343794), (6.1946605223, -2.6314343794))
                Line((6.1946605223, -2.6314343794), (8.1946605223, -2.6314343794))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-6, -2.5), (-6, -4.5))
                Line((-6, -4.5), (-8, -4.5))
                Line((-8, -4.5), (-8, -2.5))
                Line((-8, -2.5), (-6, -2.5))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((8, 4.5), (8, 2.5))
                Line((8, 2.5), (6, 2.5))
                Line((6, 2.5), (6, 4.5))
                Line((6, 4.5), (8, 4.5))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-6, 4.5), (-6, 2.5))
                Line((-6, 2.5), (-8, 2.5))
                Line((-8, 2.5), (-8, 4.5))
                Line((-8, 4.5), (-6, 4.5))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 35 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4, perimeter: 8
            with BuildLine():
                Line((6, 4.5), (8, 4.5))
                Line((6, 2.5), (6, 4.5))
                Line((8, 2.5), (6, 2.5))
                Line((8, 4.5), (8, 2.5))
            make_face()
        # OneSide extrude, distance=-16
        extrude(amount=-16)

        # Sketch1 -> Extrude3 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 35 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4, perimeter: 8
            with BuildLine():
                Line((-8, 4.5), (-6, 4.5))
                Line((-8, 2.5), (-8, 4.5))
                Line((-6, 2.5), (-8, 2.5))
                Line((-6, 4.5), (-6, 2.5))
            make_face()
        # OneSide extrude, distance=-16
        extrude(amount=-16)

        # Sketch1 -> Extrude4 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 35 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4, perimeter: 8
            with BuildLine():
                Line((6.1946605223, -2.6314343794), (8.1946605223, -2.6314343794))
                Line((6.1946605223, -4.6314343794), (6.1946605223, -2.6314343794))
                Line((8.1946605223, -4.6314343794), (6.1946605223, -4.6314343794))
                Line((8.1946605223, -2.6314343794), (8.1946605223, -4.6314343794))
            make_face()
        # OneSide extrude, distance=-16
        extrude(amount=-16)

        # Sketch1 -> Extrude5 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 35 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4, perimeter: 8
            with BuildLine():
                Line((-8, -2.5), (-6, -2.5))
                Line((-8, -4.5), (-8, -2.5))
                Line((-6, -4.5), (-8, -4.5))
                Line((-6, -2.5), (-6, -4.5))
            make_face()
        # OneSide extrude, distance=-16
        extrude(amount=-16)

        # Sketch1 -> Extrude6 (Join)
        # Sketch on YZ construction plane
        # Sketch has 35 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4, perimeter: 8
            with BuildLine():
                Line((6, 4.5), (8, 4.5))
                Line((6, 2.5), (6, 4.5))
                Line((8, 2.5), (6, 2.5))
                Line((8, 4.5), (8, 2.5))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.ADD)

        # Sketch1 -> Extrude7 (Join)
        # Sketch on YZ construction plane
        # Sketch has 35 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4, perimeter: 8
            with BuildLine():
                Line((6.1946605223, -2.6314343794), (8.1946605223, -2.6314343794))
                Line((6.1946605223, -4.6314343794), (6.1946605223, -2.6314343794))
                Line((8.1946605223, -4.6314343794), (6.1946605223, -4.6314343794))
                Line((8.1946605223, -2.6314343794), (8.1946605223, -4.6314343794))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.ADD)

        # Sketch1 -> Extrude8 (Join)
        # Sketch on YZ construction plane
        # Sketch has 35 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4, perimeter: 8
            with BuildLine():
                Line((-8, -2.5), (-6, -2.5))
                Line((-8, -4.5), (-8, -2.5))
                Line((-6, -4.5), (-8, -4.5))
                Line((-6, -2.5), (-6, -4.5))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.ADD)

        # Sketch1 -> Extrude9 (Join)
        # Sketch on YZ construction plane
        # Sketch has 35 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4, perimeter: 8
            with BuildLine():
                Line((-8, 4.5), (-6, 4.5))
                Line((-8, 2.5), (-8, 4.5))
                Line((-6, 2.5), (-8, 2.5))
                Line((-6, 4.5), (-6, 2.5))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.ADD)
    return part.part


# Description: This is a hexagonal-shaped structural frame or cage with multiple internal compartments and reinforcing ribs, featuring open mesh-like sides, internal dividers, and mounting feet at the base.
def model_44327_332ad058_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6600, perimeter: 560
            with BuildLine():
                Line((30, 70), (30, 0))
                Line((90, 70), (30, 70))
                Line((90, 0), (90, 70))
                Line((120, 0), (90, 0))
                Line((120, 90), (120, 0))
                Line((0, 90), (120, 90))
                Line((0, 0), (0, 90))
                Line((30, 0), (0, 0))
            make_face()
        # OneSide extrude, distance=80
        extrude(amount=80)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4200, perimeter: 260
            with BuildLine():
                Line((90, 0), (30, 0))
                Line((90, 70), (90, 0))
                Line((30, 70), (90, 70))
                Line((30, 0), (30, 70))
            make_face()
        # OneSide extrude, distance=40
        extrude(amount=40, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 20 constraints, 16 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 669.3564815491, perimeter: 105.0918416174
            with BuildLine():
                Line((26.5, 38.6540791913), (4.8, 38.6540791913))
                Line((26.5, 69.5), (26.5, 38.6540791913))
                Line((4.8, 69.5), (26.5, 69.5))
                Line((4.8, 38.6540791913), (4.8, 69.5))
            make_face()
            # Profile area: 610.9435184509, perimeter: 99.7081583826
            with BuildLine():
                Line((26.5, 4.5), (4.8, 4.5))
                Line((26.5, 32.6540791913), (26.5, 4.5))
                Line((4.8, 32.6540791913), (26.5, 32.6540791913))
                Line((4.8, 4.5), (4.8, 32.6540791913))
            make_face()
            # Profile area: 1739.0163074453, perimeter: 176.8994106743
            with BuildLine():
                Line((90.4497053371, 4.5), (31.5, 4.5))
                Line((90.4497053371, 34), (90.4497053371, 4.5))
                Line((31.5, 34), (90.4497053371, 34))
                Line((31.5, 4.5), (31.5, 34))
            make_face()
            # Profile area: 556.278039165, perimeter: 95.831702219
            with BuildLine():
                Line((115.2, 4.5), (95.4497053371, 4.5))
                Line((115.2, 32.6655564466), (115.2, 4.5))
                Line((95.4497053371, 32.6655564466), (115.2, 32.6655564466))
                Line((95.4497053371, 4.5), (95.4497053371, 32.6655564466))
            make_face()
            # Profile area: 669.1074251078, perimeter: 105.0688871067
            with BuildLine():
                Line((115.2, 38.6655564466), (93.5, 38.6655564466))
                Line((115.2, 69.5), (115.2, 38.6655564466))
                Line((93.5, 69.5), (115.2, 69.5))
                Line((93.5, 38.6655564466), (93.5, 69.5))
            make_face()
        # OneSide extrude, distance=-30
        extrude(amount=-30, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 80, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1425, perimeter: 1140
            with BuildLine():
                Line((2.5, 2.5), (-32.5, 2.5))
                Line((-32.5, 2.5), (-32.5, -67.5))
                Line((-32.5, -67.5), (-87.5, -67.5))
                Line((-87.5, -67.5), (-87.5, 2.5))
                Line((-87.5, 2.5), (-122.5, 2.5))
                Line((-122.5, 2.5), (-122.5, -92.5))
                Line((-122.5, -92.5), (2.5, -92.5))
                Line((2.5, -92.5), (2.5, 2.5))
            make_face()
            with BuildLine():
                Line((0, -90), (0, 0))
                Line((-120, -90), (0, -90))
                Line((-120, 0), (-120, -90))
                Line((-90, 0), (-120, 0))
                Line((-90, -70), (-90, 0))
                Line((-30, -70), (-90, -70))
                Line((-30, 0), (-30, -70))
                Line((0, 0), (-30, 0))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-2.5
        extrude(amount=-2.5, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 9 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 625.2345465964, perimeter: 100.839504236
            with BuildLine():
                Line((-64, 40), (-86, 40))
                Line((-64, 68.419752118), (-64, 40))
                Line((-86, 68.419752118), (-64, 68.419752118))
                Line((-86, 40), (-86, 68.419752118))
            make_face()
            # Profile area: 628.3743678507, perimeter: 101.1249425319
            with BuildLine():
                Line((-64, 6.4375287341), (-86, 6.4375287341))
                Line((-64, 35), (-64, 6.4375287341))
                Line((-86, 35), (-64, 35))
                Line((-86, 6.4375287341), (-86, 35))
            make_face()
        # OneSide extrude, distance=-15
        extrude(amount=-15, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 12 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(120, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 625.2345465964, perimeter: 100.839504236
            with BuildLine():
                Line((86, 40), (64, 40))
                Line((86, 68.419752118), (86, 40))
                Line((64, 68.419752118), (86, 68.419752118))
                Line((64, 40), (64, 68.419752118))
            make_face()
            # Profile area: 628.3743678507, perimeter: 101.1249425319
            with BuildLine():
                Line((86, 6.4375287341), (64, 6.4375287341))
                Line((86, 35), (86, 6.4375287341))
                Line((64, 35), (86, 35))
                Line((64, 6.4375287341), (64, 35))
            make_face()
        # OneSide extrude, distance=-15
        extrude(amount=-15, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude7 (Join)
        # Sketch on BRepFace
        # Sketch has 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 113.0973355292, perimeter: 37.6991118431
            with Locations((10, -10)):
                Circle(6)
            # Profile area: 113.0973355292, perimeter: 37.6991118431
            with Locations((110, -10)):
                Circle(6)
            # Profile area: 113.0973355292, perimeter: 37.6991118431
            with Locations((10, -80)):
                Circle(6)
            # Profile area: 113.0973355292, perimeter: 37.6991118431
            with Locations((110, -80)):
                Circle(6)
        # OneSide extrude, distance=5
        extrude(amount=5, mode=Mode.ADD)
    return part.part


# Description: This is a motorcycle saddlebag or side panel assembly consisting of two mirrored, elongated blue and dark gray components with curved edges, mounting flanges at the ends, and streamlined fairings designed to attach to the sides of a motorcycle frame.
def model_44333_da7b5f6d_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.500038763, perimeter: 6.5252939381
            with BuildLine():
                CenterArc((-5, 0), 2, 53.2593064074, 86.48337442)
                Line((-6.5262998506, 1.292442945), (-3.4737001494, 1.292442945))
                CenterArc((-5, 0), 2, 40.2573191726, 13.0019872349)
            make_face()
            # Profile area: 1.500038763, perimeter: 6.5252939381
            with BuildLine():
                Line((-6.5262998506, -1.292442945), (-3.4737001494, -1.292442945))
                CenterArc((-5, 0), 2, -139.7426808274, 91.1523029367)
                CenterArc((-5, 0), 2, -48.5903778907, 8.3330587181)
            make_face()
            # Profile area: 10.0074010362, perimeter: 14.1386620895
            with BuildLine():
                CenterArc((-5, 0), 2, -48.5903778907, 8.3330587181)
                Line((0, -1.5), (-3.6771243445, -1.5))
                Line((0, 1.6027019729), (0, -1.5))
                Line((-3.8036111059, 1.6027019729), (0, 1.6027019729))
                CenterArc((-5, 0), 2, 40.2573191726, 13.0019872349)
                CenterArc((-5, 0), 2, -40.2573191726, 80.5146383452)
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.8291679556, perimeter: 6.5850512417
            with BuildLine():
                Line((-0.8496043224, 1.292442945), (-0.1419645914, 1.292442945))
                Line((-0.8496043224, -1.292442945), (-0.8496043224, 1.292442945))
                Line((-0.1419645914, -1.292442945), (-0.8496043224, -1.292442945))
                Line((-0.1419645914, 1.292442945), (-0.1419645914, -1.292442945))
            make_face()
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (NewBody)
        # Sketch on BRepFace
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.500038763, perimeter: 6.5252939381
            with BuildLine():
                CenterArc((13, 0), 2, -131.4096221093, 91.1523029367)
                Line((14.5262998506, -1.292442945), (11.4737001494, -1.292442945))
                CenterArc((13, 0), 2, -139.7426808274, 8.3330587181)
            make_face()
            # Profile area: 1.500038763, perimeter: 6.5252939381
            with BuildLine():
                Line((11.4737001494, 1.292442945), (14.5262998506, 1.292442945))
                CenterArc((13, 0), 2, 40.2573191726, 91.9261717958)
                CenterArc((13, 0), 2, 132.1834909684, 7.559189859)
            make_face()
            # Profile area: 27.4273598629, perimeter: 25.6665624002
            with BuildLine():
                CenterArc((13, 0), 2, 132.1834909684, 7.559189859)
                Line((2.0073895753, 1.4819962261), (11.6569857835, 1.4819962261))
                Line((2.0073895753, 1.4819962261), (2.0073895753, -1.5))
                Line((2.0073895753, -1.5), (11.6771243445, -1.5))
                CenterArc((13, 0), 2, -139.7426808274, 8.3330587181)
                CenterArc((13, 0), 2, 139.7426808274, 80.5146383452)
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1)

        # Sketch5 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(2.0073895753, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.9811595326, perimeter: 12.7546576698
            with BuildLine():
                Line((1, 1.292442945), (0.828419368, 1.292442945))
                Line((0.828419368, 1.292442945), (0.828419368, -1.292442945))
                Line((0.828419368, -1.292442945), (0.1276985279, -1.292442945))
                Line((0.1276985279, -1.292442945), (0.1276985279, 1.292442945))
                Line((0.1276985279, 1.292442945), (0, 1.292442945))
                Line((0, -1.5), (0, 1.292442945))
                Line((1, -1.5), (0, -1.5))
                Line((1, 1.292442945), (1, -1.5))
            make_face()
            # Profile area: 0.1895532812, perimeter: 2.3791065623
            with BuildLine():
                Line((1, 1.4819962261), (1, 1.292442945))
                Line((0, 1.4819962261), (1, 1.4819962261))
                Line((0, 1.292442945), (0, 1.4819962261))
                Line((0.1276985279, 1.292442945), (0, 1.292442945))
                Line((0.828419368, 1.292442945), (0.1276985279, 1.292442945))
                Line((1, 1.292442945), (0.828419368, 1.292442945))
            make_face()
        # OneSide extrude, distance=-2.5
        extrude(amount=-2.5, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.828419368), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.2500000075, perimeter: 2.0000000298
            with BuildLine():
                Line((3.0000000447, 0.5000000075), (2.5000000373, 0.5000000075))
                Line((3.0000000447, 1.0000000149), (3.0000000447, 0.5000000075))
                Line((2.5000000373, 1.0000000149), (3.0000000447, 1.0000000149))
                Line((2.5000000373, 0.5000000075), (2.5000000373, 1.0000000149))
            make_face()
            # Profile area: 0.2500000075, perimeter: 2.0000000298
            with BuildLine():
                Line((2.5000000373, -0.5000000075), (3.0000000447, -0.5000000075))
                Line((2.5000000373, -1.0000000149), (2.5000000373, -0.5000000075))
                Line((3.0000000447, -1.0000000149), (2.5000000373, -1.0000000149))
                Line((3.0000000447, -0.5000000075), (3.0000000447, -1.0000000149))
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a stacked multi-chamber industrial component with an angular, trapezoidal profile featuring internal mesh partitions, multiple rectangular slots or openings on the sides, and a stepped/tiered geometric structure designed for fluid flow or filtration applications.
def model_44411_d2bc57fb_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 10 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 60.7421503462, perimeter: 30.592809324
            with BuildLine():
                CenterArc((7.2593467498, 3.1262911917), 3.1262911917, -90, 180)
                Line((5.0162601853, 6.2525823835), (7.2593467498, 6.2525823835))
                Line((5.0162601853, 6.2525823835), (0, 6.2525823835))
                Line((0, 0), (0, 6.2525823835))
                Line((7.2593467498, 0), (0, 0))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 16.7523751658, perimeter: 16.8500033862
            with BuildLine():
                CenterArc((2.0311760419, 3.1197182563), 3.1197182563, 74.8922231958, 55.7306107412)
                Line((0, 5.4876215241), (0, 0.7386691178))
                CenterArc((2.0311760419, 3.1197182563), 3.129707832, -130.4661440644, 35.887099852)
                Line((1.7813178527, 0), (2.2810342311, 0))
                CenterArc((2.0311760419, 3.1197182563), 3.129707832, -85.4209557876, 10.4793669237)
                Line((2.8442855275, 6.1316105126), (2.8442855275, 0.09748))
            make_face()
            # Profile area: 0.0033290334, perimeter: 0.9999651107
            with BuildLine():
                CenterArc((2.0311760419, 3.1197182563), 3.129707832, -94.5790442124, 9.1580884248)
                Line((1.7813178527, 0), (2.2810342311, 0))
            make_face()
        # OneSide extrude, distance=8
        extrude(amount=8, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 16.7523751658, perimeter: 16.8500033862
            with BuildLine():
                CenterArc((2.0311760419, 3.1197182563), 3.1197182563, 74.8922231958, 55.7306107412)
                Line((0, 5.4876215241), (0, 0.7386691178))
                CenterArc((2.0311760419, 3.1197182563), 3.129707832, -130.4661440644, 35.887099852)
                Line((1.7813178527, 0), (2.2810342311, 0))
                CenterArc((2.0311760419, 3.1197182563), 3.129707832, -85.4209557876, 10.4793669237)
                Line((2.8442855275, 6.1316105126), (2.8442855275, 0.09748))
            make_face()
            # Profile area: 0.0033290334, perimeter: 0.9999651107
            with BuildLine():
                CenterArc((2.0311760419, 3.1197182563), 3.129707832, -94.5790442124, 9.1580884248)
                Line((1.7813178527, 0), (2.2810342311, 0))
            make_face()
        # OneSide extrude, distance=6
        extrude(amount=6, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 3.1833762645, perimeter: 9.1591410025
            with BuildLine():
                Line((7.8546057394, 1.2750352382), (7, 1.2750352382))
                Line((7.8546057394, 5), (7.8546057394, 1.2750352382))
                Line((7, 5), (7.8546057394, 5))
                Line((7, 1.2750352382), (7, 5))
            make_face()
        # OneSide extrude, distance=-5.5
        extrude(amount=-5.5, mode=Mode.SUBTRACT)

        # Sketch1 -> Extrude5 (Join)
        # Sketch on XY construction plane
        # Sketch has 10 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 13.7817616022, perimeter: 15.5273556037
            with BuildLine():
                Line((5.0162601853, 6.2525823835), (0, 6.2525823835))
                Line((5.0162601853, 9), (5.0162601853, 6.2525823835))
                Line((0, 9), (5.0162601853, 9))
                Line((0, 6.2525823835), (0, 9))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5, mode=Mode.ADD)

        # Sketch5 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 3, perimeter: 7
            with BuildLine():
                Line((2.1174562399, 6.5294264431), (0.6174562399, 6.5294264431))
                Line((2.1174562399, 8.5294264431), (2.1174562399, 6.5294264431))
                Line((0.6174562399, 8.5294264431), (2.1174562399, 8.5294264431))
                Line((0.6174562399, 6.5294264431), (0.6174562399, 8.5294264431))
            make_face()
            # Profile area: 3.6, perimeter: 7.6
            with BuildLine():
                Line((4.8, 6.5), (3, 6.5))
                Line((4.8, 8.5), (4.8, 6.5))
                Line((3, 8.5), (4.8, 8.5))
                Line((3, 6.5), (3, 8.5))
            make_face()
        # OneSide extrude, distance=-4.5
        extrude(amount=-4.5, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 9), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 3.6435015668, perimeter: 9.4257489949
            with BuildLine():
                Line((0, 4.9717121702), (0, 1.2335025305))
                Line((0, 4.9717121702), (-0.9746648578, 4.9717121702))
                Line((-0.9746648578, 4.9717121702), (-0.9746648578, 1.2335025305))
                Line((-0.9746648578, 1.2335025305), (0, 1.2335025305))
            make_face()
            # Profile area: 3.7382096397, perimeter: 9.4764192794
            with BuildLine():
                Line((0, 1.2335025305), (1, 1.2335025305))
                Line((1, 1.2335025305), (1, 4.9717121702))
                Line((1, 4.9717121702), (0, 4.9717121702))
                Line((0, 4.9717121702), (0, 1.2335025305))
            make_face()
        # OneSide extrude, distance=-10
        extrude(amount=-10, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a dark blue rectangular housing or cover with a elongated shape, featuring rounded corners, a central longitudinal slot or depression running along its length, and a small circular hole near the bottom end.
def model_44524_011bb12f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 18 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 110.0685834706, perimeter: 43.4247779608
            with BuildLine():
                CenterArc((-2, -6.5), 1.5, 180, 90)
                Line((2, -8), (-2, -8))
                CenterArc((2, -6.5), 1.5, -90, 90)
                Line((3.5, 6.5), (3.5, -6.5))
                CenterArc((2, 6.5), 1.5, 0, 90)
                Line((-2, 8), (2, 8))
                CenterArc((-2, 6.5), 1.5, 90, 90)
                Line((-3.5, -6.5), (-3.5, 6.5))
            make_face()
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -8, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 2.4, perimeter: 9.2
            with BuildLine():
                Line((2, 0.1), (-2, 0.1))
                Line((2, 0.7), (2, 0.1))
                Line((-2, 0.7), (2, 0.7))
                Line((-2, 0.1), (-2, 0.7))
            make_face()
        # OneSide extrude, distance=-24
        extrude(amount=-24, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-3.5, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.8000000238, perimeter: 4.8000000715
            with BuildLine():
                Line((0.1000000015, -4.1000000611), (0.1000000015, -6.1000000909))
                Line((0.1000000015, -6.1000000909), (0.5000000075, -6.1000000909))
                Line((0.5000000075, -6.1000000909), (0.5000000075, -4.1000000611))
                Line((0.5000000075, -4.1000000611), (0.1000000015, -4.1000000611))
            make_face()
        # OneSide extrude, distance=-0.7
        extrude(amount=-0.7, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-3.5, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.253855552, perimeter: 2.0692777532
            with BuildLine():
                Line((0.1000000015, -3.0723638272), (0.5000000075, -3.0723638272))
                Line((0.1000000015, -3.7070026978), (0.1000000015, -3.0723638272))
                Line((0.5000000075, -3.7070026978), (0.1000000015, -3.7070026978))
                Line((0.5000000075, -3.0723638272), (0.5000000075, -3.7070026978))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 13 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.6963495408, perimeter: 3.5707963268
            with BuildLine():
                CenterArc((1.75, -6.75), 0.25, -90, 180)
                Line((0.75, -6.5), (1.75, -6.5))
                CenterArc((0.75, -6.75), 0.25, 90, 180)
                Line((1.75, -7), (0.75, -7))
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a trash/waste bin container with a rectangular prismatic body, dual hinged handles on the sides, and a fitted lid with a dark knob or latch mechanism on top.
def model_44916_a8b5eeff_0008():
    """Model: servo"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.64, perimeter: 6.8
            with BuildLine():
                Line((2.7000000075, 2.8000000596), (0.5000000075, 2.8000000596))
                Line((2.7000000075, 4.0000000596), (2.7000000075, 2.8000000596))
                Line((0.5000000075, 4.0000000596), (2.7000000075, 4.0000000596))
                Line((0.5000000075, 2.8000000596), (0.5000000075, 4.0000000596))
            make_face()
        # OneSide extrude, distance=2.3
        extrude(amount=2.3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with BuildLine():
                CenterArc((-1.1000000075, -3.4000000596), 0.6, 90, 180)
                CenterArc((-1.1000000075, -3.4000000596), 0.6, -90, 90)
                CenterArc((-1.1000000075, -3.4000000596), 0.6, 0, 90)
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-1.1000000075, -3.4000000596)):
                Circle(0.25)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(2.7000000075, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.3, perimeter: 2.9
            with BuildLine():
                Line((4.0000000596, 2.05), (2.8000000596, 2.05))
                Line((4.0000000596, 2.3), (4.0000000596, 2.05))
                Line((2.8000000596, 2.3), (4.0000000596, 2.3))
                Line((2.8000000596, 2.05), (2.8000000596, 2.3))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.5000000075, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.24, perimeter: 2.8
            with BuildLine():
                Line((-2.8000000596, 2.1), (-4.0000000596, 2.1))
                Line((-2.8000000596, 2.3), (-2.8000000596, 2.1))
                Line((-4.0000000596, 2.3), (-2.8000000596, 2.3))
                Line((-4.0000000596, 2.1), (-4.0000000596, 2.3))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1010962988, perimeter: 1.1841681577
            with BuildLine():
                CenterArc((-3.1000000462, -3.4000000507), 0.2, -119.9999871839, 239.9999743678)
                Line((-3.2000000075, -3.5732051538), (-3.2000000075, -3.2267949475))
            make_face()
            # Profile area: 0.1010963122, perimeter: 1.1841682025
            with BuildLine():
                CenterArc((-0.1000000075, -3.4000000507), 0.2, 60, 240)
                Line((-0.0000000075, -3.5732051314), (-0.0000000075, -3.2267949699))
            make_face()
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0314159331, perimeter: 0.6283185963
            with Locations((-1.1000000075, -3.4000000596)):
                Circle(0.1000000104)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a plastic connector or clip assembly featuring a rounded top head with a rectangular base, slot openings, and a ribbed central stem designed for securing or fastening components together.
def model_45112_54374f79_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 28.92, perimeter: 34.2627416998
            with BuildLine():
                Line((0, 0), (0, 1.6))
                Line((0, 1.6), (-8.8, 1.6))
                Line((-8.8, 6.2), (-8.8, 1.6))
                Line((-8.8, 6.2), (-9.8, 6.2))
                Line((-9.8, 6.2), (-11.4, 4.6))
                Line((-11.4, 0), (-11.4, 4.6))
                Line((0, 0), (-11.4, 0))
            make_face()
        # OneSide extrude, distance=6.4
        extrude(amount=6.4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 15 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 21.2720539706, perimeter: 25.0805458602
            with BuildLine():
                Line((-6.4, 0), (-6.4, 1.6))
                Line((-6.4, 0), (0, 0))
                Line((0, 0), (0, 1.6))
                Line((0, 1.6), (-0.3090069946, 1.6))
                CenterArc((-0.3090069946, 1.9), 0.3, -154.9651958684, 64.9651958684)
                Line((-0.5808222651, 1.7730493848), (-1.7503185572, 4.2770699478))
                CenterArc((-3.2, 3.6), 1.6, 25.0348041316, 129.9303917368)
                Line((-5.8191777349, 1.7730493848), (-4.6496814428, 4.2770699478))
                CenterArc((-6.0909930054, 1.9), 0.3, -90, 64.9651958684)
                Line((-6.4, 1.6), (-6.0909930054, 1.6))
            make_face()
            with BuildLine():
                CenterArc((-3.2, 3.6), 0.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-2.2
        extrude(amount=-2.2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 3.68, perimeter: 9.6
            with BuildLine():
                Line((-4.8, 0), (-1.6, 0))
                Line((-1.6, 0.7), (-1.6, 0))
                Line((-2.4, 0.7), (-1.6, 0.7))
                Line((-2.4, 1.6), (-2.4, 0.7))
                Line((-2.4, 1.6), (-4, 1.6))
                Line((-4, 1.6), (-4, 0.7))
                Line((-4, 0.7), (-4.8, 0.7))
                Line((-4.8, 0.7), (-4.8, 0))
            make_face()
        # OneSide extrude, distance=-20
        extrude(amount=-20, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (NewBody)
        # Sketch on BRepFace
        # Sketch has 16 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 16.0103148864, perimeter: 18.5878345394
            with BuildLine():
                Line((11.379174922, 1.545854599), (9.9425774352, 3.2506247798))
                CenterArc((8.7190737495, 2.2195870835), 1.6, 40.1205965445, 99.758806911)
                Line((6.058972577, 1.545854599), (7.4955700639, 3.2506247798))
                CenterArc((5.829565636, 1.739174167), 0.3, -90, 49.8794034555)
                Line((5.5190737495, 1.439174167), (5.829565636, 1.439174167))
                Line((5.5190737495, 0.439174167), (5.5190737495, 1.439174167))
                Line((5.5190737495, 0.439174167), (7.9190737495, 0.439174167))
                Line((7.9190737495, -0.460825833), (7.9190737495, 0.439174167))
                Line((7.9190737495, -0.460825833), (9.5190737495, -0.460825833))
                Line((9.5190737495, -0.460825833), (9.5190737495, 0.439174167))
                Line((9.5190737495, 0.439174167), (11.9190737495, 0.439174167))
                Line((11.9190737495, 0.439174167), (11.9190737495, 1.439174167))
                Line((11.6085818631, 1.439174167), (11.9190737495, 1.439174167))
                CenterArc((11.6085818631, 1.739174167), 0.3, -139.8794034555, 49.8794034555)
            make_face()
        # OneSide extrude, distance=2.2
        extrude(amount=2.2)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.5321638895, perimeter: 9.7743303457
            with BuildLine():
                Line((-11.9190737495, 3.8195870835), (-8.7190736698, 3.8195870835))
                Line((-11.9190737495, 1.439174167), (-11.9190737495, 3.8195870835))
                Line((-11.6085818631, 1.439174167), (-11.9190737495, 1.439174167))
                CenterArc((-11.6085818631, 1.739174167), 0.3, -90, 49.8794034555)
                Line((-9.9425774352, 3.2506247798), (-11.379174922, 1.545854599))
                CenterArc((-8.7190737495, 2.2195870835), 1.6, 89.9999971441, 49.8794063114)
            make_face()
            # Profile area: 3.5321638895, perimeter: 9.7743300267
            with BuildLine():
                Line((-8.7190736698, 3.8195870835), (-5.5190737495, 3.8195870835))
                CenterArc((-8.7190737495, 2.2195870835), 1.6, 40.1205965445, 49.8794005996)
                Line((-6.058972577, 1.545854599), (-7.4955700639, 3.2506247798))
                CenterArc((-5.829565636, 1.739174167), 0.3, -139.8794034555, 49.8794034555)
                Line((-5.5190737495, 1.439174167), (-5.829565636, 1.439174167))
                Line((-5.5190737495, 3.8195870835), (-5.5190737495, 1.439174167))
            make_face()
            # Profile area: 14.5703148864, perimeter: 16.7878345394
            with BuildLine():
                CenterArc((-8.7190737495, 2.2195870835), 1.6, 89.9999971441, 49.8794063114)
                Line((-9.9425774352, 3.2506247798), (-11.379174922, 1.545854599))
                CenterArc((-11.6085818631, 1.739174167), 0.3, -90, 49.8794034555)
                Line((-11.6085818631, 1.439174167), (-11.9190737495, 1.439174167))
                Line((-11.9190737495, 0.439174167), (-11.9190737495, 1.439174167))
                Line((-11.9190737495, 0.439174167), (-9.5190737495, 0.439174167))
                Line((-9.5190737495, 0.439174167), (-7.9190737495, 0.439174167))
                Line((-7.9190737495, 0.439174167), (-5.5190737495, 0.439174167))
                Line((-5.5190737495, 1.439174167), (-5.5190737495, 0.439174167))
                Line((-5.5190737495, 1.439174167), (-5.829565636, 1.439174167))
                CenterArc((-5.829565636, 1.739174167), 0.3, -139.8794034555, 49.8794034555)
                Line((-6.058972577, 1.545854599), (-7.4955700639, 3.2506247798))
                CenterArc((-8.7190737495, 2.2195870835), 1.6, 40.1205965445, 49.8794005996)
            make_face()
        # OneSide extrude, distance=0.8
        extrude(amount=0.8, mode=Mode.ADD)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -2.2), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((8.7190737495, 2.2195870835)):
                Circle(0.6)
        # OneSide extrude, distance=-13
        extrude(amount=-13, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical metal dowel pin or shaft with rounded ends, featuring a uniform hollow or solid tubular body with a slight taper at both extremities.
def model_45269_a8765cc8_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude5 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0240528188, perimeter: 0.5497787144
            with Locations((5.5000000596, 0)):
                Circle(0.0875)
        # Symmetric extrude, each_side=0.76
        extrude(amount=0.76, both=True)
    return part.part


# Description: This is a cylindrical tube or pipe with a tapered/stepped section near the top end, featuring a uniform hollow core throughout its length.
def model_45359_1768ab3f_0024():
    """Model: Centrifugal Pump Shaft"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            Circle(0.35)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4005530633, perimeter: 5.3407075111
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.35, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            Circle(0.35)
        # OneSide extrude, distance=5.4
        extrude(amount=5.4, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5.9, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 6.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2199114858, perimeter: 4.398229715
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8, mode=Mode.ADD)
    return part.part


# Description: This is a TIE fighter wing panel from Star Wars, featuring a distinctive angular frame structure with an X-shaped internal bracing pattern, a rectangular central opening, and dark metallic plating characteristic of Imperial spacecraft design.
def model_45360_cb4bac3f_0007():
    """Model: Cuerpo"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 28.9459781917, perimeter: 42.0591991073
            with BuildLine():
                Line((0, 0.55), (0, -4))
                Line((0, -4), (1.45, -4))
                Line((1.45, -4), (1.45, 1))
                CenterArc((-0.5560810811, 1), 2.0060810811, 0, 85.5376507839)
                CenterArc((-0.4, 4), 1, 180, 90)
                Line((-1.4, 4), (-1.4, 14))
                Line((-1.4, 14), (-2.85, 14))
                Line((-2.85, 14), (-2.85, 3.55))
                CenterArc((-0.85, 3.55), 2, 180, 89.6278903599)
                CenterArc((-0.85, 3.55), 2, -90.3721096401, 0.3721096401)
                Line((-0.8627041381, 1.55), (-0.85, 1.55))
                CenterArc((-1.0109250396, 0.55), 1.0109250396, 0, 81.5689520858)
            make_face()
        # OneSide extrude, distance=-12
        extrude(amount=-12)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-1.4, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 91.9099230594, perimeter: 49.8481817769
            with BuildLine():
                Line((4.5, -12), (14, -12))
                Line((4.5, -12), (6, -23))
                Line((6, -23), (8.3324, -23))
                CenterArc((10.00005, -26.6357865005), 4, 65.3601864156, 49.2796271689)
                Line((13, -23), (11.6677, -23))
                CenterArc((13, -22), 1, -90, 90)
                Line((14, -12), (14, -22))
            make_face()
            with BuildLine():
                CenterArc((6.9753471362, -16.0905415284), 0.55, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((11.9999302184, -18.5000551389), 0.33235, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((12.4999116355, -21.5000190481), 0.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-1.45
        extrude(amount=-1.45, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-1.4, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 16.875, perimeter: 20.7464278423
            with BuildLine():
                Line((9.5, 0), (14, 0))
                Line((9.5, 0), (14, -7.5))
                Line((14, 0), (14, -7.5))
            make_face()
            # Profile area: 2.0106192983, perimeter: 5.0265482457
            with Locations((5.4999700084, -10.9999891889)):
                Circle(0.8)
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1.45, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 96.4292036732, perimeter: 48.2831853072
            with BuildLine():
                Line((3, -12), (1, -12))
                Line((1, -12), (-4, -12))
                Line((-4, -12), (-4, -26))
                Line((-4, -26), (3, -26))
                Line((3, -26), (3, -12))
            make_face()
            with BuildLine():
                CenterArc((1.7499774481, -22.7500056375), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.7499774481, -17.2500056375), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-1.45
        extrude(amount=-1.45, mode=Mode.ADD)

        # Sketch4 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -12, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.8403622743, perimeter: 6.1102155913
            with BuildLine():
                Line((-1.45, -3), (0, -3))
                Line((0, -3), (0, -2.9274685821))
                CenterArc((0.5560810811, -1), 2.0060810811, -180, 73.9069737765)
                Line((-1.45, -3), (-1.45, -1))
            make_face()
            # Profile area: 0.0117068641, perimeter: 0.8797530545
            with BuildLine():
                Line((0, -3), (0.4, -3))
                CenterArc((0.5560810811, -1), 2.0060810811, -106.0930262235, 11.6306770074)
                Line((0, -3), (0, -2.9274685821))
            make_face()
        # OneSide extrude, distance=0.0137
        extrude(amount=0.0137, mode=Mode.ADD)

        # Sketch5 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 28.4292036732, perimeter: 35.2831853072
            with BuildLine():
                Line((-0.5, -14), (-3, -14))
                Line((-3, -14), (-3, -26))
                Line((-3, -26), (-0.5, -26))
                Line((-0.5, -26), (-0.5, -14))
            make_face()
            with BuildLine():
                CenterArc((-1.7499774481, -17.2500056375), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.7499774481, -22.7500056375), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a fastener or screw with a polygonal (likely hexagonal) head, featuring a cylindrical shaft with vertical ribbing or fluting and a faceted, geometric head design.
def model_45360_cb4bac3f_0019():
    """Model: tornillo palanca"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.4641016151, perimeter: 6.9282032303
            with BuildLine():
                Line((-1, 0.5773502692), (-1, -0.5773502692))
                Line((-1, -0.5773502692), (0, -1.1547005384))
                Line((0, -1.1547005384), (1, -0.5773502692))
                Line((1, -0.5773502692), (1, 0.5773502692))
                Line((1, 0.5773502692), (0, 1.1547005384))
                Line((0, 1.1547005384), (-1, 0.5773502692))
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=3.1
        extrude(amount=3.1, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)

        # Sketch4 -> Extrude5 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.1887902048, perimeter: 7.2551974569
            Circle(1.1547005384)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.812678048, perimeter: 9.1415926536
            with BuildLine():
                Line((0.8660254038, 0.5), (0, 1))
                Line((0, 1), (-0.8660254038, 0.5))
                Line((-0.8660254038, 0.5), (-0.8660254038, -0.5))
                Line((-0.8660254038, -0.5), (0, -1))
                Line((0, -1), (0.8660254038, -0.5))
                Line((0.8660254038, -0.5), (0.8660254038, 0.5))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6, mode=Mode.ADD)
    return part.part


# Description: This is a gripper or clamping mechanism featuring two opposing blue-shaded jaw plates with a central dark cylindrical actuator, designed to grip or clamp objects between the parallel surfaces with integrated mounting flanges.
def model_48907_25974aa4_0002():
    """Model: lenght adjustment slider v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 24 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.5, perimeter: 3
            with BuildLine():
                Line((1, -0.1), (1, -0.25))
                Line((1, 0.1), (1, -0.1))
                Line((1, 0.1), (1, 0.25))
                Line((0, 0.25), (1, 0.25))
                Line((0, -0.25), (0, 0.25))
                Line((1, -0.25), (0, -0.25))
            make_face()
            # Profile area: 0.5, perimeter: 3
            with BuildLine():
                Line((0, -0.25), (0, 0.25))
                Line((0, 0.25), (-1, 0.25))
                Line((-1, 0.1), (-1, 0.25))
                Line((-1, 0.1), (-1, -0.1))
                Line((-1, -0.1), (-1, -0.25))
                Line((-1, -0.25), (0, -0.25))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 24 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))) as sk:
            # Profile area: 0.06, perimeter: 1.1
            with BuildLine():
                Line((-1, 0.1), (-1, 0.25))
                Line((-1, 0.25), (-1.4, 0.25))
                Line((-1.4, 0.25), (-1.4, 0.1))
                Line((-1.4, 0.1), (-1, 0.1))
            make_face()
            # Profile area: 0.06, perimeter: 1.1
            with BuildLine():
                Line((-1, -0.1), (-1, -0.25))
                Line((-1.4, -0.1), (-1, -0.1))
                Line((-1.4, -0.25), (-1.4, -0.1))
                Line((-1, -0.25), (-1.4, -0.25))
            make_face()
            # Profile area: 0.06, perimeter: 1.1
            with BuildLine():
                Line((1, 0.1), (1, 0.25))
                Line((1.4, 0.1), (1, 0.1))
                Line((1.4, 0.25), (1.4, 0.1))
                Line((1, 0.25), (1.4, 0.25))
            make_face()
            # Profile area: 0.06, perimeter: 1.1
            with BuildLine():
                Line((1.4, -0.25), (1.4, -0.1))
                Line((1.4, -0.1), (1, -0.1))
                Line((1, -0.1), (1, -0.25))
                Line((1, -0.25), (1.4, -0.25))
            make_face()
        # TwoSides extrude, along=0.5, against=-0.8
        extrude(amount=0.5, mode=Mode.ADD)
        extrude(sk.sketch, amount=-0.8, mode=Mode.ADD)

        # Sketch3 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.06, perimeter: 1
            with BuildLine():
                Line((0.4, -0.15), (0.2, -0.15))
                Line((0.4, 0.15), (0.4, -0.15))
                Line((0.2, 0.15), (0.4, 0.15))
                Line((0.2, -0.15), (0.2, 0.15))
            make_face()
            # Profile area: 0.06, perimeter: 1
            with BuildLine():
                Line((-0.2, -0.15), (-0.2, 0.15))
                Line((-0.2, 0.15), (-0.4, 0.15))
                Line((-0.4, 0.15), (-0.4, -0.15))
                Line((-0.4, -0.15), (-0.2, -0.15))
            make_face()
        # OneSide extrude, distance=0.7
        extrude(amount=0.7, mode=Mode.ADD)

        # Sketch6 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.4), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with BuildLine():
                CenterArc((1.0500000156, 0), 0.15, -0.0151090122, 90.0151090122)
                CenterArc((1.0500000156, 0), 0.15, 90, 180)
                CenterArc((1.0500000156, 0), 0.15, -90, 89.9848909878)
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch7 -> Extrude7 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.4), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.07068582, perimeter: 0.9424776978
            with BuildLine():
                CenterArc((-1.0500000156, 0), 0.1499999844, -180, 90)
                CenterArc((-1.0500000156, 0), 0.1499999844, -90, 180)
                CenterArc((-1.0500000156, 0), 0.1499999844, 90, 90)
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


# Description: This is a gasket or sealing ring with an elliptical/oval shape and a hollow center, featuring a textured or ribbed surface pattern for improved sealing and grip properties.
def model_49019_748c9a9f_0017():
    """Model: srodek  v5"""
    def _nurbs_edge(ctrl_pts, weights, knots, degree):
        """Create a NURBS edge from control points, weights, and knot vector."""
        n = len(ctrl_pts)
        poles = TColgp_Array1OfPnt(1, n)
        for i, (x, y) in enumerate(ctrl_pts):
            poles.SetValue(i + 1, gp_Pnt(x, y, 0))
        w_arr = TColStd_Array1OfReal(1, n)
        for i, w in enumerate(weights):
            w_arr.SetValue(i + 1, max(w, 1e-10))  # Clamp tiny weights
        kc = Counter(knots)
        uk = sorted(kc.keys())
        nk = len(uk)
        k_arr = TColStd_Array1OfReal(1, nk)
        m_arr = TColStd_Array1OfInteger(1, nk)
        for i, k in enumerate(uk):
            k_arr.SetValue(i + 1, k)
            m_arr.SetValue(i + 1, kc[k])
        curve = Geom_BSplineCurve(poles, w_arr, k_arr, m_arr, degree)
        edge = BRepBuilderAPI_MakeEdge(curve).Edge()
        ctx = BuildLine._get_context()
        if ctx:
            ctx._add_to_context(Edge(edge))

    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 10.2101761242, perimeter: 40.8407044967
            with BuildLine():
                CenterArc((0, 0), 3.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is a spur gear with a circular disk-like shape, featuring evenly-spaced teeth around its outer perimeter and a central hub with a bore hole for shaft mounting.
def model_49134_e9867f8b_0005():
    """Model: Kolko"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 14 constraints (parametric, not converted)
        with BuildSketch(Plane.XY) as sk:
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((17.5, 10)):
                Circle(0.25)
        # TwoSides extrude, along=2, against=-1
        extrude(amount=2)
        extrude(sk.sketch, amount=-1)

        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 14 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 28.2743338823, perimeter: 56.5486677646
            with BuildLine():
                CenterArc((17.5, 10), 5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((17.5, 10), 4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-2
        extrude(amount=-2)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XY construction plane
        # Sketch has 14 constraints (parametric, not converted)
        with BuildSketch(Plane.XY) as sk:
            # Profile area: 4.9008845396, perimeter: 49.008845396
            with BuildLine():
                CenterArc((17.5, 10), 4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((17.5, 10), 3.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides extrude, along=0.3, against=-2.3
        extrude(amount=0.3, mode=Mode.ADD)
        extrude(sk.sketch, amount=-2.3, mode=Mode.ADD)

        # Sketch1 -> Extrude4 (Join)
        # Sketch on XY construction plane
        # Sketch has 14 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 32.7982273035, perimeter: 36.4424747816
            with BuildLine():
                CenterArc((17.5, 10), 3.8, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((17.5, 10), 2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-1.8
        extrude(amount=-1.8, mode=Mode.ADD)

        # Sketch1 -> Extrude5 (Cut)
        # Sketch on XY construction plane
        # Sketch has 14 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 32.7982273035, perimeter: 36.4424747816
            with BuildLine():
                CenterArc((17.5, 10), 3.8, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((17.5, 10), 2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)

        # Sketch1 -> Extrude6 (Join)
        # Sketch on XY construction plane
        # Sketch has 14 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.3876104167, perimeter: 23.8761041673
            with BuildLine():
                CenterArc((17.5, 10), 2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((17.5, 10), 1.8, 162, 144)
                CenterArc((17.5, 10), 1.8, 90, 72)
                CenterArc((17.5, 10), 1.8, 18, 72)
                CenterArc((17.5, 10), 1.8, -54, 72)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.ADD)

        # Sketch1 -> Extrude7 (Join)
        # Sketch on XY construction plane
        # Sketch has 14 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.3876104167, perimeter: 23.8761041673
            with BuildLine():
                CenterArc((17.5, 10), 2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((17.5, 10), 1.8, 162, 144)
                CenterArc((17.5, 10), 1.8, 90, 72)
                CenterArc((17.5, 10), 1.8, 18, 72)
                CenterArc((17.5, 10), 1.8, -54, 72)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch1 -> Extrude8 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 14 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.5636908002, perimeter: 16.5451635461
            with BuildLine():
                Line((16.4423552025, 8.5442768225), (17.4999691642, 9.3668802541))
                Line((18.5580134541, 8.5437694101), (17.4999691642, 9.3668802541))
                Line((18.5580134541, 8.5437694101), (18.1021554747, 9.8043478261))
                Line((19.2119017293, 10.5562305899), (18.1021554747, 9.8043478261))
                Line((19.2119017293, 10.5562305899), (17.8721525167, 10.5122241559))
                Line((17.5, 11.8), (17.8721525167, 10.5122241559))
                Line((17.5, 11.8), (17.1278474871, 10.5122241692))
                Line((15.7880982707, 10.5562305899), (17.1278474871, 10.5122241692))
                Line((15.7880982707, 10.5562305899), (16.8978768689, 9.8043259125))
                Line((16.4423552025, 8.5442768225), (16.8978768689, 9.8043259125))
            make_face()
            with BuildLine():
                CenterArc((17.5, 10), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5)

        # Sketch1 -> Extrude9 (Cut)
        # Sketch on XY construction plane
        # Sketch has 14 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.5636908002, perimeter: 16.5451635461
            with BuildLine():
                Line((16.4423552025, 8.5442768225), (17.4999691642, 9.3668802541))
                Line((18.5580134541, 8.5437694101), (17.4999691642, 9.3668802541))
                Line((18.5580134541, 8.5437694101), (18.1021554747, 9.8043478261))
                Line((19.2119017293, 10.5562305899), (18.1021554747, 9.8043478261))
                Line((19.2119017293, 10.5562305899), (17.8721525167, 10.5122241559))
                Line((17.5, 11.8), (17.8721525167, 10.5122241559))
                Line((17.5, 11.8), (17.1278474871, 10.5122241692))
                Line((15.7880982707, 10.5562305899), (17.1278474871, 10.5122241692))
                Line((15.7880982707, 10.5562305899), (16.8978768689, 9.8043259125))
                Line((16.4423552025, 8.5442768225), (16.8978768689, 9.8043259125))
            make_face()
            with BuildLine():
                CenterArc((17.5, 10), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4, mode=Mode.SUBTRACT)

        # Sketch1 -> Extrude10 (Join)
        # Sketch on XY construction plane
        # Sketch has 14 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.5890486225, perimeter: 4.7123889804
            with BuildLine():
                CenterArc((17.5, 10), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((17.5, 10), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-1.7
        extrude(amount=-1.7, mode=Mode.ADD)
    return part.part


# Description: This is a flat-panel LCD monitor with a tilted rectangular display screen and a separate pedestal stand base that supports the monitor at an angle.
def model_49902_81b1dde9_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 108.0087936795, perimeter: 42.470171033
            with BuildLine():
                Line((6.3954429652, -4.2220997931), (-6.3954429652, -4.2220997931))
                Line((6.3954429652, 4.2220997931), (6.3954429652, -4.2220997931))
                Line((-6.3954429652, 4.2220997931), (6.3954429652, 4.2220997931))
                Line((-6.3954429652, -4.2220997931), (-6.3954429652, 4.2220997931))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on BRepFace
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 1.0183992441, perimeter: 4.0917898722
            with BuildLine():
                Line((-0.4277744534, -4.2220997931), (0.4277744534, -4.2220997931))
                Line((-0.4277744534, -4.2220997931), (-0.4277744534, -5.4124458223))
                Line((-0.4277744534, -5.4124458223), (0.4277744534, -5.4124458223))
                Line((0.4277744534, -5.4124458223), (0.4277744534, -4.2220997931))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch3 -> Extrude3 (NewBody)
        # Sketch on BRepFace
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -5.4124458223, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 7.5722255466, perimeter: 19
            with BuildLine():
                Line((0, 0.4277744534), (0, 4))
                Line((0, 4), (-1, 4))
                Line((-1, 4), (-1, -4))
                Line((-1, -4), (0, -4))
                Line((0, -4), (0, -0.4277744534))
                Line((-0.5, -0.4277744534), (0, -0.4277744534))
                Line((-0.5, 0.4277744534), (-0.5, -0.4277744534))
                Line((0, 0.4277744534), (-0.5, 0.4277744534))
            make_face()
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)

        # Sketch6 -> Extrude4 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 108.0087936795, perimeter: 42.470171033
            with BuildLine():
                Line((-6.3954429652, 4.2220997931), (-6.3954429652, -4.2220997931))
                Line((-6.3954429652, -4.2220997931), (6.3954429652, -4.2220997931))
                Line((6.3954429652, -4.2220997931), (6.3954429652, 4.2220997931))
                Line((6.3954429652, 4.2220997931), (-6.3954429652, 4.2220997931))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch7 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.2, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 92.5170539406, perimeter: 39.5403662504
            with BuildLine():
                Line((6.082499866, -3.8025916966), (-6.082499866, -3.8025916966))
                Line((6.082499866, 3.8025916966), (6.082499866, -3.8025916966))
                Line((-6.082499866, 3.8025916966), (6.082499866, 3.8025916966))
                Line((-6.082499866, -3.8025916966), (-6.082499866, 3.8025916966))
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a skylight or roof window assembly featuring a parallelogram-shaped frame with an angled glazed panel, designed to fit flush with sloped roof surfaces while allowing natural light penetration.
def model_51471_289b2a1d_0011():
    """Model: corpus"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 13 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 119, perimeter: 476
            with BuildLine():
                Line((30, -30), (-30, -30))
                Line((30, 30), (30, -30))
                Line((-30, 30), (30, 30))
                Line((-30, -30), (-30, 30))
            make_face()
            with BuildLine():
                Line((29.5, 29.5), (29.5, -29.5))
                Line((29.5, -29.5), (-29.5, -29.5))
                Line((-29.5, -29.5), (-29.5, 29.5))
                Line((-29.5, 29.5), (29.5, 29.5))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=5.5
        extrude(amount=5.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 6.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 119, perimeter: 476
            with BuildLine():
                Line((-30, 30), (30, 30))
                Line((-30, -30), (-30, 30))
                Line((30, -30), (-30, -30))
                Line((30, 30), (30, -30))
            make_face()
            with BuildLine():
                Line((-29.5, -29.5), (-29.5, 29.5))
                Line((-29.5, 29.5), (29.5, 29.5))
                Line((29.5, 29.5), (29.5, -29.5))
                Line((29.5, -29.5), (-29.5, -29.5))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 3481, perimeter: 236
            with BuildLine():
                Line((29.5, -29.5), (-29.5, -29.5))
                Line((29.5, 29.5), (29.5, -29.5))
                Line((-29.5, 29.5), (29.5, 29.5))
                Line((-29.5, -29.5), (-29.5, 29.5))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 7, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-22.7345225423, 0)):
                Circle(0.5)
        # OneSide extrude, distance=-4
        extrude(amount=-4, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 35 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 30), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 4, perimeter: 10
            with BuildLine():
                Line((13, 6), (13, 2))
                Line((13, 6), (12, 6))
                Line((12, 2), (12, 6))
                Line((13, 2), (12, 2))
            make_face()
            # Profile area: 4, perimeter: 10
            with BuildLine():
                Line((14, 2), (14, 6))
                Line((15, 2), (14, 2))
                Line((15, 6), (15, 2))
                Line((14, 6), (15, 6))
            make_face()
            # Profile area: 4, perimeter: 10
            with BuildLine():
                Line((16, 2), (16, 6))
                Line((17, 2), (16, 2))
                Line((17, 6), (17, 2))
                Line((16, 6), (17, 6))
            make_face()
            # Profile area: 4, perimeter: 10
            with BuildLine():
                Line((18, 2), (18, 6))
                Line((19, 2), (18, 2))
                Line((19, 6), (19, 2))
                Line((18, 6), (19, 6))
            make_face()
            # Profile area: 4, perimeter: 10
            with BuildLine():
                Line((20, 2), (20, 6))
                Line((21, 2), (20, 2))
                Line((21, 6), (21, 2))
                Line((20, 6), (21, 6))
            make_face()
            # Profile area: 4, perimeter: 10
            with BuildLine():
                Line((22, 2), (22, 6))
                Line((23, 2), (22, 2))
                Line((23, 6), (23, 2))
                Line((22, 6), (23, 6))
            make_face()
            # Profile area: 4, perimeter: 10
            with BuildLine():
                Line((24, 2), (24, 6))
                Line((25, 2), (24, 2))
                Line((25, 6), (25, 2))
                Line((24, 6), (25, 6))
            make_face()
        # OneSide extrude, distance=-97.5
        extrude(amount=-97.5, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-30, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 6.25, perimeter: 10
            with BuildLine():
                Line((27.5, 2.5), (25, 2.5))
                Line((27.5, 5), (27.5, 2.5))
                Line((25, 5), (27.5, 5))
                Line((25, 2.5), (25, 5))
            make_face()
        # OneSide extrude, distance=-5
        extrude(amount=-5, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(30, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2, perimeter: 6
            with BuildLine():
                Line((24, 4.5), (26, 4.5))
                Line((24, 3.5), (24, 4.5))
                Line((26, 3.5), (24, 3.5))
                Line((26, 4.5), (26, 3.5))
            make_face()
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((17, 4)):
                Circle(1)
        # OneSide extrude, distance=-8
        extrude(amount=-8, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 16 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 7, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 14.6996449638, perimeter: 18.6996449638
            with BuildLine():
                Line((21.1501775181, 28.5), (28.5, 28.5))
                Line((21.1501775181, 26.5), (21.1501775181, 28.5))
                Line((28.5, 26.5), (21.1501775181, 26.5))
                Line((28.5, 28.5), (28.5, 26.5))
            make_face()
            # Profile area: 14.6996449638, perimeter: 18.6996449638
            with BuildLine():
                Line((21.1501775181, -26.5), (28.5, -26.5))
                Line((21.1501775181, -28.5), (21.1501775181, -26.5))
                Line((28.5, -28.5), (21.1501775181, -28.5))
                Line((28.5, -26.5), (28.5, -28.5))
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a hexagonal or prismatic enclosure/housing with two large circular apertures or holes on one face, a small rectangular slot at the bottom, and an internal mounting structure visible through the openings.
def model_51580_817b17c1_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 150, perimeter: 50
            with BuildLine():
                Line((-5, 5), (-5, -10))
                Line((-5, -10), (5, -10))
                Line((5, 5), (5, -10))
                Line((-5, 5), (5, 5))
            make_face()
        # OneSide extrude, distance=12.5
        extrude(amount=12.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 12.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 28.2743338823, perimeter: 18.8495559215
            Circle(3)
        # OneSide extrude, distance=-6.5
        extrude(amount=-6.5, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 12.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((0, -5)):
                Circle(1)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 12.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((-3, -5)):
                Circle(0.6)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 12.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((3, -5)):
                Circle(0.6)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8, mode=Mode.ADD)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 12.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.1604331151, perimeter: 5.0504435629
            with BuildLine():
                Line((0.9212102729, -8.6040115085), (-1, -8.6040115085))
                Line((0.9212102729, -8), (0.9212102729, -8.6040115085))
                Line((-1, -8), (0.9212102729, -8))
                Line((-1, -8.6040115085), (-1, -8))
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 12.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((3, -8)):
                Circle(0.4)
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a pair of dark metal bracket or mounting clips with bent, angled profiles featuring cylindrical holes or bosses at one end for fastening purposes.
def model_51584_b39d033d_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 30 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.9215918246, perimeter: 105.9173191312
            with BuildLine():
                Line((11.2862087406, -15.8801312041), (9.5422101996, -16.8286328317))
                CenterArc((7.2249951542, -12.5679973822), 4.85, -97, 35.5402689729)
                Line((6.6339288387, -17.3818462177), (-12.9110116319, -14.9820292842))
                Line((-12.9110116319, -14.9820292842), (-13.1713419833, -14.9820292842))
                Line((-13.1713419833, -14.9820292842), (-13.1713419833, -15.1320292842))
                Line((-13.1713419833, -15.1320292842), (-12.9110116319, -15.133155758))
                Line((6.6156484372, -17.5307281404), (-12.9110116319, -15.133155758))
                CenterArc((7.2249951542, -12.5679973822), 5, -97, 35.5402689729)
                Line((11.3578751854, -16.0119034345), (9.6138766443, -16.9604050621))
                CenterArc((10.6889883681, -14.7820292842), 1.4, -61.4597310271, 122.9194620543)
                Line((11.3578751854, -13.5521551338), (9.6138766443, -12.6036535062))
                CenterArc((7.2249951542, -16.9960611861), 5, 61.4597310271, 35.5402689729)
                Line((6.6156484372, -12.0333304279), (-12.9110116319, -14.4309028103))
                Line((-13.1713419833, -14.4320292842), (-12.9110116319, -14.4309028103))
                Line((-13.1713419833, -14.5820292842), (-13.1713419833, -14.4320292842))
                Line((-12.9110116319, -14.5820292842), (-13.1713419833, -14.5820292842))
                Line((6.6339288387, -12.1822123506), (-12.9110116319, -14.5820292842))
                CenterArc((7.2249951542, -16.9960611861), 4.85, 61.4597310271, 35.5402689729)
                Line((11.2862087406, -13.6839273642), (9.5422101996, -12.7354257366))
                CenterArc((10.6889883681, -14.7820292842), 1.25, -61.4597310271, 122.9194620543)
            make_face()
        # Symmetric extrude, each_side=1.5
        extrude(amount=1.5, both=True)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.0657230945, 0, 15.1887385248), x_dir=(0.9999906383, 0, 0.0043270532), z_dir=(-0.0043270532, 0, 0.9999906383))):
            # Profile area: 18.613072155, perimeter: 15.490457724
            with BuildLine():
                Line((-13.1057415814, 1.5), (-13.1057415814, -1.5))
                CenterArc((-15.1057415814, 0), 2.5, 36.8698976458, 286.2602047083)
            make_face()
        # OneSide extrude, distance=-0.15
        extrude(amount=-0.15, mode=Mode.ADD)

        # Sketch11 -> Extrude6 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 24 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.0006350315, perimeter: 66.9751337539
            with BuildLine():
                Line((-45.0438255992, -13.6292008423), (-36.9378088855, -13.6292008423))
                CenterArc((-36.9378088855, -10.4792008423), 3.15, -90, 52.8771217103)
                Line((-34.4261784248, -12.380309053), (-33.4354351887, -11.0713983468))
                CenterArc((-27.9736356154, -15.205554297), 6.85, 116.1911181377, 26.6860035725)
                Line((-30.9969978975, -9.0588657161), (-26.5902704216, -6.8913354332))
                Line((-26.6564754351, -6.7567364132), (-26.5902704216, -6.8913354332))
                Line((-31.063202911, -8.9242666961), (-26.6564754351, -6.7567364132))
                CenterArc((-27.9736356154, -15.205554297), 7, 116.1911181377, 26.6860035725)
                Line((-34.5457798753, -12.2897800906), (-33.5550366392, -10.9808693843))
                CenterArc((-36.9378088855, -10.4792008423), 3, -90, 52.8771217103)
                Line((-36.9378088855, -13.4792008423), (-45.0438255992, -13.4792008423))
                CenterArc((-45.0438255992, -10.4792008423), 3, -142.8771217103, 52.8771217103)
                Line((-47.4358546094, -12.2897800906), (-48.4265978456, -10.9808693843))
                CenterArc((-54.0079988694, -15.205554297), 7, 37.1228782897, 26.6860035725)
                Line((-50.9184315737, -8.9242666961), (-55.3251590497, -6.7567364132))
                Line((-55.3251590497, -6.7567364132), (-55.3913640631, -6.8913354332))
                Line((-50.9846365872, -9.0588657161), (-55.3913640631, -6.8913354332))
                CenterArc((-54.0079988694, -15.205554297), 6.85, 37.1228782897, 26.6860035725)
                Line((-47.5554560599, -12.380309053), (-48.5461992961, -11.0713983468))
                CenterArc((-45.0438255992, -10.4792008423), 3.15, -142.8771217103, 52.8771217103)
            make_face()
        # Symmetric extrude, each_side=1.5
        extrude(amount=1.5, both=True)

        # Sketch12 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 13.4792008423), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.9503317777, perimeter: 3.4557519189
            with Locations((40.9908172424, 0)):
                Circle(0.55)
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a complex stamped or cast metal housing with an irregular polygonal shape, featuring multiple angled faces, internal ribbing/reinforcement structures, and what appears to be mounting flanges or tabs protruding from its sides.
def model_51727_9778bc01_0001():
    """Model: serwo"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 7, perimeter: 11
            with BuildLine():
                Line((-2, -1), (1.5, -1))
                Line((-2, -3), (-2, -1))
                Line((1.5, -3), (-2, -3))
                Line((1.5, -1), (1.5, -3))
            make_face()
        # OneSide extrude, distance=3.5
        extrude(amount=3.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.4000000671, perimeter: 5.4000001252
            with BuildLine():
                Line((-1.2000000179, -1), (-1.2000000179, -3.0000000447))
                Line((-1.2000000179, -3.0000000447), (-0.5, -3.0000000447))
                Line((-0.5, -3.0000000447), (-0.5, -1))
                Line((-0.5, -1), (-1.2000000179, -1))
            make_face()
        # OneSide extrude, distance=0.7
        extrude(amount=0.7, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-2, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 1.4000000358, perimeter: 5.4000000358
            with BuildLine():
                Line((1.2000000179, -3), (1.2000000179, -1))
                Line((1.2000000179, -1), (0.5, -1))
                Line((0.5, -1), (0.5, -3))
                Line((0.5, -3), (1.2000000179, -3))
            make_face()
        # OneSide extrude, distance=0.7
        extrude(amount=0.7, mode=Mode.ADD)

        # Sketch5 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 2.2698006922, perimeter: 5.3407075111
            with Locations((-0.5000000075, -2.0000000298)):
                Circle(0.85)
            # Profile area: 0.6361725124, perimeter: 2.8274333882
            with Locations((0.8000000119, -2.0000000298)):
                Circle(0.45)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)

        # Sketch6 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.5), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-1.85, -2.0000000447)):
                Circle(0.2)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((2.35, -2)):
                Circle(0.2)
        # OneSide extrude, distance=-0.7
        extrude(amount=-0.7, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.4), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-0.5000000075, -2.0000000298)):
                Circle(0.2)
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a two-piece solar panel bracket or mounting frame with a bent/articulated design, featuring a truss-like lattice structure with triangular reinforcements and a hinge or pivot joint connecting the upper and lower sections at an angle.
def model_51891_9455ea02_0000():
    """Model: Base v1"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 20 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 200.32218, perimeter: 78.74
            with BuildLine():
                Line((-1.905, 1.778), (-1.905, -2.54))
                Line((-6.35, -2.54), (-1.905, -2.54))
                Line((-6.35, -10.16), (-6.35, -2.54))
                Line((6.35, -10.16), (-6.35, -10.16))
                Line((6.35, -2.54), (6.35, -10.16))
                Line((6.35, -2.54), (1.905, -2.54))
                Line((1.905, 1.778), (1.905, -2.54))
                Line((6.35, 1.778), (1.905, 1.778))
                Line((6.35, 5.08), (6.35, 1.778))
                Line((6.35, 5.08), (2.54, 10.16))
                Line((-2.54, 10.16), (2.54, 10.16))
                Line((-6.35, 5.08), (-2.54, 10.16))
                Line((-6.35, 1.778), (-6.35, 5.08))
                Line((-6.35, 1.778), (-1.905, 1.778))
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 24 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.635, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1946567452, perimeter: 1.5640104867
            with Locations((-2.54, 6.35)):
                Circle(0.24892)
            # Profile area: 0.1946567452, perimeter: 1.5640104867
            with Locations((2.54, 6.35)):
                Circle(0.24892)
            # Profile area: 0.1946567452, perimeter: 1.5640104867
            with Locations((-2.54, -6.35)):
                Circle(0.24892)
            # Profile area: 0.1946567452, perimeter: 1.5640104867
            with Locations((2.54, -6.35)):
                Circle(0.24892)
        # OneSide extrude, distance=-2.032
        extrude(amount=-2.032, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-6.35, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.1946567452, perimeter: 1.5640104867
            with Locations((9.8425, 0.3175)):
                Circle(0.24892)
        # OneSide extrude, distance=-0.762
        extrude(amount=-0.762, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.1946567452, perimeter: 1.5640104867
            with Locations((5.08, 9.8425)):
                Circle(0.24892)
            # Profile area: 0.1946567452, perimeter: 1.5640104867
            with Locations((-5.08, 9.8425)):
                Circle(0.24892)
        # OneSide extrude, distance=-0.889
        extrude(amount=-0.889, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.1946567452, perimeter: 1.5640104867
            with Locations((-5.715, -5.3975)):
                Circle(0.24892)
        # OneSide extrude, distance=-3.556
        extrude(amount=-3.556, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.635, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1946567452, perimeter: 1.5640104867
            with Locations((-3.29438, -3.81)):
                Circle(0.24892)
            # Profile area: 0.1946567452, perimeter: 1.5640104867
            with Locations((3.29438, -3.81)):
                Circle(0.24892)
            # Profile area: 0.1946567452, perimeter: 1.5640104867
            with Locations((3.81, -2.54)):
                Circle(0.24892)
            # Profile area: 0.1946567452, perimeter: 1.5640104867
            with Locations((3.81, 4.445)):
                Circle(0.24892)
        # OneSide extrude, distance=-2.032
        extrude(amount=-2.032, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a satellite component with a polygonal box-shaped main body, an angled top section with internal structural framing, and a rectangular flat mounting plate extending from the bottom, designed for structural support and assembly integration.
def model_51932_c1f74efe_0001():
    """Model: Control Box"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 174.1932, perimeter: 60.96
            with BuildLine():
                Line((-11.43, 7.62), (-11.43, 0))
                Line((-11.43, 0), (11.43, 0))
                Line((11.43, 0), (11.43, 7.62))
                Line((11.43, 7.62), (-11.43, 7.62))
            make_face()
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 14 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.27), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with Locations((-2.8574999571, 3.8099999428)):
                Circle(0.3175)
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with Locations((2.8574999571, 3.8099999428)):
                Circle(0.3175)
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with Locations((8.5724998713, 3.8099999428)):
                Circle(0.3175)
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with Locations((-8.5724998713, 3.8099999428)):
                Circle(0.3175)
        # OneSide extrude, distance=-1.27
        extrude(amount=-1.27, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 1.6128999758, perimeter: 5.0799999619
            with BuildLine():
                Line((-11.43, 1.2699999809), (-11.43, 0))
                Line((-11.43, 0), (-10.16, 0))
                Line((-10.16, 0), (-10.16, 1.2699999809))
                Line((-10.16, 1.2699999809), (-11.43, 1.2699999809))
            make_face()
            # Profile area: 1.6129001696, perimeter: 5.080000267
            with BuildLine():
                Line((10.1599998474, 0), (10.1599998474, 1.2699999809))
                Line((11.43, 0), (10.1599998474, 0))
                Line((11.43, 1.2699999809), (11.43, 0))
                Line((10.1599998474, 1.2699999809), (11.43, 1.2699999809))
            make_face()
        # OneSide extrude, distance=12.7
        extrude(amount=12.7, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -12.7), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 288.7091000242, perimeter: 71.12
            with BuildLine():
                Line((-10.16, 0), (11.43, 0))
                Line((11.43, 0), (11.43, 12.7))
                Line((11.43, 12.7), (-11.43, 12.7))
                Line((-11.43, 12.7), (-11.43, 1.2699999809))
                Line((-10.16, 1.2699999809), (-11.43, 1.2699999809))
                Line((-10.16, 0), (-10.16, 1.2699999809))
            make_face()
            # Profile area: 1.6128999758, perimeter: 5.0799999619
            with BuildLine():
                Line((-10.16, 0), (-10.16, 1.2699999809))
                Line((-10.16, 1.2699999809), (-11.43, 1.2699999809))
                Line((-11.43, 1.2699999809), (-11.43, 0))
                Line((-11.43, 0), (-10.16, 0))
            make_face()
        # OneSide extrude, distance=22.86
        extrude(amount=22.86, mode=Mode.ADD)

        # Sketch7 -> Extrude6 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, -12.7), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with Locations((-8.5724998713, 3.8099999428)):
                Circle(0.3175)
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with Locations((-2.8574999571, 3.8099999428)):
                Circle(0.3175)
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with Locations((2.8574999571, 3.8099999428)):
                Circle(0.3175)
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with Locations((8.5724998713, 3.8099999428)):
                Circle(0.3175)
        # OneSide extrude, distance=-1.27
        extrude(amount=-1.27, mode=Mode.SUBTRACT)

        # Sketch9 -> Extrude8 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 12.7, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 81.0731826532, perimeter: 31.9185786041
            with Locations((0, -24.13)):
                Circle(5.0799995613)
        # OneSide extrude, distance=-1.27
        extrude(amount=-1.27, mode=Mode.SUBTRACT)

        # Sketch10 -> Extrude9 (Join)
        # Sketch on BRepFace
        # Sketch has 47 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.27), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 3.2258023103, perimeter: 8.3820026875
            with BuildLine():
                Line((-6.9849994183, 5.8419997811), (-10.1600003242, 5.8419997811))
                Line((-6.9849994183, 6.8580002189), (-6.9849994183, 5.8419997811))
                Line((-10.1600003242, 6.8580002189), (-6.9849994183, 6.8580002189))
                Line((-10.1600003242, 5.8419997811), (-10.1600003242, 6.8580002189))
            make_face()
            # Profile area: 3.2258023103, perimeter: 8.3820026875
            with BuildLine():
                Line((-1.2699995041, 5.8419997811), (-4.4450004101, 5.8419997811))
                Line((-1.2699995041, 6.8580002189), (-1.2699995041, 5.8419997811))
                Line((-4.4450004101, 6.8580002189), (-1.2699995041, 6.8580002189))
                Line((-4.4450004101, 5.8419997811), (-4.4450004101, 6.8580002189))
            make_face()
            # Profile area: 3.2258023103, perimeter: 8.3820026875
            with BuildLine():
                Line((4.4450004101, 5.8419997811), (1.2699995041, 5.8419997811))
                Line((4.4450004101, 6.8580002189), (4.4450004101, 5.8419997811))
                Line((1.2699995041, 6.8580002189), (4.4450004101, 6.8580002189))
                Line((1.2699995041, 5.8419997811), (1.2699995041, 6.8580002189))
            make_face()
            # Profile area: 3.2258023103, perimeter: 8.3820026875
            with BuildLine():
                Line((10.1600003242, 5.8419997811), (6.9849994183, 5.8419997811))
                Line((10.1600003242, 6.8580002189), (10.1600003242, 5.8419997811))
                Line((6.9849994183, 6.8580002189), (10.1600003242, 6.8580002189))
                Line((6.9849994183, 5.8419997811), (6.9849994183, 6.8580002189))
            make_face()
        # OneSide extrude, distance=0.0635
        extrude(amount=0.0635, mode=Mode.ADD)
    return part.part


# Description: This is a desktop antenna or stand with a curved loop-shaped upper section mounted on a flat triangular base, featuring a cylindrical connector node at the center of the loop.
def model_53434_51d96387_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 585.868726387, perimeter: 287.3777638852
            with BuildLine():
                CenterArc((0, 30.4799995422), 24.9074668741, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 30.4799995422), 20.8301247829, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides extrude (symmetric), distance=1.016
        extrude(amount=1.016, both=True)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -1.016), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))) as sk:
            # Profile area: 182.4146869959, perimeter: 47.8778713217
            with Locations((0, 30.4799995422)):
                Circle(7.6199998856)
        # TwoSides extrude, along=0.762, against=-7.62
        extrude(amount=0.762)
        extrude(sk.sketch, amount=-7.62)

        # Sketch3 -> Extrude3 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1290.3199612427, perimeter: 152.3999977112
            with BuildLine():
                Line((25.3999996185, -12.6999998093), (-25.3999996185, -12.6999998093))
                Line((25.3999996185, 12.6999998093), (25.3999996185, -12.6999998093))
                Line((-25.3999996185, 12.6999998093), (25.3999996185, 12.6999998093))
                Line((-25.3999996185, -12.6999998093), (-25.3999996185, 12.6999998093))
            make_face()
        # OneSide extrude, distance=0.762
        extrude(amount=0.762)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 6.604), x_dir=(1, 0, 0), z_dir=(0, 0, 1))) as sk:
            # Profile area: 146.354386163, perimeter: 58.5656514115
            with BuildLine():
                Line((-2.8237402083, 23.4025077908), (-3.7314096888, 0.762))
                Line((-3.7314096888, 0.762), (3.7314096888, 0.762))
                Line((2.8237402083, 23.4025077908), (3.7314096888, 0.762))
                CenterArc((0, 30.4799995422), 7.6199998856, -111.7507494538, 43.5014989076)
            make_face()
        # TwoSides extrude, along=1.27, against=-0.508
        extrude(amount=1.27, mode=Mode.ADD)
        extrude(sk.sketch, amount=-0.508, mode=Mode.ADD)

        # Sketch5 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 6.604), x_dir=(1, 0, 0), z_dir=(0, 0, 1))) as sk:
            # Profile area: 40.019362965, perimeter: 25.031796281
            with BuildLine():
                Line((-2.5399999619, 30.4799995422), (-2.8237402083, 23.4025077908))
                CenterArc((0, 30.4799995422), 7.6199998856, -111.7507494538, 43.5014989076)
                Line((2.5399999619, 30.4799995422), (2.8237402083, 23.4025077908))
                Line((-2.5399999619, 30.4799995422), (2.5399999619, 30.4799995422))
            make_face()
        # TwoSides extrude, along=1.27, against=-0.508
        extrude(amount=1.27, mode=Mode.ADD)
        extrude(sk.sketch, amount=-0.508, mode=Mode.ADD)

        # Sketch16 -> Extrude9 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.762, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 96.7739970932, perimeter: 40.6399993896
            with BuildLine():
                Line((-22.8599996567, -2.5399999619), (-10.1599998474, -2.5399999619))
                Line((-22.8599996567, -10.1599998474), (-22.8599996567, -2.5399999619))
                Line((-10.1599998474, -10.1599998474), (-22.8599996567, -10.1599998474))
                Line((-10.1599998474, -2.5399999619), (-10.1599998474, -10.1599998474))
            make_face()
        # OneSide extrude, distance=-0.508
        extrude(amount=-0.508, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a vise or clamping jaw assembly featuring a main rectangular body with an angled actuating lever or handle extending from one side, designed for gripping or holding workpieces.
def model_53460_05ff662e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 11 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 21.0886676033, perimeter: 20.0591117356
            with BuildLine():
                Line((1.1859969394, 0), (6.2007748733, 0))
                Line((6.2007748733, 0), (6.2007748733, 5.0147779339))
                Line((6.2007748733, 5.0147779339), (3.2007748733, 5.0147779339))
                Line((3.2007748733, 5.0147779339), (3.2007748733, 3))
                Line((3.2007748733, 3), (1.1859969394, 3))
                Line((1.1859969394, 3), (1.1859969394, 0))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 14, perimeter: 18
            with BuildLine():
                Line((2, -7), (0, -7))
                Line((2, 0), (2, -7))
                Line((0, 0), (2, 0))
                Line((0, -7), (0, 0))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude3 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.8800000858, perimeter: 8.8000001311
            with BuildLine():
                Line((4.0000000596, 3.0000000447), (3.2000000477, 3.0000000447))
                Line((4.0000000596, 6.6000000983), (4.0000000596, 3.0000000447))
                Line((3.2000000477, 6.6000000983), (4.0000000596, 6.6000000983))
                Line((3.2000000477, 3.0000000447), (3.2000000477, 6.6000000983))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch5 -> Extrude4 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.0188979757, perimeter: 6.9503228846
            with BuildLine():
                Line((-1.516334053, 1.7205869922), (-3.2709085031, 1.7205869922))
                Line((-3.2709085031, 1.7205869922), (-3.2709085031, 0))
                Line((-1.516334053, 0), (-3.2709085031, 0))
                Line((-1.516334053, 0), (-1.516334053, 1.7205869922))
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)

        # Sketch8 -> Extrude5 (Join)
        # Sketch on XY construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.8744035273, perimeter: 7.7934506966
            with BuildLine():
                Line((1.0933265252, 1.7205869922), (-0.6000000089, 1.7205869922))
                Line((1.1000000164, 1.9000000283), (1.0933265252, 1.7205869922))
                Line((-0.9000000134, 1.9000000283), (1.1000000164, 1.9000000283))
                Line((-0.9000000134, 0), (-0.9000000134, 1.9000000283))
                Line((-0.6000000089, 0), (-0.9000000134, 0))
                Line((-0.6000000089, 1.7205869922), (-0.6000000089, 0))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)
    return part.part


MODELS = {
    "model_39953_02c01de9_0000": {"func": model_39953_02c01de9_0000, "volume": 361.1480750958, "area": 570.3025790173},
    "model_40070_be9c502b_0015": {"func": model_40070_be9c502b_0015, "volume": 36.1080505937, "area": 66.771156987},
    "model_40072_b44084ae_0017": {"func": model_40072_b44084ae_0017, "volume": 0.4680973159, "area": 7.9168135732},
    "model_40417_b8d98f73_0015": {"func": model_40417_b8d98f73_0015, "volume": 563.4686864843, "area": 603.4069835823},
    "model_40514_bb61631d_0025": {"func": model_40514_bb61631d_0025, "volume": 5.6233134052, "area": 38.910195811},
    "model_40688_effe215a_0001": {"func": model_40688_effe215a_0001, "volume": 111.5960804951, "area": 216.9778619018},
    "model_41229_16283ae1_0004": {"func": model_41229_16283ae1_0004, "volume": 1.0288052988, "area": 10.7725660089},
    "model_41303_e063f288_0000": {"func": model_41303_e063f288_0000, "volume": 6510.2058562688, "area": 14408.4121566315},
    "model_41650_9417da80_0009": {"func": model_41650_9417da80_0009, "volume": 0.4327543641, "area": 12.3541136586},
    "model_41685_df8ac866_0003": {"func": model_41685_df8ac866_0003, "volume": 24.9002633724, "area": 319.1543976782},
    "model_41698_900d863d_0004": {"func": model_41698_900d863d_0004, "volume": 76.9673119072, "area": 126.5553093477},
    "model_41717_3bb49f29_0000": {"func": model_41717_3bb49f29_0000, "volume": 1.4549095659, "area": 23.1919971294},
    "model_41780_da6cd1db_0014": {"func": model_41780_da6cd1db_0014, "volume": 0.3076500429, "area": 8.897772617},
    "model_41896_7d8659e6_0019": {"func": model_41896_7d8659e6_0019, "volume": 5.7599138052, "area": 35.9758618293},
    "model_41920_d3c8f833_0000": {"func": model_41920_d3c8f833_0000, "volume": 34580.1394192574, "area": 8202.1936598795},
    "model_41941_79d46bb4_0004": {"func": model_41941_79d46bb4_0004, "volume": 15.9961815434, "area": 42.3290155331},
    "model_41982_f75ceb8f_0014": {"func": model_41982_f75ceb8f_0014, "volume": 0.5771944524, "area": 8.6680636814},
    "model_41985_e9d6af98_0000": {"func": model_41985_e9d6af98_0000, "volume": 0.0151245392, "area": 1.3440909868},
    "model_42329_df7f540f_0060": {"func": model_42329_df7f540f_0060, "volume": 0.1189834578, "area": 6.8425881403},
    "model_42559_aff60eae_0000": {"func": model_42559_aff60eae_0000, "volume": 1121.2386725965, "area": 1438.5410846728},
    "model_42572_2c23210e_0000": {"func": model_42572_2c23210e_0000, "volume": 476.3535326723, "area": 1570.2594213881},
    "model_43529_4804941b_0058": {"func": model_43529_4804941b_0058, "volume": 2.2836634279, "area": 12.8537542462},
    "model_43928_6ca53538_0028": {"func": model_43928_6ca53538_0028, "volume": 0.8845586085, "area": 8.4526121141},
    "model_43928_6ca53538_0030": {"func": model_43928_6ca53538_0030, "volume": 1.0829442505, "area": 10.7500706802},
    "model_43933_3b763a09_0000": {"func": model_43933_3b763a09_0000, "volume": 105.8052338025, "area": 196.8980997314},
    "model_43934_912ff891_0025": {"func": model_43934_912ff891_0025, "volume": 15.8807786842, "area": 63.0542310027},
    "model_44207_cb5191a8_0000": {"func": model_44207_cb5191a8_0000, "volume": 815.080386702, "area": 1055.2495382103},
    "model_44327_332ad058_0000": {"func": model_44327_332ad058_0000, "volume": 536875.1261256295, "area": 87990.9156398991},
    "model_44333_da7b5f6d_0000": {"func": model_44333_da7b5f6d_0000, "volume": 34.9706300482, "area": 166.85048295},
    "model_44411_d2bc57fb_0000": {"func": model_44411_d2bc57fb_0000, "volume": 197.1693289288, "area": 461.0718040503},
    "model_44524_011bb12f_0000": {"func": model_44524_011bb12f_0000, "volume": 37.7645179066, "area": 269.328169868},
    "model_44916_a8b5eeff_0008": {"func": model_44916_a8b5eeff_0008, "volume": 6.9444601444, "area": 26.571234344},
    "model_45112_54374f79_0000": {"func": model_45112_54374f79_0000, "volume": 216.5440055519, "area": 438.9018245387},
    "model_45269_a8765cc8_0000": {"func": model_45269_a8765cc8_0000, "volume": 0.0365602845, "area": 0.8837692834},
    "model_45359_1768ab3f_0024": {"func": model_45359_1768ab3f_0024, "volume": 5.0524663851, "area": 23.6404847183},
    "model_45360_cb4bac3f_0007": {"func": model_45360_cb4bac3f_0007, "volume": 587.3851566932, "area": 998.979874145},
    "model_45360_cb4bac3f_0019": {"func": model_45360_cb4bac3f_0019, "volume": 3.1296420536, "area": 15.0793377299},
    "model_48907_25974aa4_0002": {"func": model_48907_25974aa4_0002, "volume": 0.93134291, "area": 12.7723449646},
    "model_49019_748c9a9f_0017": {"func": model_49019_748c9a9f_0017, "volume": 2.0420352248, "area": 28.5884931477},
    "model_49134_e9867f8b_0005": {"func": model_49134_e9867f8b_0005, "volume": 131.431365331, "area": 298.499162029},
    "model_49902_81b1dde9_0000": {"func": model_49902_81b1dde9_0000, "volume": 72.1642076863, "area": 281.885668662},
    "model_51471_289b2a1d_0011": {"func": model_51471_289b2a1d_0011, "volume": 2417.4715755987, "area": 9888.0983363392},
    "model_51580_817b17c1_0000": {"func": model_51580_817b17c1_0000, "volume": 1692.2134853769, "area": 1073.7079550022},
    "model_51584_b39d033d_0000": {"func": model_51584_b39d033d_0000, "volume": 41.4159455862, "area": 581.7871800263},
    "model_51727_9778bc01_0001": {"func": model_51727_9778bc01_0001, "volume": 27.1951328579, "area": 67.0971677955},
    "model_51891_9455ea02_0000": {"func": model_51891_9455ea02_0000, "volume": 125.6965784952, "area": 458.4782008464},
    "model_51932_c1f74efe_0001": {"func": model_51932_c1f74efe_0001, "volume": 6793.5927651708, "area": 2815.2335878944},
    "model_53434_51d96387_0000": {"func": model_53434_51d96387_0000, "volume": 3964.5904679252, "area": 5620.7626647192},
    "model_53460_05ff662e_0000": {"func": model_53460_05ff662e_0000, "volume": 97.6574379735, "area": 164.8121441194},
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
