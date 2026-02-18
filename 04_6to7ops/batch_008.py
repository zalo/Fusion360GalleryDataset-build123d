"""Batch 008 - passing/04_6to7ops
96 models bundled from Fusion360 Gallery reconstructions.
"""

from build123d import *
from build123d import Edge, BuildLine
from collections import Counter
from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
from OCP.Geom import Geom_BSplineCurve
from OCP.TColStd import TColStd_Array1OfReal, TColStd_Array1OfInteger
from OCP.TColgp import TColgp_Array1OfPnt
from OCP.gp import gp_Pnt


# Description: A dark gray rounded rectangular bar or plate with three horizontal slots or grooves cut into the right end, featuring smoothly curved edges.
def model_43540_0f53629d_0000():
    """Model: Palbolt"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=5.3
        extrude(amount=5.3)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(5.3, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            Circle(0.35)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2240664122, perimeter: 2.3367857016
            with BuildLine():
                Line((0, 0.3), (0.5601660306, -0.5))
                Line((0, -0.5), (0, 0.3))
                Line((0.5601660306, -0.5), (0, -0.5))
            make_face()
            # Profile area: 0.1, perimeter: 1.4
            with BuildLine():
                Line((0.5, 0.3), (0, 0.3))
                Line((0.5, 0.5), (0.5, 0.3))
                Line((0, 0.5), (0.5, 0.5))
                Line((0, 0.3), (0, 0.5))
            make_face()
        # Symmetric extrude, each_side=0.6
        extrude(amount=0.6, both=True, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a belt drive or pulley component featuring a curved, ribbed cylindrical drum with a central axial slot and a rectangular mounting flange on one end for attachment purposes.
def model_43540_0f53629d_0001():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 24 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.5067792582, perimeter: 29.6459826344
            with BuildLine():
                Line((8.3, 2), (8.3, -2))
                Line((8.3, 2), (4.4370598373, 2))
                CenterArc((4.4370598373, 3.25), 1.25, -143.7784533802, 53.7784533802)
                CenterArc((0, 0), 4.25, -36.2215466198, 72.4430932397)
                CenterArc((4.4370598373, -3.25), 1.25, 90, 53.7784533802)
                Line((8.3, -2), (4.4370598373, -2))
            make_face()
            with BuildLine():
                Line((7.2, -1.4), (5.7, -1.4))
                Line((5.7, -1.4), (5.7, -0.8))
                Line((5.7, -0.8), (4.9, -0.8))
                Line((4.9, -0.8), (4.9, 0.8))
                Line((5.7, 0.8), (4.9, 0.8))
                Line((5.7, 1.4), (5.7, 0.8))
                Line((7.2, 1.4), (5.7, 1.4))
                Line((7.2, -1.4), (7.2, 1.4))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 17.1530958886, perimeter: 49.008845396
            with BuildLine():
                CenterArc((0, 0), 4.25, -36.2215466198, 72.4430932397)
                CenterArc((0, 0), 4.25, 36.2215466198, 287.5569067603)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3.55, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=1.2
        extrude(amount=1.2, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 17.1530958886, perimeter: 49.008845396
            with BuildLine():
                CenterArc((0, 0), 4.25, 143.7784533802, 72.4430932397)
                CenterArc((0, 0), 4.25, -143.7784533802, 287.5569067603)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3.55, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(8.3, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.8502295699, perimeter: 5.9847340051
            Circle(0.9525)
        # OneSide extrude, distance=2.4
        extrude(amount=2.4, mode=Mode.ADD)
    return part.part


# Description: This is a plastic or composite handle assembly with an elongated rectangular body featuring a cylindrical grip extending from one end and a curved, tapered design with surface details or slots along its length.
def model_43562_004c6cea_0013():
    """Model: lever v1 (3)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 9 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 7.5255498871, perimeter: 20.9895174322
            with BuildLine():
                CenterArc((0, 0), 1, -88.5744108553, 88.5674562624)
                Line((0.0248786572, -0.9996904783), (10.0186589192, -0.7509816642))
                CenterArc((9.9999999263, -0.0012138054), 0.75, 179.9930454071, 91.4325437376)
                Line((0.9999999926, -0.0001213805), (9.2499999319, -0.00112277))
            make_face()
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with BuildLine():
                CenterArc((9.9999999263, -0.0012138054), 0.75, -88.5744108553, 177.1349125249)
                CenterArc((9.9999999263, -0.0012138054), 0.75, 88.5605016696, 91.4325437376)
                CenterArc((9.9999999263, -0.0012138054), 0.75, 179.9930454071, 91.4325437376)
            make_face()
            # Profile area: 7.5255498871, perimeter: 20.9895174322
            with BuildLine():
                Line((0.9999999926, -0.0001213805), (9.2499999319, -0.00112277))
                CenterArc((9.9999999263, -0.0012138054), 0.75, 88.5605016696, 91.4325437376)
                Line((0.0251213424, 0.9996844093), (10.0188409332, 0.7485495015))
                CenterArc((0, 0), 1, -0.0069545929, 88.5674562624)
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 9 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with BuildLine():
                CenterArc((0, 0), 1, -0.0069545929, 88.5674562624)
                CenterArc((0, 0), 1, 88.5605016696, 182.8650874751)
                CenterArc((0, 0), 1, -88.5744108553, 88.5674562624)
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 1.5393804003, perimeter: 4.398229715
            Circle(0.7)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch3 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.2), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=4
        extrude(amount=4, mode=Mode.ADD)
    return part.part


# Description: This is a knife blade or cutting tool with a curved ergonomic handle (dark gray/black) and a sharp blue blade section, featuring a streamlined teardrop-shaped grip with a small circular hole near the handle end.
def model_43866_908e0b9a_0015():
    """Model: body 2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 12 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.4190263433, perimeter: 6.9115038379
            with BuildLine():
                CenterArc((8.100000181, 0.9), 0.9, 90, 179.9999884741)
                CenterArc((8.100000181, 0.9), 0.9, -90.0000115259, 180.0000115259)
            make_face()
            with BuildLine():
                CenterArc((8.100000181, 0.9), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 3.0159189192, perimeter: 7.539817354
            with BuildLine():
                Line((0, 2), (0.0493526265, 1.9987814167))
                CenterArc((0, 1), 1, 90, 180)
                CenterArc((0, 1), 1, -90, 177.1711536404)
            make_face()
            with BuildLine():
                CenterArc((0, 1), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 11.2955110402, perimeter: 22.3517562961
            with BuildLine():
                CenterArc((0, 1), 1, -90, 177.1711536404)
                Line((0, 0), (8.1, 0))
                CenterArc((8.100000181, 0.9), 0.9, 90, 179.9999884741)
                Line((4.6560499627, 1.885035806), (8.100000181, 1.8))
                CenterArc((3.1292498374, 3.7602938674), 2.4182041725, -131.9806844702, 81.1325225808)
                Line((0.0493526265, 1.9987814167), (1.5117613346, 1.9626725605))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.81, perimeter: 16.4
            with BuildLine():
                Line((8.1, 0), (8.1, 0.1))
                Line((8.1, 0.1), (0, 0.1))
                Line((0, 0.1), (0, 0))
                Line((0, 0), (8.1, 0))
            make_face()
        # OneSide extrude, distance=1.1
        extrude(amount=1.1, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.8849555922, perimeter: 6.2831853072
            with BuildLine():
                CenterArc((8.100000181, 0.9), 0.8, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((8.100000181, 0.9), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical coupling or connector with two coaxial circular flanges of different diameters, featuring central axial holes and a recessed middle section for joining two shafts or components end-to-end.
def model_43866_908e0b9a_0018():
    """Model: nit"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=0.15
        extrude(amount=0.15)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.15), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.45), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.3769911184, perimeter: 3.7699111843
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=0.15
        extrude(amount=0.15, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical connector or coupling with a tapered end cap and a slot or notch cut into the side, featuring a stepped diameter design and a rounded top closure.
def model_43928_6ca53538_0010():
    """Model: CAptive Cover Screw v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2375829444, perimeter: 1.7278759595
            Circle(0.275)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.6), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1194590607, perimeter: 1.2252211349
            Circle(0.195)
        # OneSide extrude, distance=0.65
        extrude(amount=0.65, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.03, perimeter: 0.7
            with BuildLine():
                Line((0.1, -0.075), (-0.1, -0.075))
                Line((0.1, 0.075), (0.1, -0.075))
                Line((-0.1, 0.075), (0.1, 0.075))
                Line((-0.1, -0.075), (-0.1, 0.075))
            make_face()
        # Symmetric extrude, each_side=-1
        extrude(amount=-1, both=True, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a connector or coupling fitting with a spherical main body featuring two cylindrical ports extending from opposite sides, designed to join two tubes or pipes at various angles with internal threaded or bore connections.
def model_43928_6ca53538_0012():
    """Model: Drag Lock Pivot Pin v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            Circle(0.1)
        # OneSide extrude, distance=0.135
        extrude(amount=0.135)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.135), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1649336143, perimeter: 2.1991148575
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            Circle(0.1)
        # OneSide extrude, distance=0.225
        extrude(amount=0.225, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.36), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0651440653, perimeter: 0.9047786842
            Circle(0.144)
        # OneSide extrude, distance=0.35
        extrude(amount=0.35, mode=Mode.ADD)
    return part.part


# Description: This is a flat circular washer or spacer ring with a large central hole, featuring a thin disc-like profile with uniform thickness and a smooth outer diameter.
def model_43928_6ca53538_0021():
    """Model: Drive Gear Offset Spacer A v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 5.3092915846, perimeter: 8.1681408993
            Circle(1.3)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            Circle(0.6)
        # OneSide extrude, distance=0.375
        extrude(amount=0.375, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 9 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.475), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0699904524, perimeter: 1.3779184128
            with BuildLine():
                CenterArc((0, 0), 0.405, 37.8029497815, 104.394100437)
                Line((0.32, 0.2482438317), (-0.32, 0.2482438317))
            make_face()
            # Profile area: 0.3177521046, perimeter: 2.272975327
            with BuildLine():
                Line((0.32, 0.2482438317), (-0.32, 0.2482438317))
                Line((-0.32, 0.2482438317), (-0.32, -0.2482438317))
                Line((-0.32, -0.2482438317), (0.32, -0.2482438317))
                Line((0.32, -0.2482438317), (0.32, 0.2482438317))
            make_face()
            # Profile area: 0.0699904524, perimeter: 1.3779184128
            with BuildLine():
                Line((-0.32, -0.2482438317), (0.32, -0.2482438317))
                CenterArc((0, 0), 0.405, -142.1970502185, 104.394100437)
            make_face()
        # OneSide extrude, distance=-1.4
        extrude(amount=-1.4, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a washer or spacer ring with a flat, disc-like shape featuring a central circular hole and a uniform thickness, designed for fastening or spacing applications.
def model_43928_6ca53538_0022():
    """Model: Drive Gear Offset Spacer B v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 5.3092915846, perimeter: 8.1681408993
            Circle(1.3)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 3.1447350316, perimeter: 6.2863268998
            Circle(1.0005)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 9 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.6264683826, perimeter: 2.8317576276
            with BuildLine():
                CenterArc((0, 0), 0.455, -154.3028909451, 128.6057818901)
                Line((0.41, -0.1972941966), (0.41, 0.1972941966))
                CenterArc((0, 0), 0.455, 25.6971090549, 128.6057818901)
                Line((-0.41, 0.1972941966), (-0.41, -0.1972941966))
            make_face()
        # OneSide extrude, distance=-1.8
        extrude(amount=-1.8, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical sleeve or barrel component with a slightly tapered, curved profile and a ribbed or corrugated surface texture on its exterior walls.
def model_43931_bb001c04_0013():
    """Model: cover1 v13"""
    with BuildPart() as part:
        # Sketch4 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 7532.5690783464, perimeter: 1087.6570757846
            with BuildLine():
                CenterArc((0, 0), 93.4785, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 79.6275, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides extrude, along=26.3, against=-100
        extrude(amount=26.3)
        extrude(sk.sketch, amount=-100)

        # Sketch31 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -100, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            with Locations((89.773, 0)):
                Circle(2)
        # OneSide extrude, distance=-7
        extrude(amount=-7, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical pin or dowel with a rounded hemispherical head on one end and a tapered or slightly beveled point on the opposite end, featuring a smooth cylindrical shaft along its length.
def model_43932_4bfdfe7b_0000():
    """Model: 13 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.0106192983, perimeter: 5.0265482457
            Circle(0.8)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            Circle(0.6)
        # OneSide extrude, distance=7.6
        extrude(amount=7.6, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-7.3, 0)):
                Circle(0.3)
        # Symmetric extrude, each_side=2.5
        extrude(amount=2.5, both=True, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a dual-lobe polymer or composite connector housing featuring two rounded cylindrical bodies with central circular apertures, interconnected by a bridging web structure with triangulated reinforcement ribs for structural support.
def model_43932_4bfdfe7b_0001():
    """Model: 7 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 13 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 19.2784086738, perimeter: 26.4856236955
            with BuildLine():
                Line((-1.6, -5), (1.6, -5))
                Line((1.6, -5), (1.6, -2.3323782844))
                CenterArc((6.6, -2.3323807579), 5, 160.5370360231, 19.4629356318)
                CenterArc((0, 0), 2, -19.4629183699, 218.9258693162)
                CenterArc((-6.6, -2.3323807579), 5, 0, 19.4629509463)
                Line((-1.6, -2.3323807579), (-1.6, -5))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=2.4
        extrude(amount=2.4, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1.6, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.0422921175, perimeter: 7.3352434313
            with BuildLine():
                Line((-1.2, -2.3323782844), (-1.2, -3.6))
                Line((-1.2, -3.6), (1.2, -3.6))
                Line((1.2, -3.6), (1.2, -2.3323782844))
                Line((1.2, -2.3323782844), (-1.2, -2.3323782844))
            make_face()
            # Profile area: 14.2377078825, perimeter: 16.6647565687
            with BuildLine():
                Line((1.2, -2.3323782844), (-1.2, -2.3323782844))
                Line((1.2, -2.3323782844), (1.2, 3.6))
                Line((1.2, 3.6), (-1.2, 3.6))
                Line((-1.2, 3.6), (-1.2, -2.3323782844))
            make_face()
        # Symmetric extrude, each_side=-6
        extrude(amount=-6, both=True, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -5, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 6.157521601, perimeter: 8.7964594301
            Circle(1.4)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical sleeve or spacer with a tapered/conical end on one side and a flanged or enlarged head on the opposite end, featuring a hollow interior bore running through its length.
def model_43932_4bfdfe7b_0002():
    """Model: 8 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 5.3092915846, perimeter: 8.1681408993
            Circle(1.3)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 3.8013271108, perimeter: 6.9115038379
            Circle(1.1)
        # OneSide extrude, distance=6
        extrude(amount=6, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-5.7, 0)):
                Circle(0.3)
        # Symmetric extrude, each_side=2.6
        extrude(amount=2.6, both=True, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical connector or sleeve with a larger flanged head at one end and a tapered or threaded section, featuring a central axial bore and surface detailing along its length.
def model_43932_4bfdfe7b_0003():
    """Model: 11 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 5.3092915846, perimeter: 8.1681408993
            Circle(1.3)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.6), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 3.8013271108, perimeter: 6.9115038379
            Circle(1.1)
        # OneSide extrude, distance=8
        extrude(amount=8, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-7.8, 0)):
                Circle(0.3)
        # Symmetric extrude, each_side=7.5
        extrude(amount=7.5, both=True, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a long, slender rectangular rod or bar with a slightly tapered streamlined profile, featuring a small circular hole or indent near its center, designed for mounting or structural support applications.
def model_43932_4bfdfe7b_0004():
    """Model: 10 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 18 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 217.85257745, perimeter: 256.2995574288
            with BuildLine():
                Line((13.5, 1.1115814291), (13.5, 1.1))
                Line((13.5, 1.1), (-13.5, 1.1))
                Line((-13.5, 1.1), (-13.5, -1.1))
                Line((-13.5, -1.1), (13.5, -1.1))
                Line((13.5, -1.1), (13.5, -1.1884185709))
                CenterArc((13.85, -1.1884185709), 0.35, 90, 90)
                Line((112.5, -0.8384185709), (13.85, -0.8384185709))
                Line((112.5, 0.7615814291), (112.5, -0.8384185709))
                Line((13.85, 0.7615814291), (112.5, 0.7615814291))
                CenterArc((13.85, 1.1115814291), 0.35, 180, 90)
            make_face()
        # Symmetric extrude, each_side=3.2
        extrude(amount=3.2, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -1.1, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 3.8013271108, perimeter: 6.9115038379
            with Locations((-0.3, 0)):
                Circle(1.1)
            # Profile area: 3.8013271108, perimeter: 6.9115038379
            with Locations((-10.3, 0)):
                Circle(1.1)
            # Profile area: 22.4, perimeter: 19.8
            with BuildLine():
                Line((-13.5, 0), (-13.5, -3.2))
                Line((-13.5, 3.2), (-13.5, 0))
                Line((-13.5, 3.2), (-17, 3.2))
                Line((-17, 3.2), (-17, -3.2))
                Line((-13.5, -3.2), (-17, -3.2))
            make_face()
            # Profile area: 2.1975228068, perimeter: 11.4265482457
            with BuildLine():
                Line((-13.5, 3.2), (-13.5, 0))
                CenterArc((-10.3, 0), 3.2, 90, 90)
                Line((-10.3, 3.2), (-13.5, 3.2))
            make_face()
            # Profile area: 2.1975228068, perimeter: 11.4265482457
            with BuildLine():
                CenterArc((-10.3, 0), 3.2, 180, 90)
                Line((-13.5, 0), (-13.5, -3.2))
                Line((-10.3, -3.2), (-13.5, -3.2))
            make_face()
        # OneSide extrude, distance=-6
        extrude(amount=-6, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -0.8384185709, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with Locations((36.2346499677, 0)):
                Circle(0.75)
        # OneSide extrude, distance=-8
        extrude(amount=-8, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a hollow cylindrical sleeve or spacer with a uniform bore through its center and a textured or mesh-like surface finish on its outer walls.
def model_43932_4bfdfe7b_0005():
    """Model: 5 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 10.1787601976, perimeter: 11.3097335529
            Circle(1.8)
        # OneSide extrude, distance=2.4
        extrude(amount=2.4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.4), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.1623892818, perimeter: 23.2477856366
            with BuildLine():
                CenterArc((0, 0), 1.9, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 10.1787601976, perimeter: 11.3097335529
            Circle(1.8)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 6.157521601, perimeter: 8.7964594301
            Circle(1.4)
        # OneSide extrude, distance=-6
        extrude(amount=-6, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical suppressor or silencer with a tapered rounded end cap, featuring a smooth tubular body with what appears to be mounting threads or attachment points at the rear end.
def model_43933_3b763a09_0004():
    """Model: 5 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=4
        extrude(amount=4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 4), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-0.6, 0)):
                Circle(0.15)
        # Symmetric extrude, each_side=1.2
        extrude(amount=1.2, both=True, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical shaft or pin with a tapered or stepped design, featuring a larger diameter main body that transitions to a smaller diameter end section with what appears to be a slotted or keyed feature at the tip.
def model_43933_3b763a09_0005():
    """Model: 3 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # Symmetric extrude, each_side=1.5
        extrude(amount=1.5, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.3063052837, perimeter: 4.0840704497
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=2.2
        extrude(amount=2.2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 9 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1769049535, perimeter: 2.6587327137
            with BuildLine():
                Line((-3.3, -0.075), (-3.3, 0.075))
                Line((-3.3, 0.075), (-4.4793663568, 0.075))
                Line((-4.4793663568, 0.075), (-4.4793663568, -0.075))
                Line((-4.4793663568, -0.075), (-3.3, -0.075))
            make_face()
        # Symmetric extrude, each_side=0.85
        extrude(amount=0.85, both=True, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a blue rectangular enclosure or mounting plate with a flat main body, curved edges, a side-mounted cylindrical post or connector, and a central horizontal slot or opening on its face.
def model_43934_912ff891_0003():
    """Model: Stand v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 18 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 392.5663706144, perimeter: 76.5663706144
            with BuildLine():
                CenterArc((9, -7), 2, -90, 90)
                Line((11, -7), (11, 6.9999992507))
                CenterArc((9, 7), 2, -0.0000214655, 90.0000430135)
                Line((8.9999992478, 9), (-8.9999992507, 9))
                CenterArc((-9, 7), 2, 89.9999785343, 90.0000430137)
                Line((-11, 6.9999992478), (-11, -6.9999992507))
                CenterArc((-9, -7), 2, 179.9999785347, 90.0000429311)
                Line((-8.9999992507, -9), (9, -9))
            make_face()
        # Symmetric extrude, each_side=1
        extrude(amount=1, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 18 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 47.0238934212, perimeter: 30.9398223686
            with BuildLine():
                CenterArc((-5.15, 0.7), 1.2, 90.0000007698, 89.9999909068)
                Line((-6.35, 0.7000001743), (-6.35, -0.7000007467))
                CenterArc((-5.15, -0.7), 1.2, -179.9999643467, 89.9999626262)
                Line((-5.150000036, -1.9), (5.1499999909, -1.9))
                CenterArc((5.15, -0.7), 1.2, -90.0000004328, 89.9999647789)
                Line((6.35, -0.7000007467), (6.35, 0.7000000001))
                CenterArc((5.15, 0.7), 1.2, 0.0000000038, 89.9999999634)
                Line((5.1500000007, 1.9), (-5.1500000161, 1.9))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((5.15, 0.7)):
                Circle(0.25)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((5.15, -0.7)):
                Circle(0.25)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-5.15, -0.7)):
                Circle(0.25)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-5.15, 0.7)):
                Circle(0.25)
        # OneSide extrude, distance=-4
        extrude(amount=-4, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a stamped or molded metal bracket or chassis component with an elongated, trapezoidal base featuring multiple rectangular slots and cutouts along its top surface, angled side flanges, and a notched right end.
def model_43934_912ff891_0011():
    """Model: Bearing Keeper v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2, perimeter: 6
            with BuildLine():
                Line((1, -0.5), (1, 0.5))
                Line((1, 0.5), (-1, 0.5))
                Line((-1, 0.5), (-1, -0.5))
                Line((-1, -0.5), (1, -0.5))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.096211275, perimeter: 1.0995574288
            with Locations((-0.7, 0)):
                Circle(0.175)
            # Profile area: 0.096211275, perimeter: 1.0995574288
            with Locations((0.7, 0)):
                Circle(0.175)
        # OneSide extrude, distance=-1.4
        extrude(amount=-1.4, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.231419637, perimeter: 3.1349784258
            with BuildLine():
                Line((-1, 0.125), (-1, -0.125))
                CenterArc((-0.7, 0), 0.325, -157.380135052, 314.7602701039)
            make_face()
            with BuildLine():
                CenterArc((-0.7, 0), 0.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.231419637, perimeter: 3.1349784258
            with BuildLine():
                CenterArc((0.7, 0), 0.325, 22.619864948, 314.7602701039)
                Line((1, -0.125), (1, 0.125))
            make_face()
            with BuildLine():
                CenterArc((0.7, 0), 0.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.15
        extrude(amount=-0.15, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a shoe last or form with a rounded, foot-shaped body featuring ventilation holes across the surface, curved contours for ergonomic fit, and flanged side extensions for mounting or support.
def model_43934_912ff891_0014():
    """Model: Crankshaft Counterweight v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 25 constraints, 14 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 6.6550232343, perimeter: 14.9899467403
            with BuildLine():
                CenterArc((0, 0), 0.4, 90, 270)
                Line((0, 0.4), (0, 0.9))
                CenterArc((0, 1.3), 0.4, 90, 180)
                Line((0, 1.7), (0, 2))
                CenterArc((0, 0), 2, 90, 14.4775123026)
                CenterArc((-0.4, 1.5491933385), 0.4, 104.4775127632, 75.5229864815)
                Line((-0.8, 1.5491898531), (-0.8, 0.1810902538))
                CenterArc((-1.2, 0.1810902209), 0.4, -80.0000017445, 80.0000064545)
                Line((-1.130540741, -0.2128328824), (-1.9672654734, -0.3603700281))
                CenterArc((0, 0), 2, -169.619463466, 160.0987523891)
                Line((1.1305407413, -0.1823566016), (1.9724517525, -0.3308082282))
                CenterArc((1.2000000001, 0.2115665018), 0.4000000001, -148.0677402816, 48.0677420742)
                Line((0.4, 0), (0.8605303912, 0))
            make_face()
            # Profile area: 1.167465237, perimeter: 5.7386489868
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 90)
                Line((0.4, 0), (0.8605303912, 0))
                CenterArc((1.2000000001, 0.2115665018), 0.4000000001, -179.9999987723, 31.9322584907)
                Line((0.8, 0.2115664933), (0.8, 1.5491933521))
                CenterArc((0.3999999999, 1.5491933385), 0.4, 0.0000019461, 75.5224852583)
                CenterArc((0, 0), 2, 75.5224876934, 14.4775123066)
                Line((0, 1.7), (0, 2))
                CenterArc((0, 1.3), 0.4, -90, 180)
                Line((0, 0.4), (0, 0.9))
            make_face()
        # Symmetric extrude, each_side=0.35
        extrude(amount=0.35, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.35), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.8246680716, perimeter: 6.5973445725
            with BuildLine():
                CenterArc((0, 0), 0.65, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.08
        extrude(amount=0.08, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            Circle(0.125)
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            with Locations((0, 1.3)):
                Circle(0.125)
        # Symmetric extrude, each_side=1.3
        extrude(amount=1.3, both=True, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a circular disc or wheel with a central hub, featuring a flat face, a recessed or stepped inner section, and what appears to be a ribbed or reinforced rim around the outer edge.
def model_43934_912ff891_0020():
    """Model: Piston v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 8.0424771932, perimeter: 10.0530964915
            Circle(1.6)
        # Symmetric extrude, each_side=0.35
        extrude(amount=0.35, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 10.7992247467, perimeter: 21.9036110961
            with BuildLine():
                CenterArc((0, 0), 2.2360679775, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.15
        extrude(amount=0.15, both=True, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.35), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=-2.4
        extrude(amount=-2.4, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a toroidal ring or bearing spacer with a smooth outer curved surface and a mesh or perforated inner band, featuring a hollow center opening and symmetrical radial wall thickness throughout its circular geometry.
def model_43938_418421a7_0000():
    """Model: bearing outer cover v3 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 10.5521832522, perimeter: 47.4788897737
            with BuildLine():
                CenterArc((0, 0), 4.0005, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3.556, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=1.00076
        extrude(amount=1.00076, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.00076), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 5.4724407743, perimeter: 43.0900848366
            with BuildLine():
                CenterArc((0, 0), 3.556, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3.302, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.0254
        extrude(amount=-0.0254, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -1.00076), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 4.1423336416, perimeter: 43.4890671036
            with BuildLine():
                CenterArc((0, 0), 3.556, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3.3655, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.0254
        extrude(amount=-0.0254, mode=Mode.ADD)
    return part.part


# Description: This is a toroidal or ring-shaped component with a curved, tubular body featuring mesh or perforated surfaces on the inner and outer walls, designed to allow flow or ventilation through the structure.
def model_43938_418421a7_0002():
    """Model: bearing inner v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 8.6141082179, perimeter: 31.6951512909
            with BuildLine():
                CenterArc((0, 0), 2.794, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.25044, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=1.00076
        extrude(amount=1.00076, both=True)

        # Sketch4 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.00076), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 4.6617088077, perimeter: 36.7063685645
            with BuildLine():
                CenterArc((0, 0), 3.048, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.794, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.0254
        extrude(amount=-0.0254, mode=Mode.ADD)

        # Sketch5 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -1.00076), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 4.6617088077, perimeter: 36.7063685645
            with BuildLine():
                CenterArc((0, 0), 3.048, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.794, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.0254
        extrude(amount=-0.0254, mode=Mode.ADD)
    return part.part


# Description: This is a simple assembly consisting of a small spherical or rounded knob positioned above a larger elongated rounded rectangular bar or rail, likely representing a handle mechanism or control component.
def model_44021_f141414b_0003():
    """Model: Worm v13"""
    with BuildPart() as part:
        # Sketch25 -> Extrude8 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4.9087385212, perimeter: 7.853981634
            with Locations((5, 0)):
                Circle(1.25)
        # OneSide extrude, distance=13
        extrude(amount=13)

        # Sketch35 -> Extrude11 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.7907078125, perimeter: 11.9380520836
            with BuildLine():
                CenterArc((20, 0), 1.1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((20, 0), 0.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch36 -> Extrude12 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(2, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.3561944902, perimeter: 15.7079632679
            with BuildLine():
                CenterArc((20, 0), 1.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((20, 0), 1.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical spacer or standoff with flanged ends, featuring a hollow tubular body with circular flanges at both the top and bottom, designed for assembly and alignment purposes.
def model_44206_ff45fbf0_0010():
    """Model: perno1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0004908739, perimeter: 0.0785398163
            Circle(0.0125)
        # OneSide extrude, distance=0.075
        extrude(amount=0.075)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.075, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0004712389, perimeter: 0.1884955592
            with BuildLine():
                CenterArc((0, 0), 0.0175, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.0125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0004908739, perimeter: 0.0785398163
            Circle(0.0125)
        # OneSide extrude, distance=0.01
        extrude(amount=0.01, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0004712389, perimeter: 0.1884955592
            with BuildLine():
                CenterArc((0, 0), 0.0175, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.0125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0004908739, perimeter: 0.0785398163
            Circle(0.0125)
        # OneSide extrude, distance=0.01
        extrude(amount=0.01, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical fastener or standoff with enlarged circular flanges at both ends and a central shaft, featuring a mesh-textured top surface indicating a hexagonal or recessed head design.
def model_44206_ff45fbf0_0014():
    """Model: perno2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0004908739, perimeter: 0.0785398163
            Circle(0.0125)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.05, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0004712389, perimeter: 0.1884955592
            with BuildLine():
                CenterArc((0, 0), 0.0175, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.0125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0004908739, perimeter: 0.0785398163
            Circle(0.0125)
        # OneSide extrude, distance=0.01
        extrude(amount=0.01, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0004712389, perimeter: 0.1884955592
            with BuildLine():
                CenterArc((0, 0), 0.0175, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.0125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0004908739, perimeter: 0.0785398163
            Circle(0.0125)
        # OneSide extrude, distance=0.01
        extrude(amount=0.01, mode=Mode.ADD)
    return part.part


# Description: This is a paraglider wing or airfoil canopy featuring an elongated elliptical shape with internal structural ribs and suspension lines, designed to generate lift through aerodynamic surface curvature.
def model_44528_3cff1325_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 78.5398163397, perimeter: 31.4159265359
            Circle(5)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


# Description: This is a flat, parallelogram-shaped sheet metal bracket or mounting plate with two rectangular slots or cutouts on opposite sides and flanged edges for structural reinforcement.
def model_44553_9af8a2cb_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 100, perimeter: 40
            with BuildLine():
                Line((5, -5), (5, 5))
                Line((5, 5), (-5, 5))
                Line((-5, 5), (-5, -5))
                Line((-5, -5), (5, -5))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(-5, 0, 0), x_dir=(0, -1, 0), z_dir=(-1, 0, 0))):
            # Profile area: 2.25, perimeter: 10.4142135624
            with BuildLine():
                Line((-2.5, 1), (2.5, 1))
                Line((2.5, 1), (2, 1.5))
                Line((-2, 1.5), (2, 1.5))
                Line((-2.5, 1), (-2, 1.5))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(5, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 1.125, perimeter: 5.7071067812
            with BuildLine():
                Line((0, 1), (0, 1.5))
                Line((0, 1), (2.5, 1))
                Line((2.5, 1), (2, 1.5))
                Line((2, 1.5), (0, 1.5))
            make_face()
            # Profile area: 1.125, perimeter: 5.7071067812
            with BuildLine():
                Line((0, 1), (-2.5, 1))
                Line((0, 1), (0, 1.5))
                Line((-2, 1.5), (0, 1.5))
                Line((-2.5, 1), (-2, 1.5))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical fastener or socket (likely a bolt socket or pipe fitting) with a long tubular shaft and a larger hexagonal or multi-sided head at the top, featuring internal threading or grooves visible on the upper surface.
def model_45007_990d2758_0001():
    """Model: 19. Tornillo 4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-12.2701132057, -3.542779165)):
                Circle(0.5)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-12.2701132057, 3.542779165)):
                Circle(0.25)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.04, perimeter: 1
            with BuildLine():
                Line((12.4701132057, 3.492779165), (12.0701132057, 3.492779165))
                Line((12.4701132057, 3.592779165), (12.4701132057, 3.492779165))
                Line((12.0701132057, 3.592779165), (12.4701132057, 3.592779165))
                Line((12.0701132057, 3.492779165), (12.0701132057, 3.592779165))
            make_face()
        # OneSide extrude, distance=-0.05
        extrude(amount=-0.05, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical roller or spacer with a smooth, uniform circular cross-section and rounded ends, featuring a slightly textured surface finish.
def model_45285_dc1f2b6f_0002():
    """Model: cycle battery v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 50.2654824574, perimeter: 25.1327412287
            Circle(4)
        # OneSide extrude, distance=30
        extrude(amount=30)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 30), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 7.0685834706, perimeter: 51.9745206273
            with BuildLine():
                CenterArc((0, 0), 4.2720018727, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-2.5
        extrude(amount=-2.5, mode=Mode.ADD)
    return part.part


# Description: This is a popsicle or ice cream bar with a rounded, rectangular body featuring three curved lobes at the top and a stick handle extending from the bottom.
def model_45285_dc1f2b6f_0005():
    """Model: paddle 1 v1 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.0067837158, perimeter: 3.5569112024
            Circle(0.5661)
        # OneSide extrude, distance=12
        extrude(amount=12)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 12 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 20.1415926536, perimeter: 23.2831853072
            with BuildLine():
                CenterArc((3, 12), 1, 0, 180)
                Line((2, 12), (2, 3.5))
                CenterArc((3, 3.5), 1, 180, 180)
                Line((4, 12), (4, 3.5))
            make_face()
            # Profile area: 20.1619046198, perimeter: 23.3034972734
            with BuildLine():
                Line((-2, 12), (-2, 3.4898440169))
                CenterArc((-3, 12), 1, 0, 180)
                Line((-4, 12), (-4, 3.4898440169))
                CenterArc((-3, 3.4898440169), 1, 180, 180)
            make_face()
            # Profile area: 39.6277736948, perimeter: 26.2896338935
            with BuildLine():
                CenterArc((0, 10.5006532619), 2.4996080975, 36.8579184393, 106.2841631213)
                Line((-2, 12), (-2, 3.4898440169))
                CenterArc((-0.003776424, 4.9822911689), 2.4924500129, -143.2169138205, 106.7247744997)
                Line((2, 12), (2, 3.5))
            make_face()
        # TwoSides extrude (symmetric), distance=1
        extrude(amount=1, both=True, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Intersect)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.2793310326, perimeter: 11.0108307028
            with BuildLine():
                CenterArc((0.059706848, -6.3721100492), 7.3723518286, 90.4640293732, 15.7593306505)
                Line((-2, 0.7066736871), (-2, -0.774298472))
                CenterArc((-0.1543742295, 6.6061608702), 7.6077272944, -104.0399765612, 12.8772641528)
                Line((-0.308748459, -1), (0, -1))
                CenterArc((-0.1543742295, 6.6061608702), 7.6077272944, -88.8372875916, 15.2875181504)
                Line((2, 0.7403321453), (2, -0.6901523266))
                CenterArc((0.059706848, -6.3721100492), 7.3723518286, 74.7408610181, 14.7951096088)
                Line((0.1194136961, 1), (0, 1))
            make_face()
            # Profile area: 3.6636751633, perimeter: 7.1420043961
            with BuildLine():
                CenterArc((-3, -0.8512494074), 1.8512494074, 90, 32.6956023474)
                Line((-4, 0.7066736871), (-4, -0.774298472))
                CenterArc((-3, 1.3281658501), 2.3281658501, -115.4372710677, 25.4372710677)
                CenterArc((-3, 1.3281658501), 2.3281658501, -90, 25.4372710677)
                Line((-2, 0.7066736871), (-2, -0.774298472))
                CenterArc((-3, -0.8512494074), 1.8512494074, 57.3043976526, 32.6956023474)
            make_face()
            # Profile area: 3.7115289365, perimeter: 7.1230477609
            with BuildLine():
                CenterArc((3, -1.0553706886), 2.0553706886, 89.9999996347, 29.1127788446)
                Line((2, 0.7403321453), (2, -0.6901523266))
                CenterArc((3, 0.4962824726), 1.5516531612, -130.1262434778, 80.2524869555)
                Line((4, 0.7403321453), (4, -0.6901523266))
                CenterArc((3, -1.0553706886), 2.0553706886, 60.8872215207, 29.1127781139)
            make_face()
        # OneSide extrude, distance=17.5
        extrude(amount=17.5, mode=Mode.INTERSECT)
    return part.part


# Description: This is a cylindrical sleeve or tube with a closed top end featuring a small flange or collar, designed for insertion or assembly purposes.
def model_45303_48d14b32_0016():
    """Model: profile for join seat"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 25, perimeter: 20
            with BuildLine():
                Line((55, -55), (60, -55))
                Line((55, -60), (55, -55))
                Line((60, -60), (55, -60))
                Line((60, -55), (60, -60))
            make_face()
        # OneSide extrude, distance=40
        extrude(amount=40)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 40, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 13.69, perimeter: 14.8
            with BuildLine():
                Line((-59.35, 59.35), (-55.65, 59.35))
                Line((-59.35, 55.65), (-59.35, 59.35))
                Line((-55.65, 55.65), (-59.35, 55.65))
                Line((-55.65, 59.35), (-55.65, 55.65))
            make_face()
        # OneSide extrude, distance=-40
        extrude(amount=-40, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 40, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.2743807017, perimeter: 18.5265482457
            with BuildLine():
                Line((-55, 55.65), (-55, 59.35))
                Line((-55, 55.65), (-51.95, 55.65))
                Line((-51.95, 55.65), (-51.95, 59.35))
                Line((-51.95, 59.35), (-55, 59.35))
            make_face()
            with BuildLine():
                CenterArc((-53.5, 57.5), 0.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 9.2743807017, perimeter: 18.5265482457
            with BuildLine():
                Line((-63.05, 59.35), (-60, 59.35))
                Line((-63.05, 55.65), (-63.05, 59.35))
                Line((-60, 55.65), (-63.05, 55.65))
                Line((-60, 59.35), (-60, 55.65))
            make_face()
            with BuildLine():
                CenterArc((-61.5, 57.5), 0.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical suppressor or silencer with a tapered end cap, featuring a smooth tubular body and a slightly reduced diameter muzzle attachment point at the base.
def model_45359_1768ab3f_0010():
    """Model: Valve Linkage Bolt"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=1.6
        extrude(amount=1.6)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY) as sk:
            # Profile area: 0.0157079633, perimeter: 0.5141592654
            with BuildLine():
                CenterArc((0, 0.25), 0.1, 90, 180)
                Line((0, 0.15), (0, 0.35))
            make_face()
            # Profile area: 0.0157079633, perimeter: 0.5141592654
            with BuildLine():
                Line((0, 0.15), (0, 0.35))
                CenterArc((0, 0.25), 0.1, -90, 180)
            make_face()
        # TwoSides extrude, along=1.1, against=-0.6
        extrude(amount=1.1, mode=Mode.SUBTRACT)
        extrude(sk.sketch, amount=-0.6, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical connector or coupling with a tubular main body, a stepped diameter design, and textured end surfaces suggesting threads or a gripping pattern for assembly or connection purposes.
def model_45359_1768ab3f_0023():
    """Model: Linkage Rod D4-L18 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=0.22
        extrude(amount=0.22)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.22, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=0.09
        extrude(amount=0.09, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.31, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0549778714, perimeter: 2.1991148575
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical pipe or tube with a slightly tapered end, featuring a smooth exterior surface and a simple tubular geometry.
def model_45359_1768ab3f_0025():
    """Model: Crankshaft Bolt"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch4 -> Extrude2 (Cut)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((0, 0.4)):
                Circle(0.1)
        # Symmetric extrude, each_side=0.9
        extrude(amount=0.9, both=True, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a curved bracket or arm component featuring a rectangular base with an angled, curved upper section that tapers to a pointed end, with ribbed or textured surface details along the curved portion.
def model_45359_1768ab3f_0038():
    """Model: Centrifugal Pump Housing"""
    with BuildPart() as part:
        # Sketch3 -> Extrude3 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 17.6714586764, perimeter: 19.1371669412
            with BuildLine():
                Line((0, -1), (0, -3.5))
                CenterArc((0, 0), 1, 90, 180)
                Line((0, 3.5), (0, 1))
                CenterArc((0, 0), 3.5, 90, 180)
            make_face()
        # OneSide extrude, distance=1.08
        extrude(amount=1.08)

        # Sketch3 -> Extrude1 (Join)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 16.1988371201, perimeter: 28.4181393921
            with BuildLine():
                CenterArc((0, 0), 4.75, 90, 135.9937493644)
                CenterArc((0, 0), 4.75, -134.0062506356, 44.0062506356)
                Line((0, -3.5), (0, -4.75))
                CenterArc((0, 0), 3.5, 90, 180)
                Line((0, 4.75), (0, 3.5))
            make_face()
            # Profile area: 7.0331595058, perimeter: 14.0817522728
            with BuildLine():
                Line((-3.3, -4.95), (-3.3, -3.4165040612))
                Line((-5, -4.95), (-3.3, -4.95))
                Line((-5, -5.95), (-5, -4.95))
                Line((0, -5.95), (-5, -5.95))
                Line((0, -4.75), (0, -5.95))
                CenterArc((0, 0), 4.75, -134.0062506356, 44.0062506356)
            make_face()
        # OneSide extrude, distance=2.88
        extrude(amount=2.88, mode=Mode.ADD)

        # Sketch4 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 4.95), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.1898848422, perimeter: 1.5447211078
            with Locations((4.2, 1.44)):
                Circle(0.24585)
        # OneSide extrude, distance=-3.3
        extrude(amount=-3.3, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical connector or coupling component with a tilted orientation, featuring a hollow central bore, mesh-textured flanged ends, and a curved body design typical of a pipe joint or adapter fitting.
def model_45359_1768ab3f_0043():
    """Model: Crankshaft Nut"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3769911184, perimeter: 3.7699111843
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1570796327, perimeter: 3.1415926536
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0157079649, perimeter: 0.5141592922
            with BuildLine():
                CenterArc((0, 0.4500000052), 0.1000000052, 90, 180)
                Line((0, 0.35), (0, 0.5500000104))
            make_face()
            # Profile area: 0.0157079649, perimeter: 0.5141592922
            with BuildLine():
                Line((0, 0.35), (0, 0.5500000104))
                CenterArc((0, 0.4500000052), 0.1000000052, -90, 180)
            make_face()
        # Symmetric extrude, each_side=0.8
        extrude(amount=0.8, both=True, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a hammer or mallet consisting of a cylindrical dark gray handle with a large polyhedral blue head featuring multiple faceted surfaces, designed for striking applications.
def model_45360_cb4bac3f_0001():
    """Model: tornillo articulacion"""
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

        # Sketch3 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=3.4
        extrude(amount=3.4, mode=Mode.ADD)
    return part.part


# Description: This is a hammer or mallet head featuring a cylindrical handle (dark gray) with a polygonal striking head (light blue) composed of multiple flat faceted surfaces, creating a geometric, multi-sided hammer design.
def model_45360_cb4bac3f_0024():
    """Model: tornillo placa (1)"""
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
        # OneSide extrude, distance=2.05
        extrude(amount=2.05, mode=Mode.ADD)
    return part.part


# Description: This is a complex polyhedron or faceted hexagonal component with multiple triangular and rectangular faces, featuring a hollow or recessed central cavity and various angular surfaces that suggest it may function as a structural bracket, connector, or geometric enclosure.
def model_45360_cb4bac3f_0025():
    """Model: tuerca torno eje (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.2816854184, perimeter: 12.4301652222
            with BuildLine():
                Line((-1.25, 0.7216878365), (-1.25, -0.7216878365))
                Line((-1.25, -0.7216878365), (0, -1.443375673))
                Line((0, -1.443375673), (1.25, -0.7216878365))
                Line((1.25, -0.7216878365), (1.25, 0.7216878365))
                Line((1.25, 0.7216878365), (0, 1.443375673))
                Line((0, 1.443375673), (-1.25, 0.7216878365))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)

        # Sketch4 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.9285207249, perimeter: 11.2699111843
            with BuildLine():
                Line((-1.0825317547, -0.625), (0, -1.25))
                Line((0, -1.25), (1.0825317547, -0.625))
                Line((1.0825317547, -0.625), (1.0825317547, 0.625))
                Line((1.0825317547, 0.625), (0, 1.25))
                Line((0, 1.25), (-1.0825317547, 0.625))
                Line((-1.0825317547, 0.625), (-1.0825317547, -0.625))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical ring or bushing with a split design, featuring a radial slot that opens the ring, allowing it to compress and fit onto shafts or other components.
def model_45428_13340c06_0000():
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
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 68.3930998407, perimeter: 51.7885509064
            with BuildLine():
                CenterArc((17.8066967657, 10.0593151685), 5.7490494151, 85.6272105019, 67.0292016849)
                CenterArc((2.308165182, 18.0736411911), 11.6989849397, -67.6476296773, 40.3040418641)
                CenterArc((10.3561451481, -1.4983863237), 9.4631095354, 112.3523703227, 34.1508637467)
                Line((0, 0), (2.4646974711, 3.7242083992))
                Line((0, 0), (4.3460731852, 2.8656861444))
                CenterArc((9.5188602203, -4.9793149803), 9.3969020617, 85.7665357912, 37.6332701815)
                CenterArc((10.5425099353, 8.8495574234), 4.469805215, -94.2334642088, 97.0105982229)
                CenterArc((22.8232207682, 9.44527169), 7.8253456197, 125.8062186902, 56.970915324)
            make_face()
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)
    return part.part


# Description: This is a toroidal (doughnut-shaped) component with a large central hole and vertical slots or fins distributed around its circumference, likely designed as a stator core or similar electromagnetic component.
def model_45431_cb452deb_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 197.615916848, perimeter: 311.2061682646
            with BuildLine():
                CenterArc((0, 0), 25.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 24.13, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=25.4
        extrude(amount=25.4)

        # Sketch3 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 11 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 163.5518025138, perimeter: 72.1210103856
            with BuildLine():
                Line((0, 0), (5.0799999237, 7.6199998856))
                Line((2.5399999619, 10.1599998474), (5.0799999237, 7.6199998856))
                Line((5.0799999237, 12.6999998093), (2.5399999619, 10.1599998474))
                Line((2.5399999619, 15.2399997711), (5.0799999237, 12.6999998093))
                Line((5.0799999237, 17.779999733), (2.5399999619, 15.2399997711))
                Line((2.5399999619, 20.3199996948), (5.0799999237, 17.779999733))
                Line((5.0799999237, 22.8599996567), (2.5399999619, 20.3199996948))
                Line((2.5399999619, 23.9802152707), (5.0799999237, 22.8599996567))
                Line((-2.5036127375, 24.084747582), (2.5399999619, 23.9802152707))
                Line((-5.0918933771, 22.8755805038), (-2.5036127375, 24.084747582))
                Line((-2.4951783859, 20.2788655126), (-5.0918933771, 22.8755805038))
                Line((-5.0370220446, 17.7370218539), (-2.4951783859, 20.2788655126))
                Line((-2.5399999619, 15.2399997711), (-5.0370220446, 17.7370218539))
                Line((-5.0799999237, 12.6999998093), (-2.5399999619, 15.2399997711))
                Line((-2.5399999619, 10.1599998474), (-5.0799999237, 12.6999998093))
                Line((-5.0799999237, 7.6199998856), (-2.5399999619, 10.1599998474))
                Line((0, 0), (-5.0799999237, 7.6199998856))
            make_face()
        # OneSide extrude, distance=25.4
        extrude(amount=25.4)
    return part.part


# Description: This is a timing belt featuring a continuous loop design with regularly spaced teeth on the inner surface and a reinforced fabric covering on the outer surface, designed for power transmission in mechanical systems.
def model_45432_67aa4de8_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2026.82991639, perimeter: 159.5929068024
            with Locations((-0.5080000162, 0)):
                Circle(25.4)
        # OneSide extrude, distance=12.7
        extrude(amount=12.7)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 12.7, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1641.7321829632, perimeter: 143.633613965
            Circle(22.8599996567)
        # OneSide extrude, distance=-15.24
        extrude(amount=-15.24, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 59.5766305148, perimeter: 46.9036877936
            with BuildLine():
                Line((2.5399999619, 10.1599998474), (0, 0))
                Line((0, 0), (7.8649756152, 9.0108164418))
                Line((7.8649756152, 9.0108164418), (11.110070919, 19.9786363017))
                Line((11.110070919, 19.9786363017), (2.5399999619, 10.1599998474))
            make_face()
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)
    return part.part


# Description: This is a cylindrical ring or bushing with a rectangular slot or notch cut through one side of its curved surface.
def model_45433_80a435ab_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
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
        # Sketch on XY construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 35.3585115582, perimeter: 22.2362498802
            with BuildLine():
                CenterArc((-3.9649336721, 7.3826520451), 2.7332826884, -103.7401134383, 73.5376839742)
                CenterArc((-7.6199998856, 5.0799999237), 3.0264498199, -60.5249713538, 53.8380424104)
                CenterArc((-2.5399999619, 2.5399999619), 3.5921023945, -178.4887212288, 253.3630053045)
            make_face()
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)

        # Sketch2 -> Extrude3 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 54.9351635789, perimeter: 29.5821551238
            with BuildLine():
                CenterArc((-11.8686943711, 16.980075751), 2.9779765188, -92.9882315386, 95.5548274157)
                CenterArc((-7.6199998856, 12.6999998093), 4.5935500657, 163.4803559594, 2.8558678345)
                CenterArc((-14.0140008465, 10.8828889261), 3.4856159074, -24.043750383, 80.4132715008)
                CenterArc((-11.6428726368, 6.7051868423), 2.8746271945, 37.3005400754, 36.2905162865)
                CenterArc((-7.6199998856, 12.6999998093), 4.5935500657, -112.2076642842, 22.2076642842)
                CenterArc((-7.6199998856, 12.6999998093), 4.5935500657, -90, 13.2942583791)
                CenterArc((-3.9649336721, 7.3826520451), 2.7332826884, 87.0580481277, 74.8920171632)
                CenterArc((-7.6199998856, 12.6999998093), 4.5935500657, -34.2861449605, 140.3841533398)
            make_face()
            # Profile area: 16.9489326642, perimeter: 17.7585017376
            with BuildLine():
                CenterArc((-7.6199998856, 5.0799999237), 3.0264498199, 116.672040667, 82.6598165769)
                CenterArc((-11.6428726368, 6.7051868423), 2.8746271945, 22.0508645928, 15.2496754826)
                CenterArc((-7.6199998856, 12.6999998093), 4.5935500657, -134.6069886907, 22.3993244065)
                CenterArc((-14.0140008465, 10.8828889261), 3.4856159074, -96.8005722545, 72.1602862399)
                CenterArc((-11.6428726368, 6.7051868423), 2.8746271945, 165.5646210006, 128.3884123176)
            make_face()
            # Profile area: 18.8340483475, perimeter: 18.4194537582
            with BuildLine():
                CenterArc((-2.5399999619, 2.5399999619), 3.5921023945, 137.9183921699, 43.5928866013)
                CenterArc((-3.9649336721, 7.3826520451), 2.7332826884, 168.1610802706, 74.834025439)
                CenterArc((-7.6199998856, 5.0799999237), 3.0264498199, 71.1078957757, 18.8921042243)
                CenterArc((-7.6199998856, 5.0799999237), 3.0264498199, 90, 26.672040667)
                CenterArc((-11.6428726368, 6.7051868423), 2.8746271945, -66.0469666818, 88.0978312746)
                CenterArc((-7.6199998856, 5.0799999237), 3.0264498199, -160.6681427561, 100.1431714023)
            make_face()
            # Profile area: 25.324681436, perimeter: 22.0931750998
            with BuildLine():
                CenterArc((-14.0140008465, 10.8828889261), 3.4856159074, 139.6310013107, 123.5684264348)
                CenterArc((-11.6428726368, 6.7051868423), 2.8746271945, 74.9715814543, 90.5930395463)
                CenterArc((-7.6199998856, 12.6999998093), 4.5935500657, 166.3362237939, 58.1435620199)
                CenterArc((-14.0140008465, 10.8828889261), 3.4856159074, 56.3695211178, 14.2459631552)
                CenterArc((-14.0140008465, 10.8828889261), 3.4856159074, 70.615484273, 1.1844744949)
                CenterArc((-15.2399997711, 15.2399997711), 2.5399999619, -124.2535087532, 99.9379775849)
            make_face()
            # Profile area: 18.4508482827, perimeter: 18.559489618
            with BuildLine():
                CenterArc((-15.2399997711, 15.2399997711), 2.5399999619, -24.2790063684, 103.1584290147)
                CenterArc((-11.8686943711, 16.980075751), 2.9779765188, -110.7682688758, 1.3837532521)
                CenterArc((-11.8686943711, 16.980075751), 2.9779765188, -109.3845156236, 16.3962840851)
                CenterArc((-7.6199998856, 12.6999998093), 4.5935500657, 106.0980083792, 57.3823475802)
                CenterArc((-11.8686943711, 16.980075751), 2.9779765188, 2.5665958772, 162.8020892766)
            make_face()
            # Profile area: 14.7190961062, perimeter: 15.8215530046
            with BuildLine():
                CenterArc((-7.6199998856, 12.6999998093), 4.5935500657, -76.7057416209, 42.4195966604)
                CenterArc((-3.9649336721, 7.3826520451), 2.7332826884, 161.9500652908, 6.2110149797)
                CenterArc((-7.6199998856, 5.0799999237), 3.0264498199, 7.3948689996, 63.713026776)
                CenterArc((-2.5399999619, 2.5399999619), 3.5921023945, 74.8742840757, 50.484334799)
                CenterArc((-3.9649336721, 7.3826520451), 2.7332826884, -30.2024294641, 117.2604775918)
            make_face()
            # Profile area: 11.5047558777, perimeter: 15.4411070303
            with BuildLine():
                CenterArc((-14.0140008465, 10.8828889261), 3.4856159074, 71.7999587679, 67.8310425428)
                CenterArc((-15.2399997711, 15.2399997711), 2.5399999619, -24.3155311682, 0.0365247999)
                CenterArc((-11.8686943711, 16.980075751), 2.9779765188, 165.3686851537, 83.8630459705)
                CenterArc((-15.2399997711, 15.2399997711), 2.5399999619, 78.8794226464, 156.8670686005)
            make_face()
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)
    return part.part


# Description: This is a cylindrical sleeve or bushing with a hollow central bore and a rectangular slot or opening cut through its side, featuring a ribbed or textured surface pattern.
def model_45437_a98a4f45_0000():
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
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 100.0747271218, perimeter: 315.1959909347
            with BuildLine():
                CenterArc((0, 0), 25.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 24.765, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=25.4
        extrude(amount=25.4)

        # Sketch3 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 47.0699087649, perimeter: 36.1031846707
            with BuildLine():
                _nurbs_edge([(14.608757969, 19.997235199), (14.5951549765, 19.7821214022), (14.53953913, 19.3330440416), (14.3709014314, 18.6028890867), (13.9726825196, 17.5143201234), (13.172469476, 15.9529422482), (12.0587294909, 14.1835411893), (10.6418436646, 12.2130047424), (8.9991504161, 10.1221218076), (7.5151923235, 8.342646961), (6.3294528774, 6.9671266347), (5.5247443342, 6.0505062478), (5.1463478056, 5.6228295374)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.7856977137, 0.7856977137, 0.7856977137, 0.7856977137, 0.7856977137, 0.7856977137], 5)
                _nurbs_edge([(5.1463478056, 5.6228295374), (5.1623586055, 5.8404373798), (5.1760803902, 6.3060193443), (5.1420302996, 7.0311005564), (5.0369886488, 8.0348405096), (4.9597250725, 9.3439560238), (5.1005284541, 10.7313272885), (5.5819365282, 12.1668168686), (6.4718485097, 13.6482056329), (7.8043641738, 15.1730554623), (9.5893759739, 16.7390620241), (11.3768427747, 18.0233135746), (12.9161008273, 19.0036529041), (14.0299295343, 19.6647798622), (14.608757969, 19.997235199)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.3405061863, 0.3405061863, 0.3405061863, 0.3405061863, 0.3405061863, 0.3405061863, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9333333333, 1, 1, 1, 1, 1, 1], 5)
            make_face()
            # Profile area: 5.1681766828, perimeter: 15.6351333797
            with BuildLine():
                _nurbs_edge([(0, 0), (0.4096215781, 0.1977654649), (1.1872520534, 0.5975293322), (2.2288547658, 1.2098739684), (3.3661997862, 2.0519155625), (4.3672640488, 3.1483256226), (4.856981112, 4.086479751), (5.0540839413, 4.8191421209), (5.1231184661, 5.3268056954), (5.1444174685, 5.5965937164), (5.1463478056, 5.6228295374)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.3405061863, 0.3405061863, 0.3405061863, 0.3405061863, 0.3405061863, 0.3405061863], 5)
                _nurbs_edge([(5.1463478055, 5.6228295373), (5.0831963484, 5.5514535987), (4.57693176, 4.9799865466), (3.6044151295, 3.893075857), (2.5898458244, 2.7782634783), (1.5355290585, 1.6370789056), (0.5175192507, 0.5494591128), (0, 0)], [1, 1, 1, 1, 1, 1, 1, 1], [0.7856977137, 0.7856977137, 0.7856977137, 0.7856977137, 0.7856977137, 0.7856977137, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
            make_face()
        # OneSide extrude, distance=25.4
        extrude(amount=25.4)
    return part.part


# Description: This is a cylindrical flashlight with a dark gray barrel and a blue geometric faceted head at the top, featuring a textured grip section near the head.
def model_45468_eaf0dc99_0004():
    """Model: Screw v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5026548246, perimeter: 5.0265482457
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5542562584, perimeter: 2.7712812921
            with BuildLine():
                Line((-0.2309401077, 0.4), (-0.4618802154, 0))
                Line((-0.4618802154, 0), (-0.2309401077, -0.4))
                Line((-0.2309401077, -0.4), (0.2309401077, -0.4))
                Line((0.2309401077, -0.4), (0.4618802154, 0))
                Line((0.4618802154, 0), (0.2309401077, 0.4))
                Line((0.2309401077, 0.4), (-0.2309401077, 0.4))
            make_face()
        # OneSide extrude, distance=0.35
        extrude(amount=0.35, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical mesh or perforated container with an open top, featuring vertical slot-like perforations around its curved walls and a reinforced rim, appearing to be a filter basket or strainer component.
def model_45798_b573e9da_0005():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 22.9022111272, perimeter: 16.9646005822
            Circle(2.7000000402)
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.0090574659, perimeter: 10.0181148421
            with BuildLine():
                Line((-2.0090573763, 0.5000000075), (-2.0090573763, -0.5000000075))
                Line((-2.0090573763, -0.5000000075), (2.0000000298, -0.5000000075))
                Line((2.0000000298, -0.5000000075), (2.0000000298, 0.5000000075))
                Line((2.0000000298, 0.5000000075), (-2.0090573763, 0.5000000075))
            make_face()
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, -0.5000000075), x_dir=(1, 0, 0), z_dir=(0, 0, 1))) as sk:
            # Profile area: 0.5142754006, perimeter: 2.5421595705
            with Locations((0.0045286733, 3.5074493417)):
                Circle(0.4045972618)
        # TwoSides extrude, along=3.3, against=-2.3
        extrude(amount=3.3, mode=Mode.SUBTRACT)
        extrude(sk.sketch, amount=-2.3, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a triangular bracket or guide component with a pointed upper section, featuring an open slot through the center and a circular hole at the bottom for mounting or pivot purposes.
def model_45798_b573e9da_0012():
    """Model: Back Brace"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with BuildLine():
                CenterArc((4.0000000596, 15.0000002235), 0.6, 0, 180)
                CenterArc((4.0000000596, 15.0000002235), 0.6, 180, 180)
            make_face()
            # Profile area: 3.3345134252, perimeter: 9.9886126308
            with BuildLine():
                Line((4.6000000596, 15.0000002235), (6.0000000894, 16.5000002459))
                Line((2.0000000298, 16.5000002459), (6.0000000894, 16.5000002459))
                Line((3.4000000596, 15.0000002235), (2.0000000298, 16.5000002459))
                CenterArc((4.0000000596, 15.0000002235), 0.6, 0, 180)
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.0000000092, 0.0000001687, 0.4), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.515299735, perimeter: 2.5446900494
            with Locations((4.0000000504, 15.0000000548)):
                Circle(0.405)
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.0000000092, 0.0000001687, 0.4), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.7000000209, perimeter: 4.4413111893
            with BuildLine():
                Line((3.0000000447, 16.3000002429), (4.0000000596, 15.6000002325))
                Line((4.0000000596, 15.6000002325), (5.0000000745, 16.3000002429))
                Line((5.0000000745, 16.3000002429), (3.0000000447, 16.3000002429))
            make_face()
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical container or tube with a ribbed/knurled threaded cap on top, designed for storing or dispensing contents.
def model_45922_26941172_0007():
    """Model: bottle 18"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 27.4889357189, perimeter: 21.9911485751
            with BuildLine():
                CenterArc((75, -15), 3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((75, -15), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 27.4889357189, perimeter: 21.9911485751
            with BuildLine():
                CenterArc((-75, 15), 3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-75, 15), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-75, 15)):
                Circle(0.5)
        # OneSide extrude, distance=8
        extrude(amount=8, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 11, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 27.3397100679, perimeter: 18.5353966562
            with Locations((-75, 15)):
                Circle(2.95)
        # OneSide extrude, distance=-7.9
        extrude(amount=-7.9, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a boat hull or marine vessel component featuring an elongated, curved asymmetrical shape with a sharp bow, sloped sides, an open top section, and a flat or slightly curved bottom surface, designed for hydrodynamic water displacement.
def model_45922_26941172_0010():
    """Model: pedals 6"""
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
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 150, perimeter: 50
            with BuildLine():
                Line((60, 10), (45, 10))
                Line((60, 20), (60, 10))
                Line((45, 20), (60, 20))
                Line((45, 10), (45, 20))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.3150855798, perimeter: 8.1571068145
            with BuildLine():
                _nurbs_edge([(-46, -14), (-46.08, -13.9620761954), (-46.24, -13.889540454), (-46.48, -13.7906721407), (-46.8, -13.6790478619), (-47.2, -13.5754693053), (-47.6, -13.511055518), (-48, -13.4890026432), (-48.4, -13.511055518), (-48.8, -13.5754693053), (-49.2, -13.6790478619), (-49.52, -13.7906721407), (-49.76, -13.889540454), (-49.92, -13.9620761954), (-50, -14)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                Line((-46, -14), (-50, -14))
            make_face()
            # Profile area: 1.3150855798, perimeter: 8.1571068145
            with BuildLine():
                Line((-46, -16), (-50, -16))
                _nurbs_edge([(-46, -16), (-46.08, -16.0379238046), (-46.24, -16.110459546), (-46.48, -16.2093278593), (-46.8, -16.3209521381), (-47.2, -16.4245306947), (-47.6, -16.488944482), (-48, -16.5109973568), (-48.4, -16.488944482), (-48.8, -16.4245306947), (-49.2, -16.3209521381), (-49.52, -16.2093278593), (-49.76, -16.110459546), (-49.92, -16.0379238046), (-50, -16)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
            make_face()
            # Profile area: 116.0547432607, perimeter: 62.2131985559
            with BuildLine():
                Line((-45, -12.5), (-45, -10))
                Line((-45, -10), (-60, -10))
                Line((-60, -10), (-60, -20))
                Line((-60, -20), (-45, -20))
                Line((-45, -20), (-45, -17.5))
                _nurbs_edge([(-45, -17.5), (-45.12, -17.5379238046), (-45.36, -17.610459546), (-45.72, -17.7093278592), (-46.2, -17.8209521381), (-46.8, -17.9245306947), (-47.4, -17.988944482), (-48, -18.0109973568), (-48.6, -17.988944482), (-49.2, -17.9245306947), (-49.8, -17.8209521381), (-50.28, -17.7093278593), (-50.64, -17.610459546), (-50.88, -17.5379238046), (-51, -17.5)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                Line((-51, -17.5), (-51, -12.5))
                _nurbs_edge([(-45, -12.5), (-45.12, -12.4620761954), (-45.36, -12.389540454), (-45.72, -12.2906721407), (-46.2, -12.1790478619), (-46.8, -12.0754693053), (-47.4, -12.011055518), (-48, -11.9890026432), (-48.6, -12.011055518), (-49.2, -12.0754693053), (-49.8, -12.1790478619), (-50.28, -12.2906721407), (-50.64, -12.389540454), (-50.88, -12.4620761954), (-51, -12.5)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(51, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((15, 1)):
                Circle(0.5)
        # OneSide extrude, distance=-6.5
        extrude(amount=-6.5, mode=Mode.SUBTRACT)
    return part.part


# Description: A hex bolt or machine screw with a cylindrical shaft and hexagonal head, shown alongside its corresponding hex nut.
def model_45922_26941172_0015():
    """Model: screw sead 8"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-65, 15)):
                Circle(0.5)
        # OneSide extrude, distance=-6
        extrude(amount=-6)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.4616784181, perimeter: 7.2985145918
            with BuildLine():
                Line((-64.6380596554, 14.4092384687), (-64.307415334, 15.0180687674))
                Line((-64.307415334, 15.0180687674), (-64.6693556786, 15.6088302988))
                Line((-64.6693556786, 15.6088302988), (-65.3619403446, 15.5907615313))
                Line((-65.3619403446, 15.5907615313), (-65.692584666, 14.9819312326))
                Line((-65.692584666, 14.9819312326), (-65.3306443214, 14.3911697012))
                Line((-65.3306443214, 14.3911697012), (-64.6380596554, 14.4092384687))
            make_face()
            with BuildLine():
                CenterArc((-65, 15), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-65, 15)):
                Circle(0.5)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (NewBody)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.4616784181, perimeter: 7.2985145918
            with BuildLine():
                Line((-68.1995289552, 14.3757267015), (-67.8091279422, 14.9480789087))
                Line((-67.8091279422, 14.9480789087), (-68.109598987, 15.5723522072))
                Line((-68.109598987, 15.5723522072), (-68.8004710448, 15.6242732985))
                Line((-68.8004710448, 15.6242732985), (-69.1908720578, 15.0519210913))
                Line((-69.1908720578, 15.0519210913), (-68.890401013, 14.4276477928))
                Line((-68.890401013, 14.4276477928), (-68.1995289552, 14.3757267015))
            make_face()
            with BuildLine():
                CenterArc((-68.5, 15), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a dark gray plastic or metal bracket or clasp featuring an elongated upper arm with a curved hook or loop protrusion at the lower end, designed for gripping, holding, or securing components together.
def model_46086_371b5052_0002():
    """Model: Bottle Opener v5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 9 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.8871468345, perimeter: 10.103010341
            with BuildLine():
                Line((0, 2.7), (0, 0))
                Line((0, 0), (1.0181459801, 0))
                Line((1.25, 1.425), (1.0181459801, 0))
                CenterArc((1.1250195935, 1.425), 0.1249804065, 0, 180)
                Line((1.000039187, 1.425), (1.000039187, 1.2540813166))
                CenterArc((0.925, 1.7747012551), 0.526, 154.638717412, 123.5630839151)
                Line((0.9, 2.95), (0.4496932826, 2))
                Line((0.75, 3.7), (0.9, 2.95))
                Line((0.75, 3.7), (0.4, 3.7))
                Line((0, 2.7), (0.4, 3.7))
            make_face()
        # OneSide extrude, distance=0.16
        extrude(amount=0.16)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.16), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.28, perimeter: 2.3
            with BuildLine():
                Line((0.35, 0.8), (0, 0.8))
                Line((0, 0.8), (0, 0))
                Line((0, 0), (0.35, 0))
                Line((0.35, 0), (0.35, 0.8))
            make_face()
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((0.65, 0.2)):
                Circle(0.1)
        # OneSide extrude, distance=-2.6
        extrude(amount=-2.6, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.16), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.042475184, perimeter: 2.0107210206
            with BuildLine():
                CenterArc((-1.9114916731, 1.875), 2, -14.4775121859, 28.9550243719)
                Line((0.025, 1.375), (0.025, 2.375))
            make_face()
        # OneSide extrude, distance=-0.01
        extrude(amount=-0.01, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a curved sheet metal panel or trim piece with a trapezoidal shape, featuring a slightly angled profile, a central slot or depression running along its length, and rounded edges on both ends.
def model_46086_371b5052_0007():
    """Model: Small Part v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.7739614129, perimeter: 11.8637155809
            with BuildLine():
                Line((0, 0), (2.4558031396, 0))
                Line((2.4558031396, 0), (2.5607780479, 0.1))
                Line((2.5607780479, 0.1), (5.5607780479, 0.1))
                CenterArc((3.8838055154, -2.3875214824), 3, 56.0139634133, 28.7583546815)
                Line((0, 0.6), (4.1571466801, 0.6))
                Line((0, 0), (0, 0.6))
            make_face()
        # OneSide extrude, distance=0.16
        extrude(amount=0.16)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.16), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((0.365, 0.2650000043)):
                Circle(0.1)
        # OneSide extrude, distance=-4.4
        extrude(amount=-4.4, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.16), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0740435744, perimeter: 2.4187706161
            with BuildLine():
                CenterArc((3.7564604706, 2.4678784025), 2, -107.4576031237, 34.9152062474)
                Line((3.1564604706, 0.5599999997), (4.3564604706, 0.5599999997))
            make_face()
        # OneSide extrude, distance=-0.05
        extrude(amount=-0.05, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a curved blade or deflector panel with an elongated horizontal profile, featuring a flat top surface with a raised edge/flange along one side and a downward-curved or swept end section, designed for aerodynamic flow direction or protective shielding.
def model_46086_371b5052_0012():
    """Model: Nail Polisher v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.1161856121, perimeter: 9.3729599349
            with BuildLine():
                Line((0, 0), (3.2, 0))
                CenterArc((3.8208298714, -0.6422126526), 0.8932339113, 58.0218579977, 76.0082410961)
                CenterArc((2.6591366615, -2.4), 3, 56.9811208914, 33.0188791086)
                Line((0, 0.6), (2.6591366615, 0.6))
                Line((0, 0), (0, 0.6))
            make_face()
        # OneSide extrude, distance=0.16
        extrude(amount=0.16)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.16), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((0.35, 0.32)):
                Circle(0.1)
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0006197916, perimeter: 0.108333325
            with BuildLine():
                Line((3.0599999316, 0.1949999956), (3.0599999316, 0.16))
                Line((3.0349999322, 0.1949999956), (3.0599999316, 0.1949999956))
                Line((3.0495832637, 0.16), (3.0349999322, 0.1949999956))
                Line((3.0599999316, 0.16), (3.0495832637, 0.16))
            make_face()
            # Profile area: 0.0001302084, perimeter: 0.0625000075
            with BuildLine():
                Line((3.0599999316, 0.16), (3.0599999316, 0.134999997))
                Line((3.0599999316, 0.16), (3.0495832637, 0.16))
                Line((3.0599999316, 0.134999997), (3.0495832637, 0.16))
            make_face()
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a rectangular tray or pan with rounded corners, featuring four raised flanges or walls along its perimeter and what appears to be mesh or textured inserts on the corners.
def model_48332_fb679f90_0003():
    """Model: pedal"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 44.5707963268, perimeter: 27.1415926536
            with BuildLine():
                CenterArc((-8.5, 4), 1, 0, 90)
                Line((-8.5, 5), (-15.5, 5))
                CenterArc((-15.5, 4), 1, 90, 90)
                Line((-16.5, 4), (-16.5, 0))
                Line((-16.5, 0), (-7.5, 0))
                Line((-7.5, 0), (-7.5, 4))
            make_face()
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 31.5707960139, perimeter: 23.1415924897
            with BuildLine():
                Line((-8.0000000298, 3.4999999702), (-8.0000001192, 0.5000000075))
                CenterArc((-9.0000000298, 3.5), 1, -0.0000017075, 90.0000017075)
                Line((-15, 4.5), (-9.0000000298, 4.5))
                CenterArc((-15, 3.5), 1, 90, 90)
                Line((-16, 0.5000000075), (-16, 3.5))
                Line((-8.0000001192, 0.5000000075), (-16, 0.5000000075))
            make_face()
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a polymer magazine follower or ammunition feed component with an elongated cylindrical body, a tapered upper end with a V-notched top, ribbed grip sections on the lower portion, and a flat base with horizontal grooves for retention or guidance within a magazine assembly.
def model_48332_fb679f90_0009():
    """Model: valve lever"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.1034131683, perimeter: 5.5039986466
            with BuildLine():
                CenterArc((18.8372602165, -0.0668043336), 1.2257166316, -112.8403755059, 33.2007066345)
                CenterArc((18.6172860702, -0.5737263439), 0.6731825175, -140.7117977039, 28.3783972684)
                Line((18.3878944609, -2.9961767958), (18.0962625852, -1))
                CenterArc((18.5884530192, -2.9688285761), 0.2024145757, -8.8586964027, 196.6236731991)
                Line((19.057690796, -1.2725371484), (18.7884530192, -3.0000000447))
            make_face()
        # Symmetric extrude, each_side=0.2
        extrude(amount=0.2, both=True)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.4036993819, perimeter: 3.1653935297
            with BuildLine():
                CenterArc((18.5884530192, -2.9688285761), 0.2024145757, -8.8586964027, 196.6236731991)
                Line((18.3884530192, -3.0000000447), (18.3878944609, -2.9961767958))
                CenterArc((16.9720754378, -3.4500000224), 1.4861444859, -17.6256705119, 35.2513410238)
                CenterArc((18.5884530192, -3.9003334089), 0.2000002779, 179.9044854724, 180.1910290552)
                CenterArc((19.8747737716, -3.4500000224), 1.1758370452, 157.498595921, 45.0028081581)
            make_face()
        # Symmetric extrude, each_side=0.55
        extrude(amount=0.55, both=True, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.4993904739, perimeter: 4.4863828707
            with BuildLine():
                CenterArc((18.9384807005, -0.3), 0.3062428106, 0, 78.4112846554)
                Line((18.2000002712, 0), (19.0000002831, 0))
                CenterArc((18.2492408325, -0.3), 0.3040141985, 99.3211424894, 80.6788575106)
                Line((17.945226634, -0.3), (17.945226634, -0.5348571265))
                CenterArc((18.6172860702, -0.5737263439), 0.6731825175, 176.6899297757, 42.5982725204)
                CenterArc((18.6172860702, -0.5737263439), 0.6731825175, -140.7117977039, 28.3783972684)
                CenterArc((18.8372602165, -0.0668043336), 1.2257166316, -112.8403755059, 33.2007066345)
                CenterArc((18.996939681, -1.032316149), 0.2477838302, -75.8076536647, 75.8076536647)
                Line((19.2447235111, -0.3), (19.2447235111, -1.032316149))
            make_face()
        # Symmetric extrude, each_side=0.24
        extrude(amount=0.24, both=True, mode=Mode.ADD)

        # Sketch2 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.24), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-18.6468301136, -0.3)):
                Circle(0.15)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a curved mesh or perforated panel component with an organic, rounded trapezoidal shape featuring a textured mesh surface on one side and a solid back, likely designed as a ventilation, filtering, or structural support element.
def model_49016_cd1b47bf_0027():
    """Model: kojec v7"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 353.4291735289, perimeter: 67.9924825014
            Ellipse(12.5, 9)
        # OneSide extrude, distance=10
        extrude(amount=10)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 10, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 219.9114857513, perimeter: 53.8236898144
            Ellipse(10, 7)
        # OneSide extrude, distance=-7
        extrude(amount=-7, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 80.8497769132, perimeter: 57.2362580611
            with BuildLine():
                Line((-9, 3), (-13.5952118201, -3.7029595502))
                Line((-13.5952118201, -3.7029595502), (11.1724044676, -1.4283825442))
                Line((11.1724044676, -1.4283825442), (9, 3))
                CenterArc((0, 15), 15, -126.8698976458, 73.7397952917)
            make_face()
        # Symmetric extrude, each_side=22
        extrude(amount=22, both=True, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a disk or wheel component with an oblate ellipsoidal shape featuring a central circular hole, radial ribbing or spoke-like patterns extending from the center, and a raised outer flange or rim.
def model_49019_748c9a9f_0012():
    """Model: TACKA v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 28.2743338823, perimeter: 18.8495559215
            Circle(3)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            Circle(2.5)
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=-2.8
        extrude(amount=-2.8, mode=Mode.SUBTRACT)
    return part.part


# Description: A cylindrical fastener with a hexagonal head at one end and a threaded shaft, designed for securing components together.
def model_49019_748c9a9f_0019():
    """Model: rurkaa v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.5393804003, perimeter: 4.398229715
            Circle(0.7)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=10
        extrude(amount=10, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 10.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=-12.5
        extrude(amount=-12.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a boat or inflatable raft featuring a dark gray/charcoal hull with blue trim and interior detailing, characterized by a symmetrical rounded rectangular body with upturned bow and stern, and dual side chambers for buoyancy.
def model_49121_adb01620_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 119.3103701271, perimeter: 57.4458727849
            with BuildLine():
                Line((11.7602936753, -8.5), (11.7602936753, 2.17945741))
                Line((11.7602936753, 2.17945741), (0, 2.17945741))
                Line((0, 2.17945741), (0, -8.5))
                Line((0, -8.5), (11.7602936753, -8.5))
            make_face()
            with BuildLine():
                CenterArc((10, 0), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((10, -6.5), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 100.5113887926, perimeter: 53.9252854343
            with BuildLine():
                Line((0, 2.17945741), (0, -8.5))
                Line((0, 2.17945741), (-10, 2.17945741))
                Line((-10, 2.17945741), (-10, -8.5))
                Line((-10, -8.5), (0, -8.5))
            make_face()
            with BuildLine():
                CenterArc((-7.5, -6.5), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-7.5, 0), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((7.5, -6.5)):
                Circle(1)
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((-10, -6.5)):
                Circle(1)
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((-10, 0)):
                Circle(1)
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((7.5, 0)):
                Circle(1)
        # OneSide extrude, distance=6
        extrude(amount=6)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 43.7083895408, perimeter: 27.1219012477
            with BuildLine():
                Line((-10, 2.114728705), (-10, -8.435271295))
                CenterArc((-10, -3.160271295), 5.275, 90, 180)
            make_face()
            # Profile area: 43.7083895408, perimeter: 27.1219012477
            with BuildLine():
                Line((11.7602936753, -8.435271295), (11.7602936753, 2.114728705))
                CenterArc((11.7602936753, -3.160271295), 5.275, -90, 180)
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical tube or pipe with a hollow center, featuring rounded ends and a slightly tapered or beveled top edge.
def model_49145_4a5b250e_0002():
    """Model: dynks"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0176714587, perimeter: 0.471238898
            Circle(0.075)
        # OneSide extrude, distance=1.1
        extrude(amount=1.1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0063813601, perimeter: 1.0210176124
            with BuildLine():
                CenterArc((0, 0), 0.0875, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.075, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0176714587, perimeter: 0.471238898
            Circle(0.075)
        # OneSide extrude, distance=0.03
        extrude(amount=0.03, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0063813601, perimeter: 1.0210176124
            with BuildLine():
                CenterArc((0, 0), 0.0875, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.075, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0176714587, perimeter: 0.471238898
            Circle(0.075)
        # OneSide extrude, distance=0.03
        extrude(amount=0.03, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical sleeve or spacer with a slightly larger diameter section at the top and a smaller diameter shaft at the bottom, featuring a stepped design and textured or knurled surfaces.
def model_49145_4a5b250e_0004():
    """Model: to cos"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6361725124, perimeter: 2.8274333882
            Circle(0.45)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3848450851, perimeter: 2.1991148195
            with BuildLine():
                CenterArc((0.0014066007, -0.0999935269), 0.35, -88.6568011084, 358.9254458699)
                CenterArc((0, 0), 0.45, -89.6119579156, 0.8357594844)
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2513274273, perimeter: 5.0134201285
            with BuildLine():
                CenterArc((0, 0), 0.45, -88.7761984312, 359.1642405156)
                CenterArc((0.0014066007, -0.0999935269), 0.35, -88.6568011084, 358.9254458699)
            make_face()
            # Profile area: 0.3848450851, perimeter: 2.1991148195
            with BuildLine():
                CenterArc((0.0014066007, -0.0999935269), 0.35, -88.6568011084, 358.9254458699)
                CenterArc((0, 0), 0.45, -89.6119579156, 0.8357594844)
            make_face()
        # OneSide extrude, distance=1.7
        extrude(amount=1.7, mode=Mode.ADD)
    return part.part


# Description: This is a horizontal structural beam or shaft support with a long rectangular body and symmetrical blue flanged end caps on both sides, featuring notched cutouts for mounting or alignment purposes.
def model_49145_4a5b250e_0005():
    """Model: precik"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-1, 1)):
                Circle(0.3)
        # OneSide extrude, distance=4.5
        extrude(amount=4.5)

        # Sketch5 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(4.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0469800385, perimeter: 1.1568793295
            with BuildLine():
                Line((-1.1430941216, 1.2636741784), (-1.2150370572, 1.3962407312))
                CenterArc((-1, 1), 0.3, 44.2098954708, 74.2784770576)
                Line((-0.7849629428, 1.3962407312), (-0.7849629428, 1.2091866727))
                Line((-1.2150370572, 1.3962407312), (-0.7849629428, 1.3962407312))
            make_face()
            # Profile area: 0.1169098145, perimeter: 1.4978861987
            with BuildLine():
                CenterArc((-1, 1), 0.3, 44.2098954708, 74.2784770576)
                Line((-0.8569058784, 0.7363258216), (-1.1430941216, 1.2636741784))
                CenterArc((-1, 1), 0.3, -61.5116274716, 17.3017320008)
                Line((-0.7849629428, 1.2091866727), (-0.7849629428, 0.7908133273))
            make_face()
            # Profile area: 0.0065230286, perimeter: 0.4284756757
            with BuildLine():
                CenterArc((-1, 1), 0.3, 118.4883725284, 17.3017320008)
                Line((-1.1430941216, 1.2636741784), (-1.2150370572, 1.3962407312))
                Line((-1.2150370572, 1.2091866727), (-1.2150370572, 1.3962407312))
            make_face()
            # Profile area: 0.0469800385, perimeter: 1.1568793295
            with BuildLine():
                Line((-0.7849629428, 0.6037592688), (-0.8569058784, 0.7363258216))
                CenterArc((-1, 1), 0.3, -135.7901045292, 74.2784770576)
                Line((-1.2150370572, 0.6037592688), (-1.2150370572, 0.7908133273))
                Line((-0.7849629428, 0.6037592688), (-1.2150370572, 0.6037592688))
            make_face()
            # Profile area: 0.0065230286, perimeter: 0.4284756757
            with BuildLine():
                CenterArc((-1, 1), 0.3, -61.5116274716, 17.3017320008)
                Line((-0.7849629428, 0.6037592688), (-0.8569058784, 0.7363258216))
                Line((-0.7849629428, 0.7908133273), (-0.7849629428, 0.6037592688))
            make_face()
            # Profile area: 0.1169098145, perimeter: 1.4978861987
            with BuildLine():
                Line((-1.2150370572, 0.7908133273), (-1.2150370572, 1.2091866727))
                CenterArc((-1, 1), 0.3, -135.7901045292, 74.2784770576)
                Line((-0.8569058784, 0.7363258216), (-1.1430941216, 1.2636741784))
                CenterArc((-1, 1), 0.3, 118.4883725284, 17.3017320008)
            make_face()
        # OneSide extrude, distance=0.7
        extrude(amount=0.7, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.0037592598, 0.0150370393), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0535030671, perimeter: 1.2836950847
            with BuildLine():
                Line((0.7699259035, 0.6000000089), (0.7699259035, 0.7870540675))
                Line((1.2000000179, 0.6000000089), (0.7699259035, 0.6000000089))
                Line((1.2000000179, 0.7870540675), (1.2000000179, 0.6000000089))
                CenterArc((0.9849629607, 0.9962407402), 0.3, -135.7901045292, 91.5802090584)
            make_face()
            # Profile area: 0.0535030671, perimeter: 1.2836950847
            with BuildLine():
                CenterArc((0.9849629607, 0.9962407402), 0.3, 44.2098954708, 91.5802090584)
                Line((1.2000000179, 1.3924814714), (1.2000000179, 1.2054274129))
                Line((0.7699259035, 1.3924814714), (1.2000000179, 1.3924814714))
                Line((0.7699259035, 1.2054274129), (0.7699259035, 1.3924814714))
            make_face()
            # Profile area: 0.233819629, perimeter: 1.7957723975
            with BuildLine():
                Line((0.7699259035, 0.7870540675), (0.7699259035, 1.2054274129))
                CenterArc((0.9849629607, 0.9962407402), 0.3, -135.7901045292, 91.5802090584)
                Line((1.2000000179, 1.2054274129), (1.2000000179, 0.7870540675))
                CenterArc((0.9849629607, 0.9962407402), 0.3, 44.2098954708, 91.5802090584)
            make_face()
        # OneSide extrude, distance=0.7
        extrude(amount=0.7, mode=Mode.ADD)
    return part.part


# Description: This is a mesh filter or strainer basket with an oval cylindrical shape, featuring a solid base section and a perforated mesh upper half for fluid or particle filtration.
def model_49145_4a5b250e_0011():
    """Model: zacisk"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.930198102, perimeter: 15.3938040026
            with BuildLine():
                CenterArc((0, 0), 2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.45, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 16.6582950457, perimeter: 31.7300858013
            with BuildLine():
                CenterArc((0, 0), 3.05, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-1.3
        extrude(amount=-1.3)
    return part.part


# Description: This is a twisted or warped flat blade or fin with a tapered, elongated shape that transitions from a wider section at one end to a narrower point at the other, featuring a curved twist along its length.
def model_49222_cbe1959b_0002():
    """Model: Base Plate"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 10), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.6000000089, perimeter: 6.400000006
            with BuildLine():
                Line((-3, 0), (0, 0))
                Line((0, 0.200000003), (0, 0))
                Line((0, 0.200000003), (-3, 0.200000003))
                Line((-3, 0.200000003), (-3, 0))
            make_face()
        # OneSide extrude, distance=-10
        extrude(amount=-10)

        # Sketch4 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 5, perimeter: 20.1980390272
            with BuildLine():
                Line((-2, 5), (-3, 0))
                Line((-3, 10), (-2, 5))
                Line((-3, 10), (-3, 0))
            make_face()
            # Profile area: 5, perimeter: 20.1980390272
            with BuildLine():
                Line((0, 0), (0, 10))
                Line((-1, 5), (0, 10))
                Line((0, 0), (-1, 5))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a hammer consisting of a cylindrical dark gray handle with a blue polyhedral striking head on top, featuring a roughly cubic/octahedral shape with multiple faceted surfaces typical of a hammer's striking face and peen.
def model_49330_c6744767_0005():
    """Model: screw 12"""
    with BuildPart() as part:
        # Sketch3 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((6, -50)):
                Circle(0.25)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch4 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6696758629, perimeter: 5.0348979419
            with BuildLine():
                Line((-6.1494283313, 50.5576777808), (-6.5576772909, 50.1494301595))
                Line((-6.5576772909, 50.1494301595), (-6.4082489596, 49.5917523787))
                Line((-6.4082489596, 49.5917523787), (-5.8505716687, 49.4423222192))
                Line((-5.8505716687, 49.4423222192), (-5.4423227091, 49.8505698405))
                Line((-5.4423227091, 49.8505698405), (-5.5917510404, 50.4082476213))
                Line((-5.5917510404, 50.4082476213), (-6.1494283313, 50.5576777808))
            make_face()
            with BuildLine():
                CenterArc((-6, 50), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-6, 50)):
                Circle(0.25)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical rod or shaft with rounded ends and a slightly flattened top surface, featuring a horizontal slot or groove running along its length.
def model_49330_c6744767_0008():
    """Model: wheel axle 2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            with Locations((-50, 0)):
                Circle(1.5)
        # OneSide extrude, distance=-60
        extrude(amount=-60)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-60, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((50, 0)):
                Circle(1)
        # OneSide extrude, distance=4
        extrude(amount=4, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((-50, 0)):
                Circle(1)
        # OneSide extrude, distance=4
        extrude(amount=4, mode=Mode.ADD)
    return part.part


# Description: This is a clevis rod or eye bolt, featuring a long cylindrical shaft with a looped eye at the top and a rounded ball or knob at the bottom, used for mechanical linkages and connections.
def model_49502_0ed856f7_0008():
    """Model: Connecting Rod"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 47.9914638994, perimeter: 66.1694766866
            with BuildLine():
                Line((-1, 22), (-1, 5.0306623509))
                CenterArc((0, 4.2000000626), 1.2999999374, 140.2848660888, 259.4302678223)
                Line((1, 5.0306623509), (1, 22))
                CenterArc((5.75, 17.75), 6.373774392, 122.2674527047, 15.9123774152)
                CenterArc((0, 24), 2.5, -20.1343824848, 218.0230460541)
                CenterArc((-4.25, 19.75), 3.9528470752, 34.6951535312, 27.0564632589)
            make_face()
            with BuildLine():
                CenterArc((0, 24), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 4.2000000626), 0.5999999374, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides extrude (symmetric), distance=0.75
        extrude(amount=0.75, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.75), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 15.5000004619, perimeter: 33.0000004917
            with BuildLine():
                Line((0.5000000075, 6.0000000894), (-0.5000000075, 6.0000000894))
                Line((0.5000000075, 21.5000003204), (0.5000000075, 6.0000000894))
                Line((-0.5000000075, 21.5000003204), (0.5000000075, 21.5000003204))
                Line((-0.5000000075, 6.0000000894), (-0.5000000075, 21.5000003204))
            make_face()
        # OneSide extrude, distance=-0.25
        extrude(amount=-0.25, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.75), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 15.5000004619, perimeter: 33.0000004917
            with BuildLine():
                Line((0.5000000075, 6.0000000894), (-0.5000000075, 6.0000000894))
                Line((0.5000000075, 21.5000003204), (0.5000000075, 6.0000000894))
                Line((-0.5000000075, 21.5000003204), (0.5000000075, 21.5000003204))
                Line((-0.5000000075, 6.0000000894), (-0.5000000075, 21.5000003204))
            make_face()
        # OneSide extrude, distance=-0.25
        extrude(amount=-0.25, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a ball valve or spherical control knob featuring a rounded spherical head on the left with a cylindrical shaft extending to the right, incorporating horizontal slot details and what appears to be a textured or knurled surface for grip.
def model_49503_e42c01c0_0000():
    """Model: fork bearing"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 6.2831853072, perimeter: 12.5663706144
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.0106192983, perimeter: 5.0265482457
            with Locations((-1.0000000149, 0)):
                Circle(0.8)
        # OneSide extrude, distance=6
        extrude(amount=6, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.3926990817, perimeter: 2.5707963268
            with BuildLine():
                Line((0, 0.5), (0, -0.5))
                CenterArc((0, 0), 0.5, -90, 180)
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical tube or pipe with a slightly tapered end, featuring a smooth rounded cap or boss at the top and a hollow interior running along its length.
def model_49503_e42c01c0_0001():
    """Model: Steering wheel"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.8849555922, perimeter: 18.8495559215
            with BuildLine():
                CenterArc((0, 0), 1.6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=20
        extrude(amount=20)

        # Sketch2 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 20, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.8849555922, perimeter: 18.8495559215
            with BuildLine():
                CenterArc((0, 0), 1.6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 6.157521601, perimeter: 8.7964594301
            Circle(1.4)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)
    return part.part


# Description: This is a fastener or standoff with a cylindrical shaft and a polygonal (likely hexagonal) base, featuring a threaded or grooved upper end and a multi-faceted mounting foot designed for secure attachment or alignment.
def model_49562_6df35938_0005():
    """Model: Mast-Joint bolt"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4156921938, perimeter: 2.4
            with BuildLine():
                Line((0.3447266906, -0.2028879218), (0.3480694397, 0.1970981105))
                Line((0.3480694397, 0.1970981105), (0.0033427491, 0.3999860323))
                Line((0.0033427491, 0.3999860323), (-0.3447266906, 0.2028879218))
                Line((-0.3447266906, 0.2028879218), (-0.3480694397, -0.1970981105))
                Line((-0.3480694397, -0.1970981105), (-0.0033427491, -0.3999860323))
                Line((-0.0033427491, -0.3999860323), (0.3447266906, -0.2028879218))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=1.7
        extrude(amount=1.7, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical sleeve or barrel with a hollow core, featuring a rounded closed end on one side and an open end on the other, with a small hole near the closed end.
def model_49613_1b97c07b_0004():
    """Model: cap tube"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 8.6393797974, perimeter: 34.5575191895
            with BuildLine():
                CenterArc((0, -10), 3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, -10), 2.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=4
        extrude(amount=4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            with Locations((0, -10)):
                Circle(2.5)
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -2), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            with Locations((0, -10)):
                Circle(2)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical connector or coupling component with a hemispherical or domed top end and a flat circular base, featuring a mesh or perforated pattern on the curved upper surface.
def model_49613_1b97c07b_0007():
    """Model: focus control"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 40.7150407905, perimeter: 22.6194671058
            with Locations((30, -5)):
                Circle(3.6)
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.03925898, perimeter: 0.9890866898
            with BuildLine():
                Line((-30.1988413401, -1.5000003469), (-30.1988413401, -1.4054955666))
                Line((-29.7988413401, -1.5000003469), (-30.1988413401, -1.5000003469))
                Line((-29.7988413401, -1.4056245058), (-29.7988413401, -1.5000003469))
                CenterArc((-30, -5), 3.6, 86.796792128, 6.3694774047)
            make_face()
        # OneSide extrude, distance=-5
        extrude(amount=-5, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude6 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 38.4845065959, perimeter: 21.9911476007
            with Locations((-30, -5)):
                Circle(3.4999998449)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


# Description: This is a pyramidal or tetrahedral bracket assembly with three protruding cylindrical posts or pins extending from its angled faces, featuring internal ribbed reinforcement and a dark blue anodized finish.
def model_49693_200d4b5d_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch3 -> Extrude3 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 17.3849153842, perimeter: 16.689613796
            with BuildLine():
                Line((0, 4.3274362104), (0, 0))
                Line((0, 0), (4.0173706876, 0))
                Line((4.0173706876, 0), (4.0173706876, 4.3274362104))
                Line((4.0173706876, 4.3274362104), (0, 4.3274362104))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.2, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((0.85, 3.4774362104)):
                Circle(0.25)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((3.1673706876, 3.4774362104)):
                Circle(0.25)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((3.1673706876, 0.85)):
                Circle(0.25)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((0.85, 0.85)):
                Circle(0.25)
        # OneSide extrude, distance=2.3
        extrude(amount=2.3, mode=Mode.ADD)
    return part.part


# Description: This is a cable management clip or routing bracket featuring a blue central channel with black rubber or elastomer end caps and curved flanges designed to secure and organize cables or hoses along a surface.
def model_49803_beeceeef_0000():
    """Model: 矩形 v12"""
    with BuildPart() as part:
        # Sketch1 -> 擠出1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0157079633, perimeter: 0.5141592654
            with BuildLine():
                CenterArc((1.4, -0.25), 0.1, 0, 180)
                Line((1.3, -0.25), (1.5, -0.25))
            make_face()
            # Profile area: 2.3417656186, perimeter: 16.2154834327
            with BuildLine():
                Line((1.5, 0.55), (-1.0669872981, 0.55))
                CenterArc((-1.5, 0), 0.7, 51.7867892983, 256.4264214035)
                Line((-1.0669872981, -0.55), (1.5, -0.55))
                Line((1.5, -0.25), (1.5, -0.55))
                Line((1.3, -0.25), (1.5, -0.25))
                Line((-1.1877501001, -0.25), (1.3, -0.25))
                CenterArc((-1.5, 0), 0.4, 38.6821874535, 282.635625093)
                Line((1.5, 0.25), (-1.1877501001, 0.25))
                Line((1.5, 0.55), (1.5, 0.25))
            make_face()
        # Symmetric extrude, each_side=0.5
        extrude(amount=0.5, both=True)

        # Sketch2 -> 擠出2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.25, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 2.1849811761, perimeter: 7.9680385636
            with BuildLine():
                Line((1.5, 0.5), (0.6339745962, 0.5))
                Line((1.5, -0.5), (1.5, 0.5))
                Line((0.6339745962, -0.5), (1.5, -0.5))
                CenterArc((1.5, 0), 1, -150, 300)
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.ADD)

        # Sketch3 -> 擠出3 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.55, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((-1.5, 0)):
                Circle(0.6)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)

        # Sketch3 -> 擠出4 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.55, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.4137166941, perimeter: 9.4247779608
            with BuildLine():
                CenterArc((-1.5, 0), 0.9, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-1.5, 0), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a pulley or idler assembly featuring a central rectangular base plate with two black cylindrical wheels/rollers mounted on opposite sides, connected by blue tensioning straps or belts, designed to guide and maintain tension on a mechanical belt or chain system.
def model_49806_24485616_0000():
    """Model: clip v4"""
    with BuildPart() as part:
        # Sketch1 -> 拉伸1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0143819356, perimeter: 0.5004387708
            with BuildLine():
                CenterArc((1.4002203596, -0.2566350098), 0.1, 3.8043754137, 172.3912491727)
                Line((1.5, -0.25), (1.3004407191, -0.25))
            make_face()
            # Profile area: 2.3417656186, perimeter: 16.2154834327
            with BuildLine():
                Line((1.5, -0.2632700195), (1.5, -0.55))
                Line((1.5, -0.25), (1.5, -0.2632700195))
                Line((1.5, -0.25), (1.3004407191, -0.25))
                Line((1.3004407191, -0.25), (-1.1877501001, -0.25))
                CenterArc((-1.5, 0), 0.4, 38.6821874535, 282.635625093)
                Line((-1.1877501001, 0.25), (1.5, 0.25))
                Line((1.5, 0.55), (1.5, 0.25))
                Line((-1.0669872981, 0.55), (1.5, 0.55))
                CenterArc((-1.5, 0), 0.7, 51.7867892983, 256.4264214035)
                Line((1.5, -0.55), (-1.0669872981, -0.55))
            make_face()
        # Symmetric extrude, each_side=0.5
        extrude(amount=0.5, both=True)

        # Sketch2 -> 拉伸2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.25, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 2.1849811761, perimeter: 7.9680385636
            with BuildLine():
                Line((1.5, 0.5), (0.6339745962, 0.5))
                Line((1.5, -0.5), (1.5, 0.5))
                Line((0.6339745962, -0.5), (1.5, -0.5))
                CenterArc((1.5, 0), 1, -150, 300)
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.ADD)

        # Sketch3 -> 拉伸3 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.55, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.4137166941, perimeter: 9.4247779608
            with BuildLine():
                CenterArc((-1.5, 0), 0.9, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-1.5, 0), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)

        # Sketch3 -> 拉伸4 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.55, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((-1.5, 0)):
                Circle(0.6)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a seat component with two cylindrical backrests mounted on a blue base platform, featuring mesh-textured surfaces on the upper portions and a central divider creating a two-seat configuration.
def model_49904_639055dd_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 8.0707963268, perimeter: 16.1415926536
            with BuildLine():
                CenterArc((0, 2.5), 1, 0, 180)
                Line((-1, 0.5), (-1, 2.5))
                Line((-1, 0.5), (-2.5, 0.5))
                Line((-2.5, 0.5), (-2.5, 0))
                Line((-2.5, 0), (2.5, 0))
                Line((2.5, 0), (2.5, 0.5))
                Line((2.5, 0.5), (1, 0.5))
                Line((1, 2.5), (1, 0.5))
            make_face()
        # Symmetric extrude, each_side=2
        extrude(amount=2, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 8.8400002635, perimeter: 12.0000001788
            with BuildLine():
                Line((1.3000000194, 1.8000000268), (1.3000000194, 5.2000000775))
                Line((1.3000000194, 5.2000000775), (-1.3000000194, 5.2000000775))
                Line((-1.3000000194, 5.2000000775), (-1.3000000194, 1.8000000268))
                Line((-1.3000000194, 1.8000000268), (1.3000000194, 1.8000000268))
            make_face()
        # Symmetric extrude, each_side=2.5
        extrude(amount=2.5, both=True, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((0, 2.5)):
                Circle(1)
        # Symmetric extrude, each_side=1.2
        extrude(amount=1.2, both=True, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a slender cylindrical rod or shaft with a slightly tapered design, featuring a smooth, uniform surface with minimal features.
def model_49930_20f0e2ee_0002():
    """Model: Support Rod"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with Locations((5.0799999237, -5.0799999237)):
                Circle(0.3175)
        # OneSide extrude, distance=3.81
        extrude(amount=3.81)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.9500765233, perimeter: 5.9847340051
            with BuildLine():
                CenterArc((5.0799999237, -5.0799999237), 0.635, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((5.0799999237, -5.0799999237), 0.3175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with Locations((5.0799999237, -5.0799999237)):
                Circle(0.3175)
        # OneSide extrude, distance=-38.1
        extrude(amount=-38.1, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -38.1, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with Locations((5.0799999237, 5.0799999237)):
                Circle(0.3175)
        # OneSide extrude, distance=3.81
        extrude(amount=3.81, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical connector or coupling with a rounded, capsule-like overall shape, featuring a central axial bore, radial flanges on both ends, and a rectangular slot or key passage through its body.
def model_50001_e86a6698_0006():
    """Model: Wheel Screw"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 5.067074791, perimeter: 7.9796453401
            Circle(1.27)
        # OneSide extrude, distance=5.08
        extrude(amount=5.08)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(5.08, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 76.0061218646, perimeter: 39.8982267006
            with BuildLine():
                CenterArc((0, 0), 5.08, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.27, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 5.067074791, perimeter: 7.9796453401
            Circle(1.27)
        # OneSide extrude, distance=5.08
        extrude(amount=5.08, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 13 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(10.16, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.90725625, perimeter: 3.81
            with BuildLine():
                Line((0.47625, 0.47625), (-0.47625, 0.47625))
                Line((-0.47625, 0.47625), (-0.47625, -0.47625))
                Line((-0.47625, -0.47625), (0.47625, -0.47625))
                Line((0.47625, -0.47625), (0.47625, 0.47625))
            make_face()
            # Profile area: 2.570559375, perimeter: 7.3025
            with BuildLine():
                Line((-0.47625, -0.47625), (0.47625, -0.47625))
                Line((-0.47625, -0.47625), (-0.47625, -3.175))
                Line((-0.47625, -3.175), (0.47625, -3.175))
                Line((0.47625, -3.175), (0.47625, -0.47625))
            make_face()
            # Profile area: 2.570559375, perimeter: 7.3025
            with BuildLine():
                Line((0.47625, 3.175), (-0.47625, 3.175))
                Line((-0.47625, 3.175), (-0.47625, 0.47625))
                Line((0.47625, 0.47625), (-0.47625, 0.47625))
                Line((0.47625, 0.47625), (0.47625, 3.175))
            make_face()
            # Profile area: 2.570559375, perimeter: 7.3025
            with BuildLine():
                Line((-0.47625, 0.47625), (-0.47625, -0.47625))
                Line((-0.47625, 0.47625), (-3.175, 0.47625))
                Line((-3.175, 0.47625), (-3.175, -0.47625))
                Line((-3.175, -0.47625), (-0.47625, -0.47625))
            make_face()
            # Profile area: 2.570559375, perimeter: 7.3025
            with BuildLine():
                Line((0.47625, -0.47625), (0.47625, 0.47625))
                Line((0.47625, -0.47625), (3.175, -0.47625))
                Line((3.175, -0.47625), (3.175, 0.47625))
                Line((3.175, 0.47625), (0.47625, 0.47625))
            make_face()
        # OneSide extrude, distance=-2.54
        extrude(amount=-2.54, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical connector or adapter with a tapered end, featuring a knurled grip section and a narrower shaft, designed for tool or equipment assembly.
def model_50019_a59a348f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 6.157521601, perimeter: 8.7964594301
            Circle(1.4)
        # OneSide extrude, distance=6.475
        extrude(amount=6.475)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 6.475), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # OneSide extrude, distance=3.525
        extrude(amount=3.525, mode=Mode.ADD)
    return part.part


# Description: This is a long, flat rectangular plate with a tapered parallelogram shape, featuring a central elongated hole or slot and dark end caps on both sides.
def model_50039_be53f8de_0008():
    """Model: cutting edge"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 75.7989363843, perimeter: 42.7475774979
            with BuildLine():
                CenterArc((75, 0), 1.75, 89.9999634097, 180.0000731806)
                Line((75.0000011176, 1.75), (75.0000011176, 2.6734493849))
                Line((75.0000011176, 2.6734493849), (59.9985564833, 2.6734493849))
                Line((59.9985564833, 2.6734493849), (59.9985564833, -2.7000000402))
                Line((59.9985564833, -2.7000000402), (75.0000011176, -2.7000000402))
                Line((75.0000011176, -2.7000000402), (75.0000011176, -1.75))
            make_face()
            # Profile area: 75.7834188687, perimeter: 42.7417944903
            with BuildLine():
                CenterArc((75, 0), 1.75, -89.9999634097, 179.9999268194)
                Line((75.0000011176, -2.7000000402), (75.0000011176, -1.75))
                Line((89.9985564833, -2.7000000402), (75.0000011176, -2.7000000402))
                Line((89.9985564833, 2.6734493849), (89.9985564833, -2.7000000402))
                Line((75.0000011176, 2.6734493849), (89.9985564833, 2.6734493849))
                Line((75.0000011176, 1.75), (75.0000011176, 2.6734493849))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.7000000402), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 2.0162919795, perimeter: 10.8814598975
            with BuildLine():
                Line((77.5000011548, 0), (77.5000011548, 0.4))
                Line((72.4592712061, 0.4), (77.5000011548, 0.4))
                Line((72.4592712061, 0.4), (72.4592712061, 0))
                Line((77.5000011548, 0), (72.4592712061, 0))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -2.6734493849), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 2.0456203639, perimeter: 11.0281018194
            with BuildLine():
                Line((-72.5000010803, 0), (-72.5000010803, 0.4))
                Line((-72.5000010803, 0.4), (-77.61405199, 0.4))
                Line((-77.61405199, 0.4), (-77.61405199, 0))
                Line((-77.61405199, 0), (-72.5000010803, 0))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)
    return part.part


# Description: This is a tapered cylindrical pin or punch, featuring a gradually decreasing diameter from a thicker rounded end to a sharp point, commonly used as a drift pin, alignment pin, or removal tool.
def model_50039_be53f8de_0009():
    """Model: shaft mill"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            with Locations((45, 0)):
                Circle(1.5)
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 4.9087385212, perimeter: 7.853981634
            with Locations((45, 0)):
                Circle(1.25)
        # OneSide extrude, distance=12
        extrude(amount=12, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 2.552544031, perimeter: 20.4203522483
            with BuildLine():
                CenterArc((-45, 0), 1.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-45, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            with Locations((-45, 0)):
                Circle(1.5)
        # OneSide extrude, distance=30
        extrude(amount=30, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical hollow sleeve or bushing with a vertical slot running along its length and a mesh or perforated pattern on the upper rim, designed for structural support or alignment applications.
def model_50039_be53f8de_0012():
    """Model: windmill"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 15.5803529634, perimeter: 31.9459882446
            with BuildLine():
                CenterArc((-30, 0), 3, 0, 360)
            make_face()
            with BuildLine():
                Line((-27.75, 0.25), (-27.75, -0.25))
                Line((-27.75, -0.25), (-28.0156865167, -0.25))
                CenterArc((-30, 0), 2, 7.1807557815, 345.6384884371)
                Line((-28.0156865167, 0.25), (-27.75, 0.25))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.1267379241, perimeter: 1.5214501481
            with BuildLine():
                CenterArc((-30, 0), 3, 85.2198081528, 9.5603836944)
                Line((-29.75, 3.25), (-29.75, 2.9895651858))
                Line((-30.25, 3.25), (-29.75, 3.25))
                Line((-30.25, 2.9895651858), (-30.25, 3.25))
            make_face()
        # OneSide extrude, distance=-5
        extrude(amount=-5, mode=Mode.ADD)
    return part.part


# Description: This is a thin, flat parallelogram-shaped plate or panel with a slightly beveled edge on one side and subtle surface details suggesting it may be a cover, lid, or structural component.
def model_50222_55cff75a_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch3 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 72, perimeter: 39.6
            with BuildLine():
                Line((0, 4.8), (0, 0))
                Line((0, 0), (15, 0))
                Line((15, 0), (15, 4.8))
                Line((15, 4.8), (0, 4.8))
            make_face()
        # OneSide extrude, distance=0.35
        extrude(amount=0.35)

        # Sketch4 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.35, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 66.15, perimeter: 38.4
            with BuildLine():
                Line((-0.15, -0.15), (-14.85, -0.15))
                Line((-14.85, -0.15), (-14.85, -4.65))
                Line((-14.85, -4.65), (-0.15, -4.65))
                Line((-0.15, -4.65), (-0.15, -0.15))
            make_face()
        # OneSide extrude, distance=0.15
        extrude(amount=0.15, mode=Mode.ADD)
    return part.part


# Description: This is a flat rectangular panel or cover plate with rounded corners, four corner mounting holes, and a slight parallelogram shape, likely designed as an access cover or mounting bracket component.
def model_50409_4a322fbf_0009():
    """Model: Component24"""
    with BuildPart() as part:
        # board_outline -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 12.0091109916, perimeter: 13.787929068
            with BuildLine():
                CenterArc((4.064, 0.254), 0.254, -90, 90)
                Line((4.318, 2.54), (4.318, 0.254))
                CenterArc((4.064, 2.54), 0.254, 0, 90)
                Line((0.254, 2.794), (4.064, 2.794))
                CenterArc((0.254, 2.54), 0.254, 90, 90)
                Line((0, 0.254), (0, 2.54))
                CenterArc((0.254, 0.254), 0.254, 180, 90)
                Line((4.064, 0), (0.254, 0))
            make_face()
        # OneSide extrude, distance=0.16
        extrude(amount=0.16)

        # Drills - pads -> Extrude2 (Cut)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((0.635, 0.127)):
                Circle(0.05)
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((0.254, 0.889)):
                Circle(0.05)
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((0.254, 0.635)):
                Circle(0.05)
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((0.254, 1.143)):
                Circle(0.05)
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((0.635, 2.667)):
                Circle(0.05)
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((0.254, 1.397)):
                Circle(0.05)
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((0.889, 2.667)):
                Circle(0.05)
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((0.254, 1.651)):
                Circle(0.05)
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((1.143, 2.667)):
                Circle(0.05)
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((0.254, 1.905)):
                Circle(0.05)
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((1.397, 2.667)):
                Circle(0.05)
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((0.254, 2.159)):
                Circle(0.05)
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((1.651, 2.667)):
                Circle(0.05)
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            with Locations((0.254, 2.54)):
                Circle(0.125)
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((1.905, 2.667)):
                Circle(0.05)
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((3.683, 0.127)):
                Circle(0.05)
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((2.159, 2.667)):
                Circle(0.05)
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((3.429, 0.127)):
                Circle(0.05)
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((2.413, 2.667)):
                Circle(0.05)
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((3.175, 0.127)):
                Circle(0.05)
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((2.667, 2.667)):
                Circle(0.05)
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((2.921, 0.127)):
                Circle(0.05)
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((2.921, 2.667)):
                Circle(0.05)
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((2.667, 0.127)):
                Circle(0.05)
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((3.175, 2.667)):
                Circle(0.05)
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((2.413, 0.127)):
                Circle(0.05)
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((3.429, 2.667)):
                Circle(0.05)
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((2.159, 0.127)):
                Circle(0.05)
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((3.683, 2.667)):
                Circle(0.05)
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((1.905, 0.127)):
                Circle(0.05)
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            with Locations((0.254, 0.254)):
                Circle(0.125)
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((1.651, 0.127)):
                Circle(0.05)
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            with Locations((4.064, 2.54)):
                Circle(0.125)
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((1.397, 0.127)):
                Circle(0.05)
            # Profile area: 0.0051886846, perimeter: 0.2553486509
            with Locations((3.9751, 1.4097)):
                Circle(0.04064)
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((1.143, 0.127)):
                Circle(0.05)
            # Profile area: 0.0051886846, perimeter: 0.2553486509
            with Locations((2.9591, 1.4097)):
                Circle(0.04064)
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((0.889, 0.127)):
                Circle(0.05)
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            with Locations((4.064, 0.254)):
                Circle(0.125)
        # OneSide extrude, distance=0.16
        extrude(amount=0.16, mode=Mode.SUBTRACT)

        # Drills - vias -> Extrude3 (Cut)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0019634954, perimeter: 0.1570796327
            with Locations((2.3876, 0.9144)):
                Circle(0.025)
            # Profile area: 0.0019634954, perimeter: 0.1570796327
            with Locations((2.9718, 0.9144)):
                Circle(0.025)
            # Profile area: 0.0019634954, perimeter: 0.1570796327
            with Locations((2.921, 0.508)):
                Circle(0.025)
            # Profile area: 0.0019634954, perimeter: 0.1570796327
            with Locations((3.2893, 0.2794)):
                Circle(0.025)
            # Profile area: 0.0019634954, perimeter: 0.1570796327
            with Locations((1.0414, 1.6256)):
                Circle(0.025)
            # Profile area: 0.0019634954, perimeter: 0.1570796327
            with Locations((3.7592, 1.27)):
                Circle(0.025)
            # Profile area: 0.0019634954, perimeter: 0.1570796327
            with Locations((1.016, 1.4351)):
                Circle(0.025)
            # Profile area: 0.0019634954, perimeter: 0.1570796327
            with Locations((1.778, 1.7018)):
                Circle(0.025)
            # Profile area: 0.0019634954, perimeter: 0.1570796327
            with Locations((0.8509, 1.6383)):
                Circle(0.025)
            # Profile area: 0.0019634954, perimeter: 0.1570796327
            with Locations((0.6858, 1.5494)):
                Circle(0.025)
            # Profile area: 0.0019634954, perimeter: 0.1570796327
            with Locations((1.3716, 1.6764)):
                Circle(0.025)
            # Profile area: 0.0019634954, perimeter: 0.1570796327
            with Locations((2.7178, 0.7366)):
                Circle(0.025)
            # Profile area: 0.0019634954, perimeter: 0.1570796327
            with Locations((1.1176, 0.9652)):
                Circle(0.025)
            # Profile area: 0.0019634954, perimeter: 0.1570796327
            with Locations((3.556, 0.6604)):
                Circle(0.025)
            # Profile area: 0.0019634954, perimeter: 0.1570796327
            with Locations((2.0574, 1.7653)):
                Circle(0.025)
            # Profile area: 0.0019634954, perimeter: 0.1570796327
            with Locations((3.1496, 0.6604)):
                Circle(0.025)
            # Profile area: 0.0019634954, perimeter: 0.1570796327
            with Locations((2.0955, 1.905)):
                Circle(0.025)
            # Profile area: 0.0019634954, perimeter: 0.1570796327
            with Locations((0.9398, 2.1209)):
                Circle(0.025)
            # Profile area: 0.0019634954, perimeter: 0.1570796327
            with Locations((2.2098, 1.9431)):
                Circle(0.025)
            # Profile area: 0.0019634954, perimeter: 0.1570796327
            with Locations((1.5494, 2.1336)):
                Circle(0.025)
            # Profile area: 0.0019634954, perimeter: 0.1570796327
            with Locations((2.3114, 2.032)):
                Circle(0.025)
            # Profile area: 0.0019634954, perimeter: 0.1570796327
            with Locations((2.159, 1.397)):
                Circle(0.025)
            # Profile area: 0.0019634954, perimeter: 0.1570796327
            with Locations((2.4257, 2.1336)):
                Circle(0.025)
            # Profile area: 0.0019634954, perimeter: 0.1570796327
            with Locations((1.27, 1.4351)):
                Circle(0.025)
            # Profile area: 0.0019634954, perimeter: 0.1570796327
            with Locations((2.54, 2.1971)):
                Circle(0.025)
            # Profile area: 0.0019634954, perimeter: 0.1570796327
            with Locations((0.8382, 0.7874)):
                Circle(0.025)
            # Profile area: 0.0019634954, perimeter: 0.1570796327
            with Locations((2.3114, 2.2225)):
                Circle(0.025)
            # Profile area: 0.0019634954, perimeter: 0.1570796327
            with Locations((3.3528, 1.2573)):
                Circle(0.025)
            # Profile area: 0.0019634954, perimeter: 0.1570796327
            with Locations((2.159, 2.2225)):
                Circle(0.025)
        # OneSide extrude, distance=0.16
        extrude(amount=0.16, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a molded polymer enclosure or chassis with a rectangular base, rounded corners, ventilation slots along the sides, mounting holes distributed across the surface, and integrated flanges or bosses at the top corners for component attachment.
def model_50715_fcc44f87_0002():
    """Model: pcb"""
    with BuildPart() as part:
        # board_outline -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 1.7188089916, perimeter: 4.897929068
            with BuildLine():
                CenterArc((0.254, 1.143), 0.254, 90, 90)
                Line((0, 0.254), (0, 1.143))
                CenterArc((0.254, 0.254), 0.254, 180, 90)
                Line((1.016, 0), (0.254, 0))
                CenterArc((1.016, 0.254), 0.254, -90, 90)
                Line((1.27, 1.143), (1.27, 0.254))
                CenterArc((1.016, 1.143), 0.254, 0, 90)
                Line((0.254, 1.397), (1.016, 1.397))
            make_face()
        # OneSide extrude, distance=0.16
        extrude(amount=0.16)

        # Drills - pads -> Extrude2 (Cut)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            with Locations((0.254, 1.143)):
                Circle(0.125)
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((0.381, 0.254)):
                Circle(0.05)
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((0.635, 0.254)):
                Circle(0.05)
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((0.127, 0.254)):
                Circle(0.05)
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((0.889, 0.254)):
                Circle(0.05)
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            with Locations((1.016, 1.143)):
                Circle(0.125)
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((1.143, 0.254)):
                Circle(0.05)
        # OneSide extrude, distance=0.16
        extrude(amount=0.16, mode=Mode.SUBTRACT)

        # Drills - vias -> Extrude3 (Cut)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0019634954, perimeter: 0.1570796327
            with Locations((0.4826, 0.508)):
                Circle(0.025)
            # Profile area: 0.0019634954, perimeter: 0.1570796327
            with Locations((0.5334, 1.1176)):
                Circle(0.025)
            # Profile area: 0.0019634954, perimeter: 0.1570796327
            with Locations((1.1938, 0.9398)):
                Circle(0.025)
            # Profile area: 0.0019634954, perimeter: 0.1570796327
            with Locations((0.7366, 1.1176)):
                Circle(0.025)
            # Profile area: 0.0019634954, perimeter: 0.1570796327
            with Locations((0.635, 0.8128)):
                Circle(0.025)
        # OneSide extrude, distance=0.16
        extrude(amount=0.16, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a boomerang-shaped connector or bracket featuring two symmetrical curved arms with textured/ribbed surfaces, connected at the top by a flat bridge section, designed to grip or hold objects between its dual prongs.
def model_50777_2934de55_0021():
    """Model: Buckle Holder v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 11 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1002168056, perimeter: 1.8221237391
            with BuildLine():
                CenterArc((0, 0), 0.2, 103.2217880762, 183.9677276069)
                CenterArc((0, 0), 0.2, -72.8104843169, 176.0322723931)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.09, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.4833292293, perimeter: 4.1656568019
            with BuildLine():
                Line((1.6627985588, 0.1708412828), (1.168912344, 0.1180537011))
                CenterArc((1.6574847211, 0.2205581122), 0.05, -83.8992691826, 154.8862912211)
                Line((1.5412812388, 0.313484784), (1.6737738367, 0.2678303526))
                CenterArc((0.954873074, -1.3883158695), 1.8, 70.9870220385, 35.2879699361)
                Line((-0.045744216, 0.1946983993), (0.4504271173, 0.3395539974))
                CenterArc((0, 0), 0.2, -72.8104843169, 176.0322723931)
                Line((0.8377134893, 0.0497964699), (0.0591066485, -0.1910664913))
                CenterArc((1.354896664, -1.622035329), 1.75, 96.1007308174, 11.0887848657)
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 2.7200000811, perimeter: 6.6000000983
            with BuildLine():
                Line((0.1500000022, 1.3500000201), (0.1500000022, -0.2500000037))
                Line((0.1500000022, -0.2500000037), (1.8500000276, -0.2500000037))
                Line((1.8500000276, -0.2500000037), (1.8500000276, 1.3500000201))
                Line((1.8500000276, 1.3500000201), (0.1500000022, 1.3500000201))
            make_face()
        # TwoSides extrude, along=1.2, against=-1.3
        extrude(amount=1.2, mode=Mode.SUBTRACT)
        extrude(sk.sketch, amount=-1.3, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on XY construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0172955777, perimeter: 0.5728578339
            with BuildLine():
                Line((0.9000000134, 0.313484784), (1.0999137084, 0.313484784))
                Line((1.0999137084, 0.400000006), (1.0999137084, 0.313484784))
                Line((0.9000000134, 0.400000006), (1.0999137084, 0.400000006))
                Line((0.9000000134, 0.313484784), (0.9000000134, 0.400000006))
            make_face()
        # OneSide extrude, distance=-2.05
        extrude(amount=-2.05, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a multi-blade impeller or rotor with a central hub featuring 6 radial blades arranged symmetrically around the axis, each blade displaying a curved, fin-like profile with textured surfaces for fluid dynamics applications.
def model_50897_3be92e2f_0016():
    """Model: Front Spokes v5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude7 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 25 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 236.4634902455, perimeter: 69.4191724603
            with BuildLine():
                CenterArc((0, 0), 5.08, 120, 30)
                Line((-2.54, 4.3994090512), (-15.24, 26.3964543073))
                CenterArc((0, 0), 30.48, 120, 30)
                Line((-4.3994090512, 2.54), (-26.3964543073, 15.24))
            make_face()
            # Profile area: 236.4634902455, perimeter: 69.4191724603
            with BuildLine():
                CenterArc((0, 0), 30.48, 180, 30)
                Line((-4.3994090512, -2.54), (-26.3964543073, -15.24))
                CenterArc((0, 0), 5.08, -180, 30)
                Line((-5.08, 0), (-30.48, 0))
            make_face()
            # Profile area: 236.4634902455, perimeter: 69.4191724603
            with BuildLine():
                CenterArc((0, 0), 5.08, -120, 30)
                Line((-2.54, -4.3994090512), (-15.24, -26.3964543073))
                CenterArc((0, 0), 30.48, -120, 30)
                Line((0, -5.08), (0, -30.48))
            make_face()
            # Profile area: 69.6722783759, perimeter: 43.8880493706
            with BuildLine():
                CenterArc((0, 0), 5.08, -180, 30)
                CenterArc((0, 0), 5.08, -150, 30)
                CenterArc((0, 0), 5.08, -120, 30)
                CenterArc((0, 0), 5.08, -90, 30)
                CenterArc((0, 0), 5.08, -60, 30)
                CenterArc((0, 0), 5.08, -30, 30)
                CenterArc((0, 0), 5.08, 0, 30)
                CenterArc((0, 0), 5.08, 30, 30)
                CenterArc((0, 0), 5.08, 60, 30)
                CenterArc((0, 0), 5.08, 90, 30)
                CenterArc((0, 0), 5.08, 120, 30)
                CenterArc((0, 0), 5.08, 150, 30)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.905, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 236.4634902455, perimeter: 69.4191724603
            with BuildLine():
                CenterArc((0, 0), 5.08, -60, 30)
                Line((2.54, -4.3994090512), (15.24, -26.3964543073))
                CenterArc((0, 0), 30.48, -60, 30)
                Line((4.3994090512, -2.54), (26.3964543073, -15.24))
            make_face()
            # Profile area: 236.4634902455, perimeter: 69.4191724603
            with BuildLine():
                CenterArc((0, 0), 5.08, 60, 30)
                Line((2.54, 4.3994090512), (15.24, 26.3964543073))
                CenterArc((0, 0), 30.48, 60, 30)
                Line((0, 5.08), (0, 30.48))
            make_face()
            # Profile area: 236.4634902455, perimeter: 69.4191724603
            with BuildLine():
                CenterArc((0, 0), 5.08, 0, 30)
                Line((5.08, 0), (30.48, 0))
                CenterArc((0, 0), 30.48, 0, 30)
                Line((4.3994090512, 2.54), (26.3964543073, 15.24))
            make_face()
        # OneSide extrude, distance=3.81
        extrude(amount=3.81)

        # Sketch7 -> Extrude8 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3.81, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 34.2027548391, perimeter: 35.9084040305
            with BuildLine():
                CenterArc((0, 0), 3.81, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.905, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.27
        extrude(amount=1.27, mode=Mode.ADD)

        # Sketch8 -> Extrude9 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 34.2027548391, perimeter: 35.9084040305
            with BuildLine():
                CenterArc((0, 0), 3.81, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.905, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.27
        extrude(amount=1.27, mode=Mode.ADD)
    return part.part


# Description: This is a bracket or mounting assembly featuring a triangular/pyramidal main body with two circular mounting holes, internal webbing/bracing for structural support, and angled flanges that extend outward for attachment purposes.
def model_50914_57d3d851_0002():
    """Model: fixturepart1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 15, perimeter: 17.4031242374
            with BuildLine():
                Line((0, 0), (0, 5))
                Line((-5, 1), (0, 5))
                Line((-5, 0), (-5, 1))
                Line((0, 0), (-5, 0))
            make_face()
        # Symmetric extrude, each_side=1
        extrude(amount=1, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 12 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 15, perimeter: 17.4031242374
            with BuildLine():
                Line((0, 5), (-5, 1))
                Line((-5, 1), (-5, 0))
                Line((0, 0), (-5, 0))
                Line((0, 0), (0, 5))
            make_face()
            # Profile area: 23.7739333694, perimeter: 30.7161355982
            with BuildLine():
                CenterArc((-1.2, 6), 1.2, 0, 124.9920201986)
                Line((-6.8881548132, 3.4830783046), (-1.8881548132, 6.9830783046))
                CenterArc((-6.2, 2.5), 1.2, 124.9920201986, 55.0079798014)
                Line((-7.4, 0), (-7.4, 2.5))
                Line((-5, 0), (-7.4, 0))
                Line((-5, 1), (-5, 0))
                Line((0, 5), (-5, 1))
                Line((0, 5), (0, 6))
            make_face()
            with BuildLine():
                CenterArc((-6.2, 2.5), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.2, 6), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 26.7164270662, perimeter: 29.7955742876
            with BuildLine():
                Line((4, -7.4), (1, -7.4))
                CenterArc((4, -6.4), 1, -90, 90)
                Line((5, -1), (5, -6.4))
                CenterArc((4, -1), 1, 0, 90)
                Line((1, 0), (4, 0))
                Line((1, -7.4), (1, 0))
            make_face()
            with BuildLine():
                CenterArc((3.5, -5.2), 0.625, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.5, -2.2), 0.625, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


# Description: This is a hexagonal coffin/casket with a hinged or split lid design, featuring a tapered rectangular body with angled side panels and a dark finish with blue-tinted interior lining.
def model_50947_49287c16_0000():
    """Model: USB Socket"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 11.4348205389, perimeter: 14.661897765
            with BuildLine():
                Line((-2.5399999619, 2.5399999619), (-2.5399999619, 0.2890510031))
                Line((-2.5399999619, 0.2890510031), (2.5399999619, 0.2890510031))
                Line((2.5399999619, 0.2890510031), (2.5399999619, 2.5399999619))
                Line((2.5399999619, 2.5399999619), (-2.5399999619, 2.5399999619))
            make_face()
        # OneSide extrude, distance=13.97
        extrude(amount=13.97)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 14 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 13.97), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.9677399376, perimeter: 5.8419999874
            with BuildLine():
                Line((1.2699999809, 1.5240000486), (1.2699999809, 1.9049999809))
                Line((1.2699999809, 1.9049999809), (-1.2700000405, 1.9050000608))
                Line((-1.2700000405, 1.5240000486), (-1.2700000405, 1.9050000608))
                Line((1.2699999809, 1.5240000486), (-1.2700000405, 1.5240000486))
            make_face()
            # Profile area: 0.9677401518, perimeter: 5.8420002067
            with BuildLine():
                Line((1.2699999809, 1.9049999809), (-1.2700000405, 1.9050000608))
                Line((1.2700000405, 2.286000073), (1.2699999809, 1.9049999809))
                Line((-1.2700000405, 2.286000073), (1.2700000405, 2.286000073))
                Line((-1.2700000405, 1.9050000608), (-1.2700000405, 2.286000073))
            make_face()
            # Profile area: 0.9677399634, perimeter: 5.8420000076
            with BuildLine():
                Line((1.2699999809, 1.2699999809), (-1.2700000405, 1.2699999809))
                Line((-1.2700000405, 1.2699999809), (-1.2700000405, 0.8889999986))
                Line((-1.2700000405, 0.8889999986), (1.2699999809, 0.8889999986))
                Line((1.2699999809, 0.8889999986), (1.2699999809, 1.2699999809))
            make_face()
            # Profile area: 0.9677399634, perimeter: 5.8420000076
            with BuildLine():
                Line((-1.2700000405, 0.8889999986), (1.2699999809, 0.8889999986))
                Line((-1.2700000405, 0.8889999986), (-1.2700000405, 0.5080000162))
                Line((-1.2700000405, 0.5080000162), (1.2699999809, 0.5080000162))
                Line((1.2699999809, 0.5080000162), (1.2699999809, 0.8889999986))
            make_face()
        # OneSide extrude, distance=-0.254
        extrude(amount=-0.254, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 13.97), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.9677399376, perimeter: 5.8419999874
            with BuildLine():
                Line((-1.2700000405, 1.5240000486), (-1.2700000405, 1.9050000608))
                Line((1.2699999809, 1.5240000486), (-1.2700000405, 1.5240000486))
                Line((1.2699999809, 1.9049999809), (1.2699999809, 1.5240000486))
                Line((1.2699999809, 1.9049999809), (-1.2700000405, 1.9050000608))
            make_face()
            # Profile area: 0.9677399634, perimeter: 5.8420000076
            with BuildLine():
                Line((-1.2700000405, 0.5080000162), (-1.2700000405, 0.8889999986))
                Line((1.2699999809, 0.5080000162), (-1.2700000405, 0.5080000162))
                Line((1.2699999809, 0.8889999986), (1.2699999809, 0.5080000162))
                Line((1.2699999809, 0.8889999986), (-1.2700000405, 0.8889999986))
            make_face()
        # OneSide extrude, distance=-1.524
        extrude(amount=-1.524, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical foam roller or exercise tube with a slightly tapered end and textured surface, featuring a hollow core and subtle branding or text on the top end.
def model_51022_47816098_0005():
    """Model: hand-left"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            Circle(2)
        # OneSide extrude, distance=15
        extrude(amount=15)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 15, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            Circle(1.5)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 2.5446900494, perimeter: 5.6548667765
            Circle(0.9)
        # OneSide extrude, distance=-12
        extrude(amount=-12, mode=Mode.SUBTRACT)
    return part.part


# Description: A dual-wing airfoil structure with curved, symmetrical wings extending from a central horizontal bar, featuring textured mesh surfaces and dark cylindrical base pods.
def model_51336_33ff2eba_0005():
    """Model: Buckle v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 13 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.6208544115, perimeter: 4.440160466
            with BuildLine():
                Line((1.6038524371, 0.2461869442), (1.0258138204, 0.1261309562))
                CenterArc((1.5936846552, 0.2951421912), 0.05, -78.2667434961, 145.2265297482)
                Line((1.25271098, 0.4944936696), (1.6132535102, 0.3411537106))
                CenterArc((0.8417650252, -0.4717482371), 1.05, 66.9597862522, 44.7820439069)
                Line((-0.1111274999, 0.2786587186), (0.4528187813, 0.5035572634))
                CenterArc((0, 0), 0.3000000045, -64.3124382932, 176.0542684522)
                Line((0.7842006057, 0.0443004683), (0.13003904, -0.2703513469))
                CenterArc((1.2393372391, -0.9019292316), 1.05, 101.7332565039, 13.9543052029)
            make_face()
            # Profile area: 0.2513274207, perimeter: 2.513274151
            with BuildLine():
                CenterArc((0, 0), 0.3000000045, 111.7418301591, 183.9457315478)
                CenterArc((0, 0), 0.3000000045, -64.3124382932, 176.0542684522)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 3.715970279, perimeter: 7.8918507585
            with BuildLine():
                Line((0.3000000045, 1.25271098), (0.3000000045, -0.3000000045))
                Line((0.3000000045, -0.3000000045), (2.6932143992, -0.3000000045))
                Line((2.6932143992, -0.3000000045), (2.6932143992, 1.25271098))
                Line((0.3000000045, 1.25271098), (2.6932143992, 1.25271098))
            make_face()
        # TwoSides extrude, along=3, against=-2.2
        extrude(amount=3, mode=Mode.SUBTRACT)
        extrude(sk.sketch, amount=-2.2, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on XY construction plane
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0420203333, perimeter: 0.84236661
            with BuildLine():
                Line((1.5, 0.6000000089), (1.6623370066, 0.6000000089))
                Line((1.5, 0.3411537106), (1.5, 0.6000000089))
                Line((1.6623370066, 0.3411537106), (1.5, 0.3411537106))
                Line((1.6623370066, 0.6000000089), (1.6623370066, 0.3411537106))
            make_face()
            # Profile area: 0.0388269395, perimeter: 0.8176925565
            with BuildLine():
                Line((1.3500000201, 0.6000000089), (1.5, 0.6000000089))
                Line((1.3500000201, 0.3411537106), (1.3500000201, 0.6000000089))
                Line((1.3500000201, 0.3411537106), (1.5, 0.3411537106))
                Line((1.5, 0.3411537106), (1.5, 0.6000000089))
            make_face()
        # OneSide extrude, distance=-2.95
        extrude(amount=-2.95, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a rectangular mounting bracket or rail component with a horizontal elongated body, featuring a vertical flanged end on the left side and internal slot channels running along its length for securing or guiding other components.
def model_51345_4b292361_0005():
    """Model: Core v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude4 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 38.5, perimeter: 29
            with BuildLine():
                Line((0, 3.5), (0, 0))
                Line((0, 0), (11, 0))
                Line((11, 0), (11, 3.5))
                Line((11, 3.5), (0, 3.5))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch5 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 14 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.225, perimeter: 3.3
            with BuildLine():
                Line((1, 1.825), (0.25, 1.825))
                Line((0.25, 1.825), (0.25, 1.675))
                Line((0.25, 1.675), (1, 1.675))
                Line((1, 1.675), (1.75, 1.675))
                Line((1.75, 1.675), (1.75, 1.825))
                Line((1.75, 1.825), (1, 1.825))
            make_face()
        # OneSide extrude, distance=-8
        extrude(amount=-8, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude8 (Cut)
        # Sketch on BRepFace
        # Sketch has 26 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(11, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.05, perimeter: 4.4
            with BuildLine():
                Line((-1.3, 2), (-2, 2))
                Line((-1.3, 3.5), (-1.3, 2))
                Line((-2, 3.5), (-1.3, 3.5))
                Line((-2, 2), (-2, 3.5))
            make_face()
            # Profile area: 1.05, perimeter: 4.4
            with BuildLine():
                Line((0, 2), (0, 3.5))
                Line((0, 3.5), (-0.7, 3.5))
                Line((-0.7, 3.5), (-0.7, 2))
                Line((-0.7, 2), (0, 2))
            make_face()
            # Profile area: 1.05, perimeter: 4.4
            with BuildLine():
                Line((-0.7, 1.5), (0, 1.5))
                Line((-0.7, 0), (-0.7, 1.5))
                Line((0, 0), (-0.7, 0))
                Line((0, 1.5), (0, 0))
            make_face()
            # Profile area: 1.05, perimeter: 4.4
            with BuildLine():
                Line((-2, 1.5), (-2, 0))
                Line((-2, 0), (-1.3, 0))
                Line((-1.3, 0), (-1.3, 1.5))
                Line((-1.3, 1.5), (-2, 1.5))
            make_face()
        # OneSide extrude, distance=-10
        extrude(amount=-10, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical sleeve or bushing with a slightly tapered, curved profile and a open top featuring a recessed or flanged rim.
def model_51464_da501c24_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
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
        # Sketch on BRepFace
        # Sketch has 11 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 25.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 119.1603509622, perimeter: 75.3586253804
            with BuildLine():
                Line((-7.9261832011, 0), (-7.9261832011, 2.2233697544))
                Line((-7.9261832011, 2.2233697544), (-15.8432251839, -2.1901188845))
                Line((-15.8432251839, -2.1901188845), (-15.8432251839, 2.1989700597))
                Line((-15.8432251839, 2.1989700597), (-24.0146737086, -2.3563417985))
                CenterArc((0, 0), 24.13, -174.3960241422, 16.2565415059)
                Line((-15.4266910795, -5.1002273885), (-22.3948855428, -8.9847649676))
                Line((-15.4266910795, -7.0865425152), (-15.4266910795, -5.1002273885))
                Line((-7.8573956227, -2.8669110449), (-15.4266910795, -7.0865425152))
                Line((-7.8573956227, -4.380237769), (-7.8573956227, -2.8669110449))
                Line((0, 0), (-7.8573956227, -4.380237769))
                Line((0.08946209, 4.1152561417), (0, 0))
                Line((-2.6391316561, 0), (0.08946209, 4.1152561417))
                Line((-7.9261832011, 0), (-2.6391316561, 0))
            make_face()
        # OneSide extrude, distance=-5.08
        extrude(amount=-5.08)
    return part.part


# Description: This is an oval/elliptical plate or bracket with a textured dark surface featuring two elongated rectangular slots or cutouts along its center axis and a light blue accent strip running through the middle.
def model_51536_a18dc325_0000():
    """Model: Watch Face v6"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            Circle(2.5)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.5393804461, perimeter: 4.3982297806
            with Locations((0, 1.5000000224)):
                Circle(0.7000000104)
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981868, perimeter: 3.1415927004
            with Locations((-1.5000000224, 0)):
                Circle(0.5000000075)
        # OneSide extrude, distance=-1.1
        extrude(amount=-1.1, mode=Mode.SUBTRACT)
    return part.part


MODELS = {
    "model_43540_0f53629d_0000": {"func": model_43540_0f53629d_0000, "volume": 4.012299309, "area": 18.0008975133},
    "model_43540_0f53629d_0001": {"func": model_43540_0f53629d_0001, "volume": 73.9089417312, "area": 230.8353714157},
    "model_43562_004c6cea_0013": {"func": model_43562_004c6cea_0013, "volume": 33.3892261769, "area": 91.6217493524},
    "model_43866_908e0b9a_0015": {"func": model_43866_908e0b9a_0015, "volume": 2.9410367487, "area": 55.25392678},
    "model_43866_908e0b9a_0018": {"func": model_43866_908e0b9a_0018, "volume": 0.1884955592, "area": 2.8902652413},
    "model_43928_6ca53538_0010": {"func": model_43928_6ca53538_0010, "volume": 0.2120516013, "area": 2.3837303253},
    "model_43928_6ca53538_0012": {"func": model_43928_6ca53538_0012, "volume": 0.0712202196, "area": 1.1476237964},
    "model_43928_6ca53538_0021": {"func": model_43928_6ca53538_0021, "volume": 0.7376209872, "area": 13.1063337067},
    "model_43928_6ca53538_0022": {"func": model_43928_6ca53538_0022, "volume": 0.7201089851, "area": 11.3774447094},
    "model_43931_bb001c04_0013": {"func": model_43931_bb001c04_0013, "volume": 951275.5100008539, "area": 152524.1914225921},
    "model_43932_4bfdfe7b_0000": {"func": model_43932_4bfdfe7b_0000, "volume": 8.870254956, "area": 35.7086018882},
    "model_43932_4bfdfe7b_0001": {"func": model_43932_4bfdfe7b_0001, "volume": 60.0989416177, "area": 158.1973612796},
    "model_43932_4bfdfe7b_0002": {"func": model_43932_4bfdfe7b_0002, "volume": 24.8463697804, "area": 59.6694578428},
    "model_43932_4bfdfe7b_0003": {"func": model_43932_4bfdfe7b_0003, "volume": 32.9801125326, "area": 74.3092796085},
    "model_43932_4bfdfe7b_0004": {"func": model_43932_4bfdfe7b_0004, "volume": 1365.0341226539, "area": 2080.3998825747},
    "model_43932_4bfdfe7b_0005": {"func": model_43932_4bfdfe7b_0005, "volume": 12.7611493589, "area": 71.0628258242},
    "model_43933_3b763a09_0004": {"func": model_43933_3b763a09_0004, "volume": 2.0139804321, "area": 12.1123780936},
    "model_43933_3b763a09_0005": {"func": model_43933_3b763a09_0005, "volume": 1.6471719887, "area": 11.7548365585},
    "model_43934_912ff891_0003": {"func": model_43934_912ff891_0003, "volume": 737.3234496442, "area": 973.9176938064},
    "model_43934_912ff891_0011": {"func": model_43934_912ff891_0011, "volume": 0.4728473439, "area": 6.2056484277},
    "model_43934_912ff891_0014": {"func": model_43934_912ff891_0014, "volume": 5.4563407555, "area": 29.8986434335},
    "model_43934_912ff891_0020": {"func": model_43934_912ff891_0020, "volume": 4.5521677551, "area": 29.4367231641},
    "model_43938_418421a7_0000": {"func": model_43938_418421a7_0000, "volume": 21.3646210931, "area": 135.2929237489},
    "model_43938_418421a7_0002": {"func": model_43938_418421a7_0002, "volume": 17.4781246876, "area": 99.394604075},
    "model_44021_f141414b_0003": {"func": model_44021_f141414b_0003, "volume": 68.3374941972, "area": 144.8431292938},
    "model_44206_ff45fbf0_0010": {"func": model_44206_ff45fbf0_0010, "volume": 0.0000560578, "area": 0.0109563044},
    "model_44206_ff45fbf0_0014": {"func": model_44206_ff45fbf0_0014, "volume": 0.0000437859, "area": 0.008992809},
    "model_44528_3cff1325_0000": {"func": model_44528_3cff1325_0000, "volume": 117.8097245096, "area": 204.2035224833},
    "model_44553_9af8a2cb_0000": {"func": model_44553_9af8a2cb_0000, "volume": 104.5, "area": 249.8284271247},
    "model_45007_990d2758_0001": {"func": model_45007_990d2758_0001, "volume": 0.685223393, "area": 5.5477871438},
    "model_45285_dc1f2b6f_0002": {"func": model_45285_dc1f2b6f_0002, "volume": 1525.6359323995, "area": 872.9229641421},
    "model_45285_dc1f2b6f_0005": {"func": model_45285_dc1f2b6f_0005, "volume": 149.3001859872, "area": 237.2638722768},
    "model_45303_48d14b32_0016": {"func": model_45303_48d14b32_0016, "volume": 470.9487614034, "area": 1473.9706192983},
    "model_45359_1768ab3f_0010": {"func": model_45359_1768ab3f_0010, "volume": 0.1889065694, "area": 2.4317326903},
    "model_45359_1768ab3f_0023": {"func": model_45359_1768ab3f_0023, "volume": 0.1094059642, "area": 1.4765485472},
    "model_45359_1768ab3f_0025": {"func": model_45359_1768ab3f_0025, "volume": 0.239170886, "area": 2.9343875148},
    "model_45359_1768ab3f_0038": {"func": model_45359_1768ab3f_0038, "volume": 85.803440811, "area": 181.2752933747},
    "model_45359_1768ab3f_0043": {"func": model_45359_1768ab3f_0043, "volume": 0.1475143766, "area": 3.0815520911},
    "model_45360_cb4bac3f_0001": {"func": model_45360_cb4bac3f_0001, "volume": 4.7488147246, "area": 21.7665401906},
    "model_45360_cb4bac3f_0024": {"func": model_45360_cb4bac3f_0024, "volume": 3.688527204, "area": 17.5253901083},
    "model_45360_cb4bac3f_0025": {"func": model_45360_cb4bac3f_0025, "volume": 3.4253483347, "area": 18.5075030144},
    "model_45428_13340c06_0000": {"func": model_45428_13340c06_0000, "volume": 5193.1627615353, "area": 8568.1976266007},
    "model_45431_cb452deb_0000": {"func": model_45431_cb452deb_0000, "volume": 9173.6600717899, "area": 10458.8457764377},
    "model_45432_67aa4de8_0000": {"func": model_45432_67aa4de8_0000, "volume": 5042.0658560279, "area": 4859.460908624},
    "model_45433_80a435ab_0000": {"func": model_45433_80a435ab_0000, "volume": 5517.4774240823, "area": 9098.1962638609},
    "model_45437_a98a4f45_0000": {"func": model_45437_a98a4f45_0000, "volume": 3868.7457279123, "area": 9624.7570921131},
    "model_45468_eaf0dc99_0004": {"func": model_45468_eaf0dc99_0004, "volume": 0.9793878538, "area": 7.5672930248},
    "model_45798_b573e9da_0005": {"func": model_45798_b573e9da_0005, "volume": 100.2288931435, "area": 169.7295351095},
    "model_45798_b573e9da_0012": {"func": model_45798_b573e9da_0012, "volume": 1.3000748098, "area": 13.290219597},
    "model_45922_26941172_0007": {"func": model_45922_26941172_0007, "volume": 92.6777686791, "area": 419.7481944461},
    "model_45922_26941172_0010": {"func": model_45922_26941172_0010, "volume": 57.9177821791, "area": 156.963755365},
    "model_45922_26941172_0015": {"func": model_45922_26941172_0015, "volume": 5.5667664801, "area": 27.9947841855},
    "model_46086_371b5052_0002": {"func": model_46086_371b5052_0002, "volume": 0.4116921934, "area": 6.8885816457},
    "model_46086_371b5052_0007": {"func": model_46086_371b5052_0007, "volume": 0.4351050991, "area": 7.6047549613},
    "model_46086_371b5052_0012": {"func": model_46086_371b5052_0012, "volume": 0.333488467, "area": 5.7933730167},
    "model_48332_fb679f90_0003": {"func": model_48332_fb679f90_0003, "volume": 23.0283186559, "area": 120.1115037723},
    "model_48332_fb679f90_0009": {"func": model_48332_fb679f90_0009, "volume": 1.5712128142, "area": 12.7703694647},
    "model_49016_cd1b47bf_0027": {"func": model_49016_cd1b47bf_0027, "volume": 1744.1675668147, "area": 1674.7733214908},
    "model_49019_748c9a9f_0012": {"func": model_49019_748c9a9f_0012, "volume": 6.2329198247, "area": 71.5026487957},
    "model_49019_748c9a9f_0019": {"func": model_49019_748c9a9f_0019, "volume": 2.8274333882, "area": 49.6371639267},
    "model_49121_adb01620_0000": {"func": model_49121_adb01620_0000, "volume": 689.8752996886, "area": 994.5183563928},
    "model_49145_4a5b250e_0002": {"func": model_49145_4a5b250e_0002, "volume": 0.0208817737, "area": 0.6122178684},
    "model_49145_4a5b250e_0004": {"func": model_49145_4a5b250e_0004, "volume": 1.9768471548, "area": 11.2940255626},
    "model_49145_4a5b250e_0005": {"func": model_49145_4a5b250e_0005, "volume": 1.7495010931, "area": 12.8989669939},
    "model_49145_4a5b250e_0011": {"func": model_49145_4a5b250e_0011, "volume": 24.0418231798, "area": 101.5048586375},
    "model_49222_cbe1959b_0002": {"func": model_49222_cbe1959b_0002, "volume": 4.0000000596, "area": 45.2792156895},
    "model_49330_c6744767_0005": {"func": model_49330_c6744767_0005, "volume": 0.7275370132, "area": 5.8202961053},
    "model_49330_c6744767_0008": {"func": model_49330_c6744767_0008, "volume": 449.2477494633, "area": 629.8893270448},
    "model_49502_0ed856f7_0008": {"func": model_49502_0ed856f7_0008, "volume": 64.2371956182, "area": 211.7371430746},
    "model_49503_e42c01c0_0000": {"func": model_49503_e42c01c0_0000, "volume": 21.725586863, "area": 60.8068752524},
    "model_49503_e42c01c0_0001": {"func": model_49503_e42c01c0_0001, "volume": 40.111855001, "area": 396.0920017646},
    "model_49562_6df35938_0005": {"func": model_49562_6df35938_0005, "volume": 0.2967667392, "area": 3.4476673921},
    "model_49613_1b97c07b_0004": {"func": model_49613_1b97c07b_0004, "volume": 86.3937979737, "area": 238.7610416728},
    "model_49613_1b97c07b_0007": {"func": model_49613_1b97c07b_0007, "volume": 222.6211623506, "area": 206.3878457152},
    "model_49693_200d4b5d_0000": {"func": model_49693_200d4b5d_0000, "volume": 5.2833988526, "area": 52.559079734},
    "model_49803_beeceeef_0000": {"func": model_49803_beeceeef_0000, "volume": 2.3909325893, "area": 25.4117510616},
    "model_49806_24485616_0000": {"func": model_49806_24485616_0000, "volume": 2.3896065616, "area": 25.39625995},
    "model_49904_639055dd_0000": {"func": model_49904_639055dd_0000, "volume": 23.8499175735, "area": 81.0224415062},
    "model_49930_20f0e2ee_0002": {"func": model_49930_20f0e2ee_0002, "volume": 50.6770817532, "area": 169.7470054977},
    "model_50001_e86a6698_0006": {"func": model_50001_e86a6698_0006, "volume": 409.1712648236, "area": 429.3453849502},
    "model_50019_a59a348f_0000": {"func": model_50019_a59a348f_0000, "volume": 50.9440664706, "area": 91.4203462195},
    "model_50039_be53f8de_0008": {"func": model_50039_be53f8de_0008, "volume": 61.0391333355, "area": 338.0526559328},
    "model_50039_be53f8de_0009": {"func": model_50039_be53f8de_0009, "volume": 361.6758542445, "area": 462.2068191594},
    "model_50039_be53f8de_0012": {"func": model_50039_be53f8de_0012, "volume": 78.5354544375, "area": 193.7455685421},
    "model_50222_55cff75a_0000": {"func": model_50222_55cff75a_0000, "volume": 35.1225, "area": 163.62},
    "model_50409_4a322fbf_0009": {"func": model_50409_4a322fbf_0009, "volume": 1.8378018113, "area": 28.1505681022},
    "model_50715_fcc44f87_0002": {"func": model_50715_fcc44f87_0002, "volume": 0.2514474938, "area": 4.5550808536},
    "model_50777_2934de55_0021": {"func": model_50777_2934de55_0021, "volume": 0.2695984508, "area": 5.3806695415},
    "model_50897_3be92e2f_0016": {"func": model_50897_3be92e2f_0016, "volume": 5757.8817649156, "area": 4700.639741496},
    "model_50914_57d3d851_0002": {"func": model_50914_57d3d851_0002, "volume": 60.8951802178, "area": 182.0412621703},
    "model_50947_49287c16_0000": {"func": model_50947_49287c16_0000, "volume": 156.3031596612, "area": 245.8898648883},
    "model_51022_47816098_0005": {"func": model_51022_47816098_0005, "volume": 155.8387035813, "area": 284.3141351499},
    "model_51336_33ff2eba_0005": {"func": model_51336_33ff2eba_0005, "volume": 0.7041431146, "area": 9.3015519023},
    "model_51345_4b292361_0005": {"func": model_51345_4b292361_0005, "volume": 33.2, "area": 161.4},
    "model_51464_da501c24_0000": {"func": model_51464_da501c24_0000, "volume": 5624.7788708279, "area": 8921.0110264741},
    "model_51536_a18dc325_0000": {"func": model_51536_a18dc325_0000, "volume": 1.7310175452, "area": 36.9451294789},
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
