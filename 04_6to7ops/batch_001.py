"""Batch 001 - passing/04_6to7ops
77 models bundled from Fusion360 Gallery reconstructions.
"""

from build123d import *
from build123d import Edge, BuildLine
from collections import Counter
from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
from OCP.Geom import Geom_BSplineCurve
from OCP.TColStd import TColStd_Array1OfReal, TColStd_Array1OfInteger
from OCP.TColgp import TColgp_Array1OfPnt
from OCP.gp import gp_Pnt


def model_100801_d759cc09_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 136.925, perimeter: 47.9865007051
            with BuildLine():
                Line((0, 13.9), (3.8, 13.9))
                Line((0, 0), (0, 13.9))
                Line((12.7, 0), (0, 0))
                Line((12.7, 5), (12.7, 0))
                Line((3.8, 13.9), (12.7, 5))
            make_face()
        # Symmetric extrude, full_length=True, total=7.6
        extrude(amount=3.8, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 26.52, perimeter: 34.0499566724
            with BuildLine():
                Line((1.2, 13.9), (12.7, 2.4))
                Line((12.7, 5), (12.7, 2.4))
                Line((12.7, 5), (3.8, 13.9))
                Line((1.2, 13.9), (3.8, 13.9))
            make_face()
        # Symmetric extrude, full_length=True, total=2.6
        extrude(amount=1.3, both=True, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on XY construction plane
        # Sketch has 12 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 50.1011494795, perimeter: 41.6761041673
            with BuildLine():
                Line((3.8, 0), (8.9, 0))
                CenterArc((8.9, 3.8), 3.8, -90, 180)
                Line((3.8, 7.6), (8.9, 7.6))
                Line((3.8, 7.6), (3.8, 3.8))
                Line((3.8, 0), (3.8, 3.8))
            make_face()
            with BuildLine():
                CenterArc((8.9, 3.8), 1.9, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 50.1011494795, perimeter: 41.6761041673
            with BuildLine():
                Line((-3.8, 3.8), (-3.8, 7.6))
                Line((-3.8, 7.6), (-8.9, 7.6))
                CenterArc((-8.9, 3.8), 3.8, 90, 180)
                Line((-3.8, 0), (-8.9, 0))
                Line((-3.8, 3.8), (-3.8, 0))
            make_face()
            with BuildLine():
                CenterArc((-8.9, 3.8), 1.9, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.6
        extrude(amount=2.6, mode=Mode.ADD)
    return part.part


def model_100804_1147d10b_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 10 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.9070403054, perimeter: 4.2582126486
            with BuildLine():
                CenterArc((-2.5000002562, 0), 0.4, 119.9999576297, 120.0000847404)
                Line((-2.7, 0.8), (-2.7, 0.3464103094))
                CenterArc((-2.7000002562, 0), 0.8, 89.9999816532, 180.0000366725)
                Line((-2.7, -0.3464103094), (-2.7000000003, -0.8))
            make_face()
            # Profile area: 0.9070389367, perimeter: 4.2582099025
            with BuildLine():
                CenterArc((2.6999991788, 0), 0.8, -89.9999411826, 179.999882365)
                Line((2.7, 0.3464100136), (2.7, 0.8))
                CenterArc((2.4999997438, 0), 0.4, -59.9999576306, 119.9999152612)
                Line((2.7, -0.8), (2.7, -0.3464100136))
            make_face()
            # Profile area: 7.8312295026, perimeter: 15.9653915177
            with BuildLine():
                Line((-2.7, -0.3464103094), (-2.7000000003, -0.8))
                Line((-2.7000000003, -0.8), (2.7, -0.8))
                Line((2.7, -0.8), (2.7, -0.3464100136))
                CenterArc((2.4999997438, 0), 0.4, 59.9999576306, 240.0000847388)
                Line((2.7, 0.3464100136), (2.7, 0.8))
                Line((2.7, 0.8), (-2.7, 0.8))
                Line((-2.7, 0.8), (-2.7, 0.3464103094))
                CenterArc((-2.5000002562, 0), 0.4, -119.9999576299, 239.9999152596)
            make_face()
        # Symmetric extrude, each_side=0.3
        extrude(amount=0.3, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.5, perimeter: 23
            with BuildLine():
                Line((-0.8, -1.3), (-0.8, -5.5))
                Line((-0.8, -1.3), (0.8, -1.3))
                Line((0.8, -1.3), (0.8, -5.5))
                Line((0.8, -5.5), (1.3, -5.5))
                Line((1.3, -5.5), (1.3, -0.8))
                Line((1.3, -0.8), (0.8, -0.8))
                Line((0.8, -0.8), (0.3, -0.8))
                Line((0.3, -0.8), (-0.3, -0.8))
                Line((-0.3, -0.8), (-0.8, -0.8))
                Line((-1.3, -0.8), (-0.8, -0.8))
                Line((-1.3, -5.5), (-1.3, -0.8))
                Line((-0.8, -5.5), (-1.3, -5.5))
            make_face()
        # Symmetric extrude, each_side=1.5
        extrude(amount=1.5, both=True, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1.3, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((0, 4.5)):
                Circle(0.3)
        # OneSide extrude, distance=-13.9
        extrude(amount=-13.9, mode=Mode.SUBTRACT)
    return part.part


def model_101269_f084ba14_0021():
    """Model: leg v1 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 36.29025, perimeter: 24.13
            with BuildLine():
                Line((0, 5.715), (0, 0))
                Line((0, 0), (6.35, 0))
                Line((6.35, 0), (6.35, 5.715))
                Line((6.35, 5.715), (0, 5.715))
            make_face()
        # OneSide extrude, distance=66.04
        extrude(amount=66.04)
    return part.part


def model_101289_a540a982_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.4300000006, perimeter: 2.799999994
            with BuildLine():
                Line((0, 0), (0.35, 0))
                Line((0.35, 0), (0.35, 0.4))
                Line((0.15, 0.400000006), (0.35, 0.4))
                Line((0.15, 0.7), (0.15, 0.400000006))
                Line((-0.35, 0.7), (0.15, 0.7))
                Line((-0.35, 0), (-0.35, 0.7))
                Line((0, 0), (-0.35, 0))
            make_face()
        # Symmetric extrude, full_length=True, total=1.4
        extrude(amount=0.7, both=True)
    return part.part


def model_102931_f0404cf4_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 30 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.0494740539, perimeter: 40.60051257
            with BuildLine():
                Line((0, 0), (0, 0.85))
                Line((0, 0.85), (-0.9350889359, 0.85))
                CenterArc((-0.9350889359, -3.075), 3.925, 90, 180)
                Line((-0.9350889359, -7), (2.332697338, -7))
                CenterArc((2.332697338, -7.667302662), 0.667302662, 0, 90)
                Line((3, -7.667302662), (3, -7.82))
                Line((3, -7.82), (1.1, -7.82))
                CenterArc((1.1, -7.92), 0.1, 90, 90)
                Line((1, -7.92), (1, -7.97))
                CenterArc((1.35, -7.97), 0.35, 180, 90)
                Line((1.35, -8.32), (3.25, -8.32))
                CenterArc((3.25, -7.97), 0.35, -90, 90)
                Line((3.6, -7.97), (3.6, -7.667302662))
                CenterArc((2.332697338, -7.667302662), 1.267302662, 0, 90)
                Line((2.332697338, -6.4), (-0.9350889359, -6.4))
                CenterArc((-0.9350889359, -3.075), 3.325, 112.3599722153, 157.6400277847)
                Line((-2.2, 0), (0, 0))
            make_face()
        # OneSide extrude, distance=4.4
        extrude(amount=4.4)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 16 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.0912, perimeter: 3.896
            with BuildLine():
                Line((1.9, -0.802), (1.2, -0.802))
                Line((1.2, -0.802), (0, -0.802))
                Line((0, -0.802), (0, -0.85))
                Line((0, -0.85), (1.9, -0.85))
                Line((1.9, -0.85), (1.9, -0.802))
            make_face()
            # Profile area: 0.14544, perimeter: 6.156
            with BuildLine():
                Line((0, 0), (3.03, 0))
                Line((0, 0), (0, -0.048))
                Line((0, -0.048), (1.2, -0.048))
                Line((1.2, -0.048), (3.03, -0.048))
                Line((3.03, -0.048), (3.03, 0))
            make_face()
        # OneSide extrude, distance=-2.2
        extrude(amount=-2.2, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 16 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.9048, perimeter: 3.908
            with BuildLine():
                Line((0, -0.048), (1.2, -0.048))
                Line((0, -0.048), (0, -0.802))
                Line((1.2, -0.802), (0, -0.802))
                Line((1.2, -0.048), (1.2, -0.802))
            make_face()
        # OneSide extrude, distance=-0.913
        extrude(amount=-0.913, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 16 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.0151808502, perimeter: 0.9497218049
            with BuildLine():
                Line((4.1340308105, -0.85), (4.4, -0.85))
                Line((4.4, -0.5840308105), (4.4, -0.85))
                CenterArc((4.1340308105, -0.5840308105), 0.2659691895, -90, 90)
            make_face()
            # Profile area: 0.0151808502, perimeter: 0.9497226277
            with BuildLine():
                Line((4.4, 0), (4.4, -0.2659696009))
                Line((4.1340308105, 0), (4.4, 0))
                CenterArc((4.1340308105, -0.2659691895), 0.2659691895, -0.0000886261, 90.0000886261)
            make_face()
        # OneSide extrude, distance=-0.913
        extrude(amount=-0.913, mode=Mode.SUBTRACT)
    return part.part


def model_103552_c3a389ed_0001():
    """Model: Component2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            Circle(2.5)
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((2.5, 0)):
                Circle(0.6)
        # Symmetric extrude, each_side=4.1096
        extrude(amount=4.1096, both=True, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.4018760764, perimeter: 5.4938934233
            Circle(0.8743802951)
        # OneSide extrude, distance=50
        extrude(amount=50, mode=Mode.ADD)
    return part.part


def model_104524_f829aab2_0000():
    """Model: Component2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.3014376029, perimeter: 14.1371669412
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 10 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4.4756924563, perimeter: 9.2214096524
            with BuildLine():
                Line((-1.6969230732, 2.4000000507), (-1.5, 1))
                Line((1.5000000224, 1.0000000149), (-1.5, 1))
                Line((1.6969230732, 2.4000000507), (1.5000000224, 1.0000000149))
                Line((-1.6969230732, 2.4000000507), (1.6969230732, 2.4000000507))
            make_face()
        # Symmetric extrude, full_length=True, total=5
        extrude(amount=2.5, both=True, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.4000000507, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            Circle(0.75)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)
    return part.part


def model_104524_f829aab2_0002():
    """Model: Component3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.3014376029, perimeter: 14.1371669412
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 11.2, perimeter: 13.6
            with BuildLine():
                Line((-2, 3.8000000358), (2, 3.8000000358))
                Line((-2, 1.0000000358), (-2, 3.8000000358))
                Line((2, 1.0000000358), (-2, 1.0000000358))
                Line((2, 3.8000000358), (2, 1.0000000358))
            make_face()
        # Symmetric extrude, full_length=True, total=7
        extrude(amount=3.5, both=True, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3.8000000358, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            Circle(0.75)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)
    return part.part


def model_104542_2e4f8127_0000():
    """Model: TSH-10-C_links"""
    with BuildPart() as part:
        # Sketch11 -> Extrude8 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2714546472, perimeter: 2.2525352513
            with BuildLine():
                Line((-0.7627049575, -0.1234527858), (-0.8027982556, -0.3516673892))
                Line((-0.8027982556, -0.3516673892), (0, -0.3516673892))
                Line((0, -0.3516673892), (0, 0))
                Line((0, 0), (-0.6156730197, 0))
                Line((-0.741016471, 0), (-0.6156730197, 0))
                Line((-0.7627049575, -0.1234527858), (-0.741016471, 0))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch14 -> Extrude11 (Join)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0452389342, perimeter: 0.7539822369
            with Locations((-0.1597539173, 0.200142113)):
                Circle(0.12)
        # OneSide extrude, distance=1.34
        extrude(amount=1.34, mode=Mode.ADD)

        # Sketch11 -> Extrude12 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.015393804, perimeter: 0.4398229715
            with Locations((1.2182124796, -0.1582503919)):
                Circle(0.07)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.SUBTRACT)
    return part.part


def model_104641_2cd02839_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 96, perimeter: 40
            with BuildLine():
                Line((7, -3), (-5, -3))
                Line((7, 5), (7, -3))
                Line((-5, 5), (7, 5))
                Line((-5, -3), (-5, 5))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.3, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 62.7512142571, perimeter: 32.6127632425
            with BuildLine():
                Line((6.0827778486, -2.2236037726), (-4, -2.2236037726))
                Line((6.0827778486, 4), (6.0827778486, -2.2236037726))
                Line((-4, 4), (6.0827778486, 4))
                Line((-4, -2.2236037726), (-4, 4))
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)

        # Sketch17 -> Extrude18 (NewBody)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1500000045, perimeter: 1.6000000238
            with BuildLine():
                Line((2.5152645686, -3.3000000492), (2.0152645611, -3.3000000492))
                Line((2.5152645686, -3.0000000447), (2.5152645686, -3.3000000492))
                Line((2.0152645611, -3.0000000447), (2.5152645686, -3.0000000447))
                Line((2.0152645611, -3.3000000492), (2.0152645611, -3.0000000447))
            make_face()
            # Profile area: 0.1600000048, perimeter: 1.6000000238
            with BuildLine():
                Line((3.015264576, -3.3000000492), (2.6152645701, -3.3000000492))
                Line((3.015264576, -2.9000000432), (3.015264576, -3.3000000492))
                Line((2.6152645701, -2.9000000432), (3.015264576, -2.9000000432))
                Line((2.6152645701, -3.3000000492), (2.6152645701, -2.9000000432))
            make_face()
            # Profile area: 0.1600000048, perimeter: 1.6000000238
            with BuildLine():
                Line((3.5152645835, -3.3000000492), (3.1152645775, -3.3000000492))
                Line((3.5152645835, -2.9000000432), (3.5152645835, -3.3000000492))
                Line((3.1152645775, -2.9000000432), (3.5152645835, -2.9000000432))
                Line((3.1152645775, -3.3000000492), (3.1152645775, -2.9000000432))
            make_face()
            # Profile area: 0.200000006, perimeter: 1.8000000268
            with BuildLine():
                Line((3.415264582, -2.8000000417), (3.015264576, -2.8000000417))
                Line((3.415264582, -2.3000000343), (3.415264582, -2.8000000417))
                Line((3.015264576, -2.3000000343), (3.415264582, -2.3000000343))
                Line((3.015264576, -2.8000000417), (3.015264576, -2.3000000343))
            make_face()
            # Profile area: 0.200000006, perimeter: 1.8000000268
            with BuildLine():
                Line((2.9152645745, -1.4000000209), (2.5152645686, -1.4000000209))
                Line((2.9152645745, -0.9000000134), (2.9152645745, -1.4000000209))
                Line((2.5152645686, -0.9000000134), (2.9152645745, -0.9000000134))
                Line((2.5152645686, -1.4000000209), (2.5152645686, -0.9000000134))
            make_face()
            # Profile area: 0.200000006, perimeter: 1.8000000268
            with BuildLine():
                Line((2.9152645745, -2.1000000313), (2.5152645686, -2.1000000313))
                Line((2.9152645745, -1.6000000238), (2.9152645745, -2.1000000313))
                Line((2.5152645686, -1.6000000238), (2.9152645745, -1.6000000238))
                Line((2.5152645686, -2.1000000313), (2.5152645686, -1.6000000238))
            make_face()
            # Profile area: 0.200000006, perimeter: 1.8000000268
            with BuildLine():
                Line((3.015264576, -2.1000000313), (3.015264576, -1.6000000238))
                Line((3.415264582, -2.1000000313), (3.015264576, -2.1000000313))
                Line((3.415264582, -1.6000000238), (3.415264582, -2.1000000313))
                Line((3.015264576, -1.6000000238), (3.415264582, -1.6000000238))
            make_face()
            # Profile area: 0.0900000027, perimeter: 1.2000000179
            with BuildLine():
                Line((3.9152645894, -3.3000000492), (3.615264585, -3.3000000492))
                Line((3.9152645894, -3.0000000447), (3.9152645894, -3.3000000492))
                Line((3.615264585, -3.0000000447), (3.9152645894, -3.0000000447))
                Line((3.615264585, -3.3000000492), (3.615264585, -3.0000000447))
            make_face()
            # Profile area: 0.1500000045, perimeter: 1.6000000238
            with BuildLine():
                Line((3.8152645879, -2.8000000417), (3.5152645835, -2.8000000417))
                Line((3.8152645879, -2.3000000343), (3.8152645879, -2.8000000417))
                Line((3.5152645835, -2.3000000343), (3.8152645879, -2.3000000343))
                Line((3.5152645835, -2.8000000417), (3.5152645835, -2.3000000343))
            make_face()
            # Profile area: 0.200000006, perimeter: 1.8000000268
            with BuildLine():
                Line((4.4152645969, -2.8000000417), (4.0152645909, -2.8000000417))
                Line((4.4152645969, -2.3000000343), (4.4152645969, -2.8000000417))
                Line((4.0152645909, -2.3000000343), (4.4152645969, -2.3000000343))
                Line((4.0152645909, -2.8000000417), (4.0152645909, -2.3000000343))
            make_face()
            # Profile area: 0.0900000027, perimeter: 1.2000000179
            with BuildLine():
                Line((4.3152645954, -3.3000000492), (4.0152645909, -3.3000000492))
                Line((4.3152645954, -3.0000000447), (4.3152645954, -3.3000000492))
                Line((4.0152645909, -3.0000000447), (4.3152645954, -3.0000000447))
                Line((4.0152645909, -3.3000000492), (4.0152645909, -3.0000000447))
            make_face()
            # Profile area: 0.200000006, perimeter: 1.8000000268
            with BuildLine():
                Line((4.9152646043, -2.8000000417), (4.5152645984, -2.8000000417))
                Line((4.9152646043, -2.3000000343), (4.9152646043, -2.8000000417))
                Line((4.5152645984, -2.3000000343), (4.9152646043, -2.3000000343))
                Line((4.5152645984, -2.8000000417), (4.5152645984, -2.3000000343))
            make_face()
            # Profile area: 0.1200000036, perimeter: 1.4000000209
            with BuildLine():
                Line((4.9152646043, -3.3000000492), (4.5152645984, -3.3000000492))
                Line((4.9152646043, -3.0000000447), (4.9152646043, -3.3000000492))
                Line((4.5152645984, -3.0000000447), (4.9152646043, -3.0000000447))
                Line((4.5152645984, -3.3000000492), (4.5152645984, -3.0000000447))
            make_face()
            # Profile area: 0.1500000045, perimeter: 1.6000000238
            with BuildLine():
                Line((3.5152645835, -2.1000000313), (3.5152645835, -1.6000000238))
                Line((3.8152645879, -2.1000000313), (3.5152645835, -2.1000000313))
                Line((3.8152645879, -1.6000000238), (3.8152645879, -2.1000000313))
                Line((3.5152645835, -1.6000000238), (3.8152645879, -1.6000000238))
            make_face()
            # Profile area: 0.1500000045, perimeter: 1.6000000238
            with BuildLine():
                Line((3.8152645879, -1.4000000209), (3.5152645835, -1.4000000209))
                Line((3.8152645879, -0.9000000134), (3.8152645879, -1.4000000209))
                Line((3.5152645835, -0.9000000134), (3.8152645879, -0.9000000134))
                Line((3.5152645835, -1.4000000209), (3.5152645835, -0.9000000134))
            make_face()
            # Profile area: 0.200000006, perimeter: 1.8000000268
            with BuildLine():
                Line((3.415264582, -1.4000000209), (3.015264576, -1.4000000209))
                Line((3.415264582, -0.9000000134), (3.415264582, -1.4000000209))
                Line((3.015264576, -0.9000000134), (3.415264582, -0.9000000134))
                Line((3.015264576, -1.4000000209), (3.015264576, -0.9000000134))
            make_face()
            # Profile area: 0.200000006, perimeter: 1.8000000268
            with BuildLine():
                Line((2.9152645745, -0.6000000089), (2.5152645686, -0.6000000089))
                Line((2.9152645745, -0.1000000015), (2.9152645745, -0.6000000089))
                Line((2.5152645686, -0.1000000015), (2.9152645745, -0.1000000015))
                Line((2.5152645686, -0.6000000089), (2.5152645686, -0.1000000015))
            make_face()
            # Profile area: 0.2250000067, perimeter: 1.9000000283
            with BuildLine():
                Line((3.415264582, -0.6000000089), (2.9652645753, -0.6000000089))
                Line((3.415264582, -0.1000000015), (3.415264582, -0.6000000089))
                Line((2.9652645753, -0.1000000015), (3.415264582, -0.1000000015))
                Line((2.9652645753, -0.6000000089), (2.9652645753, -0.1000000015))
            make_face()
            # Profile area: 0.200000006, perimeter: 1.8000000268
            with BuildLine():
                Line((2.9152645745, 0.1000000015), (2.5152645686, 0.1000000015))
                Line((2.9152645745, 0.6000000089), (2.9152645745, 0.1000000015))
                Line((2.5152645686, 0.6000000089), (2.9152645745, 0.6000000089))
                Line((2.5152645686, 0.1000000015), (2.5152645686, 0.6000000089))
            make_face()
            # Profile area: 0.200000006, perimeter: 1.8000000268
            with BuildLine():
                Line((3.415264582, 0.1000000015), (3.015264576, 0.1000000015))
                Line((3.415264582, 0.6000000089), (3.415264582, 0.1000000015))
                Line((3.015264576, 0.6000000089), (3.415264582, 0.6000000089))
                Line((3.015264576, 0.1000000015), (3.015264576, 0.6000000089))
            make_face()
            # Profile area: 0.1600000048, perimeter: 1.6000000238
            with BuildLine():
                Line((2.9152645745, 0.8000000119), (2.5152645686, 0.8000000119))
                Line((2.9152645745, 1.2000000179), (2.9152645745, 0.8000000119))
                Line((2.5152645686, 1.2000000179), (2.9152645745, 1.2000000179))
                Line((2.5152645686, 0.8000000119), (2.5152645686, 1.2000000179))
            make_face()
            # Profile area: 0.1600000048, perimeter: 1.6000000238
            with BuildLine():
                Line((3.415264582, 0.8000000119), (3.015264576, 0.8000000119))
                Line((3.415264582, 1.2000000179), (3.415264582, 0.8000000119))
                Line((3.015264576, 1.2000000179), (3.415264582, 1.2000000179))
                Line((3.015264576, 0.8000000119), (3.015264576, 1.2000000179))
            make_face()
            # Profile area: 0.200000006, perimeter: 1.8000000268
            with BuildLine():
                Line((2.9152645745, 1.4000000209), (2.5152645686, 1.4000000209))
                Line((2.9152645745, 1.9000000283), (2.9152645745, 1.4000000209))
                Line((2.5152645686, 1.9000000283), (2.9152645745, 1.9000000283))
                Line((2.5152645686, 1.4000000209), (2.5152645686, 1.9000000283))
            make_face()
            # Profile area: 0.200000006, perimeter: 1.8000000268
            with BuildLine():
                Line((3.415264582, 1.4000000209), (3.015264576, 1.4000000209))
                Line((3.415264582, 1.9000000283), (3.415264582, 1.4000000209))
                Line((3.015264576, 1.9000000283), (3.415264582, 1.9000000283))
                Line((3.015264576, 1.4000000209), (3.015264576, 1.9000000283))
            make_face()
            # Profile area: 0.1812187026, perimeter: 1.7060935112
            with BuildLine():
                Line((3.415264582, 2.0469532876), (3.015264576, 2.0469532876))
                Line((3.415264582, 2.5000000373), (3.415264582, 2.0469532876))
                Line((3.015264576, 2.5000000373), (3.415264582, 2.5000000373))
                Line((3.015264576, 2.0469532876), (3.015264576, 2.5000000373))
            make_face()
            # Profile area: 0.200000006, perimeter: 1.8000000268
            with BuildLine():
                Line((2.9152645745, 2.0000000298), (2.5152645686, 2.0000000298))
                Line((2.9152645745, 2.5000000373), (2.9152645745, 2.0000000298))
                Line((2.5152645686, 2.5000000373), (2.9152645745, 2.5000000373))
                Line((2.5152645686, 2.0000000298), (2.5152645686, 2.5000000373))
            make_face()
            # Profile area: 0.200000006, perimeter: 1.8000000268
            with BuildLine():
                Line((2.9152645745, 2.7000000402), (2.5152645686, 2.7000000402))
                Line((2.9152645745, 3.2000000477), (2.9152645745, 2.7000000402))
                Line((2.5152645686, 3.2000000477), (2.9152645745, 3.2000000477))
                Line((2.5152645686, 2.7000000402), (2.5152645686, 3.2000000477))
            make_face()
            # Profile area: 0.200000006, perimeter: 1.8000000268
            with BuildLine():
                Line((3.415264582, 2.7000000402), (3.015264576, 2.7000000402))
                Line((3.415264582, 3.2000000477), (3.415264582, 2.7000000402))
                Line((3.015264576, 3.2000000477), (3.415264582, 3.2000000477))
                Line((3.015264576, 2.7000000402), (3.015264576, 3.2000000477))
            make_face()
            # Profile area: 0.200000006, perimeter: 1.8000000268
            with BuildLine():
                Line((2.9152645745, 3.3000000492), (2.5152645686, 3.3000000492))
                Line((2.9152645745, 3.8000000566), (2.9152645745, 3.3000000492))
                Line((2.5152645686, 3.8000000566), (2.9152645745, 3.8000000566))
                Line((2.5152645686, 3.3000000492), (2.5152645686, 3.8000000566))
            make_face()
            # Profile area: 0.200000006, perimeter: 1.8000000268
            with BuildLine():
                Line((3.415264582, 3.3000000492), (3.015264576, 3.3000000492))
                Line((3.415264582, 3.8000000566), (3.415264582, 3.3000000492))
                Line((3.015264576, 3.8000000566), (3.415264582, 3.8000000566))
                Line((3.015264576, 3.3000000492), (3.015264576, 3.8000000566))
            make_face()
            # Profile area: 0.200000006, perimeter: 1.8000000268
            with BuildLine():
                Line((3.415264582, 4.0000000596), (3.015264576, 4.0000000596))
                Line((3.415264582, 4.5000000671), (3.415264582, 4.0000000596))
                Line((3.015264576, 4.5000000671), (3.415264582, 4.5000000671))
                Line((3.015264576, 4.0000000596), (3.015264576, 4.5000000671))
            make_face()
            # Profile area: 0.200000006, perimeter: 1.8000000268
            with BuildLine():
                Line((2.9152645745, 4.0000000596), (2.5152645686, 4.0000000596))
                Line((2.9152645745, 4.5000000671), (2.9152645745, 4.0000000596))
                Line((2.5152645686, 4.5000000671), (2.9152645745, 4.5000000671))
                Line((2.5152645686, 4.0000000596), (2.5152645686, 4.5000000671))
            make_face()
            # Profile area: 0.200000006, perimeter: 1.8000000268
            with BuildLine():
                Line((2.9152645745, 4.6000000685), (2.5152645686, 4.6000000685))
                Line((2.9152645745, 5.100000076), (2.9152645745, 4.6000000685))
                Line((2.5152645686, 5.100000076), (2.9152645745, 5.100000076))
                Line((2.5152645686, 4.6000000685), (2.5152645686, 5.100000076))
            make_face()
            # Profile area: 0.200000006, perimeter: 1.8000000268
            with BuildLine():
                Line((3.415264582, 4.6000000685), (3.015264576, 4.6000000685))
                Line((3.415264582, 5.100000076), (3.415264582, 4.6000000685))
                Line((3.015264576, 5.100000076), (3.415264582, 5.100000076))
                Line((3.015264576, 4.6000000685), (3.015264576, 5.100000076))
            make_face()
            # Profile area: 0.1500000045, perimeter: 1.6000000238
            with BuildLine():
                Line((3.8152645879, 4.6000000685), (3.5152645835, 4.6000000685))
                Line((3.8152645879, 5.100000076), (3.8152645879, 4.6000000685))
                Line((3.5152645835, 5.100000076), (3.8152645879, 5.100000076))
                Line((3.5152645835, 4.6000000685), (3.5152645835, 5.100000076))
            make_face()
            # Profile area: 0.4400000131, perimeter: 3.0000000447
            with BuildLine():
                Line((5.0152646058, 4.70000007), (3.9152645894, 4.70000007))
                Line((5.0152646058, 5.100000076), (5.0152646058, 4.70000007))
                Line((3.9152645894, 5.100000076), (5.0152646058, 5.100000076))
                Line((3.9152645894, 4.70000007), (3.9152645894, 5.100000076))
            make_face()
            # Profile area: 0.200000006, perimeter: 1.8000000268
            with BuildLine():
                Line((4.9152646043, 4.0000000596), (4.5152645984, 4.0000000596))
                Line((4.9152646043, 4.5000000671), (4.9152646043, 4.0000000596))
                Line((4.5152645984, 4.5000000671), (4.9152646043, 4.5000000671))
                Line((4.5152645984, 4.0000000596), (4.5152645984, 4.5000000671))
            make_face()
            # Profile area: 0.200000006, perimeter: 1.8000000268
            with BuildLine():
                Line((4.4152645969, 4.0000000596), (4.0152645909, 4.0000000596))
                Line((4.4152645969, 4.5000000671), (4.4152645969, 4.0000000596))
                Line((4.0152645909, 4.5000000671), (4.4152645969, 4.5000000671))
                Line((4.0152645909, 4.0000000596), (4.0152645909, 4.5000000671))
            make_face()
            # Profile area: 0.1500000045, perimeter: 1.6000000238
            with BuildLine():
                Line((3.8152645879, 4.0000000596), (3.5152645835, 4.0000000596))
                Line((3.8152645879, 4.5000000671), (3.8152645879, 4.0000000596))
                Line((3.5152645835, 4.5000000671), (3.8152645879, 4.5000000671))
                Line((3.5152645835, 4.0000000596), (3.5152645835, 4.5000000671))
            make_face()
            # Profile area: 0.1500000045, perimeter: 1.6000000238
            with BuildLine():
                Line((3.8152645879, 3.3000000492), (3.5152645835, 3.3000000492))
                Line((3.8152645879, 3.8000000566), (3.8152645879, 3.3000000492))
                Line((3.5152645835, 3.8000000566), (3.8152645879, 3.8000000566))
                Line((3.5152645835, 3.3000000492), (3.5152645835, 3.8000000566))
            make_face()
            # Profile area: 0.1500000045, perimeter: 1.6000000238
            with BuildLine():
                Line((3.8152645879, 2.7000000402), (3.5152645835, 2.7000000402))
                Line((3.8152645879, 3.2000000477), (3.8152645879, 2.7000000402))
                Line((3.5152645835, 3.2000000477), (3.8152645879, 3.2000000477))
                Line((3.5152645835, 2.7000000402), (3.5152645835, 3.2000000477))
            make_face()
            # Profile area: 0.200000006, perimeter: 1.8000000268
            with BuildLine():
                Line((4.4152645969, 2.7000000402), (4.0152645909, 2.7000000402))
                Line((4.4152645969, 3.2000000477), (4.4152645969, 2.7000000402))
                Line((4.0152645909, 3.2000000477), (4.4152645969, 3.2000000477))
                Line((4.0152645909, 2.7000000402), (4.0152645909, 3.2000000477))
            make_face()
            # Profile area: 0.200000006, perimeter: 1.8000000268
            with BuildLine():
                Line((4.4152645969, 3.3000000492), (4.0152645909, 3.3000000492))
                Line((4.4152645969, 3.8000000566), (4.4152645969, 3.3000000492))
                Line((4.0152645909, 3.8000000566), (4.4152645969, 3.8000000566))
                Line((4.0152645909, 3.3000000492), (4.0152645909, 3.8000000566))
            make_face()
            # Profile area: 0.200000006, perimeter: 1.8000000268
            with BuildLine():
                Line((4.9152646043, 3.3000000492), (4.5152645984, 3.3000000492))
                Line((4.9152646043, 3.8000000566), (4.9152646043, 3.3000000492))
                Line((4.5152645984, 3.8000000566), (4.9152646043, 3.8000000566))
                Line((4.5152645984, 3.3000000492), (4.5152645984, 3.8000000566))
            make_face()
            # Profile area: 0.200000006, perimeter: 1.8000000268
            with BuildLine():
                Line((4.9152646043, 2.7000000402), (4.5152645984, 2.7000000402))
                Line((4.9152646043, 3.2000000477), (4.9152646043, 2.7000000402))
                Line((4.5152645984, 3.2000000477), (4.9152646043, 3.2000000477))
                Line((4.5152645984, 2.7000000402), (4.5152645984, 3.2000000477))
            make_face()
            # Profile area: 0.1500000045, perimeter: 1.6000000238
            with BuildLine():
                Line((3.8152645879, 2.0000000298), (3.5152645835, 2.0000000298))
                Line((3.8152645879, 2.5000000373), (3.8152645879, 2.0000000298))
                Line((3.5152645835, 2.5000000373), (3.8152645879, 2.5000000373))
                Line((3.5152645835, 2.0000000298), (3.5152645835, 2.5000000373))
            make_face()
            # Profile area: 0.200000006, perimeter: 1.8000000268
            with BuildLine():
                Line((4.4152645969, 2.0000000298), (4.0152645909, 2.0000000298))
                Line((4.4152645969, 2.5000000373), (4.4152645969, 2.0000000298))
                Line((4.0152645909, 2.5000000373), (4.4152645969, 2.5000000373))
                Line((4.0152645909, 2.0000000298), (4.0152645909, 2.5000000373))
            make_face()
            # Profile area: 0.200000006, perimeter: 1.8000000268
            with BuildLine():
                Line((4.9152646043, 2.0000000298), (4.5152645984, 2.0000000298))
                Line((4.9152646043, 2.5000000373), (4.9152646043, 2.0000000298))
                Line((4.5152645984, 2.5000000373), (4.9152646043, 2.5000000373))
                Line((4.5152645984, 2.0000000298), (4.5152645984, 2.5000000373))
            make_face()
            # Profile area: 0.200000006, perimeter: 1.8000000268
            with BuildLine():
                Line((4.9152646043, 1.4000000209), (4.5152645984, 1.4000000209))
                Line((4.9152646043, 1.9000000283), (4.9152646043, 1.4000000209))
                Line((4.5152645984, 1.9000000283), (4.9152646043, 1.9000000283))
                Line((4.5152645984, 1.4000000209), (4.5152645984, 1.9000000283))
            make_face()
            # Profile area: 0.200000006, perimeter: 1.8000000268
            with BuildLine():
                Line((4.4152645969, 1.4000000209), (4.0152645909, 1.4000000209))
                Line((4.4152645969, 1.9000000283), (4.4152645969, 1.4000000209))
                Line((4.0152645909, 1.9000000283), (4.4152645969, 1.9000000283))
                Line((4.0152645909, 1.4000000209), (4.0152645909, 1.9000000283))
            make_face()
            # Profile area: 0.1500000045, perimeter: 1.6000000238
            with BuildLine():
                Line((3.8152645879, 1.4000000209), (3.5152645835, 1.4000000209))
                Line((3.8152645879, 1.9000000283), (3.8152645879, 1.4000000209))
                Line((3.5152645835, 1.9000000283), (3.8152645879, 1.9000000283))
                Line((3.5152645835, 1.4000000209), (3.5152645835, 1.9000000283))
            make_face()
            # Profile area: 0.1200000036, perimeter: 1.4000000209
            with BuildLine():
                Line((3.8152645879, 0.8000000119), (3.5152645835, 0.8000000119))
                Line((3.8152645879, 1.2000000179), (3.8152645879, 0.8000000119))
                Line((3.5152645835, 1.2000000179), (3.8152645879, 1.2000000179))
                Line((3.5152645835, 0.8000000119), (3.5152645835, 1.2000000179))
            make_face()
            # Profile area: 0.1600000048, perimeter: 1.6000000238
            with BuildLine():
                Line((4.4152645969, 0.8000000119), (4.0152645909, 0.8000000119))
                Line((4.4152645969, 1.2000000179), (4.4152645969, 0.8000000119))
                Line((4.0152645909, 1.2000000179), (4.4152645969, 1.2000000179))
                Line((4.0152645909, 0.8000000119), (4.0152645909, 1.2000000179))
            make_face()
            # Profile area: 0.1600000048, perimeter: 1.6000000238
            with BuildLine():
                Line((4.9152646043, 0.8000000119), (4.5152645984, 0.8000000119))
                Line((4.9152646043, 1.2000000179), (4.9152646043, 0.8000000119))
                Line((4.5152645984, 1.2000000179), (4.9152646043, 1.2000000179))
                Line((4.5152645984, 0.8000000119), (4.5152645984, 1.2000000179))
            make_face()
            # Profile area: 0.840000025, perimeter: 5.0000000745
            with BuildLine():
                Line((4.9152646043, 0.5000000075), (4.9152646043, -1.6000000238))
                Line((4.5152645984, 0.5000000075), (4.9152646043, 0.5000000075))
                Line((4.5152645984, -1.6000000238), (4.5152645984, 0.5000000075))
                Line((4.9152646043, -1.6000000238), (4.5152645984, -1.6000000238))
            make_face()
            # Profile area: 0.200000006, perimeter: 1.8000000268
            with BuildLine():
                Line((4.4152645969, 0.1000000015), (4.0152645909, 0.1000000015))
                Line((4.4152645969, 0.6000000089), (4.4152645969, 0.1000000015))
                Line((4.0152645909, 0.6000000089), (4.4152645969, 0.6000000089))
                Line((4.0152645909, 0.1000000015), (4.0152645909, 0.6000000089))
            make_face()
            # Profile area: 0.1500000045, perimeter: 1.6000000238
            with BuildLine():
                Line((3.8152645879, 0.1000000015), (3.5152645835, 0.1000000015))
                Line((3.8152645879, 0.6000000089), (3.8152645879, 0.1000000015))
                Line((3.5152645835, 0.6000000089), (3.8152645879, 0.6000000089))
                Line((3.5152645835, 0.1000000015), (3.5152645835, 0.6000000089))
            make_face()
            # Profile area: 0.200000006, perimeter: 1.8000000268
            with BuildLine():
                Line((4.4152645969, -0.6000000089), (4.0152645909, -0.6000000089))
                Line((4.4152645969, -0.1000000015), (4.4152645969, -0.6000000089))
                Line((4.0152645909, -0.1000000015), (4.4152645969, -0.1000000015))
                Line((4.0152645909, -0.6000000089), (4.0152645909, -0.1000000015))
            make_face()
            # Profile area: 0.1500000045, perimeter: 1.6000000238
            with BuildLine():
                Line((3.8152645879, -0.6000000089), (3.5152645835, -0.6000000089))
                Line((3.8152645879, -0.1000000015), (3.8152645879, -0.6000000089))
                Line((3.5152645835, -0.1000000015), (3.8152645879, -0.1000000015))
                Line((3.5152645835, -0.6000000089), (3.5152645835, -0.1000000015))
            make_face()
            # Profile area: 0.200000006, perimeter: 1.8000000268
            with BuildLine():
                Line((4.4152645969, -1.4000000209), (4.0152645909, -1.4000000209))
                Line((4.4152645969, -0.9000000134), (4.4152645969, -1.4000000209))
                Line((4.0152645909, -0.9000000134), (4.4152645969, -0.9000000134))
                Line((4.0152645909, -1.4000000209), (4.0152645909, -0.9000000134))
            make_face()
            # Profile area: 0.200000006, perimeter: 1.8000000268
            with BuildLine():
                Line((4.0152645909, -2.1000000313), (4.0152645909, -1.6000000238))
                Line((4.4152645969, -2.1000000313), (4.0152645909, -2.1000000313))
                Line((4.4152645969, -1.6000000238), (4.4152645969, -2.1000000313))
                Line((4.0152645909, -1.6000000238), (4.4152645969, -1.6000000238))
            make_face()
            # Profile area: 0.1600000048, perimeter: 1.6000000238
            with BuildLine():
                Line((4.9152646043, -2.1000000313), (4.5152645984, -2.1000000313))
                Line((4.9152646043, -1.7000000253), (4.9152646043, -2.1000000313))
                Line((4.5152645984, -1.7000000253), (4.9152646043, -1.7000000253))
                Line((4.5152645984, -2.1000000313), (4.5152645984, -1.7000000253))
            make_face()
        # OneSide extrude, distance=-0.02
        extrude(amount=-0.02)
    return part.part


def model_104740_d3638bbe_0004():
    """Model: Spur Gear (20 teeth)"""
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
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.0319791519, perimeter: 6.9047179978
            with BuildLine():
                CenterArc((0, 0), 0.69892, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0216610644, perimeter: 0.5720512618
            with BuildLine():
                _nurbs_edge([(0.748474394, -0.0701448742), (0.7488478284, -0.0701792213), (0.7495946717, -0.0702382482), (0.7507148592, -0.0702977868), (0.7522084211, -0.0703219335), (0.7540760834, -0.0702761335), (0.7559453638, -0.0701749006), (0.7578170855, -0.0700386479), (0.7596917283, -0.0698828559), (0.7615692008, -0.0697137854), (0.7634490367, -0.0695313484), (0.7653305685, -0.0693315793), (0.7672131041, -0.0691091893), (0.7690961133, -0.0688602262), (0.770979379, -0.0685842718), (0.77286289, -0.0682831577), (0.7747467595, -0.0679600244), (0.7766311371, -0.0676182857), (0.7785161157, -0.0672605527), (0.7804016625, -0.0668878205), (0.7822876667, -0.0665000542), (0.7841739725, -0.0660965944), (0.7860604164, -0.0656766128), (0.7879468659, -0.0652395905), (0.7898332471, -0.0647856529), (0.7917195228, -0.0643153152), (0.7936056782, -0.0638293168), (0.7954917048, -0.0633284295), (0.7973775827, -0.0628132571), (0.7992632696, -0.0622841024), (0.8011487099, -0.0617410806), (0.8030338405, -0.0611841908), (0.8049185977, -0.0606134005), (0.8068029242, -0.0600287345), (0.8086867742, -0.0594303307), (0.8105701086, -0.058818393), (0.8124528928, -0.0581931613), (0.814335094, -0.0575548767), (0.8162166774, -0.0569037443), (0.8180976046, -0.0562399111), (0.8199778351, -0.0555634861), (0.8218573274, -0.0548745542), (0.8237360401, -0.0541731915), (0.8256139332, -0.0534594821), (0.8274909689, -0.0527335284), (0.8293671109, -0.0519954424), (0.8312423241, -0.0512453404), (0.8331165741, -0.0504833364), (0.8349898269, -0.0497095357), (0.8368620482, -0.0489240305), (0.8387332037, -0.0481269041), (0.840603259, -0.0473182335), (0.8424721793, -0.0464980923), (0.8443399297, -0.0456665543), (0.8462064751, -0.044823696), (0.8480717807, -0.043969594), (0.8499358124, -0.043104324), (0.8517985375, -0.0422279595), (0.853659925, -0.0413405697), (0.8555199461, -0.0404422189), (0.8573785725, -0.0395329682), (0.859235775, -0.0386128771), (0.8610915226, -0.0376820044), (0.8629457808, -0.0367404106), (0.8647985107, -0.0357881591), (0.8666496723, -0.0348253131), (0.8684992271, -0.0338519342), (0.8703471414, -0.0328680795), (0.8721933891, -0.0318738001), (0.8740379543, -0.0308691386), (0.8758808289, -0.0298541289), (0.8773537737, -0.0290338623), (0.8784577203, -0.0284140235), (0.8791933462, -0.0279987367), (0.8795610745, -0.027790578)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((0, 0), 0.88, -1.8097131993, 3.6194263985)
                _nurbs_edge([(0.748474394, 0.0701448742), (0.7488478284, 0.0701792213), (0.7495946717, 0.0702382482), (0.7507148592, 0.0702977868), (0.7522084211, 0.0703219335), (0.7540760834, 0.0702761335), (0.7559453638, 0.0701749006), (0.7578170855, 0.0700386479), (0.7596917283, 0.0698828559), (0.7615692008, 0.0697137854), (0.7634490367, 0.0695313484), (0.7653305685, 0.0693315793), (0.7672131041, 0.0691091893), (0.7690961133, 0.0688602262), (0.770979379, 0.0685842718), (0.77286289, 0.0682831577), (0.7747467595, 0.0679600244), (0.7766311371, 0.0676182857), (0.7785161157, 0.0672605527), (0.7804016625, 0.0668878205), (0.7822876667, 0.0665000542), (0.7841739725, 0.0660965944), (0.7860604164, 0.0656766128), (0.7879468659, 0.0652395905), (0.7898332471, 0.0647856529), (0.7917195228, 0.0643153152), (0.7936056782, 0.0638293168), (0.7954917048, 0.0633284295), (0.7973775827, 0.0628132571), (0.7992632696, 0.0622841024), (0.8011487099, 0.0617410806), (0.8030338405, 0.0611841908), (0.8049185977, 0.0606134005), (0.8068029242, 0.0600287345), (0.8086867742, 0.0594303307), (0.8105701086, 0.058818393), (0.8124528928, 0.0581931613), (0.814335094, 0.0575548767), (0.8162166774, 0.0569037443), (0.8180976046, 0.0562399111), (0.8199778351, 0.0555634861), (0.8218573274, 0.0548745542), (0.8237360401, 0.0541731915), (0.8256139332, 0.0534594821), (0.8274909689, 0.0527335284), (0.8293671109, 0.0519954424), (0.8312423241, 0.0512453404), (0.8331165741, 0.0504833364), (0.8349898269, 0.0497095357), (0.8368620482, 0.0489240305), (0.8387332037, 0.0481269041), (0.840603259, 0.0473182335), (0.8424721793, 0.0464980923), (0.8443399297, 0.0456665543), (0.8462064751, 0.044823696), (0.8480717807, 0.043969594), (0.8499358124, 0.043104324), (0.8517985375, 0.0422279595), (0.853659925, 0.0413405697), (0.8555199461, 0.0404422189), (0.8573785725, 0.0395329682), (0.859235775, 0.0386128771), (0.8610915226, 0.0376820044), (0.8629457808, 0.0367404106), (0.8647985107, 0.0357881591), (0.8666496723, 0.0348253131), (0.8684992271, 0.0338519342), (0.8703471414, 0.0328680795), (0.8721933891, 0.0318738001), (0.8740379543, 0.0308691386), (0.8758808289, 0.0298541289), (0.8773537737, 0.0290338623), (0.8784577203, 0.0284140235), (0.8791933462, 0.0279987367), (0.8795610745, 0.027790578)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                Line((0.6948751611, 0.065215016), (0.748474394, 0.0701448742))
                Line((0.6948751611, -0.065215016), (0.6948751611, 0.065215016))
                Line((0.6948751611, -0.065215016), (0.748474394, -0.0701448742))
            make_face()
        # OneSide extrude, distance=0.8
        extrude(amount=0.8, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on XY construction plane
        # Sketch has 43 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.8514647189, perimeter: 6.2007448477
            with BuildLine():
                Line((-0.8, 0.6681377055), (-0.8, -0.6681377055))
                _nurbs_edge([(-0.8, -0.6681377055), (-0.7751378016, -0.6681377055), (-0.7268403378, -0.6693818941), (-0.6586746967, -0.6749804854), (-0.5758732014, -0.6895785133), (-0.4832453316, -0.7177364958), (-0.3981952278, -0.7529937905), (-0.3172988646, -0.7918413672), (-0.2374342421, -0.8301223987), (-0.1562636163, -0.862915376), (-0.0721529017, -0.8849777371), (-0.0016194662, -0.8901148115), (0.0534072054, -0.8852058817), (0.0910695699, -0.8778091166), (0.1101452363, -0.8730796223)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                Line((0.1101452363, -0.8730796223), (0.1101452363, -0.4653791533))
                Line((0.1101452363, -0.4653791533), (-0.5000000075, -0.4653791533))
                Line((-0.5000000075, -0.4653791533), (-0.5000000075, 0))
                Line((-0.5000000075, 0.4653791533), (-0.5000000075, 0))
                Line((0.1101452363, 0.4653791533), (-0.5000000075, 0.4653791533))
                Line((0.1101452363, 0.8730796223), (0.1101452363, 0.4653791533))
                _nurbs_edge([(-0.8, 0.6681377055), (-0.7751378016, 0.6681377055), (-0.7268403378, 0.6693818941), (-0.6586746967, 0.6749804854), (-0.5758732014, 0.6895785133), (-0.4832453316, 0.7177364958), (-0.3981952278, 0.7529937905), (-0.3172988646, 0.7918413672), (-0.2374342421, 0.8301223987), (-0.1562636163, 0.862915376), (-0.0721529017, 0.8849777371), (-0.0016194662, 0.8901148115), (0.0534072054, 0.8852058817), (0.0910695699, 0.8778091166), (0.1101452363, 0.8730796223)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
            make_face()
        # OneSide extrude, distance=0.8
        extrude(amount=0.8, mode=Mode.ADD)
    return part.part


def model_105267_6e427767_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.8352873699, perimeter: 5.9690260418
            Circle(0.95)
        # OneSide extrude, distance=0.25
        extrude(amount=0.25)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.25, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2970572204, perimeter: 1.932079482
            Circle(0.3075)
        # OneSide extrude, distance=0.25
        extrude(amount=0.25, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.2922466566, perimeter: 1.9163715187
            Circle(0.305)
        # OneSide extrude, distance=0.25
        extrude(amount=0.25, mode=Mode.ADD)
    return part.part


def model_105278_909f3813_0001():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 14.9225651046, perimeter: 59.6902604182
            with BuildLine():
                CenterArc((0, 0), 5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 4.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 6.8722339297, perimeter: 54.9778714378
            with BuildLine():
                CenterArc((0, 0), 4.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 4.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 56.7450173055, perimeter: 26.7035375555
            Circle(4.25)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            with Locations((1, -2)):
                Circle(1.5)
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            with Locations((1, 2)):
                Circle(1.5)
            # Profile area: 6.5199916285, perimeter: 14.1733305428
            with BuildLine():
                Line((-2.0466820144, 3), (-0.960016743, 3))
                Line((-2.0466820144, -3), (-2.0466820144, 3))
                Line((-0.960016743, -3), (-2.0466820144, -3))
                Line((-0.960016743, 3), (-0.960016743, -3))
            make_face()
        # OneSide extrude, distance=-1.3
        extrude(amount=-1.3, mode=Mode.SUBTRACT)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.8722339297, perimeter: 54.9778714378
            with BuildLine():
                CenterArc((0, 0), 4.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 4.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.7
        extrude(amount=1.7, mode=Mode.ADD)
    return part.part


def model_106235_14bd7a91_0000():
    """Model: plug-paper"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 18 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.418506193, perimeter: 4.5026548246
            with BuildLine():
                Line((-1.0500000209, 1.7200000149), (-1.0500000209, 1.0000000149))
                CenterArc((-1.1300000209, 1.7200000149), 0.08, 0, 90)
                Line((-1.1700000209, 1.8000000149), (-1.1300000209, 1.8000000149))
                CenterArc((-1.1700000209, 1.7200000149), 0.08, 90, 90)
                Line((-1.2500000209, 1.0000000149), (-1.2500000209, 1.7200000149))
                Line((-1.3700000209, 1.0000000149), (-1.2500000209, 1.0000000149))
                Line((-1.3700000209, 1.7200000149), (-1.3700000209, 1.0000000149))
                CenterArc((-1.4500000209, 1.7200000149), 0.08, 0, 90)
                Line((-1.4900000209, 1.8000000149), (-1.4500000209, 1.8000000149))
                CenterArc((-1.4900000209, 1.7200000149), 0.08, 90, 90)
                Line((-1.5700000209, 1.0000000149), (-1.5700000209, 1.7200000149))
                Line((-1.5700000209, 0.8000000149), (-1.5700000209, 1.0000000149))
                Line((-1.0500000209, 0.8000000149), (-1.5700000209, 0.8000000149))
                Line((-1.0500000209, 1.0000000149), (-1.0500000209, 0.8000000149))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.8000000149, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-1.3100000209, 0.5)):
                Circle(0.25)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (NewBody)
        # Sketch on BRepFace
        # Sketch has 12 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-1.2500000209, -0.0000001136, -0.0000002682), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 22.656284561, perimeter: 30.7547361282
            with BuildLine():
                Line((3.5385698144, 2.7263001621), (4, 1))
                Line((2.8006885991, 2.2729829161), (3.5385698144, 2.7263001621))
                Line((2.0800357695, 3.4460161294), (2.8006885991, 2.2729829161))
                Line((2.0800357695, 5.1031946944), (2.0800357695, 3.4460161294))
                Line((1.2641148138, 4.6019337421), (2.0800357695, 5.1031946944))
                Line((0.4506913085, 3.4460161294), (1.2641148138, 4.6019337421))
                Line((-0.4583584848, 4.0857178358), (0.4506913085, 3.4460161294))
                Line((-1.0926328589, 5.1181496485), (-0.4583584848, 4.0857178358))
                Line((-1.8191589493, 4.0857178358), (-1.0926328589, 5.1181496485))
                Line((-2.5178268162, 2.806314423), (-1.8191589493, 4.0857178358))
                Line((-3.3038281665, 4.0857178358), (-2.5178268162, 2.806314423))
                Line((-3.8569402279, 3.2997164855), (-3.3038281665, 4.0857178358))
                Line((-3.8569402279, 2.3129123605), (-3.8569402279, 3.2997164855))
                Line((-5.3707206063, 3), (-3.8569402279, 2.3129123605))
                Line((-5.3707206063, 1.6258247209), (-5.3707206063, 3))
                Line((-5, 1.0000001285), (-5.3707206063, 1.6258247209))
                Line((0.0000002682, 1.0000001285), (-5, 1.0000001285))
                Line((0.0000002682, 1.7200001285), (0.0000002682, 1.0000001285))
                Line((1.0000002682, 1.7200001285), (0.0000002682, 1.7200001285))
                Line((1.0000002682, 1.0000000964), (1.0000002682, 1.7200001285))
                Line((4, 1), (1.0000002682, 1.0000000964))
            make_face()
        # OneSide extrude, distance=0.01
        extrude(amount=0.01)
    return part.part


def model_106645_558b1d4b_0000():
    """Model: Ball screw"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.5420224797, perimeter: 13.9549545672
            with BuildLine():
                CenterArc((0, 0), 1.221, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # OneSide extrude, distance=182.7
        extrude(amount=182.7)

        # Sketch1 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.5420224797, perimeter: 13.9549545672
            with BuildLine():
                CenterArc((0, 0), 1.221, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=8.55
        extrude(amount=8.55, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 11 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 182.7, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0518704454, perimeter: 1.6413232747
            with BuildLine():
                Line((-0.4028675341, 0.802), (0.4028675341, 0.802))
                CenterArc((0, 0), 0.8975, 63.3283132883, 53.3433734234)
            make_face()
            # Profile area: 0.0518704454, perimeter: 1.6413232747
            with BuildLine():
                Line((-0.4028675341, -0.802), (0.4028675341, -0.802))
                CenterArc((0, 0), 0.8975, -116.6716867117, 53.3433734234)
            make_face()
            # Profile area: 2.1530426158, perimeter: 13.3109280733
            with BuildLine():
                CenterArc((0, 0), 1.221, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.8975, 116.6716867117, 126.6566265766)
                CenterArc((0, 0), 0.8975, 63.3283132883, 53.3433734234)
                CenterArc((0, 0), 0.8975, -63.3283132883, 126.6566265766)
                CenterArc((0, 0), 0.8975, -116.6716867117, 53.3433734234)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-2.325
        extrude(amount=-2.325, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 11 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 182.7, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.659685759, perimeter: 10.2918415167
            with BuildLine():
                CenterArc((0, 0), 0.8975, 116.6716867117, 126.6566265766)
                Line((-0.4028675341, -0.802), (0.4028675341, -0.802))
                CenterArc((0, 0), 0.8975, -63.3283132883, 126.6566265766)
                Line((-0.4028675341, 0.802), (0.4028675341, 0.802))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-1.378
        extrude(amount=-1.378, mode=Mode.SUBTRACT)
    return part.part


def model_107055_0500fdd1_0028():
    """Model: Threaded part (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2007477706, perimeter: 4.4610615681
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.31, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.8), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.8546980392, perimeter: 5.3686295707
            with BuildLine():
                Line((-0.55, 0.3175426481), (-0.55, -0.3175426481))
                Line((-0.55, -0.3175426481), (0, -0.6350852961))
                Line((0, -0.6350852961), (0.55, -0.3175426481))
                Line((0.55, -0.3175426481), (0.55, 0.3175426481))
                Line((0.55, 0.3175426481), (0, 0.6350852961))
                Line((0, 0.6350852961), (-0.55, 0.3175426481))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2479821488, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.376
        extrude(amount=0.376, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.176), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.3689293326, perimeter: 4.215905179
            with BuildLine():
                CenterArc((0, 0), 0.423, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2479821488, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.65
        extrude(amount=0.65, mode=Mode.ADD)
    return part.part


def model_107743_e0c2c81f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 15932871.3599999994, perimeter: 16642.08
            with BuildLine():
                Line((0, 2987.04), (0, 0))
                Line((0, 0), (5334, 0))
                Line((5334, 0), (5334, 2987.04))
                Line((5334, 2987.04), (0, 2987.04))
            make_face()
        # OneSide extrude, distance=182.88
        extrude(amount=182.88)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 182.88, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1583996.8320000002, perimeter: 5242.56
            with BuildLine():
                Line((-822.9600219727, -2499.3600219727), (-822.9600219727, -822.9600219727))
                Line((-822.9600219727, -822.9600219727), (-1767.8400219727, -822.9600219727))
                Line((-1767.8400219727, -822.9600219727), (-1767.8400219727, -2499.3600219727))
                Line((-1767.8400219727, -2499.3600219727), (-822.9600219727, -2499.3600219727))
            make_face()
        # OneSide extrude, distance=30.48
        extrude(amount=30.48, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 213.36, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1479119.5707872005, perimeter: 5079.99991872
            with BuildLine():
                Line((-843.2800321327, -843.2800321327), (-1747.5200118127, -843.2800321327))
                Line((-1747.5200118127, -843.2800321327), (-1747.5200118127, -2479.0400118127))
                Line((-1747.5200118127, -2479.0400118127), (-843.2800321327, -2479.0400118127))
                Line((-843.2800321327, -2479.0400118127), (-843.2800321327, -843.2800321327))
            make_face()
        # OneSide extrude, distance=-91.44
        extrude(amount=-91.44, mode=Mode.SUBTRACT)
    return part.part


def model_107918_8e0402a9_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 18.36, perimeter: 17.4
            with BuildLine():
                Line((2.55, -1.8), (-2.55, -1.8))
                Line((2.55, 1.8), (2.55, -1.8))
                Line((-2.55, 1.8), (2.55, 1.8))
                Line((-2.55, -1.8), (-2.55, 1.8))
            make_face()
        # OneSide extrude, distance=0.32
        extrude(amount=0.32)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.32, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.1584, perimeter: 32.24
            with BuildLine():
                Line((2.55, -1.8), (2.55, 1.8))
                Line((2.55, 1.8), (-2.55, 1.8))
                Line((-2.55, 1.8), (-2.55, -1.8))
                Line((-2.55, -1.8), (2.55, -1.8))
            make_face()
            with BuildLine():
                Line((-2.23, -1.48), (2.23, -1.48))
                Line((-2.23, 1.48), (-2.23, -1.48))
                Line((2.23, 1.48), (-2.23, 1.48))
                Line((2.23, -1.48), (2.23, 1.48))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.85
        extrude(amount=0.85, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 28 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.17, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.26, perimeter: 3
            with BuildLine():
                Line((2.23, 0.65), (2.23, -0.65))
                Line((2.03, 0.65), (2.23, 0.65))
                Line((2.03, -0.65), (2.03, 0.65))
                Line((2.23, -0.65), (2.03, -0.65))
            make_face()
            # Profile area: 0.34, perimeter: 3.8
            with BuildLine():
                Line((-0.85, 1.48), (0.85, 1.48))
                Line((-0.85, 1.28), (-0.85, 1.48))
                Line((0.85, 1.28), (-0.85, 1.28))
                Line((0.85, 1.48), (0.85, 1.28))
            make_face()
            # Profile area: 0.34, perimeter: 3.8
            with BuildLine():
                Line((0.85, -1.48), (-0.85, -1.48))
                Line((0.85, -1.28), (0.85, -1.48))
                Line((-0.85, -1.28), (0.85, -1.28))
                Line((-0.85, -1.48), (-0.85, -1.28))
            make_face()
            # Profile area: 0.26, perimeter: 3
            with BuildLine():
                Line((-2.23, -0.65), (-2.23, 0.65))
                Line((-2.03, -0.65), (-2.23, -0.65))
                Line((-2.03, 0.65), (-2.03, -0.65))
                Line((-2.23, 0.65), (-2.03, 0.65))
            make_face()
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4, mode=Mode.ADD)
    return part.part


def model_108008_db1cf496_0001():
    """Model: fastnr"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=-5
        extrude(amount=-5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2473708571, perimeter: 2.4418521834
            with BuildLine():
                Line((0.125, 0.4841229183), (0.125, -0.4841229183))
                CenterArc((0, 0), 0.5, 75.5224878141, 28.9550243719)
                Line((-0.125, -0.4841229183), (-0.125, 0.4841229183))
                CenterArc((0, 0), 0.5, -104.4775121859, 28.9550243719)
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)
    return part.part


def model_109543_c2418151_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 20.0215108123, perimeter: 15.8618323383
            Circle(2.5244890231)
        # OneSide extrude, distance=10
        extrude(amount=10)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 10, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 16.9210965639, perimeter: 14.5820701762
            Circle(2.3208085491)
        # OneSide extrude, distance=-9.8
        extrude(amount=-9.8, mode=Mode.SUBTRACT)
    return part.part


def model_110518_142d2e0a_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0762499985, perimeter: 1.2139756748
            with BuildLine():
                Line((0.4, 0.1), (0.4, 0))
                Line((0.1, 0.2349999942), (0.4, 0.1))
                Line((0.1, 0.2599999942), (0.1, 0.2349999942))
                Line((0, 0.2599999942), (0.1, 0.2599999942))
                Line((0, 0), (0, 0.2599999942))
                Line((0.4, 0), (0, 0))
            make_face()
        # Symmetric extrude, full_length=True, total=0.25
        extrude(amount=0.125, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.2599999942, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.002480633, perimeter: 0.1765575071
            with Locations((-0.05, 0)):
                Circle(0.0281)
        # OneSide extrude, distance=-0.15
        extrude(amount=-0.15, mode=Mode.SUBTRACT)
    return part.part


def model_110779_4f244e41_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 16.9022736072, perimeter: 16.9346377097
            with BuildLine():
                Line((-5.2444010068, 0), (-5.2444010068, 3.2229178481))
                Line((0, 0), (-5.2444010068, 0))
                Line((0, 3.2229178481), (0, 0))
                Line((-5.2444010068, 3.2229178481), (0, 3.2229178481))
            make_face()
            # Profile area: 8.2078206813, perimeter: 13.4463956793
            with BuildLine():
                CenterArc((-4.965133804, 3.2229178481), 0.2792672028, 97.1720285643, 82.8279714357)
                Line((-5.2444010068, 3.2229178481), (0, 3.2229178481))
                Line((-2.6222005034, 6.3536602777), (0, 3.2229178481))
                Line((-5, 3.5), (-2.6222005034, 6.3536602777))
            make_face()
        # Symmetric extrude, each_side=4
        extrude(amount=4, both=True)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(4, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.3716196052, perimeter: 4.6850219483
            with BuildLine():
                Line((-2.031990551, 3.8600779748), (-3.2180720569, 3.8600779748))
                Line((-2.031990551, 5.0165074431), (-2.031990551, 3.8600779748))
                Line((-3.2180720569, 5.0165074431), (-2.031990551, 5.0165074431))
                Line((-3.2180720569, 3.8600779748), (-3.2180720569, 5.0165074431))
            make_face()
            # Profile area: 6, perimeter: 10
            with BuildLine():
                Line((-1.5, 0), (-3.5, 0))
                Line((-1.5, 3), (-1.5, 0))
                Line((-3.5, 3), (-1.5, 3))
                Line((-3.5, 0), (-3.5, 3))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)
    return part.part


def model_110875_e9e6c22e_0003():
    """Model: Untitled v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 46.1529902571, perimeter: 30.5918461155
            with BuildLine():
                CenterArc((2.5, 2), 2.5, 90, 180)
                Line((2.5, -0.5), (12.0005036235, 1.3819661247))
                CenterArc((12, 2.5), 1.1180339887, -89.9741908523, 179.9483817047)
                Line((2.5, 4.5), (12.0005036235, 3.6180338753))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with Locations((3.4148650177, 2.2497963457)):
                Circle(0.75)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((12, 2.5)):
                Circle(0.5)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


def model_111228_fcc98116_0000():
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
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 5.2492097521, perimeter: 17.0078339651
            with BuildLine():
                Line((0, 8.0256956507), (0, 0))
                Line((0, 0), (0.6, 0))
                _nurbs_edge([(0.3, 8.0256956507), (0.3386005692, 7.7116697729), (0.4127281504, 7.0941969805), (0.5146992062, 6.1997234598), (0.6319136308, 5.0716178719), (0.7444170689, 3.7785616789), (0.8179344778, 2.6196926062), (0.845455418, 1.6191400844), (0.8199238696, 0.851890868), (0.75583515, 0.3985181569), (0.6828001062, 0.1571035361), (0.6257835639, 0.0417198637), (0.6, 0)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.7720142942, 0.7720142942, 0.7720142942, 0.7720142942, 0.7720142942, 0.7720142942], 5)
                Line((0, 8.0256956507), (0.3, 8.0256956507))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 8.0256956507, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0441094342, perimeter: 0.74451024
            with Locations((-0.1343787729, 0.5)):
                Circle(0.1184924849)
        # OneSide extrude, distance=2.5
        extrude(amount=2.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            with Locations((3.2892866364, -2.7052233333)):
                Circle(0.125)
        # OneSide extrude, distance=4
        extrude(amount=4)
    return part.part


def model_111257_05ceda77_0002():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 109677.2000000001, perimeter: 8636
            with BuildLine():
                Line((-25.4, -25.4), (-25.4, 251.46))
                Line((-25.4, -25.4), (668.02, -25.4))
                Line((668.02, -25.4), (668.02, 673.1))
                Line((668.02, 673.1), (238.76, 673.1))
                Line((238.76, 673.1), (-17.78, 673.1))
                Line((-17.78, 673.1), (-17.78, 1094.74))
                Line((-17.78, 1094.74), (-421.64, 1094.74))
                Line((-421.64, 1094.74), (-421.64, 251.46))
                Line((-25.4, 251.46), (-421.64, 251.46))
            make_face()
            with BuildLine():
                Line((0, 0), (0, 276.86))
                Line((0, 276.86), (-396.24, 276.86))
                Line((-396.24, 1069.34), (-396.24, 276.86))
                Line((-43.18, 1069.34), (-396.24, 1069.34))
                Line((-43.18, 647.7), (-43.18, 1069.34))
                Line((238.76, 647.7), (-43.18, 647.7))
                Line((642.62, 647.7), (238.76, 647.7))
                Line((642.62, 0), (642.62, 647.7))
                Line((0, 0), (642.62, 0))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=353.06
        extrude(amount=353.06)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 16526.8891522133, perimeter: 535.5179634224
            with BuildLine():
                Line((238.76, -647.7), (238.76, -551.18))
                Line((238.76, -551.18), (68.58, -551.18))
                Line((68.58, -551.18), (66.4847751303, -647.7))
                Line((238.76, -647.7), (66.4847751303, -647.7))
            make_face()
        # OneSide extrude, distance=-60.96
        extrude(amount=-60.96, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -551.18), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1858.0608, perimeter: 203.2
            with BuildLine():
                Line((238.76, 60.96), (177.8, 60.96))
                Line((177.8, 60.96), (177.8, 40.64))
                Line((177.8, 40.64), (208.28, 40.64))
                Line((208.28, 40.64), (208.28, 20.32))
                Line((208.28, 20.32), (238.76, 20.32))
                Line((238.76, 20.32), (238.76, 60.96))
            make_face()
        # OneSide extrude, distance=-96.52
        extrude(amount=-96.52, mode=Mode.SUBTRACT)
    return part.part


def model_112009_7c523f63_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # base -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 9, perimeter: 17.4
            with BuildLine():
                Line((0, 1.2), (0, 0))
                Line((0, 0), (7.5, 0))
                Line((7.5, 0), (7.5, 1.2))
                Line((7.5, 1.2), (0, 1.2))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # holes -> Extrude2 (Cut)
        # Sketch on XY construction plane
        # Sketch has 8 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.331830724, perimeter: 2.0420352248
            with Locations((6.85, 0.6)):
                Circle(0.325)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((1.55, 0.6456764419)):
                Circle(0.3)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((0.6, 0.65)):
                Circle(0.3)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.SUBTRACT)

        # truck groove cutout -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.2), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 3.5275, perimeter: 10.159366606
            with BuildLine():
                Line((-2, -1.2), (-2.2, -0.35))
                Line((-2.2, -0.35), (-6, -0.35))
                Line((-6, -0.35), (-6.5, -1.2))
                Line((-2, -1.2), (-6.5, -1.2))
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)
    return part.part


def model_112633_1a74caa7_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 28.2743338823, perimeter: 18.8495559215
            with Locations((5, -5)):
                Circle(3)
        # OneSide extrude, distance=8
        extrude(amount=8)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            with Locations((-5, 5)):
                Circle(2)
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 11, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-5.9597514939, 4.25)):
                Circle(0.5)
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-4.0406248053, 4.25)):
                Circle(0.5)
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-4.0406248053, 5.75)):
                Circle(0.5)
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-5.9597514939, 5.75)):
                Circle(0.5)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


def model_113190_188366f8_0001():
    """Model: Flange"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 41.1057763768, perimeter: 42.5685804561
            with BuildLine():
                CenterArc((0, 0), 4.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.075, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 3), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 7.6340701482, perimeter: 50.8938009882
            with BuildLine():
                CenterArc((0, 0), 4.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3.9, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.15
        extrude(amount=1.15, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.45), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 36.1911473694, perimeter: 60.3185789489
            with BuildLine():
                CenterArc((0, 0), 5.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 4.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.ADD)
    return part.part


def model_113191_87565693_0002():
    """Model: Nut"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.4322831491, perimeter: 10.8070787283
            with BuildLine():
                CenterArc((0, 0), 0.9, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.82, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1)

        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.9189158512, perimeter: 12.252211349
            with BuildLine():
                CenterArc((0, 0), 1.05, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.9, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.9189158512, perimeter: 12.252211349
            with BuildLine():
                CenterArc((0, 0), 1.05, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.9, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.85
        extrude(amount=-0.85, mode=Mode.ADD)

        # Sketch2 -> Extrude4 (NewBody)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.3), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0009272062, perimeter: 0.1241764932
            with BuildLine():
                CenterArc((0, 0), 1.05, -92, 2)
                Line((-0.0366444715, -1.0493603684), (-0.037516959, -1.074345139))
                CenterArc((0, 0), 1.075, -92, 2)
                Line((0, -1.05), (0, -1.075))
            make_face()
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4)
    return part.part


def model_113341_3d297c22_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            Circle(2.5)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch9 -> Extrude6 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((7.3322602683, 4.3245371786)):
                Circle(0.5)
        # OneSide extrude, distance=13
        extrude(amount=13)
    return part.part


def model_113364_10837c89_0002():
    """Model: ashilok3 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 9 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with BuildLine():
                CenterArc((15, 0), 0.75, 90, 180)
                CenterArc((15, 0), 0.75, -90, 180)
            make_face()
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with BuildLine():
                CenterArc((0, 0), 0.75, -90, 180)
                CenterArc((0, 0), 0.75, 90, 180)
            make_face()
            # Profile area: 20.7328541324, perimeter: 34.7123889804
            with BuildLine():
                Line((15, 0.75), (0, 0.75))
                CenterArc((0, 0), 0.75, -90, 180)
                Line((0, -0.75), (15, -0.75))
                CenterArc((15, 0), 0.75, 90, 180)
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((15, 0)):
                Circle(0.25)
        # OneSide extrude, distance=-6
        extrude(amount=-6, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 10 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 17.7359658627, perimeter: 31.5977287238
            with BuildLine():
                Line((14.6199168799, -0.6465576709), (0.3800831201, -0.6465576709))
                CenterArc((15, 0), 0.75, 120.4494175816, 119.1011648368)
                Line((0.3800831201, 0.6465576709), (14.6199168799, 0.6465576709))
                CenterArc((0, 0), 0.75, -59.5505824184, 119.1011648368)
            make_face()
        # OneSide extrude, distance=-6
        extrude(amount=-6, mode=Mode.SUBTRACT)
    return part.part


def model_113856_e7484fa7_0000():
    """Model: lampfitting v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            Circle(2)
        # OneSide extrude, distance=4.422
        extrude(amount=4.422)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 16.6190251375, perimeter: 14.4513262065
            Circle(2.3)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.ADD)
    return part.part


def model_114187_69d0ae36_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 17 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 15.6780972451, perimeter: 32.7123889804
            with BuildLine():
                Line((3.5, -1.5), (5.5, -1.5))
                Line((5.5, -1.5), (5.5, -0.5))
                Line((5.5, -0.5), (3.5, -0.5))
                Line((3.5, 1.5), (3.5, -0.5))
                CenterArc((2.5, 1.5), 1, 0, 90)
                Line((-1.5, 2.5), (2.5, 2.5))
                CenterArc((-1.5, 1.5), 1, 90, 90)
                Line((-2.5, -0.5), (-2.5, 1.5))
                Line((-4.5, -0.5), (-2.5, -0.5))
                Line((-4.5, -1.5), (-4.5, -0.5))
                Line((-2.5, -1.5), (-4.5, -1.5))
                Line((-1.5, -1.5), (-2.5, -1.5))
                Line((-1.5, -1.5), (-1.5, 1))
                CenterArc((-1, 1), 0.5, 90, 90)
                Line((-1, 1.5), (2, 1.5))
                CenterArc((2, 1), 0.5, 0, 90)
                Line((2.5, 1), (2.5, -1.5))
                Line((3.5, -1.5), (2.5, -1.5))
            make_face()
        # OneSide extrude, distance=7.5
        extrude(amount=7.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((-3.75, -0.5)):
                Circle(1)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


def model_115179_e3a49444_0001():
    """Model: Support Elise v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.8659014751, perimeter: 3.2986722863
            Circle(0.525)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.3117245311, perimeter: 1.9792033718
            Circle(0.315)
        # OneSide extrude, distance=2.65
        extrude(amount=2.65, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3.65), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            Circle(0.125)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


def model_115406_290de6d9_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 12 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.9030279376, perimeter: 8.8121676709
            with BuildLine():
                Line((0, -0.0000000119), (0, -1.1750000119))
                CenterArc((0, -1.4000000119), 0.225, -90, 180)
                Line((0, -1.6250000119), (0, -2))
                CenterArc((0, 0), 2, -90, 89.9999996585)
                Line((0, -0.0000000119), (2, -0.0000000119))
            make_face()
            with BuildLine():
                CenterArc((1, -0.7000000119), 0.225, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 2.9030279853, perimeter: 8.8121677067
            with BuildLine():
                CenterArc((0, 1.3999999881), 0.225, -90, 180)
                Line((0, 1.1749999881), (0, -0.0000000119))
                Line((0, -0.0000000119), (2, -0.0000000119))
                CenterArc((0, 0), 2, 0, 90)
                Line((0, 2), (0, 1.6249999881))
            make_face()
            with BuildLine():
                CenterArc((1, 0.6999999881), 0.225, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 2.9030279376, perimeter: 8.8121676709
            with BuildLine():
                CenterArc((0, 0), 2, -179.9999996585, 89.9999996585)
                Line((0, -1.6250000119), (0, -2))
                CenterArc((0, -1.4000000119), 0.225, 90, 180)
                Line((0, -0.0000000119), (0, -1.1750000119))
                Line((-2, -0.0000000119), (0, -0.0000000119))
            make_face()
            with BuildLine():
                CenterArc((-1, -0.7000000119), 0.225, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 2.9030279853, perimeter: 8.8121677067
            with BuildLine():
                CenterArc((0, 1.3999999881), 0.225, 90, 180)
                Line((0, 2), (0, 1.6249999881))
                CenterArc((0, 0), 2, 90, 90)
                Line((-2, -0.0000000119), (0, -0.0000000119))
                Line((0, 1.1749999881), (0, -0.0000000119))
            make_face()
            with BuildLine():
                CenterArc((-1, 0.6999999881), 0.225, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 11 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.4, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1237002107, perimeter: 3.2986722863
            with BuildLine():
                CenterArc((0, 1.3999999881), 0.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 1.3999999881), 0.225, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1237002107, perimeter: 3.2986722863
            with BuildLine():
                CenterArc((1, 0.6999999881), 0.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((1, 0.6999999881), 0.225, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1237002107, perimeter: 3.2986722863
            with BuildLine():
                CenterArc((1, -0.7000000119), 0.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((1, -0.7000000119), 0.225, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1237002107, perimeter: 3.2986722863
            with BuildLine():
                CenterArc((0, -1.4000000119), 0.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, -1.4000000119), 0.225, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1237002107, perimeter: 3.2986722863
            with BuildLine():
                CenterArc((-1, -0.7000000119), 0.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-1, -0.7000000119), 0.225, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1237002107, perimeter: 3.2986722863
            with BuildLine():
                CenterArc((-1, 0.6999999881), 0.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-1, 0.6999999881), 0.225, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.4, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0402123822, perimeter: 0.8226548007
            with BuildLine():
                CenterArc((0, 0), 0.16, -179.9999957311, 179.9999914623)
                Line((-0.16, -0.0000000119), (0.16, -0.0000000119))
            make_face()
            # Profile area: 0.0402123898, perimeter: 0.8226548365
            with BuildLine():
                Line((-0.16, -0.0000000119), (0.16, -0.0000000119))
                CenterArc((0, 0), 0.16, -0.0000042689, 180.0000042689)
            make_face()
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4, mode=Mode.SUBTRACT)
    return part.part


def model_115406_9f5685a8_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 12.4859458424, perimeter: 13.5716802635
            with BuildLine():
                CenterArc((0, 0), 2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.16, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.3, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.7049733915, perimeter: 4.1469023027
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.16, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.1159247689, perimeter: 2.5761059759
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.16, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.25
        extrude(amount=-0.25, mode=Mode.SUBTRACT)
    return part.part


def model_115406_ffbeceb3_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 15 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.567999983, perimeter: 20
            with BuildLine():
                Line((-0.7999999985, 2.9000000075), (-0.7999999985, 0.3800000075))
                Line((-0.7999999985, 0.3800000075), (2.1000000015, 0.3800000075))
                Line((2.1000000015, 0.3800000075), (2.1000000015, 2.9000000075))
                Line((2.1000000015, 2.9000000075), (-0.7999999985, 2.9000000075))
            make_face()
            with BuildLine():
                Line((0.1000000015, 2.4000000358), (-0.4999999985, 2.4000000358))
                Line((0.1000000015, 2.7000000075), (0.1000000015, 2.4000000358))
                Line((1.2000000015, 2.7000000075), (0.1000000015, 2.7000000075))
                Line((1.2000000015, 2.4000000075), (1.2000000015, 2.7000000075))
                Line((1.8000000015, 2.4000000075), (1.2000000015, 2.4000000075))
                Line((1.8000000015, 0.5000000075), (1.8000000015, 2.4000000075))
                Line((0.9000000015, 0.5000000075), (1.8000000015, 0.5000000075))
                Line((0.9000000015, 0.4200000075), (0.9000000015, 0.5000000075))
                Line((0.4000000015, 0.4200000075), (0.9000000015, 0.4200000075))
                Line((0.4000000015, 0.5000000075), (0.4000000015, 0.4200000075))
                Line((-0.4999999985, 0.5000000075), (0.4000000015, 0.5000000075))
                Line((-0.4999999985, 2.4000000358), (-0.4999999985, 0.5000000075))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.3800000075), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((0.6500000015, 3)):
                Circle(0.25)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.3800000075), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.38, perimeter: 5.8
            with BuildLine():
                Line((0.9500000015, 0), (0.9500000015, 2.3))
                Line((0.9500000015, 2.3), (0.3500000015, 2.3))
                Line((0.3500000015, 2.3), (0.3500000015, 0))
                Line((0.3500000015, 0), (0.9500000015, 0))
            make_face()
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((1.5250000015, 4)):
                Circle(0.15)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-0.2249999985, 4)):
                Circle(0.15)
        # OneSide extrude, distance=-2.6
        extrude(amount=-2.6, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(2.1000000015, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            with Locations((1.4500000216, 4)):
                Circle(0.35)
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            with Locations((1.4500000216, 1)):
                Circle(0.35)
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)
    return part.part


def model_115524_f214596c_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch4 -> Extrude4 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 80, perimeter: 36
            with BuildLine():
                Line((5, 0), (13, 0))
                Line((5, -10), (5, 0))
                Line((13, -10), (5, -10))
                Line((13, 0), (13, -10))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5)
    return part.part


def model_116179_7583706e_0001():
    """Model: POST, HANDLE"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 4.3272124828, perimeter: 15.3407075494
            with BuildLine():
                CenterArc((0, 1.7), 0.5000000075, 180, 180)
                Line((0.5000000075, 1.7), (0.5000000075, 6.2))
                Line((-0.5000000075, 6.2), (0.5000000075, 6.2))
                Line((-0.5000000075, 1.7), (-0.5000000075, 6.2))
            make_face()
            with BuildLine():
                CenterArc((0, 3.7), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 1.7), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=0.5
        extrude(amount=0.25, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 6.2), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 2.6415926461, perimeter: 9.283185337
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face()
            with BuildLine():
                Line((-0.25, -0.5000000075), (0.25, -0.5000000075))
                Line((-0.25, 0.5000000075), (-0.25, -0.5000000075))
                Line((0.25, 0.5000000075), (-0.25, 0.5000000075))
                Line((0.25, -0.5000000075), (0.25, 0.5000000075))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.5000000075, perimeter: 3.0000000298
            with BuildLine():
                Line((0.25, -0.5000000075), (0.25, 0.5000000075))
                Line((0.25, 0.5000000075), (-0.25, 0.5000000075))
                Line((-0.25, 0.5000000075), (-0.25, -0.5000000075))
                Line((-0.25, -0.5000000075), (0.25, -0.5000000075))
            make_face()
        # OneSide extrude, distance=8
        extrude(amount=8, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 14.2), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            Circle(0.6)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


def model_116247_2d150add_0003():
    """Model: holder v1 v2"""
    with BuildPart() as part:
        # Sketch5 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 17, perimeter: 36
            with BuildLine():
                Line((-1, 7), (2, 7))
                Line((-1, -6), (-1, 7))
                Line((-2, -6), (-1, -6))
                Line((-2, -7), (-2, -6))
                Line((0, -7), (-2, -7))
                Line((0, 6), (0, -7))
                Line((2, 6), (0, 6))
                Line((2, 7), (2, 6))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_116248_9325a5f7_0001():
    """Model: base1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 45, perimeter: 28
            with BuildLine():
                Line((-4.5, 2.5), (4.5, 2.5))
                Line((-4.5, -2.5), (-4.5, 2.5))
                Line((4.5, -2.5), (-4.5, -2.5))
                Line((4.5, 2.5), (4.5, -2.5))
            make_face()
        # Symmetric extrude, full_length=True, total=0.5
        extrude(amount=0.25, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-4.5, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 2.7853981634, perimeter: 10.2831853072
            with BuildLine():
                Line((1, 0.25), (-1, 0.25))
                Line((1, 1.25), (1, 0.25))
                CenterArc((0, 1.25), 1, 0, 180)
                Line((-1, 0.25), (-1, 1.25))
            make_face()
            with BuildLine():
                CenterArc((0, 1.25), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-2.5
        extrude(amount=-2.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.91242255, perimeter: 5.1703537555
            with BuildLine():
                Line((3.6, 1.0499988683), (3.6, 0.25))
                Line((3.6, 0.25), (4.5, 0.25))
                Line((4.5, 0.25), (4.5, 1.05))
                CenterArc((4.05, 1.05), 0.45, 0, 180.0001440899)
            make_face()
            with BuildLine():
                CenterArc((4.05, 1.05), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=0.4
        extrude(amount=0.2, both=True, mode=Mode.ADD)
    return part.part


def model_116267_5a83e78a_0000():
    """Model: microloadcell_UbiLab v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.6129, perimeter: 5.08
            with BuildLine():
                Line((0, 0), (-1.27, 0))
                Line((0, 1.27), (0, 0))
                Line((-1.27, 1.27), (0, 1.27))
                Line((-1.27, 0), (-1.27, 1.27))
            make_face()
        # OneSide extrude, distance=5.525
        extrude(amount=5.525)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XY construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.3383802659, perimeter: 2.3257083903
            with BuildLine():
                Line((3.65931925, 0.635), (2.8885495579, 0.635))
                CenterArc((2.3885091515, 0.635), 0.5000404064, -38.5676951151, 38.5676951151)
                CenterArc((3.1641695528, 0.635), 0.4951496973, -140.9796254576, 140.9796254576)
            make_face()
            # Profile area: 0.3383802659, perimeter: 2.3257083903
            with BuildLine():
                CenterArc((2.3885091515, 0.635), 0.5000404064, 0, 38.5676951151)
                Line((3.65931925, 0.635), (2.8885495579, 0.635))
                CenterArc((3.1641695528, 0.635), 0.4951496973, 0, 140.9796254576)
            make_face()
            # Profile area: 0.0934738634, perimeter: 1.3476152313
            with BuildLine():
                CenterArc((3.1641695528, 0.635), 0.4951496973, 140.9796254576, 78.0407490847)
                CenterArc((2.3885091515, 0.635), 0.5000404064, -38.5676951151, 38.5676951151)
                CenterArc((2.3885091515, 0.635), 0.5000404064, 0, 38.5676951151)
            make_face()
            # Profile area: 0.6920512454, perimeter: 3.1430864407
            with BuildLine():
                CenterArc((2.3885091515, 0.635), 0.5000404064, 38.5676951151, 282.8646097697)
                CenterArc((3.1641695528, 0.635), 0.4951496973, 140.9796254576, 78.0407490847)
            make_face()
        # OneSide extrude, distance=2.5
        extrude(amount=2.5, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.27, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-0.7794767982, 0.635)):
                Circle(0.25)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-4.7794767982, 0.635)):
                Circle(0.25)
        # OneSide extrude, distance=-2.2
        extrude(amount=-2.2, mode=Mode.SUBTRACT)
    return part.part


def model_118113_98db6047_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 27, perimeter: 21
            with BuildLine():
                Line((3, -2.25), (3, 2.25))
                Line((3, 2.25), (-3, 2.25))
                Line((-3, 2.25), (-3, -2.25))
                Line((-3, -2.25), (3, -2.25))
            make_face()
        # OneSide extrude, distance=8.5
        extrude(amount=8.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(3, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.1500000469, perimeter: 7.2000000447
            with BuildLine():
                Line((1.05, 0), (-1.05, 0))
                Line((1.05, 1.5000000224), (1.05, 0))
                Line((-1.05, 1.5000000224), (1.05, 1.5000000224))
                Line((-1.05, 0), (-1.05, 1.5000000224))
            make_face()
        # OneSide extrude, distance=-9
        extrude(amount=-9, mode=Mode.SUBTRACT)
    return part.part


def model_118116_bcc4d1ef_0002():
    """Model: base"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 45, perimeter: 28
            with BuildLine():
                Line((-4.5, 2.5), (4.5, 2.5))
                Line((-4.5, -2.5), (-4.5, 2.5))
                Line((4.5, -2.5), (-4.5, -2.5))
                Line((4.5, 2.5), (4.5, -2.5))
            make_face()
        # Symmetric extrude, full_length=True, total=0.5
        extrude(amount=0.25, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-4.5, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 3.0853982051, perimeter: 10.5831853489
            with BuildLine():
                Line((1.0058699875, 0.25), (-0.9941300125, 0.25))
                Line((1.0058699875, 1.4000000209), (1.0058699875, 0.25))
                CenterArc((0.0058699875, 1.4000000209), 1, 0, 180)
                Line((-0.9941300125, 1.1000000164), (-0.9941300125, 1.4000000209))
                Line((-0.9941300125, 0.25), (-0.9941300125, 1.1000000164))
            make_face()
            with BuildLine():
                CenterArc((0, 1.25), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-2.5
        extrude(amount=-2.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.91242255, perimeter: 5.1703537556
            with BuildLine():
                Line((4.5, 0.25), (4.5, 1.05))
                CenterArc((4.05, 1.05), 0.45, 0, 180)
                Line((3.6, 1.05), (3.6, 0.25))
                Line((4.5, 0.25), (3.6, 0.25))
            make_face()
            with BuildLine():
                CenterArc((4.05, 1.05), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=0.4
        extrude(amount=0.2, both=True, mode=Mode.ADD)
    return part.part


def model_118433_f14b7df9_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 96.7739970932, perimeter: 40.6399993896
            with BuildLine():
                Line((-6.3499999046, 3.8099999428), (6.3499999046, 3.8099999428))
                Line((-6.3499999046, -3.8099999428), (-6.3499999046, 3.8099999428))
                Line((6.3499999046, -3.8099999428), (-6.3499999046, -3.8099999428))
                Line((6.3499999046, 3.8099999428), (6.3499999046, -3.8099999428))
            make_face()
        # OneSide extrude, distance=3.81
        extrude(amount=3.81)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 11.741912, perimeter: 19.3548
            with BuildLine():
                Line((-4.1275, 1.4224), (4.1275, 1.4224))
                Line((-4.1275, 0), (-4.1275, 1.4224))
                Line((4.1275, 0), (-4.1275, 0))
                Line((4.1275, 1.4224), (4.1275, 0))
            make_face()
        # Symmetric extrude, full_length=True, total=7.62
        extrude(amount=3.81, both=True, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 18.467705, perimeter: 17.9832
            with BuildLine():
                Line((-1.5875, 3.81), (1.5875, 3.81))
                Line((1.5875, 9.6266), (1.5875, 3.81))
                Line((-1.5875, 9.6266), (1.5875, 9.6266))
                Line((-1.5875, 3.81), (-1.5875, 9.6266))
            make_face()
        # Symmetric extrude, full_length=True, total=7.62
        extrude(amount=3.81, both=True, mode=Mode.ADD)
    return part.part


def model_118436_06c78560_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 632.2568, perimeter: 106.68
            with BuildLine():
                Line((17.78, -8.89), (17.78, 8.89))
                Line((17.78, 8.89), (-17.78, 8.89))
                Line((-17.78, 8.89), (-17.78, -8.89))
                Line((-17.78, -8.89), (17.78, -8.89))
            make_face()
        # OneSide extrude, distance=17.78
        extrude(amount=17.78)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 17.78, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 180.6448, perimeter: 81.28
            with BuildLine():
                Line((-17.78, -8.89), (17.78, -8.89))
                Line((17.78, -8.89), (17.78, -3.81))
                Line((17.78, -3.81), (-17.78, -3.81))
                Line((-17.78, -3.81), (-17.78, -8.89))
            make_face()
        # OneSide extrude, distance=-7.62
        extrude(amount=-7.62, mode=Mode.SUBTRACT)
    return part.part


def model_118544_ce1870aa_0001():
    """Model: AC Receptical + Switch v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 55 constraints, 14 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.4016091606, perimeter: 38.254986952
            with BuildLine():
                CenterArc((-1.21, -2.51), 0.39, -161.7669600806, 71.7669600806)
                Line((1.21, -2.9), (-1.21, -2.9))
                CenterArc((1.21, -2.51), 0.39, -90, 71.7669600806)
                Line((2.4036615082, -0.132975136), (1.5804187958, -2.6320242425))
                CenterArc((2, 0), 0.425, 18.2330399194, 323.5339201611)
                Line((2.4036615082, 0.132975136), (1.5804187958, 2.6320242425))
                CenterArc((1.21, 2.51), 0.39, 18.2330399194, 71.7669600806)
                Line((-1.21, 2.9), (1.21, 2.9))
                CenterArc((-1.21, 2.51), 0.39, 90, 71.7669600806)
                Line((-2.4036615082, 0.132975136), (-1.5804187958, 2.6320242425))
                CenterArc((-2, 0), 0.425, -161.7669600806, 323.5339201611)
                Line((-2.4036615082, -0.132975136), (-1.5804187958, -2.6320242425))
            make_face()
            with BuildLine():
                Line((1.21, 2.71), (-1.21, 2.71))
                CenterArc((1.21, 2.51), 0.2, 0, 90)
                Line((1.41, -2.51), (1.41, 2.51))
                CenterArc((1.21, -2.51), 0.2, -90, 90)
                Line((-1.21, -2.71), (1.21, -2.71))
                CenterArc((-1.21, -2.51), 0.2, -180, 90)
                Line((-1.41, 2.51), (-1.41, -2.51))
                CenterArc((-1.21, 2.51), 0.2, 90, 90)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.408407045, perimeter: 4.0840704497
            with BuildLine():
                CenterArc((-2, 0), 0.425, -161.7669600806, 323.5339201611)
                CenterArc((-2, 0), 0.425, 161.7669600806, 36.4660798389)
            make_face()
            with BuildLine():
                CenterArc((-2, 0), 0.225, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.408407045, perimeter: 4.0840704497
            with BuildLine():
                CenterArc((2, 0), 0.425, 18.2330399194, 323.5339201611)
                CenterArc((2, 0), 0.425, -18.2330399194, 36.4660798389)
            make_face()
            with BuildLine():
                CenterArc((2, 0), 0.225, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 15.2500637061, perimeter: 16.1366370614
            with BuildLine():
                CenterArc((-1.21, 2.51), 0.2, 90, 90)
                Line((-1.41, 2.51), (-1.41, -2.51))
                CenterArc((-1.21, -2.51), 0.2, -180, 90)
                Line((-1.21, -2.71), (1.21, -2.71))
                CenterArc((1.21, -2.51), 0.2, -90, 90)
                Line((1.41, -2.51), (1.41, 2.51))
                CenterArc((1.21, 2.51), 0.2, 0, 90)
                Line((1.21, 2.71), (-1.21, 2.71))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 55 constraints, 14 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 15.2500637061, perimeter: 16.1366370614
            with BuildLine():
                CenterArc((-1.21, 2.51), 0.2, 90, 90)
                Line((-1.41, 2.51), (-1.41, -2.51))
                CenterArc((-1.21, -2.51), 0.2, -180, 90)
                Line((-1.21, -2.71), (1.21, -2.71))
                CenterArc((1.21, -2.51), 0.2, -90, 90)
                Line((1.41, -2.51), (1.41, 2.51))
                CenterArc((1.21, 2.51), 0.2, 0, 90)
                Line((1.21, 2.71), (-1.21, 2.71))
            make_face()
        # OneSide extrude, distance=-0.075
        extrude(amount=-0.075, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 13.44, perimeter: 15.2
            with BuildLine():
                Line((1.4, -2.4), (1.4, 2.4))
                Line((1.4, 2.4), (-1.4, 2.4))
                Line((-1.4, 2.4), (-1.4, -2.4))
                Line((-1.4, -2.4), (1.4, -2.4))
            make_face()
        # OneSide extrude, distance=2.03
        extrude(amount=2.03, mode=Mode.ADD)

        # Sketch3 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -0.075, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 1.62, perimeter: 5.24
            with BuildLine():
                Line((-0.81, -1.98), (0.81, -1.98))
                Line((0.81, -1.98), (0.81, -0.98))
                Line((-0.81, -0.98), (0.81, -0.98))
                Line((-0.81, -0.98), (-0.81, -1.98))
            make_face()
        # OneSide extrude, distance=0.05
        extrude(amount=0.05, mode=Mode.ADD)
    return part.part


def model_118621_276dd2d4_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 49.1934637136, perimeter: 30.8349872739
            with BuildLine():
                Line((10.16, -0.0069348054), (0, 0))
                Line((0, 0), (-0.0045076225, -6.6039984616))
                Line((-0.0045076225, -6.6039984616), (2.5354923775, -6.605732163))
                Line((2.5354923775, -6.605732163), (2.5359258028, -5.9707323109))
                Line((2.5359258028, -5.9707323109), (10.1582662986, -2.5469348054))
                Line((10.1582662986, -2.5469348054), (10.16, -0.0069348054))
            make_face()
        # Symmetric extrude, full_length=True, total=6.35
        extrude(amount=3.175, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.0045076225, 0, 6.6039984616), x_dir=(0, -1, 0), z_dir=(-0.0006825594, 0, 0.9999997671))):
            # Profile area: 1.6004051703, perimeter: 4.4845606811
            with Locations((0, 1.27)):
                Circle(0.71374)
        # OneSide extrude, distance=-3.81
        extrude(amount=-3.81, mode=Mode.SUBTRACT)
    return part.part


def model_119027_cf658ca8_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 21 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0019922236, perimeter: 0.7687692974
            with BuildLine():
                CenterArc((0.1357846253, 7.1274869185), 2.3764074343, -94.6363342027, 9.2726684055)
                Line((-0.0563028043, 4.7588555176), (0.3278720549, 4.7588555176))
            make_face()
            # Profile area: 4.5480772392, perimeter: 10.9909325888
            with BuildLine():
                Line((-2.4791901818, 4.7588555176), (-0.0563028043, 4.7588555176))
                Line((-2.4791901818, 4.70520632), (-2.4791901818, 4.7588555176))
                Line((-2.5473237211, 4.70520632), (-2.4791901818, 4.70520632))
                CenterArc((-0.0289814656, 6.6946846226), 3.2093724671, -141.6914336457, 104.5934481882)
                Line((0.3278720549, 4.7588555176), (2.5308305019, 4.7588555176))
                CenterArc((0.1357846253, 7.1274869185), 2.3764074343, -94.6363342027, 9.2726684055)
            make_face()
            # Profile area: 14.0183143284, perimeter: 26.0803280212
            with BuildLine():
                CenterArc((2.5313556341, 6.7209568143), 0.7328272794, -164.2459641834, 133.5466358183)
                CenterArc((-0.0289814656, 6.6946846226), 3.2093724671, -6.2224483064, 195.0892236848)
                Line((-2.4791901818, 6.2000000924), (-3.2000000477, 6.2000000924))
                Line((-2.4791901818, 4.7588555176), (-2.4791901818, 6.2000000924))
                Line((-2.4791901818, 4.7588555176), (-0.0563028043, 4.7588555176))
                CenterArc((0.1357846253, 7.1274869185), 2.3764074343, -113.7413215296, 19.1049873268)
                CenterArc((-0.0310503461, 6.6368412174), 1.860654704, -3.5389592455, 248.4172921452)
            make_face()
            # Profile area: 68.4634549342, perimeter: 38.5342045639
            with BuildLine():
                CenterArc((-0.0289814656, 6.6946846226), 3.2093724671, -141.6914336457, 104.5934481882)
                Line((-3.2000000477, 4.70520632), (-2.5473237211, 4.70520632))
                Line((-3.2000000477, 4.7588555176), (-3.2000000477, 4.70520632))
                Line((-3.2123087791, 4.7588555176), (-3.2000000477, 4.7588555176))
                Line((-3.2123087791, 3.3392793438), (-3.2123087791, 4.7588555176))
                Line((-3.2123087791, 3.3392793438), (-2.8123087791, 3.3392793438))
                Line((-2.8123087791, 3.3392793438), (-2.8123087791, 0.8107734288))
                Line((-2.8123087791, 0.8107734288), (-3.2123087791, 0.8107734288))
                Line((-3.2123087791, -6.7911444824), (-3.2123087791, 0.8107734288))
                Line((3.2876912209, -6.7911444824), (-3.2123087791, -6.7911444824))
                Line((3.2876912209, 0.8303742498), (3.2876912209, -6.7911444824))
                Line((2.8876912209, 0.8303742498), (3.2876912209, 0.8303742498))
                Line((2.8876912209, 3.3588801648), (2.8876912209, 0.8303742498))
                Line((3.2876912209, 3.3588801648), (2.8876912209, 3.3588801648))
                Line((3.2876912209, 4.7588555176), (3.2876912209, 3.3588801648))
                Line((2.5308305019, 4.7588555176), (3.2876912209, 4.7588555176))
            make_face()
            # Profile area: 0.033895057, perimeter: 1.3853417583
            with BuildLine():
                CenterArc((-0.0289814656, 6.6946846226), 3.2093724671, -142.9020145425, 1.2105808968)
                Line((-3.2000000477, 4.7588555176), (-2.5887934331, 4.7588555176))
                Line((-3.2000000477, 4.7588555176), (-3.2000000477, 4.70520632))
                Line((-3.2000000477, 4.70520632), (-2.5473237211, 4.70520632))
            make_face()
            # Profile area: 0.004775814, perimeter: 0.2991956076
            with BuildLine():
                Line((-2.5887934331, 4.7588555176), (-2.4791901818, 4.7588555176))
                CenterArc((-0.0289814656, 6.6946846226), 3.2093724671, -142.9020145425, 1.2105808968)
                Line((-2.5473237211, 4.70520632), (-2.4791901818, 4.70520632))
                Line((-2.4791901818, 4.70520632), (-2.4791901818, 4.7588555176))
            make_face()
            # Profile area: 0.6998119591, perimeter: 3.8529039815
            with BuildLine():
                CenterArc((-0.0289814656, 6.6946846226), 3.2093724671, -171.1332246216, 28.2312100791)
                Line((-2.5887934331, 4.7588555176), (-2.4791901818, 4.7588555176))
                Line((-2.4791901818, 4.7588555176), (-2.4791901818, 6.2000000924))
                Line((-2.4791901818, 6.2000000924), (-3.2000000477, 6.2000000924))
            make_face()
            # Profile area: 1.011402366, perimeter: 5.85701183
            with BuildLine():
                Line((-2.8123087791, 0.8107734288), (-3.2123087791, 0.8107734288))
                Line((-2.8123087791, 3.3392793438), (-2.8123087791, 0.8107734288))
                Line((-3.2123087791, 3.3392793438), (-2.8123087791, 3.3392793438))
                Line((-3.2123087791, 0.8107734288), (-3.2123087791, 3.3392793438))
            make_face()
            # Profile area: 1.011402366, perimeter: 5.85701183
            with BuildLine():
                Line((3.2876912209, 3.3588801648), (2.8876912209, 3.3588801648))
                Line((2.8876912209, 3.3588801648), (2.8876912209, 0.8303742498))
                Line((2.8876912209, 0.8303742498), (3.2876912209, 0.8303742498))
                Line((3.2876912209, 0.8303742498), (3.2876912209, 3.3588801648))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 21 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.3389792686, perimeter: 3.6336974789
            with BuildLine():
                Line((-3.2000000477, 6.2000000924), (-3.2000000477, 4.7588555176))
                Line((-3.2000000477, 4.7588555176), (-2.5887934331, 4.7588555176))
                CenterArc((-0.0289814656, 6.6946846226), 3.2093724671, -171.1332246216, 28.2312100791)
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 17.5, perimeter: 17
            with BuildLine():
                Line((2.5764033662, -0.0441090195), (-2.4235966338, -0.0441090195))
                Line((2.5764033662, 3.4558909805), (2.5764033662, -0.0441090195))
                Line((-2.4235966338, 3.4558909805), (2.5764033662, 3.4558909805))
                Line((-2.4235966338, -0.0441090195), (-2.4235966338, 3.4558909805))
            make_face()
        # OneSide extrude, distance=1.27
        extrude(amount=1.27, mode=Mode.ADD)

        # Sketch1 -> Extrude5 (Join)
        # Sketch on XY construction plane
        # Sketch has 21 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.011402366, perimeter: 5.85701183
            with BuildLine():
                Line((3.2876912209, 3.3588801648), (2.8876912209, 3.3588801648))
                Line((2.8876912209, 3.3588801648), (2.8876912209, 0.8303742498))
                Line((2.8876912209, 0.8303742498), (3.2876912209, 0.8303742498))
                Line((3.2876912209, 0.8303742498), (3.2876912209, 3.3588801648))
            make_face()
            # Profile area: 1.011402366, perimeter: 5.85701183
            with BuildLine():
                Line((-2.8123087791, 0.8107734288), (-3.2123087791, 0.8107734288))
                Line((-2.8123087791, 3.3392793438), (-2.8123087791, 0.8107734288))
                Line((-3.2123087791, 3.3392793438), (-2.8123087791, 3.3392793438))
                Line((-3.2123087791, 0.8107734288), (-3.2123087791, 3.3392793438))
            make_face()
        # OneSide extrude, distance=-0.15
        extrude(amount=-0.15, mode=Mode.ADD)
    return part.part


def model_119895_6c95f34d_0000():
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
        # Sketch on YZ construction plane
        # Sketch has 30 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 20.08821303, perimeter: 72.5507418573
            with BuildLine():
                Line((-1, 3), (-2.373174793, 7.2474091548))
                _nurbs_edge([(-2.373174793, 7.2474091548), (-2.3687732866, 7.2716367625), (-2.364194472, 7.3274873965), (-2.3740111955, 7.423376634), (-2.4218858317, 7.5674874447), (-2.5336664224, 7.7492693011), (-2.6903553993, 7.9053060322), (-2.8717094156, 8.001142856), (-3.0595270967, 8.0166573946), (-3.2362536967, 7.9484229679), (-3.3864965157, 7.8126537691), (-3.4973907744, 7.6363330523), (-3.5468824998, 7.4880295059), (-3.5592983854, 7.3857175238), (-3.5564234708, 7.3240694552), (-3.5522214252, 7.2950733863)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.4573754539, 0.4573754539, 0.4573754539, 0.4573754539, 0.4573754539, 0.4573754539, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1, 1, 1, 1, 1], 5)
                Line((-5, 3), (-3.5522214252, 7.2950733863))
                Line((-5.2975433699, 3), (-5, 3))
                Line((-7.5, 3), (-5.2975433699, 3))
                CenterArc((-7.5, 2.5), 0.5, 90, 90)
                Line((-8, -2.5), (-8, 2.5))
                Line((-7.5, -2.5), (-8, -2.5))
                Line((-7.5, -0.5), (-7.5, -2.5))
                Line((-7.5, -0.5), (2, -0.5))
                Line((2, -0.5), (2, -2.5))
                Line((2, -2.5), (2.5, -2.5))
                Line((2.5, 2), (2.5, -2.5))
                CenterArc((1.5, 2), 1, 0, 90)
                Line((-1, 3), (1.5, 3))
            make_face()
            with BuildLine():
                Line((-7, 2.5), (-5, 2.5))
                Line((-5, 2.5), (-4.4237762112, 2.5))
                Line((-4.4237762112, 2.5), (-3, 7))
                Line((-3, 7), (-1.5508733981, 2.5176619667))
                Line((-1.5508733981, 2.5176619667), (-1, 2.5))
                Line((-1, 2.5), (1.5, 2.5))
                CenterArc((1.5, 2), 0.5, 0, 90)
                Line((2, 2), (2, 0))
                Line((2, 0), (0, 0))
                Line((0, 0), (-7.5, 0))
                Line((-7.5, 2), (-7.5, 0))
                CenterArc((-7, 2), 0.5, 90, 90)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=6
        extrude(amount=6)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -0.5, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.122874169, perimeter: 1.4079837913
            with BuildLine():
                Line((0.115957551, 7), (0.5, 7))
                Line((0.5, 7.3199494467), (0.5, 7))
                Line((0.115957551, 7.3199494467), (0.5, 7.3199494467))
                Line((0.115957551, 7), (0.115957551, 7.3199494467))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


def model_119904_87c09b29_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch4 -> Extrude4 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 96 constraints, 17 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.8012700636, perimeter: 16.2254010367
            with BuildLine():
                Line((7, -15), (15.0127005169, -15))
                Line((7, -15), (7, -15.1000000015))
                Line((7, -15.1000000015), (15.0127005169, -15.1000000015))
                Line((15.0127005169, -15), (15.0127005169, -15.1000000015))
            make_face()
            # Profile area: 1.0012700666, perimeter: 20.2254010367
            with BuildLine():
                Line((5, -11), (15.0127005169, -11))
                Line((5, -11), (5, -11.1000000015))
                Line((5, -11.1000000015), (15.0127005169, -11.1000000015))
                Line((15.0127005169, -11), (15.0127005169, -11.1000000015))
            make_face()
            # Profile area: 0.5155091336, perimeter: 10.5101825206
            with BuildLine():
                Line((7, -20.2550912603), (6.8999999985, -20.2550912603))
                Line((7, -15.1000000015), (7, -20.2550912603))
                Line((6.8999999985, -15.1000000015), (7, -15.1000000015))
                Line((6.8999999985, -15.1000000015), (6.8999999985, -20.2550912603))
            make_face()
            # Profile area: 0.5900000086, perimeter: 12
            with BuildLine():
                Line((6.8999999985, -15), (6.8999999985, -15.1000000015))
                Line((5, -15), (6.8999999985, -15))
                Line((5, -11.1000000015), (5, -15))
                Line((4.8999999985, -11.1000000015), (5, -11.1000000015))
                Line((4.8999999985, -11.1000000015), (4.8999999985, -15.1000000015))
                Line((4.8999999985, -15.1000000015), (6.8999999985, -15.1000000015))
            make_face()
            # Profile area: 0.5900000086, perimeter: 12
            with BuildLine():
                Line((4.8999999985, -11), (4.8999999985, -11.1000000015))
                Line((4, -11), (4.8999999985, -11))
                Line((4, -6.1000000015), (4, -11))
                Line((3.8999999985, -6.1000000015), (4, -6.1000000015))
                Line((3.8999999985, -6.1000000015), (3.8999999985, -11.1000000015))
                Line((3.8999999985, -11.1000000015), (4.8999999985, -11.1000000015))
            make_face()
            # Profile area: 1.1012700681, perimeter: 22.2254010367
            with BuildLine():
                Line((4, -6), (15.0127005169, -6))
                Line((4, -6), (4, -6.1000000015))
                Line((4, -6.1000000015), (15.0127005169, -6.1000000015))
                Line((15.0127005169, -6), (15.0127005169, -6.1000000015))
            make_face()
            # Profile area: 4.7522883746, perimeter: 95.2457660779
            with BuildLine():
                Line((2, -20.2550912603), (1.8999999985, -20.2550912603))
                Line((1.8999999985, -20.2550912603), (-12.8999999985, -20.2550912603))
                Line((-12.8999999985, -20.2550912603), (-12.8999999985, -15.1000000015))
                Line((-12.8999999985, -15.1000000015), (-12.8999999985, -15))
                Line((-12.8999999985, -15), (-13, -15))
                Line((-13, -20.3550912618), (-13, -15))
                Line((15.1127005184, -20.3550912618), (-13, -20.3550912618))
                Line((15.1127005184, -6.1000000015), (15.1127005184, -20.3550912618))
                Line((15.0127005169, -6.1000000015), (15.1127005184, -6.1000000015))
                Line((15.0127005169, -6.1000000015), (15.0127005169, -11))
                Line((15.0127005169, -11), (15.0127005169, -11.1000000015))
                Line((15.0127005169, -11.1000000015), (15.0127005169, -15))
                Line((15.0127005169, -15), (15.0127005169, -15.1000000015))
                Line((15.0127005169, -15.1000000015), (15.0127005169, -20.2550912603))
                Line((15.0127005169, -20.2550912603), (7, -20.2550912603))
                Line((7, -20.2550912603), (6.8999999985, -20.2550912603))
                Line((6.8999999985, -20.2550912603), (2, -20.2550912603))
            make_face()
            # Profile area: 0.4900000072, perimeter: 10
            with BuildLine():
                Line((3.8999999985, -6), (3.8999999985, -6.1000000015))
                Line((3, -6), (3.8999999985, -6))
                Line((3, -2.1000000015), (3, -6))
                Line((2.8999999985, -2.1000000015), (3, -2.1000000015))
                Line((2.8999999985, -2.1000000015), (2.8999999985, -6.1000000015))
                Line((2.8999999985, -6.1000000015), (3.8999999985, -6.1000000015))
            make_face()
            # Profile area: 1.2012700696, perimeter: 24.2254010367
            with BuildLine():
                Line((3, -2), (15.0127005169, -2))
                Line((3, -2), (3, -2.1000000015))
                Line((3, -2.1000000015), (15.0127005169, -2.1000000015))
                Line((15.0127005169, -2), (15.0127005169, -2.1000000015))
            make_face()
            # Profile area: 1.3012700711, perimeter: 26.2254010367
            with BuildLine():
                Line((2, 2), (15.0127005169, 2))
                Line((2, 2), (2, 1.8999999985))
                Line((2, 1.8999999985), (15.0127005169, 1.8999999985))
                Line((15.0127005169, 2), (15.0127005169, 1.8999999985))
            make_face()
            # Profile area: 5.4812701331, perimeter: 109.8254010308
            with BuildLine():
                Line((-2.1603295973, 15.8999999985), (-2.0603295958, 15.8999999985))
                Line((-2.0603295958, 15.8999999985), (15.0127005169, 15.8999999985))
                Line((15.0127005169, 15.8999999985), (15.0127005169, 11))
                Line((15.0127005169, 11), (15.0127005169, 10.8999999985))
                Line((15.0127005169, 10.8999999985), (15.0127005169, 7))
                Line((15.0127005169, 7), (15.0127005169, 6.8999999985))
                Line((15.0127005169, 6.8999999985), (15.0127005169, 2))
                Line((15.0127005169, 2), (15.0127005169, 1.8999999985))
                Line((15.0127005169, 1.8999999985), (15.0127005169, -2))
                Line((15.0127005169, -2), (15.0127005169, -2.1000000015))
                Line((15.0127005169, -2.1000000015), (15.0127005169, -6))
                Line((15.0127005169, -6), (15.1127005184, -6))
                Line((15.1127005184, 16), (15.1127005184, -6))
                Line((-13, 16), (15.1127005184, 16))
                Line((-13, 11.1000000015), (-13, 16))
                Line((-12.8999999985, 11.1000000015), (-13, 11.1000000015))
                Line((-12.8999999985, 11.1000000015), (-12.8999999985, 15.8999999985))
                Line((-12.8999999985, 15.8999999985), (-8.0528416518, 15.8999999985))
                Line((-8.0528416518, 15.8999999985), (-7.9528416503, 15.8999999985))
                Line((-7.9528416503, 15.8999999985), (-2.1603295973, 15.8999999985))
            make_face()
            # Profile area: 1.4012700726, perimeter: 28.2254010367
            with BuildLine():
                Line((1, 7), (15.0127005169, 7))
                Line((1, 7), (1, 6.8999999985))
                Line((1, 6.8999999985), (15.0127005169, 6.8999999985))
                Line((15.0127005169, 7), (15.0127005169, 6.8999999985))
            make_face()
            # Profile area: 1.6012700755, perimeter: 32.2254010367
            with BuildLine():
                Line((-1, 10.8999999985), (15.0127005169, 10.8999999985))
                Line((15.0127005169, 11), (15.0127005169, 10.8999999985))
                Line((-1, 11), (15.0127005169, 11))
                Line((-1, 11), (-1, 10.8999999985))
            make_face()
            # Profile area: 0.4900000072, perimeter: 10
            with BuildLine():
                Line((2.8999999985, -2), (2.8999999985, -2.1000000015))
                Line((2, -2), (2.8999999985, -2))
                Line((2, 1.8999999985), (2, -2))
                Line((1.8999999985, 1.8999999985), (2, 1.8999999985))
                Line((1.8999999985, 1.8999999985), (1.8999999985, -2.1000000015))
                Line((1.8999999985, -2.1000000015), (2.8999999985, -2.1000000015))
            make_face()
            # Profile area: 0.5960329683, perimeter: 12.1206591916
            with BuildLine():
                Line((-1.1000000015, 11), (-1.1000000015, 10.8999999985))
                Line((-2.0603295958, 11), (-1.1000000015, 11))
                Line((-2.0603295958, 15.8999999985), (-2.0603295958, 11))
                Line((-2.1603295973, 15.8999999985), (-2.0603295958, 15.8999999985))
                Line((-2.1603295973, 15.8999999985), (-2.1603295973, 10.8999999985))
                Line((-2.1603295973, 10.8999999985), (-1.1000000015, 10.8999999985))
            make_face()
            # Profile area: 0.5900000086, perimeter: 12
            with BuildLine():
                Line((-1.1000000015, 6.8999999985), (0.8999999985, 6.8999999985))
                Line((0.8999999985, 7), (0.8999999985, 6.8999999985))
                Line((-1, 7), (0.8999999985, 7))
                Line((-1, 10.8999999985), (-1, 7))
                Line((-1.1000000015, 10.8999999985), (-1, 10.8999999985))
                Line((-1.1000000015, 10.8999999985), (-1.1000000015, 6.8999999985))
            make_face()
            # Profile area: 0.5900000086, perimeter: 12
            with BuildLine():
                Line((1.8999999985, 2), (1.8999999985, 1.8999999985))
                Line((1, 2), (1.8999999985, 2))
                Line((1, 6.8999999985), (1, 2))
                Line((0.8999999985, 6.8999999985), (1, 6.8999999985))
                Line((0.8999999985, 6.8999999985), (0.8999999985, 1.8999999985))
                Line((0.8999999985, 1.8999999985), (1.8999999985, 1.8999999985))
            make_face()
            # Profile area: 1.3383357649, perimeter: 26.9667149028
            with BuildLine():
                Line((-12.8999999985, 2.4833574514), (-13, 2.4833574514))
                Line((-13, -10.8999999985), (-13, 2.4833574514))
                Line((-12.8999999985, -10.8999999985), (-13, -10.8999999985))
                Line((-12.8999999985, -10.8999999985), (-12.9000001922, -6.5538535911))
                Line((-12.9000001922, -6.5538535911), (-12.8999999985, -6.4538535896))
                Line((-12.8999999985, -6.4538535896), (-12.8999999985, -6.3538535881))
                Line((-12.8999999985, -6.3538535881), (-12.8999999985, -2.3147051895))
                Line((-12.8999999985, -2.3147051895), (-12.8999999985, -2.214705188))
                Line((-12.8999999985, -2.214705188), (-12.8999999985, 2.4833574514))
            make_face()
            # Profile area: 0.9548217244, perimeter: 19.2964342056
            with BuildLine():
                Line((-3.4517828987, -2.214705188), (-3.3517828972, -2.214705188))
                Line((-12.8999999985, -2.214705188), (-3.4517828987, -2.214705188))
                Line((-12.8999999985, -2.3147051895), (-12.8999999985, -2.214705188))
                Line((-12.8999999985, -2.3147051895), (-3.4517828987, -2.3147051895))
                Line((-3.4517828987, -2.3147051895), (-3.3517828972, -2.3147051895))
                Line((-3.3517828972, -2.3147051895), (-3.3517828972, -2.214705188))
            make_face()
            # Profile area: 0.3900000057, perimeter: 8
            with BuildLine():
                Line((-12.8999999985, -11), (-13, -11))
                Line((-13, -14.8999999985), (-13, -11))
                Line((-12.8999999985, -14.8999999985), (-13, -14.8999999985))
                Line((-12.8999999985, -14.8999999985), (-12.8999999985, -11.1000000015))
                Line((-12.8999999985, -11.1000000015), (-12.8999999985, -11))
            make_face()
            # Profile area: 0.4416642613, perimeter: 9.0332850972
            with BuildLine():
                Line((-12.8999999985, 7), (-13, 7))
                Line((-13, 2.5833574529), (-13, 7))
                Line((-12.8999999985, 2.5833574529), (-13, 2.5833574529))
                Line((-12.8999999985, 2.5833574529), (-12.8999999985, 6.8999999985))
                Line((-12.8999999985, 6.8999999985), (-12.8999999985, 7))
            make_face()
            # Profile area: 2.0116642842, perimeter: 40.4332850882
            with BuildLine():
                Line((-6.4233556668, 7), (-12.8999999985, 7))
                Line((-12.8999999985, 6.8999999985), (-12.8999999985, 7))
                Line((-6.4233556668, 6.8999999985), (-12.8999999985, 6.8999999985))
                Line((-6.4233556668, 6.8999999985), (-5.1000000015, 6.8999999985))
                Line((-5.1000000015, 6.8999999985), (-5.1000000015, 3.4884482406))
                Line((-5.1000000015, 3.4884482406), (-5.1000000015, 2.5833574529))
                Line((-5.1000000015, 2.5833574529), (-12.8999999985, 2.5833574529))
                Line((-12.8999999985, 2.4833574514), (-12.8999999985, 2.5833574529))
                Line((-5, 2.4833574514), (-12.8999999985, 2.4833574514))
                Line((-5, 2.5833574529), (-5, 2.4833574514))
                Line((-5, 3.4884482406), (-5, 2.5833574529))
                Line((-5, 7), (-5, 3.4884482406))
                Line((-6.4233556668, 7), (-5, 7))
            make_face()
            # Profile area: 1.6446337903, perimeter: 33.0926753189
            with BuildLine():
                Line((-3.3517828972, -2.3147051895), (-3.3517828972, -2.214705188))
                Line((-3.3517828972, -2.3147051895), (-2.0222968197, -2.3147051895))
                Line((-2.0222968197, -2.3147051895), (-2.0222968197, -6.3538535881))
                Line((-2.0222968197, -6.3538535881), (-12.8999999985, -6.3538535881))
                Line((-12.8999999985, -6.4538535896), (-12.8999999985, -6.3538535881))
                Line((-1.9222968182, -6.4538535896), (-12.8999999985, -6.4538535896))
                Line((-1.9222968182, -2.214705188), (-1.9222968182, -6.4538535896))
                Line((-3.3517828972, -2.214705188), (-1.9222968182, -2.214705188))
            make_face()
            # Profile area: 0.3900000057, perimeter: 8
            with BuildLine():
                Line((-12.8999999985, 11), (-13, 11))
                Line((-13, 7.1000000015), (-13, 11))
                Line((-12.8999999985, 7.1000000015), (-13, 7.1000000015))
                Line((-12.8999999985, 7.1000000015), (-12.8999999985, 10.8999999985))
                Line((-12.8999999985, 10.8999999985), (-12.8999999985, 11))
            make_face()
            # Profile area: 3.0146142644, perimeter: 60.4922930056
            with BuildLine():
                Line((-1.9222968182, -6.4538535896), (-12.8999999985, -6.4538535896))
                Line((-12.9000001922, -6.5538535911), (-12.8999999985, -6.4538535896))
                Line((-1.9222968182, -6.5538535911), (-12.9000001922, -6.5538535911))
                Line((-1.9222968182, -6.5538535911), (-0.1000000015, -6.5538535911))
                Line((-0.1000000015, -6.5538535911), (-0.1000000015, -10.8999999985))
                Line((-0.1000000015, -10.8999999985), (-12.8999999985, -10.8999999985))
                Line((-12.8999999985, -11), (-12.8999999985, -10.8999999985))
                Line((0, -11), (-12.8999999985, -11))
                Line((0, -6.4538535896), (0, -11))
                Line((-1.9222968182, -6.4538535896), (0, -6.4538535896))
            make_face()
            # Profile area: 1.675328891, perimeter: 33.706577324
            with BuildLine():
                Line((-7.9528416503, 11), (-12.8999999985, 11))
                Line((-12.8999999985, 10.8999999985), (-12.8999999985, 11))
                Line((-6.5233556682, 10.8999999985), (-12.8999999985, 10.8999999985))
                Line((-6.5233556682, 10.8999999985), (-6.5233556682, 7.1000000015))
                Line((-6.5233556682, 7.1000000015), (-12.8999999985, 7.1000000015))
                Line((-12.8999999985, 7), (-12.8999999985, 7.1000000015))
                Line((-6.4233556668, 7), (-12.8999999985, 7))
                Line((-6.4233556668, 11), (-6.4233556668, 7))
                Line((-7.9528416503, 11), (-6.4233556668, 11))
            make_face()
            # Profile area: 1.7700000259, perimeter: 35.599999994
            with BuildLine():
                Line((0, -11), (-12.8999999985, -11))
                Line((-12.8999999985, -11.1000000015), (-12.8999999985, -11))
                Line((0, -11.1000000015), (-12.8999999985, -11.1000000015))
                Line((0, -11.1000000015), (0.8999999985, -11.1000000015))
                Line((0.8999999985, -11.1000000015), (0.8999999985, -14.8999999985))
                Line((1, -14.8999999985), (0.8999999985, -14.8999999985))
                Line((1, -11), (1, -14.8999999985))
                Line((0, -11), (1, -11))
            make_face()
            # Profile area: 0.974715849, perimeter: 19.6943166934
            with BuildLine():
                Line((-8.0528416518, 15.8999999985), (-7.9528416503, 15.8999999985))
                Line((-8.0528416518, 15.8999999985), (-8.0528416518, 11.1000000015))
                Line((-8.0528416518, 11.1000000015), (-12.8999999985, 11.1000000015))
                Line((-12.8999999985, 11), (-12.8999999985, 11.1000000015))
                Line((-7.9528416503, 11), (-12.8999999985, 11))
                Line((-7.9528416503, 15.8999999985), (-7.9528416503, 11))
            make_face()
            # Profile area: 2.0055091556, perimeter: 40.3101825176
            with BuildLine():
                Line((1, -15), (0.8999999985, -15))
                Line((0.8999999985, -15), (-12.8999999985, -15))
                Line((-12.8999999985, -15.1000000015), (-12.8999999985, -15))
                Line((1, -15.1000000015), (-12.8999999985, -15.1000000015))
                Line((1.8999999985, -15.1000000015), (1, -15.1000000015))
                Line((1.8999999985, -15.1000000015), (1.8999999985, -20.2550912603))
                Line((2, -20.2550912603), (1.8999999985, -20.2550912603))
                Line((2, -15), (2, -20.2550912603))
                Line((2, -15), (1, -15))
            make_face()
            # Profile area: 0.6346279837, perimeter: 12.8925594874
            with BuildLine():
                Line((-5, 2.5833574529), (-5, 2.4833574514))
                Line((-3.4517828987, 2.4833574514), (-5, 2.4833574514))
                Line((-3.4517828987, -2.214705188), (-3.4517828987, 2.4833574514))
                Line((-3.4517828987, -2.214705188), (-3.3517828972, -2.214705188))
                Line((-3.3517828972, -2.214705188), (-3.3517828972, 2.5833574529))
                Line((-3.3517828972, 2.5833574529), (-5, 2.5833574529))
            make_face()
        # OneSide extrude, distance=14
        extrude(amount=14)
    return part.part


def model_119917_fc3018e0_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1351.934652121, perimeter: 287.1531452758
            with BuildLine():
                Line((-19.7565634664, 19.7565634664), (-39.5131269327, 0))
                Line((-39.5131269327, 0), (-20.074198449, -19.4389284837))
                CenterArc((-0.7265253404, -1.8100715979), 26.1745878634, -137.6614199857, 92.5275478736)
                CenterArc((0, -2.5399999619), 25.1447167614, -45.1338721121, 90.1338721121)
                CenterArc((3.0453318009, 1.3579189117), 20.2440758756, 43.2934750783, 91.1678234862)
                Line((-13.4703841816, 13.4703841816), (-11.1341721514, 15.8065962118))
                Line((-19.7565634664, 19.7565634664), (-13.4703841816, 13.4703841816))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 16.7894, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=20.955
        extrude(amount=20.955)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-19.7565634664, 19.7565634664, 0), x_dir=(0, 0, 1), z_dir=(-0.7071067812, 0.7071067812, 0))):
            # Profile area: 505.1916475724, perimeter: 90.9847638957
            with BuildLine():
                Line((20.104345487, -27.089345487), (20.104345487, -0.850654513))
                Line((20.104345487, -0.850654513), (0.850654513, -0.850654513))
                Line((0.850654513, -0.850654513), (0.850654513, -27.089345487))
                Line((0.850654513, -27.089345487), (20.104345487, -27.089345487))
            make_face()
        # OneSide extrude, distance=-10.16
        extrude(amount=-10.16, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-19.7565634664, 19.7565634664, 0), x_dir=(0, 0, 1), z_dir=(-0.7071067812, 0.7071067812, 0))):
            # Profile area: 414.1059475551, perimeter: 225.0243478031
            with BuildLine():
                Line((-3.6805434754, -31.6205434754), (24.6355434754, -31.6205434754))
                Line((24.6355434754, -31.6205434754), (24.6355434754, 3.6805434754))
                Line((24.6355434754, 3.6805434754), (-3.6805434754, 3.6805434754))
                Line((-3.6805434754, 3.6805434754), (-3.6805434754, -31.6205434754))
            make_face()
            with BuildLine():
                Line((20.955, -27.94), (20.955, 0))
                Line((0, -27.94), (20.955, -27.94))
                Line((0, 0), (0, -27.94))
                Line((20.955, 0), (0, 0))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3175
        extrude(amount=0.3175)
    return part.part


def model_120462_13aff06e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 117 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.5909377932, perimeter: 19.3787672852
            with BuildLine():
                Line((-0.1175881059, -1.1000000164), (0.8496707457, -1.0134807262))
                Line((0.8496707457, -0.5134807262), (0.8496707457, -1.0134807262))
                Line((0.8496707457, -0.5134807262), (0.8648238045, 0.3500000052))
                CenterArc((0.0771868559, 0.363822096), 0.7877582199, -1.0053695239, 27.0839785672)
                CenterArc((1.7437793073, 1.1795059158), 1.0677391509, -174.1878172414, 20.2664262847)
                CenterArc((-0.1651231145, 0.9851965935), 0.8510272677, 5.8121827586, 32.2612163194)
                CenterArc((0.6119857322, 1.5939453648), 0.136126837, -178.0541908344, 36.1275899124)
                Line((0.4759373876, 1.5893232803), (0.4708514294, 1.739025475))
                CenterArc((0.5728850863, 1.74249195), 0.1020925247, 131.8100375137, 50.1357716518)
                CenterArc((0.4507111902, 1.8790878492), 0.0811693114, -48.1899624863, 96.3799249726)
                CenterArc((1.0765166343, 2.5787664229), 0.8575439357, -157.1143822614, 25.3043447477)
                CenterArc((0.5580383627, 2.3599059801), 0.294765461, 157.1143822614, 45.7712354771)
                CenterArc((0.5274832605, 2.3728039231), 0.2615996472, 124.6612555686, 32.4531266929)
                CenterArc((0.3306367909, 2.6574974659), 0.0845201961, -55.3387444314, 50.2495908503)
                CenterArc((-1.8309336961, 2.8500000425), 2.254645587, -5.0891535811, 10.1783071622)
                CenterArc((0.5581742931, 3.0627663836), 0.1439178373, 107.5307113669, 77.5584422142)
                CenterArc((0.5034780561, 3.235917007), 0.0376663491, -72.4692886331, 72.1026792313)
                Line((0.5411436341, 3.2356759989), (0.5438486765, 3.6584294692))
                CenterArc((0.2041072485, 3.6606033484), 0.3397483829, -0.3666094017, 68.7869376966)
                CenterArc((0.3450551287, 4.0169664058), 0.0434760078, 178.442671843, 69.9776564519)
                Line((0.3015951795, 4.0181479601), (0.3020898463, 4.0954562181))
                CenterArc((0.4097500642, 4.0947673403), 0.1076624218, 126.9347729422, 52.698617656)
                Line((0.3450551287, 4.1808240797), (0.4236103145, 4.239879567))
                CenterArc((0.4069765956, 4.2620056206), 0.027681092, -53.0652270578, 105.397235312)
                CenterArc((0.5494399438, 4.4465446275), 0.2054507391, -174.1610490744, 46.4930573286)
                CenterArc((0.4791568254, 4.4393572524), 0.1348010746, 134.7034337074, 51.1355172183)
                CenterArc((0.5906385573, 4.3267154336), 0.29328248, 112.3409460178, 22.3624876896)
                CenterArc((0.4572775814, 4.6512223401), 0.0575591969, -67.6590539822, 66.4422854348)
                CenterArc((-1.8392462035, 4.70000007), 2.3546009382, -1.2167685474, 2.4335370949)
                CenterArc((0.4472509485, 4.7485648362), 0.0675880912, 1.2167685474, 60.6148992551)
                CenterArc((0.5576011234, 4.9546404559), 0.1661731591, 174.2651597641, 67.5665080385)
                Line((0.3922596624, 4.9712452758), (0.3922596624, 5.2500000782))
                CenterArc((0.3329809273, 5.2500000782), 0.0592787351, 0, 57.5086765214)
                CenterArc((0.4208688241, 5.3880025552), 0.104333508, 147.3917274097, 90.1169491118)
                CenterArc((0.4650171392, 5.3597595476), 0.1567428697, 117.6574018499, 29.7343255598)
                CenterArc((0.3292276176, 5.618868358), 0.1357911792, -62.3425981501, 62.0594988181)
                CenterArc((0.3598405567, 5.6187170977), 0.1051778664, -0.2830993321, 72.330429414)
                Line((0.3922596624, 5.7187740073), (0.3935780133, 5.9248104937))
                CenterArc((0.524870755, 5.9239704002), 0.1312954294, 127.337028547, 52.2963620512)
                CenterArc((0.1902320151, 6.3626581087), 0.420456319, -52.662971453, 39.7034054897)
                CenterArc((0.1011215743, 6.3831646481), 0.5118958553, -12.9595659633, 38.0211970446)
                Line((0.5648238001, 6.6000000983), (0.2148237949, 7.3000001088))
                CenterArc((-0.4882850294, 6.9484456966), 0.7860995633, 26.5650511771, 35.2990263889)
                Line((-0.1175881059, 7.6416529632), (-0.1175881059, -1.1000000164))
            make_face()
            # Profile area: 5.5909377932, perimeter: 19.3787672852
            with BuildLine():
                Line((-1.0848469575, -0.5134807262), (-1.0848469575, -1.0134807262))
                Line((-0.1175881059, -1.1000000164), (-1.0848469575, -1.0134807262))
                Line((-0.1175881059, 7.6416529632), (-0.1175881059, -1.1000000164))
                CenterArc((0.2531088176, 6.9484456966), 0.7860995633, 118.1359224341, 35.2990263889)
                Line((-0.8000000119, 6.6000000983), (-0.4500000067, 7.3000001088))
                CenterArc((-0.3362977862, 6.3831646481), 0.5118958553, 154.9383689187, 38.0211970446)
                CenterArc((-0.4254082269, 6.3626581087), 0.420456319, -167.0404340367, 39.7034054897)
                CenterArc((-0.7600469669, 5.9239704002), 0.1312954294, 0.3666094017, 52.2963620512)
                Line((-0.6274358742, 5.7187740073), (-0.6287542251, 5.9248104937))
                CenterArc((-0.5950167686, 5.6187170977), 0.1051778664, 107.9526699181, 72.330429414)
                CenterArc((-0.5644038295, 5.618868358), 0.1357911792, -179.7169006679, 62.0594988181)
                CenterArc((-0.7001933511, 5.3597595476), 0.1567428697, 32.6082725903, 29.7343255598)
                CenterArc((-0.656045036, 5.3880025552), 0.104333508, -57.5086765214, 90.1169491118)
                CenterArc((-0.5681571391, 5.2500000782), 0.0592787351, 122.4913234786, 57.5086765214)
                Line((-0.6274358742, 4.9712452758), (-0.6274358742, 5.2500000782))
                CenterArc((-0.7927773353, 4.9546404559), 0.1661731591, -61.8316678026, 67.5665080385)
                CenterArc((-0.6824271603, 4.7485648362), 0.0675880912, 118.1683321974, 60.6148992551)
                CenterArc((1.6040699916, 4.70000007), 2.3546009382, 178.7832314526, 2.4335370949)
                CenterArc((-0.6924537933, 4.6512223401), 0.0575591969, -178.7832314525, 66.4422854348)
                CenterArc((-0.8258147691, 4.3267154336), 0.29328248, 45.2965662926, 22.3624876896)
                CenterArc((-0.7143330373, 4.4393572524), 0.1348010746, -5.8389509256, 51.1355172183)
                CenterArc((-0.7846161557, 4.4465446275), 0.2054507391, -52.3320082543, 46.4930573286)
                CenterArc((-0.6421528074, 4.2620056206), 0.027681092, 127.6679917457, 105.397235312)
                Line((-0.5802313405, 4.1808240797), (-0.6587865263, 4.239879567))
                CenterArc((-0.644926276, 4.0947673403), 0.1076624218, 0.3666094017, 52.698617656)
                Line((-0.5367713913, 4.0181479601), (-0.5372660581, 4.0954562181))
                CenterArc((-0.5802313405, 4.0169664058), 0.0434760078, -68.4203282949, 69.9776564519)
                CenterArc((-0.4392834603, 3.6606033484), 0.3397483829, 111.5796717051, 68.7869376966)
                Line((-0.776319846, 3.2356759989), (-0.7790248883, 3.6584294692))
                CenterArc((-0.7386542679, 3.235917007), 0.0376663491, -179.6333905983, 72.1026792313)
                CenterArc((-0.7933505049, 3.0627663836), 0.1439178373, -5.0891535811, 77.5584422142)
                CenterArc((1.5957574843, 2.8500000425), 2.254645587, 174.9108464189, 10.1783071622)
                CenterArc((-0.5658130027, 2.6574974659), 0.0845201961, -174.9108464189, 50.2495908503)
                CenterArc((-0.7626594723, 2.3728039231), 0.2615996472, 22.8856177386, 32.4531266929)
                CenterArc((-0.7932145746, 2.3599059801), 0.294765461, -22.8856177386, 45.7712354771)
                CenterArc((-1.3116928462, 2.5787664229), 0.8575439357, -48.1899624863, 25.3043447477)
                CenterArc((-0.6858874021, 1.8790878492), 0.0811693114, 131.8100375137, 96.3799249726)
                CenterArc((-0.8080612982, 1.74249195), 0.1020925247, -1.9458091656, 50.1357716518)
                Line((-0.7111135995, 1.5893232803), (-0.7060276412, 1.739025475))
                CenterArc((-0.8471619441, 1.5939453648), 0.136126837, -38.073399078, 36.1275899124)
                CenterArc((-0.0700530973, 0.9851965935), 0.8510272677, 141.926600922, 32.2612163194)
                CenterArc((-1.9789555192, 1.1795059158), 1.0677391509, -26.0786090433, 20.2664262847)
                CenterArc((-0.3123630678, 0.363822096), 0.7877582199, 153.9213909567, 27.0839785672)
                Line((-1.0848469575, -0.5134807262), (-1.1000000164, 0.3500000052))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.0476146181, perimeter: 15.7903591516
            with BuildLine():
                Line((-0.200000003, -0.200000003), (-0.8621914831, -0.200000003))
                Line((-0.8621914831, -0.200000003), (-0.8648238045, -0.3500000052))
                CenterArc((-0.0771868559, -0.363822096), 0.7877582199, 178.9946304761, 27.0839785672)
                CenterArc((-1.7437793073, -1.1795059158), 1.0677391509, 5.8121827586, 20.2664262847)
                CenterArc((0.1651231145, -0.9851965935), 0.8510272677, -174.1878172414, 32.2612163194)
                CenterArc((-0.6119857322, -1.5939453648), 0.136126837, 1.9458091656, 36.1275899124)
                Line((-0.4759373876, -1.5893232803), (-0.4708514294, -1.739025475))
                CenterArc((-0.5728850863, -1.74249195), 0.1020925247, -48.1899624863, 50.1357716518)
                CenterArc((-0.4507111902, -1.8790878492), 0.0811693114, 131.8100375137, 96.3799249726)
                CenterArc((-1.0765166343, -2.5787664229), 0.8575439357, 22.8856177386, 25.3043447477)
                CenterArc((-0.5580383627, -2.3599059801), 0.294765461, -22.8856177386, 45.7712354771)
                CenterArc((-0.5274832605, -2.3728039231), 0.2615996472, -55.3387444314, 32.4531266929)
                CenterArc((-0.3306367909, -2.6574974659), 0.0845201961, 124.6612555686, 50.2495908503)
                CenterArc((1.8309336961, -2.8500000425), 2.254645587, 174.9108464189, 10.1783071622)
                CenterArc((-0.5581742931, -3.0627663836), 0.1439178373, -72.4692886331, 77.5584422142)
                CenterArc((-0.5034780561, -3.235917007), 0.0376663491, 107.5307113669, 72.1026792313)
                Line((-0.5411436341, -3.2356759989), (-0.5438486765, -3.6584294692))
                CenterArc((-0.2041072485, -3.6606033484), 0.3397483829, 179.6333905983, 68.7869376966)
                CenterArc((-0.3450551287, -4.0169664058), 0.0434760078, -1.557328157, 69.9776564519)
                Line((-0.3015951795, -4.0181479601), (-0.3020898463, -4.0954562181))
                CenterArc((-0.4097500642, -4.0947673403), 0.1076624218, -53.0652270578, 52.698617656)
                Line((-0.3450551287, -4.1808240797), (-0.4236103145, -4.239879567))
                CenterArc((-0.4069765956, -4.2620056206), 0.027681092, 126.9347729422, 105.397235312)
                CenterArc((-0.5494399438, -4.4465446275), 0.2054507391, 5.8389509256, 46.4930573286)
                CenterArc((-0.4791568254, -4.4393572524), 0.1348010746, -45.2965662926, 51.1355172183)
                CenterArc((-0.5906385573, -4.3267154336), 0.29328248, -67.6590539822, 22.3624876896)
                CenterArc((-0.4572775814, -4.6512223401), 0.0575591969, 112.3409460178, 66.4422854348)
                CenterArc((1.8392462035, -4.70000007), 2.3546009382, 178.7832314526, 2.4335370949)
                CenterArc((-0.4472509485, -4.7485648362), 0.0675880912, -178.7832314526, 60.6148992551)
                CenterArc((-0.5576011234, -4.9546404559), 0.1661731591, -5.7348402359, 67.5665080385)
                Line((-0.3922596624, -4.9712452758), (-0.3922596624, -5.2500000782))
                CenterArc((-0.3329809273, -5.2500000782), 0.0592787351, 180, 57.5086765214)
                CenterArc((-0.4208688241, -5.3880025552), 0.104333508, -32.6082725903, 90.1169491118)
                CenterArc((-0.4650171392, -5.3597595476), 0.1567428697, -62.3425981501, 29.7343255598)
                CenterArc((-0.3292276176, -5.618868358), 0.1357911792, 117.6574018499, 62.0594988181)
                CenterArc((-0.3598405567, -5.6187170977), 0.1051778664, 179.7169006679, 72.330429414)
                Line((-0.3922596624, -5.7187740073), (-0.3935780133, -5.9248104937))
                CenterArc((-0.524870755, -5.9239704002), 0.1312954294, -52.662971453, 52.2963620512)
                CenterArc((-0.1902320151, -6.3626581087), 0.420456319, 127.337028547, 39.7034054897)
                CenterArc((-0.1011215743, -6.3831646481), 0.5118958553, 167.0404340367, 38.0211970446)
                Line((-0.5648238001, -6.6000000983), (-0.2148237949, -7.3000001088))
                CenterArc((0.4882850294, -6.9484456966), 0.7860995633, -153.4349488229, 2.3224664278)
                Line((-0.200000003, -7.3282038271), (-0.200000003, -0.200000003))
            make_face()
        # OneSide extrude, distance=-0.15
        extrude(amount=-0.15, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.200000003, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0369053381, perimeter: 0.9041440339
            with BuildLine():
                Line((0.200000003, 0.3), (-0.1567403616, 0.3))
                CenterArc((0.200000003, 0.6492122924), 0.4992122924, -135.610962239, 45.610962239)
                Line((0.200000003, 0.3), (0.200000003, 0.15))
            make_face()
        # OneSide extrude, distance=0.95
        extrude(amount=0.95, mode=Mode.SUBTRACT)
    return part.part


def model_121267_6afe53d3_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.7413191944, perimeter: 62.875980122
            with BuildLine():
                Line((0.99999, 2.3965), (0.99999, 1.5075))
                Line((0.99999, 1.5075), (0.9099999797, 1.5075))
                Line((0.9099999797, 1.5075), (0.9099999797, 0.9099999797))
                Line((0.9099999797, 0.9099999797), (11.25, 0.9099999797))
                Line((11.25, 0.9099999797), (11.25, 6.424))
                Line((11.25, 6.424), (0.9099999797, 6.424))
                Line((0.9099999797, 6.424), (0.9099999797, 2.3965))
                Line((0.9099999797, 2.3965), (0.99999, 2.3965))
            make_face()
            with BuildLine():
                Line((11.16, 6.334), (1, 6.334))
                Line((11.16, 1), (11.16, 6.334))
                Line((1, 1), (11.16, 1))
                Line((1, 6.334), (1, 1))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0800011281, perimeter: 1.9579800407
            with BuildLine():
                Line((0.9099999797, 2.3965), (0.99999, 2.3965))
                Line((0.9099999797, 2.3965), (0.9099999797, 1.5075))
                Line((0.99999, 1.5075), (0.9099999797, 1.5075))
                Line((0.99999, 2.3965), (0.99999, 1.5075))
            make_face()
            # Profile area: 53.715404659, perimeter: 36.991583561
            with BuildLine():
                Line((1, 6.334), (1, 1))
                Line((1, 1), (11.16, 1))
                Line((11.16, 1), (11.16, 6.334))
                Line((11.16, 6.334), (1, 6.334))
            make_face()
            with BuildLine():
                CenterArc((2.524, 6.08), 0.15925, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.357, 1.254), 0.15925, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((7.604, 1.762), 0.15925, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((7.604, 4.556), 0.15925, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((10.017, 6.08), 0.15925, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((10.652, 1.254), 0.15925, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0305851716, perimeter: 1.7859954236
            with BuildLine():
                CenterArc((2.524, 6.08), 0.15925, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((2.524, 6.08), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            with Locations((2.524, 6.08)):
                Circle(0.125)
            # Profile area: 0.0305851716, perimeter: 1.7859954236
            with BuildLine():
                CenterArc((2.357, 1.254), 0.15925, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((2.357, 1.254), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            with Locations((2.357, 1.254)):
                Circle(0.125)
            # Profile area: 0.0305851716, perimeter: 1.7859954236
            with BuildLine():
                CenterArc((7.604, 1.762), 0.15925, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((7.604, 1.762), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            with Locations((7.604, 1.762)):
                Circle(0.125)
            # Profile area: 0.0305851716, perimeter: 1.7859954236
            with BuildLine():
                CenterArc((7.604, 4.556), 0.15925, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((7.604, 4.556), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            with Locations((7.604, 4.556)):
                Circle(0.125)
            # Profile area: 0.0305851716, perimeter: 1.7859954236
            with BuildLine():
                CenterArc((10.017, 6.08), 0.15925, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((10.017, 6.08), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            with Locations((10.017, 6.08)):
                Circle(0.125)
            # Profile area: 0.0305851716, perimeter: 1.7859954236
            with BuildLine():
                CenterArc((10.652, 1.254), 0.15925, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((10.652, 1.254), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            with Locations((10.652, 1.254)):
                Circle(0.125)
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


def model_121371_3af239ff_0002():
    """Model: hendal"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # Symmetric extrude, full_length=True, total=8
        extrude(amount=4, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(4, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            Circle(0.6)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on XY construction plane
        # Sketch has 10 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4.3272124041, perimeter: 15.3407075111
            with BuildLine():
                Line((-4, 0.5), (-8.5, 0.5))
                CenterArc((-8.5, 0), 0.5, 90, 180)
                Line((-8.5, -0.5), (-4, -0.5))
                Line((-4, 0.5), (-4, -0.5))
            make_face()
            with BuildLine():
                CenterArc((-6.5000000969, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-8.5, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=0.5
        extrude(amount=0.25, both=True, mode=Mode.ADD)
    return part.part


def model_121467_899f0850_0003():
    """Model: handle2"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 9.1415926536, perimeter: 12.2831853072
            with BuildLine():
                CenterArc((1.5, 0), 1, -90, 180)
                Line((-1.5, 1), (1.5, 1))
                CenterArc((-1.5, 0), 1, 90, 180)
                Line((1.5, -1), (-1.5, -1))
            make_face()
        # Symmetric extrude, full_length=True, total=0.5
        extrude(amount=0.25, both=True)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.25), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((1.5, 0)):
                Circle(0.5)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.25), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((1.5, 0)):
                Circle(0.5)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)
    return part.part


def model_121703_69c4a5ac_0001():
    """Model: shot glass v2"""
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
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 78.5398163397, perimeter: 31.4159265359
            Circle(5)
        # OneSide extrude, distance=15
        extrude(amount=15)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 80.9799687091, perimeter: 42.1394087403
            with BuildLine():
                Line((-8.0998438575, 1.25), (-8.0998438575, -3.807339807))
                Line((-8.0998438575, -3.807339807), (7.9125207057, -3.807339807))
                Line((7.9125207057, -3.807339807), (7.9125207057, 1.25))
                Line((7.9125207057, 1.25), (-8.0998438575, 1.25))
            make_face()
        # Symmetric extrude, each_side=7
        extrude(amount=7, both=True, mode=Mode.SUBTRACT)
    return part.part


def model_121860_63471748_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 17 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 50, perimeter: 30
            with BuildLine():
                Line((0, 5), (0, 0))
                Line((0, 0), (10, 0))
                Line((10, 0), (10, 5))
                Line((10, 5), (0, 5))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 32 constraints, 18 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(2, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 22.5506800965, perimeter: 24.5943283326
            with BuildLine():
                CenterArc((5.9405794551, 3.65), 0.5, 26.8918397673, 63.1081602327)
                Line((5.9405794551, 4.15), (4.0594205449, 4.15))
                CenterArc((4.0594205449, 3.65), 0.5, 90, 63.1081602327)
                CenterArc((2.9, 4.238), 0.8, -153.1081602327, 126.2163204654)
                CenterArc((1.7405794551, 3.65), 0.5, 26.8918397673, 63.1081602327)
                Line((1.7405794551, 4.15), (1.3453, 4.15))
                CenterArc((1.3453, 3.6547), 0.4953, 90, 90)
                Line((0.85, 3.6547), (0.85, 1.35))
                CenterArc((1.35, 1.35), 0.5, 180, 90)
                Line((1.35, 0.85), (3.1064971157, 0.85))
                CenterArc((3.1064971157, 1.35), 0.5, -90, 45)
                Line((4.6818019485, 2.2181980515), (3.4600505063, 0.9964466094))
                CenterArc((5, 1.9), 0.45, 45, 90)
                Line((5.3181980515, 2.2181980515), (6.5399494937, 0.9964466094))
                CenterArc((6.8935028843, 1.35), 0.5, -135, 45)
                Line((6.8935028843, 0.85), (8.65, 0.85))
                CenterArc((8.65, 1.35), 0.5, -90, 90)
                Line((9.15, 1.35), (9.15, 3.65))
                CenterArc((8.65, 3.65), 0.5, 0, 90)
                Line((8.65, 4.15), (8.2594205449, 4.15))
                CenterArc((8.2594205449, 3.65), 0.5, 90, 63.1081602327)
                CenterArc((7.1, 4.238), 0.8, -153.1081602327, 126.2163204654)
            make_face()
        # OneSide extrude, distance=-1.3
        extrude(amount=-1.3, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(2, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.726743063, perimeter: 6.2280372895
            with BuildLine():
                Line((6.334314575, 0), (5.3535531916, 0.9807602796))
                CenterArc((5, 0.6272066901), 0.5, 45.000032241, 89.999935518)
                Line((4.6464468084, 0.9807602796), (3.665685425, 0))
                Line((3.665685425, 0), (6.334314575, 0))
            make_face()
        # OneSide extrude, distance=-1.3
        extrude(amount=-1.3, mode=Mode.SUBTRACT)
    return part.part


def model_121869_a29a7922_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 14 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4.0357589723, perimeter: 9.8566025692
            with BuildLine():
                Line((0.4, 1.31), (0.86, 1.31))
                Line((0.4, 1.31), (0.4, 0.7216987154))
                Line((0.4, 0.7216987154), (-0.4, 0.7216987154))
                Line((-0.4, 0.7216987154), (-0.4, 1.31))
                Line((-0.86, 1.31), (-0.4, 1.31))
                Line((-0.86, -1.31), (-0.86, 1.31))
                Line((0.86, -1.31), (-0.86, -1.31))
                Line((0.86, 1.31), (0.86, -1.31))
            make_face()
            # Profile area: 0.4706410277, perimeter: 2.7766025692
            with BuildLine():
                Line((-0.4, 1.31), (0.4, 1.31))
                Line((-0.4, 0.7216987154), (-0.4, 1.31))
                Line((0.4, 0.7216987154), (-0.4, 0.7216987154))
                Line((0.4, 1.31), (0.4, 0.7216987154))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 0.3), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.4706410277, perimeter: 2.7766025692
            with BuildLine():
                Line((0.4, -0.7216987154), (0.4, -1.31))
                Line((-0.4, -0.7216987154), (0.4, -0.7216987154))
                Line((-0.4, -1.31), (-0.4, -0.7216987154))
                Line((-0.4, -1.31), (0.4, -1.31))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.31, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1312302004, perimeter: 1.609913973
            with BuildLine():
                Line((0.2916936622, 0.3502350255), (-0.2861665209, 0.3502350255))
                Line((0.2916936622, 0.5773318289), (0.2916936622, 0.3502350255))
                Line((-0.2861665209, 0.5773318289), (0.2916936622, 0.5773318289))
                Line((-0.2861665209, 0.3502350255), (-0.2861665209, 0.5773318289))
            make_face()
        # OneSide extrude, distance=-0.3865
        extrude(amount=-0.3865, mode=Mode.SUBTRACT)
    return part.part


def model_123863_32847f10_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 280, perimeter: 68
            with BuildLine():
                Line((-10, 7), (10, 7))
                Line((-10, -7), (-10, 7))
                Line((10, -7), (-10, -7))
                Line((10, 7), (10, -7))
            make_face()
        # OneSide extrude, distance=5.5
        extrude(amount=5.5)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 9 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 7), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.25, perimeter: 2
            with BuildLine():
                Line((7, 5), (7.5, 5))
                Line((7.5, 5), (7.5, 5.5))
                Line((7.5, 5.5), (7, 5.5))
                Line((7, 5.5), (7, 5))
            make_face()
            # Profile area: 0.25, perimeter: 2
            with BuildLine():
                Line((8.5, 5.5), (8, 5.5))
                Line((8, 5.5), (8, 5))
                Line((8, 5), (8.5, 5))
                Line((8.5, 5), (8.5, 5.5))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(8.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            with Locations((-7.25, 5.25)):
                Circle(0.125)
        # OneSide extrude, distance=-1.9
        extrude(amount=-1.9, mode=Mode.SUBTRACT)
    return part.part


def model_123927_98bb427e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.8176980266, perimeter: 42.7256600888
            with BuildLine():
                CenterArc((0, 0), 3.7, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=8
        extrude(amount=8)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 30.190705401, perimeter: 19.4778744523
            Circle(3.1)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.0212385966, perimeter: 40.2123859659
            with BuildLine():
                CenterArc((0, 0), 3.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.7752208335, perimeter: 47.7522083346
            with BuildLine():
                CenterArc((0, 0), 3.9, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3.7, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.ADD)
    return part.part


def model_124497_5c00f42d_0012():
    """Model: Grider Vise ASM v4"""
    with BuildPart() as part:
        # Sketch4 -> Extrude5 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 9.5799382767, perimeter: 10.9720123427
            with Locations((-10.16, 1.905)):
                Circle(1.74625)
        # Symmetric extrude, each_side=4.445
        extrude(amount=4.445, both=True)

        # Sketch1 -> Extrude6 (Join)
        # Sketch on XY construction plane
        # Sketch has 10 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 26.1578240743, perimeter: 31.5518882344
            with BuildLine():
                Line((0, 0), (0, 1.905))
                Line((0, 1.905), (-1.74625, 1.905))
                Line((-1.74625, 1.905), (-1.74625, 1.5875))
                Line((-1.74625, 1.5875), (-8.4428562051, 1.5875))
                CenterArc((-10.16, 1.905), 1.74625, -10.4756816964, 190.4756816964)
                Line((-11.90625, 0), (-11.90625, 1.905))
                Line((-4.445, 0), (-11.90625, 0))
                Line((-4.445, -0.635), (-4.445, 0))
                Line((-3.175, -0.635), (-4.445, -0.635))
                Line((-3.175, 0), (-3.175, -0.635))
                Line((0, 0), (-3.175, 0))
            make_face()
        # Symmetric extrude, each_side=4.1275
        extrude(amount=4.1275, both=True, mode=Mode.ADD)

        # Sketch5 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5875, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 15.4035824387, perimeter: 15.8218675899
            with BuildLine():
                Line((8.4428562051, -2.22377), (8.4428562051, 2.22377))
                Line((8.4428562051, -2.22377), (11.90625, -2.22377))
                Line((11.90625, -2.22377), (11.90625, 2.22377))
                Line((11.90625, 2.22377), (8.4428562051, 2.22377))
            make_face()
            # Profile area: 0.1294510113, perimeter: 8.9532924101
            with BuildLine():
                Line((8.41375, 2.22377), (8.41375, -2.22377))
                Line((8.41375, -2.22377), (8.4428562051, -2.22377))
                Line((8.4428562051, -2.22377), (8.4428562051, 2.22377))
                Line((8.4428562051, 2.22377), (8.41375, 2.22377))
            make_face()
        # Symmetric extrude, each_side=7.112
        extrude(amount=7.112, both=True, mode=Mode.SUBTRACT)
    return part.part


def model_124815_b75fa9f5_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4, perimeter: 8
            with BuildLine():
                Line((-3, -3), (-5, -3))
                Line((-3, -1), (-3, -3))
                Line((-5, -1), (-3, -1))
                Line((-5, -3), (-5, -1))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4, perimeter: 8
            with BuildLine():
                Line((3, -3), (1, -3))
                Line((3, -1), (3, -3))
                Line((1, -1), (3, -1))
                Line((1, -3), (1, -1))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.8284271247, perimeter: 3.313708499
            with BuildLine():
                Line((-2.2071067812, 1.5), (-1.7928932188, 1.5))
                Line((-1.7928932188, 1.5), (-1.5, 1.7928932188))
                Line((-1.5, 1.7928932188), (-1.5, 2.2071067812))
                Line((-1.5, 2.2071067812), (-1.7928932188, 2.5))
                Line((-1.7928932188, 2.5), (-2.2071067812, 2.5))
                Line((-2.2071067812, 2.5), (-2.5, 2.2071067812))
                Line((-2.5, 2.2071067812), (-2.5, 1.7928932188))
                Line((-2.5, 1.7928932188), (-2.2071067812, 1.5))
            make_face()
        # OneSide extrude, distance=4
        extrude(amount=4, mode=Mode.ADD)
    return part.part


def model_127023_9a974c7e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 20.029616662, perimeter: 15.8650429006
            Circle(2.525)
        # OneSide extrude, distance=-5.5
        extrude(amount=-5.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 15.7079632679, perimeter: 14.0496294621
            Circle(2.2360679775)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.3574347042, perimeter: 3.8641589639
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.215, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1452201204, perimeter: 1.350884841
            Circle(0.215)
        # OneSide extrude, distance=2.5
        extrude(amount=2.5, mode=Mode.SUBTRACT)
    return part.part


def model_127747_293b9c11_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 50.05, perimeter: 30.02
            with BuildLine():
                Line((-5.005, 2.5), (5.005, 2.5))
                Line((-5.005, -2.5), (-5.005, 2.5))
                Line((5.005, -2.5), (-5.005, -2.5))
                Line((5.005, 2.5), (5.005, -2.5))
            make_face()
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)

        # Sketch8 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -2.5, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((0, 1)):
                Circle(0.3)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8, mode=Mode.ADD)
    return part.part


def model_128043_31dd1a0f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            Circle(0.75)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=-1.8
        extrude(amount=-1.8, mode=Mode.SUBTRACT)
    return part.part


def model_128043_9f8cd69e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.1000000167, perimeter: 22.2000000089
            with BuildLine():
                Line((3.2, 0), (3.2, -2.2))
                Line((3.2, -2.2), (-3.2, -2.2))
                Line((-3.2, 0), (-3.2, -2.2))
                Line((-3.3000000015, 0), (-3.2, 0))
                Line((-3.3000000015, 0), (-3.3000000015, -2.3000000015))
                Line((3.3000000015, -2.3000000015), (-3.3000000015, -2.3000000015))
                Line((3.3000000015, 0), (3.3000000015, -2.3000000015))
                Line((3.2, 0), (3.3000000015, 0))
            make_face()
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(3.3000000015, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1553429178, perimeter: 1.571238901
            with BuildLine():
                Line((-0.4000000015, 0.5009649046), (0, 0.5009649046))
                CenterArc((-0.4000000015, 0.3509649046), 0.15, 90, 180)
                Line((-0.4000000015, 0.2009649046), (0, 0.2009649046))
                Line((0, 0.5009649046), (0, 0.2009649046))
            make_face()
        # OneSide extrude, distance=-7.5
        extrude(amount=-7.5, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 11 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.2), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.3600000054, perimeter: 2.4000000179
            with BuildLine():
                Line((-0.3000000045, 0), (-0.3000000045, -0.6))
                Line((-0.3000000045, -0.6), (0.3000000045, -0.6))
                Line((0.3000000045, -0.6), (0.3000000045, 0))
                Line((-0.3000000045, 0), (0.3000000045, 0))
            make_face()
            # Profile area: 0.4200000098, perimeter: 2.6000000328
            with BuildLine():
                Line((0, 0.7), (0.3, 0.7))
                Line((0.3, 0.7), (0.3, 0.8000000119))
                Line((0.3, 0.8000000119), (0.3, 1.4000000119))
                Line((-0.3, 1.4000000209), (0.3, 1.4000000119))
                Line((-0.3, 0.8000000119), (-0.3, 1.4000000209))
                Line((-0.3, 0.7), (-0.3, 0.8000000119))
                Line((0, 0.7), (-0.3, 0.7))
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.ADD)
    return part.part


def model_128043_f75f37fa_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 20 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 32.657761895, perimeter: 41.447763874
            with BuildLine():
                Line((0, 12.5), (-0.200000003, 12.5))
                Line((-0.200000003, 12.5), (-1.4, 12.5))
                Line((-1.4, 12.5), (-2.3000000195, 2.6381811448))
                CenterArc((0, 0), 3.4999999775, 48.9176665381, 82.1646673467)
                Line((1.4, 12.5), (2.3, 2.6381811618))
                Line((0, 12.5), (1.4, 12.5))
            make_face()
            with BuildLine():
                CenterArc((-1.0767438566, 12.1), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.312222601, 9.3099193988), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.5266764575, 6.7689531371), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.8, 3.530466725), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1, 12.1), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.2354787443, 9.3099193988), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.4499326008, 6.7689531371), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.8, 3.530466725), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 11), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 11.8), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 10.2), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 6.65), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.3952678923, 7.4166504195), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.5045973093, 6.1212558547), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 12 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.8803434064, perimeter: 13.3856832972
            with BuildLine():
                Line((0.4581467104, -4.8834421629), (0.4581467104, -8.4165578371))
                CenterArc((0.32, -4.825), 0.15, -22.9305095847, 205.9704528122)
                Line((0.170211079, -4.8329548193), (0.170211079, -8.4670451807))
                Line((0.65, -11), (0.170211079, -8.4670451807))
                CenterArc((0.8, -11), 0.15, 180, 190.8376439617)
                Line((0.4581467104, -8.4165578371), (0.9473245891, -10.9717960028))
            make_face()
            # Profile area: 1.8803434064, perimeter: 13.3856832972
            with BuildLine():
                CenterArc((-0.32, -4.825), 0.15, -3.0399432276, 205.9704528122)
                Line((-0.4581467104, -4.8834421629), (-0.4581467104, -8.4165578371))
                Line((-0.4581467104, -8.4165578371), (-0.9473245891, -10.9717960028))
                CenterArc((-0.8, -11), 0.15, 169.1623560383, 190.8376439617)
                Line((-0.65, -11), (-0.170211079, -8.4670451807))
                Line((-0.170211079, -4.8329548193), (-0.170211079, -8.4670451807))
            make_face()
        # OneSide extrude, distance=-0.15
        extrude(amount=-0.15, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0703407697, perimeter: 0.9416177637
            with BuildLine():
                CenterArc((0.320211079, -8.4670451807), 0.15, -158.5483676785, 154.5037819055)
                Line((0.4581467104, -8.4165578371), (0.4698374989, -8.4776250895))
                Line((0.4581467104, -8.408106555), (0.4581467104, -8.4165578371))
                CenterArc((0.320211079, -8.4670451807), 0.15, 23.1365726706, 156.8634273294)
                Line((0.1806020849, -8.5219025298), (0.170211079, -8.4670451807))
            make_face()
            # Profile area: 0.0703407697, perimeter: 0.9416177637
            with BuildLine():
                CenterArc((-0.320211079, -8.4670451807), 0.15, 0, 156.8634273294)
                Line((-0.4581467104, -8.4165578371), (-0.4581467104, -8.408106555))
                Line((-0.4698374989, -8.4776250895), (-0.4581467104, -8.4165578371))
                CenterArc((-0.320211079, -8.4670451807), 0.15, -175.955414227, 154.5037819055)
                Line((-0.170211079, -8.4670451807), (-0.1806020849, -8.5219025298))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


def model_128996_42176b10_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.1964711726, perimeter: 13.4119464091
            with BuildLine():
                CenterArc((0, 0), 0.95, 90, 180)
                Line((0, -0.95), (2.85, -0.95))
                Line((2.85, 0.95), (2.85, -0.95))
                Line((0, 0.95), (2.85, 0.95))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.45, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.45
        extrude(amount=0.45)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.45, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.995, perimeter: 5.9
            with BuildLine():
                Line((-2.85, 0.95), (-2.85, -0.95))
                Line((-2.85, -0.95), (-1.8, -0.95))
                Line((-1.8, 0), (-1.8, -0.95))
                Line((-1.8, 0), (-1.8, 0.95))
                Line((-1.8, 0.95), (-2.85, 0.95))
            make_face()
        # OneSide extrude, distance=-2.8
        extrude(amount=-2.8, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(2.85, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.6361725124, perimeter: 2.8274333882
            with Locations((0, -0.95)):
                Circle(0.45)
        # OneSide extrude, distance=-2.8
        extrude(amount=-2.8, mode=Mode.SUBTRACT)
    return part.part


def model_128996_4cad12de_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.4641016151, perimeter: 6.9282032303
            with BuildLine():
                Line((0.4746932219, -1.0526156366), (1.1489384927, -0.1152114291))
                Line((1.1489384927, -0.1152114291), (0.6742452707, 0.9374042075))
                Line((0.6742452707, 0.9374042075), (-0.4746932219, 1.0526156366))
                Line((-0.4746932219, 1.0526156366), (-1.1489384927, 0.1152114291))
                Line((-1.1489384927, 0.1152114291), (-0.6742452707, -0.9374042075))
                Line((-0.6742452707, -0.9374042075), (0.4746932219, -1.0526156366))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.0106192983, perimeter: 5.0265482457
            Circle(0.8)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=-5.2
        extrude(amount=-5.2, mode=Mode.SUBTRACT)
    return part.part


def model_128996_5943e02c_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.9485571585, perimeter: 5.1961524227
            with BuildLine():
                Line((-0.1420998458, -0.8542877933), (0.6687850082, -0.550205973))
                Line((0.6687850082, -0.550205973), (0.8108848541, 0.3040818203))
                Line((0.8108848541, 0.3040818203), (0.1420998458, 0.8542877933))
                Line((0.1420998458, 0.8542877933), (-0.6687850082, 0.550205973))
                Line((-0.6687850082, 0.550205973), (-0.8108848541, -0.3040818203))
                Line((-0.8108848541, -0.3040818203), (-0.1420998458, -0.8542877933))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            Circle(0.6)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=-3.5
        extrude(amount=-3.5, mode=Mode.SUBTRACT)
    return part.part


def model_128996_65f4b609_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.2, perimeter: 10.2
            with BuildLine():
                Line((2.2405900468, -2), (5.3405900468, -2))
                Line((5.3405900468, 0), (5.3405900468, -2))
                Line((2.2405900468, 0), (5.3405900468, 0))
                Line((2.2405900468, -2), (2.2405900468, 0))
            make_face()
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(2.2405900468, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.6361725124, perimeter: 2.8274333882
            with Locations((1, 0.6)):
                Circle(0.45)
        # OneSide extrude, distance=-0.7
        extrude(amount=-0.7, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.39, perimeter: 3.2
            with BuildLine():
                Line((4.5405900468, 0.6), (4.5405900468, 0.75))
                Line((4.5405900468, 0.75), (3.2405900468, 0.75))
                Line((3.2405900468, 0.75), (3.2405900468, 0.45))
                Line((4.5405900468, 0.45), (3.2405900468, 0.45))
                Line((4.5405900468, 0.6), (4.5405900468, 0.45))
            make_face()
        # OneSide extrude, distance=-3.1
        extrude(amount=-3.1, mode=Mode.SUBTRACT)
    return part.part


def model_128996_885b41ef_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.5914761351, perimeter: 12.0448231548
            with BuildLine():
                Line((0.95, 0), (2.3, 0))
                Line((2.3, 0), (2.3, 0.5000000075))
                Line((2.3, 0.5000000075), (1.3076696802, 0.5000000075))
                CenterArc((0, 0), 1.4, 20.9248327541, 138.1503344918)
                Line((-2.3, 0.5000000075), (-1.3076696802, 0.5000000075))
                Line((-2.3, 0), (-2.3, 0.5000000075))
                Line((-0.95, 0), (-2.3, 0))
                CenterArc((0, 0), 0.95, 0, 180)
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-1.8, 1.0000000149)):
                Circle(0.25)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((1.8, 0.9999999944)):
                Circle(0.25)
        # OneSide extrude, distance=-0.9
        extrude(amount=-0.9, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((0, 1.0000000149)):
                Circle(0.2)
        # OneSide extrude, distance=-7.5
        extrude(amount=-7.5, mode=Mode.SUBTRACT)
    return part.part


def model_128996_a3d026d6_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.8, perimeter: 9.8
            with BuildLine():
                Line((2, -2.9), (0, -2.9))
                Line((2, 0), (2, -2.9))
                Line((0, 0), (2, 0))
                Line((0, -2.9), (0, 0))
            make_face()
        # OneSide extrude, distance=1.7
        extrude(amount=1.7)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.7, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.6599999948, perimeter: 6.5999999925
            with BuildLine():
                Line((-1.7, 0.5000000075), (-0.3, 0.5))
                Line((-0.3, 0.5), (-0.3, 2.4))
                Line((-0.3, 2.4), (-1.7, 2.4))
                Line((-1.7, 2.4), (-1.7, 0.5000000075))
            make_face()
        # OneSide extrude, distance=-0.6
        extrude(amount=-0.6, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.449999995, perimeter: 2.7999999888
            with BuildLine():
                Line((-0.75, 0.9), (-0.7500000112, 0))
                Line((-1.25, 0.9), (-0.75, 0.9))
                Line((-1.25, 0), (-1.25, 0.9))
                Line((-1.25, 0), (-0.7500000112, 0))
            make_face()
        # OneSide extrude, distance=-3.8
        extrude(amount=-3.8, mode=Mode.SUBTRACT)
    return part.part


def model_128996_b005b1f9_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 5.6548667765
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5419247327, perimeter: 7.2256631033
            with BuildLine():
                CenterArc((0, 0), 0.65, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2827433388, perimeter: 5.6548667765
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 5.6548667765
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


def model_128996_c8caf184_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.893030558, perimeter: 27.9601746169
            with BuildLine():
                CenterArc((0, 0), 2.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.05, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.7188940542, perimeter: 3.5173697666
            with BuildLine():
                Line((3.1, 0), (3.1, 0.5))
                Line((3.1, 0.5), (2.9000000432, 0.5))
                Line((2.9000000432, 0.5), (2.3473389189, 0.5))
                CenterArc((0, 0), 2.4, -12.1166945794, 24.1413937599)
                Line((3.1, -0.5000000075), (2.3465330822, -0.5037682943))
                Line((3.1, 0), (3.1, -0.5000000075))
            make_face()
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.ADD)

        # Sketch5 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((2.7236694594, 0.4)):
                Circle(0.2)
        # OneSide extrude, distance=-1.7
        extrude(amount=-1.7, mode=Mode.SUBTRACT)
    return part.part


def model_128996_f12458f7_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=5.6
        extrude(amount=5.6)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5.6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=0.55
        extrude(amount=0.55, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=2.8
        extrude(amount=2.8, mode=Mode.ADD)
    return part.part


MODELS = {
    "model_100801_d759cc09_0000": {"func": model_100801_d759cc09_0000, "volume": 1232.2039772932, "area": 1025.7078286283},
    "model_100804_1147d10b_0000": {"func": model_100804_1147d10b_0000, "volume": 22.0044419083, "area": 108.956456943},
    "model_101269_f084ba14_0021": {"func": model_101269_f084ba14_0021, "volume": 2396.60811, "area": 1666.1257},
    "model_101289_a540a982_0000": {"func": model_101289_a540a982_0000, "volume": 0.6020000008, "area": 4.7799999928},
    "model_102931_f0404cf4_0000": {"func": model_102931_f0404cf4_0000, "volume": 51.7213821365, "area": 200.2455937664},
    "model_103552_c3a389ed_0001": {"func": model_103552_c3a389ed_0001, "volume": 212.6544293429, "area": 408.8011792087},
    "model_104524_f829aab2_0000": {"func": model_104524_f829aab2_0000, "volume": 26.7963269902, "area": 71.5517945499},
    "model_104524_f829aab2_0002": {"func": model_104524_f829aab2_0002, "volume": 82.8178648587, "area": 134.0933614313},
    "model_104542_2e4f8127_0000": {"func": model_104542_2e4f8127_0000, "volume": 0.1656742886, "area": 2.5178465219},
    "model_104641_2cd02839_0000": {"func": model_104641_2cd02839_0000, "volume": 22.7654029554, "area": 233.5178363379},
    "model_104740_d3638bbe_0004": {"func": model_104740_d3638bbe_0004, "volume": 1.6436964913, "area": 8.8159805097},
    "model_105267_6e427767_0000": {"func": model_105267_6e427767_0000, "volume": 0.8561478117, "area": 8.1249440003},
    "model_105278_909f3813_0001": {"func": model_105278_909f3813_0001, "volume": 92.329865155, "area": 258.1288491746},
    "model_106235_14bd7a91_0000": {"func": model_106235_14bd7a91_0000, "volume": 0.84141858, "area": 52.5305800206},
    "model_106645_558b1d4b_0000": {"func": model_106645_558b1d4b_0000, "volume": 836.3561240184, "area": 1393.0676313207},
    "model_107055_0500fdd1_0028": {"func": model_107055_0500fdd1_0028, "volume": 0.7217687454, "area": 10.0371884178},
    "model_107743_e0c2c81f_0000": {"func": model_107743_e0c2c81f_0000, "volume": 2826833044.2033786774, "area": 35533554.7317677587},
    "model_107918_8e0402a9_0000": {"func": model_107918_8e0402a9_0000, "volume": 10.73984, "area": 72.732},
    "model_108008_db1cf496_0001": {"func": model_108008_db1cf496_0001, "volume": 1.3249726145, "area": 11.2818005201},
    "model_109543_c2418151_0000": {"func": model_109543_c2418151_0000, "volume": 34.3883617977, "area": 341.5656327339},
    "model_110518_142d2e0a_0000": {"func": model_110518_142d2e0a_0000, "volume": 0.0186904047, "area": 0.4824775419},
    "model_110779_4f244e41_0000": {"func": model_110779_4f244e41_0000, "volume": 197.1949445058, "area": 214.7005505542},
    "model_110875_e9e6c22e_0003": {"func": model_110875_e9e6c22e_0003, "volume": 68.7386115335, "area": 142.1207405044},
    "model_111228_fcc98116_0000": {"func": model_111228_fcc98116_0000, "volume": 5.5558329515, "area": 32.6072964332},
    "model_111257_05ceda77_0002": {"func": model_111257_05ceda77_0002, "volume": 39550771.3663029224, "area": 3313075.71793854},
    "model_112009_7c523f63_0000": {"func": model_112009_7c523f63_0000, "volume": 0.9150365197, "area": 14.0246277997},
    "model_112633_1a74caa7_0000": {"func": model_112633_1a74caa7_0000, "volume": 267.0353755551, "area": 257.6105975944},
    "model_113190_188366f8_0001": {"func": model_113190_188366f8_0001, "volume": 31.9682577943, "area": 228.1542394761},
    "model_113191_87565693_0002": {"func": model_113191_87565693_0002, "volume": 1.1003524262, "area": 16.7937005791},
    "model_113341_3d297c22_0000": {"func": model_113341_3d297c22_0000, "volume": 20.0276531666, "area": 89.5353906273},
    "model_113364_10837c89_0002": {"func": model_113364_10837c89_0002, "volume": 18.4154427698, "area": 220.6320929198},
    "model_113856_e7484fa7_0000": {"func": model_113856_e7484fa7_0000, "volume": 63.8780034254, "area": 96.0322042349},
    "model_114187_69d0ae36_0000": {"func": model_114187_69d0ae36_0000, "volume": 120.7273219918, "area": 282.9822971503},
    "model_115179_e3a49444_0001": {"func": model_115179_e3a49444_0001, "volume": 1.6428840972, "area": 11.0607623351},
    "model_115406_290de6d9_0000": {"func": model_115406_290de6d9_0000, "volume": 4.4642345767, "area": 32.4504529967},
    "model_115406_9f5685a8_0000": {"func": model_115406_9f5685a8_0000, "volume": 4.2807812737, "area": 32.5022892755},
    "model_115406_ffbeceb3_0000": {"func": model_115406_ffbeceb3_0000, "volume": 11.9330813803, "area": 100.5534955287},
    "model_115524_f214596c_0000": {"func": model_115524_f214596c_0000, "volume": 40, "area": 178},
    "model_116179_7583706e_0001": {"func": model_116179_7583706e_0001, "volume": 28.4273208254, "area": 75.6433576744},
    "model_116247_2d150add_0003": {"func": model_116247_2d150add_0003, "volume": 17, "area": 70},
    "model_116248_9325a5f7_0001": {"func": model_116248_9325a5f7_0001, "volume": 29.8284644285, "area": 128.451746197},
    "model_116267_5a83e78a_0000": {"func": model_116267_5a83e78a_0000, "volume": 6.5554419025, "area": 37.8024459544},
    "model_118113_98db6047_0000": {"func": model_118113_98db6047_0000, "volume": 210.5999997184, "area": 244.2000001743},
    "model_118116_bcc4d1ef_0002": {"func": model_118116_bcc4d1ef_0002, "volume": 30.5784645328, "area": 129.8017463848},
    "model_118433_f14b7df9_0000": {"func": model_118433_f14b7df9_0000, "volume": 419.9594729288, "area": 472.1603384438},
    "model_118436_06c78560_0000": {"func": model_118436_06c78560_0000, "volume": 9865.012528, "area": 3083.8648},
    "model_118544_ce1870aa_0001": {"func": model_118544_ce1870aa_0001, "volume": 35.248500865, "area": 83.471335534},
    "model_118621_276dd2d4_0000": {"func": model_118621_276dd2d4_0000, "volume": 306.2809508826, "area": 311.2752728119},
    "model_119027_cf658ca8_0000": {"func": model_119027_cf658ca8_0000, "volume": 49.5680523766, "area": 220.3791947215},
    "model_119895_6c95f34d_0000": {"func": model_119895_6c95f34d_0000, "volume": 120.5415608622, "area": 475.8674110811},
    "model_119904_87c09b29_0000": {"func": model_119904_87c09b29_0000, "volume": 564.7587060164, "area": 10415.4116089964},
    "model_119917_fc3018e0_0000": {"func": model_119917_fc3018e0_0000, "volume": 23328.5221342091, "area": 10545.225790214},
    "model_120462_13aff06e_0000": {"func": model_120462_13aff06e_0000, "volume": 3.0230707681, "area": 28.6419795404},
    "model_121267_6afe53d3_0000": {"func": model_121267_6afe53d3_0000, "volume": 114.0295206449, "area": 177.4455208077},
    "model_121371_3af239ff_0002": {"func": model_121371_3af239ff_0002, "volume": 28.427320786, "area": 75.6433575126},
    "model_121467_899f0850_0003": {"func": model_121467_899f0850_0003, "volume": 6.5342917353, "area": 32.2787595947},
    "model_121703_69c4a5ac_0001": {"func": model_121703_69c4a5ac_0001, "volume": 1079.9224746715, "area": 589.0486225481},
    "model_121860_63471748_0000": {"func": model_121860_63471748_0000, "volume": 68.4393498927, "area": 193.1306395185},
    "model_121869_a29a7922_0000": {"func": model_121869_a29a7922_0000, "volume": 1.4894559386, "area": 13.3496727783},
    "model_123863_32847f10_0000": {"func": model_123863_32847f10_0000, "volume": 1540.2009126148, "area": 936.5890486225},
    "model_123927_98bb427e_0000": {"func": model_123927_98bb427e_0000, "volume": 119.0223792739, "area": 427.5707601536},
    "model_124497_5c00f42d_0012": {"func": model_124497_5c00f42d_0012, "volume": 171.1357447078, "area": 299.7301340615},
    "model_124815_b75fa9f5_0000": {"func": model_124815_b75fa9f5_0000, "volume": 19.313708499, "area": 61.2548339959},
    "model_127023_9a974c7e_0000": {"func": model_127023_9a974c7e_0000, "volume": 125.3682000846, "area": 143.8798728625},
    "model_127747_293b9c11_0000": {"func": model_127747_293b9c11_0000, "volume": 125.3511946711, "area": 176.6579644737},
    "model_128043_31dd1a0f_0000": {"func": model_128043_31dd1a0f_0000, "volume": 0.3188716543, "area": 4.7280969437},
    "model_128043_9f8cd69e_0000": {"func": model_128043_9f8cd69e_0000, "volume": 0.816931428, "area": 19.132876179},
    "model_128043_f75f37fa_0000": {"func": model_128043_f75f37fa_0000, "volume": 9.2121233258, "area": 81.7666801918},
    "model_128996_42176b10_0000": {"func": model_128996_42176b10_0000, "volume": 6.8086808897, "area": 33.9897782622},
    "model_128996_4cad12de_0000": {"func": model_128996_4cad12de_0000, "volume": 2.6925431899, "area": 17.239306891},
    "model_128996_5943e02c_0000": {"func": model_128996_5943e02c_0000, "volume": 1.8224316244, "area": 12.6200437485},
    "model_128996_65f4b609_0000": {"func": model_128996_65f4b609_0000, "volume": 6.2146792414, "area": 32.2392033718},
    "model_128996_885b41ef_0000": {"func": model_128996_885b41ef_0000, "volume": 4.929895103, "area": 30.3756327209},
    "model_128996_a3d026d6_0000": {"func": model_128996_a3d026d6_0000, "volume": 6.9590000177, "area": 36.540000038},
    "model_128996_b005b1f9_0000": {"func": model_128996_b005b1f9_0000, "volume": 0.9071348787, "area": 14.0586271248},
    "model_128996_c8caf184_0000": {"func": model_128996_c8caf184_0000, "volume": 4.3636394674, "area": 35.7955862309},
    "model_128996_f12458f7_0000": {"func": model_128996_f12458f7_0000, "volume": 2.2411336593, "area": 16.3834056885},
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
