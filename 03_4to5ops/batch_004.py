"""Batch 004 - passing/03_4to5ops
104 models bundled from Fusion360 Gallery reconstructions.
"""

from build123d import *
from build123d import Edge, BuildLine
from collections import Counter
from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
from OCP.Geom import Geom_BSplineCurve
from OCP.TColStd import TColStd_Array1OfReal, TColStd_Array1OfInteger
from OCP.TColgp import TColgp_Array1OfPnt
from OCP.gp import gp_Pnt


def model_141771_d5c3e167_0005():
    """Model: Mirror reference"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.47625), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 70.48373, perimeter: 80.518
            with BuildLine():
                Line((-6.9849999189, 2.7305), (12.0650000811, 2.7305))
                Line((-6.9849999189, -2.7305), (-6.9849999189, 2.7305))
                Line((12.0650000811, -2.7305), (-6.9849999189, -2.7305))
                Line((12.0650000811, 2.7305), (12.0650000811, -2.7305))
            make_face()
            with BuildLine():
                Line((-6.604, -1.27), (6.604, -1.27))
                Line((-6.604, 1.27), (-6.604, -1.27))
                Line((6.604, 1.27), (-6.604, 1.27))
                Line((6.604, -1.27), (6.604, 1.27))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 33.54832, perimeter: 31.496
            with BuildLine():
                Line((6.604, -1.27), (6.604, 1.27))
                Line((6.604, 1.27), (-6.604, 1.27))
                Line((-6.604, 1.27), (-6.604, -1.27))
                Line((-6.604, -1.27), (6.604, -1.27))
            make_face()
        # OneSide extrude, distance=0.254
        extrude(amount=0.254)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-6.9849999189, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.7629017, perimeter: 11.2085427706
            with BuildLine():
                Line((0.73025, -2.7305), (0.73025, 2.7305))
                Line((1.00965, 2.7305), (0.73025, -2.7305))
                Line((0.73025, 2.7305), (1.00965, 2.7305))
            make_face()
        # OneSide extrude, distance=-19.05
        extrude(amount=-19.05, mode=Mode.ADD)
    return part.part


def model_142046_0977a838_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            Circle(1.5)
        # OneSide extrude, distance=4
        extrude(amount=4)
    return part.part


def model_142246_0851be5e_0003():
    """Model: Component15"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 28.2743338823, perimeter: 56.5486677646
            with BuildLine():
                CenterArc((0, 0), 5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 18.4390488684, perimeter: 46.1327412287
            with BuildLine():
                CenterArc((0, 0), 4, 0, 360)
            make_face()
            with BuildLine():
                Line((-3.0310889132, 1.75), (-3.0310889132, -1.75))
                Line((0, 3.5), (-3.0310889132, 1.75))
                Line((3.0310889132, 1.75), (0, 3.5))
                Line((3.0310889132, -1.75), (3.0310889132, 1.75))
                Line((0, -3.5), (3.0310889132, -1.75))
                Line((-3.0310889132, -1.75), (0, -3.5))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 24.7578501185, perimeter: 30.4247779608
            with BuildLine():
                Line((-3.0310889132, -1.75), (0, -3.5))
                Line((0, -3.5), (3.0310889132, -1.75))
                Line((3.0310889132, -1.75), (3.0310889132, 1.75))
                Line((3.0310889132, 1.75), (0, 3.5))
                Line((0, 3.5), (-3.0310889132, 1.75))
                Line((-3.0310889132, 1.75), (-3.0310889132, -1.75))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            Circle(1.5)
        # OneSide extrude, distance=3
        extrude(amount=3)
    return part.part


def model_142246_0851be5e_0013():
    """Model: Component30"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 27 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 26.3315755524, perimeter: 30.092850154
            with BuildLine():
                CenterArc((10.8, 7.6), 3.4, -90, 31.2264261088)
                Line((2.5, 4.2), (10.8, 4.2))
                Line((2.5, 0), (2.5, 4.2))
                CenterArc((0, 0), 2.5, -58.7735738912, 58.7735738912)
                Line((12.5626329898, 4.6925741724), (1.296053669, -2.1378131086))
            make_face()
        # OneSide extrude, distance=2.2
        extrude(amount=2.2)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 27 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 29.1174962053, perimeter: 28.3132465286
            with BuildLine():
                Line((0, 4.2), (2.5, 4.2))
                CenterArc((0, 7.6), 3.4, -137.3320745059, 47.3320745059)
                Line((-2.5, 0), (-2.5, 5.2956562756))
                CenterArc((0, 0), 2.5, -180, 121.2264261088)
                CenterArc((0, 0), 2.5, -58.7735738912, 58.7735738912)
                Line((2.5, 0), (2.5, 4.2))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.9, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3.4
        extrude(amount=3.4, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 27 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 70.2882276049, perimeter: 73.9876080052
            with BuildLine():
                CenterArc((10.8, 7.6), 3.4, -58.7735738912, 148.7735738912)
                Line((10.8, 11), (0, 11))
                CenterArc((0, 7.6), 3.4, 90, 132.6679254941)
                CenterArc((0, 7.6), 3.4, -137.3320745059, 47.3320745059)
                Line((0, 4.2), (2.5, 4.2))
                Line((2.5, 4.2), (10.8, 4.2))
                CenterArc((10.8, 7.6), 3.4, -90, 31.2264261088)
            make_face()
            with BuildLine():
                Line((0, 6.1), (10.8, 6.1))
                CenterArc((0, 7.6), 1.5, 90, 180)
                Line((10.8, 9.1), (0, 9.1))
                CenterArc((10.8, 7.6), 1.5, -90, 180)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=5.2
        extrude(amount=5.2, mode=Mode.ADD)
    return part.part


def model_142249_ba62bf08_0000():
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
        # Sketch on XZ construction plane
        # Sketch has 21 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 22.9375, perimeter: 21.3994949366
            with BuildLine():
                Line((5.75, 5.75), (0, 0))
                Line((0, 0), (7, 0))
                Line((7, 0), (7, 4.5))
                Line((7, 4.5), (5.75, 5.75))
            make_face()
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)
    return part.part


def model_142493_fc086676_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 15 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 23.5619186799, perimeter: 21.7079457866
            with BuildLine():
                Line((3, -10), (0, -10))
                CenterArc((4, -9.9999956297), 4, -179.9999373995, 179.999874799)
                Line((8, -10), (5, -10))
                CenterArc((4, -9.9999956297), 1, -179.999749598, 179.999499196)
            make_face()
            # Profile area: 68.4291949325, perimeter: 47.1416013943
            with BuildLine():
                CenterArc((4, -9.9999956297), 1, 180, 0.000250402)
                Line((3, -4.9999956297), (3, -9.9999956297))
                CenterArc((4, -4.9999956297), 1, 0, 180)
                Line((5, -9.9999956297), (5, -4.9999956297))
                CenterArc((4, -9.9999956297), 1, -0.000250402, 0.000250402)
                Line((8, -10), (5, -10))
                Line((8, 0), (8, -10))
                Line((0, 0), (8, 0))
                Line((0, -10), (0, 0))
                Line((3, -10), (0, -10))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 18.4752086141, perimeter: 21.8564064606
            with BuildLine():
                Line((-8, 0), (0, 0))
                Line((0, 4.6188021535), (0, 0))
                Line((-8, 0), (0, 4.6188021535))
            make_face()
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.SUBTRACT)
    return part.part


def model_142579_65b06d92_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.5446900494, perimeter: 5.6548667765
            with BuildLine():
                CenterArc((0, 0), 0.9, -90, 115.4487113708)
                CenterArc((0, 0), 0.9, 25.4487113708, 244.5512886292)
            make_face()
            # Profile area: 1.2960811215, perimeter: 6.8701174473
            with BuildLine():
                Line((0, -0.9), (2.5, -0.9))
                Line((2.5, -0.9), (2.5, -0.3))
                Line((2.5, -0.3), (1.9, -0.3))
                CenterArc((1.9, 0.9041666667), 1.2041666667, -154.5512886292, 64.5512886292)
                CenterArc((0, 0), 0.9, -90, 115.4487113708)
            make_face()
        # Symmetric extrude, each_side=1.2
        extrude(amount=1.2, both=True)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1028034292, perimeter: 1.7779030299
            with BuildLine():
                Line((-1.1645808233, -0.25), (-0.8645808233, -0.25))
                CenterArc((0, 0), 0.9, 163.8723797868, 32.2552404263)
                Line((-0.8645808233, 0.25), (-1.1645808233, 0.25))
                Line((-1.1645808233, 0.15), (-1.1645808233, 0.25))
                CenterArc((-1.1645808233, 0), 0.15, -90, 180)
                Line((-1.1645808233, -0.25), (-1.1645808233, -0.15))
            make_face()
            # Profile area: 0.0628318531, perimeter: 1.4566370614
            with BuildLine():
                Line((-1.1645808233, -0.25), (-1.1645808233, -0.15))
                CenterArc((-1.1645808233, 0), 0.15, 90, 180)
                Line((-1.1645808233, 0.15), (-1.1645808233, 0.25))
                CenterArc((-1.1645808233, 0), 0.25, 90, 180)
            make_face()
        # Symmetric extrude, each_side=0.3
        extrude(amount=0.3, both=True, mode=Mode.ADD)
    return part.part


def model_142598_7e2d058b_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch8 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 48.9710952847, perimeter: 28.0938868687
            with BuildLine():
                Line((6.6218525968, -1.4250908375), (-1, -1.4250908375))
                Line((6.6218525968, 5), (6.6218525968, -1.4250908375))
                Line((-1, 5), (6.6218525968, 5))
                Line((-1, -1.4250908375), (-1, 5))
            make_face()
        # OneSide extrude, distance=8
        extrude(amount=8)
    return part.part


def model_142659_3e42350b_0005():
    """Model: battry"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 5.1183024299, perimeter: 9.9091165779
            with BuildLine():
                Line((-1.780860259, -1.7419630768), (-3.2488775298, -1.7419630768))
                Line((-1.780860259, 1.7445779413), (-1.780860259, -1.7419630768))
                Line((-3.2488775298, 1.7445779413), (-1.780860259, 1.7445779413))
                Line((-3.2488775298, -1.7419630768), (-3.2488775298, 1.7445779413))
            make_face()
        # TwoSides extrude (symmetric), distance=0.5
        extrude(amount=0.5, both=True)

        # Sketch4 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.5), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0043315657, perimeter: 0.2802673135
            with BuildLine():
                Line((3.2488775298, -1.6670967625), (3.2028480626, -1.6670967625))
                Line((3.2488775298, -1.572992573), (3.2488775298, -1.6670967625))
                Line((3.2028480626, -1.572992573), (3.2488775298, -1.572992573))
                Line((3.2028480626, -1.6670967625), (3.2028480626, -1.572992573))
            make_face()
        # OneSide extrude, distance=-1.4
        extrude(amount=-1.4, mode=Mode.SUBTRACT)
    return part.part


def model_142680_cd829f9e_0001():
    """Model: Mounting Bar"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 150, perimeter: 70
            with BuildLine():
                Line((2.3443772625, -18.2727043509), (-2.6556227375, -18.2727043509))
                Line((2.3443772625, 11.7272956491), (2.3443772625, -18.2727043509))
                Line((-2.6556227375, 11.7272956491), (2.3443772625, 11.7272956491))
                Line((-2.6556227375, -18.2727043509), (-2.6556227375, 11.7272956491))
            make_face()
        # OneSide extrude, distance=0.85
        extrude(amount=0.85)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.85), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((-0.1556227375, 9.7272956491)):
                Circle(0.4)
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((-0.1556227375, -16.2727043509)):
                Circle(0.4)
        # OneSide extrude, distance=-4.48
        extrude(amount=-4.48, mode=Mode.SUBTRACT)
    return part.part


def model_142816_3c2c9eff_0000():
    """Model: Box"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 450, perimeter: 90
            with BuildLine():
                Line((7.5, -15), (7.5, 15))
                Line((7.5, 15), (-7.5, 15))
                Line((-7.5, 15), (-7.5, -15))
                Line((-7.5, -15), (7.5, -15))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_142852_00b5fde9_0000():
    """Model: Support - Horizontal"""
    with BuildPart() as part:
        # profile -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 32.258, perimeter: 53.34
            with BuildLine():
                Line((-12.7, 0.635), (12.7, 0.635))
                Line((-12.7, -0.635), (-12.7, 0.635))
                Line((12.7, -0.635), (-12.7, -0.635))
                Line((12.7, 0.635), (12.7, -0.635))
            make_face()
        # OneSide extrude, distance=-2.54
        extrude(amount=-2.54)

        # miters cut -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 15 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.635), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 3.2258, perimeter: 8.6721024484
            with BuildLine():
                Line((1.5875, -2.54), (1.5875, 0))
                Line((1.5875, -2.54), (4.1275, -2.54))
                Line((1.5875, 0), (4.1275, -2.54))
            make_face()
            # Profile area: 0.80645, perimeter: 5.715
            with BuildLine():
                Line((-1.27, -2.54), (-1.5875, -2.54))
                Line((-1.27, 0), (-1.27, -2.54))
                Line((-1.5875, 0), (-1.27, 0))
                Line((-1.5875, -2.54), (-1.5875, 0))
            make_face()
            # Profile area: 3.2258, perimeter: 8.6721024484
            with BuildLine():
                Line((-1.5875, -2.54), (-1.5875, 0))
                Line((-1.5875, 0), (-4.1275, -2.54))
                Line((-4.1275, -2.54), (-1.5875, -2.54))
            make_face()
            # Profile area: 0.80645, perimeter: 5.715
            with BuildLine():
                Line((1.5875, 0), (1.27, 0))
                Line((1.27, 0), (1.27, -2.54))
                Line((1.27, -2.54), (1.5875, -2.54))
                Line((1.5875, -2.54), (1.5875, 0))
            make_face()
        # OneSide extrude, distance=-0.635
        extrude(amount=-0.635, mode=Mode.SUBTRACT)
    return part.part


def model_142852_65dcbe39_0001():
    """Model: Frame"""
    with BuildPart() as part:
        # profile -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 96.774, perimeter: 58.42
            with BuildLine():
                Line((-12.7, 1.905), (12.7, 1.905))
                Line((-12.7, -1.905), (-12.7, 1.905))
                Line((12.7, -1.905), (-12.7, -1.905))
                Line((12.7, 1.905), (12.7, -1.905))
            make_face()
        # OneSide extrude, distance=1.905
        extrude(amount=1.905)

        # coping -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(12.7, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0503681315, perimeter: 3.8915393546
            with BuildLine():
                Line((-1.905, 1.905), (-1.905, 1.825625))
                CenterArc((0, -20.9946874925), 22.8996874926, 90.0000497173, 4.7718383451)
                Line((-0.0000198707, 1.905), (-1.905, 1.905))
            make_face()
            # Profile area: 0.0503681315, perimeter: 3.8916188376
            with BuildLine():
                CenterArc((0, -20.9946874925), 22.8996874926, 85.2281119377, 4.7719377796)
                Line((1.905, 1.825625), (1.905, 1.905))
                Line((1.905, 1.905), (-0.0000198707, 1.905))
            make_face()
        # OneSide extrude, distance=-25.4
        extrude(amount=-25.4, mode=Mode.SUBTRACT)
    return part.part


def model_142852_f2535e8d_0001():
    """Model: X-Axis"""
    with BuildPart() as part:
        # profile -> Extrude2 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 6.4516, perimeter: 10.16
            with BuildLine():
                Line((-1.27, 1.27), (1.27, 1.27))
                Line((-1.27, -1.27), (-1.27, 1.27))
                Line((1.27, -1.27), (-1.27, -1.27))
                Line((1.27, 1.27), (1.27, -1.27))
            make_face()
        # Symmetric extrude, each_side=10.16
        extrude(amount=10.16, both=True)

        # notch -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 11 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.27), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 3.2258, perimeter: 7.62
            with BuildLine():
                Line((-1.27, 0), (-1.27, 1.27))
                Line((0, 0), (-1.27, 0))
                Line((1.27, 0), (0, 0))
                Line((1.27, 1.27), (1.27, 0))
                Line((-1.27, 1.27), (1.27, 1.27))
            make_face()
        # OneSide extrude, distance=-2.54
        extrude(amount=-2.54, mode=Mode.SUBTRACT)

        # notch -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 11 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.27), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.6129, perimeter: 5.08
            with BuildLine():
                Line((1.27, -1.27), (1.27, 0))
                Line((1.27, 0), (0, 0))
                Line((0, 0), (0, -1.27))
                Line((0, -1.27), (1.27, -1.27))
            make_face()
        # OneSide extrude, distance=-1.27
        extrude(amount=-1.27, mode=Mode.SUBTRACT)
    return part.part


def model_142918_43d48127_0000():
    """Model: Spur Gear (24 teeth)"""
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
        with BuildSketch(Plane.XY):
            # Profile area: 31.6090766195, perimeter: 24.3154236825
            with BuildLine():
                CenterArc((0, 0), 3.2349198724, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.635, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.3020038479, perimeter: 2.1452134551
            with BuildLine():
                _nurbs_edge([(3.37197784, -0.2715373584), (3.3734947609, -0.2716586925), (3.3765295461, -0.2718633558), (3.3810845536, -0.2720563376), (3.3871633568, -0.2720967844), (3.3947697566, -0.2718506792), (3.4023824404, -0.2713903194), (3.409999677, -0.2707971236), (3.4176199222, -0.2701315774), (3.4252420766, -0.2694169419), (3.4328653679, -0.2686516155), (3.4404892674, -0.2678189855), (3.448113397, -0.2668977912), (3.455737433, -0.2658732605), (3.463361033, -0.2647448447), (3.4709838571, -0.2635205545), (3.4786055742, -0.2622132946), (3.4862258736, -0.260836661), (3.493844476, -0.2594004068), (3.5014611394, -0.2579078783), (3.509075649, -0.256358557), (3.51668781, -0.2547496382), (3.52429744, -0.2530778688), (3.5319043605, -0.2513415625), (3.5395083923, -0.2495415522), (3.5471093587, -0.2476801046), (3.5547070866, -0.245760273), (3.5623014091, -0.2437851317), (3.5698921671, -0.2417569275), (3.57747921, -0.2396767447), (3.5850623941, -0.2375449747), (3.5926415808, -0.2353615999), (3.6002166353, -0.2331265281), (3.6077874252, -0.2308399651), (3.6153538196, -0.2285025504), (3.6229156896, -0.22611516), (3.6304729085, -0.2236787897), (3.6380253525, -0.2211944169), (3.6455729007, -0.2186628465), (3.6531154352, -0.2160846586), (3.6606528408, -0.2134602945), (3.6681850042, -0.2107901089), (3.6757118137, -0.2080744313), (3.6832331589, -0.2053136356), (3.6907489301, -0.202508165), (3.6982590191, -0.199658496), (3.7057633195, -0.1967651171), (3.7132617266, -0.1938285039), (3.7207541385, -0.1908490915), (3.7282404556, -0.1878272643), (3.7357205795, -0.1847633724), (3.7431944124, -0.1816577425), (3.7506618564, -0.1785106902), (3.758122812, -0.1753225344), (3.7655771786, -0.1720936033), (3.7730248564, -0.1688242254), (3.7804657478, -0.1655147242), (3.7878997592, -0.1621654114), (3.7953268034, -0.1587765802), (3.8027467994, -0.155348503), (3.8101596679, -0.1518814395), (3.8175653274, -0.1483756432), (3.8249636901, -0.1448313687), (3.8323546577, -0.14124888), (3.8397381193, -0.1376284543), (3.8471139614, -0.1339703698), (3.8544820759, -0.1302748942), (3.8618423694, -0.1265422747), (3.8691947717, -0.1227727264), (3.8765392434, -0.1189664232), (3.883875767, -0.1151234989), (3.8897386253, -0.112019938), (3.8941321932, -0.1096758554), (3.8970596497, -0.1081058418), (3.8985229808, -0.1073190121)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((0, 0), 3.8999998465, -1.576846918, 3.1536938361)
                _nurbs_edge([(3.37197784, 0.2715373584), (3.3734947609, 0.2716586925), (3.3765295461, 0.2718633558), (3.3810845536, 0.2720563376), (3.3871633568, 0.2720967844), (3.3947697566, 0.2718506792), (3.4023824404, 0.2713903194), (3.409999677, 0.2707971236), (3.4176199222, 0.2701315774), (3.4252420766, 0.2694169419), (3.4328653679, 0.2686516155), (3.4404892674, 0.2678189855), (3.448113397, 0.2668977912), (3.455737433, 0.2658732605), (3.463361033, 0.2647448447), (3.4709838571, 0.2635205545), (3.4786055742, 0.2622132946), (3.4862258736, 0.260836661), (3.493844476, 0.2594004068), (3.5014611394, 0.2579078783), (3.509075649, 0.256358557), (3.51668781, 0.2547496382), (3.52429744, 0.2530778688), (3.5319043605, 0.2513415625), (3.5395083923, 0.2495415522), (3.5471093587, 0.2476801046), (3.5547070866, 0.245760273), (3.5623014091, 0.2437851317), (3.5698921671, 0.2417569275), (3.57747921, 0.2396767447), (3.5850623941, 0.2375449747), (3.5926415808, 0.2353615999), (3.6002166353, 0.2331265281), (3.6077874252, 0.2308399651), (3.6153538196, 0.2285025504), (3.6229156896, 0.22611516), (3.6304729085, 0.2236787897), (3.6380253525, 0.2211944169), (3.6455729007, 0.2186628465), (3.6531154352, 0.2160846586), (3.6606528408, 0.2134602945), (3.6681850042, 0.2107901089), (3.6757118137, 0.2080744313), (3.6832331589, 0.2053136356), (3.6907489301, 0.202508165), (3.6982590191, 0.199658496), (3.7057633195, 0.1967651171), (3.7132617266, 0.1938285039), (3.7207541385, 0.1908490915), (3.7282404556, 0.1878272643), (3.7357205795, 0.1847633724), (3.7431944124, 0.1816577425), (3.7506618564, 0.1785106902), (3.758122812, 0.1753225344), (3.7655771786, 0.1720936033), (3.7730248564, 0.1688242254), (3.7804657478, 0.1655147242), (3.7878997592, 0.1621654114), (3.7953268034, 0.1587765802), (3.8027467994, 0.155348503), (3.8101596679, 0.1518814395), (3.8175653274, 0.1483756432), (3.8249636901, 0.1448313687), (3.8323546577, 0.14124888), (3.8397381193, 0.1376284543), (3.8471139614, 0.1339703698), (3.8544820759, 0.1302748942), (3.8618423694, 0.1265422747), (3.8691947717, 0.1227727264), (3.8765392434, 0.1189664232), (3.883875767, 0.1151234989), (3.8897386253, 0.112019938), (3.8941321932, 0.1096758554), (3.8970596497, 0.1081058418), (3.8985229808, 0.1073190121)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                Line((3.223485098, 0.2596598587), (3.37197784, 0.2715373584))
                Line((3.223485098, -0.2596598587), (3.223485098, 0.2596598587))
                Line((3.223485098, -0.2596598587), (3.37197784, -0.2715373584))
            make_face()
        # OneSide extrude, distance=1.27
        extrude(amount=1.27, mode=Mode.ADD)
    return part.part


def model_142918_43d48127_0001():
    """Model: Spur Gear (12 teeth)"""
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
        with BuildSketch(Plane.XY):
            # Profile area: 5.2017556336, perimeter: 13.0056905748
            with BuildLine():
                CenterArc((0, 0), 1.4349199433, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.635, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.279992132, perimeter: 2.0340692495
            with BuildLine():
                _nurbs_edge([(1.6734993918, -0.2457469393), (1.6747053623, -0.2459233437), (1.6771202898, -0.2462375218), (1.6807516404, -0.2465928984), (1.6856105807, -0.2468465112), (1.6917082483, -0.2468633859), (1.6978240058, -0.2466647896), (1.7039518635, -0.2463338535), (1.7100871084, -0.2459308319), (1.7162273178, -0.2454775123), (1.7223715928, -0.2449707581), (1.7285200036, -0.2443926187), (1.7346729877, -0.2437211141), (1.7408306898, -0.2429422219), (1.7469925873, -0.2420564371), (1.7531577943, -0.2410725906), (1.7593252334, -0.240004128), (1.7654938448, -0.2388647465), (1.7716628165, -0.2376635106), (1.7778316668, -0.2364030993), (1.7840001121, -0.2350824799), (1.7901679863, -0.2336985314), (1.7963351468, -0.2322479357), (1.8025013678, -0.230729335), (1.8086663147, -0.2291438261), (1.8148295967, -0.2274938624), (1.8209907988, -0.2257825772), (1.8271495185, -0.2240130021), (1.8333054089, -0.2221871661), (1.8394581836, -0.2203059843), (1.8456075933, -0.2183697176), (1.8517534114, -0.2163782736), (1.8578954169, -0.2143315446), (1.8640333747, -0.212229801), (1.870167034, -0.2100737221), (1.8762961374, -0.2078642086), (1.8824204264, -0.2056022574), (1.8885396483, -0.2032888231), (1.8946535642, -0.200924656), (1.9007619483, -0.1985102946), (1.9068645844, -0.196046147), (1.9129612621, -0.1935325467), (1.9190517738, -0.1909698138), (1.9251359106, -0.1883583279), (1.9312134625, -0.185698534), (1.93728422, -0.1829909081), (1.943347976, -0.1802359349), (1.9494045276, -0.1774340827), (1.9554536777, -0.174585775), (1.9614952353, -0.1716913871), (1.9675290122, -0.1687512625), (1.9735548219, -0.1657657241), (1.9795724771, -0.1627350862), (1.9855817878, -0.15965967), (1.9915825613, -0.1565398058), (1.997574607, -0.1533758244), (2.0035577385, -0.1501680512), (2.0095317774, -0.1469167996), (2.0154965574, -0.1436223646), (2.0214519232, -0.1402850212), (2.0273977221, -0.1369050333), (2.0333337967, -0.1334826603), (2.0392599785, -0.1300181638), (2.0451760783, -0.1265118171), (2.051081886, -0.1229639072), (2.056977188, -0.1193747212), (2.0628617822, -0.1157445362), (2.068735493, -0.1120736082), (2.0745981879, -0.1083621609), (2.0804497897, -0.1046103771), (2.0862902604, -0.1008183985), (2.0909537238, -0.0977527407), (2.0944463095, -0.0954354823), (2.0967724732, -0.0938826394), (2.0979349984, -0.0931042169)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((0, 0), 2.0999999173, -2.5410609694, 5.0821219387)
                _nurbs_edge([(1.6734993918, 0.2457469393), (1.6747053623, 0.2459233437), (1.6771202898, 0.2462375218), (1.6807516404, 0.2465928984), (1.6856105807, 0.2468465112), (1.6917082483, 0.2468633859), (1.6978240058, 0.2466647896), (1.7039518635, 0.2463338535), (1.7100871084, 0.2459308319), (1.7162273178, 0.2454775123), (1.7223715928, 0.2449707581), (1.7285200036, 0.2443926187), (1.7346729877, 0.2437211141), (1.7408306898, 0.2429422219), (1.7469925873, 0.2420564371), (1.7531577943, 0.2410725906), (1.7593252334, 0.240004128), (1.7654938448, 0.2388647465), (1.7716628165, 0.2376635106), (1.7778316668, 0.2364030993), (1.7840001121, 0.2350824799), (1.7901679863, 0.2336985314), (1.7963351468, 0.2322479357), (1.8025013678, 0.230729335), (1.8086663147, 0.2291438261), (1.8148295967, 0.2274938624), (1.8209907988, 0.2257825772), (1.8271495185, 0.2240130021), (1.8333054089, 0.2221871661), (1.8394581836, 0.2203059843), (1.8456075933, 0.2183697176), (1.8517534114, 0.2163782736), (1.8578954169, 0.2143315446), (1.8640333747, 0.212229801), (1.870167034, 0.2100737221), (1.8762961374, 0.2078642086), (1.8824204264, 0.2056022574), (1.8885396483, 0.2032888231), (1.8946535642, 0.200924656), (1.9007619483, 0.1985102946), (1.9068645844, 0.196046147), (1.9129612621, 0.1935325467), (1.9190517738, 0.1909698138), (1.9251359106, 0.1883583279), (1.9312134625, 0.185698534), (1.93728422, 0.1829909081), (1.943347976, 0.1802359349), (1.9494045276, 0.1774340827), (1.9554536777, 0.174585775), (1.9614952353, 0.1716913871), (1.9675290122, 0.1687512625), (1.9735548219, 0.1657657241), (1.9795724771, 0.1627350862), (1.9855817878, 0.15965967), (1.9915825613, 0.1565398058), (1.997574607, 0.1533758244), (2.0035577385, 0.1501680512), (2.0095317774, 0.1469167996), (2.0154965574, 0.1436223646), (2.0214519232, 0.1402850212), (2.0273977221, 0.1369050333), (2.0333337967, 0.1334826603), (2.0392599785, 0.1300181638), (2.0451760783, 0.1265118171), (2.051081886, 0.1229639072), (2.056977188, 0.1193747212), (2.0628617822, 0.1157445362), (2.068735493, 0.1120736082), (2.0745981879, 0.1083621609), (2.0804497897, 0.1046103771), (2.0862902604, 0.1008183985), (2.0909537238, 0.0977527407), (2.0944463095, 0.0954354823), (2.0967724732, 0.0938826394), (2.0979349984, 0.0931042169)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                Line((1.4187051965, 0.2084766812), (1.6734993918, 0.2457469393))
                Line((1.4187051965, -0.2084766812), (1.4187051965, 0.2084766812))
                Line((1.4187051965, -0.2084766812), (1.6734993918, -0.2457469393))
            make_face()
        # OneSide extrude, distance=1.27
        extrude(amount=1.27, mode=Mode.ADD)
    return part.part


def model_142959_e000cbf1_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 22 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 66.9109513775, perimeter: 55.7123889804
            with BuildLine():
                Line((5, -17.5), (2, -17.5))
                Line((5, 5), (5, -17.5))
                Line((2, 5), (5, 5))
                Line((2, -17.5), (2, 5))
            make_face()
            with BuildLine():
                CenterArc((3.5, -17), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.5, -16.5), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.5, -16.5), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 22 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 21.8168140899, perimeter: 28.9646003294
            with BuildLine():
                Line((2, 5), (5, 5))
                CenterArc((5, 6), 1, -90, 90)
                Line((6, 6), (6, 9))
                CenterArc((5, 9), 1, 0, 90)
                Line((5, 10), (3, 10))
                Line((3, 10), (2, 10))
                CenterArc((2, 9), 1, 90, 90)
                Line((1, 9), (1, 6))
                CenterArc((2, 6), 1, 180, 90)
            make_face()
            with BuildLine():
                CenterArc((2, 9), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2, 6), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5, 9), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5, 6), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.5, 7.5), 0.7, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XY construction plane
        # Sketch has 22 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.2598354972, perimeter: 12.6362989978
            with BuildLine():
                CenterArc((3.625, -17.5), 1.625, 180, 67.380135052)
                CenterArc((3.5580357143, -17.6607142857), 1.4508928571, -112.619864948, 118.9795251878)
                Line((5, -17.5), (2, -17.5))
            make_face()
            with BuildLine():
                CenterArc((3.5, -18.4013878189), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.5, -18), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.5, -18), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


def model_142992_3bd10abe_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 269.3770140882, perimeter: 61.5696214707
            with BuildLine():
                Line((-6, 10.75), (-6, 3.75))
                Line((-6, 3.75), (0, 0))
                Line((0, 0), (12, 0))
                Line((12, 0), (15.0175191846, 4.25))
                Line((15.0072666309, 10.2499912404), (15.0175191846, 4.25))
                Line((15.0072666309, 10.2499912404), (12, 14.5))
                Line((0, 14.5), (12, 14.5))
                Line((0, 14.5), (-6, 10.75))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # HOLES FOR BASEPLATE JGL -> Extrude4 (Cut)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.7550146509, perimeter: 25.5046699043
            with BuildLine():
                CenterArc((6.7208063763, 13.6753673869), 0.15, 0, 180)
                Line((6.5708063763, 13.6753673869), (6.5708063763, 1.3942713327))
                CenterArc((6.7208063763, 1.3942713327), 0.15, 180, 180)
                Line((6.8708063763, 1.3942713327), (6.8708063763, 13.6753673869))
            make_face()
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((3, 9.5999999791)):
                Circle(0.15)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((3, 5.3999999791)):
                Circle(0.15)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((3, 1.1999999791)):
                Circle(0.15)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((0.2, 5.3999999791)):
                Circle(0.15)
            # Profile area: 0.0791730436, perimeter: 0.9974556675
            with Locations((-0.754, 5.4226635258)):
                Circle(0.15875)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((0.2, 9.5999999791)):
                Circle(0.15)
            # Profile area: 0.0791730436, perimeter: 0.9974556675
            with Locations((-1.262, 10.6296635258)):
                Circle(0.15875)
            # Profile area: 0.0791730436, perimeter: 0.9974556675
            with Locations((-4.056, 10.6296635258)):
                Circle(0.15875)
            # Profile area: 0.0791730436, perimeter: 0.9974556675
            with Locations((-5.58, 5.5496635258)):
                Circle(0.15875)
        # OneSide extrude, distance=5
        extrude(amount=5, mode=Mode.SUBTRACT)
    return part.part


def model_143054_09a08890_0002():
    """Model: carcasa"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 31 constraints, 22 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 9.4455696102, perimeter: 15.0200637941
            with BuildLine():
                CenterArc((5, 0.35), 2.6, 127.9580285807, 69.6720196815)
                Line((0, 2.4), (3.4007814408, 2.4))
                Line((0, 2.4), (0, -2.35))
                Line((0.7154956985, -2.35), (0, -2.35))
                CenterArc((2.43, -2.16), 1.725, 86.9388862016, 99.3847838695)
            make_face()
            # Profile area: 20.0702760012, perimeter: 16.4797265667
            with BuildLine():
                CenterArc((5, 0.35), 2.6, 127.9580285807, 69.6720196815)
                CenterArc((2.43, -2.16), 1.725, 1.7077331179, 85.2311530837)
                CenterArc((5, 0.35), 2.6, -108.9834289427, 111.9306562741)
                CenterArc((5, 0.35), 2.6, 2.9472273313, 55.5612900601)
                CenterArc((5, 0.35), 2.6, 58.5085173914, 65.7025810354)
                CenterArc((5, 0.35), 2.6, 124.2110984268, 3.7469301539)
            make_face()
            # Profile area: 8.1813113028, perimeter: 10.6950498868
            with BuildLine():
                CenterArc((2.43, -2.16), 1.725, -173.6763299289, 138.6942766625)
                CenterArc((2.43, -2.16), 1.725, -34.9820532664, 36.6897863842)
                CenterArc((5, 0.35), 2.6, -162.3699517378, 53.3865227951)
                CenterArc((2.43, -2.16), 1.725, 86.9388862016, 99.3847838695)
            make_face()
            # Profile area: 2.6547797479, perimeter: 7.7232954049
            with BuildLine():
                CenterArc((2.4087736941, 1.9327991606), 4, 9.1237178344, 15.6820836794)
                CenterArc((5.8581667019, 3.5270663522), 0.2, 24.8058015138, 37.6552469539)
                CenterArc((4.8409933463, 1.5763335758), 2.4, 62.4610484677, 52.5519330593)
                CenterArc((3.9107814408, 3.57), 0.2, 115.012981527, 47.6253325911)
                CenterArc((7.5376537675, 2.4360700525), 4, 162.6383141182, 16.4441074936)
                CenterArc((5, 0.35), 2.6, 58.5085173914, 65.7025810354)
            make_face()
            # Profile area: 1.1668903371, perimeter: 4.9886518827
            with BuildLine():
                CenterArc((5, 0.35), 2.6, -162.3699517378, 53.3865227951)
                CenterArc((2.43, -2.16), 1.725, 1.7077331179, 85.2311530837)
            make_face()
        # OneSide extrude, distance=-2.2
        extrude(amount=-2.2)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 31 constraints, 22 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 20.0702760012, perimeter: 16.4797265667
            with BuildLine():
                CenterArc((5, 0.35), 2.6, 127.9580285807, 69.6720196815)
                CenterArc((2.43, -2.16), 1.725, 1.7077331179, 85.2311530837)
                CenterArc((5, 0.35), 2.6, -108.9834289427, 111.9306562741)
                CenterArc((5, 0.35), 2.6, 2.9472273313, 55.5612900601)
                CenterArc((5, 0.35), 2.6, 58.5085173914, 65.7025810354)
                CenterArc((5, 0.35), 2.6, 124.2110984268, 3.7469301539)
            make_face()
            # Profile area: 8.1813113028, perimeter: 10.6950498868
            with BuildLine():
                CenterArc((2.43, -2.16), 1.725, -173.6763299289, 138.6942766625)
                CenterArc((2.43, -2.16), 1.725, -34.9820532664, 36.6897863842)
                CenterArc((5, 0.35), 2.6, -162.3699517378, 53.3865227951)
                CenterArc((2.43, -2.16), 1.725, 86.9388862016, 99.3847838695)
            make_face()
            # Profile area: 1.1668903371, perimeter: 4.9886518827
            with BuildLine():
                CenterArc((5, 0.35), 2.6, -162.3699517378, 53.3865227951)
                CenterArc((2.43, -2.16), 1.725, 1.7077331179, 85.2311530837)
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


def model_143158_794f6243_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 25 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 97.2872228954, perimeter: 65.6567386202
            with BuildLine():
                CenterArc((0, 0), 6.6, 117.8717395023, 124.2565209954)
                CenterArc((0, 0), 6.6, -117.8717395023, 55.6440591043)
                CenterArc((0, 0), 6.6, -62.227680398, 124.455360796)
                CenterArc((0, 0), 6.6, 62.227680398, 55.6440591043)
            make_face()
            with BuildLine():
                Line((-3.4641016151, -0.5), (-4.5641016151, -0.5))
                Line((-4.5641016151, -0.5), (-4.5641016151, 0.5))
                Line((-4.5641016151, 0.5), (-3.4641016151, 0.5))
                CenterArc((0, 0), 3.5, -171.7867892983, 343.5735785965)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=4.2
        extrude(amount=4.2)

        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 25 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 28.2303107617, perimeter: 42.0736338985
            with BuildLine():
                CenterArc((-9.45, 0), 2.2, 125.1685937593, 109.6628124814)
                Line((-10.7171654994, -1.7984136335), (-10.223148875, -2.0596700748))
                Line((-10.223148875, -2.0596700748), (-3.0854594095, -5.8343757363))
                CenterArc((0, 0), 6.6, 117.8717395023, 124.2565209954)
                Line((-10.223148875, 2.0596700748), (-3.0854594095, 5.8343757363))
                Line((-10.7171654994, 1.7984136335), (-10.223148875, 2.0596700748))
            make_face()
            with BuildLine():
                CenterArc((-9.45, 0), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 28.3577038586, perimeter: 42.1208721572
            with BuildLine():
                CenterArc((0, 0), 6.6, -62.227680398, 124.455360796)
                Line((10.3667498557, -1.9998924226), (3.0753309339, -5.8397208535))
                Line((10.5803816937, -1.8873889971), (10.3667498557, -1.9998924226))
                CenterArc((9.45, 0), 2.2, -59.0820624434, 118.1641248868)
                Line((10.5803816937, 1.8873889971), (10.3667498557, 1.9998924226))
                Line((10.3667498557, 1.9998924226), (3.0753309339, 5.8397208535))
            make_face()
            with BuildLine():
                CenterArc((9.45, 0), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-2
        extrude(amount=-2)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 25 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 97.2872228954, perimeter: 65.6567386202
            with BuildLine():
                CenterArc((0, 0), 6.6, 117.8717395023, 124.2565209954)
                CenterArc((0, 0), 6.6, -117.8717395023, 55.6440591043)
                CenterArc((0, 0), 6.6, -62.227680398, 124.455360796)
                CenterArc((0, 0), 6.6, 62.227680398, 55.6440591043)
            make_face()
            with BuildLine():
                Line((-3.4641016151, -0.5), (-4.5641016151, -0.5))
                Line((-4.5641016151, -0.5), (-4.5641016151, 0.5))
                Line((-4.5641016151, 0.5), (-3.4641016151, 0.5))
                CenterArc((0, 0), 3.5, -171.7867892983, 343.5735785965)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-5.2
        extrude(amount=-5.2, mode=Mode.ADD)
    return part.part


def model_143293_fc5b0ff7_0020():
    """Model: suspension_bracket v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 40 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 53.4758459924, perimeter: 40.8266454371
            with BuildLine():
                Line((-2.0549472711, -0.5715456449), (-2.8344316065, -4.5880620673))
                CenterArc((-2, -4.75), 0.85, 169.017146925, 100.982853075)
                Line((-2, -5.6), (2, -5.6))
                CenterArc((2, -4.75), 0.85, -90, 100.982853075)
                Line((2.8344316065, -4.5880620673), (2.0549472711, -0.5715456449))
                CenterArc((5, 0), 3, 169.017146925, 21.96570615)
                Line((2.0549472711, 0.5715456449), (2.8344316065, 4.5880620673))
                CenterArc((2, 4.75), 0.85, -10.982853075, 100.982853075)
                Line((2, 5.6), (-2, 5.6))
                CenterArc((-2, 4.75), 0.85, 90, 100.982853075)
                Line((-2.8344316065, 4.5880620673), (-2.0549472711, 0.5715456449))
                CenterArc((-5, 0), 3, -10.982853075, 21.96570615)
            make_face()
            with BuildLine():
                CenterArc((-2, 4.75), 0.325, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2, 4.75), 0.325, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2, -4.75), 0.325, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-2, -4.75), 0.325, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


def model_143309_c7a044ee_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4.4463581291, perimeter: 46.6809252397
            with BuildLine():
                CenterArc((0, 0), 3.81, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3.6195, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=1.524
        extrude(amount=1.524, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.7989637627, perimeter: 11.9670551981
            with BuildLine():
                CenterArc((0, 0), 3.81, 49.1007650111, 81.7989210786)
                Line((2.7024010531, 3.1198212766), (2.494524049, 2.8798350246))
                CenterArc((0, 0), 4.1275, 49.1007650111, 81.7989210786)
                Line((-2.4945467225, 2.8798153846), (-2.702425616, 3.1198))
            make_face()
        # Symmetric extrude, each_side=2.032
        extrude(amount=2.032, both=True, mode=Mode.ADD)
    return part.part


def model_143481_e8d7fe93_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 13 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.6439024077, perimeter: 4.7090838176
            with BuildLine():
                CenterArc((-0.3476260982, 0.1998927108), 0.1, -29.8998561411, 67.5914660001)
                Line((-0.2684947908, 0.2610338279), (-0.3373922154, 0.3502036622))
                CenterArc((-0.4165235227, 0.2890625452), 0.1, 37.691609859, 107.5481858873)
                CenterArc((0, 0), 0.607, 145.2397957464, 247.4577366442)
                CenterArc((0.4266577624, 0.2738834675), 0.1, 32.6975323906, 106.1837647686)
                Line((0.2779109123, 0.255547294), (0.3513228857, 0.3396455868))
                CenterArc((0.353245789, 0.1897851747), 0.1, 138.8812971592, 69.3661057161)
                CenterArc((0, 0), 0.301, 150.1001438589, 238.1472590163)
            make_face()
        # OneSide extrude, distance=0.13
        extrude(amount=0.13)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0941412153, perimeter: 1.50304467
            with BuildLine():
                CenterArc((0, 0), 0.607, 61.4747793312, 54.3023999786)
                Line((0.2898701519, 0.5333144429), (0.2898701519, 0.7155808685))
                CenterArc((0, 0), 0.7720626168, 67.9479323507, 42.0446934823)
                Line((-0.2639675901, 0.5465986749), (-0.2639675901, 0.7255355234))
            make_face()
        # OneSide extrude, distance=-0.32
        extrude(amount=-0.32, mode=Mode.ADD)
    return part.part


def model_143509_1dd5212d_0008():
    """Model: Component50"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.6724954448, perimeter: 10.5957637237
            with BuildLine():
                Line((0.2842242087, -4.1108671082), (0.817004049, -4.8672820214))
                CenterArc((2.4031600232, -6.9183911616), 2.5928631818, 52.297398624, 75.4179642646)
                Line((3.9888591136, -4.8669287871), (4.5188308708, -4.1108671082))
                CenterArc((5.4019515338, -3.2421716796), 1.2387630334, -177.2368125024, 41.765024186)
                Line((0.6355692615, -3.3018900019), (4.1646287889, -3.3018900019))
                CenterArc((-0.5882672473, -3.2511527805), 1.2248877769, -44.5773814779, 42.2034002456)
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 14 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-3.9263005795, 4.2593012194)):
                Circle(0.15)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-2.9000990252, 3.801890002)):
                Circle(0.15)
            # Profile area: 0.0176714587, perimeter: 0.535619449
            with BuildLine():
                CenterArc((-1.9000990252, 3.801890002), 0.15, 180, 90)
                Line((-1.9000990252, 3.651890002), (-1.9000990252, 3.801890002))
                Line((-1.9000990252, 3.801890002), (-2.0500990252, 3.801890002))
            make_face()
            # Profile area: 0.053014376, perimeter: 1.0068583471
            with BuildLine():
                Line((-1.9000990252, 3.801890002), (-2.0500990252, 3.801890002))
                Line((-1.9000990252, 3.651890002), (-1.9000990252, 3.801890002))
                CenterArc((-1.9000990252, 3.801890002), 0.15, -90, 270)
            make_face()
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-0.8776373983, 4.2587361591)):
                Circle(0.15)
        # OneSide extrude, distance=-4
        extrude(amount=-4, mode=Mode.SUBTRACT)
    return part.part


def model_143815_c616f1b4_0003():
    """Model: guide pin v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1590431281, perimeter: 1.4137166941
            Circle(0.225)
        # OneSide extrude, distance=0.15
        extrude(amount=0.15)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            Circle(0.1)
        # OneSide extrude, distance=2.15
        extrude(amount=2.15, mode=Mode.ADD)
    return part.part


def model_143815_c616f1b4_0005():
    """Model: single bend v1 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 16 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.312577449, perimeter: 3.4995574247
            with BuildLine():
                Line((0, -0.9000000134), (0, -0.4500000067))
                Line((0.200000003, -0.9000000134), (0, -0.9000000134))
                Line((0.200000003, -1.1), (0.200000003, -0.9000000134))
                Line((0.7, -1.1), (0.200000003, -1.1))
                Line((0.7, -0.9), (0.7, -1.1))
                Line((0.9, -0.9), (0.7, -0.9))
                Line((0.9, -0.45), (0.9, -0.9))
                Line((0.9, -0.45), (0.8, -0.4500000007))
                CenterArc((0.45, -0.4500000034), 0.35, -90, 90.0000004269)
                CenterArc((0.45, -0.4500000034), 0.35, -180, 90)
                Line((0.1, -0.4500000034), (0, -0.4500000067))
            make_face()
            # Profile area: 0.1062887268, perimeter: 1.6497787244
            with BuildLine():
                Line((0, 0), (0, -0.400000006))
                Line((0, -0.400000006), (0, -0.4500000067))
                Line((0.1, -0.4500000034), (0, -0.4500000067))
                CenterArc((0.45, -0.4500000034), 0.35, 90, 90)
                Line((0.45, -0.1000000034), (0.45, 0))
                Line((0, 0), (0.45, 0))
            make_face()
            # Profile area: 0.1062887262, perimeter: 1.6497787151
            with BuildLine():
                CenterArc((0.45, -0.4500000034), 0.35, 0.0000004269, 89.9999995731)
                Line((0.9, -0.45), (0.8, -0.4500000007))
                Line((0.9, 0), (0.9, -0.45))
                Line((0.45, 0), (0.9, 0))
                Line((0.45, -0.1000000034), (0.45, 0))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0999999994, perimeter: 1.399999994
            with BuildLine():
                Line((0.7, 0.9), (0.200000003, 0.9))
                Line((0.7, 1.1), (0.7, 0.9))
                Line((0.200000003, 1.1), (0.7, 1.1))
                Line((0.200000003, 0.9), (0.200000003, 1.1))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


def model_143967_d7e408c9_0000():
    """Model: Component6"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 15.9043128088, perimeter: 14.1371669412
            with Locations((7.5, -12.5)):
                Circle(2.25)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            with Locations((7.5, 12.5)):
                Circle(1.5)
        # OneSide extrude, distance=10.2
        extrude(amount=10.2, mode=Mode.ADD)
    return part.part


def model_144259_1a9370ba_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 900, perimeter: 120
            with BuildLine():
                Line((30, -30), (0, -30))
                Line((30, 0), (30, -30))
                Line((0, 0), (30, 0))
                Line((0, -30), (0, 0))
            make_face()
        # OneSide extrude, distance=90
        extrude(amount=90)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 90, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 283.5287369865, perimeter: 59.6902604182
            with Locations((-20.046321607, 16.8937634886)):
                Circle(9.5)
        # OneSide extrude, distance=30.5
        extrude(amount=30.5, mode=Mode.ADD)
    return part.part


def model_144276_ff01151b_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 14 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 15.7079632679, perimeter: 31.4159265359
            with BuildLine():
                CenterArc((8, -10.5), 3, -105.4660099534, 30.9320199068)
                CenterArc((8, -10.5), 3, -74.5339900466, 149.0675886373)
                CenterArc((8, -10.5), 3, 74.5335985907, 30.9324113627)
                CenterArc((8, -10.5), 3, 105.4660099534, 149.0679800932)
            make_face()
            with BuildLine():
                CenterArc((8, -10.5), 2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3.5
        extrude(amount=3.5)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 14 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.99754167, perimeter: 25.2464187306
            with BuildLine():
                CenterArc((8, -10.5), 3, -74.5339900466, 149.0675886373)
                Line((8.8, -13.391366459), (12.98, -12.2348198754))
                CenterArc((12.5, -10.5), 1.8, -74.5339900466, 149.0679800932)
                Line((8.8000197544, -7.6086390068), (12.98, -8.7651801246))
            make_face()
            with BuildLine():
                CenterArc((12.5, -10.5), 0.65, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 14 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.99754167, perimeter: 25.2464597238
            with BuildLine():
                CenterArc((3.5, -10.5), 1.8, 105.4660099534, 149.0679800932)
                Line((3.02, -12.2348198754), (7.2, -13.391366459))
                CenterArc((8, -10.5), 3, 105.4660099534, 149.0679800932)
                Line((3.02, -8.7651801246), (7.2, -7.608633541))
            make_face()
            with BuildLine():
                CenterArc((3.5, -10.5), 0.65, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)
    return part.part


def model_144333_c6cc0474_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrusion1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 59.212, perimeter: 32.26
            with BuildLine():
                Line((5.24, -2.825), (5.24, 2.825))
                Line((5.24, 2.825), (-5.24, 2.825))
                Line((-5.24, 2.825), (-5.24, -2.825))
                Line((-5.24, -2.825), (5.24, -2.825))
            make_face()
        # OneSide extrude, distance=1.3
        extrude(amount=1.3)

        # Sketch2 -> Extrusion2 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.3), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 53.998, perimeter: 30.94
            with BuildLine():
                Line((5.075, -2.66), (-5.075, -2.66))
                Line((5.075, 2.66), (5.075, -2.66))
                Line((-5.075, 2.66), (5.075, 2.66))
                Line((-5.075, -2.66), (-5.075, 2.66))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


def model_144531_0c361490_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 12 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 1.3357580556, perimeter: 6.9734101012
            with BuildLine():
                CenterArc((0, 0), 0.9, -29.6846931386, 119.6846931386)
                CenterArc((2.0850332346, -1.1885438193), 1.5, 99.1516217636, 51.1636850978)
                CenterArc((1.941890365, -0.3), 0.6, 90, 9.1516217636)
                Line((2.5, 0.3), (1.941890365, 0.3))
                Line((2.5, 0.9), (2.5, 0.3))
                Line((0, 0.9), (2.5, 0.9))
            make_face()
            # Profile area: 2.5446900494, perimeter: 5.6548667765
            with BuildLine():
                CenterArc((0, 0), 0.9, 90, 240.3153068614)
                CenterArc((0, 0), 0.9, -29.6846931386, 119.6846931386)
            make_face()
        # Symmetric extrude, each_side=1
        extrude(amount=1, both=True)

        # Sketch4 -> Extrude3 (Join)
        # Sketch on YZ construction plane
        # Sketch has 8 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.0628318531, perimeter: 1.4566370614
            with BuildLine():
                CenterArc((-1.1645808233, 0), 0.25, 90, 180)
                Line((-1.1645808233, -0.15), (-1.1645808233, -0.25))
                CenterArc((-1.1645808233, 0), 0.15, 90, 180)
                Line((-1.1645808233, 0.25), (-1.1645808233, 0.15))
            make_face()
            # Profile area: 0.1028034292, perimeter: 1.7779030299
            with BuildLine():
                Line((-1.1645808233, 0.25), (-1.1645808233, 0.15))
                CenterArc((-1.1645808233, 0), 0.15, -90, 180)
                Line((-1.1645808233, -0.15), (-1.1645808233, -0.25))
                Line((-0.8645808233, -0.25), (-1.1645808233, -0.25))
                CenterArc((0, 0), 0.9, 163.8723797868, 32.2552404263)
                Line((-1.1645808233, 0.25), (-0.8645808233, 0.25))
            make_face()
        # Symmetric extrude, full_length=True, total=-0.3
        extrude(amount=-0.15, both=True, mode=Mode.ADD)
    return part.part


def model_144588_fec64eef_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 18, perimeter: 18
            with BuildLine():
                Line((0, 3), (0, 0))
                Line((0, 0), (6, 0))
                Line((6, 0), (6, 3))
                Line((6, 3), (0, 3))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, -1, 0), z_dir=(-1, 0, 0))):
            # Profile area: 2.25, perimeter: 7.8541019662
            with BuildLine():
                Line((-3, 1.5), (0, 0))
                Line((-3, 1.5), (-3, 0))
                Line((-3, 0), (0, 0))
            make_face()
        # OneSide extrude, distance=-6.5
        extrude(amount=-6.5, mode=Mode.SUBTRACT)
    return part.part


def model_144781_a0ee9ef1_0000():
    """Model: Volume Btn (Positive) v1"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 21 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.4567333059, perimeter: 2.9967503476
            with BuildLine():
                CenterArc((-0.4572, -0.0127), 0.1778, 180, 90)
                Line((0.4572, -0.1905), (-0.4572, -0.1905))
                CenterArc((0.4572, -0.0127), 0.1778, -90, 90)
                Line((0.635, 0.0127), (0.635, -0.0127))
                CenterArc((0.4572, 0.0127), 0.1778, 0, 90)
                Line((-0.4572, 0.1905), (0.4572, 0.1905))
                CenterArc((-0.4572, 0.0127), 0.1778, 90, 90)
                Line((-0.635, -0.0127), (-0.635, 0.0127))
            make_face()
        # OneSide extrude, distance=0.254
        extrude(amount=0.254)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 14 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.254), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.00096774, perimeter: 0.1270000003
            with BuildLine():
                Line((-0.0126999998, -0.0127), (-0.0126999998, 0.0127))
                Line((-0.0508, 0.0127), (-0.0126999998, 0.0127))
                Line((-0.0508, -0.0127), (-0.0508, 0.0127))
                Line((-0.0126999998, -0.0127), (-0.0508, -0.0127))
            make_face()
            # Profile area: 0.00096774, perimeter: 0.1269999982
            with BuildLine():
                Line((-0.0126999998, 0.0127), (0.0126999998, 0.0127))
                Line((0.0126999998, 0.0507999994), (0.0126999998, 0.0127))
                Line((-0.0126999998, 0.0507999994), (0.0126999998, 0.0507999994))
                Line((-0.0126999998, 0.0127), (-0.0126999998, 0.0507999994))
            make_face()
            # Profile area: 0.00064516, perimeter: 0.1015999994
            with BuildLine():
                Line((0.0126999998, 0.0127), (0.0126999998, -0.0127))
                Line((-0.0126999998, 0.0127), (0.0126999998, 0.0127))
                Line((-0.0126999998, -0.0127), (-0.0126999998, 0.0127))
                Line((0.0126999998, -0.0127), (-0.0126999998, -0.0127))
            make_face()
            # Profile area: 0.00096774, perimeter: 0.1270000003
            with BuildLine():
                Line((0.0508, -0.0127), (0.0126999998, -0.0127))
                Line((0.0508, 0.0127), (0.0508, -0.0127))
                Line((0.0126999998, 0.0127), (0.0508, 0.0127))
                Line((0.0126999998, 0.0127), (0.0126999998, -0.0127))
            make_face()
            # Profile area: 0.00096774, perimeter: 0.1269999982
            with BuildLine():
                Line((0.0126999998, -0.0127), (0.0126999998, -0.0507999994))
                Line((0.0126999998, -0.0127), (-0.0126999998, -0.0127))
                Line((-0.0126999998, -0.0507999994), (-0.0126999998, -0.0127))
                Line((0.0126999998, -0.0507999994), (-0.0126999998, -0.0507999994))
            make_face()
        # OneSide extrude, distance=-0.00762
        extrude(amount=-0.00762, mode=Mode.SUBTRACT)
    return part.part


def model_144781_a0ee9ef1_0002():
    """Model: Volume Btn (Negative) v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 21 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.4567333059, perimeter: 2.9967503476
            with BuildLine():
                CenterArc((0.0127, -0.4572), 0.1778, -90, 90)
                Line((0.1905, -0.4572), (0.1905, 0.4572))
                CenterArc((0.0127, 0.4572), 0.1778, 0, 90)
                Line((0.0127, 0.635), (-0.0127, 0.635))
                CenterArc((-0.0127, 0.4572), 0.1778, 90, 90)
                Line((-0.1905, 0.4572), (-0.1905, -0.4572))
                CenterArc((-0.0127, -0.4572), 0.1778, 180, 90)
                Line((-0.0127, -0.635), (0.0127, -0.635))
            make_face()
        # OneSide extrude, distance=0.381
        extrude(amount=0.381)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.381, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0048387, perimeter: 0.3302
            with BuildLine():
                Line((-0.01905, 0.0635), (-0.01905, -0.0635))
                Line((-0.01905, -0.0635), (0.01905, -0.0635))
                Line((0.01905, -0.0635), (0.01905, 0.0635))
                Line((0.01905, 0.0635), (-0.01905, 0.0635))
            make_face()
        # OneSide extrude, distance=-0.00762
        extrude(amount=-0.00762, mode=Mode.SUBTRACT)
    return part.part


def model_145040_e65b11d2_0000():
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
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 11.5512808301, perimeter: 38.4701050098
            with BuildLine():
                _nurbs_edge([(-5, 9), (-5.0832187223, 9.1015160702), (-5.2560809316, 9.2919774356), (-5.5346449836, 9.539957599), (-5.94491662, 9.7946220038), (-6.5184776389, 9.9825975356), (-7.1381487896, 10.034757549), (-7.7709353668, 9.9449152259), (-8.3618996485, 9.7072133734), (-8.8484118001, 9.3168997717), (-9.1702437153, 8.7713217127), (-9.2841785734, 8.0720041044), (-9.1680336055, 7.2247312166), (-8.8126807473, 6.2370786061), (-8.2182064817, 5.1171260196), (-7.3895226838, 3.8722120506), (-6.544501487, 2.7809514327), (-5.8108234872, 1.9105387245), (-5.2776217463, 1.307334459), (-5, 1)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9333333333, 1, 1, 1, 1, 1, 1], 5)
                Line((-5, 9), (-5, 1))
            make_face()
            with BuildLine():
                Line((-5.6000000238, 8.7728784083), (-5.6000000238, 2.6018570982))
                _nurbs_edge([(-5.6000000238, 8.7728784083), (-5.8170745267, 8.9983762973), (-6.0512401919, 9.1564997708), (-6.3105801786, 9.2601812716), (-6.5552378774, 9.3579929424), (-6.8266297693, 9.4067743753), (-7.1080229144, 9.3999525579), (-7.4200760651, 9.3923874496), (-7.7400242508, 9.3127320605), (-7.9913603889, 9.1748012416), (-8.173655733, 9.0747593365), (-8.3178458466, 8.9485566203), (-8.421968998, 8.7958879892), (-8.5321774686, 8.6342968722), (-8.6048012707, 8.4384860558), (-8.6227740488, 8.1671565731), (-8.6425510027, 7.8685900055), (-8.5880965261, 7.478183141), (-8.4268485563, 7.0052315483), (-8.1971365022, 6.33147), (-7.7527577582, 5.4977058664), (-7.0950221748, 4.5457075731), (-6.6794845094, 3.9442635303), (-6.1801386414, 3.2949453293), (-5.6000000238, 2.6018570982)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.0260870385, 0.0260870385, 0.0260870385, 0.0260870385, 0.1488515303, 0.1488515303, 0.1488515303, 0.2646658266, 0.2646658266, 0.2646658266, 0.3930990052, 0.3930990052, 0.3930990052, 0.4862522248, 0.4862522248, 0.4862522248, 0.5848496427, 0.5848496427, 0.5848496427, 0.6933446442, 0.6933446442, 0.6933446442, 0.8479054097, 0.8479054097, 0.8479054097, 0.9455522777, 0.9455522777, 0.9455522777, 0.9455522777], 3)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides extrude (symmetric), distance=0.5
        extrude(amount=0.5, both=True)
    return part.part


def model_145119_24107428_0000():
    """Model: Spur Gear (21 teeth)"""
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
        with BuildSketch(Plane.XY):
            # Profile area: 38.8320663068, perimeter: 30.88135313
            with BuildLine():
                CenterArc((0, 0), 3.71492, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.5282732505, perimeter: 2.8261980862
            with BuildLine():
                _nurbs_edge([(3.9308403746, -0.3535617878), (3.9327633334, -0.3537340065), (3.9366108028, -0.3540279926), (3.942386662, -0.35431762), (3.950096748, -0.3544160253), (3.9597470496, -0.3541460298), (3.9694071308, -0.3535930288), (3.9790739253, -0.3528654744), (3.9887448111, -0.3520432907), (3.9984180938, -0.3511566112), (4.0080927332, -0.3502026626), (4.0177681465, -0.3491589018), (4.0274439917, -0.3479969059), (4.0371199389, -0.3466974757), (4.0467955121, -0.3452603771), (4.0564701685, -0.3436965921), (4.0661433382, -0.3420234565), (4.0758144751, -0.3402590295), (4.0854831118, -0.3384159376), (4.095148886, -0.3364983251), (4.1048115038, -0.3345052965), (4.1144707174, -0.3324330159), (4.1241262988, -0.3302771624), (4.1337780102, -0.3280356636), (4.1434255924, -0.3257097584), (4.153068778, -0.3233025448), (4.1627072987, -0.3208181148), (4.1723408947, -0.3182605346), (4.1819693248, -0.3156326956), (4.1915923694, -0.3129359681), (4.2012098234, -0.3101708241), (4.2108214926, -0.3073372184), (4.2204271881, -0.304435032), (4.2300267214, -0.3014645766), (4.2396199029, -0.2984267276), (4.2492065436, -0.2953226656), (4.258786457, -0.2921537191), (4.2683594605, -0.2889211811), (4.2779253776, -0.2856261017), (4.2874840376, -0.282269238), (4.2970352746, -0.278851167), (4.3065789262, -0.2753723561), (4.3161148322, -0.2718332444), (4.3256428337, -0.2682343362), (4.3351627726, -0.2645762253), (4.3446744926, -0.2608595484), (4.3541778395, -0.2570849563), (4.3636726623, -0.2532530807), (4.3731588137, -0.2493644975), (4.3826361505, -0.245419716), (4.3921045311, -0.2414192011), (4.4015638153, -0.2373633876), (4.411013862, -0.2332526966), (4.4204545287, -0.2290875546), (4.4298856707, -0.2248684007), (4.4393071448, -0.2205956739), (4.4487188112, -0.2162698056), (4.458120536, -0.211891212), (4.4675121942, -0.2074602839), (4.47689367, -0.2029773846), (4.4862648501, -0.1984428609), (4.4956256173, -0.1938570522), (4.504975846, -0.1892202999), (4.5143153949, -0.1845329585), (4.5236441052, -0.1797954008), (4.5329618149, -0.175008), (4.5422683702, -0.1701711155), (4.5515636381, -0.1652850783), (4.5608475193, -0.1603501764), (4.5701199583, -0.1553666417), (4.5793809308, -0.1503346525), (4.5867805329, -0.1462703979), (4.592325076, -0.1432004921), (4.5960191461, -0.1411442404), (4.5978656081, -0.1401137026)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((0, 0), 4.6, -1.7454708023, 3.4909416046)
                _nurbs_edge([(3.9308403746, 0.3535617878), (3.9327633334, 0.3537340065), (3.9366108028, 0.3540279926), (3.942386662, 0.35431762), (3.950096748, 0.3544160253), (3.9597470496, 0.3541460298), (3.9694071308, 0.3535930288), (3.9790739253, 0.3528654744), (3.9887448111, 0.3520432907), (3.9984180938, 0.3511566112), (4.0080927332, 0.3502026626), (4.0177681465, 0.3491589018), (4.0274439917, 0.3479969059), (4.0371199389, 0.3466974757), (4.0467955121, 0.3452603771), (4.0564701685, 0.3436965921), (4.0661433382, 0.3420234565), (4.0758144751, 0.3402590295), (4.0854831118, 0.3384159376), (4.095148886, 0.3364983251), (4.1048115038, 0.3345052965), (4.1144707174, 0.3324330159), (4.1241262988, 0.3302771624), (4.1337780102, 0.3280356636), (4.1434255924, 0.3257097584), (4.153068778, 0.3233025448), (4.1627072987, 0.3208181148), (4.1723408947, 0.3182605346), (4.1819693248, 0.3156326956), (4.1915923694, 0.3129359681), (4.2012098234, 0.3101708241), (4.2108214926, 0.3073372184), (4.2204271881, 0.304435032), (4.2300267214, 0.3014645766), (4.2396199029, 0.2984267276), (4.2492065436, 0.2953226656), (4.258786457, 0.2921537191), (4.2683594605, 0.2889211811), (4.2779253776, 0.2856261017), (4.2874840376, 0.282269238), (4.2970352746, 0.278851167), (4.3065789262, 0.2753723561), (4.3161148322, 0.2718332444), (4.3256428337, 0.2682343362), (4.3351627726, 0.2645762253), (4.3446744926, 0.2608595484), (4.3541778395, 0.2570849563), (4.3636726623, 0.2532530807), (4.3731588137, 0.2493644975), (4.3826361505, 0.245419716), (4.3921045311, 0.2414192011), (4.4015638153, 0.2373633876), (4.411013862, 0.2332526966), (4.4204545287, 0.2290875546), (4.4298856707, 0.2248684007), (4.4393071448, 0.2205956739), (4.4487188112, 0.2162698056), (4.458120536, 0.211891212), (4.4675121942, 0.2074602839), (4.47689367, 0.2029773846), (4.4862648501, 0.1984428609), (4.4956256173, 0.1938570522), (4.504975846, 0.1892202999), (4.5143153949, 0.1845329585), (4.5236441052, 0.1797954008), (4.5329618149, 0.175008), (4.5422683702, 0.1701711155), (4.5515636381, 0.1652850783), (4.5608475193, 0.1603501764), (4.5701199583, 0.1553666417), (4.5793809308, 0.1503346525), (4.5867805329, 0.1462703979), (4.592325076, 0.1432004921), (4.5960191461, 0.1411442404), (4.5978656081, 0.1401137026)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                Line((3.6989873479, 0.3327972126), (3.9308403746, 0.3535617878))
                Line((3.6989873479, -0.3327972126), (3.6989873479, 0.3327972126))
                Line((3.6989873479, -0.3327972126), (3.9308403746, -0.3535617878))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)
    return part.part


def model_145119_24107428_0001():
    """Model: Spur Gear (10 teeth) (1)"""
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
        with BuildSketch(Plane.XY):
            # Profile area: 2.6860070752, perimeter: 17.0583454542
            with BuildLine():
                CenterArc((0, 0), 1.51492, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.4855273891, perimeter: 2.6699908004
            with BuildLine():
                _nurbs_edge([(1.8516589845, -0.3216331627), (1.8532038333, -0.3219007686), (1.8562987303, -0.3223823579), (1.8609566738, -0.3229438771), (1.8671970241, -0.3233871295), (1.8750386621, -0.32352624), (1.8829107358, -0.3233690593), (1.8908024252, -0.3230315578), (1.8987054534, -0.32259622), (1.9066158502, -0.3220915222), (1.9145324384, -0.32151166), (1.9224557771, -0.3208307252), (1.9303870058, -0.3200179586), (1.9383265481, -0.3190550684), (1.9462735174, -0.3179438428), (1.9542263253, -0.3166973028), (1.9621830235, -0.3153344811), (1.9701417172, -0.3138742642), (1.9781010335, -0.3123283792), (1.9860602179, -0.310699902), (1.9940188805, -0.308986947), (2.0019768353, -0.307184981), (2.0099339169, -0.3052894799), (2.0178897693, -0.3032989843), (2.0258438307, -0.3012152906), (2.0337954323, -0.2990419886), (2.0417438627, -0.2967834828), (2.0496884413, -0.294443899), (2.0576286026, -0.2920258272), (2.0655638898, -0.2895303961), (2.073493914, -0.2869578696), (2.0814183231, -0.2843080856), (2.0893367698, -0.2815809267), (2.0972488733, -0.2787768624), (2.1051542237, -0.2758968908), (2.1130523974, -0.2729422988), (2.1209429696, -0.2699144801), (2.1288255273, -0.2668147419), (2.1366996841, -0.2636440838), (2.1445650773, -0.2604032303), (2.1524213608, -0.2570927332), (2.160268198, -0.253713054), (2.1681052562, -0.2502646485), (2.1759321992, -0.2467480663), (2.1837486878, -0.2431639407), (2.1915543843, -0.2395129451), (2.1993489548, -0.2357957608), (2.2071320725, -0.2320130421), (2.2149034215, -0.2281653769), (2.2226626956, -0.2242532901), (2.2304095936, -0.2202772642), (2.2381438167, -0.2162377559), (2.2458650653, -0.2121352128), (2.2535730343, -0.2079700947), (2.2612674164, -0.2037428736), (2.2689479068, -0.1994540215), (2.2766142091, -0.195104002), (2.2842660396, -0.1906932614), (2.291903135, -0.1862222187), (2.2995252486, -0.1816912659), (2.3071321368, -0.177100781), (2.3147235485, -0.172451137), (2.322299214, -0.1677427126), (2.3298588309, -0.1629759055), (2.3374020649, -0.1581511335), (2.3449285784, -0.1532688145), (2.3524380528, -0.1483293512), (2.3599302127, -0.1433331145), (2.367404852, -0.1382804269), (2.3748618508, -0.1331715497), (2.3823011508, -0.128006685), (2.3882384193, -0.1238301174), (2.3926834021, -0.1206725997), (2.3956431836, -0.1185564396), (2.3971221893, -0.1174955725)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((0, 0), 2.4, -2.806121858, 5.6122437161)
                _nurbs_edge([(1.8516589845, 0.3216331627), (1.8532038333, 0.3219007686), (1.8562987303, 0.3223823579), (1.8609566738, 0.3229438771), (1.8671970241, 0.3233871295), (1.8750386621, 0.32352624), (1.8829107358, 0.3233690593), (1.8908024252, 0.3230315578), (1.8987054534, 0.32259622), (1.9066158502, 0.3220915222), (1.9145324384, 0.32151166), (1.9224557771, 0.3208307252), (1.9303870058, 0.3200179586), (1.9383265481, 0.3190550684), (1.9462735174, 0.3179438428), (1.9542263253, 0.3166973028), (1.9621830235, 0.3153344811), (1.9701417172, 0.3138742642), (1.9781010335, 0.3123283792), (1.9860602179, 0.310699902), (1.9940188805, 0.308986947), (2.0019768353, 0.307184981), (2.0099339169, 0.3052894799), (2.0178897693, 0.3032989843), (2.0258438307, 0.3012152906), (2.0337954323, 0.2990419886), (2.0417438627, 0.2967834828), (2.0496884413, 0.294443899), (2.0576286026, 0.2920258272), (2.0655638898, 0.2895303961), (2.073493914, 0.2869578696), (2.0814183231, 0.2843080856), (2.0893367698, 0.2815809267), (2.0972488733, 0.2787768624), (2.1051542237, 0.2758968908), (2.1130523974, 0.2729422988), (2.1209429696, 0.2699144801), (2.1288255273, 0.2668147419), (2.1366996841, 0.2636440838), (2.1445650773, 0.2604032303), (2.1524213608, 0.2570927332), (2.160268198, 0.253713054), (2.1681052562, 0.2502646485), (2.1759321992, 0.2467480663), (2.1837486878, 0.2431639407), (2.1915543843, 0.2395129451), (2.1993489548, 0.2357957608), (2.2071320725, 0.2320130421), (2.2149034215, 0.2281653769), (2.2226626956, 0.2242532901), (2.2304095936, 0.2202772642), (2.2381438167, 0.2162377559), (2.2458650653, 0.2121352128), (2.2535730343, 0.2079700947), (2.2612674164, 0.2037428736), (2.2689479068, 0.1994540215), (2.2766142091, 0.195104002), (2.2842660396, 0.1906932614), (2.291903135, 0.1862222187), (2.2995252486, 0.1816912659), (2.3071321368, 0.177100781), (2.3147235485, 0.172451137), (2.322299214, 0.1677427126), (2.3298588309, 0.1629759055), (2.3374020649, 0.1581511335), (2.3449285784, 0.1532688145), (2.3524380528, 0.1483293512), (2.3599302127, 0.1433331145), (2.367404852, 0.1382804269), (2.3748618508, 0.1331715497), (2.3823011508, 0.128006685), (2.3882384193, 0.1238301174), (2.3926834021, 0.1206725997), (2.3956431836, 0.1185564396), (2.3971221893, 0.1174955725)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                Line((1.4915853907, 0.2592595174), (1.8516589845, 0.3216331627))
                Line((1.4915853907, -0.2592595174), (1.4915853907, 0.2592595174))
                Line((1.4915853907, -0.2592595174), (1.8516589845, -0.3216331627))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)
    return part.part


def model_145119_24107428_0004():
    """Model: Spur Gear (15 teeth) (2)"""
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
        with BuildSketch(Plane.XY):
            # Profile area: 72.572107902, perimeter: 41.0601133276
            with BuildLine():
                CenterArc((0, 0), 5.03492, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.030879908, perimeter: 5.4985033349
            with BuildLine():
                _nurbs_edge([(5.5978629881, -0.672852096), (5.6013146584, -0.6732662933), (5.6082232589, -0.6739920795), (5.6186019382, -0.6747729391), (5.6324702687, -0.6752294714), (5.649847208, -0.675005223), (5.6672545081, -0.6742128331), (5.6846807741, -0.6730745533), (5.7021169396, -0.6717502616), (5.7195581092, -0.6702967983), (5.7370021599, -0.6687048445), (5.7544487598, -0.6669259714), (5.771898291, -0.664901608), (5.7893506627, -0.6625955517), (5.8068046839, -0.6600102342), (5.8242585879, -0.657169998), (5.8417103186, -0.6541111478), (5.8591578826, -0.6508702446), (5.876599743, -0.6474708853), (5.894034931, -0.643919808), (5.9114628218, -0.6402140183), (5.9288829943, -0.6363451586), (5.9462950704, -0.6323045709), (5.9636985308, -0.6280891091), (5.9810926834, -0.6237020413), (5.9984767503, -0.6191501689), (6.015849922, -0.6144419926), (6.0332114193, -0.6095856257), (6.0505605663, -0.6045863803), (6.0678967911, -0.5994466647), (6.0852195886, -0.5941671772), (6.1025284936, -0.5887477244), (6.1198230522, -0.5831881226), (6.1371027885, -0.5774892462), (6.154367204, -0.5716530242), (6.1716157919, -0.5656819563), (6.1888480471, -0.5595787731), (6.2060634777, -0.5533460668), (6.2232616175, -0.5469858607), (6.2404420251, -0.5404996264), (6.2576042763, -0.5338884924), (6.2747479584, -0.5271533964), (6.2918726646, -0.520295249), (6.3089779872, -0.5133151264), (6.3260635178, -0.5062142707), (6.343128851, -0.498994002), (6.3601735871, -0.491655657), (6.3771973349, -0.4842005237), (6.3941997158, -0.476629764), (6.4111803619, -0.4689444124), (6.428138912, -0.4611454181), (6.4450750075, -0.4532336755), (6.4619882887, -0.445210057), (6.4788783909, -0.4370754536), (6.4957449454, -0.4288307789), (6.5125875878, -0.4204769451), (6.5294059631, -0.4120148468), (6.5461997324, -0.4034453448), (6.5629685813, -0.3947692456), (6.579712217, -0.3859873014), (6.596430351, -0.3771002337), (6.6131226858, -0.3681087522), (6.6297889012, -0.3590135741), (6.6464286364, -0.3498154497), (6.6630414903, -0.3405151672), (6.6796270559, -0.3311135136), (6.6961849499, -0.3216112456), (6.712714842, -0.312009058), (6.7292164882, -0.3023075517), (6.7456897531, -0.2925072086), (6.7621345773, -0.2826083971), (6.7752676781, -0.2746107796), (6.7851047091, -0.2685684397), (6.7916570452, -0.2645206078), (6.7949317921, -0.2624917906)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((0, 0), 6.8, -2.2122660809, 4.4245321618)
                _nurbs_edge([(5.5978629881, 0.672852096), (5.6013146584, 0.6732662933), (5.6082232589, 0.6739920795), (5.6186019382, 0.6747729391), (5.6324702687, 0.6752294714), (5.649847208, 0.675005223), (5.6672545081, 0.6742128331), (5.6846807741, 0.6730745533), (5.7021169396, 0.6717502616), (5.7195581092, 0.6702967983), (5.7370021599, 0.6687048445), (5.7544487598, 0.6669259714), (5.771898291, 0.664901608), (5.7893506627, 0.6625955517), (5.8068046839, 0.6600102342), (5.8242585879, 0.657169998), (5.8417103186, 0.6541111478), (5.8591578826, 0.6508702446), (5.876599743, 0.6474708853), (5.894034931, 0.643919808), (5.9114628218, 0.6402140183), (5.9288829943, 0.6363451586), (5.9462950704, 0.6323045709), (5.9636985308, 0.6280891091), (5.9810926834, 0.6237020413), (5.9984767503, 0.6191501689), (6.015849922, 0.6144419926), (6.0332114193, 0.6095856257), (6.0505605663, 0.6045863803), (6.0678967911, 0.5994466647), (6.0852195886, 0.5941671772), (6.1025284936, 0.5887477244), (6.1198230522, 0.5831881226), (6.1371027885, 0.5774892462), (6.154367204, 0.5716530242), (6.1716157919, 0.5656819563), (6.1888480471, 0.5595787731), (6.2060634777, 0.5533460668), (6.2232616175, 0.5469858607), (6.2404420251, 0.5404996264), (6.2576042763, 0.5338884924), (6.2747479584, 0.5271533964), (6.2918726646, 0.520295249), (6.3089779872, 0.5133151264), (6.3260635178, 0.5062142707), (6.343128851, 0.498994002), (6.3601735871, 0.491655657), (6.3771973349, 0.4842005237), (6.3941997158, 0.476629764), (6.4111803619, 0.4689444124), (6.428138912, 0.4611454181), (6.4450750075, 0.4532336755), (6.4619882887, 0.445210057), (6.4788783909, 0.4370754536), (6.4957449454, 0.4288307789), (6.5125875878, 0.4204769451), (6.5294059631, 0.4120148468), (6.5461997324, 0.4034453448), (6.5629685813, 0.3947692456), (6.579712217, 0.3859873014), (6.596430351, 0.3771002337), (6.6131226858, 0.3681087522), (6.6297889012, 0.3590135741), (6.6464286364, 0.3498154497), (6.6630414903, 0.3405151672), (6.6796270559, 0.3311135136), (6.6961849499, 0.3216112456), (6.712714842, 0.312009058), (6.7292164882, 0.3023075517), (6.7456897531, 0.2925072086), (6.7621345773, 0.2826083971), (6.7752676781, 0.2746107796), (6.7851047091, 0.2685684397), (6.7916570452, 0.2645206078), (6.7949317921, 0.2624917906)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                Line((4.9979453972, 0.6008625232), (5.5978629881, 0.672852096))
                Line((4.9979453972, -0.6008625232), (4.9979453972, 0.6008625232))
                Line((4.9979453972, -0.6008625232), (5.5978629881, -0.672852096))
            make_face()
        # OneSide extrude, distance=2.5
        extrude(amount=2.5, mode=Mode.ADD)
    return part.part


def model_145119_24107428_0006():
    """Model: Spur Gear (26 teeth)"""
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
        with BuildSketch(Plane.XY):
            # Profile area: 118.7663175016, perimeter: 66.4441819686
            with BuildLine():
                CenterArc((0, 0), 7.07492, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.2111517999, perimeter: 4.3075759832
            with BuildLine():
                _nurbs_edge([(7.3088216823, -0.5515410918), (7.3119727802, -0.5517779511), (7.3182763843, -0.5521740743), (7.3277360158, -0.5525354757), (7.3403569791, -0.5525747602), (7.3561447208, -0.5520194849), (7.3719413051, -0.5510291299), (7.3877438034, -0.5497706833), (7.4035495473, -0.5483673829), (7.4193565376, -0.5468658721), (7.4351632767, -0.5452620866), (7.45096866, -0.543521473), (7.4667718486, -0.541600348), (7.4825721411, -0.5394690813), (7.4983688754, -0.5371272323), (7.5141614404, -0.5345916698), (7.5299492688, -0.5318890831), (7.5457318376, -0.5290473233), (7.5615086656, -0.5260859545), (7.5772793107, -0.5230114679), (7.5930433638, -0.5198225686), (7.6088004428, -0.5165134084), (7.624550188, -0.5130773625), (7.640292255, -0.5095112272), (7.6560263121, -0.5058169068), (7.6717520399, -0.5019991785), (7.687469131, -0.4980643626), (7.7031772896, -0.4940187518), (7.7188762313, -0.4898668473), (7.7345656825, -0.4856108009), (7.7502453791, -0.4812513745), (7.765915065, -0.4767885265), (7.7815744914, -0.4722220941), (7.7972234158, -0.4675525689), (7.8128616007, -0.4627813133), (7.828488814, -0.4579101611), (7.8441048291, -0.4529411756), (7.8597094242, -0.4478763685), (7.8753023826, -0.4427173792), (7.8908834929, -0.4374653941), (7.9064525475, -0.432121321), (7.9220093423, -0.4266858964), (7.9375536766, -0.4211598119), (7.9530853519, -0.415543857), (7.9686041722, -0.4098389599), (7.9841099444, -0.4040461141), (7.9996024788, -0.3981663349), (8.0150815895, -0.3922006084), (8.0305470953, -0.3861498343), (8.0459988191, -0.3800148093), (8.0614365862, -0.3737962607), (8.0768602229, -0.3674948691), (8.0922695549, -0.3611112933), (8.1076644058, -0.3546462002), (8.1230445971, -0.3481002755), (8.1384099521, -0.3414742047), (8.1537602983, -0.3347686615), (8.1690954709, -0.3279842949), (8.1844153166, -0.3211217144), (8.1997196934, -0.3141814863), (8.2150084624, -0.3071641507), (8.2302814803, -0.3000702364), (8.2455385924, -0.292900275), (8.2607796243, -0.2856548193), (8.2760043796, -0.2783344512), (8.2912126571, -0.2709397529), (8.3064042667, -0.2634712848), (8.3215790445, -0.2559295622), (8.3367368695, -0.2483150313), (8.3518776771, -0.2406280491), (8.3670014416, -0.2328688884), (8.3790868189, -0.226603969), (8.3881431878, -0.2218729348), (8.3941773619, -0.2187045412), (8.3971935976, -0.2171167518)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((0, 0), 8.4, -1.4811022732, 2.9622045463)
                _nurbs_edge([(7.3088216823, 0.5515410918), (7.3119727802, 0.5517779511), (7.3182763843, 0.5521740743), (7.3277360158, 0.5525354757), (7.3403569791, 0.5525747602), (7.3561447208, 0.5520194849), (7.3719413051, 0.5510291299), (7.3877438034, 0.5497706833), (7.4035495473, 0.5483673829), (7.4193565376, 0.5468658721), (7.4351632767, 0.5452620866), (7.45096866, 0.543521473), (7.4667718486, 0.541600348), (7.4825721411, 0.5394690813), (7.4983688754, 0.5371272323), (7.5141614404, 0.5345916698), (7.5299492688, 0.5318890831), (7.5457318376, 0.5290473233), (7.5615086656, 0.5260859545), (7.5772793107, 0.5230114679), (7.5930433638, 0.5198225686), (7.6088004428, 0.5165134084), (7.624550188, 0.5130773625), (7.640292255, 0.5095112272), (7.6560263121, 0.5058169068), (7.6717520399, 0.5019991785), (7.687469131, 0.4980643626), (7.7031772896, 0.4940187518), (7.7188762313, 0.4898668473), (7.7345656825, 0.4856108009), (7.7502453791, 0.4812513745), (7.765915065, 0.4767885265), (7.7815744914, 0.4722220941), (7.7972234158, 0.4675525689), (7.8128616007, 0.4627813133), (7.828488814, 0.4579101611), (7.8441048291, 0.4529411756), (7.8597094242, 0.4478763685), (7.8753023826, 0.4427173792), (7.8908834929, 0.4374653941), (7.9064525475, 0.432121321), (7.9220093423, 0.4266858964), (7.9375536766, 0.4211598119), (7.9530853519, 0.415543857), (7.9686041722, 0.4098389599), (7.9841099444, 0.4040461141), (7.9996024788, 0.3981663349), (8.0150815895, 0.3922006084), (8.0305470953, 0.3861498343), (8.0459988191, 0.3800148093), (8.0614365862, 0.3737962607), (8.0768602229, 0.3674948691), (8.0922695549, 0.3611112933), (8.1076644058, 0.3546462002), (8.1230445971, 0.3481002755), (8.1384099521, 0.3414742047), (8.1537602983, 0.3347686615), (8.1690954709, 0.3279842949), (8.1844153166, 0.3211217144), (8.1997196934, 0.3141814863), (8.2150084624, 0.3071641507), (8.2302814803, 0.3000702364), (8.2455385924, 0.292900275), (8.2607796243, 0.2856548193), (8.2760043796, 0.2783344512), (8.2912126571, 0.2709397529), (8.3064042667, 0.2634712848), (8.3215790445, 0.2559295622), (8.3367368695, 0.2483150313), (8.3518776771, 0.2406280491), (8.3670014416, 0.2328688884), (8.3790868189, 0.226603969), (8.3881431878, 0.2218729348), (8.3941773619, 0.2187045412), (8.3971935976, 0.2171167518)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                Line((7.0538641465, 0.5323766373), (7.3088216823, 0.5515410918))
                Line((7.0538641465, -0.5323766373), (7.0538641465, 0.5323766373))
                Line((7.0538641465, -0.5323766373), (7.3088216823, -0.5515410918))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)
    return part.part


def model_145119_24107428_0007():
    """Model: Spur Gear (50 teeth)"""
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
        with BuildSketch(Plane.XY):
            # Profile area: 245.9355050041, perimeter: 81.7751541181
            with BuildLine():
                CenterArc((0, 0), 9.51492, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.6675230192, perimeter: 3.2935954161
            with BuildLine():
                Line((9.3868471233, 0.4351129055), (9.3868471233, -0.4351129055))
                _nurbs_edge([(9.3868471233, -0.4351129055), (9.3897783958, -0.4351210159), (9.3956410205, -0.4351137479), (9.4044351965, -0.43503238), (9.4161612425, -0.4347829117), (9.4308195466, -0.4342369827), (9.445478444, -0.4334600602), (9.4601376285, -0.4324586634), (9.4747965847, -0.4312440632), (9.4894545482, -0.429833238), (9.5041106203, -0.428246164), (9.5187638716, -0.4265033496), (9.5334134468, -0.4246233832), (9.5480586784, -0.4226202335), (9.5626991665, -0.4205013728), (9.5773346911, -0.418269925), (9.5919651447, -0.4159263097), (9.6065904607, -0.4134699981), (9.621210536, -0.4109014109), (9.6358251805, -0.4082231596), (9.6504341556, -0.4054390879), (9.6650371981, -0.4025536738), (9.6796340488, -0.3995713317), (9.6942244823, -0.3964956629), (9.7088083243, -0.3933290363), (9.7233854334, -0.3900730329), (9.7379556893, -0.3867287281), (9.7525189799, -0.3832970182), (9.7670751867, -0.3797789759), (9.7816241771, -0.3761760364), (9.7961658121, -0.3724898157), (9.8106999498, -0.368722005), (9.8252264512, -0.3648742437), (9.8397451853, -0.3609479821), (9.8542560319, -0.3569444173), (9.868758878, -0.3528645766), (9.883253616, -0.3487093691), (9.897740141, -0.3444796472), (9.9122183485, -0.3401762729), (9.9266881325, -0.335800151), (9.9411493875, -0.3313521967), (9.9556020081, -0.3268333172), (9.9700458903, -0.3222443902), (9.9844809323, -0.317586241), (9.9989070348, -0.3128596315), (10.0133241007, -0.3080652752), (10.0277320351, -0.3032038466), (10.0421307449, -0.2982759922), (10.0565201391, -0.2932823436), (10.0709001279, -0.2882235247), (10.0852706226, -0.2831001474), (10.0996315348, -0.2779128106), (10.1139827754, -0.2726620985), (10.1283242543, -0.2673485788), (10.1426558805, -0.261972802), (10.1569775635, -0.2565352994), (10.1712892151, -0.2510365817), (10.185590751, -0.2454771381), (10.1998820925, -0.239857435), (10.2141631676, -0.2341779172), (10.2284339058, -0.2284390164), (10.2426942342, -0.2226411596), (10.2569440742, -0.2167847763), (10.2711833364, -0.2108703093), (10.2854119189, -0.2048982191), (10.2996297168, -0.1988689638), (10.3138366306, -0.1927829822), (10.3280325747, -0.1866406762), (10.3422174868, -0.1804423936), (10.3563913352, -0.1741884121), (10.3705541097, -0.1678789431), (10.3818754728, -0.1627870956), (10.3903615172, -0.1589433455), (10.3960166684, -0.1563697982), (10.3988436911, -0.1550802628)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((0, 0), 10.4, -0.8544013328, 1.7088026656)
                _nurbs_edge([(9.3868471233, 0.4351129055), (9.3897783958, 0.4351210159), (9.3956410205, 0.4351137479), (9.4044351965, 0.43503238), (9.4161612425, 0.4347829117), (9.4308195466, 0.4342369827), (9.445478444, 0.4334600602), (9.4601376285, 0.4324586634), (9.4747965847, 0.4312440632), (9.4894545482, 0.429833238), (9.5041106203, 0.428246164), (9.5187638716, 0.4265033496), (9.5334134468, 0.4246233832), (9.5480586784, 0.4226202335), (9.5626991665, 0.4205013728), (9.5773346911, 0.418269925), (9.5919651447, 0.4159263097), (9.6065904607, 0.4134699981), (9.621210536, 0.4109014109), (9.6358251805, 0.4082231596), (9.6504341556, 0.4054390879), (9.6650371981, 0.4025536738), (9.6796340488, 0.3995713317), (9.6942244823, 0.3964956629), (9.7088083243, 0.3933290363), (9.7233854334, 0.3900730329), (9.7379556893, 0.3867287281), (9.7525189799, 0.3832970182), (9.7670751867, 0.3797789759), (9.7816241771, 0.3761760364), (9.7961658121, 0.3724898157), (9.8106999498, 0.368722005), (9.8252264512, 0.3648742437), (9.8397451853, 0.3609479821), (9.8542560319, 0.3569444173), (9.868758878, 0.3528645766), (9.883253616, 0.3487093691), (9.897740141, 0.3444796472), (9.9122183485, 0.3401762729), (9.9266881325, 0.335800151), (9.9411493875, 0.3313521967), (9.9556020081, 0.3268333172), (9.9700458903, 0.3222443902), (9.9844809323, 0.317586241), (9.9989070348, 0.3128596315), (10.0133241007, 0.3080652752), (10.0277320351, 0.3032038466), (10.0421307449, 0.2982759922), (10.0565201391, 0.2932823436), (10.0709001279, 0.2882235247), (10.0852706226, 0.2831001474), (10.0996315348, 0.2779128106), (10.1139827754, 0.2726620985), (10.1283242543, 0.2673485788), (10.1426558805, 0.261972802), (10.1569775635, 0.2565352994), (10.1712892151, 0.2510365817), (10.185590751, 0.2454771381), (10.1998820925, 0.239857435), (10.2141631676, 0.2341779172), (10.2284339058, 0.2284390164), (10.2426942342, 0.2226411596), (10.2569440742, 0.2167847763), (10.2711833364, 0.2108703093), (10.2854119189, 0.2048982191), (10.2996297168, 0.1988689638), (10.3138366306, 0.1927829822), (10.3280325747, 0.1866406762), (10.3422174868, 0.1804423936), (10.3563913352, 0.1741884121), (10.3705541097, 0.1678789431), (10.3818754728, 0.1627870956), (10.3903615172, 0.1589433455), (10.3960166684, 0.1563697982), (10.3988436911, 0.1550802628)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)
    return part.part


def model_145119_24107428_0008():
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
        with BuildSketch(Plane.XY):
            # Profile area: 82.8902341763, perimeter: 40.6831222092
            with BuildLine():
                CenterArc((0, 0), 5.27492, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.1796076515, perimeter: 4.2176219617
            with BuildLine():
                _nurbs_edge([(5.6135579548, -0.5260865563), (5.6163984681, -0.5263520302), (5.6220819264, -0.5268069373), (5.6306144087, -0.5272611792), (5.6420050165, -0.5274332778), (5.6562628355, -0.5270571965), (5.6705353307, -0.5262565352), (5.6848174025, -0.525195282), (5.6991047626, -0.5239934184), (5.7133947412, -0.5226953959), (5.7276857913, -0.5212962034), (5.7419771359, -0.5197612512), (5.7562683798, -0.5180474853), (5.770559094, -0.5161265809), (5.7848485489, -0.5139988705), (5.7991358703, -0.5116813937), (5.8134201186, -0.5092005631), (5.8277003919, -0.5065836121), (5.8419759355, -0.5038491387), (5.8562461882, -0.5010030121), (5.8705107131, -0.4980436224), (5.884769153, -0.4949650603), (5.8990211812, -0.4917608364), (5.9132664441, -0.488428073), (5.9275045428, -0.4849688257), (5.9417350589, -0.4813878941), (5.9559575697, -0.4776915051), (5.9701716665, -0.4738857724), (5.984376975, -0.4699749385), (5.9985731594, -0.4659609897), (6.0127599099, -0.4618445849), (6.0269369341, -0.4576256383), (6.0411039485, -0.4533039881), (6.0552606676, -0.448880166), (6.0694068018, -0.444355535), (6.083542062, -0.439731906), (6.0976661622, -0.4350112969), (6.111778823, -0.4301956575), (6.1258797751, -0.425286552), (6.1399687597, -0.4202851123), (6.1540455255, -0.4151922035), (6.1681098272, -0.4100085328), (6.182161423, -0.404734771), (6.1962000726, -0.399371695), (6.2102255368, -0.3939202136), (6.2242375787, -0.3883812975), (6.2382359653, -0.3827559358), (6.2522204681, -0.3770450866), (6.266190865, -0.3712496202), (6.2801469397, -0.3653703082), (6.2940884793, -0.3594078561), (6.3080152724, -0.3533629252), (6.3219271067, -0.3472361575), (6.3358237674, -0.341028205), (6.3497050371, -0.3347397374), (6.3635707004, -0.3283714243), (6.3774205474, -0.3219239233), (6.3912543773, -0.3153978674), (6.4050720034, -0.3087938512), (6.4188732525, -0.3021124272), (6.4326579546, -0.2953541241), (6.4464259343, -0.2885194596), (6.460177003, -0.2816089554), (6.4739109481, -0.2746231549), (6.4876275313, -0.2675626291), (6.5013265098, -0.2604279493), (6.5150076541, -0.2532196652), (6.5286707659, -0.2459382823), (6.5423156986, -0.2385842386), (6.5559423714, -0.2311578858), (6.5695507503, -0.2236594928), (6.5804228158, -0.217603297), (6.5885686363, -0.2130288666), (6.5939955272, -0.2099649028), (6.5967080587, -0.2084293351)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((0, 0), 6.6, -1.8097131993, 3.6194263985)
                _nurbs_edge([(5.6135579548, 0.5260865563), (5.6163984681, 0.5263520302), (5.6220819264, 0.5268069373), (5.6306144087, 0.5272611792), (5.6420050165, 0.5274332778), (5.6562628355, 0.5270571965), (5.6705353307, 0.5262565352), (5.6848174025, 0.525195282), (5.6991047626, 0.5239934184), (5.7133947412, 0.5226953959), (5.7276857913, 0.5212962034), (5.7419771359, 0.5197612512), (5.7562683798, 0.5180474853), (5.770559094, 0.5161265809), (5.7848485489, 0.5139988705), (5.7991358703, 0.5116813937), (5.8134201186, 0.5092005631), (5.8277003919, 0.5065836121), (5.8419759355, 0.5038491387), (5.8562461882, 0.5010030121), (5.8705107131, 0.4980436224), (5.884769153, 0.4949650603), (5.8990211812, 0.4917608364), (5.9132664441, 0.488428073), (5.9275045428, 0.4849688257), (5.9417350589, 0.4813878941), (5.9559575697, 0.4776915051), (5.9701716665, 0.4738857724), (5.984376975, 0.4699749385), (5.9985731594, 0.4659609897), (6.0127599099, 0.4618445849), (6.0269369341, 0.4576256383), (6.0411039485, 0.4533039881), (6.0552606676, 0.448880166), (6.0694068018, 0.444355535), (6.083542062, 0.439731906), (6.0976661622, 0.4350112969), (6.111778823, 0.4301956575), (6.1258797751, 0.425286552), (6.1399687597, 0.4202851123), (6.1540455255, 0.4151922035), (6.1681098272, 0.4100085328), (6.182161423, 0.404734771), (6.1962000726, 0.399371695), (6.2102255368, 0.3939202136), (6.2242375787, 0.3883812975), (6.2382359653, 0.3827559358), (6.2522204681, 0.3770450866), (6.266190865, 0.3712496202), (6.2801469397, 0.3653703082), (6.2940884793, 0.3594078561), (6.3080152724, 0.3533629252), (6.3219271067, 0.3472361575), (6.3358237674, 0.341028205), (6.3497050371, 0.3347397374), (6.3635707004, 0.3283714243), (6.3774205474, 0.3219239233), (6.3912543773, 0.3153978674), (6.4050720034, 0.3087938512), (6.4188732525, 0.3021124272), (6.4326579546, 0.2953541241), (6.4464259343, 0.2885194596), (6.460177003, 0.2816089554), (6.4739109481, 0.2746231549), (6.4876275313, 0.2675626291), (6.5013265098, 0.2604279493), (6.5150076541, 0.2532196652), (6.5286707659, 0.2459382823), (6.5423156986, 0.2385842386), (6.5559423714, 0.2311578858), (6.5695507503, 0.2236594928), (6.5804228158, 0.217603297), (6.5885686363, 0.2130288666), (6.5939955272, 0.2099649028), (6.5967080587, 0.2084293351)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                Line((5.2509112934, 0.4921936592), (5.6135579548, 0.5260865563))
                Line((5.2509112934, -0.4921936592), (5.2509112934, 0.4921936592))
                Line((5.2509112934, -0.4921936592), (5.6135579548, -0.5260865563))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)
    return part.part


def model_145121_2b2a370d_0000():
    """Model: Spur Gear (14 teeth)"""
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
        with BuildSketch(Plane.XY):
            # Profile area: 6.6207412898, perimeter: 16.869849895
            with BuildLine():
                CenterArc((0, 0), 1.73492, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.95, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.8
        extrude(amount=1.8)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.285078409, perimeter: 2.0580520292
            with BuildLine():
                _nurbs_edge([(1.9574357296, -0.2501466799), (1.9586934168, -0.2503067323), (1.9612111457, -0.250588898), (1.9649948024, -0.2508983309), (1.9700532077, -0.2510945708), (1.9763952459, -0.2510447218), (1.9827517547, -0.2507826399), (1.9891180718, -0.2503898801), (1.9954904598, -0.2499259802), (2.0018668953, -0.2494128577), (2.0082465108, -0.2488478499), (2.0146291876, -0.2482136141), (2.0210151128, -0.247488651), (2.0274042997, -0.246658894), (2.0337962941, -0.245724538), (2.040190388, -0.2446940653), (2.0465857402, -0.243580596), (2.0529815237, -0.2423976263), (2.0593770861, -0.241154304), (2.0657720163, -0.2398534571), (2.0721660505, -0.2384942099), (2.0785590139, -0.2370735672), (2.0849507544, -0.2355882661), (2.0913410667, -0.2340368694), (2.0977296685, -0.2324203863), (2.1041162389, -0.2307411853), (2.11050044, -0.2290023372), (2.1168819432, -0.2272068481), (2.1232604597, -0.2253567825), (2.1296357452, -0.2234530888), (2.1360075843, -0.2214960599), (2.1423757789, -0.2194856237), (2.1487401364, -0.2174216756), (2.1551004561, -0.2153044626), (2.1614565264, -0.2131346435), (2.1678081314, -0.2109130994), (2.1741550551, -0.2086408132), (2.180497086, -0.206318733), (2.1868340226, -0.2039476136), (2.1931656741, -0.2015279968), (2.1994918565, -0.1990602935), (2.2058123911, -0.1965448371), (2.2121271012, -0.1939819449), (2.2184358101, -0.1913719885), (2.2247383401, -0.1887154053), (2.2310345147, -0.186012664), (2.2373241592, -0.1832642428), (2.2436071022, -0.1804706045), (2.2498831775, -0.1776321692), (2.2561522234, -0.1747493084), (2.2624140808, -0.1718223616), (2.2686685918, -0.168851647), (2.2749155981, -0.1658374738), (2.2811549389, -0.1627801566), (2.2873864515, -0.1596800195), (2.2936099743, -0.1565373866), (2.2998253497, -0.1533525769), (2.3060324266, -0.1501258978), (2.312231064, -0.1468576385), (2.3184211305, -0.1435480681), (2.3246024972, -0.1401974446), (2.3307750312, -0.1368060208), (2.33693859, -0.1333740514), (2.343093014, -0.1299018015), (2.349238125, -0.1263895496), (2.3553737418, -0.1228375743), (2.3614996924, -0.1192461446), (2.3676158275, -0.1156155086), (2.3737220346, -0.1119458834), (2.3798182481, -0.1082374457), (2.3859044367, -0.1044903327), (2.3907653612, -0.1014617802), (2.3944065415, -0.0991730321), (2.3968319899, -0.0976394986), (2.3980442129, -0.0968708065)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((0, 0), 2.4, -2.313248553, 4.6264971061)
                _nurbs_edge([(1.9574357296, 0.2501466799), (1.9586934168, 0.2503067323), (1.9612111457, 0.250588898), (1.9649948024, 0.2508983309), (1.9700532077, 0.2510945708), (1.9763952459, 0.2510447218), (1.9827517547, 0.2507826399), (1.9891180718, 0.2503898801), (1.9954904598, 0.2499259802), (2.0018668953, 0.2494128577), (2.0082465108, 0.2488478499), (2.0146291876, 0.2482136141), (2.0210151128, 0.247488651), (2.0274042997, 0.246658894), (2.0337962941, 0.245724538), (2.040190388, 0.2446940653), (2.0465857402, 0.243580596), (2.0529815237, 0.2423976263), (2.0593770861, 0.241154304), (2.0657720163, 0.2398534571), (2.0721660505, 0.2384942099), (2.0785590139, 0.2370735672), (2.0849507544, 0.2355882661), (2.0913410667, 0.2340368694), (2.0977296685, 0.2324203863), (2.1041162389, 0.2307411853), (2.11050044, 0.2290023372), (2.1168819432, 0.2272068481), (2.1232604597, 0.2253567825), (2.1296357452, 0.2234530888), (2.1360075843, 0.2214960599), (2.1423757789, 0.2194856237), (2.1487401364, 0.2174216756), (2.1551004561, 0.2153044626), (2.1614565264, 0.2131346435), (2.1678081314, 0.2109130994), (2.1741550551, 0.2086408132), (2.180497086, 0.206318733), (2.1868340226, 0.2039476136), (2.1931656741, 0.2015279968), (2.1994918565, 0.1990602935), (2.2058123911, 0.1965448371), (2.2121271012, 0.1939819449), (2.2184358101, 0.1913719885), (2.2247383401, 0.1887154053), (2.2310345147, 0.186012664), (2.2373241592, 0.1832642428), (2.2436071022, 0.1804706045), (2.2498831775, 0.1776321692), (2.2561522234, 0.1747493084), (2.2624140808, 0.1718223616), (2.2686685918, 0.168851647), (2.2749155981, 0.1658374738), (2.2811549389, 0.1627801566), (2.2873864515, 0.1596800195), (2.2936099743, 0.1565373866), (2.2998253497, 0.1533525769), (2.3060324266, 0.1501258978), (2.312231064, 0.1468576385), (2.3184211305, 0.1435480681), (2.3246024972, 0.1401974446), (2.3307750312, 0.1368060208), (2.33693859, 0.1333740514), (2.343093014, 0.1299018015), (2.349238125, 0.1263895496), (2.3553737418, 0.1228375743), (2.3614996924, 0.1192461446), (2.3676158275, 0.1156155086), (2.3737220346, 0.1119458834), (2.3798182481, 0.1082374457), (2.3859044367, 0.1044903327), (2.3907653612, 0.1014617802), (2.3944065415, 0.0991730321), (2.3968319899, 0.0976394986), (2.3980442129, 0.0968708065)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                Line((1.7199327105, 0.2199222071), (1.9574357296, 0.2501466799))
                Line((1.7199327105, -0.2199222071), (1.7199327105, 0.2199222071))
                Line((1.7199327105, -0.2199222071), (1.9574357296, -0.2501466799))
            make_face()
        # OneSide extrude, distance=1.8
        extrude(amount=1.8, mode=Mode.ADD)
    return part.part


def model_145121_2b2a370d_0001():
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
        with BuildSketch(Plane.XY):
            # Profile area: 18.976172807, perimeter: 22.5247166714
            with BuildLine():
                CenterArc((0, 0), 2.63492, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.95, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.8
        extrude(amount=1.8)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2963992026, perimeter: 2.1144079475
            with BuildLine():
                _nurbs_edge([(2.8067789774, -0.2630432781), (2.8081919834, -0.2631749858), (2.8110193135, -0.2634008603), (2.8152642629, -0.263627051), (2.8209318, -0.2637144677), (2.8280270831, -0.2635309925), (2.8351308394, -0.2631363723), (2.8422405648, -0.2626111272), (2.8493541317, -0.2620147865), (2.856470193, -0.2613699664), (2.863587951, -0.2606747829), (2.8707069875, -0.2599126029), (2.8778270787, -0.2590623334), (2.8849479992, -0.258109556), (2.8920693846, -0.2570539338), (2.8991908023, -0.2559035151), (2.9063117888, -0.2546711183), (2.9134318968, -0.2533701593), (2.9205507462, -0.2520101147), (2.9276680489, -0.2505941453), (2.934783577, -0.2491216374), (2.9418971425, -0.2475897621), (2.9490085731, -0.2459952963), (2.9561176868, -0.244336639), (2.9632242799, -0.2426146628), (2.9703281395, -0.240831636), (2.9774290504, -0.238990582), (2.9845268039, -0.2370945219), (2.9916212066, -0.2351456259), (2.998712084, -0.2331449266), (3.005799274, -0.231092782), (3.0128826235, -0.2289891582), (3.019961984, -0.2268339588), (3.0270372065, -0.2246273975), (3.03410814, -0.2223701113), (3.0411746341, -0.2200629668), (3.0482365396, -0.2177069442), (3.0552937102, -0.215303001), (3.0623460048, -0.2128519184), (3.0693932871, -0.2103542581), (3.0764354246, -0.2078104468), (3.0834722878, -0.2052208283), (3.0905037489, -0.202585724), (3.0975296809, -0.1999055018), (3.1045499573, -0.1971805975), (3.1115644528, -0.1944114791), (3.1185730438, -0.1915986257), (3.1255756091, -0.1887425031), (3.1325720304, -0.1858435365), (3.1395621927, -0.1829021013), (3.1465459825, -0.1799185398), (3.1535232869, -0.1768931716), (3.1604939929, -0.173826306), (3.1674579858, -0.1707182562), (3.1744151495, -0.1675693445), (3.1813653687, -0.1643798936), (3.1883085308, -0.1611502208), (3.1952445279, -0.1578806324), (3.2021732592, -0.154571416), (3.2090946309, -0.1512228393), (3.2160085516, -0.1478351577), (3.2229149267, -0.1444086207), (3.2298136549, -0.140943479), (3.2367046226, -0.1374399929), (3.2435877021, -0.1338984357), (3.250462763, -0.1303190811), (3.2573296813, -0.1267021932), (3.2641883493, -0.1230480153), (3.2710386863, -0.1193567599), (3.2778806461, -0.115628599), (3.2847142076, -0.1118636657), (3.290174335, -0.1088223761), (3.2942656514, -0.1065249287), (3.2969915166, -0.1049859749), (3.2983540294, -0.1042146675)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((0, 0), 3.3, -1.8097131993, 3.6194263985)
                _nurbs_edge([(2.8067789774, 0.2630432781), (2.8081919834, 0.2631749858), (2.8110193135, 0.2634008603), (2.8152642629, 0.263627051), (2.8209318, 0.2637144677), (2.8280270831, 0.2635309925), (2.8351308394, 0.2631363723), (2.8422405648, 0.2626111272), (2.8493541317, 0.2620147865), (2.856470193, 0.2613699664), (2.863587951, 0.2606747829), (2.8707069875, 0.2599126029), (2.8778270787, 0.2590623334), (2.8849479992, 0.258109556), (2.8920693846, 0.2570539338), (2.8991908023, 0.2559035151), (2.9063117888, 0.2546711183), (2.9134318968, 0.2533701593), (2.9205507462, 0.2520101147), (2.9276680489, 0.2505941453), (2.934783577, 0.2491216374), (2.9418971425, 0.2475897621), (2.9490085731, 0.2459952963), (2.9561176868, 0.244336639), (2.9632242799, 0.2426146628), (2.9703281395, 0.240831636), (2.9774290504, 0.238990582), (2.9845268039, 0.2370945219), (2.9916212066, 0.2351456259), (2.998712084, 0.2331449266), (3.005799274, 0.231092782), (3.0128826235, 0.2289891582), (3.019961984, 0.2268339588), (3.0270372065, 0.2246273975), (3.03410814, 0.2223701113), (3.0411746341, 0.2200629668), (3.0482365396, 0.2177069442), (3.0552937102, 0.215303001), (3.0623460048, 0.2128519184), (3.0693932871, 0.2103542581), (3.0764354246, 0.2078104468), (3.0834722878, 0.2052208283), (3.0905037489, 0.202585724), (3.0975296809, 0.1999055018), (3.1045499573, 0.1971805975), (3.1115644528, 0.1944114791), (3.1185730438, 0.1915986257), (3.1255756091, 0.1887425031), (3.1325720304, 0.1858435365), (3.1395621927, 0.1829021013), (3.1465459825, 0.1799185398), (3.1535232869, 0.1768931716), (3.1604939929, 0.173826306), (3.1674579858, 0.1707182562), (3.1744151495, 0.1675693445), (3.1813653687, 0.1643798936), (3.1883085308, 0.1611502208), (3.1952445279, 0.1578806324), (3.2021732592, 0.154571416), (3.2090946309, 0.1512228393), (3.2160085516, 0.1478351577), (3.2229149267, 0.1444086207), (3.2298136549, 0.140943479), (3.2367046226, 0.1374399929), (3.2435877021, 0.1338984357), (3.250462763, 0.1303190811), (3.2573296813, 0.1267021932), (3.2641883493, 0.1230480153), (3.2710386863, 0.1193567599), (3.2778806461, 0.115628599), (3.2847142076, 0.1118636657), (3.290174335, 0.1088223761), (3.2942656514, 0.1065249287), (3.2969915166, 0.1049859749), (3.2983540294, 0.1042146675)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                Line((2.6224289094, 0.2458598266), (2.8067789774, 0.2630432781))
                Line((2.6224289094, -0.2458598266), (2.6224289094, 0.2458598266))
                Line((2.6224289094, -0.2458598266), (2.8067789774, -0.2630432781))
            make_face()
        # OneSide extrude, distance=1.8
        extrude(amount=1.8, mode=Mode.ADD)
    return part.part


def model_145176_dc7a828b_0002():
    """Model: Camera_Holder v3"""
    with BuildPart() as part:
        # Sketch3 -> Extrude3 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 19.1014473424, perimeter: 32.4659134101
            with BuildLine():
                Line((19.2008697452, 7.7706378865), (19.2008697452, 6.4933765496))
                Line((16.8414728549, 9.1647329742), (19.2008697452, 7.7706378865))
                Line((15, 11.5), (16.8414728549, 9.1647329742))
                Line((11.1946496309, 13.159978375), (15, 11.5))
                Line((12, 8.5), (11.1946496309, 13.159978375))
                Line((17.23470567, 7.0412757729), (12, 8.5))
                Line((19.2008697452, 6.4933765496), (17.23470567, 7.0412757729))
            make_face()
            with BuildLine():
                Line((15.5, 9), (14.1517543564, 10.7436814293))
                Line((12.8035087127, 9.1210374179), (15.5, 9))
                Line((12.5, 11.5), (12.8035087127, 9.1210374179))
                Line((14.1517543564, 10.7436814293), (12.5, 11.5))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-4.7405
        extrude(amount=-4.7405)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 14 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(6.6125935782, 15.1587730254, 0), x_dir=(0, 0, -1), z_dir=(0.3998355641, 0.9165868871, 0))):
            # Profile area: 35.612531443, perimeter: 38.1602566487
            with BuildLine():
                Line((4.0090642622, -9.1506943198), (4.7405, -9.1506943198))
                Line((4.0090642622, -9.1506943198), (3.7830262368, -10.9416109822))
                Line((3.7830262368, -10.9416109822), (3.3433230609, -13.004833577))
                Line((3.3433230609, -13.004833577), (3.3433230609, -18))
                Line((3.3433230609, -18), (6.3874219712, -17.6386285848))
                Line((6.3874219712, -17.6386285848), (6.3874219712, -3.5681269551))
                Line((6.3874219712, -3.5681269551), (2.37025, -3.9401834886))
                Line((2.37025, -3.9401834886), (3.3433230609, -3.9401834886))
                Line((3.3433230609, -3.9401834886), (3.6080376089, -4.9990416806))
                Line((4.7405, -4.9990416806), (3.6080376089, -4.9990416806))
                Line((4.7405, -9.1506943198), (4.7405, -4.9990416806))
            make_face()
            # Profile area: 3.0861509619, perimeter: 10.2563058746
            with BuildLine():
                Line((4.7405, -9.1506943198), (4.7405, -4.9990416806))
                Line((4.7405, -4.9990416806), (3.6080376089, -4.9990416806))
                Line((3.6080376089, -4.9990416806), (4.2227294128, -7.457808896))
                Line((4.2227294128, -7.457808896), (4.0090642622, -9.1506943198))
                Line((4.0090642622, -9.1506943198), (4.7405, -9.1506943198))
            make_face()
            # Profile area: 3.0861509619, perimeter: 10.2563058746
            with BuildLine():
                Line((1.1324623911, -4.9990416806), (0, -4.9990416806))
                Line((0, -4.9990416806), (0, -9.1506943198))
                Line((0, -9.1506943198), (0.7314357378, -9.1506943198))
                Line((0.5177705872, -7.457808896), (0.7314357378, -9.1506943198))
                Line((1.1324623911, -4.9990416806), (0.5177705872, -7.457808896))
            make_face()
            # Profile area: 35.612531443, perimeter: 38.1602566487
            with BuildLine():
                Line((-1.6469219712, -3.5681269551), (2.37025, -3.9401834886))
                Line((-1.6469219712, -17.6386285848), (-1.6469219712, -3.5681269551))
                Line((1.3971769391, -18), (-1.6469219712, -17.6386285848))
                Line((1.3971769391, -13.004833577), (1.3971769391, -18))
                Line((0.9574737632, -10.9416109822), (1.3971769391, -13.004833577))
                Line((0.7314357378, -9.1506943198), (0.9574737632, -10.9416109822))
                Line((0, -9.1506943198), (0.7314357378, -9.1506943198))
                Line((0, -4.9990416806), (0, -9.1506943198))
                Line((1.1324623911, -4.9990416806), (0, -4.9990416806))
                Line((1.3971769391, -3.9401834886), (1.1324623911, -4.9990416806))
                Line((2.37025, -3.9401834886), (1.3971769391, -3.9401834886))
            make_face()
        # OneSide extrude, distance=-22.2803
        extrude(amount=-22.2803, mode=Mode.SUBTRACT)
    return part.part


def model_145201_a104c55b_0001():
    """Model: Grunn"""
    with BuildPart() as part:
        # Sketch1 -> Extrude6 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 6248925.5221819356, perimeter: 10281.3468482475
            with BuildLine():
                Line((-285.7178226144, 1192.6296644401), (-285.7178226144, -779.6223619868))
                Line((-285.7178226144, -779.6223619868), (2882.7035750825, -779.6223619868))
                Line((2882.7035750825, -779.6223619868), (2882.7035750825, 1192.6296644401))
                Line((2882.7035750825, 1192.6296644401), (-285.7178226144, 1192.6296644401))
            make_face()
        # OneSide extrude, distance=-10
        extrude(amount=-10)

        # Sketch4 -> Extrude8 (Join)
        # Sketch on BRepFace
        # Sketch has 12 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 2487018.9240055042, perimeter: 13719.3468482475
            with BuildLine():
                Line((0, -873.3), (100, -873.3))
                Line((-1619, -873.3), (0, -873.3))
                Line((-1619, -873.3), (-2882.7035750825, -873.3))
                Line((-2882.7035750825, -873.3), (-2882.7035750825, -1192.6296644401))
                Line((-2882.7035750825, -1192.6296644401), (285.7178226144, -1192.6296644401))
                Line((285.7178226144, -1192.6296644401), (285.7178226144, 779.6223619868))
                Line((285.7178226144, 779.6223619868), (-1619, 779.6223619868))
                Line((-1619, 100), (-1619, 779.6223619868))
                Line((100, 100), (-1619, 100))
                Line((100, -873.3), (100, 100))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch4 -> Extrude7 (Join)
        # Sketch on BRepFace
        # Sketch has 12 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 259230, perimeter: 5384.6
            with BuildLine():
                Line((100, -873.3), (100, 100))
                Line((100, 100), (-1619, 100))
                Line((-1619, 100), (-1619, 0))
                Line((-907, 0), (-1619, 0))
                Line((-820, 0), (-907, 0))
                Line((0, 0), (-820, 0))
                Line((0, -873.3), (0, 0))
                Line((0, -873.3), (100, -873.3))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)
    return part.part


def model_145257_89235edd_0005():
    """Model: COLLAR v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.8981192229, perimeter: 12.8805298797
            with BuildLine():
                CenterArc((0, 0), 1.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0353429174, perimeter: 0.771238898
            with BuildLine():
                CenterArc((-0.5, 0), 0.15, 0, 180)
                Line((-0.35, 0), (-0.65, 0))
            make_face()
            # Profile area: 0.0353429174, perimeter: 0.771238898
            with BuildLine():
                Line((-0.35, 0), (-0.65, 0))
                CenterArc((-0.5, 0), 0.15, -180, 180)
            make_face()
        # Symmetric extrude, each_side=-6.3
        extrude(amount=-6.3, both=True, mode=Mode.SUBTRACT)
    return part.part


def model_145368_8e40c6f0_0000():
    """Model: Spur Gear (13 teeth)"""
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
        with BuildSketch(Plane.XY):
            # Profile area: 0.5724015003, perimeter: 7.2722843382
            with BuildLine():
                CenterArc((0, 0), 0.65742, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0497063642, perimeter: 0.8589985829
            with BuildLine():
                _nurbs_edge([(0.7564776991, -0.1033156777), (0.7569851414, -0.1033843343), (0.7580011896, -0.1035061771), (0.7595287529, -0.1036425314), (0.7615722187, -0.1037360162), (0.7641361671, -0.103731782), (0.7667076829, -0.1036396956), (0.769284665, -0.1034926145), (0.7718654077, -0.1033150099), (0.7744489756, -0.1031163366), (0.7770349659, -0.1028959762), (0.7796233219, -0.1026472183), (0.7822141347, -0.1023614379), (0.7848074335, -0.1020325641), (0.7874030322, -0.1016602721), (0.7900006213, -0.1012477209), (0.792599824, -0.1008000692), (0.7952002628, -0.1003227801), (0.7978016301, -0.0998198033), (0.80040373, -0.0992924958), (0.8030064368, -0.0987406405), (0.8056096683, -0.0981630846), (0.8082133557, -0.097558482), (0.8108174102, -0.0969261014), (0.8134217061, -0.0962662346), (0.8160260979, -0.0955797608), (0.8186304301, -0.0948678843), (0.82123455, -0.0941318253), (0.8238383203, -0.0933724794), (0.8264416249, -0.0925902703), (0.8290443614, -0.0917853394), (0.8316464358, -0.0909576602), (0.8342477577, -0.0901071738), (0.8368482331, -0.0892339382), (0.8394477628, -0.0883381888), (0.8420462451, -0.0874202587), (0.8446435775, -0.0864805314), (0.8472396593, -0.0855193848), (0.8498343937, -0.0845371296), (0.8524276888, -0.0835339856), (0.8550194561, -0.082510116), (0.8576096092, -0.0814656494), (0.8601980631, -0.0804007039), (0.8627847325, -0.0793154153), (0.8653695315, -0.0782099482), (0.8679523744, -0.0770844813), (0.8705331763, -0.0759391991), (0.8731118537, -0.0747742813), (0.8756883252, -0.0735898926), (0.8782625113, -0.072386177), (0.8808343342, -0.0711632655), (0.8834037162, -0.0699212795), (0.8859705795, -0.0686603365), (0.8885348452, -0.0673805549), (0.891096433, -0.0660820577), (0.8936552628, -0.0647649681), (0.8962112563, -0.0634294079), (0.8987643381, -0.0620754948), (0.9013144374, -0.0607033401), (0.9038614882, -0.0593130472), (0.9064054258, -0.0579047151), (0.9089461841, -0.0564784401), (0.9114836922, -0.0550343188), (0.9140178708, -0.0535724507), (0.9165486315, -0.0520929402), (0.9190758833, -0.0505958919), (0.9215995397, -0.0490814072), (0.9241195245, -0.0475495806), (0.9266357792, -0.0460004963), (0.9291482685, -0.0444342246), (0.9316569741, -0.0428508214), (0.9336609066, -0.0415704265), (0.9351621508, -0.0406024507), (0.9361622226, -0.0399537216), (0.9366620691, -0.039628504)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((0, 0), 0.9375, -2.4226375868, 4.8452751737)
                _nurbs_edge([(0.7564776991, 0.1033156777), (0.7569851414, 0.1033843343), (0.7580011896, 0.1035061771), (0.7595287529, 0.1036425314), (0.7615722187, 0.1037360162), (0.7641361671, 0.103731782), (0.7667076829, 0.1036396956), (0.769284665, 0.1034926145), (0.7718654077, 0.1033150099), (0.7744489756, 0.1031163366), (0.7770349659, 0.1028959762), (0.7796233219, 0.1026472183), (0.7822141347, 0.1023614379), (0.7848074335, 0.1020325641), (0.7874030322, 0.1016602721), (0.7900006213, 0.1012477209), (0.792599824, 0.1008000692), (0.7952002628, 0.1003227801), (0.7978016301, 0.0998198033), (0.80040373, 0.0992924958), (0.8030064368, 0.0987406405), (0.8056096683, 0.0981630846), (0.8082133557, 0.097558482), (0.8108174102, 0.0969261014), (0.8134217061, 0.0962662346), (0.8160260979, 0.0955797608), (0.8186304301, 0.0948678843), (0.82123455, 0.0941318253), (0.8238383203, 0.0933724794), (0.8264416249, 0.0925902703), (0.8290443614, 0.0917853394), (0.8316464358, 0.0909576602), (0.8342477577, 0.0901071738), (0.8368482331, 0.0892339382), (0.8394477628, 0.0883381888), (0.8420462451, 0.0874202587), (0.8446435775, 0.0864805314), (0.8472396593, 0.0855193848), (0.8498343937, 0.0845371296), (0.8524276888, 0.0835339856), (0.8550194561, 0.082510116), (0.8576096092, 0.0814656494), (0.8601980631, 0.0804007039), (0.8627847325, 0.0793154153), (0.8653695315, 0.0782099482), (0.8679523744, 0.0770844813), (0.8705331763, 0.0759391991), (0.8731118537, 0.0747742813), (0.8756883252, 0.0735898926), (0.8782625113, 0.072386177), (0.8808343342, 0.0711632655), (0.8834037162, 0.0699212795), (0.8859705795, 0.0686603365), (0.8885348452, 0.0673805549), (0.891096433, 0.0660820577), (0.8936552628, 0.0647649681), (0.8962112563, 0.0634294079), (0.8987643381, 0.0620754948), (0.9013144374, 0.0607033401), (0.9038614882, 0.0593130472), (0.9064054258, 0.0579047151), (0.9089461841, 0.0564784401), (0.9114836922, 0.0550343188), (0.9140178708, 0.0535724507), (0.9165486315, 0.0520929402), (0.9190758833, 0.0505958919), (0.9215995397, 0.0490814072), (0.9241195245, 0.0475495806), (0.9266357792, 0.0460004963), (0.9291482685, 0.0444342246), (0.9316569741, 0.0428508214), (0.9336609066, 0.0415704265), (0.9351621508, 0.0406024507), (0.9361622226, 0.0399537216), (0.9366620691, 0.039628504)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                Line((0.650382352, 0.0889610612), (0.7564776991, 0.1033156777))
                Line((0.650382352, -0.0889610612), (0.650382352, 0.0889610612))
                Line((0.650382352, -0.0889610612), (0.7564776991, -0.1033156777))
            make_face()
        # OneSide extrude, distance=1.2
        extrude(amount=1.2, mode=Mode.ADD)
    return part.part


def model_145368_8e40c6f0_0001():
    """Model: Spur Gear (35 teeth)"""
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
        with BuildSketch(Plane.XY):
            # Profile area: 5.9084908702, perimeter: 22.1948494428
            with BuildLine():
                CenterArc((0, 0), 2.03242, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.1
        extrude(amount=1.1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0551410046, perimeter: 0.9309605304
            with BuildLine():
                _nurbs_edge([(2.0519052203, -0.1228180327), (2.0526523355, -0.1228609005), (2.0541467789, -0.1229303201), (2.0563890837, -0.122985501), (2.0593800898, -0.1229658127), (2.0631208653, -0.1228127128), (2.0668635086, -0.1225655695), (2.0706078157, -0.122258616), (2.0743535319, -0.1219178258), (2.0781003564, -0.1215537815), (2.0818479685, -0.1211664925), (2.0855960541, -0.120749506), (2.0893443306, -0.1202941649), (2.0930925747, -0.1197940545), (2.0968406431, -0.1192486194), (2.1005884477, -0.1186610072), (2.1043359357, -0.1180365148), (2.1080830683, -0.1173808692), (2.1118297989, -0.1166984337), (2.115576056, -0.1159908879), (2.1193217545, -0.1152582108), (2.1230668021, -0.1144993502), (2.1268111081, -0.1137129809), (2.1305545914, -0.1128983016), (2.1342971863, -0.1120555761), (2.1380388378, -0.1111857066), (2.1417794973, -0.1102899604), (2.1455191195, -0.1093696525), (2.1492576577, -0.10842581), (2.1529950612, -0.1074589614), (2.1567312777, -0.1064693247), (2.1604662542, -0.1054569267), (2.1641999383, -0.1044217428), (2.1679322803, -0.1033638449), (2.1716632338, -0.1022834913), (2.1753927547, -0.1011810476), (2.1791208005, -0.1000569368), (2.1828473299, -0.098911582), (2.1865723019, -0.0977453452), (2.190295675, -0.0965584903), (2.1940174082, -0.0953512192), (2.1977374604, -0.0941236928), (2.2014557909, -0.0928760577), (2.2051723599, -0.0916084732), (2.2088871283, -0.0903211287), (2.2126000577, -0.0890142286), (2.2163111103, -0.0876879835), (2.2200202492, -0.0863425998), (2.223727438, -0.0849782682), (2.2274326411, -0.0835951575), (2.231135823, -0.0821934212), (2.2348369484, -0.0807732018), (2.2385359818, -0.0793346363), (2.2422328874, -0.077877862), (2.2459276289, -0.0764030199), (2.24962017, -0.0749102513), (2.2533104754, -0.0733996956), (2.256998511, -0.0718714872), (2.2606842448, -0.0703257529), (2.2643676473, -0.0687626105), (2.2680486894, -0.0671821719), (2.2717273416, -0.0655845461), (2.2754035719, -0.0639698418), (2.2790773448, -0.0623381711), (2.2827486198, -0.060689652), (2.2864173553, -0.0590244024), (2.2900835115, -0.0573425365), (2.2937470537, -0.0556441598), (2.2974079554, -0.0539293647), (2.3010662015, -0.0521982263), (2.3047217848, -0.050450803), (2.3076441202, -0.0490398694), (2.3098346734, -0.0479743705), (2.3112945098, -0.0472607952), (2.3120242949, -0.0469031969)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((0, 0), 2.3125, -1.162179249, 2.3243584981)
                _nurbs_edge([(2.0519052203, 0.1228180327), (2.0526523355, 0.1228609005), (2.0541467789, 0.1229303201), (2.0563890837, 0.122985501), (2.0593800898, 0.1229658127), (2.0631208653, 0.1228127128), (2.0668635086, 0.1225655695), (2.0706078157, 0.122258616), (2.0743535319, 0.1219178258), (2.0781003564, 0.1215537815), (2.0818479685, 0.1211664925), (2.0855960541, 0.120749506), (2.0893443306, 0.1202941649), (2.0930925747, 0.1197940545), (2.0968406431, 0.1192486194), (2.1005884477, 0.1186610072), (2.1043359357, 0.1180365148), (2.1080830683, 0.1173808692), (2.1118297989, 0.1166984337), (2.115576056, 0.1159908879), (2.1193217545, 0.1152582108), (2.1230668021, 0.1144993502), (2.1268111081, 0.1137129809), (2.1305545914, 0.1128983016), (2.1342971863, 0.1120555761), (2.1380388378, 0.1111857066), (2.1417794973, 0.1102899604), (2.1455191195, 0.1093696525), (2.1492576577, 0.10842581), (2.1529950612, 0.1074589614), (2.1567312777, 0.1064693247), (2.1604662542, 0.1054569267), (2.1641999383, 0.1044217428), (2.1679322803, 0.1033638449), (2.1716632338, 0.1022834913), (2.1753927547, 0.1011810476), (2.1791208005, 0.1000569368), (2.1828473299, 0.098911582), (2.1865723019, 0.0977453452), (2.190295675, 0.0965584903), (2.1940174082, 0.0953512192), (2.1977374604, 0.0941236928), (2.2014557909, 0.0928760577), (2.2051723599, 0.0916084732), (2.2088871283, 0.0903211287), (2.2126000577, 0.0890142286), (2.2163111103, 0.0876879835), (2.2200202492, 0.0863425998), (2.223727438, 0.0849782682), (2.2274326411, 0.0835951575), (2.231135823, 0.0821934212), (2.2348369484, 0.0807732018), (2.2385359818, 0.0793346363), (2.2422328874, 0.077877862), (2.2459276289, 0.0764030199), (2.24962017, 0.0749102513), (2.2533104754, 0.0733996956), (2.256998511, 0.0718714872), (2.2606842448, 0.0703257529), (2.2643676473, 0.0687626105), (2.2680486894, 0.0671821719), (2.2717273416, 0.0655845461), (2.2754035719, 0.0639698418), (2.2790773448, 0.0623381711), (2.2827486198, 0.060689652), (2.2864173553, 0.0590244024), (2.2900835115, 0.0573425365), (2.2937470537, 0.0556441598), (2.2974079554, 0.0539293647), (2.3010662015, 0.0521982263), (2.3047217848, 0.050450803), (2.3076441202, 0.0490398694), (2.3098346734, 0.0479743705), (2.3112945098, 0.0472607952), (2.3120242949, 0.0469031969)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                Line((2.0277907711, 0.1214343963), (2.0519052203, 0.1228180327))
                Line((2.0277907711, -0.1214343963), (2.0277907711, 0.1214343963))
                Line((2.0277907711, -0.1214343963), (2.0519052203, -0.1228180327))
            make_face()
        # OneSide extrude, distance=1.1
        extrude(amount=1.1, mode=Mode.ADD)
    return part.part


def model_145540_a4f54d5f_0002():
    """Model: Support v1"""
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
    return part.part


def model_145540_a4f54d5f_0012():
    """Model: Tires v1 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 324.2927866224, perimeter: 63.8371627209
            Circle(10.16)
        # OneSide extrude, distance=5.08
        extrude(amount=5.08)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 5.08), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 11.4009182797, perimeter: 11.9694680102
            Circle(1.905)
        # OneSide extrude, distance=-13.5
        extrude(amount=-13.5, mode=Mode.SUBTRACT)
    return part.part


def model_145619_8e3238eb_0003():
    """Model: cap"""
    with BuildPart() as part:
        # Sketch2 -> 押し出し1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY) as sk:
            # Profile area: 0.5261104328, perimeter: 2.7
            with BuildLine():
                Line((0, -0.45), (0.3897114317, -0.225))
                Line((0.3897114317, -0.225), (0.3897114317, 0.225))
                Line((0.3897114317, 0.225), (0, 0.45))
                Line((0, 0.45), (-0.3897114317, 0.225))
                Line((-0.3897114317, 0.225), (-0.3897114317, -0.225))
                Line((-0.3897114317, -0.225), (0, -0.45))
            make_face()
        # TwoSides offset extrude, full=3.75, trim=3.55
        extrude(amount=3.75)
        extrude(sk.sketch, amount=3.55, mode=Mode.SUBTRACT)
    return part.part


def model_145619_8e3238eb_0005():
    """Model: shaft"""
    with BuildPart() as part:
        # Sketch1 -> 押し出し1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY) as sk:
            # Profile area: 0.0697464985, perimeter: 0.9361946108
            Circle(0.149)
        # TwoSides extrude, along=2.8, against=-0.2
        extrude(amount=2.8)
        extrude(sk.sketch, amount=-0.2)

        # Sketch2 -> 押し出し2 (Cut)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0206591133, perimeter: 1.7215927742
            with BuildLine():
                CenterArc((0, 0), 0.149, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.03
        extrude(amount=-0.03, mode=Mode.SUBTRACT)
    return part.part


def model_145702_e28c737e_0044():
    """Model: ????????? v1 (6)"""
    with BuildPart() as part:
        # Sketch1 -> 押し出し1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 15.9043128088, perimeter: 14.1371669412
            Circle(2.25)
        # OneSide extrude, distance=3.5
        extrude(amount=3.5)

        # Sketch2 -> 押し出し2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3.5), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 8.8357293382, perimeter: 23.5619449019
            with BuildLine():
                CenterArc((0, 0), 2.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)
    return part.part


def model_146102_93e433ac_0004():
    """Model: nut v1 (1)"""
    with BuildPart() as part:
        # Sketch3 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.2170250337, perimeter: 5.5425625842
            with BuildLine():
                Line((0.8, -0.4618802154), (0.8, 0.4618802154))
                Line((0.8, 0.4618802154), (0, 0.9237604307))
                Line((0, 0.9237604307), (-0.8, 0.4618802154))
                Line((-0.8, 0.4618802154), (-0.8, -0.4618802154))
                Line((-0.8, -0.4618802154), (0, -0.9237604307))
                Line((0, -0.9237604307), (0.8, -0.4618802154))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.7837027764, perimeter: 3.1382000477
            Circle(0.49946005)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)
    return part.part


def model_146157_bfd67e48_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 47 constraints, 17 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.7660022139, perimeter: 6.6550913129
            with BuildLine():
                Line((3.7, 0), (0.6, 0))
                CenterArc((3.4500000004, -0.0000146274), 0.25, 0.0033523582, 89.9966476418)
                Line((0.54544231, 0.2499853726), (3.4500000004, 0.2499853726))
                CenterArc((0, 0), 0.6, 0, 24.6227818107)
            make_face()
            # Profile area: 0.734741745, perimeter: 6.6303062276
            with BuildLine():
                Line((3.4502742125, -0.2397176646), (0.54971475, -0.240444783))
                CenterArc((3.450211542, 0.0102823275), 0.25, -89.9856369733, 87.6284361921)
                Line((3.7, 0), (0.6, 0))
                CenterArc((0, 0), 0.6, -23.6245292149, 23.6245292149)
            make_face()
            # Profile area: 0.0391264201, perimeter: 0.8441623113
            with BuildLine():
                Line((0.6, 0), (0.45, 0))
                CenterArc((0, 0), 0.6, 0, 24.6227818107)
                Line((0.3741755116, 0.2499853726), (0.54544231, 0.2499853726))
                CenterArc((0, 0), 0.45, 0, 33.7467487366)
            make_face()
            # Profile area: 0.7660483569, perimeter: 6.6551287347
            with BuildLine():
                Line((0, -0.6), (0, -3.7))
                CenterArc((0, -3.45), 0.25, -90, 90)
                Line((0.25, -3.45), (0.25, -0.5454356057))
                CenterArc((0, 0), 0.6, -90, 24.6243183522)
            make_face()
            # Profile area: 0.7660483569, perimeter: 6.6551287347
            with BuildLine():
                Line((0, 0.6), (0, 3.7))
                CenterArc((0, 3.45), 0.25, 90, 90)
                Line((-0.25, 3.45), (-0.25, 0.5454356057))
                CenterArc((0, 0), 0.6, 90, 24.6243183522)
            make_face()
            # Profile area: 0.7660483569, perimeter: 6.6551287347
            with BuildLine():
                Line((-0.25, -3.45), (-0.25, -0.5454356057))
                CenterArc((0, -3.45), 0.25, 180, 90)
                Line((0, -0.6), (0, -3.7))
                CenterArc((0, 0), 0.6, -114.6243183522, 24.6243183522)
            make_face()
            # Profile area: 0.7660483569, perimeter: 6.6551287347
            with BuildLine():
                Line((0.25, 3.45), (0.25, 0.5454356057))
                CenterArc((0, 3.45), 0.25, 0, 90)
                Line((0, 0.6), (0, 3.7))
                CenterArc((0, 0), 0.6, 65.3756816478, 24.6243183522)
            make_face()
            # Profile area: 0.1237002107, perimeter: 1.9493361431
            with BuildLine():
                Line((0, -0.45), (0, -0.6))
                CenterArc((0, 0), 0.6, -90, 24.6243183522)
                CenterArc((0, 0), 0.6, -65.3756816478, 41.7511524329)
                CenterArc((0, 0), 0.6, -23.6245292149, 23.6245292149)
                Line((0.6, 0), (0.45, 0))
                CenterArc((0, 0), 0.45, -90, 90)
            make_face()
            # Profile area: 0.1237002107, perimeter: 1.9493361431
            with BuildLine():
                Line((-0.6, 0), (-0.45, 0))
                CenterArc((0, 0), 0.6, -180, 23.6245292149)
                CenterArc((0, 0), 0.6, -156.3754707851, 41.7511524329)
                CenterArc((0, 0), 0.6, -114.6243183522, 24.6243183522)
                Line((0, -0.45), (0, -0.6))
                CenterArc((0, 0), 0.45, -180, 90)
            make_face()
            # Profile area: 0.0391289253, perimeter: 0.8441990624
            with BuildLine():
                Line((0, 0.45), (0, 0.6))
                CenterArc((0, 0), 0.6, 90, 24.6243183522)
                Line((-0.25, 0.5454356057), (-0.25, 0.3741657387))
                CenterArc((0, 0), 0.45, 90, 33.7489885959)
            make_face()
            # Profile area: 0.734741745, perimeter: 6.6303062276
            with BuildLine():
                Line((-3.7, 0), (-0.6, 0))
                CenterArc((-3.450211542, 0.0102823275), 0.25, -177.6427992188, 87.6284361921)
                Line((-3.4502742125, -0.2397176646), (-0.54971475, -0.240444783))
                CenterArc((0, 0), 0.6, -180, 23.6245292149)
            make_face()
            # Profile area: 0.7660022139, perimeter: 6.6550913129
            with BuildLine():
                CenterArc((0, 0), 0.6, 155.3772181893, 24.6227818107)
                Line((-0.54544231, 0.2499853726), (-3.4500000004, 0.2499853726))
                CenterArc((-3.4500000004, -0.0000146274), 0.25, 90, 89.9966476418)
                Line((-3.7, 0), (-0.6, 0))
            make_face()
            # Profile area: 0.0454448654, perimeter: 0.9460481002
            with BuildLine():
                Line((0.3741755116, 0.2499853726), (0.54544231, 0.2499853726))
                CenterArc((0, 0), 0.6, 24.6227818107, 40.7528998371)
                Line((0.25, 0.5454356057), (0.25, 0.3741657387))
                CenterArc((0, 0), 0.45, 33.7467487366, 22.5042626675)
            make_face()
            # Profile area: 0.0391289253, perimeter: 0.8441990624
            with BuildLine():
                CenterArc((0, 0), 0.45, 56.2510114041, 33.7489885959)
                Line((0.25, 0.5454356057), (0.25, 0.3741657387))
                CenterArc((0, 0), 0.6, 65.3756816478, 24.6243183522)
                Line((0, 0.45), (0, 0.6))
            make_face()
            # Profile area: 0.0454448654, perimeter: 0.9460481002
            with BuildLine():
                Line((-0.25, 0.5454356057), (-0.25, 0.3741657387))
                CenterArc((0, 0), 0.6, 114.6243183522, 40.7528998371)
                Line((-0.3741755116, 0.2499853726), (-0.54544231, 0.2499853726))
                CenterArc((0, 0), 0.45, 123.7489885959, 22.5042626675)
            make_face()
            # Profile area: 0.0391264201, perimeter: 0.8441623113
            with BuildLine():
                CenterArc((0, 0), 0.45, 146.2532512634, 33.7467487366)
                Line((-0.3741755116, 0.2499853726), (-0.54544231, 0.2499853726))
                CenterArc((0, 0), 0.6, 155.3772181893, 24.6227818107)
                Line((-0.6, 0), (-0.45, 0))
            make_face()
        # OneSide extrude, distance=9
        extrude(amount=9)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 62.9668630161, perimeter: 31.1331831971
            with BuildLine():
                CenterArc((0, 0), 4.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.455, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.ADD)
    return part.part


def model_146171_ae42d34e_0000():
    """Model: Part"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 27 constraints, 13 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 132.704892898, perimeter: 73.401369997
            with BuildLine():
                CenterArc((22, -12), 3.5, 118.9227599883, 165.5060016584)
                CenterArc((16.9218838263, -2.8096389556), 7, -90, 28.9227599883)
                CenterArc((16.9218838263, 5.1903610444), 15, -162.9479257994, 72.9479257994)
                CenterArc((0, 0), 2.7, 0, 17.0520742006)
                Line((2.7, -5), (2.7, 0))
                CenterArc((0, -5), 2.7, -143.0318329044, 143.0318329044)
                CenterArc((16.9218838263, 7.736820001), 23.8796302132, -143.0318329044, 31.0928479204)
                CenterArc((16.9218838263, 7.736820001), 23.8796302132, -111.9389849839, 10.0443693234)
                CenterArc((16.9218838263, 7.736820001), 23.8796302132, -101.8946156606, 26.3233773074)
            make_face()
        # Symmetric extrude, full_length=True, total=0.8
        extrude(amount=0.4, both=True)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 27 constraints, 13 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 28.8633825049, perimeter: 32.9867228627
            with BuildLine():
                CenterArc((22, -12), 3.5, 118.9227599883, 165.5060016584)
                CenterArc((22, -12), 3.5, -75.5712383532, 194.4939983416)
            make_face()
            with BuildLine():
                CenterArc((22, -12), 1.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 27.8336269741, perimeter: 46.3893782902
            with BuildLine():
                CenterArc((0, 0), 2.7, 17.0520742006, 162.9479257994)
                Line((-2.7, 0), (-2.7, -5))
                CenterArc((0, -5), 2.7, 180, 36.9681670956)
                CenterArc((0, -5), 2.7, -143.0318329044, 143.0318329044)
                Line((2.7, -5), (2.7, 0))
                CenterArc((0, 0), 2.7, 0, 17.0520742006)
            make_face()
            with BuildLine():
                Line((1.5, -5), (1.5, 0))
                CenterArc((0, -5), 1.5, 180, 180)
                Line((-1.5, 0), (-1.5, -5))
                CenterArc((0, 0), 1.5, 0, 180)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=1.2
        extrude(amount=0.6, both=True, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 27 constraints, 13 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 14.7988126085, perimeter: 22.7090679626
            with BuildLine():
                Line((8, -18), (8, -14.4135011729))
                CenterArc((10, -18), 2, 180, 180)
                Line((12, -15.630075358), (12, -18))
                CenterArc((16.9218838263, 7.736820001), 23.8796302132, -111.9389849839, 10.0443693234)
            make_face()
            with BuildLine():
                CenterArc((10, -18), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=0.6
        extrude(amount=0.3, both=True, mode=Mode.ADD)
    return part.part


def model_146191_c64404bd_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch14 -> Extrude26 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5183111661, perimeter: 2.6092934421
            with BuildLine():
                CenterArc((0, 0), 0.425, 124.56032178, 110.87935644)
                Line((-0.241091269, -0.35), (0.241091269, -0.35))
                CenterArc((0, 0), 0.425, -55.43967822, 110.87935644)
                Line((0.241091269, 0.35), (-0.241091269, 0.35))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch14 -> Extrude29 (Join)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0245695035, perimeter: 0.9948952328
            with BuildLine():
                CenterArc((0, 0), 0.425, -124.56032178, 69.12064356)
                Line((-0.241091269, -0.35), (0.241091269, -0.35))
            make_face()
            # Profile area: 0.0245695035, perimeter: 0.9948952328
            with BuildLine():
                Line((0.241091269, 0.35), (-0.241091269, 0.35))
                CenterArc((0, 0), 0.425, 55.43967822, 69.12064356)
            make_face()
        # OneSide extrude, distance=0.25
        extrude(amount=0.25, mode=Mode.ADD)

        # Sketch14 -> Extrude27 (Join)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.8483825753, perimeter: 13.8575197971
            with BuildLine():
                CenterArc((0, 0), 1.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.425, 55.43967822, 69.12064356)
                Line((0.9000000134, 0.35), (0.241091269, 0.35))
                Line((0.9000000134, -0.35), (0.9000000134, 0.35))
                Line((0.241091269, -0.35), (0.9000000134, -0.35))
                CenterArc((0, 0), 0.425, -124.56032178, 69.12064356)
                Line((-0.9000000134, -0.35), (-0.241091269, -0.35))
                Line((-0.9000000134, 0.35), (-0.9000000134, -0.35))
                Line((-0.241091269, 0.35), (-0.9000000134, 0.35))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0245695035, perimeter: 0.9948952328
            with BuildLine():
                Line((0.241091269, 0.35), (-0.241091269, 0.35))
                CenterArc((0, 0), 0.425, 55.43967822, 69.12064356)
            make_face()
            # Profile area: 0.5183111661, perimeter: 2.6092934421
            with BuildLine():
                CenterArc((0, 0), 0.425, 124.56032178, 110.87935644)
                Line((-0.241091269, -0.35), (0.241091269, -0.35))
                CenterArc((0, 0), 0.425, -55.43967822, 110.87935644)
                Line((0.241091269, 0.35), (-0.241091269, 0.35))
            make_face()
            # Profile area: 0.3708444263, perimeter: 2.8402816718
            with BuildLine():
                CenterArc((0, 0), 0.425, 124.56032178, 110.87935644)
                Line((-0.241091269, 0.35), (-0.9000000134, 0.35))
                Line((-0.9000000134, 0.35), (-0.9000000134, -0.35))
                Line((-0.9000000134, -0.35), (-0.241091269, -0.35))
            make_face()
            # Profile area: 0.0245695035, perimeter: 0.9948952328
            with BuildLine():
                CenterArc((0, 0), 0.425, -124.56032178, 69.12064356)
                Line((-0.241091269, -0.35), (0.241091269, -0.35))
            make_face()
            # Profile area: 0.3708444263, perimeter: 2.8402816718
            with BuildLine():
                Line((0.241091269, -0.35), (0.9000000134, -0.35))
                Line((0.9000000134, -0.35), (0.9000000134, 0.35))
                Line((0.9000000134, 0.35), (0.241091269, 0.35))
                CenterArc((0, 0), 0.425, -55.43967822, 110.87935644)
            make_face()
        # OneSide extrude, distance=-2.4
        extrude(amount=-2.4, mode=Mode.ADD)
    return part.part


def model_146226_5cf38887_0001():
    """Model: Spur Gear (16 teeth)"""
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
        with BuildSketch(Plane.XY):
            # Profile area: 12.8499760263, perimeter: 14.1994961394
            with BuildLine():
                CenterArc((0, 0), 2.03492, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.225, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.45
        extrude(amount=0.45)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2985765791, perimeter: 2.1238872321
            with BuildLine():
                _nurbs_edge([(2.1573025629, -0.2779819565), (2.1588603214, -0.2781812621), (2.161978725, -0.2785300799), (2.1666649901, -0.2789039293), (2.1729299203, -0.2791185889), (2.1807843353, -0.2790003745), (2.1886563243, -0.2786049418), (2.1965400689, -0.2780394835), (2.2044308948, -0.2773812513), (2.2123262058, -0.276657852), (2.2202247932, -0.2758649545), (2.2281263528, -0.2749793189), (2.2360309526, -0.2739727406), (2.2439384498, -0.2728276701), (2.2518481747, -0.2715451741), (2.2597591842, -0.2701368995), (2.2676703986, -0.2686202868), (2.2755807711, -0.2670129377), (2.2834894764, -0.2653262661), (2.2913959663, -0.2635635475), (2.2992998616, -0.2617233536), (2.3072008839, -0.2598016525), (2.3150987784, -0.2577942454), (2.3229932242, -0.255699562), (2.3308838182, -0.2535191345), (2.3387701171, -0.2512562047), (2.3466516629, -0.2489148444), (2.3545280132, -0.2464989498), (2.3623987759, -0.2440110801), (2.3702636102, -0.2414523898), (2.3781222084, -0.2388232066), (2.3859742831, -0.2361234244), (2.3938195531, -0.2333529373), (2.4016577273, -0.2305121446), (2.4094885042, -0.2276019577), (2.4173115789, -0.2246235652), (2.4251266481, -0.2215782696), (2.4329334148, -0.2184673096), (2.4407315955, -0.2152916525), (2.4485209192, -0.2120519994), (2.4563011235, -0.2087488855), (2.464071952, -0.2053827542), (2.4718331515, -0.2019540353), (2.4795844686, -0.1984632382), (2.4873256499, -0.1949109533), (2.4950564436, -0.1912978095), (2.5027766014, -0.1876244449), (2.5104858798, -0.1838914747), (2.5181840423, -0.1800994546), (2.5258708583, -0.1762488791), (2.5335461008, -0.1723402021), (2.541209544, -0.1683738515), (2.5488609612, -0.1643502449), (2.5565001222, -0.1602698091), (2.5641267945, -0.1561329826), (2.5717407475, -0.1519402037), (2.579341757, -0.1476919029), (2.5869296081, -0.1433884949), (2.5945041009, -0.1390303689), (2.602065049, -0.1346178887), (2.6096122683, -0.1301514035), (2.6171455692, -0.1256312571), (2.6246647474, -0.1210577973), (2.6321695735, -0.1164313881), (2.6396597924, -0.1117524121), (2.6471351455, -0.1070212518), (2.6545953881, -0.1022382758), (2.662040309, -0.0974038236), (2.6694697504, -0.0925181905), (2.6768836224, -0.0875816153), (2.6842818829, -0.0825942823), (2.690187995, -0.0785639136), (2.6946105531, -0.0755183892), (2.6975558036, -0.0734779328), (2.6990276485, -0.0724551779)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((0, 0), 2.7, -1.537731228, 3.075462456)
                _nurbs_edge([(2.1573025629, 0.2779819565), (2.1588603214, 0.2781812621), (2.161978725, 0.2785300799), (2.1666649901, 0.2789039293), (2.1729299203, 0.2791185889), (2.1807843353, 0.2790003745), (2.1886563243, 0.2786049418), (2.1965400689, 0.2780394835), (2.2044308948, 0.2773812513), (2.2123262058, 0.276657852), (2.2202247932, 0.2758649545), (2.2281263528, 0.2749793189), (2.2360309526, 0.2739727406), (2.2439384498, 0.2728276701), (2.2518481747, 0.2715451741), (2.2597591842, 0.2701368995), (2.2676703986, 0.2686202868), (2.2755807711, 0.2670129377), (2.2834894764, 0.2653262661), (2.2913959663, 0.2635635475), (2.2992998616, 0.2617233536), (2.3072008839, 0.2598016525), (2.3150987784, 0.2577942454), (2.3229932242, 0.255699562), (2.3308838182, 0.2535191345), (2.3387701171, 0.2512562047), (2.3466516629, 0.2489148444), (2.3545280132, 0.2464989498), (2.3623987759, 0.2440110801), (2.3702636102, 0.2414523898), (2.3781222084, 0.2388232066), (2.3859742831, 0.2361234244), (2.3938195531, 0.2333529373), (2.4016577273, 0.2305121446), (2.4094885042, 0.2276019577), (2.4173115789, 0.2246235652), (2.4251266481, 0.2215782696), (2.4329334148, 0.2184673096), (2.4407315955, 0.2152916525), (2.4485209192, 0.2120519994), (2.4563011235, 0.2087488855), (2.464071952, 0.2053827542), (2.4718331515, 0.2019540353), (2.4795844686, 0.1984632382), (2.4873256499, 0.1949109533), (2.4950564436, 0.1912978095), (2.5027766014, 0.1876244449), (2.5104858798, 0.1838914747), (2.5181840423, 0.1800994546), (2.5258708583, 0.1762488791), (2.5335461008, 0.1723402021), (2.541209544, 0.1683738515), (2.5488609612, 0.1643502449), (2.5565001222, 0.1602698091), (2.5641267945, 0.1561329826), (2.5717407475, 0.1519402037), (2.579341757, 0.1476919029), (2.5869296081, 0.1433884949), (2.5945041009, 0.1390303689), (2.602065049, 0.1346178887), (2.6096122683, 0.1301514035), (2.6171455692, 0.1256312571), (2.6246647474, 0.1210577973), (2.6321695735, 0.1164313881), (2.6396597924, 0.1117524121), (2.6471351455, 0.1070212518), (2.6545953881, 0.1022382758), (2.662040309, 0.0974038236), (2.6694697504, 0.0925181905), (2.6768836224, 0.0875816153), (2.6842818829, 0.0825942823), (2.690187995, 0.0785639136), (2.6946105531, 0.0755183892), (2.6975558036, 0.0734779328), (2.6990276485, 0.0724551779)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                Line((2.0172418665, 0.2600620576), (2.1573025629, 0.2779819565))
                Line((2.0172418665, -0.2600620576), (2.0172418665, 0.2600620576))
                Line((2.0172418665, -0.2600620576), (2.1573025629, -0.2779819565))
            make_face()
        # OneSide extrude, distance=0.45
        extrude(amount=0.45, mode=Mode.ADD)
    return part.part


def model_146291_6b0c8db3_0003():
    """Model: кровать v4"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0004980644, perimeter: 0.1979714127
            with BuildLine():
                Line((-1.4300455875, 0.2332516025), (-1.4359693875, 0.2332516025))
                Line((-1.4300455875, 0.2532446611), (-1.4300455875, 0.2332516025))
                Line((-1.4037103707, 0.2936661567), (-1.4300455875, 0.2532446611))
                Line((-1.3968739164, 0.2892121031), (-1.4037103707, 0.2936661567))
                Line((-1.3968739164, 0.3132516025), (-1.3968739164, 0.2892121031))
                Line((-1.4359693875, 0.2532446005), (-1.3968739164, 0.3132516025))
                Line((-1.4359693875, 0.2332516025), (-1.4359693875, 0.2532446005))
            make_face()
        # OneSide extrude, distance=0.005
        extrude(amount=0.005)
    return part.part


def model_146544_67c41937_0000():
    """Model: Base"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 142.9314165294, perimeter: 59.4247779608
            with BuildLine():
                Line((-7.5, 5), (7.5, 5))
                Line((-7.5, -5), (-7.5, 5))
                Line((7.5, -5), (-7.5, -5))
                Line((7.5, 5), (7.5, -5))
            make_face()
            with BuildLine():
                CenterArc((-3.75, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-3
        extrude(amount=-3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 25, perimeter: 20
            with BuildLine():
                Line((-7.5, -2.5), (-2.5, -2.5))
                Line((-2.5, -2.5), (-2.5, 2.5))
                Line((-2.5, 2.5), (-7.5, 2.5))
                Line((-7.5, 2.5), (-7.5, -2.5))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.ADD)
    return part.part


def model_146545_f266050f_0000():
    """Model: Shaft"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 11 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.2964600329, perimeter: 55.3097335529
            with BuildLine():
                CenterArc((0, 5.5), 1.05, 0, 180)
                Line((-1.05, 5.5), (-1.05, -5.5))
                CenterArc((0, -5.5), 1.05, 180, 180)
                Line((1.05, -5.5), (1.05, 5.5))
            make_face()
            with BuildLine():
                Line((-0.75, 5.5), (-0.75, -5.5))
                CenterArc((0, 5.5), 0.75, 0, 180)
                Line((0.75, -5.5), (0.75, 5.5))
                CenterArc((0, -5.5), 0.75, 180, 180)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=1.5
        extrude(amount=0.75, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1.05, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with BuildLine():
                CenterArc((0, 0), 0.75, 0, 180)
                CenterArc((0, 0), 0.75, -180, 180)
            make_face()
        # OneSide extrude, distance=9.95
        extrude(amount=9.95, mode=Mode.ADD)
    return part.part


def model_146617_2c247f85_0024():
    """Model: крепление для колёс верхняя часть"""
    with BuildPart() as part:
        # Sketch3 -> Extrude4 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 15.9043128088, perimeter: 14.1371669412
            with Locations((0, 15)):
                Circle(2.25)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)

        # Sketch4 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((0, -15)):
                Circle(0.4)
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)
    return part.part


def model_146617_2c247f85_0026():
    """Model: подкладка"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.9428126205, perimeter: 11.177882999
            with Locations((-7.5, 15)):
                Circle(1.7790153326)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((7.5, -15)):
                Circle(0.4)
        # OneSide extrude, distance=-1.8
        extrude(amount=-1.8, mode=Mode.SUBTRACT)
    return part.part


def model_146618_b2f1a4f4_0000():
    """Model: Boitier v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 10.6, perimeter: 14.24
            with BuildLine():
                Line((0, 2.12), (0, 0))
                Line((0, 0), (5, 0))
                Line((5, 0), (5, 2.12))
                Line((5, 2.12), (0, 2.12))
            make_face()
        # OneSide extrude, distance=3.8
        extrude(amount=3.8)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 19 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3.8), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.2134476939, perimeter: 2.0532517942
            with BuildLine():
                Line((-1.5684712014, -0.835), (-1.8836775678, -0.835))
                CenterArc((-1.0122563149, -1.06), 0.6, 112.9312370865, 45.0444500765)
                Line((-1.2460319829, -0.1908918726), (-1.2460319829, -0.5074161267))
                CenterArc((-1.0122563149, -1.06), 0.9, 105.0552725903, 60.4672152238)
            make_face()
            # Profile area: 0.2134476939, perimeter: 2.0532517942
            with BuildLine():
                Line((-1.2460319829, -1.6125838733), (-1.2460319829, -1.9291081274))
                CenterArc((-1.0122563149, -1.06), 0.6, -157.975687163, 45.0444500765)
                Line((-1.8836775678, -1.285), (-1.5684712014, -1.285))
                CenterArc((-1.0122563149, -1.06), 0.9, -165.5224878141, 60.4672152238)
            make_face()
            # Profile area: 0.2134476939, perimeter: 2.0532517942
            with BuildLine():
                CenterArc((-1.0122563149, -1.06), 0.9, 14.4775121859, 60.4672152238)
                Line((-0.7784806468, -0.5074161267), (-0.7784806468, -0.1908918726))
                CenterArc((-1.0122563149, -1.06), 0.6, 22.024312837, 45.0444500765)
                Line((-0.140835062, -0.835), (-0.4560414283, -0.835))
            make_face()
            # Profile area: 0.2134476939, perimeter: 2.0532517942
            with BuildLine():
                Line((-0.4560414283, -1.285), (-0.140835062, -1.285))
                CenterArc((-1.0122563149, -1.06), 0.6, -67.0687629135, 45.0444500765)
                Line((-0.7784806468, -1.9291081274), (-0.7784806468, -1.6125838733))
                CenterArc((-1.0122563149, -1.06), 0.9, -74.9447274097, 60.4672152238)
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)
    return part.part


def model_146618_b2f1a4f4_0001():
    """Model: dht22"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 47 constraints, 13 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.8004579571, perimeter: 6.8004579571
            with BuildLine():
                Line((0.102, -1), (0.152, -1))
                Line((0.152, -1), (0.356, -1))
                Line((0.356, -1), (0.406, -1))
                Line((0.406, -1), (0.7001144893, -1))
                Line((0.7001144893, -1), (0.7001144893, 1))
                Line((0.7001144893, 1), (0, 1))
                Line((0, 1), (-0.7001144893, 1))
                Line((-0.7001144893, -1), (-0.7001144893, 1))
                Line((-0.7001144893, -1), (-0.406, -1))
                Line((-0.406, -1), (-0.356, -1))
                Line((-0.356, -1), (-0.152, -1))
                Line((-0.152, -1), (-0.102, -1))
                Line((-0.102, -1), (0.102, -1))
            make_face()
        # OneSide extrude, distance=0.77
        extrude(amount=0.77)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 47 constraints, 13 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.244320813, perimeter: 2.3817916223
            with BuildLine():
                Line((0, 1.51), (0, 1.39))
                CenterArc((0, 1.235), 0.155, -90, 180)
                Line((0, 1.08), (0, 1))
                Line((0.7001144893, 1), (0, 1))
                Line((0.7001144893, 1), (0.406, 1.51))
                Line((0, 1.51), (0.406, 1.51))
            make_face()
            # Profile area: 0.244320813, perimeter: 2.3817916223
            with BuildLine():
                Line((0, 1), (-0.7001144893, 1))
                Line((0, 1.08), (0, 1))
                CenterArc((0, 1.235), 0.155, 90, 180)
                Line((0, 1.51), (0, 1.39))
                Line((-0.406, 1.51), (0, 1.51))
                Line((-0.7001144893, 1), (-0.406, 1.51))
            make_face()
        # OneSide extrude, distance=0.13
        extrude(amount=0.13, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 47 constraints, 13 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0425, perimeter: 1.8
            with BuildLine():
                Line((-0.356, -1), (-0.356, -1.85))
                Line((-0.406, -1), (-0.356, -1))
                Line((-0.406, -1), (-0.406, -1.85))
                Line((-0.406, -1.85), (-0.356, -1.85))
            make_face()
            # Profile area: 0.0425, perimeter: 1.8
            with BuildLine():
                Line((0.102, -1.85), (0.152, -1.85))
                Line((0.152, -1), (0.152, -1.85))
                Line((0.102, -1), (0.152, -1))
                Line((0.102, -1), (0.102, -1.85))
            make_face()
            # Profile area: 0.0425, perimeter: 1.8
            with BuildLine():
                Line((0.356, -1), (0.406, -1))
                Line((0.356, -1), (0.356, -1.85))
                Line((0.356, -1.85), (0.406, -1.85))
                Line((0.406, -1.85), (0.406, -1))
            make_face()
            # Profile area: 0.0425, perimeter: 1.8
            with BuildLine():
                Line((-0.152, -1), (-0.102, -1))
                Line((-0.152, -1), (-0.152, -1.85))
                Line((-0.152, -1.85), (-0.102, -1.85))
                Line((-0.102, -1), (-0.102, -1.85))
            make_face()
        # OneSide extrude, distance=0.23
        extrude(amount=0.23, mode=Mode.ADD)

        # Sketch1 -> Extrude4 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 47 constraints, 13 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0425, perimeter: 1.8
            with BuildLine():
                Line((-0.356, -1), (-0.356, -1.85))
                Line((-0.406, -1), (-0.356, -1))
                Line((-0.406, -1), (-0.406, -1.85))
                Line((-0.406, -1.85), (-0.356, -1.85))
            make_face()
            # Profile area: 0.0425, perimeter: 1.8
            with BuildLine():
                Line((0.102, -1.85), (0.152, -1.85))
                Line((0.152, -1), (0.152, -1.85))
                Line((0.102, -1), (0.152, -1))
                Line((0.102, -1), (0.102, -1.85))
            make_face()
            # Profile area: 0.0425, perimeter: 1.8
            with BuildLine():
                Line((0.356, -1), (0.406, -1))
                Line((0.356, -1), (0.356, -1.85))
                Line((0.356, -1.85), (0.406, -1.85))
                Line((0.406, -1.85), (0.406, -1))
            make_face()
            # Profile area: 0.0425, perimeter: 1.8
            with BuildLine():
                Line((-0.152, -1), (-0.102, -1))
                Line((-0.152, -1), (-0.152, -1.85))
                Line((-0.152, -1.85), (-0.102, -1.85))
                Line((-0.102, -1), (-0.102, -1.85))
            make_face()
        # OneSide extrude, distance=0.21
        extrude(amount=0.21, mode=Mode.SUBTRACT)
    return part.part


def model_146640_89ef3723_0000():
    """Model: Spur Gear (80 teeth) (1)"""
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
        with BuildSketch(Plane.XY):
            # Profile area: 89.2465124065, perimeter: 33.4888750324
            Circle(5.32992)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.2238682547, perimeter: 1.9682957554
            with BuildLine():
                Line((4.9785599691, 0.2471906769), (4.9785599691, -0.2471906769))
                _nurbs_edge([(4.9785599691, -0.2471906769), (4.980472867, -0.2471933563), (4.9842987639, -0.2471816655), (4.990037912, -0.2471129799), (4.9976907153, -0.2469190674), (5.0072576892, -0.2465067554), (5.0168255099, -0.2459267763), (5.0263939312, -0.2451838667), (5.035962538, -0.2442862227), (5.0455307154, -0.2432461679), (5.0550977404, -0.2420781715), (5.0646628662, -0.2407970591), (5.0742254045, -0.239416236), (5.0837848181, -0.2379457084), (5.0933407821, -0.2363907825), (5.1028931123, -0.2347536445), (5.1124417129, -0.2330345486), (5.1219865187, -0.2312330911), (5.1315274332, -0.2293496007), (5.141064291, -0.2273859885), (5.1505968882, -0.2253450415), (5.1601250024, -0.2232299924), (5.1696484143, -0.2210440136), (5.1791669329, -0.2187896679), (5.188680407, -0.2164686314), (5.1981887113, -0.214082019), (5.2076917369, -0.2116305876), (5.217189381, -0.2091149729), (5.2266815349, -0.2065359497), (5.2361680794, -0.2038945524), (5.2456488897, -0.2011919432), (5.2551238393, -0.1984293356), (5.2645928038, -0.1956079024), (5.2740556656, -0.1927286755), (5.2835123154, -0.1897925056), (5.2929626498, -0.1868001224), (5.3024065694, -0.1837521724), (5.3118439769, -0.1806492629), (5.3212747753, -0.1774920106), (5.3306988667, -0.1742810629), (5.3401161531, -0.1710170744), (5.3495265372, -0.1677006932), (5.3589299225, -0.1643325463), (5.3683262143, -0.1609132217), (5.3777153199, -0.1574432625), (5.3870971482, -0.1539231772), (5.3964716102, -0.1503534465), (5.4058386182, -0.1467345319), (5.4151980862, -0.1430668842), (5.4245499299, -0.1393509493), (5.4338940652, -0.1355871643), (5.4432304086, -0.1317759572), (5.4525588757, -0.1279177454), (5.4618793812, -0.1240129346), (5.4711918386, -0.120061918), (5.4804961619, -0.1160650751), (5.4897922673, -0.1120227708), (5.4990800744, -0.1079353546), (5.5083595084, -0.1038031603), (5.5176305001, -0.0996265061), (5.5268929819, -0.0954057017), (5.5361468838, -0.091141053), (5.5453921302, -0.0868328683), (5.5546286355, -0.0824814649), (5.5638563023, -0.0780871725), (5.5730750308, -0.073650319), (5.5822847259, -0.0691712183), (5.5914853059, -0.0646501585), (5.6006767105, -0.0600873893), (5.6098589079, -0.0554831118), (5.6190318862, -0.0508374796), (5.6263628946, -0.0470879764), (5.6318570057, -0.0442573166), (5.6355179047, -0.042361976), (5.6373478938, -0.0414122473)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((0, 0), 5.6375, -0.4208901691, 0.8417803382)
                _nurbs_edge([(4.9785599691, 0.2471906769), (4.980472867, 0.2471933563), (4.9842987639, 0.2471816655), (4.990037912, 0.2471129799), (4.9976907153, 0.2469190674), (5.0072576892, 0.2465067554), (5.0168255099, 0.2459267763), (5.0263939312, 0.2451838667), (5.035962538, 0.2442862227), (5.0455307154, 0.2432461679), (5.0550977404, 0.2420781715), (5.0646628662, 0.2407970591), (5.0742254045, 0.239416236), (5.0837848181, 0.2379457084), (5.0933407821, 0.2363907825), (5.1028931123, 0.2347536445), (5.1124417129, 0.2330345486), (5.1219865187, 0.2312330911), (5.1315274332, 0.2293496007), (5.141064291, 0.2273859885), (5.1505968882, 0.2253450415), (5.1601250024, 0.2232299924), (5.1696484143, 0.2210440136), (5.1791669329, 0.2187896679), (5.188680407, 0.2164686314), (5.1981887113, 0.214082019), (5.2076917369, 0.2116305876), (5.217189381, 0.2091149729), (5.2266815349, 0.2065359497), (5.2361680794, 0.2038945524), (5.2456488897, 0.2011919432), (5.2551238393, 0.1984293356), (5.2645928038, 0.1956079024), (5.2740556656, 0.1927286755), (5.2835123154, 0.1897925056), (5.2929626498, 0.1868001224), (5.3024065694, 0.1837521724), (5.3118439769, 0.1806492629), (5.3212747753, 0.1774920106), (5.3306988667, 0.1742810629), (5.3401161531, 0.1710170744), (5.3495265372, 0.1677006932), (5.3589299225, 0.1643325463), (5.3683262143, 0.1609132217), (5.3777153199, 0.1574432625), (5.3870971482, 0.1539231772), (5.3964716102, 0.1503534465), (5.4058386182, 0.1467345319), (5.4151980862, 0.1430668842), (5.4245499299, 0.1393509493), (5.4338940652, 0.1355871643), (5.4432304086, 0.1317759572), (5.4525588757, 0.1279177454), (5.4618793812, 0.1240129346), (5.4711918386, 0.120061918), (5.4804961619, 0.1160650751), (5.4897922673, 0.1120227708), (5.4990800744, 0.1079353546), (5.5083595084, 0.1038031603), (5.5176305001, 0.0996265061), (5.5268929819, 0.0954057017), (5.5361468838, 0.091141053), (5.5453921302, 0.0868328683), (5.5546286355, 0.0824814649), (5.5638563023, 0.0780871725), (5.5730750308, 0.073650319), (5.5822847259, 0.0691712183), (5.5914853059, 0.0646501585), (5.6006767105, 0.0600873893), (5.6098589079, 0.0554831118), (5.6190318862, 0.0508374796), (5.6263628946, 0.0470879764), (5.6318570057, 0.0442573166), (5.6355179047, 0.042361976), (5.6373478938, 0.0414122473)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


def model_146640_89ef3723_0001():
    """Model: Spur Gear (12 teeth)"""
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
        with BuildSketch(Plane.XY):
            # Profile area: 1.3474925694, perimeter: 4.1149837214
            Circle(0.65492)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0607932791, perimeter: 0.9491876301
            with BuildLine():
                _nurbs_edge([(0.7380491942, -0.1197687159), (0.7386802476, -0.1198700297), (0.739944339, -0.1200508592), (0.7418464297, -0.1202567102), (0.744393975, -0.1204068192), (0.747594608, -0.1204244179), (0.7508077692, -0.1203191712), (0.7540297187, -0.1201375008), (0.7572574845, -0.1199133081), (0.7604895044, -0.1196590839), (0.763725163, -0.1193733215), (0.766964451, -0.1190461494), (0.7702075963, -0.1186653182), (0.773454664, -0.1182227895), (0.7767053118, -0.117718634), (0.7799589725, -0.1171576372), (0.7832149592, -0.1165472246), (0.7864725919, -0.11589504), (0.7897313361, -0.1152062613), (0.792990861, -0.1144824728), (0.7962509589, -0.1137231518), (0.7995114965, -0.1129265697), (0.8027723571, -0.1120908442), (0.8060333768, -0.111215129), (0.8092943239, -0.1102999706), (0.8125549319, -0.10934669), (0.8158149182, -0.1083570094), (0.8190740071, -0.1073326161), (0.8223319554, -0.1062746642), (0.8255885576, -0.1051836736), (0.8288436317, -0.1040597918), (0.8320970097, -0.1029029592), (0.835348528, -0.1017130982), (0.8385980148, -0.1004903312), (0.8418452886, -0.0992350157), (0.8450901637, -0.0979476367), (0.8483324533, -0.0966287382), (0.8515719746, -0.0952788449), (0.8548085523, -0.0938983732), (0.85804202, -0.0924876185), (0.8612722171, -0.0910468027), (0.8644989866, -0.0895761041), (0.8677221735, -0.0880756925), (0.8709416218, -0.086545769), (0.8741571748, -0.0849865732), (0.8773686762, -0.0833983628), (0.8805759713, -0.0817814018), (0.8837789079, -0.080135946), (0.886977338, -0.0784622277), (0.8901711172, -0.0767604522), (0.8933601036, -0.075030807), (0.8965441555, -0.0732734682), (0.8997231311, -0.0714886074), (0.9028968859, -0.0696763997), (0.9060652736, -0.0678370261), (0.9092281488, -0.0659706683), (0.9123853692, -0.0640775057), (0.9155367984, -0.0621577115), (0.9186823087, -0.0602114492), (0.9218217809, -0.0582388717), (0.9249550975, -0.0562401259), (0.9280821377, -0.0542153561), (0.931202772, -0.0521647083), (0.9343168556, -0.0500883347), (0.937424227, -0.0479863954), (0.9405247218, -0.0458590512), (0.9436181838, -0.0437064579), (0.9467044767, -0.0415287601), (0.949783497, -0.0393260858), (0.9528551827, -0.0370985408), (0.9559195024, -0.0348462086), (0.9583650572, -0.0330245613), (0.9601959049, -0.0316472152), (0.9614149955, -0.030724048), (0.9620241722, -0.0302612303)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((0, 0), 0.9625, -1.8016899238, 3.6033798476)
                _nurbs_edge([(0.7380491942, 0.1197687159), (0.7386802476, 0.1198700297), (0.739944339, 0.1200508592), (0.7418464297, 0.1202567102), (0.744393975, 0.1204068192), (0.747594608, 0.1204244179), (0.7508077692, 0.1203191712), (0.7540297187, 0.1201375008), (0.7572574845, 0.1199133081), (0.7604895044, 0.1196590839), (0.763725163, 0.1193733215), (0.766964451, 0.1190461494), (0.7702075963, 0.1186653182), (0.773454664, 0.1182227895), (0.7767053118, 0.117718634), (0.7799589725, 0.1171576372), (0.7832149592, 0.1165472246), (0.7864725919, 0.11589504), (0.7897313361, 0.1152062613), (0.792990861, 0.1144824728), (0.7962509589, 0.1137231518), (0.7995114965, 0.1129265697), (0.8027723571, 0.1120908442), (0.8060333768, 0.111215129), (0.8092943239, 0.1102999706), (0.8125549319, 0.10934669), (0.8158149182, 0.1083570094), (0.8190740071, 0.1073326161), (0.8223319554, 0.1062746642), (0.8255885576, 0.1051836736), (0.8288436317, 0.1040597918), (0.8320970097, 0.1029029592), (0.835348528, 0.1017130982), (0.8385980148, 0.1004903312), (0.8418452886, 0.0992350157), (0.8450901637, 0.0979476367), (0.8483324533, 0.0966287382), (0.8515719746, 0.0952788449), (0.8548085523, 0.0938983732), (0.85804202, 0.0924876185), (0.8612722171, 0.0910468027), (0.8644989866, 0.0895761041), (0.8677221735, 0.0880756925), (0.8709416218, 0.086545769), (0.8741571748, 0.0849865732), (0.8773686762, 0.0833983628), (0.8805759713, 0.0817814018), (0.8837789079, 0.080135946), (0.886977338, 0.0784622277), (0.8901711172, 0.0767604522), (0.8933601036, 0.075030807), (0.8965441555, 0.0732734682), (0.8997231311, 0.0714886074), (0.9028968859, 0.0696763997), (0.9060652736, 0.0678370261), (0.9092281488, 0.0659706683), (0.9123853692, 0.0640775057), (0.9155367984, 0.0621577115), (0.9186823087, 0.0602114492), (0.9218217809, 0.0582388717), (0.9249550975, 0.0562401259), (0.9280821377, 0.0542153561), (0.931202772, 0.0521647083), (0.9343168556, 0.0500883347), (0.937424227, 0.0479863954), (0.9405247218, 0.0458590512), (0.9436181838, 0.0437064579), (0.9467044767, 0.0415287601), (0.949783497, 0.0393260858), (0.9528551827, 0.0370985408), (0.9559195024, 0.0348462086), (0.9583650572, 0.0330245613), (0.9601959049, 0.0316472152), (0.9614149955, 0.030724048), (0.9620241722, 0.0302612303)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                Line((0.6454762552, 0.1049064006), (0.7380491942, 0.1197687159))
                Line((0.6454762552, -0.1049064006), (0.6454762552, 0.1049064006))
                Line((0.6454762552, -0.1049064006), (0.7380491942, -0.1197687159))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


def model_146640_89ef3723_0002():
    """Model: Spur Gear (16 teeth)"""
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
        with BuildSketch(Plane.XY):
            # Profile area: 2.7166960372, perimeter: 5.8428596809
            Circle(0.92992)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0635035313, perimeter: 0.9793133267
            with BuildLine():
                _nurbs_edge([(0.9887636746, -0.1274083967), (0.989470413, -0.1274981255), (0.9908852939, -0.1276554165), (0.9930118279, -0.1278248538), (0.9958553112, -0.1279242627), (0.9994212769, -0.1278753054), (1.0029963803, -0.1277009141), (1.0065780691, -0.1274481987), (1.0101642497, -0.1271518565), (1.0137537169, -0.1268249679), (1.0173458754, -0.1264663411), (1.0209405325, -0.1260662096), (1.0245376745, -0.1256122598), (1.0281372269, -0.1250961954), (1.031738895, -0.1245179287), (1.035342265, -0.1238822151), (1.0389468617, -0.1231965493), (1.0425522181, -0.122468727), (1.0461579507, -0.121704173), (1.0497637962, -0.1209046436), (1.0533695659, -0.1200697189), (1.0569751178, -0.1191977121), (1.0605803241, -0.1182867328), (1.064185035, -0.1173358735), (1.0677890645, -0.1163456577), (1.0713922085, -0.1153174111), (1.0749942553, -0.1142528871), (1.0785949982, -0.1131538249), (1.0821942493, -0.112021452), (1.0857918441, -0.1108563395), (1.0893876323, -0.1096586714), (1.0929814736, -0.1084284099), (1.0965732312, -0.1071654874), (1.100162765, -0.1058700251), (1.1037499305, -0.1045423879), (1.1073345811, -0.103183073), (1.1109165709, -0.1017926412), (1.1144957563, -0.1003716382), (1.1180719989, -0.098920504), (1.1216451659, -0.0974395531), (1.1252151286, -0.0959290227), (1.1287817607, -0.0943891033), (1.1323449376, -0.0928199741), (1.1359045348, -0.0912218432), (1.1394604274, -0.0895949582), (1.1430124914, -0.0879395852), (1.146560604, -0.0862559971), (1.1501046446, -0.084544459), (1.1536444954, -0.0828052121), (1.1571800416, -0.0810384696), (1.1607111701, -0.0792444259), (1.1642377682, -0.077423263), (1.1677597226, -0.0755751572), (1.1712769186, -0.0737002878), (1.1747892396, -0.0717988397), (1.1782965698, -0.0698709984), (1.1817987959, -0.0679169467), (1.1852958091, -0.0659368609), (1.1887875076, -0.0639309074), (1.1922737965, -0.0618992416), (1.1957545826, -0.0598420119), (1.1992297698, -0.0577593641), (1.2026992553, -0.0556514445), (1.2061629239, -0.0535184053), (1.2096206468, -0.0513604063), (1.2130722925, -0.0491776078), (1.2165177359, -0.0469701646), (1.219956868, -0.0447382205), (1.2233896057, -0.0424819023), (1.2268159001, -0.0402013149), (1.2302357266, -0.0378965403), (1.2329664078, -0.0360334184), (1.2350115058, -0.0346252355), (1.2363736102, -0.0336816301), (1.2370543389, -0.0332086232)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((0, 0), 1.2375, -1.537731228, 3.075462456)
                _nurbs_edge([(0.9887636746, 0.1274083967), (0.989470413, 0.1274981255), (0.9908852939, 0.1276554165), (0.9930118279, 0.1278248538), (0.9958553112, 0.1279242627), (0.9994212769, 0.1278753054), (1.0029963803, 0.1277009141), (1.0065780691, 0.1274481987), (1.0101642497, 0.1271518565), (1.0137537169, 0.1268249679), (1.0173458754, 0.1264663411), (1.0209405325, 0.1260662096), (1.0245376745, 0.1256122598), (1.0281372269, 0.1250961954), (1.031738895, 0.1245179287), (1.035342265, 0.1238822151), (1.0389468617, 0.1231965493), (1.0425522181, 0.122468727), (1.0461579507, 0.121704173), (1.0497637962, 0.1209046436), (1.0533695659, 0.1200697189), (1.0569751178, 0.1191977121), (1.0605803241, 0.1182867328), (1.064185035, 0.1173358735), (1.0677890645, 0.1163456577), (1.0713922085, 0.1153174111), (1.0749942553, 0.1142528871), (1.0785949982, 0.1131538249), (1.0821942493, 0.112021452), (1.0857918441, 0.1108563395), (1.0893876323, 0.1096586714), (1.0929814736, 0.1084284099), (1.0965732312, 0.1071654874), (1.100162765, 0.1058700251), (1.1037499305, 0.1045423879), (1.1073345811, 0.103183073), (1.1109165709, 0.1017926412), (1.1144957563, 0.1003716382), (1.1180719989, 0.098920504), (1.1216451659, 0.0974395531), (1.1252151286, 0.0959290227), (1.1287817607, 0.0943891033), (1.1323449376, 0.0928199741), (1.1359045348, 0.0912218432), (1.1394604274, 0.0895949582), (1.1430124914, 0.0879395852), (1.146560604, 0.0862559971), (1.1501046446, 0.084544459), (1.1536444954, 0.0828052121), (1.1571800416, 0.0810384696), (1.1607111701, 0.0792444259), (1.1642377682, 0.077423263), (1.1677597226, 0.0755751572), (1.1712769186, 0.0737002878), (1.1747892396, 0.0717988397), (1.1782965698, 0.0698709984), (1.1817987959, 0.0679169467), (1.1852958091, 0.0659368609), (1.1887875076, 0.0639309074), (1.1922737965, 0.0618992416), (1.1957545826, 0.0598420119), (1.1992297698, 0.0577593641), (1.2026992553, 0.0556514445), (1.2061629239, 0.0535184053), (1.2096206468, 0.0513604063), (1.2130722925, 0.0491776078), (1.2165177359, 0.0469701646), (1.219956868, 0.0447382205), (1.2233896057, 0.0424819023), (1.2268159001, 0.0402013149), (1.2302357266, 0.0378965403), (1.2329664078, 0.0360334184), (1.2350115058, 0.0346252355), (1.2363736102, 0.0336816301), (1.2370543389, 0.0332086232)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                Line((0.9213028608, 0.1188434477), (0.9887636746, 0.1274083967))
                Line((0.9213028608, -0.1188434477), (0.9213028608, 0.1188434477))
                Line((0.9213028608, -0.1188434477), (0.9887636746, -0.1274083967))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


def model_146805_0416c8ff_0002():
    """Model: Lever Base"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 10.016, perimeter: 12.66
            with BuildLine():
                Line((0, 3.13), (0, 0))
                Line((0, 0), (3.2, 0))
                Line((3.2, 0), (3.2, 3.13))
                Line((3.2, 3.13), (0, 3.13))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch6 -> Extrude9 (Join)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1319135248, perimeter: 3.3137146352
            with BuildLine():
                Line((1.1500004381, 0), (2.0499995619, 0))
                Line((1.1500004381, 0), (1.15, -0.4999996057))
                CenterArc((1.6, -0.5), 0.45, 0.0000501993, 179.9999498007)
                Line((2.0499995619, 0), (2.05, -0.4999996057))
            make_face()
            # Profile area: 0.4398229715, perimeter: 4.398229715
            with BuildLine():
                CenterArc((1.6, -0.5), 0.45, 0.0000501993, 179.9999498007)
                CenterArc((1.6, -0.5), 0.45, 180, 180.0000501993)
            make_face()
            with BuildLine():
                CenterArc((1.6, -0.5), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.ADD)

        # Sketch6 -> Extrude10 (Join)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((1.6, -0.5)):
                Circle(0.25)
        # OneSide extrude, distance=-0.42
        extrude(amount=-0.42, mode=Mode.ADD)
    return part.part


def model_146827_44b163c8_0001():
    """Model: RUEDA"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 50.2654824574, perimeter: 25.1327412287
            Circle(4)
        # OneSide extrude, distance=3.5
        extrude(amount=3.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(3.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=-9.5
        extrude(amount=-9.5, mode=Mode.SUBTRACT)
    return part.part


def model_146888_62f0c3fe_0002():
    """Model: Bishop v1"""
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
        # Sketch15 -> Extrude21 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6, perimeter: 10
            with BuildLine():
                Line((-1, -13), (1, -13))
                Line((-1, -16), (-1, -13))
                Line((1, -16), (-1, -16))
                Line((1, -13), (1, -16))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


def model_147022_9b03d096_0000():
    """Model: Spur Gear (21 teeth)"""
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
        with BuildSketch(Plane.XY):
            # Profile area: 436.6076206824, perimeter: 78.1686057518
            with BuildLine():
                CenterArc((0, 0), 11.80592, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.635, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 5.2973394267, perimeter: 8.9487469406
            with BuildLine():
                _nurbs_edge([(12.4804181893, -1.1225586762), (12.4865605727, -1.1231103954), (12.4988497284, -1.124051286), (12.5172966286, -1.124974986), (12.5419176179, -1.1252800815), (12.572728515, -1.1243996502), (12.6035645841, -1.1226151307), (12.634415889, -1.1202781271), (12.6652740382, -1.1176445625), (12.6961337171, -1.1148080971), (12.7269917437, -1.1117568045), (12.7578464136, -1.1084158377), (12.7886967709, -1.1046928613), (12.8195418276, -1.1005283147), (12.8503800796, -1.0959239955), (12.8812097902, -1.0909171371), (12.912029127, -1.0855646962), (12.9428363435, -1.0799249641), (12.9736299744, -1.0740370783), (13.0044089074, -1.0679130643), (13.0351722582, -1.0615491203), (13.0659192909, -1.0549324559), (13.0966493274, -1.0480492737), (13.1273616451, -1.0408938344), (13.1580554467, -1.0334708451), (13.1887299059, -1.0257907971), (13.2193841945, -1.0178671225), (13.2500175139, -1.0097128939), (13.2806291322, -1.0013370318), (13.3112183878, -0.9927436917), (13.3417846681, -0.9839342283), (13.3723273934, -0.974908457), (13.4028460015, -0.965666084), (13.4333399283, -0.9562083634), (13.4638086048, -0.9465382953), (13.4942514649, -0.9366598196), (13.5246679502, -0.9265772937), (13.5550575153, -0.9162949053), (13.5854196356, -0.9058159896), (13.6157538058, -0.8951429697), (13.646059536, -0.8842777059), (13.676336347, -0.8732217301), (13.7065837673, -0.8619765064), (13.7368013288, -0.8505437366), (13.7669885662, -0.8389253982), (13.7971450201, -0.8271235972), (13.8272702381, -0.815140474), (13.8573637779, -0.802978098), (13.8874252095, -0.7906383456), (13.9174541146, -0.7781228836), (13.9474500816, -0.7654332383), (13.9774127012, -0.7525708434), (14.0073415634, -0.7395370923), (14.0372362527, -0.726333402), (14.0670963491, -0.7129612265), (14.0969214372, -0.6994220177), (14.1267111128, -0.6857172003), (14.1564649897, -0.6718481452), (14.1861827101, -0.6578161377), (14.2158639424, -0.6436223732), (14.2455083607, -0.6292679957), (14.2751156287, -0.6147541274), (14.3046853834, -0.6000819), (14.3342172146, -0.5852524946), (14.3637106623, -0.5702671532), (14.3931652586, -0.5551271168), (14.4225805618, -0.5398335783), (14.4519561931, -0.5243876322), (14.4812918753, -0.5087902233), (14.5105874612, -0.4930421052), (14.5398428937, -0.4771438512), (14.5632151187, -0.4643054584), (14.5807262316, -0.4546093867), (14.5923922847, -0.448115448), (14.5982233058, -0.4448610058)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((0, 0), 14.605, -1.7454708023, 3.4909416046)
                _nurbs_edge([(12.4804181893, 1.1225586762), (12.4865605727, 1.1231103954), (12.4988497284, 1.124051286), (12.5172966286, 1.124974986), (12.5419176179, 1.1252800815), (12.572728515, 1.1243996502), (12.6035645841, 1.1226151307), (12.634415889, 1.1202781271), (12.6652740382, 1.1176445625), (12.6961337171, 1.1148080971), (12.7269917437, 1.1117568045), (12.7578464136, 1.1084158377), (12.7886967709, 1.1046928613), (12.8195418276, 1.1005283147), (12.8503800796, 1.0959239955), (12.8812097902, 1.0909171371), (12.912029127, 1.0855646962), (12.9428363435, 1.0799249641), (12.9736299744, 1.0740370783), (13.0044089074, 1.0679130643), (13.0351722582, 1.0615491203), (13.0659192909, 1.0549324559), (13.0966493274, 1.0480492737), (13.1273616451, 1.0408938344), (13.1580554467, 1.0334708451), (13.1887299059, 1.0257907971), (13.2193841945, 1.0178671225), (13.2500175139, 1.0097128939), (13.2806291322, 1.0013370318), (13.3112183878, 0.9927436917), (13.3417846681, 0.9839342283), (13.3723273934, 0.974908457), (13.4028460015, 0.965666084), (13.4333399283, 0.9562083634), (13.4638086048, 0.9465382953), (13.4942514649, 0.9366598196), (13.5246679502, 0.9265772937), (13.5550575153, 0.9162949053), (13.5854196356, 0.9058159896), (13.6157538058, 0.8951429697), (13.646059536, 0.8842777059), (13.676336347, 0.8732217301), (13.7065837673, 0.8619765064), (13.7368013288, 0.8505437366), (13.7669885662, 0.8389253982), (13.7971450201, 0.8271235972), (13.8272702381, 0.815140474), (13.8573637779, 0.802978098), (13.8874252095, 0.7906383456), (13.9174541146, 0.7781228836), (13.9474500816, 0.7654332383), (13.9774127012, 0.7525708434), (14.0073415634, 0.7395370923), (14.0372362527, 0.726333402), (14.0670963491, 0.7129612265), (14.0969214372, 0.6994220177), (14.1267111128, 0.6857172003), (14.1564649897, 0.6718481452), (14.1861827101, 0.6578161377), (14.2158639424, 0.6436223732), (14.2455083607, 0.6292679957), (14.2751156287, 0.6147541274), (14.3046853834, 0.6000819), (14.3342172146, 0.5852524946), (14.3637106623, 0.5702671532), (14.3931652586, 0.5551271168), (14.4225805618, 0.5398335783), (14.4519561931, 0.5243876322), (14.4812918753, 0.5087902233), (14.5105874612, 0.4930421052), (14.5398428937, 0.4771438512), (14.5632151187, 0.4643054584), (14.5807262316, 0.4546093867), (14.5923922847, 0.448115448), (14.5982233058, 0.4448610058)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                Line((11.7574556596, 1.0576209631), (12.4804181893, 1.1225586762))
                Line((11.7574556596, -1.0576209631), (11.7574556596, 1.0576209631))
                Line((11.7574556596, -1.0576209631), (12.4804181893, -1.1225586762))
            make_face()
        # OneSide extrude, distance=1.27
        extrude(amount=1.27, mode=Mode.ADD)
    return part.part


def model_147022_9b03d096_0001():
    """Model: Spur Gear (15 teeth) (1)"""
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
        with BuildSketch(Plane.XY):
            # Profile area: 38.6300356355, perimeter: 27.2433888371
            with BuildLine():
                CenterArc((0, 0), 3.58592, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.032489038, perimeter: 3.9208226658
            with BuildLine():
                _nurbs_edge([(3.988477379, -0.4794071184), (3.9909307858, -0.4797013308), (3.9958414257, -0.4802170465), (4.0032188641, -0.4807724961), (4.0130773722, -0.481098724), (4.0254309634, -0.4809424768), (4.0378071268, -0.4803823382), (4.050197804, -0.4795754504), (4.0625965524, -0.478635431), (4.0749998647, -0.4776031648), (4.0874061964, -0.4764725637), (4.0998152751, -0.475209672), (4.1122273452, -0.4737730755), (4.1246423394, -0.4721366677), (4.1370594176, -0.4703017245), (4.1494773317, -0.4682851716), (4.161894626, -0.466112556), (4.174309884, -0.4638097927), (4.1867220019, -0.4613938945), (4.1991302779, -0.4588698599), (4.2115342541, -0.4562357217), (4.2239336194, -0.4534856211), (4.2363280961, -0.4506133818), (4.2487173117, -0.4476165992), (4.2611007706, -0.4444974676), (4.2734779161, -0.4412607188), (4.285848168, -0.4379123381), (4.298210966, -0.4344580877), (4.3105658203, -0.4309018036), (4.3229123159, -0.4272452338), (4.3352500848, -0.4234888998), (4.3475787882, -0.4196326673), (4.3598980959, -0.4156763852), (4.3722076629, -0.4116206274), (4.3845071281, -0.4074667299), (4.3967961245, -0.4032164407), (4.4090742858, -0.3988716815), (4.4213412546, -0.3944342872), (4.4335966918, -0.3899056995), (4.4458402756, -0.3852869629), (4.4580716964, -0.380578876), (4.4702906531, -0.3757820978), (4.4824968488, -0.3708972635), (4.4946899861, -0.3659251216), (4.5068697669, -0.360866541), (4.5190358953, -0.3557224474), (4.5311880793, -0.3504937803), (4.5433260329, -0.3451814464), (4.5554494789, -0.3397862652), (4.5675581481, -0.3343089649), (4.579651776, -0.3287502128), (4.5917300996, -0.3231106366), (4.6037928557, -0.3173908479), (4.6158397768, -0.3115914704), (4.627870593, -0.3057131443), (4.6398850365, -0.2997565096), (4.6518828469, -0.2937221941), (4.6638637747, -0.2876108025), (4.6758275886, -0.2814229016), (4.6877740727, -0.2751590202), (4.6997030151, -0.2688196648), (4.7116141966, -0.2624053331), (4.7235073823, -0.2559165279), (4.7353823075, -0.249353774), (4.7472386777, -0.2427176229), (4.7590761936, -0.2360086256), (4.7708945727, -0.2292273126), (4.7826935713, -0.2223741715), (4.7944730079, -0.2154496252), (4.8062327806, -0.2084540142), (4.8179728435, -0.2013875999), (4.8273491196, -0.1956779727), (4.8343724584, -0.1913640222), (4.8390507441, -0.1884739575), (4.8413889019, -0.1870254008)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((0, 0), 4.845, -2.2122660809, 4.4245321618)
                _nurbs_edge([(3.988477379, 0.4794071184), (3.9909307858, 0.4797013308), (3.9958414257, 0.4802170465), (4.0032188641, 0.4807724961), (4.0130773722, 0.481098724), (4.0254309634, 0.4809424768), (4.0378071268, 0.4803823382), (4.050197804, 0.4795754504), (4.0625965524, 0.478635431), (4.0749998647, 0.4776031648), (4.0874061964, 0.4764725637), (4.0998152751, 0.475209672), (4.1122273452, 0.4737730755), (4.1246423394, 0.4721366677), (4.1370594176, 0.4703017245), (4.1494773317, 0.4682851716), (4.161894626, 0.466112556), (4.174309884, 0.4638097927), (4.1867220019, 0.4613938945), (4.1991302779, 0.4588698599), (4.2115342541, 0.4562357217), (4.2239336194, 0.4534856211), (4.2363280961, 0.4506133818), (4.2487173117, 0.4476165992), (4.2611007706, 0.4444974676), (4.2734779161, 0.4412607188), (4.285848168, 0.4379123381), (4.298210966, 0.4344580877), (4.3105658203, 0.4309018036), (4.3229123159, 0.4272452338), (4.3352500848, 0.4234888998), (4.3475787882, 0.4196326673), (4.3598980959, 0.4156763852), (4.3722076629, 0.4116206274), (4.3845071281, 0.4074667299), (4.3967961245, 0.4032164407), (4.4090742858, 0.3988716815), (4.4213412546, 0.3944342872), (4.4335966918, 0.3899056995), (4.4458402756, 0.3852869629), (4.4580716964, 0.380578876), (4.4702906531, 0.3757820978), (4.4824968488, 0.3708972635), (4.4946899861, 0.3659251216), (4.5068697669, 0.360866541), (4.5190358953, 0.3557224474), (4.5311880793, 0.3504937803), (4.5433260329, 0.3451814464), (4.5554494789, 0.3397862652), (4.5675581481, 0.3343089649), (4.579651776, 0.3287502128), (4.5917300996, 0.3231106366), (4.6037928557, 0.3173908479), (4.6158397768, 0.3115914704), (4.627870593, 0.3057131443), (4.6398850365, 0.2997565096), (4.6518828469, 0.2937221941), (4.6638637747, 0.2876108025), (4.6758275886, 0.2814229016), (4.6877740727, 0.2751590202), (4.6997030151, 0.2688196648), (4.7116141966, 0.2624053331), (4.7235073823, 0.2559165279), (4.7353823075, 0.249353774), (4.7472386777, 0.2427176229), (4.7590761936, 0.2360086256), (4.7708945727, 0.2292273126), (4.7826935713, 0.2223741715), (4.7944730079, 0.2154496252), (4.8062327806, 0.2084540142), (4.8179728435, 0.2013875999), (4.8273491196, 0.1956779727), (4.8343724584, 0.1913640222), (4.8390507441, 0.1884739575), (4.8413889019, 0.1870254008)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                Line((3.5593005875, 0.4279402531), (3.988477379, 0.4794071184))
                Line((3.5593005875, -0.4279402531), (3.5593005875, 0.4279402531))
                Line((3.5593005875, -0.4279402531), (3.988477379, -0.4794071184))
            make_face()
        # OneSide extrude, distance=1.27
        extrude(amount=1.27, mode=Mode.ADD)
    return part.part


def model_147082_c6f4f6a5_0000():
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
        # Sketch1 -> Extrude4 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 88.8024958501, perimeter: 46.4498081893
            with BuildLine():
                Line((0, 5), (0, 0))
                _nurbs_edge([(0, 0), (0.3502681486, -0.0345030575), (1.0516598085, -0.1004765913), (2.1063133364, -0.190339326), (3.517734982, -0.291660294), (5.2912922567, -0.3854096568), (7.0749402895, -0.4433835039), (8.8694732996, -0.4627660302), (10.6752707995, -0.442211722), (12.4918244211, -0.3835229351), (14.3182962627, -0.2896703438), (15.7867441823, -0.1888118162), (16.8919078635, -0.0995971435), (17.6303570442, -0.0341878891), (18, 0)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                Line((18, 0), (18, 5))
                Line((18, 5), (17.6810713817, 5))
                CenterArc((17.6810713817, 3), 2, 90, 34.3488376033)
                _nurbs_edge([(2.2798094871, 4.6512353157), (2.3626529174, 4.594619826), (2.5311588191, 4.4928602423), (2.7923742095, 4.3746339847), (3.15562859, 4.2816627652), (3.6238731945, 4.2493952659), (4.093544075, 4.2713670467), (4.5535696615, 4.319041133), (4.9987905221, 4.3731046154), (5.4325956717, 4.4286639185), (5.8630803228, 4.4888842704), (6.3000406981, 4.5601209025), (6.7519661443, 4.6470322216), (7.2222850562, 4.7463976951), (7.7090883579, 4.8470127474), (8.2075540582, 4.9342912951), (8.7116328043, 4.9936279294), (9.2158597814, 5.0139138333), (9.7175043357, 4.991863654), (10.2171619913, 4.9329554238), (10.7171358224, 4.8476097109), (11.220362958, 4.7485461936), (11.7291696173, 4.6478051975), (12.2439970921, 4.5536518377), (12.7624248057, 4.4683024242), (13.280282997, 4.3912807412), (13.7924896765, 4.3220101861), (14.2940166358, 4.2628517286), (14.7807284178, 4.2216023667), (15.2504676112, 4.2152030945), (15.7027082703, 4.2661329563), (16.050815355, 4.3707350884), (16.3045271535, 4.493044507), (16.4704525962, 4.5950877028), (16.5526113991, 4.6512353156)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0333333333, 0.0666666667, 0.1, 0.1333333333, 0.1666666667, 0.2, 0.2333333333, 0.2666666667, 0.3, 0.3333333333, 0.3666666667, 0.4, 0.4333333333, 0.4666666667, 0.5, 0.5333333333, 0.5666666667, 0.6, 0.6333333333, 0.6666666667, 0.7, 0.7333333333, 0.7666666667, 0.8, 0.8333333333, 0.8666666667, 0.9, 0.9333333333, 0.9666666667, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((1.1513495045, 3), 2, 55.6511623968, 34.3488376032)
                Line((0, 5), (1.1513495045, 5))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch12 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 2, perimeter: 6.6
            with BuildLine():
                Line((-1, 0.65), (-3.5, 0.65))
                Line((-1, 1.45), (-1, 0.65))
                Line((-3.5, 1.45), (-1, 1.45))
                Line((-3.5, 0.65), (-3.5, 1.45))
            make_face()
        # OneSide extrude, distance=-17
        extrude(amount=-17, mode=Mode.SUBTRACT)
    return part.part


def model_147133_92c04b84_0002():
    """Model: Уплотнитель-квадрат"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.44, perimeter: 4.8
            with BuildLine():
                Line((0.6, -0.6), (-0.6, -0.6))
                Line((0.6, 0.6), (0.6, -0.6))
                Line((-0.6, 0.6), (0.6, 0.6))
                Line((-0.6, -0.6), (-0.6, 0.6))
            make_face()
        # OneSide extrude, distance=1.3
        extrude(amount=1.3)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=-1.1
        extrude(amount=-1.1, mode=Mode.SUBTRACT)
    return part.part


def model_147134_273aac81_0001():
    """Model: Центральная"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 34.8690266447, perimeter: 31.9398223686
            with BuildLine():
                Line((2.5, 7.2), (2.5, 0))
                Line((-2.5, 7.2), (2.5, 7.2))
                Line((-2.5, 0), (-2.5, 7.2))
                Line((2.5, 0), (-2.5, 0))
            make_face()
            with BuildLine():
                CenterArc((-1, 2.6694116008), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1, 4.6694116008), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1, 2.6694116008), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1, 4.6694116008), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-1, 2.6694116008)):
                Circle(0.3)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((1, 4.6694116008)):
                Circle(0.3)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((1, 2.6694116008)):
                Circle(0.3)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-1, 4.6694116008)):
                Circle(0.3)
        # Symmetric extrude, full_length=True, total=2
        extrude(amount=1, both=True)

        # Sketch1 -> Extrude2 (Cut)
        # Sketch on YZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-1, 4.6694116008)):
                Circle(0.3)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((1, 4.6694116008)):
                Circle(0.3)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-1, 2.6694116008)):
                Circle(0.3)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((1, 2.6694116008)):
                Circle(0.3)
        # Symmetric extrude, full_length=True, total=2
        extrude(amount=1, both=True, mode=Mode.SUBTRACT)
    return part.part


def model_147650_74de1acb_0000():
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
        # Sketch has 36 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.1101994874, perimeter: 3.7351276035
            with BuildLine():
                CenterArc((38.8099808813, -0.0072468094), 0.5944640212, 91.909152433, 176.7274879813)
                CenterArc((38.8099808813, -0.0072468094), 0.5944640212, -91.3633595857, 29.5346461012)
                CenterArc((38.8099808813, -0.0072468094), 0.5944640212, -61.8287134845, 34.5300159416)
                CenterArc((38.8099808813, -0.0072468094), 0.5944640212, -27.2986975429, 27.9971786386)
                CenterArc((38.8099808813, -0.0072468094), 0.5944640212, 0.6984810956, 27.6022746704)
                CenterArc((38.8099808813, -0.0072468094), 0.5944640212, 28.300755766, 34.2916687962)
                CenterArc((38.8099808813, -0.0072468094), 0.5944640212, 62.5924245622, 29.3167278708)
            make_face()
        # Symmetric extrude, each_side=0.2
        extrude(amount=0.2, both=True)
    return part.part


def model_147853_e92074c2_0008():
    """Model: disc 3 v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 153.9380400259, perimeter: 43.9822971503
            Circle(7)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 62 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.15, perimeter: 1.6
            with BuildLine():
                Line((1.5, 0), (2, 0))
                Line((1.5, 0), (1.5, -0.3))
                Line((1.5, -0.3), (2, -0.3))
                Line((2, -0.3), (2, 0))
            make_face()
            # Profile area: 0.15, perimeter: 1.6
            with BuildLine():
                Line((2, 0), (2, 0.3))
                Line((2, 0.3), (1.5, 0.3))
                Line((1.5, 0.3), (1.5, 0))
                Line((1.5, 0), (2, 0))
            make_face()
            # Profile area: 0.1499999955, perimeter: 1.5999999642
            with BuildLine():
                Line((0, -1.5000000224), (0, -2))
                Line((0.25, -2), (0, -2))
                Line((0.3000000045, -2), (0.25, -2))
                Line((0.3000000045, -2), (0.3000000045, -1.5000000224))
                Line((0.3000000045, -1.5000000224), (0, -1.5000000224))
            make_face()
            # Profile area: 0.1499999944, perimeter: 1.5999999598
            with BuildLine():
                Line((0, -1.5000000224), (-0.3000000045, -1.5000000224))
                Line((-0.3000000045, -1.5000000224), (-0.3, -2))
                Line((0, -2), (-0.3, -2))
                Line((0, -1.5000000224), (0, -2))
            make_face()
            # Profile area: 0.1499999955, perimeter: 1.5999999642
            with BuildLine():
                Line((-1.5000000224, 0.3000000045), (-1.5000000224, 0))
                Line((-2, 0.3000000045), (-1.5000000224, 0.3000000045))
                Line((-2, 0.3000000045), (-2, 0))
                Line((-1.5000000224, 0), (-2, 0))
            make_face()
            # Profile area: 0.1499999955, perimeter: 1.5999999642
            with BuildLine():
                Line((-1.5000000224, 0), (-2, 0))
                Line((-2, 0), (-2, -0.3000000045))
                Line((-1.5000000224, -0.3000000045), (-2, -0.3000000045))
                Line((-1.5000000224, 0), (-1.5000000224, -0.3000000045))
            make_face()
            # Profile area: 0.1499999978, perimeter: 1.5999999642
            with BuildLine():
                Line((0, 1.5000000224), (0, 2.0000000149))
                Line((0.3000000045, 1.5000000224), (0, 1.5000000224))
                Line((0.3000000045, 2), (0.3000000045, 1.5000000224))
                Line((0, 2.0000000149), (0.3000000045, 2))
            make_face()
            # Profile area: 0.1500000022, perimeter: 1.599999994
            with BuildLine():
                Line((-0.3000000045, 2.0000000298), (0, 2.0000000149))
                Line((-0.3000000045, 1.5000000224), (-0.3000000045, 2.0000000298))
                Line((0, 1.5000000224), (-0.3000000045, 1.5000000224))
                Line((0, 1.5000000224), (0, 2.0000000149))
            make_face()
        # OneSide extrude, distance=-6
        extrude(amount=-6, mode=Mode.SUBTRACT)
    return part.part


def model_148024_0fa50126_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 20 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2119736842, perimeter: 1.8421052632
            with BuildLine():
                Line((-1.5239091112, -6.964366056), (-1.3347016554, -6.5560762831))
                Line((-1.5239091112, -6.964366056), (-1.0965180623, -7.1624253225))
                Line((-0.9073106065, -6.7541355496), (-1.0965180623, -7.1624253225))
                Line((-0.9073106065, -6.7541355496), (-1.3347016554, -6.5560762831))
            make_face()
            # Profile area: 0.45, perimeter: 2.9
            with BuildLine():
                Line((-5.8442077958, -4.4663051448), (-6.0334152516, -4.8745949177))
                Line((-6.0334152516, -4.8745949177), (-5.1261046451, -5.2950559305))
                Line((-4.9368971893, -4.8867661576), (-5.1261046451, -5.2950559305))
                Line((-5.8442077958, -4.4663051448), (-4.9368971893, -4.8867661576))
            make_face()
            # Profile area: 1.7865855183, perimeter: 8.8403800815
            with BuildLine():
                Line((-4.9368971893, -4.8867661576), (-5.1261046451, -5.2950559305))
                Line((-5.1261046451, -5.2950559305), (-1.5239091112, -6.964366056))
                Line((-1.5239091112, -6.964366056), (-1.3347016554, -6.5560762831))
                Line((-1.3347016554, -6.5560762831), (-4.9368971893, -4.8867661576))
            make_face()
            # Profile area: 0.2241305237, perimeter: 1.8961522531
            with BuildLine():
                Line((-0.4536553033, -6.964366056), (-0.642862759, -7.3726558289))
                Line((-0.642862759, -7.3726558289), (-0.1927136115, -7.5812615314))
                Line((-0.1927136115, -7.5812615314), (0, -7.1745965624))
                Line((0, -7.1745965624), (-0.4536553033, -6.964366056))
            make_face()
            # Profile area: 0.225, perimeter: 1.9
            with BuildLine():
                Line((-0.9073106065, -6.7541355496), (-1.0965180623, -7.1624253225))
                Line((-1.0965180623, -7.1624253225), (-0.642862759, -7.3726558289))
                Line((-0.4536553033, -6.964366056), (-0.642862759, -7.3726558289))
                Line((-0.4536553033, -6.964366056), (-0.9073106065, -6.7541355496))
            make_face()
        # OneSide extrude, distance=20
        extrude(amount=20)

        # Sketch2 -> Extrude4 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 20 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2119736842, perimeter: 1.8421052632
            with BuildLine():
                Line((-1.5239091112, -6.964366056), (-1.3347016554, -6.5560762831))
                Line((-1.5239091112, -6.964366056), (-1.0965180623, -7.1624253225))
                Line((-0.9073106065, -6.7541355496), (-1.0965180623, -7.1624253225))
                Line((-0.9073106065, -6.7541355496), (-1.3347016554, -6.5560762831))
            make_face()
            # Profile area: 0.225, perimeter: 1.9
            with BuildLine():
                Line((-0.9073106065, -6.7541355496), (-1.0965180623, -7.1624253225))
                Line((-1.0965180623, -7.1624253225), (-0.642862759, -7.3726558289))
                Line((-0.4536553033, -6.964366056), (-0.642862759, -7.3726558289))
                Line((-0.4536553033, -6.964366056), (-0.9073106065, -6.7541355496))
            make_face()
        # OneSide extrude, distance=-0.45
        extrude(amount=-0.45)

        # Sketch2 -> Extrude5 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 20 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.45, perimeter: 2.9
            with BuildLine():
                Line((-5.8442077958, -4.4663051448), (-6.0334152516, -4.8745949177))
                Line((-6.0334152516, -4.8745949177), (-5.1261046451, -5.2950559305))
                Line((-4.9368971893, -4.8867661576), (-5.1261046451, -5.2950559305))
                Line((-5.8442077958, -4.4663051448), (-4.9368971893, -4.8867661576))
            make_face()
        # OneSide extrude, distance=-0.45
        extrude(amount=-0.45)
    return part.part


def model_148051_ad8f6d60_0000():
    """Model: Fin"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 2.4538644137, perimeter: 8.0643396424
            with BuildLine():
                Line((1.6187259886, 1.4398594068), (1.7871057909, 1.6082392091))
                Line((0, 3.0585853955), (1.6187259886, 1.4398594068))
                Line((0, 0.93472), (0, 3.0585853955))
                Line((2.460625, 0.93472), (0, 0.93472))
                Line((1.7871057909, 1.6082392091), (2.460625, 0.93472))
            make_face()
        # Symmetric extrude, full_length=True, total=0.238125
        extrude(amount=0.1190625, both=True)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.0894332909, -0.0894332909), x_dir=(1, 0, 0), z_dir=(0, -0.7071067812, 0.7071067812))):
            # Profile area: 0.044534837, perimeter: 0.7480917506
            with BuildLine():
                CenterArc((0, 2.281808974), 0.1190625, 180, 89.9999971049)
                CenterArc((0, 2.281808974), 0.1190625, -90.0000028951, 90.0000028951)
                CenterArc((0, 2.281808974), 0.1190625, 0, 90.0000028951)
                CenterArc((0, 2.281808974), 0.1190625, 90.0000028951, 89.9999971049)
            make_face()
        # OneSide extrude, distance=20.32
        extrude(amount=20.32)
    return part.part


def model_20232_e5b060d9_0002():
    """Model: .35 Tip"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.0694344957, perimeter: 3.8494829595
            with BuildLine():
                Line((0.3207902714, 0.5556249914), (-0.3207902714, 0.5556249914))
                Line((-0.3207902714, 0.5556249914), (-0.6415804933, -0.0000000172))
                Line((-0.6415804933, -0.0000000172), (-0.3207902417, -0.5556250086))
                Line((-0.3207902417, -0.5556250086), (0.3207902417, -0.5556250086))
                Line((0.3207902417, -0.5556250086), (0.6415804933, -0.0000000172))
                Line((0.6415804933, -0.0000000172), (0.3207902714, 0.5556249914))
            make_face()
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)
    return part.part


def model_20241_6bced5ac_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 64.516, perimeter: 35.56
            with BuildLine():
                Line((0, 5.08), (0, 0))
                Line((0, 0), (12.7, 0))
                Line((12.7, 0), (12.7, 5.08))
                Line((12.7, 5.08), (0, 5.08))
            make_face()
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.54), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 3.2258, perimeter: 7.62
            with BuildLine():
                Line((10.16, 1.27), (10.16, 3.81))
                Line((10.16, 3.81), (8.89, 3.81))
                Line((8.89, 3.81), (8.89, 1.27))
                Line((8.89, 1.27), (10.16, 1.27))
            make_face()
        # OneSide extrude, distance=-1.27
        extrude(amount=-1.27, mode=Mode.SUBTRACT)
    return part.part


def model_20849_9821b6fe_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 6 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.0196886713, perimeter: 10.4346441775
            with BuildLine():
                Line((-8.1867137542, 1.7954030693), (-8.0446529891, 1.4828693861))
                Line((-8.0446529891, 1.4828693861), (-5.814757759, 1.9725075226))
                Line((-5.814757759, 1.9725075226), (-6.0819054097, 2.0929125527))
                Line((-6.0819054097, 2.0929125527), (-8.1888125328, 2.8943128081))
                CenterArc((-8.3665717229, 2.4269781632), 0.5, 69.1747819576, 13.3681629021)
                Line((-8.3016802035, 2.9227493712), (-10.5536748001, 3.2175130619))
                CenterArc((-10.5588661217, 3.1778513652), 0.04, 82.5429448598, 159.8222900639)
                Line((-10.5774194684, 3.1424144731), (-8.3653268783, 1.9842508133))
                CenterArc((-8.5508603452, 1.6298818916), 0.4, 24.4439547804, 37.9212801432)
            make_face()
        # TwoSides extrude (symmetric), distance=0.1
        extrude(amount=0.1, both=True)

        # Sketch2 -> Extrude4 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-7, 1)):
                Circle(0.15)
        # TwoSides extrude (symmetric), distance=0.9
        extrude(amount=0.9, both=True)
    return part.part


def model_21231_eb9826e5_0000():
    """Model: Y3 v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.96, perimeter: 5.6
            with BuildLine():
                Line((1.4, -1.4), (0, -1.4))
                Line((1.4, 0), (1.4, -1.4))
                Line((0, 0), (1.4, 0))
                Line((0, -1.4), (0, 0))
            make_face()
        # OneSide extrude, distance=-0.14
        extrude(amount=-0.14)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 21 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -0.14, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.1976, perimeter: 3.3
            with BuildLine():
                Line((0.7, 1.4), (0.7, 1.27))
                Line((0.7, 1.27), (0.76, 1.27))
                Line((0.76, 1.27), (0.76, 0.13))
                Line((0.76, 0.13), (0.7, 0.13))
                Line((0.7, 0.13), (0.7, 0))
                Line((0.89, 0), (0.7, 0))
                Line((0.89, 1.4), (0.89, 0))
                Line((0.89, 1.4), (0.7, 1.4))
            make_face()
            # Profile area: 0.1976, perimeter: 3.3
            with BuildLine():
                Line((0.51, 0), (0.51, 1.4))
                Line((0.7, 0), (0.51, 0))
                Line((0.7, 0.13), (0.7, 0))
                Line((0.7, 0.13), (0.64, 0.13))
                Line((0.64, 0.13), (0.64, 1.27))
                Line((0.64, 1.27), (0.7, 1.27))
                Line((0.7, 1.4), (0.7, 1.27))
                Line((0.7, 1.4), (0.51, 1.4))
            make_face()
            # Profile area: 0.224, perimeter: 3.12
            with BuildLine():
                Line((0.16, 0), (0, 0))
                Line((0.16, 1.4), (0.16, 0))
                Line((0, 1.4), (0.16, 1.4))
                Line((0, 0), (0, 1.4))
            make_face()
            # Profile area: 0.224, perimeter: 3.12
            with BuildLine():
                Line((1.24, 1.4), (1.24, 0))
                Line((1.24, 0), (1.4, 0))
                Line((1.4, 0), (1.4, 1.4))
                Line((1.4, 1.4), (1.24, 1.4))
            make_face()
        # OneSide extrude, distance=0.23
        extrude(amount=0.23, mode=Mode.ADD)

        # Sketch3 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 21 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -0.14, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0103868907, perimeter: 0.3612831552
            with Locations((0.335, 0.7)):
                Circle(0.0575)
            # Profile area: 0.0103868907, perimeter: 0.3612831552
            with Locations((1.065, 0.7)):
                Circle(0.0575)
        # OneSide extrude, distance=0.18
        extrude(amount=0.18, mode=Mode.ADD)
    return part.part


def model_21231_eb9826e5_0001():
    """Model: negative v2"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 22 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0602651255, perimeter: 5.9801642829
            with BuildLine():
                Line((0.9307695344, 0.6054944286), (0.9500000142, 0.6000000089))
                Line((0.9557050772, 0.6199677412), (0.9500000142, 0.6000000089))
                CenterArc((0.8403221984, 0.6529342589), 0.12, -15.9453871216, 46.8849846592)
                Line((0.5487700723, 1.3727213349), (0.9432473731, 0.7146303562))
                CenterArc((0.4458448977, 1.3110252376), 0.12, 30.9395975376, 42.3679857225)
                Line((0.0514893499, 1.5545598826), (0.4803129473, 1.4259684999))
                CenterArc((0.04, 1.5162454618), 0.04, 73.3075832601, 106.6924167399)
                Line((0, 0), (0, 1.5162454618))
                Line((0, 0), (0.02, 0))
                Line((0.02, 0), (0.02, 1.4893681927))
                CenterArc((0.06, 1.4893681927), 0.04, 73.3075832601, 106.6924167399)
                Line((0.0714893499, 1.5276826135), (0.4671438368, 1.4090376559))
                CenterArc((0.4326757871, 1.2940943936), 0.12, 30.9395975376, 42.3679857225)
                Line((0.5356009618, 1.3557904909), (0.9216344061, 0.711786066))
                CenterArc((0.8187092315, 0.6500899687), 0.12, -15.9453871216, 46.8849846592)
                Line((0.9340921103, 0.617123451), (0.9307695344, 0.6054944286))
            make_face()
        # OneSide extrude, distance=0.945
        extrude(amount=0.945)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.945, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 0.0246227019, perimeter: 2.5022701929
            with BuildLine():
                Line((0, -1.2311350964), (0, 0))
                Line((0, 0), (-0.02, 0))
                Line((-0.02, 0), (-0.02, -1.2311350964))
                Line((-0.02, -1.2311350964), (0, -1.2311350964))
            make_face()
        # TwoSides extrude, along=0.1, against=-1.045
        extrude(amount=0.1, mode=Mode.ADD)
        extrude(sk.sketch, amount=-1.045, mode=Mode.ADD)
    return part.part


def model_21231_eb9826e5_0011():
    """Model: Y1 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3631681108, perimeter: 2.1362830044
            Circle(0.34)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.061575216, perimeter: 0.879645943
            Circle(0.14)
        # OneSide extrude, distance=1.32
        extrude(amount=1.32, mode=Mode.ADD)
    return part.part


def model_21234_8b71bd47_0001():
    """Model: 13 Sec Base Screw v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.009456306, perimeter: 8.4783731739
            with BuildLine():
                CenterArc((0, 0), 0.79375, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.555625, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.9698697842, perimeter: 3.4910948363
            Circle(0.555625)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.9698697842, perimeter: 3.4910948363
            Circle(0.555625)
        # OneSide extrude, distance=-2.54
        extrude(amount=-2.54, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.635), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.2515949667, perimeter: 3.477116675
            with BuildLine():
                Line((-0.079375, 0.7897712782), (-0.079375, -0.7897712782))
                CenterArc((0, 0), 0.79375, -95.7391704773, 11.4783409545)
                Line((0.079375, -0.7897712782), (0.079375, 0.7897712782))
                CenterArc((0, 0), 0.79375, 84.2608295227, 11.4783409545)
            make_face()
            # Profile area: 0.0386168485, perimeter: 0.8095848858
            with BuildLine():
                CenterArc((0, 0), 0.79375, 84.2608295227, 11.4783409545)
                Line((0.079375, 0.7897712782), (0.079375, 1.0356808306))
                Line((0.079375, 1.0356808306), (-0.079375, 1.0356808306))
                Line((-0.079375, 1.0356808306), (-0.079375, 0.7897712782))
            make_face()
            # Profile area: 0.0386168485, perimeter: 0.8095848858
            with BuildLine():
                CenterArc((0, 0), 0.79375, -95.7391704773, 11.4783409545)
                Line((-0.079375, -0.7897712782), (-0.079375, -1.0356808306))
                Line((-0.079375, -1.0356808306), (0.079375, -1.0356808306))
                Line((0.079375, -1.0356808306), (0.079375, -0.7897712782))
            make_face()
        # OneSide extrude, distance=-0.238125
        extrude(amount=-0.238125, mode=Mode.SUBTRACT)
    return part.part


def model_21234_8b71bd47_0003():
    """Model: 3 Clamp Plate v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 22.177375, perimeter: 20.32
            with BuildLine():
                Line((0, 3.175), (0, 0))
                Line((0, 0), (6.985, 0))
                Line((6.985, 0), (6.985, 3.175))
                Line((6.985, 3.175), (0, 3.175))
            make_face()
        # OneSide extrude, distance=1.11125
        extrude(amount=1.11125)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1.11125, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.4300631002, perimeter: 4.2391865869
            with Locations((1.5875, 1.5875)):
                Circle(0.6746875)
            # Profile area: 1.4300631002, perimeter: 4.2391865869
            with Locations((5.3975, 1.5875)):
                Circle(0.6746875)
        # OneSide extrude, distance=-2.54
        extrude(amount=-2.54, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1.11125, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.6626339158, perimeter: 10.4732845089
            with BuildLine():
                CenterArc((1.5875, 1.5875), 0.9921875, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((1.5875, 1.5875), 0.6746875, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.6626339158, perimeter: 10.4732845089
            with BuildLine():
                CenterArc((5.3975, 1.5875), 0.9921875, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((5.3975, 1.5875), 0.6746875, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.635
        extrude(amount=-0.635, mode=Mode.SUBTRACT)
    return part.part


def model_21234_8b71bd47_0007():
    """Model: 14 Clamp plate Screw v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.5834608722, perimeter: 9.9745566751
            with BuildLine():
                CenterArc((0, 0), 0.9525, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.635, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            Circle(0.635)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            Circle(0.635)
        # OneSide extrude, distance=-2.06375
        extrude(amount=-2.06375, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.635), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.3020683628, perimeter: 4.1146164159
            with BuildLine():
                Line((-0.079375, -0.9491869465), (-0.079375, 0.9491869465))
                CenterArc((0, 0), 0.9525, -94.7801918472, 9.5603836944)
                Line((0.079375, 0.9491869465), (0.079375, -0.9491869465))
                CenterArc((0, 0), 0.9525, 85.2198081528, 9.5603836944)
            make_face()
        # OneSide extrude, distance=-0.238125
        extrude(amount=-0.238125, mode=Mode.SUBTRACT)
    return part.part


def model_21235_01764fc7_0012():
    """Model: 12-CLAMP SCREW v4 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.7125573925, perimeter: 2.9923670025
            Circle(0.47625)
        # OneSide extrude, distance=-3.81
        extrude(amount=-3.81)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.1376721774, perimeter: 8.9771010076
            with BuildLine():
                CenterArc((0, 0), 0.9525, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.47625, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.7125573925, perimeter: 2.9923670025
            Circle(0.47625)
        # OneSide extrude, distance=2.54
        extrude(amount=2.54, mode=Mode.ADD)
    return part.part


def model_21235_01764fc7_0025():
    """Model: 8-COLLAR v2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.6127104391, perimeter: 10.9720123427
            with BuildLine():
                CenterArc((0, 0), 1.11125, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.635, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.47625
        extrude(amount=-0.47625)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0316236138, perimeter: 0.6303919819
            with Locations((0, 0.2381250306)):
                Circle(0.10033)
        # OneSide extrude, distance=1.397
        extrude(amount=1.397, mode=Mode.SUBTRACT)
    return part.part


def model_21236_b696e901_0005():
    """Model: Battery v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.4805768544, perimeter: 4.3134067134
            Circle(0.6865)
        # OneSide extrude, distance=5.5
        extrude(amount=5.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0314159275, perimeter: 0.6283185401
            Circle(0.1000000015)
        # OneSide extrude, distance=0.15
        extrude(amount=0.15, mode=Mode.ADD)
    return part.part


def model_21236_b696e901_0008():
    """Model: Motor v7 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.9843134833, perimeter: 5.6457513111
            with BuildLine():
                Line((-0.75, -0.6614378278), (-0.75, 0.6614378278))
                Line((0.75, -0.6614378278), (-0.75, -0.6614378278))
                Line((0.75, 0.6614378278), (0.75, -0.6614378278))
                Line((-0.75, 0.6614378278), (0.75, 0.6614378278))
            make_face()
            # Profile area: 0.226655877, perimeter: 2.7683441512
            with BuildLine():
                CenterArc((0, 0), 1, 138.5903778907, 82.8192442185)
                Line((-0.75, -0.6614378278), (-0.75, 0.6614378278))
            make_face()
            # Profile area: 0.226655877, perimeter: 2.7683441512
            with BuildLine():
                CenterArc((0, 0), 1, -41.4096221093, 82.8192442185)
                Line((0.75, 0.6614378278), (0.75, -0.6614378278))
            make_face()
        # OneSide extrude, distance=2.515
        extrude(amount=2.515)
    return part.part


def model_21236_b696e901_0028():
    """Model: Pink Left B9 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 10.004843361, perimeter: 18.2661151204
            with BuildLine():
                CenterArc((6.3274609999, -2.8583385592), 0.3, -135, 90)
                Line((7.1073997795, -2.5026638482), (6.5395930342, -3.0704705935))
                CenterArc((6.8952677452, -2.2905318139), 0.3, -45, 90)
                Line((4.023, 1.006), (7.1073997795, -2.0783997795))
                Line((0.3, 1.006), (4.023, 1.006))
                CenterArc((0.3, 0.706), 0.3, 90, 90)
                Line((0, 0.3), (0, 0.706))
                CenterArc((0.3, 0.3), 0.3, 180, 90)
                Line((3.044858372, 0), (0.3, 0))
                Line((6.1153289655, -3.0704705935), (3.044858372, 0))
            make_face()
        # OneSide extrude, distance=0.252
        extrude(amount=0.252)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.252, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-6.6103037124, 2.5754958467)):
                Circle(0.25)
        # OneSide extrude, distance=0.289
        extrude(amount=0.289, mode=Mode.ADD)
    return part.part


def model_21237_7887a24b_0005():
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
    return part.part


def model_21242_6c2af7c2_0006():
    """Model: 2 CROSS FRAME v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 34 constraints, 16 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 78.1592447303, perimeter: 72.1228515596
            with BuildLine():
                Line((0.3050000376, -14.2), (-0.305, -14.2))
                CenterArc((6.555, -14.2006858876), 6.25, 130.4511880009, 49.5425242448)
                Line((2.5, -9.4446923005), (2.5, -8.65))
                Line((2.5, -8.65), (2.3, -8.65))
                CenterArc((2.3, -8.45), 0.2, 180, 90)
                Line((2.1, -8.45), (2.1, 5.25))
                CenterArc((2.3, 5.25), 0.2, 90, 90)
                Line((2.5, 5.45), (2.3, 5.45))
                Line((2.5, 6.2446923005), (2.5, 5.45))
                CenterArc((6.555, 11.0006858876), 6.2500000376, -179.9937122458, 49.5425242448)
                Line((-0.305, 11), (0.305, 11))
                CenterArc((-6.555, 11.0006858876), 6.25, -49.5488119991, 49.5425242448)
                Line((-2.5, 6.2446923005), (-2.5, 5.45))
                Line((-2.5, 5.45), (-2.3, 5.45))
                CenterArc((-2.3, 5.25), 0.2, 0, 90)
                Line((-2.1, 5.25), (-2.1, -8.45))
                CenterArc((-2.3, -8.45), 0.2, -90, 90)
                Line((-2.5, -8.65), (-2.3, -8.65))
                Line((-2.4999999756, -9.4446922719), (-2.5, -8.65))
                CenterArc((-6.555, -14.2006858876), 6.2500000376, 0.0062877542, 49.5425242448)
            make_face()
            with BuildLine():
                CenterArc((0, 6), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, -1.5), 0.65, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, -9), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.5
        extrude(amount=0.5, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 19.6726771039, perimeter: 22.4840704497
            with BuildLine():
                Line((-2.1, 1), (-2.1, -4))
                Line((2.1, -4), (-2.1, -4))
                Line((2.1, -4), (2.1, 1))
                Line((-2.1, 1), (2.1, 1))
            make_face()
            with BuildLine():
                CenterArc((0, -1.5), 0.65, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)
    return part.part


def model_21246_c66f2b12_0032():
    """Model: Front Wheel v2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            Circle(1.5)
        # OneSide extrude, distance=1.45
        extrude(amount=1.45)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.45, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.4636059006, perimeter: 6.5973445725
            Circle(1.05)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)
    return part.part


def model_21256_433456a3_0015():
    """Model: Top Frame v7"""
    with BuildPart() as part:
        # Sketch5 -> Extrude26 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 37 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9, perimeter: 31.2
            with BuildLine():
                Line((7.675, -6.35), (0.375, -6.35))
                Line((0.375, -6.95), (0.375, -6.35))
                Line((15.375, -6.95), (0.375, -6.95))
                Line((15.375, -6.35), (15.375, -6.95))
                Line((15.375, -6.35), (14.675, -6.35))
                Line((8.675, -6.35), (14.675, -6.35))
                Line((8.675, -6.35), (7.675, -6.35))
            make_face()
        # OneSide extrude, distance=0.912
        extrude(amount=0.912)

        # Sketch5 -> Extrude27 (Join)
        # Sketch on XZ construction plane
        # Sketch has 37 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.7, perimeter: 27.4
            with BuildLine():
                Line((8.675, 6.35), (8.675, -6.35))
                Line((7.675, 6.35), (8.675, 6.35))
                Line((7.675, -6.35), (7.675, 6.35))
                Line((8.675, -6.35), (7.675, -6.35))
            make_face()
        # OneSide extrude, distance=0.912
        extrude(amount=0.912, mode=Mode.ADD)

        # Sketch5 -> Extrude28 (Join)
        # Sketch on XZ construction plane
        # Sketch has 37 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9, perimeter: 31.2
            with BuildLine():
                Line((7.675, 6.35), (8.675, 6.35))
                Line((8.675, 6.35), (14.675, 6.35))
                Line((14.675, 6.35), (15.375, 6.35))
                Line((15.375, 6.35), (15.375, 6.95))
                Line((15.375, 6.95), (0.375, 6.95))
                Line((0.375, 6.95), (0.375, 6.35))
                Line((0.375, 6.35), (7.675, 6.35))
            make_face()
        # OneSide extrude, distance=0.912
        extrude(amount=0.912, mode=Mode.ADD)

        # Sketch5 -> Extrude29 (Join)
        # Sketch on XZ construction plane
        # Sketch has 37 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.89, perimeter: 26.8
            with BuildLine():
                Line((15.375, 6.35), (15.375, -6.35))
                Line((14.675, 6.35), (15.375, 6.35))
                Line((14.675, -6.35), (14.675, 6.35))
                Line((15.375, -6.35), (14.675, -6.35))
            make_face()
        # OneSide extrude, distance=0.912
        extrude(amount=0.912, mode=Mode.ADD)
    return part.part


def model_21338_d5c31ee8_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 18 constraints, 37 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 14.1164233013, perimeter: 21.0873578279
            with BuildLine():
                Line((-2.006673696, 0.2160421074), (1.993326304, 0.2160421074))
                Line((1.993326304, 0.2160421074), (1.993326304, -0.2839578926))
                Line((1.993326304, -0.2839578926), (2.493326304, -0.2839578926))
                Line((2.493326304, -0.2839578926), (2.9883010508, 0.2110168542))
                Line((2.9883010508, 0.2110168542), (2.9883010508, 0.7108577503))
                Line((2.9883010508, 0.7108577503), (2.6883974863, 0.7108577503))
                Line((2.6883974863, 0.7108577503), (2.6883974863, 1.2108577503))
                Line((2.6883974863, 1.2108577503), (3.5369256237, 2.0593858877))
                Line((3.5369256237, 2.0593858877), (3.5369256237, 2.5593858877))
                Line((3.5369256237, 2.5593858877), (1.9869256237, 2.5593858877))
                Line((1.9869256237, 2.5593858877), (1.9869256237, 2.2593858877))
                Line((1.9869256237, 2.2593858877), (-2.0006195523, 2.282706184))
                Line((-2.0006195523, 2.582706184), (-2.0006195523, 2.282706184))
                Line((-3.5506029581, 2.5755338905), (-2.0006195523, 2.582706184))
                Line((-3.5506029581, 2.0755338905), (-3.5506029581, 2.5755338905))
                Line((-2.7020748207, 1.2270057531), (-3.5506029581, 2.0755338905))
                Line((-2.7020748207, 0.7270057531), (-2.7020748207, 1.2270057531))
                Line((-3.0016484428, 0.7110168542), (-2.7020748207, 0.7270057531))
                Line((-3.0016484428, 0.2110168542), (-3.0016484428, 0.7110168542))
                Line((-2.506673696, -0.2839578926), (-3.0016484428, 0.2110168542))
                Line((-2.006673696, -0.2839578926), (-2.506673696, -0.2839578926))
                Line((-2.006673696, 0.2160421074), (-2.006673696, -0.2839578926))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.2, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.3948196461, perimeter: 8.4000001043
            with BuildLine():
                Line((-1.8000000268, 2.0000000298), (-1.1000000268, 0.7875644645))
                Line((-1.1000000268, 0.7875644645), (1.0000000253, 0.7875644645))
                Line((1.7000000253, 2.0000000298), (1.0000000253, 0.7875644645))
                Line((-1.8000000268, 2.0000000298), (1.7000000253, 2.0000000298))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)
    return part.part


def model_21385_601444ba_0008():
    """Model: Valve Spindle v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0991998016, perimeter: 1.25984
            with BuildLine():
                Line((0.15748, -0.15748), (0.15748, 0.15748))
                Line((0.15748, 0.15748), (-0.15748, 0.15748))
                Line((-0.15748, 0.15748), (-0.15748, -0.15748))
                Line((-0.15748, -0.15748), (0.15748, -0.15748))
            make_face()
        # OneSide extrude, distance=0.47498
        extrude(amount=0.47498)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.47498, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0438251299, perimeter: 0.7421070166
            Circle(0.11811)
        # OneSide extrude, distance=2.79908
        extrude(amount=2.79908, mode=Mode.ADD)
    return part.part


def model_21385_601444ba_0019():
    """Model: Grounding link mounting block v2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 13 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3409495047, perimeter: 4.1211636327
            with BuildLine():
                Line((-0.3672021884, 0.15748), (-0.71628, 0.15748))
                Line((-0.71628, 0.15748), (-0.71628, 0))
                Line((-0.71628, 0), (0.71628, 0))
                Line((0.71628, 0), (0.71628, 0.15748))
                Line((0.71628, 0.15748), (0.3610114676, 0.15748))
                CenterArc((0.3610117716, 0.3203719242), 0.1628919242, -179.9473207151, 89.9472137801)
                CenterArc((0, 0.32004), 0.19812, 0.0526793156, 178.9205516712)
                CenterArc((-0.3672021881, 0.3266211585), 0.1691411585, -90.0000001163, 88.9732286553)
            make_face()
            with BuildLine():
                CenterArc((0, 0.32004), 0.084709, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.47498
        extrude(amount=0.47498)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.15748), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0401362994, perimeter: 0.7101884353
            with Locations((0.5511800068, 0.23876)):
                Circle(0.11303)
            # Profile area: 0.0401362994, perimeter: 0.7101884353
            with Locations((-0.5587999932, 0.23876)):
                Circle(0.11303)
        # OneSide extrude, distance=-0.2286
        extrude(amount=-0.2286, mode=Mode.SUBTRACT)
    return part.part


def model_21385_601444ba_0024():
    """Model: CranshaftMount v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 11 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.9295921746, perimeter: 9.0698226703
            with BuildLine():
                CenterArc((0, 0.635), 0.6350000001, 0.0009295317, 179.9981409389)
                Line((-0.635, 0.6350103018), (-0.635, 0.635))
                Line((-0.635, 0.635), (-1.27, 0.635))
                Line((-1.27, 0.635), (-1.27, 0))
                Line((-1.27, 0), (1.27, 0))
                Line((1.27, 0), (1.27, 0.635))
                Line((1.27, 0.635), (0.635, 0.635))
                Line((0.635, 0.635), (0.635, 0.6350103019))
            make_face()
            with BuildLine():
                CenterArc((0, 0.635), 0.3175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.47498
        extrude(amount=0.47498)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.635, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0374760852, perimeter: 0.6862494993
            with Locations((1.0447632869, 0.23749)):
                Circle(0.10922)
            # Profile area: 0.0374760852, perimeter: 0.6862494993
            with Locations((-1.0447632869, 0.23749)):
                Circle(0.10922)
        # OneSide extrude, distance=-1.27
        extrude(amount=-1.27, mode=Mode.SUBTRACT)
    return part.part


def model_21385_601444ba_0029():
    """Model: Rocker Mount v5 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 11 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.1083995257, perimeter: 8.0520694852
            with BuildLine():
                CenterArc((0, 0.47752), 0.45974, -0.0003214704, 180.0006429426)
                Line((-0.45974, 0.4775174205), (-0.45974, 0.3175))
                Line((-0.45974, 0.3175), (-1.27, 0.3175))
                Line((-1.27, 0.3175), (-1.27, 0))
                Line((-1.27, 0), (1.27, 0))
                Line((1.27, 0), (1.27, 0.3175))
                Line((1.27, 0.3175), (0.45974, 0.3175))
                Line((0.45974, 0.4775174205), (0.45974, 0.3175))
            make_face()
            with BuildLine():
                CenterArc((0, 0.47752), 0.23749, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.47498
        extrude(amount=0.47498)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.3175), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0374760852, perimeter: 0.6862494993
            with Locations((-0.87122, 0.23749)):
                Circle(0.10922)
            # Profile area: 0.0374760852, perimeter: 0.6862494993
            with Locations((0.87122, 0.23749)):
                Circle(0.10922)
        # OneSide extrude, distance=-0.889
        extrude(amount=-0.889, mode=Mode.SUBTRACT)
    return part.part


def model_21541_abc67be6_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch14 -> Extrude5 (NewBody)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7131994316, perimeter: 2.9937148126
            with Locations((0.8501527824, 0)):
                Circle(0.4764645106)
        # OneSide extrude, distance=-2.286
        extrude(amount=-2.286)
    return part.part


MODELS = {
    "model_141771_d5c3e167_0005": {"func": model_141771_d5c3e167_0005, "volume": 40.957418085, "area": 227.5001311805},
    "model_142046_0977a838_0000": {"func": model_142046_0977a838_0000, "volume": 28.2743338823, "area": 51.8362787842},
    "model_142246_0851be5e_0003": {"func": model_142246_0851be5e_0003, "volume": 235.6194490192, "area": 251.3274122872},
    "model_142246_0851be5e_0013": {"func": model_142246_0851be5e_0013, "volume": 522.4277368589, "area": 688.1430491252},
    "model_142249_ba62bf08_0000": {"func": model_142249_ba62bf08_0000, "volume": 57.34375, "area": 99.3737373415},
    "model_142493_fc086676_0000": {"func": model_142493_fc086676_0000, "volume": 110.2738574976, "area": 227.2343339983},
    "model_142579_65b06d92_0000": {"func": model_142579_65b06d92_0000, "volume": 9.3172319795, "area": 30.4608743756},
    "model_142598_7e2d058b_0000": {"func": model_142598_7e2d058b_0000, "volume": 391.7687622775, "area": 322.6932855187},
    "model_142659_3e42350b_0005": {"func": model_142659_3e42350b_0005, "volume": 5.1139708642, "area": 20.2291172409},
    "model_142680_cd829f9e_0001": {"func": model_142680_cd829f9e_0001, "volume": 126.6454867982, "area": 361.7619467106},
    "model_142816_3c2c9eff_0000": {"func": model_142816_3c2c9eff_0000, "volume": 450, "area": 990},
    "model_142852_00b5fde9_0000": {"func": model_142852_00b5fde9_0000, "volume": 76.8143625, "area": 203.7551201095},
    "model_142852_65dcbe39_0001": {"func": model_142852_65dcbe39_0001, "volume": 181.7957689212, "area": 300.7163455562},
    "model_142852_f2535e8d_0001": {"func": model_142852_f2535e8d_0001, "volume": 120.854597, "area": 219.3544},
    "model_142918_43d48127_0000": {"func": model_142918_43d48127_0000, "volume": 40.521845835, "area": 96.0963946516},
    "model_142918_43d48127_0001": {"func": model_142918_43d48127_0001, "volume": 6.9559261803, "area": 28.990896723},
    "model_142959_e000cbf1_0000": {"func": model_142959_e000cbf1_0000, "volume": 56.9022075273, "area": 241.1141462477},
    "model_142992_3bd10abe_0000": {"func": model_142992_3bd10abe_0000, "volume": 79.4855634268, "area": 558.6367070862},
    "model_143054_09a08890_0002": {"func": model_143054_09a08890_0002, "volume": 97.2251149263, "area": 146.1245322965},
    "model_143158_794f6243_0000": {"func": model_143158_794f6243_0000, "volume": 1027.6759244575, "area": 978.7146218036},
    "model_143293_fc5b0ff7_0020": {"func": model_143293_fc5b0ff7_0020, "volume": 26.7379229962, "area": 127.3650147033},
    "model_143309_c7a044ee_0000": {"func": model_143309_c7a044ee_0000, "volume": 20.8634883091, "area": 170.2497161652},
    "model_143481_e8d7fe93_0000": {"func": model_143481_e8d7fe93_0000, "volume": 0.1138325019, "area": 2.4196676366},
    "model_143509_1dd5212d_0008": {"func": model_143509_1dd5212d_0008, "volume": 0.8779504212, "area": 11.6526391936},
    "model_143815_c616f1b4_0003": {"func": model_143815_c616f1b4_0003, "volume": 0.0914007113, "area": 1.8810286013},
    "model_143815_c616f1b4_0005": {"func": model_143815_c616f1b4_0005, "volume": 0.2050309798, "area": 3.6901327642},
    "model_143967_d7e408c9_0000": {"func": model_143967_d7e408c9_0000, "volume": 95.9560206131, "area": 149.1471112292},
    "model_144259_1a9370ba_0000": {"func": model_144259_1a9370ba_0000, "volume": 89647.6264780876, "area": 14420.5529427553},
    "model_144276_ff01151b_0000": {"func": model_144276_ff01151b_0000, "volume": 90.9704964476, "area": 218.2701281483},
    "model_144333_c6cc0474_0000": {"func": model_144333_c6cc0474_0000, "volume": 22.9776, "area": 191.302},
    "model_144531_0c361490_0000": {"func": model_144531_0c361490_0000, "volume": 7.8105867948, "area": 26.3750730238},
    "model_144588_fec64eef_0000": {"func": model_144588_fec64eef_0000, "volume": 40.5, "area": 78.6246117975},
    "model_144781_a0ee9ef1_0000": {"func": model_144781_a0ee9ef1_0000, "volume": 0.1159758469, "area": 1.6777379681},
    "model_144781_a0ee9ef1_0002": {"func": model_144781_a0ee9ef1_0002, "volume": 0.1739785187, "area": 2.0577446182},
    "model_145040_e65b11d2_0000": {"func": model_145040_e65b11d2_0000, "volume": 11.5510543808, "area": 61.5723098861},
    "model_145119_24107428_0000": {"func": model_145119_24107428_0000, "volume": 59.0296096679, "area": 127.2660493475},
    "model_145119_24107428_0001": {"func": model_145119_24107428_0001, "volume": 4.7449492355, "area": 34.356251532},
    "model_145119_24107428_0004": {"func": model_145119_24107428_0004, "volume": 186.4325612524, "area": 259.5211009757},
    "model_145119_24107428_0006": {"func": model_145119_24107428_0006, "volume": 179.9433635766, "area": 342.8529836878},
    "model_145119_24107428_0007": {"func": model_145119_24107428_0007, "volume": 369.7425316399, "area": 617.6470097055},
    "model_145119_24107428_0008": {"func": model_145119_24107428_0008, "volume": 126.0807161403, "area": 232.5000511225},
    "model_145121_2b2a370d_0000": {"func": model_145121_2b2a370d_0000, "volume": 12.4223152739, "area": 46.2832035386},
    "model_145121_2b2a370d_0001": {"func": model_145121_2b2a370d_0001, "volume": 34.6829880897, "area": 81.1116642636},
    "model_145176_dc7a828b_0002": {"func": model_145176_dc7a828b_0002, "volume": 55.5604188774, "area": 134.4832363692},
    "model_145201_a104c55b_0001": {"func": model_145201_a104c55b_0001, "volume": 65494734.1458248645, "area": 12619568.4596945941},
    "model_145257_89235edd_0005": {"func": model_145257_89235edd_0005, "volume": 2.8343214543, "area": 19.2464399427},
    "model_145368_8e40c6f0_0000": {"func": model_145368_8e40c6f0_0000, "volume": 0.7454581636, "area": 10.5696205919},
    "model_145368_8e40c6f0_0001": {"func": model_145368_8e40c6f0_0001, "volume": 6.559086276, "area": 36.8272044579},
    "model_145540_a4f54d5f_0002": {"func": model_145540_a4f54d5f_0002, "volume": 3039.79072, "area": 2277.3856},
    "model_145540_a4f54d5f_0012": {"func": model_145540_a4f54d5f_0012, "volume": 1589.4906911809, "area": 1010.8814207995},
    "model_145619_8e3238eb_0003": {"func": model_145619_8e3238eb_0003, "volume": 0.1052220866, "area": 1.5922208656},
    "model_145619_8e3238eb_0005": {"func": model_145619_8e3238eb_0005, "volume": 0.2086197221, "area": 2.9848711625},
    "model_145702_e28c737e_0044": {"func": model_145702_e28c737e_0044, "volume": 29.1579068161, "area": 67.1515429705},
    "model_146102_93e433ac_0004": {"func": model_146102_93e433ac_0004, "volume": 0.9517719616, "area": 7.832971369},
    "model_146157_bfd67e48_0000": {"func": model_146157_bfd67e48_0000, "volume": 77.9343985981, "area": 413.4448973608},
    "model_146171_ae42d34e_0000": {"func": model_146171_ae42d34e_0000, "volume": 183.0796132582, "area": 534.7294191377},
    "model_146191_c64404bd_0000": {"func": model_146191_c64404bd_0000, "volume": 16.3452700925, "area": 41.2696912389},
    "model_146226_5cf38887_0001": {"func": model_146226_5cf38887_0001, "volume": 5.9140171663, "area": 33.1602610161},
    "model_146291_6b0c8db3_0003": {"func": model_146291_6b0c8db3_0003, "volume": 0.0000024903, "area": 0.0019859858},
    "model_146544_67c41937_0000": {"func": model_146544_67c41937_0000, "volume": 503.7942495883, "area": 524.1371669412},
    "model_146545_f266050f_0000": {"func": model_146545_f266050f_0000, "volume": 30.0277914325, "area": 146.4457907501},
    "model_146617_2c247f85_0024": {"func": model_146617_2c247f85_0024, "volume": 10.781160589, "area": 42.4586247133},
    "model_146617_2c247f85_0026": {"func": model_146617_2c247f85_0026, "volume": 3.7760631184, "area": 24.3567784407},
    "model_146618_b2f1a4f4_0000": {"func": model_146618_b2f1a4f4_0000, "volume": 40.1946209224, "area": 76.1333007177},
    "model_146618_b2f1a4f4_0001": {"func": model_146618_b2f1a4f4_0001, "volume": 2.2232760384, "area": 12.4937580807},
    "model_146640_89ef3723_0000": {"func": model_146640_89ef3723_0000, "volume": 89.3160017537, "area": 212.5293357571},
    "model_146640_89ef3723_0001": {"func": model_146640_89ef3723_0001, "volume": 1.4068963827, "area": 7.4551635191},
    "model_146640_89ef3723_0002": {"func": model_146640_89ef3723_0002, "volume": 2.7787574014, "area": 11.9014378861},
    "model_146805_0416c8ff_0002": {"func": model_146805_0416c8ff_0002, "volume": 3.258787756, "area": 26.0087827863},
    "model_146827_44b163c8_0001": {"func": model_146827_44b163c8_0001, "volume": 173.1802950291, "area": 197.9203371762},
    "model_146888_62f0c3fe_0002": {"func": model_146888_62f0c3fe_0002, "volume": 1.2, "area": 14},
    "model_147022_9b03d096_0000": {"func": model_147022_9b03d096_0000, "volume": 561.1319284469, "area": 988.9317385093},
    "model_147022_9b03d096_0001": {"func": model_147022_9b03d096_0001, "volume": 50.3517934453, "area": 116.6932910666},
    "model_147082_c6f4f6a5_0000": {"func": model_147082_c6f4f6a5_0000, "volume": 143.6065465237, "area": 382.7061388436},
    "model_147133_92c04b84_0002": {"func": model_147133_92c04b84_0002, "volume": 1.319079693, "area": 11.8846015352},
    "model_147134_273aac81_0001": {"func": model_147134_273aac81_0001, "volume": 69.7380532894, "area": 133.6176980266},
    "model_147650_74de1acb_0000": {"func": model_147650_74de1acb_0000, "volume": 0.444079795, "area": 3.7144500162},
    "model_147853_e92074c2_0008": {"func": model_147853_e92074c2_0008, "volume": 152.7380400449, "area": 358.2583771849},
    "model_148024_0fa50126_0000": {"func": model_148024_0fa50126_0000, "volume": 58.3529326833, "area": 285.7260261431},
    "model_148051_ad8f6d60_0000": {"func": model_148051_ad8f6d60_0000, "volume": 1.489274352, "area": 22.1183437517},
    "model_20232_e5b060d9_0002": {"func": model_20232_e5b060d9_0002, "volume": 1.2833213949, "area": 6.7582485429},
    "model_20241_6bced5ac_0000": {"func": model_20241_6bced5ac_0000, "volume": 159.773874, "area": 229.0318},
    "model_20849_9821b6fe_0000": {"func": model_20849_9821b6fe_0000, "volume": 0.7311722367, "area": 9.9641378804},
    "model_21231_eb9826e5_0000": {"func": model_21231_eb9826e5_0000, "volume": 0.4720752807, "area": 7.6676619359},
    "model_21231_eb9826e5_0001": {"func": model_21231_eb9826e5_0001, "volume": 0.061875084, "area": 6.2722395369},
    "model_21231_eb9826e5_0011": {"func": model_21231_eb9826e5_0011, "volume": 0.1539129073, "area": 2.3147254672},
    "model_21234_8b71bd47_0001": {"func": model_21234_8b71bd47_0001, "volume": 3.6604302678, "area": 16.6694806858},
    "model_21234_8b71bd47_0003": {"func": model_21234_8b71bd47_0003, "volume": 19.3547476555, "area": 73.1702271842},
    "model_21234_8b71bd47_0007": {"func": model_21234_8b71bd47_0007, "volume": 4.352259648, "area": 18.5631698674},
    "model_21235_01764fc7_0012": {"func": model_21235_01764fc7_0012, "volume": 9.954426773, "area": 32.3026017925},
    "model_21235_01764fc7_0025": {"func": model_21235_01764fc7_0025, "volume": 1.2292155939, "area": 10.6888265425},
    "model_21236_b696e901_0005": {"func": model_21236_b696e901_0005, "volume": 8.1478850881, "area": 26.7791384133},
    "model_21236_b696e901_0008": {"func": model_21236_b696e901_0008, "volume": 6.1306274717, "area": 19.6909570076},
    "model_21236_b696e901_0028": {"func": model_21236_b696e901_0028, "volume": 2.5779655443, "area": 25.0667078709},
    "model_21237_7887a24b_0005": {"func": model_21237_7887a24b_0005, "volume": 0.9550441667, "area": 12.8491139532},
    "model_21242_6c2af7c2_0006": {"func": model_21242_6c2af7c2_0006, "volume": 68.3229075815, "area": 225.5993067324},
    "model_21246_c66f2b12_0032": {"func": model_21246_c66f2b12_0032, "volume": 11.6348883926, "area": 30.4420328133},
    "model_21256_433456a3_0015": {"func": model_21256_433456a3_0015, "volume": 36.10608, "area": 179.3176},
    "model_21338_d5c31ee8_0000": {"func": model_21338_d5c31ee8_0000, "volume": 2.1443207311, "area": 27.340678897},
    "model_21385_601444ba_0008": {"func": model_21385_601444ba_0008, "volume": 0.1697879663, "area": 2.8740153145},
    "model_21385_601444ba_0019": {"func": model_21385_601444ba_0019, "volume": 0.1493028669, "area": 2.7025050636},
    "model_21385_601444ba_0024": {"func": model_21385_601444ba_0024, "volume": 0.8689230629, "area": 8.8888012446},
    "model_21385_601444ba_0029": {"func": model_21385_601444ba_0029, "volume": 0.5026702926, "area": 6.3272351068},
    "model_21541_abc67be6_0000": {"func": model_21541_abc67be6_0000, "volume": 1.6303739006, "area": 8.2700309248},
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
