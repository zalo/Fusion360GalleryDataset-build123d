"""Batch 003 - passing/04_6to7ops
82 models bundled from Fusion360 Gallery reconstructions.
"""

from build123d import *
from build123d import Edge, BuildLine
from collections import Counter
from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
from OCP.Geom import Geom_BSplineCurve
from OCP.TColStd import TColStd_Array1OfReal, TColStd_Array1OfInteger
from OCP.TColgp import TColgp_Array1OfPnt
from OCP.gp import gp_Pnt


# Description: This is a modular mounting bracket or adapter assembly featuring a rectangular box-shaped base with angular faceted surfaces, a cylindrical connector protruding from the right side, and an angled mounting flange on top.
def model_144912_34c55160_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.1600000644, perimeter: 6.0000000894
            with BuildLine():
                Line((1.3000000194, -0.7000000104), (0.7000000104, -0.7000000104))
                Line((1.3000000194, 0.5000000075), (1.3000000194, -0.7000000104))
                Line((-0.5000000075, 0.5000000075), (1.3000000194, 0.5000000075))
                Line((-0.5000000075, -0.7000000104), (-0.5000000075, 0.5000000075))
                Line((0.200000003, -0.7000000104), (-0.5000000075, -0.7000000104))
                Line((0.200000003, -0.7000000104), (0.7000000104, -0.7000000104))
            make_face()
        # OneSide extrude, distance=0.9
        extrude(amount=0.9)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 12 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2500000075, perimeter: 2.0000000298
            with BuildLine():
                Line((0.6000000089, 1.0000000149), (0.1000000015, 1.0000000149))
                Line((0.1000000015, 1.0000000149), (0.1000000015, 0.5500000082))
                Line((0.1000000015, 0.5500000082), (0.1000000015, 0.5000000075))
                Line((0.1000000015, 0.5000000075), (0.6000000089, 0.5000000075))
                Line((0.6000000089, 0.5000000075), (0.6000000089, 0.5500000082))
                Line((0.6000000089, 0.5500000082), (0.6000000089, 1.0000000149))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 27 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.9), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1084819978, perimeter: 1.3074815359
            with BuildLine():
                CenterArc((-0.5000000075, 0.1000000015), 0.4031128934, 7.1250163489, 40.9661357693)
                Line((-0.5000000075, 0.400000006), (-0.2307417631, 0.400000006))
                Line((-0.5000000075, 0.1000000015), (-0.5000000075, 0.400000006))
                Line((-0.5000000075, 0.1000000015), (-0.1000000015, 0.1000000015))
                Line((-0.1000000015, 0.1000000015), (-0.1000000015, 0.1500000022))
            make_face()
            # Profile area: 0.0190413642, perimeter: 0.6672270036
            with BuildLine():
                Line((-0.7692582518, -0.200000003), (-0.5000000075, -0.200000003))
                CenterArc((-0.5000000075, 0.1000000015), 0.4031128934, -131.9088478818, 41.9088478818)
                Line((-0.5000000075, -0.3031128919), (-0.5000000075, -0.200000003))
            make_face()
            # Profile area: 0.0190413642, perimeter: 0.6672270036
            with BuildLine():
                Line((-0.5000000075, -0.200000003), (-0.2307417631, -0.200000003))
                Line((-0.5000000075, -0.3031128919), (-0.5000000075, -0.200000003))
                CenterArc((-0.5000000075, 0.1000000015), 0.4031128934, -90, 41.9088478818)
            make_face()
            # Profile area: 0.1084819978, perimeter: 1.3074815359
            with BuildLine():
                Line((-0.9000000134, 0.1500000022), (-0.9000000134, 0.1000000015))
                Line((-0.9000000134, 0.1000000015), (-0.5000000075, 0.1000000015))
                Line((-0.5000000075, 0.1000000015), (-0.5000000075, 0.400000006))
                Line((-0.5000000075, 0.400000006), (-0.7692582518, 0.400000006))
                CenterArc((-0.5000000075, 0.1000000015), 0.4031128934, 131.9088478818, 40.9661357693)
            make_face()
            # Profile area: 0.1084819978, perimeter: 1.3074815359
            with BuildLine():
                CenterArc((-0.5000000075, 0.1000000015), 0.4031128934, -172.8749836511, 40.9661357693)
                Line((-0.7692582518, -0.200000003), (-0.5000000075, -0.200000003))
                Line((-0.5000000075, -0.200000003), (-0.5000000075, 0.1000000015))
                Line((-0.9000000134, 0.1000000015), (-0.5000000075, 0.1000000015))
                Line((-0.9000000134, 0.0500000007), (-0.9000000134, 0.1000000015))
            make_face()
            # Profile area: 0.0190413642, perimeter: 0.6672270036
            with BuildLine():
                Line((-0.5000000075, 0.5031128949), (-0.5000000075, 0.400000006))
                Line((-0.5000000075, 0.400000006), (-0.2307417631, 0.400000006))
                CenterArc((-0.5000000075, 0.1000000015), 0.4031128934, 48.0911521182, 41.9088478818)
            make_face()
            # Profile area: 0.1084819978, perimeter: 1.3074815359
            with BuildLine():
                Line((-0.1000000015, 0.0500000007), (-0.1000000015, 0.1000000015))
                Line((-0.5000000075, 0.1000000015), (-0.1000000015, 0.1000000015))
                Line((-0.5000000075, -0.200000003), (-0.5000000075, 0.1000000015))
                Line((-0.5000000075, -0.200000003), (-0.2307417631, -0.200000003))
                CenterArc((-0.5000000075, 0.1000000015), 0.4031128934, -48.0911521182, 40.9661357693)
            make_face()
            # Profile area: 0.0190413642, perimeter: 0.6672270036
            with BuildLine():
                Line((-0.5000000075, 0.400000006), (-0.7692582518, 0.400000006))
                Line((-0.5000000075, 0.5031128949), (-0.5000000075, 0.400000006))
                CenterArc((-0.5000000075, 0.1000000015), 0.4031128934, 90, 41.9088478818)
            make_face()
        # OneSide extrude, distance=0.8
        extrude(amount=0.8, mode=Mode.ADD)
    return part.part


# Description: This is a truss or structural bracket with a parallelogram-shaped profile, featuring two horizontal flanges connected by internal diagonal and vertical bracing members, designed to provide lightweight rigidity and support.
def model_144917_3c8ef27d_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 53 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 17.5359468809, perimeter: 70.9920153493
            with BuildLine():
                Line((0, 0), (0, -10))
                Line((13, -10), (0, -10))
                Line((13, -9.5), (13, -10))
                Line((13, -9.5), (0.5, -9.5))
                Line((0.5079881958, -0.5), (0.5, -9.5))
                Line((13, -0.5), (0.5079881958, -0.5))
                Line((13, 0), (13, -0.5))
                Line((0, 0), (13, 0))
            make_face()
        # OneSide extrude, distance=1.39
        extrude(amount=1.39)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 53 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 87.9689109126, perimeter: 120.7121379069
            with BuildLine():
                Line((13, -0.5), (0.5079881958, -0.5))
                Line((0.5079881958, -0.5), (0.5, -9.5))
                Line((13, -9.5), (0.5, -9.5))
                Line((13, -0.5), (13, -9.5))
            make_face()
            with BuildLine():
                CenterArc((3.0204590959, -1.95), 0.21, 90, 180)
                Line((3.0204590959, -1.74), (11.500886564, -1.74))
                CenterArc((11.500886564, -1.95), 0.21, -90, 180)
                Line((3.0204590959, -2.16), (11.500886564, -2.16))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((11.500886564, -8.0651923452), 0.21, -90, 180)
                Line((3.0204590959, -8.2751923452), (11.500886564, -8.2751923452))
                CenterArc((3.0204590959, -8.0651923452), 0.21, 90, 180)
                Line((11.500886564, -7.8551923452), (3.0204590959, -7.8551923452))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((4.2501985183, -7.0972960554), (7.9385435376, -5))
                Line((4.2501985183, -3.3668786594), (4.2501985183, -7.0972960554))
                Line((7.9385435376, -5), (4.2501985183, -3.3668786594))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((9.604238793, -7.1377616557), (4.9899533243, -7.1377616557))
                Line((4.9899533243, -7.1377616557), (7.768163687, -5.8090523518))
                Line((7.768163687, -5.8090523518), (9.604238793, -7.1377616557))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((8.2695685842, -4.1834393297), (5.2715058442, -3.2126132784))
                Line((5.2715058442, -3.2126132784), (9.6882679272, -3.2126132784))
                Line((9.6882679272, -3.2126132784), (8.2695685842, -4.1834393297))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((2.0046713817, -7.0514818308), (2.0046713817, -3.5140090087))
                Line((2.0046713817, -3.5140090087), (3.4196605106, -3.5140090087))
                Line((3.4196605106, -3.5140090087), (3.4196605106, -7.0514818308))
                Line((3.4196605106, -7.0514818308), (2.0046713817, -7.0514818308))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 5.0054855869, perimeter: 9.9049239019
            with BuildLine():
                Line((3.4196605106, -7.0514818308), (2.0046713817, -7.0514818308))
                Line((3.4196605106, -3.5140090087), (3.4196605106, -7.0514818308))
                Line((2.0046713817, -3.5140090087), (3.4196605106, -3.5140090087))
                Line((2.0046713817, -7.0514818308), (2.0046713817, -3.5140090087))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch2 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 10), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((1.5, 0.695)):
                Circle(0.15)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((11.5, 0.695)):
                Circle(0.15)
        # OneSide extrude, distance=-11
        extrude(amount=-11, mode=Mode.SUBTRACT)

        # Sketch1 -> Extrude5 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 53 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.0054855869, perimeter: 9.9049239019
            with BuildLine():
                Line((3.4196605106, -7.0514818308), (2.0046713817, -7.0514818308))
                Line((3.4196605106, -3.5140090087), (3.4196605106, -7.0514818308))
                Line((2.0046713817, -3.5140090087), (3.4196605106, -3.5140090087))
                Line((2.0046713817, -7.0514818308), (2.0046713817, -3.5140090087))
            make_face()
        # OneSide extrude, distance=4.5
        extrude(amount=4.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a hexagonal or prismatic connector body with a tapered/twisted design, featuring multiple flat faceted surfaces and angular geometry, likely designed as a housing or coupling component for mechanical assembly.
def model_145115_4a4d447b_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 38, perimeter: 27.807764064
            with BuildLine():
                Line((0, 0), (9.5, 0))
                Line((0, 0), (0, -2))
                Line((0, -2), (9.5, -6))
                Line((9.5, -6), (9.5, 0))
            make_face()
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 12, perimeter: 16
            with BuildLine():
                Line((9.5, 0), (11.5, 0))
                Line((9.5, -6), (9.5, 0))
                Line((11.5, -6), (9.5, -6))
                Line((11.5, 0), (11.5, -6))
            make_face()
        # OneSide extrude, distance=6
        extrude(amount=6, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 16.4087385212, perimeter: 25.3079632679
            with BuildLine():
                Line((0.00244629, -1.194811667), (0.00244629, -3.494811667))
                CenterArc((2.50244629, -3.494811667), 2.5, 180, 180)
                Line((5.00244629, -1.194811667), (5.00244629, -3.494811667))
                Line((0.00244629, -1.194811667), (5.00244629, -1.194811667))
            make_face()
            with BuildLine():
                CenterArc((2.50244629, -3.494811667), 1.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude4 (Join)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 16.4087385212, perimeter: 25.3079632679
            with BuildLine():
                Line((0.00244629, -1.194811667), (0.00244629, -3.494811667))
                CenterArc((2.50244629, -3.494811667), 2.5, 180, 180)
                Line((5.00244629, -1.194811667), (5.00244629, -3.494811667))
                Line((0.00244629, -1.194811667), (5.00244629, -1.194811667))
            make_face()
            with BuildLine():
                CenterArc((2.50244629, -3.494811667), 1.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.ADD)
    return part.part


# Description: This is a motorcycle or ATV seat featuring an ergonomic curved design with a raised rear section, a contoured sitting surface, and integrated side panels or flanges for structural support.
def model_145236_c9905a23_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 31 constraints, 23 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 25.0962987539, perimeter: 39.8353948475
            with BuildLine():
                CenterArc((0, 0), 3.8, 177.2921048021, 182.7078951979)
                CenterArc((0, 0), 3.8, 0, 177.2921048021)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.54, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=6.4
        extrude(amount=6.4)

        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 31 constraints, 23 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4.6181412008, perimeter: 13.1946891451
            with BuildLine():
                CenterArc((-22.2, -10.2), 1.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-22.2, -10.2), 0.7, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 4.6181412008, perimeter: 13.1946891451
            with BuildLine():
                CenterArc((-11.4, -14), 1.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-11.4, -14), 0.7, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 4.6181412008, perimeter: 13.1946891451
            with BuildLine():
                CenterArc((-4.4, -10.2), 1.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-4.4, -10.2), 0.7, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 4.6181412008, perimeter: 13.1946891451
            with BuildLine():
                CenterArc((1.9, -14), 1.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((1.9, -14), 0.7, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.7
        extrude(amount=1.7)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XY construction plane
        # Sketch has 31 constraints, 23 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 156.2333998562, perimeter: 106.0560925361
            with BuildLine():
                CenterArc((-22.2, -10.2), 1.9, 90, 160.6154843206)
                Line((-12.030621802, -15.7922935426), (-22.830621802, -11.9922935426))
                CenterArc((-11.4, -14), 1.9, -109.3845156794, 19.3845156794)
                Line((1.9, -15.9), (-11.4, -15.9))
                CenterArc((1.9, -14), 1.9, -90, 90)
                Line((3.8, -10.2), (3.8, -14))
                CenterArc((1.9, -10.2), 1.9, 0, 90)
                Line((-12.6858188541, -8.3), (1.9, -8.3))
                Line((-22.2, -8.3), (-12.6858188541, -8.3))
            make_face()
            with BuildLine():
                CenterArc((-22.2, -10.2), 1.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-11.4, -14), 1.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.9, -14), 1.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-4.4, -10.2), 1.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-19.7, -11.5), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.9, -14), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.9
        extrude(amount=1.9, mode=Mode.ADD)

        # Sketch1 -> Extrude4 (Join)
        # Sketch on XY construction plane
        # Sketch has 31 constraints, 23 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 58.0496370277, perimeter: 53.4474366635
            with BuildLine():
                Line((-12.6858188541, -8.3), (1.9, -8.3))
                CenterArc((1.9, -10.2), 1.9, 0, 90)
                Line((3.8, 0), (3.8, -10.2))
                CenterArc((0, 0), 3.8, 177.2921048021, 182.7078951979)
                CenterArc((-12.6858188541, 0.6), 8.9, -90, 87.2921048021)
            make_face()
        # Start offset: 0.3 (not directly supported, may affect result)
        # OneSide extrude, distance=1.6
        extrude(amount=1.6, mode=Mode.ADD)
    return part.part


# Description: This is a modular connector or coupling assembly consisting of multiple rectangular block components with angular faces and integrated slots or channels, designed to connect or interlock together as a multi-piece system.
def model_145418_53431480_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 12 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((-6.5, 2.5)):
                Circle(1)
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 12 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 6.25, perimeter: 10
            with BuildLine():
                Line((1.5, 1), (-1, 1))
                Line((1.5, 3.5), (1.5, 1))
                Line((-1, 3.5), (1.5, 3.5))
                Line((-1, 1), (-1, 3.5))
            make_face()
        # OneSide extrude, distance=8
        extrude(amount=8)

        # Sketch1 -> Extrude3 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 12 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 11.9913429477, perimeter: 13.9942286318
            with BuildLine():
                Line((1.4971143159, -4), (-2.5, -4))
                Line((1.4971143159, -1), (1.4971143159, -4))
                Line((-2.5, -1), (1.4971143159, -1))
                Line((-2.5, -4), (-2.5, -1))
            make_face()
        # OneSide extrude, distance=8
        extrude(amount=8)

        # Sketch1 -> Extrude4 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 12 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 8, perimeter: 12
            with BuildLine():
                Line((5, -2.5), (3, -2.5))
                Line((5, 1.5), (5, -2.5))
                Line((3, 1.5), (5, 1.5))
                Line((3, -2.5), (3, 1.5))
            make_face()
        # OneSide extrude, distance=9
        extrude(amount=9)

        # Sketch1 -> Extrude5 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 12 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((8, -1.5)):
                Circle(1)
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a U-shaped bracket or frame with two vertical legs connected by a horizontal top section, featuring a rectangular open center and flat mounting surfaces on the inner and outer faces.
def model_145540_a4f54d5f_0009():
    """Model: Support Front v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1548.384, perimeter: 172.72
            with BuildLine():
                Line((0, 25.4), (0, 0))
                Line((0, 0), (60.96, 0))
                Line((60.96, 0), (60.96, 25.4))
                Line((60.96, 25.4), (0, 25.4))
            make_face()
        # OneSide extrude, distance=5.08
        extrude(amount=5.08)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 5.08), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 950, perimeter: 135
            with BuildLine():
                Line((-55, 0), (-7.5, 0))
                Line((-55, -20), (-55, 0))
                Line((-7.5, -20), (-55, -20))
                Line((-7.5, 0), (-7.5, -20))
            make_face()
        # OneSide extrude, distance=-12.5
        extrude(amount=-12.5, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 5.08), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 5.067074791, perimeter: 7.9796453401
            with Locations((-30.48, -22.6935620598)):
                Circle(1.27)
        # OneSide extrude, distance=-8
        extrude(amount=-8, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical sleeve or bushing with a hollow center bore, featuring a mesh or perforated pattern on the upper outer surface and solid walls on the lower portion, designed as a filtration component or structural support ring.
def model_146191_ecf68f7a_0003():
    """Model: Та самая деталь v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6361725313, perimeter: 2.8274334304
            Circle(0.4500000067)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=-1.95
        extrude(amount=-1.95, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.3063052987, perimeter: 4.0840704871
            with BuildLine():
                CenterArc((0, 0), 0.400000006, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.02
        extrude(amount=0.02, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical tube or pipe with rounded ends, featuring a slight taper or conical shape at the top.
def model_146317_26f65f2a_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.0053096491, perimeter: 10.0530964915
            with BuildLine():
                CenterArc((0, 0), 0.9, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.7, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=10
        extrude(amount=10)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 10, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.005309725, perimeter: 10.0530965758
            with BuildLine():
                CenterArc((0, 0), 0.9000000134, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.7, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.7539822135, perimeter: 7.5398224154
            with BuildLine():
                CenterArc((0, 0), 0.7, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5000000075, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 10.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6672742562, perimeter: 7.4141587093
            with BuildLine():
                CenterArc((0, 0), 0.68, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5000000075, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


# Description: This is a phone stand or docking station featuring a cylindrical vertical support column mounted on a wide, flat trapezoidal base with a curved slot cutout for device placement.
def model_146317_3eafabf0_0000():
    """Model: bottom_mount v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 31 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 40.2876110196, perimeter: 41.9911485751
            with BuildLine():
                CenterArc((-2.5, 2.5), 1, 90, 90)
                Line((-3.5, -2.5), (-3.5, 2.5))
                CenterArc((-2.5, -2.5), 1, 180, 90)
                Line((2.5, -3.5), (-2.5, -3.5))
                CenterArc((2.5, -2.5), 1, -90, 90)
                Line((3.5, 2.5), (3.5, -2.5))
                CenterArc((2.5, 2.5), 1, 0, 90)
                Line((-2.5, 3.5), (2.5, 3.5))
            make_face()
            with BuildLine():
                CenterArc((-2.5, 2.5), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.5, 2.5), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-2.5, -2.5), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.5, -2.5), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.2725660089, perimeter: 21.3628300444
            with BuildLine():
                CenterArc((0, 0), 1.9, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=5
        extrude(amount=5, mode=Mode.ADD)

        # Sketch4 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 13 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.1706757228, perimeter: 20.9108056758
            with BuildLine():
                CenterArc((0, 0), 1.7, 6.7563271317, 166.5338360605)
                Line((-1.6883560273, 0.1986301209), (-1.889588864, 0.1986301209))
                CenterArc((0, 0), 1.9, 173.9992104004, 6.0007895996)
                CenterArc((0, 0), 1.9, -180, 6.0423285094)
                Line((-1.6881943013, -0.200000003), (-1.8894443625, -0.200000003))
                CenterArc((0, 0), 1.7, -173.2436728683, 166.4873457365)
                Line((1.6881943013, -0.200000003), (1.8894443625, -0.200000003))
                CenterArc((0, 0), 1.9, -6.0423285094, 12.0846570189)
                Line((1.6881943013, 0.200000003), (1.8894443625, 0.200000003))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)
    return part.part


# Description: This is a dark plastic or composite bracket with an elongated hexagonal body, featuring internal ribbing for structural reinforcement, angled flanges on one end, and various mounting holes and slots for assembly purposes.
def model_146317_3eafabf0_0008():
    """Model: leds_chassis v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 18 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.4667655629, perimeter: 31.1297074182
            with BuildLine():
                CenterArc((-1.3, 2.3), 0.2, 90, 90)
                Line((-1.5, -2.3), (-1.5, 2.3))
                CenterArc((-1.3, -2.3), 0.2, 180, 90)
                Line((1.3, -2.5), (-1.3, -2.5))
                CenterArc((1.3, -2.3), 0.2, -90, 90)
                Line((1.5, 2.3), (1.5, -2.3))
                CenterArc((1.3, 2.3), 0.2, 0, 90)
                Line((-1.3, 2.5), (1.3, 2.5))
            make_face()
            with BuildLine():
                CenterArc((-1.1, 2.1), 0.145, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.1, 2.1), 0.145, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.1, -2.1), 0.145, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.1, -2.1), 0.145, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-0.5343145329, 2.1), (0.5343145329, 2.1))
                CenterArc((1.1, 2.1), 0.5656854671, 180, 90)
                Line((1.1, 1.5343145329), (1.1, -1.5343145329))
                CenterArc((1.1, -2.1), 0.5656854671, 90, 90)
                Line((0.5343145329, -2.1), (-0.5343145329, -2.1))
                CenterArc((-1.1, -2.1), 0.5656854671, 0, 90)
                Line((-1.1, -1.5343145329), (-1.1, 1.5343145329))
                CenterArc((-1.1, 2.1), 0.5656854671, -90, 90)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 25.0343362939, perimeter: 43.6566370614
            with BuildLine():
                Line((2, -5), (-2, -5))
                Line((2, 5), (2, -5))
                Line((-2, 5), (2, 5))
                Line((-2, -5), (-2, 5))
            make_face()
            with BuildLine():
                CenterArc((-1.3, -2.3), 0.2, 180, 90)
                Line((-1.5, 2.3), (-1.5, -2.3))
                CenterArc((-1.3, 2.3), 0.2, 90, 90)
                Line((1.3, 2.5), (-1.3, 2.5))
                CenterArc((1.3, 2.3), 0.2, 0, 90)
                Line((1.5, -2.3), (1.5, 2.3))
                CenterArc((1.3, -2.3), 0.2, -90, 90)
                Line((-1.3, -2.5), (1.3, -2.5))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 6.4667655629, perimeter: 31.1297074182
            with BuildLine():
                Line((-1.3, -2.5), (1.3, -2.5))
                CenterArc((1.3, -2.3), 0.2, -90, 90)
                Line((1.5, -2.3), (1.5, 2.3))
                CenterArc((1.3, 2.3), 0.2, 0, 90)
                Line((1.3, 2.5), (-1.3, 2.5))
                CenterArc((-1.3, 2.3), 0.2, 90, 90)
                Line((-1.5, 2.3), (-1.5, -2.3))
                CenterArc((-1.3, -2.3), 0.2, 180, 90)
            make_face()
            with BuildLine():
                CenterArc((1.1, -2.1), 0.145, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.1, 2.1), 0.145, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.1, 2.1), 0.145, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.1, -2.1), 0.145, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((1.1, 1.5343145329), (1.1, -1.5343145329))
                CenterArc((1.1, -2.1), 0.5656854671, 90, 90)
                Line((0.5343145329, -2.1), (-0.5343145329, -2.1))
                CenterArc((-1.1, -2.1), 0.5656854671, 0, 90)
                Line((-1.1, -1.5343145329), (-1.1, 1.5343145329))
                CenterArc((-1.1, 2.1), 0.5656854671, -90, 90)
                Line((-0.5343145329, 2.1), (0.5343145329, 2.1))
                CenterArc((1.1, 2.1), 0.5656854671, 180, 90)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 13 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.5611902212, perimeter: 56.3858401318
            with BuildLine():
                Line((-2, 5), (-2, -5))
                Line((-2, -5), (2, -5))
                Line((2, -5), (2, 5))
                Line((2, 5), (-2, 5))
            make_face()
            with BuildLine():
                CenterArc((1.7, -4.7), 0.5, 90, 90)
                Line((-1.2, -4.7), (1.2, -4.7))
                CenterArc((-1.7, -4.7), 0.5, 0, 90)
                Line((-1.7, 4.2), (-1.7, -4.2))
                CenterArc((-1.7, 4.7), 0.5, -90, 90)
                Line((1.2, 4.7), (-1.2, 4.7))
                CenterArc((1.7, 4.7), 0.5, 180, 90)
                Line((1.7, -4.2), (1.7, 4.2))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.7, -4.7), 0.145, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.7, -4.7), 0.145, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.7, 4.7), 0.145, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.7, 4.7), 0.145, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2, mode=Mode.ADD)
    return part.part


# Description: This is a side marker light or turn signal lens with an elongated, swept-back triangular shape featuring a blue translucent panel, black trim frame, and internal ribbed light-directing structures.
def model_146317_5c5baff8_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 90.4542697574, perimeter: 40.9681408993
            with BuildLine():
                Line((-4.3000000224, 11.8500000991), (-4.3000000224, 1.4500000991))
                CenterArc((-3.5000000224, 1.4500000991), 0.8, -180, 90)
                Line((-3.5000000224, 0.6500000991), (2.4999999776, 0.6500000991))
                CenterArc((2.4999999776, 1.4500000991), 0.8, -90, 90)
                Line((3.2999999776, 1.4500000991), (3.2999999776, 11.8500000991))
                CenterArc((2.4999999776, 11.8500000991), 0.8, 0, 90)
                Line((2.4999999776, 12.6500000991), (-3.5000000224, 12.6500000991))
                CenterArc((-3.5000000224, 11.8500000991), 0.8, 90, 90)
            make_face()
            with BuildLine():
                CenterArc((-3.7499999925, 1.2000000991), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.7499999776, 1.2000000991), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.7499999776, 12.1000000991), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-3.7499999925, 12.1000000991), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2336559536, perimeter: 2.6703537556
            with BuildLine():
                CenterArc((3.7499999925, -1.2000000991), 0.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((3.7499999925, -1.2000000991), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2336559536, perimeter: 2.6703537556
            with BuildLine():
                CenterArc((-2.7499999776, -1.2000000991), 0.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-2.7499999776, -1.2000000991), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2336559536, perimeter: 2.6703537556
            with BuildLine():
                CenterArc((-2.7499999776, -12.1000000991), 0.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-2.7499999776, -12.1000000991), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2336559536, perimeter: 2.6703537556
            with BuildLine():
                CenterArc((3.7499999925, -12.1000000991), 0.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((3.7499999925, -12.1000000991), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.9414159265, perimeter: 13.4283185307
            with BuildLine():
                CenterArc((-2.4000000373, -4.6000001639), 0.1, 90, 90)
                Line((-2.5000000373, -4.6000001639), (-2.5000000373, -10.9000001639))
                CenterArc((-2.4000000373, -10.9000001639), 0.1, 180, 90)
                Line((-2.4000000373, -11.0000001639), (-2.3000000373, -11.0000001639))
                CenterArc((-2.3000000373, -10.9000001639), 0.1, -90, 90)
                Line((-2.2000000373, -10.9000001639), (-2.2000000373, -4.6000001639))
                CenterArc((-2.3000000373, -4.6000001639), 0.1, 0, 90)
                Line((-2.3000000373, -4.5000001639), (-2.4000000373, -4.5000001639))
            make_face()
            # Profile area: 1.9414159265, perimeter: 13.4283185307
            with BuildLine():
                CenterArc((-1.8000000373, -4.6000001639), 0.1, 90, 90)
                Line((-1.9000000373, -4.6000001639), (-1.9000000373, -10.9000001639))
                CenterArc((-1.8000000373, -10.9000001639), 0.1, 180, 90)
                Line((-1.8000000373, -11.0000001639), (-1.7000000373, -11.0000001639))
                CenterArc((-1.7000000373, -10.9000001639), 0.1, -90, 90)
                Line((-1.6000000373, -10.9000001639), (-1.6000000373, -4.6000001639))
                CenterArc((-1.7000000373, -4.6000001639), 0.1, 0, 90)
                Line((-1.7000000373, -4.5000001639), (-1.8000000373, -4.5000001639))
            make_face()
            # Profile area: 1.9414159265, perimeter: 13.4283185307
            with BuildLine():
                CenterArc((-1.2000000373, -4.6000001639), 0.1, 90, 90)
                Line((-1.3000000373, -4.6000001639), (-1.3000000373, -10.9000001639))
                CenterArc((-1.2000000373, -10.9000001639), 0.1, 180, 90)
                Line((-1.2000000373, -11.0000001639), (-1.1000000373, -11.0000001639))
                CenterArc((-1.1000000373, -10.9000001639), 0.1, -90, 90)
                Line((-1.0000000373, -10.9000001639), (-1.0000000373, -4.6000001639))
                CenterArc((-1.1000000373, -4.6000001639), 0.1, 0, 90)
                Line((-1.1000000373, -4.5000001639), (-1.2000000373, -4.5000001639))
            make_face()
            # Profile area: 1.9414159265, perimeter: 13.4283185307
            with BuildLine():
                CenterArc((-0.6000000373, -4.6000001639), 0.1, 90, 90)
                Line((-0.7000000373, -4.6000001639), (-0.7000000373, -10.9000001639))
                CenterArc((-0.6000000373, -10.9000001639), 0.1, 180, 90)
                Line((-0.6000000373, -11.0000001639), (-0.5000000373, -11.0000001639))
                CenterArc((-0.5000000373, -10.9000001639), 0.1, -90, 90)
                Line((-0.4000000373, -10.9000001639), (-0.4000000373, -4.6000001639))
                CenterArc((-0.5000000373, -4.6000001639), 0.1, 0, 90)
                Line((-0.5000000373, -4.5000001639), (-0.6000000373, -4.5000001639))
            make_face()
            # Profile area: 1.9414159265, perimeter: 13.4283185307
            with BuildLine():
                CenterArc((-0.0000000373, -4.6000001639), 0.1, 90, 90)
                Line((-0.1000000373, -4.6000001639), (-0.1000000373, -10.9000001639))
                CenterArc((-0.0000000373, -10.9000001639), 0.1, 180, 90)
                Line((-0.0000000373, -11.0000001639), (0.0999999627, -11.0000001639))
                CenterArc((0.0999999627, -10.9000001639), 0.1, -90, 90)
                Line((0.1999999627, -10.9000001639), (0.1999999627, -4.6000001639))
                CenterArc((0.0999999627, -4.6000001639), 0.1, 0, 90)
                Line((0.0999999627, -4.5000001639), (-0.0000000373, -4.5000001639))
            make_face()
            # Profile area: 1.9414159265, perimeter: 13.4283185307
            with BuildLine():
                CenterArc((0.5999999627, -4.6000001639), 0.1, 90, 90)
                Line((0.4999999627, -4.6000001639), (0.4999999627, -10.9000001639))
                CenterArc((0.5999999627, -10.9000001639), 0.1, 180, 90)
                Line((0.5999999627, -11.0000001639), (0.6999999627, -11.0000001639))
                CenterArc((0.6999999627, -10.9000001639), 0.1, -90, 90)
                Line((0.7999999627, -10.9000001639), (0.7999999627, -4.6000001639))
                CenterArc((0.6999999627, -4.6000001639), 0.1, 0, 90)
                Line((0.6999999627, -4.5000001639), (0.5999999627, -4.5000001639))
            make_face()
        # OneSide extrude, distance=-1.8
        extrude(amount=-1.8, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a phone or tablet stand with a cylindrical vertical support mounted on a wide, flat rectangular base, featuring an angled slot or channel on the base for inserting and holding devices at a viewing angle.
def model_146317_7de88751_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 31 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 40.2876110196, perimeter: 41.9911485751
            with BuildLine():
                CenterArc((-2.5, 2.5), 1, 90, 90)
                Line((-3.5, -2.5), (-3.5, 2.5))
                CenterArc((-2.5, -2.5), 1, 180, 90)
                Line((2.5, -3.5), (-2.5, -3.5))
                CenterArc((2.5, -2.5), 1, -90, 90)
                Line((3.5, 2.5), (3.5, -2.5))
                CenterArc((2.5, 2.5), 1, 0, 90)
                Line((-2.5, 3.5), (2.5, 3.5))
            make_face()
            with BuildLine():
                CenterArc((-2.5, 2.5), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.5, 2.5), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-2.5, -2.5), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.5, -2.5), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.2725660089, perimeter: 21.3628300444
            with BuildLine():
                CenterArc((0, 0), 1.9, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=5
        extrude(amount=5, mode=Mode.ADD)

        # Sketch4 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 13 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.1706757228, perimeter: 20.9108056758
            with BuildLine():
                CenterArc((0, 0), 1.7, 6.7563271317, 166.5338360605)
                Line((-1.6883560273, 0.1986301209), (-1.889588864, 0.1986301209))
                CenterArc((0, 0), 1.9, 173.9992104004, 6.0007895996)
                CenterArc((0, 0), 1.9, -180, 6.0423285094)
                Line((-1.6881943013, -0.200000003), (-1.8894443625, -0.200000003))
                CenterArc((0, 0), 1.7, -173.2436728683, 166.4873457365)
                Line((1.6881943013, -0.200000003), (1.8894443625, -0.200000003))
                CenterArc((0, 0), 1.9, -6.0423285094, 12.0846570189)
                Line((1.6881943013, 0.200000003), (1.8894443625, 0.200000003))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch4 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 13 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.1706757228, perimeter: 20.9108056758
            with BuildLine():
                CenterArc((0, 0), 1.7, 6.7563271317, 166.5338360605)
                Line((-1.6883560273, 0.1986301209), (-1.889588864, 0.1986301209))
                CenterArc((0, 0), 1.9, 173.9992104004, 6.0007895996)
                CenterArc((0, 0), 1.9, -180, 6.0423285094)
                Line((-1.6881943013, -0.200000003), (-1.8894443625, -0.200000003))
                CenterArc((0, 0), 1.7, -173.2436728683, 166.4873457365)
                Line((1.6881943013, -0.200000003), (1.8894443625, -0.200000003))
                CenterArc((0, 0), 1.9, -6.0423285094, 12.0846570189)
                Line((1.6881943013, 0.200000003), (1.8894443625, 0.200000003))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)
    return part.part


# Description: This is a mushroom-shaped fan guard or protective mesh cover featuring a large circular mesh screen with a cylindrical mounting post, designed to safely enclose a fan while allowing airflow through the perforated surface.
def model_146545_f266050f_0002():
    """Model: Wheel"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 78.5398163397, perimeter: 31.4159265359
            Circle(5)
        # Symmetric extrude, full_length=True, total=0.5
        extrude(amount=0.25, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.25, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -0.25, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with Locations((0, 3.5)):
                Circle(0.75)
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)
    return part.part


# Description: This is a reinforced polymeric belt or band featuring an elliptical/oval loop shape with a solid central body and mesh or lattice reinforcement pattern on the outer surfaces for structural support and flexibility.
def model_146617_2c247f85_0017():
    """Model: Шина"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 113.0973355292, perimeter: 37.6991118431
            with Locations((12, 15)):
                Circle(6)
        # OneSide extrude, distance=2.3
        extrude(amount=2.3)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((-12, -15)):
                Circle(0.4)
        # OneSide extrude, distance=-7
        extrude(amount=-7, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 63.1145964106, perimeter: 30.7876080052
            with BuildLine():
                CenterArc((-12, -15), 4.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-12, -15), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-9
        extrude(amount=-9, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical bolt or machine screw with a hexagonal head at the top and a threaded shaft below, designed for fastening applications.
def model_146617_2c247f85_0023():
    """Model: болт"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((19, 13)):
                Circle(0.4)
        # OneSide extrude, distance=3.3
        extrude(amount=3.3)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.8246680716, perimeter: 6.5973445725
            with BuildLine():
                CenterArc((-19, -13), 0.65, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-19, -13), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((-19, -13)):
                Circle(0.4)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3.6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1062009936, perimeter: 1.2130804315
            with BuildLine():
                Line((-19.1750930784, -13.101090036), (-19, -13.2021800719))
                Line((-19, -13.2021800719), (-18.8249069216, -13.101090036))
                Line((-18.8249069216, -13.101090036), (-18.8249069216, -12.898909964))
                Line((-18.8249069216, -12.898909964), (-19, -12.7978199281))
                Line((-19, -12.7978199281), (-19.1750930784, -12.898909964))
                Line((-19.1750930784, -12.898909964), (-19.1750930784, -13.101090036))
            make_face()
        # OneSide extrude, distance=-0.25
        extrude(amount=-0.25, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical sleeve or barrel with two protruding circular flanges or ears on opposite sides, featuring vertical ribbing or fluting on its outer surface for structural reinforcement.
def model_146868_52dcd6c2_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.5873061113, perimeter: 40.9977841293
            with BuildLine():
                CenterArc((0, 0), 3.35, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=5.1
        extrude(amount=5.1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.5271007062, perimeter: 45.5530934771
            with BuildLine():
                CenterArc((0, 0), 3.9, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3.35, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.35
        extrude(amount=0.35, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.478058657, perimeter: 43.9885803356
            with BuildLine():
                CenterArc((0, 0), 3.6705, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3.3305, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-5.1
        extrude(amount=-5.1, mode=Mode.ADD)
    return part.part


# Description: This is a rectangular duct or channel component with a elongated, rounded rectangular profile, featuring an open top with internal ribbing or structural reinforcement visible through the opening.
def model_147133_92c04b84_0006():
    """Model: Соединение"""
    with BuildPart() as part:
        # Sketch3 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.4506192983, perimeter: 16.8265482457
            with BuildLine():
                CenterArc((-2.95, 0), 0.8, 90, 180)
                Line((-2.95, -0.8), (2.95, -0.8))
                CenterArc((2.95, 0), 0.8, -90, 180)
                Line((2.95, 0.8), (-2.95, 0.8))
            make_face()
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)

        # Sketch4 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7461282552, perimeter: 5.9690260418
            with BuildLine():
                CenterArc((-2.84, 0), 0.6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-2.84, 0), 0.35, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            with Locations((-2.84, 0)):
                Circle(0.35)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)

        # Sketch1 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.8186724714, perimeter: 3.9002993481
            with BuildLine():
                Line((-2.2705780138, -0.4473570104), (-1.25, -0.4473570104))
                Line((-1.25, -0.4473570104), (-1.25, 0.4473570104))
                Line((-1.25, 0.4473570104), (-2.2705780138, 0.4473570104))
                CenterArc((-2.84, 0), 0.7241337536, -38.1543659767, 76.3087319535)
            make_face()
            # Profile area: 1.6999566397, perimeter: 5.5894280418
            with BuildLine():
                Line((-0.95, -0.4473570104), (-0.95, 0.4473570104))
                Line((-0.95, -0.4473570104), (0.95, -0.4473570104))
                Line((0.95, -0.4473570104), (0.95, 0.4473570104))
                Line((0.95, 0.4473570104), (-0.95, 0.4473570104))
            make_face()
            # Profile area: 0.8186724714, perimeter: 3.9002993481
            with BuildLine():
                Line((1.25, -0.4473570104), (1.25, 0.4473570104))
                Line((1.25, -0.4473570104), (2.2705780138, -0.4473570104))
                CenterArc((2.84, 0), 0.7241337536, 141.8456340233, 76.3087319535)
                Line((2.2705780138, 0.4473570104), (1.25, 0.4473570104))
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a bracket or clamp assembly with a rectangular box-shaped upper section, a curved lower section, and internal structural ribs, designed to mount or secure components together.
def model_147428_1502e954_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 13 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.7907070889, perimeter: 7.0916124086
            with BuildLine():
                CenterArc((-1.7261755799, -1.1000000164), 0.6738244559, 180, 180)
                Line((-1.052351124, -1.1000000164), (-0.8000000119, -0.400000006))
                Line((-0.8000000119, -0.400000006), (-1.3000000194, -0.400000006))
                Line((-1.3000000194, -0.400000006), (-1.5500000231, -0.1500000022))
                Line((-1.5500000231, -0.1500000022), (-2.4000000358, -0.1500000022))
                Line((-2.4000000358, -1.1000000164), (-2.4000000358, -0.1500000022))
            make_face()
            with BuildLine():
                CenterArc((-1.6189215503, -0.9418177447), 0.251, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.29
        extrude(amount=0.29)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 13 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.61492111, perimeter: 12.9148830151
            with BuildLine():
                Line((-0.3000000045, 0.1000000015), (-0.8000000119, -0.400000006))
                Line((0.7000000104, 0.1000000015), (-0.3000000045, 0.1000000015))
                Line((0.7000000104, 0), (0.7000000104, 0.1000000015))
                Line((1.7000000253, 0), (0.7000000104, 0))
                Line((1.7000000253, 1.4000000209), (1.7000000253, 0))
                Line((1.1000000164, 1.4000000209), (1.7000000253, 1.4000000209))
                Line((0.7000000104, 1.0464499412), (1.1000000164, 1.4000000209))
                Line((-2.0325673506, 1.0464499412), (0.7000000104, 1.0464499412))
                Line((-2.4000000358, 0.6510355864), (-2.0325673506, 1.0464499412))
                Line((-2.4000000358, -0.1500000022), (-2.4000000358, 0.6510355864))
                Line((-1.5500000231, -0.1500000022), (-2.4000000358, -0.1500000022))
                Line((-1.3000000194, -0.400000006), (-1.5500000231, -0.1500000022))
                Line((-0.8000000119, -0.400000006), (-1.3000000194, -0.400000006))
            make_face()
            with BuildLine():
                CenterArc((-1.9199999571, 0.4799999893), 0.286, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.045
        extrude(amount=1.045, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 13 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1909177272, perimeter: 2.7080528674
            with BuildLine():
                CenterArc((-1.9199999571, 0.4799999893), 0.286, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-1.9199999571, 0.4799999893), 0.145, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.9
        extrude(amount=0.9, mode=Mode.ADD)
    return part.part


# Description: This is a tilted cylindrical duct or air intake component with a large circular opening at the top, a rectangular base flange for mounting, and angled support fins or braces extending from the lower section.
def model_20442_00c8a1db_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.1681145876, perimeter: 8.8040225976
            Circle(1.4012037155)
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 10.6718887779, perimeter: 12.1603465661
            with BuildLine():
                Line((2.021269795, 0.1485944877), (0.8819482963, 1.8247682342))
                Line((0.8819482963, 1.8247682342), (-1.1393214987, 1.6761737465))
                Line((-1.1393214987, 1.6761737465), (-2.021269795, -0.1485944877))
                Line((-2.021269795, -0.1485944877), (-0.8819482963, -1.8247682342))
                Line((-0.8819482963, -1.8247682342), (1.1393214987, -1.6761737465))
                Line((1.1393214987, -1.6761737465), (2.021269795, 0.1485944877))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.31438413, perimeter: 12.5210504893
            with BuildLine():
                Line((0.9201876973, 1.8730090987), (-1.1619796124, 1.7334104715))
                Line((-1.1619796124, 1.7334104715), (-2.0821673097, -0.1395986272))
                Line((-2.0821673097, -0.1395986272), (-0.9201876973, -1.8730090987))
                Line((-0.9201876973, -1.8730090987), (1.1619796124, -1.7334104715))
                Line((1.1619796124, -1.7334104715), (2.0821673097, 0.1395986272))
                Line((2.0821673097, 0.1395986272), (0.9201876973, 1.8730090987))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)
    return part.part


# Description: This is a tapered wedge or ramp component with an elongated rectangular base that gradually slopes upward, featuring a triangulated surface structure with multiple planar facets and internal ribbing or support geometry.
def model_21234_8b71bd47_0000():
    """Model: 5 Hinge Base v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 98.28609375, perimeter: 40.3225
            with BuildLine():
                Line((0, 11.90625), (0, 0))
                Line((0, 0), (8.255, 0))
                Line((8.255, 0), (8.255, 11.90625))
                Line((8.255, 11.90625), (0, 11.90625))
            make_face()
        # OneSide extrude, distance=1.905
        extrude(amount=1.905)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.905, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 83.8708, perimeter: 36.83
            with BuildLine():
                Line((0, 0), (-8.255, 0))
                Line((-8.255, 0), (-8.255, -10.16))
                Line((-8.255, -10.16), (0, -10.16))
                Line((0, -10.16), (0, 0))
            make_face()
        # OneSide extrude, distance=-0.3175
        extrude(amount=-0.3175, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 10.48385, perimeter: 19.05
            with BuildLine():
                Line((0, -7.46125), (8.255, -7.46125))
                Line((0, -8.73125), (0, -7.46125))
                Line((8.255, -8.73125), (0, -8.73125))
                Line((8.255, -7.46125), (8.255, -8.73125))
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635, mode=Mode.ADD)
    return part.part


# Description: This is a long, narrow structural beam or rail with a tapered profile, featuring two angled end caps and a central slot or channel running along its length.
def model_21235_01764fc7_0014():
    """Model: 1-BASE v9 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 11 constraints, 13 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 111.4414272764, perimeter: 91.4793325614
            with BuildLine():
                Line((-3.7948305624, 1.905), (-3.7948305624, 1.74625))
                Line((-3.7948305624, 1.905), (-6.9698305624, 1.905))
                Line((-5.3975, 3.65125), (-6.9698305624, 1.905))
                Line((-9.5098305624, 3.65125), (-5.3975, 3.65125))
                Line((-19.6698305624, 2.54), (-9.5098305624, 3.65125))
                Line((-19.6698305624, 0), (-19.6698305624, 2.54))
                Line((-19.6698305624, 0), (20.9701694376, 0))
                Line((20.9701694376, 0), (20.9701694376, 2.54))
                Line((10.8101694376, 3.6168992582), (20.9701694376, 2.54))
                Line((8.5415694294, 3.6168992582), (10.8101694376, 3.6168992582))
                Line((8.5415694294, 3.6168992582), (7.0001694376, 1.905))
                Line((7.0001694376, 1.905), (2.5551694376, 1.905))
                Line((2.5551694376, 1.74625), (2.5551694376, 1.905))
                Line((-3.7948305624, 1.74625), (2.5551694376, 1.74625))
            make_face()
        # Symmetric extrude, each_side=3.81
        extrude(amount=3.81, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 19.6698305624), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 6.64595445, perimeter: 12.7
            with BuildLine():
                Line((-1.26238, 0), (-1.26238, -0.9525))
                Line((-1.26238, -0.9525), (-2.2225, -0.9525))
                Line((-2.2225, -0.9525), (-2.2225, -1.905))
                Line((-2.2225, -1.905), (2.2225, -1.905))
                Line((2.2225, -0.9525), (2.2225, -1.905))
                Line((1.27, -0.9525), (2.2225, -0.9525))
                Line((1.27, 0), (1.27, -0.9525))
                Line((-1.26238, 0), (1.27, 0))
            make_face()
        # OneSide extrude, distance=-38.1
        extrude(amount=-38.1, mode=Mode.ADD)
    return part.part


# Description: This is a tetrahedral or pyramid-shaped structural bracket featuring two triangular faces meeting at sharp edges with a rectangular flanged base, designed for rigid support or mounting applications.
def model_21235_01764fc7_0029():
    """Model: 4-RIGHT JAW v3 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 61.9364639673, perimeter: 41.2059759322
            with BuildLine():
                Line((4.445, 9.525), (-0.2052467985, 4.8747532015))
                Line((-4.445, 9.525), (4.445, 9.525))
                Line((-4.445, 0), (-4.445, 9.525))
                Line((4.445, 0), (-4.445, 0))
                Line((-0.2052467985, 4.6502467985), (4.445, 0))
                CenterArc((-0.3175, 4.7625), 0.15875, 45, 270)
            make_face()
        # Symmetric extrude, each_side=0.47625
        extrude(amount=0.47625, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 4.445), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 7.56046875, perimeter: 20.6375
            with BuildLine():
                Line((1.27, 0), (1.27, 9.525))
                Line((1.27, 9.525), (0.47625, 9.525))
                Line((0.47625, 0), (0.47625, 9.525))
                Line((0.47625, 0), (1.27, 0))
            make_face()
            # Profile area: 9.0725625, perimeter: 20.955
            with BuildLine():
                Line((0.47625, 0), (0.47625, 9.525))
                Line((-0.47625, 9.525), (0.47625, 9.525))
                Line((-0.47625, 9.525), (-0.47625, 0))
                Line((0.47625, 0), (-0.47625, 0))
            make_face()
            # Profile area: 7.56046875, perimeter: 20.6375
            with BuildLine():
                Line((-0.47625, 9.525), (-0.47625, 0))
                Line((-1.27, 9.525), (-0.47625, 9.525))
                Line((-1.27, 0), (-1.27, 9.525))
                Line((-0.47625, 0), (-1.27, 0))
            make_face()
        # OneSide extrude, distance=1.27
        extrude(amount=1.27, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical fastener or spacer with a flanged head at the top, featuring a hollow tubular body and a wider, textured cap or collar at the upper end.
def model_21236_b696e901_0041():
    """Model: Basic Screw v2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.061575216, perimeter: 0.879645943
            Circle(0.14)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0640884901, perimeter: 2.1362830044
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.14, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.061575216, perimeter: 0.879645943
            Circle(0.14)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 14 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.9, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0100000003, perimeter: 0.400000006
            with BuildLine():
                Line((-0.0500000007, 0.0500000007), (-0.0500000007, 0.1500000022))
                Line((-0.0500000007, 0.0500000007), (0.0500000007, 0.0500000007))
                Line((0.0500000007, 0.1500000022), (0.0500000007, 0.0500000007))
                Line((-0.0500000007, 0.1500000022), (0.0500000007, 0.1500000022))
            make_face()
            # Profile area: 0.0100000003, perimeter: 0.400000006
            with BuildLine():
                Line((-0.1500000022, 0.0500000007), (-0.0500000007, 0.0500000007))
                Line((-0.1500000022, -0.0500000007), (-0.1500000022, 0.0500000007))
                Line((-0.0500000007, -0.0500000007), (-0.1500000022, -0.0500000007))
                Line((-0.0500000007, -0.0500000007), (-0.0500000007, 0.0500000007))
            make_face()
            # Profile area: 0.0100000003, perimeter: 0.400000006
            with BuildLine():
                Line((0.0500000007, 0.0500000007), (0.0500000007, -0.0500000007))
                Line((0.1500000022, -0.0500000007), (0.0500000007, -0.0500000007))
                Line((0.1500000022, 0.0500000007), (0.1500000022, -0.0500000007))
                Line((0.0500000007, 0.0500000007), (0.1500000022, 0.0500000007))
            make_face()
            # Profile area: 0.0100000003, perimeter: 0.400000006
            with BuildLine():
                Line((-0.0500000007, -0.0500000007), (-0.0500000007, 0.0500000007))
                Line((0.0500000007, -0.0500000007), (-0.0500000007, -0.0500000007))
                Line((0.0500000007, 0.0500000007), (0.0500000007, -0.0500000007))
                Line((-0.0500000007, 0.0500000007), (0.0500000007, 0.0500000007))
            make_face()
            # Profile area: 0.0100000003, perimeter: 0.400000006
            with BuildLine():
                Line((0.0500000007, -0.0500000007), (-0.0500000007, -0.0500000007))
                Line((-0.0500000007, -0.1500000022), (-0.0500000007, -0.0500000007))
                Line((0.0500000007, -0.1500000022), (-0.0500000007, -0.1500000022))
                Line((0.0500000007, -0.0500000007), (0.0500000007, -0.1500000022))
            make_face()
        # OneSide extrude, distance=-0.075
        extrude(amount=-0.075, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a suppressor or silencer featuring a cylindrical tube with a tapered front end, internal baffles (visible through the mesh texture), and a mounting hole at the rear.
def model_21237_7887a24b_0011():
    """Model: Line Guide Shaft Housing v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.138544236, perimeter: 4.6181412008
            with BuildLine():
                CenterArc((0, 0), 0.3975, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3375, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3.825
        extrude(amount=3.825)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.2567871794, perimeter: 6.8142974356
            with BuildLine():
                CenterArc((-3.275, 0), 0.25, 53.1301023542, 253.7397952917)
                Line((-3.125, -0.2), (-0.825, -0.2))
                CenterArc((-0.675, 0), 0.25, -126.8698976458, 253.7397952917)
                Line((-3.125, 0.2), (-0.825, 0.2))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 21 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0443957307, perimeter: 1.5998576914
            with BuildLine():
                Line((0.2609097114, 0.2140849656), (0.3072936601, 0.252144515))
                CenterArc((0, 0), 0.3975, 39.37, 115.36)
                Line((-0.305203339, 0.1440734946), (-0.3594617104, 0.1696865603))
                CenterArc((0, 0), 0.3375, 39.37, 115.36)
            make_face()
        # OneSide extrude, distance=-0.225
        extrude(amount=-0.225, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 21 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0443540199, perimeter: 1.5981021555
            with BuildLine():
                Line((-0.2609097114, -0.2140849656), (-0.3072936601, -0.252144515))
                CenterArc((0, 0), 0.3975, -140.63, 115.1026170669)
                Line((0.3586958236, -0.1712996093), (0.3172153126, -0.1497438355))
                Line((0.305203339, -0.1440734946), (0.3172153126, -0.1497438355))
                CenterArc((0, 0), 0.3375, -140.63, 115.36)
            make_face()
        # OneSide extrude, distance=-0.225
        extrude(amount=-0.225, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a satellite or spacecraft component featuring a central cubic body with extended solar panels or antenna arrays on opposing sides, characterized by a skeletal frame structure with triangulated support struts and geometric panel sections.
def model_21242_6c2af7c2_0005():
    """Model: 22 ESCAPEMENT v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 24 constraints, 21 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 7.9242388636, perimeter: 26.2969915998
            with BuildLine():
                Line((-3.3351898673, 0.0202492846), (-3.429455891, 0.2680154691))
                Line((-4.5510234286, -0.1587001956), (-3.429455891, 0.2680154691))
                Line((-4.1954270413, -1.0933398103), (-4.5510234286, -0.1587001956))
                Line((-4.1954270413, -1.0933398103), (-3.0738595037, -0.6666241456))
                Line((-3.0738595037, -0.6666241456), (-3.1499522312, -0.4666241456))
                Line((-3.1499522312, -0.4666241456), (-0.5, -0.1993043382))
                Line((-0.5, -0.1993043382), (-0.5, -0.5993043382))
                Line((-0.5, -0.5993043382), (0.5, -0.5993043382))
                Line((0.5, -0.5993043382), (0.5, -0.1993043382))
                Line((0.5, -0.1993043382), (3.1349491055, -0.4005696738))
                Line((3.0467385951, -0.6005696738), (3.1349491055, -0.4005696738))
                Line((3.0467385951, -0.6005696738), (4.1446901965, -1.0848240294))
                Line((4.1446901965, -1.0848240294), (4.5482354929, -0.1698643616))
                Line((3.4502838915, 0.314389994), (4.5482354929, -0.1698643616))
                Line((3.322255414, 0.0241105773), (3.4502838915, 0.314389994))
                Line((0.5008682023, 0.6331486975), (3.322255414, 0.0241105773))
                CenterArc((0.5516674691, 0.8681062093), 0.2403863513, 102.3720350316, 155.4280454236)
                Line((0.5001626244, 1.1029100611), (0.5001626244, 1.4029100611))
                CenterArc((0.9804508603, 2.0751877838), 0.8262167548, -177.2154325394, 51.6726837922)
                Line((-0.15476156, 2.0350495616), (0.1552096538, 2.0350495616))
                CenterArc((-0.9800027666, 2.0751877838), 0.8262167548, -54.4572512528, 51.6726837922)
                Line((-0.4997145307, 1.1029100611), (-0.4997145307, 1.4029100611))
                CenterArc((-0.5512193753, 0.8681062093), 0.2403863513, -77.8000804552, 155.4280454236)
                Line((-3.3351898673, 0.0202492846), (-0.5004201085, 0.6331486975))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.3739202336, 0.5227266893), x_dir=(1, 0, 0), z_dir=(0, 0.9346396147, 0.3555963873))):
            # Profile area: 0.3107712435, perimeter: 4.4652240611
            with BuildLine():
                Line((0.9, -3.11), (1.2, -3.11))
                Line((1.2, -1.03819171), (1.2, -3.11))
                Line((0.9, -3.11), (1.2, -1.03819171))
            make_face()
            # Profile area: 0.3107712435, perimeter: 4.4652240611
            with BuildLine():
                Line((0, -3.11), (0.3, -3.11))
                Line((0.3, -3.11), (0, -1.03819171))
                Line((0, -3.11), (0, -1.03819171))
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.537132242, -0.6779560979), x_dir=(-1, 0, 0), z_dir=(0, 0.9149596678, -0.4035452964))):
            # Profile area: 0.2988137757, perimeter: 4.306646352
            with BuildLine():
                Line((0, -3.03), (-0.3, -3.03))
                Line((0, -1.0379081622), (0, -3.03))
                Line((-0.3, -3.03), (0, -1.0379081622))
            make_face()
            # Profile area: 0.2988137757, perimeter: 4.306646352
            with BuildLine():
                Line((-0.9, -3.03), (-1.2, -1.0379081622))
                Line((-1.2, -1.0379081622), (-1.2, -3.03))
                Line((-0.9, -3.03), (-1.2, -3.03))
            make_face()
        # OneSide extrude, distance=-1.9
        extrude(amount=-1.9, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a threaded rod assembly consisting of a long cylindrical shaft with a hexagonal nut fixed near the center, creating a compact fastening component with an elongated profile.
def model_21246_c66f2b12_0000():
    """Model: Hex Shaft w/spacer v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4243524479, perimeter: 2.4248711306
            with BuildLine():
                Line((0.2020725942, 0.35), (-0.2020725942, 0.35))
                Line((-0.2020725942, 0.35), (-0.4041451884, 0))
                Line((-0.4041451884, 0), (-0.2020725942, -0.35))
                Line((-0.2020725942, -0.35), (0.2020725942, -0.35))
                Line((0.2020725942, -0.35), (0.4041451884, 0))
                Line((0.4041451884, 0), (0.2020725942, 0.35))
            make_face()
        # Symmetric extrude, each_side=0.25
        extrude(amount=0.25, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.25, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0585433173, perimeter: 0.9006664199
            with BuildLine():
                Line((-0.075055535, -0.13), (0.075055535, -0.13))
                Line((0.075055535, -0.13), (0.15011107, 0))
                Line((0.15011107, 0), (0.075055535, 0.13))
                Line((0.075055535, 0.13), (-0.075055535, 0.13))
                Line((-0.075055535, 0.13), (-0.15011107, 0))
                Line((-0.15011107, 0), (-0.075055535, -0.13))
            make_face()
        # OneSide extrude, distance=3.1
        extrude(amount=3.1, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.25, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0585433173, perimeter: 0.9006664199
            with BuildLine():
                Line((-0.075055535, -0.13), (0.075055535, -0.13))
                Line((0.075055535, -0.13), (0.15011107, 0))
                Line((0.15011107, 0), (0.075055535, 0.13))
                Line((0.075055535, 0.13), (-0.075055535, 0.13))
                Line((-0.075055535, 0.13), (-0.15011107, 0))
                Line((-0.15011107, 0), (-0.075055535, -0.13))
            make_face()
        # OneSide extrude, distance=-1.875
        extrude(amount=-1.875, mode=Mode.ADD)
    return part.part


# Description: This is a bent metal bracket or angle iron featuring a sharp 90-degree bend, with a mounting hole in the upper flange and a tapered or beveled edge on the lower leg.
def model_21246_c66f2b12_0009():
    """Model: Fork v2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.82, perimeter: 14.6
            with BuildLine():
                Line((1.1, 6.2), (1.1, 0))
                Line((0, 6.2), (1.1, 6.2))
                Line((0, 0), (0, 6.2))
                Line((1.1, 0), (0, 0))
            make_face()
        # OneSide extrude, distance=0.08
        extrude(amount=0.08)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.08, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.088, perimeter: 2.36
            with BuildLine():
                Line((-1.1, -6.12), (0, -6.12))
                Line((-1.1, -6.2), (-1.1, -6.12))
                Line((0, -6.2), (-1.1, -6.2))
                Line((0, -6.12), (0, -6.2))
            make_face()
        # OneSide extrude, distance=1.8
        extrude(amount=1.8, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -6.12), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((0.5500000082, 1.38)):
                Circle(0.15)
        # OneSide extrude, distance=-0.08
        extrude(amount=-0.08, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a black plastic bracket or frame component with an angular, triangular profile featuring internal reinforcing ribs, mounting holes at the base, and a open geometric design typical of drone or robotic structural parts.
def model_21338_bd0eb54a_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude5 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 25 constraints, 29 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 19.8447226763, perimeter: 24.5759142707
            with BuildLine():
                Line((2.6866110446, 0.7270057531), (2.6866110446, 1.5270057531))
                Line((2.6866110446, 1.5270057531), (3.972186264, 3.0590946394))
                Line((3.972186264, 3.0590946394), (3.972186264, 3.5590946394))
                Line((3.972186264, 3.5590946394), (2.472186264, 3.5590946394))
                Line((2.472186264, 3.5590946394), (2.472186264, 3.0590946394))
                Line((-2.4876500177, 3.0590946394), (2.472186264, 3.0590946394))
                Line((-2.4876500177, 3.0590946394), (-2.4876500177, 3.5590946394))
                Line((-2.4876500177, 3.5590946394), (-3.98765004, 3.5590946394))
                Line((-3.98765004, 3.5590946394), (-3.98765004, 3.0590946394))
                Line((-2.7020748207, 1.5270057531), (-3.98765004, 3.0590946394))
                Line((-2.7020748207, 0.7270057531), (-2.7020748207, 1.5270057531))
                Line((-3.0016484428, 0.7110168542), (-2.7020748207, 0.7270057531))
                Line((-3.0016484428, 0.2110168542), (-3.0016484428, 0.7110168542))
                Line((-2.506673696, -0.2839578926), (-3.0016484428, 0.2110168542))
                Line((-2.006673696, -0.2839578926), (-2.506673696, -0.2839578926))
                Line((-2.006673696, 0.2160421074), (-2.006673696, -0.2839578926))
                Line((-2.006673696, 0.2160421074), (1.993326304, 0.2160421074))
                Line((1.993326304, 0.2160421074), (1.993326304, -0.2839578926))
                Line((1.993326304, -0.2839578926), (2.493326304, -0.2839578926))
                Line((2.493326304, -0.2839578926), (2.9883010508, 0.2110168542))
                Line((2.9883010508, 0.2110168542), (2.9883010508, 0.7110168542))
                Line((2.9866110446, 0.7270057531), (2.9883010508, 0.7110168542))
                Line((2.9866110446, 0.7270057531), (2.6866110446, 0.7270057531))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch4 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.2, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.7695041723, perimeter: 8.7712812921
            with BuildLine():
                Line((-1.5000000224, 1.8000000268), (1.4999999776, 1.8000000268))
                Line((1.4999999776, 1.8000000268), (1.961880193, 2.6000000268))
                Line((-1.9618802377, 2.6000000268), (1.961880193, 2.6000000268))
                Line((-1.5000000224, 1.8000000268), (-1.9618802377, 2.6000000268))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 45 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.2, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((-3.7044847497, 3.4025892903)):
                Circle(0.1)
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((-3.8000000566, 3.1525892903)):
                Circle(0.1)
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((-3.5044847497, 3.2871192364)):
                Circle(0.1)
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((-3.6000000566, 3.0371192364)):
                Circle(0.1)
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((-3.4000000566, 2.9216491826)):
                Circle(0.1)
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((-3.3044847497, 3.1716491826)):
                Circle(0.1)
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((-3.1044847497, 3.0561791287)):
                Circle(0.1)
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((-3.2000000566, 2.8061791287)):
                Circle(0.1)
            # Profile area: 0.0309058756, perimeter: 0.6256965479
            with BuildLine():
                CenterArc((-2.350000035, 3.1500000469), 0.1, -65.3749573751, 310.7499147503)
                Line((-2.3083322192, 3.0590946394), (-2.3916678508, 3.0590946394))
            make_face()
            # Profile area: 0.0005100509, perimeter: 0.169293246
            with BuildLine():
                Line((-2.3083322192, 3.0590946394), (-2.3916678508, 3.0590946394))
                CenterArc((-2.350000035, 3.1500000469), 0.1, -114.6250426249, 49.2500852497)
            make_face()
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((-2.350000035, 2.9000000432)):
                Circle(0.1)
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((-1.5000000224, 1.5000000224)):
                Circle(0.1)
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((-1.5000000224, 0.5000000075)):
                Circle(0.1)
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((-0.5000000075, 0.7000000104)):
                Circle(0.1)
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((-0.5000000075, 1.3000000194)):
                Circle(0.1)
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((-2.350000035, 2.1000000134)):
                Circle(0.1)
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((-2.350000035, 1.8000000134)):
                Circle(0.1)
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((-2.350000035, 1.5000000134)):
                Circle(0.1)
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((-2.350000035, 1.2000000134)):
                Circle(0.1)
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((-2.350000035, 0.9000000134)):
                Circle(0.1)
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((-2.206673696, -0.0839578926)):
                Circle(0.1)
            # Profile area: 0.0045331175, perimeter: 0.2890936991
            with BuildLine():
                CenterArc((-2.7499999385, 0.5199999884), 0.1, -131.4096221093, 82.8192442185)
                CenterArc((-2.7499999385, 0.3699999884), 0.1, 48.5903778907, 82.8192442185)
            make_face()
            # Profile area: 0.026882809, perimeter: 0.6283185307
            with BuildLine():
                CenterArc((-2.7499999385, 0.3699999884), 0.1, -131.4096612405, 82.8192442185)
                CenterArc((-2.750000041, 0.2199999884), 0.1, 131.409582978, 277.1807557815)
            make_face()
            # Profile area: 0.0045331175, perimeter: 0.2890936991
            with BuildLine():
                CenterArc((-2.750000041, 0.2199999884), 0.1, 48.5903387595, 82.8192442185)
                CenterArc((-2.7499999385, 0.3699999884), 0.1, -131.4096612405, 82.8192442185)
            make_face()
            # Profile area: 0.026882809, perimeter: 0.6283185307
            with BuildLine():
                CenterArc((-2.7499999385, 0.3699999884), 0.1, 48.5903778907, 82.8192442185)
                CenterArc((-2.7499999385, 0.5199999884), 0.1, -48.5903778907, 277.1807557815)
            make_face()
            # Profile area: 0.0223496915, perimeter: 0.6283185307
            with BuildLine():
                CenterArc((-2.7499999385, 0.3699999884), 0.1, 131.4096221093, 97.1807166502)
                CenterArc((-2.750000041, 0.2199999884), 0.1, 48.5903387595, 82.8192442185)
                CenterArc((-2.7499999385, 0.3699999884), 0.1, -48.590417022, 97.1807949128)
                CenterArc((-2.7499999385, 0.5199999884), 0.1, -131.4096221093, 82.8192442185)
            make_face()
            # Profile area: 0.0045331172, perimeter: 0.2890936924
            with BuildLine():
                CenterArc((-2.4500000365, 0.1000000015), 0.1, 48.5903788588, 82.8192422824)
                CenterArc((-2.4500000365, 0.2500000037), 0.1, -131.4096211412, 82.8192422824)
            make_face()
            # Profile area: 0.0268828091, perimeter: 0.6283185302
            with BuildLine():
                CenterArc((-2.4500000365, 0.400000006), 0.1000000015, 48.5903787513, 82.8192424975)
                CenterArc((-2.4500000365, 0.5500000082), 0.1, -48.5903779983, 277.1807559966)
            make_face()
            # Profile area: 0.0223496926, perimeter: 0.628318541
            with BuildLine():
                CenterArc((-2.4500000365, 0.400000006), 0.1000000015, 131.4096212487, 97.1807575025)
                CenterArc((-2.4500000365, 0.2500000037), 0.1, 48.5903779983, 82.8192440034)
                CenterArc((-2.4500000365, 0.400000006), 0.1000000015, -48.5903787513, 97.1807575025)
                CenterArc((-2.4500000365, 0.5500000082), 0.1, -131.4096220017, 82.8192440034)
            make_face()
            # Profile area: 0.0268828093, perimeter: 0.6283185307
            with BuildLine():
                CenterArc((-2.4500000365, 0.2500000037), 0.1, -131.4096211412, 82.8192422824)
                CenterArc((-2.4500000365, 0.1000000015), 0.1, 131.4096211412, 277.1807577176)
            make_face()
            # Profile area: 0.0223496918, perimeter: 0.6283185302
            with BuildLine():
                CenterArc((-2.4500000365, 0.2500000037), 0.1, 131.4096220017, 97.1807568571)
                CenterArc((-2.4500000365, 0.1000000015), 0.1, 48.5903788588, 82.8192422824)
                CenterArc((-2.4500000365, 0.2500000037), 0.1, -48.5903788588, 97.1807568571)
                CenterArc((-2.4500000365, 0.400000006), 0.1000000015, -131.4096212487, 82.8192424975)
            make_face()
            # Profile area: 0.0045331175, perimeter: 0.2890936979
            with BuildLine():
                CenterArc((-2.4500000365, 0.5500000082), 0.1, -131.4096220017, 82.8192440034)
                CenterArc((-2.4500000365, 0.400000006), 0.1000000015, 48.5903787513, 82.8192424975)
            make_face()
            # Profile area: 0.0045331175, perimeter: 0.2890936979
            with BuildLine():
                CenterArc((-2.4500000365, 0.400000006), 0.1000000015, -131.4096212487, 82.8192424975)
                CenterArc((-2.4500000365, 0.2500000037), 0.1, 48.5903779983, 82.8192440034)
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a tie rod or steering component with a hexagonal head on one end and a tapered threaded shaft, featuring a small hole near the head likely for a cotter pin or safety clip.
def model_21385_601444ba_0014():
    """Model: Piston Rod v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3835122956, perimeter: 3.5884599023
            with BuildLine():
                Line((0.3175, 0.23749), (0.3175, -0.23749))
                CenterArc((0, 0.2417394884), 0.3175284368, -0.7668132755, 181.5336265509)
                Line((-0.3175, -0.23749), (-0.3175, 0.23749))
                Line((0.3175, -0.23749), (-0.3175, -0.23749))
            make_face()
            with BuildLine():
                CenterArc((0, 0.2417394884), 0.15875, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.23749), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1248983265, perimeter: 1.2528043184
            with Locations((0, 0.3175)):
                Circle(0.19939)
        # OneSide extrude, distance=5.08
        extrude(amount=5.08, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 5.31749), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0365235258, perimeter: 0.6774718894
            with Locations((0, 0.3175)):
                Circle(0.107823)
        # OneSide extrude, distance=0.79248
        extrude(amount=0.79248, mode=Mode.ADD)
    return part.part


# Description: This is a pyramidal or wedge-shaped connector bracket featuring a pointed top section with a rectangular base, a central horizontal slot or groove running along its length, and beveled or angled side surfaces that create a faceted geometric appearance.
def model_21564_fa5b2db7_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch8 -> Extrude7 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.134885107, perimeter: 2.1971197678
            with BuildLine():
                Line((2.6500000395, -1.1000000164), (2.3502719166, -2.0000993592))
                Line((2.5000000373, -1.1000000164), (2.6500000395, -1.1000000164))
                Line((2.5000000373, -1.1000000164), (2.2005437959, -2.0001986886))
                Line((2.3502719166, -2.0000993592), (2.2005437959, -2.0001986886))
            make_face()
            # Profile area: 0.1650000049, perimeter: 2.5000000373
            with BuildLine():
                Line((2.5000000373, 0), (2.5000000373, -1.1000000164))
                Line((2.5000000373, -1.1000000164), (2.6500000395, -1.1000000164))
                Line((2.6500000395, 0), (2.6500000395, -1.1000000164))
                Line((2.5000000373, 0), (2.6500000395, 0))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch9 -> Extrude8 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.1348702091, perimeter: 2.1971031082
            with BuildLine():
                Line((2.6500000395, 1.1), (2.3502719166, 2.0000993592))
                Line((2.8000000395, 1.1), (2.6500000395, 1.1))
                Line((2.8000000395, 1.1), (2.5000000373, 2.0000000298))
                Line((2.5000000373, 2.0000000298), (2.3502719166, 2.0000993592))
            make_face()
            # Profile area: 0.165, perimeter: 2.5
            with BuildLine():
                Line((2.8000000395, 0), (2.8000000395, 1.1))
                Line((2.8000000395, 1.1), (2.6500000395, 1.1))
                Line((2.6500000395, 1.1), (2.6500000395, 0))
                Line((2.6500000395, 0), (2.8000000395, 0))
            make_face()
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.ADD)
    return part.part


# Description: This is a stepped shaft or tiered cylindrical component featuring multiple coaxial diameters of decreasing size arranged in a staircase pattern along its length, creating a series of shoulder transitions.
def model_21599_80057f94_0000():
    """Model: Untitled"""
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
        # Sketch28 -> Extrude10 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 44 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0074999991, perimeter: 0.3999999762
            with BuildLine():
                Line((1.5999999046, 0.2999999821), (1.5999999046, 0.2499999851))
                Line((1.5999999046, 0.2499999851), (1.7499998957, 0.2499999851))
                Line((1.7499998957, 0.2499999851), (1.7499998957, 0.2999999821))
                Line((1.7499998957, 0.2999999821), (1.5999999046, 0.2999999821))
            make_face()
            # Profile area: 0.0074999991, perimeter: 0.3999999762
            with BuildLine():
                Line((1.5999999046, 1.5499999821), (1.5999999046, 1.4999999851))
                Line((1.5999999046, 1.4999999851), (1.7499998957, 1.4999999851))
                Line((1.7499998957, 1.4999999851), (1.7499998957, 1.5499999821))
                Line((1.7499998957, 1.5499999821), (1.5999999046, 1.5499999821))
            make_face()
            # Profile area: 0.0074999991, perimeter: 0.3999999762
            with BuildLine():
                Line((1.5999999046, 1.2999999821), (1.5999999046, 1.2499999851))
                Line((1.5999999046, 1.2499999851), (1.7499998957, 1.2499999851))
                Line((1.7499998957, 1.2499999851), (1.7499998957, 1.2999999821))
                Line((1.7499998957, 1.2999999821), (1.5999999046, 1.2999999821))
            make_face()
            # Profile area: 0.0074999991, perimeter: 0.3999999762
            with BuildLine():
                Line((1.5999999046, 1.7999999821), (1.5999999046, 1.7499999851))
                Line((1.5999999046, 1.7499999851), (1.7499998957, 1.7499999851))
                Line((1.7499998957, 1.7499999851), (1.7499998957, 1.7999999821))
                Line((1.7499998957, 1.7999999821), (1.5999999046, 1.7999999821))
            make_face()
            # Profile area: 0.0074999991, perimeter: 0.3999999762
            with BuildLine():
                Line((1.5999999046, 0.9999999851), (1.7499998957, 0.9999999851))
                Line((1.7499998957, 0.9999999851), (1.7499998957, 1.0499999821))
                Line((1.7499998957, 1.0499999821), (1.5999999046, 1.0499999821))
                Line((1.5999999046, 1.0499999821), (1.5999999046, 0.9999999851))
            make_face()
            # Profile area: 0.0074999991, perimeter: 0.3999999762
            with BuildLine():
                Line((1.5999999046, 2.0499999821), (1.5999999046, 1.9999999851))
                Line((1.5999999046, 1.9999999851), (1.7499998957, 1.9999999851))
                Line((1.7499998957, 1.9999999851), (1.7499998957, 2.0499999821))
                Line((1.7499998957, 2.0499999821), (1.5999999046, 2.0499999821))
            make_face()
            # Profile area: 0.0074999991, perimeter: 0.3999999762
            with BuildLine():
                Line((1.5999999046, 0.7499999851), (1.7499998957, 0.7499999851))
                Line((1.7499998957, 0.7499999851), (1.7499998957, 0.7999999821))
                Line((1.7499998957, 0.7999999821), (1.5999999046, 0.7999999821))
                Line((1.5999999046, 0.7999999821), (1.5999999046, 0.7499999851))
            make_face()
            # Profile area: 0.0074999991, perimeter: 0.3999999762
            with BuildLine():
                Line((1.5999999046, 2.2999999821), (1.5999999046, 2.2499999851))
                Line((1.5999999046, 2.2499999851), (1.7499998957, 2.2499999851))
                Line((1.7499998957, 2.2499999851), (1.7499998957, 2.2999999821))
                Line((1.7499998957, 2.2999999821), (1.5999999046, 2.2999999821))
            make_face()
            # Profile area: 0.0074999991, perimeter: 0.3999999762
            with BuildLine():
                Line((1.5999999046, 0.4999999851), (1.7499998957, 0.4999999851))
                Line((1.7499998957, 0.4999999851), (1.7499998957, 0.5499999821))
                Line((1.7499998957, 0.5499999821), (1.5999999046, 0.5499999821))
                Line((1.5999999046, 0.5499999821), (1.5999999046, 0.4999999851))
            make_face()
            # Profile area: 0.0074999991, perimeter: 0.3999999762
            with BuildLine():
                Line((1.5999999046, 2.4999999851), (1.7499998957, 2.4999999851))
                Line((1.7499998957, 2.4999999851), (1.7499998957, 2.5499999821))
                Line((1.7499998957, 2.5499999821), (1.5999999046, 2.5499999821))
                Line((1.5999999046, 2.5499999821), (1.5999999046, 2.4999999851))
            make_face()
        # OneSide extrude, distance=0.01
        extrude(amount=0.01)
    return part.part


# Description: This is an elliptical structural frame or reinforcing ring with a blue membrane or panel stretched across its interior, featuring a dark rim/flange around its perimeter and internal radial support members or stringers.
def model_21647_6b6cca6f_0001():
    """Model: Cyclone v16 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 774.3711731833, perimeter: 98.6460093227
            Circle(15.7)
        # OneSide extrude, distance=1.8
        extrude(amount=1.8)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 72.2173611244, perimeter: 192.5796296651
            with BuildLine():
                CenterArc((0, 0), 15.7, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 14.95, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.9
        extrude(amount=-0.9, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical rod or shaft with a rectangular connector block or coupling attached at one end, featuring a long slender body and a compact squared-off terminal fitting.
def model_21695_1f33863f_0002():
    """Model: 11. Lamp v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0016417322, perimeter: 0.1436336161
            with Locations((-0.10922, 0)):
                Circle(0.02286)
            # Profile area: 0.0016417322, perimeter: 0.1436336161
            with Locations((0.10922, 0)):
                Circle(0.02286)
        # OneSide extrude, distance=3.556
        extrude(amount=3.556)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(3.556, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0653703319, perimeter: 1.0612928302
            with BuildLine():
                CenterArc((0, 0), 0.14605, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0.10922, 0), 0.02286, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0016417322, perimeter: 0.1436336161
            with Locations((0.10922, 0)):
                Circle(0.02286)
        # OneSide extrude, distance=0.40386
        extrude(amount=0.40386, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical rod or shaft with rounded ends, featuring a uniform circular cross-section and a slight diagonal orientation.
def model_21697_06656699_0005():
    """Model: 4. Drive Shaft v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.8601055433, perimeter: 3.2876138801
            Circle(0.52324)
        # Symmetric extrude, each_side=5.08
        extrude(amount=5.08, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5.08, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0505774395, perimeter: 0.9496945275
            with BuildLine():
                CenterArc((0, 0), 0.52324, 74.3319300723, 30.9706611472)
                Line((0.1413082405, 0.5037976566), (0.1413082405, 0.6979744045))
                Line((0.1413082405, 0.6979744045), (-0.1380917595, 0.6979744045))
                Line((-0.1380917595, 0.6979744045), (-0.1380917595, 0.5046887789))
            make_face()
            # Profile area: 0.0394055223, perimeter: 0.8188854699
            with BuildLine():
                Line((-0.1380917595, 0.5046887789), (-0.1380917595, 0.3759165598))
                Line((-0.1380917595, 0.3759165598), (0.1413082405, 0.3759165598))
                Line((0.1413082405, 0.3759165598), (0.1413082405, 0.5037976566))
                CenterArc((0, 0), 0.52324, 74.3319300723, 30.9706611472)
            make_face()
        # OneSide extrude, distance=-1.8415
        extrude(amount=-1.8415, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -5.08, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0505774395, perimeter: 0.9496945275
            with BuildLine():
                Line((-0.1413082405, 0.6979744045), (-0.1413082405, 0.5037976566))
                CenterArc((0, 0), 0.52324, 74.6974087805, 30.9706611472)
                Line((0.1380917595, 0.5046887789), (0.1380917595, 0.6979744045))
                Line((-0.1413082405, 0.6979744045), (0.1380917595, 0.6979744045))
            make_face()
            # Profile area: 0.0394055223, perimeter: 0.8188854699
            with BuildLine():
                Line((-0.1413082405, 0.5037976566), (-0.1413082405, 0.3759165598))
                Line((-0.1413082405, 0.3759165598), (0.1380917595, 0.3759165598))
                Line((0.1380917595, 0.3759165598), (0.1380917595, 0.5046887789))
                CenterArc((0, 0), 0.52324, 74.6974087805, 30.9706611472)
            make_face()
        # OneSide extrude, distance=-1.8542
        extrude(amount=-1.8542, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical threaded fastener or bolt with a knurled hexagonal head at the top and a long shaft, designed for fastening applications.
def model_21702_3390d14a_0004():
    """Model: Power Screw v1 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.0685007165, perimeter: 7.1502648796
            Circle(1.138)
        # OneSide extrude, distance=8.021
        extrude(amount=8.021)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 8.021, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6074457891, perimeter: 14.8157509543
            with BuildLine():
                CenterArc((0, 0), 1.22, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.138, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 4.0685007165, perimeter: 7.1502648796
            Circle(1.138)
        # OneSide extrude, distance=0.479
        extrude(amount=0.479, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 8.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.9722594558, perimeter: 10.0091141943
            Circle(1.593)
        # OneSide extrude, distance=0.8678
        extrude(amount=0.8678, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical sleeve or spacer with a mesh or perforated top section and a solid body, featuring a protruding collar or flange at the bottom.
def model_21702_3390d14a_0005():
    """Model: Valve Bolt v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.9245903529, perimeter: 3.4086280291
            Circle(0.5425)
        # OneSide extrude, distance=1.6
        extrude(amount=1.6)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.534561625, perimeter: 2.5918139392
            Circle(0.4125)
        # OneSide extrude, distance=0.225
        extrude(amount=0.225, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -0.225, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.3900287279, perimeter: 6.0004419684
            with BuildLine():
                CenterArc((0, 0), 0.5425, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.4125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.534561625, perimeter: 2.5918139392
            Circle(0.4125)
        # OneSide extrude, distance=0.1325
        extrude(amount=0.1325, mode=Mode.ADD)
    return part.part


# Description: This is a dark gray/charcoal bracket or mounting arm with an elongated main body featuring a central slot, two perpendicular flanges on the right end, and blue accent markings along the top surface.
def model_21710_0b9db742_0006():
    """Model: Potihalter v4 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 32 constraints, 19 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 16.0893385616, perimeter: 44.4537930175
            with BuildLine():
                CenterArc((0, 0), 2.4, 50, 109.2576200455)
                Line((-8.175, 0.85), (-2.2444375687, 0.85))
                CenterArc((-8.175, 0), 0.85, 90, 180)
                Line((-2.2444375687, -0.85), (-8.175, -0.85))
                CenterArc((0, 0), 2.4, -159.2576200455, 109.2576200455)
                Line((1.0284601755, -1.225671109), (1.5426902632, -1.8385066635))
                CenterArc((0, 0), 1.6, -176.4166783015, 126.4166783015)
                Line((-1.5968719423, -0.1), (-4.3101020514, -0.1))
                CenterArc((-4.8, 0), 0.5, 11.5369590328, 336.9260819344)
                Line((-4.3101020514, 0.1), (-1.5968719423, 0.1))
                CenterArc((0, 0), 1.6, 50, 126.4166783015)
                Line((1.0284601755, 1.225671109), (1.5426902632, 1.8385066635))
            make_face()
            with BuildLine():
                Line((-8.175, 0.325), (-7.3895860964, 0.325))
                Line((-7.3895860964, 0.325), (-7.325, 0.325))
                CenterArc((-7.325, 0), 0.325, -90, 180)
                Line((-7.325, -0.325), (-7.3895860964, -0.325))
                Line((-7.3895860964, -0.325), (-8.175, -0.325))
                CenterArc((-8.175, 0), 0.325, 90, 180)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.85), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1452201204, perimeter: 1.350884841
            with Locations((-2.9944375687, 0.4)):
                Circle(0.215)
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.85), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((2.9944375687, 0.4)):
                Circle(0.2)
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a multi-chambered housing or manifold block with a complex stepped/tiered structure featuring multiple internal cavities, rectangular openings, and angular geometric faces designed for fluid or gas flow distribution across different levels.
def model_21734_7cf58bd0_0001():
    """Model: Part 31 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 8 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.7918252296, perimeter: 9.2853981634
            with BuildLine():
                Line((0, 1.7), (0, 0))
                Line((0, 0), (1.95, 0))
                Line((1.95, 0), (1.95, 1.7))
                Line((1.225, 1.7), (1.95, 1.7))
                Line((1.225, 1.7), (1.225, 0.85))
                CenterArc((0.975, 0.85), 0.25, 180, 180)
                Line((0.725, 1.7), (0.725, 0.85))
                Line((0, 1.7), (0.725, 1.7))
            make_face()
        # OneSide extrude, distance=1.1
        extrude(amount=1.1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1.1, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))) as sk:
            # Profile area: 0.90112529, perimeter: 4.9812559873
            with BuildLine():
                Line((1.95, 0.5), (1.3320714214, 0.5))
                CenterArc((0.975, 0.85), 0.5, -135.5729959992, 91.1459919984)
                Line((0.6179285786, 0.5), (0, 0.5))
                Line((0, 0.5), (0, 0))
                Line((0, 0), (1.95, 0))
                Line((1.95, 0), (1.95, 0.5))
            make_face()
        # TwoSides extrude, along=0.4, against=-1.5
        extrude(amount=0.4, mode=Mode.ADD)
        extrude(sk.sketch, amount=-1.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 12 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 1.3103495408, perimeter: 4.2507963268
            with BuildLine():
                CenterArc((0.85, -0.605), 0.25, 0, 90)
                Line((0.85, -0.355), (0.25, -0.355))
                CenterArc((0.25, -0.605), 0.25, 90, 90)
                Line((0, -0.605), (0, -1.345))
                CenterArc((0.25, -1.345), 0.25, 180, 90)
                Line((0.25, -1.595), (0.85, -1.595))
                CenterArc((0.85, -1.345), 0.25, -90, 90)
                Line((1.1, -1.345), (1.1, -0.605))
            make_face()
        # OneSide extrude, distance=-0.25
        extrude(amount=-0.25, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical shaft or axle with hexagonal heads on both ends, designed for mechanical power transmission or as a connector between components.
def model_21773_01f6bc23_0011():
    """Model: Bolt v3 (6)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=9.9
        extrude(amount=9.9)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 9.9), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.4616784181, perimeter: 7.2985145918
            with BuildLine():
                Line((0.669213043, 0.1793150944), (0.1793150944, 0.669213043))
                Line((0.1793150944, 0.669213043), (-0.4898979486, 0.4898979486))
                Line((-0.4898979486, 0.4898979486), (-0.669213043, -0.1793150944))
                Line((-0.669213043, -0.1793150944), (-0.1793150944, -0.669213043))
                Line((-0.1793150944, -0.669213043), (0.4898979486, -0.4898979486))
                Line((0.4898979486, -0.4898979486), (0.669213043, 0.1793150944))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.4616784181, perimeter: 7.2985145918
            with BuildLine():
                Line((0.1793150944, -0.669213043), (0.669213043, -0.1793150944))
                Line((0.669213043, -0.1793150944), (0.4898979486, 0.4898979486))
                Line((0.4898979486, 0.4898979486), (-0.1793150944, 0.669213043))
                Line((-0.1793150944, 0.669213043), (-0.669213043, 0.1793150944))
                Line((-0.669213043, 0.1793150944), (-0.4898979486, -0.4898979486))
                Line((-0.4898979486, -0.4898979486), (0.1793150944, -0.669213043))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4, mode=Mode.ADD)
    return part.part


# Description: This is a parallelogram-shaped panel or bracket with a large central oval cutout, smaller circular/oval holes around the perimeter, and blue-highlighted edges/ribs that suggest structural reinforcement or design features.
def model_21803_8a36dcda_0009():
    """Model: Cylinder Head Gasket v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 22.5, perimeter: 19
            with BuildLine():
                Line((5, -4.5), (0, -4.5))
                Line((5, 0), (5, -4.5))
                Line((0, 0), (5, 0))
                Line((0, -4.5), (0, 0))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 12 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.4269796411, perimeter: 11.9054643892
            with BuildLine():
                CenterArc((-4.6, 2.25), 0.2, 90, 180)
                Line((-4.6, 2.05), (-3.7874507866, 2.05))
                CenterArc((-2.2, 2.25), 1.6, -172.8192442185, 345.6384884371)
                Line((-4.6, 2.45), (-3.7874507866, 2.45))
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            with Locations((-3.8263455967, 0.6236544033)):
                Circle(0.35)
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            with Locations((-3.8263455967, 3.8763455967)):
                Circle(0.35)
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            with Locations((-0.5736544033, 3.8763455967)):
                Circle(0.35)
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            with Locations((-0.5736544033, 0.6236544033)):
                Circle(0.35)
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical container or vessel with a curved sidewall and an open top featuring a flat or slightly recessed rim, designed as a simple cup, bucket, or storage container.
def model_21803_8a36dcda_0032():
    """Model: Piston v8 (9)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.0424771932, perimeter: 10.0530964915
            Circle(1.6)
        # OneSide extrude, distance=3.2
        extrude(amount=3.2)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # OneSide extrude, distance=-2.5
        extrude(amount=-2.5, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 2.167698931, perimeter: 14.4513262065
            with BuildLine():
                CenterArc((0, 0), 1.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a flat rectangular plate or base with a trapezoidal or wedge-like profile, featuring a sloped top surface and a thickened dark edge or flange along one side.
def model_21816_3891a442_0001():
    """Model: Base v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 100, perimeter: 40
            with BuildLine():
                Line((5, -5), (5, 5))
                Line((5, 5), (-5, 5))
                Line((-5, 5), (-5, -5))
                Line((-5, -5), (5, -5))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a multi-segment articulated arm or linkage assembly featuring a series of connected rectangular segments with pivot joints, designed to bend at multiple points with integrated mounting flanges and cylindrical pivot pins.
def model_21822_7d3db422_0002():
    """Model: Packnut Valve"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3769911184, perimeter: 3.7699111843
            with BuildLine():
                CenterArc((-8.0000001192, -7.0000001043), 0.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-8.0000001192, -7.0000001043), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.9
        extrude(amount=0.9)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.9, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.363370605, perimeter: 5.9773757896
            with BuildLine():
                Line((7.5000001118, 7.2886752432), (7.5000001118, 6.7113249654))
                Line((7.5000001118, 6.7113249654), (8.0000001192, 6.4226498265))
                Line((8.0000001192, 6.4226498265), (8.5000001267, 6.7113249654))
                Line((8.5000001267, 6.7113249654), (8.5000001267, 7.2886752432))
                Line((8.5000001267, 7.2886752432), (8.0000001192, 7.5773503821))
                Line((8.0000001192, 7.5773503821), (7.5000001118, 7.2886752432))
            make_face()
            with BuildLine():
                CenterArc((8.0000001192, 7.0000001043), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.3769911184, perimeter: 3.7699111843
            with BuildLine():
                CenterArc((8.0000001192, 7.0000001043), 0.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((8.0000001192, 7.0000001043), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 16 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.5036504592, perimeter: 17.3707963268
            with BuildLine():
                Line((-8.9, -9.65), (-10, -9.65))
                Line((-10, -10.55), (-10, -9.65))
                Line((-8.9, -10.55), (-10, -10.55))
                CenterArc((-8.9, -10.8), 0.25, -90, 180)
                Line((-10, -11.05), (-8.9, -11.05))
                Line((-10, -12.5), (-10, -11.05))
                Line((-7.8, -12.5), (-10, -12.5))
                Line((-7.8, -8.5), (-7.8, -12.5))
                Line((-10, -8.5), (-7.8, -8.5))
                Line((-10, -9.15), (-10, -8.5))
                Line((-8.9, -9.15), (-10, -9.15))
                CenterArc((-8.9, -9.4), 0.25, -90, 180)
            make_face()
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)
    return part.part


# Description: This is a cylindrical coupling or connector with a stepped diameter design, featuring a larger base flange and a smaller upper section, with mesh-textured surfaces indicating internal geometry or threading.
def model_21822_7d3db422_0003():
    """Model: Eccentric"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.0424771932, perimeter: 10.0530964915
            with Locations((-5, -7.5)):
                Circle(1.6)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.6703537556, perimeter: 10.6814150222
            with BuildLine():
                CenterArc((5.25, 7.5), 1.1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((5, 7.5), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0.6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((5, 7.5)):
                Circle(0.6)
        # OneSide extrude, distance=-2.2
        extrude(amount=-2.2, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a dark gray/blue industrial bracket or mounting plate with an irregular hexagonal base shape, featuring multiple internal cutouts, slots, and mounting holes distributed across its surface, with some raised flanges or tabs on the upper portions.
def model_21822_7d3db422_0008():
    """Model: Main Bearing Head"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.8803097999, perimeter: 13.1991148575
            with BuildLine():
                Line((-5.5, -2.5), (-7.05, -2.5))
                Line((-5.5, -0.8), (-5.5, -2.5))
                Line((-10, -0.8), (-5.5, -0.8))
                Line((-10, -2.5), (-10, -0.8))
                Line((-8.45, -2.5), (-10, -2.5))
                CenterArc((-7.75, -2.5), 0.7, 0, 180)
            make_face()
        # OneSide extrude, distance=1.6
        extrude(amount=1.6)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.8), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((9.35, 0.8)):
                Circle(0.4)
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((6.15, 0.8)):
                Circle(0.4)
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.8), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.1590431281, perimeter: 1.4137166941
            with Locations((9.35, 0.8)):
                Circle(0.225)
            # Profile area: 0.1590431281, perimeter: 1.4137166941
            with Locations((6.15, 0.8)):
                Circle(0.225)
        # OneSide extrude, distance=-2.2
        extrude(amount=-2.2, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a skid plate or protective underbody panel with a trapezoidal shape, featuring a recessed main body, angled side flanges, and ventilation or access slots/openings on the left side.
def model_21822_7d3db422_0012():
    """Model: Cylinder Foot"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 14 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.9028182176, perimeter: 18.1585670135
            with BuildLine():
                CenterArc((7.3500000894, -4.9000001043), 0.225, 90, 90)
                Line((7.3500000894, -4.4000001043), (7.3500000894, -4.6750001043))
                Line((7.3500000894, -4.4000001043), (6.7505554394, -4.4000001043))
                Line((6.0000000894, -5.7000001043), (6.7505554394, -4.4000001043))
                Line((6.0000000894, -5.7000001043), (6.0000000894, -7.0000001043))
                Line((6.0000000894, -7.0000001043), (10.6000000894, -7.0000001043))
                Line((10.6000000894, -7.0000001043), (10.6000000894, -5.7000001043))
                Line((10.6000000894, -5.7000001043), (9.8494447395, -4.4000001043))
                Line((9.8494447395, -4.4000001043), (9.2000000894, -4.4000001043))
                CenterArc((8.3000000894, -3.3276195748), 1.4, -130.0052008849, 80.0104017697)
                Line((7.4000000894, -4.4000001043), (7.3500000894, -4.4000001043))
                CenterArc((7.3500000894, -4.9000001043), 0.225, 0, 90)
                Line((7.5750000894, -5.3000001043), (7.5750000894, -4.9000001043))
                CenterArc((7.3500000894, -5.3000001043), 0.225, 180, 180)
                Line((7.1250000894, -4.9000001043), (7.1250000894, -5.3000001043))
            make_face()
            with BuildLine():
                Line((9.0250000894, -5.3000001043), (9.0250000894, -4.9000001043))
                CenterArc((9.2500000894, -4.9000001043), 0.225, 0, 180)
                Line((9.4750000894, -5.3000001043), (9.4750000894, -4.9000001043))
                CenterArc((9.2500000894, -5.3000001043), 0.225, 180, 180)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.3800000103, perimeter: 9.8000000685
            with BuildLine():
                Line((-6.0000000894, 6.7000001043), (-10.600000158, 6.7000001043))
                Line((-6.0000000894, 7.0000001043), (-6.0000000894, 6.7000001043))
                Line((-10.6000000894, 7.0000001043), (-6.0000000894, 7.0000001043))
                Line((-10.6000000894, 7.0000001043), (-10.600000158, 6.7000001043))
            make_face()
        # OneSide extrude, distance=1.7
        extrude(amount=1.7, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 6.7000001043), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.1590431281, perimeter: 1.4137166941
            with Locations((-6.5000000969, 1.5000000224)):
                Circle(0.225)
            # Profile area: 0.1590431281, perimeter: 1.4137166941
            with Locations((-10.1000001505, 1.5000000224)):
                Circle(0.225)
        # OneSide extrude, distance=-0.9
        extrude(amount=-0.9, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical connector or adapter with two coaxial tubular sections of different diameters joined together, featuring a mesh or perforated pattern on the upper end.
def model_21822_7d3db422_0013():
    """Model: Crank Screw"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((1.0000000149, 0)):
                Circle(0.3)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch8 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((1.0000000149, 0)):
                Circle(0.15)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch9 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -0.1, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.1256637061, perimeter: 2.5132741229
            with BuildLine():
                CenterArc((1.0000000149, 0), 0.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((1.0000000149, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((1.0000000149, 0)):
                Circle(0.15)
        # OneSide extrude, distance=0.9
        extrude(amount=0.9, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical spacer or sleeve with flanged ends at both the top and bottom, featuring a hollow central bore and vertical ribbing or fluting along its sides for structural reinforcement.
def model_21822_7d3db422_0022():
    """Model: Rod"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0706858368, perimeter: 0.9424778101
            Circle(0.1500000022)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0549778693, perimeter: 2.1991148716
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1500000022, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0706858368, perimeter: 0.9424778101
            Circle(0.1500000022)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0549778693, perimeter: 2.1991148716
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1500000022, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0706858368, perimeter: 0.9424778101
            Circle(0.1500000022)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical connector or coupling sleeve with an open top rim, featuring two rectangular slot cutouts on opposite sides of the body and a tapered or slightly curved profile.
def model_21822_7d3db422_0031():
    """Model: Screw 7"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1590431281, perimeter: 1.4137166941
            Circle(0.225)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
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

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.7, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1315276082, perimeter: 1.35
            with BuildLine():
                Line((-0.1948557159, -0.1125), (0, -0.225))
                Line((0, -0.225), (0.1948557159, -0.1125))
                Line((0.1948557159, -0.1125), (0.1948557159, 0.1125))
                Line((0.1948557159, 0.1125), (0, 0.225))
                Line((0, 0.225), (-0.1948557159, 0.1125))
                Line((-0.1948557159, 0.1125), (-0.1948557159, -0.1125))
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical fastener or connector with a large flanged head at the top and a threaded or ribbed cylindrical shaft below, featuring internal cavity detailing in the head region.
def model_21822_7d3db422_0032():
    """Model: Screw 6"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4417864669, perimeter: 3.926990817
            with BuildLine():
                CenterArc((0, 0), 0.425, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=-0.225
        extrude(amount=-0.225, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.233826866, perimeter: 1.8000000268
            with BuildLine():
                Line((-0.1500000022, 0.259807625), (-0.3000000045, 0))
                Line((-0.3000000045, 0), (-0.1500000022, -0.259807625))
                Line((-0.1500000022, -0.259807625), (0.1500000022, -0.259807625))
                Line((0.1500000022, -0.259807625), (0.3000000045, 0))
                Line((0.3000000045, 0), (0.1500000022, 0.259807625))
                Line((0.1500000022, 0.259807625), (-0.1500000022, 0.259807625))
            make_face()
        # OneSide extrude, distance=-0.12
        extrude(amount=-0.12, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a hex bolt or cap screw with a cylindrical shaft and a hexagonal head featuring measurement markings on top.
def model_21822_7d3db422_0035():
    """Model: Screw 5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=2.6
        extrude(amount=2.6)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5831581363, perimeter: 4.2411500823
            with BuildLine():
                CenterArc((0, 0), 0.475, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.275
        extrude(amount=-0.275, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.233826866, perimeter: 1.8000000268
            with BuildLine():
                Line((-0.1500000022, 0.259807625), (-0.3000000045, 0))
                Line((-0.3000000045, 0), (-0.1500000022, -0.259807625))
                Line((-0.1500000022, -0.259807625), (0.1500000022, -0.259807625))
                Line((0.1500000022, -0.259807625), (0.3000000045, 0))
                Line((0.3000000045, 0), (0.1500000022, 0.259807625))
                Line((0.1500000022, 0.259807625), (-0.1500000022, 0.259807625))
            make_face()
        # OneSide extrude, distance=-0.17
        extrude(amount=-0.17, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical socket or sleeve with an open top end, featuring a larger diameter hollow opening at the upper end and a tapered or stepped transition along its length, designed for fastening or assembly purposes.
def model_21822_7d3db422_0040():
    """Model: Screw 8"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            Circle(0.1)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0392699082, perimeter: 1.5707963268
            with BuildLine():
                CenterArc((0, 0), 0.15, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            Circle(0.1)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0314367208, perimeter: 0.6599999852
            with BuildLine():
                Line((-0.0549999988, 0.0952627923), (-0.1099999975, 0))
                Line((-0.1099999975, 0), (-0.0549999988, -0.0952627923))
                Line((-0.0549999988, -0.0952627923), (0.0549999988, -0.0952627923))
                Line((0.0549999988, -0.0952627923), (0.1099999975, 0))
                Line((0.1099999975, 0), (0.0549999988, 0.0952627923))
                Line((0.0549999988, 0.0952627923), (-0.0549999988, 0.0952627923))
            make_face()
        # OneSide extrude, distance=-0.18
        extrude(amount=-0.18, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical socket or sleeve with a hexagonal head at the top, commonly used as a deep socket wrench or tool holder attachment.
def model_21822_7d3db422_0041():
    """Model: Screw 9"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=1.6
        extrude(amount=1.6)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1570796327, perimeter: 3.1415926536
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1039230485, perimeter: 1.2
            with BuildLine():
                Line((0.1, -0.1732050808), (0.2, 0))
                Line((0.2, 0), (0.1, 0.1732050808))
                Line((0.1, 0.1732050808), (-0.1, 0.1732050808))
                Line((-0.1, 0.1732050808), (-0.2, 0))
                Line((-0.2, 0), (-0.1, -0.1732050808))
                Line((-0.1, -0.1732050808), (0.1, -0.1732050808))
            make_face()
        # OneSide extrude, distance=-0.33
        extrude(amount=-0.33, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical socket or sleeve with a hollow interior, featuring a knurled or textured top rim and a stepped shoulder where the diameter transitions from larger to smaller.
def model_21822_7d3db422_0047():
    """Model: Screw 10"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0549778752, perimeter: 2.1991148762
            with BuildLine():
                CenterArc((0, 0), 0.200000003, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0509222915, perimeter: 0.8399999812
            with BuildLine():
                Line((-0.0699999984, 0.1212435538), (-0.1399999969, 0))
                Line((-0.1399999969, 0), (-0.0699999984, -0.1212435538))
                Line((-0.0699999984, -0.1212435538), (0.0699999984, -0.1212435538))
                Line((0.0699999984, -0.1212435538), (0.1399999969, 0))
                Line((0.1399999969, 0), (0.0699999984, 0.1212435538))
                Line((0.0699999984, 0.1212435538), (-0.0699999984, 0.1212435538))
            make_face()
        # OneSide extrude, distance=-0.25
        extrude(amount=-0.25, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a shaft or axle component with a hexagonal or angular head on one end and a cylindrical body, featuring a tapered transition between the two sections and a dark finish on the cylindrical portion.
def model_21847_b2de7eb8_0018():
    """Model: 11A"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 11 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.2814711561, perimeter: 4.0206035815
            with BuildLine():
                CenterArc((0, 0.0500000007), 0.2000000007, -14.4775123513, 284.4775123513)
                Line((1.3, -0.15), (0, -0.15))
                Line((1.3, 0), (1.3, -0.15))
                Line((0.1936491679, 0), (1.3, 0))
            make_face()
            with BuildLine():
                CenterArc((0, 0.0500000007), 0.075, -41.8103156594, 311.8103156594)
                CenterArc((0, 0.0500000007), 0.075, -90, 48.1896843406)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0176714587, perimeter: 0.471238898
            with Locations((0, 0.0500000007)):
                Circle(0.075)
        # OneSide extrude, distance=0.45
        extrude(amount=0.45, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0176714587, perimeter: 0.471238898
            with Locations((0, 0.0500000007)):
                Circle(0.075)
        # OneSide extrude, distance=0.15
        extrude(amount=0.15, mode=Mode.ADD)
    return part.part


# Description: This is a simple spacer or shim with a rectangular shape, consisting of two parallel flat surfaces separated by a small vertical distance, designed to create spacing or alignment between components.
def model_21864_4c028c8c_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            with Locations((-20, 0)):
                Circle(2.5)
        # Symmetric extrude, each_side=60
        extrude(amount=60, both=True)

        # Sketch6 -> Extrude2 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.2619467106, perimeter: 6.1699111843
            with BuildLine():
                Line((-35.7929101456, -23.6590478275), (-34.818177827, -21.4659001108))
                CenterArc((-35.3055439863, -22.5624739692), 1.2, -113.9624889746, 180)
            make_face()
            # Profile area: 2.2619467106, perimeter: 6.1699111843
            with BuildLine():
                CenterArc((-35.3055439863, -22.5624739692), 1.2, 66.0375110254, 180)
                Line((-35.7929101456, -23.6590478275), (-34.818177827, -21.4659001108))
            make_face()
        # Symmetric extrude, each_side=72.5
        extrude(amount=72.5, both=True)
    return part.part


# Description: This is a suppressor or silencer featuring a cylindrical body with a tapered upper section, a mid-body collar or mounting flange, and what appears to be mounting holes or slots along the lower section for attachment to a firearm barrel.
def model_21893_0500d043_0032():
    """Model: SEMI ALBERO F v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=2.3
        extrude(amount=2.3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 12 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0150646979, perimeter: 0.8945147077
            with BuildLine():
                CenterArc((0, 0), 0.5, -26.0711611031, 52.1423222061)
                Line((0.4491244491, 0.2197435533), (0.4491244491, -0.2197435533))
            make_face()
            # Profile area: 0.0143045348, perimeter: 0.8793117277
            with BuildLine():
                CenterArc((0, 0), 0.5, 154.3872955767, 51.2254088465)
                Line((-0.4508683481, -0.2161428526), (-0.4508683481, 0.2161428526))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical connector or adapter with a flanged head at the top featuring a mesh or perforated opening, and a tapered cylindrical body below.
def model_21893_0500d043_0046():
    """Model: M3 X 5 -4.8 v2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 2.5132741229
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 13 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.7, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0078, perimeter: 0.3800000013
            with BuildLine():
                Line((0.0299999993, 0.03), (0.0299999993, -0.03))
                Line((0.16, -0.03), (0.0299999993, -0.03))
                Line((0.16, 0.03), (0.16, -0.03))
                Line((0.0299999993, 0.03), (0.16, 0.03))
            make_face()
            # Profile area: 0.0078, perimeter: 0.3800000013
            with BuildLine():
                Line((-0.16, 0.03), (-0.0299999993, 0.03))
                Line((-0.16, -0.03), (-0.16, 0.03))
                Line((-0.0299999993, -0.03), (-0.16, -0.03))
                Line((-0.0299999993, -0.03), (-0.0299999993, 0.03))
            make_face()
            # Profile area: 0.0077999996, perimeter: 0.3799999902
            with BuildLine():
                Line((-0.0299999993, 0.03), (-0.0299999993, 0.1599999964))
                Line((-0.0299999993, 0.03), (0.0299999993, 0.03))
                Line((0.0299999993, 0.1599999964), (0.0299999993, 0.03))
                Line((-0.0299999993, 0.1599999964), (0.0299999993, 0.1599999964))
            make_face()
            # Profile area: 0.0077999996, perimeter: 0.3799999902
            with BuildLine():
                Line((0.0299999993, -0.03), (-0.0299999993, -0.03))
                Line((-0.0299999993, -0.1599999964), (-0.0299999993, -0.03))
                Line((0.0299999993, -0.1599999964), (-0.0299999993, -0.1599999964))
                Line((0.0299999993, -0.03), (0.0299999993, -0.1599999964))
            make_face()
            # Profile area: 0.0035999999, perimeter: 0.2399999973
            with BuildLine():
                Line((-0.0299999993, -0.03), (-0.0299999993, 0.03))
                Line((0.0299999993, -0.03), (-0.0299999993, -0.03))
                Line((0.0299999993, 0.03), (0.0299999993, -0.03))
                Line((-0.0299999993, 0.03), (0.0299999993, 0.03))
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical housing or connector body with a rectangular flange extending from the top, featuring internal geometric complexity and what appears to be mounting or alignment features on the upper section.
def model_21899_d55d6c08_0013():
    """Model: BSE043-1 v2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.4635829324, perimeter: 4.5033320997
            with BuildLine():
                Line((0.375277675, 0.65), (-0.375277675, 0.65))
                Line((-0.375277675, 0.65), (-0.7505553499, 0))
                Line((-0.7505553499, 0), (-0.375277675, -0.65))
                Line((-0.375277675, -0.65), (0.375277675, -0.65))
                Line((0.375277675, -0.65), (0.7505553499, 0))
                Line((0.7505553499, 0), (0.375277675, 0.65))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.5890486225, perimeter: 4.7123889804
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.9
        extrude(amount=0.9, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical housing or connector assembly featuring a central dark cylindrical body with a blue polygonal (faceted) mounting bracket or adapter head on top, designed to interface multiple components together.
def model_21899_d55d6c08_0020():
    """Model: BSE014-1 v2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1263517077, perimeter: 6.5817930688
            with BuildLine():
                Line((0.5484827557, 0.95), (-0.5484827557, 0.95))
                Line((-0.5484827557, 0.95), (-1.0969655115, 0))
                Line((-1.0969655115, 0), (-0.5484827557, -0.95))
                Line((-0.5484827557, -0.95), (0.5484827557, -0.95))
                Line((0.5484827557, -0.95), (1.0969655115, 0))
                Line((1.0969655115, 0), (0.5484827557, 0.95))
            make_face()
        # OneSide extrude, distance=0.85
        extrude(amount=0.85)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            Circle(0.6)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -1, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.301907054, perimeter: 1.9477874452
            Circle(0.31)
        # OneSide extrude, distance=-2.5
        extrude(amount=-2.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a T-shaped connector or coupling featuring a cylindrical main body with a perpendicular branch, equipped with internal threads or grooves on both ends for fastening components together.
def model_21899_d55d6c08_0026():
    """Model: BSE017-1 v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 16 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.9724367865, perimeter: 10.584156742
            with BuildLine():
                CenterArc((0, 0), 1.9, -120.3488229276, 60.6976458553)
                Line((0.96, -1.6396341055), (0.96, 1.6396341055))
                CenterArc((0, 0), 1.9, 59.6511770724, 60.6976458553)
                Line((-0.96, 1.6396341055), (-0.96, -1.6396341055))
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.635, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((0, 0.94)):
                Circle(0.6)
        # OneSide extrude, distance=0.83
        extrude(amount=0.83, mode=Mode.ADD)

        # Sketch6 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((0, -0.94)):
                Circle(0.6)
        # OneSide extrude, distance=2.464
        extrude(amount=2.464, mode=Mode.ADD)
    return part.part


# Description: This is a rectangular duct or enclosure with a hexagonal cross-section, featuring two open mesh or perforated rectangular panels on the top surface and internal triangular bracing or baffle structures for structural support.
def model_21899_d55d6c08_0028():
    """Model: BSE037-1 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.93, perimeter: 13.2
            with BuildLine():
                Line((0.95, -2.35), (0.95, 2.35))
                Line((0.95, 2.35), (-0.95, 2.35))
                Line((-0.95, 2.35), (-0.95, -2.35))
                Line((-0.95, -2.35), (0.95, -2.35))
            make_face()
        # OneSide extrude, distance=1.9
        extrude(amount=1.9)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.35), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.182124985, perimeter: 1.7755298323
            with BuildLine():
                Line((0, 1.47), (0, 1.9))
                Line((0, 1.9), (-0.5754128952, 1.9))
                CenterArc((0, 2.07), 0.6, -163.5407503717, 73.5407503717)
            make_face()
            # Profile area: 0.7667233853, perimeter: 3.3805031007
            with BuildLine():
                CenterArc((0, 2.07), 0.6, -16.4592496283, 212.9184992565)
                Line((0, 1.9), (-0.5754128952, 1.9))
                Line((0.5754128952, 1.9), (0, 1.9))
            make_face()
            # Profile area: 0.182124985, perimeter: 1.7755298323
            with BuildLine():
                CenterArc((0, 2.07), 0.6, -90, 73.5407503717)
                Line((0.5754128952, 1.9), (0, 1.9))
                Line((0, 1.47), (0, 1.9))
            make_face()
        # OneSide extrude, distance=-6
        extrude(amount=-6, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.9, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2740916305, perimeter: 4.6491742095
            with BuildLine():
                Line((0.5754128952, -1.1), (0.7, -1.1))
                Line((0.7, -1.1), (0.7, 1.1))
                Line((0.7, 1.1), (0.5754128952, 1.1))
                Line((0.5754128952, 1.1), (0.5754128952, -1.1))
            make_face()
            # Profile area: 2.8059083695, perimeter: 6.9508257905
            with BuildLine():
                Line((0.5754128952, 1.1), (0.5754128952, -1.1))
                Line((0.5754128952, 1.1), (-0.7, 1.1))
                Line((-0.7, 1.1), (-0.7, -1.1))
                Line((-0.7, -1.1), (0.5754128952, -1.1))
            make_face()
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a bent metal bracket or support component with an angular, folded design featuring multiple rectangular cutouts and perforations along its surfaces, designed to provide structural support while minimizing weight.
def model_21941_1a683ec2_0023():
    """Model: kreuzlager v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 12 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 72.6517909552, perimeter: 37.3173866268
            with BuildLine():
                CenterArc((0, -6.5), 4.5, -90, 90)
                Line((0, -11), (0, -19.0000002831))
                Line((6.0000000894, -19.0000002831), (0, -19.0000002831))
                Line((7.5, -18.634), (6.0000000894, -19.0000002831))
                Line((7.5, -11.634), (7.5, -18.634))
                CenterArc((7.5, -10.634), 1, 180, 90)
                Line((6.5, -6.5), (6.5, -10.634))
                Line((6.5, -6.5), (4.5, -6.5))
            make_face()
            # Profile area: 18.3456871912, perimeter: 21.7254377201
            with BuildLine():
                Line((0, 0), (0, -2))
                CenterArc((0, -6.5), 4.5, 0, 90)
                Line((6.5, -6.5), (4.5, -6.5))
                Line((6.5, -4), (6.5, -6.5))
                Line((2.5, 0), (6.5, -4))
                Line((0, 0), (2.5, 0))
            make_face()
        # OneSide extrude, distance=6.8
        extrude(amount=6.8)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(7.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 6.2831853072, perimeter: 10.2831853072
            with BuildLine():
                CenterArc((-3.4, -14.5303187445), 2, 90, 180)
                Line((-3.4, -12.5303187445), (-3.4, -16.5303187445))
            make_face()
            # Profile area: 6.2831853072, perimeter: 10.2831853072
            with BuildLine():
                Line((-3.4, -12.5303187445), (-3.4, -16.5303187445))
                CenterArc((-3.4, -14.5303187445), 2, -90, 180)
            make_face()
        # OneSide extrude, distance=-16.5
        extrude(amount=-16.5, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(7.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.3379421944, perimeter: 26.7035375555
            with BuildLine():
                CenterArc((-3.4, -14.5303187445), 2.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-3.4, -14.5303187445), 2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-5
        extrude(amount=-5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a T-shaped adjustment wrench or spanner consisting of a long cylindrical handle with vertical ribbed knurling and a perpendicular horizontal bar, used for turning or adjusting mechanical components.
def model_22016_c1658896_0004():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 69.4247779608, perimeter: 138.8495559215
            with BuildLine():
                CenterArc((0, 15), 2, 0, 180)
                Line((-2, 15), (-2, -15))
                CenterArc((0, -15), 2, 180, 180)
                Line((2, 15), (2, -15))
            make_face()
            with BuildLine():
                Line((1, 15), (1, -15))
                CenterArc((0, -15), 1, 180, 180)
                Line((-1, 15), (-1, -15))
                CenterArc((0, 15), 1, 0, 180)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides extrude (symmetric), distance=0.75
        extrude(amount=0.75, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.75), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 6.0002053373, perimeter: 10.0002053439
            with BuildLine():
                Line((-2, 1.50030801), (-2.0000000026, -1.4998973313))
                Line((-4, 1.5002053394), (-2, 1.50030801))
                Line((-4, -1.4997946606), (-4, 1.5002053394))
                Line((-2.0000000026, -1.4998973313), (-4, -1.4997946606))
            make_face()
            # Profile area: 6, perimeter: 10
            with BuildLine():
                Line((4, -1.5), (2, -1.5))
                Line((4, 1.5), (4, -1.5))
                Line((2, 1.5), (4, 1.5))
                Line((2, -1.5), (2, 1.5))
            make_face()
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(4, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with BuildLine():
                CenterArc((0, 0), 0.75, -180, 180)
                CenterArc((0, 0), 0.75, 0, 180)
            make_face()
        # OneSide extrude, distance=30
        extrude(amount=30, mode=Mode.ADD)
    return part.part


# Description: A horizontal cylindrical rod or shaft with rounded ends and symmetrical ribbed or slotted patterns on both sides, designed for mechanical assembly or mounting applications.
def model_22017_6d3be48d_0006():
    """Model: Part 6 Gear and Shaft v4"""
    with BuildPart() as part:
        # Sketch3 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2700, perimeter: 310
            with BuildLine():
                Line((135, -10), (0, -10))
                Line((135, 10), (135, -10))
                Line((0, 10), (135, 10))
                Line((0, -10), (0, 10))
            make_face()
        # OneSide extrude, distance=20
        extrude(amount=20)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 14 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 20, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 225, perimeter: 100
            with BuildLine():
                Line((-88.5, 2.5), (-43.5, 2.5))
                Line((-88.5, -2.5), (-88.5, 2.5))
                Line((-43.5, -2.5), (-88.5, -2.5))
                Line((-43.5, 2.5), (-43.5, -2.5))
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude4 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 21.4601836603, perimeter: 35.7079632679
            with BuildLine():
                Line((-10, 10), (-10, 0))
                Line((-10, 0), (0, 0))
                CenterArc((0, 10), 10, -180, 90)
            make_face()
            # Profile area: 21.4601836603, perimeter: 35.7079632679
            with BuildLine():
                CenterArc((0, 10), 10, 0, 90)
                Line((10, 10), (10, 20))
                Line((10, 20), (0, 20))
            make_face()
            # Profile area: 21.4601836603, perimeter: 35.7079632679
            with BuildLine():
                CenterArc((0, 10), 10, 90, 90)
                Line((0, 20), (-10, 20))
                Line((-10, 20), (-10, 10))
            make_face()
            # Profile area: 21.4601836603, perimeter: 35.7079632679
            with BuildLine():
                CenterArc((0, 10), 10, -90, 90)
                Line((0, 0), (10, 0))
                Line((10, 0), (10, 10))
            make_face()
        # OneSide extrude, distance=-135
        extrude(amount=-135, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a timing belt or drive belt with a closed-loop, oval/elliptical shape featuring parallel ridged teeth on its inner surface for gripping pulleys or sprockets.
def model_22019_0ef07114_0003():
    """Model: Flat Washer v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7174977904, perimeter: 28.247944504
            with BuildLine():
                CenterArc((0, 0), 2.2733, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.2225, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.762
        extrude(amount=0.762)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.762, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2522370468, perimeter: 2.6821299307
            with BuildLine():
                CenterArc((0, 0), 2.2225, -104.8695679727, 30.5562410551)
                Line((0.6009118111, -1.9810949039), (0.6009118111, -2.1397222356))
                Line((-0.5703367872, -1.9810949039), (0.6009118111, -1.9810949039))
                Line((-0.5703367872, -2.1480740674), (-0.5703367872, -1.9810949039))
            make_face()
        # OneSide extrude, distance=-0.1016
        extrude(amount=-0.1016, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.762, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0566907879, perimeter: 2.2344107699
            with BuildLine():
                CenterArc((0, 0), 2.0574, -105.653322001, 31.3066440019)
                Line((0.5551195741, -1.9810949039), (-0.5551195741, -1.9810949039))
            make_face()
        # OneSide extrude, distance=-0.1016
        extrude(amount=-0.1016, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical plastic or composite housing with a textured base section and an open top featuring a blue mesh or perforated insert panel, likely designed as a filter cover or ventilation component.
def model_22025_b77024b9_0015():
    """Model: Grub Screw Part 8 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.0106192983, perimeter: 5.0265482457
            Circle(0.8)
        # OneSide extrude, distance=3.2
        extrude(amount=3.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.8981192229, perimeter: 12.8805298797
            with BuildLine():
                CenterArc((0, 0), 1.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 2.0106192983, perimeter: 5.0265482457
            Circle(0.8)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 4.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0302669279, perimeter: 0.7082268391
            with BuildLine():
                Line((-0.1000000015, -1.4000000209), (-0.1000000015, -1.2459935793))
                Line((0.1000000015, -1.4000000209), (-0.1000000015, -1.4000000209))
                Line((0.1000000015, -1.2459935793), (0.1000000015, -1.4000000209))
                CenterArc((0, 0), 1.25, -94.5885658043, 9.1771316086)
            make_face()
            # Profile area: 0.0302669279, perimeter: 0.7082268391
            with BuildLine():
                CenterArc((0, 0), 1.25, 85.4114341957, 9.1771316086)
                Line((0.1000000015, 1.4000000209), (0.1000000015, 1.2459935793))
                Line((-0.1000000015, 1.4000000209), (0.1000000015, 1.4000000209))
                Line((-0.1000000015, 1.2459935793), (-0.1000000015, 1.4000000209))
            make_face()
            # Profile area: 0.4994661609, perimeter: 5.3844022234
            with BuildLine():
                Line((-0.1000000015, -1.2459935793), (-0.1000000015, 1.2459935793))
                CenterArc((0, 0), 1.25, -94.5885658043, 9.1771316086)
                Line((0.1000000015, 1.2459935793), (0.1000000015, -1.2459935793))
                CenterArc((0, 0), 1.25, 85.4114341957, 9.1771316086)
            make_face()
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a curved structural bracket or fender guard with an arch-like shape, featuring two vertical flanges on opposite ends and a hollow central opening, designed for mounting or protective purposes.
def model_22106_db85f777_0052():
    """Model: LandingGear v2 (3)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 15 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 24.040259088, perimeter: 54.1231544882
            with BuildLine():
                CenterArc((4.5103025714, -3.5776605556), 8.6586725367, 18.9437884033, 70.1802150157)
                Line((0, 5.08), (4.6426800712, 5.08))
                Line((0, 0), (0, 5.08))
                Line((0, 0), (1.9022391464, 0.1025242889))
                CenterArc((11.0991417983, -0.3308602403), 9.2071081529, 157.1254084067, 20.1766453264)
                CenterArc((4.7142595331, -4.817081617), 8.3336173027, 26.5725472957, 78.0097612223)
                CenterArc((10.6269387572, 2.0550361627), 3.5014013101, -63.8955639503, 10.1993309232)
            make_face()
            with BuildLine():
                EllipticalCenterArc((5.2845665976, 4.2175026155), 1.7087960797, 0.2712844744, 0, 360, -12.0593393811)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                EllipticalCenterArc((8.7954847056, 3.0534343055), 0.9563452324, 0.2485199639, 0, 360, -31.7773541008)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                EllipticalCenterArc((11.1281459795, 1.1742912862), 0.7184205126, 0.1854953787, 0, 360, -45)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.9525, 4.572), 0.1905, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.9525, 0.762), 0.1905, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3.175
        extrude(amount=3.175)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 9.4820912297, perimeter: 13.7649514222
            with BuildLine():
                Line((0.635, 0.1025242889), (0.635, 5.08))
                Line((0.635, 0.1025242889), (2.54, 0.1025242889))
                Line((2.54, 5.08), (2.54, 0.1025242889))
                Line((0.635, 5.08), (2.54, 5.08))
            make_face()
        # OneSide extrude, distance=-1.905
        extrude(amount=-1.905, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0.1025242889, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.6237655739, perimeter: 7.6144782928
            with BuildLine():
                Line((0, 2.54), (-1.9022391464, 2.54))
                Line((-1.9022391464, 2.54), (-1.9022391464, 0.635))
                Line((-1.9022391464, 0.635), (0, 0.635))
                Line((0, 0.635), (0, 2.54))
            make_face()
        # OneSide extrude, distance=-0.381
        extrude(amount=-0.381, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical fastener or pin with a rounded head at the top and a flat base at the bottom, featuring a uniform tubular shaft with slight tapered ends.
def model_22106_db85f777_0079():
    """Model: 0.15inx1in pin v2 (10)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1140091828, perimeter: 1.196946801
            Circle(0.1905)
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.54, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0886738218, perimeter: 2.79287592
            with BuildLine():
                CenterArc((0, 0), 0.2540000081, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1905, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1140091828, perimeter: 1.196946801
            Circle(0.1905)
        # OneSide extrude, distance=0.127
        extrude(amount=0.127, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0886738218, perimeter: 2.79287592
            with BuildLine():
                CenterArc((0, 0), 0.2540000081, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1905, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1140091828, perimeter: 1.196946801
            Circle(0.1905)
        # OneSide extrude, distance=0.127
        extrude(amount=0.127, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical fastener or insert with a flat base and a mushroom-shaped or flanged head on top, featuring a textured surface pattern on the upper portion.
def model_22106_db85f777_0103():
    """Model: ShortPin v1 (8)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1140091828, perimeter: 1.196946801
            Circle(0.1905)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.635, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1140091828, perimeter: 1.196946801
            Circle(0.1905)
        # OneSide extrude, distance=-0.0508
        extrude(amount=-0.0508, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.635, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1312372371, perimeter: 2.9524687758
            with BuildLine():
                CenterArc((0, 0), 0.2794, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1905, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1140091828, perimeter: 1.196946801
            Circle(0.1905)
        # OneSide extrude, distance=-0.0508
        extrude(amount=-0.0508, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical suppressor or silencer with a tapered front end, featuring a smooth tubular body with internal baffles visible at the muzzle end and knurled or textured grip surfaces along its length.
def model_22198_327974c6_0005():
    """Model: Valve Linkage Rod D6-L46 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=4.6
        extrude(amount=4.6)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 9 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 4.6), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.015706104, perimeter: 0.5790786571
            with BuildLine():
                Line((-0.1990228965, -0.2244769179), (-0.1990228965, -0.0000021698))
                Line((-0.1990228965, -0.0000021698), (-0.3, -0.0000021698))
                CenterArc((0, 0), 0.3, -179.9995855921, 48.4391517647)
            make_face()
            # Profile area: 0.0157065422, perimeter: 0.5790873365
            with BuildLine():
                Line((-0.1990228965, -0.0000021698), (-0.3, -0.0000021698))
                Line((-0.1990228965, 0.2244769179), (-0.1990228965, -0.0000021698))
                CenterArc((0, 0), 0.3, 131.5604338274, 48.4399805805)
            make_face()
        # OneSide extrude, distance=-0.6
        extrude(amount=-0.6, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0309748208, perimeter: 0.9518547978
            with BuildLine():
                CenterArc((0, 0), 0.3, -48.1896851042, 96.3793702084)
                Line((0.2, -0.2236067977), (0.2, 0.2236067977))
            make_face()
        # OneSide extrude, distance=-0.6
        extrude(amount=-0.6, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical sleeve or bushing with a hollow center bore, featuring a ribbed or grooved exterior surface and what appears to be a flanged or stepped design at one end.
def model_22205_f48b96b3_0007():
    """Model: 09-Sliding Sleeve v9"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 166.253083228, perimeter: 79.1681348705
            with BuildLine():
                CenterArc((0, 0), 8.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 4.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=6.1
        extrude(amount=6.1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 6.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 43.1026512073, perimeter: 61.5752160104
            with BuildLine():
                CenterArc((0, 0), 5.6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 4.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3.6
        extrude(amount=3.6, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 9.7, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 55.4176944093, perimeter: 79.1681348705
            with BuildLine():
                CenterArc((0, 0), 7, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 5.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 43.1026512073, perimeter: 61.5752160104
            with BuildLine():
                CenterArc((0, 0), 5.6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 4.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.8
        extrude(amount=1.8, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical rod or tube with a uniform circular cross-section, tapered slightly at both ends, rendered in dark gray with 3D shading to show depth.
def model_22205_f48b96b3_0013():
    """Model: Shaft With Key v6"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 55.1027807076, perimeter: 27.1499819386
            with BuildLine():
                Line((-0.4, 4.1809089921), (-0.4, 3.8))
                CenterArc((0, 0), 4.2, 95.4650237999, 349.0699524002)
                Line((0.4, 3.8), (0.4, 4.1809089921))
                Line((-0.4, 3.8), (0.4, 3.8))
            make_face()
        # OneSide extrude, distance=9
        extrude(amount=9)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 55.4797908554, perimeter: 26.4041590189
            Circle(4.202352426)
        # OneSide extrude, distance=-40
        extrude(amount=-40, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 9, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1602550638, perimeter: 2.0044721923
            with BuildLine():
                Line((-0.4, -4.1809089921), (-0.4, -3.9799497484))
                CenterArc((0, 0), 4.2, -95.4650237999, 10.9300475998)
                Line((0.4, -3.9799497484), (0.4, -4.1809089921))
                CenterArc((0, 0), 4, -95.7391704773, 11.4783409545)
            make_face()
            # Profile area: 4.9919568881, perimeter: 50.3214843012
            with BuildLine():
                CenterArc((0, 0), 4, -84.2608295227, 348.5216590455)
                Line((0.4, -3.9799497484), (0.4, -4.1809089921))
                CenterArc((0, 0), 4.2, -84.5349762001, 349.0699524002)
                Line((-0.4, -4.1809089921), (-0.4, -3.9799497484))
            make_face()
            # Profile area: 0.154658638, perimeter: 1.9612388661
            with BuildLine():
                Line((-0.4, -3.9799497484), (-0.4, -3.8))
                CenterArc((0, 0), 4, -95.7391704773, 11.4783409545)
                Line((0.4, -3.8), (0.4, -3.9799497484))
                Line((-0.4, -3.8), (0.4, -3.8))
            make_face()
            # Profile area: 50.1108238195, perimeter: 25.4913013563
            with BuildLine():
                Line((-0.4, -3.8), (0.4, -3.8))
                Line((0.4, -3.8), (0.4, -3.9799497484))
                CenterArc((0, 0), 4, -84.2608295227, 348.5216590455)
                Line((-0.4, -3.9799497484), (-0.4, -3.8))
            make_face()
        # OneSide extrude, distance=40
        extrude(amount=40, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical capacitor or similar electronic component with a rounded dome top, a cylindrical body, and textured surface detailing including what appears to be label markings and ventilation slots or fins along its length.
def model_22211_b1ee53f0_0002():
    """Model: Ball Bearings v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.7567475535, perimeter: 8.4823001647
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.35, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3.8
        extrude(amount=3.8)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3.8), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.6022122533, perimeter: 10.6814150222
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.7, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.29
        extrude(amount=-0.29, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude4 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.5526520853, perimeter: 8.6717079252
            with BuildLine():
                CenterArc((4.2423, -1.75), 4.0277, 153.462943558, 52.2899757497)
                Line((1.3500000201, -3.5), (0.614646862, -3.5))
                Line((1.3500000201, 0.0494818087), (1.3500000201, -3.5))
                Line((0.6389359454, 0.0494818087), (1.3500000201, 0.0494818087))
            make_face()
        # TwoSides extrude (symmetric), distance=0.1
        extrude(amount=0.1, both=True, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical fastener or lug bolt featuring a long shaft with a hexagonal or knurled head at the base, designed for threaded connection or assembly purposes.
def model_22276_69c5036b_0004():
    """Model: Component21"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.9103910692, perimeter: 6.0475658582
            Circle(0.9625)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.2271846303, perimeter: 3.926990817
            Circle(0.625)
        # OneSide extrude, distance=5.4
        extrude(amount=5.4, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 28 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2771281375, perimeter: 2.4000000358
            with BuildLine():
                Line((0, 0), (0.400000006, -0.6928203334))
                Line((-0.400000006, -0.6928203334), (0, 0))
                Line((-0.400000006, -0.6928203334), (0.400000006, -0.6928203334))
            make_face()
            # Profile area: 0.2769095855, perimeter: 2.3990546084
            with BuildLine():
                Line((0.400000006, -0.6928203334), (0.7999992674, -0.0010914703))
                Line((0, 0), (0.7999992674, -0.0010914703))
                Line((0, 0), (0.400000006, -0.6928203334))
            make_face()
            # Profile area: 0.276950633, perimeter: 2.3992320331
            with BuildLine():
                Line((-0.8000000119, 0), (0, 0))
                Line((0, 0), (-0.4007676399, 0.6923765723))
                Line((-0.8000000119, 0), (-0.4007676399, 0.6923765723))
            make_face()
            # Profile area: 0.2773462906, perimeter: 2.4009455985
            with BuildLine():
                Line((0, 0), (0.4001778621, 0.6927176176))
                Line((0.4001778621, 0.6927176176), (-0.4007676399, 0.6923765723))
                Line((0, 0), (-0.4007676399, 0.6923765723))
            make_face()
            # Profile area: 0.2773051844, perimeter: 2.400767285
            with BuildLine():
                Line((0.7999992674, -0.0010914703), (0.4001778621, 0.6927176176))
                Line((0, 0), (0.4001778621, 0.6927176176))
                Line((0, 0), (0.7999992674, -0.0010914703))
            make_face()
            # Profile area: 0.2771281375, perimeter: 2.4000000358
            with BuildLine():
                Line((-0.400000006, -0.6928203334), (0, 0))
                Line((-0.8000000119, 0), (0, 0))
                Line((-0.8000000119, 0), (-0.400000006, -0.6928203334))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a TIE Fighter-inspired spacecraft or satellite component featuring a hexagonal central body with two large flat rectangular solar panel wings extending from opposite sides, connected by structural struts and bracing elements.
def model_22276_69c5036b_0011():
    """Model: Component6"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4.84, perimeter: 8.8
            with BuildLine():
                Line((0, -2.2), (0, 0))
                Line((0, 0), (-2.2, 0))
                Line((-2.2, 0), (-2.2, -2.2))
                Line((-2.2, -2.2), (0, -2.2))
            make_face()
        # OneSide extrude, distance=2.2
        extrude(amount=2.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -2.2, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 1.7, perimeter: 7.8
            with BuildLine():
                Line((1.35, 5.6), (0.85, 5.6))
                Line((0.85, 5.6), (0.85, 2.2))
                Line((0.85, 2.2), (1.35, 2.2))
                Line((1.35, 2.2), (1.35, 5.6))
            make_face()
        # OneSide extrude, distance=-2.2
        extrude(amount=-2.2, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.5393804003, perimeter: 4.398229715
            with Locations((-1.1, 1.1)):
                Circle(0.7)
        # OneSide extrude, distance=-3.3
        extrude(amount=-3.3, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a tripod or stand base featuring two long, tapered legs connected by a flat rectangular top plate, with triangular bracing elements between the legs for structural support.
def model_22305_5b45cdb3_0012():
    """Model: 34-FIRE-BOX-BRACKET v4 (3)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 9 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0838214286, perimeter: 3.845718691
            with BuildLine():
                Line((1.05, 1.45), (1, 1.45))
                Line((1, 1.45), (0.24, 0.05))
                Line((0.24, 0.05), (0, 0.05))
                Line((0, 0.05), (0, 0))
                Line((0, 0), (0.2628571429, 0))
                Line((0.2628571429, 0), (1.05, 1.45))
            make_face()
            # Profile area: 0.02, perimeter: 0.9
            with BuildLine():
                Line((1.05, 1.45), (1.05, 1.85))
                Line((1.05, 1.85), (1, 1.85))
                Line((1, 1.85), (1, 1.45))
                Line((1.05, 1.45), (1, 1.45))
            make_face()
        # OneSide extrude, distance=0.9
        extrude(amount=0.9)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.9, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))) as sk:
            # Profile area: 0.0838214286, perimeter: 3.845718691
            with BuildLine():
                Line((0.24, 0.05), (0, 0.05))
                Line((0, 0.05), (0, 0))
                Line((0, 0), (0.2628571429, 0))
                Line((0.2628571429, 0), (1.05, 1.45))
                Line((1.05, 1.45), (1, 1.45))
                Line((1, 1.45), (0.24, 0.05))
            make_face()
        # TwoSides extrude, along=0.2, against=-1.1
        extrude(amount=0.2, mode=Mode.ADD)
        extrude(sk.sketch, amount=-1.1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on XY construction plane
        # Sketch has 16 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2567490056, perimeter: 3.2140336564
            with BuildLine():
                Line((1.1, 1.45), (1.1, 0.05))
                Line((0.7332157063, 1.45), (1.1, 1.45))
                Line((0.7332157063, 1.45), (1.1, 0.05))
            make_face()
            # Profile area: 0.2567490056, perimeter: 3.2140336564
            with BuildLine():
                Line((0.1667842937, 1.45), (-0.2, 1.45))
                Line((-0.2, 0.05), (-0.2, 1.45))
                Line((0.1667842937, 1.45), (-0.2, 0.05))
            make_face()
            # Profile area: 0.4346602629, perimeter: 3.1116547819
            with BuildLine():
                CenterArc((0.45, 1.15), 0.05, 14.6809224754, 150.6381329054)
                Line((0.4016323953, 1.1626718119), (0.1101248635, 0.05))
                Line((0.1101248635, 0.05), (0.7898751365, 0.05))
                Line((0.4983676096, 1.1626717932), (0.7898751365, 0.05))
            make_face()
            # Profile area: 0.0346424856, perimeter: 1.4890743788
            with BuildLine():
                Line((0.1101248635, 0.05), (0.7898751365, 0.05))
                Line((0.1101248635, 0.05), (0.0970254244, 0))
                Line((0.0970254244, 0), (0.8029745756, 0))
                Line((0.7898751365, 0.05), (0.8029745756, 0))
            make_face()
        # OneSide extrude, distance=-10
        extrude(amount=-10, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a simplified 3D CAD model of an open-top utility vehicle or jeep featuring a boxy rectangular body with an open cabin area, a windshield frame, two large wheels, and a flat cargo bed extending toward the rear.
def model_22305_5b45cdb3_0014():
    """Model: 06-FRONT-BUFFER-PLATE v1 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 13 constraints, 40 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 5.3388678028, perimeter: 17.0600740194
            with BuildLine():
                Line((6, 0), (6, 0.7))
                Line((6, 0.7), (0, 0.7))
                Line((0, 0.7), (0, 0))
                Line((0, 0), (0.4754033308, 0))
                CenterArc((0.4754033308, -0.2), 0.2, 14.4775121859, 75.5224878141)
                CenterArc((1.25, 0), 0.6, -165.5224878141, 151.0449756281)
                CenterArc((2.0245966692, -0.2), 0.2, 90, 75.5224878141)
                Line((2.0245966692, 0), (3.9496094703, 0))
                CenterArc((3.9496094703, -0.2), 0.2, 14.0296654013, 75.9703345987)
                CenterArc((4.75, 0), 0.625, -165.9703345987, 151.9406691974)
                CenterArc((5.5503905297, -0.2), 0.2, 90, 75.9703345987)
                Line((5.5503905297, 0), (6, 0))
            make_face()
            with BuildLine():
                CenterArc((0.45, 0.6), 0.05, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.85, 0.6), 0.05, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.45, 0.3), 0.05, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.85, 0.3), 0.05, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.15, 0.6), 0.05, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.55, 0.6), 0.05, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.55, 0.3), 0.05, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.15, 0.3), 0.05, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.7, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3842920367, perimeter: 3.4283185307
            with BuildLine():
                Line((-3.5, 0), (-2.5, 0))
                Line((-3.5, 0), (-3.5, -0.4))
                Line((-3.5, -0.4), (-2.5, -0.4))
                Line((-2.5, -0.4), (-2.5, 0))
            make_face()
            with BuildLine():
                CenterArc((-2.7, -0.2), 0.05, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-3.3, -0.2), 0.05, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.05
        extrude(amount=-0.05, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.35, perimeter: 2.7
            with BuildLine():
                Line((-3.5, 0.3), (-3.5, 0.65))
                Line((-2.5, 0.3), (-3.5, 0.3))
                Line((-2.5, 0.65), (-2.5, 0.3))
                Line((-3.5, 0.65), (-2.5, 0.65))
            make_face()
        # OneSide extrude, distance=0.05
        extrude(amount=0.05, mode=Mode.ADD)
    return part.part


# Description: This is a parallel-jaw gripper or robotic end-effector with two opposing rectangular finger plates connected by a central shaft, featuring circular end flanges and linear slot details along the finger surfaces for gripping functionality.
def model_22305_5b45cdb3_0016():
    """Model: 14-LEAF-SPRING-LINK v1 (5)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 9 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0235619449, perimeter: 0.9424777961
            with BuildLine():
                CenterArc((0, 0), 0.1, 60, 60)
                CenterArc((0, 0), 0.1, 120, 300)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.05, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0235619449, perimeter: 0.9424777961
            with BuildLine():
                CenterArc((0, 0.4), 0.1, -120, 60)
                CenterArc((0, 0.4), 0.1, -60, 300)
            make_face()
            with BuildLine():
                CenterArc((0, 0.4), 0.05, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0208677705, perimeter: 0.6630293487
            with BuildLine():
                Line((-0.05, 0.3133974596), (-0.05, 0.0866025404))
                CenterArc((0, 0), 0.1, 60, 60)
                Line((0.05, 0.0866025404), (0.05, 0.3133974596))
                CenterArc((0, 0.4), 0.1, -120, 60)
            make_face()
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            Circle(0.05)
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((0, 0.4)):
                Circle(0.05)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.4, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0208677705, perimeter: 0.6630293487
            with BuildLine():
                CenterArc((0, 0), 0.1, 60, 60)
                Line((0.05, 0.3133974596), (0.05, 0.0866025404))
                CenterArc((0, 0.4), 0.1, -120, 60)
                Line((-0.05, 0.0866025404), (-0.05, 0.3133974596))
            make_face()
            # Profile area: 0.0235619449, perimeter: 0.9424777961
            with BuildLine():
                CenterArc((0, 0.4), 0.1, -60, 300)
                CenterArc((0, 0.4), 0.1, -120, 60)
            make_face()
            with BuildLine():
                CenterArc((0, 0.4), 0.05, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0235619449, perimeter: 0.9424777961
            with BuildLine():
                CenterArc((0, 0), 0.1, 120, 300)
                CenterArc((0, 0), 0.1, 60, 60)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.05, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.05
        extrude(amount=-0.05, mode=Mode.ADD)
    return part.part


# Description: This is a flashlight or torch with a cylindrical body, a textured grip section in the middle, and a ribbed circular lens head at the top, featuring a knurled bezel ring for adjusting focus or intensity.
def model_22320_e9f9e6ae_0005():
    """Model: Eye Bolt v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # OneSide extrude, distance=4.5
        extrude(amount=4.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 4.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2146018366, perimeter: 3.5707963268
            with BuildLine():
                CenterArc((0, 0), 1, -180, 90)
                Line((-1, -1), (-1, 0))
                Line((0, -1), (-1, -1))
            make_face()
            # Profile area: 0.2146018366, perimeter: 3.5707963268
            with BuildLine():
                Line((1, 1), (1, 0))
                Line((0, 1), (1, 1))
                CenterArc((0, 0), 1, 0, 90)
            make_face()
            # Profile area: 0.2146018366, perimeter: 3.5707963268
            with BuildLine():
                CenterArc((0, 0), 1, 90, 90)
                Line((-1, 1), (0, 1))
                Line((-1, 0), (-1, 1))
            make_face()
            # Profile area: 0.2146018366, perimeter: 3.5707963268
            with BuildLine():
                Line((1, -1), (0, -1))
                Line((1, 0), (1, -1))
                CenterArc((0, 0), 1, -90, 90)
            make_face()
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with BuildLine():
                CenterArc((0, 0), 1, -90, 90)
                CenterArc((0, 0), 1, 0, 90)
                CenterArc((0, 0), 1, 90, 90)
                CenterArc((0, 0), 1, -180, 90)
            make_face()
        # OneSide extrude, distance=1.8
        extrude(amount=1.8, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 6.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.5663706144, perimeter: 20.5663706144
            with BuildLine():
                CenterArc((0, 0), 2, 0, 360)
            make_face()
            with BuildLine():
                Line((1, 1), (-1, 1))
                Line((1, -1), (1, 1))
                Line((-1, -1), (1, -1))
                Line((-1, 1), (-1, -1))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 4, perimeter: 8
            with BuildLine():
                Line((-1, 1), (-1, -1))
                Line((-1, -1), (1, -1))
                Line((1, -1), (1, 1))
                Line((1, 1), (-1, 1))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical container or vessel with a rounded bottom, vertical ribbed sidewalls, and a flat top with an integrated handle and mesh or perforated lid section.
def model_22320_e9f9e6ae_0006():
    """Model: Valve v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 13 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.2606980763, perimeter: 20.1593416297
            with BuildLine():
                Line((0.2598076211, -0.45), (3.1682013825, -0.45))
                CenterArc((0, 0), 3.2, -8.0840139071, 16.1680278142)
                Line((0.2598076211, 0.45), (3.1682013825, 0.45))
                Line((0.2598076211, 0.45), (-1.1943892595, 2.9687428815))
                CenterArc((0, 0), 3.2, 111.9159860929, 16.1680278142)
                Line((-0.5196152423, 0), (-1.9738121229, 2.5187428815))
                Line((-0.5196152423, 0), (-1.9738121229, -2.5187428815))
                CenterArc((0, 0), 3.2, -128.0840139071, 16.1680278142)
                Line((0.2598076211, -0.45), (-1.1943892595, -2.9687428815))
            make_face()
        # OneSide extrude, distance=6
        extrude(amount=6)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 5.3322809241, perimeter: 9.5555037112
            with BuildLine():
                Line((2.6622359024, 0.45), (0.2598076211, 0.45))
                CenterArc((0, 0), 2.7, 9.5940682269, 100.8118635463)
                Line((0.2598076211, 0.45), (-0.9414065195, 2.5305639223))
            make_face()
            # Profile area: 5.3322809241, perimeter: 9.5555037112
            with BuildLine():
                CenterArc((0, 0), 2.7, -110.4059317731, 100.8118635463)
                Line((0.2598076211, -0.45), (2.6622359024, -0.45))
                Line((-0.9414065195, -2.5305639223), (0.2598076211, -0.45))
            make_face()
            # Profile area: 5.3322809241, perimeter: 9.5555037112
            with BuildLine():
                CenterArc((0, 0), 2.7, 129.5940682269, 100.8118635463)
                Line((-0.5196152423, 0), (-1.7208293829, -2.0805639223))
                Line((-1.7208293829, 2.0805639223), (-0.5196152423, 0))
            make_face()
        # OneSide extrude, distance=-5.4
        extrude(amount=-5.4, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 16 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.4517768014, perimeter: 2.8191436085
            with BuildLine():
                CenterArc((0, 0), 3.2, -8.0840139071, 16.1680278142)
                Line((3.1682013825, 0.45), (2.6622359024, 0.45))
                CenterArc((0, 0), 2.7, -9.5940682269, 19.1881364537)
                Line((3.1682013825, -0.45), (2.6622359024, -0.45))
            make_face()
            # Profile area: 0.4517768014, perimeter: 2.8191436085
            with BuildLine():
                CenterArc((0, 0), 2.7, -129.5940682269, 19.1881364537)
                Line((-1.9738121229, -2.5187428815), (-1.7208293829, -2.0805639223))
                CenterArc((0, 0), 3.2, -128.0840139071, 16.1680278142)
                Line((-1.1943892595, -2.9687428815), (-0.9414065195, -2.5305639223))
            make_face()
            # Profile area: 0.4517768014, perimeter: 2.8191436085
            with BuildLine():
                CenterArc((0, 0), 2.7, 110.4059317731, 19.1881364537)
                Line((-1.1943892595, 2.9687428815), (-0.9414065195, 2.5305639223))
                CenterArc((0, 0), 3.2, 111.9159860929, 16.1680278142)
                Line((-1.9738121229, 2.5187428815), (-1.7208293829, 2.0805639223))
            make_face()
        # OneSide extrude, distance=-5.4
        extrude(amount=-5.4, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a mesh or perforated funnel-shaped component with a wide, flat-bottomed circular top opening and a tapered cylindrical stem below, featuring ventilation holes or mesh panels throughout for filtering or airflow purposes.
def model_22322_f04772b3_0003():
    """Model: Gland v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 20 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.6219517816, perimeter: 16.3092057201
            with BuildLine():
                CenterArc((3.5, 0), 1.1, 71.6823015888, 216.6353968224)
                Line((3.8457142857, 1.0442612856), (0.6914285714, 2.0885225712))
                CenterArc((0, 0), 2.2, -71.6823015888, 143.3646031776)
                Line((3.8457142857, -1.0442612856), (0.6914285714, -2.0885225712))
            make_face()
            # Profile area: 3.8013271108, perimeter: 6.9115038379
            with BuildLine():
                CenterArc((3.5, 0), 1.1, 71.6823015888, 216.6353968224)
                CenterArc((3.5, 0), 1.1, -71.6823015888, 143.3646031776)
            make_face()
            # Profile area: 15.2053084434, perimeter: 13.8230076758
            with BuildLine():
                CenterArc((0, 0), 2.2, 71.6823015888, 36.6353968795)
                CenterArc((0, 0), 2.2, 108.3176984683, 143.3646023193)
                CenterArc((0, 0), 2.2, -108.3176992125, 36.6353976236)
                CenterArc((0, 0), 2.2, -71.6823015888, 143.3646031776)
            make_face()
            # Profile area: 2.6219517772, perimeter: 16.3088647639
            with BuildLine():
                CenterArc((0, 0), 2.2, 108.3176984683, 143.3646023193)
                Line((-3.8456332818, 1.0442880994), (-0.6914285735, 2.0885225706))
                CenterArc((-3.5, 0), 1.1, -108.3132648288, 216.6265188328)
                Line((-3.8456334801, -1.0442880372), (-0.6914286006, -2.0885225616))
            make_face()
            # Profile area: 3.8013271108, perimeter: 6.9115038379
            with BuildLine():
                CenterArc((-3.5, 0), 1.1, -108.3132648288, 216.6265188328)
                CenterArc((-3.5, 0), 1.1, 108.313254004, 143.3734811672)
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch7 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.3411494795, perimeter: 11.9380520836
            Circle(1.9)
        # OneSide extrude, distance=-2.6
        extrude(amount=-2.6, mode=Mode.ADD)
    return part.part


MODELS = {
    "model_144912_34c55160_0000": {"func": model_144912_34c55160_0000, "volume": 2.3770748172, "area": 12.3458535099},
    "model_144917_3c8ef27d_0000": {"func": model_144917_3c8ef27d_0000, "volume": 41.8273766776, "area": 321.5537072787},
    "model_145115_4a4d447b_0000": {"func": model_145115_4a4d447b_0000, "volume": 150.3655937129, "area": 278.3300837939},
    "model_145236_c9905a23_0000": {"func": model_145236_c9905a23_0000, "volume": 581.7425511615, "area": 932.7633095421},
    "model_145418_53431480_0000": {"func": model_145418_53431480_0000, "volume": 230.4971141962, "area": 390.1356267931},
    "model_145540_a4f54d5f_0009": {"func": model_145540_a4f54d5f_0009, "volume": 3014.0499800618, "area": 2307.7880487458},
    "model_146191_ecf68f7a_0003": {"func": model_146191_ecf68f7a_0003, "volume": 0.1820553022, "area": 2.7206192935},
    "model_146317_26f65f2a_0000": {"func": model_146317_26f65f2a_0000, "volume": 11.2481585994, "area": 114.1026457022},
    "model_146317_3eafabf0_0000": {"func": model_146317_3eafabf0_0000, "volume": 38.1290771691, "area": 210.4590733941},
    "model_146317_3eafabf0_0008": {"func": model_146317_3eafabf0_0008, "volume": 23.0404141998, "area": 170.4895333612},
    "model_146317_5c5baff8_0000": {"func": model_146317_5c5baff8_0000, "volume": 23.548269878, "area": 194.5127869931},
    "model_146317_7de88751_0000": {"func": model_146317_7de88751_0000, "volume": 38.1290771691, "area": 210.4590733941},
    "model_146545_f266050f_0002": {"func": model_146545_f266050f_0002, "volume": 43.5895980686, "area": 185.3539665618},
    "model_146617_2c247f85_0017": {"func": model_146617_2c247f85_0017, "volume": 113.8041938763, "area": 250.6990937565},
    "model_146617_2c247f85_0023": {"func": model_146617_2c247f85_0023, "volume": 2.0304075415, "area": 12.4769416405},
    "model_146868_52dcd6c2_0000": {"func": model_146868_52dcd6c2_0000, "volume": 60.8178455658, "area": 466.8687855777},
    "model_147133_92c04b84_0006": {"func": model_147133_92c04b84_0006, "volume": 8.1537431155, "area": 40.1714558961},
    "model_147428_1502e954_0000": {"func": model_147428_1502e954_0000, "volume": 5.5137235702, "area": 26.9603150046},
    "model_20442_00c8a1db_0000": {"func": model_20442_00c8a1db_0000, "volume": 32.8990807548, "area": 68.1356924048},
    "model_21234_8b71bd47_0000": {"func": model_21234_8b71bd47_0000, "volume": 167.2632743437, "area": 279.0317},
    "model_21235_01764fc7_0014": {"func": model_21235_01764fc7_0014, "volume": 1102.3945403915, "area": 1224.1499215707},
    "model_21235_01764fc7_0029": {"func": model_21235_01764fc7_0029, "volume": 89.7202269288, "area": 224.00859501},
    "model_21236_b696e901_0041": {"func": model_21236_b696e901_0041, "volume": 0.0580765433, "area": 1.1707078742},
    "model_21237_7887a24b_0011": {"func": model_21237_7887a24b_0011, "volume": 0.4297763236, "area": 15.1421121637},
    "model_21242_6c2af7c2_0005": {"func": model_21242_6c2af7c2_0005, "volume": 8.7990901558, "area": 45.5349253201},
    "model_21246_c66f2b12_0000": {"func": model_21246_c66f2b12_0000, "volume": 0.4741575688, "area": 6.0916226902},
    "model_21246_c66f2b12_0009": {"func": model_21246_c66f2b12_0009, "volume": 0.6983451332, "area": 18.9900265543},
    "model_21338_bd0eb54a_0000": {"func": model_21338_bd0eb54a_0000, "volume": 3.2561119899, "area": 42.2092460724},
    "model_21385_601444ba_0014": {"func": model_21385_601444ba_0014, "volume": 0.9069579701, "area": 9.9468254895},
    "model_21564_fa5b2db7_0000": {"func": model_21564_fa5b2db7_0000, "volume": 0.2998731883, "area": 4.7771404353},
    "model_21599_80057f94_0000": {"func": model_21599_80057f94_0000, "volume": 0.0007499999, "area": 0.1899999797},
    "model_21647_6b6cca6f_0001": {"func": model_21647_6b6cca6f_0001, "volume": 1328.8724867181, "area": 1722.0640130652},
    "model_21695_1f33863f_0002": {"func": model_21695_1f33863f_0002, "volume": 0.0387394918, "area": 1.5261522563},
    "model_21697_06656699_0005": {"func": model_21697_06656699_0005, "volume": 8.5930413314, "area": 36.0581975562},
    "model_21702_3390d14a_0004": {"func": model_21702_3390d14a_0004, "volume": 41.7915493788, "area": 85.6544706383},
    "model_21702_3390d14a_0005": {"func": model_21702_3390d14a_0005, "volume": 1.722129152, "area": 9.1178443585},
    "model_21710_0b9db742_0006": {"func": model_21710_0b9db742_0006, "volume": 12.6683079793, "area": 69.1555853109},
    "model_21734_7cf58bd0_0001": {"func": model_21734_7cf58bd0_0001, "volume": 3.4643205993, "area": 20.8452923105},
    "model_21773_01f6bc23_0011": {"func": model_21773_01f6bc23_0011, "volume": 8.1447845521, "area": 35.3315406972},
    "model_21803_8a36dcda_0009": {"func": model_21803_8a36dcda_0009, "volume": 1.2533639959, "area": 29.0374722991},
    "model_21803_8a36dcda_0032": {"func": model_21803_8a36dcda_0032, "volume": 15.7142464533, "area": 65.8477820192},
    "model_21816_3891a442_0001": {"func": model_21816_3891a442_0001, "volume": 100, "area": 240},
    "model_21822_7d3db422_0002": {"func": model_21822_7d3db422_0002, "volume": 6.6383570633, "area": 35.6658769838},
    "model_21822_7d3db422_0003": {"func": model_21822_7d3db422_0003, "volume": 6.8172560583, "area": 32.7982273035},
    "model_21822_7d3db422_0008": {"func": model_21822_7d3db422_0008, "volume": 10.1928596871, "area": 39.9293135624},
    "model_21822_7d3db422_0012": {"func": model_21822_7d3db422_0012, "volume": 5.221419609, "area": 42.0427642388},
    "model_21822_7d3db422_0013": {"func": model_21822_7d3db422_0013, "volume": 0.4665265091, "area": 4.2097341558},
    "model_21822_7d3db422_0022": {"func": model_21822_7d3db422_0022, "volume": 0.0691150401, "area": 1.2409291052},
    "model_21822_7d3db422_0031": {"func": model_21822_7d3db422_0031, "volume": 0.1213519915, "area": 2.1485839227},
    "model_21822_7d3db422_0032": {"func": model_21822_7d3db422_0032, "volume": 0.2221391785, "area": 3.1769510792},
    "model_21822_7d3db422_0035": {"func": model_21822_7d3db422_0035, "volume": 0.4473435562, "area": 5.4660659381},
    "model_21822_7d3db422_0040": {"func": model_21822_7d3db422_0040, "volume": 0.0179033352, "area": 0.6371627852},
    "model_21822_7d3db422_0041": {"func": model_21822_7d3db422_0041, "volume": 0.2798646594, "area": 3.7260882128},
    "model_21822_7d3db422_0047": {"func": model_21822_7d3db422_0047, "volume": 0.0956543748, "area": 1.7807963352},
    "model_21847_b2de7eb8_0018": {"func": model_21847_b2de7eb8_0018, "volume": 0.095044222, "area": 1.804466304},
    "model_21864_4c028c8c_0000": {"func": model_21864_4c028c8c_0000, "volume": 3012.1590362619, "area": 3026.5475306153},
    "model_21893_0500d043_0032": {"func": model_21893_0500d043_0032, "volume": 2.3425332208, "area": 12.5360898025},
    "model_21893_0500d043_0046": {"func": model_21893_0500d043_0046, "volume": 0.0711328256, "area": 1.3060972437},
    "model_21899_d55d6c08_0013": {"func": model_21899_d55d6c08_0013, "volume": 1.1637604561, "area": 9.8126810787},
    "model_21899_d55d6c08_0020": {"func": model_21899_d55d6c08_0020, "volume": 3.2298442569, "area": 18.6167313737},
    "model_21899_d55d6c08_0026": {"func": model_21899_d55d6c08_0026, "volume": 8.1529235917, "area": 33.0839005452},
    "model_21899_d55d6c08_0028": {"func": model_21899_d55d6c08_0028, "volume": 13.5923750749, "area": 48.2165203289},
    "model_21941_1a683ec2_0023": {"func": model_21941_1a683ec2_0023, "volume": 507.8453608159, "area": 633.2551818647},
    "model_22016_c1658896_0004": {"func": model_22016_c1658896_0004, "volume": 175.1518509824, "area": 524.4956618821},
    "model_22017_6d3be48d_0006": {"func": model_22017_6d3be48d_0006, "volume": 41985.163109202, "area": 9278.5760615352},
    "model_22019_0ef07114_0003": {"func": model_22019_0ef07114_0003, "volume": 0.5666008162, "area": 23.384093904},
    "model_22025_b77024b9_0015": {"func": model_22025_b77024b9_0015, "volume": 12.1246815157, "area": 37.1606279541},
    "model_22106_db85f777_0052": {"func": model_22106_db85f777_0052, "volume": 58.5131995395, "area": 226.4008384213},
    "model_22106_db85f777_0079": {"func": model_22106_db85f777_0079, "volume": 0.3410648075, "area": 4.0283245235},
    "model_22106_db85f777_0103": {"func": model_22106_db85f777_0103, "volume": 0.0790626827, "area": 1.2789296772},
    "model_22198_327974c6_0005": {"func": model_22198_327974c6_0005, "volume": 1.2631868784, "area": 9.1668433685},
    "model_22205_f48b96b3_0007": {"func": model_22205_f48b96b3_0007, "volume": 1346.6499741466, "area": 1274.6069714145},
    "model_22205_f48b96b3_0013": {"func": model_22205_f48b96b3_0013, "volume": 4931.8244369573, "area": 2467.6807389247},
    "model_22211_b1ee53f0_0002": {"func": model_22211_b1ee53f0_0002, "volume": 9.5893475751, "area": 40.6309319237},
    "model_22276_69c5036b_0004": {"func": model_22276_69c5036b_0004, "volume": 9.7867126931, "area": 35.2436114707},
    "model_22276_69c5036b_0011": {"func": model_22276_69c5036b_0011, "volume": 11.0013631194, "area": 53.9973445725},
    "model_22305_5b45cdb3_0012": {"func": model_22305_5b45cdb3_0012, "volume": 0.0699867336, "area": 3.4981708932},
    "model_22305_5b45cdb3_0014": {"func": model_22305_5b45cdb3_0014, "volume": 2.172261723, "area": 18.3767652135},
    "model_22305_5b45cdb3_0016": {"func": model_22305_5b45cdb3_0016, "volume": 0.0130823513, "area": 0.6419568657},
    "model_22320_e9f9e6ae_0005": {"func": model_22320_e9f9e6ae_0005, "volume": 33.9035375555, "area": 80.3734457254},
    "model_22320_e9f9e6ae_0006": {"func": model_22320_e9f9e6ae_0006, "volume": 128.628355247, "area": 152.219528454},
    "model_22322_f04772b3_0003": {"func": model_22322_f04772b3_0003, "volume": 57.5388548573, "area": 108.7514681378},
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
