"""Batch 008 - passing/05_8to10ops
68 models bundled from Fusion360 Gallery reconstructions.
"""

from build123d import *
from build123d import Edge, BuildLine
from collections import Counter
from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
from OCP.Geom import Geom_BSplineCurve
from OCP.TColStd import TColStd_Array1OfReal, TColStd_Array1OfInteger
from OCP.TColgp import TColgp_Array1OfPnt
from OCP.gp import gp_Pnt


def model_43928_6ca53538_0014():
    """Model: Drive spindle crossmember roller v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0804247719, perimeter: 1.0053096491
            Circle(0.16)
        # OneSide extrude, distance=0.48
        extrude(amount=0.48)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.48, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.013273229, perimeter: 0.408407045
            Circle(0.065)
        # OneSide extrude, distance=-0.95
        extrude(amount=-0.95, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.006832964, perimeter: 0.9110618695
            with BuildLine():
                CenterArc((0, 0), 0.08, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.065, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.39
        extrude(amount=-0.39, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.48, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0028604081, perimeter: 0.2524165232
            with BuildLine():
                Line((-0.0632455532, 0.015), (-0.1592953232, 0.015))
                CenterArc((0, 0), 0.16, 174.6206210089, 10.7587579822)
                Line((-0.1592953232, -0.015), (-0.0632455532, -0.015))
                CenterArc((0, 0), 0.065, 166.6576362029, 26.6847275942)
            make_face()
            # Profile area: 0.0004080324, perimeter: 0.0881862638
            with BuildLine():
                CenterArc((0, 0), 0.16, -5.3793789911, 10.7587579822)
                Line((0.1592953232, -0.015), (0.1733663951, -0.015))
                Line((0.1733663951, -0.015), (0.1733663951, 0.015))
                Line((0.1733663951, 0.015), (0.1592953232, 0.015))
            make_face()
            # Profile area: 0.0028604081, perimeter: 0.2524165232
            with BuildLine():
                Line((0.0632455532, -0.015), (0.1592953232, -0.015))
                CenterArc((0, 0), 0.16, -5.3793789911, 10.7587579822)
                Line((0.1592953232, 0.015), (0.0632455532, 0.015))
                CenterArc((0, 0), 0.065, -13.3423637971, 26.6847275942)
            make_face()
            # Profile area: 0.0004080324, perimeter: 0.0881862638
            with BuildLine():
                Line((-0.1592953232, 0.015), (-0.1733663951, 0.015))
                Line((-0.1733663951, 0.015), (-0.1733663951, -0.015))
                Line((-0.1733663951, -0.015), (-0.1592953232, -0.015))
                CenterArc((0, 0), 0.16, 174.6206210089, 10.7587579822)
            make_face()
            # Profile area: 0.0038651027, perimeter: 0.3135279392
            with BuildLine():
                CenterArc((0, 0), 0.065, 166.6576362029, 26.6847275942)
                Line((-0.0632455532, -0.015), (0.0632455532, -0.015))
                CenterArc((0, 0), 0.065, -13.3423637971, 26.6847275942)
                Line((0.0632455532, 0.015), (-0.0632455532, 0.015))
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)
    return part.part


def model_43928_6ca53538_0018():
    """Model: Drag Lock Guide v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 10 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0225, perimeter: 0.7684658438
            with BuildLine():
                Line((0, -0.075), (0, 0.075))
                Line((0.3, 0), (0, -0.075))
                Line((0, 0.075), (0.3, 0))
            make_face()
            # Profile area: 0.0225, perimeter: 1.2184658438
            with BuildLine():
                Line((0.6, -0.075), (0, -0.075))
                Line((0.3, 0), (0.6, -0.075))
                Line((0.3, 0), (0, -0.075))
            make_face()
            # Profile area: 0.0225, perimeter: 1.2184658438
            with BuildLine():
                Line((0, 0.075), (0.3, 0))
                Line((0.6, 0.075), (0.3, 0))
                Line((0, 0.075), (0.6, 0.075))
            make_face()
            # Profile area: 0.0225, perimeter: 0.7684658438
            with BuildLine():
                Line((0.3, 0), (0.6, -0.075))
                Line((0.6, 0.075), (0.6, -0.075))
                Line((0.6, 0.075), (0.3, 0))
            make_face()
        # OneSide extrude, distance=0.025
        extrude(amount=0.025)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 16 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.6, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0329916448, perimeter: 2.6893315868
            with BuildLine():
                Line((0, 0.075), (-0.025, 0.075))
                Line((0, 0.1), (0, 0.075))
                Line((-1.3196657934, 0.1), (0, 0.1))
                Line((-1.3196657934, 0.075), (-1.3196657934, 0.1))
                Line((-0.025, 0.075), (-1.3196657934, 0.075))
            make_face()
            # Profile area: 0.0329916448, perimeter: 2.6893315868
            with BuildLine():
                Line((-1.3196657934, -0.075), (-1.3196657934, -0.1))
                Line((-1.3196657934, -0.1), (0, -0.1))
                Line((0, -0.1), (0, -0.075))
                Line((0, -0.075), (-0.025, -0.075))
                Line((-0.025, -0.075), (-1.3196657934, -0.075))
            make_face()
        # OneSide extrude, distance=-0.9
        extrude(amount=-0.9, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 14 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7744484958, perimeter: 6.0955411239
            with BuildLine():
                CenterArc((0.7000601181, 1.5251495366), 1.1, -148.4546340104, 25.4709127806)
                CenterArc((0.074, 0.5605), 0.05, -38.0820124363, 95.0992790963)
                Line((0.1133564348, 0.5296605604), (-0.04635652, 0.325839331))
                CenterArc((-0.007, 0.295), 0.05, 141.9181457124, 49.1964518909)
                Line((0, 0), (-0.0560621791, 0.2853614015))
                Line((0, 0), (0.3, 0))
                Line((0.3, 0), (0.3, 1.3196657934))
                Line((0.3, 1.3196657934), (-0.6, 1.3196657934))
                Line((-0.6, 1.3196657934), (-0.6, 0))
                Line((-0.6, 0), (-0.3280197418, 0.9374321356))
                CenterArc((-0.28, 0.9235), 0.05, 31.5453672304, 132.2754185608)
            make_face()
        # OneSide extrude, distance=-1.2
        extrude(amount=-1.2, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0176714587, perimeter: 0.471238898
            with Locations((-0.272, 0.18)):
                Circle(0.075)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)
    return part.part


def model_43928_6ca53538_0029():
    """Model: Strut v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)

        # Sketch2 -> Extrude2 (Join)
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

        # Sketch3 -> Extrude3 (Join)
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

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 5.06), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1194590607, perimeter: 1.2252211349
            Circle(0.195)
        # OneSide extrude, distance=0.18
        extrude(amount=0.18, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 5.24), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0754767635, perimeter: 0.9738937226
            Circle(0.155)
        # OneSide extrude, distance=1.01
        extrude(amount=1.01, mode=Mode.ADD)
    return part.part


def model_43928_6ca53538_0033():
    """Model: line guide bushing v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.3525652355, perimeter: 2.1048670779
            Circle(0.335)
        # OneSide extrude, distance=0.325
        extrude(amount=0.325)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.325), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.2016117085, perimeter: 4.7438049069
            with BuildLine():
                CenterArc((0, 0), 0.42, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.335, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.3525652355, perimeter: 2.1048670779
            Circle(0.335)
        # OneSide extrude, distance=0.125
        extrude(amount=0.125, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.45), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=0.08
        extrude(amount=0.08, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.53), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.101787602, perimeter: 1.1309733553
            Circle(0.18)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


def model_43932_4bfdfe7b_0008():
    """Model: 12 v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 995.3822163634, perimeter: 111.8406984678
            Circle(17.8)
        # Symmetric extrude, each_side=7.2
        extrude(amount=7.2, both=True)

        # Sketch4 -> Extrude2 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 37 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 17.9795630531, perimeter: 20.745057321
            with BuildLine():
                Line((-1, 11.1), (-1.1, 11.1))
                Line((1, 11.1), (-1, 11.1))
                Line((1.1, 11.1), (1, 11.1))
                Line((1.1, 19.2725286605), (1.1, 11.1))
                Line((-1.1, 19.2725286605), (1.1, 19.2725286605))
                Line((-1.1, 11.1), (-1.1, 19.2725286605))
            make_face()
        # Symmetric extrude, each_side=3.3
        extrude(amount=3.3, both=True, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 37 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 15.762503669, perimeter: 18.72954879
            with BuildLine():
                Line((1, -11.1), (-1, -11.1))
                Line((-1, -11.1), (-1.1, -11.1))
                Line((-1.1, -11.1), (-1.1, -18.264774395))
                Line((-1.1, -18.264774395), (1.1, -18.264774395))
                Line((1.1, -18.264774395), (1.1, -11.1))
                Line((1.1, -11.1), (1, -11.1))
            make_face()
        # Symmetric extrude, each_side=3.3
        extrude(amount=3.3, both=True, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 37 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 87.9415926536, perimeter: 50.6831853072
            with BuildLine():
                CenterArc((-1, 10.1), 1, 90, 90)
                Line((-2, 10.1), (-2, -10.1))
                CenterArc((-1, -10.1), 1, 180, 90)
                Line((1, -11.1), (-1, -11.1))
                CenterArc((1, -10.1), 1, -90, 90)
                Line((2, -10.1), (2, 10.1))
                CenterArc((1, 10.1), 1, 0, 90)
                Line((1, 11.1), (-1, 11.1))
            make_face()
        # Symmetric extrude, each_side=4.4
        extrude(amount=4.4, both=True, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 7.2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            Circle(0.75)
        # OneSide extrude, distance=-50
        extrude(amount=-50, mode=Mode.SUBTRACT)
    return part.part


def model_43932_4bfdfe7b_0009():
    """Model: 2 v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 84.9486653531, perimeter: 32.6725635973
            Circle(5.2)
        # OneSide extrude, distance=3.6
        extrude(amount=3.6)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3.6), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 78.5398163397, perimeter: 31.4159265359
            Circle(5)
        # OneSide extrude, distance=-7.5
        extrude(amount=-7.5, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3.6), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 17.1216799621, perimeter: 68.4867198483
            with BuildLine():
                CenterArc((0, 0), 5.7, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 5.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-2.8
        extrude(amount=-2.8, mode=Mode.ADD)

        # Sketch5 -> Extrude4 (Join)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((0, -1.1)):
                Circle(0.3)
        # Symmetric extrude, each_side=6.9
        extrude(amount=6.9, both=True, mode=Mode.ADD)

        # Sketch6 -> Extrude5 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 78.5398163397, perimeter: 31.4159265359
            Circle(5)
        # OneSide extrude, distance=-11.5
        extrude(amount=-11.5, mode=Mode.SUBTRACT)
    return part.part


def model_43934_912ff891_0000():
    """Model: Cylinder Piping Connector v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1590431281, perimeter: 1.4137166941
            Circle(0.225)
        # Symmetric extrude, each_side=0.75
        extrude(amount=0.75, both=True)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.3436116965, perimeter: 3.926990817
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.225, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.25
        extrude(amount=0.25, both=True, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.75), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0373064128, perimeter: 2.9845130209
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.225, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.75), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0373064128, perimeter: 2.9845130209
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.225, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4, mode=Mode.ADD)
    return part.part


def model_43934_912ff891_0001():
    """Model: Lover Eccentric Trap v1 v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.566869336, perimeter: 9.6535390627
            with BuildLine():
                CenterArc((0, 0), 1.6, 0, 180)
                Line((-1.25, 0), (-1.6, 0))
                CenterArc((0, 0), 1.25, 0, 180)
                Line((1.25, 0), (1.6, 0))
            make_face()
        # Symmetric extrude, each_side=0.225
        extrude(amount=0.225, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.5537056486, perimeter: 7.6827427546
            with BuildLine():
                CenterArc((0, 0), 1.25, 0, 180)
                Line((-1.1000000164, 0), (-1.25, 0))
                CenterArc((0, 0), 1.1000000164, 0, 180)
                Line((1.25, 0), (1.1000000164, 0))
            make_face()
        # Symmetric extrude, each_side=0.075
        extrude(amount=0.075, both=True, mode=Mode.ADD)

        # Sketch6 -> Extrude7 (Join)
        # Sketch on XY construction plane
        # Sketch has 13 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.5, perimeter: 3
            with BuildLine():
                Line((1.75, 1), (1.75, 0))
                Line((1.25, 1), (1.75, 1))
                Line((1.25, 0), (1.25, 1))
                Line((1.75, 0), (1.25, 0))
            make_face()
            # Profile area: 0.5, perimeter: 3
            with BuildLine():
                Line((-1.25, 0), (-1.25, 1))
                Line((-1.25, 1), (-1.75, 1))
                Line((-1.75, 1), (-1.75, 0))
                Line((-1.75, 0), (-1.25, 0))
            make_face()
        # Symmetric extrude, each_side=0.2
        extrude(amount=0.2, both=True, mode=Mode.ADD)

        # Sketch7 -> Extrude8 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-1.5, 0)):
                Circle(0.15)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((1.5, 0)):
                Circle(0.15)
        # OneSide extrude, distance=-1.8
        extrude(amount=-1.8, mode=Mode.SUBTRACT)
    return part.part


def model_43934_912ff891_0021():
    """Model: Crosshead v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 26 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.7213915589, perimeter: 4.2386708919
            with BuildLine():
                CenterArc((0, 0), 0.7810249676, 140.1944289077, 79.6111421845)
                Line((-0.6, 0.875), (-0.6, 0.5))
                Line((-0.6, 0.875), (-0.8212033853, 0.875))
                CenterArc((0, 0), 1.2, 133.1834217962, 93.6331564077)
                Line((-0.6, -0.875), (-0.8212033853, -0.875))
                Line((-0.6, -0.5), (-0.6, -0.875))
            make_face()
        # Symmetric extrude, each_side=0.8
        extrude(amount=0.8, both=True)

        # Sketch1 -> Extrude5 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 26 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.7213915589, perimeter: 4.2386708919
            with BuildLine():
                Line((0.6, 0.5), (0.6, 0.875))
                CenterArc((0, 0), 0.7810249676, -39.8055710923, 79.6111421845)
                Line((0.6, -0.875), (0.6, -0.5))
                Line((0.6, -0.875), (0.8212033853, -0.875))
                CenterArc((0, 0), 1.2, -46.8165782038, 93.6331564077)
                Line((0.6, 0.875), (0.8212033853, 0.875))
            make_face()
        # Symmetric extrude, each_side=0.8
        extrude(amount=0.8, both=True)

        # Sketch1 -> Extrude6 (Join)
        # Sketch on XY construction plane
        # Sketch has 26 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY) as sk:
            # Profile area: 0.1237903485, perimeter: 2.0852158793
            with BuildLine():
                Line((0.6, -0.5), (0.6, 0.5))
                CenterArc((0, 0), 0.7810249676, -39.8055710923, 79.6111421845)
            make_face()
            # Profile area: 0.1237903485, perimeter: 2.0852158793
            with BuildLine():
                Line((-0.6, 0.5), (-0.6, -0.5))
                CenterArc((0, 0), 0.7810249676, 140.1944289077, 79.6111421845)
            make_face()
            # Profile area: 1.2, perimeter: 4.4
            with BuildLine():
                Line((-0.6, 0.5), (0.6, 0.5))
                Line((-0.6, 0.5), (-0.6, -0.5))
                Line((-0.6, -0.5), (0.6, -0.5))
                Line((0.6, -0.5), (0.6, 0.5))
            make_face()
        # TwoSides extrude, along=0.6, against=-0.8
        extrude(amount=0.6, mode=Mode.ADD)
        extrude(sk.sketch, amount=-0.8, mode=Mode.ADD)

        # Sketch4 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -0.5, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((0, -0.2)):
                Circle(0.3)
        # OneSide extrude, distance=-2.7
        extrude(amount=-2.7, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude8 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.6), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.7088218425, perimeter: 2.9845130209
            Circle(0.475)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch6 -> Extrude9 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.9), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


def model_43934_912ff891_0026():
    """Model: Steam Chest Slide Valve Rod v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0549778714, perimeter: 2.1991148575
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=5
        extrude(amount=5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on YZ construction plane
        # Sketch has 23 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.9499743807, perimeter: 5.0703537556
            with BuildLine():
                Line((-6.2585786438, 0.2585786438), (-6.4, 0.4))
                Line((-6.4, 0.4), (-7.2, 0.4))
                CenterArc((-7.2, 0), 0.4, 90, 180)
                Line((-7.2, -0.4), (-6.4, -0.4))
                Line((-6.2585786438, -0.2585786438), (-6.4, -0.4))
                CenterArc((-6.1171572875, -0.4), 0.2, 90, 45)
                Line((-6.1171572875, 0.2), (-6.1171572875, -0.2))
                CenterArc((-6.1171572875, 0.4), 0.2, -135, 45)
            make_face()
            with BuildLine():
                CenterArc((-7.2, 0), 0.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.3
        extrude(amount=0.3, both=True, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.18, perimeter: 1.8
            with BuildLine():
                Line((-0.15, 6.6), (-0.15, 7.2))
                Line((0.15, 6.6), (-0.15, 6.6))
                Line((0.15, 7.2), (0.15, 6.6))
                Line((0.15, 7.2), (-0.15, 7.2))
            make_face()
            # Profile area: 0.2032230982, perimeter: 1.9548206544
            with BuildLine():
                Line((0.15, 7.2), (-0.15, 7.2))
                Line((0.15, 7.8774103272), (0.15, 7.2))
                Line((-0.15, 7.8774103272), (0.15, 7.8774103272))
                Line((-0.15, 7.2), (-0.15, 7.8774103272))
            make_face()
        # OneSide extrude, distance=-1.2
        extrude(amount=-1.2, mode=Mode.SUBTRACT)
    return part.part


def model_43934_912ff891_0028():
    """Model: Steam Chest Slide Valve v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.4, perimeter: 6.4
            with BuildLine():
                Line((1, -0.6), (1, 0.6))
                Line((1, 0.6), (-1, 0.6))
                Line((-1, 0.6), (-1, -0.6))
                Line((-1, -0.6), (1, -0.6))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.8, perimeter: 5.6
            with BuildLine():
                Line((-0.9, 0.5), (-0.9, -0.5))
                Line((-0.9, -0.5), (0.9, -0.5))
                Line((0.9, -0.5), (0.9, 0.5))
                Line((0.9, 0.5), (-0.9, 0.5))
            make_face()
        # OneSide extrude, distance=1.1
        extrude(amount=1.1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1590431281, perimeter: 1.4137166941
            with Locations((0, 0.8)):
                Circle(0.225)
        # OneSide extrude, distance=-2.2
        extrude(amount=-2.2, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 18 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.8056637187, perimeter: 3.6566370793
            with BuildLine():
                CenterArc((0.5, -0.1000000045), 0.2, -90, 90)
                Line((0.7, -0.1000000045), (0.7, 0.1000000045))
                CenterArc((0.5, 0.1000000045), 0.2, 0, 90)
                Line((0.5, 0.3000000045), (-0.5, 0.3000000045))
                CenterArc((-0.5, 0.1000000045), 0.2, 90, 90)
                Line((-0.7, 0.1000000045), (-0.7, -0.1000000045))
                CenterArc((-0.5, -0.1000000045), 0.2, -180, 90)
                Line((-0.5, -0.3000000045), (0.5, -0.3000000045))
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)
    return part.part


def model_44021_f141414b_0006():
    """Model: Filling Tray v7"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.9957131563, perimeter: 29.0597320457
            with BuildLine():
                CenterArc((0, 0), 2.45, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 111.1425900968, perimeter: 61.3938040026
            with BuildLine():
                Line((-9.8, 5), (3.2, 5))
                Line((-9.8, -5), (-9.8, 5))
                Line((3.2, -5), (-9.8, -5))
                Line((3.2, 5), (3.2, -5))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.45, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 13.4399999177, perimeter: 89.6000000133
            with BuildLine():
                Line((-9.8, 5), (3.2, 5))
                Line((-9.8, -5), (-9.8, 5))
                Line((3.2, -5), (-9.8, -5))
                Line((3.2, 5), (3.2, -5))
            make_face()
            with BuildLine():
                Line((2.9, 4.7000000133), (2.9, -4.7))
                Line((2.9, -4.7), (-9.5, -4.7))
                Line((-9.5, -4.7), (-9.5, 4.7))
                Line((-9.5, 4.7), (2.9, 4.7000000133))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.2953261325, perimeter: 26.2322986575
            with BuildLine():
                CenterArc((0, 0), 2.175, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.ADD)
    return part.part


def model_44221_25c62f03_0000():
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
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 17.2306474447, perimeter: 32.2669181874
            with BuildLine():
                Line((-5.4864000678, 0.6096000075), (-5.4864000678, 0))
                _nurbs_edge([(-5.4864000678, 0), (-5.1974576986, -0.0069587415), (-4.6233097514, -0.0171820357), (-3.7732981071, -0.0214344461), (-2.6625335749, -0.0047778528), (-1.3133228558, 0.0544123068), (-0.0064734818, 0.1537513775), (1.2531481222, 0.2954379649), (2.4587249348, 0.4817648803), (3.6014327553, 0.7147679146), (4.6703079567, 0.9955722412), (5.6528066838, 1.3242760093), (6.5360510829, 1.7004476875), (7.3082839129, 2.1232767272), (7.9602790923, 2.5917262295), (8.4879845826, 3.1044146454), (8.8111605621, 3.5487593823), (8.9987353558, 3.9007487922), (9.0996082526, 4.1436722848), (9.144000113, 4.2672000527)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9333333333, 1, 1, 1, 1, 1, 1], 5)
                Line((6.0960000753, 4.2672000527), (9.144000113, 4.2672000527))
                _nurbs_edge([(-5.4864000678, 0.6096000075), (-5.2427469414, 0.5924124946), (-4.7601477876, 0.5634115174), (-4.0503702856, 0.5360321729), (-3.1324485977, 0.5320052277), (-2.0340540882, 0.5824041748), (-0.9872930446, 0.6896590533), (0.004315223, 0.8546211229), (0.9366237609, 1.07664735), (1.8052034287, 1.3526782472), (2.6059333683, 1.6757045507), (3.3354305978, 2.0343016554), (3.9908045598, 2.4150935654), (4.5698093227, 2.8045637187), (5.0710129302, 3.1908449445), (5.4944801239, 3.5659164651), (5.7723016879, 3.8542372267), (5.9471062519, 4.0634344964), (6.0488365755, 4.1997956403), (6.0960000753, 4.2672000527)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9333333333, 1, 1, 1, 1, 1, 1], 5)
            make_face()
        # OneSide extrude, distance=2.4384
        extrude(amount=2.4384)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.7161216919, perimeter: 8.5344001055
            with BuildLine():
                Line((0.6096000075, -1.2192000151), (0.6096000075, -4.2672000527))
                Line((0.6096000075, -4.2672000527), (1.8288000226, -4.2672000527))
                Line((1.8288000226, -4.2672000527), (1.8288000226, -1.2192000151))
                Line((1.8288000226, -1.2192000151), (0.6096000075, -1.2192000151))
            make_face()
        # OneSide extrude, distance=3.048
        extrude(amount=3.048, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude4 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 105.0708654628, perimeter: 36.3367504901
            with Locations((-7.3152000904, -24.3840003014)):
                Circle(5.7831734564)
        # OneSide extrude, distance=1.2192
        extrude(amount=1.2192)

        # Sketch7 -> Extrude5 (NewBody)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 1.2192, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.3349081214, perimeter: 5.4167629451
            with Locations((14.0208001733, 16.4592002034)):
                Circle(0.8621045983)
        # OneSide extrude, distance=6.7056
        extrude(amount=6.7056)
    return part.part


def model_44328_8b922c11_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 18 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 110.3656538338, perimeter: 62.9277234403
            with BuildLine():
                CenterArc((0, 0), 4, 41.0976110564, 78.9023889436)
                Line((-2, 3.4641016151), (1, 2.5))
                Line((1, 2.5), (3, 0))
                Line((3, 0), (1, -2.5))
                Line((1, -2.5), (-2.3132153441, -3.2632858857))
                CenterArc((0, 0), 4, -125.331331722, 76.7409538313)
                Line((18.7129422276, -3), (2.6457513111, -3))
                CenterArc((18.7129422276, -1.5), 1.5, -90, 90)
                Line((20.2129422276, 1.1293753018), (20.2129422276, -1.5))
                CenterArc((18.7129422276, 1.1293753018), 1.5, 0, 90)
                Line((3.0143632035, 2.6293753018), (18.7129422276, 2.6293753018))
            make_face()
        # OneSide extrude, distance=6.5
        extrude(amount=6.5)

        # Sketch4 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(6.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 10.4948537803, perimeter: 11.4839985261
            with Locations((18, 0)):
                Circle(1.8277351319)
        # OneSide extrude, distance=-8
        extrude(amount=-8, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(6.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 86.216856466, perimeter: 71.9714488154
            with BuildLine():
                Line((19.9917865371, -1.5), (19.9917865371, 1.1293753018))
                CenterArc((18.7129422276, 1.1293753018), 1.2788443095, 0, 90)
                Line((18.7129422276, 2.4082196113), (2.9120684434, 2.4082196113))
                CenterArc((0, 0), 3.7788443095, 39.590035618, 72.2993716443)
                Line((-1.4088145253, 3.5064092671), (1.131081484, 2.6901699855))
                Line((1.131081484, 2.6901699855), (3.2832174724, 0))
                Line((3.2832174724, 0), (1.1246276289, -2.6982373044))
                Line((1.1246276289, -2.6982373044), (-1.7349614178, -3.3570184977))
                CenterArc((0, 0), 3.7788443095, -117.3306516334, 69.9922608875)
                Line((2.5607984339, -2.7788443095), (18.7129422276, -2.7788443095))
                CenterArc((18.7129422276, -1.5), 1.2788443095, -90, 90)
            make_face()
            with BuildLine():
                CenterArc((18, 0), 1.8277351319, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)
    return part.part


def model_44363_b199af8c_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch22 -> Extrude5 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))) as sk:
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((25, 0)):
                Circle(0.5)
        # TwoSides extrude, along=36.5, against=-6.5
        extrude(amount=36.5)
        extrude(sk.sketch, amount=-6.5)
    return part.part


def model_44392_ced313da_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch12 -> Extrude7 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.9000000566, perimeter: 5.8000000864
            with BuildLine():
                Line((-3.4000000507, 0.3000000045), (-3.4000000507, 2.2000000328))
                Line((-3.4000000507, 2.2000000328), (-4.4000000656, 2.2000000328))
                Line((-4.4000000656, 2.2000000328), (-4.4000000656, 0.3000000045))
                Line((-4.4000000656, 0.3000000045), (-3.4000000507, 0.3000000045))
            make_face()
        # OneSide extrude, distance=-0.01
        extrude(amount=-0.01)

        # Sketch13 -> Extrude8 (Join)
        # Sketch on BRepFace
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.01, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.1570796374, perimeter: 1.4049629671
            with Locations((3.9000000581, 1.1000000164)):
                Circle(0.2236068011)
            # Profile area: 0.0315562673, perimeter: 0.6297203745
            with Locations((3.7000000551, 1.6000000238)):
                Circle(0.1002231104)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)
    return part.part


def model_44399_86308373_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 10 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 62.2853981634, perimeter: 34.1415926536
            with BuildLine():
                CenterArc((0.5, 0.5), 0.5, 180, 90)
                Line((0.5, 0), (12, 0))
                CenterArc((12, 0.5), 0.5, -90, 90)
                Line((12.5, 0.5), (12.5, 4.5))
                CenterArc((12, 4.5), 0.5, 0, 90)
                Line((12, 5), (0.5, 5))
                CenterArc((0.5, 4.5), 0.5, 90, 90)
                Line((0, 4.5), (0, 0.5))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 12 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 38.6308280335, perimeter: 27.465957696
            with BuildLine():
                CenterArc((1.3402587287, 3.8035085602), 0.5, 90, 90)
                Line((0.8402587287, 1.0834325585), (0.8402587287, 3.8035085602))
                CenterArc((1.3402587287, 1.0834325585), 0.5, -180, 90)
                Line((10.7823652483, 0.5834325585), (1.3402587287, 0.5834325585))
                CenterArc((10.7823652483, 1.0834325585), 0.5, -90, 90)
                Line((11.2823652483, 3.8035085602), (11.2823652483, 1.0834325585))
                CenterArc((10.7823652483, 3.8035085602), 0.5, 0, 90)
                Line((1.3402587287, 4.3035085602), (10.7823652483, 4.3035085602))
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.5561339429, perimeter: 2.6435932437
            with Locations((11.8589232476, 2.4915338059)):
                Circle(0.4207409323)
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0453955674, perimeter: 0.7552863856
            with Locations((0.385148388, 2.5354818984)):
                Circle(0.1202075617)
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-1.0454566548, 3.791696502)):
                Circle(0.5)
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)
    return part.part


def model_44407_e4543694_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 15 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 37.4463495408, perimeter: 24.5707963268
            with BuildLine():
                CenterArc((5.25, 11.25), 0.25, 90, 90)
                Line((5, 4.25), (5, 11.25))
                CenterArc((5.25, 4.25), 0.25, 180, 90)
                Line((9.75, 4), (5.25, 4))
                CenterArc((9.75, 4.25), 0.25, -90, 90)
                Line((10, 11.25), (10, 4.25))
                CenterArc((9.75, 11.25), 0.25, 0, 90)
                Line((5.25, 11.5), (9.75, 11.5))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-7.5, -5)):
                Circle(0.5)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(10, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0314159275, perimeter: 0.6283185401
            with Locations((9.3000001386, 0.3000000045)):
                Circle(0.1000000015)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(10, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0314159275, perimeter: 0.6283185401
            with Locations((10.000000149, 0.3000000045)):
                Circle(0.1000000015)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05, mode=Mode.ADD)
    return part.part


def model_44541_cefe3e4c_0000():
    """Model: Component1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 17, perimeter: 68
            with BuildLine():
                Line((0, 11), (0, 0))
                Line((0, 0), (7, 0))
                Line((7, 0), (7, 11))
                Line((7, 11), (0, 11))
            make_face()
            with BuildLine():
                Line((6.5, 10.5), (0.5, 10.5))
                Line((6.5, 0.5), (6.5, 10.5))
                Line((0.5, 0.5), (6.5, 0.5))
                Line((0.5, 10.5), (0.5, 0.5))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XY construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 77, perimeter: 36
            with BuildLine():
                Line((0, 11), (0, 0))
                Line((0, 0), (7, 0))
                Line((7, 0), (7, 11))
                Line((7, 11), (0, 11))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on XY construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 76.8137030443, perimeter: 35.9467722984
            with BuildLine():
                Line((7, 0), (7, 10.9733861492))
                Line((7, 10.9733861492), (0, 10.9733861492))
                Line((0, 10.9733861492), (0, 0))
                Line((0, 0), (7, 0))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.9886852486, perimeter: 4.0526763078
            with BuildLine():
                CenterArc((1, 10), 0.3266935809, 90, 180)
                Line((1, 9.6733064191), (2, 9.6733064191))
                CenterArc((2, 10), 0.3266935809, -90, 180)
                Line((2, 10.3266935809), (1, 10.3266935809))
            make_face()
        # OneSide extrude, distance=-4
        extrude(amount=-4, mode=Mode.SUBTRACT)
    return part.part


def model_44646_300a8b20_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 25, perimeter: 25
            with BuildLine():
                Line((2.5, 0), (-2.5, 0))
                Line((-2.5, 0), (-2.5, -2.5))
                Line((-2.5, -2.5), (-5, -2.5))
                Line((-5, -2.5), (-5, -5))
                Line((-5, -5), (0, -5))
                Line((0, -5), (0, -2.5))
                Line((0, -2.5), (2.5, -2.5))
                Line((2.5, -2.5), (2.5, 0))
            make_face()
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(2.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with Locations((-1.25, 1.25)):
                Circle(0.75)
        # OneSide extrude, distance=-5.3
        extrude(amount=-5.3, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with Locations((1.25, 1.25)):
                Circle(0.75)
        # OneSide extrude, distance=-2.6
        extrude(amount=-2.6, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with Locations((-1.25, 1.25)):
                Circle(0.75)
        # OneSide extrude, distance=-2.6
        extrude(amount=-2.6, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.8913441284, perimeter: 9.5217921712
            with BuildLine():
                Line((0.8695519572, 4.5), (0.8695519572, 3))
                Line((0.8695519572, 3), (4.1304480428, 3))
                Line((4.1304480428, 3), (4.1304480428, 4.5))
                Line((4.1304480428, 4.5), (0.8695519572, 4.5))
            make_face()
        # OneSide extrude, distance=-2.6
        extrude(amount=-2.6, mode=Mode.SUBTRACT)
    return part.part


def model_45303_48d14b32_0005():
    """Model: profil for exercises legs"""
    with BuildPart() as part:
        # Sketch3 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 13 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.31, perimeter: 34.8
            with BuildLine():
                Line((102.5, -27.5), (102.5, -22.5))
                Line((102.5, -22.5), (97.5, -22.5))
                Line((97.5, -22.5), (97.5, -27.5))
                Line((97.5, -27.5), (102.5, -27.5))
            make_face()
            with BuildLine():
                Line((98.15, -26.85), (98.15, -23.15))
                Line((98.15, -23.15), (101.85, -23.15))
                Line((101.85, -23.15), (101.85, -26.85))
                Line((101.85, -26.85), (98.15, -26.85))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=50
        extrude(amount=50)

        # Sketch4 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(102.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 19.6847152318, perimeter: 22.336946173
            with BuildLine():
                CenterArc((-25, -1.5), 2.9154759474, 149.0362434679, 241.9275130641)
                Line((-27.5, 0), (-22.5, 0))
            make_face()
            with BuildLine():
                CenterArc((-25, -1.5), 0.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-5
        extrude(amount=-5, mode=Mode.ADD)

        # Sketch5 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(102.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            with Locations((-25, 40)):
                Circle(1.5)
        # OneSide extrude, distance=-5
        extrude(amount=-5, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 22.5), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 5, perimeter: 12
            with BuildLine():
                Line((-102.5, 48.6595350568), (-97.5, 48.6595350568))
                Line((-102.5, 47.6595350568), (-102.5, 48.6595350568))
                Line((-97.5, 47.6595350568), (-102.5, 47.6595350568))
                Line((-97.5, 48.6595350568), (-97.5, 47.6595350568))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.ADD)

        # Sketch7 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 48.6595350568, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.5274078043, perimeter: 5.9208410124
            with BuildLine():
                CenterArc((-100, 22), 1, 150, 240)
                Line((-99.1339745962, 22.5), (-100.8660254038, 22.5))
            make_face()
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)
    return part.part


def model_45303_48d14b32_0017():
    """Model: load (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 583.5990449985, perimeter: 99.6863812741
            with BuildLine():
                Line((-20.0146340641, -2.4423095196), (-20.0146340641, 2.5576904804))
                Line((-14.9614524969, -7.9556227074), (-20.0146340641, -2.4423095196))
                Line((15.0385475031, -7.9556227074), (-14.9614524969, -7.9556227074))
                Line((20, -2.475027071), (15.0385475031, -7.9556227074))
                Line((20, 2.524972929), (20, -2.475027071))
                Line((14.9723614257, 8), (20, 2.524972929))
                Line((-15.0276385743, 8), (14.9723614257, 8))
                Line((-20.0146340641, 2.5576904804), (-15.0276385743, 8))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            Circle(2)
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.0424771932, perimeter: 10.0530964915
            with Locations((9.5, 0)):
                Circle(1.6)
            # Profile area: 8.0424771932, perimeter: 10.0530964915
            with Locations((-9.5, 0)):
                Circle(1.6)
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)
    return part.part


def model_45359_1768ab3f_0034():
    """Model: Piston"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            Circle(0.6)
        # OneSide extrude, distance=0.25
        extrude(amount=0.25)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.25, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.9503317777, perimeter: 3.4557519189
            Circle(0.55)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.35, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1806415776, perimeter: 7.2256631033
            with BuildLine():
                CenterArc((0, 0), 0.6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.55, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.9503317777, perimeter: 3.4557519189
            Circle(0.55)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.65, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.9503317777, perimeter: 3.4557519189
            Circle(0.55)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.75, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1806415776, perimeter: 7.2256631033
            with BuildLine():
                CenterArc((0, 0), 0.6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.55, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.9503317777, perimeter: 3.4557519189
            Circle(0.55)
        # OneSide extrude, distance=0.25
        extrude(amount=0.25, mode=Mode.ADD)
    return part.part


def model_45360_cb4bac3f_0015():
    """Model: Enlace articulaciones"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 16 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.75, perimeter: 12
            with BuildLine():
                Line((0, 4), (5.5, 4))
                Line((5.5, 4), (5.5, 4.5))
                Line((5.5, 4.5), (0, 4.5))
                Line((0, 4.5), (0, 4))
            make_face()
            # Profile area: 2.75, perimeter: 12
            with BuildLine():
                Line((0, 0), (5.5, 0))
                Line((5.5, 0), (5.5, 0.5))
                Line((5.5, 0.5), (0, 0.5))
                Line((0, 0.5), (0, 0))
            make_face()
        # TwoSides extrude (symmetric), distance=0.85
        extrude(amount=0.85, both=True)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 16 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 18.9029906004, perimeter: 20.0882166368
            with BuildLine():
                Line((5.5, 0.5), (0, 0.5))
                Line((5.5, 4), (5.5, 0.5))
                Line((0, 4), (5.5, 4))
                Line((0, 0.5), (0, 4))
            make_face()
            with BuildLine():
                CenterArc((2.90381814, 2.25), 0.33235, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides extrude, along=0.15, against=-0.85
        extrude(amount=0.15, mode=Mode.ADD)
        extrude(sk.sketch, amount=-0.85, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 16 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 2.0554408546, perimeter: 9.7837320264
            with BuildLine():
                CenterArc((0.9976332677, -2.3251161725), 6.5, 101.4315722959, 1.8893516132)
                Line((-0.5, 4), (-0.5, 0))
                Line((0, 0), (-0.5, 0))
                Line((0, 0.5), (0, 0))
                Line((0, 0.5), (0, 4))
                Line((0, 4.5), (0, 4))
                CenterArc((-0.5, 4.5), 0.5, -65.247503795, 65.247503795)
            make_face()
            # Profile area: 0.0760647603, perimeter: 1.3970577812
            with BuildLine():
                Line((-0.5, 0), (-0.5, -0.2972534893))
                CenterArc((0.8401663189, -2.2261950845), 2.3488, 110.9590267651, 13.8312980634)
                Line((0, 0), (0, -0.0328))
                Line((0, 0), (-0.5, 0))
            make_face()
        # TwoSides extrude, along=0.85, against=-0.35
        extrude(amount=0.85, mode=Mode.ADD)
        extrude(sk.sketch, amount=-0.35, mode=Mode.ADD)

        # Sketch1 -> Extrude4 (Join)
        # Sketch on XZ construction plane
        # Sketch has 16 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 14.8087211429, perimeter: 21.2693056243
            with BuildLine():
                Line((-0.5, 0), (-5.0722789874, 0))
                CenterArc((0.9976332677, -2.3251161725), 6.5, 159.0403632123, 19.4134260007)
                Line((-5.5, -2.1497254134), (-5.5, -2.4895473538))
                Line((-5.5, -2.4895473538), (-5.5, -2.5005069316))
                CenterArc((0.9976332677, -2.3251161725), 6.5, -178.4537892131, 1.3714705167)
                CenterArc((-3.5000148687, -2.5000554), 2.0000127361, -175.5287648049, 85.0558193954)
                Line((-3.5165236955, -4.5), (-3.4835060419, -4.5))
                CenterArc((-3.5000148687, -2.5000554), 2.0000127361, -89.5270545906, 93.1375640972)
                CenterArc((0.8401663189, -2.2261950845), 2.3488, 124.7903248285, 58.8201846782)
                Line((-0.5, 0), (-0.5, -0.2972534893))
            make_face()
            with BuildLine():
                CenterArc((-4.0084474759, -2.4999570311), 0.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 11.4475974883, perimeter: 18.0350415168
            with BuildLine():
                CenterArc((0.9976332677, -2.3251161725), 6.5, 103.3209239091, 55.7194393032)
                Line((-0.5, 0), (-5.0722789874, 0))
                Line((-0.5, 4), (-0.5, 0))
            make_face()
            with BuildLine():
                CenterArc((-3.3924382832, 1.00009681), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides extrude, along=0.45, against=-0.35
        extrude(amount=0.45, mode=Mode.ADD)
        extrude(sk.sketch, amount=-0.35, mode=Mode.ADD)

        # Sketch2 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -0.35, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 1.7905206934, perimeter: 8.0685073764
            with BuildLine():
                CenterArc((-1.7549573182, 2.3741074339), 0.2509855488, 0, 173.4757680663)
                CenterArc((0.8401663189, 2.2261950845), 2.8499500979, 176.4507543991, 0.5742592682)
                CenterArc((0.8401663189, 2.2261950845), 2.8499500979, 177.0250136672, 75.8294197749)
                Line((0, 0.0328), (0, -0.4971))
                CenterArc((0.8401663189, 2.2261950845), 2.3488, 177.086277573, 71.9546956619)
                CenterArc((0.8401663189, 2.2261950845), 2.3488, 176.3894904933, 0.6967870796)
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch3 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -0.85, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 3.8077468847, perimeter: 9.3138797401
            with BuildLine():
                CenterArc((2.90381814, -2.25), 1.15, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((2.90381814, -2.25), 0.33235, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)
    return part.part


def model_45360_cb4bac3f_0016():
    """Model: tornillo-eje (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.5446900494, perimeter: 5.6548667765
            Circle(0.9)
        # OneSide extrude, distance=1.8
        extrude(amount=1.8)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6361725124, perimeter: 2.8274333882
            Circle(0.45)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4948008429, perimeter: 6.5973445725
            with BuildLine():
                CenterArc((0, 0), 0.6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.45, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.6361725124, perimeter: 2.8274333882
            Circle(0.45)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 2.3640484718, perimeter: 13.5088484104
            with BuildLine():
                CenterArc((0, 0), 1.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.9, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 2.5446900494, perimeter: 5.6548667765
            Circle(0.9)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8, mode=Mode.ADD)
    return part.part


def model_45424_63abf99e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 197.615916848, perimeter: 311.2061682646
            with BuildLine():
                CenterArc((0, 0), 25.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 24.13, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=25.4
        extrude(amount=25.4)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 84.5136165756, perimeter: 51.1407776004
            with BuildLine():
                Line((12.6999998093, 10.1599998474), (20.4252091483, 12.8478687433))
                Line((0, 0), (12.6999998093, 10.1599998474))
                Line((17.779999733, 5.0799999237), (0, 0))
                Line((20.4252091483, 12.8478687433), (17.779999733, 5.0799999237))
            make_face()
        # OneSide extrude, distance=20.32
        extrude(amount=20.32)
    return part.part


def model_45806_2c8651cd_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 42.5, perimeter: 27
            with BuildLine():
                Line((2.5, -4.25), (2.5, 4.25))
                Line((2.5, 4.25), (-2.5, 4.25))
                Line((-2.5, 4.25), (-2.5, -4.25))
                Line((-2.5, -4.25), (2.5, -4.25))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(2.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.4528725289, perimeter: 9.4600363503
            with BuildLine():
                CenterArc((-4.3741178425, -3.663069857), 0.286557588, 90, 180)
                Line((-4.3741178425, -3.949627445), (-0.5443468807, -3.949627445))
                CenterArc((-0.5443468807, -3.663069857), 0.286557588, -90, 180)
                Line((-0.5443468807, -3.376512269), (-4.3741178425, -3.376512269))
            make_face()
        # TwoSides extrude (symmetric), distance=1
        extrude(amount=1, both=True, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(2.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.2850233697, perimeter: 13.7415026453
            with BuildLine():
                CenterArc((-2.5, -1.5), 1.1870280715, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-2.5, -1.5), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides extrude (symmetric), distance=1
        extrude(amount=1, both=True, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 16 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(2.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.5269322318, perimeter: 15.2887270025
            with BuildLine():
                CenterArc((-3, 2.5), 1, 90, 180)
                Line((-3, 1.5), (-2, 1.5))
                CenterArc((-2, 2.5), 1, -90, 180)
                Line((-2, 3.5), (-3, 3.5))
            make_face()
            with BuildLine():
                Line((-2.0422571915, 3.310716119), (-2.9980882357, 3.310716119))
                CenterArc((-2.0422571915, 2.5), 0.810716119, -90, 180)
                Line((-2.9980882357, 1.689283881), (-2.0422571915, 1.689283881))
                CenterArc((-2.9980882357, 2.5), 0.810716119, 90, 180)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides extrude (symmetric), distance=1
        extrude(amount=1, both=True, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(2.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.8172149327, perimeter: 4.7786814427
            with Locations((-2.5, -1.5)):
                Circle(0.7605507731)
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4, taper=-25, mode=Mode.SUBTRACT)
    return part.part


def model_45819_28cdbf87_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 11.5443493658, perimeter: 27.4578109911
            with BuildLine():
                Line((-0.5, 0), (7.443473719, 0))
                Line((-0.5, 0), (-0.5, -0.7521909638))
                Line((7.2677842709, -1.0498574986), (-0.5, -0.7521909638))
                CenterArc((7.499815655, 0.715340766), 1.7803829579, -97.4884697863, 45.348614097)
                Line((8.5925010448, -0.6902915171), (11.8353208122, 1.6881132401))
                Line((11.7435861325, 2.3279705211), (11.8353208122, 1.6881132401))
                Line((7.943473719, 0.1339745962), (11.7435861325, 2.3279705211))
                CenterArc((7.443473719, 1), 1, -90, 30)
            make_face()
        # Symmetric extrude, each_side=5
        extrude(amount=5, both=True)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -3.3391440703, -1.9278557279), x_dir=(1, 0, 0), z_dir=(0, 0.8660254038, 0.5))):
            # Profile area: 16, perimeter: 20
            with BuildLine():
                Line((4, 8), (4, 10))
                Line((4, 10), (-4, 10))
                Line((-4, 10), (-4, 8))
                Line((-4, 8), (4, 8))
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -3.3391440703, -1.9278557279), x_dir=(1, 0, 0), z_dir=(0, 0.8660254038, 0.5))):
            # Profile area: 1.3298547503, perimeter: 5.6670378763
            with BuildLine():
                Line((-1.2397738328, 10.5), (-1.2397738328, 11.0937451054))
                Line((1, 10.5), (-1.2397738328, 10.5))
                Line((1, 11.0937451054), (1, 10.5))
                Line((-1.2397738328, 11.0937451054), (1, 11.0937451054))
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 12 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.9914159265, perimeter: 3.8283185307
            with BuildLine():
                CenterArc((-3.3821543611, -0.9932256346), 0.1, -90, 90)
                Line((-3.2821543611, -0.1932256346), (-3.2821543611, -0.9932256346))
                CenterArc((-3.3821543611, -0.1932256346), 0.1, 0, 90)
                Line((-4.1821543611, -0.0932256346), (-3.3821543611, -0.0932256346))
                CenterArc((-4.1821543611, -0.1932256346), 0.1, 90, 90)
                Line((-4.2821543611, -0.9932256346), (-4.2821543611, -0.1932256346))
                CenterArc((-4.1821543611, -0.9932256346), 0.1, 180, 90)
                Line((-3.3821543611, -1.0932256346), (-4.1821543611, -1.0932256346))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch6 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 12 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.7914159265, perimeter: 11.4283185307
            with BuildLine():
                CenterArc((-3.4821543611, -1.9512381471), 0.1, 0, 90)
                Line((-3.4821543611, -1.8512381471), (-4.2821543611, -1.8512381471))
                CenterArc((-4.2821543611, -1.9512381471), 0.1, 90, 90)
                Line((-4.3821543611, -1.9512381471), (-4.3821543611, -6.5512381471))
                CenterArc((-4.2821543611, -6.5512381471), 0.1, -180, 90)
                Line((-4.2821543611, -6.6512381471), (-3.4821543611, -6.6512381471))
                CenterArc((-3.4821543611, -6.5512381471), 0.1, -90, 90)
                Line((-3.3821543611, -6.5512381471), (-3.3821543611, -1.9512381471))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


def model_45922_26941172_0003():
    """Model: bottle holder 17"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 30, perimeter: 26
            with BuildLine():
                Line((78, 20), (75, 20))
                Line((78, 30), (78, 20))
                Line((75, 30), (78, 30))
                Line((75, 20), (75, 30))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((76.5, 25)):
                Circle(0.5)
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(78, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.25, perimeter: 14
            with BuildLine():
                Line((-7, 20.5), (-0.5, 20.5))
                Line((-7, 20), (-7, 20.5))
                Line((-0.5, 20), (-7, 20))
                Line((-0.5, 20.5), (-0.5, 20))
            make_face()
            # Profile area: 0.25, perimeter: 2
            with BuildLine():
                Line((-0.5, 20.5), (-0.5, 20))
                Line((0, 20), (-0.5, 20))
                Line((0, 20.5), (0, 20))
                Line((-0.5, 20.5), (0, 20.5))
            make_face()
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 20.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-76.5, 4)):
                Circle(0.5)
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.ADD)
    return part.part


def model_46086_371b5052_0009():
    """Model: Knife v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 5.6934125237, perimeter: 12.062969267
            with BuildLine():
                CenterArc((-3.2522321429, 5.5251116071), 4.5078564201, -2.8624052261, 28.8450720407)
                CenterArc((2.9, 5.5), 2.9, 136.3971810273, 43.6028189727)
                Line((0, 2.1), (0, 5.5))
                Line((0.9, 2.1), (0, 2.1))
                Line((1.1, 2.3), (0.9, 2.1))
                Line((1.25, 5.3), (1.1, 2.3))
            make_face()
        # OneSide extrude, distance=0.16
        extrude(amount=0.16)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.2075719188, perimeter: 6.1980564395
            with BuildLine():
                Line((0, 0), (0, 2.1))
                Line((0, 0), (1.0132335988, 0))
                Line((1.0132335988, 0), (1.1, 1.9))
                Line((0.9, 2.1), (1.1, 1.9))
                Line((0.9, 2.1), (0, 2.1))
            make_face()
        # OneSide extrude, distance=0.16
        extrude(amount=0.16, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on Profile plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.16), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.2800000021, perimeter: 2.3000000119
            with BuildLine():
                Line((0, 0), (0.35, 0))
                Line((0.35, 0), (0.35, 0.8000000119))
                Line((0.35, 0.8000000119), (0, 0.8))
                Line((0, 0), (0, 0.8))
            make_face()
        # OneSide extrude, distance=-3.3
        extrude(amount=-3.3, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on Profile plane
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.16), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((0.65, 0.4)):
                Circle(0.1)
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)
    return part.part


def model_47799_8b49af01_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 13 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.4836504592, perimeter: 6.7707963268
            with BuildLine():
                Line((3, 0), (3, -1.4))
                Line((4.2, -1.4), (3, -1.4))
                Line((4.2, 0), (4.2, -1.4))
                Line((3, 0), (4.2, 0))
            make_face()
            with BuildLine():
                CenterArc((3.475, -0.7), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 2.52, perimeter: 6.4
            with BuildLine():
                Line((1.2, 0), (1.2, -1.4))
                Line((3, -1.4), (1.2, -1.4))
                Line((3, 0), (3, -1.4))
                Line((1.2, 0), (3, 0))
            make_face()
            # Profile area: 1.4836504592, perimeter: 6.7707963268
            with BuildLine():
                Line((0, 0), (1.2, 0))
                Line((0, -1.4), (0, 0))
                Line((1.2, -1.4), (0, -1.4))
                Line((1.2, 0), (1.2, -1.4))
            make_face()
            with BuildLine():
                CenterArc((0.725, -0.7), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 15 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.181743185, perimeter: 2.2377397645
            with BuildLine():
                Line((2.2, 2.7), (2.2, 1.8))
                Line((2.2, 2.7), (2, 2.7))
                Line((2, 2.7), (2, 1.8))
                Line((2, 1.8), (1.9997564817, 1.7826591552))
                CenterArc((2.1, 1.4), 0.3955714753, 75.2797518422, 29.3999008912)
                Line((2.2, 1.8), (2.2005146162, 1.7825880343))
            make_face()
            # Profile area: 3.106670531, perimeter: 12.1172334055
            with BuildLine():
                Line((2.2, 1.8), (2.2005146162, 1.7825880343))
                CenterArc((2.1, 1.4), 0.3955714753, 104.6796527334, 330.6000991088)
                Line((2, 1.8), (1.9997564817, 1.7826591552))
                Line((2, 2.7), (2, 1.8))
                Line((2, 2.7), (1.3999999896, 2.7))
                Line((1.3999999896, 2.7), (1.3999999896, 0))
                Line((1.3999999896, 0), (2.8000000104, 0))
                Line((2.8000000104, 0), (2.8000000104, 2.7))
                Line((2.8000000104, 2.7), (2.2, 2.7))
                Line((2.2, 2.7), (2.2, 1.8))
            make_face()
            # Profile area: 0.4915863404, perimeter: 2.4854488814
            with BuildLine():
                CenterArc((2.1, 1.4), 0.3955714753, 104.6796527334, 330.6000991088)
                CenterArc((2.1, 1.4), 0.3955714753, 75.2797518422, 29.3999008912)
            make_face()
        # OneSide extrude, distance=1.4
        extrude(amount=1.4, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on XY construction plane
        # Sketch has 15 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.181743185, perimeter: 2.2377397645
            with BuildLine():
                Line((2.2, 2.7), (2.2, 1.8))
                Line((2.2, 2.7), (2, 2.7))
                Line((2, 2.7), (2, 1.8))
                Line((2, 1.8), (1.9997564817, 1.7826591552))
                CenterArc((2.1, 1.4), 0.3955714753, 75.2797518422, 29.3999008912)
                Line((2.2, 1.8), (2.2005146162, 1.7825880343))
            make_face()
            # Profile area: 0.4915863404, perimeter: 2.4854488814
            with BuildLine():
                CenterArc((2.1, 1.4), 0.3955714753, 104.6796527334, 330.6000991088)
                CenterArc((2.1, 1.4), 0.3955714753, 75.2797518422, 29.3999008912)
            make_face()
        # OneSide extrude, distance=1.4
        extrude(amount=1.4, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude4 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-0.7, 2.25)):
                Circle(0.2)
        # OneSide extrude, distance=7.2
        extrude(amount=7.2, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude5 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.3803388222, perimeter: 3.7782665551
            with BuildLine():
                CenterArc((-0.7, 2.25), 0.4013297986, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-0.7, 2.25), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.SUBTRACT)
    return part.part


def model_47878_0edb6829_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch6 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 24.8291943113, perimeter: 17.6638856929
            with Locations((2.8744227156, -3.5475848202)):
                Circle(2.8112947222)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


def model_48077_2cfc0eaa_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 25, perimeter: 20
            with BuildLine():
                Line((2.5, -2.5), (-2.5, -2.5))
                Line((2.5, 2.5), (2.5, -2.5))
                Line((-2.5, 2.5), (2.5, 2.5))
                Line((-2.5, -2.5), (-2.5, 2.5))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(2.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            with Locations((0, 2.5)):
                Circle(1.5)
        # OneSide extrude, distance=-5
        extrude(amount=-5, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 2.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            with Locations((0, 2.5)):
                Circle(1.5)
        # OneSide extrude, distance=-5
        extrude(amount=-5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            Circle(1.5)
        # OneSide extrude, distance=-5
        extrude(amount=-5, mode=Mode.SUBTRACT)
    return part.part


def model_48224_53cae924_0012():
    """Model: rear hub link v2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 120.3815597502, perimeter: 56.006605534
            with BuildLine():
                CenterArc((9.75, -2.189868996), 2.5, -115.3173478285, 180)
                CenterArc((0, -22.8), 25.3, 64.6826521715, 50.6346956569)
                CenterArc((-9.75, -2.189868996), 2.5, 115.3173478285, 180.0000008538)
                CenterArc((0, -22.8), 20.3, 64.6826521715, 50.6346955518)
            make_face()
        # OneSide extrude, distance=0.95
        extrude(amount=0.95)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.95, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 39.4755779405, perimeter: 25.8298863517
            with BuildLine():
                Line((3.2779812988, 2.7664072467), (4.5772423296, -2.0825009325))
                CenterArc((0, 22.8), 20.3, -99.2926318294, 18.5852636588)
                Line((-3.2779812988, 2.7664072467), (-4.5772423296, -2.0825009325))
                CenterArc((0, 22.8), 25.3, -100.4232742491, 20.8465484981)
            make_face()
        # OneSide extrude, distance=1.9
        extrude(amount=1.9, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 2.85, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 40.4529907989, perimeter: 25.1282778318
            with BuildLine():
                Line((4.5772423296, -2.0825009325), (3.2779812988, 2.7664072467))
                CenterArc((0, 22.8), 25.3, -79.5767257509, 14.8940735794)
                CenterArc((9.75, 2.189868996), 2.5, -64.6826521715, 180)
                CenterArc((0, 22.8), 20.3, -80.7073681706, 16.0247158939)
            make_face()
            # Profile area: 40.4529909049, perimeter: 25.1282778691
            with BuildLine():
                CenterArc((-9.75, 2.189868996), 2.5, 64.6826521715, 180)
                CenterArc((0, 22.8), 25.3, -115.3173478285, 14.8940735794)
                Line((-4.5772423296, -2.0825009325), (-3.2779812988, 2.7664072467))
                CenterArc((0, 22.8), 20.3, -115.3173478285, 16.0247159991)
            make_face()
            # Profile area: 39.4755779405, perimeter: 25.8298863517
            with BuildLine():
                Line((-4.5772423296, -2.0825009325), (-3.2779812988, 2.7664072467))
                CenterArc((0, 22.8), 25.3, -100.4232742491, 20.8465484981)
                Line((4.5772423296, -2.0825009325), (3.2779812988, 2.7664072467))
                CenterArc((0, 22.8), 20.3, -99.2926318294, 18.5852636588)
            make_face()
        # OneSide extrude, distance=0.95
        extrude(amount=0.95, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.8352873699, perimeter: 5.9690260418
            with Locations((-9.75, 2.189868996)):
                Circle(0.95)
            # Profile area: 2.8352873699, perimeter: 5.9690260418
            with Locations((9.75, 2.189868996)):
                Circle(0.95)
        # OneSide extrude, distance=-9.5
        extrude(amount=-9.5, mode=Mode.SUBTRACT)
    return part.part


def model_48332_fb679f90_0006():
    """Model: lower frame"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 37.2039028363, perimeter: 52.720354927
            with BuildLine():
                Line((-29.5000001714, 2.5), (-11.5000001714, 0))
                Line((-11.5000001714, 0), (-11.2936476145, 1.4857384098))
                Line((-11.2936476145, 1.4857384098), (-29.2936476145, 3.9857384098))
                CenterArc((-30.0537597015, -1.487068617), 5.5253404544, 82.092837297, 82.3256308791)
                Line((-35.3760394619, -0.002910509), (-33.8128591228, -0.002910509))
                CenterArc((-30.0566742948, -1.5080536891), 4.046526962, 82.092837297, 76.0706618492)
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch4 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-11.2823620152, 1.5669947243, 0), x_dir=(0, 0, -1), z_dir=(0.9904922732, -0.1375683713, 0))):
            # Profile area: 1.35, perimeter: 4.8
            with BuildLine():
                Line((-0.3, -1.5820362932), (-1.2, -1.5820362932))
                Line((-0.3, -0.0820362932), (-0.3, -1.5820362932))
                Line((-1.2, -0.0820362932), (-0.3, -0.0820362932))
                Line((-1.2, -1.5820362932), (-1.2, -0.0820362932))
            make_face()
            # Profile area: 0.45, perimeter: 3.6
            with BuildLine():
                Line((0, -1.5820362932), (-0.3, -1.5820362932))
                Line((0, -1.5820362932), (0, -0.0820362932))
                Line((-0.3, -0.0820362932), (0, -0.0820362932))
                Line((-0.3, -0.0820362932), (-0.3, -1.5820362932))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch5 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -0.002910509, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 1.3110817423, perimeter: 4.6471708583
            with BuildLine():
                Line((-35.3760394619, 0), (-33.8128591228, 0))
                Line((-35.3760394619, 0), (-35.100000523, -0.9000000134))
                CenterArc((-34.6821648895, -0.7718456765), 0.4370470806, -162.9487034583, 84.5266327607)
                CenterArc((-34.6626762758, -0.7009767522), 0.5036656858, -82.214730381, 58.939429924)
                Line((-33.8128591228, 0), (-34.2000005096, -0.9000000134))
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.ADD)

        # Sketch2 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((13.1950823758, 1.0982356656)):
                Circle(0.2)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((16.4000002444, 1.2000000179)):
                Circle(0.2)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((32.6946976031, 2.7357553401)):
                Circle(0.2)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)
    return part.part


def model_48724_70685a9d_0007():
    """Model: shield wire"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 25 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 62.3561944902, perimeter: 36.5663706144
            with BuildLine():
                CenterArc((17, -3), 1, -180, 90)
                Line((23, -4), (17, -4))
                CenterArc((23, -3), 1, -90, 90)
                Line((24, 3), (24, -3))
                CenterArc((23, 3), 1, 0, 90)
                Line((17, 4), (23, 4))
                CenterArc((17, 3), 1, 90, 90)
                Line((16, -3), (16, 3))
            make_face()
            with BuildLine():
                CenterArc((16.6, -3.4), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((23.4, -3.4), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((23.4, 3.4), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((16.6, 3.4), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 36, perimeter: 24
            with BuildLine():
                Line((-23.000000298, 3), (-17.000000298, 3))
                Line((-23.000000298, -3), (-23.000000298, 3))
                Line((-17.000000298, -3), (-23.000000298, -3))
                Line((-17.000000298, 3), (-17.000000298, -3))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 17 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 24.7853981634, perimeter: 19.1415926536
            with BuildLine():
                CenterArc((18, -2), 0.5, 180, 90)
                Line((22, -2.5), (18, -2.5))
                CenterArc((22, -2), 0.5, -90, 90)
                Line((22.5, 2), (22.5, -2))
                CenterArc((22, 2), 0.5, 0, 90)
                Line((18, 2.5), (22, 2.5))
                CenterArc((18, 2), 0.5, 90, 90)
                Line((17.5, -2), (17.5, 2))
            make_face()
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-20.000000298, 0)):
                Circle(0.25)
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.SUBTRACT)
    return part.part


def model_48907_25974aa4_0003():
    """Model: pull lever v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.4632190529, perimeter: 13.2461487033
            with BuildLine():
                CenterArc((0, 0), 0.35, 90, 180)
                Line((4.5000000671, -0.200000003), (0, -0.35))
                CenterArc((4.5, 0), 0.200000003, -89.9999807901, 179.9999615802)
                Line((0, 0.35), (4.5000000671, 0.200000003))
            make_face()
            with BuildLine():
                CenterArc((4.5, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1884895179, perimeter: 3.7699025524
            with BuildLine():
                CenterArc((0, 0), 0.35, 90, 180)
                Line((0, -0.35), (0.0233074354, -0.3492230855))
                CenterArc((0, 0), 0.35, -86.1816952667, 172.3633905332)
                Line((0.0233074354, 0.3492230855), (0, 0.35))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.054977852, perimeter: 2.1991140476
            with BuildLine():
                CenterArc((-4.5, 0), 0.1999999359, -90.0000192099, 180.0000377795)
                CenterArc((-4.5, 0), 0.1999999359, 90.0000185696, 179.9999622205)
            make_face()
            with BuildLine():
                CenterArc((-4.5, 0), 0.1499999352, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1884895179, perimeter: 3.7699025524
            with BuildLine():
                CenterArc((0, 0), 0.35, 93.8183047333, 172.3633905334)
                Line((-0.0233074354, -0.3492230855), (0, -0.35))
                CenterArc((0, 0), 0.35, -90, 180)
                Line((0, 0.35), (-0.0233074354, 0.3492230855))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1884895179, perimeter: 3.7699025524
            with BuildLine():
                Line((0, -0.35), (0.0233074354, -0.3492230855))
                CenterArc((0, 0), 0.35, -86.1816952667, 172.3633905332)
                Line((0.0233074354, 0.3492230855), (0, 0.35))
                CenterArc((0, 0), 0.35, 90, 180)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.6257849591, perimeter: 7.7836518489
            with BuildLine():
                Line((-4.2170696149, 0.2094310177), (-0.3931371732, 0.336895428))
                Line((-4.2170696149, 0.2094310177), (-4.0000000596, 0.1000000015))
                Line((-4.0000000596, 0.1000000015), (-0.6000000089, 0.1000000015))
                Line((-0.6000000089, 0.1000000015), (-0.3931371732, 0.336895428))
            make_face()
            # Profile area: 0.6257849591, perimeter: 7.7836518489
            with BuildLine():
                Line((-4.2170696149, -0.2094310177), (-0.3931371732, -0.336895428))
                Line((-0.6000000089, -0.1000000015), (-0.3931371732, -0.336895428))
                Line((-4.0000000596, -0.1000000015), (-0.6000000089, -0.1000000015))
                Line((-4.2170696149, -0.2094310177), (-4.0000000596, -0.1000000015))
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)
    return part.part


def model_48907_25974aa4_0006():
    """Model: bottom slider v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 25 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.75, perimeter: 4
            with BuildLine():
                Line((1.5, 0), (1, 0))
                Line((0, 0), (1, 0))
                Line((0, 0), (0, -0.5))
                Line((1.5, -0.5), (0, -0.5))
                Line((1.5, 0), (1.5, -0.5))
            make_face()
            # Profile area: 0.75, perimeter: 4
            with BuildLine():
                Line((0, 0), (0, -0.5))
                Line((0, 0), (-1, 0))
                Line((-1, 0), (-1.5, 0))
                Line((-1.5, 0), (-1.5, -0.5))
                Line((-1.5, -0.5), (0, -0.5))
            make_face()
        # TwoSides extrude (symmetric), distance=0.25
        extrude(amount=0.25, both=True)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 25 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.1, perimeter: 7.4
            with BuildLine():
                Line((2.2, 2.2), (2.2, 5.2))
                Line((2.2, 5.2), (1.5, 5.2))
                Line((1.5, 5.2), (1.5, 5))
                Line((1.5, 5), (1.5, 2.2))
                Line((1.5, 2.2), (2.2, 2.2))
            make_face()
            # Profile area: 2.5, perimeter: 11
            with BuildLine():
                Line((1.5, 5), (1.5, 2.2))
                Line((1, 5), (1.5, 5))
                Line((1, 0), (1, 5))
                Line((1.5, 0), (1, 0))
                Line((1.5, 2.2), (1.5, 0))
            make_face()
            # Profile area: 2.5, perimeter: 11
            with BuildLine():
                Line((-1, 0), (-1.5, 0))
                Line((-1, 0), (-1, 5))
                Line((-1, 5), (-1.5, 5))
                Line((-1.5, 5), (-1.5, 2.2))
                Line((-1.5, 2.2), (-1.5, 0))
            make_face()
            # Profile area: 2.1, perimeter: 7.4
            with BuildLine():
                Line((-1.5, 5), (-1.5, 2.2))
                Line((-1.5, 5.2), (-1.5, 5))
                Line((-2.2, 5.2), (-1.5, 5.2))
                Line((-2.2, 2.2), (-2.2, 5.2))
                Line((-1.5, 2.2), (-2.2, 2.2))
            make_face()
        # Symmetric extrude, each_side=0.1
        extrude(amount=0.1, both=True, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0907920277, perimeter: 1.0681415022
            Circle(0.17)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0682511004, perimeter: 2.4818581963
            with BuildLine():
                CenterArc((0, 0), 0.225, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.17, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.15
        extrude(amount=-0.15, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-0.2500000037, 0)):
                Circle(0.15)
        # OneSide extrude, distance=-0.7
        extrude(amount=-0.7, mode=Mode.SUBTRACT)
    return part.part


def model_48907_25974aa4_0009():
    """Model: right release leaver v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.8), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1256637061, perimeter: 2.5132741229
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.9), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.0355649933, perimeter: 7.0265489514
            with BuildLine():
                Line((-0.9961226717, -0.3999812075), (-0.0000075463, -0.3999999999))
                CenterArc((0, 0), 0.4, -90.0010809281, 181.2192372706)
                Line((-0.0085036949, 0.3999095988), (-0.9999635287, 0.3999999983))
                CenterArc((-1, 0), 0.4, 89.9947758703, 180.5606191897)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.4), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.020106193, perimeter: 2.0106192983
            with BuildLine():
                CenterArc((-1, 0), 0.17, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-1, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-1, 0)):
                Circle(0.15)
        # OneSide extrude, distance=-0.05
        extrude(amount=-0.05, mode=Mode.SUBTRACT)
    return part.part


def model_49017_b6231068_0001():
    """Model: zatyczka v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=5.7
        extrude(amount=5.7)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5.7, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.2252211948, perimeter: 8.1681409742
            with BuildLine():
                CenterArc((0, 0), 0.8000000119, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 1.2252211948, perimeter: 8.1681409742
            with BuildLine():
                CenterArc((0, 0), 0.8000000119, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5026548396, perimeter: 2.5132741603
            Circle(0.400000006)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)
    return part.part


def model_49024_b7f02205_0022():
    """Model: ogon v7"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            Circle(2.5)
        # OneSide extrude, distance=48
        extrude(amount=48)

        # Sketch5 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 28, perimeter: 22
            with BuildLine():
                Line((-3, -46), (-3, -50))
                Line((-3, -50), (4, -50))
                Line((4, -50), (4, -46))
                Line((4, -46), (-3, -46))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((0, 47)):
                Circle(0.2)
        # OneSide extrude, distance=-1.9
        extrude(amount=-1.9, mode=Mode.SUBTRACT)
    return part.part


def model_49116_4bd17b23_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 109.6660179723, perimeter: 46.1101884003
            with BuildLine():
                Line((-8.1730433653, 3.3545037347), (-8.1730433653, -3.3545037347))
                Line((-8.1730433653, -3.3545037347), (8.1730433653, -3.3545037347))
                Line((8.1730433653, -3.3545037347), (8.1730433653, 3.3545037347))
                Line((8.1730433653, 3.3545037347), (-8.1730433653, 3.3545037347))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(8.1730433653, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 11.9819878223, perimeter: 15.5750224135
            with BuildLine():
                Line((0, -3.3545037347), (0, 3.3545037347))
                CenterArc((-1.0887359769, 0), 3.5267607423, -72.0186701779, 144.0373403558)
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.ADD)

        # Sketch6 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-8.1730433653, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 4.5511862861, perimeter: 13.8086824684
            with BuildLine():
                Line((0, 3.3545037347), (0, -3.3545037347))
                CenterArc((5.1263476531, 0), 6.1263476531, 146.8006586968, 66.3986826065)
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.ADD)
    return part.part


def model_49145_4a5b250e_0000():
    """Model: duza sruba"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=7
        extrude(amount=7)

        # Sketch3 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 7, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch4 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 7.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1649336143, perimeter: 6.5973445725
            with BuildLine():
                CenterArc((0, 0), 0.55, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=5
        extrude(amount=5, mode=Mode.ADD)

        # Sketch5 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 12.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5890486225, perimeter: 7.853981634
            with BuildLine():
                CenterArc((0, 0), 0.7, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.55, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.9503317777, perimeter: 3.4557519189
            Circle(0.55)
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)
    return part.part


def model_49591_0b6b6dde_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 47.5, perimeter: 29
            with BuildLine():
                Line((2.5, -7), (-2.5, -7))
                Line((2.5, 2.5), (2.5, -7))
                Line((-2.5, 2.5), (2.5, 2.5))
                Line((-2.5, -7), (-2.5, 2.5))
            make_face()
        # OneSide extrude, distance=3.9
        extrude(amount=3.9)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(2.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4.7956799442, perimeter: 7.7630078917
            with Locations((-2, 2)):
                Circle(1.2355210792)
        # OneSide extrude, distance=15
        extrude(amount=15, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3.9, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.125, perimeter: 9.5276925691
            with BuildLine():
                Line((2, -2.5), (2.5, -2.5))
                Line((2.5, -2.5), (2.5, 2))
                Line((2.5, 2), (2, -2.5))
            make_face()
            # Profile area: 1.25, perimeter: 10.5249378106
            with BuildLine():
                Line((2.5, 2), (2, 7))
                Line((2.5, 2), (2.5, 7))
                Line((2.5, 7), (2, 7))
            make_face()
        # OneSide extrude, distance=-10.5
        extrude(amount=-10.5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3.9, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7226751322, perimeter: 10.2974192315
            with BuildLine():
                Line((-2.5, 2), (-2.2109299471, 7))
                Line((-2.2109299471, 7), (-2.5, 7))
                Line((-2.5, 2), (-2.5, 7))
            make_face()
            # Profile area: 0.5995246067, perimeter: 9.2743371971
            with BuildLine():
                Line((-2.2335446193, -2.5), (-2.5, 2))
                Line((-2.5, -2.5), (-2.5, 2))
                Line((-2.2335446193, -2.5), (-2.5, -2.5))
            make_face()
        # OneSide extrude, distance=-3.9
        extrude(amount=-3.9, mode=Mode.SUBTRACT)
    return part.part


def model_49613_1b97c07b_0002():
    """Model: prism"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((7.5, -10)):
                Circle(1)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(1, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 5.8584073464, perimeter: 18.2831853072
            with BuildLine():
                Line((9, -11.5), (6, -11.5))
                Line((9, -8.5), (9, -11.5))
                Line((6, -8.5), (9, -8.5))
                Line((6, -11.5), (6, -8.5))
            make_face()
            with BuildLine():
                CenterArc((7.5, -10), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((7.5, -10)):
                Circle(1)
        # OneSide extrude, distance=4
        extrude(amount=4, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -6), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 6, perimeter: 12
            with BuildLine():
                Line((1, -11.5), (5, -8.5))
                Line((1, -11.5), (5, -11.5))
                Line((5, -8.5), (5, -11.5))
            make_face()
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -8.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((-3, -7.5)):
                Circle(1)
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.ADD)
    return part.part


def model_49695_28e7f7e5_0000():
    """Model: iPhone 6 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 92.46, perimeter: 41
            with BuildLine():
                Line((4.5206361106, -10.0965539311), (-2.1793638894, -10.0965539311))
                Line((4.5206361106, 3.7034460689), (4.5206361106, -10.0965539311))
                Line((-2.1793638894, 3.7034460689), (4.5206361106, 3.7034460689))
                Line((-2.1793638894, -10.0965539311), (-2.1793638894, 3.7034460689))
            make_face()
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.7, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 63.6, perimeter: 33.2
            with BuildLine():
                Line((4.1706361106, -8.4965539311), (-1.8293638894, -8.4965539311))
                Line((4.1706361106, 2.1034460689), (4.1706361106, -8.4965539311))
                Line((-1.8293638894, 2.1034460689), (4.1706361106, 2.1034460689))
                Line((-1.8293638894, -8.4965539311), (-1.8293638894, 2.1034460689))
            make_face()
        # OneSide extrude, distance=-0.05
        extrude(amount=-0.05, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.7, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((1.1706361106, -9.2965539311)):
                Circle(0.5)
        # OneSide extrude, distance=-0.05
        extrude(amount=-0.05, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.7, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.6979304304, perimeter: 5.1241141782
            with BuildLine():
                CenterArc((0.4, 2.9534385921), 0.1500074768, 90.0001306324, 179.1908536688)
                Line((2.4905853346, 2.8034460689), (0.3978819667, 2.8034460689))
                CenterArc((2.4905848489, 2.9535890377), 0.1501429688, -89.9998146837, 176.4631843698)
                Line((0.399999658, 3.1034460689), (2.4998466663, 3.1034460689))
            make_face()
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-0.5, 2.9534385921)):
                Circle(0.15)
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)
    return part.part


def model_49901_cd5499cd_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 56.1135320777, perimeter: 31.5619263218
            with BuildLine():
                Line((5.1848140529, -2.7056675276), (-5.1848140529, -2.7056675276))
                Line((5.1848140529, 2.7056675276), (5.1848140529, -2.7056675276))
                Line((-5.1848140529, 2.7056675276), (5.1848140529, 2.7056675276))
                Line((-5.1848140529, -2.7056675276), (-5.1848140529, 2.7056675276))
            make_face()
        # Symmetric extrude, each_side=1
        extrude(amount=1, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 13.7544177995, perimeter: 13.1469810851
            with Locations((-2.0924070264, 0)):
                Circle(2.0924070264)
        # OneSide extrude, distance=4
        extrude(amount=4, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with Locations((-2.0924070264, 0)):
                Circle(0.75)
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)
    return part.part


def model_50379_ebec8fae_0003():
    """Model: Crank Handle"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 92.4741149353, perimeter: 291.2570549143
            with BuildLine():
                CenterArc((-20.2221339103, -24.0777673782), 23.495, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-20.2221339103, -24.0777673782), 22.86, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=1.27
        extrude(amount=1.27, both=True)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 262.221120433, perimeter: 275.2977642341
            with BuildLine():
                CenterArc((-20.2221339103, -24.0777673782), 22.86, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-20.2221339103, -24.0777673782), 20.955, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.635
        extrude(amount=0.635, both=True, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (NewBody)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.635), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 5.9379782707, perimeter: 14.9618350127
            with BuildLine():
                CenterArc((-20.2221339103, -24.0777673782), 1.5875, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-20.2221339103, -24.0777673782), 0.79375, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=2.54
        extrude(amount=2.54, both=True)

        # Sketch3 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.635), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 42.5370906464, perimeter: 50.8197514762
            with BuildLine():
                CenterArc((-7.2475480859, -20.2189913499), 13.9355002424, 97.152856243, 92.9757360025)
                Line((-20.9658711427, -22.6696605474), (-20.9591101621, -22.6717011442))
                CenterArc((-20.2221339103, -24.0777673782), 1.5875, 28.749453973, 88.9113997812)
                Line((-19.0905595308, -22.334651058), (-18.8303229089, -23.3142109714))
                CenterArc((-7.2475480859, -20.2189913499), 12.0305002424, 92.1775593198, 97.9510329256)
                CenterArc((-7.430389601, 21.056450468), 29.2549148378, -90.5371748621, 2.2347643998)
                CenterArc((-20.2221339103, -24.0777673782), 20.955, 49.3228056528, 8.2411426086)
            make_face()
        # OneSide extrude, distance=-1.27
        extrude(amount=-1.27, mode=Mode.ADD)

        # Sketch4 -> Extrude5 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 3.175), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 5.9379782707, perimeter: 14.9618350127
            with BuildLine():
                CenterArc((-20.2221339103, -24.0777673782), 1.5875, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-20.2221339103, -24.0777673782), 0.79375, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-1.27
        extrude(amount=-1.27, mode=Mode.SUBTRACT)
    return part.part


def model_50711_05fbe39a_0000():
    """Model: indexplate v1"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 25.6520661293, perimeter: 17.9542020153
            Circle(2.8575)
        # OneSide extrude, distance=0.3302
        extrude(amount=0.3302)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.3302), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            Circle(0.635)
        # OneSide extrude, distance=-0.508
        extrude(amount=-0.508, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.3302), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.7125573925, perimeter: 2.9923670025
            with Locations((0.9013900499, -1.7070266951)):
                Circle(0.47625)
        # OneSide extrude, distance=-2.032
        extrude(amount=-2.032, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.3302), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.061311605, perimeter: 0.8777609874
            with Locations((1.4018028157, 1.7903900499)):
                Circle(0.1397)
        # OneSide extrude, distance=-1.524
        extrude(amount=-1.524, mode=Mode.SUBTRACT)
    return part.part


def model_50777_2934de55_0001():
    """Model: Casing v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.9951323192, perimeter: 33.3008821281
            with BuildLine():
                CenterArc((0, 0), 2.8, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.928448377, perimeter: 5.2775304953
            with BuildLine():
                Line((1, 2.6153393661), (1, 3.5))
                CenterArc((0, 0), 2.8, 33.2017267486, 35.8734408238)
                Line((2.3428938706, 1.5332476353), (1.5, 3.5))
                Line((1.5, 3.5), (1, 3.5))
            make_face()
            # Profile area: 0.928448377, perimeter: 5.2775304953
            with BuildLine():
                Line((-1, -2.6153393661), (-1, -3.5))
                CenterArc((0, 0), 2.8, -146.7982732514, 35.8734408238)
                Line((-2.3428938706, -1.5332476353), (-1.5, -3.5))
                Line((-1.5, -3.5), (-1, -3.5))
            make_face()
            # Profile area: 0.928448377, perimeter: 5.2775304953
            with BuildLine():
                CenterArc((0, 0), 2.8, -69.0751675724, 35.8734408238)
                Line((1, -3.5), (1, -2.6153393661))
                Line((1, -3.5), (1.5, -3.5))
                Line((1.5, -3.5), (2.3428938706, -1.5332476353))
            make_face()
            # Profile area: 0.928448377, perimeter: 5.2775304953
            with BuildLine():
                CenterArc((0, 0), 2.8, 110.9248324276, 35.8734408238)
                Line((-1, 3.5), (-1, 2.6153393661))
                Line((-1.5, 3.5), (-1, 3.5))
                Line((-1.5, 3.5), (-2.3428938706, 1.5332476353))
            make_face()
        # OneSide extrude, distance=0.7
        extrude(amount=0.7, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on YZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.5026548396, perimeter: 2.5132741603
            with Locations((0, 0.6000000089)):
                Circle(0.400000006)
        # OneSide extrude, distance=-5
        extrude(amount=-5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on YZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))) as sk:
            # Profile area: 0.1256637099, perimeter: 1.2566370802
            with Locations((3.1000000462, 0.3000000045)):
                Circle(0.200000003)
            # Profile area: 0.1256637099, perimeter: 1.2566370802
            with Locations((-3.1000000462, 0.3000000045)):
                Circle(0.200000003)
        # TwoSides extrude, along=4, against=-3.8
        extrude(amount=4, mode=Mode.SUBTRACT)
        extrude(sk.sketch, amount=-3.8, mode=Mode.SUBTRACT)
    return part.part


def model_50784_bb6b362c_0001():
    """Model: pcb"""
    with BuildPart() as part:
        # board_outline -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 4.155070155, perimeter: 7.2259360291
            Circle(1.1500434375)
        # OneSide extrude, distance=0.16
        extrude(amount=0.16)

        # Drills - holes -> Extrude2 (Cut)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0380132711, perimeter: 0.6911503838
            with Locations((0.95, 0)):
                Circle(0.11)
            # Profile area: 0.0380132711, perimeter: 0.6911503838
            with Locations((-0.95, 0)):
                Circle(0.11)
        # OneSide extrude, distance=0.16
        extrude(amount=0.16, mode=Mode.SUBTRACT)

        # Drills - pads -> Extrude3 (Cut)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0081073197, perimeter: 0.3191858136
            with Locations((0.2043065625, -0.41412)):
                Circle(0.0508)
            # Profile area: 0.0081073197, perimeter: 0.3191858136
            with Locations((-0.2040725, -0.3962840625)):
                Circle(0.0508)
            # Profile area: 0.0081073197, perimeter: 0.3191858136
            with Locations((0.42071375, -0.0107659375)):
                Circle(0.0508)
            # Profile area: 0.0081073197, perimeter: 0.3191858136
            with Locations((-0.230339375, 0.40042125)):
                Circle(0.0508)
            # Profile area: 0.0081073197, perimeter: 0.3191858136
            with Locations((0.23, 0.42)):
                Circle(0.0508)
        # OneSide extrude, distance=0.16
        extrude(amount=0.16, mode=Mode.SUBTRACT)

        # Drills - vias -> Extrude4 (Cut)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0012566371, perimeter: 0.1256637061
            with Locations((-0.51, 0.38)):
                Circle(0.02)
            # Profile area: 0.0012566371, perimeter: 0.1256637061
            with Locations((0.84, 0.46)):
                Circle(0.02)
            # Profile area: 0.0012566371, perimeter: 0.1256637061
            with Locations((0.58, -0.27)):
                Circle(0.02)
            # Profile area: 0.0012566371, perimeter: 0.1256637061
            with Locations((0.5, 0.38)):
                Circle(0.02)
            # Profile area: 0.0012566371, perimeter: 0.1256637061
            with Locations((0.8, -0.56)):
                Circle(0.02)
            # Profile area: 0.0012566371, perimeter: 0.1256637061
            with Locations((0.05, 0.97)):
                Circle(0.02)
            # Profile area: 0.0012566371, perimeter: 0.1256637061
            with Locations((0.09, -0.65)):
                Circle(0.02)
            # Profile area: 0.0012566371, perimeter: 0.1256637061
            with Locations((-0.59, -0.24)):
                Circle(0.02)
            # Profile area: 0.0012566371, perimeter: 0.1256637061
            with Locations((-0.04, -1)):
                Circle(0.02)
            # Profile area: 0.0012566371, perimeter: 0.1256637061
            with Locations((0.51, -0.41)):
                Circle(0.02)
            # Profile area: 0.0012566371, perimeter: 0.1256637061
            with Locations((-0.53, -0.37)):
                Circle(0.02)
            # Profile area: 0.0012566371, perimeter: 0.1256637061
            with Locations((0.57, 0.26)):
                Circle(0.02)
            # Profile area: 0.0012566371, perimeter: 0.1256637061
            with Locations((-0.87, -0.43)):
                Circle(0.02)
            # Profile area: 0.0012566371, perimeter: 0.1256637061
            with Locations((0.08, 0.64)):
                Circle(0.02)
            # Profile area: 0.0012566371, perimeter: 0.1256637061
            with Locations((-0.72, 0.37)):
                Circle(0.02)
        # OneSide extrude, distance=0.16
        extrude(amount=0.16, mode=Mode.SUBTRACT)
    return part.part


def model_50821_9dfe2ba3_0005():
    """Model: Component6"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.81, perimeter: 3.6
            with BuildLine():
                Line((0.9, -0.9), (0, -0.9))
                Line((0.9, 0), (0.9, -0.9))
                Line((0, 0), (0.9, 0))
                Line((0, -0.9), (0, 0))
            make_face()
        # OneSide extrude, distance=2.6
        extrude(amount=2.6)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-0.45, 0.45)):
                Circle(0.25)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((0.45, 0.75)):
                Circle(0.25)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 9 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 2.08, perimeter: 10.4
            with BuildLine():
                Line((1.3, -0.4), (1.3, 1.3))
                Line((1.3, 1.3), (-0.4, 1.3))
                Line((-0.4, 1.3), (-0.4, -0.4))
                Line((-0.4, -0.4), (1.3, -0.4))
            make_face()
            with BuildLine():
                Line((0.9, 0.9), (0, 0.9))
                Line((0.9, 0), (0.9, 0.9))
                Line((0, 0), (0.9, 0))
                Line((0, 0.9), (0, 0))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.405, perimeter: 3.0727922061
            with BuildLine():
                Line((0, 0.9), (0, 0))
                Line((0, 0), (0.9, 0.9))
                Line((0.9, 0.9), (0, 0.9))
            make_face()
            # Profile area: 0.405, perimeter: 3.0727922061
            with BuildLine():
                Line((0, 0), (0.9, 0.9))
                Line((0, 0), (0.9, 0))
                Line((0.9, 0), (0.9, 0.9))
            make_face()
        # OneSide extrude, distance=0.15
        extrude(amount=0.15, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.34, perimeter: 3.8
            with BuildLine():
                Line((0.4, -0.2), (0.4, -0.4))
                Line((-1.3, -0.2), (0.4, -0.2))
                Line((-1.3, -0.4), (-1.3, -0.2))
                Line((0.4, -0.4), (-1.3, -0.4))
            make_face()
            # Profile area: 0.34, perimeter: 3.8
            with BuildLine():
                Line((-1.3, 1.1), (0.4, 1.1))
                Line((0.4, 1.1), (0.4, 1.3))
                Line((0.4, 1.3), (-1.3, 1.3))
                Line((-1.3, 1.3), (-1.3, 1.1))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


def model_51109_97b211c3_0001():
    """Model: gear shaft v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.3968123738, perimeter: 4.3994090512
            with BuildLine():
                Line((0.3666174209, 0.635), (-0.3666174209, 0.635))
                Line((-0.3666174209, 0.635), (-0.7332348419, 0))
                Line((-0.7332348419, 0), (-0.3666174209, -0.635))
                Line((-0.3666174209, -0.635), (0.3666174209, -0.635))
                Line((0.3666174209, -0.635), (0.7332348419, 0))
                Line((0.7332348419, 0), (0.3666174209, 0.635))
            make_face()
        # OneSide extrude, distance=4.445
        extrude(amount=4.445)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(4.445, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.7945984004, perimeter: 3.1599395547
            Circle(0.50292)
        # OneSide extrude, distance=0.0889
        extrude(amount=0.0889, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(4.5339, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.6022139733, perimeter: 7.5593486059
            with BuildLine():
                Line((0.7332348419, 0), (0.3666174209, 0.635))
                Line((0.3666174209, 0.635), (-0.3666174209, 0.635))
                Line((-0.3666174209, 0.635), (-0.7332348419, 0))
                Line((-0.7332348419, 0), (-0.3666174209, -0.635))
                Line((-0.3666174209, -0.635), (0.3666174209, -0.635))
                Line((0.3666174209, -0.635), (0.7332348419, 0))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.50292, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.7945984004, perimeter: 3.1599395547
            Circle(0.50292)
        # OneSide extrude, distance=0.0381
        extrude(amount=0.0381, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.7945984004, perimeter: 3.1599395547
            Circle(0.50292)
        # OneSide extrude, distance=0.0889
        extrude(amount=0.0889, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(-0.0889, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.6022139733, perimeter: 7.5593486059
            with BuildLine():
                Line((0.7332348419, 0), (0.3666174209, 0.635))
                Line((0.3666174209, 0.635), (-0.3666174209, 0.635))
                Line((-0.3666174209, 0.635), (-0.7332348419, 0))
                Line((-0.7332348419, 0), (-0.3666174209, -0.635))
                Line((-0.3666174209, -0.635), (0.3666174209, -0.635))
                Line((0.3666174209, -0.635), (0.7332348419, 0))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.50292, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.7945984004, perimeter: 3.1599395547
            Circle(0.50292)
        # OneSide extrude, distance=0.0381
        extrude(amount=0.0381, mode=Mode.ADD)
    return part.part


def model_51336_33ff2eba_0003():
    """Model: Hole Picker v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 11 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2513274123, perimeter: 2.5132741229
            with BuildLine():
                CenterArc((0, 0), 0.3, -48.6962410674, 140.2050600616)
                CenterArc((0, 0), 0.3, 91.5088189942, 219.7949399384)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1, 115.0756739308, 355.1014677411)
                CenterArc((0, 0), 0.1, 110.1771416719, 4.8985322589)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2633248212, perimeter: 3.4702471465
            with BuildLine():
                CenterArc((0.6478044029, -0.9203145455), 1.3, 77.4234152229, 20.6254128217)
                Line((-0.0078992447, 0.2998959852), (0.465782346, 0.3668792903))
                CenterArc((0, 0), 0.3, -48.6962410674, 140.2050600616)
                Line((0.2624542062, -0.1687477842), (0.1980152861, -0.2253662496))
                CenterArc((1.2855331846, -1.3331400738), 1.55, 102.8975832145, 28.406175718)
                Line((1.2344812765, 0.245287444), (0.9395592353, 0.177754372))
                Line((1.3934753308, 0.245287444), (1.2344812765, 0.245287444))
                Line((0.9308721133, 0.3484930331), (1.3934753308, 0.245287444))
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on XY construction plane
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0749999989, perimeter: 1.7000000164
            with BuildLine():
                Line((1.0000000149, 0.3), (0.2500000037, 0.3))
                Line((0.2500000037, 0.3), (0.2500000037, 0.200000003))
                Line((0.2500000037, 0.200000003), (1.0000000149, 0.200000003))
                Line((1.0000000149, 0.200000003), (1.0000000149, 0.3))
            make_face()
            # Profile area: 0.4930426026, perimeter: 4.5869506705
            with BuildLine():
                Line((1.0000000149, 0.200000003), (1.0000000149, 0.3))
                Line((0.2500000037, 0.200000003), (1.0000000149, 0.200000003))
                Line((0.2500000037, 0.3), (0.2500000037, 0.200000003))
                Line((0.2500000037, 0.3), (-0.5000000075, 0.3))
                Line((-0.5000000075, 0.3), (-0.5000000075, 0))
                Line((-0.5000000075, 0), (1.3934753308, 0))
                Line((1.3934753308, 0), (1.3934753308, 0.3))
                Line((1.3934753308, 0.3), (1.0000000149, 0.3))
            make_face()
        # OneSide extrude, distance=-1.25
        extrude(amount=-1.25, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on XY construction plane
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0749999989, perimeter: 1.7000000164
            with BuildLine():
                Line((1.0000000149, 0.3), (0.2500000037, 0.3))
                Line((0.2500000037, 0.3), (0.2500000037, 0.200000003))
                Line((0.2500000037, 0.200000003), (1.0000000149, 0.200000003))
                Line((1.0000000149, 0.200000003), (1.0000000149, 0.3))
            make_face()
            # Profile area: 0.4930426026, perimeter: 4.5869506705
            with BuildLine():
                Line((1.0000000149, 0.200000003), (1.0000000149, 0.3))
                Line((0.2500000037, 0.200000003), (1.0000000149, 0.200000003))
                Line((0.2500000037, 0.3), (0.2500000037, 0.200000003))
                Line((0.2500000037, 0.3), (-0.5000000075, 0.3))
                Line((-0.5000000075, 0.3), (-0.5000000075, 0))
                Line((-0.5000000075, 0), (1.3934753308, 0))
                Line((1.3934753308, 0), (1.3934753308, 0.3))
                Line((1.3934753308, 0.3), (1.0000000149, 0.3))
            make_face()
        # OneSide extrude, distance=0.9
        extrude(amount=0.9, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on XY construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.437500013, perimeter: 4.0000000596
            with BuildLine():
                Line((1.4000000209, 0.1000000015), (-0.3500000052, 0.1000000015))
                Line((1.4000000209, 0.3500000052), (1.4000000209, 0.1000000015))
                Line((-0.3500000052, 0.3500000052), (1.4000000209, 0.3500000052))
                Line((-0.3500000052, 0.1000000015), (-0.3500000052, 0.3500000052))
            make_face()
        # TwoSides extrude (symmetric), distance=0.95
        extrude(amount=0.95, both=True, mode=Mode.SUBTRACT)
    return part.part


def model_51336_33ff2eba_0006():
    """Model: WatchFace v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            Circle(2)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981868, perimeter: 3.1415927004
            with Locations((1.0000000149, -0.5000000075)):
                Circle(0.5000000075)
            # Profile area: 0.7853981868, perimeter: 3.1415927004
            with Locations((-1.0000000149, -0.5000000075)):
                Circle(0.5000000075)
        # OneSide extrude, distance=-1.8
        extrude(amount=-1.8, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0200000006, perimeter: 0.5656854334
            with BuildLine():
                Line((0, -1.7000000253), (-0.1000000015, -1.6000000238))
                Line((0.1000000015, -1.6000000238), (0, -1.7000000253))
                Line((0, -1.5000000224), (0.1000000015, -1.6000000238))
                Line((-0.1000000015, -1.6000000238), (0, -1.5000000224))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0314159275, perimeter: 0.6283185401
            Circle(0.1000000015)
        # OneSide extrude, distance=-1.9
        extrude(amount=-1.9, mode=Mode.SUBTRACT)
    return part.part


def model_51336_33ff2eba_0017():
    """Model: Watch Casing v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 35 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0683659323, perimeter: 2.2375042677
            with BuildLine():
                CenterArc((0, 0), 2.5, 0, 23.5781784782)
                Line((2.5, 1), (2.5, 0))
                Line((2.2912878475, 1), (2.5, 1))
            make_face()
            # Profile area: 7.0685834706, perimeter: 28.2743338823
            with BuildLine():
                CenterArc((0, 0), 2.5, 23.5781784782, 29.551923876)
                CenterArc((0, 0), 2.5, 53.1301023542, 73.7397952917)
                CenterArc((0, 0), 2.5, 126.8698976458, 29.551923876)
                CenterArc((0, 0), 2.5, 156.4218215218, 47.1563569564)
                CenterArc((0, 0), 2.5, -156.4218215218, 29.551923876)
                CenterArc((0, 0), 2.5, -126.8698976458, 73.7397952917)
                CenterArc((0, 0), 2.5, -53.1301023542, 29.551923876)
                CenterArc((0, 0), 2.5, -23.5781784782, 23.5781784782)
                CenterArc((0, 0), 2.5, 0, 23.5781784782)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0683659323, perimeter: 2.2375042677
            with BuildLine():
                CenterArc((0, 0), 2.5, -23.5781784782, 23.5781784782)
                Line((2.5, -1), (2.2912878475, -1))
                Line((2.5, 0), (2.5, -1))
            make_face()
            # Profile area: 1.1367318646, perimeter: 5.4750085354
            with BuildLine():
                Line((-2.5, 1), (-2.2912878475, 1))
                Line((-3, 1), (-2.5, 1))
                Line((-3, -1), (-3, 1))
                Line((-2.5, -1), (-3, -1))
                Line((-2.2912878475, -1), (-2.5, -1))
                CenterArc((0, 0), 2.5, 156.4218215218, 47.1563569564)
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 35 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.0338365114, perimeter: 5.0597108952
            with BuildLine():
                Line((2.2912878475, 1), (2.5, 1))
                Line((2.5, 1), (2, 3))
                Line((2, 3), (1.5, 3))
                Line((1.5, 3), (1.5, 2))
                CenterArc((0, 0), 2.5, 23.5781784782, 29.551923876)
            make_face()
            # Profile area: 1.0338365114, perimeter: 5.0597108952
            with BuildLine():
                Line((-1.5, 3), (-1.5, 2))
                Line((-2, 3), (-1.5, 3))
                Line((-2.5, 1), (-2, 3))
                Line((-2.5, 1), (-2.2912878475, 1))
                CenterArc((0, 0), 2.5, 126.8698976458, 29.551923876)
            make_face()
            # Profile area: 1.0338365114, perimeter: 5.0597108952
            with BuildLine():
                Line((-2.2912878475, -1), (-2.5, -1))
                Line((-2.5, -1), (-2, -3))
                Line((-2, -3), (-1.5, -3))
                Line((-1.5, -3), (-1.5, -2))
                CenterArc((0, 0), 2.5, -156.4218215218, 29.551923876)
            make_face()
            # Profile area: 1.0338365114, perimeter: 5.0597108952
            with BuildLine():
                Line((1.5, -3), (1.5, -2))
                Line((2, -3), (1.5, -3))
                Line((2.5, -1), (2, -3))
                Line((2.5, -1), (2.2912878475, -1))
                CenterArc((0, 0), 2.5, -53.1301023542, 29.551923876)
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 35 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.0338365114, perimeter: 5.0597108952
            with BuildLine():
                Line((2.2912878475, 1), (2.5, 1))
                Line((2.5, 1), (2, 3))
                Line((2, 3), (1.5, 3))
                Line((1.5, 3), (1.5, 2))
                CenterArc((0, 0), 2.5, 23.5781784782, 29.551923876)
            make_face()
            # Profile area: 1.0338365114, perimeter: 5.0597108952
            with BuildLine():
                Line((-1.5, 3), (-1.5, 2))
                Line((-2, 3), (-1.5, 3))
                Line((-2.5, 1), (-2, 3))
                Line((-2.5, 1), (-2.2912878475, 1))
                CenterArc((0, 0), 2.5, 126.8698976458, 29.551923876)
            make_face()
            # Profile area: 1.0338365114, perimeter: 5.0597108952
            with BuildLine():
                Line((-2.2912878475, -1), (-2.5, -1))
                Line((-2.5, -1), (-2, -3))
                Line((-2, -3), (-1.5, -3))
                Line((-1.5, -3), (-1.5, -2))
                CenterArc((0, 0), 2.5, -156.4218215218, 29.551923876)
            make_face()
            # Profile area: 1.0338365114, perimeter: 5.0597108952
            with BuildLine():
                Line((1.5, -3), (1.5, -2))
                Line((2, -3), (1.5, -3))
                Line((2.5, -1), (2, -3))
                Line((2.5, -1), (2.2912878475, -1))
                CenterArc((0, 0), 2.5, -53.1301023542, 29.551923876)
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.SUBTRACT)

        # Sketch1 -> Extrude4 (Join)
        # Sketch on XZ construction plane
        # Sketch has 35 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2500000205, perimeter: 2.000000082
            with BuildLine():
                Line((-2, -3), (-1.5, -3))
                Line((-2, -3), (-2, -3.5000000522))
                Line((-2, -3.5000000522), (-1.5000000224, -3.5000000522))
                Line((-1.5000000224, -3.5000000522), (-1.5, -3))
            make_face()
            # Profile area: 0.2500000335, perimeter: 2.0000001341
            with BuildLine():
                Line((2, -3), (1.5, -3))
                Line((1.5, -3), (1.5, -3.5000000522))
                Line((1.5, -3.5000000522), (2.0000000298, -3.5000000522))
                Line((2.0000000298, -3.5000000522), (2, -3))
            make_face()
            # Profile area: 0.2500000261, perimeter: 2.0000001043
            with BuildLine():
                Line((-2, 3), (-1.5, 3))
                Line((-1.5, 3), (-1.5, 3.5000000522))
                Line((-1.5, 3.5000000522), (-2, 3.5000000522))
                Line((-2, 3.5000000522), (-2, 3))
            make_face()
            # Profile area: 0.2500000261, perimeter: 2.0000001043
            with BuildLine():
                Line((2, 3), (2, 3.5000000522))
                Line((2, 3.5000000522), (1.5, 3.5000000522))
                Line((1.5, 3.5000000522), (1.5, 3))
                Line((2, 3), (1.5, 3))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch1 -> Extrude5 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 35 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2500000261, perimeter: 2.0000001043
            with BuildLine():
                Line((-2, 3), (-1.5, 3))
                Line((-1.5, 3), (-1.5, 3.5000000522))
                Line((-1.5, 3.5000000522), (-2, 3.5000000522))
                Line((-2, 3.5000000522), (-2, 3))
            make_face()
            # Profile area: 0.2500000261, perimeter: 2.0000001043
            with BuildLine():
                Line((2, 3), (2, 3.5000000522))
                Line((2, 3.5000000522), (1.5, 3.5000000522))
                Line((1.5, 3.5000000522), (1.5, 3))
                Line((2, 3), (1.5, 3))
            make_face()
            # Profile area: 0.2500000335, perimeter: 2.0000001341
            with BuildLine():
                Line((2, -3), (1.5, -3))
                Line((1.5, -3), (1.5, -3.5000000522))
                Line((1.5, -3.5000000522), (2.0000000298, -3.5000000522))
                Line((2.0000000298, -3.5000000522), (2, -3))
            make_face()
            # Profile area: 0.2500000205, perimeter: 2.000000082
            with BuildLine():
                Line((-2, -3), (-1.5, -3))
                Line((-2, -3), (-2, -3.5000000522))
                Line((-2, -3.5000000522), (-1.5000000224, -3.5000000522))
                Line((-1.5000000224, -3.5000000522), (-1.5, -3))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude6 (Cut)
        # Sketch on YZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1256637099, perimeter: 1.2566370802
            with Locations((-3.1000000462, 0.5000000075)):
                Circle(0.200000003)
            # Profile area: 0.1256637099, perimeter: 1.2566370802
            with Locations((3.1000000462, 0.5000000075)):
                Circle(0.200000003)
        # TwoSides extrude (symmetric), distance=6
        extrude(amount=6, both=True, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude7 (Cut)
        # Sketch on YZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.5026548396, perimeter: 2.5132741603
            with Locations((0, 0.7000000104)):
                Circle(0.400000006)
        # OneSide extrude, distance=-7.2
        extrude(amount=-7.2, mode=Mode.SUBTRACT)
    return part.part


def model_51345_4b292361_0000():
    """Model: Passive Handle v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 19.074064596, perimeter: 24.3513409532
            with BuildLine():
                Line((7, 0), (-0.1935757549, 0))
                CenterArc((-1.1935757549, 0), 1, 0, 180)
                CenterArc((0.0788493762, 0), 2.2724251311, 180, 61.6564808609)
                Line((7, -2), (-1, -2))
                Line((7, 0), (7, -2))
            make_face()
            with BuildLine():
                CenterArc((-1.1935757549, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.452
        extrude(amount=0.452)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.3505764853, perimeter: 4.9168484902
            with BuildLine():
                Line((0.1935757549, 0.15), (0.1935757549, 0.302))
                Line((0.1935757549, 0.15), (2.5, 0.15))
                Line((2.5, 0.15), (2.5, 0.302))
                Line((0.1935757549, 0.302), (2.5, 0.302))
            make_face()
            # Profile area: 1.0934235147, perimeter: 14.6911515098
            with BuildLine():
                Line((-7, 0.302), (0.1935757549, 0.302))
                Line((-7, 0.302), (-7, 0.15))
                Line((-7, 0.15), (0.1935757549, 0.15))
                Line((0.1935757549, 0.15), (0.1935757549, 0.302))
            make_face()
        # Symmetric extrude, each_side=1.8
        extrude(amount=1.8, both=True, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(7, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.225, perimeter: 3.3
            with BuildLine():
                Line((-2, 0.15), (-1.8, 0.15))
                Line((-2, 0.15), (-2, 0))
                Line((-2, 0), (-0.5, 0))
                Line((-0.5, 0.15), (-0.5, 0))
                Line((-1.8, 0.15), (-0.5, 0.15))
            make_face()
        # OneSide extrude, distance=8
        extrude(amount=8, mode=Mode.ADD)

        # Sketch8 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.452, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.3273228961, perimeter: 4.0840704497
            with Locations((-1.8064242451, 1)):
                Circle(0.65)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)
    return part.part


def model_51431_266a602e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch3 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 60, perimeter: 46
            with BuildLine():
                Line((27.5112205944, 0.949448248), (7.5112205944, 0.949448248))
                Line((27.5112205944, 3.949448248), (27.5112205944, 0.949448248))
                Line((7.5112205944, 3.949448248), (27.5112205944, 3.949448248))
                Line((7.5112205944, 0.949448248), (7.5112205944, 3.949448248))
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2)

        # Sketch10 -> Extrude5 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 450, perimeter: 90
            with BuildLine():
                Line((-32.5559187273, 48.9676310892), (-32.5559187273, 18.9676310892))
                Line((-32.5559187273, 18.9676310892), (-17.5559187273, 18.9676310892))
                Line((-17.5559187273, 18.9676310892), (-17.5559187273, 48.9676310892))
                Line((-17.5559187273, 48.9676310892), (-32.5559187273, 48.9676310892))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch11 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            with Locations((-25.0559187273, 41.4676310892)):
                Circle(1.5)
        # OneSide extrude, distance=5
        extrude(amount=5, mode=Mode.ADD)
    return part.part


def model_51574_5abe1279_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 52.25, perimeter: 30
            with BuildLine():
                Line((1.5, -5.5), (-4, -5.5))
                Line((1.5, 4), (1.5, -5.5))
                Line((-4, 4), (1.5, 4))
                Line((-4, -5.5), (-4, 4))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 32.8953991894, perimeter: 24.0264709184
            with BuildLine():
                Line((-0.7605834001, 4.4444468881), (3.4616416149, 4.4444468881))
                Line((-0.7605834001, -3.3465635562), (-0.7605834001, 4.4444468881))
                Line((3.4616416149, -3.3465635562), (-0.7605834001, -3.3465635562))
                Line((3.4616416149, 4.4444468881), (3.4616416149, -3.3465635562))
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3748961674, perimeter: 4.4692486355
            with BuildLine():
                Line((0.0104187604, -3.6482349727), (2.0623379453, -3.6482349727))
                Line((0.0104187604, -3.8309401056), (0.0104187604, -3.6482349727))
                Line((2.0623379453, -3.8309401056), (0.0104187604, -3.8309401056))
                Line((2.0623379453, -3.6482349727), (2.0623379453, -3.8309401056))
            make_face()
            # Profile area: 0.062053269, perimeter: 0.8830540051
            with Locations((2.9899178508, -3.8028316236)):
                Circle(0.1405424099)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 5.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0702236664, perimeter: 1.4190629905
            with BuildLine():
                Line((-1.25, 0.1811051265), (-1.8406366218, 0.1811051265))
                Line((-1.25, 0.3), (-1.25, 0.1811051265))
                Line((-1.8406366218, 0.3), (-1.25, 0.3))
                Line((-1.8406366218, 0.1811051265), (-1.8406366218, 0.3))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(1.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1450000043, perimeter: 3.1000000462
            with BuildLine():
                Line((1.6000000238, 0.200000003), (0.1500000022, 0.200000003))
                Line((1.6000000238, 0.3000000045), (1.6000000238, 0.200000003))
                Line((0.1500000022, 0.3000000045), (1.6000000238, 0.3000000045))
                Line((0.1500000022, 0.200000003), (0.1500000022, 0.3000000045))
            make_face()
            # Profile area: 0.0302832372, perimeter: 0.6168876571
            with Locations((-0.548941666, 0.2780041596)):
                Circle(0.09818072)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)
    return part.part


def model_51606_b72fa3d6_0019():
    """Model: Wheel Bar v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.8502295699, perimeter: 17.9542020153
            with BuildLine():
                CenterArc((0, 0), 1.5875, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.27, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=45.72
        extrude(amount=45.72)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 9 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 45.72, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.162131317, perimeter: 1.66744649
            with BuildLine():
                Line((-0.1580070864, 1.5796170456), (-0.1580070864, 2.0954998262))
                CenterArc((0, 0), 1.5875, 89.973186889, 5.7390360347)
                CenterArc((0, 0), 1.5875, 84.2338806953, 5.7393061937)
                Line((0.1594929136, 2.0954998262), (0.1594929136, 1.5794677143))
                Line((-0.1580070864, 2.0954998262), (0.1594929136, 2.0954998262))
            make_face()
            # Profile area: 0.0297449942, perimeter: 0.689254032
            with BuildLine():
                Line((0.0005051812, 1.0794998262), (0.0005943309, 1.2699998609))
                Line((0.1594929136, 1.0794998262), (0.0005051812, 1.0794998262))
                Line((0.1594929136, 1.2599452411), (0.1594929136, 1.0794998262))
                CenterArc((0, 0), 1.27, 82.7854616185, 7.1877252705)
            make_face()
            # Profile area: 0.0504836678, perimeter: 0.9550085816
            with BuildLine():
                Line((-0.1580070864, 1.2601324377), (-0.1580070864, 1.5796170456))
                CenterArc((0, 0), 1.27, 89.973186889, 7.1737888018)
                Line((0.0005943309, 1.2699998609), (0.0007429136, 1.5874998262))
                CenterArc((0, 0), 1.5875, 89.973186889, 5.7390360347)
            make_face()
            # Profile area: 0.0296862014, perimeter: 0.6886568526
            with BuildLine():
                Line((-0.1580070864, 1.0794998262), (-0.1580070864, 1.2601324377))
                Line((0.0005051812, 1.0794998262), (-0.1580070864, 1.0794998262))
                Line((0.0005051812, 1.0794998262), (0.0005943309, 1.2699998609))
                CenterArc((0, 0), 1.27, 89.973186889, 7.1737888018)
            make_face()
            # Profile area: 0.0505338196, perimeter: 0.9553628437
            with BuildLine():
                Line((0.0005943309, 1.2699998609), (0.0007429136, 1.5874998262))
                CenterArc((0, 0), 1.27, 82.7854616185, 7.1877252705)
                Line((0.1594929136, 1.5794677143), (0.1594929136, 1.2599452411))
                CenterArc((0, 0), 1.5875, 84.2338806953, 5.7393061937)
            make_face()
        # OneSide extrude, distance=-1.27
        extrude(amount=-1.27, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude3 (Join)
        # Sketch on YZ construction plane
        # Sketch has 6 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 31.1024076654, perimeter: 25.9689747087
            with BuildLine():
                Line((-1.905, 1.27), (-1.905, -6.35))
                CenterArc((-0.3589649174, -6.35), 1.5460350826, 180, 180)
                Line((1.9050000608, -2.54), (1.1870701651, -6.35))
                Line((1.9050000608, 1.27), (1.9050000608, -2.54))
                Line((-1.905, 1.27), (1.9050000608, 1.27))
            make_face()
            with BuildLine():
                CenterArc((-0.3589649174, -6.35), 0.3175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=2.032
        extrude(amount=2.032, both=True, mode=Mode.ADD)

        # Sketch5 -> Extrude4 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 29.8927326461, perimeter: 25.3339747087
            with BuildLine():
                CenterArc((-0.3589649174, -6.35), 1.5460350826, 180, 180)
                Line((1.1870701651, -6.35), (1.9050000608, -2.54))
                Line((1.9050000608, -2.54), (1.9050000608, 0.9525))
                Line((1.9050000608, 0.9525), (-1.905, 0.9525))
                Line((-1.905, 0.9525), (-1.905, -6.35))
            make_face()
            with BuildLine():
                CenterArc((-0.3589649174, -6.35), 0.3175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with Locations((-0.3589649174, -6.35)):
                Circle(0.3175)
        # Symmetric extrude, each_side=1.5875
        extrude(amount=1.5875, both=True, mode=Mode.SUBTRACT)
    return part.part


def model_51766_7e02ec47_0001():
    """Model: pcb"""
    with BuildPart() as part:
        # board_outline -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 3.8155789916, perimeter: 7.437929068
            with BuildLine():
                CenterArc((0.254, 0.254), 0.254, 180, 90)
                Line((1.778, 0), (0.254, 0))
                CenterArc((1.778, 0.254), 0.254, -90, 90)
                Line((2.032, 1.651), (2.032, 0.254))
                CenterArc((1.778, 1.651), 0.254, 0, 90)
                Line((0.254, 1.905), (1.778, 1.905))
                CenterArc((0.254, 1.651), 0.254, 90, 90)
                Line((0, 0.254), (0, 1.651))
            make_face()
        # OneSide extrude, distance=0.16
        extrude(amount=0.16)

        # Drills - holes -> Extrude2 (Cut)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.003848451, perimeter: 0.2199114858
            with Locations((0.4318, 1.1475)):
                Circle(0.035)
            # Profile area: 0.003848451, perimeter: 0.2199114858
            with Locations((0.4318, 0.7575)):
                Circle(0.035)
        # OneSide extrude, distance=0.16
        extrude(amount=0.16, mode=Mode.SUBTRACT)

        # Drills - pads -> Extrude3 (Cut)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0028274334, perimeter: 0.1884955592
            with Locations((0.2418, 1.3125)):
                Circle(0.03)
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((1.397, 1.651)):
                Circle(0.05)
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((0.889, 1.651)):
                Circle(0.05)
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((1.143, 1.651)):
                Circle(0.05)
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((0.635, 1.651)):
                Circle(0.05)
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            with Locations((0.254, 0.254)):
                Circle(0.125)
            # Profile area: 0.0028274334, perimeter: 0.1884955592
            with Locations((0.2418, 0.5925)):
                Circle(0.03)
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            with Locations((0.254, 1.651)):
                Circle(0.125)
            # Profile area: 0.003848451, perimeter: 0.2199114858
            with Locations((0.5218, 1.2825)):
                Circle(0.035)
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            with Locations((1.778, 0.254)):
                Circle(0.125)
            # Profile area: 0.003848451, perimeter: 0.2199114858
            with Locations((0.5218, 0.6225)):
                Circle(0.035)
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            with Locations((1.778, 1.651)):
                Circle(0.125)
        # OneSide extrude, distance=0.16
        extrude(amount=0.16, mode=Mode.SUBTRACT)

        # Drills - vias -> Extrude4 (Cut)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0012173647, perimeter: 0.1236845028
            with Locations((0.0762, 1.1303)):
                Circle(0.019685)
            # Profile area: 0.0012173647, perimeter: 0.1236845028
            with Locations((1.4097, 1.1811)):
                Circle(0.019685)
            # Profile area: 0.0012173647, perimeter: 0.1236845028
            with Locations((0.8255, 1.0795)):
                Circle(0.019685)
            # Profile area: 0.0012173647, perimeter: 0.1236845028
            with Locations((1.7526, 1.1176)):
                Circle(0.019685)
            # Profile area: 0.0012173647, perimeter: 0.1236845028
            with Locations((1.4732, 0.4572)):
                Circle(0.019685)
            # Profile area: 0.0012173647, perimeter: 0.1236845028
            with Locations((0.9398, 0.254)):
                Circle(0.019685)
            # Profile area: 0.0012173647, perimeter: 0.1236845028
            with Locations((0.7112, 1.0922)):
                Circle(0.019685)
            # Profile area: 0.0012173647, perimeter: 0.1236845028
            with Locations((1.5494, 0.7112)):
                Circle(0.019685)
            # Profile area: 0.0012173647, perimeter: 0.1236845028
            with Locations((0.9398, 0.1397)):
                Circle(0.019685)
            # Profile area: 0.0012173647, perimeter: 0.1236845028
            with Locations((0.8382, 0.9017)):
                Circle(0.019685)
            # Profile area: 0.0012173647, perimeter: 0.1236845028
            with Locations((1.2827, 1.4224)):
                Circle(0.019685)
        # OneSide extrude, distance=0.16
        extrude(amount=0.16, mode=Mode.SUBTRACT)
    return part.part


def model_51775_49ef614a_0001():
    """Model: zarowka_plastik"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0100000003, perimeter: 0.5000000075
            with BuildLine():
                Line((-0.200000003, -0.1000000015), (-0.2500000037, -0.1000000015))
                Line((-0.200000003, 0.1000000015), (-0.200000003, -0.1000000015))
                Line((-0.2500000037, 0.1000000015), (-0.200000003, 0.1000000015))
                Line((-0.2500000037, -0.1000000015), (-0.2500000037, 0.1000000015))
            make_face()
            # Profile area: 0.0100000003, perimeter: 0.5000000075
            with BuildLine():
                Line((0.2500000037, -0.1000000015), (0.200000003, -0.1000000015))
                Line((0.2500000037, 0.1000000015), (0.2500000037, -0.1000000015))
                Line((0.200000003, 0.1000000015), (0.2500000037, 0.1000000015))
                Line((0.200000003, -0.1000000015), (0.200000003, 0.1000000015))
            make_face()
        # OneSide extrude, distance=-1.3
        extrude(amount=-1.3, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.482654824, perimeter: 3.5132741378
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face()
            with BuildLine():
                Line((-0.2500000037, 0.1000000015), (-0.200000003, 0.1000000015))
                Line((-0.200000003, 0.1000000015), (-0.200000003, -0.1000000015))
                Line((-0.200000003, -0.1000000015), (-0.2500000037, -0.1000000015))
                Line((-0.2500000037, -0.1000000015), (-0.2500000037, 0.1000000015))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((0.200000003, 0.1000000015), (0.2500000037, 0.1000000015))
                Line((0.2500000037, 0.1000000015), (0.2500000037, -0.1000000015))
                Line((0.2500000037, -0.1000000015), (0.200000003, -0.1000000015))
                Line((0.200000003, -0.1000000015), (0.200000003, 0.1000000015))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.00001
        extrude(amount=-0.00001, mode=Mode.SUBTRACT)
    return part.part


def model_51775_49ef614a_0006():
    """Model: teleskop3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=13
        extrude(amount=13)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 13, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2199114858, perimeter: 4.398229715
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on XY construction plane
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0799999815, perimeter: 1.7999996096
            with BuildLine():
                Line((0, 13.2000001967), (0, 14))
                Line((0.1000000015, 13.2000001967), (0, 13.2000001967))
                Line((0.1000000015, 14), (0.1000000015, 13.2000001967))
                Line((0.1000000015, 14), (0, 14))
            make_face()
            # Profile area: 0.0799999815, perimeter: 1.7999996096
            with BuildLine():
                Line((-0.1000000015, 14), (-0.1000000015, 13.2000001967))
                Line((-0.1000000015, 13.2000001967), (0, 13.2000001967))
                Line((0, 13.2000001967), (0, 14))
                Line((0, 14), (-0.1000000015, 14))
            make_face()
        # Symmetric extrude, each_side=1.1
        extrude(amount=1.1, both=True, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.1000000015, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((0, 13.6000002027)):
                Circle(0.15)
        # Symmetric extrude, each_side=1.3
        extrude(amount=1.3, both=True, mode=Mode.SUBTRACT)
    return part.part


def model_51871_86ebf5b2_0005():
    """Model: Mounting Rack v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 87.9, perimeter: 351.6
            with BuildLine():
                Line((59.69, -29.21), (0, -29.21))
                Line((59.69, 0), (59.69, -29.21))
                Line((0, 0), (59.69, 0))
                Line((0, -29.21), (0, 0))
            make_face()
            with BuildLine():
                Line((0.5, -28.71), (59.19, -28.71))
                Line((0.5, -0.5), (0.5, -28.71))
                Line((59.19, -0.5), (0.5, -0.5))
                Line((59.19, -28.71), (59.19, -0.5))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1655.6449, perimeter: 173.8
            with BuildLine():
                Line((59.19, -28.71), (59.19, -0.5))
                Line((59.19, -0.5), (0.5, -0.5))
                Line((0.5, -0.5), (0.5, -28.71))
                Line((0.5, -28.71), (59.19, -28.71))
            make_face()
        # OneSide extrude, distance=10
        extrude(amount=10)

        # Sketch1 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1655.6449, perimeter: 173.8
            with BuildLine():
                Line((59.19, -28.71), (59.19, -0.5))
                Line((59.19, -0.5), (0.5, -0.5))
                Line((0.5, -0.5), (0.5, -28.71))
                Line((0.5, -28.71), (59.19, -28.71))
            make_face()
        # OneSide extrude, distance=25
        extrude(amount=25, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 29.21), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 2.4543692606, perimeter: 6.426990817
            with BuildLine():
                Line((11.095, 5), (13.595, 5))
                CenterArc((12.345, 5), 1.25, 180, 180)
            make_face()
            # Profile area: 2.4543692606, perimeter: 6.426990817
            with BuildLine():
                CenterArc((12.345, 5), 1.25, 0, 180)
                Line((11.095, 5), (13.595, 5))
            make_face()
            # Profile area: 2.4543692606, perimeter: 6.426990817
            with BuildLine():
                CenterArc((29.845, 5), 1.25, 0, 180)
                Line((28.595, 5), (31.095, 5))
            make_face()
            # Profile area: 2.4543692606, perimeter: 6.426990817
            with BuildLine():
                Line((28.595, 5), (31.095, 5))
                CenterArc((29.845, 5), 1.25, 180, 180)
            make_face()
            # Profile area: 2.4543692606, perimeter: 6.426990817
            with BuildLine():
                CenterArc((47.345, 5), 1.25, 0, 180)
                Line((46.095, 5), (48.595, 5))
            make_face()
            # Profile area: 2.4543692606, perimeter: 6.426990817
            with BuildLine():
                Line((46.095, 5), (48.595, 5))
                CenterArc((47.345, 5), 1.25, 180, 180)
            make_face()
        # OneSide extrude, distance=-5
        extrude(amount=-5, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 29.21), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.251768586, perimeter: 1.8275281213
            with BuildLine():
                CenterArc((1.5, 10.200000152), 0.3, -41.8103538413, 263.6207076827)
                Line((1.7236066618, 10), (1.2763933382, 10))
            make_face()
            # Profile area: 0.0309747528, perimeter: 0.9518541181
            with BuildLine():
                Line((1.7236066618, 10), (1.2763933382, 10))
                CenterArc((1.5, 10.200000152), 0.3, -138.1896461587, 96.3792923173)
            make_face()
        # OneSide extrude, distance=-1.9
        extrude(amount=-1.9, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude6 (Join)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 135.252, perimeter: 340.4
            with BuildLine():
                Line((59.19, -28.71), (0.5, -28.71))
                Line((59.19, -0.5), (59.19, -28.71))
                Line((0.5, -0.5), (59.19, -0.5))
                Line((0.5, -28.71), (0.5, -0.5))
            make_face()
            with BuildLine():
                Line((57.99, -1.1), (57.99, -28.11))
                Line((57.99, -28.11), (1.7, -28.11))
                Line((1.7, -28.11), (1.7, -1.1))
                Line((1.7, -1.1), (57.99, -1.1))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=8.6
        extrude(amount=8.6, mode=Mode.ADD)

        # Sketch3 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 29.21), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 4.9087385212, perimeter: 7.853981634
            with Locations((12.345, 5)):
                Circle(1.25)
            # Profile area: 4.9087385212, perimeter: 7.853981634
            with Locations((29.845, 5)):
                Circle(1.25)
            # Profile area: 4.9087385212, perimeter: 7.853981634
            with Locations((47.345, 5)):
                Circle(1.25)
        # OneSide extrude, distance=-5
        extrude(amount=-5, mode=Mode.SUBTRACT)
    return part.part


def model_51871_86ebf5b2_0012():
    """Model: Bucket v5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1858.0608, perimeter: 182.88
            with BuildLine():
                Line((0, -30.48), (0, 0))
                Line((0, 0), (-60.96, 0))
                Line((-60.96, 0), (-60.96, -30.48))
                Line((-60.96, -30.48), (0, -30.48))
            make_face()
        # OneSide extrude, distance=20.32
        extrude(amount=20.32)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 20.32, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1743.5449, perimeter: 177.8
            with BuildLine():
                Line((0.635, 29.845), (60.325, 29.845))
                Line((0.635, 0.635), (0.635, 29.845))
                Line((60.325, 0.635), (0.635, 0.635))
                Line((60.325, 29.845), (60.325, 0.635))
            make_face()
        # OneSide extrude, distance=-19.685
        extrude(amount=-19.685, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.1413716694, perimeter: 1.5424777961
            with BuildLine():
                CenterArc((18, 19.12), 0.3, 0, 180)
                Line((17.7, 19.12), (18.3, 19.12))
            make_face()
            # Profile area: 0.1413716694, perimeter: 1.5424777961
            with BuildLine():
                Line((17.7, 19.12), (18.3, 19.12))
                CenterArc((18, 19.12), 0.3, 180, 180)
            make_face()
            # Profile area: 0.1413716694, perimeter: 1.5424777961
            with BuildLine():
                CenterArc((21, 19.12), 0.3, 0, 180)
                Line((20.7, 19.12), (21.3, 19.12))
            make_face()
            # Profile area: 0.1413716694, perimeter: 1.5424777961
            with BuildLine():
                Line((20.7, 19.12), (21.3, 19.12))
                CenterArc((21, 19.12), 0.3, 180, 180)
            make_face()
            # Profile area: 0.1413716694, perimeter: 1.5424777961
            with BuildLine():
                CenterArc((41, 19.12), 0.3, 0, 180)
                Line((40.7, 19.12), (41.3, 19.12))
            make_face()
            # Profile area: 0.1413716694, perimeter: 1.5424777961
            with BuildLine():
                Line((40.7, 19.12), (41.3, 19.12))
                CenterArc((41, 19.12), 0.3, 180, 180)
            make_face()
            # Profile area: 0.1413716694, perimeter: 1.5424777961
            with BuildLine():
                Line((43.7, 19.12), (44.3, 19.12))
                CenterArc((44, 19.12), 0.3, 180, 180)
            make_face()
            # Profile area: 0.1413716694, perimeter: 1.5424777961
            with BuildLine():
                CenterArc((44, 19.12), 0.3, 0, 180)
                Line((43.7, 19.12), (44.3, 19.12))
            make_face()
        # OneSide extrude, distance=-1.1
        extrude(amount=-1.1, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 30.48), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.5654866776, perimeter: 3.0849555922
            with BuildLine():
                CenterArc((-47.46, 12.82), 0.6, 0, 180)
                Line((-48.06, 12.82), (-46.86, 12.82))
            make_face()
            # Profile area: 0.5654866776, perimeter: 3.0849555922
            with BuildLine():
                Line((-48.06, 12.82), (-46.86, 12.82))
                CenterArc((-47.46, 12.82), 0.6, 180, 180)
            make_face()
            # Profile area: 0.5654866776, perimeter: 3.0849555922
            with BuildLine():
                CenterArc((-29.96, 12.82), 0.6, 0, 180)
                Line((-30.56, 12.82), (-29.36, 12.82))
            make_face()
            # Profile area: 0.5654866776, perimeter: 3.0849555922
            with BuildLine():
                Line((-30.56, 12.82), (-29.36, 12.82))
                CenterArc((-29.96, 12.82), 0.6, 180, 180)
            make_face()
            # Profile area: 0.5654866776, perimeter: 3.0849555922
            with BuildLine():
                Line((-13.06, 12.82), (-11.86, 12.82))
                CenterArc((-12.46, 12.82), 0.6, 180, 180)
            make_face()
            # Profile area: 0.5654866776, perimeter: 3.0849555922
            with BuildLine():
                CenterArc((-12.46, 12.82), 0.6, 0, 180)
                Line((-13.06, 12.82), (-11.86, 12.82))
            make_face()
        # OneSide extrude, distance=-5
        extrude(amount=-5, mode=Mode.SUBTRACT)
    return part.part


def model_51891_9455ea02_0006():
    """Model: DC Motor Holder DC v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 22.5806, perimeter: 22.86
            with BuildLine():
                Line((1.27, -4.445), (-1.27, -4.445))
                Line((1.27, 4.445), (1.27, -4.445))
                Line((-1.27, 4.445), (1.27, 4.445))
                Line((-1.27, -4.445), (-1.27, 4.445))
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1.27, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 29.0322, perimeter: 22.86
            with BuildLine():
                Line((0.635, 0.635), (0.635, 8.255))
                Line((0.635, 8.255), (-3.175, 8.255))
                Line((-3.175, 8.255), (-3.175, 0.635))
                Line((-3.175, 0.635), (0.635, 0.635))
            make_face()
        # OneSide extrude, distance=-2.54
        extrude(amount=-2.54, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1.27, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 6.9957301333, perimeter: 9.3760832746
            with Locations((-1.27, 6.35)):
                Circle(1.49225)
        # OneSide extrude, distance=-5.842
        extrude(amount=-5.842, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.635, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1946567452, perimeter: 1.5640104867
            with Locations((0, -3.175)):
                Circle(0.24892)
            # Profile area: 0.1946567452, perimeter: 1.5640104867
            with Locations((0, 3.81)):
                Circle(0.24892)
        # OneSide extrude, distance=-1.016
        extrude(amount=-1.016, mode=Mode.SUBTRACT)
    return part.part


def model_52024_97da327b_0011():
    """Model: Top Limb"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 42.7959587106, perimeter: 82.1714577917
            with BuildLine():
                CenterArc((9.905999485, 15.24), 22.6059992943, 115.9892330037, 64.0107669963)
                Line((-12.6999998093, 0), (-12.6999998093, 15.24))
                Line((-12.6999998093, 0), (-11.4299998093, 0))
                Line((-11.4299998093, 0), (-11.4299998093, 15.2399997711))
                CenterArc((8.7695598904, 16.2826645377), 20.2264520338, 114.3647430153, 68.5901390725)
                Line((0, 35.5599994659), (0.4252592305, 34.7077020784))
            make_face()
        # OneSide extrude, distance=7.62
        extrude(amount=7.62)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-12.6999998093, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 28.3399373955, perimeter: 26.8498226701
            with BuildLine():
                Line((0, 5.0800001621), (-10.16, 5.0800001621))
                CenterArc((-10.16, 3.8100001621), 1.27, 90, 180)
                Line((-10.16, 2.5400001621), (0, 2.5400001621))
                Line((0, 2.5400001621), (0, 5.0800001621))
            make_face()
        # OneSide extrude, distance=-1.905
        extrude(amount=-1.905, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-12.6999998093, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 6.4046529945, perimeter: 15.1486820279
            with BuildLine():
                Line((-35.5599994659, 4.28625), (-35.5599994659, 3.33375))
                Line((-35.5599994659, 3.33375), (-29.2099994659, 3.33375))
                CenterArc((-29.2100001991, 3.81), 0.47625, -89.9999117991, 179.9999991462)
                Line((-35.5599994659, 4.28625), (-29.2100009251, 4.28625))
            make_face()
        # OneSide extrude, distance=-15.24
        extrude(amount=-15.24, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 7.62, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0791730436, perimeter: 0.9974556675
            with Locations((1.1430000365, -34.4170010984)):
                Circle(0.15875)
        # OneSide extrude, distance=-10.16
        extrude(amount=-10.16, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-12.6999998093, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 1.4398342035, perimeter: 4.5349111061
            with BuildLine():
                Line((-15.2399997711, 4.445), (-15.24, 3.175))
                Line((-14.605, 3.1749998856), (-15.24, 3.175))
                CenterArc((-14.605, 3.8099998856), 0.635, -90, 180)
                Line((-14.605, 4.4449998856), (-15.2399997711, 4.445))
            make_face()
            # Profile area: 13.5244737602, perimeter: 23.5658395419
            with BuildLine():
                Line((-25.390463989, 4.445), (-15.2399997711, 4.445))
                CenterArc((-25.390463989, 3.81), 0.635, 90, 180)
                Line((-15.24, 3.175), (-25.390463989, 3.175))
                Line((-15.2399997711, 4.445), (-15.24, 3.175))
            make_face()
        # OneSide extrude, distance=-15.24
        extrude(amount=-15.24, mode=Mode.SUBTRACT)
    return part.part


def model_52035_0244dcd2_0006():
    """Model: Tuners"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.2028272095, perimeter: 5.6762918559
            with BuildLine():
                Line((50.0000621354, 8.1080001043), (50.0000621354, 7.0000001043))
                Line((50.0000621354, 7.0000001043), (51.3460621354, 7.0000001043))
                Line((51.3460621354, 7.0000001043), (51.3460621354, 8.1080001043))
                CenterArc((50.6730621354, 8.1080001043), 0.673, 0, 180)
            make_face()
        # OneSide extrude, distance=0.9525
        extrude(amount=0.9525)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.9525, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7313824047, perimeter: 3.0316369107
            with Locations((-50.6730621354, -8.1080001043)):
                Circle(0.4825)
        # OneSide extrude, distance=0.5715
        extrude(amount=0.5715, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.524, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3066390981, perimeter: 1.9629927537
            with Locations((-50.6730621354, -8.1080001043)):
                Circle(0.31242)
        # OneSide extrude, distance=1.27
        extrude(amount=1.27, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.794, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1883860493, perimeter: 1.5386126591
            with Locations((-50.6730621354, -8.1080001043)):
                Circle(0.2448778102)
        # OneSide extrude, distance=0.15875
        extrude(amount=0.15875, mode=Mode.ADD)
    return part.part


MODELS = {
    "model_43928_6ca53538_0014": {"func": model_43928_6ca53538_0014, "volume": 0.0280420304, "area": 0.9140576878},
    "model_43928_6ca53538_0018": {"func": model_43928_6ca53538_0018, "volume": 0.0220061539, "area": 1.9048951828},
    "model_43928_6ca53538_0029": {"func": model_43928_6ca53538_0029, "volume": 0.8980124791, "area": 8.5977536947},
    "model_43928_6ca53538_0033": {"func": model_43928_6ca53538_0033, "volume": 0.1525278576, "area": 2.6689400389},
    "model_43932_4bfdfe7b_0008": {"func": model_43932_4bfdfe7b_0008, "volume": 13349.6481412223, "area": 4442.555578898},
    "model_43932_4bfdfe7b_0009": {"func": model_43932_4bfdfe7b_0009, "volume": 71.692260627, "area": 291.1140206197},
    "model_43934_912ff891_0000": {"func": model_43934_912ff891_0000, "volume": 0.4402156706, "area": 3.9505527619},
    "model_43934_912ff891_0001": {"func": model_43934_912ff891_0001, "volume": 0.8558403491, "area": 11.6652073963},
    "model_43934_912ff891_0021": {"func": model_43934_912ff891_0021, "volume": 4.0260652026, "area": 22.9563998168},
    "model_43934_912ff891_0026": {"func": model_43934_912ff891_0026, "volume": 1.0821809973, "area": 12.695590382},
    "model_43934_912ff891_0028": {"func": model_43934_912ff891_0028, "volume": 2.2992577563, "area": 15.0726215617},
    "model_44021_f141414b_0006": {"func": model_44021_f141414b_0006, "volume": 91.131319036, "area": 487.1599536593},
    "model_44221_25c62f03_0000": {"func": model_44221_25c62f03_0000, "volume": 183.6940148417, "area": 409.4189463786},
    "model_44328_8b922c11_0000": {"func": model_44328_8b922c11_0000, "volume": 606.0517721146, "area": 707.9195187702},
    "model_44363_b199af8c_0000": {"func": model_44363_b199af8c_0000, "volume": 33.7721210261, "area": 136.6592804312},
    "model_44392_ced313da_0000": {"func": model_44392_ced313da_0000, "volume": 0.037863591, "area": 4.0614684483},
    "model_44399_86308373_0000": {"func": model_44399_86308373_0000, "volume": 58.2836225927, "area": 162.1130319783},
    "model_44407_e4543694_0000": {"func": model_44407_e4543694_0000, "volume": 18.7655862713, "area": 87.3980087318},
    "model_44541_cefe3e4c_0000": {"func": model_44541_cefe3e4c_0000, "volume": 23.6836332547, "area": 194.0278419941},
    "model_44646_300a8b20_0000": {"func": model_44646_300a8b20_0000, "volume": 37.3731517755, "area": 143.9509236772},
    "model_45303_48d14b32_0005": {"func": model_45303_48d14b32_0005, "volume": 667.2070098428, "area": 1911.898064199},
    "model_45303_48d14b32_0017": {"func": model_45303_48d14b32_0017, "volume": 1664.8431599933, "area": 1506.97227461},
    "model_45359_1768ab3f_0034": {"func": model_45359_1768ab3f_0034, "volume": 1.0948450398, "area": 6.6915923521},
    "model_45360_cb4bac3f_0015": {"func": model_45360_cb4bac3f_0015, "volume": 53.0918872785, "area": 172.5075615115},
    "model_45360_cb4bac3f_0016": {"func": model_45360_cb4bac3f_0016, "volume": 10.1826871884, "area": 33.2066343484},
    "model_45424_63abf99e_0000": {"func": model_45424_63abf99e_0000, "volume": 6736.7609767567, "area": 9508.0763416086},
    "model_45806_2c8651cd_0000": {"func": model_45806_2c8651cd_0000, "volume": 206.6719795983, "area": 259.5586842899},
    "model_45819_28cdbf87_0000": {"func": model_45819_28cdbf87_0000, "volume": 113.2670745537, "area": 305.2848398429},
    "model_45922_26941172_0003": {"func": model_45922_26941172_0003, "volume": 26.7134954085, "area": 127.9247779608},
    "model_46086_371b5052_0009": {"func": model_46086_371b5052_0009, "volume": 1.2143309622, "area": 17.9134321077},
    "model_47799_8b49af01_0000": {"func": model_47799_8b49af01_0000, "volume": 5.5714287628, "area": 34.8605155844},
    "model_47878_0edb6829_0000": {"func": model_47878_0edb6829_0000, "volume": 12.4145971556, "area": 58.490331469},
    "model_48077_2cfc0eaa_0000": {"func": model_48077_2cfc0eaa_0000, "volume": 57.1550141254, "area": 172.5926362199},
    "model_48224_53cae924_0012": {"func": model_48224_53cae924_0012, "volume": 292.9544697381, "area": 558.0644174483},
    "model_48332_fb679f90_0006": {"func": model_48332_fb679f90_0006, "volume": 11.9813980381, "area": 98.0262522246},
    "model_48724_70685a9d_0007": {"func": model_48724_70685a9d_0007, "volume": 47.9018252296, "area": 208.1006623496},
    "model_48907_25974aa4_0003": {"func": model_48907_25974aa4_0003, "volume": 0.6127410152, "area": 11.6546627784},
    "model_48907_25974aa4_0006": {"func": model_48907_25974aa4_0006, "volume": 2.4848862368, "area": 30.6840574318},
    "model_48907_25974aa4_0009": {"func": model_48907_25974aa4_0009, "volume": 0.6911355793, "area": 6.1090504354},
    "model_49017_b6231068_0001": {"func": model_49017_b6231068_0001, "volume": 5.8339375982, "area": 28.148670472},
    "model_49024_b7f02205_0022": {"func": model_49024_b7f02205_0022, "volume": 922.6040809503, "area": 789.9317921802},
    "model_49116_4bd17b23_0000": {"func": model_49116_4bd17b23_0000, "volume": 114.3380086799, "area": 299.1353078215},
    "model_49145_4a5b250e_0000": {"func": model_49145_4a5b250e_0000, "volume": 13.7209059146, "area": 52.7159247272},
    "model_49591_0b6b6dde_0000": {"func": model_49591_0b6b6dde_0000, "volume": 242.7661201818, "area": 320.9440889565},
    "model_49613_1b97c07b_0002": {"func": model_49613_1b97c07b_0002, "volume": 30.5663706144, "area": 73.1327412287},
    "model_49695_28e7f7e5_0000": {"func": model_49695_28e7f7e5_0000, "volume": 61.4258684653, "area": 216.0437388301},
    "model_49901_cd5499cd_0000": {"func": model_49901_cd5499cd_0000, "volume": 170.7790270885, "area": 237.3636191003},
    "model_50379_ebec8fae_0003": {"func": model_50379_ebec8fae_0003, "volume": 644.5508772177, "area": 1638.5650249096},
    "model_50711_05fbe39a_0000": {"func": model_50711_05fbe39a_0000, "volume": 7.7964936689, "area": 55.7466900816},
    "model_50777_2934de55_0001": {"func": model_50777_2934de55_0001, "volume": 8.1050864684, "area": 64.4143961343},
    "model_50784_bb6b362c_0001": {"func": model_50784_bb6b362c_0001, "volume": 0.6431451934, "area": 9.9735743502},
    "model_50821_9dfe2ba3_0005": {"func": model_50821_9dfe2ba3_0005, "volume": 2.3809756887, "area": 20.0361944902},
    "model_51109_97b211c3_0001": {"func": model_51109_97b211c3_0001, "volume": 6.4565476999, "area": 25.6549260961},
    "model_51336_33ff2eba_0003": {"func": model_51336_33ff2eba_0003, "volume": 0.1286630557, "area": 2.1581287718},
    "model_51336_33ff2eba_0006": {"func": model_51336_33ff2eba_0006, "volume": 1.0984158314, "area": 23.9326726254},
    "model_51336_33ff2eba_0017": {"func": model_51336_33ff2eba_0017, "volume": 16.374840868, "area": 86.0625229144},
    "model_51345_4b292361_0000": {"func": model_51345_4b292361_0000, "volume": 7.5712826369, "area": 107.2594941593},
    "model_51431_266a602e_0000": {"func": model_51431_266a602e_0000, "volume": 1055.3429173529, "area": 1339.1238898038},
    "model_51574_5abe1279_0000": {"func": model_51574_5abe1279_0000, "volume": 22.6953748515, "area": 124.7638593808},
    "model_51606_b72fa3d6_0019": {"func": model_51606_b72fa3d6_0019, "volume": 158.0551707749, "area": 969.3539603795},
    "model_51766_7e02ec47_0001": {"func": model_51766_7e02ec47_0001, "volume": 0.5685398147, "area": 9.4192797431},
    "model_51775_49ef614a_0001": {"func": model_51775_49ef614a_0001, "volume": 0.2413225854, "area": 2.7219115841},
    "model_51775_49ef614a_0006": {"func": model_51775_49ef614a_0006, "volume": 4.0102577953, "area": 29.1918000738},
    "model_51871_86ebf5b2_0005": {"func": model_51871_86ebf5b2_0005, "volume": 2025.9528755035, "area": 3896.8164724945},
    "model_51871_86ebf5b2_0012": {"func": model_51871_86ebf5b2_0012, "volume": 3431.2414271776, "area": 10935.1578811678},
    "model_51891_9455ea02_0006": {"func": model_51891_9455ea02_0006, "volume": 70.0641003951, "area": 167.4827575884},
    "model_52024_97da327b_0011": {"func": model_52024_97da327b_0011, "volume": 264.6290995185, "area": 684.5751567991},
    "model_52035_0244dcd2_0006": {"func": model_52035_0244dcd2_0006, "volume": 2.9355159012, "area": 14.282158463},
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
