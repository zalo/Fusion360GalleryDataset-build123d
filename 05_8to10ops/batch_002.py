"""Batch 002 - passing/05_8to10ops
58 models bundled from Fusion360 Gallery reconstructions.
"""

from build123d import *
from build123d import Edge, BuildLine
from collections import Counter
from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
from OCP.Geom import Geom_BSplineCurve
from OCP.TColStd import TColStd_Array1OfReal, TColStd_Array1OfInteger
from OCP.TColgp import TColgp_Array1OfPnt
from OCP.gp import gp_Pnt


def model_131580_430d48a6_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.5, perimeter: 15
            with BuildLine():
                Line((2.5, 0), (5, 0))
                Line((2.5, -5), (2.5, 0))
                Line((5, -5), (2.5, -5))
                Line((5, 0), (5, -5))
            make_face()
            # Profile area: 12.5, perimeter: 15
            with BuildLine():
                Line((0, 0), (2.5, 0))
                Line((0, -5), (0, 0))
                Line((2.5, -5), (0, -5))
                Line((2.5, -5), (2.5, 0))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 7.0873412263, perimeter: 13.1698729811
            with BuildLine():
                Line((0, 5), (0, 0))
                Line((0, 0), (2.5, 4.3301270189))
                Line((2.5, 4.3301270189), (2.5, 5))
                Line((0, 5), (2.5, 5))
            make_face()
        # OneSide extrude, distance=-5
        extrude(amount=-5, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 7.0873412263, perimeter: 13.1698729811
            with BuildLine():
                Line((5, 5), (2.5, 5))
                Line((2.5, 5), (2.5, 4.3301270189))
                Line((2.5, 4.3301270189), (5, 0))
                Line((5, 0), (5, 5))
            make_face()
        # OneSide extrude, distance=-5
        extrude(amount=-5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 9 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(3.75, 2.1650635095, 0), x_dir=(0, 0, -1), z_dir=(0.8660254038, 0.5, 0))):
            # Profile area: 12.25, perimeter: 14
            with BuildLine():
                Line((-4.25, -1.75), (-0.75, -1.75))
                Line((-0.75, -1.75), (-0.75, 1.75))
                Line((-0.75, 1.75), (-4.25, 1.75))
                Line((-4.25, 1.75), (-4.25, -1.75))
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(3.4901923789, 2.0150635095, 0), x_dir=(0, 0, -1), z_dir=(0.8660254038, 0.5, 0))):
            # Profile area: 8.1562415863, perimeter: 11.4253327144
            with BuildLine():
                Line((-3.9234132322, 1.4520347871), (-3.9234132322, -1.4532641032))
                Line((-3.9234132322, -1.4532641032), (-1.1160457652, -1.4532641032))
                Line((-1.1160457652, -1.4532641032), (-1.1160457652, 1.4520347871))
                Line((-1.1160457652, 1.4520347871), (-3.9234132322, 1.4520347871))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


def model_131656_7da36cb9_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 36, perimeter: 24
            with BuildLine():
                Line((6, -6), (0, -6))
                Line((6, 0), (6, -6))
                Line((0, 0), (6, 0))
                Line((0, -6), (0, 0))
            make_face()
        # OneSide extrude, distance=6
        extrude(amount=6)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(6, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 20.4115427319, perimeter: 30
            with BuildLine():
                Line((-6, 6), (-6, 0))
                Line((-6, 0), (-3, 5.1961524227))
                Line((-3, 5.1961524227), (0, 0))
                Line((0, 0), (0, 6))
                Line((0, 6), (-3, 6))
                Line((-6, 6), (-3, 6))
            make_face()
        # OneSide extrude, distance=-10
        extrude(amount=-10, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 12.25, perimeter: 14
            with BuildLine():
                Line((1.25, 4.75), (1.25, 1.25))
                Line((1.25, 1.25), (4.75, 1.25))
                Line((4.75, 1.25), (4.75, 4.75))
                Line((4.75, 4.75), (1.25, 4.75))
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.2, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 10.1928424786, perimeter: 12.7704925378
            with BuildLine():
                Line((4.5923932528, 1.3909961114), (1.3997701184, 1.3909961114))
                Line((4.5923932528, 4.5836192459), (4.5923932528, 1.3909961114))
                Line((1.3997701184, 4.5836192459), (4.5923932528, 4.5836192459))
                Line((1.3997701184, 1.3909961114), (1.3997701184, 4.5836192459))
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0.5, -0.8660254038))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-5, 3)):
                Circle(0.25)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


def model_132217_356cdf43_0000():
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
        # Sketch has 29 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.2984419364, perimeter: 8.9467833399
            with BuildLine():
                Line((0, 0), (1.2, 0))
                Line((1.2, 0), (1.2, 2.3))
                _nurbs_edge([(1.2, 2.3), (1.2365770778, 2.3144964835), (1.3053221794, 2.3428802391), (1.3952122946, 2.3836281859), (1.4881786892, 2.4342437155), (1.5568611419, 2.4909463883), (1.5748672701, 2.540646969), (1.5400182998, 2.5830444101), (1.4540859902, 2.6183835209), (1.3214377653, 2.6472677605), (1.1468305394, 2.6703544055), (0.9768456246, 2.6846372039), (0.8334915446, 2.693157136), (0.7309865151, 2.6978787732), (0.678, 2.7)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                Line((0.45, 2.7), (0.678, 2.7))
                Line((0.45, 1.5), (0.45, 2.7))
                Line((0.8, 1.5), (0.45, 1.5))
                Line((0.8, 0.9), (0.8, 1.5))
                Line((0, 0.9), (0.8, 0.9))
                Line((0, 0), (0, 0.9))
            make_face()
            # Profile area: 2.2984419364, perimeter: 8.9467833399
            with BuildLine():
                Line((0, 0), (0, 0.9))
                Line((0, 0.9), (-0.8, 0.9))
                Line((-0.8, 0.9), (-0.8, 1.5))
                Line((-0.8, 1.5), (-0.45, 1.5))
                Line((-0.45, 1.5), (-0.45, 2.7))
                Line((-0.45, 2.7), (-0.678, 2.7))
                _nurbs_edge([(-1.2, 2.3), (-1.2365770778, 2.3144964835), (-1.3053221794, 2.3428802391), (-1.3952122946, 2.3836281859), (-1.4881786892, 2.4342437155), (-1.5568611419, 2.4909463883), (-1.5748672701, 2.540646969), (-1.5400182998, 2.5830444101), (-1.4540859902, 2.6183835209), (-1.3214377653, 2.6472677605), (-1.1468305394, 2.6703544055), (-0.9768456246, 2.6846372039), (-0.8334915446, 2.693157136), (-0.7309865151, 2.6978787732), (-0.678, 2.7)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                Line((-1.2, 0), (-1.2, 2.3))
                Line((0, 0), (-1.2, 0))
            make_face()
        # Symmetric extrude, each_side=12.673
        extrude(amount=12.673, both=True)

        # Sketch6 -> Extrude2 (Cut)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 1.425, perimeter: 5.1531714102
            with BuildLine():
                Line((0.289, 2.7), (0.289, 1.5))
                Line((0.289, 2.7), (-0.386, 2.7))
                Line((-0.386, 2.7), (-1.411, 1.5))
                Line((0.289, 1.5), (-1.411, 1.5))
            make_face()
        # Symmetric extrude, each_side=0.8
        extrude(amount=0.8, both=True, mode=Mode.SUBTRACT)
    return part.part


def model_132464_8dc52066_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch6 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 31.8264335891, perimeter: 21
            with BuildLine():
                Line((-3.5, 0), (0, 0))
                Line((0, 0), (1.75, 3.0310889132))
                Line((1.75, 3.0310889132), (0, 6.0621778265))
                Line((0, 6.0621778265), (-3.5, 6.0621778265))
                Line((-3.5, 6.0621778265), (-5.25, 3.0310889132))
                Line((-5.25, 3.0310889132), (-3.5, 0))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


def model_132949_ac3b23b9_0000():
    """Model: servo"""
    with BuildPart() as part:
        # Body -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.84375, perimeter: 7.05
            with BuildLine():
                Line((-0.625, 1.1375), (0.625, 1.1375))
                Line((-0.625, -1.1375), (-0.625, 1.1375))
                Line((0.625, -1.1375), (-0.625, -1.1375))
                Line((0.625, 1.1375), (0.625, -1.1375))
            make_face()
        # OneSide extrude, distance=2.235
        extrude(amount=2.235)

        # Tab -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.1375), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.33125, perimeter: 3.03
            with BuildLine():
                Line((-0.625, 1.82), (0.625, 1.82))
                Line((-0.625, 1.555), (-0.625, 1.82))
                Line((0.625, 1.555), (-0.625, 1.555))
                Line((0.625, 1.82), (0.625, 1.555))
            make_face()
        # OneSide extrude, distance=0.485
        extrude(amount=0.485, mode=Mode.ADD)

        # Bump -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.235, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.211950375, perimeter: 4.1338468684
            with BuildLine():
                CenterArc((0, -0.0625), 0.28, 180, 180)
                Line((0.28, 0.0267101704), (0.28, -0.0625))
                CenterArc((0, 0.5375), 0.5825, -61.2697392283, 302.5394784566)
                Line((-0.28, -0.0625), (-0.28, 0.0267101704))
            make_face()
        # OneSide extrude, distance=0.43
        extrude(amount=0.43, mode=Mode.ADD)

        # Wire -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.1375), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0396, perimeter: 0.94
            with BuildLine():
                Line((0.18, 0.44), (-0.18, 0.44))
                Line((0.18, 0.55), (0.18, 0.44))
                Line((-0.18, 0.55), (0.18, 0.55))
                Line((-0.18, 0.44), (-0.18, 0.55))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


def model_133113_e6041880_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 22 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 260.9436686977, perimeter: 63.6798226701
            with BuildLine():
                CenterArc((0.635, -0.635), 0.635, 90, 90)
                Line((0, -16.51), (0, -0.635))
                CenterArc((0.635, -16.51), 0.635, 180, 90)
                Line((14.605, -17.145), (0.635, -17.145))
                CenterArc((14.605, -16.51), 0.635, -90, 90)
                Line((15.24, -0.635), (15.24, -16.51))
                CenterArc((14.605, -0.635), 0.635, 0, 90)
                Line((0.635, 0), (14.605, 0))
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0.635, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 60.3108576996, perimeter: 27.5297764234
            with Locations((-7.62, 7.6716287675)):
                Circle(4.3815)
        # OneSide extrude, distance=-0.29972
        extrude(amount=-0.29972, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.635, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 10.9448815485, perimeter: 57.4534464489
            with BuildLine():
                CenterArc((-7.62, 7.6716287675), 4.7625, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-7.62, 7.6716287675), 4.3815, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1143
        extrude(amount=0.1143, mode=Mode.ADD)

        # Sketch5 -> Extrude4 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0.635, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0791730436, perimeter: 0.9974556675
            with Locations((-3.175, 15.113)):
                Circle(0.15875)
            # Profile area: 0.0791730436, perimeter: 0.9974556675
            with Locations((-12.065, 15.113)):
                Circle(0.15875)
        # OneSide extrude, distance=-0.381
        extrude(amount=-0.381, mode=Mode.SUBTRACT)
    return part.part


def model_133248_a739c5b6_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 117 constraints, 40 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 27.3, perimeter: 182
            with BuildLine():
                Line((29.8, -16.3), (0, -16.3))
                Line((29.8, 0), (29.8, -16.3))
                Line((0, 0), (29.8, 0))
                Line((0, -16.3), (0, 0))
            make_face()
            with BuildLine():
                Line((14.2, -0.3), (29.5, -0.3))
                Line((29.5, -0.3), (29.5, -16))
                Line((29.5, -16), (14.2, -16))
                Line((14.2, -16), (13.9, -16))
                Line((13.9, -16), (8.7, -16))
                Line((8.4, -16), (8.7, -16))
                Line((8.4, -16), (3.2, -16))
                Line((3.2, -16), (2.9, -16))
                Line((2.9, -16), (0.3, -16))
                Line((0.3, -16), (0.3, -0.3))
                Line((0.3, -0.3), (2.9, -0.3))
                Line((2.9, -0.3), (3.2, -0.3))
                Line((3.2, -0.3), (8.4, -0.3))
                Line((8.4, -0.3), (8.7, -0.3))
                Line((8.7, -0.3), (13.9, -0.3))
                Line((13.9, -0.3), (14.2, -0.3))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=6.4
        extrude(amount=6.4)

        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 117 constraints, 40 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 27.3, perimeter: 182
            with BuildLine():
                Line((29.8, -16.3), (0, -16.3))
                Line((29.8, 0), (29.8, -16.3))
                Line((0, 0), (29.8, 0))
                Line((0, -16.3), (0, 0))
            make_face()
            with BuildLine():
                Line((14.2, -0.3), (29.5, -0.3))
                Line((29.5, -0.3), (29.5, -16))
                Line((29.5, -16), (14.2, -16))
                Line((14.2, -16), (13.9, -16))
                Line((13.9, -16), (8.7, -16))
                Line((8.4, -16), (8.7, -16))
                Line((8.4, -16), (3.2, -16))
                Line((3.2, -16), (2.9, -16))
                Line((2.9, -16), (0.3, -16))
                Line((0.3, -16), (0.3, -0.3))
                Line((0.3, -0.3), (2.9, -0.3))
                Line((2.9, -0.3), (3.2, -0.3))
                Line((3.2, -0.3), (8.4, -0.3))
                Line((8.4, -0.3), (8.7, -0.3))
                Line((8.7, -0.3), (13.9, -0.3))
                Line((13.9, -0.3), (14.2, -0.3))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 240.21, perimeter: 62
            with BuildLine():
                Line((14.2, -0.3), (14.2, -4.4))
                Line((14.2, -6.4), (14.2, -4.4))
                Line((14.2, -6.4), (14.2, -16))
                Line((29.5, -16), (14.2, -16))
                Line((29.5, -0.3), (29.5, -16))
                Line((14.2, -0.3), (29.5, -0.3))
            make_face()
            # Profile area: 1.23, perimeter: 8.8
            with BuildLine():
                Line((13.9, -0.3), (14.2, -0.3))
                Line((13.9, -4.4), (13.9, -0.3))
                Line((14.2, -4.4), (13.9, -4.4))
                Line((14.2, -0.3), (14.2, -4.4))
            make_face()
            # Profile area: 109.14, perimeter: 41.8
            with BuildLine():
                Line((8.7, -0.3), (13.9, -0.3))
                Line((8.4, -0.3), (8.7, -0.3))
                Line((3.2, -0.3), (8.4, -0.3))
                Line((3.2, -0.3), (3.2, -1.108))
                Line((3.2, -1.108), (3.2, -1.608))
                Line((3.2, -1.608), (3.2, -2.108))
                Line((3.2, -2.108), (3.2, -3.725))
                Line((3.2, -4.225), (3.2, -3.725))
                Line((3.2, -4.225), (3.2, -4.725))
                Line((3.2, -4.725), (3.2, -6.342))
                Line((3.2, -6.842), (3.2, -6.342))
                Line((3.2, -6.842), (3.2, -7.342))
                Line((3.2, -7.342), (3.2, -8.959))
                Line((3.2, -9.459), (3.2, -8.959))
                Line((3.2, -9.459), (3.2, -9.959))
                Line((3.2, -9.959), (3.2, -10.5))
                Line((4.8, -10.5), (3.2, -10.5))
                Line((4.8, -10.5), (6.8, -10.5))
                Line((10.3, -10.5), (6.8, -10.5))
                Line((10.3, -10.5), (12.3, -10.5))
                Line((13.9, -10.5), (12.3, -10.5))
                Line((13.9, -10.5), (13.9, -6.4))
                Line((13.9, -4.4), (13.9, -6.4))
                Line((13.9, -4.4), (13.9, -0.3))
            make_face()
            # Profile area: 0.2424, perimeter: 2.216
            with BuildLine():
                Line((2.9, -1.108), (2.9, -0.3))
                Line((2.9, -1.108), (3.2, -1.108))
                Line((3.2, -0.3), (3.2, -1.108))
                Line((2.9, -0.3), (3.2, -0.3))
            make_face()
            # Profile area: 40.82, perimeter: 36.6
            with BuildLine():
                Line((2.9, -16), (2.9, -15.193))
                Line((2.9, -15.193), (2.9, -14.693))
                Line((2.9, -14.193), (2.9, -14.693))
                Line((2.9, -14.193), (2.9, -12.576))
                Line((2.9, -12.576), (2.9, -12.076))
                Line((2.9, -11.576), (2.9, -12.076))
                Line((2.9, -11.576), (2.9, -9.959))
                Line((2.9, -9.959), (2.9, -9.459))
                Line((2.9, -8.959), (2.9, -9.459))
                Line((2.9, -8.959), (2.9, -7.342))
                Line((2.9, -7.342), (2.9, -6.842))
                Line((2.9, -6.342), (2.9, -6.842))
                Line((2.9, -6.342), (2.9, -4.725))
                Line((2.9, -4.725), (2.9, -4.225))
                Line((2.9, -3.725), (2.9, -4.225))
                Line((2.9, -3.725), (2.9, -2.108))
                Line((2.9, -2.108), (2.9, -1.608))
                Line((2.9, -1.608), (2.9, -1.108))
                Line((2.9, -1.108), (2.9, -0.3))
                Line((0.3, -0.3), (2.9, -0.3))
                Line((0.3, -16), (0.3, -0.3))
                Line((2.9, -16), (0.3, -16))
            make_face()
            # Profile area: 0.2421, perimeter: 2.214
            with BuildLine():
                Line((3.2, -15.193), (3.2, -16))
                Line((3.2, -15.193), (2.9, -15.193))
                Line((2.9, -16), (2.9, -15.193))
                Line((3.2, -16), (2.9, -16))
            make_face()
            # Profile area: 27.04, perimeter: 20.8
            with BuildLine():
                Line((8.4, -10.8), (8.4, -16))
                Line((6.8, -10.8), (8.4, -10.8))
                Line((6.8, -10.8), (4.8, -10.8))
                Line((3.2, -10.8), (4.8, -10.8))
                Line((3.2, -10.8), (3.2, -11.576))
                Line((3.2, -12.076), (3.2, -11.576))
                Line((3.2, -12.076), (3.2, -12.576))
                Line((3.2, -12.576), (3.2, -14.193))
                Line((3.2, -14.693), (3.2, -14.193))
                Line((3.2, -14.693), (3.2, -15.193))
                Line((3.2, -15.193), (3.2, -16))
                Line((8.4, -16), (3.2, -16))
            make_face()
            # Profile area: 1.56, perimeter: 11
            with BuildLine():
                Line((8.7, -16), (8.7, -10.8))
                Line((8.7, -10.8), (8.4, -10.8))
                Line((8.4, -10.8), (8.4, -16))
                Line((8.4, -16), (8.7, -16))
            make_face()
            # Profile area: 27.04, perimeter: 20.8
            with BuildLine():
                Line((13.9, -16), (13.9, -10.8))
                Line((12.3, -10.8), (13.9, -10.8))
                Line((12.3, -10.8), (10.3, -10.8))
                Line((8.7, -10.8), (10.3, -10.8))
                Line((8.7, -16), (8.7, -10.8))
                Line((13.9, -16), (8.7, -16))
            make_face()
            # Profile area: 2.88, perimeter: 19.8
            with BuildLine():
                Line((14.2, -6.4), (14.2, -16))
                Line((13.9, -6.4), (14.2, -6.4))
                Line((13.9, -10.5), (13.9, -6.4))
                Line((13.9, -10.8), (13.9, -10.5))
                Line((13.9, -16), (13.9, -10.8))
                Line((14.2, -16), (13.9, -16))
            make_face()
            # Profile area: 0.6, perimeter: 4.6
            with BuildLine():
                Line((13.9, -4.4), (13.9, -6.4))
                Line((13.9, -6.4), (14.2, -6.4))
                Line((14.2, -6.4), (14.2, -4.4))
                Line((14.2, -4.4), (13.9, -4.4))
            make_face()
            # Profile area: 0.48, perimeter: 3.8
            with BuildLine():
                Line((12.3, -10.5), (12.3, -10.8))
                Line((12.3, -10.8), (13.9, -10.8))
                Line((13.9, -10.8), (13.9, -10.5))
                Line((13.9, -10.5), (12.3, -10.5))
            make_face()
            # Profile area: 0.6, perimeter: 4.6
            with BuildLine():
                Line((10.3, -10.8), (10.3, -10.5))
                Line((12.3, -10.8), (10.3, -10.8))
                Line((12.3, -10.5), (12.3, -10.8))
                Line((10.3, -10.5), (12.3, -10.5))
            make_face()
            # Profile area: 1.05, perimeter: 7.6
            with BuildLine():
                Line((6.8, -10.5), (6.8, -10.8))
                Line((6.8, -10.8), (8.4, -10.8))
                Line((8.7, -10.8), (8.4, -10.8))
                Line((8.7, -10.8), (10.3, -10.8))
                Line((10.3, -10.8), (10.3, -10.5))
                Line((10.3, -10.5), (6.8, -10.5))
            make_face()
            # Profile area: 0.6, perimeter: 4.6
            with BuildLine():
                Line((4.8, -10.8), (4.8, -10.5))
                Line((6.8, -10.8), (4.8, -10.8))
                Line((6.8, -10.5), (6.8, -10.8))
                Line((4.8, -10.5), (6.8, -10.5))
            make_face()
            # Profile area: 0.48, perimeter: 3.8
            with BuildLine():
                Line((3.2, -10.5), (3.2, -10.8))
                Line((3.2, -10.8), (4.8, -10.8))
                Line((4.8, -10.8), (4.8, -10.5))
                Line((4.8, -10.5), (3.2, -10.5))
            make_face()
            # Profile area: 0.4851, perimeter: 3.834
            with BuildLine():
                Line((3.2, -9.959), (2.9, -9.959))
                Line((2.9, -11.576), (2.9, -9.959))
                Line((3.2, -11.576), (2.9, -11.576))
                Line((3.2, -10.8), (3.2, -11.576))
                Line((3.2, -10.5), (3.2, -10.8))
                Line((3.2, -9.959), (3.2, -10.5))
            make_face()
            # Profile area: 0.15, perimeter: 1.6
            with BuildLine():
                Line((2.9, -9.459), (3.2, -9.459))
                Line((2.9, -9.959), (2.9, -9.459))
                Line((3.2, -9.959), (2.9, -9.959))
                Line((3.2, -9.459), (3.2, -9.959))
            make_face()
            # Profile area: 0.15, perimeter: 1.6
            with BuildLine():
                Line((3.2, -8.959), (2.9, -8.959))
                Line((2.9, -8.959), (2.9, -9.459))
                Line((2.9, -9.459), (3.2, -9.459))
                Line((3.2, -9.459), (3.2, -8.959))
            make_face()
            # Profile area: 0.4851, perimeter: 3.834
            with BuildLine():
                Line((3.2, -7.342), (2.9, -7.342))
                Line((2.9, -8.959), (2.9, -7.342))
                Line((3.2, -8.959), (2.9, -8.959))
                Line((3.2, -7.342), (3.2, -8.959))
            make_face()
            # Profile area: 0.15, perimeter: 1.6
            with BuildLine():
                Line((2.9, -6.842), (3.2, -6.842))
                Line((2.9, -7.342), (2.9, -6.842))
                Line((3.2, -7.342), (2.9, -7.342))
                Line((3.2, -6.842), (3.2, -7.342))
            make_face()
            # Profile area: 0.15, perimeter: 1.6
            with BuildLine():
                Line((3.2, -6.342), (2.9, -6.342))
                Line((2.9, -6.342), (2.9, -6.842))
                Line((2.9, -6.842), (3.2, -6.842))
                Line((3.2, -6.842), (3.2, -6.342))
            make_face()
            # Profile area: 0.4851, perimeter: 3.834
            with BuildLine():
                Line((3.2, -4.725), (2.9, -4.725))
                Line((2.9, -6.342), (2.9, -4.725))
                Line((3.2, -6.342), (2.9, -6.342))
                Line((3.2, -4.725), (3.2, -6.342))
            make_face()
            # Profile area: 0.15, perimeter: 1.6
            with BuildLine():
                Line((2.9, -4.225), (3.2, -4.225))
                Line((2.9, -4.725), (2.9, -4.225))
                Line((3.2, -4.725), (2.9, -4.725))
                Line((3.2, -4.225), (3.2, -4.725))
            make_face()
            # Profile area: 0.15, perimeter: 1.6
            with BuildLine():
                Line((3.2, -3.725), (2.9, -3.725))
                Line((2.9, -3.725), (2.9, -4.225))
                Line((2.9, -4.225), (3.2, -4.225))
                Line((3.2, -4.225), (3.2, -3.725))
            make_face()
            # Profile area: 0.4851, perimeter: 3.834
            with BuildLine():
                Line((3.2, -2.108), (2.9, -2.108))
                Line((2.9, -3.725), (2.9, -2.108))
                Line((3.2, -3.725), (2.9, -3.725))
                Line((3.2, -2.108), (3.2, -3.725))
            make_face()
            # Profile area: 0.15, perimeter: 1.6
            with BuildLine():
                Line((2.9, -1.608), (3.2, -1.608))
                Line((2.9, -2.108), (2.9, -1.608))
                Line((3.2, -2.108), (2.9, -2.108))
                Line((3.2, -1.608), (3.2, -2.108))
            make_face()
            # Profile area: 0.15, perimeter: 1.6
            with BuildLine():
                Line((2.9, -1.108), (3.2, -1.108))
                Line((2.9, -1.608), (2.9, -1.108))
                Line((2.9, -1.608), (3.2, -1.608))
                Line((3.2, -1.108), (3.2, -1.608))
            make_face()
            # Profile area: 0.15, perimeter: 1.6
            with BuildLine():
                Line((3.2, -11.576), (2.9, -11.576))
                Line((2.9, -11.576), (2.9, -12.076))
                Line((2.9, -12.076), (3.2, -12.076))
                Line((3.2, -12.076), (3.2, -11.576))
            make_face()
            # Profile area: 0.15, perimeter: 1.6
            with BuildLine():
                Line((2.9, -12.076), (3.2, -12.076))
                Line((2.9, -12.576), (2.9, -12.076))
                Line((3.2, -12.576), (2.9, -12.576))
                Line((3.2, -12.076), (3.2, -12.576))
            make_face()
            # Profile area: 0.4851, perimeter: 3.834
            with BuildLine():
                Line((3.2, -12.576), (2.9, -12.576))
                Line((2.9, -14.193), (2.9, -12.576))
                Line((3.2, -14.193), (2.9, -14.193))
                Line((3.2, -12.576), (3.2, -14.193))
            make_face()
            # Profile area: 0.15, perimeter: 1.6
            with BuildLine():
                Line((3.2, -14.193), (2.9, -14.193))
                Line((2.9, -14.193), (2.9, -14.693))
                Line((2.9, -14.693), (3.2, -14.693))
                Line((3.2, -14.693), (3.2, -14.193))
            make_face()
            # Profile area: 0.15, perimeter: 1.6
            with BuildLine():
                Line((2.9, -14.693), (3.2, -14.693))
                Line((2.9, -15.193), (2.9, -14.693))
                Line((3.2, -15.193), (2.9, -15.193))
                Line((3.2, -14.693), (3.2, -15.193))
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 117 constraints, 40 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4851, perimeter: 3.834
            with BuildLine():
                Line((3.2, -2.108), (2.9, -2.108))
                Line((2.9, -3.725), (2.9, -2.108))
                Line((3.2, -3.725), (2.9, -3.725))
                Line((3.2, -2.108), (3.2, -3.725))
            make_face()
            # Profile area: 0.4851, perimeter: 3.834
            with BuildLine():
                Line((3.2, -9.959), (2.9, -9.959))
                Line((2.9, -11.576), (2.9, -9.959))
                Line((3.2, -11.576), (2.9, -11.576))
                Line((3.2, -10.8), (3.2, -11.576))
                Line((3.2, -10.5), (3.2, -10.8))
                Line((3.2, -9.959), (3.2, -10.5))
            make_face()
            # Profile area: 0.2421, perimeter: 2.214
            with BuildLine():
                Line((3.2, -15.193), (3.2, -16))
                Line((3.2, -15.193), (2.9, -15.193))
                Line((2.9, -16), (2.9, -15.193))
                Line((3.2, -16), (2.9, -16))
            make_face()
            # Profile area: 0.4851, perimeter: 3.834
            with BuildLine():
                Line((3.2, -4.725), (2.9, -4.725))
                Line((2.9, -6.342), (2.9, -4.725))
                Line((3.2, -6.342), (2.9, -6.342))
                Line((3.2, -4.725), (3.2, -6.342))
            make_face()
            # Profile area: 0.2424, perimeter: 2.216
            with BuildLine():
                Line((2.9, -1.108), (2.9, -0.3))
                Line((2.9, -1.108), (3.2, -1.108))
                Line((3.2, -0.3), (3.2, -1.108))
                Line((2.9, -0.3), (3.2, -0.3))
            make_face()
            # Profile area: 0.4851, perimeter: 3.834
            with BuildLine():
                Line((3.2, -12.576), (2.9, -12.576))
                Line((2.9, -14.193), (2.9, -12.576))
                Line((3.2, -14.193), (2.9, -14.193))
                Line((3.2, -12.576), (3.2, -14.193))
            make_face()
            # Profile area: 0.4851, perimeter: 3.834
            with BuildLine():
                Line((3.2, -7.342), (2.9, -7.342))
                Line((2.9, -8.959), (2.9, -7.342))
                Line((3.2, -8.959), (2.9, -8.959))
                Line((3.2, -7.342), (3.2, -8.959))
            make_face()
            # Profile area: 1.05, perimeter: 7.6
            with BuildLine():
                Line((6.8, -10.5), (6.8, -10.8))
                Line((6.8, -10.8), (8.4, -10.8))
                Line((8.7, -10.8), (8.4, -10.8))
                Line((8.7, -10.8), (10.3, -10.8))
                Line((10.3, -10.8), (10.3, -10.5))
                Line((10.3, -10.5), (6.8, -10.5))
            make_face()
            # Profile area: 0.48, perimeter: 3.8
            with BuildLine():
                Line((12.3, -10.5), (12.3, -10.8))
                Line((12.3, -10.8), (13.9, -10.8))
                Line((13.9, -10.8), (13.9, -10.5))
                Line((13.9, -10.5), (12.3, -10.5))
            make_face()
            # Profile area: 0.48, perimeter: 3.8
            with BuildLine():
                Line((3.2, -10.5), (3.2, -10.8))
                Line((3.2, -10.8), (4.8, -10.8))
                Line((4.8, -10.8), (4.8, -10.5))
                Line((4.8, -10.5), (3.2, -10.5))
            make_face()
            # Profile area: 1.56, perimeter: 11
            with BuildLine():
                Line((8.7, -16), (8.7, -10.8))
                Line((8.7, -10.8), (8.4, -10.8))
                Line((8.4, -10.8), (8.4, -16))
                Line((8.4, -16), (8.7, -16))
            make_face()
            # Profile area: 2.88, perimeter: 19.8
            with BuildLine():
                Line((14.2, -6.4), (14.2, -16))
                Line((13.9, -6.4), (14.2, -6.4))
                Line((13.9, -10.5), (13.9, -6.4))
                Line((13.9, -10.8), (13.9, -10.5))
                Line((13.9, -16), (13.9, -10.8))
                Line((14.2, -16), (13.9, -16))
            make_face()
            # Profile area: 1.23, perimeter: 8.8
            with BuildLine():
                Line((13.9, -0.3), (14.2, -0.3))
                Line((13.9, -4.4), (13.9, -0.3))
                Line((14.2, -4.4), (13.9, -4.4))
                Line((14.2, -0.3), (14.2, -4.4))
            make_face()
        # OneSide extrude, distance=6
        extrude(amount=6, mode=Mode.ADD)

        # Sketch1 -> Extrude4 (Join)
        # Sketch on XZ construction plane
        # Sketch has 117 constraints, 40 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.15, perimeter: 1.6
            with BuildLine():
                Line((2.9, -1.608), (3.2, -1.608))
                Line((2.9, -2.108), (2.9, -1.608))
                Line((3.2, -2.108), (2.9, -2.108))
                Line((3.2, -1.608), (3.2, -2.108))
            make_face()
            # Profile area: 0.15, perimeter: 1.6
            with BuildLine():
                Line((2.9, -1.108), (3.2, -1.108))
                Line((2.9, -1.608), (2.9, -1.108))
                Line((2.9, -1.608), (3.2, -1.608))
                Line((3.2, -1.108), (3.2, -1.608))
            make_face()
            # Profile area: 0.15, perimeter: 1.6
            with BuildLine():
                Line((2.9, -4.225), (3.2, -4.225))
                Line((2.9, -4.725), (2.9, -4.225))
                Line((3.2, -4.725), (2.9, -4.725))
                Line((3.2, -4.225), (3.2, -4.725))
            make_face()
            # Profile area: 0.15, perimeter: 1.6
            with BuildLine():
                Line((3.2, -3.725), (2.9, -3.725))
                Line((2.9, -3.725), (2.9, -4.225))
                Line((2.9, -4.225), (3.2, -4.225))
                Line((3.2, -4.225), (3.2, -3.725))
            make_face()
            # Profile area: 0.15, perimeter: 1.6
            with BuildLine():
                Line((2.9, -6.842), (3.2, -6.842))
                Line((2.9, -7.342), (2.9, -6.842))
                Line((3.2, -7.342), (2.9, -7.342))
                Line((3.2, -6.842), (3.2, -7.342))
            make_face()
            # Profile area: 0.15, perimeter: 1.6
            with BuildLine():
                Line((3.2, -6.342), (2.9, -6.342))
                Line((2.9, -6.342), (2.9, -6.842))
                Line((2.9, -6.842), (3.2, -6.842))
                Line((3.2, -6.842), (3.2, -6.342))
            make_face()
            # Profile area: 0.15, perimeter: 1.6
            with BuildLine():
                Line((3.2, -8.959), (2.9, -8.959))
                Line((2.9, -8.959), (2.9, -9.459))
                Line((2.9, -9.459), (3.2, -9.459))
                Line((3.2, -9.459), (3.2, -8.959))
            make_face()
            # Profile area: 0.15, perimeter: 1.6
            with BuildLine():
                Line((2.9, -9.459), (3.2, -9.459))
                Line((2.9, -9.959), (2.9, -9.459))
                Line((3.2, -9.959), (2.9, -9.959))
                Line((3.2, -9.459), (3.2, -9.959))
            make_face()
            # Profile area: 0.15, perimeter: 1.6
            with BuildLine():
                Line((3.2, -14.193), (2.9, -14.193))
                Line((2.9, -14.193), (2.9, -14.693))
                Line((2.9, -14.693), (3.2, -14.693))
                Line((3.2, -14.693), (3.2, -14.193))
            make_face()
            # Profile area: 0.15, perimeter: 1.6
            with BuildLine():
                Line((2.9, -14.693), (3.2, -14.693))
                Line((2.9, -15.193), (2.9, -14.693))
                Line((3.2, -15.193), (2.9, -15.193))
                Line((3.2, -14.693), (3.2, -15.193))
            make_face()
        # OneSide extrude, distance=6
        extrude(amount=6, mode=Mode.ADD)

        # Sketch2 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -0.3, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 455.7496, perimeter: 89.56
            with BuildLine():
                Line((29.47, 0.33), (29.47, 15.97))
                Line((29.47, 15.97), (0.33, 15.97))
                Line((0.33, 15.97), (0.33, 0.33))
                Line((0.33, 0.33), (29.47, 0.33))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)
    return part.part


def model_134320_c6ad7b8d_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrusion1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.1547562844, perimeter: 7.2256631033
            Circle(1.15)
        # OneSide extrude, distance=1.8
        extrude(amount=1.8)

        # Sketch2 -> Extrusion2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.8352873699, perimeter: 5.9690260418
            Circle(0.95)
        # OneSide extrude, distance=-1.6
        extrude(amount=-1.6, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrusion3 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2085555646, perimeter: 2.5433123761
            with BuildLine():
                Line((-0.5000000075, -1.0356157553), (-0.5000000075, -0.8077747165))
                CenterArc((0, 0), 1.15, -115.7714621528, 51.5429243055)
                Line((0.5000000075, -0.8077747165), (0.5000000075, -1.0356157553))
                CenterArc((0, 0), 0.95, -121.7568643878, 63.5137287755)
            make_face()
            # Profile area: 0.2085555646, perimeter: 2.5433123761
            with BuildLine():
                CenterArc((0, 0), 0.95, 58.2431356122, 63.5137287755)
                Line((0.5000000075, 1.0356157553), (0.5000000075, 0.8077747165))
                CenterArc((0, 0), 1.15, 64.2285378472, 51.5429243055)
                Line((-0.5000000075, 0.8077747165), (-0.5000000075, 1.0356157553))
            make_face()
        # OneSide extrude, distance=-1.1
        extrude(amount=-1.1, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrusion4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.6174047886, perimeter: 14.3901744529
            with BuildLine():
                CenterArc((0, 0), 1.5000000224, 0, 360)
            make_face()
            with BuildLine():
                Line((-0.5000000075, 0.8077747165), (-0.5000000075, 1.0356157553))
                CenterArc((0, 0), 0.95, 121.7568643878, 116.4862712245)
                Line((-0.5000000075, -1.0356157553), (-0.5000000075, -0.8077747165))
                CenterArc((0, 0), 1.15, 115.7714621528, 128.4570756945)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.ADD)

        # Sketch5 -> Extrusion5 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 2.9434797426, perimeter: 7.6958758209
            with BuildLine():
                CenterArc((0, 0), 1.5000000224, -109.4712206345, 38.942441269)
                Line((0.5000000075, -1.4142135834), (0.5000000075, -1.0356157553))
                Line((0.5000000075, -1.0356157553), (0.5000000075, -0.8077747165))
                Line((0.5000000075, -0.8077747165), (0.5000000075, 0.8077747165))
                Line((0.5000000075, 0.8077747165), (0.5000000075, 1.0356157553))
                Line((0.5000000075, 1.0356157553), (0.5000000075, 1.4142135834))
                CenterArc((0, 0), 1.5000000224, 70.5287793655, 38.942441269)
                Line((-0.5000000075, 1.0356157553), (-0.5000000075, 1.4142135834))
                Line((-0.5000000075, 0.8077747165), (-0.5000000075, 1.0356157553))
                Line((-0.5000000075, -0.8077747165), (-0.5000000075, 0.8077747165))
                Line((-0.5000000075, -1.0356157553), (-0.5000000075, -0.8077747165))
                Line((-0.5000000075, -1.4142135834), (-0.5000000075, -1.0356157553))
            make_face()
            # Profile area: 0.5135350068, perimeter: 3.5469649508
            with BuildLine():
                CenterArc((0, 0), 0.95, 121.7568643878, 116.4862712245)
                Line((-0.5000000075, -0.8077747165), (-0.5000000075, 0.8077747165))
            make_face()
            # Profile area: 0.5135350068, perimeter: 3.5469649508
            with BuildLine():
                CenterArc((0, 0), 0.95, -58.2431356122, 116.4862712245)
                Line((0.5000000075, -0.8077747165), (0.5000000075, 0.8077747165))
            make_face()
        # OneSide extrude, distance=-1.1
        extrude(amount=-1.1, mode=Mode.SUBTRACT)
    return part.part


def model_134408_8183bf58_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3100000073, perimeter: 6.4000000566
            with BuildLine():
                Line((0, -3.1000000268), (0, 0))
                Line((0, 0), (-0.1000000015, 0))
                Line((-0.1000000015, 0), (-0.1000000015, -3.1000000268))
                Line((-0.1000000015, -3.1000000268), (0, -3.1000000268))
            make_face()
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0349999991, perimeter: 0.8999999747
            with BuildLine():
                Line((0.1000000015, 2.750000041), (0, 2.750000041))
                Line((0.1000000015, 2.750000041), (0.1000000015, 3.1000000268))
                Line((0.1000000015, 3.1000000268), (0, 3.1000000268))
                Line((0, 3.1000000268), (0, 2.750000041))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0998159704, perimeter: 2.1963870938
            with BuildLine():
                Line((0, 0), (0.1000000015, 0))
                Line((0.1000000015, 0), (0.1000000015, 0.9963193629))
                Line((0.1000000015, 0.9963193629), (0, 1.0000000149))
                Line((0, 1.0000000149), (0, 0))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.1000000015, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.130994934, perimeter: 1.7482412675
            with BuildLine():
                Line((3.1000000268, 0), (3.1000000268, 0.5239797486))
                Line((3.1000000268, 0.5239797486), (2.6000000387, 0))
                Line((3.1000000268, 0), (2.6000000387, 0))
            make_face()
        # OneSide extrude, distance=-0.65
        extrude(amount=-0.65, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.1000000015, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.096211275, perimeter: 1.0995574288
            with Locations((1.7500000261, 0.5000000075)):
                Circle(0.175)
        # OneSide extrude, distance=-0.45
        extrude(amount=-0.45, mode=Mode.SUBTRACT)
    return part.part


def model_134925_98617d78_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 49, perimeter: 28
            with BuildLine():
                Line((3.5, -3.5), (3.5, 3.5))
                Line((3.5, 3.5), (-3.5, 3.5))
                Line((-3.5, 3.5), (-3.5, -3.5))
                Line((-3.5, -3.5), (3.5, -3.5))
            make_face()
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7753653755, perimeter: 4.101461502
            with BuildLine():
                Line((-3.0066148124, 3.5), (-3.0066148124, 3))
                Line((-3.0066148124, 3), (-1.4558840614, 3))
                Line((-1.4558840614, 3), (-1.4558840614, 3.5))
                Line((-1.4558840614, 3.5), (-3.0066148124, 3.5))
            make_face()
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 22 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 24.5, perimeter: 21
            with BuildLine():
                Line((3, 0), (3.5, 0))
                Line((3, 0), (-3.0066148124, 0))
                Line((-3.0066148124, 0), (-3.5, 0))
                Line((-3.5, 0), (-3.5, -3.5))
                Line((-3.5, -3.5), (3.5, -3.5))
                Line((3.5, -3.5), (3.5, 0))
            make_face()
        # OneSide extrude, distance=2.2
        extrude(amount=2.2, mode=Mode.ADD)
    return part.part


def model_135214_40ed3b60_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 40 constraints, 18 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.4772777446, perimeter: 4.3451166838
            with BuildLine():
                Line((-1.7511496224, -0.75), (-2.0202784462, -0.75))
                CenterArc((0, 0), 2.155, -159.6332635125, 56.0557478023)
                Line((-0.505909251, -1.8365949008), (-0.505909251, -2.0947746489))
                CenterArc((0, 0), 1.905, -156.8150298947, 51.4142547447)
            make_face()
            # Profile area: 4.7563107566, perimeter: 17.2607825987
            with BuildLine():
                CenterArc((0, 0), 0.75, -90, 180)
                Line((0, -0.75), (-1.7511496224, -0.75))
                CenterArc((0, 0), 1.905, -156.8150298947, 51.4142547447)
                CenterArc((0, 0), 1.905, -105.40077515, 39.3448984366)
                Line((0.7731357355, 1.7410589118), (0.7731357355, -1.7410589118))
                CenterArc((0, 0), 1.905, 66.0558767135, 39.3448984366)
                CenterArc((0, 0), 1.905, 105.40077515, 51.4142547447)
                Line((0, 0.75), (-1.7511496224, 0.75))
            make_face()
            with BuildLine():
                CenterArc((0, -1.2), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 1.2), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.4772777446, perimeter: 4.3451166838
            with BuildLine():
                CenterArc((0, 0), 1.905, 105.40077515, 51.4142547447)
                Line((-0.505909251, 2.0947746489), (-0.505909251, 1.8365949008))
                CenterArc((0, 0), 2.155, 103.5775157102, 56.0557478023)
                Line((-1.7511496224, 0.75), (-2.0202784462, 0.75))
            make_face()
            # Profile area: 2.8378009837, perimeter: 7.874638397
            with BuildLine():
                CenterArc((0, 0), 1.905, -66.0558767135, 132.1117534269)
                Line((0.7731357355, 1.7410589118), (0.7731357355, -1.7410589118))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 40 constraints, 18 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.3261433886, perimeter: 3.1382565441
            with BuildLine():
                Line((0.7731357355, 2.0115382508), (0.7731357355, 1.7410589118))
                CenterArc((0, 0), 2.155, 68.9757110728, 34.6018046373)
                Line((-0.505909251, 2.0947746489), (-0.505909251, 1.8365949008))
                CenterArc((0, 0), 1.905, 66.0558767135, 39.3448984366)
            make_face()
            # Profile area: 0.3261433886, perimeter: 3.1382565441
            with BuildLine():
                Line((-0.505909251, -1.8365949008), (-0.505909251, -2.0947746489))
                CenterArc((0, 0), 2.155, -103.5775157102, 34.6018046373)
                Line((0.7731357355, -1.7410589118), (0.7731357355, -2.0115382508))
                CenterArc((0, 0), 1.905, -105.40077515, 39.3448984366)
            make_face()
            # Profile area: 1.1977315568, perimeter: 10.1220868111
            with BuildLine():
                Line((0.7731357355, -1.7410589118), (0.7731357355, -2.0115382508))
                CenterArc((0, 0), 2.155, -68.9757110728, 55.5597688166)
                CenterArc((0, 0), 2.155, -13.4159422562, 26.8318841366)
                CenterArc((0, 0), 2.155, 13.4159418803, 55.5597691925)
                Line((0.7731357355, 2.0115382508), (0.7731357355, 1.7410589118))
                CenterArc((0, 0), 1.905, -66.0558767135, 132.1117534269)
            make_face()
        # OneSide extrude, distance=6.1
        extrude(amount=6.1, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XY construction plane
        # Sketch has 40 constraints, 18 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.970687068, perimeter: 7.7091966707
            with BuildLine():
                Line((3.6761929811, -0.5000000022), (2.0961929811, -0.5000000075))
                Line((3.6761929801, -0.2000000052), (3.6761929811, -0.5000000022))
                Line((4.0761929811, -0.2000000039), (3.6761929801, -0.2000000052))
                Line((4.0761929811, -0.5000000009), (4.0761929811, -0.2000000039))
                Line((4.3461929811, -0.5), (4.0761929811, -0.5000000009))
                Line((4.3461929778, 0.5), (4.3461929811, -0.5))
                Line((4.0761929778, 0.4999999991), (4.3461929778, 0.5))
                Line((4.0761929778, 0.4999999991), (4.0761929788, 0.1999999991))
                Line((4.0761929788, 0.1999999991), (3.6761929788, 0.1999999978))
                Line((3.6761929788, 0.1999999978), (3.6761929778, 0.4999999978))
                Line((2.0961929795, 0.4999999925), (3.6761929778, 0.4999999978))
                CenterArc((0, 0), 2.155, -13.4159422562, 26.8318841366)
            make_face()
        # OneSide extrude, distance=4.8
        extrude(amount=4.8, mode=Mode.ADD)

        # Sketch1 -> Extrude4 (Join)
        # Sketch on XY construction plane
        # Sketch has 40 constraints, 18 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.12, perimeter: 1.4
            with BuildLine():
                Line((3.6761929788, 0.1999999978), (3.6761929778, 0.4999999978))
                Line((4.0761929788, 0.1999999991), (3.6761929788, 0.1999999978))
                Line((4.0761929778, 0.4999999991), (4.0761929788, 0.1999999991))
                Line((3.6761929778, 0.4999999978), (4.0761929778, 0.4999999991))
            make_face()
            # Profile area: 0.119999999, perimeter: 1.399999995
            with BuildLine():
                Line((4.0761929811, -0.5000000009), (4.0761929811, -0.2000000039))
                Line((4.0761929811, -0.2000000039), (3.6761929801, -0.2000000052))
                Line((3.6761929801, -0.2000000052), (3.6761929811, -0.5000000022))
                Line((4.0761929811, -0.5000000009), (3.6761929811, -0.5000000022))
            make_face()
        # OneSide extrude, distance=1.2
        extrude(amount=1.2, mode=Mode.ADD)

        # Sketch3 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 6.1), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 2.8799492012, perimeter: 7.9116787668
            with BuildLine():
                CenterArc((0, 0), 1.905, 113.5470086457, 132.9059827087)
                Line((-0.761050056, -1.7463756217), (-0.761050056, 1.7463756217))
            make_face()
            # Profile area: 1.2042607571, perimeter: 10.1729330376
            with BuildLine():
                Line((-0.761050056, -2.0161418135), (-0.761050056, -1.7463756217))
                CenterArc((0, 0), 1.905, 113.5470086457, 132.9059827087)
                Line((-0.761050056, 1.7463756217), (-0.761050056, 2.0161418135))
                CenterArc((0, 0), 2.155, 110.680440191, 138.639119618)
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch3 -> Extrude7 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 6.1), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1263527163, perimeter: 1.5190907292
            with BuildLine():
                Line((0.505909251, 1.8365949008), (0.505909251, 2.0947746489))
                CenterArc((0, 0), 2.155, 76.4224842898, 13.4204040781)
                Line((0.005909251, 1.9049908348), (0.005909251, 2.1549918981))
                CenterArc((0, 0), 1.905, 74.59922485, 15.2230451313)
            make_face()
            # Profile area: 0.1965260722, perimeter: 2.0923185337
            with BuildLine():
                CenterArc((0, 0), 1.905, -113.5470086457, 23.7247386644)
                Line((-0.761050056, -2.0161418135), (-0.761050056, -1.7463756217))
                CenterArc((0, 0), 2.155, -110.680440191, 20.837551823)
                Line((0.005909251, -2.1549918981), (0.005909251, -1.9049908348))
            make_face()
            # Profile area: 0.1965260722, perimeter: 2.0923185337
            with BuildLine():
                CenterArc((0, 0), 2.155, 89.842888368, 20.837551823)
                Line((-0.761050056, 1.7463756217), (-0.761050056, 2.0161418135))
                CenterArc((0, 0), 1.905, 89.8222699813, 23.7247386644)
                Line((0.005909251, 1.9049908348), (0.005909251, 2.1549918981))
            make_face()
            # Profile area: 0.1263527163, perimeter: 1.5190907292
            with BuildLine():
                Line((0.005909251, -2.1549918981), (0.005909251, -1.9049908348))
                CenterArc((0, 0), 2.155, -89.842888368, 13.4204040781)
                Line((0.505909251, -2.0947746489), (0.505909251, -1.8365949008))
                CenterArc((0, 0), 1.905, -89.8222699813, 15.2230451313)
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


def model_135538_9913818f_0024():
    """Model: Walls"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 8 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 19045.1232, perimeter: 643.89
            with BuildLine():
                Line((-78.105, 213.3599967957), (-78.105, 243.84))
                Line((-78.105, 0), (-78.105, 213.3599967957))
                Line((0, 0), (-78.105, 0))
                Line((0, 243.84), (0, 0))
                Line((-78.105, 243.84), (0, 243.84))
            make_face()
        # OneSide extrude, distance=-12.7
        extrude(amount=-12.7)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 9 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 20128.992, perimeter: 652.78
            with BuildLine():
                Line((82.55, 215.7384456275), (82.55, 243.84))
                Line((82.55, 243.84), (0, 243.84))
                Line((0, 243.84), (0, 0))
                Line((0, 0), (82.55, 0))
                Line((82.55, 0), (82.55, 215.7384456275))
            make_face()
        # OneSide extrude, distance=-12.7
        extrude(amount=-12.7)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on YZ construction plane
        # Sketch has 8 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2883.8655031792, perimeter: 250.1900064087
            with BuildLine():
                Line((-78.105, 243.84), (-172.72, 243.84))
                Line((-172.72, 243.84), (-172.72, 213.3599967957))
                Line((-172.72, 213.3599967957), (-78.105, 213.3599967957))
                Line((-78.105, 213.3599967957), (-78.105, 243.84))
            make_face()
        # OneSide extrude, distance=-12.7
        extrude(amount=-12.7, mode=Mode.ADD)

        # Sketch2 -> Extrude4 (Join)
        # Sketch on XY construction plane
        # Sketch has 9 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2248.4052967371, perimeter: 216.2231038622
            with BuildLine():
                Line((82.55, 215.7384456275), (162.5599975586, 215.7384456275))
                Line((162.5599975586, 215.7384456275), (162.5599975586, 243.84))
                Line((162.5599975586, 243.84), (82.55, 243.84))
                Line((82.55, 215.7384456275), (82.55, 243.84))
            make_face()
        # OneSide extrude, distance=-12.7
        extrude(amount=-12.7, mode=Mode.ADD)

        # Sketch3 -> Extrude5 (Join)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 140322.295785141, perimeter: 1498.5999774933
            with BuildLine():
                Line((368.2999944687, -380.999994278), (0, -380.999994278))
                Line((368.2999944687, 0), (368.2999944687, -380.999994278))
                Line((0, 0), (368.2999944687, 0))
                Line((0, -380.999994278), (0, 0))
            make_face()
        # OneSide extrude, distance=0.254
        extrude(amount=0.254, mode=Mode.ADD)
    return part.part


def model_135700_4190876c_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 14 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6650000283, perimeter: 6.1086792852
            with BuildLine():
                Line((0.65, -0.3), (1.0000000149, 0.8))
                Line((0.65, -0.3), (0.65, -1.1))
                Line((0.65, -1.1), (1.0000000149, -2.2))
                Line((1.0000000149, -2.2), (1.0000000149, 0.8))
            make_face()
            # Profile area: 0.4, perimeter: 2.6
            with BuildLine():
                Line((0.15, -0.3), (0.65, -0.3))
                Line((0.15, -1.1), (0.15, -0.3))
                Line((0.65, -1.1), (0.15, -1.1))
                Line((0.65, -0.3), (0.65, -1.1))
            make_face()
            # Profile area: 3.9, perimeter: 8.6
            with BuildLine():
                Line((1.0000000149, -2.2), (1.0000000149, 0.8))
                Line((2.3000000149, -2.2), (1.0000000149, -2.2))
                Line((2.3000000149, 0.8), (2.3000000149, -2.2))
                Line((1.0000000149, 0.8), (2.3000000149, 0.8))
            make_face()
            # Profile area: 0.21, perimeter: 3.1
            with BuildLine():
                Line((0.15, -1.1), (0.15, -0.3))
                Line((0.15, 0), (0.15, -0.3))
                Line((0, 0), (0.15, 0))
                Line((0, -1.4), (0, 0))
                Line((0.15, -1.4), (0, -1.4))
                Line((0.15, -1.1), (0.15, -1.4))
            make_face()
        # OneSide extrude, distance=2.4
        extrude(amount=2.4)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.925, perimeter: 4.6142135624
            with BuildLine():
                Line((-2.0500000149, -0.35), (-1.8000000149, -0.1))
                Line((-1.8000000149, -0.1), (-1.8000000149, 1.5))
                Line((-1.8000000149, 1.5), (-2.0500000149, 1.75))
                Line((-2.0500000149, 1.75), (-2.3000000149, 1.5))
                Line((-2.3000000149, -0.1), (-2.3000000149, 1.5))
                Line((-2.3000000149, -0.1), (-2.0500000149, -0.35))
            make_face()
        # OneSide extrude, distance=-2.4
        extrude(amount=-2.4, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0907920277, perimeter: 1.0681415022
            with Locations((1.9500000149, 1.1848445756)):
                Circle(0.17)
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.12, perimeter: 1.9
            with BuildLine():
                Line((1.1, 1.125), (0.3, 1.125))
                Line((1.1, 1.125), (1.1, 1.275))
                Line((0.3, 1.275), (1.1, 1.275))
                Line((0.3, 1.125), (0.3, 1.275))
            make_face()
        # OneSide extrude, distance=0.06
        extrude(amount=0.06, mode=Mode.ADD)
    return part.part


def model_135779_4106c13d_0001():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude4 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 40 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 120.6366192983, perimeter: 45.5665482457
            with BuildLine():
                Line((7.67, 11.0504182104), (7.67, 12.1286052999))
                Line((7.67, 12.1286052999), (7.67, 15))
                CenterArc((6.87, 15), 0.8, 0, 90)
                Line((6.87, 15.8), (0.8, 15.8))
                CenterArc((0.8, 15), 0.8, 90, 90)
                Line((0, 15), (0, 0.8))
                CenterArc((0.8, 0.8), 0.8, 180, 90)
                Line((0.8, 0), (6.87, 0))
                CenterArc((6.87, 0.8), 0.8, -90, 90)
                Line((7.67, 0.8), (7.67, 8.0486905442))
                Line((7.67, 8.0486905442), (7.67, 10.1925515518))
                Line((7.67, 10.1925515518), (7.67, 11.0504182104))
            make_face()
        # OneSide extrude, distance=0.79
        extrude(amount=0.79)

        # Sketch6 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 60 constraints, 20 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.79), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.11868158, perimeter: 1.7833666086
            with BuildLine():
                CenterArc((-3.5140990056, -14.8786132003), 0.0769914235, -90, 180)
                Line((-3.5140990056, -14.8016217768), (-4.1639066196, -14.8016217768))
                CenterArc((-4.1639066196, -14.8786132003), 0.0769914235, 90, 180)
                Line((-4.1639066196, -14.9556046238), (-3.5140990056, -14.9556046238))
            make_face()
            # Profile area: 0.1343305845, perimeter: 1.299248979
            with Locations((-3.0314363887, -15.0004545239)):
                Circle(0.2067818973)
            # Profile area: 0.1058572962, perimeter: 1.2066556719
            with BuildLine():
                CenterArc((-3.7566894901, -15.2909948532), 0.1356010777, -90, 180)
                Line((-3.7566894901, -15.1553937755), (-3.9340139764, -15.1553937755))
                CenterArc((-3.9340139764, -15.2909948532), 0.1356010777, 90, 180)
                Line((-3.9340139764, -15.426595931), (-3.7566894901, -15.426595931))
            make_face()
            # Profile area: 0.1343305845, perimeter: 1.299248979
            with Locations((-4.6747609905, -15.0004545177)):
                Circle(0.2067818973)
        # OneSide extrude, distance=-0.01
        extrude(amount=-0.01, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 60 constraints, 20 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.79), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.3753101917, perimeter: 4.666272275
            with BuildLine():
                CenterArc((-2.8133218412, -0.4979042387), 0.08533285, -90, 180)
                Line((-2.8133218412, -0.4125713887), (-4.878376924, -0.4125713887))
                CenterArc((-4.878376924, -0.4979042387), 0.08533285, 90, 180)
                Line((-4.878376924, -0.5832370887), (-2.8133218412, -0.5832370887))
            make_face()
        # OneSide extrude, distance=-0.01
        extrude(amount=-0.01, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 60 constraints, 20 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.79), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 99.0090179468, perimeter: 43.3359521006
            with BuildLine():
                Line((-3.8350000286, -1.0260735887), (-7.1456949113, -1.0260735887))
                CenterArc((-7.1456949113, -1.2260735887), 0.2, 90, 90)
                Line((-7.3456949113, -1.2260735887), (-7.3456949113, -14.9267127172))
                CenterArc((-6.8456949113, -14.9267127172), 0.5, 180, 89.9999997381)
                Line((-6.8456949136, -15.4267127172), (-5.3247610598, -15.4267127208))
                CenterArc((-5.3247610587, -15.1767127208), 0.25, -90.0000002619, 89.9999780812)
                Line((-5.0747609905, -15.0004543629), (-5.0747610587, -15.1767128176))
                CenterArc((-4.6747609905, -15.0004545177), 0.4, 89.9999999014, 89.9999779178)
                Line((-3.031436388, -14.6004545239), (-4.6747609898, -14.6004545177))
                CenterArc((-3.0314363887, -15.0004545239), 0.4, 0, 89.9999999014)
                Line((-2.6314363887, -15.0004545239), (-2.6314363887, -15.1758266113))
                CenterArc((-2.3814363887, -15.1758266113), 0.25, 180, 90)
                Line((-0.8243050887, -15.4258266113), (-2.3814363887, -15.4258266113))
                CenterArc((-0.8243050887, -14.9258266113), 0.5, -90, 90)
                Line((-0.3243050887, -1.2260735887), (-0.3243050887, -14.9258266113))
                CenterArc((-0.5243050887, -1.2260735887), 0.2, 0, 90)
                Line((-3.8350000286, -1.0260735887), (-0.5243050887, -1.0260735887))
            make_face()
        # OneSide extrude, distance=0.005
        extrude(amount=0.005, mode=Mode.ADD)

        # Sketch10 -> Extrude13 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.1536693701, perimeter: 1.3896281001
            with Locations((4.8836368113, -14.3446728113)):
                Circle(0.2211661812)
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((5.4120133113, -14.3446728113)):
                Circle(0.1)
        # OneSide extrude, distance=-0.01
        extrude(amount=-0.01, mode=Mode.SUBTRACT)

        # Sketch10 -> Extrude12 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 1.162668253, perimeter: 3.8223710139
            with Locations((3.8268839362, -11.6405675644)):
                Circle(0.6083492412)
        # OneSide extrude, distance=-0.06
        extrude(amount=-0.06, mode=Mode.SUBTRACT)

        # Sketch10 -> Extrude11 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.714707542, perimeter: 2.9968783515
            with Locations((6.2225928113, -14.3446728113)):
                Circle(0.4769680035)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)
    return part.part


def model_136120_439f44c2_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 28 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1595760608, perimeter: 1.6472224302
            with BuildLine():
                CenterArc((0.2599182278, 0.0260817722), 0.0260817722, -90, 90)
                Line((0.286, 0.0260817722), (0.286, 0.5339182278))
                CenterArc((0.2599182278, 0.5339182278), 0.0260817722, 0, 90)
                Line((0.2599182278, 0.56), (0.0260817722, 0.56))
                CenterArc((0.0260817722, 0.5339182278), 0.0260817722, 90, 90)
                Line((0, 0.5339182278), (0, 0.0260817722))
                CenterArc((0.0260817722, 0.0260817722), 0.0260817722, 180, 90)
                Line((0.0260817722, 0), (0.2599182278, 0))
            make_face()
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 14 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.286, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.0013725767, perimeter: 0.2968857663
            with BuildLine():
                CenterArc((0.3400000141, 0.0285857857), 0.0014142136, 90, 90)
                Line((0.3385858004, 0.0285857857), (0.3385858004, 0.0215857857))
                CenterArc((0.3400000141, 0.0215857857), 0.0014142136, 180, 90)
                Line((0.3400000141, 0.0201715721), (0.4770000141, 0.0201715721))
                CenterArc((0.4770000141, 0.0215857857), 0.0014142136, -90, 90)
                Line((0.4784142277, 0.0215857857), (0.4784142277, 0.0285857857))
                CenterArc((0.4770000141, 0.0285857857), 0.0014142136, 0, 90)
                Line((0.4770000141, 0.0299999993), (0.3433963223, 0.0299999993))
                Line((0.3400000141, 0.0299999993), (0.3433963223, 0.0299999993))
            make_face()
        # OneSide extrude, distance=0.005
        extrude(amount=0.005, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 12 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.286, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.0004139246, perimeter: 0.110021236
            with BuildLine():
                CenterArc((0.2810000133, 0.0223922992), 0.0020381114, 180, 90)
                Line((0.3250000133, 0.0203541877), (0.2810000133, 0.0203541877))
                CenterArc((0.3250000133, 0.0223922992), 0.0020381114, -90, 90)
                Line((0.3270381248, 0.0270000013), (0.3270381248, 0.0223922992))
                CenterArc((0.3250000133, 0.0270000013), 0.0020381114, 0, 90)
                Line((0.2810000133, 0.0290381127), (0.3250000133, 0.0290381127))
                CenterArc((0.2810000133, 0.0270000013), 0.0020381114, 90, 90)
                Line((0.2789619019, 0.0223922992), (0.2789619019, 0.0270000013))
            make_face()
        # OneSide extrude, distance=0.003
        extrude(amount=0.003, mode=Mode.ADD)

        # Sketch6 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0004412644, perimeter: 0.1078451357
            with BuildLine():
                CenterArc((0.1115000048, 0.0255000008), 0.0095, 180, 90)
                Line((0.1405000071, 0.0160000008), (0.1115000048, 0.0160000008))
                CenterArc((0.1405000071, 0.0255000008), 0.0095, -90, 90)
                Line((0.1500000071, 0.0260000012), (0.1500000071, 0.0255000008))
                Line((0.1020000048, 0.0260000012), (0.1500000071, 0.0260000012))
                Line((0.1020000048, 0.0255000008), (0.1020000048, 0.0260000012))
            make_face()
        # OneSide extrude, distance=-0.027
        extrude(amount=-0.027, mode=Mode.SUBTRACT)
    return part.part


def model_136355_b5fd1a59_0003():
    """Model: Stepper Connector"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.9, perimeter: 4.2
            with BuildLine():
                Line((1.5, -0.6), (0, -0.6))
                Line((1.5, 0), (1.5, -0.6))
                Line((0, 0), (1.5, 0))
                Line((0, -0.6), (0, 0))
            make_face()
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.7, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5200000155, perimeter: 3.4000000507
            with BuildLine():
                Line((-1.4000000209, 0.5000000075), (-0.1000000015, 0.5000000075))
                Line((-1.4000000209, 0.1000000015), (-1.4000000209, 0.5000000075))
                Line((-0.1000000015, 0.1000000015), (-1.4000000209, 0.1000000015))
                Line((-0.1000000015, 0.5000000075), (-0.1000000015, 0.1000000015))
            make_face()
        # OneSide extrude, distance=-0.6
        extrude(amount=-0.6, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0350102262, perimeter: 0.9000584356
            with BuildLine():
                Line((0.3999707896, 0.7), (0.3999707896, 0.35))
                Line((0.3999707896, 0.35), (0.5000000075, 0.35))
                Line((0.5000000075, 0.35), (0.5000000075, 0.7))
                Line((0.5000000075, 0.7), (0.3999707896, 0.7))
            make_face()
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.6), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.04, perimeter: 1
            with BuildLine():
                Line((0.3, 0.7), (0.3, 0.3))
                Line((0.2, 0.7), (0.3, 0.7))
                Line((0.2, 0.3), (0.2, 0.7))
                Line((0.3, 0.3), (0.2, 0.3))
            make_face()
            # Profile area: 0.04, perimeter: 1
            with BuildLine():
                Line((1.3, 0.7), (1.2, 0.7))
                Line((1.2, 0.7), (1.2, 0.3))
                Line((1.2, 0.3), (1.3, 0.3))
                Line((1.3, 0.3), (1.3, 0.7))
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)
    return part.part


def model_136477_c46134fc_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.0989662886, perimeter: 12.7800928338
            with BuildLine():
                Line((2.3236670652, -0.8713561433), (2.3236670652, 0.8713561433))
                Line((2.3236670652, 0.8713561433), (-2.3236670652, 0.8713561433))
                Line((-2.3236670652, 0.8713561433), (-2.3236670652, -0.8713561433))
                Line((-2.3236670652, -0.8713561433), (2.3236670652, -0.8713561433))
            make_face()
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)
    return part.part


def model_136593_1772a66f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 55, perimeter: 31
            with BuildLine():
                Line((-2.75, 5), (2.75, 5))
                Line((-2.75, -5), (-2.75, 5))
                Line((2.75, -5), (-2.75, -5))
                Line((2.75, 5), (2.75, -5))
            make_face()
        # OneSide extrude, distance=-0.7
        extrude(amount=-0.7)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -0.7, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 3.6393804003, perimeter: 7.398229715
            with BuildLine():
                CenterArc((0, 3.8658546062), 0.7, 0, 180)
                Line((-0.7, 3.8658546062), (-0.7, 2.3658546062))
                CenterArc((0, 2.3658546062), 0.7, -180, 180)
                Line((0.7, 2.3658546062), (0.7, 3.8658546062))
            make_face()
        # Symmetric extrude, each_side=2
        extrude(amount=2, both=True, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 9 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -5), x_dir=(1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 2.2426990817, perimeter: 9.9707963268
            with BuildLine():
                CenterArc((1.85, 0), 0.5, 0, 90)
                Line((1.85, 0.5), (-1.85, 0.5))
                CenterArc((-1.85, 0), 0.5, 90, 90)
                Line((-2.35, 0), (2.35, 0))
            make_face()
        # OneSide extrude, distance=-20
        extrude(amount=-20, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 14 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-2.75, 0, 0), x_dir=(0, -1, 0), z_dir=(-1, 0, 0))):
            # Profile area: 0.516211275, perimeter: 3.4995574288
            with BuildLine():
                CenterArc((0.35, 3.9249015792), 0.175, 0, 180)
                Line((0.175, 3.9249015792), (0.175, 2.7249015792))
                CenterArc((0.35, 2.7249015792), 0.175, 180, 180)
                Line((0.525, 2.7249015792), (0.525, 3.9249015792))
            make_face()
            # Profile area: 0.351711275, perimeter: 2.5595574288
            with BuildLine():
                CenterArc((0.35, 2.23), 0.175, 0, 180)
                Line((0.175, 2.23), (0.175, 1.5))
                CenterArc((0.35, 1.5), 0.175, 180, 180)
                Line((0.525, 1.5), (0.525, 2.23))
            make_face()
        # Symmetric extrude, full_length=True, total=0.4
        extrude(amount=0.2, both=True, mode=Mode.SUBTRACT)
    return part.part


def model_136609_a3c013f6_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 60, perimeter: 34
            with BuildLine():
                Line((0, 12), (0, 0))
                Line((0, 0), (5, 0))
                Line((5, 0), (5, 12))
                Line((5, 12), (0, 12))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch5 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 18 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0176714587, perimeter: 0.471238898
            with Locations((0.7, 0.65)):
                Circle(0.075)
            # Profile area: 0.0176714587, perimeter: 0.471238898
            with Locations((1, 0.65)):
                Circle(0.075)
            # Profile area: 0.0176714587, perimeter: 0.471238898
            with Locations((1.3, 0.65)):
                Circle(0.075)
            # Profile area: 0.0176714587, perimeter: 0.471238898
            with Locations((1.6, 0.65)):
                Circle(0.075)
            # Profile area: 0.0176714587, perimeter: 0.471238898
            with Locations((1.9, 0.65)):
                Circle(0.075)
            # Profile area: 0.0524416116, perimeter: 1.1511147609
            with BuildLine():
                Line((2.2689685828, 0.706747273), (2.7310314172, 0.706747273))
                Line((2.2689685828, 0.593252727), (2.2689685828, 0.706747273))
                Line((2.7310314172, 0.593252727), (2.2689685828, 0.593252727))
                Line((2.7310314172, 0.706747273), (2.7310314172, 0.593252727))
            make_face()
            # Profile area: 0.0176714587, perimeter: 0.471238898
            with Locations((3.1, 0.6626659013)):
                Circle(0.075)
            # Profile area: 0.0176714587, perimeter: 0.471238898
            with Locations((3.4, 0.6626659013)):
                Circle(0.075)
            # Profile area: 0.0176714587, perimeter: 0.471238898
            with Locations((3.7, 0.6626659013)):
                Circle(0.075)
            # Profile area: 0.0176714587, perimeter: 0.471238898
            with Locations((4, 0.6626659013)):
                Circle(0.075)
            # Profile area: 0.0176714587, perimeter: 0.471238898
            with Locations((4.3, 0.6626659013)):
                Circle(0.075)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 12 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.3121892301, perimeter: 4.7631093526
            with BuildLine():
                Line((-0.729874774, 10.0124682152), (-0.5906493551, 10.0124682152))
                Line((-0.729874774, 7.7701389578), (-0.729874774, 10.0124682152))
                Line((-0.5906493551, 7.7701389578), (-0.729874774, 7.7701389578))
                Line((-0.5906493551, 10.0124682152), (-0.5906493551, 7.7701389578))
            make_face()
            # Profile area: 0.1445545776, perimeter: 2.3611379416
            with BuildLine():
                Line((-0.5929513596, 6.4314587023), (-0.5929513596, 7.473275242))
                Line((-0.5929513596, 7.473275242), (-0.7317037906, 7.473275242))
                Line((-0.7317037906, 7.473275242), (-0.7317037906, 6.4314587023))
                Line((-0.7317037906, 6.4314587023), (-0.5929513596, 6.4314587023))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch7 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 12, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0176714587, perimeter: 0.471238898
            with Locations((-1.1119039227, 0.6515835085)):
                Circle(0.075)
            # Profile area: 0.0019634954, perimeter: 0.1570796327
            with Locations((-1.5836529492, 0.6617651422)):
                Circle(0.025)
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((-3.8677327683, 0.6626659013)):
                Circle(0.05)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)
    return part.part


def model_136832_d2438c00_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 510.7051557492, perimeter: 80.1106126665
            Circle(12.75)
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(2.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 226.9800692219, perimeter: 53.407075111
            Circle(8.5)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 44.6970094789, perimeter: 85.1371609123
            with BuildLine():
                CenterArc((0, 0), 7.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 6.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.7
        extrude(amount=-0.7, mode=Mode.SUBTRACT)

        # Sketch15 -> Extrude15 (NewBody)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 2.2698006922, perimeter: 5.3407075111
            Circle(0.85)
        # OneSide extrude, distance=5.5
        extrude(amount=5.5)
    return part.part


def model_136861_0ab0408d_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 291.885373445, perimeter: 102.415920507
            with BuildLine():
                CenterArc((0, 0), 11, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 5.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=6
        extrude(amount=6)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 11 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2, perimeter: 6.8284271247
            with BuildLine():
                Line((1, 3), (1, 5))
                Line((1, 5), (0, 4))
                Line((0, 4), (0, 2))
                Line((0, 2), (1, 3))
            make_face()
            # Profile area: 2, perimeter: 6.8284271247
            with BuildLine():
                Line((-6, 4), (-6, 2))
                Line((-7, 5), (-6, 4))
                Line((-7, 3), (-7, 5))
                Line((-6, 2), (-7, 3))
            make_face()
            # Profile area: 4.5, perimeter: 11
            with BuildLine():
                Line((0, 4), (0, 2))
                Line((-3, 0), (0, 4))
                Line((-3, 0), (-1.5, 0))
                Line((0, 2), (-1.5, 0))
            make_face()
            # Profile area: 4.5, perimeter: 11
            with BuildLine():
                Line((-4.5, 0), (-3, 0))
                Line((-6, 4), (-3, 0))
                Line((-6, 4), (-6, 2))
                Line((-6, 2), (-4.5, 0))
            make_face()
            # Profile area: 3, perimeter: 8
            with BuildLine():
                Line((-3, 0), (-1.5, 0))
                Line((-4.5, 0), (-3, 0))
                Line((-4.5, 0), (-3, -2))
                Line((-1.5, 0), (-3, -2))
            make_face()
        # OneSide extrude, distance=12
        extrude(amount=12, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on XY construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 88.2473376393, perimeter: 33.3008821281
            Circle(5.3)
        # OneSide extrude, distance=20
        extrude(amount=20, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on XY construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 88.2473376393, perimeter: 33.3008821281
            Circle(5.3)
        # OneSide extrude, distance=-9
        extrude(amount=-9, mode=Mode.SUBTRACT)
    return part.part


def model_137053_59e609b3_0000():
    """Model: Finger"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 20 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.7068583471, perimeter: 4.7123889804
            with BuildLine():
                CenterArc((0, -1.5), 0.525, 73.398450401, 33.203099198)
                CenterArc((0, -1.5), 0.525, 106.601549599, 326.796900802)
            make_face()
            with BuildLine():
                CenterArc((0, -1.5), 0.225, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 2.6669085918, perimeter: 9.3009664642
            with BuildLine():
                Line((0.5225969864, 0.0501735972), (3.5474416482, 1.8576378819))
                Line((3.5474416482, 1.8576378819), (3.1628339983, 2.5012901005))
                Line((-0.2572615081, 0.4576478083), (3.1628339983, 2.5012901005))
                CenterArc((0, 0), 0.525, 5.4840561068, 113.8579662308)
            make_face()
            # Profile area: 0.1590431067, perimeter: 1.4137166466
            with BuildLine():
                CenterArc((0, 0), 0.225, -58.647764883, 359.0155030206)
                Line((0.1137483053, -0.1941296553), (0.117067024, -0.1921465896))
            make_face()
            # Profile area: 0.1393397861, perimeter: 1.5960173933
            with BuildLine():
                Line((-0.15, -0.5031152949), (-0.15, -0.9968847051))
                CenterArc((0, -1.5), 0.525, 73.398450401, 33.203099198)
                Line((0.15, -0.9968847051), (0.15, -0.5031152949))
                CenterArc((0, 0), 0.525, -106.601549599, 33.203099198)
            make_face()
            # Profile area: 0.7068583471, perimeter: 5.1848015366
            with BuildLine():
                CenterArc((0, 0), 0.225, -59.6322618624, 0.9844969794)
                CenterArc((0, 0), 0.225, -58.647764883, 359.0155030206)
                Line((0.117067024, -0.1921465896), (0.5225969864, 0.0501735972))
                CenterArc((0, 0), 0.525, 5.4840561068, 113.8579662308)
                CenterArc((0, 0), 0.525, 119.3420223376, 134.0564280634)
                CenterArc((0, 0), 0.525, -106.601549599, 33.203099198)
                CenterArc((0, 0), 0.525, -73.398450401, 78.8825065078)
            make_face()
            # Profile area: 0.1590431281, perimeter: 1.4137166941
            with Locations((0, -1.5)):
                Circle(0.225)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.000000014, 0, 0), x_dir=(1, -0.000000023, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.1590431281, perimeter: 1.4137166941
            with Locations((0.0000000485, 1.4999999996)):
                Circle(0.225)
            # Profile area: 3.6721498317, perimeter: 11.5083535345
            with BuildLine():
                CenterArc((0.000000014, -0.0000000004), 0.525, 106.6015482809, 134.0564280634)
                Line((-0.2572615046, -0.4576478028), (3.1628339547, -2.5012901737))
                Line((3.1628339547, -2.5012901737), (3.5474416195, -1.857637964))
                Line((3.5474416195, -1.857637964), (0.5225969992, -0.0501736096))
                CenterArc((0.000000014, -0.0000000004), 0.525, -5.4840574249, 78.8825065078)
                Line((0.1500000256, 0.5031152911), (0.1500000369, 0.9968847012))
                CenterArc((0.0000000485, 1.4999999996), 0.525, -106.6015509171, 33.203099198)
                Line((-0.1499999631, 0.9968847081), (-0.1499999744, 0.503115298))
            make_face()
            with BuildLine():
                Line((0.1170670424, 0.1921465865), (0.1137483238, 0.1941296522))
                CenterArc((0.000000014, -0.0000000004), 0.225, 58.6477635649, 0.9844969794)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0000000214, perimeter: 0.0077321736
            with BuildLine():
                CenterArc((0.000000014, -0.0000000004), 0.225, 58.6477635649, 0.9844969794)
                Line((0.1170670424, 0.1921465865), (0.1137483238, 0.1941296522))
            make_face()
        # OneSide extrude, distance=0.25
        extrude(amount=0.25, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.0000000835, 0.0000000712, 0.4), x_dir=(-1, 0.0000000014, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.8659014537, perimeter: 3.3064044599
            with BuildLine():
                CenterArc((0.0000000835, 0.0000000712), 0.525, -174.5159438116, 113.8579662309)
                CenterArc((0.0000000835, 0.0000000712), 0.525, -60.6579775807, 134.0564280635)
                CenterArc((0.0000000835, 0.0000000712), 0.525, 73.3984504828, 33.203099198)
                CenterArc((0.0000000835, 0.0000000712), 0.525, 106.6015496808, 73.3984503192)
                CenterArc((0.0000000835, 0.0000000712), 0.525, -180, 5.4840561884)
            make_face()
            with BuildLine():
                Line((-0.1137482221, 0.1941297263), (-0.1170669408, 0.1921466606))
                CenterArc((0.0000000835, 0.0000000712), 0.225, 120.3677382193, 0.9844969794)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 2.6669085918, perimeter: 9.3009664642
            with BuildLine():
                Line((-3.5474415621, -1.8576378158), (-3.1628339112, -2.5012900338))
                Line((-3.1628339112, -2.5012900338), (0.2572615923, -0.4576477367))
                CenterArc((0.0000000835, 0.0000000712), 0.525, -174.5159438116, 113.8579662309)
                Line((-0.5225969028, -0.0501735267), (-3.5474415621, -1.8576378158))
            make_face()
        # OneSide extrude, distance=1.4
        extrude(amount=1.4, mode=Mode.ADD)

        # Sketch7 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.8), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 2.6669085918, perimeter: 9.3009664642
            with BuildLine():
                Line((-3.5474416482, -1.8576378819), (-3.1628339983, -2.5012901005))
                Line((-3.1628339983, -2.5012901005), (0.2572615081, -0.4576478083))
                CenterArc((0, 0), 0.525, -174.5159438932, 113.8579662308)
                Line((-0.5225969864, -0.0501735972), (-3.5474416482, -1.8576378819))
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.0000000835, 0.0000000712, 1.8), x_dir=(-1, 0.0000000014, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1590431066, perimeter: 1.4137166466
            with BuildLine():
                CenterArc((0, 0), 0.225, 121.3522076073, 359.0155031007)
                Line((-0.1137482123, 0.1941297097), (-0.1170669317, 0.1921466458))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)
    return part.part


def model_137053_59e609b3_0004():
    """Model: Lever"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 10 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.3493397861, perimeter: 2.9960173933
            with BuildLine():
                CenterArc((0, 0), 0.525, -16.601549599, 33.203099198)
                Line((1.6968847051, -0.15), (0.5031152949, -0.15))
                CenterArc((2.2, 0), 0.525, 163.398450401, 33.203099198)
                Line((0.5031152949, 0.15), (1.6968847051, 0.15))
            make_face()
            # Profile area: 0.8659014751, perimeter: 3.2986722863
            with BuildLine():
                CenterArc((0, 0), 0.525, 16.601549599, 326.796900802)
                CenterArc((0, 0), 0.525, -16.601549599, 33.203099198)
            make_face()
            # Profile area: 0.8659014751, perimeter: 3.2986722863
            with BuildLine():
                CenterArc((2.2, 0), 0.525, -163.398450401, 326.796900802)
                CenterArc((2.2, 0), 0.525, 163.398450401, 33.203099198)
            make_face()
        # OneSide extrude, distance=0.25
        extrude(amount=0.25)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.25), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.0405713682, perimeter: 4.4882024099
            with BuildLine():
                Line((-1.1, -0.15), (-1.1, 0.15))
                Line((-1.1, -0.15), (-0.5031152949, -0.15))
                CenterArc((0, 0), 0.525, -163.398450401, 326.796900802)
                Line((-0.5031152949, 0.15), (-1.1, 0.15))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.8659014751, perimeter: 3.2986722863
            with BuildLine():
                CenterArc((0, 0), 0.525, -180, 163.398450401)
                CenterArc((0, 0), 0.525, -16.601549599, 33.203099198)
                CenterArc((0, 0), 0.525, 16.601549599, 163.398450401)
            make_face()
        # OneSide extrude, distance=-0.25
        extrude(amount=-0.25, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.25), x_dir=(1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.1520530844, perimeter: 1.3823007676
            Circle(0.22)
        # OneSide extrude, distance=0.25
        extrude(amount=0.25, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.25), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1590431281, perimeter: 1.4137166941
            with Locations((-2.2, 0)):
                Circle(0.225)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)
    return part.part


def model_137118_4ff32ab1_0003():
    """Model: ServoMotor SG-90 Body v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.655, perimeter: 6.86
            with BuildLine():
                Line((1.125, -0.59), (-1.125, -0.59))
                Line((1.125, 0.59), (1.125, -0.59))
                Line((-1.125, 0.59), (1.125, 0.59))
                Line((-1.125, -0.59), (-1.125, 0.59))
            make_face()
        # OneSide extrude, distance=2.27
        extrude(amount=2.27)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1.125, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.295, perimeter: 2.86
            with BuildLine():
                Line((-0.59, 1.84), (0.59, 1.84))
                Line((-0.59, 1.59), (-0.59, 1.84))
                Line((0.59, 1.59), (-0.59, 1.59))
                Line((0.59, 1.84), (0.59, 1.59))
            make_face()
        # OneSide extrude, distance=0.47
        extrude(amount=0.47, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.84), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0178845833, perimeter: 0.5795300458
            with BuildLine():
                Line((-1.4409934208, -0.065), (-1.595, -0.065))
                CenterArc((-1.365, 0), 0.1, 139.4583981265, 81.083203747)
                Line((-1.4409934208, 0.065), (-1.595, 0.065))
                Line((-1.595, 0.065), (-1.595, -0.065))
            make_face()
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with BuildLine():
                CenterArc((-1.365, 0), 0.1, 139.4583981265, 81.083203747)
                CenterArc((-1.365, 0), 0.1, -139.4583981265, 278.916796253)
            make_face()
        # OneSide extrude, distance=-0.25
        extrude(amount=-0.25, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.27), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.0234434046, perimeter: 3.8309562134
            with BuildLine():
                CenterArc((0.535, 0), 0.59, -90, 90)
                CenterArc((0.535, 0), 0.59, 0, 90)
                CenterArc((0.535, 0), 0.59, 90, 66.6468550067)
                CenterArc((-0.095, 0), 0.25, -69.3086672418, 138.6173344836)
                CenterArc((0.535, 0), 0.59, -156.6468550067, 66.6468550067)
            make_face()
            # Profile area: 0.1262045428, perimeter: 1.4469194446
            with BuildLine():
                CenterArc((0.535, 0), 0.59, 156.6468550067, 46.7062899867)
                CenterArc((-0.095, 0), 0.25, 69.3086672418, 221.3826655164)
            make_face()
            # Profile area: 0.0701449981, perimeter: 1.0857875613
            with BuildLine():
                CenterArc((-0.095, 0), 0.25, -69.3086672418, 138.6173344836)
                CenterArc((0.535, 0), 0.59, 156.6468550067, 46.7062899867)
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.67), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1661902514, perimeter: 1.4451326207
            with Locations((0.535, 0)):
                Circle(0.23)
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4, mode=Mode.SUBTRACT)
    return part.part


def model_137274_719a5ae0_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 79.9565496941, perimeter: 35.3548461197
            with BuildLine():
                Line((2.5, 0), (2.5, 6))
                Line((2.5, 6), (-2.0069548212, 9.605563857))
                CenterArc((-3.1314059068, 8.2), 1.8, 51.3401917459, 38.6598082541)
                Line((-6.5, 10), (-3.1314059068, 10))
                Line((-6.5, 0), (-6.5, 10))
                Line((2.5, 0), (-6.5, 0))
            make_face()
        # OneSide extrude, distance=-7.5
        extrude(amount=-7.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(2.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 14, perimeter: 15
            with BuildLine():
                Line((5.5, 0), (5.5, 4))
                Line((2, 4), (5.5, 4))
                Line((2, 0), (2, 4))
                Line((2, 0), (5.5, 0))
            make_face()
        # OneSide extrude, distance=-12.5
        extrude(amount=-12.5, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 10, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 15.1586734192, perimeter: 15.7371881863
            with BuildLine():
                Line((3.1314059068, -1.5), (3.1314059068, -6))
                Line((3.1314059068, -6), (6.5, -6))
                Line((6.5, -1.5), (6.5, -6))
                Line((6.5, -1.5), (3.1314059068, -1.5))
            make_face()
            # Profile area: 25.3413265808, perimeter: 20.2628118137
            with BuildLine():
                Line((3.1314059068, -1.5), (-2.5, -1.5))
                Line((-2.5, -1.5), (-2.5, -6))
                Line((-2.5, -6), (3.1314059068, -6))
                Line((3.1314059068, -1.5), (3.1314059068, -6))
            make_face()
        # OneSide extrude, distance=-4
        extrude(amount=-4, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -6), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((-3, 8)):
                Circle(1)
        # OneSide extrude, distance=-4
        extrude(amount=-4, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.9087385212, perimeter: 7.853981634
            with Locations((-0.4142560904, -3.75)):
                Circle(1.25)
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)
    return part.part


def model_137290_d81443d2_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 6.3739469719, perimeter: 31.8697348593
            with BuildLine():
                Line((1.443375673, 2.5), (-1.443375673, 2.5))
                Line((-1.443375673, 2.5), (-2.8867513459, 0))
                Line((-2.8867513459, 0), (-1.443375673, -2.5))
                Line((-1.443375673, -2.5), (1.443375673, -2.5))
                Line((1.443375673, -2.5), (2.8867513459, 0))
                Line((2.8867513459, 0), (1.443375673, 2.5))
            make_face()
            with BuildLine():
                Line((2.4248711306, 0), (1.2124355653, 2.1))
                Line((1.2124355653, -2.1), (2.4248711306, 0))
                Line((-1.2124355653, -2.1), (1.2124355653, -2.1))
                Line((-2.4248711306, 0), (-1.2124355653, -2.1))
                Line((-1.2124355653, 2.1), (-2.4248711306, 0))
                Line((1.2124355653, 2.1), (-1.2124355653, 2.1))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=17.7
        extrude(amount=17.7)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(2.1650635095, -1.25, 0), x_dir=(0.5, 0.8660254038, 0), z_dir=(0.8660254038, -0.5, 0))):
            # Profile area: 17.1625725196, perimeter: 33.863125464
            with BuildLine():
                Line((-0.5414518843, 16.842569839), (-0.5414518843, 0.9939108756))
                Line((-0.5414518843, 0.9939108756), (0.5414518843, 0.9939108756))
                Line((0.5414518843, 0.9939108756), (0.5414518843, 16.842569839))
                Line((0.5414518843, 16.842569839), (-0.5414518843, 16.842569839))
            make_face()
        # OneSide extrude, distance=-27.5
        extrude(amount=-27.5, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -2.5, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 1.015571166, perimeter: 3.751288694
            with BuildLine():
                Line((0.5414518843, 15.6873926088), (0.5414518843, 16.3126073912))
                Line((0.5414518843, 16.3126073912), (0, 16.6252147823))
                Line((0, 16.6252147823), (-0.5414518843, 16.3126073912))
                Line((-0.5414518843, 16.3126073912), (-0.5414518843, 15.6873926088))
                Line((-0.5414518843, 15.6873926088), (0, 15.3747852177))
                Line((0, 15.3747852177), (0.5414518843, 15.6873926088))
            make_face()
            # Profile area: 1.015571166, perimeter: 3.751288694
            with BuildLine():
                Line((0.5414518843, 13.6873926088), (0.5414518843, 14.3126073912))
                Line((0.5414518843, 14.3126073912), (0, 14.6252147823))
                Line((0, 14.6252147823), (-0.5414518843, 14.3126073912))
                Line((-0.5414518843, 14.3126073912), (-0.5414518843, 13.6873926088))
                Line((-0.5414518843, 13.6873926088), (0, 13.3747852177))
                Line((0, 13.3747852177), (0.5414518843, 13.6873926088))
            make_face()
            # Profile area: 1.015571166, perimeter: 3.751288694
            with BuildLine():
                Line((-0.5414518843, 12.3126073912), (-0.5414518843, 11.6873926088))
                Line((-0.5414518843, 11.6873926088), (0, 11.3747852177))
                Line((0, 11.3747852177), (0.5414518843, 11.6873926088))
                Line((0.5414518843, 11.6873926088), (0.5414518843, 12.3126073912))
                Line((0.5414518843, 12.3126073912), (0, 12.6252147823))
                Line((0, 12.6252147823), (-0.5414518843, 12.3126073912))
            make_face()
            # Profile area: 1.015571166, perimeter: 3.751288694
            with BuildLine():
                Line((-0.5414518843, 10.3126073912), (-0.5414518843, 9.6873926088))
                Line((-0.5414518843, 9.6873926088), (0, 9.3747852177))
                Line((0, 9.3747852177), (0.5414518843, 9.6873926088))
                Line((0.5414518843, 9.6873926088), (0.5414518843, 10.3126073912))
                Line((0.5414518843, 10.3126073912), (0, 10.6252147823))
                Line((0, 10.6252147823), (-0.5414518843, 10.3126073912))
            make_face()
            # Profile area: 1.015571166, perimeter: 3.751288694
            with BuildLine():
                Line((0.5414518843, 7.6873926088), (0.5414518843, 8.3126073912))
                Line((0.5414518843, 8.3126073912), (0, 8.6252147823))
                Line((0, 8.6252147823), (-0.5414518843, 8.3126073912))
                Line((-0.5414518843, 8.3126073912), (-0.5414518843, 7.6873926088))
                Line((-0.5414518843, 7.6873926088), (0, 7.3747852177))
                Line((0, 7.3747852177), (0.5414518843, 7.6873926088))
            make_face()
            # Profile area: 1.015571166, perimeter: 3.751288694
            with BuildLine():
                Line((0.5414518843, 5.6873926088), (0.5414518843, 6.3126073912))
                Line((0.5414518843, 6.3126073912), (0, 6.6252147823))
                Line((0, 6.6252147823), (-0.5414518843, 6.3126073912))
                Line((-0.5414518843, 6.3126073912), (-0.5414518843, 5.6873926088))
                Line((-0.5414518843, 5.6873926088), (0, 5.3747852177))
                Line((0, 5.3747852177), (0.5414518843, 5.6873926088))
            make_face()
            # Profile area: 1.015571166, perimeter: 3.751288694
            with BuildLine():
                Line((-0.5414518843, 4.3126073912), (-0.5414518843, 3.6873926088))
                Line((-0.5414518843, 3.6873926088), (0, 3.3747852177))
                Line((0, 3.3747852177), (0.5414518843, 3.6873926088))
                Line((0.5414518843, 3.6873926088), (0.5414518843, 4.3126073912))
                Line((0.5414518843, 4.3126073912), (0, 4.6252147823))
                Line((0, 4.6252147823), (-0.5414518843, 4.3126073912))
            make_face()
            # Profile area: 1.015571166, perimeter: 3.751288694
            with BuildLine():
                Line((-0.5414518843, 2.3126073912), (-0.5414518843, 1.6873926088))
                Line((-0.5414518843, 1.6873926088), (0, 1.3747852177))
                Line((0, 1.3747852177), (0.5414518843, 1.6873926088))
                Line((0.5414518843, 1.6873926088), (0.5414518843, 2.3126073912))
                Line((0.5414518843, 2.3126073912), (0, 2.6252147823))
                Line((0, 2.6252147823), (-0.5414518843, 2.3126073912))
            make_face()
        # OneSide extrude, distance=-14
        extrude(amount=-14, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-2.1650635095, -1.25, 0), x_dir=(0.5, -0.8660254038, 0), z_dir=(-0.8660254038, -0.5, 0))):
            # Profile area: 17.1353669774, perimeter: 33.8128799243
            with BuildLine():
                Line((0.5414518843, 0.9503772199), (-0.5414518843, 0.9503772199))
                Line((0.5414518843, 16.7739134134), (0.5414518843, 0.9503772199))
                Line((-0.5414518843, 16.7739134134), (0.5414518843, 16.7739134134))
                Line((-0.5414518843, 0.9503772199), (-0.5414518843, 16.7739134134))
            make_face()
        # OneSide extrude, distance=-10
        extrude(amount=-10, mode=Mode.SUBTRACT)
    return part.part


def model_137367_8c1f526a_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 10 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0443722339, perimeter: 1.0426990817
            with BuildLine():
                CenterArc((0, 0), 0.075, 0, 180)
                Line((-0.075, 0), (-0.075, -0.25))
                Line((-0.075, -0.25), (0.075, -0.25))
                Line((0.075, 0), (0.075, -0.25))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.025, -180, 180)
                CenterArc((0, 0), 0.025, 0, 180)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.15
        extrude(amount=0.15)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.075), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.006626797, perimeter: 0.4284291735
            with BuildLine():
                Line((-0.0375, -0.25), (0, -0.25))
                CenterArc((-0.075, -0.25), 0.0375, 180, 180)
                Line((-0.15, -0.25), (-0.1125, -0.25))
                CenterArc((-0.075, -0.25), 0.075, 180, 180)
            make_face()
        # OneSide extrude, distance=-0.15
        extrude(amount=-0.15, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.075), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0022089323, perimeter: 0.1928097245
            with BuildLine():
                CenterArc((-0.075, -0.25), 0.0375, 0, 180)
                Line((-0.1125, -0.25), (-0.0375, -0.25))
            make_face()
        # OneSide extrude, distance=-0.24
        extrude(amount=-0.24, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.075), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0050064501, perimeter: 0.3002580058
            with BuildLine():
                Line((-0.05, 0), (-0.1, 0))
                Line((-0.05, 0), (-0.05, 0.1001290029))
                Line((-0.05, 0.1001290029), (-0.075, 0.1001290029))
                Line((-0.075, 0.1001290029), (-0.1, 0.1001290029))
                Line((-0.1, 0.1001290029), (-0.1, 0))
            make_face()
            # Profile area: 0.008, perimeter: 0.42
            with BuildLine():
                Line((-0.1, 0), (-0.1, -0.16))
                Line((-0.075, -0.16), (-0.1, -0.16))
                Line((-0.075, -0.16), (-0.05, -0.16))
                Line((-0.05, -0.16), (-0.05, 0))
                Line((-0.05, 0), (-0.1, 0))
            make_face()
        # OneSide extrude, distance=-0.22
        extrude(amount=-0.22, mode=Mode.SUBTRACT)
    return part.part


def model_137393_0ccfdbe5_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.3862, perimeter: 10.46
            with BuildLine():
                Line((0, 1.41), (0, 0))
                Line((0, 0), (3.82, 0))
                Line((3.82, 0), (3.82, 1.41))
                Line((3.82, 1.41), (0, 1.41))
            make_face()
        # OneSide extrude, distance=0.14
        extrude(amount=0.14)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.5428, perimeter: 22.04
            with BuildLine():
                Line((-0.14, 1.55), (-0.14, -0.14))
                Line((-0.14, -0.14), (3.96, -0.14))
                Line((3.96, -0.14), (3.96, 1.55))
                Line((3.96, 1.55), (-0.14, 1.55))
            make_face()
            with BuildLine():
                Line((3.82, 1.41), (0, 1.41))
                Line((3.82, 0), (3.82, 1.41))
                Line((0, 0), (3.82, 0))
                Line((0, 1.41), (0, 0))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=5
        extrude(amount=5, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -1.55), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-1.91, 4.1)):
                Circle(0.2)
        # OneSide extrude, distance=-0.14
        extrude(amount=-0.14, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -1.55), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-1.91, 2.6)):
                Circle(0.2)
        # OneSide extrude, distance=-0.14
        extrude(amount=-0.14, mode=Mode.SUBTRACT)
    return part.part


def model_137433_1c5808b2_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.8221237391, perimeter: 18.2212373908
            with BuildLine():
                CenterArc((0, 0), 1.55, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.35, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=6
        extrude(amount=6)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0603872067, perimeter: 1.0717664278
            with BuildLine():
                Line((0.0987866561, 2.3398561032), (0.0012967357, 2.6398561032))
                Line((0.0012967357, 2.6398561032), (-0.112099394, 2.3398561032))
                CenterArc((-0.006656369, 2.3), 0.1127241789, 159.2940546142, 221.4118907717)
            make_face()
        # OneSide extrude, distance=3.6
        extrude(amount=3.6, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.7255526112, perimeter: 8.4823001647
            Circle(1.35)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch5 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=-2.3
        extrude(amount=-2.3, mode=Mode.SUBTRACT)
    return part.part


def model_137772_7e081a63_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 58.5209216676, perimeter: 37.846
            with BuildLine():
                Line((0, 3.89382), (0, 0))
                Line((0, 0), (15.02918, 0))
                Line((15.02918, 0), (15.02918, 3.89382))
                Line((15.02918, 3.89382), (0, 3.89382))
            make_face()
        # OneSide extrude, distance=3.19024
        extrude(amount=3.19024)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3.89382), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 5.5450276847, perimeter: 8.3475069903
            with BuildLine():
                CenterArc((-1.59512, -13.456793), 1.328547, -90, 180)
                CenterArc((-1.59512, -13.456793), 1.328547, 90, 180)
            make_face()
            # Profile area: 5.5450276847, perimeter: 8.3475069903
            with Locations((-1.59512, -9.494647)):
                Circle(1.328547)
            # Profile area: 5.5450276847, perimeter: 8.3475069903
            with Locations((-1.59512, -5.535041)):
                Circle(1.328547)
            # Profile area: 5.5450276847, perimeter: 8.3475069903
            with Locations((-1.59512, -1.572387)):
                Circle(1.328547)
        # OneSide extrude, distance=3.134106
        extrude(amount=3.134106, mode=Mode.ADD)

        # Sketch5 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 37 constraints, 13 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 10.8837661118, perimeter: 13.2530342
            with BuildLine():
                Line((3.0985206, -11.3177447), (3.0985206, -14.9374606))
                Line((3.0985206, -11.3177447), (0.0917194, -11.3177447))
                Line((0.0917194, -14.9374606), (0.0917194, -11.3177447))
                Line((3.0985206, -14.9374606), (0.0917194, -14.9374606))
            make_face()
            # Profile area: 10.8837661118, perimeter: 13.2530342
            with BuildLine():
                Line((3.0985206, -3.7114353), (0.0917194, -3.7114353))
                Line((3.0985206, -0.0917194), (3.0985206, -3.7114353))
                Line((0.0917194, -0.0917194), (3.0985206, -0.0917194))
                Line((0.0917194, -3.7114353), (0.0917194, -0.0917194))
            make_face()
            # Profile area: 11.0216571128, perimeter: 13.3447536
            with BuildLine():
                Line((3.0985206, -7.4687303), (0.0917194, -7.4687303))
                Line((3.0985206, -3.8031547), (3.0985206, -7.4687303))
                Line((0.0917194, -3.8031547), (3.0985206, -3.8031547))
                Line((0.0917194, -7.4687303), (0.0917194, -3.8031547))
            make_face()
            # Profile area: 11.0216571128, perimeter: 13.3447536
            with BuildLine():
                Line((0.0917194, -11.2260253), (3.0985206, -11.2260253))
                Line((3.0985206, -7.5604497), (3.0985206, -11.2260253))
                Line((0.0917194, -7.5604497), (3.0985206, -7.5604497))
                Line((0.0917194, -11.2260253), (0.0917194, -7.5604497))
            make_face()
        # OneSide extrude, distance=-3.741928
        extrude(amount=-3.741928, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 37 constraints, 13 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 10.8837661118, perimeter: 13.2530342
            with BuildLine():
                Line((3.0985206, -11.3177447), (3.0985206, -14.9374606))
                Line((3.0985206, -11.3177447), (0.0917194, -11.3177447))
                Line((0.0917194, -14.9374606), (0.0917194, -11.3177447))
                Line((3.0985206, -14.9374606), (0.0917194, -14.9374606))
            make_face()
            # Profile area: 10.8837661118, perimeter: 13.2530342
            with BuildLine():
                Line((3.0985206, -3.7114353), (0.0917194, -3.7114353))
                Line((3.0985206, -0.0917194), (3.0985206, -3.7114353))
                Line((0.0917194, -0.0917194), (3.0985206, -0.0917194))
                Line((0.0917194, -3.7114353), (0.0917194, -0.0917194))
            make_face()
            # Profile area: 11.0216571128, perimeter: 13.3447536
            with BuildLine():
                Line((3.0985206, -7.4687303), (0.0917194, -7.4687303))
                Line((3.0985206, -3.8031547), (3.0985206, -7.4687303))
                Line((0.0917194, -3.8031547), (3.0985206, -3.8031547))
                Line((0.0917194, -7.4687303), (0.0917194, -3.8031547))
            make_face()
            # Profile area: 11.0216571128, perimeter: 13.3447536
            with BuildLine():
                Line((0.0917194, -11.2260253), (3.0985206, -11.2260253))
                Line((3.0985206, -7.5604497), (3.0985206, -11.2260253))
                Line((0.0917194, -7.5604497), (3.0985206, -7.5604497))
                Line((0.0917194, -11.2260253), (0.0917194, -7.5604497))
            make_face()
        # OneSide extrude, distance=-3.81
        extrude(amount=-3.81, mode=Mode.ADD)
    return part.part


def model_137923_d4b1556f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1, perimeter: 4
            with BuildLine():
                Line((0, 0), (0, -1))
                Line((0, -1), (1, -1))
                Line((1, -1), (1, 0))
                Line((1, 0), (0, 0))
            make_face()
        # OneSide extrude, distance=10
        extrude(amount=10)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.2513274123, perimeter: 2.9132741229
            with BuildLine():
                CenterArc((-0.5, 10), 0.5, 0, 180)
                Line((-0.8, 10), (-1, 10))
                CenterArc((-0.5, 10), 0.3, 0, 180)
                Line((0, 10), (-0.2, 10))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -1, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.2513274123, perimeter: 2.9132741229
            with BuildLine():
                CenterArc((0.5, 0), 0.3, -180, 180)
                Line((0, 0), (0.2, 0))
                CenterArc((0.5, 0), 0.5, -180, 180)
                Line((0.8, 0), (1, 0))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.ADD)

        # Sketch3 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.1413716694, perimeter: 1.5424777961
            with BuildLine():
                Line((-0.2, 10), (-0.8, 10))
                CenterArc((-0.5, 10), 0.3, 180, 180)
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -1, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.1413716694, perimeter: 1.5424777961
            with BuildLine():
                CenterArc((0.5, 0), 0.3, 0, 180)
                Line((0.2, 0), (0.8, 0))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


def model_138161_8fa1cb24_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch3 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 16 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0885822258, perimeter: 1.3892754847
            with BuildLine():
                Line((0.5449527151, 0.6324721007), (0.3699999917, 0.6899999846))
                Line((0.3699999917, 0.6899999846), (0.3399999924, 0.6499999855))
                Line((0.3399999924, 0.6499999855), (0.26115737, 0.5448764889))
                CenterArc((1.9135902203, -0.6944481488), 2.0655410629, 143.1301023542, 7.1361084539)
                Line((0.1199999973, 0.3299999926), (0.1009627154, 0.2949724236))
                Line((0.1009627154, 0.2949724236), (0.3050923379, 0.2095043757))
                CenterArc((0.2568186928, 0.229752185), 0.0523480525, -22.7550366817, 45.5100733635)
                Line((0.3050923379, 0.2499999944), (0.3299999926, 0.2799999937))
                CenterArc((0.041334243, 0.5196662265), 0.3751903759, -39.7013288916, 29.0004104923)
                CenterArc((0.6663336105, 0.4015609942), 0.2608701993, 117.7291409395, 51.5699406612)
            make_face()
            # Profile area: 0.2011909145, perimeter: 2.5950523059
            with BuildLine():
                Line((0.0777901764, 0.2396277451), (0.2818848116, 0.1541743462))
                Line((0.0171968614, 0.137245944), (0.0777901764, 0.2396277451))
                CenterArc((-1.4590372688, 1.0109355921), 1.7154010634, -58.3924977538, 27.7738905949)
                Line((-0.6899999846, -0.5299999882), (-0.5599999875, -0.4499999899))
                CenterArc((-0.5646568905, -0.0022873125), 0.5423942839, -103.3613832699, 43.7842977596)
                CenterArc((-0.9418928026, 0.6401069628), 1.2873622956, -59.5770855103, 25.797772294)
                Line((0.2818848116, 0.1541743462), (0.1281437708, -0.0756607451))
            make_face()
        # OneSide extrude, distance=0.02
        extrude(amount=0.02)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 16 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0132768621, perimeter: 0.5625620817
            with BuildLine():
                Line((0.0777901764, 0.2396277451), (0.1009627154, 0.2949724236))
                Line((0.0777901764, 0.2396277451), (0.2818848116, 0.1541743462))
                Line((0.2818848116, 0.1541743462), (0.3050923379, 0.2095043757))
                Line((0.1009627154, 0.2949724236), (0.3050923379, 0.2095043757))
            make_face()
            # Profile area: 0.003, perimeter: 0.220000004
            with BuildLine():
                Line((0.2818848116, 0.1541743462), (0.3050923379, 0.2095043757))
                Line((0.2818848116, 0.1541743462), (0.3279931511, 0.1348347487))
                Line((0.3512006774, 0.1901647781), (0.3279931511, 0.1348347487))
                Line((0.3050923379, 0.2095043757), (0.3512006774, 0.1901647781))
            make_face()
            # Profile area: 0.0029927334, perimeter: 0.2197101828
            with BuildLine():
                Line((0.0547298937, 0.3140147628), (0.1009627154, 0.2949724236))
                Line((0.031669611, 0.2589381943), (0.0547298937, 0.3140147628))
                Line((0.0777901764, 0.2396277451), (0.031669611, 0.2589381943))
                Line((0.0777901764, 0.2396277451), (0.1009627154, 0.2949724236))
            make_face()
        # OneSide extrude, distance=0.03
        extrude(amount=0.03, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on XY construction plane
        # Sketch has 16 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0132768621, perimeter: 0.5625620817
            with BuildLine():
                Line((0.0777901764, 0.2396277451), (0.1009627154, 0.2949724236))
                Line((0.0777901764, 0.2396277451), (0.2818848116, 0.1541743462))
                Line((0.2818848116, 0.1541743462), (0.3050923379, 0.2095043757))
                Line((0.1009627154, 0.2949724236), (0.3050923379, 0.2095043757))
            make_face()
        # OneSide extrude, distance=-0.01
        extrude(amount=-0.01, mode=Mode.ADD)

        # Sketch3 -> Extrude4 (Join)
        # Sketch on XY construction plane
        # Sketch has 16 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.003, perimeter: 0.220000004
            with BuildLine():
                Line((0.2818848116, 0.1541743462), (0.3050923379, 0.2095043757))
                Line((0.2818848116, 0.1541743462), (0.3279931511, 0.1348347487))
                Line((0.3512006774, 0.1901647781), (0.3279931511, 0.1348347487))
                Line((0.3050923379, 0.2095043757), (0.3512006774, 0.1901647781))
            make_face()
        # OneSide extrude, distance=-0.01
        extrude(amount=-0.01, mode=Mode.ADD)

        # Sketch3 -> Extrude5 (Join)
        # Sketch on XY construction plane
        # Sketch has 16 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0029927334, perimeter: 0.2197101828
            with BuildLine():
                Line((0.0547298937, 0.3140147628), (0.1009627154, 0.2949724236))
                Line((0.031669611, 0.2589381943), (0.0547298937, 0.3140147628))
                Line((0.0777901764, 0.2396277451), (0.031669611, 0.2589381943))
                Line((0.0777901764, 0.2396277451), (0.1009627154, 0.2949724236))
            make_face()
        # OneSide extrude, distance=-0.01
        extrude(amount=-0.01, mode=Mode.ADD)
    return part.part


def model_138748_5721b4fa_0000():
    """Model: Batterie"""
    with BuildPart() as part:
        # Sketch1 -> Extrusion1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 260.1552876438, perimeter: 57.1769862953
            with Locations((21.3692372735, 6.6081411398)):
                Circle(9.1)
        # OneSide extrude, distance=66
        extrude(amount=66)

        # Sketch2 -> Extrusion2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(66, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 157.2124595013, perimeter: 44.4476099615
            with Locations((21.3692372735, 6.6081411398)):
                Circle(7.074056834)
        # OneSide extrude, distance=-0.01
        extrude(amount=-0.01, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrusion3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 157.2124595013, perimeter: 44.4476099615
            with Locations((-21.3692372735, 6.6081411398)):
                Circle(7.074056834)
        # OneSide extrude, distance=-0.01
        extrude(amount=-0.01, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrusion4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.01, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 30.7500642908, perimeter: 19.6574846889
            with Locations((-21.3692372735, 6.6081411398)):
                Circle(3.128585857)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)
    return part.part


def model_139041_2e8aee3e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.48, perimeter: 8.2
            with BuildLine():
                Line((1.45, -0.6), (1.45, 0.6))
                Line((1.45, 0.6), (-1.45, 0.6))
                Line((-1.45, 0.6), (-1.45, -0.6))
                Line((-1.45, -0.6), (1.45, -0.6))
            make_face()
        # OneSide extrude, distance=0.25
        extrude(amount=0.25)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.25), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.435, perimeter: 6.1
            with BuildLine():
                Line((-1.45, -0.45), (1.45, -0.45))
                Line((-1.45, -0.6), (-1.45, -0.45))
                Line((1.45, -0.6), (-1.45, -0.6))
                Line((1.45, -0.45), (1.45, -0.6))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.096211275, perimeter: 1.0995574288
            with Locations((-0.7999360544, 1.4639143031)):
                Circle(0.175)
            # Profile area: 0.4417864669, perimeter: 2.3561944902
            with Locations((0.0009253515, 1.5514358691)):
                Circle(0.375)
            # Profile area: 0.096211275, perimeter: 1.0995574288
            with Locations((0.8000634664, 1.4651525891)):
                Circle(0.175)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.25), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((1.0436060319, -0.0012103714)):
                Circle(0.15)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-1.0563935945, 0.000042268)):
                Circle(0.15)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)
    return part.part


def model_139254_697caddb_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrusion1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 26 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4.5947455592, perimeter: 19.2849555922
            with BuildLine():
                CenterArc((3.25, 1.8), 0.4, 0, 90)
                Line((3.25, 2.2), (1.6, 2.2))
                CenterArc((1.6, 1.8), 0.4, 90, 90)
                Line((1.2, 1.8), (1.2, 0.7))
                CenterArc((1, 0.7), 0.2, -90, 90)
                Line((0, 0.5), (1, 0.5))
                Line((0, 0.5), (0, 0))
                Line((0, 0), (4.9, 0))
                Line((4.9, 0), (4.9, 0.475))
                Line((3.85, 0.475), (4.9, 0.475))
                CenterArc((3.85, 0.675), 0.2, 180, 90)
                Line((3.65, 0.675), (3.65, 1.8))
            make_face()
            with BuildLine():
                Line((3.225, 1.725), (3.225, 0.475))
                Line((3.225, 0.475), (1.675, 0.475))
                Line((1.675, 0.475), (1.675, 1.725))
                Line((1.675, 1.725), (3.225, 1.725))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.9375, perimeter: 5.6
            with BuildLine():
                Line((1.675, 1.725), (3.225, 1.725))
                Line((1.675, 0.475), (1.675, 1.725))
                Line((3.225, 0.475), (1.675, 0.475))
                Line((3.225, 1.725), (3.225, 0.475))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch2 -> Extrusion2 (Cut)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.9375, perimeter: 5.6
            with BuildLine():
                Line((1.624669301, 1.712227893), (1.624669301, 0.462227893))
                Line((1.624669301, 0.462227893), (3.174669301, 0.462227893))
                Line((3.174669301, 0.462227893), (3.174669301, 1.712227893))
                Line((3.174669301, 1.712227893), (1.624669301, 1.712227893))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrusion3 (Join)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.855, perimeter: 6.2999999791
            with BuildLine():
                Line((1, 1), (1, 0.7000000104))
                Line((1, 0.7000000104), (3.85, 0.7000000104))
                Line((3.85, 1), (3.85, 0.7000000104))
                Line((1, 1), (3.85, 1))
            make_face()
            # Profile area: 0.855, perimeter: 6.3
            with BuildLine():
                Line((1, 1.3), (1, 1))
                Line((1, 1), (3.85, 1))
                Line((3.85, 1.3), (3.85, 1))
                Line((1, 1.3), (3.85, 1.3))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)
    return part.part


def model_139493_7f7d8123_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 18.0955736847, perimeter: 15.0796447372
            Circle(2.4)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1620453998, perimeter: 1.5995580157
            with BuildLine():
                CenterArc((0, 0), 2.4, 85.3497757884, 9.5604083527)
                Line((-0.2054256455, 1.9920996678), (-0.2054256455, 2.3911922349))
                Line((0.1945743545, 1.9920996678), (-0.2054256455, 1.9920996678))
                Line((0.1945743545, 2.3920996678), (0.1945743545, 1.9920996678))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            Circle(1.5)
        # OneSide extrude, distance=4
        extrude(amount=4, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 5), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 3.866976633, perimeter: 7.32
            with BuildLine():
                Line((-1.0565509926, -0.61), (0, -1.22))
                Line((0, -1.22), (1.0565509926, -0.61))
                Line((1.0565509926, -0.61), (1.0565509926, 0.61))
                Line((1.0565509926, 0.61), (0, 1.22))
                Line((0, 1.22), (-1.0565509926, 0.61))
                Line((-1.0565509926, 0.61), (-1.0565509926, -0.61))
            make_face()
        # OneSide extrude, distance=-5
        extrude(amount=-5, mode=Mode.SUBTRACT)
    return part.part


def model_139801_97e2ca6a_0000():
    """Model: led v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1590431281, perimeter: 1.4137166941
            Circle(0.225)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0019634954, perimeter: 0.1570796327
            with Locations((0.1000000015, 0)):
                Circle(0.025)
        # OneSide extrude, distance=-1.6
        extrude(amount=-1.6, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0019634954, perimeter: 0.1570796327
            with Locations((-0.1000000015, 0)):
                Circle(0.025)
        # OneSide extrude, distance=-1.8
        extrude(amount=-1.8, mode=Mode.ADD)
    return part.part


def model_140351_ffb3acec_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.9442957472, perimeter: 23.7490112583
            with BuildLine():
                Line((3, 7.5), (4.9610459858, 6.130516053))
                Line((4.9610459858, 6.130516053), (5.1752280708, 6.4144892366))
                Line((3.1255545498, 7.8458656571), (5.1752280708, 6.4144892366))
                CenterArc((2.5886345251, 6.9756686473), 1.0225096326, 58.3250102897, 106.5943289588)
                Line((-0.35, 0), (1.601339608, 7.2417037867))
                Line((-0.35, 0), (0, 0))
                Line((0, 0), (1.9288469573, 7.1582303039))
                CenterArc((2.5744534813, 6.9842660521), 0.6686339392, 50.4730053815, 114.446333867)
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(4.5040676768, 0, -6.4496439382), x_dir=(0, -1, 0), z_dir=(-0.5725505682, 0, 0.8198694084))):
            # Profile area: 0.0367061082, perimeter: 1.4503541352
            with BuildLine():
                Line((-0.1103148567, -1.8345210364), (0, -1.8345210364))
                Line((0, -2.5), (-0.1103148567, -1.8345210364))
                Line((0, -2.5), (0, -1.8345210364))
            make_face()
            # Profile area: 0.7380559504, perimeter: 5.4335708598
            with BuildLine():
                Line((0, -1.8345210364), (0, 0.5573793878))
                Line((-0.506814471, 0.5573793878), (0, 0.5573793878))
                Line((-0.1103148567, -1.8345210364), (-0.506814471, 0.5573793878))
                Line((-0.1103148567, -1.8345210364), (0, -1.8345210364))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.2149355073, 0, 0.1621115576), x_dir=(0, 1, 0), z_dir=(0.7983747184, 0, 0.6021609495))):
            # Profile area: 0.1802683821, perimeter: 1.7250071384
            with BuildLine():
                Line((0, -7.8817971884), (0, -8.2374862866))
                Line((0, -8.2374862866), (0.506814471, -8.2374862866))
                Line((0.506814471, -8.2374862866), (0.506814471, -7.8817971884))
                Line((0.506814471, -7.8817971884), (0, -7.8817971884))
            make_face()
        # OneSide extrude, distance=-0.02
        extrude(amount=-0.02, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(4.5040676768, 0, -6.4496439382), x_dir=(0, 1, 0), z_dir=(0.5725505682, 0, -0.8198694084))):
            # Profile area: 0.0258312129, perimeter: 1.216682569
            with BuildLine():
                Line((0, -2.5), (0.0925416489, -1.9417386517))
                Line((0, -1.9417386517), (0.0925416489, -1.9417386517))
                Line((0, -2.5), (0, -1.9417386517))
            make_face()
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4, mode=Mode.SUBTRACT)
    return part.part


def model_140400_0aab1cd3_0000():
    """Model: bigbocks v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 161.304, perimeter: 293.28
            with BuildLine():
                Line((36.66, 36.66), (36.66, -1.1))
                Line((-1.1, 36.66), (36.66, 36.66))
                Line((-1.1, -1.1), (-1.1, 36.66))
                Line((36.66, -1.1), (-1.1, -1.1))
            make_face()
            with BuildLine():
                Line((35.56, 0), (0, 0))
                Line((0, 0), (0, 35.56))
                Line((0, 35.56), (35.56, 35.56))
                Line((35.56, 35.56), (35.56, 0))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=8.89
        extrude(amount=8.89)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, -36.66), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-17.78, 7.2189034686)):
                Circle(0.5)
        # OneSide extrude, distance=-45
        extrude(amount=-45, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((17.78, 1.2383341843)):
                Circle(0.5)
        # OneSide extrude, distance=-72
        extrude(amount=-72, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(36.66, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((17.78, 6)):
                Circle(0.5)
        # OneSide extrude, distance=-56
        extrude(amount=-56, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-1.1, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-17.78, 0.7725293416)):
                Circle(0.5)
        # OneSide extrude, distance=-45
        extrude(amount=-45, mode=Mode.SUBTRACT)
    return part.part


def model_140600_a065e504_0000():
    """Model: 40rod v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            Circle(0.1)
        # OneSide extrude, distance=10
        extrude(amount=10)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 10), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.9999999944, perimeter: 10.7999999978
            with BuildLine():
                Line((2.5, -0.1999999989), (-2.5, -0.1999999989))
                Line((2.5, 0.2000000011), (2.5, -0.1999999989))
                Line((-2.5, 0.1999999989), (2.5, 0.2000000011))
                Line((-2.5, -0.1999999989), (-2.5, 0.1999999989))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((0, -7)):
                Circle(0.1)
        # OneSide extrude, distance=-10
        extrude(amount=-10)

        # Sketch5 -> Extrude5 (NewBody)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 10), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.9685840735, perimeter: 11.4283185307
            with BuildLine():
                Line((2.5, -6.8), (2.5, -7.2))
                Line((-2.5, -6.8), (2.5, -6.8))
                Line((-2.5, -7.2), (-2.5, -6.8))
                Line((2.5, -7.2), (-2.5, -7.2))
            make_face()
            with BuildLine():
                CenterArc((0, -7), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((0, -7)):
                Circle(0.1)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch6 -> Extrude6 (NewBody)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 11.1178107405, perimeter: 49.4125065695
            with BuildLine():
                CenterArc((-0.3280205493, -0.7735421446), 3.3886016444, 176.5551610357, 125.6931573669)
                Line((1.4801023655, -3.6394299005), (6.1936842151, -0.6655746491))
                Line((6.1936842151, -0.6655746491), (1.6058256869, 2.551632639))
                CenterArc((-0.3397250517, -0.2227958477), 3.3886016444, 54.96017973, 130.9196012593)
            make_face()
            with BuildLine():
                CenterArc((-0.3397250517, -0.2227958477), 2.9386016444, 54.96017973, 131.6355231197)
                Line((5.3816977968, -0.6457903814), (1.347460165, 2.1831936928))
                Line((1.2399870031, -3.2588453334), (5.3816977968, -0.6457903814))
                CenterArc((-0.3280205493, -0.7735421446), 2.9386016444, 175.8392391753, 126.4090792274)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


def model_140600_a065e504_0001():
    """Model: 38rod v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            Circle(0.1)
        # OneSide extrude, distance=10
        extrude(amount=10)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 10), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.9999999944, perimeter: 10.7999999978
            with BuildLine():
                Line((2.5, -0.1999999989), (-2.5, -0.1999999989))
                Line((2.5, 0.2000000011), (2.5, -0.1999999989))
                Line((-2.5, 0.1999999989), (2.5, 0.2000000011))
                Line((-2.5, -0.1999999989), (-2.5, 0.1999999989))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((0, -9)):
                Circle(0.1)
        # OneSide extrude, distance=-10
        extrude(amount=-10)

        # Sketch4 -> Extrude4 (NewBody)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 10), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.9685840735, perimeter: 11.4283185307
            with BuildLine():
                Line((2.5, -9.2), (-2.5, -9.2))
                Line((2.5, -8.8), (2.5, -9.2))
                Line((-2.5, -8.8), (2.5, -8.8))
                Line((-2.5, -9.2), (-2.5, -8.8))
            make_face()
            with BuildLine():
                CenterArc((0, -9), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((0, -9)):
                Circle(0.1)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch5 -> Extrude5 (NewBody)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 14.4122241571, perimeter: 64.0543343392
            with BuildLine():
                CenterArc((-0.3280205493, -0.7735421446), 4.3886016444, 177.6191356138, 124.6291827889)
                Line((2.0136920595, -4.4851733831), (7.998098478, -0.7095396884))
                Line((7.998098478, -0.7095396884), (2.1799712911, 3.3703858528))
                CenterArc((-0.3397250517, -0.2227958477), 4.3886016444, 54.96017973, 129.8556266812)
            make_face()
            with BuildLine():
                CenterArc((-0.3397250517, -0.2227958477), 3.9386016444, 54.96017973, 130.2673879459)
                Line((7.1861120597, -0.6897554207), (1.9216057692, 3.0019469066))
                Line((1.7735766972, -4.104588816), (7.1861120597, -0.6897554207))
                CenterArc((-0.3280205493, -0.7735421446), 3.9386016444, 177.2073743492, 125.0409440535)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


def model_140600_a065e504_0002():
    """Model: 37rodv1:1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            Circle(0.1)
        # OneSide extrude, distance=10
        extrude(amount=10)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 10), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.9999999944, perimeter: 10.7999999978
            with BuildLine():
                Line((2.5, -0.1999999989), (-2.5, -0.1999999989))
                Line((2.5, 0.2000000011), (2.5, -0.1999999989))
                Line((-2.5, 0.1999999989), (2.5, 0.2000000011))
                Line((-2.5, -0.1999999989), (-2.5, 0.1999999989))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch3 -> Extrude4 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0314159275, perimeter: 0.6283185401
            with Locations((0, -10)):
                Circle(0.1000000015)
        # OneSide extrude, distance=-10
        extrude(amount=-10)

        # Sketch4 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 10), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.9685840725, perimeter: 11.4283185401
            with BuildLine():
                Line((2.5, -10.2), (-2.5, -10.2))
                Line((2.5, -9.8), (2.5, -10.2))
                Line((-2.5, -9.8), (2.5, -9.8))
                Line((-2.5, -10.2), (-2.5, -9.8))
            make_face()
            with BuildLine():
                CenterArc((0, -10), 0.1000000015, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0314159275, perimeter: 0.6283185401
            with Locations((0, -10)):
                Circle(0.1000000015)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch5 -> Extrude6 (NewBody)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 16.0594609301, perimeter: 71.3753849231
            with BuildLine():
                CenterArc((-0.3280205493, -0.7735421446), 4.8886016444, 177.9875814829, 124.2607369198)
                Line((2.2804869066, -4.9080451244), (8.9003056095, -0.7315222081))
                Line((8.9003056095, -0.7315222081), (2.4670440932, 3.7797624598))
                CenterArc((-0.3397250517, -0.2227958477), 4.8886016444, 54.96017973, 129.4871808121)
            make_face()
            with BuildLine():
                CenterArc((-0.3397250517, -0.2227958477), 4.4386016444, 54.96017973, 129.8150396444)
                Line((8.0883191912, -0.7117379404), (2.2086785713, 3.4113235135))
                Line((2.0403715442, -4.5274605573), (8.0883191912, -0.7117379404))
                CenterArc((-0.3280205493, -0.7735421446), 4.4386016444, 177.6597226506, 124.588595752)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


def model_140600_a065e504_0003():
    """Model: 41rod v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            Circle(0.1)
        # OneSide extrude, distance=10
        extrude(amount=10)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 10), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.9999999944, perimeter: 10.7999999978
            with BuildLine():
                Line((2.5, -0.1999999989), (-2.5, -0.1999999989))
                Line((2.5, 0.2000000011), (2.5, -0.1999999989))
                Line((-2.5, 0.1999999989), (2.5, 0.2000000011))
                Line((-2.5, -0.1999999989), (-2.5, 0.1999999989))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((0, -6)):
                Circle(0.1)
        # OneSide extrude, distance=-10
        extrude(amount=-10)

        # Sketch4 -> Extrude4 (NewBody)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 10), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.9685840735, perimeter: 11.4283185307
            with BuildLine():
                Line((2.4999999627, -6.2000000864), (-2.5000000373, -6.2000000864))
                Line((2.4999999627, -5.8000000864), (2.4999999627, -6.2000000864))
                Line((-2.5000000373, -5.8000000864), (2.4999999627, -5.8000000864))
                Line((-2.5000000373, -6.2000000864), (-2.5000000373, -5.8000000864))
            make_face()
            with BuildLine():
                CenterArc((0, -6), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((0, -6)):
                Circle(0.1)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch5 -> Extrude5 (NewBody)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 9.4706682447, perimeter: 42.0918877603
            with BuildLine():
                CenterArc((-0.3280205493, -0.7735421446), 2.8886016444, 175.7458635428, 126.5024548599)
                Line((1.2133075184, -3.2165581592), (5.2914770836, -0.6435921294))
                Line((5.2914770836, -0.6435921294), (1.3187528848, 2.1422560321))
                CenterArc((-0.3397250517, -0.2227958477), 2.8886016444, 54.96017973, 131.7288987522)
            make_face()
            with BuildLine():
                CenterArc((-0.3397250517, -0.2227958477), 2.4386016444, 54.96017973, 132.7425777483)
                Line((4.4794906653, -0.6238078617), (1.0603873629, 1.7738170859))
                Line((0.9731921561, -2.835973592), (4.4794906653, -0.6238078617))
                CenterArc((-0.3280205493, -0.7735421446), 2.4386016444, 174.7321845468, 127.5161338559)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


def model_140600_a065e504_0004():
    """Model: 46rod v5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            Circle(0.1)
        # OneSide extrude, distance=10
        extrude(amount=10)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 10), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.9999999944, perimeter: 10.7999999978
            with BuildLine():
                Line((2.5, -0.1999999989), (-2.5, -0.1999999989))
                Line((2.5, 0.2000000011), (2.5, -0.1999999989))
                Line((-2.5, 0.1999999989), (2.5, 0.2000000011))
                Line((-2.5, -0.1999999989), (-2.5, 0.1999999989))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((0, -1)):
                Circle(0.1)
        # OneSide extrude, distance=-10
        extrude(amount=-10)

        # Sketch4 -> Extrude4 (NewBody)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 10), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.9685840735, perimeter: 11.4283185307
            with BuildLine():
                Line((2.5, -1.2), (-2.5, -1.2))
                Line((2.5, -0.8), (2.5, -1.2))
                Line((-2.5, -0.8), (2.5, -0.8))
                Line((-2.5, -1.2), (-2.5, -0.8))
            make_face()
            with BuildLine():
                CenterArc((0, -1), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((0, -1)):
                Circle(0.1)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch6 -> Extrude6 (NewBody)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.892475682, perimeter: 8.993472932
            with BuildLine():
                CenterArc((-0.3397250517, -0.2227958477), 0.4886016444, 54.96017973, 160.5708590598)
                CenterArc((-0.3280205493, -0.7735421446), 0.4886016444, 146.9039032353, 155.3444151674)
                Line((-0.0673077474, -1.186773801), (0.9608828526, -0.5380760351))
                Line((0.9608828526, -0.5380760351), (-0.0591965653, 0.1772483189))
            make_face()
            with BuildLine():
                Line((-0.1740256862, -1.0176251044), (0.6, -0.5292830272))
                CenterArc((-0.3280205493, -0.7735421446), 0.2886016444, 108.590896073, 193.6574223297)
                CenterArc((-0.3397250517, -0.2227958477), 0.2886016444, 54.96017973, 198.8838662221)
                Line((0.6, -0.5292830272), (-0.1740256862, 0.0134976761))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


def model_140600_a065e504_0005():
    """Model: 45rod v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            Circle(0.1)
        # OneSide extrude, distance=10
        extrude(amount=10)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 10), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.9999999944, perimeter: 10.7999999978
            with BuildLine():
                Line((2.5, -0.1999999989), (-2.5, -0.1999999989))
                Line((2.5, 0.2000000011), (2.5, -0.1999999989))
                Line((-2.5, 0.1999999989), (2.5, 0.2000000011))
                Line((-2.5, -0.1999999989), (-2.5, 0.1999999989))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((0, -2)):
                Circle(0.1)
        # OneSide extrude, distance=-10
        extrude(amount=-10)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 10), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.9685840735, perimeter: 11.4283185307
            with BuildLine():
                Line((2.5, -2.2), (-2.5, -2.2))
                Line((2.5, -1.8), (2.5, -2.2))
                Line((-2.5, -1.8), (2.5, -1.8))
                Line((-2.5, -2.2), (-2.5, -1.8))
            make_face()
            with BuildLine():
                CenterArc((0, -2), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((0, -2)):
                Circle(0.1)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch6 -> Extrude6 (NewBody)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 2.3745354494, perimeter: 13.5737249937
            with BuildLine():
                Line((1.6826485578, -0.5556620508), (0.1704616764, 0.5047496044))
                CenterArc((-0.3397250517, -0.2227958477), 0.8886016444, 54.96017973, 144.3144070302)
                CenterArc((-0.3280205493, -0.7735421446), 0.8886016444, 163.1603552649, 139.0879631378)
                Line((0.1461281303, -1.525071194), (1.6826485578, -0.5556620508))
            make_face()
            with BuildLine():
                CenterArc((-0.3280205493, -0.7735421446), 0.5386016444, 150.4610303408, 151.7872880619)
                CenterArc((-0.3397250517, -0.2227958477), 0.5386016444, 54.96017973, 157.0137319543)
                Line((1.0511035657, -0.540274287), (-0.0304892851, 0.2181859796))
                Line((-0.0406282627, -1.2290609751), (1.0511035657, -0.540274287))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


def model_140600_a065e504_0006():
    """Model: 44rod v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            Circle(0.1)
        # OneSide extrude, distance=10
        extrude(amount=10)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 10), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.9999999944, perimeter: 10.7999999978
            with BuildLine():
                Line((2.5, -0.1999999989), (-2.5, -0.1999999989))
                Line((2.5, 0.2000000011), (2.5, -0.1999999989))
                Line((-2.5, 0.1999999989), (2.5, 0.2000000011))
                Line((-2.5, -0.1999999989), (-2.5, 0.1999999989))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((0, -3)):
                Circle(0.1)
        # OneSide extrude, distance=-10
        extrude(amount=-10)

        # Sketch4 -> Extrude4 (NewBody)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 10), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.9685840735, perimeter: 11.4283185307
            with BuildLine():
                Line((-2.5, -2.8), (2.5, -2.8))
                Line((-2.5, -3.2), (-2.5, -2.8))
                Line((2.5, -3.2), (-2.5, -3.2))
                Line((2.5, -2.8), (2.5, -3.2))
            make_face()
            with BuildLine():
                CenterArc((0, -3), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((0, -3)):
                Circle(0.1)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch6 -> Extrude6 (NewBody)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 4.5308734994, perimeter: 20.1381281787
            with BuildLine():
                Line((0.4129229773, -1.9479429353), (2.5848556892, -0.5776445705))
                Line((2.5848556892, -0.5776445705), (0.4575344785, 0.9141262113))
                CenterArc((-0.3397250517, -0.2227958477), 1.3886016444, 54.96017973, 137.6980400192)
                CenterArc((-0.3280205493, -0.7735421446), 1.3886016444, 169.7767222758, 132.4715961269)
            make_face()
            with BuildLine():
                CenterArc((-0.3280205493, -0.7735421446), 0.9386016444, 164.1526843518, 138.0956340509)
                CenterArc((-0.3397250517, -0.2227958477), 0.9386016444, 54.96017973, 143.3220779433)
                Line((1.7728692709, -0.5578603028), (0.1991689566, 0.5456872651))
                Line((0.172807615, -1.5673583681), (1.7728692709, -0.5578603028))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


def model_140600_a065e504_0007():
    """Model: 39rod v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            Circle(0.1)
        # OneSide extrude, distance=10
        extrude(amount=10)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 10), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.9999999944, perimeter: 10.7999999978
            with BuildLine():
                Line((2.5, -0.1999999989), (-2.5, -0.1999999989))
                Line((2.5, 0.2000000011), (2.5, -0.1999999989))
                Line((-2.5, 0.1999999989), (2.5, 0.2000000011))
                Line((-2.5, -0.1999999989), (-2.5, 0.1999999989))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((0, -8)):
                Circle(0.1)
        # OneSide extrude, distance=-10
        extrude(amount=-10)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 10), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.9685840735, perimeter: 11.4283185307
            with BuildLine():
                Line((2.5, -8.2), (-2.5, -8.2))
                Line((2.5, -7.8), (2.5, -8.2))
                Line((-2.5, -7.8), (2.5, -7.8))
                Line((-2.5, -8.2), (-2.5, -7.8))
            make_face()
            with BuildLine():
                CenterArc((0, -8), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((0, -8)):
                Circle(0.1)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch6 -> Extrude5 (NewBody)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 12.7650036847, perimeter: 56.7333576663
            with BuildLine():
                Line((7.0958913465, -0.6875571687), (1.892898489, 2.9610092459))
                CenterArc((-0.3397250517, -0.2227958477), 3.8886016444, 54.96017973, 130.3190361371)
                CenterArc((-0.3280205493, -0.7735421446), 3.8886016444, 177.155726158, 125.0925922447)
                Line((1.7468972125, -4.0623016418), (7.0958913465, -0.6875571687))
            make_face()
            with BuildLine():
                Line((1.5067818502, -3.6817170747), (6.2839049282, -0.6677729011))
                CenterArc((-0.3280205493, -0.7735421446), 3.4386016444, 176.6231014876, 125.6252169151)
                CenterArc((-0.3397250517, -0.2227958477), 3.4386016444, 54.96017973, 130.8516608074)
                Line((6.2839049282, -0.6677729011), (1.6345329671, 2.5925702997))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


def model_140600_a065e504_0008():
    """Model: 43rod v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            Circle(0.1)
        # OneSide extrude, distance=10
        extrude(amount=10)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 10), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.9999999944, perimeter: 10.7999999978
            with BuildLine():
                Line((2.5, -0.1999999989), (-2.5, -0.1999999989))
                Line((2.5, 0.2000000011), (2.5, -0.1999999989))
                Line((-2.5, 0.1999999989), (2.5, 0.2000000011))
                Line((-2.5, -0.1999999989), (-2.5, 0.1999999989))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((0, -4)):
                Circle(0.1)
        # OneSide extrude, distance=-10
        extrude(amount=-10)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 10), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.9685840735, perimeter: 11.4283185307
            with BuildLine():
                Line((2.5, -4.2), (-2.5, -4.2))
                Line((2.5, -3.8), (2.5, -4.2))
                Line((-2.5, -3.8), (2.5, -3.8))
                Line((-2.5, -4.2), (-2.5, -3.8))
            make_face()
            with BuildLine():
                CenterArc((0, -4), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((0, -4)):
                Circle(0.1)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch6 -> Extrude6 (NewBody)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 6.1768422709, perimeter: 27.4528318775
            with BuildLine():
                Line((3.4870628207, -0.5996270901), (0.7446072806, 1.3235028183))
                CenterArc((-0.3397250517, -0.2227958477), 1.8886016444, 54.96017973, 134.6432670529)
                CenterArc((-0.3280205493, -0.7735421446), 1.8886016444, 172.8314952421, 129.4168231605)
                Line((0.6797178243, -2.3708146766), (3.4870628207, -0.5996270901))
            make_face()
            with BuildLine():
                CenterArc((-0.3280205493, -0.7735421446), 1.4386016444, 170.1794439596, 132.068874443)
                CenterArc((-0.3397250517, -0.2227958477), 1.4386016444, 54.96017973, 137.2953183354)
                Line((2.6750764024, -0.5798428224), (0.4862417587, 0.955063872))
                Line((0.439602462, -1.9902301094), (2.6750764024, -0.5798428224))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


def model_140600_a065e504_0009():
    """Model: 36rod v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            Circle(0.1)
        # OneSide extrude, distance=10
        extrude(amount=10)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 10), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.9999999944, perimeter: 10.7999999978
            with BuildLine():
                Line((2.5, -0.1999999989), (-2.5, -0.1999999989))
                Line((2.5, 0.2000000011), (2.5, -0.1999999989))
                Line((-2.5, 0.1999999989), (2.5, 0.2000000011))
                Line((-2.5, -0.1999999989), (-2.5, 0.1999999989))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((0, -11)):
                Circle(0.1)
        # OneSide extrude, distance=-10
        extrude(amount=-10)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 10), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.9685840735, perimeter: 11.4283185307
            with BuildLine():
                Line((-2.5, -10.8), (2.5, -10.8))
                Line((-2.5, -11.2), (-2.5, -10.8))
                Line((2.5, -11.2), (-2.5, -11.2))
                Line((2.5, -10.8), (2.5, -11.2))
            make_face()
            with BuildLine():
                CenterArc((0, -11), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((0, -11)):
                Circle(0.1)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (NewBody)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 17.706707972, perimeter: 78.6964818758
            with BuildLine():
                CenterArc((-0.3280205493, -0.7735421446), 5.3886016444, 178.2875528519, 123.9607655508)
                Line((2.5472817536, -5.3309168657), (9.8025127409, -0.7535047277))
                Line((9.8025127409, -0.7535047277), (2.7541168953, 4.1891390667))
                CenterArc((-0.3397250517, -0.2227958477), 5.3886016444, 54.96017973, 129.1872094431)
            make_face()
            with BuildLine():
                CenterArc((-0.3397250517, -0.2227958477), 4.9386016444, 54.96017973, 129.4544462092)
                Line((8.9905263226, -0.73372046), (2.4957513734, 3.8207001205))
                Line((2.3071663913, -4.9503322986), (8.9905263226, -0.73372046))
                CenterArc((-0.3280205493, -0.7735421446), 4.9386016444, 178.0203160859, 124.2280023168)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


def model_140600_a065e504_0015():
    """Model: 35rod v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            Circle(0.1)
        # OneSide extrude, distance=10
        extrude(amount=10)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 10), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.9999999944, perimeter: 10.7999999978
            with BuildLine():
                Line((2.5, -0.1999999989), (-2.5, -0.1999999989))
                Line((2.5, 0.2000000011), (2.5, -0.1999999989))
                Line((-2.5, 0.1999999989), (2.5, 0.2000000011))
                Line((-2.5, -0.1999999989), (-2.5, 0.1999999989))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch5 -> Extrude4 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((0, -12)):
                Circle(0.1)
        # OneSide extrude, distance=-10
        extrude(amount=-10)

        # Sketch6 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 10), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.9685840735, perimeter: 11.4283185307
            with BuildLine():
                Line((2.5, -11.8), (2.5, -12.2))
                Line((-2.5, -11.8), (2.5, -11.8))
                Line((-2.5, -12.2), (-2.5, -11.8))
                Line((2.5, -12.2), (-2.5, -12.2))
            make_face()
            with BuildLine():
                CenterArc((0, -12), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((0, -12)):
                Circle(0.1)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch7 -> Extrude6 (NewBody)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 19.3539618053, perimeter: 86.0176094036
            with BuildLine():
                CenterArc((-0.3280205493, -0.7735421446), 5.8886016444, 178.5365217974, 123.7117966052)
                Line((2.8140766006, -5.7537886071), (10.7047198724, -0.7754872474))
                Line((10.7047198724, -0.7754872474), (3.0411896974, 4.5985156736))
                CenterArc((-0.3397250517, -0.2227958477), 5.8886016444, 54.96017973, 128.9382404976)
            make_face()
            with BuildLine():
                CenterArc((-0.3397250517, -0.2227958477), 5.4386016444, 54.96017973, 129.1602499442)
                Line((9.8927334541, -0.7557029797), (2.7828241755, 4.2300767274))
                Line((2.5739612383, -5.3732040399), (9.8927334541, -0.7557029797))
                CenterArc((-0.3280205493, -0.7735421446), 5.4386016444, 178.3145123509, 123.9338060518)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


def model_140628_4b9e7242_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 29.758005, perimeter: 22.0375266243
            with BuildLine():
                Line((0, 0), (5.715, 0))
                Line((5.715, 0), (5.715, 6.35))
                Line((5.715, 6.35), (4.1148, 6.35))
                Line((0, 3.175), (4.1148, 6.35))
                Line((0, 0), (0, 3.175))
            make_face()
        # Symmetric extrude, full_length=True, total=5.08
        extrude(amount=2.54, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(2.54, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 6.532245, perimeter: 12.4871266243
            with BuildLine():
                Line((0, 6.35), (0, 3.175))
                Line((0, 3.175), (4.1148, 6.35))
                Line((4.1148, 6.35), (0, 6.35))
            make_face()
        # OneSide extrude, distance=-1.27
        extrude(amount=-1.27, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-2.54, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 6.532245, perimeter: 12.4871266243
            with BuildLine():
                Line((0, 3.175), (-4.1148, 6.35))
                Line((0, 6.35), (0, 3.175))
                Line((-4.1148, 6.35), (0, 6.35))
            make_face()
        # OneSide extrude, distance=-1.27
        extrude(amount=-1.27, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(2.54, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.57676704, perimeter: 7.6708
            with BuildLine():
                Line((0, 2.2352), (0, 0))
                Line((0, 0), (1.6002, 0))
                Line((1.6002, 0), (1.6002, 2.2352))
                Line((1.6002, 2.2352), (0, 2.2352))
            make_face()
            # Profile area: 3.57676704, perimeter: 7.6708
            with BuildLine():
                Line((4.1148, 0), (4.1148, 2.2352))
                Line((5.715, 0), (4.1148, 0))
                Line((5.715, 2.2352), (5.715, 0))
                Line((4.1148, 2.2352), (5.715, 2.2352))
            make_face()
        # OneSide extrude, distance=1.27
        extrude(amount=1.27, mode=Mode.ADD)
    return part.part


def model_140735_cbd9cc5f_0000():
    """Model: Cabin"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 28.2743338823, perimeter: 56.5486677646
            with BuildLine():
                CenterArc((0, 0), 5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 4, -172.1145744517, 164.2291489034)
                CenterArc((0, 0), 4, 173.2360365957, 14.6493889526)
                CenterArc((0, 0), 4, 6.7639634043, 166.4720731914)
                CenterArc((0, 0), 4, -7.8854255483, 14.6493889526)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.1217782237, perimeter: 17.6880814537
            with BuildLine():
                CenterArc((0, 0), 4, -6.4023278869, 12.8046557738)
                Line((-3.9750535577, 0.4460372328), (3.9750535577, 0.4460372328))
                CenterArc((0, 0), 4, 173.5976721131, 12.8046557738)
                Line((3.9750535577, -0.4460372328), (-3.9750535577, -0.4460372328))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.ADD)

        # Sketch6 -> Extrude4 (Join)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 222.2233604623, perimeter: 64.7289823643
            with BuildLine():
                Line((0, -5.028539117), (0, 4.9718338198))
                Line((0, 4.9718338198), (-13.5226344816, 4.9718338198))
                Line((-13.5226344816, 4.9718338198), (-15.4855140085, 4.768946461))
                Line((-15.4855140085, 4.768946461), (-17.1560281891, 4.3605985502))
                Line((-17.1560281891, 4.3605985502), (-18.6161813247, 3.7913863109))
                Line((-18.6161813247, 3.7913863109), (-19.8721605049, 3.0922451909))
                Line((-19.8721605049, 3.0922451909), (-20.7631014012, 2.3745428022))
                Line((-20.7631014012, 2.3745428022), (-22.1467679971, 0.9626824497))
                Line((-22.1467679971, 0.9626824497), (-23.9591056576, 0.1482311124))
                Line((-23.9591056576, 0.1482311124), (-24.5778670111, -0.2528216672))
                Line((-24.5778670111, -0.2528216672), (-25.1586209125, -0.8454090798))
                Line((-25.1586209125, -0.8454090798), (-25.4691100563, -1.329039684))
                Line((-25.4691100563, -1.329039684), (-25.540577659, -1.8461288093))
                Line((-25.540577659, -1.8461288093), (-25.4691100563, -2.2370986358))
                Line((-25.4691100563, -2.2370986358), (-25.2378913418, -2.7247599247))
                Line((-25.2378913418, -2.7247599247), (-24.6661505203, -3.3385405124))
                Line((-24.6661505203, -3.3385405124), (-23.8463750778, -3.897669404))
                Line((-23.8463750778, -3.897669404), (-22.429634954, -4.3853306929))
                Line((-22.429634954, -4.3853306929), (-20.9162033678, -4.6585891737))
                Line((-20.9162033678, -4.6585891737), (-19.5372990337, -4.8267482388))
                Line((-19.5372990337, -4.8267482388), (-17.7043652237, -4.9570715143))
                Line((-17.7043652237, -4.9570715143), (-15.4468297743, -5.028539117))
                Line((-15.4468297743, -5.028539117), (-13.8367067256, -5.028539117))
                Line((-13.8367067256, -5.028539117), (0, -5.028539117))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


def model_141399_f6311635_0000():
    """Model: Component1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 638.7084, perimeter: 101.6
            with BuildLine():
                Line((22.86, -27.94), (0, -27.94))
                Line((22.86, 0), (22.86, -27.94))
                Line((0, 0), (22.86, 0))
                Line((0, -27.94), (0, 0))
            make_face()
        # OneSide extrude, distance=0.508
        extrude(amount=0.508)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 25.599771, perimeter: 42.8546
            with BuildLine():
                Line((1.3513517695, 26.5886482305), (21.5086482305, 26.5886482305))
                Line((1.3513517695, 25.3186482305), (1.3513517695, 26.5886482305))
                Line((21.5086517695, 25.3186482305), (1.3513517695, 25.3186482305))
                Line((21.5086517695, 26.5886482305), (21.5086517695, 25.3186482305))
                Line((21.5086482305, 26.5886482305), (21.5086517695, 26.5886482305))
            make_face()
        # OneSide extrude, distance=-0.127
        extrude(amount=-0.127, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 11.2903, perimeter: 20.32
            with BuildLine():
                Line((2.6213517695, 16.4286482305), (1.3513517695, 16.4286482305))
                Line((2.6213517695, 25.3186482305), (2.6213517695, 16.4286482305))
                Line((1.3513517695, 25.3186482305), (2.6213517695, 25.3186482305))
                Line((1.3513517695, 16.4286482305), (1.3513517695, 25.3186482305))
            make_face()
        # OneSide extrude, distance=-0.127
        extrude(amount=-0.127, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 11.2903, perimeter: 20.32
            with BuildLine():
                Line((20.2386517695, 25.3186482305), (20.2386517695, 16.4286482305))
                Line((20.2386517695, 16.4286482305), (21.5086517695, 16.4286482305))
                Line((21.5086517695, 16.4286482305), (21.5086517695, 25.3186482305))
                Line((21.5086517695, 25.3186482305), (20.2386517695, 25.3186482305))
            make_face()
        # OneSide extrude, distance=-0.127
        extrude(amount=-0.127, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.508, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 588.127856, perimeter: 97.536
            with BuildLine():
                Line((-0.508, 0.508), (-0.508, 27.432))
                Line((-0.508, 27.432), (-22.352, 27.432))
                Line((-22.352, 27.432), (-22.352, 0.508))
                Line((-22.352, 0.508), (-0.508, 0.508))
            make_face()
        # OneSide extrude, distance=-0.3175
        extrude(amount=-0.3175, mode=Mode.SUBTRACT)
    return part.part


def model_141598_04a7e7ae_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            Circle(0.6)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=-1.45
        extrude(amount=-1.45, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=-0.05
        extrude(amount=-0.05, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.1649336143, perimeter: 6.5973445725
            with BuildLine():
                CenterArc((0, 0), 0.55, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-1.45
        extrude(amount=-1.45, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.1649336143, perimeter: 6.5973445725
            with BuildLine():
                CenterArc((0, 0), 0.55, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.05
        extrude(amount=-0.05, mode=Mode.ADD)
    return part.part


def model_141665_0564e852_0000():
    """Model: Cajon v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1280, perimeter: 144
            with BuildLine():
                Line((32, -40), (0, -40))
                Line((32, 0), (32, -40))
                Line((0, 0), (32, 0))
                Line((0, -40), (0, 0))
            make_face()
        # OneSide extrude, distance=13
        extrude(amount=13)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 13, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 64, perimeter: 68
            with BuildLine():
                Line((0, 40), (-32, 40))
                Line((-32, 40), (-32, 38))
                Line((-32, 38), (0, 38))
                Line((0, 38), (0, 40))
            make_face()
        # OneSide extrude, distance=6
        extrude(amount=6, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 64, perimeter: 68
            with BuildLine():
                Line((32, 38), (0, 38))
                Line((32, 40), (32, 38))
                Line((0, 40), (32, 40))
                Line((0, 38), (0, 40))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 13, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1008, perimeter: 128
            with BuildLine():
                Line((-30, 38), (-30, 2))
                Line((-30, 2), (-2, 2))
                Line((-2, 2), (-2, 38))
                Line((-2, 38), (-30, 38))
            make_face()
        # OneSide extrude, distance=-12
        extrude(amount=-12, mode=Mode.SUBTRACT)
    return part.part


def model_141665_0564e852_0003():
    """Model: Table legs v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 840, perimeter: 188
            with BuildLine():
                Line((10, -84), (0, -84))
                Line((10, 0), (10, -84))
                Line((0, 0), (10, 0))
                Line((0, -84), (0, 0))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 13 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 30, perimeter: 26
            with BuildLine():
                Line((-10, 0), (0, 0))
                Line((0, 0), (0, 3))
                Line((0, 3), (-10, 3))
                Line((-10, 3), (-10, 0))
            make_face()
        # OneSide extrude, distance=67
        extrude(amount=67, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 30, perimeter: 26
            with BuildLine():
                Line((0, 84), (-10, 84))
                Line((-10, 84), (-10, 81))
                Line((-10, 81), (0, 81))
                Line((0, 81), (0, 84))
            make_face()
        # OneSide extrude, distance=67
        extrude(amount=67, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 30, perimeter: 26
            with BuildLine():
                Line((10, 70), (0, 70))
                Line((0, 70), (0, 67))
                Line((0, 67), (10, 67))
                Line((10, 67), (10, 70))
            make_face()
        # OneSide extrude, distance=78
        extrude(amount=78, mode=Mode.ADD)
    return part.part


def model_141695_7f47dedb_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 11 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4, perimeter: 8
            with BuildLine():
                Line((3, 3), (5, 3))
                Line((3, 1), (3, 3))
                Line((5, 1), (3, 1))
                Line((5, 3), (5, 1))
            make_face()
            # Profile area: 36, perimeter: 24
            with BuildLine():
                Line((-3, 3), (3, 3))
                Line((-3, -3), (-3, 3))
                Line((3, -3), (-3, -3))
                Line((3, 1), (3, -3))
                Line((3, 1), (3, 3))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(3, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 4, perimeter: 10.472135955
            with BuildLine():
                Line((1, 4), (-3, 2))
                Line((-3, 2), (1, 2))
                Line((1, 2), (1, 4))
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 8, perimeter: 12
            with BuildLine():
                Line((-3, -1), (-5, -1))
                Line((-5, -1), (-5, -3))
                Line((-5, -3), (-1, -3))
                Line((-1, -3), (-1, -1))
                Line((-1, -1), (-3, -1))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 16, perimeter: 16
            with BuildLine():
                Line((-1, 1), (3, 1))
                Line((-1, -3), (-1, 1))
                Line((3, -3), (-1, -3))
                Line((3, 1), (3, -3))
            make_face()
        # OneSide extrude, distance=4
        extrude(amount=4, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 6), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.5707963268, perimeter: 5.1415926536
            with BuildLine():
                Line((1.7071067812, -1.7071067812), (0.2928932188, -0.2928932188))
                CenterArc((1, -1), 1, -45, 180)
            make_face()
            # Profile area: 1.5707963268, perimeter: 5.1415926536
            with BuildLine():
                CenterArc((1, -1), 1, 135, 180)
                Line((1.7071067812, -1.7071067812), (0.2928932188, -0.2928932188))
            make_face()
        # OneSide extrude, distance=-6
        extrude(amount=-6, mode=Mode.SUBTRACT)
    return part.part


def model_141773_1821f078_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 22.209633, perimeter: 18.8595
            with BuildLine():
                Line((0, 4.85775), (0, 0))
                Line((0, 0), (4.572, 0))
                Line((4.572, 0), (4.572, 4.85775))
                Line((4.572, 4.85775), (0, 4.85775))
            make_face()
        # OneSide extrude, distance=11.43
        extrude(amount=11.43)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 16.62496675, perimeter: 16.3195
            with BuildLine():
                Line((-4.2545, 4.54025), (-4.2545, 0.3175))
                Line((-4.2545, 0.3175), (-0.3175, 0.3175))
                Line((-0.3175, 0.3175), (-0.3175, 4.54025))
                Line((-0.3175, 4.54025), (-4.2545, 4.54025))
            make_face()
        # OneSide extrude, distance=-11.43
        extrude(amount=-11.43, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 4.54025, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))) as sk:
            # Profile area: 0.0288782854, perimeter: 0.8484937834
            with BuildLine():
                Line((0, 0.3175), (0.1044072324, 0.4219072324))
                Line((0.1044072324, 0.4219072324), (0.1044072324, 0.5940927676))
                Line((0.1044072324, 0.5940927676), (0, 0.6985))
                Line((0, 0.3175), (0, 0.6985))
            make_face()
        # TwoSides extrude, along=4.4196, against=-0.2286
        extrude(amount=4.4196, mode=Mode.SUBTRACT)
        extrude(sk.sketch, amount=-0.2286, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(4.2545, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))) as sk:
            # Profile area: 0.030241875, perimeter: 0.92075
            with BuildLine():
                Line((10.7315, 4.85775), (11.1125, 4.85775))
                Line((11.1125, 4.937125), (11.1125, 4.85775))
                Line((10.7315, 4.937125), (11.1125, 4.937125))
                Line((10.7315, 4.85775), (10.7315, 4.937125))
            make_face()
        # TwoSides extrude, along=4.1148, against=-0.1778
        extrude(amount=4.1148, mode=Mode.ADD)
        extrude(sk.sketch, amount=-0.1778, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 11.43), x_dir=(1, 0, 0), z_dir=(0, 0, 1))) as sk:
            # Profile area: 0.0565707542, perimeter: 1.5868309661
            with BuildLine():
                Line((0.3175, 4.85775), (0, 4.85775))
                Line((0.3175, 4.937125), (0.3175, 4.85775))
                Line((-0.079040483, 4.937125), (0.3175, 4.937125))
                Line((-0.079040483, 4.54025), (-0.079040483, 4.937125))
                Line((0, 4.54025), (-0.079040483, 4.54025))
                Line((0, 4.85775), (0, 4.54025))
            make_face()
            # Profile area: 0.10080625, perimeter: 1.27
            with BuildLine():
                Line((0, 4.85775), (0, 4.54025))
                Line((0.3175, 4.54025), (0, 4.54025))
                Line((0.3175, 4.85775), (0.3175, 4.54025))
                Line((0.3175, 4.85775), (0, 4.85775))
            make_face()
        # TwoSides extrude, along=-0.3175, against=0.039624
        extrude(amount=-0.3175, mode=Mode.ADD)
        extrude(sk.sketch, amount=0.039624, mode=Mode.ADD)
    return part.part


MODELS = {
    "model_131580_430d48a6_0000": {"func": model_131580_430d48a6_0000, "volume": 42.2953461503, "area": 112.275967809},
    "model_131656_7da36cb9_0000": {"func": model_131656_7da36cb9_0000, "volume": 70.4987091106, "area": 169.0886959386},
    "model_132217_356cdf43_0000": {"func": model_132217_356cdf43_0000, "volume": 115.5155851306, "area": 417.3737254623},
    "model_132464_8dc52066_0000": {"func": model_132464_8dc52066_0000, "volume": 47.7396503836, "area": 95.1528671782},
    "model_132949_ac3b23b9_0000": {"func": model_132949_ac3b23b9_0000, "volume": 7.0573761612, "area": 25.1613541534},
    "model_133113_e6041880_0000": {"func": model_133113_e6041880_0000, "volume": 148.8135294551, "area": 577.9022395283},
    "model_133248_a739c5b6_0000": {"func": model_133248_a739c5b6_0000, "volume": 529.70688, "area": 2674.408},
    "model_134320_c6ad7b8d_0000": {"func": model_134320_c6ad7b8d_0000, "volume": 3.1419821199, "area": 32.7902791395},
    "model_134408_8183bf58_0000": {"func": model_134408_8183bf58_0000, "volume": 0.2856873695, "area": 6.7337651046},
    "model_134925_98617d78_0000": {"func": model_134925_98617d78_0000, "volume": 92.7898538498, "area": 167},
    "model_135214_40ed3b60_0000": {"func": model_135214_40ed3b60_0000, "volume": 24.5430034885, "area": 154.6563326569},
    "model_135538_9913818f_0024": {"func": model_135538_9913818f_0024, "volume": 598332.9653283623, "area": 390459.5791623861},
    "model_135700_4190876c_0000": {"func": model_135700_4190876c_0000, "volume": 10.1023686135, "area": 39.7166048073},
    "model_135779_4106c13d_0001": {"func": model_135779_4106c13d_0001, "volume": 95.7891490391, "area": 278.1392489587},
    "model_136120_439f44c2_0000": {"func": model_136120_439f44c2_0000, "volume": 0.0079749936, "area": 0.4062395543},
    "model_136355_b5fd1a59_0003": {"func": model_136355_b5fd1a59_0003, "volume": 0.3029979467, "area": 6.7799591082},
    "model_136477_c46134fc_0000": {"func": model_136477_c46134fc_0000, "volume": 9.7187595463, "area": 31.5340439777},
    "model_136593_1772a66f_0000": {"func": model_136593_1772a66f_0000, "volume": 15.171548593, "area": 128.3352732185},
    "model_136609_a3c013f6_0000": {"func": model_136609_a3c013f6_0000, "volume": 59.9255984944, "area": 157.8326721593},
    "model_136832_d2438c00_0000": {"func": model_136832_d2438c00_0000, "volume": 1030.9788173231, "area": 1368.6034236099},
    "model_136861_0ab0408d_0000": {"func": model_136861_0ab0408d_0000, "volume": 1797.2712713916, "area": 1287.358247243},
    "model_137053_59e609b3_0000": {"func": model_137053_59e609b3_0000, "volume": 7.2332840509, "area": 31.6944796122},
    "model_137053_59e609b3_0004": {"func": model_137053_59e609b3_0004, "volume": 0.510177078, "area": 6.8623968406},
    "model_137118_4ff32ab1_0003": {"func": model_137118_4ff32ab1_0003, "volume": 6.5746159502, "area": 24.5488909678},
    "model_137274_719a5ae0_0000": {"func": model_137274_719a5ae0_0000, "volume": 342.3397830594, "area": 505.9228160146},
    "model_137290_d81443d2_0000": {"func": model_137290_d81443d2_0000, "volume": 78.8808543417, "area": 485.3012176049},
    "model_137367_8c1f526a_0000": {"func": model_137367_8c1f526a_0000, "volume": 0.0057749031, "area": 0.3357804079},
    "model_137393_0ccfdbe5_0000": {"func": model_137393_0ccfdbe5_0000, "volume": 8.4328821623, "area": 122.4428035526},
    "model_137433_1c5808b2_0000": {"func": model_137433_1c5808b2_0000, "volume": 11.9652389744, "area": 122.3177468724},
    "model_137772_7e081a63_0000": {"func": model_137772_7e081a63_0000, "volume": 256.2106032882, "area": 342.4275533485},
    "model_137923_d4b1556f_0000": {"func": model_137923_d4b1556f_0000, "volume": 10.2199114858, "area": 47.3513268094},
    "model_138161_8fa1cb24_0000": {"func": model_138161_8fa1cb24_0000, "volume": 0.0065662466, "area": 0.7105604345},
    "model_138748_5721b4fa_0000": {"func": model_138748_5721b4fa_0000, "volume": 17213.2298317351, "area": 4324.3668500122},
    "model_139041_2e8aee3e_0000": {"func": model_139041_2e8aee3e_0000, "volume": 1.6095257301, "area": 20.8133739275},
    "model_139254_697caddb_0000": {"func": model_139254_697caddb_0000, "volume": 16.2347366687, "area": 67.3893578589},
    "model_139493_7f7d8123_0000": {"func": model_139493_7f7d8123_0000, "volume": 26.8729790023, "area": 118.3104870026},
    "model_139801_97e2ca6a_0000": {"func": model_139801_97e2ca6a_0000, "volume": 0.1376410281, "area": 2.0734511514},
    "model_140351_ffb3acec_0000": {"func": model_140351_ffb3acec_0000, "volume": 7.6115368273, "area": 53.6618525482},
    "model_140400_0aab1cd3_0000": {"func": model_140400_0aab1cd3_0000, "volume": 1427.0810561621, "area": 2944.9468447372},
    "model_140600_a065e504_0000": {"func": model_140600_a065e504_0000, "volume": 3.740099602, "area": 58.606074593},
    "model_140600_a065e504_0001": {"func": model_140600_a065e504_0001, "volume": 4.0695409436, "area": 66.6590842032},
    "model_140600_a065e504_0002": {"func": model_140600_a065e504_0002, "volume": 4.2342646303, "area": 70.6228310482},
    "model_140600_a065e504_0003": {"func": model_140600_a065e504_0003, "volume": 3.5753853524, "area": 54.5797277206},
    "model_140600_a065e504_0004": {"func": model_140600_a065e504_0004, "volume": 2.7175660961, "area": 34.1135011123},
    "model_140600_a065e504_0005": {"func": model_140600_a065e504_0005, "volume": 2.8657720729, "area": 37.4728140003},
    "model_140600_a065e504_0006": {"func": model_140600_a065e504_0006, "volume": 3.0814058779, "area": 42.5047622717},
    "model_140600_a065e504_0007": {"func": model_140600_a065e504_0007, "volume": 3.9048188964, "area": 62.569713738},
    "model_140600_a065e504_0008": {"func": model_140600_a065e504_0008, "volume": 3.246002755, "area": 46.4653383317},
    "model_140600_a065e504_0009": {"func": model_140600_a065e504_0009, "volume": 4.3989893251, "area": 74.6494347337},
    "model_140600_a065e504_0015": {"func": model_140600_a065e504_0015, "volume": 4.5637147085, "area": 78.676055153},
    "model_140628_4b9e7242_0000": {"func": model_140628_4b9e7242_0000, "volume": 176.8475559816, "area": 222.3943396258},
    "model_140735_cbd9cc5f_0000": {"func": model_140735_cbd9cc5f_0000, "volume": 128.8097362841, "area": 580.0574988618},
    "model_141399_f6311635_0000": {"func": model_141399_f6311635_0000, "volume": 131.614365803, "area": 1369.9559342},
    "model_141598_04a7e7ae_0000": {"func": model_141598_04a7e7ae_0000, "volume": 0.3015928947, "area": 12.3621670919},
    "model_141665_0564e852_0000": {"func": model_141665_0564e852_0000, "volume": 5056, "area": 6512},
    "model_141665_0564e852_0003": {"func": model_141665_0564e852_0003, "volume": 8880, "area": 7696},
    "model_141695_7f47dedb_0000": {"func": model_141695_7f47dedb_0000, "volume": 149.1504440785, "area": 246.3601984459},
    "model_141773_1821f078_0000": {"func": model_141773_1821f078_0000, "volume": 63.8525165849, "area": 414.7154196549},
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
