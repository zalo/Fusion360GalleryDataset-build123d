"""Batch 009 - passing/04_6to7ops
84 models bundled from Fusion360 Gallery reconstructions.
"""

from build123d import *
from build123d import Edge, BuildLine
from collections import Counter
from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
from OCP.Geom import Geom_BSplineCurve
from OCP.TColStd import TColStd_Array1OfReal, TColStd_Array1OfInteger
from OCP.TColgp import TColgp_Array1OfPnt
from OCP.gp import gp_Pnt


# Description: This is a complex molded plastic or composite component with an organic, curved form featuring multiple internal ribs, lattice reinforcement structures, and hollow sections throughout its body—designed to provide structural strength while minimizing weight.
def model_51583_cebed5ca_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 11 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 37.5302247103, perimeter: 40.3382471325
            with BuildLine():
                CenterArc((-0.2484097665, -2.6), 5.8, 61.5592823209, 56.8814353582)
                Line((-7.5, 2.5), (-3.0106552299, 2.5))
                Line((-7.5, 0.5), (-7.5, 2.5))
                Line((-7.5, 0.5), (-3.9, 0.5))
                Line((-3.9, 0.5), (-3.9, -2))
                Line((-3.9, -2), (-3.3407389857, -2))
                CenterArc((-0.2484097665, -2.6), 3.15, 13.0285284371, 155.9908961353)
                Line((3.3, -1.8898760328), (2.8205027366, -1.8898760328))
                Line((3.3, 0.5), (3.3, -1.8898760328))
                Line((6.9, 0.5), (3.3, 0.5))
                Line((6.9, 2.5), (6.9, 0.5))
                Line((2.5138356969, 2.5), (6.9, 2.5))
            make_face()
        # OneSide extrude, distance=6.3
        extrude(amount=6.3)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.7429699908, perimeter: 14.3515776023
            with BuildLine():
                Line((0, 7.5), (-6.3, 7.5))
                Line((-6.3, 7.5), (-6.3, 6.734490681))
                CenterArc((-3.15, 0.2601181246), 7.2, 64.0555202276, 51.8889595447)
                Line((0, 6.734490681), (0, 7.5))
            make_face()
            # Profile area: 8.1704583603, perimeter: 16.3920501005
            with BuildLine():
                Line((-6.3, -8), (-6.3, -6.2142544319))
                Line((0, -8), (-6.3, -8))
                Line((0, -6.2142544319), (0, -8))
                CenterArc((-3.15, 0.2601181246), 7.2, -115.9444797724, 51.8889595447)
            make_face()
            # Profile area: 9.45, perimeter: 15.6
            with BuildLine():
                Line((0, 9), (-6.3, 9))
                Line((-6.3, 9), (-6.3, 7.5))
                Line((0, 7.5), (-6.3, 7.5))
                Line((0, 7.5), (0, 9))
            make_face()
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.8352873699, perimeter: 5.9690260418
            with Locations((-3.15, 5.5101181246)):
                Circle(0.95)
            # Profile area: 2.8352873699, perimeter: 5.9690260418
            with Locations((-3.15, -4.9898818754)):
                Circle(0.95)
        # OneSide extrude, distance=-7
        extrude(amount=-7, mode=Mode.SUBTRACT)
    return part.part


# Description: A flat, elongated parallelogram-shaped plate with diagonal surface striping pattern, featuring no holes or complex features—a simple geometric sheet metal or planar component.
def model_51585_b695905b_0013():
    """Model: Heatcoil"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 85 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 17.8073290999, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 90, perimeter: 361
            with BuildLine():
                Line((1, 0.5), (2.5, 0.5))
                Line((2.5, 0.5), (2.5, 9))
                Line((2.5, 9), (3, 9))
                Line((3, 9), (3, 0.5))
                Line((3, 0.5), (4.5, 0.5))
                Line((4.5, 0.5), (4.5, 9))
                Line((4.5, 9), (5, 9))
                Line((5, 9), (5, 0.5))
                Line((5, 0.5), (6.5, 0.5))
                Line((6.5, 0.5), (6.5, 9))
                Line((6.5, 9), (7, 9))
                Line((7, 9), (7, 0.5))
                Line((7, 0.5), (8.5, 0.5))
                Line((8.5, 0.5), (8.5, 9))
                Line((8.5, 9), (9, 9))
                Line((9, 9), (9, 0.5))
                Line((9, 0.5), (10.5, 0.5))
                Line((10.5, 0.5), (10.5, 9))
                Line((10.5, 9), (11, 9))
                Line((11, 9), (11, 0.5))
                Line((11, 0.5), (12.5, 0.5))
                Line((12.5, 0.5), (12.5, 9))
                Line((12.5, 9), (13, 9))
                Line((13, 9), (13, 0.5))
                Line((13, 0.5), (14.5, 0.5))
                Line((14.5, 0.5), (14.5, 9))
                Line((14.5, 9), (15, 9))
                Line((15, 9), (15, 0.5))
                Line((15, 0.5), (16.5, 0.5))
                Line((16.5, 0.5), (16.5, 9))
                Line((16.5, 9), (17, 9))
                Line((17, 9), (17, 0.5))
                Line((17, 0.5), (18.5, 0.5))
                Line((18.5, 0.5), (18.5, 9))
                Line((18.5, 9), (19, 9))
                Line((19, 9), (19, 0.5))
                Line((19, 0.5), (19.5, 0.5))
                Line((19.5, 9.5), (19.5, 0.5))
                Line((18, 9.5), (19.5, 9.5))
                Line((18, 1), (18, 9.5))
                Line((17.5, 1), (18, 1))
                Line((17.5, 9.5), (17.5, 1))
                Line((16, 9.5), (17.5, 9.5))
                Line((16, 1), (16, 9.5))
                Line((15.5, 1), (16, 1))
                Line((15.5, 9.5), (15.5, 1))
                Line((14, 9.5), (15.5, 9.5))
                Line((14, 1), (14, 9.5))
                Line((13.5, 1), (14, 1))
                Line((13.5, 9.5), (13.5, 1))
                Line((12, 9.5), (13.5, 9.5))
                Line((12, 1), (12, 9.5))
                Line((11.5, 1), (12, 1))
                Line((11.5, 9.5), (11.5, 1))
                Line((10, 9.5), (11.5, 9.5))
                Line((10, 1), (10, 9.5))
                Line((9.5, 1), (10, 1))
                Line((9.5, 9.5), (9.5, 1))
                Line((8, 9.5), (9.5, 9.5))
                Line((8, 1), (8, 9.5))
                Line((7.5, 1), (8, 1))
                Line((7.5, 9.5), (7.5, 1))
                Line((6, 9.5), (7.5, 9.5))
                Line((6, 1), (6, 9.5))
                Line((5.5, 1), (6, 1))
                Line((5.5, 9.5), (5.5, 1))
                Line((4, 9.5), (5.5, 9.5))
                Line((4, 1), (4, 9.5))
                Line((3.5, 1), (4, 1))
                Line((3.5, 9.5), (3.5, 1))
                Line((2, 9.5), (3.5, 9.5))
                Line((2, 1), (2, 9.5))
                Line((1.5, 1), (2, 1))
                Line((1.5, 9.5), (1.5, 1))
                Line((1, 9.5), (1.5, 9.5))
                Line((1, 0.5), (1, 9.5))
            make_face()
        # OneSide extrude, distance=0.025
        extrude(amount=0.025)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 12 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 17.7823290999, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.25, perimeter: 2
            with BuildLine():
                Line((1.5, 9), (1.5, 9.5))
                Line((1.5, 9.5), (1, 9.5))
                Line((1, 9.5), (1, 9))
                Line((1, 9), (1.5, 9))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 12 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 17.7823290999, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.25, perimeter: 2
            with BuildLine():
                Line((19, 1), (19, 0.5))
                Line((19, 0.5), (19.5, 0.5))
                Line((19.5, 0.5), (19.5, 1))
                Line((19.5, 1), (19, 1))
            make_face()
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a curved, box-like structural component with a large oval or eye-shaped cutout through its center, featuring horizontal ribbing or fluting on its outer surfaces for reinforcement and weight reduction.
def model_51606_b72fa3d6_0009():
    """Model: Height Lock Metal Nut v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0561313471, perimeter: 2.6594927452
            with BuildLine():
                CenterArc((-0.9807821165, 0.635), 1.1684, -32.9207345281, 65.8414690562)
                Line((0, 1.190625), (0, 1.27))
                CenterArc((-1.0278323888, 0.635), 1.1684, -28.3947417411, 56.7894834823)
                Line((0, 0), (0, 0.079375))
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.635), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1054582749, perimeter: 2.2693253952
            with BuildLine():
                CenterArc((-1.0278323888, 0.635), 1.1684, -28.3947417411, 56.7894834823)
                Line((0, 1.190625), (0, 0.079375))
            make_face()
        # OneSide extrude, distance=-0.635
        extrude(amount=-0.635, mode=Mode.ADD)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0791730436, perimeter: 0.9974556675
            with Locations((-0.3175, 0.635)):
                Circle(0.15875)
        # OneSide extrude, distance=0.508
        extrude(amount=0.508, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a timing belt or synchronous drive belt with a hollow, oval-loop shape featuring regularly-spaced teeth or grooves on its inner surface for precise mechanical power transmission between pulleys.
def model_51731_22e19a47_0031():
    """Model: nakladka duza2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.167698931, perimeter: 43.3539786195
            with BuildLine():
                CenterArc((0, 0), 3.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.9
        extrude(amount=1.9)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 16.6818569906, perimeter: 37.0707933124
            with BuildLine():
                CenterArc((0, 0), 3.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.5393804003, perimeter: 30.7876080052
            with BuildLine():
                CenterArc((0, 0), 2.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6, mode=Mode.ADD)

        # Sketch2 -> Extrude5 (Cut)
        # Sketch on Profile plane
        # Sketch has 6 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0481056375, perimeter: 0.8997787144
            with BuildLine():
                Line((0, 2.7750000373), (0, 3.1250000373))
                CenterArc((0, 2.9500000373), 0.175, -90, 180)
            make_face()
            # Profile area: 0.0481056375, perimeter: 0.8997787144
            with BuildLine():
                CenterArc((0, 2.9500000373), 0.175, 90, 180)
                Line((0, 2.7750000373), (0, 3.1250000373))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a hydraulic cylinder with a long, slender rectangular body featuring rod ends at both extremities and a central longitudinal groove along its length.
def model_51775_49ef614a_0002():
    """Model: polaczenie_wlacznik"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.015655, perimeter: 0.7262
            with BuildLine():
                Line((0.0148627664, -0.3133380643), (-0.0351372336, -0.3133380643))
                Line((0.0148627664, -0.0002380643), (0.0148627664, -0.3133380643))
                Line((-0.0351372336, -0.0002380643), (0.0148627664, -0.0002380643))
                Line((-0.0351372336, -0.3133380643), (-0.0351372336, -0.0002380643))
            make_face()
        # Symmetric extrude, each_side=0.025
        extrude(amount=0.025, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.0148627664, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0003462875, perimeter: 0.0766439627
            with BuildLine():
                CenterArc((0, 0), 0.015, 90.9093767126, 178.1812465748)
                Line((-0.0002380643, -0.0149981107), (-0.0002380643, 0.0149981107))
            make_face()
            # Profile area: 0.0003605708, perimeter: 0.0775962598
            with BuildLine():
                Line((-0.0002380643, -0.0149981107), (-0.0002380643, 0.0149981107))
                CenterArc((0, 0), 0.015, -90.9093767126, 181.8187534252)
            make_face()
            # Profile area: 0.0003534292, perimeter: 0.0771238898
            with BuildLine():
                Line((-0.3133380643, 0.015), (-0.3133380643, -0.015))
                CenterArc((-0.3133380643, 0), 0.015, 90, 180)
            make_face()
            # Profile area: 0.0003534292, perimeter: 0.0771238898
            with BuildLine():
                CenterArc((-0.3133380643, 0), 0.015, -90, 180)
                Line((-0.3133380643, 0.015), (-0.3133380643, -0.015))
            make_face()
        # OneSide extrude, distance=0.045
        extrude(amount=0.045, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.0351372336, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0003534292, perimeter: 0.0771238898
            with BuildLine():
                Line((0.3133380643, -0.015), (0.3133380643, 0.015))
                CenterArc((0.3133380643, 0), 0.015, -90, 180)
            make_face()
            # Profile area: 0.0003534292, perimeter: 0.0771238898
            with BuildLine():
                CenterArc((0.3133380643, 0), 0.015, 90, 180)
                Line((0.3133380643, -0.015), (0.3133380643, 0.015))
            make_face()
            # Profile area: 0.0003605708, perimeter: 0.0775962598
            with BuildLine():
                Line((0.0002380643, 0.0149981107), (0.0002380643, -0.0149981107))
                CenterArc((0, 0), 0.015, 89.0906232874, 181.8187534252)
            make_face()
            # Profile area: 0.0003462875, perimeter: 0.0766439627
            with BuildLine():
                CenterArc((0, 0), 0.015, -89.0906232874, 178.1812465748)
                Line((0.0002380643, 0.0149981107), (0.0002380643, -0.0149981107))
            make_face()
        # OneSide extrude, distance=0.045
        extrude(amount=0.045, mode=Mode.ADD)
    return part.part


# Description: This is a pair of binoculars featuring two parallel cylindrical barrels connected by a central bridge, with a curved H-shaped profile and textured grip surfaces on the sides.
def model_51775_49ef614a_0009():
    """Model: lacznik_teleskopow"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6361725124, perimeter: 2.8274333882
            with Locations((-0.6000000089, 0)):
                Circle(0.45)
            # Profile area: 0.6361725124, perimeter: 2.8274333882
            with Locations((1.4003999911, 0)):
                Circle(0.45)
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((0.6000000089, 0)):
                Circle(0.4)
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((-1.4000000209, 0)):
                Circle(0.4)
        # OneSide extrude, distance=-2.7
        extrude(amount=-2.7, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on XY construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.5129977977, perimeter: 3.9740044944
            with BuildLine():
                Line((-0.200000003, 0.8000000119), (-0.200000003, 1.5000000224))
                CenterArc((0.400000006, 0), 1.0000000149, 53.1301023542, 73.7397952917)
                Line((1.0000000149, 1.5000000224), (1.0000000149, 0.8000000119))
                CenterArc((0.400000006, 2.3000000343), 1.0000000149, -126.8698976458, 73.7397952917)
            make_face()
        # Symmetric extrude, each_side=0.1
        extrude(amount=0.1, both=True, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical rod or tube with a tapered or pointed end, featuring a smooth elongated shape with a darker colored tip or ferrule at the bottom.
def model_51775_49ef614a_0010():
    """Model: teleskop1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.200000006, perimeter: 2.4000000358
            with BuildLine():
                Line((0.1000000015, 1.7000000253), (0.1000000015, 0.7000000104))
                Line((-0.1000000015, 1.7000000253), (0.1000000015, 1.7000000253))
                Line((-0.1000000015, 0.7000000104), (-0.1000000015, 1.7000000253))
                Line((0.1000000015, 0.7000000104), (-0.1000000015, 0.7000000104))
            make_face()
        # Symmetric extrude, each_side=0.5
        extrude(amount=0.5, both=True)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.7000000253, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1721687368, perimeter: 1.8290895227
            with BuildLine():
                CenterArc((0, 0), 0.4, 104.4775124064, 151.0449751873)
                Line((-0.1000000015, 0.3872983342), (-0.1000000015, -0.3872983342))
            make_face()
            # Profile area: 0.1583173509, perimeter: 1.9534817513
            with BuildLine():
                Line((-0.1000000015, 0.3872983342), (-0.1000000015, -0.3872983342))
                CenterArc((0, 0), 0.4, -104.4775124064, 28.9550248127)
                Line((0.1000000015, -0.3872983342), (0.1000000015, 0.3872983342))
                CenterArc((0, 0), 0.4, 75.5224875936, 28.9550248127)
            make_face()
            # Profile area: 0.1721687368, perimeter: 1.8290895227
            with BuildLine():
                Line((0.1000000015, -0.3872983342), (0.1000000015, 0.3872983342))
                CenterArc((0, 0), 0.4, -75.5224875936, 151.0449751873)
            make_face()
        # OneSide extrude, distance=13
        extrude(amount=13, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 14.7000000253, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            Circle(0.35)
        # OneSide extrude, distance=-12.5
        extrude(amount=-12.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a parallelogram-shaped flat plate or panel with internal triangular reinforcement ribs that radiate from a central point, providing structural support and reducing weight while maintaining rigidity.
def model_51777_87ff5835_0007():
    """Model: Table-005"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 140.3223, perimeter: 151.13
            with BuildLine():
                Line((36.83, -0.9525), (-36.83, -0.9525))
                Line((36.83, 0.9525), (36.83, -0.9525))
                Line((-36.83, 0.9525), (36.83, 0.9525))
                Line((-36.83, -0.9525), (-36.83, 0.9525))
            make_face()
        # Symmetric extrude, each_side=34.29
        extrude(amount=34.29, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.9525, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            with Locations((0, 25.4)):
                Circle(0.635)
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            with Locations((0, -25.4)):
                Circle(0.635)
        # OneSide extrude, distance=-12.7
        extrude(amount=-12.7, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(36.83, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            with Locations((-19.05, 0)):
                Circle(0.635)
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            with Locations((19.05, 0)):
                Circle(0.635)
        # OneSide extrude, distance=-1.27
        extrude(amount=-1.27, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a complex industrial housing or enclosure with an irregular, angular shape featuring multiple flat and curved surfaces, several rectangular openings or slots along the top, and four protruding cylindrical posts or mounting flanges at the corners.
def model_51863_0b8751d1_0002():
    """Model: Pedal"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 15 constraints, 13 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 54.9456480012, perimeter: 68.3233725926
            with BuildLine():
                CenterArc((3.4363409108, 25.5510714856), 2.54, 180, 90)
                Line((3.4363409108, 23.0110714856), (5.9763407964, 23.0110714856))
                CenterArc((5.9763407964, 25.5510714856), 2.54, -90, 90)
                Line((8.5163407964, 25.5510714856), (8.5163407964, 30.6310714856))
                CenterArc((5.9763407964, 30.6310714856), 2.54, 0, 90)
                Line((5.9763407964, 33.1710714856), (3.4363409108, 33.1710714856))
                CenterArc((3.4363409108, 30.6310714856), 2.54, 90, 90)
                Line((0.8963409108, 30.6310714856), (0.8963409108, 25.5510714856))
            make_face()
            with BuildLine():
                Line((6.1907015287, 23.646423612), (8.1353407964, 28.091423612))
                Line((6.2698260126, 32.5360714856), (6.1907015287, 23.646423612))
                Line((8.1353407964, 28.091423612), (6.2698260126, 32.5360714856))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((3.1425776607, 23.6460714856), (1.277066011, 28.0910714856))
                Line((1.277066011, 28.0910714856), (3.2217021445, 32.5357193592))
                Line((3.2217021445, 32.5357193592), (3.1425776607, 23.6460714856))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 30 constraints, 14 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.54, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 0.80645, perimeter: 3.81
            with BuildLine():
                Line((-0.8963409108, -29.3610714856), (-0.8963409108, -30.6310714856))
                Line((-1.5313409108, -29.3610714856), (-0.8963409108, -29.3610714856))
                Line((-1.5313409108, -30.6310714856), (-1.5313409108, -29.3610714856))
                Line((-0.8963409108, -30.6310714856), (-1.5313409108, -30.6310714856))
            make_face()
            # Profile area: 0.80645, perimeter: 3.81
            with BuildLine():
                Line((-0.8963409108, -26.8210714856), (-0.8963409108, -25.5510714856))
                Line((-0.8963409108, -25.5510714856), (-1.5313409108, -25.5510714856))
                Line((-1.5313409108, -25.5510714856), (-1.5313409108, -26.8210714856))
                Line((-1.5313409108, -26.8210714856), (-0.8963409108, -26.8210714856))
            make_face()
            # Profile area: 0.80645, perimeter: 3.81
            with BuildLine():
                Line((-4.0713409108, -23.0110714856), (-5.3413409108, -23.0110714856))
                Line((-5.3413409108, -23.0110714856), (-5.3413409108, -23.6460714856))
                Line((-5.3413409108, -23.6460714856), (-4.0713409108, -23.6460714856))
                Line((-4.0713409108, -23.6460714856), (-4.0713409108, -23.0110714856))
            make_face()
            # Profile area: 0.80645, perimeter: 3.81
            with BuildLine():
                Line((-8.5163407964, -26.8210714856), (-8.5163407964, -25.5510714856))
                Line((-7.8813407964, -26.8210714856), (-8.5163407964, -26.8210714856))
                Line((-7.8813407964, -25.5510714856), (-7.8813407964, -26.8210714856))
                Line((-8.5163407964, -25.5510714856), (-7.8813407964, -25.5510714856))
            make_face()
            # Profile area: 0.80645, perimeter: 3.81
            with BuildLine():
                Line((-8.5163407964, -29.3610714856), (-8.5163407964, -30.6310714856))
                Line((-8.5163407964, -30.6310714856), (-7.8813407964, -30.6310714856))
                Line((-7.8813407964, -30.6310714856), (-7.8813407964, -29.3610714856))
                Line((-7.8813407964, -29.3610714856), (-8.5163407964, -29.3610714856))
            make_face()
            # Profile area: 0.80645, perimeter: 3.81
            with BuildLine():
                Line((-4.0713409108, -33.1710714856), (-5.3413409108, -33.1710714856))
                Line((-4.0713409108, -32.5360714856), (-4.0713409108, -33.1710714856))
                Line((-5.3413409108, -32.5360714856), (-4.0713409108, -32.5360714856))
                Line((-5.3413409108, -33.1710714856), (-5.3413409108, -32.5360714856))
            make_face()
        # TwoSides extrude, along=0.635, against=-3.175
        extrude(amount=0.635, mode=Mode.ADD)
        extrude(sk.sketch, amount=-3.175, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -23.0110714856), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 4.8664186293, perimeter: 7.8200524333
            with Locations((4.7063407964, 1.27)):
                Circle(1.2446)
        # OneSide extrude, distance=-5.08
        extrude(amount=-5.08, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a stylus pen with a long, tapered cylindrical shaft and a small rounded tip, featuring a smooth, streamlined design for digital input devices.
def model_51863_0b8751d1_0009():
    """Model: handle bars"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 15.2012237641, perimeter: 23.9389357807
            with BuildLine():
                CenterArc((66.0399990082, 12.6999998093), 2.5399999619, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((66.0399990082, 12.6999998093), 1.27, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=5.08
        extrude(amount=5.08)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5.08, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 15.2012237641, perimeter: 23.9389357807
            with BuildLine():
                CenterArc((-66.0399990082, -12.6999998093), 2.5399999619, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-66.0399990082, -12.6999998093), 1.27, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 5.067074791, perimeter: 7.9796453401
            with Locations((-66.0399990082, -12.6999998093)):
                Circle(1.27)
        # OneSide extrude, distance=2.54
        extrude(amount=2.54, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 116.1288, perimeter: 96.52
            with BuildLine():
                Line((22.86, 5.08), (-22.86, 5.08))
                Line((22.86, 7.62), (22.86, 5.08))
                Line((-22.86, 7.62), (22.86, 7.62))
                Line((-22.86, 5.08), (-22.86, 7.62))
            make_face()
        # OneSide extrude, distance=2.54
        extrude(amount=2.54, mode=Mode.ADD)
    return part.part


# Description: This is a metal mounting bracket or support beam with an elongated rectangular base, angled flanges along the top edges, three evenly-spaced rectangular holes for fastening or mounting, and a truss-like internal ribbed structure for reinforcement and lightweight strength.
def model_51871_86ebf5b2_0000():
    """Model: Panel Cover v7"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 6 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 11.1343239514, perimeter: 50.6573134971
            with BuildLine():
                Line((-2.9, 6.9640971056), (-2.9, 0))
                Line((-2.9, 0), (-2.5, 0))
                Line((-2.5, 0), (-2.5, 6.5087894743))
                Line((-2.5, 6.5087894743), (2.4680334757, 10))
                Line((2.4680334757, 10), (4, 10))
                Line((4, 10), (4, 0))
                Line((4, 0), (4.4, 0))
                Line((4.4, 0), (4.4, 10.4))
                Line((4.4, 10.4), (2.0232482349, 10.4))
                Line((-2.9, 6.9640971056), (2.0232482349, 10.4))
            make_face()
        # OneSide extrude, distance=60
        extrude(amount=60)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.9), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.3926990817, perimeter: 2.5707963268
            with BuildLine():
                Line((12.0003954093, 3.2), (13.0003954093, 3.2))
                CenterArc((12.5003954093, 3.2), 0.5, 0, 180)
            make_face()
            # Profile area: 0.3926990817, perimeter: 2.5707963268
            with BuildLine():
                CenterArc((12.5003954093, 3.2), 0.5, 180, 180)
                Line((12.0003954093, 3.2), (13.0003954093, 3.2))
            make_face()
            # Profile area: 0.3926990817, perimeter: 2.5707963268
            with BuildLine():
                CenterArc((30.0003954093, 3.2), 0.5, 180, 180)
                Line((29.5003954093, 3.2), (30.5003954093, 3.2))
            make_face()
            # Profile area: 0.3926990817, perimeter: 2.5707963268
            with BuildLine():
                Line((29.5003954093, 3.2), (30.5003954093, 3.2))
                CenterArc((30.0003954093, 3.2), 0.5, 0, 180)
            make_face()
            # Profile area: 0.3926990817, perimeter: 2.5707963268
            with BuildLine():
                CenterArc((47.5003954093, 3.2), 0.5, 0, 180)
                Line((47.0003954093, 3.2), (48.0003954093, 3.2))
            make_face()
            # Profile area: 0.3926990817, perimeter: 2.5707963268
            with BuildLine():
                Line((47.0003954093, 3.2), (48.0003954093, 3.2))
                CenterArc((47.5003954093, 3.2), 0.5, 180, 180)
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.9), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 2.0616701789, perimeter: 6.9977871438
            with BuildLine():
                Line((11.2503954093, 3.2), (12.0003954093, 3.2))
                CenterArc((12.5003954093, 3.2), 0.5, 0, 180)
                Line((13.0003954093, 3.2), (13.7503954093, 3.2))
                CenterArc((12.5003954093, 3.2), 1.25, 0, 180)
            make_face()
            # Profile area: 2.0616701789, perimeter: 6.9977871438
            with BuildLine():
                CenterArc((12.5003954093, 3.2), 1.25, 180, 180)
                Line((13.0003954093, 3.2), (13.7503954093, 3.2))
                CenterArc((12.5003954093, 3.2), 0.5, 180, 180)
                Line((11.2503954093, 3.2), (12.0003954093, 3.2))
            make_face()
            # Profile area: 2.0616701789, perimeter: 6.9977871438
            with BuildLine():
                CenterArc((30.0003954093, 3.2), 1.25, 180, 180)
                Line((30.5003954093, 3.2), (31.2503954093, 3.2))
                CenterArc((30.0003954093, 3.2), 0.5, 180, 180)
                Line((28.7503954093, 3.2), (29.5003954093, 3.2))
            make_face()
            # Profile area: 2.0616701789, perimeter: 6.9977871438
            with BuildLine():
                Line((28.7503954093, 3.2), (29.5003954093, 3.2))
                CenterArc((30.0003954093, 3.2), 0.5, 0, 180)
                Line((30.5003954093, 3.2), (31.2503954093, 3.2))
                CenterArc((30.0003954093, 3.2), 1.25, 0, 180)
            make_face()
            # Profile area: 2.0616701789, perimeter: 6.9977871438
            with BuildLine():
                Line((48.0003954093, 3.2), (48.7503954093, 3.2))
                CenterArc((47.5003954093, 3.2), 1.25, 0, 180)
                Line((46.2503954093, 3.2), (47.0003954093, 3.2))
                CenterArc((47.5003954093, 3.2), 0.5, 0, 180)
            make_face()
            # Profile area: 2.0616701789, perimeter: 6.9977871438
            with BuildLine():
                CenterArc((47.5003954093, 3.2), 0.5, 180, 180)
                Line((46.2503954093, 3.2), (47.0003954093, 3.2))
                CenterArc((47.5003954093, 3.2), 1.25, 180, 180)
                Line((48.0003954093, 3.2), (48.7503954093, 3.2))
            make_face()
            # Profile area: 0.3926990817, perimeter: 2.5707963268
            with BuildLine():
                Line((12.0003954093, 3.2), (13.0003954093, 3.2))
                CenterArc((12.5003954093, 3.2), 0.5, 0, 180)
            make_face()
            # Profile area: 0.3926990817, perimeter: 2.5707963268
            with BuildLine():
                CenterArc((12.5003954093, 3.2), 0.5, 180, 180)
                Line((12.0003954093, 3.2), (13.0003954093, 3.2))
            make_face()
            # Profile area: 0.3926990817, perimeter: 2.5707963268
            with BuildLine():
                CenterArc((30.0003954093, 3.2), 0.5, 180, 180)
                Line((29.5003954093, 3.2), (30.5003954093, 3.2))
            make_face()
            # Profile area: 0.3926990817, perimeter: 2.5707963268
            with BuildLine():
                Line((29.5003954093, 3.2), (30.5003954093, 3.2))
                CenterArc((30.0003954093, 3.2), 0.5, 0, 180)
            make_face()
            # Profile area: 0.3926990817, perimeter: 2.5707963268
            with BuildLine():
                CenterArc((47.5003954093, 3.2), 0.5, 0, 180)
                Line((47.0003954093, 3.2), (48.0003954093, 3.2))
            make_face()
            # Profile area: 0.3926990817, perimeter: 2.5707963268
            with BuildLine():
                Line((47.0003954093, 3.2), (48.0003954093, 3.2))
                CenterArc((47.5003954093, 3.2), 0.5, 180, 180)
            make_face()
        # TwoSides extrude (symmetric), distance=10
        extrude(amount=10, both=True, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a flat sheet metal or plastic panel with a trapezoidal shape and a triangular fold or flange on the left side, featuring internal ribbing or structural reinforcements visible through the translucent rendering.
def model_51871_86ebf5b2_0010():
    """Model: Shelf v2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 600, perimeter: 100
            with BuildLine():
                Line((30, -20), (0, -20))
                Line((30, 0), (30, -20))
                Line((0, 0), (30, 0))
                Line((0, -20), (0, 0))
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 65, perimeter: 39.4012194669
            with BuildLine():
                Line((0, 0), (0, -10))
                Line((-13, 0), (0, 0))
                Line((0, -10), (-13, 0))
            make_face()
        # OneSide extrude, distance=30
        extrude(amount=30, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 336, perimeter: 80
            with BuildLine():
                Line((1, 13), (29, 13))
                Line((1, 1), (1, 13))
                Line((29, 1), (1, 1))
                Line((29, 13), (29, 1))
            make_face()
        # OneSide extrude, distance=11
        extrude(amount=11, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a timing belt or drive belt featuring a toroidal/donut shape with evenly-spaced teeth on the inner surface and a mesh-textured outer rim for grip and durability.
def model_51876_8346832d_0011():
    """Model: New Wheel v1 (1)"""
    with BuildPart() as part:
        # Sketch12 -> Extrude6 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 81.0731966556, perimeter: 31.9185813605
            Circle(5.08)
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)

        # Sketch13 -> Extrude7 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 45.6036731188, perimeter: 23.9389360204
            Circle(3.81)
        # OneSide extrude, distance=46.482
        extrude(amount=46.482, mode=Mode.SUBTRACT)

        # Sketch14 -> Extrude8 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.9030833901, perimeter: 8.2661703793
            with BuildLine():
                Line((0.0369728705, -3.8098206003), (0.7620000243, -2.5400000811))
                Line((0.7620000243, -2.5400000811), (0, 0))
                Line((0, 0), (-0.7620000243, -2.5400000811))
                Line((-0.7620000243, -2.5400000811), (0.0369728705, -3.8098206003))
            make_face()
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)
    return part.part


# Description: This is a flat, disk-shaped washer or spacer ring with a central hole and a small radial hole or slot positioned near the outer edge, featuring a slightly beveled or curved outer rim.
def model_51895_5760b481_0006():
    """Model: Obrecz"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 7.6340701482, perimeter: 50.8938009882
            with BuildLine():
                CenterArc((0, 0), 4.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3.9, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 33.4717062286, perimeter: 40.683624864
            with BuildLine():
                CenterArc((0, 0), 3.9, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.075, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 3), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 7.6340701482, perimeter: 50.8938009882
            with BuildLine():
                CenterArc((0, 0), 4.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3.9, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.15
        extrude(amount=1.15, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -1.15), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
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


# Description: This is a bent or curved bracket or connector part with an angular, tubular structure featuring multiple flat faces, internal voids, and triangulated geometric sections that form an asymmetrical 90-degree bent configuration.
def model_51895_5760b481_0007():
    """Model: Connector"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 7.4194650547, perimeter: 74.1946505208
            with BuildLine():
                Line((4.6, 0.1), (4.6, -5))
                Line((4.6, -5), (8, -5))
                Line((8, -5), (8.0001999984, 1.5998969628))
                CenterArc((4.6, 1.6), 3.4002, -0.0017362493, 90.003472485)
                Line((-2.0001030333, 4.9999999984), (4.5998969636, 5.0001999984))
                Line((-2.0001030333, 4.9999999984), (-2, 1.6))
                Line((-2, 1.6), (3.1, 1.6))
                CenterArc((3.1, 0.1), 1.5, 0, 90)
            make_face()
            with BuildLine():
                CenterArc((3.1, 0.1), 1.7, 0, 90)
                Line((-1.8000060607, 1.8), (3.1, 1.8))
                Line((-1.8000969726, 4.8000060591), (-1.8000060607, 1.8))
                Line((-1.8000969726, 4.8000060591), (4.5999030242, 4.8001999985))
                CenterArc((4.6, 1.6), 3.2002, 0.0001084545, 90.0016277812)
                Line((7.8000060606, -4.8), (7.8002000017, 1.6000060576))
                Line((4.8, -4.8), (7.8000060606, -4.8))
                Line((4.8, 0.1), (4.8, -4.8))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3.4
        extrude(amount=3.4)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 47.0251551915, perimeter: 36.2973313208
            with BuildLine():
                Line((4.8, 0.1), (4.8, -4.8))
                Line((4.8, -4.8), (7.8000060606, -4.8))
                Line((7.8000060606, -4.8), (7.8002000017, 1.6000060576))
                CenterArc((4.6, 1.6), 3.2002, 0.0001084545, 90.0016277812)
                Line((-1.8000969726, 4.8000060591), (4.5999030242, 4.8001999985))
                Line((-1.8000969726, 4.8000060591), (-1.8000060607, 1.8))
                Line((-1.8000060607, 1.8), (3.1, 1.8))
                CenterArc((3.1, 0.1), 1.7, 0, 90)
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 47.0251551915, perimeter: 36.2973313208
            with BuildLine():
                Line((4.8, 0.1), (4.8, -4.8))
                Line((4.8, -4.8), (7.8000060606, -4.8))
                Line((7.8000060606, -4.8), (7.8002000017, 1.6000060576))
                CenterArc((4.6, 1.6), 3.2002, 0.0001084545, 90.0016277812)
                Line((-1.8000969726, 4.8000060591), (4.5999030242, 4.8001999985))
                Line((-1.8000969726, 4.8000060591), (-1.8000060607, 1.8))
                Line((-1.8000060607, 1.8), (3.1, 1.8))
                CenterArc((3.1, 0.1), 1.7, 0, 90)
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch1 -> Extrude4 (Cut)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 47.0251551915, perimeter: 36.2973313208
            with BuildLine():
                Line((4.8, 0.1), (4.8, -4.8))
                Line((4.8, -4.8), (7.8000060606, -4.8))
                Line((7.8000060606, -4.8), (7.8002000017, 1.6000060576))
                CenterArc((4.6, 1.6), 3.2002, 0.0001084545, 90.0016277812)
                Line((-1.8000969726, 4.8000060591), (4.5999030242, 4.8001999985))
                Line((-1.8000969726, 4.8000060591), (-1.8000060607, 1.8))
                Line((-1.8000060607, 1.8), (3.1, 1.8))
                CenterArc((3.1, 0.1), 1.7, 0, 90)
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.SUBTRACT)

        # Sketch1 -> Extrude5 (Join)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 7.4194650547, perimeter: 74.1946505208
            with BuildLine():
                Line((4.6, 0.1), (4.6, -5))
                Line((4.6, -5), (8, -5))
                Line((8, -5), (8.0001999984, 1.5998969628))
                CenterArc((4.6, 1.6), 3.4002, -0.0017362493, 90.003472485)
                Line((-2.0001030333, 4.9999999984), (4.5998969636, 5.0001999984))
                Line((-2.0001030333, 4.9999999984), (-2, 1.6))
                Line((-2, 1.6), (3.1, 1.6))
                CenterArc((3.1, 0.1), 1.5, 0, 90)
            make_face()
            with BuildLine():
                CenterArc((3.1, 0.1), 1.7, 0, 90)
                Line((-1.8000060607, 1.8), (3.1, 1.8))
                Line((-1.8000969726, 4.8000060591), (-1.8000060607, 1.8))
                Line((-1.8000969726, 4.8000060591), (4.5999030242, 4.8001999985))
                CenterArc((4.6, 1.6), 3.2002, 0.0001084545, 90.0016277812)
                Line((7.8000060606, -4.8), (7.8002000017, 1.6000060576))
                Line((4.8, -4.8), (7.8000060606, -4.8))
                Line((4.8, 0.1), (4.8, -4.8))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 47.0251551915, perimeter: 36.2973313208
            with BuildLine():
                Line((4.8, 0.1), (4.8, -4.8))
                Line((4.8, -4.8), (7.8000060606, -4.8))
                Line((7.8000060606, -4.8), (7.8002000017, 1.6000060576))
                CenterArc((4.6, 1.6), 3.2002, 0.0001084545, 90.0016277812)
                Line((-1.8000969726, 4.8000060591), (4.5999030242, 4.8001999985))
                Line((-1.8000969726, 4.8000060591), (-1.8000060607, 1.8))
                Line((-1.8000060607, 1.8), (3.1, 1.8))
                CenterArc((3.1, 0.1), 1.7, 0, 90)
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch1 -> Extrude6 (Join)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 7.4194650547, perimeter: 74.1946505208
            with BuildLine():
                Line((4.6, 0.1), (4.6, -5))
                Line((4.6, -5), (8, -5))
                Line((8, -5), (8.0001999984, 1.5998969628))
                CenterArc((4.6, 1.6), 3.4002, -0.0017362493, 90.003472485)
                Line((-2.0001030333, 4.9999999984), (4.5998969636, 5.0001999984))
                Line((-2.0001030333, 4.9999999984), (-2, 1.6))
                Line((-2, 1.6), (3.1, 1.6))
                CenterArc((3.1, 0.1), 1.5, 0, 90)
            make_face()
            with BuildLine():
                CenterArc((3.1, 0.1), 1.7, 0, 90)
                Line((-1.8000060607, 1.8), (3.1, 1.8))
                Line((-1.8000969726, 4.8000060591), (-1.8000060607, 1.8))
                Line((-1.8000969726, 4.8000060591), (4.5999030242, 4.8001999985))
                CenterArc((4.6, 1.6), 3.2002, 0.0001084545, 90.0016277812)
                Line((7.8000060606, -4.8), (7.8002000017, 1.6000060576))
                Line((4.8, -4.8), (7.8000060606, -4.8))
                Line((4.8, 0.1), (4.8, -4.8))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 47.0251551915, perimeter: 36.2973313208
            with BuildLine():
                Line((4.8, 0.1), (4.8, -4.8))
                Line((4.8, -4.8), (7.8000060606, -4.8))
                Line((7.8000060606, -4.8), (7.8002000017, 1.6000060576))
                CenterArc((4.6, 1.6), 3.2002, 0.0001084545, 90.0016277812)
                Line((-1.8000969726, 4.8000060591), (4.5999030242, 4.8001999985))
                Line((-1.8000969726, 4.8000060591), (-1.8000060607, 1.8))
                Line((-1.8000060607, 1.8), (3.1, 1.8))
                CenterArc((3.1, 0.1), 1.7, 0, 90)
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.ADD)
    return part.part


# Description: This is a Saturn-shaped planetary gear or pulley featuring a large central dome with a wide, flat annular flange extending radially outward, and textured surface details suggesting internal ribbing or structural reinforcement.
def model_51940_aa0fca73_0005():
    """Model: piastra v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 107.5131545875, perimeter: 36.756634047
            Circle(5.85)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 17.6243347866, perimeter: 32.0442450666
            with BuildLine():
                CenterArc((0, 0), 3.1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            Circle(2)
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical socket or sleeve with a hexagonal or knurled head at the top, featuring a hollow interior bore, commonly used as a fastener or connector component.
def model_52024_97da327b_0006():
    """Model: Arrow Rest Bracket Screw (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.8107319666, perimeter: 3.191858136
            with Locations((-1.0160000324, 0)):
                Circle(0.508)
        # OneSide extrude, distance=0.508
        extrude(amount=0.508)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.1829214, perimeter: 1.5161326146
            with Locations((-1.0160000324, 0)):
                Circle(0.2413)
        # OneSide extrude, distance=1.905
        extrude(amount=1.905, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.508, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.377139365, perimeter: 2.286000073
            with BuildLine():
                Line((0.6860443431, -0.1905000061), (1.0160000324, -0.3810000122))
                Line((1.0160000324, -0.3810000122), (1.3459557218, -0.1905000061))
                Line((1.3459557218, -0.1905000061), (1.3459557218, 0.1905000061))
                Line((1.3459557218, 0.1905000061), (1.0160000324, 0.3810000122))
                Line((1.0160000324, 0.3810000122), (0.6860443431, 0.1905000061))
                Line((0.6860443431, 0.1905000061), (0.6860443431, -0.1905000061))
            make_face()
        # OneSide extrude, distance=-0.254
        extrude(amount=-0.254, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a small metal razor blade or utility knife blade, characterized by a thin rectangular shape with a sharp cutting edge and two circular holes or slots for attachment and blade retention.
def model_52352_adac16c3_0005():
    """Model: FrontDashboard (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-183.9, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 1500, perimeter: 160
            with BuildLine():
                Line((-160, 165), (-130, 165))
                Line((-160, 115), (-160, 165))
                Line((-130, 115), (-160, 115))
                Line((-130, 165), (-130, 115))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-184.9, 0, 0), x_dir=(0, 0, -1), z_dir=(-1, 0, 0))):
            # Profile area: 2400, perimeter: 200
            with BuildLine():
                Line((-165, 170), (-125, 170))
                Line((-165, 110), (-165, 170))
                Line((-125, 110), (-165, 110))
                Line((-125, 170), (-125, 110))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 39 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-185.9, 0, 0), x_dir=(0, 0, -1), z_dir=(-1, 0, 0))):
            # Profile area: 117, perimeter: 49.6227766017
            with BuildLine():
                Line((-136.3915207776, 135.1739576782), (-136, 135.1739576782))
                Line((-154, 135.1739576782), (-136.3915207776, 135.1739576782))
                Line((-154, 135.1739576782), (-145, 122.1739576782))
                Line((-145, 122.1739576782), (-136, 135.1739576782))
            make_face()
            # Profile area: 117, perimeter: 49.6227766017
            with BuildLine():
                Line((-136, 144.8260423218), (-136.3915207776, 144.8260423218))
                Line((-145, 157.8260423218), (-136, 144.8260423218))
                Line((-154, 144.8260423218), (-145, 157.8260423218))
                Line((-136.3915207776, 144.8260423218), (-154, 144.8260423218))
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a boat hull or marine vessel structure with a trapezoidal plan view, featuring multiple internal compartments, reinforcing ribs, and rectangular openings or slots along the sides for ventilation or access points.
def model_52443_085efc00_0013():
    """Model: screen part 1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 21 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 31.8690266447, perimeter: 51.5398223686
            with BuildLine():
                Line((-3.9, 3.1), (3.9, 3.1))
                Line((-3.9, -3.1), (-3.9, 3.1))
                Line((3.9, -3.1), (-3.9, -3.1))
                Line((3.9, 3.1), (3.9, -3.1))
            make_face()
            with BuildLine():
                Line((2.4, 1.6), (2.4, -1.6))
                Line((2.4, -1.6), (-2.4, -1.6))
                Line((-2.4, -1.6), (-2.4, 1.6))
                Line((-2.4, 1.6), (2.4, 1.6))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.5, 2.35), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.5, 2.35), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.5, -2.35), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.5, -2.35), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 15.36, perimeter: 16
            with BuildLine():
                Line((-2.4, 1.6), (2.4, 1.6))
                Line((-2.4, -1.6), (-2.4, 1.6))
                Line((2.4, -1.6), (-2.4, -1.6))
                Line((2.4, 1.6), (2.4, -1.6))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 21 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 15.36, perimeter: 16
            with BuildLine():
                Line((-2.4, 1.6), (2.4, 1.6))
                Line((-2.4, -1.6), (-2.4, 1.6))
                Line((2.4, -1.6), (-2.4, -1.6))
                Line((2.4, 1.6), (2.4, -1.6))
            make_face()
        # OneSide extrude, distance=2.5
        extrude(amount=2.5, mode=Mode.ADD)
    return part.part


# Description: This is a curved, aerodynamic air intake or duct component with a tapered tubular shape, featuring mesh or perforated sections on the upper surface and a solid base, designed to direct airflow with smooth transitions and internal ribbing for structural support.
def model_52446_094458cd_0000():
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
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 13.1712100906, perimeter: 12.8652363926
            with BuildLine():
                CenterArc((-9.4106056425, -2.7618081777), 2.0475659659, -35.064592198, 250.1291843959)
                CenterArc((-9.4106056425, -2.7618081777), 2.0475659659, -144.935407802, 109.8708156041)
            make_face()
            # Profile area: 148.9188545222, perimeter: 76.9620863355
            with BuildLine():
                Line((8.4942876766, -3.938133883), (-7.7346628571, -3.938133883))
                CenterArc((10.0740365135, -2.6709649448), 2.0251724633, -37.4219739503, 256.1562299912)
                Line((13.8601854843, -3.9016226934), (11.6823912666, -3.9016226934))
                _nurbs_edge([(11.4091567671, 1.9084323293), (11.6149340331, 1.8688630646), (12.0126782215, 1.7829732319), (12.5678641081, 1.6338848829), (13.2238824727, 1.3939241211), (13.8941012487, 1.0207401275), (14.4015446499, 0.5679820139), (14.7335753688, 0.0294719256), (14.8844932453, -0.597576709), (14.8628269466, -1.3089945785), (14.6821743399, -2.0981342507), (14.4211847055, -2.7863821357), (14.1641362654, -3.3325381113), (13.9659694697, -3.7097440734), (13.8601854843, -3.9016226934)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(-6.6067096751, 0.9929031085), (-6.4247542585, 1.1446395367), (-6.0552316292, 1.4362248949), (-5.484111955, 1.8379398517), (-4.6887057734, 2.3017201957), (-3.6370111936, 2.7594436527), (-2.5277948828, 3.0939606821), (-1.3628940623, 3.3071325298), (-0.1478223993, 3.4071213754), (1.1077886464, 3.4092982885), (2.392327145, 3.3325308512), (3.6936187528, 3.1968481486), (5.000411753, 3.0210119619), (6.3039678672, 2.8200755888), (7.5990341792, 2.6038542564), (8.882729775, 2.3783507121), (9.8996560805, 2.1929528468), (10.6566189657, 2.0515875815), (11.158732286, 1.9563212032), (11.4091567671, 1.9084323293)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9333333333, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(-13.8090408884, -3.938133883), (-13.9217727058, -3.8446306058), (-14.1253542251, -3.6551525489), (-14.365081693, -3.3635213855), (-14.5524608027, -2.9597400484), (-14.5638104165, -2.4310545581), (-14.3548781762, -1.8823382832), (-13.9395649564, -1.3225821064), (-13.3486861664, -0.7675807624), (-12.6232264428, -0.2373437717), (-11.8093777157, 0.2460239588), (-10.9535549415, 0.6606311294), (-10.0979106354, 0.9871025157), (-9.2755611735, 1.2112864361), (-8.5062707183, 1.3268524018), (-7.800314138, 1.3323793251), (-7.289255099, 1.2498176116), (-6.9362781774, 1.1398928565), (-6.7143364399, 1.0454297214), (-6.6067096751, 0.9929031085)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9333333333, 1, 1, 1, 1, 1, 1], 5)
                Line((-11.0865484279, -3.938133883), (-13.8090408884, -3.938133883))
                CenterArc((-9.4106056425, -2.7618081777), 2.0475659659, -35.064592198, 250.1291843959)
            make_face()
            # Profile area: 12.8846877965, perimeter: 12.7245338658
            with BuildLine():
                CenterArc((10.0740365135, -2.6709649448), 2.0251724633, -37.4219739503, 256.1562299912)
                CenterArc((10.0740365135, -2.6709649448), 2.0251724633, -141.2657439591, 103.8437700088)
            make_face()
        # OneSide extrude, distance=10
        extrude(amount=10)
    return part.part


# Description: This is a square-to-round adapter or transition ring featuring a square outer profile with an integrated circular opening, characterized by curved transitional walls that connect the square perimeter to the central oval aperture.
def model_52557_e6a00b06_0013():
    """Model: seal bag"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 120.8859085142, perimeter: 99.9800526056
            with BuildLine():
                Line((-14.2, 8), (-15.2000002265, 15.8000002354))
                Line((-29.8126586661, 15.8000002354), (-15.2000002265, 15.8000002354))
                Line((-30.8, 8), (-29.8126586661, 15.8000002354))
                Line((-30.8, 8), (-29.8250000004, 0.200000003))
                Line((-15.1749999996, 0.200000003), (-29.8250000004, 0.200000003))
                Line((-14.2, 8), (-15.1749999996, 0.200000003))
            make_face()
            with BuildLine():
                CenterArc((-22.5, 8.4487527048), 6.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 20.4203522483, perimeter: 81.6814089933
            with BuildLine():
                CenterArc((-22.5, 8.4487527048), 6.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-22.5, 8.4487527048), 6.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 54.9286378751, perimeter: 89.192824834
            with BuildLine():
                Line((29, 1), (29.4832107595, 7.9642245957))
                CenterArc((22.5, 8.4487527048), 7, -3.969090276, 187.9381805519)
                Line((16, 1), (15.5167892405, 7.9642245957))
                Line((29, 1), (16, 1))
            make_face()
            with BuildLine():
                CenterArc((22.5, 8.4487527048), 6.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a boat hull or marine vessel component with an elongated, tapered hull shape featuring internal compartmentalized structures, multiple rectangular openings or ports, and curved sides designed for water displacement.
def model_52783_2a26d5d9_0001():
    """Model: Grounded"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 250000, perimeter: 2000
            with BuildLine():
                Line((-250, 250), (250, 250))
                Line((-250, -250), (-250, 250))
                Line((250, -250), (-250, -250))
                Line((250, 250), (250, -250))
            make_face()
        # OneSide extrude, distance=-150
        extrude(amount=-150)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 16 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 40000, perimeter: 1000
            with BuildLine():
                Line((-50, -100), (-200, -100))
                Line((-200, -200), (-200, -100))
                Line((200, -200), (-200, -200))
                Line((200, -100), (200, -200))
                Line((200, -100), (50, -100))
                Line((50, -100), (-50, -100))
            make_face()
            # Profile area: 40000, perimeter: 1000
            with BuildLine():
                Line((-50, 100), (50, 100))
                Line((50, 100), (200, 100))
                Line((200, 200), (200, 100))
                Line((-200, 200), (200, 200))
                Line((-200, 100), (-200, 200))
                Line((-200, 100), (-50, 100))
            make_face()
        # OneSide extrude, distance=-100
        extrude(amount=-100, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 16 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 20000, perimeter: 600
            with BuildLine():
                Line((50, -100), (-50, -100))
                Line((50, 100), (50, -100))
                Line((-50, 100), (50, 100))
                Line((-50, -100), (-50, 100))
            make_face()
        # OneSide extrude, distance=-50
        extrude(amount=-50, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 34 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4980.0241022199, perimeter: 267.502234278
            with BuildLine():
                Line((-200, 100), (-200, 168.3012701892))
                Line((-131.6987298108, 100), (-200, 100))
                CenterArc((-175, 125), 50, -30, 150)
            make_face()
            # Profile area: 2873.9575317546, perimeter: 319.8621118378
            with BuildLine():
                CenterArc((-175, 125), 50, 120, 0.9637565321)
                CenterArc((-175, 125), 50, 120.9637565321, 180)
                CenterArc((-175, 125), 50, -59.0362434679, 29.0362434679)
                Line((-131.6987298108, 100), (-200, 100))
                Line((-200, 100), (-200, 168.3012701892))
            make_face()
            # Profile area: 4920.2835675197, perimeter: 275.1950144698
            with BuildLine():
                Line((200, 198.9897948557), (200, 101.0102051443))
                CenterArc((190, 150), 50, 78.4630409672, 11.5369590328)
                CenterArc((190, 150), 50, 90, 149.0362434679)
                CenterArc((190, 150), 50, -120.9637565321, 30.9637565321)
                CenterArc((190, 150), 50, -90, 11.5369590328)
            make_face()
            # Profile area: 2933.6980664548, perimeter: 234.9234303118
            with BuildLine():
                CenterArc((190, 150), 50, 59.0362434679, 19.4267974993)
                Line((200, 198.9897948557), (200, 101.0102051443))
                CenterArc((190, 150), 50, -78.4630409672, 137.4992844351)
            make_face()
            # Profile area: 4980.0241022199, perimeter: 267.502234278
            with BuildLine():
                CenterArc((175, -125), 50, 150, 150)
                Line((200, -100), (200, -168.3012701892))
                Line((131.6987298108, -100), (200, -100))
            make_face()
            # Profile area: 2873.9575317546, perimeter: 319.8621118378
            with BuildLine():
                Line((131.6987298108, -100), (200, -100))
                Line((200, -100), (200, -168.3012701892))
                CenterArc((175, -125), 50, -60, 0.9637565321)
                CenterArc((175, -125), 50, -59.0362434679, 180)
                CenterArc((175, -125), 50, 120.9637565321, 29.0362434679)
            make_face()
            # Profile area: 2873.9575317546, perimeter: 319.8621118378
            with BuildLine():
                CenterArc((-175, -125), 50, 30, 29.0362434679)
                CenterArc((-175, -125), 50, 59.0362434679, 180)
                CenterArc((-175, -125), 50, -120.9637565321, 0.9637565321)
                Line((-200, -168.3012701892), (-200, -100))
                Line((-200, -100), (-131.6987298108, -100))
            make_face()
            # Profile area: 4980.0241022199, perimeter: 267.502234278
            with BuildLine():
                Line((-200, -100), (-131.6987298108, -100))
                Line((-200, -168.3012701892), (-200, -100))
                CenterArc((-175, -125), 50, -120, 150)
            make_face()
        # OneSide extrude, distance=-120
        extrude(amount=-120, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical capsule or rounded rectangular tube with hemispherical end caps, featuring a central rectangular slot or window running along its length and circular openings on the curved side surfaces.
def model_52866_a4bc0a26_0003():
    """Model: Main Cyl"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 4.859651136, perimeter: 8.6393797974
            with BuildLine():
                CenterArc((0, 5.9000000879), 1.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 5.9000000879), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3.3
        extrude(amount=3.3)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(3.3, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.233655962, perimeter: 2.6703537836
            with BuildLine():
                CenterArc((0, 5.9000000879), 0.3000000045, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 5.9000000879), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.3685562913, perimeter: 6.4402649679
            with BuildLine():
                CenterArc((0, 5.9000000879), 0.725, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 5.9000000879), 0.3000000045, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-2.4
        extrude(amount=-2.4, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(3.3, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.4869468613, perimeter: 9.7389372261
            with BuildLine():
                CenterArc((0, 5.9000000879), 0.825, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 5.9000000879), 0.725, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-2.05
        extrude(amount=-2.05, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(3.3, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.233655962, perimeter: 2.6703537836
            with BuildLine():
                CenterArc((0, 5.9000000879), 0.3000000045, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 5.9000000879), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-3.2
        extrude(amount=-3.2, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical housing or bracket assembly featuring a large circular opening on one side, a rectangular slot on the top, and a vertical rectangular flange or mounting ear, with an overall compact, box-like shape designed to contain or mount internal components.
def model_52879_de812eb3_0000():
    """Model: fork v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 22.4601667134, perimeter: 24.1473342574
            with BuildLine():
                Line((-1.8, 2.85), (-3.4, 2.85))
                Line((-3.4, 2.85), (-3.4, -2.85))
                Line((-3.4, -2.85), (-1.8, -2.85))
                Line((-1.8, -2.85), (0.7275105345, -1.8629891095))
                CenterArc((0, 0), 2, -68.6690002146, 137.3380004293)
                Line((-1.8, 2.85), (0.7275105345, 1.8629891095))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=8.4
        extrude(amount=8.4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-3.4, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 25.5175863288, perimeter: 17.9070781255
            with BuildLine():
                CenterArc((0, 4.2), 2.85, -0.0000012303, 180.0000012303)
                CenterArc((0, 4.2), 2.85, 180, 179.9999987697)
            make_face()
        # OneSide extrude, distance=3.8
        extrude(amount=3.8, mode=Mode.ADD)
    return part.part


# Description: This appears to be a small fastener or mechanical connector with a compact, roughly cylindrical or block-like shape and what looks like a slotted or recessed feature on top for tool engagement.
def model_52974_259cdd82_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0235619449, perimeter: 0.9424777961
            with BuildLine():
                CenterArc((0, 0), 0.1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.05, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch9 -> Extrude3 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0050265482, perimeter: 0.2513274123
            with Locations((3.4000000507, 0.6000000089)):
                Circle(0.04)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)
    return part.part


# Description: This is a tapered cylindrical sleeve or cone-shaped tube with a rounded top end and a flared or angled base, featuring a hollow interior and smooth curved surfaces.
def model_53078_b592f2bd_0000():
    """Model: cover mangler"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 11.0323648175, perimeter: 57.1804663934
            with BuildLine():
                Line((93.6319999945, 2.3000000343), (91.8761372006, 13.274142496))
                Line((93.6319999945, 2.3000000343), (94.0319999945, 2.3000000343))
                Line((94.0319999945, 2.3000000343), (92.2711140912, 13.3055369301))
                CenterArc((90.0000006378, 12.9421587776), 2.3, 9.0902769208, 161.8194461583)
                Line((85.968001281, 2.3000000343), (87.7288871844, 13.3055369301))
                Line((85.968001281, 2.3000000343), (86.3680000055, 2.3000000343))
                Line((88.1238627994, 13.274142496), (86.3680000055, 2.3000000343))
                CenterArc((90, 12.9739605439), 1.9, 9.0902769208, 161.8194461584)
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 64.9817289943, perimeter: 34.8575836542
            with BuildLine():
                Line((91.8761372006, 13.274142496), (93.6319999945, 2.3000000343))
                CenterArc((90, 12.9739605439), 1.9, 9.0902769208, 161.8194461584)
                Line((86.3680000055, 2.3000000343), (88.1238627994, 13.274142496))
                Line((93.6319999945, 2.3000000343), (86.3680000055, 2.3000000343))
            make_face()
            # Profile area: 11.0323648175, perimeter: 57.1804663934
            with BuildLine():
                CenterArc((90.0000006378, 12.9421587776), 2.3, 9.0902769208, 161.8194461583)
                Line((87.7288871844, 13.3055369301), (85.968001281, 2.3000000343))
                Line((86.3680000055, 2.3000000343), (85.968001281, 2.3000000343))
                Line((86.3680000055, 2.3000000343), (88.1238627994, 13.274142496))
                CenterArc((90, 12.9739605439), 1.9, 9.0902769208, 161.8194461584)
                Line((91.8761372006, 13.274142496), (93.6319999945, 2.3000000343))
                Line((94.0319999945, 2.3000000343), (93.6319999945, 2.3000000343))
                Line((94.0319999945, 2.3000000343), (92.2711140912, 13.3055369301))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((90.0000013411, 4.5000000671)):
                Circle(0.6)
        # OneSide extrude, distance=-5
        extrude(amount=-5, mode=Mode.SUBTRACT)
    return part.part


# Description: A circular brake rotor with a solid front face, ventilated cooling fins visible through curved slots on the back surface, and a central hub for wheel mounting.
def model_53119_aabd4fc1_0023():
    """Model: Circle"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1963.4954084936, perimeter: 157.0796326795
            Circle(25)
        # OneSide extrude, distance=10
        extrude(amount=10)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 1354.8118318606, perimeter: 361.2831551628
            with BuildLine():
                CenterArc((0, 0), 32.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1963.4954084936, perimeter: 157.0796326795
            Circle(25)
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 10), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            Circle(2.5)
        # OneSide extrude, distance=-100
        extrude(amount=-100, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a metal wrench or spanner with a wavy, undulating S-shaped profile featuring two open jaw openings at opposite ends for gripping fasteners of different sizes.
def model_53216_2857e8ac_0003():
    """Model: handle"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 33 constraints, 13 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 7.8699694517, perimeter: 47.9652156888
            with BuildLine():
                CenterArc((54, 0), 1.6, -152.6919765647, 125.3838678256)
                CenterArc((56.100000836, -1.6000000238), 1.1000000164, 47.4333666158, 80.6386842071)
                CenterArc((56.100000836, -1.6000000238), 1.1000000164, 47.3744729224, 0.0588936934)
                CenterArc((56.100000836, -1.2000000179), 0.8500000179, 28.6191511605, 0.1719542831)
                CenterArc((58, 0), 1.4, -145.5052749173, 87.8976828333)
                Line((58.7500008754, -1.1821584863), (58.7500008754, -0.804673031))
                CenterArc((58, 0), 1.1, 47.014051585, 265.9718968301)
                Line((58.7500008754, 0.804673031), (58.7500008754, 1.1821584863))
                CenterArc((58, 0), 1.4, 57.607592084, 87.8976828333)
                CenterArc((56.100000836, 1.2000000179), 0.8500000179, -28.7911054436, 0.1719542831)
                CenterArc((56.100000836, 1.6000000238), 1.1000000164, -47.4333666158, 0.0588936934)
                CenterArc((56.100000836, 1.6000000238), 1.1000000164, -128.0720508229, 80.6386842071)
                CenterArc((54, 0), 1.6, 27.3081087392, 36.7474639832)
                Line((54.6999986818, 1.4387500983), (54.6999983508, 1.8000006413))
                Line((54.6999983508, 1.8000006413), (53.2999983508, 1.7999993587))
                Line((53.2999983508, 1.7999993587), (53.2999986818, 1.4387488156))
                CenterArc((54, 0), 1.6, 115.9445322671, 36.7474442977)
                CenterArc((51.9000007734, 1.6000000238), 1.1000000164, -132.5669390324, 80.6388110666)
                CenterArc((51.9000007734, 1.6000000238), 1.1000000164, -132.6255270776, 0.0585880452)
                CenterArc((51.9000007734, 1.2000000179), 0.8500000179, -151.3799753514, 0.171080795)
                CenterArc((50, 0), 1.4, 34.4941602364, 87.8981696804)
                Line((49.2500007339, 0.804674531), (49.2500007339, 1.1821595074))
                CenterArc((50, 0), 1.1, -132.9858338251, 265.9716676501)
                Line((49.2500007339, -1.1821595074), (49.2500007339, -0.804674531))
                CenterArc((50, 0), 1.4, -122.3923299167, 87.8981696804)
                CenterArc((51.9000007734, -1.2000000179), 0.8500000179, 151.2088945564, 0.171080795)
                CenterArc((51.9000007734, -1.6000000238), 1.1000000164, 132.5669390324, 0.0585880452)
                CenterArc((51.9000007734, -1.6000000238), 1.1000000164, 51.9281279658, 80.6388110666)
            make_face()
            with BuildLine():
                Line((55.750000836, -0.35), (55.750000836, 0.35))
                Line((55.750000836, 0.35), (56.450000836, 0.35))
                Line((56.450000836, 0.35), (56.450000836, -0.35))
                Line((56.450000836, -0.35), (55.750000836, -0.35))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((51.5500007734, -0.35), (52.2500007734, -0.35))
                Line((51.5500007734, 0.35), (51.5500007734, -0.35))
                Line((52.2500007734, 0.35), (51.5500007734, 0.35))
                Line((52.2500007734, -0.35), (52.2500007734, 0.35))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((54, 0), 1.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-1
        extrude(amount=-1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.0000016491, 1.7999505249, 0), x_dir=(0, 0, 1), z_dir=(-0.0000009162, 1, 0))):
            # Profile area: 0.4417864669, perimeter: 2.3561944902
            with Locations((-0.5000000075, 54.0000008047)):
                Circle(0.375)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.0000014657, 1.5999505249, 0), x_dir=(0, 0, 1), z_dir=(-0.0000009161, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-0.5000000075, 54.0000008045)):
                Circle(0.2)
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a hose clamp (or band clamp) with a curved, circular band design featuring a tightening mechanism with a screw or lever component on one side, used to secure hoses or tubing.
def model_53216_2857e8ac_0004():
    """Model: clamp top"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 24 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.1370062285, perimeter: 22.1579244319
            with BuildLine():
                CenterArc((-49.15, 2.1369741957), 0.2, 0, 90)
                Line((-49.55, 2.3369741957), (-49.15, 2.3369741957))
                CenterArc((-49.55, 2.1369741957), 0.2, 90, 90)
                Line((-49.75, 2.1369741957), (-49.75, 1.6393596311))
                CenterArc((-49.55, 1.6393596311), 0.2, -180, 74.650522983)
                CenterArc((-50, 0), 1.5, 105.349477017, 329.301045966)
                CenterArc((-50.45, 1.6393596311), 0.2, -74.650522983, 74.650522983)
                Line((-50.25, 2.1369741957), (-50.25, 1.6393596311))
                CenterArc((-50.45, 2.1369741957), 0.2, 0, 90)
                Line((-50.85, 2.3369741957), (-50.45, 2.3369741957))
                CenterArc((-50.85, 2.1369741957), 0.2, 90, 90)
                Line((-51.05, 1.5612494996), (-51.05, 2.1369741957))
                CenterArc((-51.55, 1.5612494996), 0.5, -45.2071662976, 45.2071662976)
                CenterArc((-50, 0), 1.7, 134.7928337024, 270.4143325953)
                CenterArc((-48.45, 1.5612494996), 0.5, -180, 45.2071662976)
                Line((-48.95, 2.1369741957), (-48.95, 1.5612494996))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 51.05), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0015253646, perimeter: 0.3523375439
            with BuildLine():
                Line((0.8374404298, 2.1369741957), (0.6625595925, 2.1369741957))
                CenterArc((0.7500000112, 1.8500000276), 0.3, 73.0541327765, 33.8917344471)
            make_face()
            # Profile area: 0.2799926399, perimeter: 1.8803142383
            with BuildLine():
                CenterArc((0.7500000112, 1.8500000276), 0.3, 106.9458672235, 147.3139559518)
                Line((0.6686173804, 1.5612494996), (0.831382642, 1.5612494996))
                CenterArc((0.7500000112, 1.8500000276), 0.3, -74.2598231753, 147.3139559518)
                Line((0.8374404298, 2.1369741957), (0.6625595925, 2.1369741957))
            make_face()
            # Profile area: 0.0012253343, perimeter: 0.3275960079
            with BuildLine():
                CenterArc((0.7500000112, 1.8500000276), 0.3, -105.7401768247, 31.4803536493)
                Line((0.6686173804, 1.5612494996), (0.831382642, 1.5612494996))
            make_face()
        # Symmetric extrude, each_side=2.8
        extrude(amount=2.8, both=True, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.2689168216, perimeter: 2.4698670709
            with BuildLine():
                CenterArc((48.5000007227, 2.0000000298), 0.8, -62.3928633576, 87.3043536984)
                Line((49.2255683705, 2.3369741957), (49.15, 2.3369741957))
                CenterArc((49.15, 2.1369741957), 0.2, 90, 90)
                Line((48.95, 2.1369741957), (48.95, 1.5612494996))
                CenterArc((48.45, 1.5612494996), 0.5, -32.7062644368, 32.7062644368)
            make_face()
            # Profile area: 1.7417024767, perimeter: 5.0584178392
            with BuildLine():
                CenterArc((48.45, 1.5612494996), 0.5, -32.7062644368, 32.7062644368)
                Line((48.95, 2.1369741957), (48.95, 1.5612494996))
                CenterArc((49.15, 2.1369741957), 0.2, 90, 90)
                Line((49.2255683705, 2.3369741957), (49.15, 2.3369741957))
                CenterArc((48.5000007227, 2.0000000298), 0.8, 24.9114903408, 272.6956463016)
            make_face()
        # OneSide extrude, distance=-2.3
        extrude(amount=-2.3, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a rectangular tray or bin with sloped side walls, featuring a trapezoidal top opening and a dark metallic finish with blue surface details or reflections.
def model_53216_2857e8ac_0011():
    """Model: bracket"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 8 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4.8, perimeter: 24
            with BuildLine():
                Line((-41.7, 6.7), (-38.3, 6.7))
                Line((-41.7, 3.3), (-41.7, 6.7))
                Line((-38.3, 3.3), (-41.7, 3.3))
                Line((-38.3, 6.7), (-38.3, 3.3))
            make_face()
            with BuildLine():
                Line((-41.3, 3.7), (-38.7, 3.7))
                Line((-41.3, 6.3), (-41.3, 3.7))
                Line((-38.7, 6.3), (-41.3, 6.3))
                Line((-38.7, 3.7), (-38.7, 6.3))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=18
        extrude(amount=18)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 41.7), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 7.7540509028, perimeter: 17.0382476373
            with BuildLine():
                Line((0, 6.7), (0, 3.3))
                Line((-1, 7), (0, 6.7))
                Line((-1, 2.5), (-1, 7))
                Line((2.9808023382, 1.5370989029), (-1, 2.5))
                Line((1.9629909152, 3.3), (2.9808023382, 1.5370989029))
                Line((0, 3.3), (1.9629909152, 3.3))
            make_face()
            # Profile area: 3.3370845559, perimeter: 9.2889727457
            with BuildLine():
                Line((0, 3.3), (1.9629909152, 3.3))
                Line((0, 6.7), (1.9629909152, 3.3))
                Line((0, 6.7), (0, 3.3))
            make_face()
        # OneSide extrude, distance=-7
        extrude(amount=-7, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 38.3), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-2.6547005384, 4.1019237886)):
                Circle(0.3)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-1.6547005384, 5.8339745962)):
                Circle(0.3)
        # OneSide extrude, distance=-5
        extrude(amount=-5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a rectangular tray or shallow box with an open top, featuring a flat base, vertical side walls, and an angled or hinged lid/cover element on one end.
def model_53458_1aff9fae_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 36.2569562246, perimeter: 51.9901880796
            with BuildLine():
                Line((-0.5750383839, 6.4605419493), (-2.0750383839, 6.4605419493))
                Line((-2.0750383839, 6.4605419493), (0, 0))
                Line((0, 0), (19, 0))
                Line((19, 0), (19, 1.5))
                Line((19, 1.5), (1, 1.5))
                Line((1, 1.5), (-0.5750383839, 6.4605419493))
            make_face()
        # OneSide extrude, distance=15
        extrude(amount=15)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 240.0915072973, perimeter: 62.1958283687
            with BuildLine():
                Line((-18.5798037916, 14.6410660867), (-18.5798037916, 0.3877012749))
                Line((-18.5798037916, 0.3877012749), (-1.735254419, 0.3877012749))
                Line((-1.735254419, 0.3877012749), (-1.735254419, 14.6410660867))
                Line((-1.735254419, 14.6410660867), (-18.5798037916, 14.6410660867))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch6 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(1.3410703911, 0.4258077773, 0), x_dir=(0, 0, -1), z_dir=(0.9531096838, 0.3026250662, 0))):
            # Profile area: 71.069481847, perimeter: 38.2931709379
            with BuildLine():
                Line((-0.4672909323, 1.1777543337), (-0.4672909323, 6.2146992053))
                Line((-0.4672909323, 6.2146992053), (-14.5769315297, 6.2146992053))
                Line((-14.5769315297, 6.2146992053), (-14.5769315297, 1.1777543337))
                Line((-14.5769315297, 1.1777543337), (-0.4672909323, 1.1777543337))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


# Description: This is a rectangular base plate with two parallel vertical flanges positioned at opposite ends, featuring internal ribbing or cross-bracing between the flanges for structural reinforcement.
def model_53470_39f2e9dc_0002():
    """Model: board"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11200, perimeter: 460
            with BuildLine():
                Line((-320, 15), (-320, 85))
                Line((-320, 85), (-480, 85))
                Line((-480, 85), (-480, 15))
                Line((-480, 15), (-320, 15))
            make_face()
        # OneSide extrude, distance=-4
        extrude(amount=-4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 552, perimeter: 154
            with BuildLine():
                Line((340.5, -84.5), (348.5, -84.5))
                Line((348.5, -15.5), (348.5, -84.5))
                Line((340.5, -15.5), (348.5, -15.5))
                Line((340.5, -84.5), (340.5, -15.5))
            make_face()
            # Profile area: 552, perimeter: 154
            with BuildLine():
                Line((451.5, -84.5), (459.5, -84.5))
                Line((459.5, -84.5), (459.5, -15.5))
                Line((451.5, -15.5), (459.5, -15.5))
                Line((451.5, -15.5), (451.5, -84.5))
            make_face()
        # OneSide extrude, distance=10
        extrude(amount=10, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 45.45, perimeter: 102.8
            with BuildLine():
                Line((375, -61.7), (375, -62.6))
                Line((375, -62.6), (425.5, -62.6))
                Line((425.5, -62.6), (425.5, -61.7))
                Line((425.5, -61.7), (375, -61.7))
            make_face()
        # OneSide extrude, distance=-10
        extrude(amount=-10, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a truck cab assembly featuring a rounded rectangular cabin with windowed upper section mounted on a cylindrical horizontal base frame, with visible structural ribbing and support elements.
def model_53595_51bad85d_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 9 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4.8859795423, perimeter: 7.844769498
            with BuildLine():
                CenterArc((5.4422330611, 4.5279738709), 1.25, 135.1884179382, 181.1144917928)
                Line((6.3459858499, 3.6644167525), (6.6671706236, 4.2789197241))
                CenterArc((5.4422330611, 4.5279738709), 1.25, -11.4927137928, 146.681131731)
            make_face()
            # Profile area: 7.0651766393, perimeter: 9.4236393962
            with BuildLine():
                CenterArc((-5.1686968336, 2.2227101407), 1.5, -111.8028178071, 168.8000609918)
                CenterArc((-5.1686968336, 2.2227101407), 1.5, 56.9972431846, 176.1197351619)
                Line((-6.0689716786, 1.0229163236), (-5.7258170807, 0.8300087978))
            make_face()
            # Profile area: 38.4096621853, perimeter: 37.0318759106
            with BuildLine():
                CenterArc((1.3560414213, -0.0537361122), 2.7, -119.3429197303, 91.7480176993)
                Line((3.7489023762, -1.304422504), (6.3459858499, 3.6644167525))
                CenterArc((5.4422330611, 4.5279738709), 1.25, 135.1884179382, 181.1144917928)
                Line((1.3134706001, 2.1455758058), (4.5554477065, 5.4089459107))
                CenterArc((0.2729625084, 1.7887244206), 1.1, -123.0027568154, 141.9326118843)
                Line((-4.3516777524, 3.4806766828), (-0.3261848178, 0.866215623))
                CenterArc((-5.1686968336, 2.2227101407), 1.5, -111.8028178071, 168.8000609918)
                Line((-5.7258170807, 0.8300087978), (0.0329453734, -2.4073326894))
            make_face()
        # OneSide extrude, distance=6
        extrude(amount=6)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(6, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.5824987231, perimeter: 4.4594019163
            with Locations((-5.1564831584, 2.5554772953)):
                Circle(0.7097358582)
            # Profile area: 1.256104448, perimeter: 3.9729930812
            with Locations((-2.6539638537, 0.7329035953)):
                Circle(0.6323214877)
            # Profile area: 1.746324714, perimeter: 4.6845451827
            with Locations((1.1027696911, -1.2384516311)):
                Circle(0.745568522)
            # Profile area: 0.8375391392, perimeter: 3.2441990116
            with Locations((5.4422330611, 4.5279738709)):
                Circle(0.5163303091)
            # Profile area: 1.0358535257, perimeter: 3.6078967981
            with Locations((3.4460787339, 2.3598459979)):
                Circle(0.5742146096)
        # OneSide extrude, distance=-18
        extrude(amount=-18, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(6, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 9.3022356953, perimeter: 73.5001073175
            with BuildLine():
                Line((-0.3261848178, 0.866215623), (-4.3516777524, 3.4806766828))
                CenterArc((-5.1686968336, 2.2227101407), 1.5, 56.9972431846, 176.1197351619)
                Line((-6.0689716786, 1.0229163236), (0.0329453734, -2.4073326894))
                CenterArc((1.3560414213, -0.0537361122), 2.7, -119.3429197303, 91.7480176993)
                Line((3.7489023762, -1.304422504), (6.6671706236, 4.2789197241))
                CenterArc((5.4422330611, 4.5279738709), 1.25, -11.4927137928, 146.681131731)
                Line((4.5554477065, 5.4089459107), (1.3134706001, 2.1455758058))
                CenterArc((0.2729625084, 1.7887244206), 1.1, -123.0027568154, 141.9326118843)
            make_face()
            with BuildLine():
                CenterArc((0.2729625084, 1.7887244206), 1.3531274, -123.0027568154, 135.0483585947)
                Line((4.7350234748, 5.23054735), (1.5962964974, 2.0711087586))
                CenterArc((5.4422330611, 4.5279738709), 0.9968725558, -9.5486687929, 144.7370867311)
                Line((3.5245694955, -1.1871695225), (6.4252939967, 4.3626073406))
                CenterArc((1.3560414213, -0.0537361122), 2.4468725558, -119.3429197303, 91.7480176993)
                Line((-5.929715857, 1.2350151844), (0.1569868256, -2.1866808797))
                CenterArc((-5.1686968336, 2.2227101407), 1.2468726, 56.9972431846, 175.3885031057)
                Line((-0.4640580949, 0.6539317563), (-4.4895510296, 3.268392816))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


# Description: This is a thin, elongated rectangular enclosure or cover with a tapered hexagonal cross-section, featuring a recessed central panel and raised perimeter flanges with what appears to be mounting holes at the corners.
def model_53614_f6a8f7e1_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch4 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 63.2622199666, perimeter: 32.147858136
            with BuildLine():
                CenterArc((0.508, -9.906), 0.508, -180, 90)
                Line((5.588, -10.414), (0.508, -10.414))
                CenterArc((5.588, -9.906), 0.508, -90, 90)
                Line((6.096, -0.508), (6.096, -9.906))
                CenterArc((5.588, -0.508), 0.508, 0, 90)
                Line((0.508, 0), (5.588, 0))
                CenterArc((0.508, -0.508), 0.508, 90, 90)
                Line((0, -9.906), (0, -0.508))
            make_face()
        # OneSide extrude, distance=0.508
        extrude(amount=0.508)

        # Sketch6 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 10.414), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.16129, perimeter: 2.794
            with BuildLine():
                Line((3.6830000973, 0.1905000081), (2.4130000973, 0.1905000081))
                Line((3.6830000973, 0.3175000081), (3.6830000973, 0.1905000081))
                Line((2.4130000973, 0.3175000081), (3.6830000973, 0.3175000081))
                Line((2.4130000973, 0.1905000081), (2.4130000973, 0.3175000081))
            make_face()
        # OneSide extrude, distance=-0.127
        extrude(amount=-0.127, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0722824303, perimeter: 1.7680001432
            with BuildLine():
                Line((-4.5570003537, 0.254), (-5.3498302647, 0.254))
                Line((-4.5570003537, 0.3451701606), (-4.5570003537, 0.254))
                Line((-5.3498302647, 0.3451701606), (-4.5570003537, 0.3451701606))
                Line((-5.3498302647, 0.254), (-5.3498302647, 0.3451701606))
            make_face()
            # Profile area: 0.012667687, perimeter: 0.398982267
            with Locations((-1.7167525407, 0.1905000081)):
                Circle(0.0635)
        # OneSide extrude, distance=-1.27
        extrude(amount=-1.27, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a rectangular enclosure or housing with rounded corners, featuring a dark blue central panel, black corner reinforcements, two circular mounting holes at the top, and four small circular feet or mounting points at the bottom.
def model_53627_7b1adb8e_0003():
    """Model: pcb"""
    with BuildPart() as part:
        # board_outline -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 2.3639689916, perimeter: 5.913929068
            with BuildLine():
                CenterArc((0.254, 1.651), 0.254, 90, 90)
                Line((0, 0.254), (0, 1.651))
                CenterArc((0.254, 0.254), 0.254, 180, 90)
                Line((1.016, 0), (0.254, 0))
                CenterArc((1.016, 0.254), 0.254, -90, 90)
                Line((1.27, 1.651), (1.27, 0.254))
                CenterArc((1.016, 1.651), 0.254, 0, 90)
                Line((0.254, 1.905), (1.016, 1.905))
            make_face()
        # OneSide extrude, distance=0.16
        extrude(amount=0.16)

        # Drills - pads -> Extrude2 (Cut)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            with Locations((0.254, 1.651)):
                Circle(0.125)
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((0.508, 0.1905)):
                Circle(0.05)
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((0.254, 0.1905)):
                Circle(0.05)
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((0.762, 0.1905)):
                Circle(0.05)
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            with Locations((1.016, 1.651)):
                Circle(0.125)
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((1.016, 0.1905)):
                Circle(0.05)
        # OneSide extrude, distance=0.16
        extrude(amount=0.16, mode=Mode.SUBTRACT)

        # Drills - vias -> Extrude3 (Cut)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0019634954, perimeter: 0.1570796327
            with Locations((0.889, 0.4826)):
                Circle(0.025)
        # OneSide extrude, distance=0.16
        extrude(amount=0.16, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a dual-chambered connector or junction box with two cubic/rectangular housings connected by a central bridge or crossbar, featuring angled top panels and internal ribbed structural elements for reinforcement.
def model_53702_02f39181_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6, perimeter: 14
            with BuildLine():
                Line((-4, -3.5), (-5, -3.5))
                Line((-4, 2.5), (-4, -3.5))
                Line((-5, 2.5), (-4, 2.5))
                Line((-5, -3.5), (-5, 2.5))
            make_face()
            # Profile area: 6, perimeter: 14
            with BuildLine():
                Line((4, 2.5), (3, 2.5))
                Line((3, 2.5), (3, -3.5))
                Line((3, -3.5), (4, -3.5))
                Line((4, -3.5), (4, 2.5))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 10 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 26.4292036732, perimeter: 23.1415926536
            with BuildLine():
                CenterArc((-1, 0), 1, 90, 180)
                Line((-1, 4), (-1, 1))
                Line((-5, 4), (-1, 4))
                Line((-5, -3), (-5, 4))
                Line((-1, -3), (-5, -3))
                Line((-1, -1), (-1, -3))
            make_face()
            # Profile area: 1.5707963268, perimeter: 5.1415926536
            with BuildLine():
                CenterArc((1, 0), 1, 90, 180)
                Line((1, -1), (1, 1))
            make_face()
            # Profile area: 27.4292036732, perimeter: 39.1415926536
            with BuildLine():
                CenterArc((1, 0), 1, -90, 180)
                Line((1, -3), (1, -1))
                Line((6, -3), (1, -3))
                Line((6, 4), (6, -3))
                Line((1, 4), (6, 4))
                Line((1, 1), (1, 4))
            make_face()
            with BuildLine():
                Line((4, -2.5), (5, -2.5))
                Line((4, 3.5), (4, -2.5))
                Line((5, 3.5), (4, 3.5))
                Line((5, -2.5), (5, 3.5))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.5707963268, perimeter: 5.1415926536
            with BuildLine():
                Line((1, -1), (1, 1))
                CenterArc((1, 0), 1, -90, 180)
            make_face()
            # Profile area: 6, perimeter: 14
            with BuildLine():
                Line((5, -2.5), (5, 3.5))
                Line((5, 3.5), (4, 3.5))
                Line((4, 3.5), (4, -2.5))
                Line((4, -2.5), (5, -2.5))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-1, 0)):
                Circle(0.5)
        # OneSide extrude, distance=5
        extrude(amount=5, mode=Mode.ADD)
    return part.part


# Description: This is a black polymer or composite bracket or mounting fixture with an angled top plate and multiple vertical cylindrical posts or standoffs extending downward, featuring a slotted or ribbed design on its sides.
def model_53706_7d9ee99b_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 16 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1, perimeter: 4
            with BuildLine():
                Line((0, -1), (-1, -1))
                Line((0, 0), (0, -1))
                Line((-1, 0), (0, 0))
                Line((-1, -1), (-1, 0))
            make_face()
            # Profile area: 1, perimeter: 4
            with BuildLine():
                Line((0, 1), (-1, 1))
                Line((0, 2), (0, 1))
                Line((-1, 2), (0, 2))
                Line((-1, 1), (-1, 2))
            make_face()
            # Profile area: 1, perimeter: 4
            with BuildLine():
                Line((2, 1), (1, 1))
                Line((2, 2), (2, 1))
                Line((1, 2), (2, 2))
                Line((1, 1), (1, 2))
            make_face()
            # Profile area: 1, perimeter: 4
            with BuildLine():
                Line((2, -1), (1, -1))
                Line((2, 0), (2, -1))
                Line((1, 0), (2, 0))
                Line((1, -1), (1, 0))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 24, perimeter: 24
            with BuildLine():
                Line((-3, 2), (2, 2))
                Line((-3, -3), (-3, 2))
                Line((2, -3), (-3, -3))
                Line((2, 2), (2, -3))
            make_face()
            with BuildLine():
                Line((0, 0), (1, 0))
                Line((0, 1), (0, 0))
                Line((1, 1), (0, 1))
                Line((1, 0), (1, 1))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1, perimeter: 4
            with BuildLine():
                Line((1, 0), (1, 1))
                Line((1, 1), (0, 1))
                Line((0, 1), (0, 0))
                Line((0, 0), (1, 0))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-2, -2)):
                Circle(0.5)
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((1, -2)):
                Circle(0.5)
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-2, 1)):
                Circle(0.5)
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((1, 1)):
                Circle(0.5)
        # OneSide extrude, distance=0.01
        extrude(amount=0.01, mode=Mode.ADD)
    return part.part


# Description: This is a centrifugal fan impeller featuring a circular disk with radial blades extending from a central hub, designed to move air or gas through rotational motion.
def model_53831_de0554da_0001():
    """Model: screw mounting"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((60, -140)):
                Circle(0.5)
        # OneSide extrude, distance=4
        extrude(amount=4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(4, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 49.480084294, perimeter: 28.2743338823
            with BuildLine():
                CenterArc((60, -140), 4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((60, -140), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((60, -140)):
                Circle(0.5)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(4.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 17.2572999142, perimeter: 18.3043589306
            with BuildLine():
                CenterArc((60, -140), 4, -75.5996692034, 151.1993384068)
                Line((60.9947819171, -143.8743269012), (60.9947819171, -136.1256730988))
            make_face()
            # Profile area: 17.2572999142, perimeter: 18.3043589306
            with BuildLine():
                CenterArc((60, -140), 4, 104.4003307966, 151.1993384068)
                Line((59.0052180829, -136.1256730988), (59.0052180829, -143.8743269012))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


# Description: This is a hexagonal or polygonal box-shaped enclosure with an angled top section, featuring a recessed or open cavity on one side and internal geometric divisions or mounting features visible through the translucent surfaces.
def model_53846_89405f98_0005():
    """Model: podstawa v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 36, perimeter: 24
            with BuildLine():
                Line((-3, 3), (3, 3))
                Line((-3, -3), (-3, 3))
                Line((3, -3), (-3, -3))
                Line((3, 3), (3, -3))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.857819147, perimeter: 15.1598918871
            with BuildLine():
                Line((2.6402295049, 2.3000000343), (-1.8000000268, 2.3000000343))
                Line((2.6402295049, -2.1402294974), (-1.8000000268, 2.3000000343))
                Line((2.6402295049, -2.1402294974), (2.6402295049, 2.3000000343))
            make_face()
        # OneSide extrude, distance=-1.8
        extrude(amount=-1.8, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((-2.0000000298, 2.7000000402)):
                Circle(0.1)
        # OneSide extrude, distance=-1.3
        extrude(amount=-1.3, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 18, perimeter: 20.4852813742
            with BuildLine():
                Line((-3, 3), (3, -3))
                Line((-3, -3), (-3, 3))
                Line((3, -3), (-3, -3))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)
    return part.part


# Description: A long, cylindrical rod or shaft with rounded ends and a slightly tapered or beveled edge profile, appearing to be a simple mechanical component used for alignment, support, or structural purposes.
def model_53927_ef5208b9_0001():
    """Model: rod narrow"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 19 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.2580033097, perimeter: 5.3278760042
            with BuildLine():
                CenterArc((33.8000004992, 0.3), 0.3, 90, 180)
                Line((33.8000004992, 0), (34.6750005037, 0))
                CenterArc((34.6750005037, 0.025), 0.025, -90, 89.9999897547)
                Line((34.7000005037, 0.0249999955), (34.7000005126, 0.074999997))
                CenterArc((34.6750005126, 0.0750000015), 0.025, -0.0000102453, 90.0000102453)
                Line((33.8000005007, 0.1000000015), (34.6750005126, 0.1000000015))
                CenterArc((33.8000005007, 0.3000000075), 0.2, 90, 180)
                Line((34.6750005171, 0.5000000075), (33.8000005007, 0.5000000075))
                CenterArc((34.6750005171, 0.5250000075), 0.025, -90, 90)
                Line((34.7000005171, 0.575), (34.7000005171, 0.5250000075))
                CenterArc((34.6750005171, 0.575), 0.025, 0, 90)
                Line((33.8000004992, 0.6), (34.6750005171, 0.6))
            make_face()
        # OneSide extrude, distance=-41
        extrude(amount=-41)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((-40.5, -34.2375005014)):
                Circle(0.4)
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((-0.5, -34.2375005014)):
                Circle(0.4)
            # Profile area: 3.2301928248, perimeter: 8.7081222859
            with BuildLine():
                Line((-0.1807343427, -34.6750005037), (0, -34.6750005037))
                CenterArc((-0.9527343952, -34.1000005081), 0.9626053584, -38.5581361794, 1.8787099887)
                Line((-0.5000000075, -35.6000005305), (-0.200000003, -34.7000005171))
                Line((1.4000000209, -34.8000005186), (-0.5000000075, -35.6000005305))
                Line((1.0000000149, -32.3000004813), (1.4000000209, -34.8000005186))
                Line((-0.200000003, -33.5000004992), (1.0000000149, -32.3000004813))
                CenterArc((-0.9527343952, -34.1000005081), 0.9626053584, 18.1589489531, 20.3991872264)
                Line((0, -33.8000004992), (-0.0380710306, -33.8000004992))
                Line((0, -33.9625005148), (0, -33.8000004992))
                CenterArc((-0.9527343952, -34.1000005081), 0.9626053584, -8.2123051448, 16.4246102896)
                Line((0, -34.6750005037), (0, -34.2375005014))
            make_face()
            # Profile area: 0.0301812342, perimeter: 1.0964999954
            with BuildLine():
                Line((0, -34.6750005037), (0, -34.2375005014))
                CenterArc((-0.9527343952, -34.1000005081), 0.9626053584, -36.6794261908, 28.467121046)
                Line((-0.1807343427, -34.6750005037), (0, -34.6750005037))
            make_face()
            # Profile area: 0.0026898838, perimeter: 0.3676809574
            with BuildLine():
                CenterArc((-0.9527343952, -34.1000005081), 0.9626053584, 8.2123051448, 9.9466438083)
                Line((0, -33.9625005148), (0, -33.8000004992))
                Line((0, -33.8000004992), (-0.0380710306, -33.8000004992))
            make_face()
            # Profile area: 3.1330229923, perimeter: 7.8317507372
            with BuildLine():
                Line((-41, -34.6750005037), (-40.8192661956, -34.6750005037))
                Line((-41, -34.2375005014), (-41, -34.6750005037))
                CenterArc((-40.0472633054, -34.1000005081), 0.9626076342, 171.7877144051, 16.4245711897)
                Line((-41, -33.8000004992), (-41, -33.9625005148))
                Line((-40.9619290651, -33.8000004992), (-41, -33.8000004992))
                CenterArc((-40.0472633054, -34.1000005081), 0.9626076342, 141.4419717956, 20.3991236811)
                Line((-40.800000608, -33.5000004992), (-41.6154573674, -32.6876050674))
                Line((-41.6154573674, -32.6876050674), (-42.7188138841, -34.4275134206))
                Line((-42.7188138841, -34.4275134206), (-42.7188138841, -35.5))
                Line((-42.7188138841, -35.5), (-40.800000608, -34.7000005171))
                CenterArc((-40.0472633054, -34.1000005081), 0.9626076342, -143.320674703, 1.8787029074)
            make_face()
            # Profile area: 0.0026898772, perimeter: 0.3676808388
            with BuildLine():
                Line((-40.9619290651, -33.8000004992), (-41, -33.8000004992))
                Line((-41, -33.8000004992), (-41, -33.9625005148))
                CenterArc((-40.0472633054, -34.1000005081), 0.9626076342, 161.8410954767, 9.9466189284)
            make_face()
            # Profile area: 0.0301811517, perimeter: 1.0964992211
            with BuildLine():
                CenterArc((-40.0472633054, -34.1000005081), 0.9626076342, -171.7877144051, 28.4670397021)
                Line((-41, -34.2375005014), (-41, -34.6750005037))
                Line((-41, -34.6750005037), (-40.8192661956, -34.6750005037))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3769911184, perimeter: 3.7699111843
            with BuildLine():
                CenterArc((40.5, -34.2375005014), 0.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((40.5, -34.2375005014), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.3769911184, perimeter: 3.7699111843
            with BuildLine():
                CenterArc((0.5, -34.2375005014), 0.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0.5, -34.2375005014), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.ADD)
    return part.part


# Description: This is a bracket or mounting component with a distinctive inverted V-shaped top featuring two vertical posts, a curved/swept base with internal ribbing for structural reinforcement, and a circular mounting hole on the side.
def model_53927_ef5208b9_0002():
    """Model: lower link"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 12 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 20.775197733, perimeter: 27.7398436499
            with BuildLine():
                Line((14.0325642318, 2.8937335425), (12.4838462501, 2.6523708872))
                CenterArc((12.5223432297, 2.4053527045), 0.25, 98.858103557, 131.141896443)
                Line((15, 0), (12.3616463273, 2.2138415937))
                Line((15, 0), (17.0635907227, 0))
                CenterArc((17.0635907227, 2.475), 2.475, -90, 20)
                Line((17.9100905775, 0.1492607636), (19.7477685195, 0.8181208346))
                CenterArc((19.6622634837, 1.0530439898), 0.25, -70, 135.2949410474)
                Line((18.7071735892, 1.7676260002), (19.766750306, 1.2801618094))
                CenterArc((19.0624287851, 2.5398265867), 0.85, 164.3161969658, 80.9787440816)
                Line((18.2440758116, 2.7696056345), (19.2220469805, 6.2526282248))
                CenterArc((18.9813549295, 6.3202102977), 0.25, -15.6838030342, 154.3838030342)
                Line((16.0932377433, 3.4115224131), (18.7935388961, 6.4852107147))
                CenterArc((15.4546632298, 3.9725238309), 0.85, -81.2536399117, 39.9536399117)
                Line((14.0325642318, 2.8937335425), (15.5839147371, 3.1324083342))
            make_face()
            with BuildLine():
                CenterArc((19.1749997726, 1.074999976), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((16.0317953614, 2.5), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.8
        extrude(amount=0.8, both=True)

        # Sketch1 -> Extrude3 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 12 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 20.775197733, perimeter: 27.7398436499
            with BuildLine():
                Line((14.0325642318, 2.8937335425), (12.4838462501, 2.6523708872))
                CenterArc((12.5223432297, 2.4053527045), 0.25, 98.858103557, 131.141896443)
                Line((15, 0), (12.3616463273, 2.2138415937))
                Line((15, 0), (17.0635907227, 0))
                CenterArc((17.0635907227, 2.475), 2.475, -90, 20)
                Line((17.9100905775, 0.1492607636), (19.7477685195, 0.8181208346))
                CenterArc((19.6622634837, 1.0530439898), 0.25, -70, 135.2949410474)
                Line((18.7071735892, 1.7676260002), (19.766750306, 1.2801618094))
                CenterArc((19.0624287851, 2.5398265867), 0.85, 164.3161969658, 80.9787440816)
                Line((18.2440758116, 2.7696056345), (19.2220469805, 6.2526282248))
                CenterArc((18.9813549295, 6.3202102977), 0.25, -15.6838030342, 154.3838030342)
                Line((16.0932377433, 3.4115224131), (18.7935388961, 6.4852107147))
                CenterArc((15.4546632298, 3.9725238309), 0.85, -81.2536399117, 39.9536399117)
                Line((14.0325642318, 2.8937335425), (15.5839147371, 3.1324083342))
            make_face()
            with BuildLine():
                CenterArc((19.1749997726, 1.074999976), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((16.0317953614, 2.5), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.7
        extrude(amount=0.7, both=True, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude4 (Join)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((18.6000002772, 5.6000000834)):
                Circle(0.4)
        # Symmetric extrude, each_side=1.6
        extrude(amount=1.6, both=True, mode=Mode.ADD)

        # Sketch2 -> Extrude5 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((18.6000002772, 5.6000000834)):
                Circle(0.4)
        # Symmetric extrude, each_side=0.7
        extrude(amount=0.7, both=True, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a gray and blue cast or forged bracket with a curved, clamping design featuring two opposing C-shaped arms, internal geometric cutouts, and triangular reinforcement features for securing or holding cylindrical components.
def model_54177_2b99e039_0002():
    """Model: hitch beam"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 28 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.3231747501, perimeter: 8.9561946824
            with BuildLine():
                Line((-1.5, 1), (-1.5, 1.05))
                CenterArc((-1.75, 1.05), 0.25, 0, 90)
                Line((-1.75, 1.3), (-2.75, 1.3))
                CenterArc((-2.75, 1.05), 0.25, 90, 90)
                Line((-3, 1.05), (-3, 0.6500000097))
                Line((-3.5000000522, 0.6500000097), (-3, 0.6500000097))
                Line((-3.5000000522, 0.6500000097), (-3.5000000522, 0.3500000052))
                Line((-3.5000000522, 0.3500000052), (-3, 0.3500000052))
                Line((-3, 0), (-3, 0.3500000052))
                Line((-3.0000000075, -0.0499999627), (-3, 0))
                CenterArc((-2.7500000075, -0.05), 0.25, 179.9999914623, 90.0000085377)
                Line((-1.75, -0.3), (-2.7500000075, -0.3))
                CenterArc((-1.75, -0.05), 0.25, -90, 90)
                Line((-1.5, 0), (-1.5, -0.05))
                Line((-1.5, 0), (-2.4500000402, 0))
                CenterArc((-2.4500000402, 0.25), 0.25, -180, 90)
                Line((-2.7000000402, 0.25), (-2.7000000402, 0.75))
                CenterArc((-2.4500000402, 0.75), 0.25, 90, 90)
                Line((-1.5, 1), (-2.4500000402, 1))
            make_face()
        # Symmetric extrude, each_side=0.4
        extrude(amount=0.4, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((0, 2.0500000305)):
                Circle(0.25)
        # OneSide extrude, distance=-1.8
        extrude(amount=-1.8, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1762941474, perimeter: 3.7516966606
            with BuildLine():
                CenterArc((0, 2.0500000305), 0.35, -58.9972905747, 297.9945811494)
                Line((-0.1802775129, 1.75), (0.1802775129, 1.75))
            make_face()
            with BuildLine():
                CenterArc((0, 2.0500000305), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0122014118, perimeter: 0.7393245754
            with BuildLine():
                Line((-0.1802775129, 1.75), (0.1802775129, 1.75))
                CenterArc((0, 2.0500000305), 0.35, -121.0027094253, 62.0054188506)
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a simple rounded rectangular bar or shaft with a uniform cylindrical profile and slightly rounded ends.
def model_54177_2b99e039_0009():
    """Model: clip horse"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-10, 0)):
                Circle(0.5)
        # OneSide extrude, distance=20
        extrude(amount=20)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((10, 0)):
                Circle(0.1)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.061575216, perimeter: 6.157521601
            with BuildLine():
                CenterArc((10, 0), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((10, 0), 0.48, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a long, narrow hexagonal or prismatic beam with angled end faces and internal slot features, characterized by a tapered geometry that narrows toward one end.
def model_54177_2b99e039_0010():
    """Model: beam rotation"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.1025, perimeter: 5.8
            with BuildLine():
                Line((-6.45, 1.45), (-5, 1.45))
                Line((-6.45, 0), (-6.45, 1.45))
                Line((-5, 0), (-6.45, 0))
                Line((-5, 1.45), (-5, 0))
            make_face()
        # OneSide extrude, distance=11
        extrude(amount=11)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.45, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-5.500000082, 5.7500000857)):
                Circle(0.25)
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.45, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3063052837, perimeter: 4.0840704497
            with BuildLine():
                CenterArc((-5.500000082, 5.7500000857), 0.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-5.500000082, 5.7500000857), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a flat parallelogram-shaped plate or panel with a beveled or angled edge along one side, featuring a thin dark edge that suggests material thickness or a chamfered detail.
def model_54273_21c2b38f_0015():
    """Model: gladki-bialy ROG v2 (2)"""
    with BuildPart() as part:
        # Sketch7 -> Extrude1 (NewBody)
        # Sketch on Plane1 construction plane
        with BuildSketch(Plane(origin=(0, 1.15, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3984, perimeter: 13.28
            with BuildLine():
                Line((-0.86, -0.86), (0.86, -0.86))
                Line((0.86, -0.86), (0.86, 0.86))
                Line((0.86, 0.86), (-0.86, 0.86))
                Line((-0.86, 0.86), (-0.86, -0.86))
            make_face()
            with BuildLine():
                Line((0.8, 0.8), (0.8, -0.8))
                Line((0.8, -0.8), (-0.8, -0.8))
                Line((-0.8, -0.8), (-0.8, 0.8))
                Line((-0.8, 0.8), (0.8, 0.8))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 2.56, perimeter: 6.4
            with BuildLine():
                Line((-0.8, 0.8), (0.8, 0.8))
                Line((-0.8, -0.8), (-0.8, 0.8))
                Line((0.8, -0.8), (-0.8, -0.8))
                Line((0.8, 0.8), (0.8, -0.8))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a cylindrical connector or adapter with a tapered stem, featuring a textured grip band around the middle section and a slender shaft extending from one end.
def model_54360_db08c779_0000():
    """Model: main assembly part"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1.3250374823, 0.0488862321, -1.4525910371), x_dir=(-0.9998407062, -0.017848313, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            with Locations((2, 6)):
                Circle(0.125)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)

        # Sketch6 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -1.4525910371), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1472621556, perimeter: 2.3561944902
            with BuildLine():
                CenterArc((-0.7817338081, 6.0122338431), 0.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-0.7817338081, 6.0122338431), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            with Locations((-0.7817338081, 6.0122338431)):
                Circle(0.125)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch7 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.9525910371), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.5890486225, perimeter: 4.7123889804
            with BuildLine():
                CenterArc((-0.7817338081, 6.0122338431), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-0.7817338081, 6.0122338431), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-0.7817338081, 6.0122338431)):
                Circle(0.25)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


# Description: This is a metal bracket or support structure featuring two perpendicular hollow rectangular tubes joined at a 90-degree angle, with reinforcing internal braces and triangulated support webbing for structural rigidity.
def model_54360_db08c779_0001():
    """Model: basis third hand"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 20, perimeter: 25
            with BuildLine():
                Line((2.5, 2.5), (1, 2.5))
                Line((1, 2.5), (1, 0))
                Line((1, 0), (-1, 0))
                Line((-1, 2.5), (-1, 0))
                Line((-2.5, 2.5), (-1, 2.5))
                Line((-2.5, -2.5), (-2.5, 2.5))
                Line((2.5, -2.5), (-2.5, -2.5))
                Line((2.5, 2.5), (2.5, -2.5))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3, perimeter: 7
            with BuildLine():
                Line((-1, 1.5), (1, 1.5))
                Line((-1, 0), (-1, 1.5))
                Line((1, 0), (-1, 0))
                Line((1, 1.5), (1, 0))
            make_face()
        # OneSide extrude, distance=4.5
        extrude(amount=4.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((0, 4.5)):
                Circle(0.25)
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a turning tool or lathe insert holder featuring a cylindrical shaft with an angled, multi-faceted cutting head mounted on one end, designed for precision machining operations.
def model_54360_db08c779_0003():
    """Model: connector screw (long)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-3.5, 4)):
                Circle(0.2)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1.2, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0971681469, perimeter: 1.8283185307
            with BuildLine():
                CenterArc((-3.5, 4), 0.2, -90, 180)
                Line((-3.1, 3.8), (-3.5, 3.8))
                Line((-3.1, 4.2), (-3.1, 3.8))
                Line((-3.5, 4.2), (-3.1, 4.2))
            make_face()
            # Profile area: 0.0971681469, perimeter: 1.8283185307
            with BuildLine():
                CenterArc((-3.5, 4), 0.2, 90, 180)
                Line((-3.9, 4.2), (-3.5, 4.2))
                Line((-3.9, 3.8), (-3.9, 4.2))
                Line((-3.5, 3.8), (-3.9, 3.8))
            make_face()
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with BuildLine():
                CenterArc((-3.5, 4), 0.2, 90, 180)
                CenterArc((-3.5, 4), 0.2, -90, 180)
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 10 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3.9), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0175000325, perimeter: 0.8000001855
            with BuildLine():
                Line((1.55, 4.1499999072), (1.2, 4.1499999072))
                Line((1.55, 4.2), (1.55, 4.1499999072))
                Line((1.2, 4.2), (1.55, 4.2))
                Line((1.2, 4.2), (1.2, 4.1499999072))
            make_face()
            # Profile area: 0.0174999699, perimeter: 0.7999998279
            with BuildLine():
                Line((1.2, 3.8), (1.55, 3.8))
                Line((1.55, 3.8), (1.55, 3.8499999139))
                Line((1.55, 3.8499999139), (1.2, 3.8499999139))
                Line((1.2, 3.8499999139), (1.2, 3.8))
            make_face()
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical paddle or spatula-like component featuring a rounded, flat blade body with horizontal ribbed or textured surface detailing on one face, and a solid cylindrical handle extending from the rear.
def model_54360_db08c779_0007():
    """Model: assembly part"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            with Locations((5, 1)):
                Circle(0.125)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.3357577149, perimeter: 2.9845130209
            with BuildLine():
                CenterArc((-5, 1), 0.35, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-5, 1), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            with Locations((-5, 1)):
                Circle(0.125)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-1, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-5, 1)):
                Circle(0.25)
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical housing or manifold block with a rounded rectangular body, featuring an internal cavity with blue wire-frame detail visible through the translucent surface, and a protruding cylindrical port or nozzle extending from one end.
def model_54360_db08c779_0008():
    """Model: connector with magnifier"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            with Locations((-3.5, 5)):
                Circle(0.125)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.7363107782, perimeter: 3.926990817
            with BuildLine():
                CenterArc((3.5, 5), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((3.5, 5), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            with Locations((3.5, 5)):
                Circle(0.125)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.1, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.4820619248, perimeter: 5.0939849285
            with BuildLine():
                CenterArc((3.5, 5), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((3.5, 5), 0.3107328814, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


# Description: This is a dual-paddle handle or control lever featuring two elongated, rounded rectangular paddles with a curved connecting bridge and a central cylindrical grip shaft, designed for ergonomic two-handed operation.
def model_54641_8c7f9e9a_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 17 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 404.9867228627, perimeter: 275.9911485751
            with BuildLine():
                Line((-12, -40), (-12, 9))
                CenterArc((-7, -40), 5, 180, 90)
                Line((-7, -45), (19, -45))
                CenterArc((19, -40), 5, -90, 90)
                Line((24, -40), (24, 9))
                Line((24, 9), (21, 9))
                Line((21, 9), (21, -40))
                CenterArc((19, -40), 2, -90, 90)
                Line((19, -42), (-7, -42))
                CenterArc((-7, -40), 2, -180, 90)
                Line((-9, 9), (-9, -40))
                Line((-12, 9), (-9, 9))
            make_face()
        # OneSide extrude, distance=28
        extrude(amount=28)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 9 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -24), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 140.1239199482, perimeter: 103.9822971486
            with BuildLine():
                CenterArc((-14, -7), 14, 0.0000000033, 179.9999999967)
                Line((0, 9), (0, -6.9999999992))
                Line((0, 9), (-28, 9))
                Line((-28, -7), (-28, 9))
            make_face()
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            with Locations((-14, -7)):
                Circle(2.5)
        # OneSide extrude, distance=-60
        extrude(amount=-60, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -45, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 44.1786466911, perimeter: 23.5619449019
            with Locations((14, -6)):
                Circle(3.75)
        # OneSide extrude, distance=32.5
        extrude(amount=32.5, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical band or ring with a ribbed/fluted exterior surface, featuring a hollow center and textured top surface, appearing to be a mechanical component such as a bearing race, spacer, or retaining ring.
def model_54654_f19e7f7d_0002():
    """Model: speed control"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.5670783737, perimeter: 12.6178926583
            with BuildLine():
                CenterArc((2.0200000964, -30.0100014259), 0.01, -90, 89.9999999999)
                Line((2.0300000964, -30.0100014259), (2.0300000964, -30.0050014247))
                CenterArc((2.0200000964, -30.0050014247), 0.01, 0, 90)
                Line((2.0200000964, -29.9950014247), (1.9999937536, -29.9950014247))
                CenterArc((0, -30), 2, 0.1431987836, 359.2837930212)
                Line((1.9998999832, -30.0200014259), (2.0200000964, -30.0200014259))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            with Locations((-1.5000000224, 30.000000447)):
                Circle(0.35)
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 8.2938090893, perimeter: 13.8230103133
            with BuildLine():
                CenterArc((0, 30), 1.7000004198, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 30), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((0, 30)):
                Circle(0.25)
        # OneSide extrude, distance=-0.6
        extrude(amount=-0.6, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a classic top hat featuring a tall cylindrical crown with a curved brim, characterized by a textured fabric surface and a decorative band around the base of the crown.
def model_54657_2a66e0de_0001():
    """Model: pedicle_inner (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 9.0081289858, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((7.5631277769, 18.5928709625)):
                Circle(0.15)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 9.0081289858, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.1256637061, perimeter: 2.5132741229
            with BuildLine():
                CenterArc((7.5631277769, 18.5928709625), 0.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((7.5631277769, 18.5928709625), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((7.5631277769, 18.5928709625)):
                Circle(0.15)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 8.9581289858, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((7.5631277769, 18.5928709625)):
                Circle(0.15)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)
    return part.part


# Description: This is a rectangular flat plate or tray with a shallow, elongated parallelogram shape, featuring a slightly recessed or sunken top surface with subtle surface details or reinforcement ribs.
def model_54766_194d23e7_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.270000008, perimeter: 3.9000000581
            with BuildLine():
                Line((2.1000000313, 1.0000000149), (0.3000000045, 1.0000000149))
                Line((0.3000000045, 1.0000000149), (0.3000000045, 0.8500000127))
                Line((0.3000000045, 0.8500000127), (2.1000000313, 0.8500000127))
                Line((2.1000000313, 0.8500000127), (2.1000000313, 1.0000000149))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0088357296, perimeter: 0.3856194548
            with BuildLine():
                Line((0.3000000045, 1.0000000149), (0.3000000045, 0.8500000127))
                CenterArc((0.3000000045, 0.9250000138), 0.0750000011, 90, 180)
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.9000000201, perimeter: 4.6000000611
            with BuildLine():
                Line((0.3000000045, 0), (0.3000000045, -0.5000000075))
                Line((0.3000000045, -0.5000000075), (2.1000000313, -0.5))
                Line((2.1000000313, 0), (2.1000000313, -0.5))
                Line((2.1000000313, 0), (0.3000000045, 0))
            make_face()
        # OneSide extrude, distance=1.6
        extrude(amount=1.6, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a curved saddle-shaped structural component with a twisted, hyperbolic form featuring a hollow center, flat top and bottom flanges, and vertical side walls that taper and curve inward, creating a complex 3D geometry commonly used in architectural or mechanical applications.
def model_54807_c9f36e22_0000():
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
        # Sketch19 -> Extrude10 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 500, perimeter: 90
            with BuildLine():
                Line((40, 10), (20, 10))
                Line((40, 35), (40, 10))
                Line((20, 35), (40, 35))
                Line((20, 10), (20, 35))
            make_face()
        # OneSide extrude, distance=25
        extrude(amount=25)

        # Sketch20 -> Extrude11 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(40, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 303.1185220559, perimeter: 68.1592504966
            with BuildLine():
                Line((10, 25), (30, 25))
                Line((10, 8.6695595426), (10, 25))
                Line((19.1910487974, 8.6695595426), (10, 8.6695595426))
                _nurbs_edge([(30, 25), (30.0586135584, 24.7954043751), (30.1645996371, 24.3806399618), (30.28985607, 23.7417743115), (30.3891403291, 22.856374893), (30.3997744954, 21.6946078814), (30.297932052, 20.4820191877), (30.0879702552, 19.2282892647), (29.7791283974, 17.950476975), (29.3881476769, 16.6761604393), (28.9362410238, 15.4398780038), (28.4445588712, 14.2777369441), (27.9301272999, 13.222521906), (27.4018552579, 12.2987859185), (26.855790016, 11.5170222121), (26.2724475488, 10.8700122477), (25.6245170954, 10.3403770013), (24.8827689752, 9.9060983695), (24.0232128201, 9.5470015356), (23.0322475227, 9.2495083648), (21.9031922155, 9.0048959727), (20.8879754385, 8.8477115661), (20.0638140104, 8.7505912227), (19.4865995162, 8.6950378766), (19.1910487974, 8.6695595426)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1, 1, 1, 1, 1], 5)
            make_face()
        # OneSide extrude, distance=-32.5
        extrude(amount=-32.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a tilted elliptical ring or washer with a smooth, uniform circular cross-section and an oval opening in the center.
def model_54811_79e68850_0001():
    """Model: net v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 120.7596800113, perimeter: 241.5193600227
            with BuildLine():
                CenterArc((0, 0), 19.7195, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 18.7195, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 883.492555327, perimeter: 284.9802214043
            with BuildLine():
                CenterArc((0, 0), 25.778194487, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 19.5778164329, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=20
        extrude(amount=20, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a flat parallelogram plate or panel with a simple rectangular shape that appears to be slightly skewed, featuring clean edges and a uniform thickness with subtle 3D depth shown through shading on the left edge.
def model_54832_b6237bb1_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 12.25, perimeter: 14
            with BuildLine():
                Line((-1.75, 1.75), (1.75, 1.75))
                Line((-1.75, -1.75), (-1.75, 1.75))
                Line((1.75, -1.75), (-1.75, -1.75))
                Line((1.75, 1.75), (1.75, -1.75))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is a camera or optical device housing featuring a roughly rectangular/trapezoidal body with a cylindrical lens barrel protruding from one side, internal ribbing for structural reinforcement, and a flat mounting surface.
def model_54973_4e7a9d66_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 72, perimeter: 36
            with BuildLine():
                Line((-8, 12.5), (-2, 12.5))
                Line((-8, 0.5), (-8, 12.5))
                Line((-2, 0.5), (-8, 0.5))
                Line((-2, 12.5), (-2, 0.5))
            make_face()
        # OneSide extrude, distance=7
        extrude(amount=7)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(7, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 15.7079632679, perimeter: 14.0496294621
            with Locations((-5, 10)):
                Circle(2.2360679775)
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(7, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 6.9673033315, perimeter: 12.7867739713
            with BuildLine():
                Line((-7.4999489253, 2.6967445676), (-2.5000510747, 2.6967445676))
                Line((-7.4999489253, 1.3032554324), (-7.4999489253, 2.6967445676))
                Line((-2.5000510747, 1.3032554324), (-7.4999489253, 1.3032554324))
                Line((-2.5000510747, 2.6967445676), (-2.5000510747, 1.3032554324))
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a dumbbell with a large circular head on top, a cylindrical handle shaft in the middle, and a weighted cylindrical base, designed for strength training exercises.
def model_54974_0c1b77ef_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 14.794325696, perimeter: 13.6349176633
            with Locations((2.8185881892, -2.1281273926)):
                Circle(2.1700645448)
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.5743532167, perimeter: 5.687730357
            with Locations((-3.4092940946, 2.8140636963)):
                Circle(0.9052304013)
        # OneSide extrude, distance=8
        extrude(amount=8, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 13, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 65.2531436586, perimeter: 34.8826864895
            with BuildLine():
                CenterArc((-2.6895132702, 2.2651031838), 4.6465215818, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-3.4092940946, 2.8140636963), 0.9052304013, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a grinding wheel or abrasive disc with a circular disc shape featuring radial grooves across its surface, a central mounting hole, and a reinforced outer rim with blue-highlighted structural bands for strength and durability.
def model_54979_6bd8ad31_0000():
    """Model: pad"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 18.8495559215, perimeter: 37.6991118431
            with BuildLine():
                CenterArc((-200, 45), 3.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-200, 45), 2.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 18.8495559215, perimeter: 37.6991118431
            with BuildLine():
                CenterArc((-200, 45), 3.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-200, 45), 2.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            with Locations((-200, 45)):
                Circle(2.5)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.8, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-200, 45)):
                Circle(0.5)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a slotted linear rail or channel extrusion with a long, rectangular profile featuring parallel grooves or slots running along its length, used for mounting and guiding components in mechanical assemblies.
def model_54979_6bd8ad31_0004():
    """Model: big side"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 24 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 25, perimeter: 55.313708499
            with BuildLine():
                Line((29, 30), (29, 26))
                Line((29, 26), (30, 25))
                Line((30, 25), (30, 21))
                Line((30, 21), (29, 20))
                Line((29, 20), (29, 16))
                Line((29, 16), (30, 15))
                Line((30, 15), (30, 11))
                Line((30, 11), (29, 10))
                Line((29, 10), (29, 5))
                Line((29, 5), (30, 5))
                Line((30, 10), (30, 5))
                Line((31, 11), (30, 10))
                Line((31, 11), (31, 15))
                Line((31, 15), (30, 16))
                Line((30, 20), (30, 16))
                Line((31, 21), (30, 20))
                Line((31, 21), (31, 25))
                Line((31, 25), (30, 26))
                Line((30, 30), (30, 26))
                Line((29, 30), (30, 30))
            make_face()
        # OneSide extrude, distance=150
        extrude(amount=150)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(29, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((25, 29)):
                Circle(0.1)
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((50, 29)):
                Circle(0.1)
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((75, 29)):
                Circle(0.1)
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((100, 29)):
                Circle(0.1)
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((125.0000018626, 29.0000004321)):
                Circle(0.1)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a tapered cylindrical rod or pin with a gradually decreasing diameter from the thicker end on the left to a sharp point on the right, resembling a needle or cone-shaped shaft with no holes or special features.
def model_54979_6bd8ad31_0007():
    """Model: long border"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 150.2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.48000108, perimeter: 5.2000009
            with BuildLine():
                Line((28.8, 30.20000045), (28.8, 30))
                Line((28.8, 30), (31.2, 30))
                Line((31.2, 30), (31.2, 30.20000045))
                Line((31.2, 30.20000045), (28.8, 30.20000045))
            make_face()
        # OneSide extrude, distance=-2.2
        extrude(amount=-2.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 148), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.48000108, perimeter: 5.2000009
            with BuildLine():
                Line((-29, 30), (-28.8, 30))
                Line((-28.8, 30), (-28.8, 30.20000045))
                Line((-28.8, 30.20000045), (-31.2, 30.20000045))
                Line((-31.2, 30.20000045), (-31.2, 30))
                Line((-31.2, 30), (-31, 30))
                Line((-31, 30), (-29, 30))
            make_face()
            # Profile area: 0.39999991, perimeter: 4.3999986708
            with BuildLine():
                Line((-29, 30), (-29, 28.00000045))
                Line((-29, 28.00000045), (-28.8000004292, 28.00000045))
                Line((-28.8, 30), (-28.8000004292, 28.00000045))
                Line((-29, 30), (-28.8, 30))
            make_face()
            # Profile area: 0.39999991, perimeter: 4.3999991
            with BuildLine():
                Line((-31.2, 30), (-31.2, 28.00000045))
                Line((-31.2, 28.00000045), (-31, 28.00000045))
                Line((-31, 30), (-31, 28.00000045))
                Line((-31.2, 30), (-31, 30))
            make_face()
        # OneSide extrude, distance=146
        extrude(amount=146, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.48000108, perimeter: 5.2000009
            with BuildLine():
                Line((-28.8, 30), (-29, 30))
                Line((-28.8, 30), (-28.8, 30.20000045))
                Line((-31.2, 30.20000045), (-28.8, 30.20000045))
                Line((-31.2, 30.20000045), (-31.2, 30))
                Line((-31, 30), (-31.2, 30))
                Line((-29, 30), (-31, 30))
            make_face()
        # OneSide extrude, distance=2.2
        extrude(amount=2.2, mode=Mode.ADD)
    return part.part


# Description: This is a computer chassis or enclosure panel with a rectangular box-like shape, featuring ventilation mesh cutouts on the upper surface and side panels, along with mounting flanges on the bottom edges for assembly.
def model_54998_a60733aa_0000():
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
        # Sketch5 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 15 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 22.006108734, perimeter: 25.1249619995
            with BuildLine():
                Line((3.25, 0), (7.3165975123, 0))
                CenterArc((8.0665975123, 0), 0.75, 0, 180)
                Line((8.8165975123, 0), (9.800000146, 0))
                Line((9.6712690785, 1.4138068244), (9.800000146, 0))
                Line((9.800000146, 1.8000000268), (9.6712690785, 1.4138068244))
                Line((9.2000001371, 2.0000000298), (9.800000146, 1.8000000268))
                Line((9.1125379593, 2.0728851747), (9.2000001371, 2.0000000298))
                CenterArc((6.5518004282, -1), 4, 50.1944301674, 39.8055698326)
                Line((4.3928932982, 3.0000000298), (6.5518004282, 3))
                CenterArc((4.3928932843, 2.0000000298), 1, 89.9999991996, 36.8807780612)
                Line((2.9618924355, 2.1765028265), (3.792741387, 2.7998860843))
                Line((2.1447576444, 2.003763371), (2.9618924355, 2.1765028265))
                CenterArc((3.4891244976, -4.3556924048), 6.5, 101.9363929366, 19.8685331929)
                Line((0.0418913435, 1.1549542285), (0.0634368756, 1.1683155891))
                CenterArc((0.200000003, 0.9000000134), 0.3, 121.8049261295, 58.1950738705)
                Line((-0.099999997, 0.9000000134), (-0.099999997, 0))
                Line((-0.099999997, 0), (1.75, 0))
                CenterArc((2.5, 0), 0.75, 0, 180)
            make_face()
        # TwoSides extrude, along=5.5, against=-1
        extrude(amount=5.5)
        extrude(sk.sketch, amount=-1)

        # Sketch1 -> Extrude2 (Intersect)
        # Sketch on XY construction plane
        # Sketch has 46 constraints, 13 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.3819292053, perimeter: 7.735763888
            with BuildLine():
                Line((8.0665975123, -0.2587874986), (8.0665975123, -0.6257495565))
                Line((4.5665975123, -0.2587874986), (8.0665975123, -0.2587874986))
                Line((4.5665975123, -0.2587874986), (4.5665975123, -0.6255113764))
                CenterArc((5.3697804759, 9.3421812918), 10, -94.6068616488, 4.6068616488)
                Line((7.501209958, -0.6578187082), (5.3697804759, -0.6578187082))
                CenterArc((7.501209958, 4.3421812918), 5, -90, 6.4927512096)
            make_face()
            # Profile area: 1.6387519886, perimeter: 5.2894236935
            with BuildLine():
                Line((0.0665975123, 3.3179556591), (1.5665975123, 3.3179556591))
                Line((1.5665975123, 4.8179556591), (1.5665975123, 3.3179556591))
                _nurbs_edge([(0.0665975123, 3.3179556591), (0.0648863984, 3.3575066525), (0.0644062557, 3.4357225197), (0.0725126429, 3.5503878581), (0.1012618033, 3.6978714768), (0.1689514491, 3.8726623324), (0.2706070379, 4.0372230681), (0.4079348694, 4.1910397678), (0.5801299472, 4.3343548862), (0.7843897107, 4.4680125199), (1.0175729044, 4.5929587758), (1.2250500137, 4.6866117578), (1.3916277596, 4.7535474925), (1.5074749818, 4.7967270033), (1.5665975123, 4.8179556591)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
            make_face()
            # Profile area: 2.7455052156, perimeter: 6.610134999
            with BuildLine():
                Line((8.0665975123, 1.3179556591), (9.8084513288, 1.3179556591))
                Line((8.0665975123, 1.3179556591), (8.0665975123, -0.2587874986))
                Line((8.0665975123, -0.2587874986), (9.7688729964, -0.2587874986))
                CenterArc((9.7084513288, -0.1791054926), 0.1, -52.8275044687, 52.8275044687)
                Line((9.8084513288, 1.3179556591), (9.8084513288, -0.1791054926))
            make_face()
            # Profile area: 2.8064786248, perimeter: 6.6790645014
            with BuildLine():
                Line((8.0665975123, 4.9297441401), (9.7665231057, 4.9297441401))
                Line((8.0665975123, 4.9297441401), (8.0665975123, 3.3179556591))
                Line((8.0665975123, 3.3179556591), (9.8084513288, 3.3179556591))
                Line((9.8084513288, 4.8483336449), (9.8084513288, 3.3179556591))
                CenterArc((9.7084513288, 4.8483336449), 0.1, 0, 54.4989574652)
            make_face()
            # Profile area: 1.250206588, perimeter: 7.6662400644
            with BuildLine():
                Line((4.5665975123, 5.2598313111), (4.5665975123, 4.9297441401))
                Line((4.5665975123, 4.9297441401), (8.0665975123, 4.9297441401))
                Line((8.0665975123, 5.2641944969), (8.0665975123, 4.9297441401))
                CenterArc((7.5542372768, 0.2905150753), 5, 84.1184601889, 5.8815398111)
                Line((5.3493706539, 5.2905150753), (7.5542372768, 5.2905150753))
                CenterArc((5.3493706539, -4.7094849247), 10, 90, 4.489552552)
            make_face()
            # Profile area: 1.5, perimeter: 5
            with BuildLine():
                Line((0.0665975123, 2.3179556591), (0.0665975123, 3.3179556591))
                Line((0.0665975123, 2.3179556591), (1.5665975123, 2.3179556591))
                Line((1.5665975123, 3.3179556591), (1.5665975123, 2.3179556591))
                Line((0.0665975123, 3.3179556591), (1.5665975123, 3.3179556591))
            make_face()
            # Profile area: 6.3502869572, perimeter: 11.3721740995
            with BuildLine():
                Line((2.0537943924, -0.2587874986), (4.5665975123, -0.2587874986))
                Line((4.5665975123, 1.3179556591), (4.5665975123, -0.2587874986))
                Line((1.5665975123, 1.3179556591), (4.5665975123, 1.3179556591))
                Line((0.0665975123, 1.3179556591), (1.5665975123, 1.3179556591))
                _nurbs_edge([(0.0665975123, 1.3179556591), (0.0648863984, 1.2784046658), (0.0644062557, 1.2001887985), (0.0725126429, 1.0855234602), (0.1012618033, 0.9380398415), (0.1689514491, 0.7632489859), (0.2706070379, 0.5986882501), (0.4079348694, 0.4448715504), (0.5801299472, 0.301556432), (0.7843897107, 0.1678987984), (1.0175729044, 0.0429525424), (1.2250500137, -0.0507004395), (1.3916277596, -0.1176361743), (1.5074749818, -0.1608156851), (1.5665975123, -0.1820443409)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                Line((1.5665975123, -0.1820443409), (2.0537943924, -0.2587874986))
            make_face()
            # Profile area: 4.7956984803, perimeter: 9.1205389831
            with BuildLine():
                Line((1.5665975123, 3.3179556591), (4.5665975123, 3.3179556591))
                Line((4.5665975123, 4.9297441401), (4.5665975123, 3.3179556591))
                Line((2.2762764046, 4.9297441401), (4.5665975123, 4.9297441401))
                Line((1.5665975123, 4.8179556591), (2.2762764046, 4.9297441401))
                Line((1.5665975123, 4.8179556591), (1.5665975123, 3.3179556591))
            make_face()
            # Profile area: 0.4899861286, perimeter: 5.4195132936
            with BuildLine():
                Line((4.5665975123, -0.2587874986), (4.5665975123, -0.6255113764))
                Line((2.0537943924, -0.2587874986), (4.5665975123, -0.2587874986))
                Line((2.0537943924, -0.2587874986), (3.8137684044, -0.5360182625))
                CenterArc((5.3697804759, 9.3421812918), 10, -98.9516659505, 4.3448043018)
            make_face()
            # Profile area: 1.5, perimeter: 5
            with BuildLine():
                Line((0.0665975123, 1.3179556591), (0.0665975123, 2.3179556591))
                Line((0.0665975123, 1.3179556591), (1.5665975123, 1.3179556591))
                Line((1.5665975123, 2.3179556591), (1.5665975123, 1.3179556591))
                Line((0.0665975123, 2.3179556591), (1.5665975123, 2.3179556591))
            make_face()
            # Profile area: 0.3413164369, perimeter: 3.8128944123
            with BuildLine():
                Line((8.0665975123, -0.2587874986), (9.7688729964, -0.2587874986))
                Line((8.0665975123, -0.2587874986), (8.0665975123, -0.6257495565))
                CenterArc((7.501209958, 4.3421812918), 5, -83.5072487904, 6.4101688255)
                Line((8.6177089263, -0.531567784), (9.7307813082, -0.2765804741))
                CenterArc((9.7084513288, -0.1791054926), 0.1, -77.0970799649, 24.2695754962)
            make_face()
            # Profile area: 1.7418538165, perimeter: 5.483707633
            with BuildLine():
                Line((8.0665975123, 2.3179556591), (9.8084513288, 2.3179556591))
                Line((8.0665975123, 2.3179556591), (8.0665975123, 1.3179556591))
                Line((8.0665975123, 1.3179556591), (9.8084513288, 1.3179556591))
                Line((9.8084513288, 2.3179556591), (9.8084513288, 1.3179556591))
            make_face()
            # Profile area: 1.7418538165, perimeter: 5.483707633
            with BuildLine():
                Line((8.0665975123, 3.3179556591), (9.8084513288, 3.3179556591))
                Line((8.0665975123, 3.3179556591), (8.0665975123, 2.3179556591))
                Line((8.0665975123, 2.3179556591), (9.8084513288, 2.3179556591))
                Line((9.8084513288, 3.3179556591), (9.8084513288, 2.3179556591))
            make_face()
            # Profile area: 0.3094979703, perimeter: 3.7688608831
            with BuildLine():
                Line((8.0665975123, 5.2641944969), (8.0665975123, 4.9297441401))
                Line((8.0665975123, 4.9297441401), (9.7665231057, 4.9297441401))
                CenterArc((9.7084513288, 4.8483336449), 0.1, 54.4989574652, 23.7994544306)
                Line((9.7287327725, 4.9462553639), (8.568309462, 5.1866010226))
                CenterArc((7.5542372768, 0.2905150753), 5, 78.2984118958, 5.8200482931)
            make_face()
            # Profile area: 0.4052126693, perimeter: 4.9349821286
            with BuildLine():
                Line((2.2762764046, 4.9297441401), (4.5665975123, 4.9297441401))
                Line((4.5665975123, 5.2598313111), (4.5665975123, 4.9297441401))
                CenterArc((5.3493706539, -4.7094849247), 10, 94.489552552, 4.4621133985)
                Line((2.2762764046, 4.9297441401), (3.7933585824, 5.1687146296))
            make_face()
            # Profile area: 5.5186010521, perimeter: 10.1534863155
            with BuildLine():
                Line((4.5665975123, 1.3179556591), (4.5665975123, -0.2587874986))
                Line((4.5665975123, -0.2587874986), (8.0665975123, -0.2587874986))
                Line((8.0665975123, 1.3179556591), (8.0665975123, -0.2587874986))
                Line((4.5665975123, 1.3179556591), (8.0665975123, 1.3179556591))
            make_face()
            # Profile area: 3.5, perimeter: 9
            with BuildLine():
                Line((4.5665975123, 2.3179556591), (4.5665975123, 1.3179556591))
                Line((4.5665975123, 1.3179556591), (8.0665975123, 1.3179556591))
                Line((8.0665975123, 2.3179556591), (8.0665975123, 1.3179556591))
                Line((4.5665975123, 2.3179556591), (8.0665975123, 2.3179556591))
            make_face()
            # Profile area: 3, perimeter: 8
            with BuildLine():
                Line((1.5665975123, 2.3179556591), (1.5665975123, 1.3179556591))
                Line((1.5665975123, 1.3179556591), (4.5665975123, 1.3179556591))
                Line((4.5665975123, 2.3179556591), (4.5665975123, 1.3179556591))
                Line((1.5665975123, 2.3179556591), (4.5665975123, 2.3179556591))
            make_face()
            # Profile area: 3, perimeter: 8
            with BuildLine():
                Line((1.5665975123, 2.3179556591), (4.5665975123, 2.3179556591))
                Line((4.5665975123, 3.3179556591), (4.5665975123, 2.3179556591))
                Line((1.5665975123, 3.3179556591), (4.5665975123, 3.3179556591))
                Line((1.5665975123, 3.3179556591), (1.5665975123, 2.3179556591))
            make_face()
            # Profile area: 3.5, perimeter: 9
            with BuildLine():
                Line((4.5665975123, 2.3179556591), (8.0665975123, 2.3179556591))
                Line((8.0665975123, 3.3179556591), (8.0665975123, 2.3179556591))
                Line((4.5665975123, 3.3179556591), (8.0665975123, 3.3179556591))
                Line((4.5665975123, 3.3179556591), (4.5665975123, 2.3179556591))
            make_face()
            # Profile area: 5.6412596835, perimeter: 10.223576962
            with BuildLine():
                Line((4.5665975123, 3.3179556591), (8.0665975123, 3.3179556591))
                Line((8.0665975123, 4.9297441401), (8.0665975123, 3.3179556591))
                Line((4.5665975123, 4.9297441401), (8.0665975123, 4.9297441401))
                Line((4.5665975123, 4.9297441401), (4.5665975123, 3.3179556591))
            make_face()
        # OneSide extrude, distance=-3.5
        extrude(amount=-3.5, mode=Mode.INTERSECT)

        # Sketch6 -> Extrude3 (Intersect)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 16.3478764717, perimeter: 16.319046031
            with BuildLine():
                _nurbs_edge([(3.0073148077, 0.4098101137), (3.0041387536, 0.3936442573), (2.9961970431, 0.3615167479), (2.9795156473, 0.3139380968), (2.9475794021, 0.2517452544), (2.8905504082, 0.1762020159), (2.8153409475, 0.1029942748), (2.7213285755, 0.0322019916), (2.6093575003, -0.0362832825), (2.4810569959, -0.1026708469), (2.3381572652, -0.167182967), (2.2133188346, -0.2174414177), (2.1141877242, -0.2544284214), (2.0456948549, -0.2787774136), (2.0108470299, -0.2908746539)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                Line((3.0073148077, 0.4098101137), (3.0073148077, 4.2098101137))
                _nurbs_edge([(3.0073148077, 4.2098101137), (3.0039928777, 4.2253424584), (2.9957696707, 4.2562412353), (2.9786968234, 4.3020916631), (2.9463010014, 4.3622137091), (2.888813095, 4.4355811143), (2.8132794416, 4.5070527884), (2.719114594, 4.5765672293), (2.6071943821, 4.644216444), (2.4791469831, 4.7101714751), (2.3366938057, 4.7746131587), (2.2123564188, 4.8250766136), (2.1136773593, 4.8623541937), (2.0455191786, 4.886956717), (2.0108470299, 4.8991956771)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(2.0108470299, 4.8991956771), (2.0027081667, 4.9136991537), (1.9859095727, 4.9417798399), (1.959149083, 4.9811220853), (1.9203304444, 5.0279980146), (1.8664992473, 5.077319003), (1.8072574152, 5.1176797623), (1.7425030056, 5.1499004574), (1.6721632292, 5.1755261281), (1.5961600351, 5.196417426), (1.5143808111, 5.2143571507), (1.4266537822, 5.2306682748), (1.3327243321, 5.2457953151), (1.2322883341, 5.2595132605), (1.1250322145, 5.2711680195), (1.0106789616, 5.2799035399), (0.889035225, 5.2848810317), (0.7600582288, 5.2855325723), (0.6238175401, 5.2815325771), (0.4804440291, 5.2727240817), (0.3300921958, 5.2590687144), (0.2043427929, 5.2442891635), (0.1070018928, 5.2310581571), (0.0407672825, 5.2212874312), (0.0073148077, 5.2161645546)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1, 1, 1, 1, 1], 5)
                Line((0.0073148077, 5.2161645546), (0.0073148077, -0.520000118))
                _nurbs_edge([(2.0108470299, -0.2908746539), (2.0028167691, -0.3052927078), (1.9862075731, -0.3332245337), (1.9596477618, -0.3724094422), (1.9209291615, -0.4192080485), (1.8669607379, -0.4686412615), (1.8073772688, -0.5092819742), (1.7421992292, -0.5418627311), (1.6715635965, -0.5677783871), (1.5956243023, -0.588699752), (1.5144583009, -0.6062008778), (1.4279777417, -0.6213985812), (1.335834293, -0.6345550588), (1.2375027254, -0.6452891856), (1.1323782041, -0.6528225595), (1.019874769, -0.6562102401), (0.89952717, -0.6545716206), (0.7711098371, -0.6473405751), (0.6345757984, -0.6342054536), (0.4899913545, -0.6150348459), (0.3374830846, -0.5898180314), (0.2092485618, -0.5648502251), (0.1096192249, -0.5434579096), (0.04167105, -0.5280160941), (0.0073148077, -0.520000118)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1, 1, 1, 1, 1], 5)
            make_face()
        # OneSide extrude, distance=10
        extrude(amount=10, mode=Mode.INTERSECT)
    return part.part


# Description: This is a shaft or spindle component with an elongated cylindrical body, featuring two enlarged hexagonal or polygonal end sections (flanges/hubs) and a tapered or angled head section, designed for mechanical power transmission or alignment purposes.
def model_55006_9cd4b6f8_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 6 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 81.8450000282, perimeter: 57.1628041802
            with BuildLine():
                Line((-13.5, 2.5), (10, 2.5))
                Line((-13.5, 2.5), (-13.5, 0.6000000089))
                Line((-11.4000001699, 0.6000000089), (-13.5, 0.6000000089))
                Line((-10.5, 0), (-11.4000001699, 0.6000000089))
                Line((-10.5, -1.5), (-10.5, 0))
                Line((1, -1.5), (-10.5, -1.5))
                Line((2.5, 0.5), (1, -1.5))
                Line((3.5, 0.5), (2.5, 0.5))
                Line((5, 0), (3.5, 0.5))
                Line((5, -1.5), (5, 0))
                Line((10, -1.5), (5, -1.5))
                Line((10, 2.5), (10, -1.5))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch4 -> Extrude2 (NewBody)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            with BuildLine():
                CenterArc((-12, -0.8999999911), 1.5, 0, 89.9999993977)
                CenterArc((-12, -0.8999999911), 1.5, 89.9999993977, 270.0000006023)
            make_face()
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            with BuildLine():
                CenterArc((3.5, -1.0811388301), 1.5, 71.5652507677, 288.4347492323)
                CenterArc((3.5, -1.0811388301), 1.5, 0, 71.5652507677)
            make_face()
        # OneSide extrude, distance=-5
        extrude(amount=-5)
    return part.part


# Description: This is a cylindrical sleeve or tube with a solid, uniform circular cross-section and flat ends, featuring a fine mesh or grid pattern across its curved surface that suggests either a structural lattice design or a textured finish.
def model_55020_c9063bb6_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            Circle(2.5)
        # Symmetric extrude, each_side=4
        extrude(amount=4, both=True)
    return part.part


# Description: This is a rotary valve or ball valve handle featuring a cylindrical knob with knurled gripping surfaces on the left side and a flat rectangular stem extending to the right for manual operation.
def model_55073_02853607_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 78.5398163397, perimeter: 31.4159265359
            Circle(5)
        # OneSide extrude, distance=10
        extrude(amount=10)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(10, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 6.2831853072, perimeter: 8.8857658763
            Circle(1.4142135624)
        # OneSide extrude, distance=25
        extrude(amount=25, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 4.9087385212, perimeter: 7.853981634
            with Locations((4, 0)):
                Circle(1.25)
        # TwoSides extrude, along=5, against=-6
        extrude(amount=5, mode=Mode.SUBTRACT)
        extrude(sk.sketch, amount=-6, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a sculptural or decorative geometric component featuring an angular, abstract form with a large faceted polygonal head section on the left connected to a smaller protruding geometric shape on the right, composed of flat planes and sharp edges throughout.
def model_55093_2020cff0_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 11.2302394582, perimeter: 21.2733795469
            with BuildLine():
                Line((8.9536897771, 0.6353230728), (8.9099241863, -0.0272014855))
                Line((8.8661585955, 1.4520888385), (8.9536897771, 0.6353230728))
                Line((8.525437249, 0.7706461456), (8.8661585955, 1.4520888385))
                Line((6, 0.5), (8.525437249, 0.7706461456))
                Line((5, 1), (6, 0.5))
                Line((4.0375623085, 2.0822297637), (5, 1))
                Line((2.2763063517, 2.0822297637), (4.0375623085, 2.0822297637))
                Line((0.6293843919, 1.2587687839), (2.2763063517, 2.0822297637))
                Line((0, 0), (0.6293843919, 1.2587687839))
                Line((8.9099241863, -0.0272014855), (0, 0))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-0.0030529282, -0.9999953398, 0))):
            # Profile area: 3, perimeter: 13
            with BuildLine():
                Line((2, -1), (2, -7))
                Line((2, -7), (2.5, -7))
                Line((2.5, -1), (2.5, -7))
                Line((2.5, -1), (2, -1))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.ADD)
    return part.part


# Description: This is a polyhedral or geodesic dome-like 3D CAD part with an irregular, faceted spherical shape composed of multiple triangular and polygonal faces in varying shades of blue and dark gray, suggesting a complex geometric structure with multiple intersecting planes.
def model_55096_93c251f9_0000():
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
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 58.0288978064, perimeter: 28.3314755754
            with BuildLine():
                Line((-3.2466475046, -0.9479679869), (-3.8940292525, 3.6425571345))
                Line((-0.5394147407, -2.2427314827), (-3.2466475046, -0.9479679869))
                Line((4.9339036734, -0.9479679869), (-0.5394147407, -2.2427314827))
                Line((4.9339036734, 3.0540282728), (4.9339036734, -0.9479679869))
                Line((2.8446262142, 5.8201139229), (4.9339036734, 3.0540282728))
                Line((0.0785405642, 6.3203634553), (2.8446262142, 5.8201139229))
                Line((-3.8940292525, 3.6425571345), (0.0785405642, 6.3203634553))
            make_face()
        # OneSide extrude, distance=-8
        extrude(amount=-8)

        # Sketch5 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 15.5415630383, perimeter: 17.6143724002
            with BuildLine():
                Line((-1.4048548669, 4.6407235212), (-0.9512895509, 3.1609519515))
                CenterArc((-0.3438213453, 0.8836439305), 2.3569364531, 18.6416392684, 86.2941483588)
                Line((4.3468961596, 0.2724570445), (1.8894616387, 1.6370339737))
                Line((4.145584473, 3.0016109029), (4.3468961596, 0.2724570445))
                Line((2.4385143896, 5.2616755203), (4.145584473, 3.0016109029))
                _nurbs_edge([(-1.4048548669, 4.6407235212), (-1.3513164463, 4.6651385008), (-1.2452563356, 4.7141128206), (-1.0892163407, 4.7880073783), (-0.8873079001, 4.8874059679), (-0.6451704776, 5.0127789687), (-0.4128294085, 5.138214599), (-0.1889841481, 5.261511379), (0.0289444192, 5.3788991335), (0.2453007611, 5.4845750533), (0.4654025276, 5.5716531008), (0.6947114847, 5.6332024511), (0.9381091103, 5.6631725702), (1.1988780065, 5.6577746245), (1.4785752379, 5.6155972916), (1.7777348481, 5.5365434595), (2.0325478977, 5.4443080016), (2.2322241217, 5.3591582189), (2.3691210452, 5.2953443365), (2.4385143896, 5.2616755203)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9333333333, 1, 1, 1, 1, 1, 1], 5)
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical sleeve or pipe component with a rounded rectangular cross-section, featuring a large circular hole on one end and horizontal slot details or windows along its length.
def model_55110_ccc772b9_0009():
    """Model: bolt clamp"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((5, 5)):
                Circle(0.25)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(1, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0424042587, perimeter: 0.9876246213
            with BuildLine():
                CenterArc((5, 5), 0.25, -62.3984420264, 124.7968840527)
                Line((5.1158300331, 5.2215477453), (5.1158300331, 4.7784522547))
            make_face()
            # Profile area: 0.0424042587, perimeter: 0.9876246213
            with BuildLine():
                CenterArc((5, 5), 0.25, 117.6015579736, 124.7968840527)
                Line((4.8841699669, 5.2215477453), (4.8841699669, 4.7784522547))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, -4.8841699669), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0706858368, perimeter: 0.9424778101
            with Locations((-1.2500000186, 5.0000000745)):
                Circle(0.1500000022)
        # TwoSides extrude (symmetric), distance=0.5
        extrude(amount=0.5, both=True, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a shoe sole or footwear component featuring an elongated oval shape with a large central cutout, textured surface patterns, and a curved, ergonomic profile designed for shoe construction.
def model_55114_7bf17f6a_0006():
    """Model: MOUNT CABLE"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 29.7969091269, perimeter: 38.3949157236
            with BuildLine():
                CenterArc((169.8670710526, 44.107546849), 2, -176.1922177587, 171.6558660722)
                Line((172.2991299237, 49.4739852026), (171.860805761, 43.9493636876))
                Line((172.3405975664, 49.9966418346), (172.2991299237, 49.4739852026))
                CenterArc((169.8414346513, 49.9319523932), 2.5, 1.482738282, 183.6997419838)
                Line((167.8714861379, 43.9747279951), (167.3516544877, 49.7061322498))
            make_face()
            with BuildLine():
                CenterArc((169.8414346513, 49.9319523932), 2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.3854541192, perimeter: 6.5289423489
            with BuildLine():
                Line((171.263048964, 43.9985777895), (168.5, 43.9985777895))
                Line((171.263048964, 44.5), (171.263048964, 43.9985777895))
                Line((168.5, 44.5), (171.263048964, 44.5))
                Line((168.5, 43.9985777895), (168.5, 44.5))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 44.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.381524482, perimeter: 6.5260979279
            with BuildLine():
                Line((-1, -168.5), (-1, -171.263048964))
                Line((-1.5, -168.5), (-1, -168.5))
                Line((-1.5, -171.263048964), (-1.5, -168.5))
                Line((-1, -171.263048964), (-1.5, -171.263048964))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


# Description: This is a dark blue/gray aerodynamic fairing or shroud with an elongated, streamlined body that tapers to a pointed nose, featuring a protruding rectangular mounting block or bracket on the right side.
def model_55135_f1186d58_0005():
    """Model: 3. Pilnik"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 22 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.2527007733, perimeter: 4.5720043458
            with BuildLine():
                CenterArc((7.9, 1.9138812599), 0.1, 59.4501667019, 22.0190663522)
                Line((7.9148340476, 2.0127748949), (6.9853649946, 2.152195275))
                CenterArc((6.6145138046, -0.3201455985), 2.5, 81.4692330541, 30.3966418001)
                Line((7.9508287577, 2), (5.6834260527, 2))
            make_face()
            # Profile area: 2.5237358108, perimeter: 9.5169571769
            with BuildLine():
                CenterArc((7.6000001118, 0.9000000119), 0.1, 180, 90)
                Line((7.6000001118, 0.8000000119), (8.4000001267, 0.8000000119))
                CenterArc((8.4000001267, 0.9000000119), 0.1, -90, 90)
                Line((8.5000001267, 1.3000000134), (8.5000001267, 0.9000000119))
                CenterArc((8.3000001267, 1.3000000134), 0.2, 0, 90.0000025613)
                Line((8, 1.5), (8.3000001177, 1.5000000134))
                Line((8, 1.9138812599), (8, 1.5))
                CenterArc((7.9, 1.9138812599), 0.1, 0, 59.4501667019)
                Line((7.9508287577, 2), (5.6834260527, 2))
                CenterArc((6.6145138046, -0.3201455985), 2.5, 111.8658748541, 13.0634040927)
                Line((5.183101535, 1.7295028871), (5.0048463124, 1.6050148519))
                CenterArc((6.5024231562, 4.2465358634), 3.0365061596, -119.5505189795, 29.5505189795)
                Line((7.5000001118, 1.2100297038), (6.5024231562, 1.2100297038))
                Line((7.5000001118, 1.0003343033), (7.5000001118, 1.2100297038))
                CenterArc((8, 1), 0.5, 179.9616916607, 0.0766166785)
                Line((7.5000001118, 0.9000000119), (7.5000001118, 0.9996656967))
            make_face()
            with BuildLine():
                CenterArc((8, 1), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.0000000671, 1.4999996424, 0), x_dir=(0, 0, 1), z_dir=(-0.0000000447, 1, 0))) as sk:
            # Profile area: 0.1939991836, perimeter: 5.9563618525
            with BuildLine():
                Line((0.1, 5.0048463841), (0.2333333333, 5.0048463841))
                Line((0.2333333333, 5.0048463841), (0.1, 7.9148341376))
                Line((0.1, 7.9148341376), (0.1, 5.0048463841))
            make_face()
        # TwoSides extrude, along=1.1, against=-0.9
        extrude(amount=1.1, mode=Mode.SUBTRACT)
        extrude(sk.sketch, amount=-0.9, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 16 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.6482205853, perimeter: 6.1695242756
            with BuildLine():
                Line((6.970530947, 2.0533016401), (7.9, 1.9138812599))
                CenterArc((6.6145138046, -0.3201455985), 2.4, 81.4692330541, 43.4600458928)
                Line((5.1960888279, 1.616600684), (5.2403580258, 1.6475169477))
                CenterArc((6.5024231562, 4.2465358634), 2.9365061596, -116.4143862723, 26.4143862723)
                Line((6.5024231562, 1.3100297038), (7.9, 1.3100297038))
                Line((7.9, 1.9138812599), (7.9, 1.3100297038))
            make_face()
        # OneSide extrude, distance=-0.01
        extrude(amount=-0.01, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a lever arm or handle assembly with an angular L-shaped design, featuring a rectangular shaft extending horizontally from a compact pivot head on the left, with a hollow interior construction and reinforced edges.
def model_55197_77c1ca4a_0002():
    """Model: Cargador_02_Grab v9"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 10 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 8.76, perimeter: 17
            with BuildLine():
                Line((3.65, -0.6), (-2.2487854525, -0.6))
                Line((3.65, 0.6), (3.65, -0.6))
                Line((-3.65, 0.6), (3.65, 0.6))
                Line((-3.65, -0.6), (-3.65, 0.6))
                Line((-2.2487854525, -0.6), (-3.65, -0.6))
            make_face()
            # Profile area: 0.3676821821, perimeter: 3.2131145998
            with BuildLine():
                Line((-2.2487854525, -0.6), (-3.65, -0.6))
                Line((-3.65, -0.9), (-3.65, -0.6))
                Line((-2.6, -0.9), (-3.65, -0.9))
                Line((-2.2487854525, -0.6), (-2.6, -0.9))
            make_face()
        # OneSide extrude, distance=1.15
        extrude(amount=1.15)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -0.6, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 6.6636032704, perimeter: 14.897570905
            with BuildLine():
                Line((3.65, 1.15), (-2.2487854525, 1.15))
                Line((-2.2487854525, 1.15), (-2.2487854525, 0))
                Line((-2.2487854525, 0), (3.65, 0))
                Line((3.65, 0), (3.65, 0.425))
                Line((3.25, 0.425), (3.65, 0.425))
                Line((3.25, 0.725), (3.25, 0.425))
                Line((3.65, 0.725), (3.25, 0.725))
                Line((3.65, 0.725), (3.65, 1.15))
            make_face()
            # Profile area: 0.12, perimeter: 1.4
            with BuildLine():
                Line((3.65, 0.725), (3.25, 0.725))
                Line((3.25, 0.725), (3.25, 0.425))
                Line((3.25, 0.425), (3.65, 0.425))
                Line((3.65, 0.425), (3.65, 0.725))
            make_face()
        # OneSide extrude, distance=-0.25
        extrude(amount=-0.25, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a parabolic satellite dish antenna featuring a large concave reflective surface with a central feed support structure and radial ribbing for structural reinforcement.
def model_55197_77c1ca4a_0003():
    """Model: Selector_Grap v6"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.5476763502, perimeter: 9.7389372261
            Circle(1.55)
        # OneSide extrude, distance=0.25
        extrude(amount=0.25)

        # Sketch7 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 9 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0049580166, perimeter: 0.2964928504
            with BuildLine():
                CenterArc((-0.6, 0), 0.1, 30, 55.2198081528)
                CenterArc((0, 0), 0.6, 170.4396163056, 9.5603836944)
                Line((-0.5133974596, 0.05), (-0.6, 0))
            make_face()
            # Profile area: 0.0052359878, perimeter: 0.3047197551
            with BuildLine():
                CenterArc((-0.6, 0), 0.1, -30, 60)
                Line((-0.5133974596, 0.05), (-0.6, 0))
                Line((-0.6, 0), (-0.5133974596, -0.05))
            make_face()
            # Profile area: 0.0049580166, perimeter: 0.2964928504
            with BuildLine():
                Line((-0.6, 0), (-0.5133974596, -0.05))
                CenterArc((0, 0), 0.6, -180, 9.5603836944)
                CenterArc((-0.6, 0), 0.1, -85.2198081528, 55.2198081528)
            make_face()
            # Profile area: 0.0162639055, perimeter: 0.5310774905
            with BuildLine():
                CenterArc((0, 0), 0.6, -180, 9.5603836944)
                CenterArc((0, 0), 0.6, 170.4396163056, 9.5603836944)
                CenterArc((-0.6, 0), 0.1, 85.2198081528, 189.5603836944)
            make_face()
            # Profile area: 0.0049580166, perimeter: 0.2964928504
            with BuildLine():
                CenterArc((0, 0), 0.6, -60, 9.5603836944)
                CenterArc((0.3, -0.5196152423), 0.1, 34.7801918472, 55.2198081528)
                Line((0.3, -0.5196152423), (0.3, -0.4196152423))
            make_face()
            # Profile area: 0.0049580166, perimeter: 0.2964928504
            with BuildLine():
                CenterArc((0.3, -0.5196152423), 0.1, 150, 55.2198081528)
                CenterArc((0, 0), 0.6, -69.5603836944, 9.5603836944)
                Line((0.2133974596, -0.4696152423), (0.3, -0.5196152423))
            make_face()
            # Profile area: 0.0162639055, perimeter: 0.5310774905
            with BuildLine():
                CenterArc((0.3, -0.5196152423), 0.1, -154.7801918472, 189.5603836944)
                CenterArc((0, 0), 0.6, -60, 9.5603836944)
                CenterArc((0, 0), 0.6, -69.5603836944, 9.5603836944)
            make_face()
            # Profile area: 0.0052359878, perimeter: 0.3047197551
            with BuildLine():
                Line((0.2133974596, -0.4696152423), (0.3, -0.5196152423))
                Line((0.3, -0.5196152423), (0.3, -0.4196152423))
                CenterArc((0.3, -0.5196152423), 0.1, 90, 60)
            make_face()
            # Profile area: 0.0162639055, perimeter: 0.5310774905
            with BuildLine():
                CenterArc((0, 0), 0.6, 60, 9.5603836944)
                CenterArc((0, 0), 0.6, 50.4396163056, 9.5603836944)
                CenterArc((0.3, 0.5196152423), 0.1, -34.7801918472, 189.5603836944)
            make_face()
            # Profile area: 0.0049580166, perimeter: 0.2964928504
            with BuildLine():
                CenterArc((0.3, 0.5196152423), 0.1, -90, 55.2198081528)
                CenterArc((0, 0), 0.6, 50.4396163056, 9.5603836944)
                Line((0.3, 0.4196152423), (0.3, 0.5196152423))
            make_face()
            # Profile area: 0.0052359878, perimeter: 0.3047197551
            with BuildLine():
                Line((0.3, 0.4196152423), (0.3, 0.5196152423))
                Line((0.3, 0.5196152423), (0.2133974596, 0.4696152423))
                CenterArc((0.3, 0.5196152423), 0.1, -150, 60)
            make_face()
            # Profile area: 0.0049580166, perimeter: 0.2964928504
            with BuildLine():
                Line((0.3, 0.5196152423), (0.2133974596, 0.4696152423))
                CenterArc((0, 0), 0.6, 60, 9.5603836944)
                CenterArc((0.3, 0.5196152423), 0.1, 154.7801918472, 55.2198081528)
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)
    return part.part


# Description: This is a router base or mounting bracket featuring a rectangular blue base plate with three vertical dark posts or standoffs extending upward, designed for component mounting or cable management.
def model_55207_9a9a54a1_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 30, perimeter: 22
            with BuildLine():
                Line((-3, 2.5), (3, 2.5))
                Line((-3, -2.5), (-3, 2.5))
                Line((3, -2.5), (-3, -2.5))
                Line((3, 2.5), (3, -2.5))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((2, -1.5)):
                Circle(0.3)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-2, -1.5)):
                Circle(0.3)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-2, 1.5)):
                Circle(0.3)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((2, 1.5)):
                Circle(0.3)
        # OneSide extrude, distance=4
        extrude(amount=4, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            Circle(0.75)
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a wireframe 3D CAD model of a hollow ellipsoidal (egg-shaped) shell featuring a dense network of radial ribs or meridian lines extending from a central axis to the outer surface, creating a ribbed skeletal framework.
def model_55318_1778e966_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch11 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.926990817, perimeter: 7.024814731
            with Locations((3, 0.5)):
                Circle(1.1180339887)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is an earbud or earphone housing featuring an oval-shaped blue body with two protruding cylindrical stems (one upper, one lower) that serve as connection points or support structures, along with small circular holes or vents visible on the surface.
def model_55389_a736bd99_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 27.6993238953, perimeter: 18.6569013996
            Circle(2.9693380805)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-0.0094524718, -2.3873959085)):
                Circle(0.5)
        # OneSide extrude, distance=4
        extrude(amount=4, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((0.0000000779, 2.296819005)):
                Circle(0.5)
        # OneSide extrude, distance=4
        extrude(amount=4, mode=Mode.ADD)
    return part.part


# Description: This is a fixed dumbbell consisting of two cylindrical weighted heads connected by a shorter cylindrical handle shaft, with knurled grip texture on the handle and textured surfaces on the weight heads.
def model_55402_4edbf450_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 31.4159265359, perimeter: 19.8691765316
            Circle(3.1622776602)
        # OneSide extrude, distance=3.5
        extrude(amount=3.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            Circle(1.5)
        # OneSide extrude, distance=10.5
        extrude(amount=10.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 14), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 24.3473430653, perimeter: 29.2939544924
            with BuildLine():
                CenterArc((0, 0), 3.1622776602, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            Circle(1.5)
        # OneSide extrude, distance=3.5
        extrude(amount=3.5, mode=Mode.ADD)
    return part.part


# Description: This is a long, narrow rectangular tray or channel with a shallow depth, featuring angled end caps on both sides and a slightly recessed or beveled top surface with subtle surface details.
def model_55408_e4a0550d_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.5, perimeter: 3
            with BuildLine():
                Line((-3, 1.5), (-4, 1.5))
                Line((-3, 2), (-3, 1.5))
                Line((-4, 2), (-3, 2))
                Line((-4, 1.5), (-4, 2))
            make_face()
        # OneSide extrude, distance=10
        extrude(amount=10)
    return part.part


# Description: This assembly consists of three components: a tapered blade or fin with a curved profile (left), a cylindrical barrel or housing with textured surface details (top center), and an oval-shaped disc or end cap with radial ribbing or vanes (bottom right), appearing to be parts of a mechanical device such as a fan, motor, or turbine assembly.
def model_55571_74a416b1_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 39.2699081699, perimeter: 22.2144146908
            Circle(3.5355339059)
        # OneSide extrude, distance=9
        extrude(amount=9)

        # Sketch4 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 71.8339151, perimeter: 53.6291731288
            with BuildLine():
                Line((-22.5, 0), (-22.5, -15.4594531441))
                CenterArc((-29.0460315051, -15.4594531441), 6.5460315051, -48.070130942, 48.070130942)
                CenterArc((-20, -26), 7.3471832367, 61.4967540497, 67.9876426929)
                CenterArc((-13.3487176152, -15), 5.5257691213, 180, 55.307106043)
                Line((-18.8744867364, 0), (-18.8744867364, -15))
                Line((-22.5, 0), (-18.8744867364, 0))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch5 -> Extrude3 (NewBody)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 69.2753988442, perimeter: 29.5049205444
            with Locations((-8, -26)):
                Circle(4.6958539502)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a cylindrical bolt or fastener with a hexagonal head at the top and a long, tapered threaded shaft extending downward at an angle.
def model_55611_69142616_0001():
    """Model: screw M6x45"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((12, -8)):
                Circle(0.3)
        # OneSide extrude, distance=4.5
        extrude(amount=4.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 4.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5026548246, perimeter: 5.0265482457
            with BuildLine():
                CenterArc((-12, 8), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-12, 8), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-12, 8)):
                Circle(0.3)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3117691454, perimeter: 2.0784609691
            with BuildLine():
                Line((-12.1745058265, 7.7007547552), (-11.8280989294, 7.6992508987))
                Line((-11.8280989294, 7.6992508987), (-11.6535931028, 7.9984961435))
                Line((-11.6535931028, 7.9984961435), (-11.8254941735, 8.2992452448))
                Line((-11.8254941735, 8.2992452448), (-12.1719010706, 8.3007491013))
                Line((-12.1719010706, 8.3007491013), (-12.3464068972, 8.0015038565))
                Line((-12.3464068972, 8.0015038565), (-12.1745058265, 7.7007547552))
            make_face()
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a shaft or axle assembly with a cylindrical body featuring a enlarged circular flange or collar on the left end and a tapered or rounded transition, designed to support rotational components or serve as a drive shaft with mounting capabilities.
def model_55611_69142616_0004():
    """Model: screw M8x46"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((-92.5, 10)):
                Circle(0.4)
        # OneSide extrude, distance=4.6103
        extrude(amount=4.6103)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.6283185307, perimeter: 6.2831853072
            with BuildLine():
                CenterArc((92.5, 10), 0.6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((92.5, 10), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((92.5, 10)):
                Circle(0.4)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(-0.3, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.2388842145, perimeter: 2.7683073059
            with BuildLine():
                Line((92.3999999985, 10.5916079781), (92.3999999985, 9.4083920219))
                CenterArc((92.5, 10), 0.6, -99.5940683712, 19.188136598)
                Line((92.6, 10.5916079783), (92.6, 9.4083920217))
                CenterArc((92.5, 10), 0.6, 80.4059317731, 19.188136598)
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical sleeve or bushing with a perforated or mesh-textured surface and a solid flanged end, designed for filtration, ventilation, or mechanical coupling applications.
def model_55611_69142616_0005():
    """Model: screw M8x20"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((28.9394079538, -2.3715405978)):
                Circle(0.4)
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.6283185307, perimeter: 6.2831853072
            with BuildLine():
                CenterArc((28.9394079538, -2.3715405978), 0.6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((28.9394079538, -2.3715405978), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((28.9394079538, -2.3715405978)):
                Circle(0.4)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 2.3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.2388842127, perimeter: 2.7683073034
            with BuildLine():
                Line((28.8394079538, -1.7799326195), (28.8394079538, -2.9631485761))
                CenterArc((28.9394079538, -2.3715405978), 0.6, -99.5940682269, 19.1881364537)
                Line((29.0394079538, -1.7799326195), (29.0394079538, -2.9631485761))
                CenterArc((28.9394079538, -2.3715405978), 0.6, 80.4059317731, 19.1881364537)
            make_face()
        # OneSide extrude, distance=-0.15
        extrude(amount=-0.15, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a simple straight rod or cylindrical shaft with a tapered or pointed end, featuring a linear, elongated design with no holes, slots, or flanges.
def model_55611_69142616_0007():
    """Model: shaft"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((40, 10)):
                Circle(0.5)
        # OneSide extrude, distance=150
        extrude(amount=150)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 150), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.2809, perimeter: 2.12
            with BuildLine():
                Line((39.735, 10.265), (40.265, 10.265))
                Line((39.735, 9.735), (39.735, 10.265))
                Line((40.265, 9.735), (39.735, 9.735))
                Line((40.265, 10.265), (40.265, 9.735))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.2809, perimeter: 2.12
            with BuildLine():
                Line((-40.265, 10.265), (-39.735, 10.265))
                Line((-40.265, 9.735), (-40.265, 10.265))
                Line((-39.735, 9.735), (-40.265, 9.735))
                Line((-39.735, 10.265), (-39.735, 9.735))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical actuator or connector component with a tapered/pointed end at one terminus and a slightly bulbous end at the other, featuring a smooth elongated body with minimal surface features.
def model_55611_69142616_0013():
    """Model: engine shaft"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((17.5, 12.5)):
                Circle(1)
        # OneSide extrude, distance=11.5
        extrude(amount=11.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 1, perimeter: 4
            with BuildLine():
                Line((-18, 13), (-17, 13))
                Line((-18, 12), (-18, 13))
                Line((-17, 12), (-18, 12))
                Line((-17, 13), (-17, 12))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 11.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((17.5, 12.5)):
                Circle(0.5)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


MODELS = {
    "model_51583_cebed5ca_0000": {"func": model_51583_cebed5ca_0000, "volume": 219.0518805191, "area": 330.7505900763},
    "model_51585_b695905b_0013": {"func": model_51585_b695905b_0013, "volume": 2.2375, "area": 187.975},
    "model_51606_b72fa3d6_0009": {"func": model_51606_b72fa3d6_0009, "volume": 0.0879724821, "area": 2.0054361001},
    "model_51731_22e19a47_0031": {"func": model_51731_22e19a47_0031, "volume": 6.7008207806, "area": 137.8334506854},
    "model_51775_49ef614a_0002": {"func": model_51775_49ef614a_0002, "volume": 0.0009099845, "area": 0.0874406002},
    "model_51775_49ef614a_0009": {"func": model_51775_49ef614a_0009, "volume": 0.6243861629, "area": 23.0328825412},
    "model_51775_49ef614a_0010": {"func": model_51775_49ef614a_0010, "volume": 1.9239489746, "area": 63.6501743113},
    "model_51777_87ff5835_0007": {"func": model_51777_87ff5835_0007, "volume": 9615.2593527693, "area": 10665.4082991639},
    "model_51863_0b8751d1_0002": {"func": model_51863_0b8751d1_0002, "volume": 120.9856882864, "area": 352.1907287487},
    "model_51863_0b8751d1_0009": {"func": model_51863_0b8751d1_0009, "volume": 423.6708470517, "area": 680.101388595},
    "model_51871_86ebf5b2_0000": {"func": model_51871_86ebf5b2_0000, "volume": 656.2784646302, "area": 3021.6521513966},
    "model_51871_86ebf5b2_0010": {"func": model_51871_86ebf5b2_0010, "volume": 759.2307692308, "area": 2073.3589116316},
    "model_51876_8346832d_0011": {"func": model_51876_8346832d_0011, "volume": 97.4664215944, "area": 239.6193807647},
    "model_51895_5760b481_0006": {"func": model_51895_5760b481_0006, "volume": 31.9682577943, "area": 228.1542394761},
    "model_51895_5760b481_0007": {"func": model_51895_5760b481_0007, "volume": 45.5201362652, "area": 361.4710498391},
    "model_51940_aa0fca73_0005": {"func": model_51940_aa0fca73_0005, "volume": 63.7327047652, "area": 268.7789594779},
    "model_52024_97da327b_0006": {"func": model_52024_97da327b_0006, "volume": 0.6645237072, "area": 6.7118045156},
    "model_52352_adac16c3_0005": {"func": model_52352_adac16c3_0005, "volume": 3666, "area": 7791.2455532034},
    "model_52443_085efc00_0013": {"func": model_52443_085efc00_0013, "volume": 70.2690266447, "area": 153.997875658},
    "model_52446_094458cd_0000": {"func": model_52446_094458cd_0000, "volume": 1749.748034491, "area": 1015.6103960438},
    "model_52557_e6a00b06_0013": {"func": model_52557_e6a00b06_0013, "volume": 156.2337492234, "area": 506.1799884701},
    "model_52783_2a26d5d9_0001": {"func": model_52783_2a26d5d9_0001, "volume": 26716124.403110195, "area": 1053026.2756419196},
    "model_52866_a4bc0a26_0003": {"func": model_52866_a4bc0a26_0003, "volume": 11.0063735056, "area": 49.4447413992},
    "model_52879_de812eb3_0000": {"func": model_52879_de812eb3_0000, "volume": 285.6322284418, "area": 315.8048380659},
    "model_52974_259cdd82_0000": {"func": model_52974_259cdd82_0000, "volume": 0.0082309728, "area": 0.4216017341},
    "model_53078_b592f2bd_0000": {"func": model_53078_b592f2bd_0000, "volume": 96.9478500916, "area": 304.7479676014},
    "model_53119_aabd4fc1_0023": {"func": model_53119_aabd4fc1_0023, "volume": 26035.9491166254, "area": 8765.0435035155},
    "model_53216_2857e8ac_0003": {"func": model_53216_2857e8ac_0003, "volume": 7.7434282933, "area": 64.3115105977},
    "model_53216_2857e8ac_0004": {"func": model_53216_2857e8ac_0004, "volume": 3.9406531757, "area": 40.2119419855},
    "model_53216_2857e8ac_0011": {"func": model_53216_2857e8ac_0011, "volume": 81.2364324613, "area": 419.5406538381},
    "model_53458_1aff9fae_0000": {"func": model_53458_1aff9fae_0000, "volume": 854.0122858423, "area": 930.3676626231},
    "model_53470_39f2e9dc_0002": {"func": model_53470_39f2e9dc_0002, "volume": 55658.2, "area": 27640.3},
    "model_53595_51bad85d_0000": {"func": model_53595_51bad85d_0000, "volume": 272.7172225541, "area": 506.4752614931},
    "model_53614_f6a8f7e1_0000": {"func": model_53614_f6a8f7e1_0000, "volume": 32.008837264, "area": 145.9624575272},
    "model_53627_7b1adb8e_0003": {"func": model_53627_7b1adb8e_0003, "volume": 0.3571863679, "area": 5.8885803328},
    "model_53702_02f39181_0000": {"func": model_53702_02f39181_0000, "volume": 95.426990817, "area": 305.8495559215},
    "model_53706_7d9ee99b_0000": {"func": model_53706_7d9ee99b_0000, "volume": 32.5314159265, "area": 140.1256637061},
    "model_53831_de0554da_0001": {"func": model_53831_de0554da_0001, "volume": 45.5316337965, "area": 143.9680650742},
    "model_53846_89405f98_0005": {"func": model_53846_89405f98_0005, "volume": 90.2150848309, "area": 189.0751822352},
    "model_53927_ef5208b9_0001": {"func": model_53927_ef5208b9_0001, "volume": 10.4200333504, "area": 216.5163288866},
    "model_53927_ef5208b9_0002": {"func": model_53927_ef5208b9_0002, "volume": 4.9592872659, "area": 92.6699982584},
    "model_54177_2b99e039_0002": {"func": model_54177_2b99e039_0002, "volume": 0.9030450932, "area": 10.0929803675},
    "model_54177_2b99e039_0009": {"func": model_54177_2b99e039_0009, "volume": 15.6737827399, "area": 64.6791095521},
    "model_54177_2b99e039_0010": {"func": model_54177_2b99e039_0010, "volume": 22.6896405239, "area": 70.3611944902},
    "model_54273_21c2b38f_0015": {"func": model_54273_21c2b38f_0015, "volume": 0.29584, "area": 6.6048},
    "model_54360_db08c779_0000": {"func": model_54360_db08c779_0000, "volume": 0.9179341035, "area": 6.0475658582},
    "model_54360_db08c779_0001": {"func": model_54360_db08c779_0001, "volume": 33.2054756887, "area": 98.4634954085},
    "model_54360_db08c779_0003": {"func": model_54360_db08c779_0003, "volume": 0.3147964455, "area": 3.5542294129},
    "model_54360_db08c779_0007": {"func": model_54360_db08c779_0007, "volume": 0.262126637, "area": 4.7752208335},
    "model_54360_db08c779_0008": {"func": model_54360_db08c779_0008, "volume": 0.5949629108, "area": 7.528719235},
    "model_54641_8c7f9e9a_0000": {"func": model_54641_8c7f9e9a_0000, "volume": 11816.8810134175, "area": 8662.5948815133},
    "model_54654_f19e7f7d_0002": {"func": model_54654_f19e7f7d_0002, "volume": 7.4344986856, "area": 47.2082448755},
    "model_54657_2a66e0de_0001": {"func": model_54657_2a66e0de_0001, "volume": 0.0310232275, "area": 0.7539822369},
    "model_54766_194d23e7_0000": {"func": model_54766_194d23e7_0000, "volume": 0.135883576, "area": 2.5162334349},
    "model_54807_c9f36e22_0000": {"func": model_54807_c9f36e22_0000, "volume": 6437.630281479, "area": 2553.7303554033},
    "model_54811_79e68850_0001": {"func": model_54811_79e68850_0001, "volume": 30.9803912385, "area": 278.7246823647},
    "model_54832_b6237bb1_0000": {"func": model_54832_b6237bb1_0000, "volume": 2.45, "area": 27.3},
    "model_54973_4e7a9d66_0000": {"func": model_54973_4e7a9d66_0000, "volume": 521.481319873, "area": 449.6728068668},
    "model_54974_0c1b77ef_0000": {"func": model_54974_0c1b77ef_0000, "volume": 225.0727415307, "area": 343.5367428603},
    "model_54979_6bd8ad31_0000": {"func": model_54979_6bd8ad31_0000, "volume": 20.7345115137, "area": 101.7876019763},
    "model_54979_6bd8ad31_0004": {"func": model_54979_6bd8ad31_0004, "volume": 3749.8429203673, "area": 8349.8837082359},
    "model_54979_6bd8ad31_0007": {"func": model_54979_6bd8ad31_0007, "volume": 188.9921361566, "area": 1952.6398116994},
    "model_54998_a60733aa_0000": {"func": model_54998_a60733aa_0000, "volume": 115.4260153006, "area": 169.2171610798},
    "model_55006_9cd4b6f8_0000": {"func": model_55006_9cd4b6f8_0000, "volume": 479.9108348466, "area": 572.0261344474},
    "model_55020_c9063bb6_0000": {"func": model_55020_c9063bb6_0000, "volume": 157.0796326795, "area": 164.9336143135},
    "model_55073_02853607_0000": {"func": model_55073_02853607_0000, "volume": 893.7755034986, "area": 760.7841956869},
    "model_55093_2020cff0_0000": {"func": model_55093_2020cff0_0000, "volume": 42.6907183745, "area": 125.2806175569},
    "model_55096_93c251f9_0000": {"func": model_55096_93c251f9_0000, "volume": 456.4603737015, "area": 351.5167824049},
    "model_55110_ccc772b9_0009": {"func": model_55110_ccc772b9_0009, "volume": 0.2214616558, "area": 2.8680385754},
    "model_55114_7bf17f6a_0006": {"func": model_55114_7bf17f6a_0006, "volume": 17.6654331647, "area": 91.8463163925},
    "model_55135_f1186d58_0005": {"func": model_55135_f1186d58_0005, "volume": 0.4073916924, "area": 7.1088803271},
    "model_55197_77c1ca4a_0002": {"func": model_55197_77c1ca4a_0002, "volume": 8.8009336918, "area": 35.3282599686},
    "model_55197_77c1ca4a_0003": {"func": model_55197_77c1ca4a_0003, "volume": 1.8963438655, "area": 17.7185825662},
    "model_55207_9a9a54a1_0000": {"func": model_55207_9a9a54a1_0000, "volume": 18.6403204873, "area": 99.9811922294},
    "model_55318_1778e966_0000": {"func": model_55318_1778e966_0000, "volume": 0.7853981634, "area": 9.2589445802},
    "model_55389_a736bd99_0000": {"func": model_55389_a736bd99_0000, "volume": 20.1328472548, "area": 89.8598397192},
    "model_55402_4edbf450_0000": {"func": model_55402_4edbf450_0000, "volume": 294.1316121923, "area": 349.5709435117},
    "model_55408_e4a0550d_0000": {"func": model_55408_e4a0550d_0000, "volume": 5, "area": 31},
    "model_55571_74a416b1_0000": {"func": model_55571_74a416b1_0000, "volume": 494.538487473, "area": 643.8222701185},
    "model_55611_69142616_0001": {"func": model_55611_69142616_0001, "volume": 1.6188762646, "area": 12.7694364713},
    "model_55611_69142616_0004": {"func": model_55611_69142616_0004, "volume": 2.6089047014, "area": 15.3727790585},
    "model_55611_69142616_0005": {"func": model_55611_69142616_0005, "volume": 1.3087690238, "area": 8.7141517901},
    "model_55611_69142616_0007": {"func": model_55611_69142616_0007, "volume": 118.6524245096, "area": 479.1696943653},
    "model_55611_69142616_0013": {"func": model_55611_69142616_0013, "volume": 37.9137136797, "area": 85.6814089933},
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
