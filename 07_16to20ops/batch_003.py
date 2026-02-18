"""Batch 003 - passing/07_16to20ops
27 models bundled from Fusion360 Gallery reconstructions.
"""

from build123d import *
from build123d import Edge, BuildLine
from collections import Counter
from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
from OCP.Geom import Geom_BSplineCurve
from OCP.TColStd import TColStd_Array1OfReal, TColStd_Array1OfInteger
from OCP.TColgp import TColgp_Array1OfPnt
from OCP.gp import gp_Pnt


# Description: This appears to be a fastener or spacer component shown in an exploded view, displaying multiple small cylindrical or rounded rectangular elements that could be bushings, grommets, or similar hardware pieces arranged in a scattered pattern.
def model_54726_96c2c7c8_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((-4, -2)):
                Circle(1)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((7, -2)):
                Circle(1)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch3 -> Extrude3 (NewBody)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((7, 17)):
                Circle(1)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch4 -> Extrude4 (NewBody)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((-4, 17)):
                Circle(1)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch14 -> Extrude32 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.5446900494, perimeter: 5.6548667765
            with Locations((-3, 21)):
                Circle(0.9)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch15 -> Extrude33 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.5446900494, perimeter: 5.6548667765
            with Locations((6, 21)):
                Circle(0.9)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch16 -> Extrude34 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.5446900494, perimeter: 5.6548667765
            with Locations((-3, 27)):
                Circle(0.9)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch17 -> Extrude35 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.5446900494, perimeter: 5.6548667765
            with Locations((6, 27)):
                Circle(0.9)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)
    return part.part


# Description: This is a microphone shock mount assembly featuring a cylindrical barrel with a tapered head, designed with internal shock-absorbing mechanisms and elastic suspension elements to isolate microphones from vibration and handling noise.
def model_55021_bf798ad2_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 18 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 52.1908540938, perimeter: 36.3028901057
            with BuildLine():
                CenterArc((4.3475624111, 7.1524375889), 2.3525064277, 86.2847480474, 97.4305039052)
                Line((2.5, 7), (2, 7))
                CenterArc((2.5, 6.5), 0.5, 0, 90)
                Line((3, 5.5), (3, 6.5))
                CenterArc((2.5, 5.5), 0.5, -90, 90)
                Line((1.5, 5), (2.5, 5))
                Line((1.5, 4.5), (1.5, 5))
                CenterArc((1.9230342154, 3.5432585538), 1.046093754, -85.7806813522, 199.6338496403)
                CenterArc((5, 3.05), 3.05, -169.6111421845, 159.2222843691)
                CenterArc((8.3819815048, 3.4670046238), 1.0397152555, 83.4822853033, 164.9629424576)
                Line((8.5, 4.5), (8.5, 5))
                Line((8.5, 5), (8, 5))
                CenterArc((8, 5.5), 0.5, 180, 90)
                Line((7.5, 5.5), (7.5, 6.5))
                CenterArc((8, 6.5), 0.5, 90, 90)
                Line((8, 7), (8.5, 7))
                CenterArc((5.8461538462, 8.1346153846), 2.8862175038, -23.1484629853, 120.0367212623)
                Line((5.5, 9.5), (5.5, 11))
                Line((4.5, 9.5), (5.5, 9.5))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 9.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3647738984, perimeter: 4.7166988284
            with BuildLine():
                Line((-1.3394216772, -4.481072263), (0, -4.481072263))
                Line((-1.3394216772, -5.5), (-1.3394216772, -4.481072263))
                Line((-1, -5.5), (-1.3394216772, -5.5))
                Line((-1, -4.5), (-1, -5.5))
                Line((0, -4.5), (-1, -4.5))
                Line((0, -4.481072263), (0, -4.5))
            make_face()
            # Profile area: 1, perimeter: 4
            with BuildLine():
                Line((0, -5.5), (-1, -5.5))
                Line((0, -4.5), (0, -5.5))
                Line((0, -4.5), (-1, -4.5))
                Line((-1, -4.5), (-1, -5.5))
            make_face()
        # OneSide extrude, distance=25
        extrude(amount=25, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 9.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.018927737, perimeter: 4.0378554739
            with BuildLine():
                Line((-1, -4.481072263), (-1, -5.5))
                Line((0, -5.5), (-1, -5.5))
                Line((0, -4.481072263), (0, -5.5))
                Line((-1, -4.481072263), (0, -4.481072263))
            make_face()
            # Profile area: 0.2831530977, perimeter: 2.5936418902
            with BuildLine():
                Line((-1.2778932081, -4.481072263), (-1, -4.481072263))
                Line((-1.2778932081, -5.5), (-1.2778932081, -4.481072263))
                Line((-1, -5.5), (-1.2778932081, -5.5))
                Line((-1, -4.481072263), (-1, -5.5))
            make_face()
        # OneSide extrude, distance=13
        extrude(amount=13, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 12 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(1, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.8686457627, perimeter: 6.4149645928
            with BuildLine():
                Line((6.3714280255, 2.7597088548), (3.9290332494, 2.7597088548))
                Line((6.3714280255, 3.5247963751), (6.3714280255, 2.7597088548))
                Line((3.9290332494, 3.5247963751), (6.3714280255, 3.5247963751))
                Line((3.9290332494, 2.7597088548), (3.9290332494, 3.5247963751))
            make_face()
            # Profile area: 1.2074187063, perimeter: 4.7023560991
            with BuildLine():
                Line((5.8461538462, 3.7969735563), (4.2527241233, 3.7969735563))
                Line((5.8461538462, 4.5547218831), (5.8461538462, 3.7969735563))
                Line((4.2527241233, 4.5547218831), (5.8461538462, 4.5547218831))
                Line((4.2527241233, 3.7969735563), (4.2527241233, 4.5547218831))
            make_face()
            # Profile area: 1.8294995578, perimeter: 5.9644066133
            with BuildLine():
                Line((6.0477371516, 8.1346153846), (3.9290332494, 8.1346153846))
                Line((6.0477371516, 8.9981147891), (6.0477371516, 8.1346153846))
                Line((3.9290332494, 8.9981147891), (6.0477371516, 8.9981147891))
                Line((3.9290332494, 8.1346153846), (3.9290332494, 8.9981147891))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 22.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4544807725, perimeter: 2.9299320285
            with BuildLine():
                Line((-1.2778932081, -4.481072263), (-1.2778932081, -5.5))
                Line((-1.2778932081, -5.5), (-0.8318549308, -5.5))
                Line((-0.8318549308, -4.481072263), (-0.8318549308, -5.5))
                Line((-0.8318549308, -4.481072263), (-1.2778932081, -4.481072263))
            make_face()
            # Profile area: 1.1647291627, perimeter: 6.5187159551
            with BuildLine():
                Line((-0.8318549308, -4.481072263), (-1.2778932081, -4.481072263))
                Line((-0.8318549308, -3.9669134982), (-0.8318549308, -4.481072263))
                Line((-1.6389466041, -3.9669134982), (-0.8318549308, -3.9669134982))
                Line((-1.6389466041, -5.9731415252), (-1.6389466041, -3.9669134982))
                Line((-0.8318549308, -5.9731415252), (-1.6389466041, -5.9731415252))
                Line((-0.8318549308, -5.5), (-0.8318549308, -5.9731415252))
                Line((-1.2778932081, -5.5), (-0.8318549308, -5.5))
                Line((-1.2778932081, -4.481072263), (-1.2778932081, -5.5))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.ADD)

        # Sketch6 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1.6389466041, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.096211275, perimeter: 1.0995574288
            with Locations((4.4674499494, 24.7987540652)):
                Circle(0.175)
            # Profile area: 0.096211275, perimeter: 1.0995574288
            with Locations((4.4378942667, 24.0007506311)):
                Circle(0.175)
            # Profile area: 0.096211275, perimeter: 1.0995574288
            with Locations((4.4083385839, 23.1288579902)):
                Circle(0.175)
            # Profile area: 0.096211275, perimeter: 1.0995574288
            with Locations((5.4575653213, 23.1731915143)):
                Circle(0.175)
            # Profile area: 0.096211275, perimeter: 1.0995574288
            with Locations((5.5018988454, 23.9859727897)):
                Circle(0.175)
            # Profile area: 0.096211275, perimeter: 1.0995574288
            with Locations((5.4723431627, 24.7987540652)):
                Circle(0.175)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch7 -> Extrude7 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(1.3, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0951482701, perimeter: 1.0934662435
            with Locations((4.381328581, 3.1524743244)):
                Circle(0.1740305578)
            # Profile area: 0.0921035255, perimeter: 1.0758285347
            with Locations((5.1502306375, 3.1369085581)):
                Circle(0.1712234292)
            # Profile area: 0.0989542009, perimeter: 1.1151211426
            with Locations((5.8445106125, 3.1369085581)):
                Circle(0.177477042)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


# Description: This is a wrench or spanner with a long cylindrical shaft featuring open-ended jaws at both ends and rounded flanges, designed for gripping and turning nuts or bolts of different sizes.
def model_55082_55dae462_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 15, perimeter: 23
            with BuildLine():
                Line((10, -1.5), (0, -1.5))
                Line((10, 0), (10, -1.5))
                Line((0, 0), (10, 0))
                Line((0, -1.5), (0, 0))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.9591590609, perimeter: 9.2747933758
            with BuildLine():
                CenterArc((-11, 0.5), 1.4351431288, 44.1703976805, 295.4402838281)
                Line((-10, 0), (-9.6547729559, 0))
                Line((-10, 1.5), (-10, 0))
                Line((-9.9706138721, 1.5), (-10, 1.5))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.4441956889, perimeter: 5.9764767526
            with BuildLine():
                CenterArc((-11, 0.5), 1.4351431288, -164.5187393638, 59.0374787275)
                Line((-11.3830729869, -0.8830729869), (-10.5, 0))
                Line((-10.5, 0), (-10.5, 1))
                Line((-10.5, 1), (-11.5, 1))
                Line((-11.5, 1), (-12.3830729869, 0.1169270131))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.6844736283, perimeter: 18.1390795431
            with BuildLine():
                Line((-9, 1.2526230938), (-1, 1.2526230938))
                Line((-9, 0.3050300003), (-9, 1.2526230938))
                Line((-0.7810687276, 0.3050300003), (-9, 0.3050300003))
                Line((-1, 1.2526230938), (-0.7810687276, 0.3050300003))
            make_face()
        # OneSide extrude, distance=-0.25
        extrude(amount=-0.25, mode=Mode.SUBTRACT)

        # Sketch8 -> Extrude7 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.8823510277, perimeter: 8.692329704
            with BuildLine():
                Line((0, 0), (0, 1.5))
                Line((-0.0112709552, 0), (0, 0))
                CenterArc((1.1705051372, 0.7411625146), 1.3949611484, -147.9057142693, 294.9504071936)
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.ADD)

        # Sketch9 -> Extrude8 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.2119693813, perimeter: 5.5362394118
            with BuildLine():
                Line((1.8050121663, 1.4110791078), (0.9075938636, 1.6256200172))
                Line((0.9075938636, 1.6256200172), (0.2730868346, 0.955703424))
                Line((0.2730868346, 0.955703424), (0.5359981082, 0.0712459214))
                Line((0.5359981082, 0.0712459214), (1.4334164109, -0.1432949881))
                Line((1.4334164109, -0.1432949881), (2.0679234399, 0.5266216051))
                Line((2.0679234399, 0.5266216051), (1.8050121663, 1.4110791078))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch11 -> Extrude9 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 8.4255301457, perimeter: 19.7606389942
            with BuildLine():
                Line((9.5166839181, 1.2428466046), (0.5790719434, 1.2526230938))
                Line((0.5790719434, 1.2526230938), (0.5790719434, 0.3050300003))
                Line((0.5790719434, 0.3050300003), (9.5166839181, 0.3050300003))
                Line((9.5166839181, 0.3050300003), (9.5166839181, 1.2428466046))
            make_face()
        # OneSide extrude, distance=-0.25
        extrude(amount=-0.25, mode=Mode.SUBTRACT)
    return part.part


# Description: This is an oval-shaped enclosure or cover with a domed/curved surface, featuring a central rectangular opening or window and radial ribbing or fin-like structures across its exterior for structural reinforcement and heat dissipation.
def model_55284_834c8e1d_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            with Locations((-3, 3)):
                Circle(2)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-3, 3)):
                Circle(0.5)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.ADD)

        # Sketch6 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-3, 3)):
                Circle(0.5)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


# Description: This is a structural bracket or support frame with a complex angular geometry, featuring a main body with internal ribbing/bracing, two rectangular cutout holes on one side, and a sloped or curved upper surface for load distribution or mounting purposes.
def model_55341_a059c86e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch3 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 49, perimeter: 35
            with BuildLine():
                Line((15.5, 1.5), (1.5, 1.5))
                Line((15.5, 5), (15.5, 1.5))
                Line((1.5, 5), (15.5, 5))
                Line((1.5, 1.5), (1.5, 5))
            make_face()
        # OneSide extrude, distance=22
        extrude(amount=22)

        # Sketch5 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 11 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 55, perimeter: 49
            with BuildLine():
                Line((15.5, 0), (15.5, 22))
                Line((15.5, 22), (13, 22))
                Line((13, 22), (13, 0))
                Line((13, 0), (15.5, 0))
            make_face()
        # OneSide extrude, distance=6
        extrude(amount=6, mode=Mode.ADD)

        # Sketch6 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 55, perimeter: 49
            with BuildLine():
                Line((4, 22), (4, 0))
                Line((1.5, 22), (4, 22))
                Line((1.5, 0), (1.5, 22))
                Line((4, 0), (1.5, 0))
            make_face()
        # OneSide extrude, distance=6
        extrude(amount=6, mode=Mode.ADD)

        # Sketch7 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 308, perimeter: 72
            with BuildLine():
                Line((-1.5, 0), (-1.5, 22))
                Line((-15.5, 22), (-1.5, 22))
                Line((-15.5, 22), (-15.5, 0))
                Line((-1.5, 0), (-15.5, 0))
            make_face()
        # OneSide extrude, distance=6
        extrude(amount=6, mode=Mode.ADD)

        # Sketch9 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 22), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 45, perimeter: 28
            with BuildLine():
                Line((13, 5), (4, 5))
                Line((13, 10), (13, 5))
                Line((4, 10), (13, 10))
                Line((4, 5), (4, 10))
            make_face()
        # OneSide extrude, distance=-22
        extrude(amount=-22, mode=Mode.SUBTRACT)

        # Sketch10 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 20 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 14, perimeter: 18
            with BuildLine():
                Line((-12, 20), (-5, 20))
                Line((-12, 18), (-12, 20))
                Line((-5, 18), (-12, 18))
                Line((-5, 20), (-5, 18))
            make_face()
            # Profile area: 14, perimeter: 18
            with BuildLine():
                Line((-12, 16), (-5, 16))
                Line((-12, 14), (-12, 16))
                Line((-5, 14), (-12, 14))
                Line((-5, 16), (-5, 14))
            make_face()
            # Profile area: 14, perimeter: 18
            with BuildLine():
                Line((-12, 12), (-5, 12))
                Line((-12, 10), (-12, 12))
                Line((-5, 10), (-12, 10))
                Line((-5, 12), (-5, 10))
            make_face()
            # Profile area: 14, perimeter: 18
            with BuildLine():
                Line((-12, 8), (-5, 8))
                Line((-12, 6), (-12, 8))
                Line((-5, 6), (-12, 6))
                Line((-5, 8), (-5, 6))
            make_face()
            # Profile area: 14, perimeter: 18
            with BuildLine():
                Line((-12, 4), (-5, 4))
                Line((-12, 2), (-12, 4))
                Line((-5, 2), (-12, 2))
                Line((-5, 4), (-5, 2))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)
    return part.part


# Description: This is a multi-tiered bracket or mounting plate with three stacked horizontal levels featuring rectangular slots and flanges, designed for structural support or component attachment in an assembly.
def model_55423_a50f82f4_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 60.5, perimeter: 33
            with BuildLine():
                Line((5.5, -3), (-5.5, -3))
                Line((5.5, 2.5), (5.5, -3))
                Line((-5.5, 2.5), (5.5, 2.5))
                Line((-5.5, -3), (-5.5, 2.5))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 30 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(1, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 20.5, perimeter: 24.5
            with BuildLine():
                Line((-4, 1), (-5, 1))
                Line((-5, 1), (-5, -0.25))
                Line((-5, -0.25), (5, -0.25))
                Line((5, -0.25), (5, 1))
                Line((4, 1), (5, 1))
                Line((4, 2), (4, 1))
                Line((-4, 2), (4, 2))
                Line((-4, 2), (-4, 1))
            make_face()
            # Profile area: 20.5, perimeter: 24.5
            with BuildLine():
                Line((-5, -0.25), (-5, -1.5))
                Line((-4, -1.5), (-5, -1.5))
                Line((-4, -2.5), (-4, -1.5))
                Line((-4, -2.5), (4, -2.5))
                Line((4, -1.5), (4, -2.5))
                Line((5, -1.5), (4, -1.5))
                Line((5, -1.5), (5, -0.25))
                Line((-5, -0.25), (5, -0.25))
            make_face()
        # OneSide extrude, distance=2.5
        extrude(amount=2.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 23 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(1, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1, perimeter: 4
            with BuildLine():
                Line((-4, 1), (-4, 2))
                Line((-4, 2), (-5, 2))
                Line((-5, 2), (-5, 1))
                Line((-5, 1), (-4, 1))
            make_face()
            # Profile area: 1, perimeter: 4
            with BuildLine():
                Line((-5, -2.5), (-5, -1.5))
                Line((-4, -2.5), (-5, -2.5))
                Line((-4, -1.5), (-4, -2.5))
                Line((-5, -1.5), (-4, -1.5))
            make_face()
            # Profile area: 1, perimeter: 4
            with BuildLine():
                Line((5, 2), (5, 1))
                Line((4, 2), (5, 2))
                Line((4, 1), (4, 2))
                Line((5, 1), (4, 1))
            make_face()
            # Profile area: 1, perimeter: 4
            with BuildLine():
                Line((5, -2.5), (4, -2.5))
                Line((5, -1.5), (5, -2.5))
                Line((4, -1.5), (5, -1.5))
                Line((4, -2.5), (4, -1.5))
            make_face()
        # OneSide extrude, distance=8
        extrude(amount=8, mode=Mode.ADD)

        # Sketch6 -> Extrude4 (NewBody)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 60.5, perimeter: 33
            with BuildLine():
                Line((7, 15.5), (18, 15.5))
                Line((7, 10), (7, 15.5))
                Line((18, 10), (7, 10))
                Line((18, 15.5), (18, 10))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch7 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.5, perimeter: 11
            with BuildLine():
                Line((-1, -1), (-3.5, -1))
                Line((-3.5, -1), (-3.5, -4))
                Line((-3.5, -4), (-1, -4))
                Line((-1, -4), (-1, -1))
            make_face()
            # Profile area: 7.5, perimeter: 11
            with BuildLine():
                Line((-3.5, 4), (-1, 4))
                Line((-3.5, 1), (-3.5, 4))
                Line((-1, 1), (-3.5, 1))
                Line((-1, 4), (-1, 1))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch8 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-2.25, 2.4571570998)):
                Circle(0.25)
        # OneSide extrude, distance=0.25
        extrude(amount=0.25, mode=Mode.ADD)

        # Sketch9 -> Extrude7 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((4.5, -0.5)):
                Circle(0.25)
        # OneSide extrude, distance=0.25
        extrude(amount=0.25)
    return part.part


# Description: This is a toroidal (doughnut-shaped) component with a large central hole and a smooth, rounded outer surface, featuring a wireframe mesh visualization that highlights its symmetrical, ring-like geometry.
def model_55605_2f8bc12e_0010():
    """Model: rollcage new v1"""
    with BuildPart() as part:
        # C_BEARING AXLE -> Extrude13 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 6 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 14.567879294, perimeter: 23.6876086081
            with BuildLine():
                CenterArc((-155, 5), 2.5, 0, 180.0000389852)
                CenterArc((-155, 5), 2.5, -179.9999610148, 179.9999610148)
            make_face()
            with BuildLine():
                CenterArc((-155, 5), 1.27, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=1
        extrude(amount=1, both=True)
    return part.part


# Description: This is a cylindrical motor or actuator housing with a domed, mesh-textured top cover, a solid base with a split or notched bottom section, and curved ribbed side panels that provide structural reinforcement.
def model_55611_69142616_0017():
    """Model: crankcase 2"""
    with BuildPart() as part:
        # Sketch10 -> Extrude9 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 22.3838476568, perimeter: 32.8451302091
            with BuildLine():
                CenterArc((10, 12.5), 5.5, 0, 180)
                Line((6, 12.5), (4.5, 12.5))
                CenterArc((10, 12.5), 4, 0, 180)
                Line((15.5, 12.5), (14, 12.5))
            make_face()
        # OneSide extrude, distance=11
        extrude(amount=11)

        # Sketch11 -> Extrude10 (Join)
        # Sketch on BRepFace
        # Sketch has 9 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 11), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.5116111894, perimeter: 5.051657841
            with BuildLine():
                CenterArc((10, 12.5), 4, 165.5224878141, 14.4775121859)
                Line((6.1270166538, 13.5), (4.5916730868, 13.5))
                CenterArc((10, 12.5), 5.5, 169.5243183036, 10.4756816964)
                Line((4.5, 12.5), (6, 12.5))
            make_face()
            # Profile area: 1.5304550964, perimeter: 5.0972663403
            with BuildLine():
                CenterArc((10, 12.5), 5.5, 169.5243183036, 10.4756816964)
                Line((4.5916730868, 13.5), (3, 13.5))
                Line((3, 13.5), (3, 12.5))
                Line((3, 12.5), (4.5, 12.5))
            make_face()
            # Profile area: 1.5304550964, perimeter: 5.0972663403
            with BuildLine():
                CenterArc((10, 12.5), 5.5, 0, 10.4756816964)
                Line((15.5, 12.5), (17, 12.5))
                Line((17, 12.5), (17, 13.5))
                Line((17, 13.5), (15.4083269132, 13.5))
            make_face()
            # Profile area: 1.5116111894, perimeter: 5.051657841
            with BuildLine():
                Line((14, 12.5), (15.5, 12.5))
                CenterArc((10, 12.5), 5.5, 0, 10.4756816964)
                Line((15.4083269132, 13.5), (13.8729833462, 13.5))
                CenterArc((10, 12.5), 4, 0, 14.4775121859)
            make_face()
        # OneSide extrude, distance=-11
        extrude(amount=-11, mode=Mode.ADD)

        # Sketch12 -> Extrude11 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 11), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 25.1327412287, perimeter: 20.5663706144
            with BuildLine():
                CenterArc((10, 12.5), 4, 0, 180)
                Line((14, 12.5), (6, 12.5))
            make_face()
        # OneSide extrude, distance=-3.5
        extrude(amount=-3.5, mode=Mode.ADD)

        # Sketch13 -> Extrude12 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 25.1327412287, perimeter: 20.5663706144
            with BuildLine():
                CenterArc((-10, 12.5), 4, 0, 180)
                Line((-6, 12.5), (-14, 12.5))
            make_face()
        # OneSide extrude, distance=-3.5
        extrude(amount=-3.5, mode=Mode.ADD)

        # Sketch14 -> Extrude13 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 1.5707963268, perimeter: 5.1415926536
            with BuildLine():
                CenterArc((-10, 12.5), 1, 0, 180)
                Line((-11, 12.5), (-9, 12.5))
            make_face()
        # OneSide extrude, distance=-13
        extrude(amount=-13, mode=Mode.SUBTRACT)

        # Sketch19 -> Extrude19 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 13.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-3.7863183826, 10.3821786108)):
                Circle(0.3)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-3.7863183826, 0.6178215532)):
                Circle(0.3)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-16.2136816621, 0.6178215532)):
                Circle(0.3)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-16.2136816621, 10.3821786108)):
                Circle(0.3)
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)

        # Sketch20 -> Extrude20 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 11), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((7.5251262658, 14.9748737342)):
                Circle(0.4)
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((12.4748737342, 14.9748737342)):
                Circle(0.4)
        # OneSide extrude, distance=-0.6
        extrude(amount=-0.6, mode=Mode.SUBTRACT)

        # Sketch21 -> Extrude21 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 11), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.0122637093, perimeter: 7.3500848106
            with BuildLine():
                CenterArc((10, 12.5), 3.8, 63.3483192192, 53.3033615617)
                Line((8.2954513565, 15.8962499793), (8.449225122, 15.6376897995))
                CenterArc((10, 12.5), 3.5, 63.6995305217, 52.6009389566)
                Line((11.7045486435, 15.8962499793), (11.550774878, 15.6376897995))
            make_face()
        # OneSide extrude, distance=0.8
        extrude(amount=0.8, mode=Mode.ADD)
    return part.part


# Description: This is a dark blue triangular bracket or mounting block with an angular, wedge-like shape featuring a vertical slot or opening on one side and a protruding flange or lip, designed for structural support or component attachment.
def model_55749_6526b76b_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 97.5316522068, perimeter: 47.9395017172
            with BuildLine():
                Line((-7.3481202675, 7.3481202675), (-7.3481202675, -6.4449382637))
                Line((-7.3481202675, -6.4449382637), (6.7940153562, -6.7940153562))
                Line((-7.3481202675, 7.3481202675), (6.7940153562, -6.7940153562))
            make_face()
        # TwoSides extrude (symmetric), distance=5
        extrude(amount=5, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(0.7071067812, 0.7071067812, 0))):
            # Profile area: 84.2567378781, perimeter: 48.4287547742
            with BuildLine():
                Line((-2.0676871474, 10.3918113402), (-2.4138983069, -9.6081886598))
                Line((-2.4138983069, -9.6081886598), (1.9429483254, -9.6081886598))
                Line((1.9429483254, -9.6081886598), (2.0011400081, 10.3918113402))
                Line((2.0011400081, 10.3918113402), (-2.0676871474, 10.3918113402))
            make_face()
        # OneSide extrude, distance=-10
        extrude(amount=-10, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane.XY) as sk:
            # Profile area: 3.3063461811, perimeter: 9.4894246797
            with BuildLine():
                Line((0, -1.2073946851), (2.6217962673, -3.8291909524))
                Line((2.6217962673, -3.8291909524), (3.3893428823, -3.3893428823))
                Line((0.5343116931, -0.5343116931), (3.3893428823, -3.3893428823))
                Line((0.5343116931, -0.5343116931), (0, -1.2073946851))
            make_face()
        # TwoSides extrude, along=2, against=-1.7
        extrude(amount=2)
        extrude(sk.sketch, amount=-1.7)

        # Sketch4 -> Extrude4 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane.XY) as sk:
            # Profile area: 2.6055315597, perimeter: 9.9188468572
            with BuildLine():
                Line((-2.1813920401, 3.2324209114), (-1, 3))
                Line((-1, 3), (-4.336334408, 6.336334408))
                Line((-4.336334408, 6.336334408), (-4.336334408, 5.3873632793))
                Line((-4.336334408, 5.3873632793), (-2.1813920401, 3.2324209114))
            make_face()
        # TwoSides extrude, along=2, against=-1.7
        extrude(amount=2)
        extrude(sk.sketch, amount=-1.7)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on XY construction plane
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 16.2399986112, perimeter: 34.8415004441
            with BuildLine():
                Line((0.570062324, -3.0207292678), (1.0869472561, -2.2943419412))
                Line((1.0869472561, -2.2943419412), (-3.9058126586, 2.6984179735))
                Line((-3.9058126586, 2.6984179735), (-2.7766008804, 3.8276297518))
                Line((-2.7766008804, 3.8276297518), (-3.7063254752, 4.7573543465))
                Line((-3.7063254752, 4.7573543465), (-4.8730873627, 3.590592459))
                Line((-4.8730873627, 3.590592459), (-10, 8))
                Line((-10, 8), (-10, 7))
                Line((-10, 7), (0.570062324, -3.0207292678))
            make_face()
        # TwoSides extrude (symmetric), distance=0.5
        extrude(amount=0.5, both=True, mode=Mode.ADD)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on XY construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4.3884800718, perimeter: 7.4261205899
            with Locations((-10, 7.5)):
                Circle(1.1819037999)
        # TwoSides extrude (symmetric), distance=0.5
        extrude(amount=0.5, both=True, taper=-5, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude7 (Join)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.9436390964, perimeter: 6.0820111674
            with Locations((-9.8626330468, 7.3778147136)):
                Circle(0.9679821412)
        # TwoSides extrude (symmetric), distance=0.5
        extrude(amount=0.5, both=True, mode=Mode.ADD)

        # Sketch8 -> Extrude8 (Join)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 1.8517383223, perimeter: 5.7279055326
            with BuildLine():
                Line((-8.9391702846, 0.5), (-8.9391702846, 1.4860862178))
                Line((-8.9391702846, 1.4860862178), (-10.8170368332, 1.4860862178))
                Line((-10.8170368332, 1.4860862178), (-10.8170368332, 0.5))
                Line((-8.9391702846, 0.5), (-10.8170368332, 0.5))
            make_face()
            # Profile area: 1.8035558508, perimeter: 5.6071117016
            with BuildLine():
                Line((-9, -1.5), (-10.8035558508, -1.5))
                Line((-9, -0.5), (-9, -1.5))
                Line((-10.8035558508, -0.5), (-9, -0.5))
                Line((-10.8035558508, -1.5), (-10.8035558508, -0.5))
            make_face()
        # TwoSides extrude, along=9, against=-7
        extrude(amount=9, mode=Mode.ADD)
        extrude(sk.sketch, amount=-7, mode=Mode.ADD)
    return part.part


# Description: This is a rectangular magazine body with a long, narrow profile, featuring a central loading slot and reinforced top and bottom ends, designed to hold and feed ammunition rounds.
def model_57140_c8f10944_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 225, perimeter: 60
            with BuildLine():
                Line((14, -14.5), (-1, -14.5))
                Line((14, 0.5), (14, -14.5))
                Line((-1, 0.5), (14, 0.5))
                Line((-1, -14.5), (-1, 0.5))
            make_face()
        # OneSide extrude, distance=100
        extrude(amount=100)

        # Sketch11 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(14, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 74.5088929763, perimeter: 149.0177859526
            with BuildLine():
                Line((0.2, 0.3), (-14.5, 0.3))
                Line((0.2, 24.8544464881), (0.2, 0.3))
                Line((-14.5, 24.8544464881), (0.2, 24.8544464881))
                Line((-14.5, 24.8544464881), (-14.5, 0.3))
            make_face()
            with BuildLine():
                Line((-0.8, 23.8544464881), (-0.8, 1.3))
                Line((-0.8, 1.3), (-13.5, 1.3))
                Line((-13.5, 1.3), (-13.5, 23.8544464881))
                Line((-13.5, 23.8544464881), (-0.8, 23.8544464881))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch10 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 14.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 73.9088929763, perimeter: 147.8177859526
            with BuildLine():
                Line((-0.7, 24.8544464881), (-0.7, 0.3))
                Line((-0.7, 0.3), (13.7, 0.3))
                Line((13.7, 0.3), (13.7, 24.8544464881))
                Line((13.7, 24.8544464881), (-0.7, 24.8544464881))
            make_face()
            with BuildLine():
                Line((12.7, 23.8544464881), (0.3, 23.8544464881))
                Line((12.7, 1.3), (12.7, 23.8544464881))
                Line((0.3, 1.3), (12.7, 1.3))
                Line((0.3, 23.8544464881), (0.3, 1.3))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch12 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.5), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 73.9088929763, perimeter: 147.8177859526
            with BuildLine():
                Line((0.7, 0.3), (-13.7, 0.3))
                Line((0.7, 24.8544464881), (0.7, 0.3))
                Line((-13.7, 24.8544464881), (0.7, 24.8544464881))
                Line((-13.7, 0.3), (-13.7, 24.8544464881))
            make_face()
            with BuildLine():
                Line((-0.3, 23.8544464881), (-0.3, 1.3))
                Line((-0.3, 1.3), (-12.7, 1.3))
                Line((-12.7, 1.3), (-12.7, 23.8544464881))
                Line((-12.7, 23.8544464881), (-0.3, 23.8544464881))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch16 -> Extrude9 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.5), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 155.8573505004, perimeter: 53.9088929763
            with BuildLine():
                Line((-10.7, 21.8544464881), (-10.7, 3.3))
                Line((-10.7, 3.3), (-2.3, 3.3))
                Line((-2.3, 3.3), (-2.3, 21.8544464881))
                Line((-2.3, 21.8544464881), (-10.7, 21.8544464881))
            make_face()
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.SUBTRACT)

        # Sketch14 -> Extrude11 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 14.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 155.8573505004, perimeter: 53.9088929763
            with BuildLine():
                Line((2.3, 21.8544464881), (2.3, 3.3))
                Line((2.3, 3.3), (10.7, 3.3))
                Line((10.7, 3.3), (10.7, 21.8544464881))
                Line((10.7, 21.8544464881), (2.3, 21.8544464881))
            make_face()
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.SUBTRACT)

        # Sketch15 -> Extrude12 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(14, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 161.4236844468, perimeter: 54.5088929763
            with BuildLine():
                Line((-11.5, 21.8544464881), (-11.5, 3.3))
                Line((-11.5, 3.3), (-2.8, 3.3))
                Line((-2.8, 3.3), (-2.8, 21.8544464881))
                Line((-2.8, 21.8544464881), (-11.5, 21.8544464881))
            make_face()
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a marker or highlighter pen with a cylindrical barrel body, a detachable cap on top, and a tapered tip designed for writing or marking.
def model_57830_d9dbe398_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch6 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0044178647, perimeter: 0.235619449
            Circle(0.0375)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch7 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0078539816, perimeter: 0.6283185307
            with BuildLine():
                CenterArc((0, 0), 0.0625, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.0375, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0044178647, perimeter: 0.235619449
            Circle(0.0375)
        # OneSide extrude, distance=0.0255
        extrude(amount=0.0255, mode=Mode.ADD)

        # Sketch8 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.1255), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0053996124, perimeter: 0.8639379797
            with BuildLine():
                CenterArc((0, 0), 0.075, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.0625, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0122718463, perimeter: 0.3926990817
            Circle(0.0625)
        # OneSide extrude, distance=0.599
        extrude(amount=0.599, mode=Mode.ADD)

        # Sketch9 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.7245), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0122718463, perimeter: 0.3926990817
            Circle(0.0625)
        # OneSide extrude, distance=0.0255
        extrude(amount=0.0255, mode=Mode.ADD)

        # Sketch10 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.75), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0044178647, perimeter: 0.235619449
            Circle(0.0375)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch11 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.85), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0019634954, perimeter: 0.1570796327
            Circle(0.025)
        # OneSide extrude, distance=0.15
        extrude(amount=0.15, mode=Mode.ADD)

        # Sketch12 -> Extrude7 (NewBody)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0097163376, perimeter: 0.349426816
            with Locations((0, 0.1706129111)):
                Circle(0.055613005)
        # OneSide extrude, distance=0.125
        extrude(amount=0.125)

        # Sketch13 -> Extrude8 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.125, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0216995889, perimeter: 0.9777453468
            with BuildLine():
                CenterArc((0, -0.1706129111), 0.1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, -0.1706129111), 0.055613005, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0097163376, perimeter: 0.349426816
            with Locations((0, -0.1706129111)):
                Circle(0.055613005)
        # OneSide extrude, distance=0.25
        extrude(amount=0.25, mode=Mode.ADD)
    return part.part


# Description: This is a modular electronic enclosure system consisting of a larger hexagonal/trapezoidal main chassis with internal ventilation fans and a smaller rectangular power supply or accessory module, both featuring mesh vents, mounting brackets, and connection interfaces for component assembly.
def model_57837_62fa414f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 27 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 10, perimeter: 41.0000001639
            with BuildLine():
                Line((0.5, -0.5), (9.5, -0.5))
                Line((9.5, -0.5), (9.5, -5))
                Line((9.5, -5), (9.5, -5.500000082))
                Line((10, -5.5), (9.5, -5.500000082))
                Line((10, 0), (10, -5.5))
                Line((0, 0), (10, 0))
                Line((0, -5.5), (0, 0))
                Line((0.5, -5.500000082), (0, -5.5))
                Line((0.5, -5), (0.5, -5.500000082))
                Line((0.5, -5), (0.5, -0.5))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 27 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.2710607185, perimeter: 13.4807656489
            with BuildLine():
                Line((1, -2.75), (1, -1))
                Line((1.2649103052, -2.75), (1, -2.75))
                CenterArc((3, -2.75), 1.7350896948, 0, 180)
                Line((5, -2.75), (4.7350896948, -2.75))
                Line((5, -2.75), (5, -1))
                Line((1, -1), (5, -1))
            make_face()
            # Profile area: 12.5, perimeter: 50
            with BuildLine():
                Line((0.5, -5), (0.5, -0.5))
                Line((9.5, -5), (0.5, -5))
                Line((9.5, -0.5), (9.5, -5))
                Line((0.5, -0.5), (9.5, -0.5))
            make_face()
            with BuildLine():
                Line((1, -1), (5, -1))
                Line((5, -1), (9, -1))
                Line((9, -1), (9, -2.75))
                Line((9, -2.75), (9, -4.5))
                Line((9, -4.5), (5, -4.5))
                Line((5, -4.5), (1, -4.5))
                Line((1, -4.5), (1, -2.75))
                Line((1, -2.75), (1, -1))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 2.2710607185, perimeter: 13.4807656489
            with BuildLine():
                Line((1, -4.5), (1, -2.75))
                Line((5, -4.5), (1, -4.5))
                Line((5, -4.5), (5, -2.75))
                Line((5, -2.75), (4.7350896948, -2.75))
                CenterArc((3, -2.75), 1.7350896948, 180, 180)
                Line((1.2649103052, -2.75), (1, -2.75))
            make_face()
            # Profile area: 2.3293346768, perimeter: 13.4685234891
            with BuildLine():
                Line((5, -2.75), (5.2756340601, -2.75))
                CenterArc((7, -2.75), 1.7243659399, 0, 180)
                Line((8.7243659399, -2.75), (9, -2.75))
                Line((9, -1), (9, -2.75))
                Line((5, -1), (9, -1))
                Line((5, -2.75), (5, -1))
            make_face()
            # Profile area: 2.3293346768, perimeter: 13.4685234891
            with BuildLine():
                Line((5, -4.5), (5, -2.75))
                Line((9, -4.5), (5, -4.5))
                Line((9, -2.75), (9, -4.5))
                Line((8.7243659399, -2.75), (9, -2.75))
                CenterArc((7, -2.75), 1.7243659399, 180, 180)
                Line((5, -2.75), (5.2756340601, -2.75))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 27 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.2710607185, perimeter: 13.4807656489
            with BuildLine():
                Line((1, -2.75), (1, -1))
                Line((1.2649103052, -2.75), (1, -2.75))
                CenterArc((3, -2.75), 1.7350896948, 0, 180)
                Line((5, -2.75), (4.7350896948, -2.75))
                Line((5, -2.75), (5, -1))
                Line((1, -1), (5, -1))
            make_face()
            # Profile area: 2.2710607185, perimeter: 13.4807656489
            with BuildLine():
                Line((1, -4.5), (1, -2.75))
                Line((5, -4.5), (1, -4.5))
                Line((5, -4.5), (5, -2.75))
                Line((5, -2.75), (4.7350896948, -2.75))
                CenterArc((3, -2.75), 1.7350896948, 180, 180)
                Line((1.2649103052, -2.75), (1, -2.75))
            make_face()
            # Profile area: 2.3293346768, perimeter: 13.4685234891
            with BuildLine():
                Line((5, -2.75), (5.2756340601, -2.75))
                CenterArc((7, -2.75), 1.7243659399, 0, 180)
                Line((8.7243659399, -2.75), (9, -2.75))
                Line((9, -1), (9, -2.75))
                Line((5, -1), (9, -1))
                Line((5, -2.75), (5, -1))
            make_face()
            # Profile area: 2.3293346768, perimeter: 13.4685234891
            with BuildLine():
                Line((5, -4.5), (5, -2.75))
                Line((9, -4.5), (5, -4.5))
                Line((9, -2.75), (9, -4.5))
                Line((8.7243659399, -2.75), (9, -2.75))
                CenterArc((7, -2.75), 1.7243659399, 180, 180)
                Line((5, -2.75), (5.2756340601, -2.75))
            make_face()
        # OneSide extrude, distance=1.3
        extrude(amount=1.3, mode=Mode.ADD)

        # Sketch1 -> Extrude4 (Join)
        # Sketch on XZ construction plane
        # Sketch has 27 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.7289392815, perimeter: 8.921124428
            with BuildLine():
                Line((4.7350896948, -2.75), (1.2649103052, -2.75))
                CenterArc((3, -2.75), 1.7350896948, 0, 180)
            make_face()
            # Profile area: 4.7289392815, perimeter: 8.921124428
            with BuildLine():
                CenterArc((3, -2.75), 1.7350896948, 180, 180)
                Line((4.7350896948, -2.75), (1.2649103052, -2.75))
            make_face()
            # Profile area: 4.6706653232, perimeter: 8.8659872489
            with BuildLine():
                CenterArc((7, -2.75), 1.7243659399, 0, 180)
                Line((5.2756340601, -2.75), (8.7243659399, -2.75))
            make_face()
            # Profile area: 4.6706653232, perimeter: 8.8659872489
            with BuildLine():
                Line((5.2756340601, -2.75), (8.7243659399, -2.75))
                CenterArc((7, -2.75), 1.7243659399, 180, 180)
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)

        # Sketch3 -> Extrude6 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 17 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.2042108157, perimeter: 28.8658895737
            with BuildLine():
                Line((7.4731917148, -8.5967834761), (9.4329447869, -8.5967834761))
                Line((9.4329447869, -8.5967834761), (9.4329447869, -10.4912114458))
                Line((9.4329447869, -10.4912114458), (9.4329447869, -12.3856394154))
                Line((9.4329447869, -12.3856394154), (7.4731917148, -12.3856394154))
                Line((7.4731917148, -12.3856394154), (5.5134386427, -12.3856394154))
                Line((5.5134386427, -12.3856394154), (5, -12.3856394154))
                Line((5, -12.3856394154), (5, -13))
                Line((5, -13), (10, -13))
                Line((10, -13), (10, -8))
                Line((10, -8), (5, -8))
                Line((5, -8), (5, -8.5967834761))
                Line((5.5134386427, -8.5967834761), (5, -8.5967834761))
                Line((5.5134386427, -8.5967834761), (7.4731917148, -8.5967834761))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch3 -> Extrude7 (Join)
        # Sketch on XZ construction plane
        # Sketch has 17 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.0349637213, perimeter: 6.9158695559
            with BuildLine():
                Line((9.31961703, -10.4912114458), (9.4329447869, -10.4912114458))
                CenterArc((7.4731917148, -10.4912114458), 1.8464253152, -90, 90)
                Line((7.4731917148, -12.3376367609), (7.4731917148, -12.3856394154))
                Line((9.4329447869, -12.3856394154), (7.4731917148, -12.3856394154))
                Line((9.4329447869, -10.4912114458), (9.4329447869, -12.3856394154))
            make_face()
            # Profile area: 1.0349637213, perimeter: 6.9158695559
            with BuildLine():
                Line((7.4731917148, -8.5967834761), (7.4731917148, -8.6447861306))
                CenterArc((7.4731917148, -10.4912114458), 1.8464253152, 0, 90)
                Line((9.31961703, -10.4912114458), (9.4329447869, -10.4912114458))
                Line((9.4329447869, -8.5967834761), (9.4329447869, -10.4912114458))
                Line((7.4731917148, -8.5967834761), (9.4329447869, -8.5967834761))
            make_face()
            # Profile area: 1.0349637213, perimeter: 6.9158695559
            with BuildLine():
                Line((7.4731917148, -12.3376367609), (7.4731917148, -12.3856394154))
                CenterArc((7.4731917148, -10.4912114458), 1.8464253152, 180, 90)
                Line((5.5134386427, -10.4912114458), (5.6267663996, -10.4912114458))
                Line((5.5134386427, -12.3856394154), (5.5134386427, -10.4912114458))
                Line((7.4731917148, -12.3856394154), (5.5134386427, -12.3856394154))
            make_face()
            # Profile area: 1.0349637213, perimeter: 6.9158695559
            with BuildLine():
                Line((5.5134386427, -8.5967834761), (7.4731917148, -8.5967834761))
                Line((5.5134386427, -10.4912114458), (5.5134386427, -8.5967834761))
                Line((5.5134386427, -10.4912114458), (5.6267663996, -10.4912114458))
                CenterArc((7.4731917148, -10.4912114458), 1.8464253152, 90, 90)
                Line((7.4731917148, -8.5967834761), (7.4731917148, -8.6447861306))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)

        # Sketch3 -> Extrude8 (Join)
        # Sketch on XZ construction plane
        # Sketch has 17 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.945345051, perimeter: 8.6045891641
            with BuildLine():
                Line((5.5134386427, -12.3856394154), (5.5134386427, -10.4912114458))
                Line((5.5134386427, -10.4912114458), (5.5134386427, -8.5967834761))
                Line((5.5134386427, -8.5967834761), (5, -8.5967834761))
                Line((5, -8.5967834761), (5, -12.3856394154))
                Line((5.5134386427, -12.3856394154), (5, -12.3856394154))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch3 -> Extrude9 (Join)
        # Sketch on XZ construction plane
        # Sketch has 17 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.677647312, perimeter: 6.5932087332
            with BuildLine():
                CenterArc((7.4731917148, -10.4912114458), 1.8464253152, 180, 90)
                Line((7.4731917148, -10.4912114458), (7.4731917148, -12.3376367609))
                Line((5.6267663996, -10.4912114458), (7.4731917148, -10.4912114458))
            make_face()
            # Profile area: 2.677647312, perimeter: 6.5932087332
            with BuildLine():
                CenterArc((7.4731917148, -10.4912114458), 1.8464253152, 90, 90)
                Line((5.6267663996, -10.4912114458), (7.4731917148, -10.4912114458))
                Line((7.4731917148, -8.6447861306), (7.4731917148, -10.4912114458))
            make_face()
            # Profile area: 2.677647312, perimeter: 6.5932087332
            with BuildLine():
                Line((7.4731917148, -10.4912114458), (9.31961703, -10.4912114458))
                Line((7.4731917148, -10.4912114458), (7.4731917148, -12.3376367609))
                CenterArc((7.4731917148, -10.4912114458), 1.8464253152, -90, 90)
            make_face()
            # Profile area: 2.677647312, perimeter: 6.5932087332
            with BuildLine():
                Line((7.4731917148, -8.6447861306), (7.4731917148, -10.4912114458))
                Line((7.4731917148, -10.4912114458), (9.31961703, -10.4912114458))
                CenterArc((7.4731917148, -10.4912114458), 1.8464253152, 0, 90)
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)

        # Sketch4 -> Extrude10 (Join)
        # Sketch on BRepFace
        # Sketch has 16 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.8100000241, perimeter: 3.6000000536
            with BuildLine():
                Line((-7.4000001103, 10.400000155), (-6.5000000969, 10.400000155))
                Line((-7.4000001103, 9.5000001416), (-7.4000001103, 10.400000155))
                Line((-6.5000000969, 9.5000001416), (-7.4000001103, 9.5000001416))
                Line((-6.5000000969, 10.400000155), (-6.5000000969, 9.5000001416))
            make_face()
            # Profile area: 0.7200000215, perimeter: 3.4000000507
            with BuildLine():
                Line((-8.4000001252, 10.400000155), (-7.6000001132, 10.400000155))
                Line((-8.4000001252, 9.5000001416), (-8.4000001252, 10.400000155))
                Line((-7.6000001132, 9.5000001416), (-8.4000001252, 9.5000001416))
                Line((-7.6000001132, 10.400000155), (-7.6000001132, 9.5000001416))
            make_face()
            # Profile area: 0.7200000215, perimeter: 3.4000000507
            with BuildLine():
                Line((-7.4000001103, 11.5000001714), (-6.5000000969, 11.5000001714))
                Line((-7.4000001103, 10.7000001594), (-7.4000001103, 11.5000001714))
                Line((-6.5000000969, 10.7000001594), (-7.4000001103, 10.7000001594))
                Line((-6.5000000969, 11.5000001714), (-6.5000000969, 10.7000001594))
            make_face()
            # Profile area: 0.6400000191, perimeter: 3.2000000477
            with BuildLine():
                Line((-8.4000001252, 11.5000001714), (-7.6000001132, 11.5000001714))
                Line((-8.4000001252, 10.7000001594), (-8.4000001252, 11.5000001714))
                Line((-7.6000001132, 10.7000001594), (-8.4000001252, 10.7000001594))
                Line((-7.6000001132, 11.5000001714), (-7.6000001132, 10.7000001594))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch5 -> Extrude11 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.7, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4900000146, perimeter: 2.8000000417
            with BuildLine():
                Line((-7.3000001088, 10.3000001535), (-6.6000000983, 10.3000001535))
                Line((-7.3000001088, 9.6000001431), (-7.3000001088, 10.3000001535))
                Line((-6.6000000983, 9.6000001431), (-7.3000001088, 9.6000001431))
                Line((-6.6000000983, 10.3000001535), (-6.6000000983, 9.6000001431))
            make_face()

        # Sketch6 -> Extrude11 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.7, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4200000125, perimeter: 2.6000000387
            with BuildLine():
                Line((-8.3000001237, 10.3000001535), (-7.7000001147, 10.3000001535))
                Line((-8.3000001237, 9.6000001431), (-8.3000001237, 10.3000001535))
                Line((-7.7000001147, 9.6000001431), (-8.3000001237, 9.6000001431))
                Line((-7.7000001147, 10.3000001535), (-7.7000001147, 9.6000001431))
            make_face()

        # Sketch7 -> Extrude11 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.7, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4200000125, perimeter: 2.6000000387
            with BuildLine():
                Line((-7.3000001088, 11.4000001699), (-6.6000000983, 11.4000001699))
                Line((-7.3000001088, 10.8000001609), (-7.3000001088, 11.4000001699))
                Line((-6.6000000983, 10.8000001609), (-7.3000001088, 10.8000001609))
                Line((-6.6000000983, 11.4000001699), (-6.6000000983, 10.8000001609))
            make_face()

        # Sketch8 -> Extrude11 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.7, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3600000107, perimeter: 2.4000000358
            with BuildLine():
                Line((-8.3000001237, 11.4000001699), (-7.7000001147, 11.4000001699))
                Line((-8.3000001237, 10.8000001609), (-8.3000001237, 11.4000001699))
                Line((-7.7000001147, 10.8000001609), (-8.3000001237, 10.8000001609))
                Line((-7.7000001147, 11.4000001699), (-7.7000001147, 10.8000001609))
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a plastic mounting bracket or connector assembly with a rectangular main body featuring a curved front section, vertical flanges on the sides, ventilation slots or ribbing patterns, and an angled top section designed for component attachment or alignment.
def model_60975_54324202_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 64.4026493986, perimeter: 28.4483314254
            Circle(4.5276925691)
        # OneSide extrude, distance=6
        extrude(amount=6)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.5942180339, perimeter: 12.4824103051
            with BuildLine():
                Line((2, -2.7412051525), (-1.5, -2.7412051525))
                Line((2, 0), (2, -2.7412051525))
                Line((-1.5, 0), (2, 0))
                Line((-1.5, -2.7412051525), (-1.5, 0))
            make_face()
        # OneSide extrude, distance=6.5
        extrude(amount=6.5, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.4057819661, perimeter: 13.5175896949
            with BuildLine():
                Line((-1.5, -6), (-1.5, -2.7412051525))
                Line((2, -6), (-1.5, -6))
                Line((2, -2.7412051525), (2, -6))
                Line((2, -2.7412051525), (-1.5, -2.7412051525))
            make_face()
        # OneSide extrude, distance=14
        extrude(amount=14, mode=Mode.ADD)

        # Sketch3 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.4167904507, perimeter: 11.4344288851
            with BuildLine():
                Line((1.5, -2), (1.5, -4.2720018727))
                Line((-2, -2), (1.5, -2))
                Line((-2, -4.0620192023), (-2, -2))
                CenterArc((0, 0), 4.5276925691, -116.2140653402, 45.5614353011)
            make_face()
        # OneSide extrude, distance=-6.5
        extrude(amount=-6.5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 31 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -2), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 5.25, perimeter: 10
            with BuildLine():
                Line((1.5, 5.5), (-2, 5.5))
                Line((-2, 4), (-2, 5.5))
                Line((-2, 4), (1.5, 4))
                Line((1.5, 5.5), (1.5, 4))
            make_face()
            # Profile area: 5.25, perimeter: 10
            with BuildLine():
                Line((1.5, 3.5), (-2, 3.5))
                Line((-2, 2), (-2, 3.5))
                Line((-2, 2), (1.5, 2))
                Line((1.5, 3.5), (1.5, 2))
            make_face()
            # Profile area: 5.25, perimeter: 10
            with BuildLine():
                Line((1.5, 1.5), (-2, 1.5))
                Line((-2, 0), (-2, 1.5))
                Line((1.5, 0), (-2, 0))
                Line((1.5, 1.5), (1.5, 0))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)

        # Sketch4 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 31 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -2), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 1.75, perimeter: 8
            with BuildLine():
                Line((1.5, 6), (1.5, 5.5))
                Line((-2, 6), (1.5, 6))
                Line((-2, 5.5), (-2, 6))
                Line((1.5, 5.5), (-2, 5.5))
            make_face()
            # Profile area: 1.75, perimeter: 8
            with BuildLine():
                Line((-2, 4), (1.5, 4))
                Line((-2, 3.5), (-2, 4))
                Line((1.5, 3.5), (-2, 3.5))
                Line((1.5, 4), (1.5, 3.5))
            make_face()
            # Profile area: 1.75, perimeter: 8
            with BuildLine():
                Line((-2, 2), (1.5, 2))
                Line((-2, 1.5), (-2, 2))
                Line((1.5, 1.5), (-2, 1.5))
                Line((1.5, 2), (1.5, 1.5))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch5 -> Extrude7 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.7412051525), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 19.6052238097, perimeter: 19.9724743463
            with BuildLine():
                Line((1.0995661978, 6.3034651393), (-1.5857375327, 6.3034651393))
                Line((1.0995661978, 13.604398582), (1.0995661978, 6.3034651393))
                Line((-1.5857375327, 13.604398582), (1.0995661978, 13.604398582))
                Line((-1.5857375327, 6.3034651393), (-1.5857375327, 13.604398582))
            make_face()
        # OneSide extrude, distance=0.15
        extrude(amount=0.15, mode=Mode.ADD)

        # Sketch6 -> Extrude8 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, -3.5), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.1006424195, perimeter: 1.1245932343
            with Locations((-1.6652400652, 1.0687837041)):
                Circle(0.1789845722)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch6 -> Extrude9 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, -3.5), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.1469668893, perimeter: 1.3589850619
            with Locations((-1.6652400652, 3.1395590723)):
                Circle(0.2162891902)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch6 -> Extrude10 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, -3.5), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.1255414955, perimeter: 1.2560258597
            with Locations((-1.6652400652, 5.1125025333)):
                Circle(0.1999027242)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


# Description: This is a boat trailer winch stand or marine equipment bracket featuring a curved, boat-hull-shaped upper basket or cradle (light blue mesh) mounted on a cylindrical pivot joint to a rectangular mounting flange (dark gray), designed to secure and support a boat during towing or storage.
def model_61469_c09267fc_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 17.4087385212, perimeter: 17.853981634
            with BuildLine():
                CenterArc((1.25, -2.5), 1.25, 180, 180)
                Line((2.5, -2.5), (2.5, 2.5))
                CenterArc((1.25, 2.5), 1.25, 0, 180)
                Line((0, 2.5), (0, -2.5))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.8153903268, perimeter: 8.7871717013
            with BuildLine():
                Line((-2.2020147463, 1.1412527473), (-0.1077344057, 1.1412527473))
                Line((-2.2020147463, -1.1580527628), (-2.2020147463, 1.1412527473))
                Line((-0.1077344057, -1.1580527628), (-2.2020147463, -1.1580527628))
                Line((-0.1077344057, 1.1412527473), (-0.1077344057, -1.1580527628))
            make_face()
        # OneSide extrude, distance=0.08
        extrude(amount=0.08, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 5.08, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.8355092367, perimeter: 5.9692595813
            with Locations((-1.25, -0.0084000077)):
                Circle(0.950037169)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch5 -> Extrude4 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 35 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 33.090050358, perimeter: 109.4103178361
            with BuildLine():
                Line((-2.9825906751, 6), (3, 6))
                Line((3, 6), (12, 8.5))
                Line((12, 8.5), (12, 12.5))
                Line((12, 12.5), (11.5, 12.5))
                Line((11.5, 12.5), (11.5, 9.5177242144))
                Line((11.5, 9.5177242144), (11.5, 9))
                Line((11.5, 9), (10.3000001535, 9))
                Line((10.3000001535, 9), (-10.3000001535, 9))
                Line((-10.3000001535, 9), (-11.4304769116, 9))
                Line((-11.4304769116, 9), (-11.5052621651, 9))
                Line((-11.5052621651, 9), (-11.5052621651, 9.0210398937))
                Line((-11.5052621651, 9.0210398937), (-11.5052621651, 9.4834908028))
                Line((-11.5052621651, 9.4834908028), (-11.5052621651, 12.5))
                Line((-11.5052621651, 12.5), (-12, 12.5))
                Line((-12, 12.5), (-12, 8.5369350918))
                Line((-2.9825906751, 6), (-12, 8.5369350918))
            make_face()
            with BuildLine():
                Line((-3.2034308002, 6.6854236922), (-9.3685403779, 8.4199))
                Line((-3.2034308002, 8.4199), (-9.3685403779, 8.4199))
                Line((-3.2034308002, 6.6854236922), (-3.2034308002, 8.4199))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-2.8113705922, 6.4828), (-2.8113705922, 8.4199))
                Line((-0.506093117, 8.4199), (-2.8113705922, 8.4199))
                Line((-0.506093117, 6.4828), (-0.506093117, 8.4199))
                Line((-2.8113705922, 6.4828), (-0.506093117, 6.4828))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((0.5102717769, 6.4828), (0.5102717769, 8.4199))
                Line((2.7985076686, 8.4199), (0.5102717769, 8.4199))
                Line((2.7985076686, 6.4828), (2.7985076686, 8.4199))
                Line((0.5102717769, 6.4828), (2.7985076686, 6.4828))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((3.2007720042, 6.6784880576), (3.2007720042, 8.4199))
                Line((9.4698549969, 8.4199), (3.2007720042, 8.4199))
                Line((3.2007720042, 6.6784880576), (9.4698549969, 8.4199))
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=12
        extrude(amount=12, both=True)

        # Sketch7 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5.38, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.97988109, perimeter: 14.7564312827
            with BuildLine():
                Line((-2.2020147463, 1.1412527473), (-2.2020147463, -1.1580527628))
                Line((-2.2020147463, -1.1580527628), (-0.1077344057, -1.1580527628))
                Line((-0.1077344057, -1.1580527628), (-0.1077344057, 1.1412527473))
                Line((-0.1077344057, 1.1412527473), (-2.2020147463, 1.1412527473))
            make_face()
            with BuildLine():
                CenterArc((-1.25, -0.0084000077), 0.950037169, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.63
        extrude(amount=0.63, taper=20, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5.38, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.97988109, perimeter: 14.7564312827
            with BuildLine():
                Line((-2.2020147463, 1.1412527473), (-2.2020147463, -1.1580527628))
                Line((-2.2020147463, -1.1580527628), (-0.1077344057, -1.1580527628))
                Line((-0.1077344057, -1.1580527628), (-0.1077344057, 1.1412527473))
                Line((-0.1077344057, 1.1412527473), (-2.2020147463, 1.1412527473))
            make_face()
            with BuildLine():
                CenterArc((-1.25, -0.0084000077), 0.950037169, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.63
        extrude(amount=0.63, taper=30, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude7 (NewBody)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5.38, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.97988109, perimeter: 14.7564312827
            with BuildLine():
                Line((-2.2020147463, 1.1412527473), (-2.2020147463, -1.1580527628))
                Line((-2.2020147463, -1.1580527628), (-0.1077344057, -1.1580527628))
                Line((-0.1077344057, -1.1580527628), (-0.1077344057, 1.1412527473))
                Line((-0.1077344057, 1.1412527473), (-2.2020147463, 1.1412527473))
            make_face()
            with BuildLine():
                CenterArc((-1.25, -0.0084000077), 0.950037169, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.65
        extrude(amount=0.65, taper=30)

        # Sketch8 -> Extrude8 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 9, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 49.5528, perimeter: 52.1294
            with BuildLine():
                Line((-12, 1.0436310825), (12, 1.0436310825))
                Line((-12, 1.0436310825), (-12, -1.0210689175))
                Line((-12, -1.0210689175), (12, -1.0210689175))
                Line((12, -1.0210689175), (12, 1.0436310825))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


# Description: This is a cast iron fireplace grate with a rectangular frame, horizontal parallel bars forming the base, and four corner flanges designed for mounting or support.
def model_63539_dd7fddaa_0005():
    """Model: frame v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 33 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 101.92, perimeter: 54.4
            with BuildLine():
                Line((0, 0), (0, -1.6))
                Line((0, -1.6), (-0.8, -1.6))
                Line((-0.8, -1.6), (-0.8, -2.8))
                Line((-0.8, -2.8), (0, -2.8))
                Line((0, -2.8), (0, -4.4))
                Line((0, -4.4), (-0.8, -4.4))
                Line((-0.8, -4.4), (-0.8, -5.6))
                Line((-0.8, -5.6), (0, -5.6))
                Line((0, -5.6), (0, -7.2))
                Line((0, -7.2), (-0.8, -7.2))
                Line((-0.8, -7.2), (-0.8, -8.4))
                Line((-0.8, -8.4), (0, -8.4))
                Line((0, -8.4), (0, -10))
                Line((0, -10), (9.2, -10))
                Line((9.2, -10), (9.2, -11.2))
                Line((9.2, -11.2), (10, -11.2))
                Line((10, -8.4), (10, -11.2))
                Line((9.2, -8.4), (10, -8.4))
                Line((9.2, -7.2), (9.2, -8.4))
                Line((10, -7.2), (9.2, -7.2))
                Line((10, -5.6), (10, -7.2))
                Line((9.2, -5.6), (10, -5.6))
                Line((9.2, -4.4), (9.2, -5.6))
                Line((10, -4.4), (9.2, -4.4))
                Line((10, -2.8), (10, -4.4))
                Line((9.2, -2.8), (10, -2.8))
                Line((9.2, -1.6), (9.2, -2.8))
                Line((10, -1.6), (9.2, -1.6))
                Line((10, 1.2), (10, -1.6))
                Line((9.2, 1.2), (10, 1.2))
                Line((9.2, 0), (9.2, 1.2))
                Line((0, 0), (9.2, 0))
            make_face()
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 25 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 8.4830298189, perimeter: 11.8051054905
            with BuildLine():
                Line((-8.5136188841, -1.0693107876), (-8.5136188841, -4.3819378244))
                Line((-8.5136188841, -4.3819378244), (-5.8736107764, -4.3819378244))
                Line((-5.8736107764, -4.3819378244), (-5.4551951414, -3.3235923946))
                CenterArc((-5.8271794294, -3.1765288389), 0.4, -21.5713071913, 72.4487072439)
                Line((-6.0167523015, -2.5067445327), (-5.5747866835, -2.8662098066))
                CenterArc((-5.2911231569, -1.6145773149), 1.15, -180, 50.8774000527)
                Line((-6.4411231569, -1.0693107876), (-6.4411231569, -1.6145773149))
                Line((-8.5136188841, -1.0693107876), (-6.4411231569, -1.0693107876))
            make_face()
            # Profile area: 10.9986427613, perimeter: 14.8010550244
            with BuildLine():
                CenterArc((-5.0720246265, -2.4967360997), 0.475, -134.7120958658, 39.7463475963)
                Line((-2.9937582246, -3.1540985777), (-5.1131407199, -2.9699532453))
                CenterArc((-2.9898630158, -3.1092674797), 0.045, -94.9657482695, 4.9657482695)
                Line((-0.5458365035, -3.1542674797), (-2.9898630158, -3.1542674797))
                Line((-0.5458365035, -1.068520054), (-0.5458365035, -3.1542674797))
                Line((-6.2763265435, -1.068520054), (-0.5458365035, -1.068520054))
                Line((-6.2329795689, -1.7423046311), (-6.2763265435, -1.068520054))
                CenterArc((-5.4346299715, -1.6909439426), 0.8, -176.3190300134, 25.3303653159)
                Line((-6.1340013939, -2.0793765289), (-6.1342489923, -2.0789300578))
                CenterArc((-5.6005418905, -1.783537116), 0.61, -150.9886646975, 16.2765688317)
                Line((-5.4062083808, -2.8342953069), (-6.0297041855, -2.2170342032))
            make_face()
            # Profile area: 5.4944464762, perimeter: 12.0892901659
            with BuildLine():
                CenterArc((-4.8887124405, -3.6022416664), 0.45, 84.7896385397, 75.7941983812)
                Line((-5.3131204537, -3.4526494261), (-5.6465224355, -4.3985438947))
                Line((-5.6465224355, -4.3985438947), (-0.5438485932, -4.3985438947))
                Line((-0.5438485932, -4.3985438947), (-0.5458365035, -3.3192257383))
                Line((-0.5458365035, -3.3192257383), (-2.5316321601, -3.3228832174))
                CenterArc((-2.5497280156, 6.5021001179), 9.825, -95.2103614603, 5.3158898811)
                Line((-3.4419625577, -3.2823029054), (-4.8478467363, -3.1541010699))
            make_face()
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 29 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 8.2099443041, perimeter: 12.1724196974
            with BuildLine():
                CenterArc((-8.2606304623, -5.2804814769), 0.25, 57.0292814492, 122.9305462327)
                Line((-8.5132852576, -9.0667958053), (-8.5106304008, -5.2803061921))
                CenterArc((-8.2632853191, -9.0669710901), 0.25, 179.959827682, 124.5658151679)
                Line((-5.2874218674, -7.3232002095), (-8.1215915642, -9.2729392426))
                CenterArc((-5.4291156223, -7.117232057), 0.25, -55.4743571502, 112.5036385994)
                Line((-8.1245778736, -5.0707442768), (-5.2930630336, -6.9074948569))
            make_face()
            # Profile area: 6.7660222543, perimeter: 14.3250332336
            with BuildLine():
                CenterArc((-1.1323657256, -5.1102252079), 0.1, -67.3675443889, 157.3675443889)
                Line((-7.523785366, -5.0102252079), (-1.1323657256, -5.0102252079))
                CenterArc((-7.523785366, -5.1602252079), 0.15, 90, 148.2596463649)
                Line((-7.6026959786, -5.2877913289), (-5.1517772669, -6.8038952541))
                CenterArc((-5.0465631169, -6.6338070927), 0.2, -121.7403536351, 54.3728092462)
                Line((-1.0938839036, -5.2025244461), (-4.9695994728, -6.8184055692))
            make_face()
            # Profile area: 7.8819774892, perimeter: 12.5159863967
            with BuildLine():
                CenterArc((-4.9133836501, -7.0781328886), 0.1, 112.0019827428, 133.0246642213)
                Line((-1.1124953245, -8.9586784873), (-4.9556033214, -7.1687833125))
                CenterArc((-1.0491658175, -8.8227028515), 0.15, -114.9733530359, 114.9733530359)
                Line((-0.8991658175, -5.4965286643), (-0.8991658175, -8.8227028515))
                CenterArc((-0.9991658175, -5.4965286643), 0.1, 0, 112.0019827428)
                Line((-4.950847518, -6.9854157995), (-1.0366296854, -5.4038115753))
            make_face()
            # Profile area: 7.2322483632, perimeter: 14.5306784289
            with BuildLine():
                CenterArc((-1.0673645054, -9.2170877097), 0.1, -90, 155.5512563079)
                Line((-1.0259766021, -9.1260545209), (-4.8932999085, -7.3677902511))
                CenterArc((-4.9967696669, -7.595373223), 0.25, 65.5512563079, 59.7488093031)
                Line((-5.1412343066, -7.391338991), (-7.6045585588, -9.1354740168))
                CenterArc((-7.5467727029, -9.2170877097), 0.1, 125.300065611, 144.699934389)
                Line((-7.5467727029, -9.3170877097), (-1.0673645054, -9.3170877097))
            make_face()
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 32 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.4, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.7937973316, perimeter: 10.6913060011
            with BuildLine():
                CenterArc((-7.0025561994, -5.2732088143), 0.0759416402, 90, 180)
                Line((-7.0025561994, -5.3491504545), (-1.8954808977, -5.3491504545))
                CenterArc((-1.8954808977, -5.2732088143), 0.0759416402, -90, 180)
                Line((-1.8954808977, -5.1972671741), (-7.0025561994, -5.1972671741))
            make_face()
            # Profile area: 0.6879530616, perimeter: 8.3208179403
            with BuildLine():
                CenterArc((-6.5943698835, -5.6719024252), 0.0854343452, 90, 180)
                Line((-6.5943698835, -5.7573367704), (-2.7023608246, -5.7573367704))
                CenterArc((-2.7023608246, -5.6719024252), 0.0854343452, -90, 180)
                Line((-2.7023608246, -5.58646808), (-6.5943698835, -5.58646808))
            make_face()
            # Profile area: 0.5113772775, perimeter: 5.5209141015
            with BuildLine():
                CenterArc((-5.9836619637, -6.0104650076), 0.0981018486, 90, 180)
                Line((-5.9836619637, -6.1085668562), (-3.5314009598, -6.1085668562))
                CenterArc((-3.5314009598, -6.0104650076), 0.0981018486, -90, 180)
                Line((-3.5314009598, -5.912363159), (-5.9836619637, -5.912363159))
            make_face()
            # Profile area: 0.2143272876, perimeter: 2.7770782076
            with BuildLine():
                CenterArc((-5.4362598708, -6.3933480069), 0.0854343452, 90, 180)
                Line((-5.4362598708, -6.4787823521), (-4.3161206783, -6.4787823521))
                CenterArc((-4.3161206783, -6.3933480069), 0.0854343452, -90, 180)
                Line((-4.3161206783, -6.3079136617), (-5.4362598708, -6.3079136617))
            make_face()
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 73 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.4, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0417378921, perimeter: 0.8852924938
            with BuildLine():
                CenterArc((-8.3200367182, -5.2877913289), 0.0598625528, 90, 180)
                Line((-8.3200367182, -5.3476538817), (-8.0654542273, -5.3476538817))
                CenterArc((-8.0654542273, -5.2877913289), 0.0598625528, -90, 180)
                Line((-8.0654542273, -5.2279287761), (-8.3200367182, -5.2279287761))
            make_face()
            # Profile area: 0.1207534842, perimeter: 1.9907835625
            with BuildLine():
                CenterArc((-8.3119587918, -5.6242686895), 0.0679404791, 90, 180)
                Line((-8.3119587918, -5.6922091686), (-7.5300083207, -5.6922091686))
                CenterArc((-7.5300083207, -5.6242686895), 0.0679404791, -90, 180)
                Line((-7.5300083207, -5.5563282104), (-8.3119587918, -5.5563282104))
            make_face()
            # Profile area: 0.2086437829, perimeter: 3.1160205314
            with BuildLine():
                CenterArc((-8.2397423699, -6.0929586393), 0.0722164219, 90, 180)
                Line((-8.2397423699, -6.1651750612), (-6.9086066847, -6.1651750612))
                CenterArc((-6.9086066847, -6.0929586393), 0.0722164219, -90, 180)
                Line((-6.9086066847, -6.0207422174), (-8.2397423699, -6.0207422174))
            make_face()
            # Profile area: 0.375811907, perimeter: 4.3392261088
            with BuildLine():
                CenterArc((-8.2191091065, -6.5582387289), 0.0928496853, 90, 180)
                Line((-8.2191091065, -6.6510884141), (-6.3411919413, -6.6510884141))
                CenterArc((-6.3411919413, -6.5582387289), 0.0928496853, -90, 180)
                Line((-6.3411919413, -6.4653890436), (-8.2191091065, -6.4653890436))
            make_face()
            # Profile area: 0.474150597, perimeter: 5.0497745871
            with BuildLine():
                CenterArc((-8.2118255751, -7.5528384408), 0.1001332413, 89.9598276819, 180)
                Line((-8.2118957825, -7.6529716575), (-6.0015868875, -7.654521392))
                CenterArc((-6.0015166802, -7.5543881753), 0.1001332413, -90.040172318, 180)
                Line((-6.0014464728, -7.4542549586), (-8.2117553678, -7.4527052241))
            make_face()
            # Profile area: 0.2116267052, perimeter: 3.5670354655
            with BuildLine():
                CenterArc((-8.2080845889, -8.0391241414), 0.0628021487, 89.9598276819, 180.0000012074)
                Line((-8.2081286206, -8.1019262747), (-6.6219100481, -8.1030384349))
                CenterArc((-6.6218660151, -8.0402363016), 0.0628021487, -90.0401723181, 180)
                Line((-6.621821982, -7.9774341683), (-8.2080405558, -7.9763220081))
            make_face()
            # Profile area: 0.1814357476, perimeter: 2.255474479
            with BuildLine():
                CenterArc((-8.2218349252, -8.4848620187), 0.0923116933, 89.959827682, 180)
                Line((-8.2218996486, -8.5771736893), (-7.3841683525, -8.5777610557))
                CenterArc((-7.3841036291, -8.4854493851), 0.0923116933, -90.040172318, 180)
                Line((-7.3840389058, -8.3931377145), (-8.2217702019, -8.3925503481))
            make_face()
            # Profile area: 0.0584565131, perimeter: 1.0504622136
            with BuildLine():
                CenterArc((-8.1772353914, -8.8964592579), 0.0705221063, 89.959827682, 180)
                Line((-8.1772848372, -8.9669813468), (-7.8736055352, -8.9671942683))
                CenterArc((-7.8735560894, -8.8966721794), 0.0705221063, -90.040172318, 179.9999987926)
                Line((-7.8735066436, -8.8261500904), (-8.1771859456, -8.8259371689))
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.4, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.5047328287, perimeter: 5.6458926383
            with BuildLine():
                CenterArc((-8.1708216138, -7.0696295333), 0.0943517955, 90, 180)
                Line((-8.1708216138, -7.1639813288), (-5.6442902021, -7.1639813288))
                CenterArc((-5.6442902021, -7.0696295333), 0.0943517955, -90, 180)
                Line((-5.6442902021, -6.9752777379), (-8.1708216138, -6.9752777379))
            make_face()
        # OneSide extrude, distance=-1.7
        extrude(amount=-1.7, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 88 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.4, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0509884604, perimeter: 0.9445754423
            with BuildLine():
                CenterArc((-1.4347290714, -5.7248256947), 0.0705207211, 90, 180)
                Line((-1.4347290714, -5.7953464158), (-1.1839887296, -5.7953464158))
                CenterArc((-1.1839887296, -5.7248256947), 0.0705207211, -90, 180)
                Line((-1.1839887296, -5.6543049736), (-1.4347290714, -5.6543049736))
            make_face()
            # Profile area: 0.103537264, perimeter: 1.848635924
            with BuildLine():
                CenterArc((-1.9583895018, -5.9912373078), 0.0626850854, 90, 180)
                Line((-1.9583895018, -6.0539223933), (-1.2310025437, -6.0539223933))
                CenterArc((-1.2310025437, -5.9912373078), 0.0626850854, -90, 180)
                Line((-1.2310025437, -5.9285522224), (-1.9583895018, -5.9285522224))
            make_face()
            # Profile area: 0.1855718866, perimeter: 3.1573144079
            with BuildLine():
                CenterArc((-2.7119376873, -6.257648921), 0.0626850854, 90, 180)
                Line((-2.7119376873, -6.3203340064), (-1.3302114872, -6.3203340064))
                CenterArc((-1.3302114872, -6.257648921), 0.0626850854, -90, 180)
                Line((-1.3302114872, -6.1949638355), (-2.7119376873, -6.1949638355))
            make_face()
            # Profile area: 0.287864792, perimeter: 4.3035361541
            with BuildLine():
                CenterArc((-3.2682678206, -6.4927179914), 0.0705207211, 90, 180)
                Line((-3.2682678206, -6.5632387125), (-1.3380471229, -6.5632387125))
                CenterArc((-1.3380471229, -6.4927179914), 0.0705207211, -90, 180)
                Line((-1.3380471229, -6.4221972702), (-3.2682678206, -6.4221972702))
            make_face()
            # Profile area: 0.4224700043, perimeter: 5.6378131567
            with BuildLine():
                CenterArc((-3.918625582, -6.7277870618), 0.0783563568, 90, 180)
                Line((-3.918625582, -6.8061434186), (-1.3458827586, -6.8061434186))
                CenterArc((-1.3458827586, -6.7277870618), 0.0783563568, -90, 180)
                Line((-1.3458827586, -6.649430705), (-3.918625582, -6.649430705))
            make_face()
            # Profile area: 0.7702396281, perimeter: 7.0768928269
            with BuildLine():
                CenterArc((-4.4457057334, -7.0739500722), 0.1146765738, 90, 180)
                Line((-4.4457057334, -7.188626646), (-1.2675264018, -7.188626646))
                CenterArc((-1.2675264018, -7.0739500722), 0.1146765738, -90, 180)
                Line((-1.2675264018, -6.9592734984), (-4.4457057334, -6.9592734984))
            make_face()
            # Profile area: 0.551650592, perimeter: 5.8644607585
            with BuildLine():
                CenterArc((-3.9504553685, -7.4149949768), 0.0993548209, 90, 180)
                Line((-3.9504553685, -7.5143497977), (-1.3303573646, -7.5143497977))
                CenterArc((-1.3303573646, -7.4149949768), 0.0993548209, -90, 180)
                Line((-1.3303573646, -7.3156401559), (-3.9504553685, -7.3156401559))
            make_face()
            # Profile area: 0.2945407178, perimeter: 4.3032392432
            with BuildLine():
                CenterArc((-3.2278748529, -7.7943497475), 0.0722580516, 90, 180)
                Line((-3.2278748529, -7.866607799), (-1.3032605953, -7.866607799))
                CenterArc((-1.3032605953, -7.7943497475), 0.0722580516, -90, 180)
                Line((-1.3032605953, -7.7220916959), (-3.2278748529, -7.7220916959))
            make_face()
            # Profile area: 0.1934783411, perimeter: 2.9573559011
            with BuildLine():
                CenterArc((-2.5581876577, -8.0637308999), 0.0707383994, 90, 180)
                Line((-2.5581876577, -8.1344692993), (-1.3017409432, -8.1344692993))
                CenterArc((-1.3017409432, -8.0637308999), 0.0707383994, -90, 180)
                Line((-1.3017409432, -7.9929925005), (-2.5581876577, -7.9929925005))
            make_face()
            # Profile area: 0.0958398192, perimeter: 2.1705124897
            with BuildLine():
                CenterArc((-2.1252106636, -8.3715118375), 0.0474085076, 90, 180)
                Line((-2.1252106636, -8.4189203451), (-1.1888926381, -8.4189203451))
                CenterArc((-1.1888926381, -8.3715118375), 0.0474085076, -90, 180)
                Line((-1.1888926381, -8.3241033298), (-2.1252106636, -8.3241033298))
            make_face()
            # Profile area: 0.0353969979, perimeter: 0.983621625
            with BuildLine():
                CenterArc((-1.5444564452, -8.6441107563), 0.0414824442, 90, 180)
                Line((-1.5444564452, -8.6855932005), (-1.1829665746, -8.6855932005))
                CenterArc((-1.1829665746, -8.6441107563), 0.0414824442, -90, 180)
                Line((-1.1829665746, -8.6026283121), (-1.5444564452, -8.6026283121))
            make_face()
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)

        # Sketch8 -> Extrude8 (Cut)
        # Sketch on BRepFace
        # Sketch has 56 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.4, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0828737393, perimeter: 1.5728591819
            with BuildLine():
                CenterArc((-5.251022652, -7.6513792251), 0.0598427916, 90, 180)
                Line((-5.251022652, -7.7112220167), (-4.6525947357, -7.7112220167))
                CenterArc((-4.6525947357, -7.6513792251), 0.0598427916, -90, 180)
                Line((-4.6525947357, -7.5915364335), (-5.251022652, -7.5915364335))
            make_face()
            # Profile area: 0.1176007771, perimeter: 2.6728603167
            with BuildLine():
                CenterArc((-5.4637970223, -7.8641535954), 0.0465443935, 90, 180)
                Line((-5.4637970223, -7.9106979889), (-4.2735903886, -7.9106979889))
                CenterArc((-4.2735903886, -7.8641535954), 0.0465443935, -90, 180)
                Line((-4.2735903886, -7.8176092019), (-5.4637970223, -7.8176092019))
            make_face()
            # Profile area: 0.2526335425, perimeter: 4.0083489974
            with BuildLine():
                CenterArc((-5.7364141842, -8.0503311694), 0.0664919907, 90, 180)
                Line((-5.7364141842, -8.1168231601), (-3.9411304351, -8.1168231601))
                CenterArc((-3.9411304351, -8.0503311694), 0.0664919907, -90, 180)
                Line((-3.9411304351, -7.9838391786), (-5.7364141842, -7.9838391786))
            make_face()
            # Profile area: 0.3671896042, perimeter: 5.7976540614
            with BuildLine():
                CenterArc((-6.0424415192, -8.2763218489), 0.0656711019, 90, 180)
                Line((-6.0424415192, -8.3419929508), (-3.3499263399, -8.3419929508))
                CenterArc((-3.3499263399, -8.2763218489), 0.0656711019, -90, 180)
                Line((-3.3499263399, -8.210650747), (-6.0424415192, -8.210650747))
            make_face()
            # Profile area: 0.5435657733, perimeter: 7.5895162256
            with BuildLine():
                CenterArc((-6.4036325799, -8.5472151444), 0.0738799897, 90, 180)
                Line((-6.4036325799, -8.621095134), (-2.8409752999, -8.621095134))
                CenterArc((-2.8409752999, -8.5472151444), 0.0738799897, -90, 180)
                Line((-2.8409752999, -8.4733351547), (-6.4036325799, -8.4733351547))
            make_face()
            # Profile area: 0.7420160441, perimeter: 9.6612899339
            with BuildLine():
                CenterArc((-6.7972538143, -8.8271168215), 0.0788233391, 90, 180)
                Line((-6.7972538143, -8.9059401605), (-2.2142396704, -8.9059401605))
                CenterArc((-2.2142396704, -8.8271168215), 0.0788233391, -90, 180)
                Line((-2.2142396704, -8.7482934824), (-6.7972538143, -8.7482934824))
            make_face()
            # Profile area: 0.9035571325, perimeter: 11.7106967501
            with BuildLine():
                CenterArc((-7.2251519408, -9.1311497008), 0.0788233391, 90, 180)
                Line((-7.2251519408, -9.2099730399), (-1.6174343887, -9.2099730399))
                CenterArc((-1.6174343887, -9.1311497008), 0.0788233391, -90, 180)
                Line((-1.6174343887, -9.0523263617), (-7.2251519408, -9.0523263617))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch9 -> Extrude9 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.8, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-0.4, -2.1363937669)):
                Circle(0.2)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-0.3933136958, -5)):
                Circle(0.2)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-0.4605617247, -7.8679390436)):
                Circle(0.2)
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)

        # Sketch10 -> Extrude10 (NewBody)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.8, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-0.4, -2.1363937669)):
                Circle(0.2)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-0.3933136958, -5)):
                Circle(0.2)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-0.4605617247, -7.8679390436)):
                Circle(0.2)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a boat propeller assembly mount or gearbox housing featuring a rectangular box-like base with an angled top surface and a vertical shaft connector, designed to house and position a propeller mechanism for marine applications.
def model_69239_a96344a9_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 10 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 32.25, perimeter: 32
            with BuildLine():
                Line((-3, -1.5), (-5, -1.5))
                Line((-3, 0), (-3, -1.5))
                Line((3.5, 0), (-3, 0))
                Line((3.5, -1.5), (3.5, 0))
                Line((5.5, -1.5), (3.5, -1.5))
                Line((5.5, 2.5), (5.5, -1.5))
                Line((-5, 2.5), (5.5, 2.5))
                Line((-5, -1.5), (-5, 2.5))
            make_face()
        # OneSide extrude, distance=10
        extrude(amount=10)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 2.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 31.4159265359, perimeter: 19.8691765316
            with Locations((0, 5)):
                Circle(3.1622776602)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            with Locations((0, 5)):
                Circle(2)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch5 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.7328323218, perimeter: 5.8601863266
            with Locations((0, 5)):
                Circle(0.9326776213)
        # OneSide extrude, distance=0.25
        extrude(amount=0.25, mode=Mode.ADD)

        # Sketch6 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3.75, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2670844321, perimeter: 1.8320158184
            with Locations((0, 5)):
                Circle(0.2915743733)
        # OneSide extrude, distance=3.5
        extrude(amount=3.5, mode=Mode.ADD)

        # Sketch7 -> Extrude6 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2513274198, perimeter: 1.7771532017
            with Locations((2.7000000402, 5.0000000745)):
                Circle(0.2828427167)
        # OneSide extrude, distance=-4.6
        extrude(amount=-4.6, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude7 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3557142963, perimeter: 2.6436895216
            with BuildLine():
                Line((-3.2000000477, 3.1000000462), (-2.9000000432, 3.3571429072))
                Line((-2.6000000387, 2.4000000358), (-3.2000000477, 3.1000000462))
                Line((-2.3000000343, 2.6000000387), (-2.6000000387, 2.4000000358))
                Line((-2.9000000432, 3.3571429072), (-2.3000000343, 2.6000000387))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch8 -> Extrude8 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(5.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 7.4893271224, perimeter: 15.4309319314
            with BuildLine():
                CenterArc((-8, 0), 0.5460497763, 90, 180)
                Line((-8, -0.5460497763), (-2, -0.5460497763))
                CenterArc((-2, 0), 0.5460497763, -90, 180)
                Line((-2, 0.5460497763), (-8, 0.5460497763))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


# Description: This is a structural bracket or frame assembly with an elongated, angular truss-like design featuring multiple internal diagonal bracing members, a flat base platform, and mounting flanges on the ends.
def model_69455_034b69e7_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 13 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 521.3336293856, perimeter: 109.7327412287
            with BuildLine():
                CenterArc((18.2, -7.4471672704), 1.5, -90, 90)
                Line((19.7, 7.3528327296), (19.7, -7.4471672704))
                CenterArc((18.2, 7.3528327296), 1.5, 0, 90)
                Line((18.2, 8.8528327296), (-9.3, 8.8528327296))
                CenterArc((-9.3, 7.3528327296), 1.5, 90, 90)
                Line((-10.8, 7.3528327296), (-10.8, -7.4471672704))
                CenterArc((-9.3, -7.4471672704), 1.5, -180, 90)
                Line((-9.3, -8.9471672704), (18.2, -8.9471672704))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.8696902001, perimeter: 6.5991148575
            with BuildLine():
                Line((-19.7, 4.2528327296), (-19.7, 5.6528327296))
                Line((-18.2, 4.2528327296), (-19.7, 4.2528327296))
                CenterArc((-18.2, 4.9528327296), 0.7, -90, 180)
                Line((-18.2, 5.6528327296), (-19.7, 5.6528327296))
            make_face()
            # Profile area: 2.8696902001, perimeter: 6.5991148575
            with BuildLine():
                Line((-19.7, -5.6528327296), (-19.7, -4.2528327296))
                Line((-18.2, -5.6528327296), (-19.7, -5.6528327296))
                CenterArc((-18.2, -4.9528327296), 0.7, -90, 180)
                Line((-18.2, -4.2528327296), (-19.7, -4.2528327296))
            make_face()
            # Profile area: 2.8696902001, perimeter: 6.5991148575
            with BuildLine():
                CenterArc((9.3, -4.9528327296), 0.7, 90, 180)
                Line((9.3, -5.6528327296), (10.8, -5.6528327296))
                Line((10.8, -5.6528327296), (10.8, -4.2528327296))
                Line((9.3, -4.2528327296), (10.8, -4.2528327296))
            make_face()
            # Profile area: 2.8696902001, perimeter: 6.5991148575
            with BuildLine():
                Line((10.8, 4.2528327296), (10.8, 5.6528327296))
                Line((9.3, 5.6528327296), (10.8, 5.6528327296))
                CenterArc((9.3, 4.9528327296), 0.7, 90, 180)
                Line((9.3, 4.2528327296), (10.8, 4.2528327296))
            make_face()
        # OneSide extrude, distance=-6.8
        extrude(amount=-6.8, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.4090706004, perimeter: 13.9973445725
            with BuildLine():
                Line((10.8, -5.6528327296), (9.3, -5.6528327296))
                CenterArc((9.3, -4.9528327296), 0.7, 90, 180)
                Line((9.3, -4.2528327296), (10.8, -4.2528327296))
                Line((10.8, -4.2528327296), (10.8, -3.5528327296))
                Line((9.3, -3.5528327296), (10.8, -3.5528327296))
                CenterArc((9.3, -4.9528327296), 1.4, 90, 180)
                Line((9.3, -6.3528327296), (10.8, -6.3528327296))
                Line((10.8, -6.3528327296), (10.8, -5.6528327296))
            make_face()
            # Profile area: 4.4090706004, perimeter: 13.9973445725
            with BuildLine():
                Line((9.3, 6.3528327296), (10.8, 6.3528327296))
                CenterArc((9.3, 4.9528327296), 1.4, 90, 180)
                Line((9.3, 3.5528327296), (10.8, 3.5528327296))
                Line((10.8, 4.2528327296), (10.8, 3.5528327296))
                Line((9.3, 4.2528327296), (10.8, 4.2528327296))
                CenterArc((9.3, 4.9528327296), 0.7, 90, 180)
                Line((10.8, 5.6528327296), (9.3, 5.6528327296))
                Line((10.8, 6.3528327296), (10.8, 5.6528327296))
            make_face()
            # Profile area: 4.4090706004, perimeter: 13.9973445725
            with BuildLine():
                Line((-18.2, 3.5528327296), (-19.7, 3.5528327296))
                CenterArc((-18.2, 4.9528327296), 1.4, -90, 180)
                Line((-18.2, 6.3528327296), (-19.7, 6.3528327296))
                Line((-19.7, 6.3528327296), (-19.7, 5.6528327296))
                Line((-19.7, 5.6528327296), (-18.2, 5.6528327296))
                CenterArc((-18.2, 4.9528327296), 0.7, -90, 180)
                Line((-18.2, 4.2528327296), (-19.7, 4.2528327296))
                Line((-19.7, 4.2528327296), (-19.7, 3.5528327296))
            make_face()
            # Profile area: 4.4090706004, perimeter: 13.9973445725
            with BuildLine():
                Line((-18.2, -6.3528327296), (-19.7, -6.3528327296))
                CenterArc((-18.2, -4.9528327296), 1.4, -90, 180)
                Line((-18.2, -3.5528327296), (-19.7, -3.5528327296))
                Line((-19.7, -4.2528327296), (-19.7, -3.5528327296))
                Line((-18.2, -4.2528327296), (-19.7, -4.2528327296))
                CenterArc((-18.2, -4.9528327296), 0.7, -90, 180)
                Line((-19.7, -5.6528327296), (-18.2, -5.6528327296))
                Line((-19.7, -6.3528327296), (-19.7, -5.6528327296))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 14 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 174.4336293856, perimeter: 69.1327412287
            with BuildLine():
                Line((-5.5, -7), (5.5, -7))
                CenterArc((5.5, -5.5), 1.5, -90, 90)
                Line((7, -5.5), (7, 5.5))
                CenterArc((5.5, 5.5), 1.5, 0, 90)
                Line((5.5, 7), (-5.5, 7))
                CenterArc((-5.5, 5.5), 1.5, 90, 90)
                Line((-7, -5.5), (-7, 5.5))
                CenterArc((-5.5, -5.5), 1.5, -180, 90)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 14 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.4227433388, perimeter: 14.4849555922
            with BuildLine():
                CenterArc((-11.95, -2.2), 0.3, -180, 90)
                Line((-11.95, -2.5), (-10.05, -2.5))
                CenterArc((-10.05, -2.2), 0.3, -90, 90)
                Line((-9.75, -2.2), (-9.75, 2.2))
                CenterArc((-10.05, 2.2), 0.3, 0, 90)
                Line((-11.95, 2.5), (-10.05, 2.5))
                CenterArc((-11.95, 2.2), 0.3, 90, 90)
                Line((-12.25, -2.2), (-12.25, 2.2))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch7 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.5049182598, perimeter: 6.6365730484
            with Locations((-14.5, -3.8)):
                Circle(1.0562434058)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch9 -> Extrude7 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 43 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 342.4253981634, perimeter: 78.8247779608
            with BuildLine():
                CenterArc((-6.5, -6.5), 0.5, 180, 90)
                Line((-6.5, -7), (15.4, -7))
                CenterArc((15.4, -6.5), 0.5, -90, 90)
                Line((15.9, -3.4), (15.9, -6.5))
                CenterArc((16.4, -3.4), 0.5, 90, 90)
                Line((16.4, -2.9), (17.3, -2.9))
                CenterArc((17.3, -2.4), 0.5, -90, 90)
                Line((17.8, -2.4), (17.8, 2.4))
                CenterArc((17.3, 2.4), 0.5, 0, 90)
                Line((16.4, 2.9), (17.3, 2.9))
                CenterArc((16.4, 3.4), 0.5, 180, 90)
                Line((15.9, 3.4), (15.9, 6.5))
                CenterArc((15.4, 6.5), 0.5, 0, 90)
                Line((-6.5, 7), (15.4, 7))
                CenterArc((-6.5, 6.5), 0.5, 90, 90)
                Line((-7, 6.5), (-7, 3.4))
                CenterArc((-7.5, 3.4), 0.5, -90, 90)
                Line((-7.5, 2.9), (-8.4, 2.9))
                CenterArc((-8.4, 2.4), 0.5, 90, 90)
                Line((-8.9, 2.4), (-8.9, -2.4))
                CenterArc((-8.4, -2.4), 0.5, -180, 90)
                Line((-7.5, -2.9), (-8.4, -2.9))
                CenterArc((-7.5, -3.4), 0.5, 0, 90)
                Line((-7, -6.5), (-7, -3.4))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a robotic camera or sensor head mount assembly featuring a cylindrical lens/camera barrel at the top, a blocky rectangular body with angular faceted surfaces, a articulated neck joint with triangulated structural elements, and a rectangular base platform with mounting slots.
def model_70621_14f013e9_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 30.2753472978, perimeter: 33.2174030405
            with BuildLine():
                Line((0, 2.5), (0, -0.551169449))
                Line((3, 2.5), (0, 2.5))
                Line((3, 5), (3, 2.5))
                Line((-2.5, 5), (3, 5))
                Line((-2.5, -2.5), (-2.5, 5))
                Line((3, -2.5), (-2.5, -2.5))
                Line((3, -1), (3, -2.5))
                Line((0.448830551, -1), (3, -1))
                CenterArc((0, -1), 0.448830551, 90, 270)
            make_face()
        # Symmetric extrude, each_side=1.5
        extrude(amount=1.5, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 15 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(3, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.125, perimeter: 5
            with BuildLine():
                Line((-1.5, -1), (-0.5, -1))
                Line((-1.5, -2.5), (-1.5, -1))
                Line((-1.5, -2.5), (-1, -2.5))
                Line((-1, -1.75), (-1, -2.5))
                Line((-0.5, -1.75), (-1, -1.75))
                Line((-0.5, -1.75), (-0.5, -1))
            make_face()
        # OneSide extrude, distance=-9.5
        extrude(amount=-9.5, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(3, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.125, perimeter: 5
            with BuildLine():
                Line((0.5, -1.75), (1, -1.75))
                Line((1, -1.75), (1, -2.5))
                Line((1, -2.5), (1.5, -2.5))
                Line((1.5, -1), (1.5, -2.5))
                Line((1.5, -1), (0.5, -1))
                Line((0.5, -1), (0.5, -1.75))
            make_face()
        # OneSide extrude, distance=-12.5
        extrude(amount=-12.5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 10 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-2.5, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.75, perimeter: 4
            with BuildLine():
                Line((-1, -1), (-1, 0.5))
                Line((-1, 0.5), (-1.5, 0.5))
                Line((-1.5, -1), (-1.5, 0.5))
                Line((-1.5, -1), (-1, -1))
            make_face()
            # Profile area: 0.75, perimeter: 4
            with BuildLine():
                Line((1.5, 0.5), (1, 0.5))
                Line((1, 0.5), (1, -1))
                Line((1, -1), (1.5, -1))
                Line((1.5, -1), (1.5, 0.5))
            make_face()
        # OneSide extrude, distance=-9.5
        extrude(amount=-9.5, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 2.5, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.2608398361, perimeter: 3.1329281698
            with BuildLine():
                CenterArc((1.5, 0), 1.253324025, 52.9279666936, 74.1440666127)
                Line((2.2555270422, 1), (0.7444729578, 1))
            make_face()
            # Profile area: 4.674040228, perimeter: 7.7640470978
            with BuildLine():
                Line((2.2555270422, 1), (0.7444729578, 1))
                CenterArc((1.5, 0), 1.253324025, 127.0720333064, 285.8559333873)
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch6 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 2.5185768976, perimeter: 5.6257773433
            with Locations((1.5, 0)):
                Circle(0.8953702729)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7, mode=Mode.ADD)

        # Sketch9 -> Extrude7 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            with BuildLine():
                CenterArc((-1.5, 0), 1.5, -180, 90)
                CenterArc((-1.5, 0), 1.5, -90, 180)
                CenterArc((-1.5, 0), 1.5, 90, 90)
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


# Description: This is a garbage truck or waste collection vehicle featuring a boxy, rectangular cargo body with an angular, faceted design, two rear wheels, and a hinged or articulated front section for waste loading and compaction.
def model_72714_066283c4_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 9 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 37500, perimeter: 800
            with BuildLine():
                Line((800, 0), (800, 250))
                Line((800, 250), (650, 250))
                Line((650, 250), (650, 0))
                Line((650, 0), (800, 0))
            make_face()
            # Profile area: 227500, perimeter: 2000
            with BuildLine():
                Line((650, 250), (650, 0))
                Line((650, 250), (650, 350))
                Line((650, 350), (0, 350))
                Line((0, 350), (0, 0))
                Line((0, 0), (650, 0))
            make_face()
        # Symmetric extrude, each_side=150
        extrude(amount=150, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 150), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 5654.8667764616, perimeter: 308.4955592154
            with BuildLine():
                CenterArc((180, 0), 60, -180, 180)
                Line((120, 0), (240, 0))
            make_face()
            # Profile area: 5654.8667764616, perimeter: 308.4955592154
            with BuildLine():
                Line((120, 0), (240, 0))
                CenterArc((180, 0), 60, 0, 180)
            make_face()
            # Profile area: 5654.8667764616, perimeter: 308.4955592154
            with BuildLine():
                CenterArc((650, 0), 60, 0, 180)
                Line((590, 0), (710, 0))
            make_face()
            # Profile area: 5654.8667764616, perimeter: 308.4955592154
            with BuildLine():
                Line((590, 0), (710, 0))
                CenterArc((650, 0), 60, -180, 180)
            make_face()
        # OneSide extrude, distance=-750
        extrude(amount=-750, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 150), x_dir=(1, 0, 0), z_dir=(0, 0, 1))) as sk:
            # Profile area: 7853.9816339745, perimeter: 314.159265359
            with Locations((180, 0)):
                Circle(50)
        # TwoSides extrude, along=20, against=-30
        extrude(amount=20)
        extrude(sk.sketch, amount=-30)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 170), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1963.4954084936, perimeter: 157.0796326795
            with Locations((180, 0)):
                Circle(25)
        # OneSide extrude, distance=-20
        extrude(amount=-20, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 150), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 7853.9816339745, perimeter: 314.159265359
            with Locations((650, 0)):
                Circle(50)
        # OneSide extrude, distance=-40
        extrude(amount=-40)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 150), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1963.4954084936, perimeter: 157.0796326795
            with Locations((650, 0)):
                Circle(25)
        # OneSide extrude, distance=-20
        extrude(amount=-20, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 130), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 84.4866621084, perimeter: 37.542483586
            with Locations((650, 17.7232634433)):
                Ellipse(8.1278341185, 3.3087461441)
        # OneSide extrude, distance=-115
        extrude(amount=-115, mode=Mode.SUBTRACT)

        # Sketch17 -> Extrude14 (Join)
        # Sketch on Profile plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 150), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1179.718260696, perimeter: 441.187133678
            with BuildLine():
                Line((245.7292776814, 0), (251.213551485, 0))
                CenterArc((180, 0), 71.213551485, 0, 180)
                Line((114.2707223186, 0), (108.786448515, 0))
                CenterArc((180, 0), 65.7292776814, 0, 180)
            make_face()
        # OneSide extrude, distance=20
        extrude(amount=20, mode=Mode.ADD)
    return part.part


# Description: This is a garbage truck or waste collection vehicle featuring a boxy cargo container body with a hinged or angled rear collection mechanism, rounded wheels, and a complex geometric frame structure with triangulated support elements on top.
def model_73416_5b3ea504_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 9 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 37500, perimeter: 800
            with BuildLine():
                Line((800, 0), (800, 250))
                Line((800, 250), (650, 250))
                Line((650, 250), (650, 0))
                Line((650, 0), (800, 0))
            make_face()
            # Profile area: 227500, perimeter: 2000
            with BuildLine():
                Line((650, 250), (650, 0))
                Line((650, 250), (650, 350))
                Line((650, 350), (0, 350))
                Line((0, 350), (0, 0))
                Line((0, 0), (650, 0))
            make_face()
        # Symmetric extrude, each_side=150
        extrude(amount=150, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 150), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 5654.8667764616, perimeter: 308.4955592154
            with BuildLine():
                CenterArc((180, 0), 60, -180, 180)
                Line((120, 0), (240, 0))
            make_face()
            # Profile area: 5654.8667764616, perimeter: 308.4955592154
            with BuildLine():
                Line((120, 0), (240, 0))
                CenterArc((180, 0), 60, 0, 180)
            make_face()
            # Profile area: 5654.8667764616, perimeter: 308.4955592154
            with BuildLine():
                CenterArc((650, 0), 60, 0, 180)
                Line((590, 0), (710, 0))
            make_face()
            # Profile area: 5654.8667764616, perimeter: 308.4955592154
            with BuildLine():
                Line((590, 0), (710, 0))
                CenterArc((650, 0), 60, -180, 180)
            make_face()
        # OneSide extrude, distance=-380
        extrude(amount=-380, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 150), x_dir=(1, 0, 0), z_dir=(0, 0, 1))) as sk:
            # Profile area: 7853.9816339745, perimeter: 314.159265359
            with Locations((180, 0)):
                Circle(50)
        # TwoSides extrude, along=20, against=-30
        extrude(amount=20)
        extrude(sk.sketch, amount=-30)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 170), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1963.4954084936, perimeter: 157.0796326795
            with Locations((180, 0)):
                Circle(25)
        # OneSide extrude, distance=-20
        extrude(amount=-20, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 150), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 7853.9816339745, perimeter: 314.159265359
            with Locations((650, 0)):
                Circle(50)
        # OneSide extrude, distance=-40
        extrude(amount=-40)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 150), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1963.4954084936, perimeter: 157.0796326795
            with Locations((650, 0)):
                Circle(25)
        # OneSide extrude, distance=-20
        extrude(amount=-20, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 130), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 75.3982236862, perimeter: 36.3668625119
            with Locations((650, 15)):
                Ellipse(8, 3)
        # OneSide extrude, distance=-65
        extrude(amount=-65, mode=Mode.SUBTRACT)

        # Sketch13 -> Extrude13 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 150), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1167.1344730572, perimeter: 407.3347416352
            with BuildLine():
                Line((240, 0), (245.9016, 0))
                CenterArc((180, 0), 65.9016, 0, 180)
                Line((114.0984, 0), (120, 0))
                CenterArc((180, 0), 60, 0, 180)
            make_face()
        # OneSide extrude, distance=20
        extrude(amount=20, mode=Mode.ADD)

        # Sketch14 -> Extrude14 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 150), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 779.1149780903, perimeter: 397.5574890451
            with BuildLine():
                CenterArc((650, 0), 64, 0, 180)
                Line((586, 0), (590, 0))
                CenterArc((650, 0), 60, 0, 180)
                Line((710, 0), (714, 0))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5, mode=Mode.ADD)
    return part.part


# Description: This is a rectangular storage basket or container with a hinged handle, featuring an open-top design with a curved bail handle for carrying, and a structured box-like base with slotted or ribbed side panels.
def model_73762_8c704690_0001():
    """Model: Bed v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 21 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.2950025664, perimeter: 10.5180010266
            with BuildLine():
                Line((-3.7409994867, -2.5), (-4, -2.5))
                Line((-3.7409994867, 2.5), (-3.7409994867, -2.5))
                Line((-4, 2.5), (-3.7409994867, 2.5))
                Line((-4, -2.5), (-4, 2.5))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 21 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.931829679, perimeter: 46.9126833126
            with BuildLine():
                Line((4, -2.5), (-3.7409994867, -2.5))
                Line((4, 2.5), (4, -2.5))
                Line((-3.7409994867, 2.5), (4, 2.5))
                Line((-3.7409994867, 2.5), (-3.7409994867, -2.5))
            make_face()
            with BuildLine():
                Line((3.5, 1.967897111), (3.5, -2))
                Line((3.5, -2), (0, -2))
                Line((-3.2474450586, -2), (0, -2))
                Line((-3.2474450586, 1.967897111), (-3.2474450586, -2))
                Line((0, 1.967897111), (-3.2474450586, 1.967897111))
                Line((0, 1.967897111), (3.5, 1.967897111))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 21 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 13.8876398885, perimeter: 14.935794222
            with BuildLine():
                Line((0, 1.967897111), (3.5, 1.967897111))
                Line((0, -2), (0, 1.967897111))
                Line((3.5, -2), (0, -2))
                Line((3.5, 1.967897111), (3.5, -2))
            make_face()
            # Profile area: 12.8855278661, perimeter: 14.4306843392
            with BuildLine():
                Line((0, 1.967897111), (-3.2474450586, 1.967897111))
                Line((-3.2474450586, 1.967897111), (-3.2474450586, -2))
                Line((-3.2474450586, -2), (0, -2))
                Line((0, -2), (0, 1.967897111))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)

        # Sketch7 -> Extrude8 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-3.7409994867, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 5.3618195856, perimeter: 10.6980377212
            with BuildLine():
                Line((2.012859574, 2.1638407134), (-2, 2.1638407134))
                Line((2.012859574, 3.5), (2.012859574, 2.1638407134))
                Line((-2, 3.5), (2.012859574, 3.5))
                Line((-2, 2.1638407134), (-2, 3.5))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch8 -> Extrude9 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 26.7002231305, perimeter: 21.3939169422
            with BuildLine():
                Line((-3.5, 2), (-3.5, -1.967897111))
                Line((-3.5, -1.967897111), (3.2290613601, -1.967897111))
                Line((3.2290613601, 2), (3.2290613601, -1.967897111))
                Line((3.2290613601, 2), (-3.5, 2))
            make_face()
            # Profile area: 1.2377832072, perimeter: 35.2855850827
            with BuildLine():
                Line((3.2290613601, 2), (-3.5, 2))
                Line((3.2290613601, 2.058650584), (3.2290613601, 2))
                Line((-3.584040101, 2.058650584), (3.2290613601, 2.058650584))
                Line((-3.584040101, -2.0419791362), (-3.584040101, 2.058650584))
                Line((3.2290613601, -2.0419791362), (-3.584040101, -2.0419791362))
                Line((3.2290613601, -1.967897111), (3.2290613601, -2.0419791362))
                Line((-3.5, -1.967897111), (3.2290613601, -1.967897111))
                Line((-3.5, 2), (-3.5, -1.967897111))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch9 -> Extrude10 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(4, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.967897111, perimeter: 9.935794222
            with BuildLine():
                Line((1.967897111, 1), (1.967897111, 0))
                Line((-2, 1), (1.967897111, 1))
                Line((-2, 0), (-2, 1))
                Line((1.967897111, 0), (-2, 0))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch10 -> Extrude11 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -2.5), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 5.7957197018, perimeter: 15.8387881796
            with BuildLine():
                Line((3.6034974498, 0.18410336), (-3.5, 0.18410336))
                Line((3.6034974498, 1), (3.6034974498, 0.18410336))
                Line((-3.5, 1), (3.6034974498, 1))
                Line((-3.5, 0.18410336), (-3.5, 1))
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)

        # Sketch11 -> Extrude12 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 5.7957197018, perimeter: 15.8387881796
            with BuildLine():
                Line((3.5, 0.18410336), (-3.6034974498, 0.18410336))
                Line((3.5, 1), (3.5, 0.18410336))
                Line((-3.6034974498, 1), (3.5, 1))
                Line((-3.6034974498, 0.18410336), (-3.6034974498, 1))
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)

        # Sketch13 -> Extrude16 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(-3.7409994867, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4.8359234054, perimeter: 10.2994285717
            with BuildLine():
                CenterArc((0, 2.5), 2.5, 90.0002556338, 65.8616264128)
                Line((-2.281405799, 3.5223441594), (2.2782279849, 3.5294062604))
                CenterArc((0, 2.5), 2.5, 24.3156007422, 65.6846548916)
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch14 -> Extrude17 (Cut)
        # Sketch on BRepFace
        # Sketch has 17 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-3.7409994867, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.9399164989, perimeter: 4.0792114613
            with BuildLine():
                Line((-1.2965535559, 3.5), (-1.2965535559, 2.1638407134))
                Line((-2, 3.5), (-1.2965535559, 3.5))
                Line((-2, 2.1638407134), (-2, 3.5))
                Line((-1.2965535559, 2.1638407134), (-2, 2.1638407134))
            make_face()
            # Profile area: 0.3529452729, perimeter: 2.9529687646
            with BuildLine():
                Line((-0.5764844211, 3.5), (0.6000000089, 3.5))
                Line((-0.5764844211, 3.2000000477), (-0.5764844211, 3.5))
                Line((0.6000000089, 3.2000000477), (-0.5764844211, 3.2000000477))
                Line((0.6000000089, 3.5), (0.6000000089, 3.2000000477))
            make_face()
            # Profile area: 0.3954862105, perimeter: 3.0252875077
            with BuildLine():
                Line((0.6000000089, 2.1638407134), (0.6000000089, 2.5000000373))
                Line((0.6000000089, 2.5000000373), (-0.5764844211, 2.5000000373))
                Line((-0.5764844211, 2.5000000373), (-0.5764844211, 2.1638407134))
                Line((0.6000000089, 2.1638407134), (-0.5764844211, 2.1638407134))
            make_face()
            # Profile area: 0.952493914, perimeter: 4.0980376825
            with BuildLine():
                Line((1.3000000194, 3.5), (1.3000000194, 2.1638407134))
                Line((2.012859574, 2.1638407134), (1.3000000194, 2.1638407134))
                Line((2.012859574, 3.5), (2.012859574, 2.1638407134))
                Line((1.3000000194, 3.5), (2.012859574, 3.5))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a rectangular enclosure or housing component with a hexagonal/angled top, featuring an open front panel with internal framework, and a solid right-side flange or mounting bracket.
def model_73908_60ffee0f_0001():
    """Model: L-Section Sofa v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 19 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 30, perimeter: 34
            with BuildLine():
                Line((1.5, 2.5), (5, 2.5))
                Line((8.5, 2.5), (5, 2.5))
                Line((8.5, 0), (8.5, 2.5))
                Line((8.5, 0), (9.5, 0))
                Line((9.5, 0), (9.5, 5))
                Line((9.5, 5), (0, 5))
                Line((0, 5), (0, 0))
                Line((0, 0), (1.5, 0))
                Line((1.5, 0), (1.5, 2.5))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 19 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.75, perimeter: 12
            with BuildLine():
                Line((1.5, 0), (1.5, 2.5))
                Line((5, 0), (1.5, 0))
                Line((5, 2.5), (5, 0))
                Line((1.5, 2.5), (5, 2.5))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 19 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.75, perimeter: 12
            with BuildLine():
                Line((5, 0), (8.5, 0))
                Line((8.5, 0), (8.5, 2.5))
                Line((8.5, 2.5), (5, 2.5))
                Line((5, 2.5), (5, 0))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)

        # Sketch2 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.4419532795, perimeter: 10.3497399702
            with BuildLine():
                Line((-4.7698665077, -0.2341633511), (-1.6795731244, -0.2341633511))
                Line((-4.7698665077, -2.3187399529), (-4.7698665077, -0.2341633511))
                Line((-1.6795731244, -2.3187399529), (-4.7698665077, -2.3187399529))
                Line((-1.6795731244, -0.2341633511), (-1.6795731244, -2.3187399529))
            make_face()
            # Profile area: 6.3275990793, perimeter: 10.2400254122
            with BuildLine():
                Line((-8.2807323633, -0.2341633511), (-5.245296259, -0.2341633511))
                Line((-8.2807323633, -2.3187399529), (-8.2807323633, -0.2341633511))
                Line((-5.245296259, -2.3187399529), (-8.2807323633, -2.3187399529))
                Line((-5.245296259, -0.2341633511), (-5.245296259, -2.3187399529))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)

        # Sketch6 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.2042908051, perimeter: 14.7802627531
            with BuildLine():
                Line((1.2703758287, 0.9208731304), (1.2703758287, 0.7541526116))
                Line((8.4937866866, 0.7541526116), (1.2703758287, 0.7541526116))
                Line((8.4937866866, 0.9208731304), (8.4937866866, 0.7541526116))
                Line((1.2703758287, 0.9208731304), (8.4937866866, 0.9208731304))
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 2.3780761433, perimeter: 7.6817372056
            with BuildLine():
                Line((-0.9350169829, 0.2241144143), (-4, 0.2241144143))
                Line((-0.9350169829, 1), (-0.9350169829, 0.2241144143))
                Line((-4, 1), (-0.9350169829, 1))
                Line((-4, 0.2241144143), (-4, 1))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -5), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 8.1197716699, perimeter: 16.3372205478
            with BuildLine():
                Line((-1.2703758287, 0.3417462607), (-8.2807323633, 0.3417462607))
                Line((-1.2703758287, 1.5), (-1.2703758287, 0.3417462607))
                Line((-8.2807323633, 1.5), (-1.2703758287, 1.5))
                Line((-8.2807323633, 0.3417462607), (-8.2807323633, 1.5))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude8 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(9.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.3780761433, perimeter: 7.6817372056
            with BuildLine():
                Line((4, 0.2241144143), (0.9350169829, 0.2241144143))
                Line((4, 1), (4, 0.2241144143))
                Line((0.9350169829, 1), (4, 1))
                Line((0.9350169829, 0.2241144143), (0.9350169829, 1))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude9 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 23.5032840312, perimeter: 20.4328403119
            with BuildLine():
                Line((-9.5, 0), (-9.5, -5))
                Line((-8.9835798441, 0), (-9.5, 0))
                Line((-8.9835798441, 0), (-8.9835798441, 0.2))
                Line((-8.9835798441, 0.2), (-14, 0.2))
                Line((-14, 0.2), (-14, -5))
                Line((-14, -5), (-9.5, -5))
            make_face()
            # Profile area: 2.5821007797, perimeter: 11.0328403119
            with BuildLine():
                Line((-8.9835798441, -5), (-8.9835798441, 0))
                Line((-8.9835798441, 0), (-9.5, 0))
                Line((-9.5, 0), (-9.5, -5))
                Line((-9.5, -5), (-8.9835798441, -5))
            make_face()
        # OneSide extrude, distance=-5.1
        extrude(amount=-5.1, mode=Mode.ADD)
    return part.part


# Description: This is a complex sheet metal or cast bracket/enclosure featuring an angular box-like structure with multiple planar faces, internal ribbing or bracing elements, and a protruding mounting flange or foot at the base.
def model_74050_623ff55e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5643737378, perimeter: 4.9453958172
            with BuildLine():
                Line((7.7455802687, -2.5), (7.7455802687, -0.2817218227))
                Line((8, -2.5), (7.7455802687, -2.5))
                Line((8, -0.2817218227), (8, -2.5))
                Line((8, -0.2817218227), (7.7455802687, -0.2817218227))
            make_face()
            # Profile area: 0.7127546272, perimeter: 6.1962770601
            with BuildLine():
                Line((0.2817218227, -8.0000001277), (3.129583147, -8.0000014189))
                Line((3.129583147, -8.0000014189), (3.1295832605, -7.7497236244))
                Line((3.1295832605, -7.7497236244), (0.2817218227, -7.7497236244))
                Line((0.2817218227, -7.7497236244), (0.2817218227, -8.0000001277))
            make_face()
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.4281819957, perimeter: 32.0000001277
            with BuildLine():
                Line((0.2817218227, -0.2817218227), (0.2817218227, -8.0000001277))
                Line((8, -0.2817218227), (0.2817218227, -0.2817218227))
                Line((8, 0), (8, -0.2817218227))
                Line((0, 0), (8, 0))
                Line((0, -8), (0, 0))
                Line((0.2817218227, -8.0000001277), (0, -8))
            make_face()
        # OneSide extrude, distance=7
        extrude(amount=7)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 7.7497236244), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.5533698472, perimeter: 6.0502982068
            with BuildLine():
                Line((-0.2817218227, 3.7000000551), (-3.1113050787, 3.7000000551))
                Line((-0.2817218227, 3.8955659025), (-0.2817218227, 3.7000000551))
                Line((-3.1113050787, 3.8955659025), (-0.2817218227, 3.8955659025))
                Line((-3.1113050787, 3.7000000551), (-3.1113050787, 3.8955659025))
            make_face()
        # OneSide extrude, distance=7.7
        extrude(amount=7.7, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(3.1113050787, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.4274798781, perimeter: 4.7628549155
            with BuildLine():
                Line((-2.4675834331, 3.7000000551), (-2.4675834331, 3.8955659025))
                Line((-0.2817218227, 3.7000000551), (-2.4675834331, 3.7000000551))
                Line((-0.2817218227, 3.8955659025), (-0.2817218227, 3.7000000551))
                Line((-2.4675834331, 3.8955659025), (-0.2817218227, 3.8955659025))
            make_face()
        # OneSide extrude, distance=4.8
        extrude(amount=4.8, mode=Mode.ADD)

        # Sketch5 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.2817218227, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 6.6064153498, perimeter: 11.616665496
            with BuildLine():
                Line((-3.4936079251, 7), (-3.4936079251, 5.4477829513))
                Line((-7.7497236244, 7), (-3.4936079251, 7))
                Line((-7.7497236244, 5.4477829513), (-7.7497236244, 7))
                Line((-3.4936079251, 5.4477829513), (-7.7497236244, 5.4477829513))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)

        # Sketch6 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 12 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(2.2817218227, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.3032076749, perimeter: 7.3605497968
            with BuildLine():
                Line((-5.6216657747, 5.4477829513), (-5.6216657747, 7))
                Line((-3.4936079251, 5.4477829513), (-5.6216657747, 5.4477829513))
                Line((-3.4936079251, 7), (-3.4936079251, 5.4477829513))
                Line((-5.6216657747, 7), (-3.4936079251, 7))
            make_face()
            # Profile area: 3.0799978446, perimeter: 7.0729484841
            with BuildLine():
                Line((-7.7497236244, 7), (-5.765466431, 7))
                Line((-7.7497236244, 5.4477829513), (-7.7497236244, 7))
                Line((-5.765466431, 5.4477829513), (-7.7497236244, 5.4477829513))
                Line((-5.765466431, 7), (-5.765466431, 5.4477829513))
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude6 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(2.1817218227, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0628318549, perimeter: 0.8885766009
            with Locations((-5.300000079, 6.7000000998)):
                Circle(0.1414213583)
            # Profile area: 0.0805458387, perimeter: 1.0060660316
            with Locations((-7.4601204908, 6.7000000998)):
                Circle(0.160120382)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch9 -> Extrude7 (Join)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.5245251568, perimeter: 19.6888220776
            with BuildLine():
                Line((3.129583147, -10.3009047672), (0, -10.3009047672))
                Line((3.129583147, -8), (3.129583147, -10.3009047672))
                Line((0, -8), (3.129583147, -8))
                Line((0, -10.3009047672), (0, -8))
            make_face()
            with BuildLine():
                Line((0.236160527, -10.0680453146), (0.236160527, -8.3019144587))
                Line((0.236160527, -8.3019144587), (2.8839527956, -8.3019144587))
                Line((2.8839527956, -8.3019144587), (2.8839527956, -10.0680453146))
                Line((2.8839527956, -10.0680453146), (0.236160527, -10.0680453146))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch9 -> Extrude8 (Join)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.6763476256, perimeter: 8.827846249
            with BuildLine():
                Line((2.8839527956, -10.0680453146), (0.236160527, -10.0680453146))
                Line((2.8839527956, -8.3019144587), (2.8839527956, -10.0680453146))
                Line((0.236160527, -8.3019144587), (2.8839527956, -8.3019144587))
                Line((0.236160527, -10.0680453146), (0.236160527, -8.3019144587))
            make_face()
        # OneSide extrude, distance=0.8
        extrude(amount=0.8, mode=Mode.ADD)
    return part.part


# Description: This is a flat, rectangular plate with a parallelogram shape, featuring a simple planar geometry with no holes, slots, or additional features.
def model_77686_d2bfddf4_0000():
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
        # Sketch4 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 18 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.5377269315, perimeter: 10.51530714
            with BuildLine():
                CenterArc((-1.1523013742, -5.4379192788), 0.3, -147.6525565006, 69.4459861855)
                Line((-0.0921819494, -5.5230449746), (-1.0909862342, -5.7315865285))
                Line((1.2328078269, -5.2567790865), (-0.0921819494, -5.5230449746))
                CenterArc((1.2077865218, -5.1322683067), 0.127, -78.6373575321, 48.2031217787)
                Line((1.5773731596, -4.7539007641), (1.3172873375, -5.1966000359))
                CenterArc((1.6868739752, -4.8182324933), 0.127, 112.4054088834, 37.1603553632)
                Line((2.3521021552, -4.4066016944), (1.6384669531, -4.7008197163))
                Line((2.3521021552, -4.4066016944), (1.519724325, -4.5981807188))
                Line((1.519724325, -4.5981807188), (-1.2945054819, -4.4924819467))
                CenterArc((-1.2846428745, -4.2298900241), 0.2627770706, -156.0258646575, 63.87492153)
                CenterArc((-1.6407934777, -4.3882658827), 0.127, 23.9741353425, 66.0258646575)
                Line((-1.6407934777, -4.2612658827), (-2.0788525636, -4.2612658827))
                CenterArc((-2.0788525636, -4.3882658827), 0.127, 90, 91.7965054723)
                _nurbs_edge([(-1.6022268672, -5.3754465652), (-1.60292876, -5.3753618344), (-1.6157961546, -5.3737768884), (-1.6409777773, -5.3695475777), (-1.6788233766, -5.3599304932), (-1.7298443618, -5.3404904929), (-1.7936387685, -5.305499602), (-1.8575697504, -5.2593230652), (-1.9202695903, -5.2020938008), (-1.9800454757, -5.134117631), (-2.0351147929, -5.0558112822), (-2.0838397988, -4.9676605621), (-2.1250063414, -4.8702155775), (-2.1580346123, -4.764088572), (-2.1827432964, -4.649864295), (-2.1960365699, -4.5514877874), (-2.2023157956, -4.4741457208), (-2.204878715, -4.4207979339), (-2.2057586369, -4.3932517003), (-2.2057901399, -4.3922473071)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.0628189882, 0.0628189882, 0.0628189882, 0.0628189882, 0.0628189882, 0.0628189882, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9333333333, 0.9358548198, 0.9358548198, 0.9358548198, 0.9358548198, 0.9358548198, 0.9358548198], 5)
                CenterArc((-1.6174474937, -5.5015311897), 0.127, 32.3474434994, 50.7692577541)
                Line((-1.5101554711, -5.4335795753), (-1.4057470969, -5.5984349031))
            make_face()
        # Symmetric extrude, each_side=0.71374
        extrude(amount=0.71374, both=True)

        # Sketch5 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 15 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.0216449162, perimeter: 13.9975528657
            with BuildLine():
                _nurbs_edge([(0.6378822948, -0.71374), (0.6353332134, -0.7139385791), (0.6065804909, -0.7161326862), (0.5515740723, -0.7193526335), (0.4704277528, -0.7216487508), (0.3638851859, -0.7211181491), (0.2358991896, -0.7177875653), (0.1353746208, -0.7151145603), (0.0610462799, -0.7139899241), (0.0119611636, -0.71374), (-0.0124646131, -0.71374)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.6601806937, 0.6601806937, 0.6601806937, 0.6601806937, 0.6601806937, 0.6601806937, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9333333333, 1, 1, 1, 1, 1, 1], 5)
                Line((0.6759084398, -1.2296638119), (-0.0124646131, -0.71374))
                Line((2.9785935336, -1.3965250506), (0.6759084398, -1.2296638119))
                Line((2.9785935336, 1.0213075906), (2.9785935336, -1.3965250506))
                Line((1.0430031649, 1.3288751812), (2.9785935336, 1.0213075906))
                Line((-0.0124646131, 0.71374), (1.0430031649, 1.3288751812))
                _nurbs_edge([(0.6378822948, 0.71374), (0.6353332134, 0.7139385791), (0.6065804909, 0.7161326862), (0.5515740723, 0.7193526335), (0.4704277528, 0.7216487508), (0.3638851859, 0.7211181491), (0.2358991896, 0.7177875653), (0.1353746208, 0.7151145603), (0.0610462799, 0.7139899241), (0.0119611636, 0.71374), (-0.0124646131, 0.71374)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.6601806937, 0.6601806937, 0.6601806937, 0.6601806937, 0.6601806937, 0.6601806937, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9333333333, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(1.4792331373, 0.167100353), (1.4733106632, 0.184695563), (1.4582410394, 0.2259048851), (1.4309109449, 0.2879617986), (1.3858945767, 0.3660058045), (1.3154373914, 0.4528453941), (1.2259445479, 0.5305942511), (1.1227393829, 0.5939907216), (1.0080995895, 0.6433702178), (0.8873154942, 0.6787593121), (0.7870296982, 0.6976784134), (0.711343996, 0.7072803761), (0.6615341797, 0.7118974652), (0.6378822948, 0.71374)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.0853238005, 0.0853238005, 0.0853238005, 0.0853238005, 0.0853238005, 0.0853238005, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6601806937, 0.6601806937, 0.6601806937, 0.6601806937, 0.6601806937, 0.6601806937], 5)
                CenterArc((1.5305941715, 0.2059875961), 0.0644218404, -142.8693570997, 43.1554159682)
                Line((2.3521021552, 0), (1.519724325, 0.1424894075))
                Line((2.3521021552, 0), (1.519724325, -0.1424894075))
                CenterArc((1.5305941715, -0.2059875961), 0.0644218404, 99.7139411315, 43.1554159682)
                _nurbs_edge([(1.4792331373, -0.167100353), (1.4733106632, -0.184695563), (1.4582410394, -0.2259048851), (1.4309109449, -0.2879617986), (1.3858945767, -0.3660058045), (1.3154373914, -0.4528453941), (1.2259445479, -0.5305942511), (1.1227393829, -0.5939907216), (1.0080995895, -0.6433702178), (0.8873154942, -0.6787593121), (0.7870296982, -0.6976784134), (0.711343996, -0.7072803761), (0.6615341797, -0.7118974652), (0.6378822948, -0.71374)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.0853238005, 0.0853238005, 0.0853238005, 0.0853238005, 0.0853238005, 0.0853238005, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6601806937, 0.6601806937, 0.6601806937, 0.6601806937, 0.6601806937, 0.6601806937], 5)
            make_face()
        # OneSide extrude, distance=-7.10184
        extrude(amount=-7.10184, mode=Mode.SUBTRACT)

        # Sketch14 -> Extrude5 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 68 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0222040954, perimeter: 0.6930595754
            with BuildLine():
                Line((-1.4969177003, -10.2389228752), (-1.4007453529, -10.4705162448))
                Line((-1.5924960535, -10.4705162448), (-1.4969177003, -10.2389228752))
                Line((-1.4007453529, -10.4705162448), (-1.5924960535, -10.4705162448))
            make_face()
            # Profile area: 50.8789550583, perimeter: 65.9731912583
            with BuildLine():
                Line((6.5533678831, -12.5151297445), (-6.2455319202, -12.5151297445))
                Line((6.5533678831, -8.2094124075), (6.5533678831, -12.5151297445))
                Line((-6.2455319202, -8.2094124075), (6.5533678831, -8.2094124075))
                Line((-6.2455319202, -12.5151297445), (-6.2455319202, -8.2094124075))
            make_face()
            with BuildLine():
                Line((-4.0818697936, -9.7485762067), (-4.0818697936, -10.4222817217))
                Line((-4.0818697936, -9.7485762067), (-3.8133887214, -9.7485762067))
                Line((-3.8133887214, -10.9375258488), (-3.8133887214, -9.7485762067))
                Line((-3.9501620978, -10.9375258488), (-3.8133887214, -10.9375258488))
                Line((-4.5225840064, -10.2905740259), (-3.9501620978, -10.9375258488))
                Line((-4.5225840064, -10.2905740259), (-4.5225840064, -10.9375258488))
                Line((-4.8058861257, -10.9375258488), (-4.5225840064, -10.9375258488))
                Line((-4.8058861257, -10.9375258488), (-4.8058861257, -9.7485762067))
                Line((-4.677963325, -9.7485762067), (-4.8058861257, -9.7485762067))
                Line((-4.0818697936, -10.4222817217), (-4.677963325, -9.7485762067))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((0.0463170718, -10.3390478811), (0.0463170718, -10.9375258488))
                Line((-0.2602683175, -10.9375258488), (0.0463170718, -10.9375258488))
                Line((-0.2602683175, -10.9375258488), (-0.2602683175, -9.7485762067))
                Line((-0.1279723693, -9.7485762067), (-0.2602683175, -9.7485762067))
                Line((-0.1279723693, -9.7485762067), (0.4838963912, -10.4255329838))
                Line((0.4838963912, -10.4255329838), (0.4838963912, -9.7485762067))
                Line((0.7691595296, -9.7485762067), (0.4838963912, -9.7485762067))
                Line((0.7691595296, -9.7485762067), (0.7691595296, -10.9375258488))
                Line((0.5872526008, -10.9375258488), (0.7691595296, -10.9375258488))
                Line((0.5872526008, -10.9375258488), (0.0463170718, -10.3390478811))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-2.7698585164, -9.7485762067), (-2.7698585164, -10.9375258488))
                Line((-3.0231425467, -10.9375258488), (-2.7698585164, -10.9375258488))
                Line((-3.0231425467, -9.7485762067), (-3.0231425467, -10.9375258488))
                Line((-2.7698585164, -9.7485762067), (-3.0231425467, -9.7485762067))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-1.3676713658, -9.7485762067), (-0.8880985535, -10.9375258488))
                Line((-1.2105699273, -10.9375258488), (-0.8880985535, -10.9375258488))
                Line((-1.2105699273, -10.9375258488), (-1.2954241641, -10.7271565119))
                Line((-1.2954241641, -10.7271565119), (-1.6984112364, -10.7271565119))
                Line((-1.6984112364, -10.7271565119), (-1.7852304524, -10.9375258488))
                Line((-2.0539565972, -10.9375258488), (-1.7852304524, -10.9375258488))
                Line((-2.0539565972, -10.9375258488), (-1.6281290139, -9.7485762067))
                Line((-1.3676713658, -9.7485762067), (-1.6281290139, -9.7485762067))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((1.814848896, -10.0723472534), (1.4758405287, -10.0723472534))
                Line((1.4758405287, -10.0723472534), (1.4758405287, -9.7485762067))
                Line((2.4391204016, -9.7485762067), (1.4758405287, -9.7485762067))
                Line((2.4391204016, -9.7485762067), (2.4391204016, -10.0723472534))
                Line((2.4391204016, -10.0723472534), (2.1207832762, -10.0723472534))
                Line((2.1207832762, -10.0723472534), (2.1207832762, -10.9375258488))
                Line((1.814848896, -10.9375258488), (2.1207832762, -10.9375258488))
                Line((1.814848896, -10.9375258488), (1.814848896, -10.0723472534))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((3.1709965349, -10.9375258488), (3.1709965349, -9.7485762067))
                Line((3.1709965349, -9.7485762067), (3.4355884313, -9.7485762067))
                Line((3.4355884313, -9.7485762067), (3.4355884313, -10.9375258488))
                Line((3.1709965349, -10.9375258488), (3.4355884313, -10.9375258488))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.7003320357, -10.3407808044), 0.2894269156, 36.5906996008, 279.2782191578)
                Line((4.9080678224, -10.5423094187), (5.1349723251, -10.7430171832))
                CenterArc((4.7003320357, -10.3407808044), 0.5922045977, 42.7145424102, 274.5028456312)
                Line((4.9327170292, -10.168254997), (5.1354498902, -9.9390610785))
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.3175
        extrude(amount=0.3175, both=True)

        # Sketch15 -> Extrude6 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 100806.25, perimeter: 1270
            with BuildLine():
                Line((176.388959547, -178.3547400488), (-141.111040453, -178.3547400488))
                Line((176.388959547, 139.1452599512), (176.388959547, -178.3547400488))
                Line((-141.111040453, 139.1452599512), (176.388959547, 139.1452599512))
                Line((-141.111040453, -178.3547400488), (-141.111040453, 139.1452599512))
            make_face()
        # OneSide extrude, distance=-7.62
        extrude(amount=-7.62)
    return part.part


# Description: This is a VR controller or handheld device mount featuring a cylindrical grip handle with an angled front faceplate, ventilation slots on the side panel, and a textured grip surface for ergonomic handling.
def model_83429_64b0cab4_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 27 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 86.480566964, perimeter: 62.8801502739
            with BuildLine():
                Line((-5.8593783389, -3.1812496759), (-8, -7))
                CenterArc((-3.2424802932, -4.6481663806), 3, 90, 60.7269480815)
                Line((6.7953813026, -1.6481663806), (-3.2424802932, -1.6481663806))
                CenterArc((6.7953813026, -4.6481663806), 3, 26.5583774112, 63.4416225888)
                Line((11.3248623665, -7), (9.4788191306, -3.3068381496))
                CenterArc((12.6624311832, -7), 1.3375688168, 58.7752807517, 121.2247192483)
                Line((9.5101912445, 0.972147422), (13.3558214981, -5.8561904831))
                CenterArc((6.8962321844, -0.5), 3, 29.3876403758, 9.6546964073)
                Line((9.3256856523, 1.1683766277), (9.2262743872, 1.3896833949))
                CenterArc((4.7647157327, -0.8804165275), 5, 24.1896732834, 3.0899085272)
                CenterArc((6.8962321844, -0.5), 3, 39.5746172524, 50.4253827476)
                Line((-3.1888035968, 2.5), (6.8962321844, 2.5))
                CenterArc((-3.1888035968, -0.5), 3, 90, 62.2414593989)
                Line((-9.5661605206, -6.1757049892), (-5.8435582639, 0.8972392985))
                CenterArc((-9, -7), 1, 0, 124.4829187979)
            make_face()
            # Profile area: 2.6576142394, perimeter: 6.8178585822
            with BuildLine():
                Line((14, -7), (11.3248623665, -7))
                Line((13.3558214981, -5.8561904831), (14, -7))
                CenterArc((12.6624311832, -7), 1.3375688168, 58.7752807517, 121.2247192483)
            make_face()
            # Profile area: 18.6755125874, perimeter: 33.4056242366
            with BuildLine():
                CenterArc((4.7647157327, -0.8804165275), 5, 27.2795818106, 62.7204181894)
                Line((-1.128926974, 4.1195834725), (4.7647157327, 4.1195834725))
                CenterArc((-1.128926974, -0.8804165275), 5, 90, 62.2414593989)
                Line((-5.8435582639, 0.8972392985), (-5.553518086, 1.4483156367))
                CenterArc((-3.1888035968, -0.5), 3, 90, 62.2414593989)
                Line((-3.1888035968, 2.5), (6.8962321844, 2.5))
                CenterArc((6.8962321844, -0.5), 3, 39.5746172524, 50.4253827476)
            make_face()
            # Profile area: 1.4984659032, perimeter: 5.1041296612
            with BuildLine():
                CenterArc((-9, -7), 1, 0, 124.4829187979)
                Line((-10, -7), (-9.5661605206, -6.1757049892))
                Line((-8, -7), (-10, -7))
            make_face()
            # Profile area: 0.0723304236, perimeter: 1.9004487237
            with BuildLine():
                CenterArc((-9, -7), 1, 124.4829187979, 55.5170812021)
                Line((-10, -7), (-9.5661605206, -6.1757049892))
            make_face()
            # Profile area: 0.1526822943, perimeter: 2.6848400669
            with BuildLine():
                Line((13.3558214981, -5.8561904831), (14, -7))
                CenterArc((12.6624311832, -7), 1.3375688168, 0, 58.7752807517)
            make_face()
            # Profile area: 2.8102965337, perimeter: 6.877234002
            with BuildLine():
                CenterArc((12.6624311832, -7), 1.3375688168, 180, 180)
                Line((14, -7), (11.3248623665, -7))
            make_face()
            # Profile area: 1.5707963268, perimeter: 5.1415926536
            with BuildLine():
                Line((-8, -7), (-10, -7))
                CenterArc((-9, -7), 1, 180, 180)
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.0801244057, perimeter: 5.1126914835
            with Locations((2, -2)):
                Circle(0.8137101221)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.7941514129, perimeter: 12.9390543944
            with BuildLine():
                CenterArc((2, -2), 1.2456043437, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((2, -2), 0.8137101221, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.6481663806), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 4.7647157327, perimeter: 11.5294314655
            with BuildLine():
                Line((4.7647157327, 3.5), (4.7647157327, 4.5))
                Line((0, 4.5), (4.7647157327, 4.5))
                Line((0, 3.5), (0, 4.5))
                Line((4.7647157327, 3.5), (0, 3.5))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.25, perimeter: 6
            with BuildLine():
                Line((-6, -3), (-4.9393398282, -1.9393398282))
                Line((-4.9393398282, -1.9393398282), (-6, -0.8786796564))
                Line((-6, -0.8786796564), (-7.0606601718, -1.9393398282))
                Line((-6, -3), (-7.0606601718, -1.9393398282))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 4.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1570796374, perimeter: 1.4049629671
            with Locations((-5.4000000805, -1.9000000283)):
                Circle(0.2236068011)
            # Profile area: 0.1525388529, perimeter: 1.6986886449
            with BuildLine():
                Line((-6.3414742969, -1.7600951215), (-5.7500460515, -1.7600951215))
                Line((-6.3414742969, -2.0180111984), (-6.3414742969, -1.7600951215))
                Line((-5.7500460515, -2.0180111984), (-6.3414742969, -2.0180111984))
                Line((-5.7500460515, -1.7600951215), (-5.7500460515, -2.0180111984))
            make_face()
            # Profile area: 0.1190539888, perimeter: 1.2231420796
            with Locations((-6.7000000998, -1.9000000283)):
                Circle(0.1946691081)
            # Profile area: 0.1570796374, perimeter: 1.4049629671
            with Locations((-6.0000000894, -2.5000000373)):
                Circle(0.2236068011)
            # Profile area: 0.1570796374, perimeter: 1.4049629671
            with Locations((-6.0000000894, -1.3000000194)):
                Circle(0.2236068011)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8, mode=Mode.ADD)

        # Sketch7 -> Extrude7 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, -4.1195834725), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.5820552229, perimeter: 2.7045002587
            with Locations((-2.0697870435, 4.1946374666)):
                Circle(0.4304345848)
        # OneSide extrude, distance=2.5
        extrude(amount=2.5, mode=Mode.ADD)
    return part.part


# Description: This is an earbud or earphone with a compact design featuring a rounded, bulbous outer shell with mesh acoustic elements, a curved stem, and an ergonomic hook or ear-fit wing that extends from the main body to secure it in the ear.
def model_91401_961dbead_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 5.1750949804, perimeter: 18.0607819003
            with BuildLine():
                CenterArc((-1.450088477, 5.2238105232), 4.0895333901, -80.8532335109, 0.5466730419)
                CenterArc((-0.6000000089, 0.1000000015), 1.1045361182, 100.4321774026, 185.6765745961)
                CenterArc((-0.6000000089, 0.1000000015), 1.1045361182, -73.8912480013, 0.4739676226)
                CenterArc((0, 0), 1, -41.2416387966, 294.6967682412)
                Line((0.7519360182, -0.6592360917), (1.311533442, -0.4976239903))
                Line((1.311533442, -0.4976239903), (1.452904358, -0.4567959774))
                CenterArc((1.1000000164, 0.5000000075), 1.0198039179, -69.7540235462, 123.6834735)
                Line((1.7004411603, 1.3242999915), (-0.6000000089, 3.0000000447))
                CenterArc((-0.5500000082, 2.750000041), 0.2549509795, 101.309932474, 90)
                CenterArc((-3.2679588863, -1.8899412248), 5.2113704361, 42.889871402, 18.843717918)
                CenterArc((-1.450088477, 5.2238105232), 4.0895333901, -80.3065604691, 19.5899045872)
            make_face()
            # Profile area: 3.0260007121, perimeter: 6.2224989775
            with BuildLine():
                CenterArc((0, 0), 1, -106.5448705554, 0.0040133494)
                Line((-0.2846989999, -0.9586169618), (0.7519360182, -0.6592360917))
                CenterArc((0, 0), 1, -41.2416387966, 294.6967682412)
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 2.7407607482, perimeter: 7.6913411076
            with BuildLine():
                Line((-0.6000000089, -2.8000000119), (-0.4303272468, -2.8000000119))
                Line((-0.200000003, -3.6000000536), (-0.4303272468, -2.8000000119))
                Line((0.200000003, -3.6000000536), (-0.200000003, -3.6000000536))
                Line((0.200000003, -3.6000000536), (0.4303272468, -2.8000000119))
                Line((0.4303272468, -2.8000000119), (0.6000000089, -2.8000000119))
                Line((0.6000000089, -0.8000000119), (0.6000000089, -2.8000000119))
                CenterArc((0, 0), 1.0000000149, -126.8698976458, 73.7397952917)
                Line((-0.6000000089, -0.8000000119), (-0.6000000089, -2.8000000119))
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.ADD)

        # Sketch8 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            Circle(0.75)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch10 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch11 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.7), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.2644910431, perimeter: 7.2256631033
            with BuildLine():
                CenterArc((0, 0), 0.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)
    return part.part


# Description: This is a skid plate or undercarriage protection component with a trapezoidal shape, featuring a curved upper surface, reinforcing ribs throughout, a central rectangular opening, and angled flanges on both sides for mounting.
def model_99367_dc809a62_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 21 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 16.7137255785, perimeter: 31.9424203205
            with BuildLine():
                CenterArc((-1.6175191142, 4.8262828731), 1.5, -170.4899404926, 84.36170082)
                Line((1.0000000149, 3.5000000522), (-1.5162337915, 3.329706352))
                CenterArc((1.0299918958, 3.0568445823), 0.4441692058, 64.7551902189, 29.1165701085)
                CenterArc((1.7205462001, 4.5213730627), 1.175, -115.2448097811, 31.3298279485)
                Line((4.1426319831, 3.5979209943), (1.8451009775, 3.3529933695))
                CenterArc((4.1000000611, 3.9978275489), 0.4021725167, -83.9149818327, 173.9149818327)
                Line((-0.5316313479, 4.4000000656), (4.1000000611, 4.4000000656))
                CenterArc((-0.5316313479, 5.4000000656), 1, -159.1305659708, 69.1305659708)
                CenterArc((1.6822641867, 6.2440515545), 3.3693366908, -176.5124101403, 17.3818441695)
                CenterArc((-2.6789804837, 5.9782545606), 1, 3.4875898597, 17.3976317572)
                Line((-2.7552645061, 8.9832498664), (-1.7446840265, 6.3347515874))
                CenterArc((-3.6895609633, 8.6267528396), 1, 20.8852216169, 15.3967393087)
                CenterArc((-0.0122953715, 11.3261908964), 3.5617154729, 169.5566419088, 46.7253190169)
                CenterArc((-3.4166660836, 11.9536732225), 0.1, 146.1684716874, 23.3881702214)
                CenterArc((-3.899110113, 12.2770259415), 0.4807832835, -33.8315283126, 223.3415878199)
                Line((-3.0969040272, 4.5784517226), (-4.3732858037, 12.1975905586))
            make_face()
        # OneSide extrude, distance=8
        extrude(amount=8)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3.4166726091, 0.2312336076), x_dir=(-1, 0, 0), z_dir=(0, -0.9977176807, -0.0675235485))):
            # Profile area: 1.5707963268, perimeter: 5.1415926536
            with BuildLine():
                CenterArc((-4, 1.2340501189), 1, -180, 180)
                Line((-3, 1.2340501189), (-5, 1.2340501189))
            make_face()
            # Profile area: 1.5707963268, perimeter: 5.1415926536
            with BuildLine():
                Line((-3, 1.2340501189), (-5, 1.2340501189))
                CenterArc((-4, 1.2340501189), 1, 0, 180)
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.4189549284, 0.1637100591), x_dir=(-1, 0, 0), z_dir=(0, -0.9977176807, -0.0675235485))):
            # Profile area: 2.0106192983, perimeter: 5.0265482457
            with Locations((-4, 1.2340501189)):
                Circle(0.8)
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (NewBody)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(8, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.4627374675, perimeter: 9.1296617753
            with BuildLine():
                Line((0.002939306, 6.5631240235), (-0.9615879371, 6.5631240235))
                Line((1.8039444977, 6.5631240235), (0.002939306, 6.5631240235))
                CenterArc((1.8485869687, 7.0817393994), 0.5205332443, -94.9198993869, 190.2757244297)
                Line((1.8000000268, 7.6000001132), (-1.3990965585, 7.3000848084))
                CenterArc((-1.3035035085, 6.9378042242), 0.3746802008, 104.7814292149, 165.2185707851)
                Line((-0.9615879371, 6.5631240235), (-1.3035035085, 6.5631240235))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch4 -> Extrude5 (NewBody)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(8, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.5594285972, perimeter: 5.5330407531
            with BuildLine():
                CenterArc((1.6822641867, 6.2440515545), 3.3693366908, -166.1921612874, 7.0615953166)
                CenterArc((-0.5316313479, 5.4000000656), 1, -159.1305659708, 34.1123442408)
                Line((0.002939306, 6.5631240235), (-1.1054682695, 4.5810304767))
                Line((0.002939306, 6.5631240235), (-0.9615879371, 6.5631240235))
                Line((-0.9615879371, 6.5631240235), (-1.5897041884, 5.439904374))
            make_face()
            # Profile area: 0.9064499621, perimeter: 3.98313664
            with BuildLine():
                Line((-1.5897041884, 5.439904374), (-2.1899835792, 4.3664635812))
                CenterArc((-1.709585751, 4.3631271037), 0.4804094144, 179.6020735423, 122.3670929549)
                Line((-1.1054682695, 4.5810304767), (-1.4552268307, 3.9555798732))
                CenterArc((-0.5316313479, 5.4000000656), 1, -159.1305659708, 34.1123442408)
                CenterArc((1.6822641867, 6.2440515545), 3.3693366908, -166.1921612874, 7.0615953166)
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch5 -> Extrude6 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(8.2, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.6175245807, perimeter: 3.1276462925
            with BuildLine():
                CenterArc((-1.0000000149, 5.500000082), 1.0447594636, -146.8966671423, 47.6325765456)
                Line((-1.8751813822, 4.9294039804), (-2.1899835792, 4.3664635812))
                CenterArc((-1.709585751, 4.3631271037), 0.4804094144, 179.6020735423, 122.3670929549)
                Line((-1.4552268307, 3.9555798732), (-1.1681909202, 4.468867619))
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(8.1, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((-1.9022825437, 4.5600838922)):
                Circle(0.05)
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((-1.473592518, 4.3098824801)):
                Circle(0.05)
            # Profile area: 0.0239916103, perimeter: 0.5490787436
            with Locations((-1.8460497879, 4.1511302012)):
                Circle(0.0873885962)
        # OneSide extrude, distance=-0.04
        extrude(amount=-0.04, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude8 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(8.06, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((-1.8460497879, 4.1511302012)):
                Circle(0.05)
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4, mode=Mode.SUBTRACT)
    return part.part


MODELS = {
    "model_54726_96c2c7c8_0000": {"func": model_54726_96c2c7c8_0000, "volume": 16.6378746934, "area": 79.670789695},
    "model_55021_bf798ad2_0000": {"func": model_55021_bf798ad2_0000, "volume": 75.7930678335, "area": 226.2564893739},
    "model_55082_55dae462_0000": {"func": model_55082_55dae462_0000, "volume": 18.1578440749, "area": 96.5961523342},
    "model_55284_834c8e1d_0000": {"func": model_55284_834c8e1d_0000, "volume": 7.853981634, "area": 37.6991118431},
    "model_55341_a059c86e_0000": {"func": model_55341_a059c86e_0000, "volume": 2701, "area": 2549},
    "model_55423_a50f82f4_0000": {"func": model_55423_a50f82f4_0000, "volume": 257.0981747704, "area": 470.6780972451},
    "model_55605_2f8bc12e_0010": {"func": model_55605_2f8bc12e_0010, "volume": 29.1357585879, "area": 76.5109758041},
    "model_55611_69142616_0017": {"func": model_55611_69142616_0017, "volume": 443.9016024816, "area": 564.5279106691},
    "model_55749_6526b76b_0000": {"func": model_55749_6526b76b_0000, "volume": 663.2107904036, "area": 996.6063925375},
    "model_57140_c8f10944_0000": {"func": model_57140_c8f10944_0000, "volume": 22013.7635746859, "area": 6733.1555719051},
    "model_57830_d9dbe398_0000": {"func": model_57830_d9dbe398_0000, "volume": 0.021457689, "area": 0.6719183429},
    "model_57837_62fa414f_0000": {"func": model_57837_62fa414f_0000, "volume": 131.0657013758, "area": 334.8979973124},
    "model_60975_54324202_0000": {"func": model_60975_54324202_0000, "volume": 434.9857722415, "area": 509.21376713},
    "model_61469_c09267fc_0000": {"func": model_61469_c09267fc_0000, "volume": 910.2559087595, "area": 2865.8756015356},
    "model_63539_dd7fddaa_0005": {"func": model_63539_dd7fddaa_0005, "volume": 45.1008061946, "area": 287.3915552266},
    "model_69239_a96344a9_0000": {"func": model_69239_a96344a9_0000, "volume": 349.4555477661, "area": 423.7828357721},
    "model_69455_034b69e7_0000": {"func": model_69455_034b69e7_0000, "volume": 1014.2459994001, "area": 1439.0226479578},
    "model_70621_14f013e9_0000": {"func": model_70621_14f013e9_0000, "volume": 89.2585970934, "area": 170.3131471148},
    "model_72714_066283c4_0000": {"func": model_72714_066283c4_0000, "volume": 76757303.09681274, "area": 1313856.9331703938},
    "model_73416_5b3ea504_0000": {"func": model_73416_5b3ea504_0000, "volume": 76761128.7647188306, "area": 1315162.3372336356},
    "model_73762_8c704690_0001": {"func": model_73762_8c704690_0001, "volume": 79.3387933709, "area": 179.4619737296},
    "model_73908_60ffee0f_0001": {"func": model_73908_60ffee0f_0001, "volume": 310.0395051077, "area": 399.4000315946},
    "model_74050_623ff55e_0000": {"func": model_74050_623ff55e_0000, "volume": 63.6429864189, "area": 402.9502257069},
    "model_77686_d2bfddf4_0000": {"func": model_77686_d2bfddf4_0000, "volume": 768180.7646611456, "area": 211453.2729448172},
    "model_83429_64b0cab4_0000": {"func": model_83429_64b0cab4_0000, "volume": 571.1841201913, "area": 626.061378097},
    "model_91401_961dbead_0000": {"func": model_91401_961dbead_0000, "volume": 8.007820058, "area": 40.5914500513},
    "model_99367_dc809a62_0000": {"func": model_99367_dc809a62_0000, "volume": 138.9423838208, "area": 321.2131351479},
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
