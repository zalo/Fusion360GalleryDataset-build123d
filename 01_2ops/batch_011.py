"""Batch 011 - passing/01_2ops
203 models bundled from Fusion360 Gallery reconstructions.
"""

from build123d import *
from build123d import Edge, BuildLine
from collections import Counter
from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
from OCP.Geom import Geom_BSplineCurve
from OCP.TColStd import TColStd_Array1OfReal, TColStd_Array1OfInteger
from OCP.TColgp import TColgp_Array1OfPnt
from OCP.gp import gp_Pnt


def model_37599_faf701a1_0009():
    """Model: bolec"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # TwoSides extrude, along=2.2, against=-19.9
        extrude(amount=2.2)
        extrude(sk.sketch, amount=-19.9)
    return part.part


def model_37605_e35cc4df_0001():
    """Model: bolec 2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with Locations((-65, 10)):
                Circle(0.75)
        # OneSide extrude, distance=1.4
        extrude(amount=1.4)
    return part.part


def model_37605_e35cc4df_0007():
    """Model: os"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.5026548396, perimeter: 2.5132741603
            with Locations((6.0000000894, 1.5000000224)):
                Circle(0.400000006)
        # OneSide extrude, distance=8
        extrude(amount=8)
    return part.part


def model_37605_e35cc4df_0009():
    """Model: ramie 1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 9 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 23.4056591941, perimeter: 39.5133524201
            with BuildLine():
                Line((-65.0628543056, 19.6012305136), (-53.3334248778, 17.6735177969))
                CenterArc((-65.2250271027, 18.614468139), 1, 80.6669643097, 177.3674018783)
                Line((-65.4323520601, 17.6361960081), (-65.3418598036, 17.6213165292))
                Line((-65.3418598036, 17.6213165292), (-53.6421165833, 15.6975488035))
                CenterArc((-53.4798670946, 16.6842985709), 1, -99.3374887779, 179.0922210928)
                Line((-53.3334248778, 17.6735177969), (-53.302004826, 17.6683539624))
            make_face()
            with BuildLine():
                CenterArc((-65.2250271027, 18.614468139), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-53.4798670946, 16.6842985709), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_37605_e35cc4df_0010():
    """Model: bolec1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with Locations((-59, 12.5)):
                Circle(0.75)
        # OneSide extrude, distance=1.6
        extrude(amount=1.6)
    return part.part


def model_37605_e35cc4df_0011():
    """Model: spych lacznik"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.4993455679, perimeter: 10.7690260854
            with BuildLine():
                Line((-54.102741265, 6.7499893665), (-54.0972634729, 6.7499893909))
                CenterArc((-54.1000008062, 6.4000000954), 0.35, 90.4486238019, 179.5513761981)
                Line((-51.7000007704, 6.0500000954), (-54.1000008062, 6.0500000954))
                CenterArc((-51.7000007704, 6.4000000954), 0.35, -90, 180.0002558402)
                Line((-54.0972634729, 6.7499893909), (-51.7000023332, 6.7500000954))
            make_face()
            with BuildLine():
                CenterArc((-54.1000008062, 6.4000000954), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-51.7000007704, 6.4000000954), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


def model_37605_e35cc4df_0013():
    """Model: RAMIE22"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 24.0806977302, perimeter: 41.1471793942
            with BuildLine():
                Line((-53, 31), (-61, 33))
                Line((-61, 33), (-65.4278775383, 30.9038367177))
                CenterArc((-65, 30), 1, 115.332938613, 182.7395483228)
                Line((-61, 31), (-64.5294117647, 29.1176470588))
                Line((-53.4705882353, 29.1176470588), (-61, 31))
                Line((-53, 29), (-53.4705882353, 29.1176470588))
                CenterArc((-53, 30), 1, -90, 180)
            make_face()
            with BuildLine():
                CenterArc((-53, 30), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-65, 30), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_37615_8399c412_0004():
    """Model: Component3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=3.2
        extrude(amount=3.2)
    return part.part


def model_37619_ae810a8d_0001():
    """Model: Component2"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 11 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.496412683, perimeter: 17.2260569103
            with BuildLine():
                Line((1.2002589138, -1.9), (1.2002589138, -1.7))
                CenterArc((-4.7997410862, -1.7), 6, 0, 36.8698976458)
                CenterArc((4.8002589138, -1.7), 6, 143.1301023542, 36.8698976458)
                Line((-1.1997410862, -1.7), (-1.1997410862, -1.9))
                Line((-1.1997410862, -1.9), (-0.4969686627, -1.9))
                Line((-0.4969686627, -1.6), (-0.4969686627, -1.9))
                Line((-0.8988638257, -1.6), (-0.4969686627, -1.6))
                CenterArc((4.8002589138, -1.7), 5.7, 147.3631024964, 31.6316568181)
                CenterArc((-4.7997410862, -1.7), 5.7, 1.0052406854, 31.6316568181)
                Line((0.4969686627, -1.6), (0.8993816533, -1.6))
                Line((0.4969686627, -1.6), (0.4969686627, -1.9))
                Line((0.4969686627, -1.9), (1.2002589138, -1.9))
            make_face()
        # OneSide extrude, distance=150
        extrude(amount=150)
    return part.part


def model_37619_ae810a8d_0003():
    """Model: Wtyczka"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 17 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 10.7463495408, perimeter: 12.7707963268
            with BuildLine():
                CenterArc((11.7500001937, -31.2500004619), 0.25, 90, 90)
                Line((11.5000001937, -34.3500004619), (11.5000001937, -31.2500004619))
                CenterArc((11.7500001937, -34.3500004619), 0.25, 180, 90)
                Line((14.2500001937, -34.6000004619), (11.7500001937, -34.6000004619))
                CenterArc((14.2500001937, -34.3500004619), 0.25, -90, 90)
                Line((14.5000001937, -31.2500004619), (14.5000001937, -34.3500004619))
                CenterArc((14.2500001937, -31.2500004619), 0.25, 0, 90)
                Line((11.7500001937, -31.0000004619), (14.2500001937, -31.0000004619))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


def model_37619_ae810a8d_0004():
    """Model: Component1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 955.7467102453, perimeter: 120.4777561812
            with BuildLine():
                CenterArc((0.0002589138, 0), 17.5, 0, 360)
            make_face()
            with BuildLine():
                Line((-1.1997410862, -1.9), (1.2002589138, -1.9))
                Line((-1.1997410862, -1.7), (-1.1997410862, -1.9))
                CenterArc((4.8002589138, -1.7), 6, 143.1301023542, 36.8698976458)
                CenterArc((-4.7997410862, -1.7), 6, 0, 36.8698976458)
                Line((1.2002589138, -1.9), (1.2002589138, -1.7))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


def model_37683_e2cca100_0008():
    """Model: lid5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 41.61551, perimeter: 27.1518
            with BuildLine():
                Line((-2.33795, 4.45), (-2.33795, -4.45))
                Line((-2.33795, -4.45), (2.33795, -4.45))
                Line((2.33795, -4.45), (2.33795, 4.45))
                Line((2.33795, 4.45), (-2.33795, 4.45))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


def model_37846_cde34fcd_0027():
    """Model: NAKRETKA v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6368848312, perimeter: 7.0274333882
            with BuildLine():
                Line((0.6062177826, 1.05), (0.6062177826, 0.35))
                Line((0, 1.4), (0.6062177826, 1.05))
                Line((-0.6062177826, 1.05), (0, 1.4))
                Line((-0.6062177826, 0.35), (-0.6062177826, 1.05))
                Line((0, 0), (-0.6062177826, 0.35))
                Line((0.6062177826, 0.35), (0, 0))
            make_face()
            with BuildLine():
                CenterArc((0, 0.7000000104), 0.45, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)
    return part.part


def model_37846_cde34fcd_0029():
    """Model: M4x4 v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)
    return part.part


def model_37846_cde34fcd_0045():
    """Model: trzymadelko v1 (1)"""
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
        # Sketch has 6 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0082397423, perimeter: 0.4295074911
            with BuildLine():
                _nurbs_edge([(0, 0), (-0.0030654564, 0.0002522605), (-0.0089989332, 0.0008568076), (-0.0173068611, 0.0020636967), (-0.0271798609, 0.0042829803), (-0.0373774812, 0.0081431036), (-0.0452385314, 0.0131869944), (-0.0505701801, 0.0195123464), (-0.0532632627, 0.0271744649), (-0.0534172989, 0.0361229309), (-0.0512218564, 0.0462617043), (-0.0477390969, 0.0552473652), (-0.0442174926, 0.062447405), (-0.0414721075, 0.0674488909), (-0.04, 0.07)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                Line((-0.081, 0.099), (-0.04, 0.07))
                _nurbs_edge([(-0.081, 0.099), (-0.0838733892, 0.0940814896), (-0.0892254279, 0.0844147648), (-0.0960692915, 0.0704255557), (-0.1027868805, 0.0528119327), (-0.1069009729, 0.0326426037), (-0.106357416, 0.0144826493), (-0.100788557, -0.00150932), (-0.0900166637, -0.0152566282), (-0.0742743461, -0.0268596263), (-0.0539478549, -0.0364849484), (-0.034325813, -0.0427352892), (-0.0178397922, -0.0466596624), (-0.0060755324, -0.0489421785), (0, -0.05)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                Line((0, 0), (0, -0.05))
            make_face()
        # OneSide extrude, distance=3.4
        extrude(amount=3.4)
    return part.part


def model_37846_cde34fcd_0058():
    """Model: waleczek v2 (5) (1) (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            Circle(0.1)
        # OneSide extrude, distance=0.48
        extrude(amount=0.48)
    return part.part


def model_37995_1cc61263_0001():
    """Model: PullupBar"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4.1043305807, perimeter: 7.1816808061
            Circle(1.143)
        # OneSide extrude, distance=50.8
        extrude(amount=50.8)
    return part.part


def model_37995_1cc61263_0005():
    """Model: Leg (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 180.6448, perimeter: 81.28
            with BuildLine():
                Line((-5.08, 35.56), (0, 35.56))
                Line((-5.08, 0), (-5.08, 35.56))
                Line((0, 0), (-5.08, 0))
                Line((0, 35.56), (0, 0))
            make_face()
        # OneSide extrude, distance=5.08
        extrude(amount=5.08)
    return part.part


def model_37995_1cc61263_0006():
    """Model: Bottomleg1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 361.2896, perimeter: 152.4
            with BuildLine():
                Line((12.6999998093, 5.0799998474), (12.6999998093, 10.1599998474))
                Line((12.6999998093, 10.1599998474), (-58.4200001907, 10.1599998474))
                Line((-58.4200001907, 10.1599998474), (-58.4200001907, 5.0799998474))
                Line((-58.4200001907, 5.0799998474), (12.6999998093, 5.0799998474))
            make_face()
        # OneSide extrude, distance=5.08
        extrude(amount=5.08)
    return part.part


def model_37995_1cc61263_0009():
    """Model: WeightHolderOuter"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 9.0713002421, perimeter: 10.6767654651
            with Locations((-12.6999998093, 10.1599998474)):
                Circle(1.69926)
        # OneSide extrude, distance=12.7
        extrude(amount=12.7)
    return part.part


def model_37995_1cc61263_0010():
    """Model: WeightHolderInner"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 9.0713002421, perimeter: 10.6767654651
            with Locations((0, 6.3499999046)):
                Circle(1.69926)
        # OneSide extrude, distance=7.62
        extrude(amount=7.62)
    return part.part


def model_37995_1cc61263_0012():
    """Model: MiniRectConnector"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 29.0322, perimeter: 22.86
            with BuildLine():
                Line((34.2900012159, -3.8099998784), (38.1000012159, -3.8099998784))
                Line((38.1000012159, -3.8099998784), (38.1000012159, 3.8100001216))
                Line((34.2900012159, 3.8100001216), (38.1000012159, 3.8100001216))
                Line((34.2900012159, 3.8100001216), (34.2900012159, -3.8099998784))
            make_face()
        # OneSide extrude, distance=-2.54
        extrude(amount=-2.54)
    return part.part


def model_38114_917ea77b_0001():
    """Model: Gummi"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 9 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.6091953217, perimeter: 17.3210405556
            with BuildLine():
                CenterArc((0, 0), 1.49, 95.6819590705, 348.6360818589)
                Line((0.1475195778, 1.2916028701), (0.1475195778, 1.4826793228))
                CenterArc((0, 0), 1.3, 96.5157653696, 346.9684692608)
                Line((-0.1475195778, 1.4826793228), (-0.1475195778, 1.2916028701))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)
    return part.part


def model_38114_917ea77b_0006():
    """Model: Runder Gummi"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.3876104167, perimeter: 23.8761041673
            with BuildLine():
                CenterArc((-11.3639340532, 8.5263506094), 2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-11.3639340532, 8.5263506094), 1.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3
        extrude(amount=3)
    return part.part


def model_38114_917ea77b_0007():
    """Model: Becher"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.0685834706, perimeter: 28.2743338823
            with BuildLine():
                CenterArc((-1.0177878474, -53.9454337329), 2.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-1.0177878474, -53.9454337329), 2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=6
        extrude(amount=6)
    return part.part


def model_38198_7c60c095_0000():
    """Model: Bolt_a_1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0452389342, perimeter: 0.7539822369
            Circle(0.12)
        # Symmetric extrude, each_side=0.59
        extrude(amount=0.59, both=True)
    return part.part


def model_38198_7c60c095_0002():
    """Model: Lense_R"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 46 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 23.9977897009, perimeter: 18.1279136629
            with BuildLine():
                CenterArc((-7.7814634254, 3.4968895771), 14.1060371369, -10.6494943432, 12.0465088139)
                CenterArc((5.7205591976, 3.8261679288), 0.6, 1.3970144707, 74.8975231481)
                CenterArc((3.4399373847, -5.5254440152), 10.2256886406, 76.2945376188, 28.2035592481)
                CenterArc((0.9800973982, 3.9873549684), 0.4, 104.4980968669, 72.4983079674)
                CenterArc((9.4501257197, 3.5429266592), 8.8816800393, 176.9964048343, 12.4502209847)
                CenterArc((2.0699053081, 2.3149678298), 1.4, -170.553374181, 7.8818234509)
                CenterArc((6.1190518717, 3.578342465), 5.6416628063, -162.6715507301, 17.0564211144)
                CenterArc((1.9583558355, 0.7310679178), 0.6, -145.6151296157, 43.0692633825)
                CenterArc((3.3485422779, 6.9781233733), 6.999868765, -102.5458662332, 31.4890311944)
                CenterArc((5.393669174, 1.0194488198), 0.7, -71.0568350389, 60.4073406956)
            make_face()
            # Profile area: 23.9977897009, perimeter: 18.1279136629
            with BuildLine():
                CenterArc((-3.4391756757, -5.5254440152), 10.2256886406, 75.5019031331, 28.2035592481)
                CenterArc((-5.7197974886, 3.8261679288), 0.6, 103.7054623812, 74.8975231481)
                CenterArc((7.7822251344, 3.4968895771), 14.1060371369, 178.6029855293, 12.0465088139)
                CenterArc((-5.392907465, 1.0194488198), 0.7, -169.3505056568, 60.4073406956)
                CenterArc((-3.3477805689, 6.9781233733), 6.999868765, -108.9431649611, 31.4890311944)
                CenterArc((-1.9575941265, 0.7310679178), 0.6, -77.4541337668, 43.0692633825)
                CenterArc((-6.1182901627, 3.578342465), 5.6416628063, -34.3848703843, 17.0564211144)
                CenterArc((-2.0691435991, 2.3149678298), 1.4, -17.3284492699, 7.8818234509)
                CenterArc((-9.4493640107, 3.5429266592), 8.8816800393, -9.446625819, 12.4502209847)
                CenterArc((-0.9793356892, 3.9873549684), 0.4, 3.0035951657, 72.4983079674)
            make_face()
        # Symmetric extrude, each_side=0.17
        extrude(amount=0.17, both=True)
    return part.part


def model_38198_7c60c095_0004():
    """Model: Lense_L"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 23.9977897009, perimeter: 18.1279136629
            with BuildLine():
                CenterArc((5.7205591976, 3.8261679288), 0.6, 1.3970144707, 74.8975231481)
                CenterArc((3.4399373847, -5.5254440152), 10.2256886406, 76.2945376188, 28.2035592481)
                CenterArc((0.9800973982, 3.9873549684), 0.4, 104.4980968669, 72.4983079674)
                CenterArc((9.4501257197, 3.5429266592), 8.8816800393, 176.9964048343, 12.4502209847)
                CenterArc((2.0699053081, 2.3149678298), 1.4, -170.553374181, 7.8818234509)
                CenterArc((6.1190518717, 3.578342465), 5.6416628063, -162.6715507301, 17.0564211144)
                CenterArc((1.9583558355, 0.7310679178), 0.6, -145.6151296157, 43.0692633825)
                CenterArc((3.3485422779, 6.9781233733), 6.999868765, -102.5458662332, 31.4890311944)
                CenterArc((5.393669174, 1.0194488198), 0.7, -71.0568350389, 60.4073406956)
                CenterArc((-7.7814634254, 3.4968895771), 14.1060371369, -10.6494943432, 12.0465088139)
            make_face()
        # Symmetric extrude, each_side=0.17
        extrude(amount=0.17, both=True)
    return part.part


def model_38198_7c60c095_0006():
    """Model: Frame"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 31 constraints, 23 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4.9268728124, perimeter: 38.7329665195
            with BuildLine():
                CenterArc((10.1097344336, 3.2), 16.6193535791, 180, 9.0958433645)
                CenterArc((-6.0044078117, 0.6201316046), 0.3, -170.9041566355, 7.4435654187)
                CenterArc((-5.7761619362, 0.6879119131), 0.5380973538, -163.4605912168, 60.4061205665)
                CenterArc((-3.3455436105, 8.7774650441), 8.9838807932, -106.5040062018, 25.8953565573)
                CenterArc((-2.0427577128, 0.9005937474), 1, -80.6086496445, 44.1543952747)
                CenterArc((-4.7723761241, 2.9170344605), 4.3936484528, -36.4542543698, 30.7493357857)
                CenterArc((-0.0004898974, 2.4800015104), 0.3999994374, 89.8752737027, 90.0843933007)
                Line((0.0003808545, 4.65), (0.0003808545, 2.88))
                Line((0.0003808545, 4.65), (-0.214751358, 4.6376222873))
                CenterArc((-0.3870725028, 7.6326691021), 3, -98.6432675463, 11.936171448)
                CenterArc((-3.3970910258, -12.1690027122), 17.0291392264, 81.3567324537, 17.7453742291)
                CenterArc((-6.0119078407, 4.1520014416), 0.5, 99.1021066828, 75.3646933246)
                CenterArc((-5.9123737913, 4.1423591899), 0.6, 174.4668000074, 0.0204061438)
                Line((-6.5096191455, 4.1), (-6.5095986544, 4.2))
                Line((-6.5096191455, 3.2), (-6.5096191455, 4.1))
            make_face()
            with BuildLine():
                CenterArc((-9.4493640107, 3.5429266592), 8.8816800393, -9.446625819, 12.4502209847)
                CenterArc((-2.0691435991, 2.3149678298), 1.4, -17.3284492699, 7.8818234509)
                CenterArc((-6.1182901627, 3.578342465), 5.6416628063, -34.3848703843, 17.0564211144)
                CenterArc((-1.9575941265, 0.7310679178), 0.6, -77.4541337668, 43.0692633825)
                CenterArc((-3.3477805689, 6.9781233733), 6.999868765, -108.9431649611, 31.4890311944)
                CenterArc((-5.392907465, 1.0194488198), 0.7, -169.3505056568, 60.4073406956)
                CenterArc((7.7822251344, 3.4968895771), 14.1060371369, 178.6029855293, 12.0465088139)
                CenterArc((-5.7197974886, 3.8261679288), 0.6, 103.7054623812, 74.8975231481)
                CenterArc((-3.4391756757, -5.5254440152), 10.2256886406, 75.5019031331, 28.2035592481)
                CenterArc((-0.9793356892, 3.9873549684), 0.4, 3.0035951657, 72.4983079674)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.2
        extrude(amount=0.2, both=True)
    return part.part


def model_38260_2a31c6df_0011():
    """Model: Component2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 13 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1486757711, perimeter: 2.6948225489
            with BuildLine():
                Line((0, 0.7), (0, 0.7442))
                Line((0, 0.7), (0.05525, 0.7))
                CenterArc((0.0625, 0.7), 0.00725, 0, 360)
                Line((0, 0.1), (0, 0.7))
                Line((0, 0.1), (0.07505, 0.1))
                CenterArc((0.1188, 0.1), 0.04375, 0, 360)
                Line((0, 0), (0, 0.1))
                Line((0, 0), (0.225, 0))
                Line((0.225, 0), (0.225, 0.1875))
                Line((0.0938, 0.925), (0.225, 0.1875))
                Line((0, 0.925), (0.0938, 0.925))
                Line((0, 0.8558), (0, 0.925))
                CenterArc((0, 0.8), 0.0558, -90, 180)
            make_face()
            # Profile area: 0.1486757711, perimeter: 2.5645225489
            with BuildLine():
                CenterArc((0, 0.8), 0.0558, 90, 180)
                Line((0, 0.8558), (0, 0.925))
                Line((0, 0.925), (-0.0938, 0.925))
                Line((-0.0938, 0.925), (-0.225, 0.1875))
                Line((-0.225, 0), (-0.225, 0.1875))
                Line((0, 0), (-0.225, 0))
                Line((0, 0), (0, 0.1))
                Line((0, 0.1), (0, 0.7))
                Line((0, 0.7), (0, 0.7442))
            make_face()
            with BuildLine():
                CenterArc((-0.1188, 0.1), 0.04375, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-0.0625, 0.7), 0.00725, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.075
        extrude(amount=0.075)
    return part.part


def model_38260_2a31c6df_0012():
    """Model: Component19"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0072795652, perimeter: 0.4188008791
            with BuildLine():
                Line((0, -0.04375), (-0.0875, -0.04375))
                Line((0, 0.04375), (0, -0.04375))
                Line((-0.0875, 0.04375), (0, 0.04375))
                Line((-0.0875, -0.04375), (-0.0875, 0.04375))
            make_face()
            with BuildLine():
                CenterArc((-0.0624808613, -0.0125403429), 0.01095, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0072795652, perimeter: 0.4188008791
            with BuildLine():
                Line((0.0875, -0.04375), (0, -0.04375))
                Line((0.0875, 0.04375), (0.0875, -0.04375))
                Line((0, 0.04375), (0.0875, 0.04375))
                Line((0, 0.04375), (0, -0.04375))
            make_face()
            with BuildLine():
                CenterArc((0.0624808613, -0.0125403429), 0.01095, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.0125
        extrude(amount=0.0125)
    return part.part


def model_38260_2a31c6df_0014():
    """Model: Component26"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 18 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0015349378, perimeter: 0.4139335242
            with BuildLine():
                Line((0, 0), (0.0154123656, -0.0070092073))
                Line((0, 0), (-0.12, 0))
                Line((-0.12, 0), (-0.1595944084, -0.0151671626))
                Line((-0.1595944084, -0.0151671626), (-0.1569830809, -0.0219841245))
                Line((-0.119954928, -0.0078), (-0.1569830809, -0.0219841245))
                Line((-0.0016903391, -0.0078), (-0.119954928, -0.0078))
                Line((-0.0016903391, -0.0078), (0.0121833333, -0.0141094433))
                CenterArc((0.0186, 0), 0.0155, -114.455003884, 114.455003884)
                Line((0.0263, 0), (0.0341, 0))
                CenterArc((0.0186, 0), 0.0077, -114.455003884, 114.455003884)
            make_face()
            # Profile area: 0.0014799983, perimeter: 0.3988818047
            with BuildLine():
                Line((0, 0), (0.0154123656, 0.0070092073))
                CenterArc((0.0186, 0), 0.0077, 0, 114.455003884)
                Line((0.0263, 0), (0.0341, 0))
                CenterArc((0.0186, 0), 0.0155, 0, 114.455003884)
                Line((-0.0016903391, 0.0078), (0.0121833333, 0.0141094433))
                Line((-0.0016903391, 0.0078), (-0.119954928, 0.0078))
                Line((-0.119954928, 0.0078), (-0.1499308834, 0.0192826868))
                Line((-0.1499308834, 0.0192826868), (-0.1525906805, 0.0124842919))
                Line((-0.12, 0), (-0.1525906805, 0.0124842919))
                Line((0, 0), (-0.12, 0))
            make_face()
        # OneSide extrude, distance=0.0156
        extrude(amount=0.0156)
    return part.part


def model_38260_2a31c6df_0018():
    """Model: Component30"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0047771267, perimeter: 0.5458049716
            with BuildLine():
                CenterArc((0, 0), 0.0516, 15, 345)
                Line((0.0328, 0), (0.0516, 0))
                CenterArc((0, 0), 0.0328, 15, 345)
                Line((0.0316823671, 0.0084892647), (0.0498417726, 0.0133550627))
            make_face()
        # OneSide extrude, distance=0.0094
        extrude(amount=0.0094)
    return part.part


def model_38260_2a31c6df_0022():
    """Model: Component32"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0086606798, perimeter: 1.1415435635
            with BuildLine():
                CenterArc((0, 0), 0.1, 15, 345)
                Line((0.0844, 0), (0.1, 0))
                CenterArc((0, 0), 0.0844, 15, 345)
                Line((0.0815241397, 0.0218443274), (0.0965925826, 0.0258819045))
            make_face()
        # OneSide extrude, distance=0.0156
        extrude(amount=0.0156)
    return part.part


def model_38260_2a31c6df_0024():
    """Model: Component23"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0171425401, perimeter: 0.8444601053
            with BuildLine():
                CenterArc((0, 0), 0.0875, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.0469, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.0177
        extrude(amount=0.0177)
    return part.part


def model_38276_c9ef069a_0002():
    """Model: Piece 4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 12 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 5.7621183289, perimeter: 18.9771796556
            with BuildLine():
                CenterArc((7.0000001043, 4.0000000596), 0.9, -173.6206297916, 180)
                Line((7.8944272953, 4.1000000596), (10.5776150467, 4.602563921))
                CenterArc((10.5500001043, 4.7500000596), 0.15, -79.391357429, 169.391357429)
                Line((10.5500001043, 4.9000000596), (4.1000001043, 4.9000000596))
                Line((3.3666410794, 4.0808592331), (4.1000001043, 4.9000000596))
                Line((3.3666410794, 4.0808592331), (5.3631207352, 4.1994719803))
                CenterArc((5.3809131135, 3.9000000596), 0.3, 0, 93.4000892017)
                Line((6.1055729133, 3.9000000596), (5.6809131135, 3.9000000596))
            make_face()
            with BuildLine():
                CenterArc((7.0000001043, 4.0000000596), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.55
        extrude(amount=0.55)
    return part.part


def model_38276_c9ef069a_0003():
    """Model: Piece 5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.4431691252, perimeter: 7.6969020013
            with BuildLine():
                CenterArc((6.0000000894, 3.5000000522), 0.8, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((6.0000000894, 3.5000000522), 0.425, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


def model_38276_c9ef069a_0006():
    """Model: Piece 3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 43 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 20.1951507016, perimeter: 34.1629446555
            with BuildLine():
                Line((10.0983379712, 1.4995465273), (9.9983682027, 1.6727690587))
                Line((8.4932445884, 2.0189019757), (9.9983682027, 1.6727690587))
                Line((9.000453427, 2.5978143724), (8.4932445884, 2.0189019757))
                Line((8.8272658022, 2.6978446009), (9.000453427, 2.5978143724))
                Line((7.3507240579, 2.2450426929), (8.8272658022, 2.6978446009))
                Line((7.3507240579, 2.2450426929), (7.5005235988, 2.9999999543))
                Line((7.3005236018, 3.0000348609), (7.5005235988, 2.9999999543))
                Line((7.3005236018, 3.0000348609), (6.2482018955, 1.8696260336))
                Line((6.2482018955, 1.8696260336), (6.0004534727, 2.5983379712))
                Line((6.0004534727, 2.5983379712), (5.8272309413, 2.4983682027))
                Line((5.8272309413, 2.4983682027), (5.4810980243, 0.9932445884))
                Line((5.4810980243, 0.9932445884), (4.9021856276, 1.500453427))
                Line((4.9021856276, 1.500453427), (4.8021553991, 1.3272658022))
                Line((4.8021553991, 1.3272658022), (5.2549573071, -0.1492759421))
                Line((5.2549573071, -0.1492759421), (4.5000000457, 0.0005235988))
                Line((4.5000000457, 0.0005235988), (4.4999651391, -0.1994763982))
                Line((5.6303739664, -1.2517981045), (4.4999651391, -0.1994763982))
                Line((5.6303739664, -1.2517981045), (4.9016620288, -1.4995465273))
                Line((4.9016620288, -1.4995465273), (5.0126865239, -1.6653674257))
                Line((5.0126865239, -1.6653674257), (6.5067554116, -2.0189019757))
                Line((6.5067554116, -2.0189019757), (5.999546573, -2.5978143724))
                Line((5.999546573, -2.5978143724), (6.1727341978, -2.6978446009))
                Line((6.1727341978, -2.6978446009), (7.6492759421, -2.2450426929))
                Line((7.6492759421, -2.2450426929), (7.4994764012, -2.9999999543))
                Line((7.4994764012, -2.9999999543), (7.6994763982, -3.0000348609))
                Line((7.6994763982, -3.0000348609), (8.7517981045, -1.8696260336))
                Line((8.7517981045, -1.8696260336), (8.9995465273, -2.5983379712))
                Line((8.9995465273, -2.5983379712), (9.1727690587, -2.4983682027))
                Line((9.1727690587, -2.4983682027), (9.5189019757, -0.9932445884))
                Line((9.5189019757, -0.9932445884), (10.0978143724, -1.500453427))
                Line((10.0978143724, -1.500453427), (10.2016722131, -1.3295337121))
                Line((9.7450426929, 0.1492759421), (10.2016722131, -1.3295337121))
                Line((10.4999999543, -0.0005235988), (9.7450426929, 0.1492759421))
                Line((10.5, 0.2), (10.4999999543, -0.0005235988))
                Line((9.3696260336, 1.2517981045), (10.5, 0.2))
                Line((10.0983379712, 1.4995465273), (9.3696260336, 1.2517981045))
            make_face()
            with BuildLine():
                Line((7, -0.5), (8, -0.5))
                Line((7, 0.5), (7, -0.5))
                Line((8, 0.5), (7, 0.5))
                Line((8, -0.5), (8, 0.5))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.75
        extrude(amount=0.75)
    return part.part


def model_38276_c9ef069a_0010():
    """Model: Piece 15"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.67512164, perimeter: 10.076953585
            with BuildLine():
                Line((0.5773503311, 7.2000001073), (-0.5773503311, 7.2000001073))
                Line((-0.5773503311, 7.2000001073), (-1.1547006623, 6.2))
                Line((-1.1547006623, 6.2), (-0.5773503311, 5.1999998927))
                Line((-0.5773503311, 5.1999998927), (0.5773503311, 5.1999998927))
                Line((0.5773503311, 5.1999998927), (1.1547006623, 6.2))
                Line((1.1547006623, 6.2), (0.5773503311, 7.2000001073))
            make_face()
            with BuildLine():
                CenterArc((0, 6.2), 0.5011390652, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


def model_38287_88ec74de_0007():
    """Model: Tlok v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # OneSide extrude, distance=8
        extrude(amount=8)
    return part.part


def model_38287_88ec74de_0011():
    """Model: Wysięgnik v2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 16 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 226.2004255215, perimeter: 136.4123767481
            with BuildLine():
                CenterArc((23, 10), 2.25, 12.7146515497, 77.2880708233)
                Line((18.9998931017, 12.24980994), (22.9998930927, 12.2499999975))
                CenterArc((19.000000009, 9.9998099425), 2.25, 90.002722373, 70.1684345079)
                Line((14.8568651112, 5.1429909983), (16.8834022242, 10.7630358707))
                CenterArc((11.094024605, 6.4998370929), 4, -89.9993287838, 70.1704856648)
                Line((-4.9581113853, 2.4996490429), (11.0940714647, 2.4998370932))
                CenterArc((-5.0000000745, 0), 2.5, 89.0399370343, 180.9600629657)
                Line((-5.0000000745, -2.5), (25, -2.5))
                CenterArc((25, 0), 2.5, -90, 102.7146515497)
                Line((25.1948261603, 10.4952152321), (27.4386957337, 0.5502391467))
            make_face()
            with BuildLine():
                CenterArc((19.000000009, 9.9998099425), 1.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((23, 10), 1.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((25, 0), 2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-5.0000000745, 0), 2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_38287_88ec74de_0012():
    """Model: Oś v6"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.6211275016, perimeter: 10.9955742876
            Circle(1.75)
        # OneSide extrude, distance=13
        extrude(amount=13)
    return part.part


def model_38287_88ec74de_0014():
    """Model: Oś 35 150 v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.6211275016, perimeter: 10.9955742876
            Circle(1.75)
        # OneSide extrude, distance=15
        extrude(amount=15)
    return part.part


def model_38287_88ec74de_0017():
    """Model: 2ramie v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 27 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 282.9155194849, perimeter: 171.9600342874
            with BuildLine():
                CenterArc((4.8264574798, 17.8023659281), 2.25, 52.2020998757, 111.8522916108)
                Line((2.6630308913, 18.4204964939), (-2.4038073563, 0.68681175))
                CenterArc((0, 0), 2.5000000373, 164.0543914865, 105.9456085991)
                Line((0.0000000037, -2.5000000373), (24.9170036601, -2.5))
                CenterArc((24.9170036564, 0), 2.5, -89.9999999143, 143.8104794297)
                Line((16.5892060933, 11.4633371451), (26.393148814, 2.0176708041))
                Line((16.2534981041, 11.786776984), (16.5892060933, 11.4633371451))
                Line((6.2054331919, 19.5802652462), (16.2534981041, 11.786776984))
            make_face()
            with BuildLine():
                Line((7.3632530008, 13.0549435748), (13.4681173064, 8.4255845682))
                CenterArc((12.2596620508, 6.8319610571), 2, 43.4098506829, 9.416866301)
                Line((17.5146276742, 4.1872124305), (13.7125751137, 8.2063858937))
                CenterArc((16.7881711427, 3.5000000122), 1, -90.0000000857, 133.4098507686)
                Line((16.7881711412, 2.5000000122), (4.5115558494, 2.5000000305))
                CenterArc((4.5115558509, 3.5000000305), 1, 165.607589283, 104.3924106313)
                Line((5.7904092794, 12.5066934077), (3.5429397573, 3.7485616189))
                CenterArc((6.759025373, 12.2581318192), 1, 52.8267169839, 112.7808722992)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((14.9170036564, 10.0636483266), 1.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.8264574798, 17.8023659281), 1.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((24.9170036564, 0), 1.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0), 2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_38287_88ec74de_0023():
    """Model: oś 110 v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.6211275016, perimeter: 10.9955742876
            Circle(1.75)
        # OneSide extrude, distance=11
        extrude(amount=11)
    return part.part


def model_38287_88ec74de_0029():
    """Model: Noweramie v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 13 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 86.884070764, perimeter: 76.0067328081
            with BuildLine():
                Line((-5, -2.5), (4, -2.5))
                Line((4, -2.5), (2.2471910112, 1.095505618))
                CenterArc((0, 0), 2.5, 25.9892335838, 27.6691124918)
                Line((1.4814973266, 2.0137441921), (-11.1560202246, 13.4811206444))
                CenterArc((-12.5, 12), 2, 47.7791683184, 177.3613578978)
                Line((-13.9107407482, 10.5823221306), (-6.219476889, 2.7597922366))
                CenterArc((-9.25, -0.2198771534), 4.25, 0, 44.5152178485)
                Line((-5, -2.5), (-5, -0.2198771534))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-12.5, 12), 1.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_38287_88ec74de_0034():
    """Model: sruba v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5542562584, perimeter: 2.7712812921
            with BuildLine():
                Line((0.4, -0.2309401077), (0.4, 0.2309401077))
                Line((0.4, 0.2309401077), (0, 0.4618802154))
                Line((0, 0.4618802154), (-0.4, 0.2309401077))
                Line((-0.4, 0.2309401077), (-0.4, -0.2309401077))
                Line((-0.4, -0.2309401077), (0, -0.4618802154))
                Line((0, -0.4618802154), (0.4, -0.2309401077))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


def model_38287_88ec74de_0035():
    """Model: ząb v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.8600201314, perimeter: 13.0705248412
            with BuildLine():
                Line((-2.8786796388, -0.1213203594), (-3, 0))
                CenterArc((-0.7573593111, 2), 3, -134.9999995731, 44.9999995731)
                Line((3, -1), (-0.7573593111, -1))
                Line((3, -0.5), (3, -1))
                Line((0.5, -0.5), (3, -0.5))
                CenterArc((0.5, 0), 0.5, 180, 90)
                Line((-3, 0), (0, 0))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


def model_38287_88ec74de_0066():
    """Model: szeroki v1 (8)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.6211275016, perimeter: 10.9955742876
            Circle(1.75)
        # OneSide extrude, distance=0.25
        extrude(amount=0.25)
    return part.part


def model_38287_88ec74de_0074():
    """Model: Podstawa v5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 14 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 340.2563270116, perimeter: 90.5532192682
            with BuildLine():
                CenterArc((4.3521490745, 7.5381433192), 2.5, 30, 60)
                Line((4.3521490745, 10.0381433192), (-4.3521490745, 10.0381433192))
                CenterArc((-4.3521490745, 7.5381433192), 2.5, 90, 60)
                Line((-6.517212584, 8.7881433192), (-10.8693616585, 1.25))
                CenterArc((-8.7042981491, 0), 2.5, 150, 60)
                Line((-10.8693616585, -1.25), (-6.517212584, -8.7881433192))
                CenterArc((-4.3521490745, -7.5381433192), 2.5, -150, 60)
                Line((-4.3521490745, -10.0381433192), (4.3521490745, -10.0381433192))
                CenterArc((4.3521490745, -7.5381433192), 2.5, -90, 60)
                Line((10.8693616585, -1.25), (6.517212584, -8.7881433192))
                CenterArc((8.7042981491, 0), 2.5, -30, 60)
                Line((6.517212584, 8.7881433192), (10.8693616585, 1.25))
            make_face()
            with BuildLine():
                CenterArc((4.9294993437, -8.5381433192), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-4.9294993437, -8.5381433192), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-9.8589986874, 0), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-4.9294993437, 8.5381433192), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.9294993437, 8.5381433192), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((9.8589986874, 0), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_38287_88ec74de_0076():
    """Model: Untitled v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 10.0138265833, perimeter: 26.7035375555
            with BuildLine():
                CenterArc((0, 0), 2.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.25
        extrude(amount=0.25)
    return part.part


def model_38287_88ec74de_0080():
    """Model: Siłownik2 v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.7123889804, perimeter: 18.8495559215
            with BuildLine():
                CenterArc((0, 0), 1.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=11.3
        extrude(amount=11.3)
    return part.part


def model_38287_88ec74de_0083():
    """Model: zeger 4 v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 14 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2560404002, perimeter: 4.8697867548
            with BuildLine():
                CenterArc((0.3499999922, -0.1499999966), 0.1, -100.3003034021, 192.3629318569)
                Line((0.3464008039, -0.0500647884), (0.2224597354, -0.0500647884))
                CenterArc((0.2224597354, -0.0900647884), 0.04, 90, 67.9590015182)
                CenterArc((0, 0), 0.2, 22.0409984818, 315.9180030365)
                CenterArc((0.2224597354, 0.0900647884), 0.04, -157.9590015182, 67.9590015182)
                Line((0.3464008039, 0.0500647884), (0.2224597354, 0.0500647884))
                CenterArc((0.3499999922, 0.1499999966), 0.1, -92.0626284548, 192.3629318569)
                CenterArc((0.3052981359, 0.3959710194), 0.15, -127.6326297943, 47.9329331964)
                CenterArc((0, 0), 0.35, 52.3673702057, 255.2652595886)
                CenterArc((0.3052981359, -0.3959710194), 0.15, 79.6996965979, 47.9329331964)
            make_face()
            with BuildLine():
                CenterArc((0.3499999922, -0.1499999966), 0.075, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.3499999922, 0.1499999966), 0.075, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


def model_38287_88ec74de_0086():
    """Model: Sruba 10 v2 (4)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.812678048, perimeter: 9.1415926536
            with BuildLine():
                Line((0.5, -0.8660254038), (1, 0))
                Line((1, 0), (0.5, 0.8660254038))
                Line((0.5, 0.8660254038), (-0.5, 0.8660254038))
                Line((-0.5, 0.8660254038), (-1, 0))
                Line((-1, 0), (-0.5, -0.8660254038))
                Line((-0.5, -0.8660254038), (0.5, -0.8660254038))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


def model_38287_88ec74de_0087():
    """Model: Oko v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.3673171724, perimeter: 16.1283983886
            with BuildLine():
                Line((-1.7500000261, 0.5000000075), (-1.7500000261, -0.5000000075))
                Line((-1.7500000261, -0.5000000075), (-0.9552958829, -1.1564643428))
                CenterArc((0, 0), 1.5, -129.5583655666, 259.1167311331)
                Line((-1.7500000261, 0.5000000075), (-0.9552958829, 1.1564643428))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_38287_88ec74de_0089():
    """Model: zeger v1 (3)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 14 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.2366545475, perimeter: 28.1565773594
            with BuildLine():
                CenterArc((2.2500000335, -0.2500000037), 0.2, -58.4265901456, 150.1761576456)
                Line((2.2438938399, -0.0500932395), (1.8398059938, -0.0624361866))
                CenterArc((1.8428590906, -0.1623895688), 0.1, 91.7495675, 83.2146342612)
                CenterArc((0, 0), 1.75, 5.0357982388, 349.9284035224)
                CenterArc((1.8428590906, 0.1623895688), 0.1, -174.9642017612, 83.2146342612)
                Line((2.2438938399, 0.0500932395), (1.8398059938, 0.0624361866))
                CenterArc((2.2500000335, 0.2500000037), 0.2, -91.7495675, 150.1761576456)
                CenterArc((2.6165134363, 0.8463790154), 0.5, -162.0748562268, 40.5014463723)
                CenterArc((0, 0), 2.25, 17.9251437732, 324.1497124535)
                CenterArc((2.6165134363, -0.8463790154), 0.5, 121.5734098544, 40.5014463723)
            make_face()
            with BuildLine():
                CenterArc((2.2500000335, -0.2500000037), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.2500000335, 0.2500000037), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


def model_38287_88ec74de_0091():
    """Model: zeger 2 v1 (11)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 16 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.0619992331, perimeter: 26.4551583481
            with BuildLine():
                CenterArc((2.0000000298, -0.400000006), 0.3000000045, -68.8313290423, 159.3092036722)
                Line((1.9974979131, -0.100010436), (1.7374481262, -0.1021794278))
                CenterArc((1.7382821651, -0.2021759496), 0.1, 90.4778746299, 82.8879809)
                CenterArc((0, 0), 1.65, 6.6341444701, 346.7317110598)
                CenterArc((1.7382821651, 0.2021759496), 0.1, -173.3658555299, 82.8879809)
                Line((1.9974979131, 0.100010436), (1.7374481262, 0.1021794278))
                CenterArc((2.0000000298, 0.400000006), 0.3000000045, -90.4778746299, 159.3092036722)
                CenterArc((2.3791704938, 1.3791474763), 0.75, -149.9001698024, 38.7314988447)
                CenterArc((0, 0), 2, 30.0998301976, 299.8003396047)
                CenterArc((2.3791704938, -1.3791474763), 0.75, 111.1686709577, 38.7314988447)
            make_face()
            with BuildLine():
                CenterArc((2.0000000298, -0.400000006), 0.200000003, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.0000000298, 0.400000006), 0.200000003, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.25
        extrude(amount=0.25)
    return part.part


def model_38287_88ec74de_0093():
    """Model: wazki v1 (11)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.5529859994, perimeter: 10.3672557568
            Circle(1.65)
        # OneSide extrude, distance=0.25
        extrude(amount=0.25)
    return part.part


def model_38287_88ec74de_0094():
    """Model: uchwyt v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.5749131403, perimeter: 24.0849918007
            with BuildLine():
                Line((-2.5, 0.2132462576), (-2.5, -0.2132462576))
                Line((-2.5, -0.2132462576), (-1.4858021567, -1.3388024317))
                CenterArc((0, 0), 2, -137.9791328362, 275.9582656724)
                Line((-2.5, 0.2132462576), (-1.4858021567, 1.3388024317))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_38288_740bfe5a_0006():
    """Model: Standoffs v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.3430308594, perimeter: 5.9690260418
            with BuildLine():
                CenterArc((3.5, 3.5), 0.7, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((3.5, 3.5), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


def model_38358_1b7da978_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch3 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 14.0562628348, perimeter: 26.6897216544
            with BuildLine():
                Line((-4.5812522441, -3.5448013032), (-4.5812522441, 0))
                Line((0, -4.7467284963), (-4.5812522441, -3.5448013032))
                Line((0, 0), (0, -4.7467284963))
                Line((-4.5812522441, 0), (0, 0))
            make_face()
            with BuildLine():
                Line((-0.7982413054, -2.1115156716), (-2.054748176, -1.1250863529))
                Line((-0.7982413054, -3.4540484591), (-0.7982413054, -2.1115156716))
                Line((-3.6769425338, -2.6563786345), (-0.7982413054, -3.4540484591))
                Line((-3.6769425338, -1.1250863529), (-3.6769425338, -2.6563786345))
                Line((-2.054748176, -1.1250863529), (-3.6769425338, -1.1250863529))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_38360_ad61c9b2_0002():
    """Model: C_SwingArm"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 8 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 21.3964701218, perimeter: 31.8153468615
            with BuildLine():
                CenterArc((0, 7.5000001118), 1.75, 174.2265241677, 192.7587404169)
                Line((1.7370105574, 7.7128247428), (0.9211985422, 14.3712367724))
                CenterArc((-0.0713789192, 14.2496226975), 1, 6.9852645846, 167.2412595831)
                Line((-1.0663063038, 14.3502184197), (-1.7411229231, 7.6760426256))
            make_face()
            with BuildLine():
                CenterArc((-0.0713789192, 14.2496226975), 0.7517013797, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 7.5000001118), 0.775, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.5
        extrude(amount=0.5, both=True)
    return part.part


def model_38362_ab17f1f1_0002():
    """Model: handle"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 9.2092511455, perimeter: 31.8474139133
            with BuildLine():
                CenterArc((7.25, 21.75), 2.4748737342, -45, 90)
                Line((6, 26.5), (9, 23.5))
                CenterArc((6, 26), 0.5, 90, 90)
                Line((5.5, 20.5), (5.5, 26))
                Line((6, 20), (5.5, 20.5))
                Line((9, 20), (6, 20))
            make_face()
            with BuildLine():
                Line((8.7457364951, 20.6549197096), (6.3671925387, 20.6549197096))
                Line((6.3671925387, 20.6549197096), (5.9844305434, 21.0079200759))
                Line((5.9844305434, 21.0079200759), (6, 25.5))
                Line((6, 25.5), (8.7457364951, 22.9677580318))
                CenterArc((7.6792346156, 21.8113388707), 1.5731279462, -47.3163547226, 94.6327094451)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.4877
        extrude(amount=0.4877, both=True)
    return part.part


def model_38362_ab17f1f1_0004():
    """Model: trigger"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 5.0790307638, perimeter: 11.2772485584
            with BuildLine():
                Line((7.6000001132, -6.6000000983), (7.3000001088, -6.9000001028))
                Line((7.3000001088, -6.9000001028), (9.1000001356, -7.7000001147))
                CenterArc((10.3168593292, -4.9620669291), 2.9961682907, -113.9624889746, 47.9249779492)
                Line((11.5337185228, -7.7000001147), (12.4000001848, -6.6000000983))
                Line((12.4000001848, -6.6000000983), (12.0000001788, -6.3000000939))
                CenterArc((11.8000001758, -6.5666667645), 0.3333333383, 53.1301023542, 73.7397952917)
                Line((11.6000001729, -6.3000000939), (9.1000001356, -6.7000000998))
                CenterArc((8.5682354218, -3.3764706385), 3.3658018051, -106.7184265894, 25.8087035102)
            make_face()
        # Symmetric extrude, each_side=0.4996
        extrude(amount=0.4996, both=True)
    return part.part


def model_38362_ab17f1f1_0005():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 14 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.7559523013, perimeter: 16.6142751805
            with BuildLine():
                CenterArc((-0.7795522978, 0.257993334), 0.3, -162.9511662185, 72.9511662185)
                Line((0.7771196008, -0.042006666), (-0.7795522978, -0.042006666))
                CenterArc((0.7771196008, 0.257993334), 0.3, -90, 72.8886617738)
                Line((1.6911469617, 2.2073826418), (1.0638400434, 0.1697244958))
                CenterArc((1.5, 2.266228534), 0.2, -17.1113382262, 107.1113382262)
                Line((-1.5, 2.466228534), (1.5, 2.466228534))
                CenterArc((-1.5, 2.266228534), 0.2, 90, 107.0488337815)
                Line((-1.066368863, 0.170037334), (-1.6912110434, 2.2075912006))
            make_face()
            with BuildLine():
                CenterArc((0, 1.233114267), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=60.96
        extrude(amount=60.96)
    return part.part


def model_38454_24787d99_0002():
    """Model: Back Foot"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -5.1812348354), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 2.6143106161, perimeter: 8.9850098892
            with BuildLine():
                Line((10.8000001386, 1.5000000075), (9.3000001386, 1.5000000075))
                Line((9.3000001386, 1.5000000075), (9.3000001386, -0.2071067639))
                Line((11.5071069296, -0.2071067639), (9.3000001386, -0.2071067639))
                Line((10.8000001386, 0.5000000075), (11.5071069296, -0.2071067639))
                Line((10.8000001386, 1.5000000075), (10.8000001386, 0.5000000075))
            make_face()
            with BuildLine():
                CenterArc((10.05002239, 0.7500000079), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


def model_38675_6e07d74b_0004():
    """Model: BLADE v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 11 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.5458935228, perimeter: 12.3309310816
            with BuildLine():
                CenterArc((-1.8898718519, -0.1999999985), 0.3, 90, 70.0168934781)
                Line((-2.5000000373, -1.0000000149), (-2.171809879, -0.0974770796))
                Line((-2.0829179905, -0.1658359214), (-2.5000000373, -1.0000000149))
                CenterArc((-1.8145898332, -0.3), 0.3, 90, 63.4349488229)
                Line((-1.8145898332, 0), (1.8145898332, 0))
                CenterArc((1.8145898332, 0.3), 0.3, -90, 63.4349488229)
                Line((2.0829179905, 0.1658359214), (2.5000000373, 1.0000000149))
                Line((2.5000000373, 1.0000000149), (1.9890599891, 0.2335899426))
                CenterArc((1.7394449008, 0.4000000015), 0.3, -90, 56.309932474)
                Line((-1.8898718519, 0.1000000015), (1.7394449008, 0.1000000015))
            make_face()
        # Symmetric extrude, each_side=0.2
        extrude(amount=0.2, both=True)
    return part.part


def model_38739_f321c899_0006():
    """Model: Brake BB Sleeve v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.0782923947, perimeter: 17.4554741815
            with BuildLine():
                CenterArc((0, 0), 1.508125, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.27, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=5.08
        extrude(amount=5.08)
    return part.part


def model_38739_f321c899_0007():
    """Model: Rear Master Cylinder Casing v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.9173043609, perimeter: 9.9745566751
            Circle(1.5875)
        # OneSide extrude, distance=4.826
        extrude(amount=4.826)
    return part.part


def model_38739_f321c899_0016():
    """Model: Bushing 1 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4750382617, perimeter: 5.9847340051
            with BuildLine():
                CenterArc((0, 0), 0.555625, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.396875, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.13538
        extrude(amount=1.13538)
    return part.part


def model_38739_f321c899_0018():
    """Model: Bushing 2 v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4750382617, perimeter: 5.9847340051
            with BuildLine():
                CenterArc((0, 0), 0.555625, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.396875, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.5875
        extrude(amount=1.5875)
    return part.part


def model_38953_19054857_0003():
    """Model: Opona"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.5663706144, perimeter: 25.1327412287
            with BuildLine():
                CenterArc((-10.5000001565, -3.0000000447), 2.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-10.5000001565, -3.0000000447), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_38953_19054857_0006():
    """Model: Nakr kola"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0779422863, perimeter: 1.0392304845
            with BuildLine():
                Line((-0.8500000149, -4.0866026), (-0.8500000149, -3.9133975192))
                Line((-0.8500000149, -3.9133975192), (-1.0000000149, -3.8267949788))
                Line((-1.0000000149, -3.8267949788), (-1.1500000149, -3.9133975192))
                Line((-1.1500000149, -3.9133975192), (-1.1500000149, -4.0866026))
                Line((-1.1500000149, -4.0866026), (-1.0000000149, -4.1732051404))
                Line((-1.0000000149, -4.1732051404), (-0.8500000149, -4.0866026))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


def model_38953_19054857_0007():
    """Model: Zaczep krotki"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1457079995, perimeter: 3.3853984669
            with BuildLine():
                Line((1.7999999866, -1.8999999575), (0.4999999888, -1.8999999575))
                CenterArc((0.5000000075, -2.0000000298), 0.1000000723, 90.0000106722, 270.0000320165)
                Line((1.7999999866, -1.9999999553), (0.6000000797, -1.9999999553))
                Line((1.7999999866, -1.8999999575), (1.7999999866, -1.9999999553))
            make_face()
            with BuildLine():
                CenterArc((0.5000000075, -2.0000000298), 0.0500000007, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)
    return part.part


def model_38953_19054857_0008():
    """Model: Sruba 0.8 zawias"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0124707715, perimeter: 0.4156922878
            with BuildLine():
                Line((0.3399999859, 0.3346410173), (0.3399999989, 0.2653589693))
                Line((0.3399999989, 0.2653589693), (0.4000000189, 0.2307179565))
                Line((0.4000000189, 0.2307179565), (0.460000026, 0.2653589917))
                Line((0.460000026, 0.2653589917), (0.4600000131, 0.3346410396))
                Line((0.4600000131, 0.3346410396), (0.3999999931, 0.3692820524))
                Line((0.3999999931, 0.3692820524), (0.3399999859, 0.3346410173))
            make_face()
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)
    return part.part


def model_38953_19054857_0011():
    """Model: mocowanie wajchy 2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude3 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.4298938023, perimeter: 4.0053096684
            with BuildLine():
                Line((-7.8899600147, 16.0648611022), (-7.8899600147, 16.2148611022))
                Line((-7.8899600147, 16.2148611022), (-7.5899599938, 16.2148611022))
                Line((-7.5899599938, 16.2148611022), (-7.5899599938, 16.5148610628))
                Line((-7.5899599938, 16.5148610628), (-7.8899600147, 16.5148610628))
                Line((-7.8899600147, 16.6648611022), (-7.8899600147, 16.5148610628))
                Line((-8.4899600147, 16.6648611022), (-7.8899600147, 16.6648611022))
                Line((-8.4899600147, 16.0648611022), (-8.4899600147, 16.6648611022))
                Line((-7.8899600147, 16.0648611022), (-8.4899600147, 16.0648611022))
            make_face()
            with BuildLine():
                CenterArc((-8.4299600272, 16.1248611702), 0.0399999991, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-7.9499600379, 16.1248611702), 0.0399999991, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-7.9499600379, 16.6048611595), 0.0399999991, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-8.4299600272, 16.6048611595), 0.0399999991, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


def model_38953_19054857_0013():
    """Model: mocowanie wajcha"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3398938079, perimeter: 3.4053096267
            with BuildLine():
                Line((0.1499999966, 2.299999962), (0.1499999966, 1.699999962))
                Line((0.1499999966, 1.699999962), (0.7499999966, 1.699999962))
                Line((0.7499999966, 1.699999962), (0.7499999966, 2.299999962))
                Line((0.7499999966, 2.299999962), (0.1499999966, 2.299999962))
            make_face()
            with BuildLine():
                CenterArc((0.2099999953, 2.2399999499), 0.0399999991, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.6899999846, 2.2399999499), 0.0399999991, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.6899999846, 1.7599999607), 0.0399999991, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.2099999953, 1.7599999607), 0.0399999991, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


def model_38953_19054857_0014():
    """Model: zaczep"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.4943362901, perimeter: 7.9132741603
            with BuildLine():
                Line((3, 4.8), (3, 3))
                Line((3, 3), (3.9, 3))
                Line((3.9, 3), (3.9, 4.8))
                Line((3.9, 4.8), (3, 4.8))
            make_face()
            with BuildLine():
                CenterArc((3.7000000551, 3.2000000477), 0.1000000015, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.7000000551, 4.6000000685), 0.1000000015, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.2000000477, 4.6000000685), 0.1000000015, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.2000000477, 3.2000000477), 0.1000000015, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


def model_38953_19054857_0015():
    """Model: Zawias z dluga"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0457079571, perimeter: 1.7853981846
            with BuildLine():
                Line((0.5999999866, 0.9499999788), (0.6000000089, 0.9999999702))
                CenterArc((0.5000000075, 1.0000000149), 0.1000000015, -0.0000256132, 270.0000217712)
                Line((0.9999999866, 0.8999999799), (0.5000000007, 0.9000000134))
                Line((0.9999999866, 0.9499999788), (0.9999999866, 0.8999999799))
                Line((0.5999999866, 0.9499999788), (0.9999999866, 0.9499999788))
            make_face()
            with BuildLine():
                CenterArc((0.5000000075, 1.0000000149), 0.05, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


def model_39124_28e99e62_0000():
    """Model: Bucket"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 6.8713203436, perimeter: 28.4852813742
            with BuildLine():
                Line((-2.5, 7.5), (-2.5, 5))
                Line((-2.5, 5), (0, 2.5))
                Line((0, 2.5), (2.5, 2.5))
                Line((2.5, 2.5), (5, 5))
                Line((5, 5), (5, 7.5))
                Line((4.5, 7.5), (5, 7.5))
                Line((4.5, 5.2071067812), (4.5, 7.5))
                Line((2.2928932188, 3), (4.5, 5.2071067812))
                Line((0.2071067812, 3), (2.2928932188, 3))
                Line((-2, 5.2071067812), (0.2071067812, 3))
                Line((-2, 7.5), (-2, 5.2071067812))
                Line((-2.5, 7.5), (-2, 7.5))
            make_face()
        # Symmetric extrude, each_side=2.5
        extrude(amount=2.5, both=True)
    return part.part


def model_39124_28e99e62_0003():
    """Model: Chute"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 10.3304476863, perimeter: 17.1866404513
            with BuildLine():
                Line((2.5, 10), (3, 10))
                Line((3, 10), (3, 12.3050746144))
                Line((3, 12.3050746144), (-3, 12.3050746144))
                Line((-3, 12.3050746144), (-3, 10))
                Line((-3, 10), (-2.5, 10))
                Line((-2.5, 10), (-2, 10.5))
                Line((-2, 10.5), (-0.5, 11))
                Line((-0.5, 11), (0.5, 11))
                Line((0.5, 11), (2, 10.5))
                Line((2, 10.5), (2.5, 10))
            make_face()
        # OneSide extrude, distance=-37.194
        extrude(amount=-37.194)
    return part.part


def model_39306_ee445998_0010():
    """Model: Rod v6 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            Circle(0.1)
        # OneSide extrude, distance=10
        extrude(amount=10)
    return part.part


def model_39306_ee445998_0011():
    """Model: Bracket v6"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 13 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.3280390026, perimeter: 6.2407914115
            with BuildLine():
                Line((0, 0.1000000015), (0, 0))
                Line((0, 0), (0.8000000119, 0))
                Line((0.8000000119, 0.1000000015), (0.8000000119, 0))
                Line((0.6000000089, 0.1000000015), (0.8000000119, 0.1000000015))
                Line((0.6000000089, 1.0500000156), (0.6000000089, 0.1000000015))
                CenterArc((0.400000006, 1.0500000156), 0.200000003, 0, 180)
                Line((0.200000003, 0.1000000015), (0.200000003, 1.0500000156))
                Line((0, 0.1000000015), (0.200000003, 0.1000000015))
            make_face()
            with BuildLine():
                Line((0.2991655104, 0.1500244111), (0.4948865533, 0.1500244111))
                Line((0.2991655104, 1.0500000156), (0.2991655104, 0.1500244111))
                CenterArc((0.400000006, 1.0500000156), 0.1008344956, -0.4251315568, 180.4251315568)
                Line((0.4948865533, 0.1500244111), (0.5008317258, 1.0492518361))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_39306_ee445998_0017():
    """Model: Brace v15"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.7999999754, perimeter: 21.6000001356
            with BuildLine():
                Line((2.4999999441, -0.400000006), (2.4999999441, 3.0000000447))
                Line((2.4999999441, 3.0000000447), (-2.5000000373, 3.0000000447))
                Line((-2.5000000373, -0.400000006), (-2.5000000373, 3.0000000447))
                Line((-2.5000000373, -0.400000006), (-1.5000000224, -0.400000006))
                Line((-1.5000000224, -0.400000006), (-1.5000000224, 2.0000000298))
                Line((-1.5000000224, 2.0000000298), (1.5000000224, 2.0000000298))
                Line((1.5000000224, 2.0000000298), (1.5000000224, -0.400000006))
                Line((2.4999999441, -0.400000006), (1.5000000224, -0.400000006))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


def model_39306_ee445998_0030():
    """Model: Connector v5 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0007068584, perimeter: 0.0942477841
            Circle(0.0150000007)
        # OneSide extrude, distance=21.05
        extrude(amount=21.05)
    return part.part


def model_39306_ee445998_0033():
    """Model: Stopper v1 (3)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.065500293, perimeter: 1.5121079993
            with BuildLine():
                Line((0.1000000015, -0.1000000015), (0.1000000015, 0.2999999933))
                CenterArc((0.1024999977, 0.1974999953), 0.1025304811, 91.3971789297, 87.2056357374)
                Line((0, 0), (0, 0.200000003))
                Line((-0.200000003, 0), (0, 0))
                CenterArc((-0.1974999953, -0.1024999978), 0.1025304813, 91.3971853698, 87.2056335293)
                Line((-0.2999999933, -0.0999999978), (-0.200000003, -0.1000000015))
                Line((0.1000000015, -0.1000000015), (-0.200000003, -0.1000000015))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


def model_39389_d641313f_0018():
    """Model: Dust Seal"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.0159289474, perimeter: 15.0796447372
            with BuildLine():
                CenterArc((0, 0), 1.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


def model_39389_d641313f_0022():
    """Model: Retainder Ring"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.926990817, perimeter: 15.7079632679
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


def model_39389_d641313f_0046():
    """Model: O-ring Sealant (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.3379421944, perimeter: 26.7035375555
            with BuildLine():
                CenterArc((0, 0), 2.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


def model_39389_d641313f_0048():
    """Model: O-ring Piston (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.5238934212, perimeter: 22.6194671058
            with BuildLine():
                CenterArc((0, 0), 2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


def model_39389_d641313f_0049():
    """Model: Piston Seal UHMWP (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.5238934212, perimeter: 22.6194671058
            with BuildLine():
                CenterArc((0, 0), 2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_39389_d641313f_0062():
    """Model: Spacer 10mm UHMWP (5)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.0579641723, perimeter: 14.4513262065
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_39389_d641313f_0065():
    """Model: Main Arm Plate 2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 321.0274060002, perimeter: 141.2305382322
            with BuildLine():
                Line((37.61, 7.6457029028), (37.61, 7.016))
                CenterArc((36.11, 7.016), 1.5, -90, 90)
                Line((0, 5.516), (36.11, 5.516))
                CenterArc((0, 2.758), 2.758, 90, 180)
                Line((0, 0), (50, 0))
                CenterArc((50, 2.8), 2.8, -90, 180)
                CenterArc((58.1378979209, 38.2290631232), 33.6285762837, -121.3292805871, 17.3250504851)
                CenterArc((58.1378979209, 38.2290631232), 33.6285762837, -121.356266943, 0.0269863559)
                CenterArc((39.605, 7.799), 2.0008810559, 58.8840051046, 125.5100052986)
            make_face()
            with BuildLine():
                CenterArc((50, 2.8), 0.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((39.605, 7.799), 0.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 2.758), 0.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((35, 2.8), 0.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_39390_61cd2601_0006():
    """Model: Clamp Base"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 30.1090713822, perimeter: 44.9251676687
            with BuildLine():
                Line((10.6401737391, -5.3447954252), (6.3223437131, -4.676783491))
                CenterArc((10.7916, -4.3664390344), 0.9900056262, -98.7982092589, 171.3589082098)
                Line((11.0883, -3.4219390344), (6.3267, -1.9261390344))
                CenterArc((5.9401, -3.1567), 1.2898603995, 72.5590719492, 37.9777798937)
                Line((5.4876043787, -1.9488144248), (2.2982, -3.1434786076))
                CenterArc((2.0842, -2.5722), 0.6100452832, -166.0005047822, 96.5363695945)
                Line((1.4922743687, -2.7197780964), (0.7665353075, 0.1911115443))
                CenterArc((0, 0), 0.79, 13.9994952178, 180)
                Line((0.3220646925, -4.5574115443), (-0.7665353075, -0.1911115443))
                CenterArc((1.0886, -4.3663), 0.79, -166.0005047822, 82.2647444874)
                Line((5.6385, -4.6616831082), (1.1748, -5.1515831082))
                CenterArc((5.9233, -7.2560831082), 2.6099851341, 81.2054878306, 15.0590672466)
            make_face()
            with BuildLine():
                CenterArc((8.851, -3.8826390344), 0.31, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((10.7916, -4.3664390344), 0.41, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.9401, -3.1567), 0.41, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.0886, -4.3663), 0.31, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0), 0.31, -174.0854913973, 354.0854913973)
                Line((-0.3221, -0.0333682333), (-0.3083497943, -0.0319437687))
                Line((-0.3221, 0), (-0.3221, -0.0333682333))
                Line((-0.31, 0), (-0.3221, 0))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.25
        extrude(amount=0.25)
    return part.part


def model_39390_61cd2601_0019():
    """Model: Clamp Foot Pin (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.175396618, perimeter: 3.0464023962
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.18485, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)
    return part.part


def model_39394_3e0555d8_0000():
    """Model: House-Roof"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 5.275687829, perimeter: 22.1027513158
            with BuildLine():
                Line((8.2640028993, 4.4736793379), (13.7640028993, 4.4736793379))
                Line((13.7640028993, 4.4736793379), (13.7640028993, 4.9736793379))
                Line((13.7640028993, 4.9736793379), (8.7126272414, 4.9736793379))
                Line((8.1670819249, 9.9955093176), (8.7126272414, 4.9736793379))
                Line((7.6700064429, 9.9415096397), (8.1670819249, 9.9955093176))
                Line((8.2640028993, 4.4736793379), (7.6700064429, 9.9415096397))
            make_face()
        # OneSide extrude, distance=12.5
        extrude(amount=12.5)
    return part.part


def model_39395_c95928c9_0000():
    """Model: Pencil"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0042813504, perimeter: 0.2435654549
            with BuildLine():
                Line((-3.8490279667, 2.525273344), (-3.8190138924, 2.5526055203))
                Line((-3.8190138924, 2.5526055203), (-3.8276772143, 2.5922645594))
                Line((-3.8276772143, 2.5922645594), (-3.8663546105, 2.604591422))
                Line((-3.8663546105, 2.604591422), (-3.8963686849, 2.5772592457))
                Line((-3.8963686849, 2.5772592457), (-3.8877053629, 2.5376002066))
                Line((-3.8877053629, 2.5376002066), (-3.8490279667, 2.525273344))
            make_face()
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)
    return part.part


def model_39633_694ad30a_0000():
    """Model: Axis"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            Circle(0.6)
        # TwoSides extrude (symmetric), distance=5.5
        extrude(amount=5.5, both=True)
    return part.part


def model_39633_694ad30a_0003():
    """Model: Rear axis"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-140, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((105.2812622126, 2.9136811781)):
                Circle(0.6)
        # Symmetric extrude, each_side=8
        extrude(amount=8, both=True)
    return part.part


def model_39708_228f26be_0000():
    """Model: locking pin 6"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 29.1863515174, perimeter: 19.151149053
            Circle(3.0480000377)
        # OneSide extrude, distance=18.288
        extrude(amount=18.288)
    return part.part


def model_39708_228f26be_0001():
    """Model: Wheel 1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2881.4738612296, perimeter: 215.895488941
            with BuildLine():
                CenterArc((0, 0), 30.48, 0, 360)
            make_face()
            with BuildLine():
                Line((-3.0480000973, -3.0480000973), (3.0480000973, -3.0480000973))
                Line((-3.0480000973, 3.0480000973), (-3.0480000973, -3.0480000973))
                Line((3.0480000973, 3.0480000973), (-3.0480000973, 3.0480000973))
                Line((3.0480000973, -3.0480000973), (3.0480000973, 3.0480000973))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=9.144
        extrude(amount=9.144)
    return part.part


def model_39708_228f26be_0012():
    """Model: long locking pin 13"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.296587699, perimeter: 9.5755744081
            Circle(1.524)
        # OneSide extrude, distance=54.864
        extrude(amount=54.864)
    return part.part


def model_39793_5193d5ab_0014():
    """Model: Gear Knob v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0197932609, perimeter: 0.4987278338
            Circle(0.079375)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


def model_39793_5193d5ab_0016():
    """Model: Gas Tank v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 5.067074791, perimeter: 7.9796453401
            Circle(1.27)
        # OneSide extrude, distance=3.81
        extrude(amount=3.81)
    return part.part


def model_39793_5193d5ab_0019():
    """Model: Smoke Stack v6"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            Circle(0.635)
        # OneSide extrude, distance=5.715
        extrude(amount=5.715)
    return part.part


def model_39793_5193d5ab_0021():
    """Model: Bottom Headlight v3 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.9793260902, perimeter: 4.9872783376
            Circle(0.79375)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


def model_39793_5193d5ab_0023():
    """Model: Tire v2 (3)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 55.7378227007, perimeter: 43.8880493706
            with BuildLine():
                CenterArc((0, 0), 4.7625, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.2225, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3.81
        extrude(amount=3.81)
    return part.part


def model_39793_5193d5ab_0026():
    """Model: Axle v5 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.3166921744, perimeter: 1.994911335
            Circle(0.3175)
        # OneSide extrude, distance=17.4625
        extrude(amount=17.4625)
    return part.part


def model_39795_7d4d7d57_0003():
    """Model: Back Pillars"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.6129, perimeter: 5.08
            with BuildLine():
                Line((2.5399999809, 10.1599998283), (1.2699999809, 10.1599998283))
                Line((2.5399999809, 11.4299998283), (2.5399999809, 10.1599998283))
                Line((1.2699999809, 11.4299998283), (2.5399999809, 11.4299998283))
                Line((1.2699999809, 10.1599998283), (1.2699999809, 11.4299998283))
            make_face()
            # Profile area: 1.6129, perimeter: 5.08
            with BuildLine():
                Line((13.9699997902, 10.1599998283), (13.9699997902, 11.4299998283))
                Line((13.9699997902, 11.4299998283), (12.6999997902, 11.4299998283))
                Line((12.6999997902, 11.4299998283), (12.6999997902, 10.1599998283))
                Line((12.6999997902, 10.1599998283), (13.9699997902, 10.1599998283))
            make_face()
        # OneSide extrude, distance=17.78
        extrude(amount=17.78)
    return part.part


def model_39795_7d4d7d57_0004():
    """Model: Front Pillars"""
    with BuildPart() as part:
        # Sketch4 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.8502295699, perimeter: 5.9847340051
            with Locations((12.7, 2.54)):
                Circle(0.9525)
            # Profile area: 2.8502295699, perimeter: 5.9847340051
            with Locations((2.5399999619, 2.5399999619)):
                Circle(0.9525)
        # OneSide extrude, distance=17.78
        extrude(amount=17.78)
    return part.part


def model_39850_b2aa4f1e_0011():
    """Model: intermediate motor v3"""
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
        # Sketch1 -> Extrude3 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 23.7272228374, perimeter: 41.1165839247
            with BuildLine():
                Line((1.2246428571, 0), (-1.2246428571, 0))
                _nurbs_edge([(-1.2246428571, 0), (-1.302391867, -0.0112447416), (-1.4551982324, -0.04920341), (-1.6763321299, -0.1525451021), (-1.9549146809, -0.3838498386), (-2.2740128504, -0.8291012499), (-2.5592311041, -1.4246590334), (-2.8017732828, -2.1518024442), (-2.9885863019, -2.976832268), (-3.104161877, -3.8579266592), (-3.1319310316, -4.749359417), (-3.0561078205, -5.6065625945), (-2.8634158318, -6.3903328432), (-2.5458187057, -7.0725703641), (-2.1015548961, -7.638667006), (-1.5321105831, -8.0824456944), (-0.9788251622, -8.3390564455), (-0.5101486231, -8.4768724566), (-0.1739993181, -8.5446421828), (0, -8.5725)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9333333333, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(1.2246428571, 0), (1.302391867, -0.0112447416), (1.4551982324, -0.04920341), (1.6763321299, -0.1525451021), (1.9549146809, -0.3838498386), (2.2740128504, -0.8291012499), (2.5592311041, -1.4246590334), (2.8017732828, -2.1518024442), (2.9885863019, -2.976832268), (3.104161877, -3.8579266592), (3.1319310316, -4.749359417), (3.0561078205, -5.6065625945), (2.8634158318, -6.3903328432), (2.5458187057, -7.0725703641), (2.1015548961, -7.638667006), (1.5321105831, -8.0824456944), (0.9788251622, -8.3390564455), (0.5101486231, -8.4768724566), (0.1739993181, -8.5446421828), (0, -8.5725)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9333333333, 1, 1, 1, 1, 1, 1], 5)
            make_face()
            with BuildLine():
                CenterArc((0, -4.92125), 2.54, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-2.2225, -2.38125), 0.079375, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.2225, -2.38125), 0.079375, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3175
        extrude(amount=0.3175)
    return part.part


def model_39932_7b9150e8_0001():
    """Model: Workbench Bottom"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -4, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 14468.856, perimeter: 494.68
            with BuildLine():
                Line((76.2, 46.219999904), (-76.2, 46.219999904))
                Line((-76.2, -48.720000096), (-76.2, 46.219999904))
                Line((76.2, -48.720000096), (-76.2, -48.720000096))
                Line((76.2, 46.219999904), (76.2, -48.720000096))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


def model_39932_7b9150e8_0004():
    """Model: Bottom Left/Right Frame"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 15 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 23.7071035847, perimeter: 21.0004704858
            with BuildLine():
                CenterArc((0.8904, 3.3904), 0.6096, 0, 90)
                Line((0.8904, 4), (-1, 4))
                CenterArc((-1, 3.5), 0.5, 90, 90)
                Line((-1.5, 3.5), (-1.5, -3.3904))
                CenterArc((-0.8904, -3.3904), 0.6096, -180, 90)
                Line((-0.8904, -4), (0.8904, -4))
                CenterArc((0.8904, -3.3904), 0.6096, -90, 90)
                Line((1.5, -3.3904), (1.5, 3.3904))
            make_face()
        # Symmetric extrude, each_side=45.72
        extrude(amount=45.72, both=True)
    return part.part


def model_39932_7b9150e8_0005():
    """Model: Bottom Front/Back Frame"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 15 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 23.7853981634, perimeter: 21.1415926536
            with BuildLine():
                CenterArc((1, 3.5), 0.5, 0, 90)
                Line((1, 4), (-1, 4))
                CenterArc((-1, 3.5), 0.5, 90, 90)
                Line((-1.5, 3.5), (-1.5, -3.5))
                CenterArc((-1, -3.5), 0.5, 180, 90)
                Line((-1, -4), (1, -4))
                CenterArc((1, -3.5), 0.5, -90, 90)
                Line((1.5, -3.5), (1.5, 3.5))
            make_face()
        # Symmetric extrude, each_side=76.2
        extrude(amount=76.2, both=True)
    return part.part


def model_39932_7b9150e8_0006():
    """Model: Wheel"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 48.719999904), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 136.6375829119, perimeter: 52.3775498336
            with BuildLine():
                CenterArc((-64.0080020428, 0), 11.7763499202, -162.7101434067, 145.4202868134)
                Line((-75.2522191094, -3.5), (-52.7637849761, -3.5))
            make_face()
            # Profile area: 162.4084979938, perimeter: 59.1916256566
            with BuildLine():
                CenterArc((-64.0080020428, 0), 11.7763499202, 162.7101434067, 34.5797131866)
                Line((-75.2522191094, -3.5), (-52.7637849761, -3.5))
                CenterArc((-64.0080020428, 0), 11.7763499202, -17.2898565933, 34.5797131866)
                Line((-52.7637849761, 3.5), (-75.2522191094, 3.5))
            make_face()
            # Profile area: 136.6375829119, perimeter: 52.3775498336
            with BuildLine():
                Line((-52.7637849761, 3.5), (-75.2522191094, 3.5))
                CenterArc((-64.0080020428, 0), 11.7763499202, 17.2898565933, 145.4202868134)
            make_face()
        # OneSide extrude, distance=6.096
        extrude(amount=6.096)
    return part.part


def model_40052_42bdc982_0001():
    """Model: ClampGear"""
    with BuildPart() as part:
        # Sketch1 -> Extrude4 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 18 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 20.080967894, perimeter: 28.0770659524
            with BuildLine():
                Line((-1.6577610037, -0.0003656642), (0, 0))
                Line((1.6577610037, -0.0003656642), (0, 0))
                CenterArc((0, 2.5), 3, -56.4553262753, 95.411840654)
                CenterArc((0, 2.5), 3, 38.9565143787, 102.0869712426)
                CenterArc((0, 2.5), 3, 141.0434856213, 95.411840654)
            make_face()
            with BuildLine():
                CenterArc((0, 2.5), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 21.7153592503, perimeter: 23.3750364412
            with BuildLine():
                Line((-2.8126641585, 4.0603023912), (-10.0575112021, 1.8))
                Line((-10.0575112021, 1.8), (-10.057113674, -0.0022183693))
                Line((-10.057113674, -0.0022183693), (-1.6577610037, -0.0003656642))
                CenterArc((0, 2.5), 3, 141.0434856213, 95.411840654)
                CenterArc((-3.1104934846, 5.014921526), 1, -72.6727260304, 33.7162116517)
            make_face()
            # Profile area: 21.7153592503, perimeter: 23.3750364412
            with BuildLine():
                CenterArc((0, 2.5), 3, -56.4553262753, 95.411840654)
                Line((10.057113674, -0.0022183693), (1.6577610037, -0.0003656642))
                Line((10.0575112021, 1.8), (10.057113674, -0.0022183693))
                Line((2.8126641585, 4.0603023912), (10.0575112021, 1.8))
                CenterArc((3.1104934846, 5.014921526), 1, -141.0434856213, 33.7162116517)
            make_face()
        # Symmetric extrude, each_side=1
        extrude(amount=1, both=True)
    return part.part


def model_40052_42bdc982_0007():
    """Model: SideGuard"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 8 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2634.5307191372, perimeter: 260.2617358356
            with BuildLine():
                Line((-56.1, 0), (56.1, 0))
                Line((56.1, 0), (46.7794745265, 25.6079332759))
                Line((46.7794745265, 25.6079332759), (-46.7794745265, 25.6079332759))
                Line((-56.1, 0), (-46.7794745265, 25.6079332759))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


def model_40052_42bdc982_0012():
    """Model: |Beam"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 10 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 443.8058802057, perimeter: 260.941062349
            with BuildLine():
                Line((0, -3.6), (0, 0))
                Line((-127.577708599, 0), (0, 0))
                CenterArc((-125, 0), 2.577708599, 180, 90)
                Line((-114.5327505353, -2.577708599), (-125, -2.577708599))
                CenterArc((-114.5, -3.3770379444), 0.8, 87.6537600211, 4.6924799579)
                CenterArc((-114.5, -3.3770379444), 0.8, -16.1827852622, 103.8365452832)
                Line((0, -3.6), (-113.731698027, -3.6))
            make_face()
        # TwoSides extrude (symmetric), distance=1.9
        extrude(amount=1.9, both=True)
    return part.part


def model_40052_42bdc982_0013():
    """Model: Beam"""
    with BuildPart() as part:
        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 40.32, perimeter: 25.6
            with BuildLine():
                Line((-5.6, 7.2), (0, 7.2))
                Line((-5.6, 0), (-5.6, 7.2))
                Line((0, 0), (-5.6, 0))
                Line((0, 7.2), (0, 0))
            make_face()
        # TwoSides extrude (symmetric), distance=61
        extrude(amount=61, both=True)
    return part.part


def model_40052_42bdc982_0014():
    """Model: Floor"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 15 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 22043.2896691685, perimeter: 924.3698273363
            with BuildLine():
                Line((-56, 108.75), (56, 108.75))
                Line((-56, -108.75), (-56, 108.75))
                Line((56, -108.75), (-56, -108.75))
                Line((56, 108.75), (56, -108.75))
            make_face()
            with BuildLine():
                Line((-10.3424568341, -56), (10.3424568341, -56))
                Line((-10.3424568341, 56), (-10.3424568341, -56))
                Line((10.3424568341, 56), (-10.3424568341, 56))
                Line((10.3424568341, -56), (10.3424568341, 56))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3
        extrude(amount=3)
    return part.part


def model_40052_42bdc982_0015():
    """Model: BrakeJoint"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 12 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.799111126, perimeter: 12.6192904099
            with BuildLine():
                CenterArc((0, 0), 1.2, 14.2800298656, 331.4399402688)
                Line((0.8499340246, -0.295993503), (1.1629221153, -0.295993503))
                CenterArc((0, 0), 0.9, 19.2009114735, 321.598177053)
                Line((0.8499340246, 0.295993503), (1.1629221153, 0.295993503))
            make_face()
            # Profile area: 6.1737024496, perimeter: 22.1756626368
            with BuildLine():
                CenterArc((0, 0), 1.2, -14.2800298656, 28.5600597312)
                Line((1.1629221153, -0.295993503), (11.6500659754, -0.295993503))
                CenterArc((12.5, 0), 0.9, 160.7990885265, 38.401822947)
                Line((1.1629221153, 0.295993503), (11.6500659754, 0.295993503))
            make_face()
            # Profile area: 1.2309024992, perimeter: 8.8585294696
            with BuildLine():
                Line((11.6500659754, 0.295993503), (11.9780921095, 0.295993503))
                CenterArc((12.5, 0), 0.6, -150.4408048699, 300.8816097398)
                Line((11.6500659754, -0.295993503), (11.9780921095, -0.295993503))
                CenterArc((12.5, 0), 0.9, -160.7990885265, 321.598177053)
            make_face()
            # Profile area: 0.1828141949, perimeter: 1.8783530276
            with BuildLine():
                CenterArc((12.5, 0), 0.9, 160.7990885265, 38.401822947)
                Line((11.6500659754, -0.295993503), (11.9780921095, -0.295993503))
                CenterArc((12.5, 0), 0.6, 150.4408048699, 59.1183902602)
                Line((11.6500659754, 0.295993503), (11.9780921095, 0.295993503))
            make_face()
            # Profile area: 0.1800922458, perimeter: 1.8273510979
            with BuildLine():
                Line((0.8499340246, 0.295993503), (1.1629221153, 0.295993503))
                CenterArc((0, 0), 0.9, -19.2009114735, 38.401822947)
                Line((0.8499340246, -0.295993503), (1.1629221153, -0.295993503))
                CenterArc((0, 0), 1.2, -14.2800298656, 28.5600597312)
            make_face()
        # Symmetric extrude, each_side=0.5
        extrude(amount=0.5, both=True)
    return part.part


def model_40052_42bdc982_0018():
    """Model: RearAxis"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 11.3411494795, perimeter: 11.9380520836
            Circle(1.9)
        # Symmetric extrude, each_side=72
        extrude(amount=72, both=True)
    return part.part


def model_40052_42bdc982_0022():
    """Model: WheelJoint"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 14 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 141.8367374377, perimeter: 84.8772070221
            with BuildLine():
                Line((-3.7250495959, -6.9573968259), (-8, -3.4106158457))
                CenterArc((0, -5.5), 4, -158.6324627483, 137.2649254965)
                Line((3.7250495959, -6.9573968259), (8, -3.4106158457))
                Line((8, -3.4106158457), (16, -2))
                Line((16, -2), (16, 0))
                Line((16, 0), (-16, 0))
                Line((-16, -2), (-16, 0))
                Line((-8, -3.4106158457), (-16, -2))
            make_face()
            with BuildLine():
                CenterArc((0, -5.5), 1.9, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=1.6
        extrude(amount=1.6, both=True)
    return part.part


def model_40061_d07e8764_0007():
    """Model: Mounting_b_1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 16.4933614313, perimeter: 21.9911485751
            with BuildLine():
                CenterArc((0, 0), 2.5, 36.8698976458, 323.1301023542)
                CenterArc((0, 0), 2.5, 0, 36.8698976458)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=1.5
        extrude(amount=1.5, both=True)
    return part.part


def model_40061_d07e8764_0012():
    """Model: Muzzle_brake"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 10 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 28.2743338823, perimeter: 56.5486677646
            with BuildLine():
                CenterArc((0, 0), 5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


def model_40061_d07e8764_0013():
    """Model: Mounting_a_2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 20 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 9.4247779608, perimeter: 18.8495559215
            with BuildLine():
                CenterArc((0, 0), 2, -180, 323.1301023542)
                CenterArc((0, 0), 2, 143.1301023542, 36.8698976458)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=1.5
        extrude(amount=1.5, both=True)
    return part.part


def model_40070_be9c502b_0009():
    """Model: WYLOT v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.070685831, perimeter: 2.827433407
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.200000003, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1256637099, perimeter: 1.2566370802
            Circle(0.200000003)
        # OneSide extrude, distance=0.55
        extrude(amount=0.55)
    return part.part


def model_40070_be9c502b_0061():
    """Model: opony v3 (4)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.0995574625, perimeter: 4.3982297712
            with BuildLine():
                CenterArc((0, 0), 0.6000000089, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)
    return part.part


def model_40074_4615c9d1_0016():
    """Model: od zarowki1 v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.6211275016, perimeter: 10.9955742876
            Circle(1.75)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_40176_01ed49ea_0000():
    """Model: Component5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.9676890771, perimeter: 3.4871678455
            Circle(0.555)
        # OneSide extrude, distance=9.89
        extrude(amount=9.89)
    return part.part


def model_40176_01ed49ea_0001():
    """Model: Component8"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 22 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.6163553815, perimeter: 7.1316234239
            with BuildLine():
                Line((0.9313450052, 1.8460890317), (1.0554221117, 1.9701661381))
                Line((1.0554221117, 1.9701661381), (1.058, 3.0409368657))
                Line((1.058, 3.0409368657), (1.058, 3.2579894008))
                CenterArc((-0.3108577588, 3.2234590895), 1.3692932141, 1.4450161866, 75.4332589497)
                Line((0, 4.557), (0, 1.714))
                Line((0.875, 1.714), (0, 1.714))
                CenterArc((1.058, 1.714), 0.183, 133.7968742037, 46.2031257963)
            make_face()
            # Profile area: 1.3596157655, perimeter: 6.6917729581
            with BuildLine():
                Line((0.875, 1.714), (0, 1.714))
                Line((0, 1.714), (0, 0))
                Line((0, 0), (0.875, 0))
                Line((0.875, 0), (0.875, 1.714))
            make_face()
            with BuildLine():
                Line((0.5625, 0.6749063013), (0.5625, 1.0390936987))
                CenterArc((0.4375, 0.6749063013), 0.125, 180, 180)
                Line((0.3125, 1.0390936987), (0.3125, 0.6749063013))
                CenterArc((0.4375, 1.0390936987), 0.125, 0, 180)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.064
        extrude(amount=0.064)
    return part.part


def model_40176_01ed49ea_0002():
    """Model: Component26"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 15 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.6720463285, perimeter: 9.0735573631
            with BuildLine():
                Line((1, 0.7), (1.7595724803, 0.8))
                Line((0, 0.7), (1, 0.7))
                Line((0, 0.7), (0, 0.1))
                Line((0, 0.1), (1, 0.1))
                Line((1, 0.1), (1.68, 0))
                Line((2.0300679551, 0.3500679551), (1.68, 0))
                Line((2.9000679551, 0.3500679551), (2.0300679551, 0.3500679551))
                Line((3.35, 0.8), (2.9000679551, 0.3500679551))
                Line((3.35, 0.8), (1.7595724803, 0.8))
            make_face()
            with BuildLine():
                Line((0.600000003, 0.500000006), (0.200000003, 0.500000006))
                CenterArc((0.600000003, 0.400000006), 0.1, -90, 180)
                Line((0.200000003, 0.300000006), (0.600000003, 0.300000006))
                CenterArc((0.200000003, 0.400000006), 0.1, 90, 180)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.064
        extrude(amount=0.064)
    return part.part


def model_40176_01ed49ea_0004():
    """Model: Component2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 23 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.0924612939, perimeter: 6.9566370614
            with BuildLine():
                Line((0.035, -0.8625), (0.035, -2.4375))
                Line((0.035, -2.4375), (0.91, -2.4375))
                Line((0.91, -2.4375), (0.91, -0.8624999358))
                Line((0.91, -0.8624999358), (0.035, -0.8625))
            make_face()
            with BuildLine():
                Line((0.6665538073, -1.9375), (0.6665538073, -1.5375))
                CenterArc((0.4665538073, -1.9375), 0.2, 180, 180)
                Line((0.2665538073, -1.5375), (0.2665538073, -1.9375))
                CenterArc((0.4665538073, -1.5375), 0.2, 0, 180)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 2.1736566602, perimeter: 6.6105516831
            with BuildLine():
                CenterArc((0, -0.8625), 0.035, 0, 90)
                Line((0.91, -0.8624999358), (0.035, -0.8625))
                CenterArc((0.945, -0.8624999358), 0.035, 90, 90)
                Line((0.945, -0.8274999358), (0.945, 1.1669039956))
                Line((0, 1.7125), (0.945, 1.1669039956))
                Line((0, 1.7125), (0, -0.8275))
            make_face()
        # OneSide extrude, distance=0.064
        extrude(amount=0.064)
    return part.part


def model_40341_9514acd7_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 27.7931894616, perimeter: 36.75004416
            with BuildLine():
                CenterArc((5.5, 0.5), 0.5, -90, 180)
                Line((5.5, 1), (5.5, 6.6))
                CenterArc((4.9, 6.35), 0.65, 22.619864948, 134.7602701039)
                Line((4.3, 6.6), (4.3, 5))
                Line((4.3, 5), (2, 5))
                CenterArc((2, 3), 2, 90, 90)
                Line((0, 3), (0, 1))
                CenterArc((0, 0.5), 0.5, 90, 180)
                Line((0, 0), (5.5, 0))
            make_face()
            with BuildLine():
                CenterArc((3.7, 4.4), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.1, 4.4), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.1000000164, 0.5000000075), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.7, 0.5), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.9, 6), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0.5), 0.45, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.5, 0.5), 0.45, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


def model_40352_a9774a3f_0009():
    """Model: mediumSpacer"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.238125, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1711138489, perimeter: 3.3474612202
            with BuildLine():
                CenterArc((3.048, 5.588), 0.3175, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((3.048, 5.588), 0.215265, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1455783255, perimeter: 1.3525498852
            with Locations((3.048, 5.588)):
                Circle(0.215265)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


def model_40413_c590b4b4_0000():
    """Model: Aluminum Tube v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.9500765233, perimeter: 11.9694680102
            with BuildLine():
                CenterArc((0, 0), 1.031875, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.873125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=15.5194
        extrude(amount=15.5194)
    return part.part


def model_40413_c590b4b4_0002():
    """Model: Rod v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2634878891, perimeter: 4.1494155769
            with BuildLine():
                CenterArc((0, 0), 0.3937, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2667, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=15.24
        extrude(amount=15.24)
    return part.part


def model_40417_b8d98f73_0009():
    """Model: Component9"""
    with BuildPart() as part:
        # Sketch3 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.5446900494, perimeter: 5.6548667765
            Circle(0.9)
        # OneSide extrude, distance=3.2
        extrude(amount=3.2)
    return part.part


def model_40491_ac67bf4c_0000():
    """Model: Broad blade"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.1089830129, perimeter: 24.630527401
            with BuildLine():
                CenterArc((2, 24.5), 25, -106.2602047083, 16.2602047083)
                Line((5.5, -0.5), (2, -0.5))
                Line((5.5, -0.3), (5.5, -0.5))
                Line((7, -0.3), (5.5, -0.3))
                Line((7, -0.2), (7, -0.3))
                Line((5.5, -0.2), (7, -0.2))
                Line((5.5, 0), (5.5, -0.2))
                Line((4, 0), (5.5, 0))
                CenterArc((4.1736997744, 22.0632979698), 22.0639817103, -102.2293150078, 11.7782465238)
                Line((-5, 0.5), (-0.5, 0.5))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


def model_40491_ac67bf4c_0004():
    """Model: Broad handle spacer"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 10 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0371238912, perimeter: 1.1932719913
            with BuildLine():
                EllipticalCenterArc((0, 0), 0.1500000022, 0.1000000015, 0, 360, 0)
            make_face()
            with BuildLine():
                Line((-0.05, -0.05), (0.05, -0.05))
                Line((-0.05, 0.05), (-0.05, -0.05))
                Line((0.05, 0.05), (-0.05, 0.05))
                Line((0.05, -0.05), (0.05, 0.05))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


def model_40491_ac67bf4c_0008():
    """Model: Straight guard"""
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
        # Sketch has 11 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0853302216, perimeter: 1.2359802916
            with BuildLine():
                Line((5.0301801824, -0.7981894958), (5.0301801824, -0.698189498))
                CenterArc((5.0429133383, -0.5205027489), 0.2779785292, -92.6254238535, 64.1144324905)
                Line((5.2871801771, -0.6531895007), (5.2871801771, -0.5031895007))
                CenterArc((5.0429133383, -0.6358762526), 0.2779785292, 28.510991363, 64.1144324905)
                Line((5.0301801824, -0.3581895056), (5.0301801824, -0.4581895034))
                _nurbs_edge([(5.0301801824, -0.4581895034), (5.0318183149, -0.4592504355), (5.0350198718, -0.4614916593), (5.0395980816, -0.4652115759), (5.0452467469, -0.4708993909), (5.0514980338, -0.4793025536), (5.0568727507, -0.4891061949), (5.0613076058, -0.5004114351), (5.0647834343, -0.5132488933), (5.0673541154, -0.5275324877), (5.0690949271, -0.543141948), (5.0698815258, -0.5565977917), (5.0701527624, -0.5671988749), (5.0701942637, -0.5744888577), (5.0701801815, -0.5781895007)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(5.0301801824, -0.698189498), (5.0318183149, -0.697128566), (5.0350198718, -0.6948873422), (5.0395980816, -0.6911674255), (5.0452467469, -0.6854796105), (5.0514980338, -0.6770764478), (5.0568727507, -0.6672728065), (5.0613076058, -0.6559675663), (5.0647834343, -0.6431301082), (5.0673541154, -0.6288465138), (5.0690949271, -0.6132370534), (5.0698815258, -0.5997812098), (5.0701527624, -0.5891801266), (5.0701942637, -0.5818901438), (5.0701801815, -0.5781895007)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


def model_40491_ac67bf4c_0012():
    """Model: Screw (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0066967582, perimeter: 0.5034897865
            with BuildLine():
                Line((0.0288675128, 0.0499999989), (-0.0288675128, 0.0499999989))
                Line((-0.0288675128, 0.0499999989), (-0.0577350256, 0))
                Line((-0.0577350256, 0), (-0.0288675128, -0.0499999989))
                Line((-0.0288675128, -0.0499999989), (0.0288675128, -0.0499999989))
                Line((0.0288675128, -0.0499999989), (0.0577350256, 0))
                Line((0.0577350256, 0), (0.0288675128, 0.0499999989))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.025, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.04
        extrude(amount=0.04)
    return part.part


def model_40491_ac67bf4c_0015():
    """Model: Base suppport (1)"""
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
        # Sketch has 6 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.3220023336, perimeter: 4.0475105118
            with BuildLine():
                Line((0.9000000089, 0.3000000037), (0.9000000089, 0.5999999866))
                Line((0.9000000089, 0.5999999866), (0.7999999821, 0.5999999866))
                Line((0.7999999821, 0.5999999866), (0.8000000075, 0.3))
                Line((0.5000000075, 0.3), (0.8000000075, 0.3))
                Line((0.4999999888, 0.5999999866), (0.5000000075, 0.3))
                Line((0.400000006, 0.5999999866), (0.4999999888, 0.5999999866))
                Line((0.400000006, 0.3), (0.400000006, 0.5999999866))
                _nurbs_edge([(0.400000006, 0.3), (0.399294362, 0.2939140178), (0.3972913389, 0.2820311792), (0.3925115515, 0.2650743232), (0.3825625919, 0.2442123867), (0.3640994579, 0.2210762353), (0.3396909777, 0.2008306355), (0.3097106208, 0.1832715796), (0.2750504584, 0.1679259481), (0.2371711847, 0.1540266549), (0.1978150124, 0.1406611154), (0.1588148104, 0.1268707987), (0.1218722264, 0.1117673439), (0.0883560545, 0.0946387356), (0.059055818, 0.0750797816), (0.0343321358, 0.0529110084), (0.0182891447, 0.0330556853), (0.0083402314, 0.0169836363), (0.0026268695, 0.0057480298), (0, 0)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9333333333, 1, 1, 1, 1, 1, 1], 5)
                Line((0, 0), (1.3000000194, 0.0000000097))
                _nurbs_edge([(0.9000000089, 0.3000000037), (0.900705653, 0.2939140215), (0.9027086762, 0.2820311829), (0.9074884639, 0.2650743271), (0.9174374239, 0.2442123907), (0.9359005582, 0.2210762396), (0.9603090387, 0.2008306401), (0.9902893959, 0.1832715847), (1.0249495584, 0.1679259537), (1.0628288323, 0.1540266611), (1.1021850049, 0.1406611222), (1.1411852071, 0.1268708061), (1.1781277913, 0.1117673517), (1.2116439635, 0.094638744), (1.2409442003, 0.0750797904), (1.2656678828, 0.0529110176), (1.2817108742, 0.0330556947), (1.2916597877, 0.0169836458), (1.2973731497, 0.0057480395), (1.3000000194, 0.0000000097)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9333333333, 1, 1, 1, 1, 1, 1], 5)
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


def model_40491_ac67bf4c_0019():
    """Model: Blade rack"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 19 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1242520181, perimeter: 2.3969598786
            with BuildLine():
                Line((-2.8831413582, 1.2283823611), (-3.2626149254, 1.7297329457))
                Line((-2.8074510969, 1.1283823611), (-2.8831413582, 1.2283823611))
                Line((-2.6574049112, 1.2419527111), (-2.8074510969, 1.1283823611))
                Line((-3.1125687397, 1.8433032957), (-2.6574049112, 1.2419527111))
                Line((-3.1875918326, 1.7865181207), (-3.1125687397, 1.8433032957))
                Line((-3.1875918326, 1.7865181207), (-3.1628555788, 1.7538372271))
                CenterArc((-3.1175918326, 1.6940359455), 0.075, 0, 360)
                Line((-3.2626149254, 1.7297329457), (-3.1875918326, 1.7865181207))
            make_face()
            # Profile area: 0.0629230515, perimeter: 1.5714345864
            with BuildLine():
                CenterArc((-3.1175918326, 1.6940359455), 0.5213446898, -84.2772948709, 21.0019502265)
                Line((-3.0656064359, 1.0977528634), (-3.0656064359, 1.1752895681))
                Line((-3.1856064359, 1.0977528634), (-3.0656064359, 1.0977528634))
                Line((-3.1856064359, 1.1771468865), (-3.1856064359, 1.0977528634))
                CenterArc((-3.1175918326, 1.6940359455), 0.5213446898, -118.4863345124, 20.9901625112)
                Line((-3.366246735, 1.2358099914), (-3.4409106188, 1.1358099914))
                CenterArc((-3.1175918326, 1.6940359455), 0.6450978634, -120.0789856252, 58.8143893868)
                Line((-2.8074510969, 1.1283823611), (-2.8831413582, 1.2283823611))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


def model_40500_6055e3d7_0004():
    """Model: Konstrukcja stalowa pionowa v12"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 10 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4365.7310911366, perimeter: 1099.0718152403
            with BuildLine():
                Line((0, 0), (59, 0))
                Line((59, 0), (59, 30))
                Line((59, 30), (97.8603516352, 220.3880057326))
                Line((97.8603516352, 220.3880057326), (0, 200))
                Line((0, 0), (0, 200))
            make_face()
            with BuildLine():
                Line((51, 8), (8, 8))
                Line((8, 193.4949276956), (8, 8))
                Line((87.7630198673, 210.1125759988), (8, 193.4949276956))
                Line((51, 30), (87.7630198673, 210.1125759988))
                Line((51, 8), (51, 30))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=54
        extrude(amount=54)
    return part.part


def model_40500_6055e3d7_0006():
    """Model: konstrukcja ławeczki v12"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 10 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1536, perimeter: 400
            with BuildLine():
                Line((-46, 58), (18, 58))
                Line((-46, 78), (-46, 58))
                Line((-54, 78), (-46, 78))
                Line((-54, 0), (-54, 78))
                Line((-54, 0), (-46, 0))
                Line((-46, 0), (-46, 50))
                Line((10, 50), (-46, 50))
                Line((10, 0), (10, 50))
                Line((18, 0), (10, 0))
                Line((18, 58), (18, 0))
            make_face()
        # OneSide extrude, distance=8
        extrude(amount=8)
    return part.part


def model_40500_6055e3d7_0010():
    """Model: guma pod obciążenie v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.4247779608, perimeter: 18.8495559215
            with BuildLine():
                CenterArc((0, 0), 2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


def model_40500_6055e3d7_0011():
    """Model: belka pod ciężar v2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # OneSide extrude, distance=200
        extrude(amount=200)
    return part.part


def model_40500_6055e3d7_0012():
    """Model: na uda v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 240, perimeter: 92
            with BuildLine():
                Line((0, 40), (0, 0))
                Line((0, 0), (6, 0))
                Line((6, 0), (6, 40))
                Line((6, 40), (0, 40))
            make_face()
        # OneSide extrude, distance=6
        extrude(amount=6)
    return part.part


def model_40500_6055e3d7_0028():
    """Model: obiążenie v12 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 504, perimeter: 92
            with BuildLine():
                Line((14, -9), (14, 9))
                Line((14, 9), (-14, 9))
                Line((-14, 9), (-14, -9))
                Line((-14, -9), (14, -9))
            make_face()
        # OneSide extrude, distance=4
        extrude(amount=4)
    return part.part


def model_40500_6055e3d7_0030():
    """Model: gąbka udo v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 71.4712328692, perimeter: 40.8407044967
            with BuildLine():
                CenterArc((0, 0), 5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=20
        extrude(amount=20)
    return part.part


def model_40513_89770261_0005():
    """Model: shaft (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((3, -5)):
                Circle(0.2)
        # OneSide extrude, distance=0.775
        extrude(amount=0.775)
    return part.part


def model_40514_bb61631d_0017():
    """Model: balance_a"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.7902646384, perimeter: 19.6805298797
            with BuildLine():
                Line((0.6, 1.5), (0.6, 0))
                CenterArc((0, 1.5), 0.6, 0, 180)
                Line((-0.6, 1.5), (-0.6, 0))
                Line((-0.6, 0), (-2.5, 0))
                CenterArc((0, 0), 2.5, 180, 180)
                Line((0.6, 0), (2.5, 0))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 1.5), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)
    return part.part


def model_40514_bb61631d_0020():
    """Model: balance_b"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 11.9866141793, perimeter: 18.1097335529
            with BuildLine():
                Line((0.6, 1.5), (0.6, 0))
                CenterArc((0, 1.5), 0.6, 0, 180)
                Line((-0.6, 1.5), (-0.6, 0))
                Line((-0.6, 0), (-2.5, 0))
                CenterArc((0, 0), 2.5, 180, 180)
                Line((0.6, 0), (2.5, 0))
            make_face()
            with BuildLine():
                CenterArc((0, 1.5), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8)
    return part.part


def model_40514_bb61631d_0021():
    """Model: dowel_pin_M3x16"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=1.6
        extrude(amount=1.6)
    return part.part


def model_40514_bb61631d_0024():
    """Model: BASE"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 11 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 91.964011415, perimeter: 60.9487633629
            with BuildLine():
                Line((7, -4), (7, 4))
                Line((7, 4), (-7, 4))
                Line((-7, 4), (-7, -4))
                Line((-7, -4), (7, -4))
            make_face()
            with BuildLine():
                CenterArc((2.2, -2.85), 0.25, 177.1340160174, 185.7319679652)
                CenterArc((2.2, -0.35), 2.5, -174.2680320348, 78.5360640696)
                CenterArc((-0.3, -0.35), 0.25, 87.1340160174, 185.7319679652)
                CenterArc((2.2, -0.35), 2.5, 95.7319679652, 78.5360640696)
                CenterArc((2.2, 2.15), 0.25, -2.8659839826, 185.7319679652)
                CenterArc((2.2, -0.35), 2.5, 5.7319679652, 78.5360640696)
                CenterArc((4.7, -0.35), 0.25, -92.8659839826, 185.7319679652)
                CenterArc((2.2, -0.35), 2.5, -84.2680320348, 78.5360640696)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 19.2505904216, perimeter: 16.7486799357
            with BuildLine():
                CenterArc((2.2, -2.85), 0.25, 2.8659839826, 174.2680320348)
                CenterArc((2.2, -0.35), 2.5, -84.2680320348, 78.5360640696)
                CenterArc((4.7, -0.35), 0.25, 92.8659839826, 174.2680320348)
                CenterArc((2.2, -0.35), 2.5, 5.7319679652, 78.5360640696)
                CenterArc((2.2, 2.15), 0.25, -177.1340160174, 174.2680320348)
                CenterArc((2.2, -0.35), 2.5, 95.7319679652, 78.5360640696)
                CenterArc((-0.3, -0.35), 0.25, -87.1340160174, 174.2680320348)
                CenterArc((2.2, -0.35), 2.5, -174.2680320348, 78.5360640696)
            make_face()
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)
    return part.part


def model_40519_55a097c6_0003():
    """Model: Trigger v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.0163178406, perimeter: 23.8528027196
            with BuildLine():
                CenterArc((1.2725845904, 4.1757679338), 6.7095, -82.1479801382, 43.6588256697)
                CenterArc((0.0000961472, -1.566), 6.7095, 13.4973507135, 43.6588256697)
                Line((2.8884830428, 3.7971762367), (3.639, 4.071))
                CenterArc((2.239, 1.494), 2.393, -25.3262936768, 99.578133421)
                CenterArc((2.0090407786, 0.4563697641), 2.393, -99.2436434993, 99.578133421)
                Line((1.6246458531, -1.9055552011), (2.1892031613, -2.470825227))
            make_face()
            with BuildLine():
                CenterArc((5.433284545, 0.2417870084), 0.5907722235, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.1
        extrude(amount=2.1)
    return part.part


def model_40519_55a097c6_0007():
    """Model: Fisrt Step Pad v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 38.1624967595, perimeter: 35.4999969856
            with BuildLine():
                CenterArc((0, 0), 3.9, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


def model_40519_55a097c6_0009():
    """Model: Parallel Key 7x8x22 v2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 18 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.5596566371, perimeter: 2.9656637061
            with BuildLine():
                CenterArc((0.38, -0.33), 0.02, -90, 90)
                Line((0.4, -0.33), (0.4, 0.33))
                CenterArc((0.38, 0.33), 0.02, 0, 90)
                Line((0.38, 0.35), (-0.38, 0.35))
                CenterArc((-0.38, 0.33), 0.02, 90, 90)
                Line((-0.4, 0.33), (-0.4, -0.33))
                CenterArc((-0.38, -0.33), 0.02, 180, 90)
                Line((-0.38, -0.35), (0.38, -0.35))
            make_face()
        # OneSide extrude, distance=2.2
        extrude(amount=2.2)
    return part.part


def model_40519_55a097c6_0011():
    """Model: Second Step Pad v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 46.2442438608, perimeter: 57.8053048261
            with BuildLine():
                CenterArc((0, 0), 5.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


def model_40519_55a097c6_0012():
    """Model: First step Puck v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 16.7682507885, perimeter: 19.1637151869
            with BuildLine():
                CenterArc((0, 0), 2.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.65, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.9
        extrude(amount=1.9)
    return part.part


def model_40519_55a097c6_0013():
    """Model: Trigger Pad v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.5814156251, perimeter: 11.9380520836
            with BuildLine():
                CenterArc((0, 0), 1.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.65, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.14
        extrude(amount=0.14)
    return part.part


def model_40519_55a097c6_0014():
    """Model: Gearshift Pad v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.2708234977, perimeter: 25.2898208614
            with BuildLine():
                CenterArc((0, 0), 2.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.725, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.14
        extrude(amount=0.14)
    return part.part


def model_40519_55a097c6_0016():
    """Model: Secon Step Puck v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 21.9911485751, perimeter: 43.9822971503
            with BuildLine():
                CenterArc((0, 0), 4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


def model_40586_86bc7430_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 29.548328, perimeter: 42.164
            with BuildLine():
                Line((0, 1.778), (0, 0))
                Line((0, 0), (17.018, 0))
                Line((17.018, 0), (17.018, 0.508))
                Line((17.018, 0.508), (18.796, 0.508))
                Line((18.796, 0.508), (18.796, 1.778))
                Line((18.796, 1.778), (7.874, 1.778))
                Line((7.874, 1.778), (7.874, 1.27))
                Line((7.874, 1.27), (2.032, 1.27))
                Line((2.032, 1.27), (2.032, 1.778))
                Line((2.032, 1.778), (0, 1.778))
            make_face()
        # OneSide extrude, distance=2.032
        extrude(amount=2.032)
    return part.part


def model_40624_e1c5c424_0000():
    """Model: Belka II"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4552.3214359463, perimeter: 625.1217873622
            with BuildLine():
                Line((0, 0), (-132.7905619136, -230))
                Line((-132.7905619136, -230), (-112.7905619136, -230))
                Line((-112.7905619136, -230), (-48.2355715851, -118.187476869))
                Line((-55, -120), (-48.2355715851, -118.187476869))
                Line((-55, -110), (-55, -120))
                Line((-55, -110), (-45.0480947162, -112.666604984))
                Line((-45.0480947162, -112.666604984), (20, 0))
                Line((12.5, 0), (20, 0))
                Line((16.8301270189, 7.5), (12.5, 0))
                Line((11.8301270189, 7.5), (16.8301270189, 7.5))
                Line((7.5, 0), (11.8301270189, 7.5))
                Line((0, 0), (7.5, 0))
            make_face()
            with BuildLine():
                CenterArc((-120, -227), 2.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=20
        extrude(amount=20)
    return part.part


def model_40624_e1c5c424_0001():
    """Model: Belka I"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 24 constraints, 17 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1086.223229311, perimeter: 242.2834075116
            with BuildLine():
                Line((52.5, 0), (60, 0))
                Line((60, 0), (48.4529946162, 20))
                Line((48.4529946162, 20), (40, 20))
                Line((40, 20), (42.0096189432, 12.5))
                Line((17.9903810568, 12.5), (42.0096189432, 12.5))
                Line((20, 20), (17.9903810568, 12.5))
                Line((20, 20), (11.5470053838, 20))
                Line((0, 0), (11.5470053838, 20))
                Line((0, 0), (7.5, 0))
                Line((7.5, 0), (11.8301270189, 7.5))
                Line((11.8301270189, 7.5), (16.8301270189, 7.5))
                Line((16.8301270189, 7.5), (12.5, 0))
                Line((12.5, 0), (20, 0))
                Line((20, 0), (12.5, -12.9903810568))
                Line((12.5, -12.9903810568), (47.5, -12.9903810568))
                Line((40, 0), (47.5, -12.9903810568))
                Line((40, 0), (47.5, 0))
                Line((43.1698729811, 7.5), (47.5, 0))
                Line((48.1698729811, 7.5), (43.1698729811, 7.5))
                Line((52.5, 0), (48.1698729811, 7.5))
            make_face()
        # OneSide extrude, distance=20
        extrude(amount=20)
    return part.part


def model_40624_e1c5c424_0003():
    """Model: Rorka ustalajaca"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            with Locations((-125, -240)):
                Circle(2.5)
        # OneSide extrude, distance=296
        extrude(amount=296)
    return part.part


def model_40624_e1c5c424_0004():
    """Model: Belka III"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3186.8984582098, perimeter: 393.6312820905
            with BuildLine():
                Line((115, -110), (105.0480947162, -112.666604984))
                Line((100.6217782649, -105), (105.0480947162, -112.666604984))
                Line((100.6217782649, -105), (-40.6217782649, -105))
                Line((-40.6217782649, -105), (-45.0480947162, -112.666604984))
                Line((-55, -110), (-45.0480947162, -112.666604984))
                Line((-55, -110), (-55, -120))
                Line((-55, -120), (-48.2355715851, -118.187476869))
                Line((-48.2355715851, -118.187476869), (-52.1687836487, -125))
                Line((-52.1687836487, -125), (112.1687836487, -125))
                Line((108.2355715851, -118.187476869), (112.1687836487, -125))
                Line((115, -120), (108.2355715851, -118.187476869))
                Line((115, -110), (115, -120))
            make_face()
        # OneSide extrude, distance=20
        extrude(amount=20)
    return part.part


def model_40624_e1c5c424_0006():
    """Model: Deska stojak"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 456.0342917353, perimeter: 102.4203522483
            with BuildLine():
                CenterArc((191.5, -12.5), 2.5, -180, 90)
                Line((191.5, -15), (217.5, -15))
                CenterArc((217.5, -12.5), 2.5, -90, 90)
                Line((220, -12.5), (220, 0))
                Line((220, 0), (189, 0))
                Line((189, 0), (189, -12.5))
            make_face()
            with BuildLine():
                CenterArc((217, -7.5), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((192, -7.5), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=4
        extrude(amount=4)
    return part.part


def model_40624_e1c5c424_0007():
    """Model: Drazek chwyt"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 16.8393589724, perimeter: 15.0714871779
            with BuildLine():
                CenterArc((25, -225), 2.5, -36.8698976458, 253.7397952917)
                Line((23, -226.5), (27, -226.5))
            make_face()
        # OneSide extrude, distance=106
        extrude(amount=106)
    return part.part


def model_40624_e1c5c424_0008():
    """Model: Raczka drazek"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 6.0621692301, perimeter: 9.0428923068
            with BuildLine():
                CenterArc((105, 100), 1.5, -36.8698976458, 253.7397952917)
                Line((106.2, 99.1), (103.8, 99.1))
            make_face()
        # OneSide extrude, distance=39
        extrude(amount=39)
    return part.part


def model_40624_e1c5c424_0010():
    """Model: Siodelko"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 16 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 708.8672587713, perimeter: 153.9822971503
            with BuildLine():
                CenterArc((-74, 14), 1, 90, 90)
                Line((-75, -25), (-75, 14))
                CenterArc((-74, -25), 1, 180, 90)
                Line((-58, -26), (-74, -26))
                CenterArc((-58, -25), 1, -90, 90)
                Line((-57, 14), (-57, -25))
                CenterArc((-58, 14), 1, 0, 90)
                Line((-74, 15), (-58, 15))
            make_face()
            with BuildLine():
                CenterArc((-72, 9), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-60, 9), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-60, -20), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-72, -20), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 3.926990817, perimeter: 15.7079632679
            with BuildLine():
                CenterArc((-60, 9), 1.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-60, 9), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 3.926990817, perimeter: 15.7079632679
            with BuildLine():
                CenterArc((-72, 9), 1.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-72, 9), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 3.926990817, perimeter: 15.7079632679
            with BuildLine():
                CenterArc((-60, -20), 1.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-60, -20), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 3.926990817, perimeter: 15.7079632679
            with BuildLine():
                CenterArc((-72, -20), 1.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-72, -20), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=4
        extrude(amount=4)
    return part.part


def model_40624_e1c5c424_0011():
    """Model: Sruba I"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with Locations((-140, -240)):
                Circle(0.75)
        # OneSide extrude, distance=7
        extrude(amount=7)
    return part.part


def model_40624_e1c5c424_0012():
    """Model: Kun"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 110 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4604.2788916653, perimeter: 711.5048702157
            with BuildLine():
                CenterArc((20, -165.0000024959), 2.5, 90, 126.8699690826)
                Line((20, -147.0856878724), (20, -162.5000024959))
                Line((16.2541555717, -147.0856878724), (20, -147.0856878724))
                Line((16.2541555717, -136.3236570262), (16.2541555717, -147.0856878724))
                CenterArc((13.2541555717, -136.3236570262), 3, 0, 44.8476086107)
                Line((7.91437741, -126.7014281555), (15.3811105478, -134.2079863218))
                Line((5.9656736436, -111.2736938555), (7.91437741, -126.7014281555))
                CenterArc((2.9893230075, -111.6496418452), 3, 7.1990045429, 82.8009954571)
                Line((-12.5400557114, -108.6496418452), (2.9893230075, -108.6496418452))
                CenterArc((-12.5400557114, -105.6496418452), 3, -126.0349077408, 36.0349077408)
                Line((-20.9719575713, -103.2255009483), (-14.3048898339, -108.0756180446))
                Line((-20.9719575713, -103.2255009483), (-18.6243648506, -112.9512422198))
                Line((-33.053312852, -132.5366067135), (-18.6243648506, -112.9512422198))
                CenterArc((-30.6380055811, -134.3160141394), 3, 143.6201480884, 92.4904242127)
                Line((-27.6311996049, -139.9496549455), (-32.3107814143, -136.8063597002))
                Line((-27.6311996049, -139.9496549455), (-25, -134))
                Line((-25, -134), (-25, -140.302093913))
                CenterArc((-25.9584237717, -137.4593093848), 3, -71.3688466667, 29.5687780335)
                Line((-17.5, -132.5), (-23.7219981679, -139.4589094745))
                Line((-16.2781659254, -131.9414785002), (-17.5, -132.5))
                CenterArc((-15.0309443105, -134.6699282877), 3, 0, 114.5659603658)
                Line((-12.0309443105, -140.4423359465), (-12.0309443105, -134.6699282877))
                CenterArc((-15.0309443105, -140.4423359465), 3, -20.5760412539, 20.5760412539)
                Line((-12.2223245716, -141.4966865343), (-14.7214070381, -148.1538387434))
                CenterArc((-13.7852004585, -148.5052889393), 1, 159.4239587461, 54.7804179921)
                Line((-14.6122380936, -149.0674354949), (-13.1315498125, -151.2458441717))
                CenterArc((-14.555862815, -152.3464496736), 1.8, -52.3057595333, 90)
                Line((-31.9643166977, -168.0732176552), (-13.455257313, -153.7707626761))
                CenterArc((-30.8637111957, -169.4975306577), 1.8, 127.6942404667, 90)
                Line((-20.2607548234, -186.1628377035), (-32.2880241982, -170.5981361596))
                Line((-15, -185), (-20.2607548234, -186.1628377035))
                Line((-15, -179.7796461965), (-15, -185))
                Line((-18.0386118981, -179.7796461965), (-15, -179.7796461965))
                Line((-23.5454141757, -172.4929803817), (-18.0386118981, -179.7796461965))
                CenterArc((-22.109378262, -171.4077150434), 1.8, 127.079687324, 90)
                Line((-11.1737557256, -160.8870505204), (-23.1946436003, -169.9716791297))
                CenterArc((-10.0884903873, -162.3230864342), 1.8, 48.5574309828, 78.5222563412)
                Line((-5.9355742972, -163.5886436303), (-8.897126201, -160.9737712836))
                CenterArc((-7.1269384835, -164.9379587809), 1.8, -4.2558271518, 52.8132581346)
                Line((-7.5872405603, -195.3790786289), (-5.3319017263, -165.0715366245))
                Line((-8.2025768955, -198.9172645941), (-7.5872405603, -195.3790786289))
                Line((-2.3285707937, -198.9172645941), (-8.2025768955, -198.9172645941))
                Line((2.2211758886, -172.7562061042), (-2.3285707937, -198.9172645941))
                CenterArc((3.9945570772, -173.0646200464), 1.8, 80.1341986273, 90)
                Line((4.3029710194, -171.2912388577), (34.3507677362, -171.3756654287))
                CenterArc((34.6028384676, -173.1579281328), 1.8, 77.6194984712, 20.4306216254)
                Line((44.6925710698, -173.5298452984), (34.9887637613, -171.3997865948))
                CenterArc((44.3066457762, -175.2879868365), 1.8, 0, 77.6194984712)
                Line((46.1066457762, -193.6790500113), (46.1066457762, -175.2879868365))
                Line((44.9104748516, -199.1283891024), (46.1066457762, -193.6790500113))
                Line((51.8190675186, -199.1283891024), (44.9104748516, -199.1283891024))
                Line((53.3666520509, -192.0781317225), (51.8190675186, -199.1283891024))
                Line((57.5844123494, -172.22437526), (53.3666520509, -192.0781317225))
                CenterArc((59.3451192476, -172.5984223411), 1.8, 96.719298239, 71.2870136345)
                Line((62.3506433631, -170.4318789018), (59.1345098011, -170.8107860075))
                CenterArc((62.5612528095, -172.2195152353), 1.8, 30.6610714106, 66.0582268284)
                Line((70.8915097099, -182.7413073473), (64.1096109237, -171.3015897753))
                CenterArc((69.3431515957, -183.6592328074), 1.8, 6.719298239, 23.9417731716)
                Line((72.7806463329, -197.4524910742), (71.1307879293, -183.4486233609))
                CenterArc((70.9930099993, -197.6631005206), 1.8, -23.8084261898, 30.5277244288)
                Line((71.0285691615, -202.0414882705), (72.6398305585, -198.3897242512))
                Line((78.5813209689, -202.0414882705), (71.0285691615, -202.0414882705))
                Line((79.165094644, -200.7184231824), (78.5813209689, -202.0414882705))
                CenterArc((76.328903681, -199.4670156464), 3.1, -23.8084261898, 23.8084261898)
                Line((79.428903681, -183.3549374695), (79.428903681, -199.4670156464))
                CenterArc((76.328903681, -183.3549374695), 3.1, 0, 66.1915738102)
                Line((78.4507850758, -180.9028241518), (77.5803112169, -180.5187465065))
                CenterArc((79.7021926118, -178.0666331888), 3.1, -159.7242567829, 45.915830593)
                Line((75.1804850334, -174.7725602787), (76.7942818504, -179.1409027097))
                CenterArc((78.0883957948, -173.6982907577), 3.1, 156.1915738102, 44.084169407)
                Line((78.3694223358, -165.38201917), (75.2522048317, -172.4468832218))
                CenterArc((81.2056132988, -166.633426706), 3.1, 134.8476086107, 21.3439651995)
                Line((87.671479318, -155.8294164787), (79.0194202376, -164.4355732306))
                CenterArc((85.4852862568, -153.6315630034), 3.1, -45.1523913893, 45.1523913893)
                Line((88.5852862568, -153.4818713571), (88.5852862568, -153.6315630034))
                CenterArc((85.4852862568, -153.4818713571), 3.1, 0, 44.8476086107)
                Line((72.4681080787, -135.9994948112), (87.6831397321, -151.2956782958))
                CenterArc((70.2702546033, -138.1856878724), 3.1, 44.8476086107, 45.1523913893)
                Line((64.2541555717, -135.0856878724), (70.2702546033, -135.0856878724))
                CenterArc((64.2541555717, -138.0856878724), 3, 90, 90)
                Line((61.2541555717, -147.0856878724), (61.2541555717, -138.0856878724))
                Line((20, -147.0856878724), (61.2541555717, -147.0856878724))
                CenterArc((20, -165.0000024959), 2.5, -36.8699691853, 126.8699691853)
                Line((18.0000018702, -166.5000049896), (21.9999981271, -166.5000049931))
            make_face()
            with BuildLine():
                Line((47, -166.5), (43, -166.5))
                CenterArc((45, -165), 2.5, -36.8698976458, 253.7397952917)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-2, -146.5), (2, -146.5))
                CenterArc((0, -145), 2.5, -36.8698976458, 253.7397952917)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((68, -146.5), (72, -146.5))
                CenterArc((70, -145), 2.5, -36.8698976458, 253.7397952917)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((1.7893230075, -112.5496418452), (4.1893230075, -112.5496418452))
                CenterArc((2.9893230075, -111.6496418452), 1.5, -36.8698976458, 253.7397952917)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=20
        extrude(amount=20)
    return part.part


def model_40624_e1c5c424_0013():
    """Model: Chwyt kunia"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 11 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2117.6788486357, perimeter: 737.3471979566
            with BuildLine():
                Line((30, 13), (66.0994097163, -145.8862253883))
                CenterArc((70, -145), 4, -167.1995387981, 181.1095024518)
                Line((34, 17), (73.8826987664, -144.0384126198))
                CenterArc((30, 17), 4, 0, 180)
                Line((26, 17), (-3.9328307468, -144.2700395098))
                CenterArc((0, -145), 4, 169.4851638804, 181.1890814381)
                Line((30, 13), (3.9471319006, -145.6481896014))
            make_face()
            with BuildLine():
                Line((-2, -146.5), (2, -146.5))
                CenterArc((0, -145), 2.5, -36.8698976458, 253.7397952917)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((68, -146.5), (72, -146.5))
                CenterArc((70, -145), 2.5, -36.8698976458, 253.7397952917)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((30, 17), 2.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


def model_40624_e1c5c424_0014():
    """Model: Drazek"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            with Locations((-105, -240)):
                Circle(2.5)
        # OneSide extrude, distance=286
        extrude(amount=286)
    return part.part


def model_40624_e1c5c424_0015():
    """Model: Drazek stojaka"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 16.8393589724, perimeter: 15.0714871779
            with BuildLine():
                CenterArc((150, -220), 2.5, -36.8698976458, 253.7397952917)
                Line((148, -221.5), (152, -221.5))
            make_face()
        # OneSide extrude, distance=45
        extrude(amount=45)
    return part.part


def model_40624_e1c5c424_0016():
    """Model: Pianka na siodelko"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 989.1415926536, perimeter: 132.2831853072
            with BuildLine():
                CenterArc((-159, -34), 1, 180, 90)
                Line((-139, -35), (-159, -35))
                CenterArc((-139, -34), 1, -90, 90)
                Line((-138, 9), (-138, -34))
                CenterArc((-139, 9), 1, 0, 90)
                Line((-159, 10), (-139, 10))
                CenterArc((-159, 9), 1, 90, 90)
                Line((-160, -34), (-160, 9))
            make_face()
        # OneSide extrude, distance=7
        extrude(amount=7)
    return part.part


def model_40705_5ff43505_0040():
    """Model: Cylindrical Joint"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.3876104167, perimeter: 11.9380520836
            with BuildLine():
                CenterArc((0, 0), 1.15, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=2.5
        extrude(amount=2.5, both=True)
    return part.part


def model_40712_8e707290_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 19.2, perimeter: 18.4
            with BuildLine():
                Line((0, 3.2), (0, 0))
                Line((0, 0), (6, 0))
                Line((6, 0), (6, 3.2))
                Line((6, 3.2), (0, 3.2))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


def model_40723_f18d24a6_0004():
    """Model: Component12"""
    with BuildPart() as part:
        # Sketch8 -> Extrude5 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0506707511, perimeter: 0.7979645595
            with Locations((5.5880001783, 3.1750001013)):
                Circle(0.1270000041)
        # OneSide extrude, distance=-0.381
        extrude(amount=-0.381)
    return part.part


def model_40723_f18d24a6_0008():
    """Model: Component6"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY) as sk:
            # Profile area: 0.0758211544, perimeter: 0.9761130707
            with Locations((4.2815918204, -5.881730446)):
                Circle(0.1553532202)
        # TwoSides extrude, along=22.86, against=-2.54
        extrude(amount=22.86)
        extrude(sk.sketch, amount=-2.54)
    return part.part


def model_40782_3383cd58_0010():
    """Model: Lozysko v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.5079644737, perimeter: 7.5398223686
            with BuildLine():
                CenterArc((0, 0), 0.8, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


def model_40782_3383cd58_0013():
    """Model: Centrownik_nakretka v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 13 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.228002907, perimeter: 3.9956674574
            with BuildLine():
                Line((0.35, 0.045527727), (0.35, -0.3586174615))
                Line((0, 0.2476003212), (0.35, 0.045527727))
                Line((-0.35, 0.045527727), (0, 0.2476003212))
                Line((-0.35, -0.3586174615), (-0.35, 0.045527727))
                Line((0, -0.5606900557), (-0.35, -0.3586174615))
                Line((0.35, -0.3586174615), (0, -0.5606900557))
            make_face()
            with BuildLine():
                CenterArc((0, -0.1565448672), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


def model_40782_3383cd58_0018():
    """Model: Pokretlo_podkladka v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3985895679, perimeter: 4.5553093477
            with BuildLine():
                CenterArc((0, 0), 0.45, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.275, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.15
        extrude(amount=0.15)
    return part.part


def model_40782_3383cd58_0026():
    """Model: Belka - lezka v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 16 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.2663052779, perimeter: 6.4840704731
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 180)
                Line((-0.4, 0), (-0.4, -1.2))
                CenterArc((0, -1.2), 0.4, 180, 180)
                Line((0.4, -1.2), (0.4, 0))
            make_face()
            with BuildLine():
                CenterArc((0, -0.6000000089), 0.2500000037, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0000000106, perimeter: 0.0064642117
            with BuildLine():
                CenterArc((0, 0), 0.4, -90.2314827655, 0.462965531)
                CenterArc((0, -1.2), 0.8000048968, 89.8842595618, 0.2314808763)
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


def model_40887_454ffc48_0002():
    """Model: bushing_4x8x4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.3769911184, perimeter: 3.7699111843
            with BuildLine():
                CenterArc((2.2000000328, 8.0000001192), 0.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((2.2000000328, 8.0000001192), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4)
    return part.part


def model_40887_454ffc48_0005():
    """Model: bushing_3x4x8"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0549778714, perimeter: 2.1991148575
            with BuildLine():
                CenterArc((1.7000000253, 5.0000000745), 0.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((1.7000000253, 5.0000000745), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)
    return part.part


def model_40887_454ffc48_0011():
    """Model: shaft"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((8.5, 10)):
                Circle(0.2)
        # OneSide extrude, distance=2.35
        extrude(amount=2.35)
    return part.part


def model_40887_454ffc48_0013():
    """Model: washer_4mm"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.3769911184, perimeter: 3.7699111843
            with BuildLine():
                CenterArc((2.5000000373, 6.0000000894), 0.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((2.5000000373, 6.0000000894), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


def model_40887_454ffc48_0014():
    """Model: washer_3mm"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2120575041, perimeter: 2.8274333882
            with BuildLine():
                CenterArc((2.5000000373, 6.0000000894), 0.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((2.5000000373, 6.0000000894), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


def model_40887_454ffc48_0015():
    """Model: flywheel_shaft"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((4.0000000596, 5.500000082)):
                Circle(0.2)
        # OneSide extrude, distance=3.4
        extrude(amount=3.4)
    return part.part


def model_40939_0bedb1ea_0002():
    """Model: Camera case"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.9000000566, perimeter: 6.6000000983
            with BuildLine():
                Line((-0.3000000045, -1.5000000224), (-0.3000000045, -1.0000000149))
                Line((0.3000000045, -1.5000000224), (-0.3000000045, -1.5000000224))
                Line((0.3000000045, -1.0000000149), (0.3000000045, -1.5000000224))
                Line((0.400000006, -1.0000000149), (0.3000000045, -1.0000000149))
                Line((0.400000006, 1.0000000149), (0.400000006, -1.0000000149))
                Line((-0.400000006, 1.0000000149), (0.400000006, 1.0000000149))
                Line((-0.400000006, -1.0000000149), (-0.400000006, 1.0000000149))
                Line((-0.3000000045, -1.0000000149), (-0.400000006, -1.0000000149))
            make_face()
        # OneSide extrude, distance=0.333
        extrude(amount=0.333)
    return part.part


def model_40939_0bedb1ea_0004():
    """Model: rotor pin"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((4.70000007, -3.8500000574)):
                Circle(0.05)
        # OneSide extrude, distance=1.8
        extrude(amount=1.8)
    return part.part


def model_40939_0bedb1ea_0008():
    """Model: Body design"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.4289524388, perimeter: 13.9468563259
            with BuildLine():
                Line((1.25, 2), (-1.25, 2))
                CenterArc((-1.5, 2), 0.25, -90, 90)
                CenterArc((-4.3025000981, 0), 3.3040137409, -31.9824051748, 63.9648103496)
                CenterArc((-1.5, -2), 0.25, 0, 90)
                Line((-1.25, -2), (1.25, -2))
                CenterArc((1.5, -2), 0.25, 90, 90)
                CenterArc((4.3125000987, 0), 3.3125000838, 148.1092091003, 63.7815817995)
                CenterArc((1.5, 2), 0.25, 180, 90)
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_40939_0bedb1ea_0009():
    """Model: on button"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-0.7000000104, -1.7000000253)):
                Circle(0.2)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


def model_40939_0bedb1ea_0010():
    """Model: record button"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1500000045, perimeter: 1.6000000238
            with BuildLine():
                Line((0.5000000075, -1.5000000224), (1.0000000149, -1.5000000224))
                Line((0.5000000075, -1.8000000268), (0.5000000075, -1.5000000224))
                Line((1.0000000149, -1.8000000268), (0.5000000075, -1.8000000268))
                Line((1.0000000149, -1.5000000224), (1.0000000149, -1.8000000268))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


def model_40939_0bedb1ea_0011():
    """Model: battery box"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 1.6000000477, perimeter: 5.6000000834
            with BuildLine():
                Line((0.400000006, -1.0000000149), (0.400000006, 1.0000000149))
                Line((0.400000006, 1.0000000149), (-0.400000006, 1.0000000149))
                Line((-0.400000006, 1.0000000149), (-0.400000006, -1.0000000149))
                Line((-0.400000006, -1.0000000149), (0.400000006, -1.0000000149))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


def model_40999_cad6be09_0000():
    """Model: Seat connector 2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1090.3203672501, perimeter: 132.0799980164
            with BuildLine():
                Line((231.1399965286, 48.2599992752), (198.1199970245, 48.2599992752))
                Line((198.1199970245, 48.2599992752), (198.1199970245, 15.2399997711))
                Line((198.1199970245, 15.2399997711), (231.1399965286, 15.2399997711))
                Line((231.1399965286, 15.2399997711), (231.1399965286, 48.2599992752))
            make_face()
        # OneSide extrude, distance=20.32
        extrude(amount=20.32)
    return part.part


def model_40999_cad6be09_0002():
    """Model: Seat connector"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1090.3203672501, perimeter: 132.0799980164
            with BuildLine():
                Line((-195.5799970627, 203.1999969482), (-228.5999965668, 203.1999969482))
                Line((-228.5999965668, 203.1999969482), (-228.5999965668, 170.1799974442))
                Line((-228.5999965668, 170.1799974442), (-195.5799970627, 170.1799974442))
                Line((-195.5799970627, 170.1799974442), (-195.5799970627, 203.1999969482))
            make_face()
        # OneSide extrude, distance=35.56
        extrude(amount=35.56)
    return part.part


def model_40999_cad6be09_0003():
    """Model: Headrest"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 438.0124533344, perimeter: 83.1834072322
            with BuildLine():
                Line((68.57999897, 7.6199998856), (88.8999986649, 7.6199998856))
                CenterArc((68.8181239665, 12.382499814), 20.6388734424, -13.3414593034, 104.002535115)
                Line((68.57999897, 7.6199998856), (68.57999897, 33.0199995041))
            make_face()
        # OneSide extrude, distance=22.86
        extrude(amount=22.86)
    return part.part


def model_40999_cad6be09_0007():
    """Model: Door lock"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.067074791, perimeter: 7.9796453401
            with Locations((109.2199983597, 55.8799991608)):
                Circle(1.27)
        # OneSide extrude, distance=11.43
        extrude(amount=11.43)
    return part.part


MODELS = {
    "model_37599_faf701a1_0009": {"func": model_37599_faf701a1_0009, "volume": 17.3572994111, "area": 70.9999939711},
    "model_37605_e35cc4df_0001": {"func": model_37605_e35cc4df_0001, "volume": 2.4740042147, "area": 10.1316363078},
    "model_37605_e35cc4df_0007": {"func": model_37605_e35cc4df_0007, "volume": 4.0212387164, "area": 21.1115029617},
    "model_37605_e35cc4df_0009": {"func": model_37605_e35cc4df_0009, "volume": 23.4056591941, "area": 86.3246708083},
    "model_37605_e35cc4df_0010": {"func": model_37605_e35cc4df_0010, "volume": 2.8274333882, "area": 11.0741141039},
    "model_37605_e35cc4df_0011": {"func": model_37605_e35cc4df_0011, "volume": 0.2998691136, "area": 5.1524963528},
    "model_37605_e35cc4df_0013": {"func": model_37605_e35cc4df_0013, "volume": 24.0806977302, "area": 89.3085748547},
    "model_37615_8399c412_0004": {"func": model_37615_8399c412_0004, "volume": 0.4021238597, "area": 4.2725660089},
    "model_37619_ae810a8d_0001": {"func": model_37619_ae810a8d_0001, "volume": 374.4619024534, "area": 2588.9013619082},
    "model_37619_ae810a8d_0003": {"func": model_37619_ae810a8d_0003, "volume": 21.4926990817, "area": 47.0342917353},
    "model_37619_ae810a8d_0004": {"func": model_37619_ae810a8d_0004, "volume": 4778.7335512266, "area": 2513.8822013964},
    "model_37683_e2cca100_0008": {"func": model_37683_e2cca100_0008, "volume": 4.161551, "area": 85.9462},
    "model_37846_cde34fcd_0027": {"func": model_37846_cde34fcd_0027, "volume": 0.2547539325, "area": 4.0847430177},
    "model_37846_cde34fcd_0029": {"func": model_37846_cde34fcd_0029, "volume": 0.0502654825, "area": 0.7539822369},
    "model_37846_cde34fcd_0045": {"func": model_37846_cde34fcd_0045, "volume": 0.0280151273, "area": 1.4768051843},
    "model_37846_cde34fcd_0058": {"func": model_37846_cde34fcd_0058, "volume": 0.0150796447, "area": 0.3644247478},
    "model_37995_1cc61263_0001": {"func": model_37995_1cc61263_0001, "volume": 208.499993499, "area": 373.0380461116},
    "model_37995_1cc61263_0005": {"func": model_37995_1cc61263_0005, "volume": 917.675584, "area": 774.192},
    "model_37995_1cc61263_0006": {"func": model_37995_1cc61263_0006, "volume": 1835.351168, "area": 1496.7712},
    "model_37995_1cc61263_0009": {"func": model_37995_1cc61263_0009, "volume": 115.2055130746, "area": 153.7375218907},
    "model_37995_1cc61263_0010": {"func": model_37995_1cc61263_0010, "volume": 69.1233078448, "area": 99.4995533281},
    "model_37995_1cc61263_0012": {"func": model_37995_1cc61263_0012, "volume": 73.741788, "area": 116.1288},
    "model_38114_917ea77b_0001": {"func": model_38114_917ea77b_0001, "volume": 4.8275859652, "area": 55.1815123101},
    "model_38114_917ea77b_0006": {"func": model_38114_917ea77b_0006, "volume": 7.1628312502, "area": 76.4035333353},
    "model_38114_917ea77b_0007": {"func": model_38114_917ea77b_0007, "volume": 42.4115008235, "area": 183.783170235},
    "model_38198_7c60c095_0000": {"func": model_38198_7c60c095_0000, "volume": 0.0533819424, "area": 0.9801769079},
    "model_38198_7c60c095_0002": {"func": model_38198_7c60c095_0002, "volume": 16.3184969966, "area": 108.3181400942},
    "model_38198_7c60c095_0004": {"func": model_38198_7c60c095_0004, "volume": 8.1592484983, "area": 54.1590700471},
    "model_38198_7c60c095_0006": {"func": model_38198_7c60c095_0006, "volume": 1.970749125, "area": 25.3469322326},
    "model_38260_2a31c6df_0011": {"func": model_38260_2a31c6df_0011, "volume": 0.0223013657, "area": 0.8573714666},
    "model_38260_2a31c6df_0012": {"func": model_38260_2a31c6df_0012, "volume": 0.0001819891, "area": 0.0374007827},
    "model_38260_2a31c6df_0014": {"func": model_38260_2a31c6df_0014, "volume": 0.000047033, "area": 0.0147224313},
    "model_38260_2a31c6df_0018": {"func": model_38260_2a31c6df_0018, "volume": 0.000044905, "area": 0.0146848202},
    "model_38260_2a31c6df_0022": {"func": model_38260_2a31c6df_0022, "volume": 0.0001351066, "area": 0.0351294392},
    "model_38260_2a31c6df_0024": {"func": model_38260_2a31c6df_0024, "volume": 0.000303423, "area": 0.0492320241},
    "model_38276_c9ef069a_0002": {"func": model_38276_c9ef069a_0002, "volume": 3.1691650809, "area": 21.9616854684},
    "model_38276_c9ef069a_0003": {"func": model_38276_c9ef069a_0003, "volume": 0.288633825, "area": 4.4257186507},
    "model_38276_c9ef069a_0006": {"func": model_38276_c9ef069a_0006, "volume": 15.1463630262, "area": 66.0125098948},
    "model_38276_c9ef069a_0010": {"func": model_38276_c9ef069a_0010, "volume": 1.33756082, "area": 10.3887200726},
    "model_38287_88ec74de_0007": {"func": model_38287_88ec74de_0007, "volume": 25.1327412287, "area": 56.5486677646},
    "model_38287_88ec74de_0011": {"func": model_38287_88ec74de_0011, "volume": 226.2004255215, "area": 588.813227791},
    "model_38287_88ec74de_0012": {"func": model_38287_88ec74de_0012, "volume": 125.074657521, "area": 162.1847207416},
    "model_38287_88ec74de_0014": {"func": model_38287_88ec74de_0014, "volume": 144.3169125243, "area": 184.1758693167},
    "model_38287_88ec74de_0017": {"func": model_38287_88ec74de_0017, "volume": 282.9155194849, "area": 737.7910732572},
    "model_38287_88ec74de_0023": {"func": model_38287_88ec74de_0023, "volume": 105.8324025178, "area": 140.1935721664},
    "model_38287_88ec74de_0029": {"func": model_38287_88ec74de_0029, "volume": 86.884070764, "area": 249.7748743362},
    "model_38287_88ec74de_0034": {"func": model_38287_88ec74de_0034, "volume": 0.1108512517, "area": 1.6627687753},
    "model_38287_88ec74de_0035": {"func": model_38287_88ec74de_0035, "volume": 5.7900301971, "area": 27.3258275246},
    "model_38287_88ec74de_0066": {"func": model_38287_88ec74de_0066, "volume": 2.4052818754, "area": 21.9911485751},
    "model_38287_88ec74de_0074": {"func": model_38287_88ec74de_0074, "volume": 340.2563270116, "area": 771.0658732914},
    "model_38287_88ec74de_0076": {"func": model_38287_88ec74de_0076, "volume": 2.5034566458, "area": 26.7035375555},
    "model_38287_88ec74de_0080": {"func": model_38287_88ec74de_0080, "volume": 53.2499954783, "area": 222.4247598742},
    "model_38287_88ec74de_0083": {"func": model_38287_88ec74de_0083, "volume": 0.02560404, "area": 0.9990594758},
    "model_38287_88ec74de_0086": {"func": model_38287_88ec74de_0086, "volume": 0.906339024, "area": 8.1961524227},
    "model_38287_88ec74de_0087": {"func": model_38287_88ec74de_0087, "volume": 4.3673171724, "area": 24.8630327333},
    "model_38287_88ec74de_0089": {"func": model_38287_88ec74de_0089, "volume": 1.2473309095, "area": 18.1046245668},
    "model_38287_88ec74de_0091": {"func": model_38287_88ec74de_0091, "volume": 1.0154998083, "area": 14.7377880532},
    "model_38287_88ec74de_0093": {"func": model_38287_88ec74de_0093, "volume": 2.1382464998, "area": 19.697785938},
    "model_38287_88ec74de_0094": {"func": model_38287_88ec74de_0094, "volume": 3.5749131403, "area": 31.2348180814},
    "model_38288_740bfe5a_0006": {"func": model_38288_740bfe5a_0006, "volume": 2.6860617188, "area": 14.6241138025},
    "model_38358_1b7da978_0000": {"func": model_38358_1b7da978_0000, "volume": 14.0562628348, "area": 54.8022473239},
    "model_38360_ad61c9b2_0002": {"func": model_38360_ad61c9b2_0002, "volume": 21.3964701218, "area": 74.6082871051},
    "model_38362_ab17f1f1_0002": {"func": model_38362_ab17f1f1_0002, "volume": 8.9827035673, "area": 49.4824698219},
    "model_38362_ab17f1f1_0004": {"func": model_38362_ab17f1f1_0004, "volume": 5.0749675392, "area": 21.4262882872},
    "model_38362_ab17f1f1_0005": {"func": model_38362_ab17f1f1_0005, "volume": 228.9628522868, "area": 1020.3181196085},
    "model_38454_24787d99_0002": {"func": model_38454_24787d99_0002, "volume": 1.3071553081, "area": 9.7211261768},
    "model_38675_6e07d74b_0004": {"func": model_38675_6e07d74b_0004, "volume": 0.2183574091, "area": 6.0241594783},
    "model_38739_f321c899_0006": {"func": model_38739_f321c899_0006, "volume": 10.5577253653, "area": 92.8303936315},
    "model_38739_f321c899_0007": {"func": model_38739_f321c899_0007, "volume": 38.2089108457, "area": 63.9718192361},
    "model_38739_f321c899_0016": {"func": model_38739_f321c899_0016, "volume": 0.5393489415, "area": 7.745023818},
    "model_38739_f321c899_0018": {"func": model_38739_f321c899_0018, "volume": 0.7541232404, "area": 10.4508417564},
    "model_38953_19054857_0003": {"func": model_38953_19054857_0003, "volume": 12.5663706144, "area": 50.2654824574},
    "model_38953_19054857_0006": {"func": model_38953_19054857_0006, "volume": 0.0077942286, "area": 0.2598076211},
    "model_38953_19054857_0007": {"func": model_38953_19054857_0007, "volume": 0.0874247997, "area": 2.3226550793},
    "model_38953_19054857_0008": {"func": model_38953_19054857_0008, "volume": 0.0006235386, "area": 0.0457261573},
    "model_38953_19054857_0011": {"func": model_38953_19054857_0011, "volume": 0.0429893802, "area": 1.2603185715},
    "model_38953_19054857_0013": {"func": model_38953_19054857_0013, "volume": 0.0339893808, "area": 1.0203185785},
    "model_38953_19054857_0014": {"func": model_38953_19054857_0014, "volume": 0.298867258, "area": 4.5713274123},
    "model_38953_19054857_0015": {"func": model_38953_19054857_0015, "volume": 0.0228539786, "area": 0.9841150065},
    "model_39124_28e99e62_0000": {"func": model_39124_28e99e62_0000, "volume": 34.3566017178, "area": 156.1690475583},
    "model_39124_28e99e62_0003": {"func": model_39124_28e99e62_0003, "volume": 384.2306712446, "area": 659.9008003187},
    "model_39306_ee445998_0010": {"func": model_39306_ee445998_0010, "volume": 0.3141592654, "area": 6.3460171603},
    "model_39306_ee445998_0011": {"func": model_39306_ee445998_0011, "volume": 0.3280390026, "area": 6.8968694166},
    "model_39306_ee445998_0017": {"func": model_39306_ee445998_0017, "volume": 2.9399999926, "area": 26.0799999915},
    "model_39306_ee445998_0030": {"func": model_39306_ee445998_0030, "volume": 0.0148793696, "area": 1.9853295718},
    "model_39306_ee445998_0033": {"func": model_39306_ee445998_0033, "volume": 0.0065500293, "area": 0.282211386},
    "model_39389_d641313f_0018": {"func": model_39389_d641313f_0018, "volume": 0.9047786842, "area": 10.5557513161},
    "model_39389_d641313f_0022": {"func": model_39389_d641313f_0022, "volume": 5.8904862255, "area": 31.4159265359},
    "model_39389_d641313f_0046": {"func": model_39389_d641313f_0046, "volume": 0.6675884389, "area": 12.0165919},
    "model_39389_d641313f_0048": {"func": model_39389_d641313f_0048, "volume": 0.4523893421, "area": 11.3097335529},
    "model_39389_d641313f_0049": {"func": model_39389_d641313f_0049, "volume": 4.5238934212, "area": 31.6672539482},
    "model_39389_d641313f_0062": {"func": model_39389_d641313f_0062, "volume": 5.0579641723, "area": 24.5672545511},
    "model_39389_d641313f_0065": {"func": model_39389_d641313f_0065, "volume": 321.0274060002, "area": 783.2853502327},
    "model_39390_61cd2601_0006": {"func": model_39390_61cd2601_0006, "volume": 7.5272678455, "area": 71.4494346815},
    "model_39390_61cd2601_0019": {"func": model_39390_61cd2601_0019, "volume": 0.4384915449, "area": 7.9667992264},
    "model_39394_3e0555d8_0000": {"func": model_39394_3e0555d8_0000, "volume": 65.946097862, "area": 286.8357671057},
    "model_39395_c95928c9_0000": {"func": model_39395_c95928c9_0000, "volume": 0.0051376204, "area": 0.3008412466},
    "model_39633_694ad30a_0000": {"func": model_39633_694ad30a_0000, "volume": 12.4407069082, "area": 43.730969738},
    "model_39633_694ad30a_0003": {"func": model_39633_694ad30a_0003, "volume": 18.0955736847, "area": 62.5805256595},
    "model_39708_228f26be_0000": {"func": model_39708_228f26be_0000, "volume": 533.759996551, "area": 408.6089169156},
    "model_39708_228f26be_0001": {"func": model_39708_228f26be_0001, "volume": 26348.1969870838, "area": 7737.0960733361},
    "model_39708_228f26be_0012": {"func": model_39708_228f26be_0012, "volume": 400.3199875182, "area": 539.9474897263},
    "model_39793_5193d5ab_0014": {"func": model_39793_5193d5ab_0014, "volume": 0.0125687207, "area": 0.3562786962},
    "model_39793_5193d5ab_0016": {"func": model_39793_5193d5ab_0016, "volume": 19.3055549536, "area": 40.5365983278},
    "model_39793_5193d5ab_0019": {"func": model_39793_5193d5ab_0019, "volume": 7.2395831076, "area": 25.3353739549},
    "model_39793_5193d5ab_0021": {"func": model_39793_5193d5ab_0021, "volume": 1.2568720673, "area": 7.1255739248},
    "model_39793_5193d5ab_0023": {"func": model_39793_5193d5ab_0023, "volume": 212.3611044898, "area": 278.6891135036},
    "model_39793_5193d5ab_0026": {"func": model_39793_5193d5ab_0026, "volume": 5.5302370961, "area": 35.4695235368},
    "model_39795_7d4d7d57_0003": {"func": model_39795_7d4d7d57_0003, "volume": 57.354724, "area": 187.0964},
    "model_39795_7d4d7d57_0004": {"func": model_39795_7d4d7d57_0004, "volume": 101.3541635065, "area": 224.2180595006},
    "model_39850_b2aa4f1e_0011": {"func": model_39850_b2aa4f1e_0011, "volume": 7.5333741788, "area": 60.5088684914},
    "model_39932_7b9150e8_0001": {"func": model_39932_7b9150e8_0001, "volume": 28937.712, "area": 29927.072},
    "model_39932_7b9150e8_0004": {"func": model_39932_7b9150e8_0004, "volume": 2167.7775517877, "area": 1967.6972283947},
    "model_39932_7b9150e8_0005": {"func": model_39932_7b9150e8_0005, "volume": 3624.8946801018, "area": 3269.5495167339},
    "model_39932_7b9150e8_0006": {"func": model_39932_7b9150e8_0006, "volume": 2655.9276146319, "area": 1322.4285873021},
    "model_40052_42bdc982_0001": {"func": model_40052_42bdc982_0001, "volume": 127.0233727891, "area": 236.7116321036},
    "model_40052_42bdc982_0007": {"func": model_40052_42bdc982_0007, "volume": 5269.0614382744, "area": 5789.5849099455},
    "model_40052_42bdc982_0012": {"func": model_40052_42bdc982_0012, "volume": 1686.4623447815, "area": 1879.1877973377},
    "model_40052_42bdc982_0013": {"func": model_40052_42bdc982_0013, "volume": 4919.04, "area": 3203.84},
    "model_40052_42bdc982_0014": {"func": model_40052_42bdc982_0014, "volume": 66129.8690075056, "area": 46859.6888203459},
    "model_40052_42bdc982_0015": {"func": model_40052_42bdc982_0015, "volume": 9.5666225155, "area": 61.5256249406},
    "model_40052_42bdc982_0018": {"func": model_40052_42bdc982_0018, "volume": 1633.1255250421, "area": 1741.7617990033},
    "model_40052_42bdc982_0022": {"func": model_40052_42bdc982_0022, "volume": 453.8775598007, "area": 555.2805373463},
    "model_40061_d07e8764_0007": {"func": model_40061_d07e8764_0007, "volume": 49.480084294, "area": 98.9601685881},
    "model_40061_d07e8764_0012": {"func": model_40061_d07e8764_0012, "volume": 141.3716694115, "area": 339.2920065877},
    "model_40061_d07e8764_0013": {"func": model_40061_d07e8764_0013, "volume": 28.2743338823, "area": 75.3982236862},
    "model_40070_be9c502b_0009": {"func": model_40070_be9c502b_0009, "volume": 0.1079922475, "area": 1.2566370614},
    "model_40070_be9c502b_0061": {"func": model_40070_be9c502b_0061, "volume": 0.439822985, "area": 3.9584068334},
    "model_40074_4615c9d1_0016": {"func": model_40074_4615c9d1_0016, "volume": 9.6211275016, "area": 30.2378292908},
    "model_40176_01ed49ea_0000": {"func": model_40176_01ed49ea_0000, "volume": 9.5704449727, "area": 36.4234681461},
    "model_40176_01ed49ea_0001": {"func": model_40176_01ed49ea_0001, "volume": 0.2544621534, "area": 8.7246396624},
    "model_40176_01ed49ea_0002": {"func": model_40176_01ed49ea_0002, "volume": 0.107010965, "area": 3.9248003282},
    "model_40176_01ed49ea_0004": {"func": model_40176_01ed49ea_0004, "volume": 0.2090315473, "area": 7.2885359877},
    "model_40341_9514acd7_0000": {"func": model_40341_9514acd7_0000, "volume": 41.6897841923, "area": 110.7114451632},
    "model_40352_a9774a3f_0009": {"func": model_40352_a9774a3f_0009, "volume": 0.2010995308, "area": 1.9001530466},
    "model_40413_c590b4b4_0000": {"func": model_40413_c590b4b4_0000, "volume": 14.7446175958, "area": 187.6591148838},
    "model_40413_c590b4b4_0002": {"func": model_40413_c590b4b4_0002, "volume": 4.0155554304, "area": 63.7640691696},
    "model_40417_b8d98f73_0009": {"func": model_40417_b8d98f73_0009, "volume": 8.1430081581, "area": 23.1849537835},
    "model_40491_ac67bf4c_0000": {"func": model_40491_ac67bf4c_0000, "volume": 0.6108983013, "area": 14.681018766},
    "model_40491_ac67bf4c_0004": {"func": model_40491_ac67bf4c_0004, "volume": 0.0111371674, "area": 0.4322293798},
    "model_40491_ac67bf4c_0008": {"func": model_40491_ac67bf4c_0008, "volume": 0.0085330221, "area": 0.2942584733},
    "model_40491_ac67bf4c_0012": {"func": model_40491_ac67bf4c_0012, "volume": 0.0002678703, "area": 0.0335331079},
    "model_40491_ac67bf4c_0015": {"func": model_40491_ac67bf4c_0015, "volume": 0.064400475, "area": 1.4535067799},
    "model_40491_ac67bf4c_0019": {"func": model_40491_ac67bf4c_0019, "volume": 0.0374350139, "area": 1.1096655104},
    "model_40500_6055e3d7_0004": {"func": model_40500_6055e3d7_0004, "volume": 235749.4789213776, "area": 68081.3402052498},
    "model_40500_6055e3d7_0006": {"func": model_40500_6055e3d7_0006, "volume": 12288, "area": 6272},
    "model_40500_6055e3d7_0010": {"func": model_40500_6055e3d7_0010, "volume": 47.1238898038, "area": 113.0973355292},
    "model_40500_6055e3d7_0011": {"func": model_40500_6055e3d7_0011, "volume": 628.318530718, "area": 1262.9202467431},
    "model_40500_6055e3d7_0012": {"func": model_40500_6055e3d7_0012, "volume": 1440, "area": 1032},
    "model_40500_6055e3d7_0028": {"func": model_40500_6055e3d7_0028, "volume": 2016, "area": 1376},
    "model_40500_6055e3d7_0030": {"func": model_40500_6055e3d7_0030, "volume": 1429.4246573834, "area": 959.7565556717},
    "model_40513_89770261_0005": {"func": model_40513_89770261_0005, "volume": 0.0973893723, "area": 1.2252211349},
    "model_40514_bb61631d_0017": {"func": model_40514_bb61631d_0017, "volume": 9.4322117107, "area": 39.3249531806},
    "model_40514_bb61631d_0020": {"func": model_40514_bb61631d_0020, "volume": 9.5892913434, "area": 38.4610152009},
    "model_40514_bb61631d_0021": {"func": model_40514_bb61631d_0021, "volume": 0.1130973355, "area": 1.6493361431},
    "model_40514_bb61631d_0024": {"func": model_40514_bb61631d_0024, "volume": 133.4575222039, "area": 282.7690260418},
    "model_40519_55a097c6_0003": {"func": model_40519_55a097c6_0003, "volume": 16.8342674654, "area": 66.1235213924},
    "model_40519_55a097c6_0007": {"func": model_40519_55a097c6_0007, "volume": 3.8162496759, "area": 79.8749932175},
    "model_40519_55a097c6_0009": {"func": model_40519_55a097c6_0009, "volume": 1.2312446015, "area": 7.6437734276},
    "model_40519_55a097c6_0011": {"func": model_40519_55a097c6_0011, "volume": 4.6244243861, "area": 98.2690182043},
    "model_40519_55a097c6_0012": {"func": model_40519_55a097c6_0012, "volume": 31.8596764982, "area": 69.9475604322},
    "model_40519_55a097c6_0013": {"func": model_40519_55a097c6_0013, "volume": 0.5013981875, "area": 8.8341585419},
    "model_40519_55a097c6_0014": {"func": model_40519_55a097c6_0014, "volume": 1.0179152897, "area": 18.0822219159},
    "model_40519_55a097c6_0016": {"func": model_40519_55a097c6_0016, "volume": 10.9955742876, "area": 65.9734457254},
    "model_40586_86bc7430_0000": {"func": model_40586_86bc7430_0000, "volume": 60.042202496, "area": 144.773904},
    "model_40624_e1c5c424_0000": {"func": model_40624_e1c5c424_0000, "volume": 91046.4287189257, "area": 21607.0786191358},
    "model_40624_e1c5c424_0001": {"func": model_40624_e1c5c424_0001, "volume": 21724.4645862196, "area": 7018.1146088536},
    "model_40624_e1c5c424_0003": {"func": model_40624_e1c5c424_0003, "volume": 5811.9464091411, "area": 4688.8270354828},
    "model_40624_e1c5c424_0004": {"func": model_40624_e1c5c424_0004, "volume": 63737.9691641961, "area": 14246.4225582302},
    "model_40624_e1c5c424_0006": {"func": model_40624_e1c5c424_0006, "volume": 1824.1371669412, "area": 1321.7499924639},
    "model_40624_e1c5c424_0007": {"func": model_40624_e1c5c424_0007, "volume": 1784.9720510772, "area": 1631.2563588066},
    "model_40624_e1c5c424_0008": {"func": model_40624_e1c5c424_0008, "volume": 236.4245999729, "area": 364.797138424},
    "model_40624_e1c5c424_0010": {"func": model_40624_e1c5c424_0010, "volume": 2898.3008881569, "area": 2014.8141502221},
    "model_40624_e1c5c424_0011": {"func": model_40624_e1c5c424_0011, "volume": 12.3700210735, "area": 36.521014598},
    "model_40624_e1c5c424_0012": {"func": model_40624_e1c5c424_0012, "volume": 92085.5778333063, "area": 23130.3688951735},
    "model_40624_e1c5c424_0013": {"func": model_40624_e1c5c424_0013, "volume": 10588.3942431785, "area": 7922.0936870543},
    "model_40624_e1c5c424_0014": {"func": model_40624_e1c5c424_0014, "volume": 5615.5968682918, "area": 4531.7474028033},
    "model_40624_e1c5c424_0015": {"func": model_40624_e1c5c424_0015, "volume": 757.7711537592, "area": 711.8956409522},
    "model_40624_e1c5c424_0016": {"func": model_40624_e1c5c424_0016, "volume": 6923.9911485751, "area": 2904.2654824574},
    "model_40705_5ff43505_0040": {"func": model_40705_5ff43505_0040, "volume": 11.9380520836, "area": 64.4654812517},
    "model_40712_8e707290_0000": {"func": model_40712_8e707290_0000, "volume": 38.4, "area": 75.2},
    "model_40723_f18d24a6_0004": {"func": model_40723_f18d24a6_0004, "volume": 0.0193055562, "area": 0.4053659994},
    "model_40723_f18d24a6_0008": {"func": model_40723_f18d24a6_0008, "volume": 1.9258573222, "area": 24.9449143052},
    "model_40782_3383cd58_0010": {"func": model_40782_3383cd58_0010, "volume": 0.7539822369, "area": 6.7858401318},
    "model_40782_3383cd58_0013": {"func": model_40782_3383cd58_0013, "volume": 0.0684008721, "area": 1.6547060512},
    "model_40782_3383cd58_0018": {"func": model_40782_3383cd58_0018, "volume": 0.0597884352, "area": 1.480475538},
    "model_40782_3383cd58_0026": {"func": model_40782_3383cd58_0026, "volume": 0.3798915865, "area": 4.4797709823},
    "model_40887_454ffc48_0002": {"func": model_40887_454ffc48_0002, "volume": 0.1507964474, "area": 2.2619467106},
    "model_40887_454ffc48_0005": {"func": model_40887_454ffc48_0005, "volume": 0.0439822972, "area": 1.8692476289},
    "model_40887_454ffc48_0011": {"func": model_40887_454ffc48_0011, "volume": 0.2953097094, "area": 3.2044245067},
    "model_40887_454ffc48_0013": {"func": model_40887_454ffc48_0013, "volume": 0.0376991118, "area": 1.1309733553},
    "model_40887_454ffc48_0014": {"func": model_40887_454ffc48_0014, "volume": 0.0212057504, "area": 0.7068583471},
    "model_40887_454ffc48_0015": {"func": model_40887_454ffc48_0015, "volume": 0.4272566009, "area": 4.5238934212},
    "model_40939_0bedb1ea_0002": {"func": model_40939_0bedb1ea_0002, "volume": 0.6327000189, "area": 5.997800146},
    "model_40939_0bedb1ea_0004": {"func": model_40939_0bedb1ea_0004, "volume": 0.0141371669, "area": 0.5811946409},
    "model_40939_0bedb1ea_0008": {"func": model_40939_0bedb1ea_0008, "volume": 9.4289524388, "area": 32.8047612035},
    "model_40939_0bedb1ea_0009": {"func": model_40939_0bedb1ea_0009, "volume": 0.0125663706, "area": 0.3769911184},
    "model_40939_0bedb1ea_0010": {"func": model_40939_0bedb1ea_0010, "volume": 0.0150000004, "area": 0.4600000113},
    "model_40939_0bedb1ea_0011": {"func": model_40939_0bedb1ea_0011, "volume": 0.3200000095, "area": 4.3200001121},
    "model_40999_cad6be09_0000": {"func": model_40999_cad6be09_0000, "volume": 22155.3098625212, "area": 4864.5062941925},
    "model_40999_cad6be09_0002": {"func": model_40999_cad6be09_0002, "volume": 38771.7922594122, "area": 6877.4054639618},
    "model_40999_cad6be09_0003": {"func": model_40999_cad6be09_0003, "volume": 10012.9646832254, "area": 2777.5975959966},
    "model_40999_cad6be09_0007": {"func": model_40999_cad6be09_0007, "volume": 57.9166648608, "area": 101.3414958195},
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
