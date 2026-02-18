"""Batch 007 - passing/01_2ops
195 models bundled from Fusion360 Gallery reconstructions.
"""

from build123d import *
from build123d import Edge, BuildLine
from collections import Counter
from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
from OCP.Geom import Geom_BSplineCurve
from OCP.TColStd import TColStd_Array1OfReal, TColStd_Array1OfInteger
from OCP.TColgp import TColgp_Array1OfPnt
from OCP.gp import gp_Pnt


def model_21908_385686ec_0032():
    """Model: 01B v3 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2199999961, perimeter: 4.6000000387
            with BuildLine():
                Line((0, 0.7000000104), (0, 0))
                Line((0, 0), (1, 0))
                Line((1, 0), (1, 0.7000000104))
                Line((1, 0.7000000104), (0.9000000134, 0.7000000104))
                Line((0.9000000134, 0.7000000104), (0.9000000134, 0.1000000015))
                Line((0.9000000134, 0.1000000015), (0.1000000015, 0.1000000015))
                Line((0.1000000015, 0.1000000015), (0.1000000015, 0.7000000104))
                Line((0.1000000015, 0.7000000104), (0, 0.7000000104))
            make_face()
        # OneSide extrude, distance=7.4
        extrude(amount=7.4)
    return part.part


def model_21908_385686ec_0033():
    """Model: 04B v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.8282288682, perimeter: 12.225852666
            with BuildLine():
                CenterArc((2.25, 12.003872107), 12.2129212542, -100.6163075591, 21.2326151183)
                Line((4.5, 0), (4.5, 1.6))
                Line((4.5, 1.6), (0, 1.6))
                Line((0, 1.6), (0, 0))
            make_face()
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)
    return part.part


def model_21908_385686ec_0034():
    """Model: 14A v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.4569489622, perimeter: 4.492099423
            with BuildLine():
                Line((1, 0), (1, 0.200000003))
                Line((1, 0.200000003), (0.6, 0.2226568488))
                Line((0.6, 0.2226568488), (0.6, 0.6000000089))
                Line((0.6, 0.6000000089), (0.8000000119, 0.6000000089))
                Line((0.8000000119, 0.6000000089), (0.7700508999, 0.9000000134))
                Line((0.2334258293, 0.9000000134), (0.7700508999, 0.9000000134))
                Line((0.2034767173, 0.6000000089), (0.2334258293, 0.9000000134))
                Line((0.4034767293, 0.6000000089), (0.2034767173, 0.6000000089))
                Line((0.4034767293, 0.2226568488), (0.4034767293, 0.6000000089))
                Line((0.0034767293, 0.200000003), (0.4034767293, 0.2226568488))
                Line((0.0034767293, 0), (0.0034767293, 0.200000003))
                Line((0.0034767293, 0), (1, 0))
            make_face()
        # OneSide extrude, distance=15
        extrude(amount=15)
    return part.part


def model_21918_976c2754_0008():
    """Model: Base v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 20 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 72.51195175, perimeter: 47.2450209402
            with BuildLine():
                Line((0, 0), (0.9525, 0))
                Line((0.9525, 0), (3.175, 2.35585))
                Line((3.175, 2.35585), (9.525, 2.35585))
                Line((11.7475, 0), (9.525, 2.35585))
                Line((12.7, 0), (11.7475, 0))
                Line((12.7, 8.89), (12.7, 0))
                Line((11.7475, 8.89), (12.7, 8.89))
                Line((9.525, 6.53415), (11.7475, 8.89))
                Line((3.175, 6.53415), (9.525, 6.53415))
                Line((0.9525, 8.89), (3.175, 6.53415))
                Line((0, 8.89), (0.9525, 8.89))
                Line((0, 0), (0, 8.89))
            make_face()
        # OneSide extrude, distance=3.81
        extrude(amount=3.81)
    return part.part


def model_21918_976c2754_0014():
    """Model: Jack Screw v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            Circle(0.635)
        # OneSide extrude, distance=37.7825
        extrude(amount=37.7825)
    return part.part


def model_21940_6c2dac17_0000():
    """Model: Support Link Holder v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.4450878146, perimeter: 6.7399392915
            with BuildLine():
                CenterArc((0, 0), 1.1, 125.5317247796, 108.9365504408)
                Line((-0.6392690083, -0.895173243), (0.6392690083, -0.895173243))
                CenterArc((0, 0), 1.1, -54.4682752204, 108.9365504408)
                Line((-0.6392690083, 0.895173243), (0.6392690083, 0.895173243))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


def model_21941_1a683ec2_0000():
    """Model: ring v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 90.3207887907, perimeter: 72.2566310326
            with BuildLine():
                CenterArc((0, 0), 7, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 4.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.6
        extrude(amount=2.6)
    return part.part


def model_21941_1a683ec2_0001():
    """Model: buchse v1 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.9772398764, perimeter: 8.325220532
            with BuildLine():
                CenterArc((0, 0), 0.9, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.425, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.65
        extrude(amount=0.65)
    return part.part


def model_21941_1a683ec2_0007():
    """Model: scheibe v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 969.9058634382, perimeter: 130.847334022
            with BuildLine():
                CenterArc((0, 0), 17.825, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


def model_21941_1a683ec2_0008():
    """Model: ut1 v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 844.7747797715, perimeter: 195.1431692704
            with BuildLine():
                CenterArc((0, 0), 19.858, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 11.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.11
        extrude(amount=1.11)
    return part.part


def model_21941_1a683ec2_0018():
    """Model: schottblech v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 16 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 413.7745056735, perimeter: 90.3118428006
            with BuildLine():
                Line((0, 2.5), (0, -12.989))
                Line((0, -12.989), (3.5, -12.989))
                Line((3.5, -12.989), (7.5, -16.989))
                Line((7.5, -16.989), (7.5, -26.489))
                Line((7.5, -26.489), (19.5, -26.489))
                Line((19.5, -26.489), (21.5000003204, -24.5000003651))
                Line((21.5000003204, -24.5000003651), (21.5000003204, -17))
                Line((11.5, -0.85), (21.5000003204, -17))
                Line((11.5, 2.5), (11.5, -0.85))
                Line((0, 2.5), (11.5, 2.5))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)
    return part.part


def model_21941_1a683ec2_0021():
    """Model: pendelachse v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            Circle(2)
        # OneSide extrude, distance=27.8
        extrude(amount=27.8)
    return part.part


def model_21958_e48ddf4e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude6 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 178.0029193613, perimeter: 50.8579769604
            with BuildLine():
                Line((5.085797696, 7), (-5.085797696, 7))
                Line((-5.085797696, 7), (-8.2289935321, -2.6737620788))
                Line((-8.2289935321, -2.6737620788), (0, -8.6524758425))
                Line((0, -8.6524758425), (8.2289935321, -2.6737620788))
                Line((8.2289935321, -2.6737620788), (5.085797696, 7))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


def model_21979_29f59427_0003():
    """Model: 10-32 x 3 stud v1 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2026830046, perimeter: 1.595929119
            Circle(0.2540000081)
        # OneSide extrude, distance=7.62
        extrude(amount=7.62)
    return part.part


def model_22002_315afcfc_0008():
    """Model: Pin 0.5 length v1 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0791730436, perimeter: 0.9974556675
            Circle(0.15875)
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)
    return part.part


def model_22002_315afcfc_0010():
    """Model: Pin 0.75 length v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1781393481, perimeter: 1.4961835013
            Circle(0.238125)
        # OneSide extrude, distance=1.905
        extrude(amount=1.905)
    return part.part


def model_22011_0832eefe_0005():
    """Model: Upper Driveshaft v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=10.5
        extrude(amount=10.5)
    return part.part


def model_22011_0832eefe_0014():
    """Model: Lower Driveshaft v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=11.35
        extrude(amount=11.35)
    return part.part


def model_22011_0832eefe_0015():
    """Model: 2mm Pin v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            Circle(0.1)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


def model_22016_c1658896_0006():
    """Model: Washer v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 11.4353972591, perimeter: 16.3362817987
            with BuildLine():
                CenterArc((0, 0), 2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides extrude (symmetric), distance=0.1
        extrude(amount=0.1, both=True)
    return part.part


def model_22016_c1658896_0009():
    """Model: Static 2 v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 11.1881386018, perimeter: 19.1186721657
            with BuildLine():
                Line((3.6, 3.6), (3.6, 0))
                Line((0, 3.6), (3.6, 3.6))
                Line((0, 0), (0, 3.6))
                Line((3.6, 0), (0, 0))
            make_face()
            with BuildLine():
                CenterArc((1.8, 1.8), 0.751, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides extrude (symmetric), distance=1
        extrude(amount=1, both=True)
    return part.part


def model_22016_c1658896_0012():
    """Model: Keyway (4x4x15) v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with BuildLine():
                CenterArc((-0.55, 0), 0.2, 89.3366091039, 181.3267817922)
                CenterArc((-0.55, 0), 0.2, -89.3366091039, 178.6732182078)
            make_face()
            # Profile area: 0.314321558, perimeter: 3.4473647106
            with BuildLine():
                CenterArc((-0.55, 0), 0.2, -89.3366091039, 178.6732182078)
                Line((-0.5476843807, -0.1999865943), (0.5499975575, -0.2))
                CenterArc((0.55, 0), 0.2, 90.0006997365, 179.998600527)
                Line((-0.5476843807, 0.1999865943), (0.5499975575, 0.2))
            make_face()
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with BuildLine():
                CenterArc((0.55, 0), 0.2, 90.0006997365, 179.998600527)
                CenterArc((0.55, 0), 0.2, -90.0006997365, 180.001399473)
            make_face()
        # TwoSides extrude (symmetric), distance=0.2
        extrude(amount=0.2, both=True)
    return part.part


def model_22025_b77024b9_0006():
    """Model: Handle Part 5 v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=11.5
        extrude(amount=11.5)
    return part.part


def model_22025_b77024b9_0013():
    """Model: Stud Part 3 v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4.9087385212, perimeter: 7.853981634
            Circle(1.25)
        # OneSide extrude, distance=-16
        extrude(amount=-16)
    return part.part


def model_22040_6461a147_0003():
    """Model: hex nut v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4.9883063258, perimeter: 8.3138438763
            with BuildLine():
                Line((0.692820323, 1.2), (-0.692820323, 1.2))
                Line((-0.692820323, 1.2), (-1.3856406461, 0))
                Line((-1.3856406461, 0), (-0.692820323, -1.2))
                Line((-0.692820323, -1.2), (0.692820323, -1.2))
                Line((0.692820323, -1.2), (1.3856406461, 0))
                Line((1.3856406461, 0), (0.692820323, 1.2))
            make_face()
        # OneSide extrude, distance=1.3
        extrude(amount=1.3)
    return part.part


def model_22079_31335df2_0001():
    """Model: M10 Jam Nut (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.5028134169, perimeter: 5.8889727457
            with BuildLine():
                Line((-0.8373009098, 0.5121137762), (-0.8621539947, -0.4690669704))
                Line((-0.8621539947, -0.4690669704), (-0.0248530849, -0.9811807466))
                Line((-0.0248530849, -0.9811807466), (0.8373009098, -0.5121137762))
                Line((0.8373009098, -0.5121137762), (0.8621539947, 0.4690669704))
                Line((0.8621539947, 0.4690669704), (0.0248530849, 0.9811807466))
                Line((0.0248530849, 0.9811807466), (-0.8373009098, 0.5121137762))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


def model_22106_db85f777_0006():
    """Model: Plate v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 17 constraints, 71 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 634.4041369388, perimeter: 158.7462007569
            with BuildLine():
                Line((0, 0), (0, -20.32))
                Line((0, -20.32), (18.288, -20.32))
                Line((18.288, -20.32), (20.292561725, -23.5898662741))
                Line((20.292561725, -23.5898662741), (25.7279023529, -20.257780228))
                Line((25.7279023529, -20.257780228), (25.4041927167, -18.5094964777))
                Line((25.4041927167, -18.5094964777), (27.2766402712, -18.3456785437))
                Line((27.2766402712, -18.3456785437), (29.3049515405, -20.7552290318))
                Line((29.3049515405, -20.7552290318), (32.6472312498, -17.9417650131))
                Line((32.6472312498, -17.9417650131), (32.6472312498, -2.3782349869))
                Line((29.3049515405, 0.4352290318), (32.6472312498, -2.3782349869))
                Line((27.2766402712, -1.9743214563), (29.3049515405, 0.4352290318))
                Line((25.4041927167, -1.8105035223), (27.2766402712, -1.9743214563))
                Line((25.7279023529, -0.062219772), (25.4041927167, -1.8105035223))
                Line((20.292561725, 3.2698662741), (25.7279023529, -0.062219772))
                Line((18.288, 0), (20.292561725, 3.2698662741))
                Line((0, 0), (18.288, 0))
            make_face()
            with BuildLine():
                Line((26.5212772811, -10.1389644362), (24.6724212684, -6.9787227088))
                Line((24.7088556693, -13.3202415749), (26.5212772811, -10.1389644362))
                Line((21.0475780449, -13.341276986), (24.7088556693, -13.3202415749))
                Line((19.1987220323, -10.1810352586), (21.0475780449, -13.341276986))
                Line((21.011143644, -6.99975812), (19.1987220323, -10.1810352586))
                Line((24.6724212684, -6.9787227088), (21.011143644, -6.99975812))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.2700000405, -19.050000608), 0.1905, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.2700000405, -1.2700000405), 0.1905, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((20.8310139302, -22.0382596285), 0.1905, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((20.3132794449, -21.1937246306), 0.1905, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((22.4354443116, -19.8927507958), 0.1905, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((22.9531787968, -20.7372857938), 0.1905, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((30.1887270013, -18.6892482191), 0.1905, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((29.4279319337, -19.323660723), 0.1905, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((27.824911737, -17.419338563), 0.1905, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((28.5857068046, -16.7849260591), 0.1905, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((28.5827543008, -3.5385979608), 0.1905, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((27.8249117732, -2.9006613939), 0.1905, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((29.4279319699, -0.996339234), 0.1905, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((30.1857744975, -1.6342758009), 0.1905, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((22.2321721194, -0.2728420285), 0.1905, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((22.7499066047, 0.5716929694), 0.1905, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((20.627741738, 1.8726668042), 0.1905, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((20.1100072527, 1.0281318062), 0.1905, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3175
        extrude(amount=0.3175)
    return part.part


def model_22124_6f71410e_0000():
    """Model: Spacer v3 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 15.2083626045, perimeter: 27.0296453401
            with BuildLine():
                Line((11.8436285883, -0.6010022295), (4.8586285883, -0.6010022295))
                Line((11.8436285883, 1.9389977705), (11.8436285883, -0.6010022295))
                Line((4.8586285883, 1.9389977705), (11.8436285883, 1.9389977705))
                Line((4.8586285883, -0.6010022295), (4.8586285883, 1.9389977705))
            make_face()
            with BuildLine():
                CenterArc((10.4148785883, 0.6689977705), 0.635, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.2873785883, 0.6689977705), 0.635, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


def model_22124_6f71410e_0003():
    """Model: Reg Hex Nut v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.7370199251, perimeter: 14.7835521075
            with BuildLine():
                Line((4.2663905564, -1.8928016244), (5.4816345191, -1.0719999161))
                Line((5.4816345191, -1.0719999161), (5.3784213697, 0.3908330815))
                Line((5.3784213697, 0.3908330815), (4.0599642575, 1.032864371))
                Line((4.0599642575, 1.032864371), (2.8447202947, 0.2120626627))
                Line((2.8447202947, 0.2120626627), (2.9479334442, -1.250770335))
                Line((2.9479334442, -1.250770335), (4.2663905564, -1.8928016244))
            make_face()
            with BuildLine():
                CenterArc((4.1631774069, -0.4299686267), 0.9525, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)
    return part.part


def model_22197_5e5f919c_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 153.976, perimeter: 50.66
            with BuildLine():
                Line((7.6, -5.065), (7.6, 5.065))
                Line((7.6, 5.065), (-7.6, 5.065))
                Line((-7.6, 5.065), (-7.6, -5.065))
                Line((-7.6, -5.065), (7.6, -5.065))
            make_face()
        # OneSide extrude, distance=0.85
        extrude(amount=0.85)
    return part.part


def model_22199_8ec9eeb2_0000():
    """Model: Lower Tube v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.5814156251, perimeter: 23.8761041673
            with BuildLine():
                CenterArc((0, 0), 2.05, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=25.75
        extrude(amount=25.75)
    return part.part


def model_22199_8ec9eeb2_0002():
    """Model: Spacer 2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.4164820108, perimeter: 27.3318560862
            with BuildLine():
                CenterArc((-9.0791937798, -3.970060851), 2.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-9.0791937798, -3.970060851), 2.05, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_22199_8ec9eeb2_0003():
    """Model: Spacer 1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.4164820108, perimeter: 27.3318560862
            with BuildLine():
                CenterArc((-3.4179896043, -8.4504854359), 2.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-3.4179896043, -8.4504854359), 2.05, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


def model_22205_f48b96b3_0000():
    """Model: 10-M28 Stud v5 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.157521601, perimeter: 8.7964594301
            Circle(1.4)
        # OneSide extrude, distance=8.1
        extrude(amount=8.1)
    return part.part


def model_22205_f48b96b3_0004():
    """Model: washer for pins v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.7987827784, perimeter: 14.7654854719
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.85, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


def model_22206_703c82ed_0003():
    """Model: 3/16 SLOTTED SPRING PIN LONG"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.1781393481, perimeter: 1.4961835013
            Circle(0.238125)
        # OneSide extrude, distance=3.81
        extrude(amount=3.81)
    return part.part


def model_22211_b1ee53f0_0005():
    """Model: Thick Washer v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 6.6837383705, perimeter: 11.6238928183
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.35, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)
    return part.part


def model_22211_b1ee53f0_0011():
    """Model: Nut v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 20 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1612544872, perimeter: 4.2962769254
            with BuildLine():
                CenterArc((0, 0), 2.0000000298, -180, 59.9997657576)
                Line((-2.0000000298, 0.000000021), (-2.0000000298, -0.5773507191))
                CenterArc((-1.0000000298, -0.5773502864), 1, -179.9999752065, 59.9999503881)
                Line((-1.5000004049, -1.4433754736), (-1.000007096, -1.7320467451))
            make_face()
            # Profile area: 0.1612544872, perimeter: 4.2963081526
            with BuildLine():
                Line((1.0000064889, 1.7320470956), (0.4999996248, 2.0207261932))
                CenterArc((0, 1.1547005728), 1, 60.0000248205, 59.9999503397)
                Line((-0.4999996245, 2.0207261933), (-0.9999999906, 1.7320508474))
                CenterArc((0, 0), 2.0000000298, 59.9997858426, 60.0002133547)
            make_face()
            # Profile area: 0.1612544872, perimeter: 4.2962932745
            with BuildLine():
                Line((0.9999999893, -1.7320508481), (1.5000000298, -1.4433756902))
                CenterArc((1.0000000298, -0.5773502864), 1, -60, 60)
                Line((2.0000000298, -0.5773502864), (2.0000000298, -0.0000000211))
                CenterArc((0, 0), 2.0000000298, -60.0000008454, 60.0000002421)
            make_face()
            # Profile area: 0.1612544872, perimeter: 4.2962932716
            with BuildLine():
                Line((-0.9999999906, 1.7320508474), (-1.5000004047, 1.4433754737))
                CenterArc((-1.0000000298, 0.5773502864), 1, 120.0000248025, 59.9999503729)
                Line((-2.0000000298, 0.5773507197), (-2.0000000298, 0.000000021))
                CenterArc((0, 0), 2.0000000298, 119.9999991973, 60.0000002005)
            make_face()
            # Profile area: 2.9452432005, perimeter: 23.561945232
            with BuildLine():
                CenterArc((0, 0), 2.0000000298, -60.0000008454, 60.0000002421)
                CenterArc((0, 0), 2.0000000298, -0.0000006034, 59.9997864459)
                CenterArc((0, 0), 2.0000000298, 59.9997858426, 60.0002133547)
                CenterArc((0, 0), 2.0000000298, 119.9999991973, 60.0000002005)
                CenterArc((0, 0), 2.0000000298, -180, 59.9997657576)
                CenterArc((0, 0), 2.0000000298, -120.0002342424, 60.000233397)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.7500000261, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1612544872, perimeter: 4.2962783487
            with BuildLine():
                Line((2.0000000298, -0.0000000211), (2.0000000298, 0.5773507191))
                CenterArc((1.0000000298, 0.5773502864), 1, 0.0000247935, 59.9999503878)
                Line((1.5000004049, 1.4433754736), (1.0000064889, 1.7320470956))
                CenterArc((0, 0), 2.0000000298, -0.0000006034, 59.9997864459)
            make_face()
            # Profile area: 0.1612544872, perimeter: 4.2963095518
            with BuildLine():
                CenterArc((0, 0), 2.0000000298, -120.0002342424, 60.000233397)
                Line((-1.000007096, -1.7320467451), (-0.4999996254, -2.0207261929))
                CenterArc((0, -1.1547005728), 1, -119.9999752158, 59.999950395)
                Line((0.4999996248, -2.0207261932), (0.9999999893, -1.7320508481))
            make_face()
        # OneSide extrude, distance=2.1
        extrude(amount=2.1)
    return part.part


def model_22212_aadd1fae_0000():
    """Model: Fuel Injector Lock Nut v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.9609281078, perimeter: 7.0166062226
            with BuildLine():
                Line((-0.375277675, 0.65), (0, 0))
                Line((0, 0), (0.7505553499, 0))
                Line((0.7505553499, 0), (1.1258330249, 0.65))
                Line((1.1258330249, 0.65), (0.7505553499, 1.3))
                Line((0.7505553499, 1.3), (0, 1.3))
                Line((0, 1.3), (-0.375277675, 0.65))
            make_face()
            with BuildLine():
                CenterArc((0.375277675, 0.65), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


def model_22225_a3ce4d29_0002():
    """Model: Wrist Pin  (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1790906914, perimeter: 1.5001733239
            Circle(0.23876)
        # OneSide extrude, distance=2.159
        extrude(amount=2.159)
    return part.part


def model_22225_a3ce4d29_0004():
    """Model: Cam Shaft"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.3166921744, perimeter: 1.994911335
            Circle(0.3175)
        # OneSide extrude, distance=2.38252
        extrude(amount=2.38252)
    return part.part


def model_22225_a3ce4d29_0014():
    """Model: Exhaust Cam  v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.059762178, perimeter: 7.7825813833
            with BuildLine():
                CenterArc((0, 0), 0.90424, 69.0997808201, 41.8004383599)
                Line((-0.32258, 0.8447438199), (-0.6103635048, 0.3699745661))
                CenterArc((0, 0), 0.71374, 148.7776641702, 242.4447214085)
                Line((0.32258, 0.8447438199), (0.6103631836, 0.3699750961))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.47625, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.238125
        extrude(amount=0.238125, both=True)
    return part.part


def model_22228_1c82530b_0008():
    """Model: Component4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0100556613, perimeter: 0.5595804835
            with BuildLine():
                CenterArc((0, 0), 0.0625, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.02656, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.00625
        extrude(amount=0.00625)
    return part.part


def model_22228_1c82530b_0009():
    """Model: Component5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0005588501, perimeter: 0.168075207
            with BuildLine():
                CenterArc((0, 0), 0.0167, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.01005, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.00625
        extrude(amount=0.00625)
    return part.part


def model_22228_1c82530b_0010():
    """Model: Component6"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0947295304, perimeter: 1.2729792058
            with BuildLine():
                Line((0.2121629007, -0.0924630763), (0.1861629007, -0.1374963973))
                Line((0.026, 0.22997), (0.2121629007, -0.0924630763))
                Line((0.026, 0.22997), (-0.026, 0.22997))
                Line((-0.2121634688, -0.0924620924), (-0.026, 0.22997))
                Line((-0.1861634688, -0.1374954134), (-0.2121634688, -0.0924620924))
                Line((0.1861629007, -0.1374963973), (-0.1861634688, -0.1374954134))
            make_face()
            with BuildLine():
                Line((-0.0259948641, -0.0150070546), (-0.0260006474, -0.0150103934))
                Line((-0.0260006474, -0.0150037157), (-0.0260006474, -0.0150103934))
                Line((-0.0259948641, -0.0150070546), (-0.0260006474, -0.0150037157))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.025
        extrude(amount=0.025)
    return part.part


def model_22228_1c82530b_0013():
    """Model: Component15"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 13 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0269783611, perimeter: 2.9151520168
            with BuildLine():
                Line((0.0372795239, 0.0241481457), (1.3253995688, 0.3692988714))
                CenterArc((1.3318700449, 0.3451507258), 0.025, 67, 38)
                Line((1.3746876844, 0.3541347256), (1.3416383231, 0.3681633471))
                Line((1.3746876844, 0.3541347256), (1.3761610521, 0.353557363))
                Line((1.3761610521, 0.353557363), (1.3834834638, 0.3707703958))
                Line((1.3489645318, 0.3854228131), (1.3834834638, 0.3707703958))
                CenterArc((1.3318700449, 0.3451507258), 0.04375, 67, 38)
                Line((0.0324266668, 0.0422592549), (1.3205467117, 0.3874099807))
                CenterArc((0.04375, 0), 0.04375, 105, 75)
                Line((0, 0), (0.01875, 0))
                CenterArc((0.04375, 0), 0.025, 105, 75)
            make_face()
            # Profile area: 0.0011685, perimeter: 0.16214
            with BuildLine():
                Line((0, 0), (0.01875, 0))
                Line((0, -0.06232), (0, 0))
                Line((0.01875, -0.06232), (0, -0.06232))
                Line((0.01875, 0), (0.01875, -0.06232))
            make_face()
        # OneSide extrude, distance=0.0375
        extrude(amount=0.0375)
    return part.part


def model_22228_1c82530b_0019():
    """Model: Component28"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.002120575, perimeter: 0.2827433388
            with BuildLine():
                CenterArc((2.0000000298, 1.0000000149), 0.03, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((2.0000000298, 1.0000000149), 0.015, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.00625
        extrude(amount=0.00625)
    return part.part


def model_22254_539990c2_0006():
    """Model: Ground Steel Dowel v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=4.158
        extrude(amount=4.158)
    return part.part


def model_22254_539990c2_0007():
    """Model: Ground Steel Dowel 6 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.3273228961, perimeter: 4.0840704497
            Circle(0.65)
        # OneSide extrude, distance=3.8
        extrude(amount=3.8)
    return part.part


def model_22254_539990c2_0008():
    """Model: Expansion Pin v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1155487857, perimeter: 2.5176993257
            with BuildLine():
                CenterArc((0, 0), 0.15, 19.4712206345, 321.057558731)
                Line((0.1414213562, 0.05), (0.2449489743, 0.05))
                CenterArc((0, 0), 0.25, 11.5369590328, 336.9260819344)
                Line((0.2449489743, -0.05), (0.1414213562, -0.05))
            make_face()
        # OneSide extrude, distance=3.937
        extrude(amount=3.937)
    return part.part


def model_22276_69c5036b_0005():
    """Model: Component1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 30.9132717113, perimeter: 51.5221195189
            with BuildLine():
                CenterArc((0, 0), 4.7, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.3
        extrude(amount=1.3)
    return part.part


def model_22276_69c5036b_0006():
    """Model: Component2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 126.449104307, perimeter: 72.2566310326
            with BuildLine():
                CenterArc((0, 0), 7.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)
    return part.part


def model_22276_69c5036b_0009():
    """Model: Component4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 37.6991118431, perimeter: 62.8318530718
            with BuildLine():
                CenterArc((0, 0), 5.6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 4.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.3
        extrude(amount=1.3)
    return part.part


def model_22276_69c5036b_0012():
    """Model: Component16"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 15 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2084664734, perimeter: 4.3839187561
            with BuildLine():
                Line((24.97, 25.2984962311), (24.9164862939, 25.391184689))
                CenterArc((25, 25), 0.4, 102.0511165988, 335.8977668025)
                Line((25.03, 25.2984962311), (25.0835137061, 25.391184689))
                CenterArc((25, 25), 0.3, 95.7391704773, 348.5216590455)
            make_face()
        # OneSide extrude, distance=1.3
        extrude(amount=1.3)
    return part.part


def model_22276_69c5036b_0014():
    """Model: Component18"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 17 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0987183528, perimeter: 4.0585323404
            with BuildLine():
                CenterArc((1.5, 1.5), 0.3, 93.8225537293, 352.3548925415)
                Line((1.48, 1.7993325909), (1.452608184, 1.8467766079))
                CenterArc((1.5, 1.5), 0.35, 97.7820506183, 344.4358987634)
                Line((1.52, 1.7993325909), (1.547391816, 1.8467766079))
            make_face()
        # OneSide extrude, distance=2.2
        extrude(amount=2.2)
    return part.part


def model_22284_5d31c681_0000():
    """Model: Lock Nut"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.9485571585, perimeter: 5.1961524227
            with BuildLine():
                Line((0.4330127019, -0.75), (0.8660254038, 0))
                Line((0.8660254038, 0), (0.4330127019, 0.75))
                Line((0.4330127019, 0.75), (-0.4330127019, 0.75))
                Line((-0.4330127019, 0.75), (-0.8660254038, 0))
                Line((-0.8660254038, 0), (-0.4330127019, -0.75))
                Line((-0.4330127019, -0.75), (0.4330127019, -0.75))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


def model_22289_4b848f64_0003():
    """Model: Film Ring"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.2064993881, perimeter: 49.6999957798
            with BuildLine():
                CenterArc((-2.5, 0.5), 4.1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-2.5, 0.5), 3.81, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


def model_22305_5b45cdb3_0000():
    """Model: 37-CON-ROD v1 (3)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 15 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.2129707736, perimeter: 6.5184969612
            with BuildLine():
                Line((0.2, -0.1842838874), (3.03, -0.2443276841))
                Line((3.03, -0.2443276841), (3.03, 0.2443277016))
                Line((0.2, 0.1842838886), (3.03, 0.2443277016))
                Line((0.2, 0.1842838886), (0.2, -0.1842838874))
            make_face()
        # OneSide extrude, distance=0.15
        extrude(amount=0.15)
    return part.part


def model_22305_5b45cdb3_0008():
    """Model: 08-AXLE-BOX-SHEEN-PLATE-2 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 15 constraints, 26 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.6685840735, perimeter: 5.0566370614
            with BuildLine():
                Line((0.5, 0), (0.9, 0))
                Line((0.9, 0), (1.4, 0))
                Line((1.4, 0), (1.4, 0.5))
                Line((1.4, 0.5), (0, 0.5))
                Line((0, 0.5), (0, 0))
                Line((0, 0), (0.5, 0))
            make_face()
            with BuildLine():
                CenterArc((1.2124148983, 0.4), 0.05, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.2124148983, 0.1), 0.05, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.158917545, 0.1), 0.05, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.158917545, 0.4), 0.05, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.3793562998, perimeter: 3.3743632831
            with BuildLine():
                Line((0.9, 0), (0.9, -1.1))
                CenterArc((1.0000000015, -1.1), 0.1000000015, 180, 166.2249074551)
                Line((1.0971237912, -1.123811127), (1.3236067977, -0.2))
                CenterArc((1.6236067977, -0.2), 0.3, 138.1896851042, 41.8103148958)
                Line((0.9, 0), (1.4, 0))
            make_face()
            with BuildLine():
                CenterArc((1.0000000015, -1.1), 0.0500000007, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.3793562998, perimeter: 3.3743632831
            with BuildLine():
                Line((0, 0), (0.5, 0))
                CenterArc((-0.2236067977, -0.2), 0.3, 0, 41.8103148958)
                Line((0.3028762024, -1.123811101), (0.0763932023, -0.2))
                CenterArc((0.3999999985, -1.1), 0.1000000015, -166.2249228106, 166.2249228106)
                Line((0.5, 0), (0.5, -1.1))
            make_face()
            with BuildLine():
                CenterArc((0.3999999985, -1.1), 0.0500000007, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


def model_22305_5b45cdb3_0011():
    """Model: 07-AXLE-BOX-SHEEN-PLATE-1 v1 (3)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 15 constraints, 37 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.6228543219, perimeter: 11.3016093253
            with BuildLine():
                CenterArc((2.9346546369, 3.0095943133), 0.1, 105, 172.1807557815)
                CenterArc((3.3346546369, 3.0095943133), 0.4, -165.6384884371, 45.6384884371)
                Line((3.1346546369, 2.6631841517), (3.1346546369, 3.5095943133))
                Line((3.1346546369, 3.5095943133), (3.5346546369, 3.5095943133))
                Line((3.5346546369, 3.5095943133), (3.5346546369, 2.6631841517))
                CenterArc((3.3346546369, 3.0095943133), 0.4, -60, 45.6384884371)
                CenterArc((3.7346546369, 3.0095943133), 0.1, -97.1807557815, 172.1807557815)
                Line((3.7605365414, 3.1061868959), (3.9846568329, 3.9426152107))
                CenterArc((4.2846546369, 3.9437630737), 0.3, 146.4426902381, 33.7765359893)
                Line((4.0346546369, 4.1095943133), (4.0346546369, 4.6095943133))
                Line((4.0346546369, 4.6095943133), (2.6346546369, 4.6095943133))
                Line((2.6346546369, 4.6095943133), (2.6346546369, 4.1095943133))
                CenterArc((2.3846546369, 3.9437630737), 0.3, -0.2192262273, 33.7765359893)
                Line((2.9087727324, 3.1061868959), (2.6846524409, 3.9426152107))
            make_face()
            with BuildLine():
                Line((3.5346546369, 4.1095943133), (3.1346546369, 4.1095943133))
                Line((3.5346546369, 3.7095943133), (3.5346546369, 4.1095943133))
                Line((3.1346546369, 3.7095943133), (3.5346546369, 3.7095943133))
                Line((3.1346546369, 4.1095943133), (3.1346546369, 3.7095943133))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.7846546369, 4.5095943133), 0.05, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.7846546369, 4.2095943133), 0.05, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.8846546369, 4.2095943133), 0.05, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.8846546369, 4.5095943133), 0.05, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.9346546369, 3.0095943133), 0.05, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.7346546369, 3.0095943133), 0.05, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


def model_22305_5b45cdb3_0020():
    """Model: 20-DRIVER-PROTECTION-SIDE-PLATE v1 (3)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.2931932155, perimeter: 16.3524601219
            with BuildLine():
                CenterArc((0, 0), 2.25, 18.1262039606, 143.7475920789)
                Line((-2.138340478, 0.7), (2.138340478, 0.7))
            make_face()
            with BuildLine():
                Line((-1.4874474781, 1.1), (1.4874474781, 1.1))
                CenterArc((0, 0), 1.85, 36.4837370614, 107.0325258773)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)
    return part.part


def model_22320_e9f9e6ae_0000():
    """Model: Washer v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 24.2743338823, perimeter: 26.8495559215
            with BuildLine():
                CenterArc((0, 0), 3, 0, 360)
            make_face()
            with BuildLine():
                Line((1, 1), (1, -1))
                Line((1, -1), (-1, -1))
                Line((-1, -1), (-1, 1))
                Line((-1, 1), (1, 1))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)
    return part.part


def model_22320_e9f9e6ae_0003():
    """Model: Nut v2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 10.714813807, perimeter: 20.1395917677
            with BuildLine():
                Line((0.5758910152, -2.2364442474), (2.22476304, -0.6194858747))
                Line((2.22476304, -0.6194858747), (1.6488720248, 1.6169583727))
                Line((1.6488720248, 1.6169583727), (-0.5758910152, 2.2364442474))
                Line((-0.5758910152, 2.2364442474), (-2.22476304, 0.6194858747))
                Line((-2.22476304, 0.6194858747), (-1.6488720248, -1.6169583727))
                Line((-1.6488720248, -1.6169583727), (0.5758910152, -2.2364442474))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.6
        extrude(amount=0.6, both=True)
    return part.part


def model_22320_e9f9e6ae_0008():
    """Model: Safety Link v4 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 32.0219501, perimeter: 39.8796475617
            with BuildLine():
                CenterArc((-6.2000007062, 0), 1.2, 89.9999439215, 180.0000540041)
                Line((-6.2000007496, -1.2), (6.200000467, -1.2))
                CenterArc((6.2000007062, 0), 1.2, -90.0000114189, 180.0000227655)
                Line((6.2000004683, 1.2), (-6.1999995317, 1.2))
            make_face()
            with BuildLine():
                CenterArc((-6.2000007062, 0), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.2000007062, 0), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)
    return part.part


def model_22320_e9f9e6ae_0009():
    """Model: Pin v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            Circle(0.6)
        # Symmetric extrude, each_side=3.75
        extrude(amount=3.75, both=True)
    return part.part


def model_22322_f04772b3_0002():
    """Model: Stud v3 (1)"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981868, perimeter: 3.1415927004
            Circle(0.5000000075)
        # OneSide extrude, distance=4.4
        extrude(amount=4.4)
    return part.part


def model_22323_aa6edb8b_0000():
    """Model: Hex Nut v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.4489259255, perimeter: 12.7120735914
            with BuildLine():
                Line((0, -1.3856406461), (1.2, -0.692820323))
                Line((1.2, -0.692820323), (1.2, 0.692820323))
                Line((1.2, 0.692820323), (0, 1.3856406461))
                Line((0, 1.3856406461), (-1.2, 0.692820323))
                Line((-1.2, 0.692820323), (-1.2, -0.692820323))
                Line((-1.2, -0.692820323), (0, -1.3856406461))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.7, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.6
        extrude(amount=1.6)
    return part.part


def model_22323_aa6edb8b_0006():
    """Model: Hex Nut 2 v1 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.6495748606, perimeter: 8.2129163398
            with BuildLine():
                Line((0.8, -0.4618802154), (0.8, 0.4618802154))
                Line((0.8, 0.4618802154), (0, 0.9237604307))
                Line((0, 0.9237604307), (-0.8, 0.4618802154))
                Line((-0.8, 0.4618802154), (-0.8, -0.4618802154))
                Line((-0.8, -0.4618802154), (0, -0.9237604307))
                Line((0, -0.9237604307), (0.8, -0.4618802154))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.425, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)
    return part.part


def model_22323_aa6edb8b_0009():
    """Model: Stud v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.0106192983, perimeter: 5.0265482457
            Circle(0.8)
        # OneSide extrude, distance=5.2
        extrude(amount=5.2)
    return part.part


def model_22340_ec24cd79_0036():
    """Model: part 4 v2 (4)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 11 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.0592944134, perimeter: 6.5171505587
            with BuildLine():
                Line((0, 10.65), (0, 13.5))
                CenterArc((0, 0), 13.5, 90, 3.1490135935)
                Line((0, 10.65), (-0.7415953633, 13.4796155849))
            make_face()
            # Profile area: 793.1657512334, perimeter: 215.8274153016
            with BuildLine():
                CenterArc((0, 0), 20.85, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 13.5, 93.1490135935, 23.0739180656)
                CenterArc((0, 0), 13.5, 90, 3.1490135935)
                CenterArc((0, 0), 13.5, 116.2229316591, 333.7770683409)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 199.6454959759, perimeter: 145.8758884972
            with BuildLine():
                CenterArc((0, 0), 13.5, 116.2229316591, 333.7770683409)
                Line((0, 10.65), (0, 13.5))
                CenterArc((0, 0), 10.65, 119.3719452526, 330.6280547474)
                Line((-5.2235811888, 9.2809859155), (-5.9651765521, 12.1106015004))
            make_face()
        # OneSide extrude, distance=0.9
        extrude(amount=0.9)
    return part.part


def model_22341_0f9c52ed_0001():
    """Model: 3 v6"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 32.1699087728, perimeter: 20.106192983
            Circle(3.2)
        # OneSide extrude, distance=-1
        extrude(amount=-1)
    return part.part


def model_22342_274ed8a6_0001():
    """Model: 5 v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.4823001647, perimeter: 18.8495559215
            with BuildLine():
                CenterArc((0, 0), 1.95, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.05, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.6
        extrude(amount=1.6)
    return part.part


def model_22342_274ed8a6_0003():
    """Model: 12 v1"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.9792033718, perimeter: 13.1946891451
            with BuildLine():
                CenterArc((0, 0), 1.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.9, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=5.4
        extrude(amount=5.4)
    return part.part


def model_22355_6a8b11c3_0011():
    """Model: M3-silver v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.181847173, perimeter: 2.8130926683
            with BuildLine():
                Line((-0.1546362145, -0.2707169023), (0.1571296074, -0.2692773412))
                Line((0.1571296074, -0.2692773412), (0.3117658218, 0.001439561))
                Line((0.3117658218, 0.001439561), (0.1546362145, 0.2707169023))
                Line((0.1546362145, 0.2707169023), (-0.1571296074, 0.2692773412))
                Line((-0.1571296074, 0.2692773412), (-0.3117658218, -0.001439561))
                Line((-0.3117658218, -0.001439561), (-0.1546362145, -0.2707169023))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.226
        extrude(amount=0.226)
    return part.part


def model_22357_e2f7b060_0018():
    """Model: Valve Linkage v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.5373451754, perimeter: 20.1132741229
            with BuildLine():
                CenterArc((8.8, 0), 0.4, 90, 180)
                Line((0, 0.4), (8.8, 0.4))
                CenterArc((0, 0), 0.4, -90, 180)
                Line((0, -0.4), (8.8, -0.4))
            make_face()
            # Profile area: 0.3769909499, perimeter: 3.7699120269
            with BuildLine():
                CenterArc((8.8, 0), 0.4, 90, 180)
                CenterArc((8.8, 0), 0.4, -90, 180)
            make_face()
            with BuildLine():
                CenterArc((8.8, 0), 0.2000001341, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.3769911184, perimeter: 3.7699111843
            with BuildLine():
                CenterArc((0, 0), 0.4, 90, 180)
                CenterArc((0, 0), 0.4, -90, 180)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


def model_22357_e2f7b060_0021():
    """Model: Beam Linkage v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3769911184, perimeter: 3.7699111843
            with BuildLine():
                CenterArc((0, 3.2000000238), 0.4, 180, 180.0000034151)
                CenterArc((0, 3.2000000238), 0.4, 0.0000034151, 179.9999965849)
            make_face()
            with BuildLine():
                CenterArc((0, 3.2000000238), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.3769911184, perimeter: 3.7699111843
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 180)
                CenterArc((0, 0), 0.4, -180, 180)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 2.0573451945, perimeter: 8.9132741944
            with BuildLine():
                Line((0.4, 0), (0.4, 3.2000000477))
                CenterArc((0, 3.2000000238), 0.4, 180, 180.0000034151)
                Line((-0.4, 0), (-0.4, 3.2000000238))
                CenterArc((0, 0), 0.4, 0, 180)
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


def model_22357_e2f7b060_0023():
    """Model: DIN 6799 - 3.2 v1 (3)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 30 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1925858855, perimeter: 3.3505602401
            with BuildLine():
                CenterArc((0.2532789977, -0.1816772944), 0.0533, -160, 124.3480856581)
                CenterArc((0, 0), 0.365, -35.6519143419, 251.3038286839)
                CenterArc((-0.2532789977, -0.1816772944), 0.0533, -144.3480856581, 124.3480856581)
                Line((-0.1503508193, -0.0547232229), (-0.203193381, -0.1999069681))
                CenterArc((0, 0), 0.16, 163.3580800245, 36.6419199755)
                CenterArc((-0.1768677145, 0.0528674905), 0.0246, -16.6419199755, 82.3419199755)
                Line((-0.1667444613, 0.0752880111), (-0.213578583, 0.0964344279))
                CenterArc((-0.1967064943, 0.1338019623), 0.041, 145.7760236696, 99.9239763304)
                CenterArc((0, 0), 0.2789, 107.6239763304, 38.1520473392)
                CenterArc((-0.0720286837, 0.2267339382), 0.041, 7.7, 99.9239763304)
                Line((-0.0245132477, 0.1813038904), (-0.0313983725, 0.2322273718))
                CenterArc((-0.000135061, 0.1845999506), 0.0246, -172.3, 82.3419199755)
                CenterArc((0, 0), 0.16, 89.9580800245, 0.0838399511)
                CenterArc((0.000135061, 0.1845999506), 0.0246, -90.0419199755, 82.3419199755)
                Line((0.0245132477, 0.1813038904), (0.0313983725, 0.2322273718))
                CenterArc((0.0720286837, 0.2267339382), 0.041, 72.3760236696, 99.9239763304)
                CenterArc((0, 0), 0.2789, 34.2239763304, 38.1520473392)
                CenterArc((0.1967064943, 0.1338019623), 0.041, -65.7, 99.9239763304)
                Line((0.1667444613, 0.0752880111), (0.213578583, 0.0964344279))
                CenterArc((0.1768677145, 0.0528674905), 0.0246, 114.3, 82.3419199755)
                CenterArc((0, 0), 0.16, -20, 36.6419199755)
                Line((0.1503508193, -0.0547232229), (0.203193381, -0.1999069681))
            make_face()
        # OneSide extrude, distance=0.06
        extrude(amount=0.06)
    return part.part


def model_22369_481ab478_0014():
    """Model: valve link bell crank v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 29 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7416631443, perimeter: 6.745464978
            with BuildLine():
                Line((0, 0.28956), (0.0795182424, 0.2784274461))
                CenterArc((0, 0), 0.28956, 90, 90)
                Line((-0.2845587875, -0.0535844202), (-0.28956, 0))
                Line((-0.20066, -0.9525), (-0.2845587875, -0.0535844202))
                CenterArc((0, -0.9525), 0.20066, 180, 180)
                Line((0.20066, -0.9525), (0.2658299708, -0.3532027931))
                CenterArc((0.4223870277, -0.3702274325), 0.15748, 93.2052988897, 80.5885158812)
                Line((0.6338783183, -0.2006568649), (0.4135817156, -0.2129937946))
                CenterArc((0.635, 0), 0.20066, -90.3202828682, 180.3202828682)
                Line((0.0795182424, 0.2784274461), (0.635, 0.20066))
            make_face()
            with BuildLine():
                CenterArc((0.635, 0), 0.11049, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0), 0.15875, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, -0.9525), 0.11049, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.15748
        extrude(amount=0.15748)
    return part.part


def model_22369_481ab478_0023():
    """Model: rocking beam v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 75 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.1466741092, perimeter: 12.2762118573
            with BuildLine():
                Line((0.0008515176, -0.3174988581), (0.0008515176, -0.6312053509))
                CenterArc((0, 0), 0.3175, -180, 90.1536643216)
                Line((-0.3175, 0), (-0.7050774865, 0))
                Line((-0.7050774865, -0.4272946871), (-0.7050774865, 0))
                Line((-0.7050774865, -0.4272946871), (-4.7517400151, -0.1774429281))
                Line((-4.7517400151, -0.1774429281), (-4.7517400151, 0))
                Line((-4.7517400151, 0), (-4.92125, 0))
                CenterArc((-5.08, 0), 0.15875, -180, 180)
                Line((-5.23875, 0), (-5.3975, 0))
                CenterArc((-5.08, 0), 0.3175, -180, 90)
                Line((-5.08, -0.3175), (0.0008515176, -0.6312053509))
            make_face()
            # Profile area: 1.1466741092, perimeter: 12.2762118573
            with BuildLine():
                Line((-5.23875, 0), (-5.3975, 0))
                CenterArc((-5.08, 0), 0.15875, 0, 180)
                Line((-4.7517400151, 0), (-4.92125, 0))
                Line((-4.7517400151, 0.1774429281), (-4.7517400151, 0))
                Line((-4.7517400151, 0.1774429281), (-0.7050774865, 0.4272946871))
                Line((-0.7050774865, 0.4272946871), (-0.7050774865, 0))
                Line((-0.3175, 0), (-0.7050774865, 0))
                CenterArc((0, 0), 0.3175, 89.8463356784, 90.1536643216)
                Line((0.0008515176, 0.6312053509), (0.0008515176, 0.3174988581))
                Line((-5.08, 0.3175), (0.0008515176, 0.6312053509))
                CenterArc((-5.08, 0), 0.3175, 90, 90)
            make_face()
            # Profile area: 1.3411386197, perimeter: 13.0828683149
            with BuildLine():
                CenterArc((5.08, 0), 0.3175, -90, 90)
                Line((5.23875, 0), (5.3975, 0))
                CenterArc((5.08, 0), 0.15875, -180, 180)
                Line((4.92125, 0), (4.71745818, 0))
                Line((4.71745818, 0), (4.71745818, -0.1795817))
                Line((2.90254182, -0.2916770592), (4.71745818, -0.1795817))
                Line((2.90254182, 0), (2.90254182, -0.2916770592))
                Line((2.69875, 0), (2.90254182, 0))
                CenterArc((2.54, 0), 0.15875, -180, 180)
                Line((2.1774575191, 0), (2.38125, 0))
                Line((2.1774575191, 0), (2.1774575191, -0.3364607126))
                Line((0.7067805217, -0.4272946871), (2.1774575191, -0.3364607126))
                Line((0.7067805217, -0.4272946871), (0.7067805217, 0))
                Line((0.3175, 0), (0.7067805217, 0))
                CenterArc((0, 0), 0.3175, -89.8463356784, 89.8463356784)
                Line((0.0008515176, -0.3174988581), (0.0008515176, -0.6312053509))
                Line((0.0008515176, -0.6312053509), (5.08, -0.3175))
            make_face()
            # Profile area: 1.3411386197, perimeter: 13.0828683149
            with BuildLine():
                Line((0.0008515176, 0.6312053509), (0.0008515176, 0.3174988581))
                CenterArc((0, 0), 0.3175, 0, 89.8463356784)
                Line((0.3175, 0), (0.7067805217, 0))
                Line((0.7067805217, 0.4272946871), (0.7067805217, 0))
                Line((0.7067805217, 0.4272946871), (2.1774575191, 0.3364607126))
                Line((2.1774575191, 0), (2.1774575191, 0.3364607126))
                Line((2.1774575191, 0), (2.38125, 0))
                CenterArc((2.54, 0), 0.15875, 0, 180)
                Line((2.69875, 0), (2.90254182, 0))
                Line((2.90254182, 0), (2.90254182, 0.2916770592))
                Line((2.90254182, 0.2916770592), (4.71745818, 0.1795817))
                Line((4.71745818, 0), (4.71745818, 0.1795817))
                Line((4.92125, 0), (4.71745818, 0))
                CenterArc((5.08, 0), 0.15875, 0, 180)
                Line((5.23875, 0), (5.3975, 0))
                CenterArc((5.08, 0), 0.3175, 0, 90)
                Line((0.0008515176, 0.6312053509), (5.08, 0.3175))
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


def model_22369_481ab478_0027():
    """Model: beam parellel links v3 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 17 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.2065878464, perimeter: 7.8111015742
            with BuildLine():
                CenterArc((0.9525, 0), 0.3175, -90, 180)
                CenterArc((0.0000000378, 7.4295003486), 7.1755003405, -97.6281496092, 15.256298609)
                CenterArc((-0.9525, 0), 0.3175000101, 90, 180)
                CenterArc((0.0000000378, -7.4295003486), 7.1755003405, 82.3718510003, 15.256298609)
            make_face()
            with BuildLine():
                CenterArc((0.9525, 0), 0.15875, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-0.9525, 0), 0.15875, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.15748
        extrude(amount=0.15748)
    return part.part


def model_22395_7f99d894_0003():
    """Model: BRACE v1 (3)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 6 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 14.1362830044, perimeter: 23.3097335529
            with BuildLine():
                CenterArc((-5, 5), 1, 0, 180)
                Line((-6, 5), (-6, -1))
                CenterArc((-5, -1), 1, 180, 180)
                Line((-4, 5), (-4, -1))
            make_face()
            with BuildLine():
                CenterArc((-5, -1), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-5, 5), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)
    return part.part


def model_22395_7f99d894_0007():
    """Model: E CLIP v1 v1 (3)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 20 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.252188416, perimeter: 4.6546673205
            with BuildLine():
                Line((0.3601969301, -0.1739487613), (0.4591756851, -0.3862093865))
                CenterArc((0, 0), 0.6, -40.0669514093, 220.0669514093)
                Line((-0.6, 0), (-0.5, 0))
                CenterArc((0, 0), 0.5, 101.9542921818, 78.0457078182)
                Line((-0.0861882859, 0.3906046305), (-0.1035656528, 0.4891565757))
                CenterArc((0, 0), 0.4000004974, 89.8886642733, 12.5544645595)
                CenterArc((0.0001718476, -0.001590702), 0.4015909006, 77.599616496, 12.3140065752)
                Line((0.1037750441, 0.4891121959), (0.0864102263, 0.3906314206))
                CenterArc((0, 0), 0.5, 0, 78.0211803317)
                Line((0.4, 0), (0.5, 0))
                CenterArc((0, 0), 0.4, -25.7771431719, 25.7771431719)
            make_face()
            # Profile area: 0.0602631617, perimeter: 1.0337422289
            with BuildLine():
                Line((-0.6, 0), (-0.5, 0))
                CenterArc((0, 0), 0.6, 180, 40.0669514093)
                Line((-0.3601969301, -0.1739487613), (-0.4591756851, -0.3862093865))
                CenterArc((0, 0), 0.4, -180, 25.7771431719)
                Line((-0.5, 0), (-0.4, 0))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


def model_22404_66db7dd7_0002():
    """Model: Inner Plate"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 0.4), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 13.0467166404, perimeter: 24.3245471165
            with BuildLine():
                CenterArc((1.6992002608, -9.8826187656), 0.8570705916, -179.566979226, 185.015408253)
                CenterArc((-96.8564087068, -19.2829215609), 99.8599682846, 5.448429027, 0.4641021976)
                Line((2.4723356484, -8.9963375498), (2.5120845597, -8.9922251339))
                CenterArc((2.50694161, -8.9425155085), 0.0499749616, -84.0932035146, 90.0343809411)
                CenterArc((-96.8564125645, -19.2828978999), 99.9499232139, 5.9411774265, 0.5907879244)
                CenterArc((2.3950147844, -7.9185313383), 0.05, 6.5319653512, 44.429905027)
                CenterArc((3.3429539699, -6.7495154826), 1.4550537433, 143.2976903309, 87.6641800473)
                CenterArc((2.1362747946, -5.8500088745), 0.05, -36.7023096691, 44.4299050273)
                CenterArc((-96.8564125662, -19.2828979009), 99.9499232157, 7.7275953587, 1.5075781017)
                CenterArc((1.7486254835, -3.250239594), 0.0499749616, 9.23517346, 90.0344084171)
                Line((1.7405755227, -3.2009172368), (1.70113492, -3.2073543847))
                CenterArc((-96.8564087074, -19.2829215595), 99.8599682849, 9.2638471366, 0.8651794898)
                CenterArc((0.7966683886, -1.8306393888), 0.6596694932, 9.5669792254, 180.5620474023)
                CenterArc((-49.221332598, -10.267465059), 50.0649165386, 6.8313994261, 2.7355797999)
                Line((0.4881466068, -4.3123374187), (0.6008137036, -4.302480325))
                CenterArc((0.6051714907, -4.3522900599), 0.05, -85, 180)
                Line((0.6095292778, -4.4020997948), (0.8709965071, -7.390683889))
                CenterArc((0.8753542932, -7.440493624), 0.05, -85, 179.9999987926)
                Line((0.8797120804, -7.4903033589), (0.7670449836, -7.5001604526))
                CenterArc((-49.221332598, -10.267465059), 50.0649165386, 0.433020774, 2.7355797999)
            make_face()
            with BuildLine():
                CenterArc((0.796499983, -1.834553836), 0.21, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.6983767094, -9.8841885091), 0.21, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


def model_22430_c6f08b03_0037():
    """Model: CamBearing v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0578862624, perimeter: 3.2556952988
            with BuildLine():
                CenterArc((0, 0), 0.27686, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2413, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-8.255
        extrude(amount=-8.255)
    return part.part


def model_22433_9f17ac4c_0001():
    """Model: Air Tube"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0084872089, perimeter: 1.9399334636
            with BuildLine():
                CenterArc((0, 0), 0.15875, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.302
        extrude(amount=2.302)
    return part.part


def model_22433_9f17ac4c_0006():
    """Model: Cylinder Liner"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.8696564638, perimeter: 10.973583139
            with BuildLine():
                CenterArc((0, 0), 0.9525, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.794, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=1.7
        extrude(amount=1.7, both=True)
    return part.part


def model_22447_4062c6cb_0006():
    """Model: Circle switch Final v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6901441002, perimeter: 2.9449289535
            Circle(0.4687)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)
    return part.part


def model_22461_0ba0e480_0002():
    """Model: Washer v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.8142697574, perimeter: 6.5973445725
            with BuildLine():
                CenterArc((0, 0), 0.8, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


def model_22461_0ba0e480_0004():
    """Model: Valve Seat v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.6756634047, perimeter: 8.1681408993
            with BuildLine():
                CenterArc((0, 0), 1.1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


def model_22463_c48bb23e_0002():
    """Model: Base Part 2 v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 16, perimeter: 16
            with BuildLine():
                Line((2, -2), (2, 2))
                Line((2, 2), (-2, 2))
                Line((-2, 2), (-2, -2))
                Line((-2, -2), (2, -2))
            make_face()
        # OneSide extrude, distance=4
        extrude(amount=4)
    return part.part


def model_22524_0be3da8a_0000():
    """Model: Wrist Pin v2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0201112198, perimeter: 0.5027176564
            Circle(0.08001)
        # OneSide extrude, distance=0.79248
        extrude(amount=0.79248)
    return part.part


def model_22524_0be3da8a_0002():
    """Model: Connecting Rod Bottom v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.3380210301, perimeter: 3.6108009874
            with BuildLine():
                Line((-0.5842, 0), (-0.5842, -0.3302))
                Line((-0.5842, -0.3302), (-0.254, -0.3302))
                Line((-0.254, -0.3302), (-0.254, -0.47752))
                Line((0.254, -0.47752), (-0.254, -0.47752))
                Line((0.254, -0.3302), (0.254, -0.47752))
                Line((0.5842, -0.3302), (0.254, -0.3302))
                Line((0.5842, 0), (0.5842, -0.3302))
                Line((0.2794, 0), (0.5842, 0))
                CenterArc((0, 0), 0.2794, -180, 180)
                Line((-0.2794, 0), (-0.5842, 0))
            make_face()
        # OneSide extrude, distance=0.31623
        extrude(amount=0.31623)
    return part.part


def model_22524_0be3da8a_0007():
    """Model: Valve Flange v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.314158637, perimeter: 3.9898226701
            with BuildLine():
                CenterArc((0, 0), 0.39624, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.23876, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3175
        extrude(amount=0.3175)
    return part.part


def model_22534_e899f645_0005():
    """Model: 1016 - Handle Screw v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5296359925, perimeter: 4.5084996172
            with BuildLine():
                CenterArc((0, 0), 0.47625, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2413, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.47625
        extrude(amount=0.47625)
    return part.part


def model_22543_684108ff_0000():
    """Model: 8.5_Needle_Thimble v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1779523743, perimeter: 1.4953981031
            Circle(0.238)
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)
    return part.part


def model_22543_684108ff_0003():
    """Model: 6.2_Compression_Screw v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3166921744, perimeter: 1.994911335
            Circle(0.3175)
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)
    return part.part


def model_22543_684108ff_0011():
    """Model: 8.2_Jam_Nut v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.5740594769, perimeter: 6.3424131428
            with BuildLine():
                Line((0.6246009371, 0.1459931597), (0.1858666835, 0.6139168586))
                Line((0.1858666835, 0.6139168586), (-0.4387342536, 0.4679236989))
                Line((-0.4387342536, 0.4679236989), (-0.6246009371, -0.1459931597))
                Line((-0.6246009371, -0.1459931597), (-0.1858666835, -0.6139168586))
                Line((-0.1858666835, -0.6139168586), (0.4387342536, -0.4679236989))
                Line((0.4387342536, -0.4679236989), (0.6246009371, 0.1459931597))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3969, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.343
        extrude(amount=0.343)
    return part.part


def model_22543_684108ff_0016():
    """Model: 7.3_Stud v2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)
    return part.part


def model_22545_7c2ca3ce_0005():
    """Model: Cover Plate v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 64 constraints, 19 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 14.0531392648, perimeter: 25.7989643397
            with BuildLine():
                CenterArc((-0.95504, 5.08), 0.47752, 0, 180)
                Line((-1.43256, 5.08), (-1.43256, 4.9276178725))
                CenterArc((-1.91516, 4.9276178725), 0.4826, -90, 90)
                Line((-1.8999203789, 4.4450178725), (-1.91516, 4.4450178725))
                CenterArc((-1.89992, 3.9624178725), 0.4826, 90.0000449807, 89.9999885469)
                Line((-2.38252, 1.1176), (-2.38252, 3.9624175901))
                CenterArc((-1.89992, 1.1176), 0.4826, 180, 90)
                Line((-0.96012, 0.635), (-1.89992, 0.635))
                CenterArc((-0.96012, 0.1524), 0.4826, 0, 90)
                Line((-0.47752, 0), (-0.47752, 0.1524))
                CenterArc((0, 0), 0.47752, 180, 180)
                Line((0.47752, 0), (0.47752, 0.1524))
                CenterArc((0.96012, 0.1524), 0.4826, 90, 90)
                Line((0.94488, 0.635), (0.96012, 0.635))
                CenterArc((0.94488, 1.1176), 0.4826, -90, 89.9996394835)
                Line((1.42748, 1.905), (1.42748, 1.1175969634))
                Line((1.42748, 1.905), (1.1176000001, 1.905))
                Line((0.787185078, 1.9054660248), (1.1176000001, 1.905))
                CenterArc((0.7874000262, 2.0578658732), 0.1524, -179.9999954445, 89.9191842202)
                Line((0.635, 2.3876), (0.6350000262, 2.0578658611))
                Line((0.635, 2.3876), (0.635, 3.0225999737))
                CenterArc((0.7874, 3.0225999737), 0.1524, 90.0000045555, 89.9999954445)
                Line((0.7873999879, 3.1749999737), (1.1176, 3.175))
                Line((1.1176, 3.175), (1.42748, 3.175))
                Line((1.42748, 3.9624030366), (1.42748, 3.175))
                CenterArc((0.9448800002, 3.9624178725), 0.4826, -0.0017613675, 90.0017613933)
                Line((0.00508, 4.4450178725), (0.94488, 4.4450178725))
                CenterArc((0.00508, 4.9276178725), 0.4826, -180, 90)
                Line((-0.47752, 5.08), (-0.47752, 4.9276178725))
            make_face()
            with BuildLine():
                Line((-0.6400799976, 3.175), (-0.1523999821, 3.175))
                CenterArc((-0.1524, 3.0226), 0.1524, 0, 89.9999932637)
                Line((0, 3.0226), (0, 2.0574))
                CenterArc((-0.1524, 2.0574), 0.1524, -89.9999937982, 89.9999937982)
                Line((-0.1523999835, 1.905), (-0.6400800008, 1.905))
                CenterArc((-0.64008, 2.0574), 0.1524, 179.9999991347, 90.0000005698)
                Line((-0.79248, 2.0574000023), (-0.79248, 3.0226))
                CenterArc((-0.64008, 3.0226), 0.1524, 89.9999990919, 90.0000009081)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-0.95504, 5.08), 0.25527, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0), 0.25527, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.11684
        extrude(amount=0.11684)
    return part.part


def model_22545_7c2ca3ce_0006():
    """Model: Brake Lever v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7125573925, perimeter: 2.9923670025
            Circle(0.47625)
        # OneSide extrude, distance=9.525
        extrude(amount=9.525)
    return part.part


def model_22606_f1813fe7_0006():
    """Model: Solar v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 13.34593804, perimeter: 14.9158
            with BuildLine():
                Line((2.9812, -4.4767), (0, -4.4767))
                Line((2.9812, 0), (2.9812, -4.4767))
                Line((0, 0), (2.9812, 0))
                Line((0, -4.4767), (0, 0))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


def model_22607_5d64eeb2_0006():
    """Model: P5 v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            Circle(0.1)
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


def model_22611_35dd01a9_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 15 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 91.6539506536, perimeter: 39.3051853072
            with BuildLine():
                CenterArc((2.3485, 5.907), 1, 0, 90)
                Line((2.3485, 6.907), (-2.3485, 6.907))
                CenterArc((-2.3485, 5.907), 1, 90, 90)
                Line((-3.3485, 5.907), (-3.3485, -5.907))
                CenterArc((-2.3485, -5.907), 1, 180, 90)
                Line((-2.3485, -6.907), (2.3485, -6.907))
                CenterArc((2.3485, -5.907), 1, -90, 90)
                Line((3.3485, -5.907), (3.3485, 5.907))
            make_face()
        # Symmetric extrude, each_side=0.345
        extrude(amount=0.345, both=True)
    return part.part


def model_22624_7af10d7d_0005():
    """Model: plate_down v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 19 constraints, 19 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 21.5830531387, perimeter: 28.8256631033
            with BuildLine():
                Line((6, 0), (6, 2.2))
                CenterArc((5.7, 2.2), 0.3, 0, 90)
                Line((5.7, 2.5), (-2.6, 2.5))
                CenterArc((-2.6, 2.2), 0.3, 90, 90)
                Line((-2.9, 2.2), (-2.9, 0))
                Line((-2.9, 0), (6, 0))
            make_face()
            with BuildLine():
                CenterArc((5.55, 1), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.15, 1), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.3, 2), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1, 2), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-2.3, 2), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 21.5830531387, perimeter: 28.8256631033
            with BuildLine():
                CenterArc((-2.6, -2.2), 0.3, 180, 90)
                Line((5.7, -2.5), (-2.6, -2.5))
                CenterArc((5.7, -2.2), 0.3, -90, 90)
                Line((6, 0), (6, -2.2))
                Line((-2.9, 0), (6, 0))
                Line((-2.9, -2.2), (-2.9, 0))
            make_face()
            with BuildLine():
                CenterArc((5.55, -1), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.15, -1), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.3, -2), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1, -2), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-2.3, -2), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)
    return part.part


def model_22630_b6010fff_0001():
    """Model: Piston_Pin v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.8509953331, perimeter: 10.3672557568
            with BuildLine():
                CenterArc((0, 0), 1.1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.55, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=4
        extrude(amount=4, both=True)
    return part.part


def model_22630_b6010fff_0003():
    """Model: Rod_bush v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7225663103, perimeter: 14.4513262065
            with BuildLine():
                CenterArc((0, 0), 1.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=4.2
        extrude(amount=4.2)
    return part.part


def model_22630_b6010fff_0010():
    """Model: Piston_ring v1 (4)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.7805304826, perimeter: 57.8053048261
            with BuildLine():
                CenterArc((0, 0), 4.7, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 4.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


def model_22630_b6010fff_0011():
    """Model: Piston_Pin_Lower v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6361725124, perimeter: 8.4823001647
            with BuildLine():
                CenterArc((0, 0), 0.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.4
        extrude(amount=2.4)
    return part.part


def model_22657_bc1010fa_0007():
    """Model: P1-Floor"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 20 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 499.1415926536, perimeter: 88.2831853072
            with BuildLine():
                CenterArc((-11.5, 9), 1, 90, 90)
                Line((-12.5, -9), (-12.5, 9))
                CenterArc((-11.5, -9), 1, 180, 90)
                Line((11.5, -10), (-11.5, -10))
                CenterArc((11.5, -9), 1, -90, 90)
                Line((12.5, 9), (12.5, -9))
                CenterArc((11.5, 9), 1, 0, 90)
                Line((-11.5, 10), (11.5, 10))
            make_face()
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)
    return part.part


def model_22666_bdaa1303_0012():
    """Model: Nut5-40 v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1452734749, perimeter: 2.4641118053
            with BuildLine():
                Line((0.2756963005, 0), (0.1378481503, 0.23876))
                Line((0.1378481503, 0.23876), (-0.1378481503, 0.23876))
                Line((-0.1378481503, 0.23876), (-0.2756963005, 0))
                Line((-0.2756963005, 0), (-0.1378481503, -0.23876))
                Line((-0.1378481503, -0.23876), (0.1378481503, -0.23876))
                Line((0.1378481503, -0.23876), (0.2756963005, 0))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.128905, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.11938
        extrude(amount=0.11938)
    return part.part


def model_22666_bdaa1303_0013():
    """Model: Nut1-4-40 v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2839704298, perimeter: 4.5733892036
            with BuildLine():
                Line((0.2295025055, 0.39751), (-0.2295025055, 0.39751))
                Line((-0.2295025055, 0.39751), (-0.459005011, 0))
                Line((-0.459005011, 0), (-0.2295025055, -0.39751))
                Line((-0.2295025055, -0.39751), (0.2295025055, -0.39751))
                Line((0.2295025055, -0.39751), (0.459005011, 0))
                Line((0.459005011, 0), (0.2295025055, 0.39751))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.28956, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.11938
        extrude(amount=0.11938)
    return part.part


def model_22666_bdaa1303_0020():
    """Model: ConnectingRod v2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0785396593, perimeter: 1.994911335
            with BuildLine():
                CenterArc((0, 2.14376), 0.19812, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 2.14376), 0.11938, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1174953303, perimeter: 2.9843873572
            with BuildLine():
                CenterArc((0, 0), 0.27686, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.19812, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.3175
        extrude(amount=-0.3175)
    return part.part


def model_22670_9353c710_0003():
    """Model: P20-Link Bushing"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2513274123, perimeter: 2.5132741229
            with BuildLine():
                CenterArc((7, 2), 0.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((7, 2), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.25
        extrude(amount=0.25)
    return part.part


def model_22687_6f36672c_0000():
    """Model: shift v6"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 69 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 40.2470845583, perimeter: 68.1770042553
            with BuildLine():
                CenterArc((-2.8271028384, -2.7611403944), 1.2310739567, -179.9999994012, 89.99999956)
                Line((2.8271028842, -3.9922143498), (-2.827102835, -3.9922143511))
                CenterArc((2.8271028546, -2.7611404102), 1.2310739396, -89.999998619, 89.9999976012)
                Line((4.0581767815, 2.761140418), (4.0581767941, -2.761140432))
                CenterArc((2.8271028384, 2.7611404102), 1.2310739431, 0.0000003641, 89.9999995163)
                Line((-2.8271028223, 3.992214352), (2.827102841, 3.9922143533))
                CenterArc((-2.8271028546, 2.7611404102), 1.2310739418, 89.9999984969, 90.000000358)
                Line((-4.0581767951, -2.7611404072), (-4.0581767964, 2.7611404348))
            make_face()
            with BuildLine():
                Line((-0.635, -2.5865243318), (-0.635, -0.8152889719))
                CenterArc((-0.889, -0.8152889719), 0.254, 0, 90)
                Line((-1.3031028539, -0.5612889719), (-0.889, -0.5612889719))
                CenterArc((-1.3031028539, -0.8152889719), 0.254, 90, 90.0000001578)
                Line((-1.5571028539, -0.8152889726), (-1.5571028492, -2.5071403977))
                CenterArc((-1.8111028492, -2.5071403984), 0.254, -90.0000002266, 90.0000003845)
                Line((-1.8111028502, -2.7611403984), (-2.5731028409, -2.7611403954))
                CenterArc((-2.5731028399, -2.5071403954), 0.254, -179.999999665, 89.9999994383)
                Line((-2.8271028399, -2.5071403969), (-2.8271028546, 0))
                Line((-2.8271028546, 2.5071404102), (-2.8271028546, 0))
                CenterArc((-2.5731028546, 2.5071404102), 0.254, 90, 90)
                Line((-1.8111028546, 2.7611404102), (-2.5731028546, 2.7611404102))
                CenterArc((-1.8111028546, 2.5071404102), 0.254, 0, 90)
                Line((-1.5571028546, 0.8152889719), (-1.5571028546, 2.5071404102))
                CenterArc((-1.3031028546, 0.8152889719), 0.254, -180, 90)
                Line((-1.3031028546, 0.5612889719), (-0.889, 0.5612889719))
                CenterArc((-0.889, 0.8152889719), 0.254, -90, 90)
                Line((-0.635, 2.5865243318), (-0.635, 0.8152889719))
                CenterArc((-0.381, 2.5865243318), 0.254, 90, 90)
                Line((0, 2.8405243318), (-0.381, 2.8405243318))
                Line((0, 2.8405243318), (0.381, 2.8405243318))
                CenterArc((0.381, 2.5865243318), 0.254, 0, 90)
                Line((0.635, 2.5865243318), (0.635, 0.8152889719))
                CenterArc((0.889, 0.8152889719), 0.254, -180, 90)
                Line((1.3031028546, 0.5612889719), (0.889, 0.5612889719))
                CenterArc((1.3031028546, 0.8152889719), 0.254, -90, 90)
                Line((1.5571028546, 0.8152889719), (1.5571028546, 2.5071404016))
                CenterArc((1.8111028546, 2.5071404016), 0.254, 90.0000004862, 89.9999995138)
                Line((1.8111028524, 2.7611404016), (2.5731028377, 2.761140408))
                CenterArc((2.5731028399, 2.507140408), 0.254, 0.000000335, 90.0000001512)
                Line((2.8271028399, 2.5071404095), (2.8271028546, 0))
                Line((2.8271028546, -2.507140408), (2.8271028546, 0))
                CenterArc((2.5731028546, -2.507140408), 0.254, -90.0000004862, 90.0000004862)
                Line((1.8111028524, -2.7611404016), (2.5731028524, -2.761140408))
                CenterArc((1.8111028546, -2.5071404016), 0.254, 180, 89.9999995138)
                Line((1.5571028546, -0.8152889719), (1.5571028546, -2.5071404016))
                CenterArc((1.3031028546, -0.8152889719), 0.254, 0, 90)
                Line((1.3031028546, -0.5612889719), (0.889, -0.5612889719))
                CenterArc((0.889, -0.8152889719), 0.254, 90, 90)
                Line((0.635, -2.5865243318), (0.635, -0.8152889719))
                CenterArc((0.381, -2.5865243318), 0.254, -90, 90)
                Line((0.381, -2.8405243318), (-0.381, -2.8405243318))
                CenterArc((-0.381, -2.5865243318), 0.254, 180, 90)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.016
        extrude(amount=1.016)
    return part.part


def model_22711_33843a5d_0000():
    """Model: Washer 35mm v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.6105082033, perimeter: 16.0221225333
            with BuildLine():
                CenterArc((0, 0), 1.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


def model_22711_33843a5d_0008():
    """Model: Adjustable Strip v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1, perimeter: 5.4135116758
            with BuildLine():
                Line((0.9326153163, 2), (0, 0))
                Line((0, 0), (0.5, 0))
                Line((0.5, 0), (1.4326153163, 2))
                Line((1.4326153163, 2), (0.9326153163, 2))
            make_face()
        # OneSide extrude, distance=23.2
        extrude(amount=23.2)
    return part.part


def model_22734_f6bad9f7_0023():
    """Model: Wrist Pins v2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0791730436, perimeter: 0.9974556675
            Circle(0.15875)
        # OneSide extrude, distance=1.11125
        extrude(amount=1.11125)
    return part.part


def model_22734_f6bad9f7_0026():
    """Model: Connecting Rods v2 (3)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5344180444, perimeter: 4.4885505038
            with BuildLine():
                CenterArc((0, 0), 0.47625, 30.264992611, 299.470014778)
                CenterArc((0, 0), 0.47625, -30.264992611, 60.529985222)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.238125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.9597042095, perimeter: 5.8029751556
            with BuildLine():
                CenterArc((0, 0), 0.47625, -30.264992611, 60.529985222)
                Line((0.4113388647, -0.24003), (2.8936869343, -0.15875))
                CenterArc((3.16865, 0), 0.3175, 150, 60)
                Line((0.4113388647, 0.24003), (2.8936869343, 0.15875))
            make_face()
            # Profile area: 0.2375191308, perimeter: 2.9923670025
            with BuildLine():
                CenterArc((3.16865, 0), 0.3175, 150, 60)
                CenterArc((3.16865, 0), 0.3175, -150, 300)
            make_face()
            with BuildLine():
                CenterArc((3.16865, 0), 0.15875, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.47625
        extrude(amount=0.47625)
    return part.part


def model_22742_3c107495_0014():
    """Model: Rod v3 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.5393804003, perimeter: 4.398229715
            with BuildLine():
                CenterArc((0, 0), 0.7, 107.2751685363, 183.3693692859)
                CenterArc((0, 0), 0.7, -69.3554621778, 69.3554621778)
                CenterArc((0, 0), 0.7, 0, 107.2751685363)
            make_face()
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with BuildLine():
                CenterArc((5.5, 0), 0.4, 66.8561132819, 113.1438867181)
                CenterArc((5.5, 0), 0.4, -180, 75.313878967)
                CenterArc((5.5, 0), 0.4, -104.686121033, 171.5422343149)
            make_face()
            # Profile area: 0.9976526924, perimeter: 11.0145390489
            with BuildLine():
                CenterArc((5.5, 0), 0.4, -180, 75.313878967)
                Line((0.7, 0), (5.1, 0))
                CenterArc((0, 0), 0.7, -69.3554621778, 69.3554621778)
                CenterArc((3.2436363636, -8.6092289516), 8.5, 75.313855911, 35.3306818605)
            make_face()
            # Profile area: 4.3855280061, perimeter: 12.496864609
            with BuildLine():
                CenterArc((0, 0), 0.7, 0, 107.2751685363)
                Line((0.7, 0), (5.1, 0))
                CenterArc((5.5, 0), 0.4, 66.8561132819, 113.1438867181)
                CenterArc((2.3163636364, -7.4481178498), 8.5, 66.8561149831, 40.4195290262)
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)
    return part.part


def model_22743_64aefcb6_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 14 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1977.5675882443, perimeter: 234.2050493005
            with BuildLine():
                Line((0, 0), (0, 73.66))
                Line((0, 73.66), (-27.94, 73.66))
                Line((-27.94, 73.66), (-27.94, 68.57999897))
                CenterArc((-95.2499950123, 41.90999897), 72.4011348568, -21.6147803968, 43.2295607935)
                Line((-27.94, 15.23999897), (-28.575, 15.23999897))
                Line((-28.575, 15.23999897), (-28.575, 12.69999897))
                CenterArc((-28.5907570541, 10.1177724164), 2.5822746289, 89.6503786671, 90)
                Line((-31.1729836077, 10.1335294705), (-31.8079836077, 10.1335294705))
                Line((-31.8079836077, 10.1335294705), (-31.8079836077, 7.5935294705))
                CenterArc((-44.7733019395, 21.4474810083), 18.9744947933, -85.183158322, 38.2854067397)
                CenterArc((-43.3866771677, 0.2066771854), 2.3424583024, 84.9381447587, 100.1236949937)
                Line((0, 0), (-45.72, 0))
            make_face()
        # OneSide extrude, distance=3.81
        extrude(amount=3.81)
    return part.part


def model_22751_90a6225a_0000():
    """Model: TAco C v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2827433388, perimeter: 5.6548667765
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.45
        extrude(amount=1.45)
    return part.part


def model_22751_90a6225a_0002():
    """Model: taco v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2179479903, perimeter: 5.8119464091
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.425, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)
    return part.part


def model_22751_90a6225a_0010():
    """Model: Taco E v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.3455751919, perimeter: 6.9115038379
            with BuildLine():
                CenterArc((0, 0), 0.6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


def model_22753_071ecad9_0003():
    """Model: 8. C washer"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 9 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-2.7454300033, -0.8398345188, -0.0504528522), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 16.0985215064, perimeter: 21.2349540447
            with BuildLine():
                CenterArc((-8.3310934503, 2.686354131), 2.5, 13.8865403626, 332.2269192747)
                Line((-5.9041612304, 2.086354131), (-8.3310934503, 2.086354131))
                CenterArc((-8.3310934503, 2.686354131), 0.6, 90, 180)
                Line((-5.9041612304, 3.286354131), (-8.3310934503, 3.286354131))
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)
    return part.part


def model_22756_fc3fdda5_0019():
    """Model: Washer 3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.9066636398, perimeter: 4.9008845396
            with BuildLine():
                CenterArc((0, 0), 0.575, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.205, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.17
        extrude(amount=0.17)
    return part.part


def model_22756_fc3fdda5_0024():
    """Model: Washer 2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.9066636398, perimeter: 4.9008845396
            with BuildLine():
                CenterArc((0, 0), 0.575, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.205, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.07
        extrude(amount=0.07)
    return part.part


def model_22760_c2a5214f_0000():
    """Model: Motor Mouting Plate v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 21 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 22.0853963547, perimeter: 42.0973415581
            with BuildLine():
                CenterArc((0, 0), 3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.9, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.6, 1.6), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.6, 1.6), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.6, -1.6), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.6, -1.6), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 1.6), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.6, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, -1.6), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.6, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_22760_c2a5214f_0011():
    """Model: Mount Retainer v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 11 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 5.2649477914, perimeter: 12.3222787933
            with BuildLine():
                Line((0, 0.9930285886), (0, 1.7930285886))
                Line((0, 1.7930285886), (-2, 1.7930285886))
                Line((-2, 1.7930285886), (-2, -1.6))
                Line((-2, -1.6), (0, -1.6))
                Line((0, -1.6), (0, -0.8))
                Line((0, -0.8), (-0.91, -0.8))
                Line((-0.91, -0.8), (-0.91, 0.6))
                CenterArc((0, -0.2569714114), 1.25, 90, 46.7189879976)
            make_face()
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)
    return part.part


def model_22776_facf9bcf_0007():
    """Model: Base v2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 53.3613465165, perimeter: 41.2620858881
            with BuildLine():
                CenterArc((0.0086036883, 6.1999940304), 2, 12.0239399693, 155.7931022585)
                Line((-1.9463537279, 6.6220621536), (-3.2256797368, 0.6964124033))
                CenterArc((0, 0), 3.3, 167.8170422278, 204.2068977415)
                Line((1.964724975, 6.616634777), (3.227600123, 0.687457232))
            make_face()
            with BuildLine():
                CenterArc((1.1086036883, 5.1999940304), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.1086036883, 4.1999940304), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0), 0.7, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.0086036883, 6.1999940304), 0.7, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)
    return part.part


def model_22776_facf9bcf_0009():
    """Model: Bloqueo v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.4085080677, perimeter: 18.2343527833
            with BuildLine():
                Line((-1.3249792268, -0.1), (-0.894427191, -0.1))
                CenterArc((0, 0), 0.9, -173.6206297916, 180)
                Line((3.5677743047, 0.7521366066), (0.894427191, 0.1))
                CenterArc((3.55, 0.825), 0.075, -76.2910014583, 166.2910014583)
                Line((-2.9, 0.9), (3.55, 0.9))
                Line((-2.9, 0.9), (-3.3, 0.1))
                Line((-3.3, 0.1), (-1.6429538051, 0.1994610401))
                CenterArc((-1.6249792268, -0.1), 0.3, 0, 93.4349488229)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.55
        extrude(amount=0.55)
    return part.part


def model_22788_b6a9e30a_0000():
    """Model: Top2 v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2420, perimeter: 201
            with BuildLine():
                Line((-30.25, 20), (30.25, 20))
                Line((-30.25, -20), (-30.25, 20))
                Line((30.25, -20), (-30.25, -20))
                Line((30.25, 20), (30.25, -20))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


def model_22788_b6a9e30a_0004():
    """Model: Leg v2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9, perimeter: 12
            with BuildLine():
                Line((-1.5, 1.5), (1.5, 1.5))
                Line((-1.5, -1.5), (-1.5, 1.5))
                Line((1.5, -1.5), (-1.5, -1.5))
                Line((1.5, 1.5), (1.5, -1.5))
            make_face()
        # OneSide extrude, distance=53.5
        extrude(amount=53.5)
    return part.part


def model_22788_b6a9e30a_0005():
    """Model: BottomStorageBack v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3135, perimeter: 224
            with BuildLine():
                Line((-28.5, 27.5), (28.5, 27.5))
                Line((-28.5, -27.5), (-28.5, 27.5))
                Line((28.5, -27.5), (-28.5, -27.5))
                Line((28.5, 27.5), (28.5, -27.5))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


def model_22788_b6a9e30a_0006():
    """Model: BottomStorageSupport v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4125, perimeter: 260
            with BuildLine():
                Line((-37.5, 27.5), (37.5, 27.5))
                Line((-37.5, -27.5), (-37.5, 27.5))
                Line((37.5, -27.5), (-37.5, -27.5))
                Line((37.5, 27.5), (37.5, -27.5))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


def model_22788_b6a9e30a_0007():
    """Model: Triangle v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 15, perimeter: 23
            with BuildLine():
                Line((0, 0), (-1.5, 0))
                Line((0, 10), (0, 0))
                Line((-1.5, 10), (0, 10))
                Line((-1.5, 0), (-1.5, 10))
            make_face()
            # Profile area: 300.0018993273, perimeter: 130.8283798655
            with BuildLine():
                Line((-1.5, 0), (-1.5, 10))
                Line((-61.5003798655, 10), (-1.5, 10))
                Line((-1.5, 0), (-61.5003798655, 10))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


def model_22788_b6a9e30a_0009():
    """Model: Top 1 v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3580, perimeter: 259
            with BuildLine():
                Line((-44.75, 20), (44.75, 20))
                Line((-44.75, -20), (-44.75, 20))
                Line((44.75, -20), (-44.75, -20))
                Line((44.75, 20), (44.75, -20))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


def model_22788_b6a9e30a_0010():
    """Model: Shelf v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2252.25, perimeter: 194
            with BuildLine():
                Line((-29.25, 19.25), (29.25, 19.25))
                Line((-29.25, -19.25), (-29.25, 19.25))
                Line((29.25, -19.25), (-29.25, -19.25))
                Line((29.25, 19.25), (29.25, -19.25))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


def model_22790_2bdc9e13_0004():
    """Model: Mid-Top"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 163.306125, perimeter: 175.26
            with BuildLine():
                Line((-0.9525, 184.785), (-0.9525, 182.88))
                Line((-0.9525, 182.88), (84.7725, 182.88))
                Line((84.7725, 182.88), (84.7725, 184.785))
                Line((84.7725, 184.785), (-0.9525, 184.785))
            make_face()
        # OneSide extrude, distance=-45.72
        extrude(amount=-45.72)
    return part.part


def model_22790_2bdc9e13_0005():
    """Model: Shelf"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1415.31975, perimeter: 204.47
            with BuildLine():
                Line((-116.9776122385, 3.8100001907), (-116.9776122385, -12.6999998093))
                Line((-116.9776122385, -12.6999998093), (-31.2526122385, -12.6999998093))
                Line((-31.2526122385, -12.6999998093), (-31.2526122385, 3.8100001907))
                Line((-31.2526122385, 3.8100001907), (-116.9776122385, 3.8100001907))
            make_face()
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)
    return part.part


def model_22790_2bdc9e13_0010():
    """Model: Back"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 17.93875), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 15840.6941250002, perimeter: 541.02
            with BuildLine():
                Line((-0.9525, 183.8325), (84.7725, 183.8325))
                Line((-0.9525, -0.9525), (-0.9525, 183.8325))
                Line((84.7725, -0.9525), (-0.9525, -0.9525))
                Line((84.7725, 183.8325), (84.7725, -0.9525))
            make_face()
        # OneSide extrude, distance=-1.27
        extrude(amount=-1.27)
    return part.part


def model_22848_cc91b848_0006():
    """Model: Bottom Tray v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5109.8688125, perimeter: 321.945
            with BuildLine():
                Line((58.7375, -21.74875), (-58.7375, -21.74875))
                Line((58.7375, 21.74875), (58.7375, -21.74875))
                Line((-58.7375, 21.74875), (58.7375, 21.74875))
                Line((-58.7375, -21.74875), (-58.7375, 21.74875))
            make_face()
        # OneSide extrude, distance=1.905
        extrude(amount=1.905)
    return part.part


def model_22848_cc91b848_0034():
    """Model: Bottom Bracket v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 12 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.4524684528, perimeter: 8.3059332196
            with BuildLine():
                Line((-0.9525, 1.5875), (-0.4576459479, -0.1306209478))
                CenterArc((0, 0.0011904663), 0.47625, -163.9325149401, 147.8650298802)
                Line((0.9525, 1.5875), (0.4576459479, -0.1306209478))
                Line((0.9525, 1.5875), (-0.9525, 1.5875))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.254, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.15875
        extrude(amount=0.15875)
    return part.part


def model_22899_5b97e4f5_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.2698006922, perimeter: 5.3407075111
            Circle(0.85)
        # OneSide extrude, distance=5.5
        extrude(amount=5.5)
    return part.part


def model_23001_234eee16_0001():
    """Model: Detent v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.8827433388, perimeter: 3.8849555922
            with BuildLine():
                CenterArc((0, -0.5), 0.3, 180, 180)
                Line((0.3, -0.5), (0.3, 0.5))
                CenterArc((0, 0.5), 0.3, 0, 180)
                Line((-0.3, 0.5), (-0.3, -0.5))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


def model_23001_234eee16_0003():
    """Model: Double Gimbal (Double Cardan) v3"""
    with BuildPart() as part:
        # Sketch3 -> Extrude3 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            Circle(2)
        # Symmetric extrude, each_side=4
        extrude(amount=4, both=True)
    return part.part


def model_23001_234eee16_0004():
    """Model: Gimbal v4"""
    with BuildPart() as part:
        # Sketch3 -> Extrude3 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            Circle(2)
        # OneSide extrude, distance=6
        extrude(amount=6)
    return part.part


def model_23001_234eee16_0006():
    """Model: Knuckle v2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.8013271108, perimeter: 6.9115038379
            Circle(1.1)
        # TwoSides extrude (symmetric), distance=0.7
        extrude(amount=0.7, both=True)
    return part.part


def model_23044_9a964a68_0007():
    """Model: PVC Pipe 0.5in v3 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.3085592748, perimeter: 10.6927247558
            with BuildLine():
                CenterArc((0, 0), 1.0668, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.635, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=27.94
        extrude(amount=27.94)
    return part.part


def model_23054_311abee4_0005():
    """Model: P6,10-Piston 1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude6 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 43 constraints, 20 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3926990817, perimeter: 2.5707963268
            with BuildLine():
                CenterArc((0, -1), 0.5, 90, 180)
                Line((0, -0.5), (0, -1.5))
            make_face()
            # Profile area: 0.3926990817, perimeter: 2.5707963268
            with BuildLine():
                Line((0, -0.5), (0, -1.5))
                CenterArc((0, -1), 0.5, -90, 180)
            make_face()
        # Symmetric extrude, each_side=1.95
        extrude(amount=1.95, both=True)
    return part.part


def model_23054_311abee4_0006():
    """Model: P7,11-Piston 2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude6 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 31 constraints, 17 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3926990817, perimeter: 2.5707963268
            with BuildLine():
                Line((0, -0.5), (0, -1.5))
                CenterArc((0, -1), 0.5, 90, 180)
            make_face()
            # Profile area: 0.3926990817, perimeter: 2.5707963268
            with BuildLine():
                CenterArc((0, -1), 0.5, -90, 180)
                Line((0, -0.5), (0, -1.5))
            make_face()
        # Symmetric extrude, each_side=1.3
        extrude(amount=1.3, both=True)
    return part.part


def model_23127_38d73061_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 82 constraints, 26 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1015.4329653927, perimeter: 307.8833850598
            with BuildLine():
                Line((17.7849819965, 43.9826884242), (32.7758444017, 43.4591959736))
                Line((15.7862003425, 44.0524874176), (17.7849819965, 43.9826884242))
                Line((15.7862003425, 44.0524874176), (8.5032782826, 44.30681266))
                Line((5.9729437494, 44.0854370735), (8.5032782826, 44.30681266))
                Line((5.5665123279, 48.7309694796), (5.9729437494, 44.0854370735))
                Line((8.096846861, 48.9523450662), (5.5665123279, 48.7309694796))
                Line((7.9225353755, 50.9447344624), (8.096846861, 48.9523450662))
                Line((5.3922008424, 50.7233588758), (7.9225353755, 50.9447344624))
                Line((5, 55.2062350172), (5.3922008424, 50.7233588758))
                Line((7.5303345332, 55.4276106038), (5, 55.2062350172))
                Line((7.3560230477, 57.42), (7.5303345332, 55.4276106038))
                Line((7.3560230477, 57.42), (5.3716300128, 57.2463881055))
                CenterArc((5.7202532994, 53.2616093402), 4.0000000005, 95.0000045382, 82.9999696944)
                Line((0.0024366902, 4.1395979394), (1.7226900536, 53.4012091248))
                CenterArc((4.0000000005, 4.0000000005), 4.0000000005, 178.0000006881, 175.9999993119)
                Line((11.0165508622, 32.4909298633), (7.9780875825, 3.5818861474))
                CenterArc((14.9946383213, 32.0728148403), 4.0000000005, 87.999999937, 85.9999832142)
                Line((24.0060619048, 35.7605671723), (15.1342363125, 36.0703781488))
                CenterArc((23.8664638554, 31.7630038659), 4.0000000005, 17.0000128255, 70.9999862764)
                Line((36.8949460013, 2.8299734051), (27.6916826179, 32.9324915412))
                CenterArc((40.7199999995, 4.0000000005), 4.0000000404, -162.9919149959, 175.9919149959)
                Line((38.1458985628, 32.9313042041), (44.6174802979, 4.899804227))
                CenterArc((42.0433790332, 33.8311075087), 4.0000000005, 99.5217717182, 93.4782148623)
                CenterArc((40.7199999995, 41.7208900121), 4.0000000005, -80.4782273052, 168.4779728544)
                Line((40.7709710179, 43.18), (40.8596157395, 45.7184527007))
                Line((34.7746260558, 43.3893969802), (40.7709710179, 43.18))
                Line((32.7758444017, 43.4591959736), (34.7746260558, 43.3893969802))
            make_face()
            with BuildLine():
                Line((31.5843637425, 39.154509974), (34.0592637071, 39.725885652))
                Line((34.0592637071, 39.725885652), (34.6306393851, 37.2509856875))
                Line((34.6306393851, 37.2509856875), (32.1557394206, 36.6796100094))
                Line((32.1557394206, 36.6796100094), (31.5843637425, 39.154509974))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((38.0449580233, 11.1706017134), (38.6163337013, 8.6957017488))
                Line((40.5198579878, 11.7419773914), (38.0449580233, 11.1706017134))
                Line((41.0912336659, 9.2670774268), (40.5198579878, 11.7419773914))
                Line((38.6163337013, 8.6957017488), (41.0912336659, 9.2670774268))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((3.1046619508, 8.7843464694), (3.0160172, 6.2458938))
                Line((5.6431146212, 8.6957017488), (3.1046619508, 8.7843464694))
                Line((5.5544699006, 6.1572490784), (5.6431146212, 8.6957017488))
                Line((3.0160172, 6.2458938), (5.5544699006, 6.1572490784))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((4.1075323875, 37.5027991711), (6.6459850881, 37.4141544494))
                Line((6.6459850881, 37.4141544494), (6.5573403665, 34.8757017488))
                Line((6.5573403665, 34.8757017488), (4.0188876659, 34.9643464704))
                Line((4.0188876659, 34.9643464704), (4.1075323875, 37.5027991711))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 5.0800000001, perimeter: 9.0800000001
            with BuildLine():
                Line((32.7758444017, 43.4591959736), (32.8644891233, 45.9976486743))
                Line((32.7758444017, 43.4591959736), (34.7746260558, 43.3893969802))
                Line((34.8632707774, 45.9278496809), (34.7746260558, 43.3893969802))
                Line((32.8644891233, 45.9976486743), (34.8632707774, 45.9278496809))
            make_face()
            # Profile area: 5.08, perimeter: 9.08
            with BuildLine():
                Line((15.7862003425, 44.0524874176), (17.7849819965, 43.9826884242))
                Line((17.8736267181, 46.5211411248), (17.7849819965, 43.9826884242))
                Line((15.874845064, 46.5909401182), (17.8736267181, 46.5211411248))
                Line((15.7862003425, 44.0524874176), (15.874845064, 46.5909401182))
            make_face()
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)
    return part.part


def model_23137_e55b73cb_0005():
    """Model: Bearing_Shaft v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=6.35
        extrude(amount=6.35)
    return part.part


def model_23144_88ca00a5_0002():
    """Model: Inside Door v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2258.06, perimeter: 190.5
            with BuildLine():
                Line((-25.4, 22.225), (-25.4, -22.225))
                Line((-25.4, -22.225), (25.4, -22.225))
                Line((25.4, -22.225), (25.4, 22.225))
                Line((25.4, 22.225), (-25.4, 22.225))
            make_face()
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)
    return part.part


def model_23144_88ca00a5_0003():
    """Model: bottom inside door v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1161.288, perimeter: 147.32
            with BuildLine():
                Line((25.4, -11.43), (-25.4, -11.43))
                Line((25.4, 11.43), (25.4, -11.43))
                Line((-25.4, 11.43), (25.4, 11.43))
                Line((-25.4, -11.43), (-25.4, 11.43))
            make_face()
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)
    return part.part


def model_23179_729dc326_0001():
    """Model: handle v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.2146018366, perimeter: 14.1415926536
            with BuildLine():
                Line((-8.5, 1), (-5, 1))
                Line((-8.5, -1), (-8.5, 1))
                Line((-5, -1), (-8.5, -1))
                Line((-5, 1), (-5, -1))
            make_face()
            with BuildLine():
                CenterArc((-7.5, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.5026548246, perimeter: 5.0265482457
            with BuildLine():
                CenterArc((-7.5, 0), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-7.5, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-7.5, 0)):
                Circle(0.3)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)
    return part.part


def model_23179_729dc326_0004():
    """Model: mount_base v16"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 45 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 295.731715231, perimeter: 92.2141791795
            with BuildLine():
                CenterArc((0, 0), 10, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 8, 172.5, 15)
                CenterArc((-8.4272813217, -1.1094726339), 0.5, -172.5, 180)
                CenterArc((0, 0), 9, 172.5, 15)
                CenterArc((-8.4272813217, 1.1094726339), 0.5, -7.5, 180)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0), 8, -7.5, 15)
                CenterArc((8.4272813217, 1.1094726339), 0.5, 7.5, 180)
                CenterArc((0, 0), 9, -7.5, 15)
                CenterArc((8.4272813217, -1.1094726339), 0.5, 172.5, 180)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0), 5.0289163843, -107.3540246363, 34.7080492725)
                Line((1.5, -4.8), (2.4277825508, -7.7689041625))
                CenterArc((0, 0), 8.139410298, -107.3540246363, 34.7080492725)
                Line((-1.5, -4.8), (-2.4277825508, -7.7689041625))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)
    return part.part


def model_23182_1e6e757d_0000():
    """Model: UpperFinMount"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 40 constraints, 18 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.123), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.8103650459, perimeter: 6.1849555922
            with BuildLine():
                Line((0.3932570722, 7.8), (-0.0067429278, 7.8))
                CenterArc((0.3932570722, 7.9), 0.1, -90, 89.9999999999)
                Line((0.4932570722, 8.4), (0.4932570722, 7.9))
                CenterArc((0.3932570722, 8.4), 0.1, -0.0000000001, 90.0000000001)
                Line((0.3432570722, 8.5), (0.3932570722, 8.5))
                CenterArc((0.3432570722, 8.6), 0.1, -180, 90)
                Line((0.2432570722, 9), (0.2432570722, 8.6))
                CenterArc((0.3432570722, 9), 0.1, 90, 90)
                Line((0.3432570722, 9.1), (0.3932570722, 9.1))
                CenterArc((0.3932570722, 9.2), 0.1, -90, 90)
                Line((0.4932570722, 9.7), (0.4932570722, 9.2))
                CenterArc((0.3932570722, 9.7), 0.1, 0, 90)
                Line((-0.0067429278, 9.8), (0.3932570722, 9.8))
                Line((-0.0067429278, 9.8), (-0.0067429278, 7.8))
            make_face()
            with BuildLine():
                CenterArc((0.2432570722, 8.15), 0.075, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.2432570722, 9.45), 0.075, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2941203553, perimeter: 4.2939822369
            with BuildLine():
                CenterArc((-0.0067429278, 7.9), 0.1, 180, 90)
                Line((-0.0067429278, 9.8), (-0.0067429278, 7.8))
                CenterArc((-0.0067429278, 9.7), 0.1, 90, 90)
                Line((-0.1067429278, 9.24), (-0.1067429278, 9.7))
                CenterArc((-0.2467429278, 9.24), 0.14, -90, 90)
                Line((-0.2567429278, 9.1), (-0.2467429278, 9.1))
                Line((-0.2567429278, 9.1), (-0.2567429278, 8.5))
                Line((-0.2567429278, 8.5), (-0.2467429278, 8.5))
                CenterArc((-0.2467429278, 8.36), 0.14, 0, 90)
                Line((-0.1067429278, 7.9), (-0.1067429278, 8.36))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


def model_23190_7d4ff7f9_0005():
    """Model: Cover Plug v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.9173043609, perimeter: 9.9745566751
            Circle(1.5875)
        # OneSide extrude, distance=0.254
        extrude(amount=0.254)
    return part.part


def model_23206_b99a5251_0036():
    """Model: 1_003-a v5 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 16 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 9.9707963268, perimeter: 15.9415926536
            with BuildLine():
                Line((-2.5, 0), (2.5, 0))
                Line((2.5, 0), (2.5, 1.2))
                Line((2.5, 1.2), (1, 1.2))
                Line((1, 1.2), (1, 2.4))
                CenterArc((0, 2.4), 1, 0, 180)
                Line((-1, 1.2), (-1, 2.4))
                Line((-2.5, 1.2), (-1, 1.2))
                Line((-2.5, 0), (-2.5, 1.2))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_23206_b99a5251_0040():
    """Model: 0_005-a v3"""
    with BuildPart() as part:
        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.5783312984, perimeter: 4.6765371804
            with BuildLine():
                Line((0.3897114317, 0.675), (-0.3897114317, 0.675))
                Line((-0.3897114317, 0.675), (-0.7794228634, 0))
                Line((-0.7794228634, 0), (-0.3897114317, -0.675))
                Line((-0.3897114317, -0.675), (0.3897114317, -0.675))
                Line((0.3897114317, -0.675), (0.7794228634, 0))
                Line((0.7794228634, 0), (0.3897114317, 0.675))
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)
    return part.part


def model_23206_b99a5251_0042():
    """Model: 1_004-a v6 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 18 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 8.2994340212, perimeter: 17.468123494
            with BuildLine():
                Line((-1.25, 5), (1.25, 5))
                Line((-1.25, 5), (-1.25, 3.5))
                Line((-1.25, 3.5), (-2.25, 3.5))
                Line((-2.25, 3.5), (-2.25, 3.3545750844))
                CenterArc((-2.5746925002, 1.9316740783), 1.4594767874, 24.2617559466, 52.8839858336)
                CenterArc((0, 2.6524828039), 1.25, -174.4404154314, 168.8808308628)
                CenterArc((2.5746925002, 1.9316740783), 1.4594767874, 102.8542582197, 52.8839858336)
                Line((2.25, 3.5), (2.25, 3.3545750844))
                Line((1.25, 3.5), (2.25, 3.5))
                Line((1.25, 5), (1.25, 3.5))
            make_face()
            with BuildLine():
                CenterArc((0, 2.6524828039), 0.525, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_23206_b99a5251_0046():
    """Model: 1_015-a v7"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 19 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.52, perimeter: 17.6
            with BuildLine():
                Line((1.3, -1.3), (-1.3, -1.3))
                Line((1.3, -1.3), (1.3, 1.3))
                Line((-1.3, 1.3), (1.3, 1.3))
                Line((-1.3, -1.3), (-1.3, 1.3))
            make_face()
            with BuildLine():
                Line((0.9, 0.9), (-0.9, 0.9))
                Line((0.9, 0.9), (0.9, -0.9))
                Line((-0.9, -0.9), (0.9, -0.9))
                Line((-0.9, 0.9), (-0.9, -0.9))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.9
        extrude(amount=0.9)
    return part.part


def model_23231_efe613bb_0001():
    """Model: Rod 8mm v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=30
        extrude(amount=30)
    return part.part


def model_23231_efe613bb_0005():
    """Model: X carriage adapter v5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 37.5258230559, perimeter: 30.077875658
            with BuildLine():
                Line((5.6, -6.8), (0, -6.8))
                Line((5.6, 0), (5.6, -6.8))
                Line((0, 0), (5.6, 0))
                Line((0, -6.8), (0, 0))
            make_face()
            with BuildLine():
                CenterArc((4.35, -4.525), 0.21, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.35, -2.275), 0.21, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.25, -2.275), 0.21, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.25, -4.525), 0.21, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.8
        extrude(amount=2.8)
    return part.part


def model_23231_efe613bb_0011():
    """Model: Nema black v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.1349544844, perimeter: 7.900502557
            with BuildLine():
                Line((0, -0.7), (0.7, 0))
                Line((0, -2.105), (0, -0.7))
                Line((1.85, -2.105), (0, -2.105))
                CenterArc((2.105, -2.105), 0.255, 90, 90)
                Line((2.105, 0), (2.105, -1.85))
                Line((0.7, 0), (2.105, 0))
            make_face()
        # OneSide extrude, distance=3.15
        extrude(amount=3.15)
    return part.part


def model_23231_efe613bb_0016():
    """Model: Prusa i3 adapter plate v6"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 14 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 56.3698721099, perimeter: 53.8725648563
            with BuildLine():
                Line((5.6, 0), (5.6, -11.1))
                Line((5.6, 0), (0, 0))
                Line((0, -11.1), (0, 0))
                Line((5.6, -11.1), (0, -11.1))
            make_face()
            with BuildLine():
                Line((0.6500000097, -2.8000000417), (0.6500000097, -3.8000000566))
                CenterArc((0.400000006, -3.8000000566), 0.2500000037, 180, 180)
                Line((0.1500000022, -2.8000000417), (0.1500000022, -3.8000000566))
                CenterArc((0.400000006, -2.8000000417), 0.2500000037, 0, 180)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.25, -8.825), 0.21, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.35, -8.825), 0.21, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.35, -6.575), 0.21, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.25, -6.575), 0.21, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.32, -2.1000000313), 1.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.87, -3.65), 0.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.77, -3.65), 0.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.77, -0.55), 0.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.87, -0.55), 0.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)
    return part.part


def model_23255_972fbfe6_0014():
    """Model: part9"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.8396855996, perimeter: 8.2309727524
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.31, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


def model_23258_87a2ba81_0001():
    """Model: P10-Axle"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with Locations((-19, 0)):
                Circle(0.75)
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with Locations((19, 0)):
                Circle(0.75)
        # Symmetric extrude, each_side=13.75
        extrude(amount=13.75, both=True)
    return part.part


def model_23264_20be13a0_0009():
    """Model: Nut v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4673127508, perimeter: 3.2510310271
            with BuildLine():
                Line((0, 0), (0.4494217152, 1.085))
                CenterArc((0, 4.0511), 2.9999548477, -98.6158865727, 17.2317731454)
                Line((0, 0), (-0.4494217152, 1.085))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


def model_23278_8d704515_0000():
    """Model: Arm"""
    with BuildPart() as part:
        # Sketch1 -> Extrude4 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 18 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.0307511407, perimeter: 4.2488365806
            with BuildLine():
                CenterArc((-5.8, 0), 0.75, -97.9141063462, 7.9141063462)
                Line((-5.8, 0), (-5.8, -0.75))
                Line((-5.8, 0), (-5.425, 0.6495190528))
                CenterArc((-5.8, 0), 0.75, 60, 91.444625844)
                CenterArc((-5.8, 0), 0.75, 151.444625844, 103.6399213109)
                CenterArc((2.4033100634, 40.6297905709), 42.1982837662, -101.4769591921, 0.1243591929)
            make_face()
            # Profile area: 2.0997401006, perimeter: 8.1853830306
            with BuildLine():
                CenterArc((-5.8, 0), 0.75, 60, 91.444625844)
                Line((-5.425, 0.6495190528), (-4, 3.1176914536))
                Line((-4, 3.1176914536), (-4.4330127019, 3.3676914536))
                CenterArc((5.725329441, -5.657255589), 13.5882884947, 138.3812424834, 15.341414828)
            make_face()
            # Profile area: 0.0005736644, perimeter: 0.2223521798
            with BuildLine():
                Line((-5.8, -0.75), (-5.8, -0.7634559412))
                CenterArc((-5.8, 0), 0.75, -97.9141063462, 7.9141063462)
                CenterArc((2.4033100634, 40.6297905709), 42.1982837662, -101.3525999992, 0.1429748447)
            make_face()
            # Profile area: 0.2945243113, perimeter: 2.2853981634
            with BuildLine():
                Line((-5.8, 0), (-5.425, 0.6495190528))
                Line((-5.05, 0), (-5.8, 0))
                CenterArc((-5.8, 0), 0.75, 0, 60)
            make_face()
            # Profile area: 0.0002981704, perimeter: 0.3543925227
            with BuildLine():
                CenterArc((2.4033100634, 40.6297905709), 42.1982837662, -93.5054440121, 0.2405227665)
                CenterArc((0, 0), 1.5, -96.7703652577, 6.7703652577)
            make_face()
            # Profile area: 2.8370467465, perimeter: 16.7364402431
            with BuildLine():
                CenterArc((-4.9579262635, 9.9520443257), 9.6202089529, -89.2456001105, 25.3476150883)
                CenterArc((-4.8345545176, 0.5826475877), 0.25, 164.7906969497, 105.9637029398)
                CenterArc((-1.0983197996, -0.4331163765), 4.1218505006, 126.7927401325, 37.9979568172)
                Line((-4, 3.1176914536), (-3.5669872981, 2.8676914536))
                Line((-5.425, 0.6495190528), (-4, 3.1176914536))
                CenterArc((-5.8, 0), 0.75, 0, 60)
                Line((-1.5, 0), (-5.05, 0))
                CenterArc((0, 0), 1.5, 118.9171102058, 61.0828897942)
            make_face()
            # Profile area: 1.6411839911, perimeter: 5.1844100477
            with BuildLine():
                Line((-0.4, 0), (-1.5, 0))
                CenterArc((0, 0), 1.5, -180, 83.2296347423)
                CenterArc((2.4033100634, 40.6297905709), 42.1982837662, -93.5054440121, 0.2405227665)
                Line((0, -0.4), (0, -1.5))
                CenterArc((0, 0), 0.4, -180, 90)
            make_face()
            # Profile area: 0.4417864669, perimeter: 2.6780972451
            with BuildLine():
                Line((-5.05, 0), (-5.8, 0))
                Line((-5.8, 0), (-5.8, -0.75))
                CenterArc((-5.8, 0), 0.75, -90, 90)
            make_face()
            # Profile area: 4.7506236731, perimeter: 12.5946215618
            with BuildLine():
                Line((-1.5, 0), (-5.05, 0))
                CenterArc((-5.8, 0), 0.75, -90, 90)
                Line((-5.8, -0.75), (-5.8, -0.7634559412))
                CenterArc((2.4033100634, 40.6297905709), 42.1982837662, -101.2096251544, 7.7041811423)
                CenterArc((0, 0), 1.5, -180, 83.2296347423)
            make_face()
            # Profile area: 0.0000839488, perimeter: 0.1832378314
            with BuildLine():
                CenterArc((2.4033100634, 40.6297905709), 42.1982837662, -101.4769591921, 0.1243591929)
                CenterArc((-5.8, 0), 0.75, -104.9154528451, 7.0013464989)
            make_face()
            # Profile area: 4.9244464845, perimeter: 11.1535390627
            with BuildLine():
                CenterArc((0, 0), 0.4, -90, 270)
                Line((0, -0.4), (0, -1.5))
                CenterArc((0, 0), 1.5, -90, 208.9171102058)
                CenterArc((0, 0), 1.5, 118.9171102058, 61.0828897942)
                Line((-0.4, 0), (-1.5, 0))
            make_face()
        # TwoSides extrude (symmetric), distance=0.1
        extrude(amount=0.1, both=True)
    return part.part


def model_23313_210c6783_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 44.1786466911, perimeter: 23.5619449019
            Circle(3.75)
        # Symmetric extrude, each_side=15
        extrude(amount=15, both=True)
    return part.part


def model_23366_cc0bc28e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 13 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 24, perimeter: 35.0312195419
            with BuildLine():
                Line((0, 1), (16, 2))
                Line((0, 1), (0, 0))
                Line((0, 0), (16, 0))
                Line((16, 0), (16, 2))
            make_face()
            # Profile area: 24, perimeter: 35.0312195419
            with BuildLine():
                Line((16, 4.5), (16, 2.5))
                Line((0, 4.5), (16, 4.5))
                Line((0, 3.5), (0, 4.5))
                Line((16, 2.5), (0, 3.5))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


def model_23368_648717d8_0004():
    """Model: Base"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 70, perimeter: 34
            with BuildLine():
                Line((5, -3.5), (5, 3.5))
                Line((5, 3.5), (-5, 3.5))
                Line((-5, 3.5), (-5, -3.5))
                Line((-5, -3.5), (5, -3.5))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


def model_23376_9b48819a_0000():
    """Model: FPV_Frame_Mount"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 100 constraints, 23 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.3872362357, perimeter: 30.2737681151
            with BuildLine():
                Line((0.475, 1.9704664799), (0.475, 1.7812376471))
                CenterArc((0.38, 1.7812376387), 0.095, -179.9999961514, 180.0000012074)
                Line((-0.2851920809, 1.7812376324), (0.285, 1.7812376324))
                CenterArc((-0.38, 1.7872757176), 0.095, -179.9999948901, 176.3558880434)
                Line((-0.475, 1.7872757091), (-0.475, 1.9704664799))
                Line((-1.3438197525, 1.9704664799), (-0.475, 1.9704664799))
                Line((-1.3438197525, 1.7812376324), (-1.3438197525, 1.9704664799))
                CenterArc((-1.4388197525, 1.781237462), 0.095, 179.9998972637, 180.0002054723)
                Line((-2.0368468558, 1.7812376324), (-1.5338197525, 1.7812376324))
                Line((-2.0368468558, -1.7603307475), (-2.0368468558, 1.7812376324))
                Line((-1.5399924639, -1.7603307475), (-2.0368468558, -1.7603307475))
                CenterArc((-1.445, -1.7591341665), 0.095, 0.0000478016, 180.7216453809)
                Line((-1.35, -1.9795286853), (-1.35, -1.7591340872))
                Line((-0.475, -1.9795286853), (-1.35, -1.9795286853))
                Line((-0.475, -1.9795286853), (-0.475, -1.7603334338))
                CenterArc((-0.38, -1.7603320906), 0.095, 0.0008100845, 180)
                Line((0.2894775822, -1.7603307475), (-0.285, -1.7603307475))
                CenterArc((0.38, -1.7891524731), 0.095, -0.0000301983, 162.3389068786)
                Line((0.475, -1.7891525231), (0.475, -1.9795286853))
                Line((1.35, -1.9795286853), (0.475, -1.9795286853))
                Line((1.35, -1.7603307474), (1.35, -1.9795286853))
                CenterArc((1.445, -1.7603307588), 0.095, 0.0000068594, 179.9999862333)
                Line((2.0129398139, -1.7603307475), (1.54, -1.7603307475))
                Line((2.0129398139, 1.7396692525), (2.0129398139, -1.7603307475))
                Line((1.5242426217, 1.7396692525), (2.0129398139, 1.7396692525))
                CenterArc((1.4388197525, 1.781237671), 0.095, -179.9999766937, 154.0515272822)
                Line((1.3438197525, 1.9704664799), (1.3438197525, 1.7812376324))
                Line((0.475, 1.9704664799), (1.3438197525, 1.9704664799))
            make_face()
            with BuildLine():
                Line((1.3262563133, -1.4676776695), (1.3792893219, -1.5207106781))
                CenterArc((1.3969669914, -1.3969669914), 0.1, 45, 180)
                Line((1.5207106781, -1.3792893219), (1.4676776695, -1.3262563133))
                CenterArc((1.45, -1.45), 0.1, -135, 180)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-1.4676776695, -1.3262563133), (-1.5207106781, -1.3792893219))
                CenterArc((-1.3969669914, -1.3969669914), 0.1, -45, 180)
                Line((-1.3792893219, -1.5207106781), (-1.3262563133, -1.4676776695))
                CenterArc((-1.45, -1.45), 0.1, 135, 180)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-1.3262563133, 1.4676776695), (-1.3792893219, 1.5207106781))
                CenterArc((-1.3969669914, 1.3969669914), 0.1, -135, 180)
                Line((-1.5207106781, 1.3792893219), (-1.4676776695, 1.3262563133))
                CenterArc((-1.45, 1.45), 0.1, 45, 180)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((1.4676776695, 1.3262563133), (1.5207106781, 1.3792893219))
                CenterArc((1.3969669914, 1.3969669914), 0.1, 135, 180)
                Line((1.3792893219, 1.5207106781), (1.3262563133, 1.4676776695))
                CenterArc((1.45, 1.45), 0.1, -45, 180)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-1.55, -0.775), (-1.55, 0.775))
                Line((-1.55, 0.775), (0, 1.275))
                Line((0, 1.275), (1.55, 0.775))
                Line((1.55, 0.775), (1.55, -0.775))
                Line((0, -1.275), (1.55, -0.775))
                Line((-1.55, -0.775), (0, -1.275))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.175
        extrude(amount=0.175)
    return part.part


def model_23410_0163b27d_0000():
    """Model: eccentric ring"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.7907078125, perimeter: 11.9380520836
            with BuildLine():
                CenterArc((0, 0), 1.1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


def model_23410_0163b27d_0006():
    """Model: bush slider"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4243524479, perimeter: 2.4248711306
            with BuildLine():
                Line((0.2979274132, 0.6500000149), (0.7020726017, 0.6500000149))
                Line((0.7020726017, 0.6500000149), (0.9041451959, 1.0000000149))
                Line((0.9041451959, 1.0000000149), (0.7020726017, 1.3500000149))
                Line((0.7020726017, 1.3500000149), (0.2979274132, 1.3500000149))
                Line((0.2979274132, 1.3500000149), (0.095854819, 1.0000000149))
                Line((0.095854819, 1.0000000149), (0.2979274132, 0.6500000149))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


def model_23410_0163b27d_0007():
    """Model: bush cylinder"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.8660254038, perimeter: 3.4641016151
            with BuildLine():
                Line((1.2113248654, 4), (1.7886751346, 4))
                Line((1.7886751346, 4), (2.0773502692, 4.5))
                Line((2.0773502692, 4.5), (1.7886751346, 5))
                Line((1.7886751346, 5), (1.2113248654, 5))
                Line((1.2113248654, 5), (0.9226497308, 4.5))
                Line((0.9226497308, 4.5), (1.2113248654, 4))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


def model_23410_0163b27d_0008():
    """Model: lever"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7366966311, perimeter: 5.5171421623
            with BuildLine():
                CenterArc((16.0000002384, -15.100000225), 0.275, -82.1990126312, 164.3980252623)
                Line((16.037326716, -15.3724552379), (18.2000002712, -15.225000225))
                CenterArc((18.2000002712, -15.100000225), 0.125, 90, 180)
                Line((16.037326716, -14.8275452121), (18.2000002712, -14.975000225))
            make_face()
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            with BuildLine():
                CenterArc((18.2000002712, -15.100000225), 0.125, 90, 180)
                CenterArc((18.2000002712, -15.100000225), 0.125, -90, 180)
            make_face()
            # Profile area: 0.1571263897, perimeter: 2.7331277815
            with BuildLine():
                CenterArc((16.0000002384, -15.100000225), 0.275, 90, 180)
                Line((16.0000002384, -15.375000225), (16.037326716, -15.3724552379))
                CenterArc((16.0000002384, -15.100000225), 0.275, -82.1990126312, 164.3980252623)
                Line((16.0000002384, -14.825000225), (16.037326716, -14.8275452121))
            make_face()
            with BuildLine():
                CenterArc((16.0000002384, -15.100000225), 0.16, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


def model_23410_0163b27d_0011():
    """Model: M2 screw"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1385640687, perimeter: 1.3856406667
            with BuildLine():
                Line((1.3845299668, 2.8000000417), (1.6154700779, 2.8000000417))
                Line((1.6154700779, 2.8000000417), (1.7309401335, 3.0000000447))
                Line((1.7309401335, 3.0000000447), (1.6154700779, 3.2000000477))
                Line((1.6154700779, 3.2000000477), (1.3845299668, 3.2000000477))
                Line((1.3845299668, 3.2000000477), (1.2690599112, 3.0000000447))
                Line((1.2690599112, 3.0000000447), (1.3845299668, 2.8000000417))
            make_face()
        # OneSide extrude, distance=0.14
        extrude(amount=0.14)
    return part.part


def model_23410_0163b27d_0012():
    """Model: M3 screw"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2619726846, perimeter: 1.9052558883
            with BuildLine():
                Line((1.3412286983, 2.7250000447), (1.6587713464, 2.7250000447))
                Line((1.6587713464, 2.7250000447), (1.8175426704, 3.0000000447))
                Line((1.8175426704, 3.0000000447), (1.6587713464, 3.2750000447))
                Line((1.6587713464, 3.2750000447), (1.3412286983, 3.2750000447))
                Line((1.3412286983, 3.2750000447), (1.1824573743, 3.0000000447))
                Line((1.1824573743, 3.0000000447), (1.3412286983, 2.7250000447))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


def model_23471_3dafd9b1_0001():
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
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 5278.0835193667, perimeter: 335.0205244937
            with BuildLine():
                _nurbs_edge([(49.2718231713, -71.5900933913), (49.4592524897, -71.5922251695), (49.8333486727, -71.5926457717), (50.3922053386, -71.5817476478), (51.1362847476, -71.5462487451), (52.0822878, -71.4780112167), (53.0621721886, -71.3983093941), (54.0855001021, -71.3162364155), (55.1450211715, -71.233165171), (56.2209372027, -71.1451943212), (57.2847388743, -71.0455339641), (58.3033685181, -70.9266698877), (59.2427905644, -70.7832064617), (60.0739218663, -70.6115259018), (60.779565561, -70.4077104164), (61.3614933533, -70.165983931), (61.846496669, -69.8769798682), (62.2685392775, -69.5281632851), (62.6453047664, -69.104404592), (62.9767284809, -68.5877377019), (63.2648817578, -67.9561116808), (63.5265952053, -67.1828400601), (63.7848312089, -66.2460212902), (64.0612031335, -65.1362901103), (64.3665411959, -63.867573635), (64.6979239447, -62.4781269712), (65.0441522405, -61.0188470898), (65.3890276195, -59.5449954416), (65.7156686155, -58.1060966043), (66.0100151785, -56.7376626899), (66.2655917019, -55.4495039825), (66.4839061146, -54.2264948893), (66.6714390659, -53.0391355193), (66.8375585509, -51.8515255881), (66.9921781707, -50.6298800449), (67.1432455764, -49.3520258957), (67.2952251115, -48.0125149374), (67.4501039523, -46.6168826623), (67.6078775493, -45.1781697458), (67.767254362, -43.7124234777), (67.9262296618, -42.2349479925), (68.0828002082, -40.7554773304), (68.2352694856, -39.2768689931), (68.3821967327, -37.7969632246), (68.5224430625, -36.3095591974), (68.655180133, -34.8057542993), (68.7799114408, -33.275102597), (68.896498401, -31.7068968923), (69.0051542112, -30.0912402412), (69.1063410363, -28.4196426437), (69.2006858544, -26.6857066225), (69.2888894676, -24.8857785919), (69.3716382156, -23.0196259531), (69.449515662, -21.0910943778), (69.5229117246, -19.1088156239), (69.5919397812, -17.0868025438), (69.656491393, -15.0431267324), (69.7162835819, -12.9987005186), (69.7709085845, -10.9760272371), (69.8198825564, -8.9979629251), (69.8626942009, -7.0864865206), (69.8988544089, -5.2614364302), (69.9279431971, -3.53932582), (69.94704078, -2.12607375), (69.9574366534, -1.10488663), (69.9625779077, -0.4205617738), (69.9648259083, -0.0342427461), (69.9654034883, 0.074364916)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0153846154, 0.0307692308, 0.0461538462, 0.0615384615, 0.0769230769, 0.0923076923, 0.1076923077, 0.1230769231, 0.1384615385, 0.1538461538, 0.1692307692, 0.1846153846, 0.2, 0.2153846154, 0.2307692308, 0.2461538462, 0.2615384615, 0.2769230769, 0.2923076923, 0.3076923077, 0.3230769231, 0.3384615385, 0.3538461538, 0.3692307692, 0.3846153846, 0.4, 0.4153846154, 0.4307692308, 0.4461538462, 0.4615384615, 0.4769230769, 0.4923076923, 0.5076923077, 0.5230769231, 0.5384615385, 0.5538461538, 0.5692307692, 0.5846153846, 0.6, 0.6153846154, 0.6307692308, 0.6461538462, 0.6615384615, 0.6769230769, 0.6923076923, 0.7076923077, 0.7230769231, 0.7384615385, 0.7538461538, 0.7692307692, 0.7846153846, 0.8, 0.8153846154, 0.8307692308, 0.8461538462, 0.8615384615, 0.8769230769, 0.8923076923, 0.9076923077, 0.9230769231, 0.9384615385, 0.9538461538, 0.9599402361, 0.9599402361, 0.9599402361, 0.9599402361, 0.9599402361, 0.9599402361], 5)
                _nurbs_edge([(49.2718231713, 71.7388232234), (49.4592524897, 71.7409550015), (49.8333486727, 71.7413756038), (50.3922053386, 71.7304774798), (51.1362847476, 71.6949785772), (52.0822878, 71.6267410487), (53.0621721886, 71.5470392261), (54.0855001021, 71.4649662475), (55.1450211715, 71.3818950031), (56.2209372027, 71.2939241532), (57.2847388743, 71.1942637962), (58.3033685181, 71.0753997198), (59.2427905644, 70.9319362937), (60.0739218663, 70.7602557338), (60.779565561, 70.5564402485), (61.3614933533, 70.3147137631), (61.846496669, 70.0257097003), (62.2685392775, 69.6768931172), (62.6453047664, 69.253134424), (62.9767284809, 68.736467534), (63.2648817578, 68.1048415128), (63.5265952053, 67.3315698922), (63.7848312089, 66.3947511223), (64.0612031335, 65.2850199423), (64.3665411959, 64.0163034671), (64.6979239447, 62.6268568032), (65.0441522405, 61.1675769218), (65.3890276195, 59.6937252737), (65.7156686155, 58.2548264363), (66.0100151785, 56.886392522), (66.2655917019, 55.5982338146), (66.4839061146, 54.3752247214), (66.6714390659, 53.1878653513), (66.8375585509, 52.0002554202), (66.9921781707, 50.778609877), (67.1432455764, 49.5007557277), (67.2952251115, 48.1612447695), (67.4501039523, 46.7656124944), (67.6078775493, 45.3268995779), (67.767254362, 43.8611533098), (67.9262296618, 42.3836778245), (68.0828002082, 40.9042071624), (68.2352694856, 39.4255988252), (68.3821967327, 37.9456930567), (68.5224430625, 36.4582890295), (68.655180133, 34.9544841313), (68.7799114408, 33.423832429), (68.896498401, 31.8556267244), (69.0051542112, 30.2399700733), (69.1063410363, 28.5683724758), (69.2006858544, 26.8344364546), (69.2888894676, 25.034508424), (69.3716382156, 23.1683557852), (69.449515662, 21.2398242098), (69.5229117246, 19.257545456), (69.5919397812, 17.2355323759), (69.656491393, 15.1918565645), (69.7162835819, 13.1474303507), (69.7709085845, 11.1247570692), (69.8198825564, 9.1466927571), (69.8626942009, 7.2352163526), (69.8988544089, 5.4101662623), (69.9279431971, 3.6880556521), (69.94704078, 2.274803582), (69.9574366534, 1.2536164621), (69.9625779077, 0.5692916058), (69.9648259083, 0.1829725782), (69.9654034883, 0.074364916)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0153846154, 0.0307692308, 0.0461538462, 0.0615384615, 0.0769230769, 0.0923076923, 0.1076923077, 0.1230769231, 0.1384615385, 0.1538461538, 0.1692307692, 0.1846153846, 0.2, 0.2153846154, 0.2307692308, 0.2461538462, 0.2615384615, 0.2769230769, 0.2923076923, 0.3076923077, 0.3230769231, 0.3384615385, 0.3538461538, 0.3692307692, 0.3846153846, 0.4, 0.4153846154, 0.4307692308, 0.4461538462, 0.4615384615, 0.4769230769, 0.4923076923, 0.5076923077, 0.5230769231, 0.5384615385, 0.5538461538, 0.5692307692, 0.5846153846, 0.6, 0.6153846154, 0.6307692308, 0.6461538462, 0.6615384615, 0.6769230769, 0.6923076923, 0.7076923077, 0.7230769231, 0.7384615385, 0.7538461538, 0.7692307692, 0.7846153846, 0.8, 0.8153846154, 0.8307692308, 0.8461538462, 0.8615384615, 0.8769230769, 0.8923076923, 0.9076923077, 0.9230769231, 0.9384615385, 0.9538461538, 0.9599402361, 0.9599402361, 0.9599402361, 0.9599402361, 0.9599402361, 0.9599402361], 5)
                _nurbs_edge([(49.2718231713, 71.7388232234), (49.0843938528, 71.7409550015), (48.7102976699, 71.7413756038), (48.151441004, 71.7304774798), (47.407361595, 71.6949785772), (46.4613585426, 71.6267410487), (45.4814741539, 71.5470392261), (44.4581462405, 71.4649662475), (43.3986251711, 71.3818950031), (42.3227091399, 71.2939241532), (41.2589074683, 71.1942637962), (40.2402778245, 71.0753997198), (39.3008557782, 70.9319362937), (38.4697244763, 70.7602557338), (37.7640807815, 70.5564402485), (37.1821529892, 70.3147137631), (36.6971496736, 70.0257097003), (36.275107065, 69.6768931172), (35.8983415761, 69.253134424), (35.5669178617, 68.736467534), (35.2787645848, 68.1048415128), (35.0170511373, 67.3315698922), (34.7588151337, 66.3947511223), (34.4824432091, 65.2850199423), (34.1771051467, 64.0163034671), (33.8457223979, 62.6268568032), (33.499494102, 61.1675769218), (33.1546187231, 59.6937252737), (32.827977727, 58.2548264363), (32.5336311641, 56.886392522), (32.2780546407, 55.5982338146), (32.0597402279, 54.3752247214), (31.8722072766, 53.1878653513), (31.7060877917, 52.0002554202), (31.5514681719, 50.778609877), (31.4004007662, 49.5007557277), (31.2484212311, 48.1612447695), (31.0935423902, 46.7656124944), (30.9357687932, 45.3268995779), (30.7763919805, 43.8611533098), (30.6174166808, 42.3836778245), (30.4608461343, 40.9042071624), (30.3083768569, 39.4255988252), (30.1614496099, 37.9456930567), (30.02120328, 36.4582890295), (29.8884662096, 34.9544841313), (29.7637349017, 33.423832429), (29.6471479415, 31.8556267244), (29.5384921313, 30.2399700733), (29.4373053062, 28.5683724758), (29.3429604882, 26.8344364546), (29.254756875, 25.034508424), (29.172008127, 23.1683557852), (29.0941306806, 21.2398242098), (29.020734618, 19.257545456), (28.9517065614, 17.2355323759), (28.8871549496, 15.1918565645), (28.8273627607, 13.1474303507), (28.772737758, 11.1247570692), (28.7237637861, 9.1466927571), (28.6809521416, 7.2352163526), (28.6447919337, 5.4101662623), (28.6157031455, 3.6880556521), (28.5966055625, 2.274803582), (28.5862096892, 1.2536164621), (28.5810684348, 0.5692916058), (28.5788204343, 0.1829725782), (28.5782428542, 0.074364916)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0153846154, 0.0307692308, 0.0461538462, 0.0615384615, 0.0769230769, 0.0923076923, 0.1076923077, 0.1230769231, 0.1384615385, 0.1538461538, 0.1692307692, 0.1846153846, 0.2, 0.2153846154, 0.2307692308, 0.2461538462, 0.2615384615, 0.2769230769, 0.2923076923, 0.3076923077, 0.3230769231, 0.3384615385, 0.3538461538, 0.3692307692, 0.3846153846, 0.4, 0.4153846154, 0.4307692308, 0.4461538462, 0.4615384615, 0.4769230769, 0.4923076923, 0.5076923077, 0.5230769231, 0.5384615385, 0.5538461538, 0.5692307692, 0.5846153846, 0.6, 0.6153846154, 0.6307692308, 0.6461538462, 0.6615384615, 0.6769230769, 0.6923076923, 0.7076923077, 0.7230769231, 0.7384615385, 0.7538461538, 0.7692307692, 0.7846153846, 0.8, 0.8153846154, 0.8307692308, 0.8461538462, 0.8615384615, 0.8769230769, 0.8923076923, 0.9076923077, 0.9230769231, 0.9384615385, 0.9538461538, 0.9599402361, 0.9599402361, 0.9599402361, 0.9599402361, 0.9599402361, 0.9599402361], 5)
                _nurbs_edge([(49.2718231713, -71.5900933913), (49.0843938528, -71.5922251695), (48.7102976699, -71.5926457717), (48.151441004, -71.5817476478), (47.407361595, -71.5462487451), (46.4613585426, -71.4780112167), (45.4814741539, -71.3983093941), (44.4581462405, -71.3162364155), (43.3986251711, -71.233165171), (42.3227091399, -71.1451943212), (41.2589074683, -71.0455339641), (40.2402778245, -70.9266698877), (39.3008557782, -70.7832064617), (38.4697244763, -70.6115259018), (37.7640807815, -70.4077104164), (37.1821529892, -70.165983931), (36.6971496736, -69.8769798682), (36.275107065, -69.5281632851), (35.8983415761, -69.104404592), (35.5669178617, -68.5877377019), (35.2787645848, -67.9561116808), (35.0170511373, -67.1828400601), (34.7588151337, -66.2460212902), (34.4824432091, -65.1362901103), (34.1771051467, -63.867573635), (33.8457223979, -62.4781269712), (33.4994941021, -61.0188470898), (33.1546187231, -59.5449954416), (32.827977727, -58.1060966043), (32.5336311641, -56.7376626899), (32.2780546407, -55.4495039825), (32.0597402279, -54.2264948893), (31.8722072766, -53.0391355193), (31.7060877917, -51.8515255881), (31.5514681719, -50.6298800449), (31.4004007662, -49.3520258957), (31.2484212311, -48.0125149374), (31.0935423902, -46.6168826623), (30.9357687932, -45.1781697458), (30.7763919805, -43.7124234777), (30.6174166808, -42.2349479925), (30.4608461343, -40.7554773304), (30.3083768569, -39.2768689931), (30.1614496099, -37.7969632246), (30.02120328, -36.3095591974), (29.8884662096, -34.8057542993), (29.7637349017, -33.275102597), (29.6471479415, -31.7068968923), (29.5384921313, -30.0912402412), (29.4373053062, -28.4196426437), (29.3429604882, -26.6857066225), (29.254756875, -24.8857785919), (29.172008127, -23.0196259531), (29.0941306806, -21.0910943778), (29.020734618, -19.1088156239), (28.9517065614, -17.0868025438), (28.8871549496, -15.0431267324), (28.8273627607, -12.9987005186), (28.772737758, -10.9760272371), (28.7237637861, -8.9979629251), (28.6809521416, -7.0864865206), (28.6447919337, -5.2614364302), (28.6157031455, -3.53932582), (28.5966055625, -2.12607375), (28.5862096892, -1.10488663), (28.5810684348, -0.4205617738), (28.5788204343, -0.0342427461), (28.5782428542, 0.074364916)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0153846154, 0.0307692308, 0.0461538462, 0.0615384615, 0.0769230769, 0.0923076923, 0.1076923077, 0.1230769231, 0.1384615385, 0.1538461538, 0.1692307692, 0.1846153846, 0.2, 0.2153846154, 0.2307692308, 0.2461538462, 0.2615384615, 0.2769230769, 0.2923076923, 0.3076923077, 0.3230769231, 0.3384615385, 0.3538461538, 0.3692307692, 0.3846153846, 0.4, 0.4153846154, 0.4307692308, 0.4461538462, 0.4615384615, 0.4769230769, 0.4923076923, 0.5076923077, 0.5230769231, 0.5384615385, 0.5538461538, 0.5692307692, 0.5846153846, 0.6, 0.6153846154, 0.6307692308, 0.6461538462, 0.6615384615, 0.6769230769, 0.6923076923, 0.7076923077, 0.7230769231, 0.7384615385, 0.7538461538, 0.7692307692, 0.7846153846, 0.8, 0.8153846154, 0.8307692308, 0.8461538462, 0.8615384615, 0.8769230769, 0.8923076923, 0.9076923077, 0.9230769231, 0.9384615385, 0.9538461538, 0.9599402361, 0.9599402361, 0.9599402361, 0.9599402361, 0.9599402361, 0.9599402361], 5)
            make_face()
        # OneSide extrude, distance=7.5
        extrude(amount=7.5)
    return part.part


def model_23472_ed1faab6_0004():
    """Model: Speed Switch"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 27 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 23.3138421422, perimeter: 22.1771915707
            with BuildLine():
                Line((3.7067135145, -3.586886792), (0.5317135145, -3.586886792))
                Line((0.5317135145, -3.586886792), (0.5317135145, -3.85221765))
                Line((0.5317135145, -3.85221765), (-1.3732864855, -3.85221765))
                CenterArc((-1.3732864855, -4.8047145691), 0.9524969192, 90, 90)
                Line((-2.3257834046, -4.8047145691), (-2.3257834046, -5.4396796745))
                CenterArc((-1.3732454292, -5.4396796745), 0.9525379754, 180, 90)
                Line((-1.3732454292, -6.39221765), (0.5317413588, -6.39221765))
                Line((0.5317413588, -6.39221765), (0.5317413588, -6.6031367134))
                Line((0.5317413588, -6.6031367134), (3.7066856702, -6.6031367134))
                Line((3.7066856702, -6.39221765), (3.7066856702, -6.6031367134))
                Line((5.6116724582, -6.39221765), (3.7066856702, -6.39221765))
                CenterArc((5.6116724582, -5.4396796745), 0.9525379754, -90, 90)
                Line((6.5642104337, -4.8047145691), (6.5642104337, -5.4396796745))
                CenterArc((5.6117135145, -4.8047145691), 0.9524969192, 0, 90)
                Line((3.7067135145, -3.85221765), (5.6117135145, -3.85221765))
                Line((3.7067135145, -3.586886792), (3.7067135145, -3.85221765))
            make_face()
        # OneSide extrude, distance=0.079375
        extrude(amount=0.079375)
    return part.part


def model_23479_81a49137_0003():
    """Model: angolo v2 (3)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1, perimeter: 10.4
            with BuildLine():
                Line((0, 0.2), (0, 0))
                Line((-5, 0.2), (0, 0.2))
                Line((-5, 0), (-5, 0.2))
                Line((0, 0), (-5, 0))
            make_face()
            # Profile area: 1.04, perimeter: 10.8
            with BuildLine():
                Line((0, 0), (0, -5))
                Line((0, -5), (0.2, -5))
                Line((0.2, -5), (0.2, 0.2))
                Line((0.2, 0.2), (0, 0.2))
                Line((0, 0.2), (0, 0))
            make_face()
        # OneSide extrude, distance=50
        extrude(amount=50)
    return part.part


def model_23493_57512264_0000():
    """Model: obudowa"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 11 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 18.2641088543, perimeter: 26.4620929178
            with BuildLine():
                CenterArc((3.1894237366, 2.9473601358), 1, 0, 92.9270465577)
                CenterArc((4.05751822, -14.0304610427), 18, 92.9270465577, 33.7763101142)
                CenterArc((-6.4017438443, 0), 0.5, 126.7033566719, 173.0682917889)
                CenterArc((2.2566560905, -15.1357805396), 16.9373089086, 87.1082636852, 32.6633847757)
                CenterArc((3.1629110531, 2.8051667078), 1.0265126835, -92.8917363148, 92.8917363148)
                Line((4.1894237366, 2.9473601358), (4.1894237366, 2.8051667078))
            make_face()
            with BuildLine():
                CenterArc((-6.4017438443, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.9
        extrude(amount=1.9)
    return part.part


def model_23493_57512264_0005():
    """Model: bolec_maly"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            Circle(0.1)
        # OneSide extrude, distance=1.4
        extrude(amount=1.4)
    return part.part


def model_23505_161e8ec5_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch25 -> Extrude19 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1297.1711464896, perimeter: 127.6743254419
            with Locations((-71.1199989319, 45.7199993134)):
                Circle(20.32)
        # OneSide extrude, distance=-137.16
        extrude(amount=-137.16)
    return part.part


def model_23519_31078773_0002():
    """Model: guarnizione v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.9821896726, perimeter: 39.8982267006
            with BuildLine():
                CenterArc((0, 0), 3.35, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)
    return part.part


def model_23536_f2c05b8a_0000():
    """Model: staple v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 18 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.101556, perimeter: 4.791238898
            with BuildLine():
                CenterArc((1.193, 0.542), 0.075, 0, 90)
                Line((0.075, 0.617), (1.193, 0.617))
                CenterArc((0.075, 0.542), 0.075, 90, 90)
                Line((0, 0), (0, 0.542))
                Line((0, 0), (0.042, 0))
                Line((0.042, 0), (0.042, 0.5))
                CenterArc((0.117, 0.5), 0.075, 90, 90)
                Line((1.151, 0.575), (0.117, 0.575))
                CenterArc((1.151, 0.5), 0.075, 0, 90)
                Line((1.226, 0), (1.226, 0.5))
                Line((1.268, 0), (1.226, 0))
                Line((1.268, 0.542), (1.268, 0))
            make_face()
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)
    return part.part


def model_23539_b3917f22_0001():
    """Model: Shim_Druck v0"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 26 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2785428853, perimeter: 3.756491678
            with BuildLine():
                Line((0.5, 0), (0.6, 0))
                CenterArc((0, 0), 0.6, 0, 45.9703345987)
                Line((0.4170184332, 0.431388023), (0.5562960077, 0.5754648137))
                CenterArc((0.4125, 0.7144709581), 0.2, -44.0296654013, 208.0296654013)
                Line((0.1649588434, 0.5767834088), (0.2202476608, 0.7695984293))
                CenterArc((0.1552914271, 0.5795554958), 0.0100570077, 166, 178)
                Line((0.1455331554, 0.5819885061), (0.1940591453, 0.7766156209))
                CenterArc((0, 0.825), 0.2, -14, 104)
                Line((0, 1.025), (0, 0.95))
                CenterArc((0, 0.825), 0.125, -90, 180)
                Line((0, 0.7), (0, 0.5))
                CenterArc((0, 0), 0.5, 0, 90)
            make_face()
        # OneSide extrude, distance=0.02
        extrude(amount=0.02)
    return part.part


def model_23539_b3917f22_0002():
    """Model: Shim_Zug v0"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 21 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.034925032, perimeter: 2.5078076737
            with BuildLine():
                CenterArc((0, 0), 0.6, -44.0296654013, 88.0593308026)
                Line((0.431388023, -0.4170184332), (0.5754648137, -0.5562960077))
                CenterArc((0.7144709581, -0.4125), 0.2, 150, 75.9703345987)
                CenterArc((0, 0), 0.625, -30, 60)
                CenterArc((0.7144709581, 0.4125), 0.2, 134.0296654013, 75.9703345987)
                Line((0.431388023, 0.4170184332), (0.5754648137, 0.5562960077))
            make_face()
            # Profile area: 0.7060061821, perimeter: 4.7343210404
            with BuildLine():
                CenterArc((0, 0), 0.25, 44.0296654013, 271.9406691974)
                Line((0.1797450096, 0.1737576805), (0.431388023, 0.4170184332))
                CenterArc((0, 0), 0.6, 44.0296654013, 271.9406691974)
                Line((0.1797450096, -0.1737576805), (0.431388023, -0.4170184332))
            make_face()
            # Profile area: 0.471238898, perimeter: 2.9845130209
            with BuildLine():
                CenterArc((0.7144709581, -0.4125), 0.2, -134.0296654013, 104.0296654013)
                CenterArc((0, 0), 1.025, -30, 60)
                CenterArc((0.7144709581, 0.4125), 0.2, 30, 104.0296654013)
                CenterArc((0.7144709581, 0.4125), 0.2, 134.0296654013, 75.9703345987)
                CenterArc((0, 0), 0.625, -30, 60)
                CenterArc((0.7144709581, -0.4125), 0.2, 150, 75.9703345987)
            make_face()
            # Profile area: 0.2286176324, perimeter: 2.0063864707
            with BuildLine():
                Line((0.1797450096, -0.1737576805), (0.431388023, -0.4170184332))
                CenterArc((0, 0), 0.6, -44.0296654013, 88.0593308026)
                Line((0.1797450096, 0.1737576805), (0.431388023, 0.4170184332))
                CenterArc((0, 0), 0.25, -44.0296654013, 88.0593308026)
            make_face()
        # OneSide extrude, distance=0.02
        extrude(amount=0.02)
    return part.part


def model_23539_b3917f22_0003():
    """Model: Gabelbrücke v0"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 22.8360846418, perimeter: 38.4884614025
            with BuildLine():
                CenterArc((7, -1.2), 2, -96.000665009, 172.2360329412)
                Line((0.5948348593, 2.4282033461), (7.4758678875, 0.7425626769))
                CenterArc((0, 0), 2.5, 76.2353679322, 13.7646320677)
                Line((0, 2), (0, 2.5))
                CenterArc((0, 0), 2, -90, 180)
                Line((0, -2.5), (0, -2))
                CenterArc((0, -7), 4.5, 83.999334991, 6.000665009)
                Line((6.7909199874, -3.1890413642), (0.4704300282, -2.5246569306))
            make_face()
            with BuildLine():
                CenterArc((7, -1.2), 1.7, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


def model_23539_b3917f22_0005():
    """Model: Gleitlager_Unten v0 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.4636059006, perimeter: 19.7920337176
            with BuildLine():
                CenterArc((0, 0), 1.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


def model_23539_b3917f22_0006():
    """Model: Gleitlager_Oben v0 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.4871678455, perimeter: 23.2477856366
            with BuildLine():
                CenterArc((0, 0), 2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.7, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


def model_23552_10239b96_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 10.1402553777, perimeter: 14.5119841047
            with BuildLine():
                Line((1.9, 0), (3.8, 0))
                Line((3.8, 0), (3.8, 1.9))
                Line((3.8, 1.9), (1.1745166004, 1.9))
                Line((0, 0.7254833996), (1.1745166004, 1.9))
                Line((0, -1.9), (0, 0.7254833996))
                Line((1.9, -1.9), (0, -1.9))
                Line((1.9, 0), (1.9, -1.9))
            make_face()
        # OneSide extrude, distance=4.4
        extrude(amount=4.4)
    return part.part


def model_23554_a0845d54_0000():
    """Model: guarnzione pistone grande v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.5423667011, perimeter: 37.3849525777
            with BuildLine():
                CenterArc((0, 0), 3.15, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


MODELS = {
    "model_21908_385686ec_0032": {"func": model_21908_385686ec_0032, "volume": 1.6279999713, "area": 34.4800002789},
    "model_21908_385686ec_0033": {"func": model_21908_385686ec_0033, "volume": 6.2625830946, "area": 25.4371398692},
    "model_21908_385686ec_0034": {"func": model_21908_385686ec_0034, "volume": 6.8542344332, "area": 68.2953892693},
    "model_21918_976c2754_0008": {"func": model_21918_976c2754_0008, "volume": 276.2705361675, "area": 325.027433282},
    "model_21918_976c2754_0014": {"func": model_21918_976c2754_0014, "volume": 47.8616883225, "area": 153.279012427},
    "model_21940_6c2dac17_0000": {"func": model_21940_6c2dac17_0000, "volume": 0.6890175629, "area": 8.2381634876},
    "model_21941_1a683ec2_0000": {"func": model_21941_1a683ec2_0000, "volume": 234.8340508558, "area": 368.5088182661},
    "model_21941_1a683ec2_0001": {"func": model_21941_1a683ec2_0001, "volume": 1.2852059196, "area": 9.3658730985},
    "model_21941_1a683ec2_0007": {"func": model_21941_1a683ec2_0007, "volume": 1939.8117268764, "area": 2201.5063949204},
    "model_21941_1a683ec2_0008": {"func": model_21941_1a683ec2_0008, "volume": 937.7000055464, "area": 1906.1584774331},
    "model_21941_1a683ec2_0018": {"func": model_21941_1a683ec2_0018, "volume": 1241.3235170206, "area": 1098.4845397489},
    "model_21941_1a683ec2_0021": {"func": model_21941_1a683ec2_0021, "volume": 349.3451030792, "area": 374.4778443079},
    "model_21958_e48ddf4e_0000": {"func": model_21958_e48ddf4e_0000, "volume": 89.0014596807, "area": 381.4348272028},
    "model_21979_29f59427_0003": {"func": model_21979_29f59427_0003, "volume": 1.5444444949, "area": 12.5663458956},
    "model_22002_315afcfc_0008": {"func": model_22002_315afcfc_0008, "volume": 0.1005497654, "area": 1.425114785},
    "model_22002_315afcfc_0010": {"func": model_22002_315afcfc_0010, "volume": 0.3393554582, "area": 3.2065082662},
    "model_22011_0832eefe_0005": {"func": model_22011_0832eefe_0005, "volume": 8.2466807157, "area": 34.5575191895},
    "model_22011_0832eefe_0014": {"func": model_22011_0832eefe_0014, "volume": 8.9142691546, "area": 37.227872945},
    "model_22011_0832eefe_0015": {"func": model_22011_0832eefe_0015, "volume": 0.0471238898, "area": 1.0053096491},
    "model_22016_c1658896_0006": {"func": model_22016_c1658896_0006, "volume": 2.2870794518, "area": 26.1380508779},
    "model_22016_c1658896_0009": {"func": model_22016_c1658896_0009, "volume": 22.3762772036, "area": 60.6136215349},
    "model_22016_c1658896_0012": {"func": model_22016_c1658896_0012, "volume": 0.2262595881, "area": 2.5139528065},
    "model_22025_b77024b9_0006": {"func": model_22025_b77024b9_0006, "volume": 9.0320788791, "area": 37.6991118431},
    "model_22025_b77024b9_0013": {"func": model_22025_b77024b9_0013, "volume": 78.5398163397, "area": 135.4811831861},
    "model_22040_6461a147_0003": {"func": model_22040_6461a147_0003, "volume": 6.4847982235, "area": 20.7846096908},
    "model_22079_31335df2_0001": {"func": model_22079_31335df2_0001, "volume": 1.2514067085, "area": 7.9501132067},
    "model_22106_db85f777_0006": {"func": model_22106_db85f777_0006, "volume": 201.4233134781, "area": 1319.2101926179},
    "model_22124_6f71410e_0000": {"func": model_22124_6f71410e_0000, "volume": 9.6573102539, "area": 47.58055},
    "model_22124_6f71410e_0003": {"func": model_22124_6f71410e_0003, "volume": 3.4760153049, "area": 24.2491510268},
    "model_22197_5e5f919c_0000": {"func": model_22197_5e5f919c_0000, "volume": 130.8796, "area": 351.013},
    "model_22199_8ec9eeb2_0000": {"func": model_22199_8ec9eeb2_0000, "volume": 92.2214523461, "area": 621.9725135577},
    "model_22199_8ec9eeb2_0002": {"func": model_22199_8ec9eeb2_0002, "volume": 3.4164820108, "area": 34.1648201078},
    "model_22199_8ec9eeb2_0003": {"func": model_22199_8ec9eeb2_0003, "volume": 0.6832964022, "area": 12.2993352388},
    "model_22205_f48b96b3_0000": {"func": model_22205_f48b96b3_0000, "volume": 49.8759249684, "area": 83.5663645855},
    "model_22205_f48b96b3_0004": {"func": model_22205_f48b96b3_0004, "volume": 1.4396348335, "area": 14.0272111983},
    "model_22206_703c82ed_0003": {"func": model_22206_703c82ed_0003, "volume": 0.6787109163, "area": 6.0567378361},
    "model_22211_b1ee53f0_0005": {"func": model_22211_b1ee53f0_0005, "volume": 5.3469906964, "area": 22.6665909957},
    "model_22211_b1ee53f0_0011": {"func": model_22211_b1ee53f0_0011, "volume": 8.2168172596, "area": 58.6601629574},
    "model_22212_aadd1fae_0000": {"func": model_22212_aadd1fae_0000, "volume": 0.4804640539, "area": 5.4301593269},
    "model_22225_a3ce4d29_0002": {"func": model_22225_a3ce4d29_0002, "volume": 0.3866568028, "area": 3.5970555892},
    "model_22225_a3ce4d29_0004": {"func": model_22225_a3ce4d29_0004, "volume": 0.7545254394, "area": 5.3863005028},
    "model_22225_a3ce4d29_0014": {"func": model_22225_a3ce4d29_0014, "volume": 0.5047117373, "area": 5.8259787397},
    "model_22228_1c82530b_0008": {"func": model_22228_1c82530b_0008, "volume": 0.0000628479, "area": 0.0236087006},
    "model_22228_1c82530b_0009": {"func": model_22228_1c82530b_0009, "volume": 0.0000034928, "area": 0.0021681702},
    "model_22228_1c82530b_0010": {"func": model_22228_1c82530b_0010, "volume": 0.0023682383, "area": 0.2212835409},
    "model_22228_1c82530b_0013": {"func": model_22228_1c82530b_0013, "volume": 0.0010555073, "area": 0.1702859229},
    "model_22228_1c82530b_0019": {"func": model_22228_1c82530b_0019, "volume": 0.0000132536, "area": 0.0060082959},
    "model_22254_539990c2_0006": {"func": model_22254_539990c2_0006, "volume": 3.2656855634, "area": 14.6335385804},
    "model_22254_539990c2_0007": {"func": model_22254_539990c2_0007, "volume": 5.0438270053, "area": 18.174113501},
    "model_22254_539990c2_0008": {"func": model_22254_539990c2_0008, "volume": 0.4549155691, "area": 10.1432798167},
    "model_22276_69c5036b_0005": {"func": model_22276_69c5036b_0005, "volume": 40.1872532247, "area": 128.8052987972},
    "model_22276_69c5036b_0006": {"func": model_22276_69c5036b_0006, "volume": 316.1227607675, "area": 433.5397861954},
    "model_22276_69c5036b_0009": {"func": model_22276_69c5036b_0009, "volume": 49.008845396, "area": 157.0796326795},
    "model_22276_69c5036b_0012": {"func": model_22276_69c5036b_0012, "volume": 0.2710064154, "area": 6.1160273298},
    "model_22276_69c5036b_0014": {"func": model_22276_69c5036b_0014, "volume": 0.2171803761, "area": 9.1262078544},
    "model_22284_5d31c681_0000": {"func": model_22284_5d31c681_0000, "volume": 0.9742785793, "area": 6.4951905284},
    "model_22289_4b848f64_0003": {"func": model_22289_4b848f64_0003, "volume": 0.7206499388, "area": 19.3829983541},
    "model_22305_5b45cdb3_0000": {"func": model_22305_5b45cdb3_0000, "volume": 0.181945616, "area": 3.4037160914},
    "model_22305_5b45cdb3_0008": {"func": model_22305_5b45cdb3_0008, "volume": 0.1427296673, "area": 3.8351297088},
    "model_22305_5b45cdb3_0011": {"func": model_22305_5b45cdb3_0011, "volume": 0.1622854322, "area": 4.3758695763},
    "model_22305_5b45cdb3_0020": {"func": model_22305_5b45cdb3_0020, "volume": 0.1646596608, "area": 7.4040094371},
    "model_22320_e9f9e6ae_0000": {"func": model_22320_e9f9e6ae_0000, "volume": 14.5646003294, "area": 64.6584013175},
    "model_22320_e9f9e6ae_0003": {"func": model_22320_e9f9e6ae_0003, "volume": 12.8577765684, "area": 45.5971377352},
    "model_22320_e9f9e6ae_0008": {"func": model_22320_e9f9e6ae_0008, "volume": 19.2131700601, "area": 87.971688737},
    "model_22320_e9f9e6ae_0009": {"func": model_22320_e9f9e6ae_0009, "volume": 8.4823001647, "area": 30.5362805929},
    "model_22322_f04772b3_0002": {"func": model_22322_f04772b3_0002, "volume": 3.4557520219, "area": 15.3938042554},
    "model_22323_aa6edb8b_0000": {"func": model_22323_aa6edb8b_0000, "volume": 5.5182814809, "area": 27.2371695972},
    "model_22323_aa6edb8b_0006": {"func": model_22323_aa6edb8b_0006, "volume": 0.9897449164, "area": 8.2268995251},
    "model_22323_aa6edb8b_0009": {"func": model_22323_aa6edb8b_0009, "volume": 10.4552203511, "area": 30.1592894745},
    "model_22340_ec24cd79_0036": {"func": model_22340_ec24cd79_0036, "volume": 894.4834874604, "area": 2171.1140841531},
    "model_22341_0f9c52ed_0001": {"func": model_22341_0f9c52ed_0001, "volume": 32.1699087728, "area": 84.4460105285},
    "model_22342_274ed8a6_0001": {"func": model_22342_274ed8a6_0001, "volume": 13.5716802635, "area": 47.1238898038},
    "model_22342_274ed8a6_0003": {"func": model_22342_274ed8a6_0003, "volume": 10.6876982075, "area": 75.2097281269},
    "model_22355_6a8b11c3_0011": {"func": model_22355_6a8b11c3_0011, "volume": 0.0410974611, "area": 0.9994532891},
    "model_22357_e2f7b060_0018": {"func": model_22357_e2f7b060_0018, "volume": 2.1873981731, "area": 21.370619214},
    "model_22357_e2f7b060_0021": {"func": model_22357_e2f7b060_0021, "volume": 0.5622654844, "area": 7.9079645166},
    "model_22357_e2f7b060_0023": {"func": model_22357_e2f7b060_0023, "volume": 0.0115551531, "area": 0.5862053854},
    "model_22369_481ab478_0014": {"func": model_22369_481ab478_0014, "volume": 0.116797112, "area": 2.5456021134},
    "model_22369_481ab478_0023": {"func": model_22369_481ab478_0023, "volume": 3.1595221657, "area": 38.9789082175},
    "model_22369_481ab478_0027": {"func": model_22369_481ab478_0027, "volume": 0.190013454, "area": 3.6432679687},
    "model_22395_7f99d894_0003": {"func": model_22395_7f99d894_0003, "volume": 8.4817698027, "area": 42.2584061406},
    "model_22395_7f99d894_0007": {"func": model_22395_7f99d894_0007, "volume": 0.0312451578, "area": 1.1737441104},
    "model_22404_66db7dd7_0002": {"func": model_22404_66db7dd7_0002, "volume": 1.3046716642, "area": 28.5258879925},
    "model_22430_c6f08b03_0037": {"func": model_22430_c6f08b03_0037, "volume": 0.4778510962, "area": 26.9915372162},
    "model_22433_9f17ac4c_0001": {"func": model_22433_9f17ac4c_0001, "volume": 0.0195375549, "area": 4.482701251},
    "model_22433_9f17ac4c_0006": {"func": model_22433_9f17ac4c_0006, "volume": 2.9568319768, "area": 39.0494956001},
    "model_22447_4062c6cb_0006": {"func": model_22447_4062c6cb_0006, "volume": 0.2760576401, "area": 2.5582597819},
    "model_22461_0ba0e480_0002": {"func": model_22461_0ba0e480_0002, "volume": 0.1814269757, "area": 4.2882739722},
    "model_22461_0ba0e480_0004": {"func": model_22461_0ba0e480_0004, "volume": 0.7351326809, "area": 8.9849549893},
    "model_22463_c48bb23e_0002": {"func": model_22463_c48bb23e_0002, "volume": 64, "area": 96},
    "model_22524_0be3da8a_0000": {"func": model_22524_0be3da8a_0000, "volume": 0.0159377395, "area": 0.4386161281},
    "model_22524_0be3da8a_0002": {"func": model_22524_0be3da8a_0002, "volume": 0.1068923903, "area": 1.8178856564},
    "model_22524_0be3da8a_0007": {"func": model_22524_0be3da8a_0007, "volume": 0.0997453673, "area": 1.8950859718},
    "model_22534_e899f645_0005": {"func": model_22534_e899f645_0005, "volume": 0.2522391414, "area": 3.2064449277},
    "model_22543_684108ff_0000": {"func": model_22543_684108ff_0000, "volume": 0.2259995153, "area": 2.2550603395},
    "model_22543_684108ff_0003": {"func": model_22543_684108ff_0003, "volume": 0.8043981231, "area": 5.7004591398},
    "model_22543_684108ff_0011": {"func": model_22543_684108ff_0011, "volume": 0.1969024006, "area": 3.3235666618},
    "model_22543_684108ff_0016": {"func": model_22543_684108ff_0016, "volume": 0.3191858136, "area": 3.4431855483},
    "model_22545_7c2ca3ce_0005": {"func": model_22545_7c2ca3ce_0005, "volume": 1.6419687917, "area": 31.120629523},
    "model_22545_7c2ca3ce_0006": {"func": model_22545_7c2ca3ce_0006, "volume": 6.7871091634, "area": 29.9274104842},
    "model_22606_f1813fe7_0006": {"func": model_22606_f1813fe7_0006, "volume": 2.669187608, "area": 29.67503608},
    "model_22607_5d64eeb2_0006": {"func": model_22607_5d64eeb2_0006, "volume": 0.0628318531, "area": 1.3194689145},
    "model_22611_35dd01a9_0000": {"func": model_22611_35dd01a9_0000, "volume": 63.241225951, "area": 210.4284791691},
    "model_22624_7af10d7d_0005": {"func": model_22624_7af10d7d_0005, "volume": 25.8996637664, "area": 110.2430082787},
    "model_22630_b6010fff_0001": {"func": model_22630_b6010fff_0001, "volume": 22.8079626651, "area": 88.640036721},
    "model_22630_b6010fff_0003": {"func": model_22630_b6010fff_0003, "volume": 3.0347785034, "area": 62.140702688},
    "model_22630_b6010fff_0010": {"func": model_22630_b6010fff_0010, "volume": 1.7341591448, "area": 28.902652413},
    "model_22630_b6010fff_0011": {"func": model_22630_b6010fff_0011, "volume": 1.5268140296, "area": 21.62986542},
    "model_22657_bc1010fa_0007": {"func": model_22657_bc1010fa_0007, "volume": 1247.853981634, "area": 1218.9911485751},
    "model_22666_bdaa1303_0012": {"func": model_22666_bdaa1303_0012, "volume": 0.0173427474, "area": 0.5847126171},
    "model_22666_bdaa1303_0013": {"func": model_22666_bdaa1303_0013, "volume": 0.0339003899, "area": 1.1139120628},
    "model_22666_bdaa1303_0020": {"func": model_22666_bdaa1303_0020, "volume": 0.0622411092, "area": 1.9729973138},
    "model_22670_9353c710_0003": {"func": model_22670_9353c710_0003, "volume": 0.0628318531, "area": 1.1309733553},
    "model_22687_6f36672c_0000": {"func": model_22687_6f36672c_0000, "volume": 40.8910379112, "area": 149.7620054399},
    "model_22711_33843a5d_0000": {"func": model_22711_33843a5d_0000, "volume": 3.8052541017, "area": 23.2320776733},
    "model_22711_33843a5d_0008": {"func": model_22711_33843a5d_0008, "volume": 23.2, "area": 127.5934708797},
    "model_22734_f6bad9f7_0023": {"func": model_22734_f6bad9f7_0023, "volume": 0.0879810447, "area": 1.2667686977},
    "model_22734_f6bad9f7_0026": {"func": model_22734_f6bad9f7_0026, "volume": 0.8246942095, "area": 8.9938101592},
    "model_22742_3c107495_0014": {"func": model_22742_3c107495_0014, "volume": 2.9700863693, "area": 20.7206879243},
    "model_22743_64aefcb6_0000": {"func": model_22743_64aefcb6_0000, "volume": 7534.5325112107, "area": 4847.4564143236},
    "model_22751_90a6225a_0000": {"func": model_22751_90a6225a_0000, "volume": 0.4099778413, "area": 8.7650435035},
    "model_22751_90a6225a_0002": {"func": model_22751_90a6225a_0002, "volume": 0.1525635932, "area": 4.5042584671},
    "model_22751_90a6225a_0010": {"func": model_22751_90a6225a_0010, "volume": 0.1727875959, "area": 4.1469023027},
    "model_22753_071ecad9_0003": {"func": model_22753_071ecad9_0003, "volume": 9.6591129038, "area": 44.9380154395},
    "model_22756_fc3fdda5_0019": {"func": model_22756_fc3fdda5_0019, "volume": 0.1541328188, "area": 2.6464776514},
    "model_22756_fc3fdda5_0024": {"func": model_22756_fc3fdda5_0024, "volume": 0.0634664548, "area": 2.1563891974},
    "model_22760_c2a5214f_0000": {"func": model_22760_c2a5214f_0000, "volume": 22.0853963547, "area": 86.2681342676},
    "model_22760_c2a5214f_0011": {"func": model_22760_c2a5214f_0011, "volume": 6.6864836951, "area": 26.1791896503},
    "model_22776_facf9bcf_0007": {"func": model_22776_facf9bcf_0007, "volume": 21.3445386066, "area": 123.2275273883},
    "model_22776_facf9bcf_0009": {"func": model_22776_facf9bcf_0009, "volume": 2.9746794372, "area": 20.8459101662},
    "model_22788_b6a9e30a_0000": {"func": model_22788_b6a9e30a_0000, "volume": 3630, "area": 5141.5},
    "model_22788_b6a9e30a_0004": {"func": model_22788_b6a9e30a_0004, "volume": 481.5, "area": 660},
    "model_22788_b6a9e30a_0005": {"func": model_22788_b6a9e30a_0005, "volume": 4702.5, "area": 6606},
    "model_22788_b6a9e30a_0006": {"func": model_22788_b6a9e30a_0006, "volume": 6187.5, "area": 8640},
    "model_22788_b6a9e30a_0007": {"func": model_22788_b6a9e30a_0007, "volume": 472.502848991, "area": 830.7463684528},
    "model_22788_b6a9e30a_0009": {"func": model_22788_b6a9e30a_0009, "volume": 5370, "area": 7548.5},
    "model_22788_b6a9e30a_0010": {"func": model_22788_b6a9e30a_0010, "volume": 3378.375, "area": 4795.5},
    "model_22790_2bdc9e13_0004": {"func": model_22790_2bdc9e13_0004, "volume": 7466.356035, "area": 8339.49945},
    "model_22790_2bdc9e13_0005": {"func": model_22790_2bdc9e13_0005, "volume": 1797.4560825, "area": 3090.3164},
    "model_22790_2bdc9e13_0010": {"func": model_22790_2bdc9e13_0010, "volume": 20117.6815387503, "area": 32368.4836500004},
    "model_22848_cc91b848_0006": {"func": model_22848_cc91b848_0006, "volume": 9734.3000878125, "area": 10833.04285},
    "model_22848_cc91b848_0034": {"func": model_22848_cc91b848_0034, "volume": 0.3893293669, "area": 6.2235038042},
    "model_22899_5b97e4f5_0000": {"func": model_22899_5b97e4f5_0000, "volume": 12.4839038072, "area": 33.9134926955},
    "model_23001_234eee16_0001": {"func": model_23001_234eee16_0001, "volume": 0.2648230016, "area": 2.9309733553},
    "model_23001_234eee16_0003": {"func": model_23001_234eee16_0003, "volume": 100.5309649149, "area": 125.6637061436},
    "model_23001_234eee16_0004": {"func": model_23001_234eee16_0004, "volume": 75.3982236862, "area": 100.5309649149},
    "model_23001_234eee16_0006": {"func": model_23001_234eee16_0006, "volume": 5.3218579552, "area": 17.2787595947},
    "model_23044_9a964a68_0007": {"func": model_23044_9a964a68_0007, "volume": 64.501146137, "area": 303.3718482254},
    "model_23054_311abee4_0005": {"func": model_23054_311abee4_0005, "volume": 3.0630528373, "area": 13.8230076758},
    "model_23054_311abee4_0006": {"func": model_23054_311abee4_0006, "volume": 2.0420352248, "area": 9.7389372261},
    "model_23127_38d73061_0000": {"func": model_23127_38d73061_0000, "volume": 2605.0061302577, "area": 2859.0161288378},
    "model_23137_e55b73cb_0005": {"func": model_23137_e55b73cb_0005, "volume": 3.191858136, "area": 16.9646003294},
    "model_23144_88ca00a5_0002": {"func": model_23144_88ca00a5_0002, "volume": 5735.4724, "area": 4999.99},
    "model_23144_88ca00a5_0003": {"func": model_23144_88ca00a5_0003, "volume": 2949.67152, "area": 2696.7688},
    "model_23179_729dc326_0001": {"func": model_23179_729dc326_0001, "volume": 8.4, "area": 27.2},
    "model_23179_729dc326_0004": {"func": model_23179_729dc326_0004, "volume": 236.5853721848, "area": 665.2347738055},
    "model_23182_1e6e757d_0000": {"func": model_23182_1e6e757d_0000, "volume": 0.1104485401, "area": 2.8568645852},
    "model_23190_7d4ff7f9_0005": {"func": model_23190_7d4ff7f9_0005, "volume": 2.0109953077, "area": 18.3681461173},
    "model_23206_b99a5251_0036": {"func": model_23206_b99a5251_0036, "volume": 9.9707963268, "area": 35.8831853072},
    "model_23206_b99a5251_0040": {"func": model_23206_b99a5251_0040, "volume": 0.946998779, "area": 5.9625849051},
    "model_23206_b99a5251_0042": {"func": model_23206_b99a5251_0042, "volume": 8.2994340212, "area": 34.0669915364},
    "model_23206_b99a5251_0046": {"func": model_23206_b99a5251_0046, "volume": 3.168, "area": 22.88},
    "model_23231_efe613bb_0001": {"func": model_23231_efe613bb_0001, "volume": 15.0796447372, "area": 76.4035333353},
    "model_23231_efe613bb_0005": {"func": model_23231_efe613bb_0005, "volume": 105.0723045565, "area": 159.2696979543},
    "model_23231_efe613bb_0011": {"func": model_23231_efe613bb_0011, "volume": 13.0251066259, "area": 33.1564920234},
    "model_23231_efe613bb_0016": {"func": model_23231_efe613bb_0016, "volume": 22.5479488439, "area": 134.2887701623},
    "model_23255_972fbfe6_0014": {"func": model_23255_972fbfe6_0014, "volume": 0.8519056799, "area": 8.1486630249},
    "model_23258_87a2ba81_0001": {"func": model_23258_87a2ba81_0001, "volume": 97.1930227204, "area": 266.2499773917},
    "model_23264_20be13a0_0009": {"func": model_23264_20be13a0_0009, "volume": 0.0934625502, "area": 1.5848317071},
    "model_23278_8d704515_0000": {"func": model_23278_8d704515_0000, "volume": 3.6042117396, "area": 41.5377061442},
    "model_23313_210c6783_0000": {"func": model_23313_210c6783_0000, "volume": 1325.3594007332, "area": 795.2156404399},
    "model_23366_cc0bc28e_0000": {"func": model_23366_cc0bc28e_0000, "volume": 96, "area": 236.1248781675},
    "model_23368_648717d8_0004": {"func": model_23368_648717d8_0004, "volume": 35, "area": 157},
    "model_23376_9b48819a_0000": {"func": model_23376_9b48819a_0000, "volume": 1.4677663412, "area": 22.0723818916},
    "model_23410_0163b27d_0000": {"func": model_23410_0163b27d_0000, "volume": 0.8953539063, "area": 9.5504416669},
    "model_23410_0163b27d_0006": {"func": model_23410_0163b27d_0006, "volume": 0.0848704896, "area": 1.3336791218},
    "model_23410_0163b27d_0007": {"func": model_23410_0163b27d_0007, "volume": 0.1732050808, "area": 2.4248711306},
    "model_23410_0163b27d_0008": {"func": model_23410_0163b27d_0008, "volume": 0.1885820812, "area": 3.22025325},
    "model_23410_0163b27d_0011": {"func": model_23410_0163b27d_0011, "volume": 0.0193989696, "area": 0.4711178308},
    "model_23410_0163b27d_0012": {"func": model_23410_0163b27d_0012, "volume": 0.0523945369, "area": 0.904996547},
    "model_23471_3dafd9b1_0001": {"func": model_23471_3dafd9b1_0001, "volume": 39585.6208250767, "area": 13068.8230693307},
    "model_23472_ed1faab6_0004": {"func": model_23472_ed1faab6_0004, "volume": 1.85053622, "area": 48.3879988654},
    "model_23479_81a49137_0003": {"func": model_23479_81a49137_0003, "volume": 102, "area": 1044.08},
    "model_23493_57512264_0000": {"func": model_23493_57512264_0000, "volume": 34.7018068231, "area": 86.8061942523},
    "model_23493_57512264_0005": {"func": model_23493_57512264_0005, "volume": 0.0439822972, "area": 0.9424777961},
    "model_23505_161e8ec5_0000": {"func": model_23505_161e8ec5_0000, "volume": 177919.9944525129, "area": 20106.1527705887},
    "model_23519_31078773_0002": {"func": model_23519_31078773_0002, "volume": 4.8875327708, "area": 41.8931380356},
    "model_23536_f2c05b8a_0000": {"func": model_23536_f2c05b8a_0000, "volume": 0.0050778, "area": 0.4426739449},
    "model_23539_b3917f22_0001": {"func": model_23539_b3917f22_0001, "volume": 0.0055708577, "area": 0.6322156042},
    "model_23539_b3917f22_0002": {"func": model_23539_b3917f22_0002, "volume": 0.0288157549, "area": 3.0139549885},
    "model_23539_b3917f22_0003": {"func": model_23539_b3917f22_0003, "volume": 114.1804232088, "area": 238.1144762959},
    "model_23539_b3917f22_0005": {"func": model_23539_b3917f22_0005, "volume": 6.9272118012, "area": 46.5112792364},
    "model_23539_b3917f22_0006": {"func": model_23539_b3917f22_0006, "volume": 6.974335691, "area": 53.4699069641},
    "model_23552_10239b96_0000": {"func": model_23552_10239b96_0000, "volume": 44.6171236618, "area": 84.1332408161},
    "model_23554_a0845d54_0000": {"func": model_23554_a0845d54_0000, "volume": 6.5423667011, "area": 50.4696859799},
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
