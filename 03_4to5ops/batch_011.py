"""Batch 011 - passing/03_4to5ops
123 models bundled from Fusion360 Gallery reconstructions.
"""

from build123d import *
from build123d import Edge, BuildLine
from collections import Counter
from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
from OCP.Geom import Geom_BSplineCurve
from OCP.TColStd import TColStd_Array1OfReal, TColStd_Array1OfInteger
from OCP.TColgp import TColgp_Array1OfPnt
from OCP.gp import gp_Pnt


def model_41753_9b4f8d8a_0001():
    """Model: Turn Table Top v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 314.159265359, perimeter: 62.8318530718
            Circle(10)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 32.2013350216, perimeter: 128.8052997803
            with BuildLine():
                CenterArc((0, 0), 10.5000001565, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 10, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


def model_41753_9b4f8d8a_0006():
    """Model: turn table v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 18.0641549259, perimeter: 72.2566315475
            with BuildLine():
                CenterArc((0, 0), 6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 5.500000082, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.3751295086, perimeter: 11.5237144503
            with BuildLine():
                Line((0, 0), (-3.5399999209, 4.2099999059))
                Line((-3.1573087017, 4.5317877719), (0, 0))
                Line((-3.5399999209, 4.2099999059), (-3.1573087017, 4.5317877719))
            make_face()
            # Profile area: 1.3738676569, perimeter: 11.5026647302
            with BuildLine():
                Line((0, 0), (3.5500000529, -4.2000000626))
                Line((3.5500000529, -4.2000000626), (3.9195266963, -3.8631765779))
                Line((3.9195266963, -3.8631765779), (0, 0))
            make_face()
            # Profile area: 1.3742000346, perimeter: 11.4989243401
            with BuildLine():
                Line((4.1999999061, 3.5499999207), (0, 0))
                Line((3.8600001833, 3.917000186), (4.1999999061, 3.5499999207))
                Line((0, 0), (3.8600001833, 3.917000186))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


def model_41754_fb582b36_0000():
    """Model: headtube"""
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
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            with Locations((81.5000012144, 40.000000596)):
                Circle(1.5)
        # OneSide extrude, distance=6.8
        extrude(amount=6.8)
    return part.part


def model_41757_c1173a7e_0000():
    """Model: Cross v3"""
    with BuildPart() as part:
        # Sketch7 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.1290165189, perimeter: 13.7160004377
            with BuildLine():
                Line((2.5400000811, 2.7940000892), (2.5400000811, -2.5400000811))
                Line((2.5400000811, -2.5400000811), (4.0640001297, -2.5400000811))
                Line((4.0640001297, -2.5400000811), (4.0640001297, 2.7940000892))
                Line((4.0640001297, 2.7940000892), (2.5400000811, 2.7940000892))
            make_face()
            # Profile area: 8.1290165189, perimeter: 13.7160004377
            with BuildLine():
                Line((-2.5400000811, 2.7940000892), (-4.0640001297, 2.7940000892))
                Line((-4.0640001297, 2.7940000892), (-4.0640001297, -2.5400000811))
                Line((-4.0640001297, -2.5400000811), (-2.5400000811, -2.5400000811))
                Line((-2.5400000811, -2.5400000811), (-2.5400000811, 2.7940000892))
            make_face()
            # Profile area: 27.0967217295, perimeter: 20.8280006647
            with BuildLine():
                Line((-2.5400000811, -2.5400000811), (-2.5400000811, 2.7940000892))
                Line((-2.5400000811, -2.5400000811), (2.5400000811, -2.5400000811))
                Line((2.5400000811, 2.7940000892), (2.5400000811, -2.5400000811))
                Line((2.5400000811, 2.7940000892), (-2.5400000811, 2.7940000892))
            make_face()
            # Profile area: 6.4516004118, perimeter: 12.7000004053
            with BuildLine():
                Line((2.5400000811, 2.7940000892), (-2.5400000811, 2.7940000892))
                Line((2.5400000811, 4.0640001297), (2.5400000811, 2.7940000892))
                Line((-2.5400000811, 4.0640001297), (2.5400000811, 4.0640001297))
                Line((-2.5400000811, 2.7940000892), (-2.5400000811, 4.0640001297))
            make_face()
            # Profile area: 7.7419204942, perimeter: 13.2080004215
            with BuildLine():
                Line((-2.5400000811, -4.0640001297), (-2.5400000811, -2.5400000811))
                Line((2.5400000811, -4.0640001297), (-2.5400000811, -4.0640001297))
                Line((2.5400000811, -2.5400000811), (2.5400000811, -4.0640001297))
                Line((-2.5400000811, -2.5400000811), (2.5400000811, -2.5400000811))
            make_face()
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)

        # Sketch8 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.27, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.4009182797, perimeter: 11.9694680102
            Circle(1.905)
        # OneSide extrude, distance=-1.27
        extrude(amount=-1.27, mode=Mode.SUBTRACT)
    return part.part


def model_41757_c1173a7e_0002():
    """Model: Main_Shaft v6"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 20.2682985551, perimeter: 15.9592904406
            Circle(2.5399999619)
        # OneSide extrude, distance=15.24
        extrude(amount=15.24)
    return part.part


def model_41757_c1173a7e_0006():
    """Model: Gear 2 v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 273.6220387126, perimeter: 71.8168080611
            with BuildLine():
                CenterArc((0, 0), 9.525, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.905, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.635, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2026829916, perimeter: 1.595929068
            with Locations((0, -9.1440002918)):
                Circle(0.254)
        # OneSide extrude, distance=0.762
        extrude(amount=0.762, mode=Mode.ADD)
    return part.part


def model_41757_c1173a7e_0024():
    """Model: Stick v4 (3)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.96774, perimeter: 4.064
            with BuildLine():
                Line((0, 0.762), (0, 0))
                Line((0, 0), (1.27, 0))
                Line((1.27, 0), (1.27, 0.762))
                Line((1.27, 0.762), (0, 0.762))
            make_face()
        # OneSide extrude, distance=8.382
        extrude(amount=8.382)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1.27, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.0484357591, perimeter: 16.7647993556
            with BuildLine():
                Line((-8.2553996778, 0.3175), (-8.2553996778, 0.4445))
                Line((-8.2553996778, 0.3175), (0, 0.3175))
                Line((0, 0.3175), (0, 0.4445))
                Line((-8.2553996778, 0.4445), (0, 0.4445))
            make_face()
        # OneSide extrude, distance=-0.508
        extrude(amount=-0.508, mode=Mode.SUBTRACT)
    return part.part


def model_41759_fb1f25f1_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.067199997, perimeter: 1.1599999741
            with BuildLine():
                Line((0.2099999953, -0.0799999982), (0.2099999953, 0.0799999982))
                Line((0.2099999953, 0.0799999982), (-0.2099999953, 0.0799999982))
                Line((-0.2099999953, 0.0799999982), (-0.2099999953, -0.0799999982))
                Line((-0.2099999953, -0.0799999982), (0.2099999953, -0.0799999982))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.0799999982), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0683346145, perimeter: 1.1192735029
            with BuildLine():
                Line((0.1898183777, 0.179999996), (0.1898183777, 0))
                Line((-0.1898183777, 0.179999996), (0.1898183777, 0.179999996))
                Line((-0.1898183777, 0), (-0.1898183777, 0.179999996))
                Line((0.1898183777, 0), (-0.1898183777, 0))
            make_face()
        # OneSide extrude, distance=-0.02
        extrude(amount=-0.02, mode=Mode.SUBTRACT)
    return part.part


def model_41762_1fb3760e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2431.1976, perimeter: 199.8344
            with BuildLine():
                Line((0, 41.9172), (0, 0))
                Line((0, 0), (58, 0))
                Line((58, 0), (58, 41.9172))
                Line((58, 41.9172), (0, 41.9172))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 875, perimeter: 120
            with BuildLine():
                Line((10, 35), (10, 10))
                Line((10, 10), (45, 10))
                Line((45, 10), (45, 35))
                Line((45, 35), (10, 35))
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)
    return part.part


def model_41762_228d379c_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 130, perimeter: 46
            with BuildLine():
                Line((0, 13), (0, 0))
                Line((0, 0), (10, 0))
                Line((10, 0), (10, 13))
                Line((10, 13), (0, 13))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 48 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.0000001192, perimeter: 17.0000002533
            with BuildLine():
                Line((-1.0000000149, -3.5000001863), (-9.0000001341, -3.5000001863))
                Line((-1.0000000149, -3.0000001788), (-1.0000000149, -3.5000001863))
                Line((-9.0000001341, -3.0000001788), (-1.0000000149, -3.0000001788))
                Line((-9.0000001341, -3.5000001863), (-9.0000001341, -3.0000001788))
            make_face()
            # Profile area: 4.0000001192, perimeter: 17.0000002533
            with BuildLine():
                Line((-1.0000000149, -2.5000001863), (-9.0000001341, -2.5000001863))
                Line((-1.0000000149, -2.0000001788), (-1.0000000149, -2.5000001863))
                Line((-9.0000001341, -2.0000001788), (-1.0000000149, -2.0000001788))
                Line((-9.0000001341, -2.5000001863), (-9.0000001341, -2.0000001788))
            make_face()
            # Profile area: 4.0000001192, perimeter: 17.0000002533
            with BuildLine():
                Line((-1.0000000149, -1.5000001863), (-9.0000001341, -1.5000001863))
                Line((-1.0000000149, -1.0000001788), (-1.0000000149, -1.5000001863))
                Line((-9.0000001341, -1.0000001788), (-1.0000000149, -1.0000001788))
                Line((-9.0000001341, -1.5000001863), (-9.0000001341, -1.0000001788))
            make_face()
            # Profile area: 4.0000001192, perimeter: 17.0000002533
            with BuildLine():
                Line((-1.0000000149, -4.5000001863), (-9.0000001341, -4.5000001863))
                Line((-1.0000000149, -4.0000001788), (-1.0000000149, -4.5000001863))
                Line((-9.0000001341, -4.0000001788), (-1.0000000149, -4.0000001788))
                Line((-9.0000001341, -4.5000001863), (-9.0000001341, -4.0000001788))
            make_face()
            # Profile area: 4.0000001192, perimeter: 17.0000002533
            with BuildLine():
                Line((-1.0000000149, -5.5000001863), (-9.0000001341, -5.5000001863))
                Line((-1.0000000149, -5.0000001788), (-1.0000000149, -5.5000001863))
                Line((-9.0000001341, -5.0000001788), (-1.0000000149, -5.0000001788))
                Line((-9.0000001341, -5.5000001863), (-9.0000001341, -5.0000001788))
            make_face()
            # Profile area: 4.0000001192, perimeter: 17.0000002533
            with BuildLine():
                Line((-1.0000000149, -6.5000001863), (-9.0000001341, -6.5000001863))
                Line((-1.0000000149, -6.0000001788), (-1.0000000149, -6.5000001863))
                Line((-9.0000001341, -6.0000001788), (-1.0000000149, -6.0000001788))
                Line((-9.0000001341, -6.5000001863), (-9.0000001341, -6.0000001788))
            make_face()
            # Profile area: 4.0000001192, perimeter: 17.0000002533
            with BuildLine():
                Line((-1.0000000149, -7.5000001863), (-9.0000001341, -7.5000001863))
                Line((-1.0000000149, -7.0000001788), (-1.0000000149, -7.5000001863))
                Line((-9.0000001341, -7.0000001788), (-1.0000000149, -7.0000001788))
                Line((-9.0000001341, -7.5000001863), (-9.0000001341, -7.0000001788))
            make_face()
            # Profile area: 4.0000001192, perimeter: 17.0000002533
            with BuildLine():
                Line((-1.0000000149, -8.5000001863), (-9.0000001341, -8.5000001863))
                Line((-1.0000000149, -8.0000001788), (-1.0000000149, -8.5000001863))
                Line((-9.0000001341, -8.0000001788), (-1.0000000149, -8.0000001788))
                Line((-9.0000001341, -8.5000001863), (-9.0000001341, -8.0000001788))
            make_face()
            # Profile area: 4.0000001192, perimeter: 17.0000002533
            with BuildLine():
                Line((-1.0000000149, -9.5000001863), (-9.0000001341, -9.5000001863))
                Line((-1.0000000149, -9.0000001788), (-1.0000000149, -9.5000001863))
                Line((-9.0000001341, -9.0000001788), (-1.0000000149, -9.0000001788))
                Line((-9.0000001341, -9.5000001863), (-9.0000001341, -9.0000001788))
            make_face()
            # Profile area: 4.0000001192, perimeter: 17.0000002533
            with BuildLine():
                Line((-1.0000000149, -10.5000001863), (-9.0000001341, -10.5000001863))
                Line((-1.0000000149, -10.0000001788), (-1.0000000149, -10.5000001863))
                Line((-9.0000001341, -10.0000001788), (-1.0000000149, -10.0000001788))
                Line((-9.0000001341, -10.5000001863), (-9.0000001341, -10.0000001788))
            make_face()
            # Profile area: 4.0000001192, perimeter: 17.0000002533
            with BuildLine():
                Line((-1.0000000149, -11.5000001863), (-9.0000001341, -11.5000001863))
                Line((-1.0000000149, -11.0000001788), (-1.0000000149, -11.5000001863))
                Line((-9.0000001341, -11.0000001788), (-1.0000000149, -11.0000001788))
                Line((-9.0000001341, -11.5000001863), (-9.0000001341, -11.0000001788))
            make_face()
            # Profile area: 4.0000001192, perimeter: 17.0000002533
            with BuildLine():
                Line((-9.0000001341, -12.0000001788), (-1.0000000149, -12.0000001788))
                Line((-9.0000001341, -12.5000001863), (-9.0000001341, -12.0000001788))
                Line((-1.0000000149, -12.5000001863), (-9.0000001341, -12.5000001863))
                Line((-1.0000000149, -12.0000001788), (-1.0000000149, -12.5000001863))
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)
    return part.part


def model_41762_67992d19_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.9087385212, perimeter: 7.853981634
            Circle(1.25)
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0314159275, perimeter: 0.6283185401
            Circle(0.1000000015)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


def model_41762_942c9cc2_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 224, perimeter: 60
            with BuildLine():
                Line((0, 16), (0, 0))
                Line((0, 0), (14, 0))
                Line((14, 0), (14, 16))
                Line((14, 16), (0, 16))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.8, perimeter: 28.4
            with BuildLine():
                Line((0, 0), (-14, 0))
                Line((0, 0.2), (0, 0))
                Line((-14, 0.2), (0, 0.2))
                Line((-14, 0), (-14, 0.2))
            make_face()
        # OneSide extrude, distance=-13
        extrude(amount=-13, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.8, perimeter: 28.4
            with BuildLine():
                Line((0, 0), (-14, 0))
                Line((0, 0.2), (0, 0))
                Line((-14, 0.2), (0, 0.2))
                Line((-14, 0), (-14, 0.2))
            make_face()
        # OneSide extrude, distance=-14
        extrude(amount=-14, mode=Mode.ADD)
    return part.part


def model_41762_d2d9e84d_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 144, perimeter: 48
            with BuildLine():
                Line((0, 12), (0, 0))
                Line((0, 0), (12, 0))
                Line((12, 0), (12, 12))
                Line((12, 12), (0, 12))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 40 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.2500001565, perimeter: 22.0000003278
            with BuildLine():
                Line((-1.0000000149, -11.0000001639), (-1.0000000149, -0.5000000075))
                Line((-1.0000000149, -0.5000000075), (-1.5000000224, -0.5000000075))
                Line((-1.5000000224, -0.5000000075), (-1.5000000224, -11.0000001639))
                Line((-1.5000000224, -11.0000001639), (-1.0000000149, -11.0000001639))
            make_face()
            # Profile area: 5.2500001565, perimeter: 22.0000003278
            with BuildLine():
                Line((-2.0000000149, -0.5000000075), (-2.5000000224, -0.5000000075))
                Line((-2.5000000224, -0.5000000075), (-2.5000000224, -11.0000001639))
                Line((-2.5000000224, -11.0000001639), (-2.0000000149, -11.0000001639))
                Line((-2.0000000149, -11.0000001639), (-2.0000000149, -0.5000000075))
            make_face()
            # Profile area: 5.2500001565, perimeter: 22.0000003278
            with BuildLine():
                Line((-3.0000000149, -0.5000000075), (-3.5000000224, -0.5000000075))
                Line((-3.5000000224, -0.5000000075), (-3.5000000224, -11.0000001639))
                Line((-3.5000000224, -11.0000001639), (-3.0000000149, -11.0000001639))
                Line((-3.0000000149, -11.0000001639), (-3.0000000149, -0.5000000075))
            make_face()
            # Profile area: 5.2500001565, perimeter: 22.0000003278
            with BuildLine():
                Line((-4.0000000149, -0.5000000075), (-4.5000000224, -0.5000000075))
                Line((-4.5000000224, -0.5000000075), (-4.5000000224, -11.0000001639))
                Line((-4.5000000224, -11.0000001639), (-4.0000000149, -11.0000001639))
                Line((-4.0000000149, -11.0000001639), (-4.0000000149, -0.5000000075))
            make_face()
            # Profile area: 5.2500001565, perimeter: 22.0000003278
            with BuildLine():
                Line((-5.0000000149, -0.5000000075), (-5.5000000224, -0.5000000075))
                Line((-5.5000000224, -0.5000000075), (-5.5000000224, -11.0000001639))
                Line((-5.5000000224, -11.0000001639), (-5.0000000149, -11.0000001639))
                Line((-5.0000000149, -11.0000001639), (-5.0000000149, -0.5000000075))
            make_face()
            # Profile area: 5.2500001565, perimeter: 22.0000003278
            with BuildLine():
                Line((-6.0000000149, -0.5000000075), (-6.5000000224, -0.5000000075))
                Line((-6.5000000224, -0.5000000075), (-6.5000000224, -11.0000001639))
                Line((-6.5000000224, -11.0000001639), (-6.0000000149, -11.0000001639))
                Line((-6.0000000149, -11.0000001639), (-6.0000000149, -0.5000000075))
            make_face()
            # Profile area: 5.2500001565, perimeter: 22.0000003278
            with BuildLine():
                Line((-7.0000000149, -0.5000000075), (-7.5000000224, -0.5000000075))
                Line((-7.5000000224, -0.5000000075), (-7.5000000224, -11.0000001639))
                Line((-7.5000000224, -11.0000001639), (-7.0000000149, -11.0000001639))
                Line((-7.0000000149, -11.0000001639), (-7.0000000149, -0.5000000075))
            make_face()
            # Profile area: 5.2500001565, perimeter: 22.0000003278
            with BuildLine():
                Line((-8.0000000149, -0.5000000075), (-8.5000000224, -0.5000000075))
                Line((-8.5000000224, -0.5000000075), (-8.5000000224, -11.0000001639))
                Line((-8.5000000224, -11.0000001639), (-8.0000000149, -11.0000001639))
                Line((-8.0000000149, -11.0000001639), (-8.0000000149, -0.5000000075))
            make_face()
            # Profile area: 5.2500001565, perimeter: 22.0000003278
            with BuildLine():
                Line((-9.0000000149, -0.5000000075), (-9.5000000224, -0.5000000075))
                Line((-9.5000000224, -0.5000000075), (-9.5000000224, -11.0000001639))
                Line((-9.5000000224, -11.0000001639), (-9.0000000149, -11.0000001639))
                Line((-9.0000000149, -11.0000001639), (-9.0000000149, -0.5000000075))
            make_face()
            # Profile area: 5.2500001565, perimeter: 22.0000003278
            with BuildLine():
                Line((-10.0000000149, -0.5000000075), (-10.5000000224, -0.5000000075))
                Line((-10.5000000224, -0.5000000075), (-10.5000000224, -11.0000001639))
                Line((-10.5000000224, -11.0000001639), (-10.0000000149, -11.0000001639))
                Line((-10.0000000149, -11.0000001639), (-10.0000000149, -0.5000000075))
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)
    return part.part


def model_41762_e0b6edc5_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 293.262, perimeter: 72.877
            with BuildLine():
                Line((0, 24.4385), (0, 0))
                Line((0, 0), (12, 0))
                Line((12, 0), (12, 24.4385))
                Line((12, 24.4385), (0, 24.4385))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 40 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.4999998324, perimeter: 47.0000006706
            with BuildLine():
                Line((-10.0000000149, -0.5), (-10.0000000149, -23.5000003502))
                Line((-10.5, -0.5), (-10.0000000149, -0.5))
                Line((-10.5, -23.5000003502), (-10.5, -0.5))
                Line((-10.0000000149, -23.5000003502), (-10.5, -23.5000003502))
            make_face()
            # Profile area: 11.4999998324, perimeter: 47.0000006706
            with BuildLine():
                Line((-9.0000000149, -0.5), (-9.0000000149, -23.5000003502))
                Line((-9.5, -0.5), (-9.0000000149, -0.5))
                Line((-9.5, -23.5000003502), (-9.5, -0.5))
                Line((-9.0000000149, -23.5000003502), (-9.5, -23.5000003502))
            make_face()
            # Profile area: 11.4999998324, perimeter: 47.0000006706
            with BuildLine():
                Line((-8.0000000149, -0.5), (-8.0000000149, -23.5000003502))
                Line((-8.5, -0.5), (-8.0000000149, -0.5))
                Line((-8.5, -23.5000003502), (-8.5, -0.5))
                Line((-8.0000000149, -23.5000003502), (-8.5, -23.5000003502))
            make_face()
            # Profile area: 11.4999998324, perimeter: 47.0000006706
            with BuildLine():
                Line((-7.0000000149, -0.5), (-7.0000000149, -23.5000003502))
                Line((-7.5, -0.5), (-7.0000000149, -0.5))
                Line((-7.5, -23.5000003502), (-7.5, -0.5))
                Line((-7.0000000149, -23.5000003502), (-7.5, -23.5000003502))
            make_face()
            # Profile area: 11.4999998324, perimeter: 47.0000006706
            with BuildLine():
                Line((-6.0000000149, -0.5), (-6.0000000149, -23.5000003502))
                Line((-6.5, -0.5), (-6.0000000149, -0.5))
                Line((-6.5, -23.5000003502), (-6.5, -0.5))
                Line((-6.0000000149, -23.5000003502), (-6.5, -23.5000003502))
            make_face()
            # Profile area: 11.4999998324, perimeter: 47.0000006706
            with BuildLine():
                Line((-5.0000000149, -0.5), (-5.0000000149, -23.5000003502))
                Line((-5.5, -0.5), (-5.0000000149, -0.5))
                Line((-5.5, -23.5000003502), (-5.5, -0.5))
                Line((-5.0000000149, -23.5000003502), (-5.5, -23.5000003502))
            make_face()
            # Profile area: 11.4999998324, perimeter: 47.0000006706
            with BuildLine():
                Line((-4.0000000149, -0.5), (-4.0000000149, -23.5000003502))
                Line((-4.5, -0.5), (-4.0000000149, -0.5))
                Line((-4.5, -23.5000003502), (-4.5, -0.5))
                Line((-4.0000000149, -23.5000003502), (-4.5, -23.5000003502))
            make_face()
            # Profile area: 11.4999998324, perimeter: 47.0000006706
            with BuildLine():
                Line((-3.0000000149, -0.5), (-3.0000000149, -23.5000003502))
                Line((-3.5, -0.5), (-3.0000000149, -0.5))
                Line((-3.5, -23.5000003502), (-3.5, -0.5))
                Line((-3.0000000149, -23.5000003502), (-3.5, -23.5000003502))
            make_face()
            # Profile area: 11.4999998324, perimeter: 47.0000006706
            with BuildLine():
                Line((-2.0000000149, -0.5), (-2.0000000149, -23.5000003502))
                Line((-2.5, -0.5), (-2.0000000149, -0.5))
                Line((-2.5, -23.5000003502), (-2.5, -0.5))
                Line((-2.0000000149, -23.5000003502), (-2.5, -23.5000003502))
            make_face()
            # Profile area: 11.4999998324, perimeter: 47.0000006706
            with BuildLine():
                Line((-1.5, -0.5), (-1.0000000149, -0.5))
                Line((-1.5, -23.5000003502), (-1.5, -0.5))
                Line((-1.0000000149, -23.5000003502), (-1.5, -23.5000003502))
                Line((-1.0000000149, -0.5), (-1.0000000149, -23.5000003502))
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)
    return part.part


def model_41776_50aabc9d_0003():
    """Model: Top Plastic Section v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude3 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 9 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 15.8354940042, perimeter: 19.7509283001
            with BuildLine():
                CenterArc((-3.2, 0), 1, 90, 101.1012508804)
                Line((-4.1812884606, -0.19254339), (-3.7812884606, -0.19254339))
                Line((-3.7812884606, -0.19254339), (-3.7812884606, -0.49254339))
                Line((-3.7812884606, -0.49254339), (-4.0702878885, -0.49254339))
                CenterArc((-3.2, 0), 1, -150.4921112515, 60.4921112515)
                Line((3.2, -1), (-3.2, -1))
                CenterArc((3.2, 0), 1, -90, 180)
                Line((-3.2, 1), (3.2, 1))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch3 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 12.9563288114, perimeter: 18.597560734
            with BuildLine():
                CenterArc((-3.2, 0), 0.85, 90, 180)
                Line((-3.2, -0.85), (3.2, -0.85))
                CenterArc((3.2, 0), 0.85, -90, 40.8930048274)
                Line((3.7564512485, -0.64254339), (3.6312884606, -0.64254339))
                Line((3.6312884606, -0.64254339), (3.6312884606, -0.04254339))
                Line((3.6312884606, -0.04254339), (4.0489346618, -0.04254339))
                CenterArc((3.2, 0), 0.85, -2.8689124331, 92.8689124331)
                Line((3.2, 0.85), (-3.2, 0.85))
            make_face()
        # OneSide extrude, distance=-0.15
        extrude(amount=-0.15, mode=Mode.SUBTRACT)
    return part.part


def model_41776_50aabc9d_0006():
    """Model: Top Minus 1 Plate v2 (1)"""
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
        # Sketch has 17 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 15.5331856019, perimeter: 23.4814150876
            with BuildLine():
                CenterArc((-3.2, 0), 1, 90, 180)
                Line((3.1999990631, -1), (-3.2, -1))
                CenterArc((3.2, 0), 1, -90.0000536822, 180.0000536724)
                Line((-3.2, 1), (3.2000000002, 1))
            make_face()
            with BuildLine():
                CenterArc((-3.38015193, -0.19824781), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.1, 0.6), 0.1000000104, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.9797958971, 0.2), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.3802792094, -0.1976174882), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 9 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 4.2040118144, perimeter: 11.7913373868
            with BuildLine():
                CenterArc((1.9624956574, -0.6521619039), 0.5, 0, 89.9263056447)
                _nurbs_edge([(1.9631387618, -0.1521623175), (1.801832363, -0.1519548436), (1.4526669166, -0.1527885275), (0.8493517955, -0.1577821247), (-0.0755148718, -0.1713665587), (-1.2467920944, -0.1993775933), (-2.0170941951, -0.2321212398), (-2.4013361127, -0.2642702853), (-2.553491965, -0.2895244995), (-2.603543004, -0.3031078001)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.2, 0.4, 0.6, 0.8, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((-2.5249695025, -0.5926353547), 0.3, 105.1835242523, 74.8164757477)
                Line((-2.8249695025, -1), (-2.8249695025, -0.5926353547))
                Line((-2.8249695025, -1), (2.4624956574, -1))
                Line((2.4624956574, -1), (2.4624956574, -0.6521619039))
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)
    return part.part


def model_41778_3d8cc892_0008():
    """Model: plate"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 162.146390876, perimeter: 49.2173164369
            with Locations((6.3499999046, 6.3499999046)):
                Ellipse(10.1599998474, 5.08, rotation=180)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)

        # Sketch3 -> Extrude2 (NewBody)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.635, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 65.8719678689, perimeter: 106.2207210154
            with BuildLine():
                EllipticalCenterArc((-6.3499999046, -6.3499999046), 11.4299998283, 6.3499999046, 0, 360, 180)
            make_face()
            with BuildLine():
                EllipticalCenterArc((-6.3499999046, -6.3499999046), 10.1599998474, 5.08, 0, 360, 0)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


def model_41785_5fecc307_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 20.2682991639, perimeter: 15.9592906802
            Circle(2.54)
        # OneSide extrude, distance=17.272
        extrude(amount=17.272)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 17.272, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 18.2921399954, perimeter: 15.1613261462
            Circle(2.413)
        # OneSide extrude, distance=-17.018
        extrude(amount=-17.018, mode=Mode.SUBTRACT)
    return part.part


def model_41785_a4e25fe9_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7391931082, perimeter: 3.2004
            with BuildLine():
                Line((0.4117974414, 0.339025703), (-0.0877061506, 0.5261398969))
                Line((-0.0877061506, 0.5261398969), (-0.499503592, 0.187114194))
                Line((-0.499503592, 0.187114194), (-0.4117974414, -0.339025703))
                Line((-0.4117974414, -0.339025703), (0.0877061506, -0.5261398969))
                Line((0.0877061506, -0.5261398969), (0.499503592, -0.187114194))
                Line((0.499503592, -0.187114194), (0.4117974414, 0.339025703))
            make_face()
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.54, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0932433178, perimeter: 6.1921457862
            with BuildLine():
                Line((-0.499503592, 0.187114194), (-0.4117974414, -0.339025703))
                Line((-0.4117974414, -0.339025703), (0.0877061506, -0.5261398969))
                Line((0.0877061506, -0.5261398969), (0.499503592, -0.187114194))
                Line((0.499503592, -0.187114194), (0.4117974414, 0.339025703))
                Line((0.4117974414, 0.339025703), (-0.0877061506, 0.5261398969))
                Line((-0.0877061506, 0.5261398969), (-0.499503592, 0.187114194))
            make_face()
            with BuildLine():
                Line((-0.4669378098, 0.1749150423), (-0.384949775, -0.3169224841))
                Line((-0.0819880348, 0.4918375264), (-0.4669378098, 0.1749150423))
                Line((0.384949775, 0.3169224841), (-0.0819880348, 0.4918375264))
                Line((0.4669378098, -0.1749150423), (0.384949775, 0.3169224841))
                Line((0.0819880348, -0.4918375264), (0.4669378098, -0.1749150423))
                Line((-0.384949775, -0.3169224841), (0.0819880348, -0.4918375264))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.889
        extrude(amount=-0.889, mode=Mode.SUBTRACT)
    return part.part


def model_41785_d82bdc46_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 21.2943818091, perimeter: 16.3582729472
            Circle(2.6035)
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.27, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 19.2675518927, perimeter: 15.5603084132
            Circle(2.4765)
        # OneSide extrude, distance=-1.016
        extrude(amount=-1.016, mode=Mode.SUBTRACT)
    return part.part


def model_41789_6056d5cf_0008():
    """Model: Component14"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 11.7474999925, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3016.123, perimeter: 226.06
            with BuildLine():
                Line((-109.2199990082, 72.3899999619), (-66.0399990082, 72.3899999619))
                Line((-109.2199990082, 2.5399999619), (-109.2199990082, 72.3899999619))
                Line((-66.0399990082, 2.5399999619), (-109.2199990082, 2.5399999619))
                Line((-66.0399990082, 72.3899999619), (-66.0399990082, 2.5399999619))
            make_face()
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 13.0174999925, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 141.9352, perimeter: 226.06
            with BuildLine():
                Line((-67.3099990082, 3.8099999619), (-67.3099990082, 72.3899999619))
                Line((-109.2199990082, 3.8099999619), (-67.3099990082, 3.8099999619))
                Line((-109.2199990082, 2.5399999619), (-109.2199990082, 3.8099999619))
                Line((-66.0399990082, 2.5399999619), (-109.2199990082, 2.5399999619))
                Line((-66.0399990082, 72.3899999619), (-66.0399990082, 2.5399999619))
                Line((-67.3099990082, 72.3899999619), (-66.0399990082, 72.3899999619))
            make_face()
        # OneSide extrude, distance=27.305
        extrude(amount=27.305, mode=Mode.ADD)
    return part.part


def model_41789_6056d5cf_0010():
    """Model: Component22"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 11.7474999925, 60.9592197874), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 931.44975, perimeter: 166.37
            with BuildLine():
                Line((154.3049974823, 82.5499998093), (167.6399974823, 82.5499998093))
                Line((154.3049974823, 12.6999998093), (154.3049974823, 82.5499998093))
                Line((167.6399974823, 12.6999998093), (154.3049974823, 12.6999998093))
                Line((167.6399974823, 82.5499998093), (167.6399974823, 12.6999998093))
            make_face()
        # OneSide extrude, distance=10.16
        extrude(amount=10.16)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 21.9074999925, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 740.3211, perimeter: 158.75
            with BuildLine():
                Line((155.5749974823, 74.9292195967), (155.5749974823, 143.5092195967))
                Line((166.3699974823, 74.9292195967), (155.5749974823, 74.9292195967))
                Line((166.3699974823, 143.5092195967), (166.3699974823, 74.9292195967))
                Line((166.3699974823, 143.5092195967), (155.5749974823, 143.5092195967))
            make_face()
        # OneSide extrude, distance=-8.89
        extrude(amount=-8.89, mode=Mode.SUBTRACT)
    return part.part


def model_41789_6056d5cf_0013():
    """Model: Component2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3974.1855403137, perimeter: 253.9999983215
            with BuildLine():
                Line((50.7999992371, 5.0799999237), (-5.0799999237, 5.0799999237))
                Line((-5.0799999237, 5.0799999237), (-5.0799999237, -66.0400000763))
                Line((-5.0799999237, -66.0400000763), (50.7999992371, -66.0400000763))
                Line((50.7999992371, -66.0400000763), (50.7999992371, 5.0799999237))
            make_face()
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.27, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 42.7671598898, perimeter: 23.1824929915
            with Locations((0, -0.0003901063)):
                Circle(3.6896083528)
            # Profile area: 42.7671598898, perimeter: 23.1824929915
            with Locations((-45.72, -0.0003901063)):
                Circle(3.6896083528)
            # Profile area: 42.7671598898, perimeter: 23.1824929915
            with Locations((-45.72, 60.9596098937)):
                Circle(3.6896083528)
            # Profile area: 42.7671598898, perimeter: 23.1824929915
            with Locations((0, 60.9596098937)):
                Circle(3.6896083528)
        # OneSide extrude, distance=0.3175
        extrude(amount=0.3175, mode=Mode.ADD)
    return part.part


def model_41789_6056d5cf_0014():
    """Model: Component4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 11.7474999925, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2890.3167131836, perimeter: 223.5199966431
            with BuildLine():
                Line((86.359998703, 66.0399990082), (126.9999980927, 66.0399990082))
                Line((86.359998703, -5.0799999237), (86.359998703, 66.0399990082))
                Line((126.9999980927, -5.0799999237), (86.359998703, -5.0799999237))
                Line((126.9999980927, 66.0399990082), (126.9999980927, -5.0799999237))
            make_face()
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 13.0174999925, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 42.7671598898, perimeter: 23.1824929915
            with Locations((121.92, -0.0003901063)):
                Circle(3.6896083528)
            # Profile area: 42.7671598898, perimeter: 23.1824929915
            with Locations((91.44, -0.0003901063)):
                Circle(3.6896083528)
            # Profile area: 42.7671598898, perimeter: 23.1824929915
            with Locations((121.92, 60.9596098937)):
                Circle(3.6896083528)
            # Profile area: 42.7671598898, perimeter: 23.1824929915
            with Locations((91.44, 60.9596098937)):
                Circle(3.6896083528)
        # OneSide extrude, distance=0.3175
        extrude(amount=0.3175, mode=Mode.ADD)
    return part.part


def model_41845_866e0992_0007():
    """Model: Back WHeel Place holder"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.002025, perimeter: 0.18
            with BuildLine():
                Line((11.0734234944, -0.0198858041), (11.0734234944, 0.0251141959))
                Line((11.0734234944, 0.0251141959), (11.0284234944, 0.0251141959))
                Line((11.0284234944, 0.0251141959), (11.0284234944, -0.0198858041))
                Line((11.0284234944, -0.0198858041), (11.0734234944, -0.0198858041))
            make_face()
        # OneSide extrude, distance=0.01
        extrude(amount=0.01)
    return part.part


def model_41845_a5180a74_0001():
    """Model: Wheel Cap"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            with Locations((-7.1999998391, -0.9999999776)):
                Circle(0.125)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0176714587, perimeter: 0.471238898
            with Locations((-7.1999998391, -0.9999999776)):
                Circle(0.075)
        # OneSide extrude, distance=-0.15
        extrude(amount=-0.15, mode=Mode.SUBTRACT)
    return part.part


def model_41845_a5180a74_0006():
    """Model: Wheels"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.4417864669, perimeter: 2.3561944902
            with Locations((-7.2000001073, -1.0000000149)):
                Circle(0.375)
        # OneSide extrude, distance=0.25
        extrude(amount=0.25)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.25), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((-7.2000001073, -1.0000000149)):
                Circle(0.1)
        # OneSide extrude, distance=-0.6
        extrude(amount=-0.6, mode=Mode.SUBTRACT)
    return part.part


def model_41859_173a686e_0002():
    """Model: E v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 13 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0311087305, perimeter: 0.6267520882
            with BuildLine():
                CenterArc((0.6999999844, 1.6799999624), 0.0999999978, -69.2788702623, 318.5577405246)
                Line((0.6646180055, 1.5864686034), (0.7353819632, 1.5864686034))
            make_face()
            # Profile area: 0.0003071947, perimeter: 0.1430943437
            with BuildLine():
                Line((0.6646180055, 1.5864686034), (0.7353819632, 1.5864686034))
                CenterArc((0.6999999844, 1.6799999624), 0.0999999978, -110.7211297377, 41.4422594754)
            make_face()
            # Profile area: 1.0374064718, perimeter: 7.8526063651
            with BuildLine():
                Line((0.7353819632, 1.5864686034), (0.9095060359, 1.5864686034))
                CenterArc((0.6999999844, 1.6799999624), 0.0999999978, -110.7211297377, 41.4422594754)
                Line((0.5266999824, 1.5864686034), (0.6646180055, 1.5864686034))
                CenterArc((0.5070808225, 1.1581286007), 0.4287890732, 87.377527285, 84.5440198702)
                Line((0.2686666395, 1.2674500865), (0.082546805, 1.2183858597))
                Line((0.2686666395, 0.4381783685), (0.2686666395, 1.2674500865))
                CenterArc((0.4875259858, 0.0989232608), 0.4037244624, 122.8267629156, 57.046296899)
                CenterArc((0.5080584139, -1.1937959403), 1.3614071302, 90, 18.157515732)
                Line((0.9257536554, 0.1676111899), (0.5080584139, 0.1676111899))
                CenterArc((0.9493995127, 0.5184954856), 0.3516801324, -93.8552951491, 99.5997853106)
                CenterArc((0.9851971952, 1.1181889874), 0.6460042088, -90, 29.0940785242)
                Line((0.5776605835, 0.4721847786), (0.9851971952, 0.4721847786))
                Line((0.5776605835, 0.7318014473), (0.5776605835, 0.4721847786))
                Line((0.7328828285, 0.7318014473), (0.5776605835, 0.7318014473))
                CenterArc((0.7536667039, 1.1251727218), 0.3939199526, -93.0244254732, 85.3747833157)
                CenterArc((0.8690169341, 1.620927664), 0.6133305223, -90, 26.645952203)
                Line((0.577495401, 1.0075971418), (0.8690169341, 1.0075971418))
                Line((0.577495401, 1.288321581), (0.577495401, 1.0075971418))
                Line((0.9284009501, 1.288321581), (0.577495401, 1.288321581))
                CenterArc((0.9433239166, 1.6433035557), 0.3552955071, -92.4072204101, 97.4944563821)
                CenterArc((0.9095060359, 2.4814549784), 0.894986375, -90, 25.6712189728)
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0122718463, perimeter: 0.3926990817
            with Locations((0.6999999844, 1.6799999624)):
                Circle(0.0625)
        # OneSide extrude, distance=-0.43
        extrude(amount=-0.43, mode=Mode.SUBTRACT)
    return part.part


def model_41859_173a686e_0003():
    """Model: LightningBolt v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0187261745, perimeter: 1.0560833154
            with BuildLine():
                CenterArc((0.5500000082, 2.0500000305), 0.1000000015, -35.370206215, 343.7939537393)
                Line((0.6121472638, 1.9716564352), (0.6000000089, 2.0000000298))
                Line((0.6000000089, 2.0000000298), (0.6315429006, 1.9921143069))
            make_face()
            with BuildLine():
                CenterArc((0.5500000082, 2.0500000305), 0.0625, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.6745821135, perimeter: 5.3009296659
            with BuildLine():
                Line((0.6315429006, 1.9921143069), (1.0000000149, 1.9000000283))
                CenterArc((0.5500000082, 2.0500000305), 0.1000000015, -51.5762524757, 16.2060462607)
                Line((0.9000000134, 1.3000000194), (0.6121472638, 1.9716564352))
                Line((0.5000000075, 1.2000000179), (0.9000000134, 1.3000000194))
                Line((1.4000000209, 0), (0.5000000075, 1.2000000179))
                Line((1.1000000164, 0.9000000134), (1.4000000209, 0))
                Line((1.4000000209, 1.0000000149), (1.1000000164, 0.9000000134))
                Line((1.0000000149, 1.9000000283), (1.4000000209, 1.0000000149))
            make_face()
            # Profile area: 0.0004179066, perimeter: 0.0916354677
            with BuildLine():
                Line((0.6000000089, 2.0000000298), (0.6315429006, 1.9921143069))
                Line((0.6121472638, 1.9716564352), (0.6000000089, 2.0000000298))
                CenterArc((0.5500000082, 2.0500000305), 0.1000000015, -51.5762524757, 16.2060462607)
            make_face()
            # Profile area: 0.0122718463, perimeter: 0.3926990817
            with Locations((0.5500000082, 2.0500000305)):
                Circle(0.0625)
        # OneSide extrude, distance=0.25
        extrude(amount=0.25)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.25), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0122718463, perimeter: 0.3926990817
            with Locations((0.5500000082, 2.0500000305)):
                Circle(0.0625)
        # OneSide extrude, distance=-0.54
        extrude(amount=-0.54, mode=Mode.SUBTRACT)
    return part.part


def model_41859_173a686e_0005():
    """Model: Heart v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.0501600476, perimeter: 4.4385290259
            with BuildLine():
                CenterArc((-0.1399056506, 1.8435844732), 1.7887304691, -46.0830088066, 12.2932513193)
                CenterArc((1.0376177132, 1.0266422282), 0.3565831389, -29.919021585, 174.8956585883)
                CenterArc((0.4477929824, 1.0357564542), 0.3562655908, 33.2874187442, 74.6816334913)
                CenterArc((0.2565227179, 1.4327854403), 0.1, -35.5496762631, 302.5445998131)
                CenterArc((0.4477929824, 1.0357564542), 0.3562655908, 123.4761950514, 88.1787707861)
                CenterArc((0.772610658, 1.115868099), 0.6825071078, -156.9631473193, 32.2142674678)
                CenterArc((-0.1748445037, -0.341711492), 1.0564518552, 29.7691876944, 28.3199757015)
                CenterArc((1.9506884463, -0.6224792502), 1.4522335483, 125.8198393989, 20.5019701118)
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.020106193, perimeter: 0.5026548246
            with Locations((0.2565227179, 1.4327854403)):
                Circle(0.08)
        # OneSide extrude, distance=-0.6
        extrude(amount=-0.6, mode=Mode.SUBTRACT)
    return part.part


def model_41859_173a686e_0009():
    """Model: Cat v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.6250331672, perimeter: 5.8204662579
            with BuildLine():
                CenterArc((0.9504469308, 1.4364245074), 0.0832690063, 31.722719851, 54.3489129279)
                CenterArc((0.8654147971, 1.5368773678), 0.0923862499, -10.8429602339, 35.8968417967)
                CenterArc((0.9349999791, 1.6749999626), 0.0999999978, -81.8893984723, 336.4153603109)
                CenterArc((0.9434574238, 1.5586223191), 0.0404320669, 150.3487946651, 37.0584447834)
                CenterArc((0.7932319863, 1.4980607201), 0.1232570787, 26.6829935253, 13.2685863084)
                CenterArc((0.8780220488, 1.5655610952), 0.0151562199, 50.2215705179, 79.5568589641)
                CenterArc((0.9035600784, 1.5073407372), 0.0782502564, 116.7622755923, 42.6635649333)
                CenterArc((0.9398070183, 1.3584641055), 0.2076050638, 121.8349332744, 61.3604164119)
                CenterArc((1.0219071593, 1.0543194076), 0.4115106048, 134.6859099456, 24.8551210126)
                CenterArc((0.7533995111, 0.7816413237), 0.43264928, 105.695998025, 106.3877364402)
                CenterArc((0.4921756006, 0.4031994298), 0.1821842129, 125.3275551675, 132.94916668)
                CenterArc((0.6142467652, 0.8649517219), 0.6596085528, -103.9565439666, 37.493349378)
                CenterArc((0.8737409165, 0.2795510559), 0.0197229169, -78.5576637216, 203.9727130607)
                CenterArc((0.6897962519, 0.8659562305), 0.5958519393, -112.8508740149, 39.6805247353)
                CenterArc((0.4890594492, 0.3917170245), 0.0808828717, 112.2703304021, 135.4593391959)
                CenterArc((0.5938097648, 1.0893368506), 0.6373200659, -102.2663735508, 11.9354379655)
                CenterArc((0.7259141804, -0.7241148127), 1.1839544939, 84.8892134865, 11.6964224986)
                CenterArc((0.8359871773, 0.4912487418), 0.0364083887, -97.2650492414, 150.8728627043)
                CenterArc((0.8095563324, 0.4660041883), 0.0726846761, 48.6367335611, 47.7761978195)
                CenterArc((0.4789933408, 0.6544587476), 0.3427516634, -19.8216244843, 26.246446273)
                CenterArc((0.8282135984, 0.6812675964), 0.0144086688, 53.249141499, 73.5017170021)
                CenterArc((-0.3596340526, 0.2004682931), 1.2938085559, 15.9683084116, 6.3987441123)
                CenterArc((1.014315632, 0.6060805864), 0.1392285169, -159.0955119744, 66.5744358135)
                CenterArc((1.0071635857, 0.5079951092), 0.0410211601, -88.564258321, 126.688566053)
                CenterArc((0.9662787985, 0.4669868276), 0.098751164, 42.2002442677, 45.3707826715)
                CenterArc((-1.1629131297, 0.5333203296), 2.1336220298, 0.8681868169, 9.2591270623)
                CenterArc((0.7856519081, 1.0951092195), 0.2405722125, -50.8720821475, 80.6480334587)
                CenterArc((1.0463439887, 1.2641020458), 0.0717228584, 80.8157572285, 142.851404341)
                CenterArc((1.0509446215, 1.3664569002), 0.0322858642, -77.7560074895, 74.2662322704)
                CenterArc((1.1256324089, 1.3787543718), 0.0447931812, 161.4330306003, 37.1339387993)
                CenterArc((1.0351860615, 1.3980040735), 0.0482430049, -5.9333788606, 78.9680817442)
                CenterArc((1.0613611282, 1.4824281672), 0.0401467884, -176.8299970358, 69.2914592867)
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.020106193, perimeter: 0.5026548246
            with Locations((0.9349999791, 1.6749999626)):
                Circle(0.08)
        # OneSide extrude, distance=-0.45
        extrude(amount=-0.45, mode=Mode.SUBTRACT)
    return part.part


def model_41878_3aeaed3d_0000():
    """Model: Component15"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-1.6241759518, 1.6241759518, 0), x_dir=(0, 0, 1), z_dir=(-0.7071067812, 0.7071067812, 0))):
            # Profile area: 0.5, perimeter: 3
            with BuildLine():
                Line((-22, 3.5), (-22, 4.5))
                Line((-22.5, 4.5), (-22, 4.5))
                Line((-22.5, 4.5), (-22.5, 3.5))
                Line((-22.5, 3.5), (-22, 3.5))
            make_face()
            # Profile area: 1.5, perimeter: 5
            with BuildLine():
                Line((-21, 4.5), (-21, 3.5))
                Line((-21, 3.5), (-19.5, 3.5))
                Line((-19.5, 4.5), (-19.5, 3.5))
                Line((-21, 4.5), (-19.5, 4.5))
            make_face()
            # Profile area: 1, perimeter: 4
            with BuildLine():
                Line((-22, 3.5), (-21, 3.5))
                Line((-21, 4.5), (-21, 3.5))
                Line((-22, 4.5), (-21, 4.5))
                Line((-22, 3.5), (-22, 4.5))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-1.9777293424, 1.9777293424, 0), x_dir=(0, 0, 1), z_dir=(-0.7071067812, 0.7071067812, 0))):
            # Profile area: 1.5, perimeter: 5
            with BuildLine():
                Line((-19.5, 3.5), (-19.5, 4.5))
                Line((-19.5, 4.5), (-21, 4.5))
                Line((-21, 4.5), (-21, 3.5))
                Line((-21, 3.5), (-19.5, 3.5))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


def model_41892_7b3433f9_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch8 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.4525725529, perimeter: 32.0040010214
            with BuildLine():
                Line((-7.3660002351, 3.2630881762), (4.5330882168, 3.2630881762))
                Line((4.5330882168, 3.2630881762), (4.5330882168, 0.2540000081))
                Line((4.5330882168, 0.2540000081), (5.0800001621, 0.2540000081))
                Line((5.0800001621, 3.8100001216), (5.0800001621, 0.2540000081))
                Line((-7.3660002351, 3.8100001216), (5.0800001621, 3.8100001216))
                Line((-7.3660002351, 3.2630881762), (-7.3660002351, 3.8100001216))
            make_face()
        # OneSide extrude, distance=5.08
        extrude(amount=5.08)

        # Sketch12 -> Extrude6 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.5483802265, perimeter: 8.1280002594
            with BuildLine():
                Line((3.5559999595, -3.8100001216), (3.5559999595, -2.5400000811))
                Line((3.5559999595, -2.5400000811), (0.7619998703, -2.5400000811))
                Line((0.7619998703, -2.5400000811), (0.7619998703, -3.8100001216))
                Line((0.7619998703, -3.8100001216), (3.5559999595, -3.8100001216))
            make_face()
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)
    return part.part


def model_41896_7d8659e6_0005():
    """Model: Front Wheel Holder v5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 24.9492507386, perimeter: 21.1838015365
            with BuildLine():
                CenterArc((0, 0.4223063675), 1.0822282972, -157.0318544891, 134.0637089783)
                CenterArc((0, 0.4223063675), 1.0822282972, -22.9681455109, 4.5331966879)
                Line((3, 6), (1.0266919102, 0.0800757307))
                Line((-3, 6), (3, 6))
                Line((-1.0266919102, 0.0800757307), (-3, 6))
                CenterArc((0, 0.4223063675), 1.0822282972, -161.5650511771, 4.5331966879)
            make_face()
        # OneSide extrude, distance=3.6
        extrude(amount=3.6)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 18.0051715132, perimeter: 18.9167418295
            with BuildLine():
                Line((3.8172524048, -3.1411185099), (-3, -3.1411185099))
                Line((3.8172524048, -0.5), (3.8172524048, -3.1411185099))
                Line((-3, -0.5), (3.8172524048, -0.5))
                Line((-3, -3.1411185099), (-3, -0.5))
            make_face()
        # OneSide extrude, distance=7.5
        extrude(amount=7.5, mode=Mode.SUBTRACT)
    return part.part


def model_41896_7d8659e6_0008():
    """Model: Base Neck Clamp v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 10 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.215909709, perimeter: 1.9683769428
            with BuildLine():
                Line((0.200000003, -1.4866068743), (0.200000003, -1.0816653821))
                CenterArc((0, 0), 1.5, -82.3377442244, 20.1558839595)
                Line((0.7000000104, -0.8485281288), (0.7000000104, -1.3266499106))
                CenterArc((0, 0), 1.1, -79.5243181457, 29.0455152087)
            make_face()
            # Profile area: 0.215909709, perimeter: 1.9683769428
            with BuildLine():
                Line((-0.7000000104, -1.3266499106), (-0.7000000104, -0.8485281288))
                CenterArc((0, 0), 1.5, -117.8181397351, 20.1558839595)
                Line((-0.200000003, -1.0816653821), (-0.200000003, -1.4866068743))
                CenterArc((0, 0), 1.1, -129.521197063, 29.0455152087)
            make_face()
            # Profile area: 0.2385733862, perimeter: 2.0144230872
            with BuildLine():
                Line((-0.7000000104, -1.9000000283), (-0.7000000104, -1.3266499106))
                Line((-0.200000003, -1.9000000283), (-0.7000000104, -1.9000000283))
                Line((-0.200000003, -1.4866068743), (-0.200000003, -1.9000000283))
                CenterArc((0, 0), 1.5, -117.8181397351, 20.1558839595)
            make_face()
            # Profile area: 2.6747830804, perimeter: 14.3184659431
            with BuildLine():
                CenterArc((0, 0), 1.1, -50.478802937, 280.9576058741)
                Line((0.7000000104, -0.8485281288), (0.7000000104, -1.3266499106))
                CenterArc((0, 0), 1.5, -62.1818602649, 304.3637205297)
                Line((-0.7000000104, -1.3266499106), (-0.7000000104, -0.8485281288))
            make_face()
            # Profile area: 0.2385733862, perimeter: 2.0144230872
            with BuildLine():
                CenterArc((0, 0), 1.5, -82.3377442244, 20.1558839595)
                Line((0.200000003, -1.9000000283), (0.200000003, -1.4866068743))
                Line((0.7000000104, -1.9000000283), (0.200000003, -1.9000000283))
                Line((0.7000000104, -1.3266499106), (0.7000000104, -1.9000000283))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.7000000104, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-0.4999999888, -1.6399999633)):
                Circle(0.15)
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.SUBTRACT)
    return part.part


def model_41896_7d8659e6_0020():
    """Model: Brake #2 v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 12 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 6.3428306836, perimeter: 22.7478181888
            with BuildLine():
                CenterArc((-4.2999514524, 5.1362525977), 0.3, 28.7200782014, 61.2799217986)
                Line((-4.2999514524, 5.4362525977), (-4.4184822246, 5.4362525977))
                CenterArc((-4.4184822246, 5.1362525977), 0.3, 90, 118.6581945462)
                Line((-2.1533014073, 0.3660958403), (-4.6817311211, 4.9923775878))
                CenterArc((-1.8900525108, 0.5099708502), 0.3, -151.3418054538, 59.6133293109)
                Line((1.6372382931, 0.1033920963), (-1.899101418, 0.2101073525))
                Line((1.5917361224, 1.0763793943), (1.6372382931, 0.1033920963))
                Line((-1.5014967802, 0.9925770545), (1.5917361224, 1.0763793943))
                CenterArc((-1.509621445, 1.2924670173), 0.3, -151.2799217986, 62.8318082247)
                Line((-4.036858105, 5.2804118518), (-1.7727147925, 1.1483077632))
            make_face()
            with BuildLine():
                CenterArc((-4.3474291139, 5.1362525977), 0.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.0742771358, 0.5589204076), 0.375, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3.5
        extrude(amount=3.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 20.2173018678, perimeter: 19.7187809112
            with BuildLine():
                Line((-5.1177744512, -0.293112218), (1.8329584237, -0.293112218))
                Line((-5.1177744512, -3.2017697986), (-5.1177744512, -0.293112218))
                Line((1.8329584237, -3.2017697986), (-5.1177744512, -3.2017697986))
                Line((1.8329584237, -0.293112218), (1.8329584237, -3.2017697986))
            make_face()
        # OneSide extrude, distance=7
        extrude(amount=7, mode=Mode.SUBTRACT)
    return part.part


def model_41902_43d78d0f_0008():
    """Model: Chair CupHolder v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 110.0624659764, perimeter: 81.9827437645
            with BuildLine():
                Line((8.2132137859, 0.4562780189), (8.2132137859, 1.0912780189))
                Line((8.2132137859, 1.0912780189), (-12.1067862141, 1.0912780189))
                Line((-12.1067862141, 1.0912780189), (-12.1067862141, -2.1345219811))
                Line((-12.1067862141, -2.1345219811), (-11.5001223235, -9.0687219811))
                Line((-11.5001223235, -9.0687219811), (-2.5534501048, -9.0687219811))
                Line((-1.9467862141, -2.1345219811), (-2.5534501048, -9.0687219811))
                Line((8.2132137859, -2.1345219811), (-1.9467862141, -2.1345219811))
                Line((8.2132137859, -1.4995219811), (8.2132137859, -2.1345219811))
                Line((8.2132137859, -1.4995219811), (-2.8742059328, -1.5077759822))
                Line((-2.8742059328, 0.4562780189), (-2.8742059328, -1.5077759822))
                Line((8.2132137859, 0.4562780189), (-2.8742059328, 0.4562780189))
            make_face()
        # OneSide extrude, distance=10.16
        extrude(amount=10.16)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 13 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -1.0912780189), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 30.0300965, perimeter: 55.2894967108
            with BuildLine():
                Line((2.8742059328, 0), (7.9203419421, 0.4781311894))
                Line((13.5459271747, 0), (2.8742059328, 0))
                Line((13.5459271747, 10.16), (13.5459271747, 0))
                Line((2.8742059328, 10.16), (13.5459271747, 10.16))
                Line((2.8742059328, 10.16), (7.9203419421, 9.6818688106))
                CenterArc((7.4843059328, 5.08), 4.6224802813, -84.5872733515, 169.174546703)
            make_face()
        # OneSide extrude, distance=-28.194
        extrude(amount=-28.194, mode=Mode.SUBTRACT)
    return part.part


def model_41902_43d78d0f_0013():
    """Model: Back Support v2"""
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
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 482.1023631765, perimeter: 127.6953141121
            with BuildLine():
                CenterArc((42.7498419276, -4.7051820534), 6.0325, -90, 180)
                Line((42.7498419276, 1.3273179466), (-1.0651580724, 1.3273179466))
                CenterArc((-1.0651580724, -4.7051820534), 6.0325, 90, 180)
                Line((0.2170893859, -10.7376820534), (-1.0651580724, -10.7376820534))
                _nurbs_edge([(0.2170893859, -10.7376820534), (1.0422373761, -10.285396483), (2.6920536173, -9.4202680696), (5.1653388087, -8.240899734), (8.4601262924, -6.9089842044), (12.5734022426, -5.6723092146), (16.6810020534, -4.9023094338), (20.7824589501, -4.6373616684), (24.8775116529, -4.8989475698), (28.9664054945, -5.6668965997), (33.0496018542, -6.9032755546), (36.3119732015, -8.2365177718), (38.7565466235, -9.4177452131), (40.3852981774, -10.2844923672), (41.1994329323, -10.7376820534)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                Line((42.7498419276, -10.7376820534), (41.1994329323, -10.7376820534))
            make_face()
        # OneSide extrude, distance=1.905
        extrude(amount=1.905)
    return part.part


def model_41902_43d78d0f_0016():
    """Model: bottom seat tilt v1"""
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
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.4952911825, perimeter: 13.5297467767
            with BuildLine():
                Line((-8.2990988133, 4.3126528087), (-3.2190988133, 4.3126528087))
                Line((-3.2190988133, 6.2176528087), (-3.2190988133, 4.3126528087))
                _nurbs_edge([(-3.7695516309, 6.2176528087), (-3.7648733018, 6.2174722234), (-3.6998010822, 6.214974046), (-3.5829332791, 6.2108626723), (-3.4353606686, 6.2070562868), (-3.3269861998, 6.2070833779), (-3.2586388071, 6.2109037422), (-3.2295351633, 6.2151241796), (-3.2190988133, 6.2176528087)], [1, 1, 1, 1, 1, 1, 1, 1, 1], [0.7948628881, 0.7948628881, 0.7948628881, 0.7948628881, 0.7948628881, 0.7948628881, 0.8, 0.8666666667, 0.9333333333, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(-8.2990988133, 5.6263531877), (-8.2675994043, 5.6630380953), (-8.1990776616, 5.7338153233), (-8.0797264599, 5.8322034798), (-7.8872118051, 5.9477185762), (-7.5902823969, 6.0654898827), (-7.2376448653, 6.1563053116), (-6.8325934761, 6.2204862733), (-6.382729173, 6.2595399956), (-5.9020072737, 6.2768603831), (-5.4088368075, 6.2771357349), (-4.9240701335, 6.2657450543), (-4.4761985305, 6.248516796), (-4.1578540135, 6.2341208961), (-3.9491537184, 6.2248770941), (-3.8255861317, 6.2198157618), (-3.7695516309, 6.2176528087)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.7948628881, 0.7948628881, 0.7948628881, 0.7948628881, 0.7948628881, 0.7948628881], 5)
                Line((-8.2990988133, 5.6263531877), (-8.2990988133, 4.3126528087))
            make_face()
        # OneSide extrude, distance=48.26
        extrude(amount=48.26)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -4.3126528087), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 34.9981663301, perimeter: 56.2139151429
            with BuildLine():
                _nurbs_edge([(-8.2990988133, 10.16), (-8.1546091178, 10.7188), (-7.878247943, 11.8364), (-7.5015596695, 13.5128), (-7.0762711671, 15.748), (-6.6816368664, 18.542), (-6.436220337, 21.336), (-6.3521988839, 24.13), (-6.436220337, 26.924), (-6.6816368664, 29.718), (-7.0762711671, 32.512), (-7.5015596695, 34.7472), (-7.878247943, 36.4236), (-8.1546091178, 37.5412), (-8.2990988133, 38.1)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                Line((-8.2990988133, 10.16), (-8.2990988133, 38.1))
            make_face()
        # OneSide extrude, distance=-12.7
        extrude(amount=-12.7, mode=Mode.SUBTRACT)
    return part.part


def model_41902_43d78d0f_0025():
    """Model: Backbones of Seat v1 (1)"""
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
        # Sketch has 27 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 427.8945580571, perimeter: 178.8198194898
            with BuildLine():
                Line((26.6015046391, -4.1775585898), (31.6815046391, -4.1775585898))
                Line((31.6815046391, -4.1775585898), (31.6815046391, 79.0875234983))
                _nurbs_edge([(26.6015046123, 80.8999894979), (27.1887942125, 80.7328157588), (28.2032882982, 80.4220515379), (29.2188730732, 80.0738216772), (30.2355092139, 79.6894769599), (31.2531651949, 79.2701002957), (31.6815046391, 79.0875234983)], [1, 1, 1, 1, 1, 1, 1], [0.7248195579, 0.7248195579, 0.7248195579, 0.7248195579, 0.7248195579, 0.7248195579, 0.8, 0.8546049205, 0.8546049205, 0.8546049205, 0.8546049205, 0.8546049205, 0.8546049205], 5)
                Line((26.6015046391, -4.1775585898), (26.6015046123, 80.8999894979))
            make_face()
            # Profile area: 435.8355225101, perimeter: 181.7048709892
            with BuildLine():
                Line((20.8865046391, -4.1775585898), (25.9665046391, -4.1775585898))
                Line((25.9665046391, -4.1775585898), (25.9665045752, 81.0747581734))
                _nurbs_edge([(20.8865046494, 82.022162349), (21.0565100804, 82.0044296159), (22.0037714995, 81.8988976069), (23.018709819, 81.7458854365), (24.0348676895, 81.5509811743), (25.0522035697, 81.315611776), (25.8996930178, 81.0925134328), (25.9665045752, 81.0747581734)], [1, 1, 1, 1, 1, 1, 1, 1], [0.5781219568, 0.5781219568, 0.5781219568, 0.5781219568, 0.5781219568, 0.5781219568, 0.6, 0.7, 0.7085574637, 0.7085574637, 0.7085574637, 0.7085574637, 0.7085574637, 0.7085574637], 5)
                Line((20.8865046391, -4.1775585898), (20.8865046494, 82.022162349))
            make_face()
            # Profile area: 438.5204245647, perimeter: 182.6642880387
            with BuildLine():
                Line((15.1715046391, -4.1775585898), (20.2515046391, -4.1775585898))
                Line((20.2515046391, -4.1775585898), (20.2515046391, 82.081636579))
                _nurbs_edge([(17.9398636103, 82.1824414069), (18.4016578785, 82.1806214218), (18.8637199546, 82.1696021238), (19.3260495799, 82.1493923948), (19.7886452428, 82.1200441655), (20.2515046391, 82.081636579)], [1, 1, 1, 1, 1, 1], [0.5021706198, 0.5021706198, 0.5021706198, 0.5021706198, 0.5021706198, 0.5021706198, 0.5617732124, 0.5617732124, 0.5617732124, 0.5617732124, 0.5617732124, 0.5617732124], 5)
                Line((17.7115027954, 82.1824414029), (17.9398636103, 82.1824414069))
                _nurbs_edge([(15.1715046456, 82.0610267945), (15.6788589612, 82.1074765387), (16.1865336093, 82.1429227243), (16.6945315569, 82.1672634382), (17.2028546232, 82.1804361843), (17.7115027954, 82.1824414029)], [1, 1, 1, 1, 1, 1], [0.4306101821, 0.4306101821, 0.4306101821, 0.4306101821, 0.4306101821, 0.4306101821, 0.4962751553, 0.4962751553, 0.4962751553, 0.4962751553, 0.4962751553, 0.4962751553], 5)
                Line((15.1715046456, 82.0610267945), (15.1715046391, -4.1775585898))
            make_face()
            # Profile area: 415.5394282221, perimeter: 174.2941416644
            with BuildLine():
                Line((-1.3384953609, -4.1775585898), (3.7415046391, -4.1775585898))
                Line((3.7415046391, 78.8903747691), (3.7415046391, -4.1775585898))
                _nurbs_edge([(-1.3384953609, 76.2322614003), (-0.5769668377, 76.6847072174), (0.4377408367, 77.2607218224), (1.4534716036, 77.8015927681), (2.4702367411, 78.3069326435), (3.488060783, 78.775898705), (3.7415046391, 78.8903747691)], [1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.1331452758, 0.1331452758, 0.1331452758, 0.1331452758, 0.1331452758, 0.1331452758], 5)
                Line((-1.3384953609, -4.1775585898), (-1.3384953609, 76.2322614003))
            make_face()
            # Profile area: 428.3617391989, perimeter: 178.9968468301
            with BuildLine():
                Line((4.3765046391, -4.1775585898), (9.4565046391, -4.1775585898))
                Line((9.4565046391, -4.1775585898), (9.4565046391, 80.9903612033))
                _nurbs_edge([(4.3765046391, 79.1714054736), (4.7609411722, 79.3380310638), (5.7751441723, 79.7635499201), (6.7904248016, 80.1520517529), (7.806816828, 80.5023766252), (8.8243620615, 80.8130883448), (9.4565046391, 80.9903612033)], [1, 1, 1, 1, 1, 1, 1], [0.1497499302, 0.1497499302, 0.1497499302, 0.1497499302, 0.1497499302, 0.1497499302, 0.2, 0.2822645277, 0.2822645277, 0.2822645277, 0.2822645277, 0.2822645277, 0.2822645277], 5)
                Line((4.3765046391, 79.1714054736), (4.3765046391, -4.1775585898))
            make_face()
            # Profile area: 415.3093980168, perimeter: 174.1787029615
            with BuildLine():
                Line((32.3165046391, -4.1775585898), (37.3965046391, -4.1775585898))
                Line((37.3965046391, -4.1775585898), (37.3965046391, 76.2322614003))
                _nurbs_edge([(32.3165046391, 78.8115560434), (32.5457428967, 78.7100230851), (33.560024371, 78.2531962419), (34.5752901209, 77.7625591178), (35.5915181724, 77.2388665231), (36.6086983097, 76.6824693747), (37.3965046391, 76.2322614003)], [1, 1, 1, 1, 1, 1, 1], [0.8707909567, 0.8707909567, 0.8707909567, 0.8707909567, 0.8707909567, 0.8707909567, 0.9, 1, 1, 1, 1, 1, 1], 5)
                Line((32.3165046391, -4.1775585898), (32.3165046391, 78.8115560434))
            make_face()
            # Profile area: 381.4302273097, perimeter: 180.4845188551
            with BuildLine():
                Line((10.0915046391, -4.1775585898), (14.5365046391, -4.1775585898))
                Line((14.5365046391, -4.1775585898), (14.5365046542, 81.9959900391))
                _nurbs_edge([(10.0915046391, 81.1620561512), (10.100831003, 81.164483809), (10.8790393564, 81.3667625941), (11.766977144, 81.5700369191), (12.655846252, 81.741319997), (13.5456746152, 81.8796522501), (14.4271069642, 81.9835989414), (14.5365046542, 81.9959900391)], [1, 1, 1, 1, 1, 1, 1, 1], [0.2987870095, 0.2987870095, 0.2987870095, 0.2987870095, 0.2987870095, 0.2987870095, 0.3, 0.4, 0.4141678606, 0.4141678606, 0.4141678606, 0.4141678606, 0.4141678606, 0.4141678606], 5)
                Line((10.0915046391, 81.1620561512), (10.0915046391, -4.1775585898))
            make_face()
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 4.1775585898), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 13.2474097653, perimeter: 35.5917354828
            with BuildLine():
                Line((20.2515046391, 1.2913291093), (20.2515046391, 2.54))
                _nurbs_edge([(20.2515046391, 1.2913291093), (20.5508474385, 1.2966098003), (21.6269862037, 1.3184949181), (23.4820768489, 1.3740638079), (26.1201873936, 1.4955436818), (29.5468025173, 1.7263846572), (32.6813451974, 2.0095413477), (35.0370786331, 2.2601442391), (36.6096776194, 2.4439286711), (37.3965046391, 2.54)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.5614462087, 0.5614462087, 0.5614462087, 0.5614462087, 0.5614462087, 0.5614462087, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                Line((20.2515046391, 2.54), (37.3965046391, 2.54))
            make_face()
            # Profile area: 3.2027038516, perimeter: 7.594065538
            with BuildLine():
                _nurbs_edge([(15.1715046391, 1.2961019034), (15.6789071374, 1.2861509826), (16.1866060562, 1.2785483308), (16.6946041351, 1.2733156519), (17.2029030525, 1.2704662431), (17.7115027954, 1.27)], [1, 1, 1, 1, 1, 1], [0.4302831142, 0.4302831142, 0.4302831142, 0.4302831142, 0.4302831142, 0.4302831142, 0.4959418977, 0.4959418977, 0.4959418977, 0.4959418977, 0.4959418977, 0.4959418977], 5)
                Line((17.7115027954, 1.27), (17.7115027954, 2.54))
                Line((15.1715046391, 2.54), (17.7115027954, 2.54))
                Line((15.1715046391, 2.54), (15.1715046391, 1.2961019034))
            make_face()
            # Profile area: 3.2086962494, perimeter: 7.5988006075
            with BuildLine():
                Line((17.7115027954, 1.27), (17.7115027954, 2.54))
                _nurbs_edge([(17.7115027954, 1.27), (17.7429372761, 1.2699711834), (18.250359007, 1.2696529845), (18.7580801486, 1.2717067446), (19.2661005842, 1.2761315377), (19.7744184825, 1.2829128568), (20.2515046391, 1.2913291093)], [1, 1, 1, 1, 1, 1, 1], [0.4959418977, 0.4959418977, 0.4959418977, 0.4959418977, 0.4959418977, 0.4959418977, 0.5, 0.5614462087, 0.5614462087, 0.5614462087, 0.5614462087, 0.5614462087, 0.5614462087], 5)
                Line((20.2515046391, 1.2913291093), (20.2515046391, 2.54))
                Line((17.7115027954, 2.54), (20.2515046391, 2.54))
            make_face()
            # Profile area: 12.6894541642, perimeter: 34.3184468869
            with BuildLine():
                Line((15.1715046391, 2.54), (15.1715046391, 1.2961019034))
                Line((-1.3384953609, 2.54), (15.1715046391, 2.54))
                _nurbs_edge([(-1.3384953609, 2.54), (-0.5759880688, 2.443408284), (0.9500953363, 2.2586921455), (3.2424268287, 2.0070192029), (6.3053877609, 1.7230989207), (9.610220185, 1.4967580175), (12.1538768544, 1.3775573876), (13.9309410876, 1.3225855991), (14.9374806907, 1.3006914626), (15.1715046391, 1.2961019034)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.4302831142, 0.4302831142, 0.4302831142, 0.4302831142, 0.4302831142, 0.4302831142], 5)
            make_face()
        # OneSide extrude, distance=-96.52
        extrude(amount=-96.52, mode=Mode.SUBTRACT)
    return part.part


def model_41907_7bcecdb1_0000():
    """Model: Knife"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.4151912755, perimeter: 15.4002640711
            with BuildLine():
                CenterArc((3.1250000273, 3.5000000599), 3.6250000347, 136.3971809053, 43.6028192166)
                Line((-0.5000000075, 3.5000000522), (-0.5, -0.0000000011))
                CenterArc((0, 0), 0.5, -179.999999878, 180)
                Line((0.5000000075, 6.0000000894), (0.5, 0.0000000011))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.05
        extrude(amount=0.05, both=True)
    return part.part


def model_41920_1455d829_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 78.5398163397, perimeter: 31.4159265359
            Circle(5)
        # OneSide extrude, distance=80
        extrude(amount=80)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 80, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.9329275694, perimeter: 9.8115382179
            with BuildLine():
                Line((-1, 2), (-1.0000000144, 4.8989794826))
                Line((1.0000000149, 2), (-1, 2))
                Line((1.0000000149, 4.8989794825), (1.0000000149, 2))
                CenterArc((0, 0), 5, 78.4630407929, 11.5369592071)
                CenterArc((0, 0), 5, 90, 11.5369592012)
            make_face()
        # OneSide extrude, distance=-20
        extrude(amount=-20, mode=Mode.SUBTRACT)
    return part.part


def model_41941_79d46bb4_0002():
    """Model: little house"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5806440371, perimeter: 3.0480000973
            with BuildLine():
                Line((17.2720005512, -4.826000154), (16.5100005269, -4.826000154))
                Line((17.2720005512, -4.0640001297), (17.2720005512, -4.826000154))
                Line((16.5100005269, -4.0640001297), (17.2720005512, -4.0640001297))
                Line((16.5100005269, -4.826000154), (16.5100005269, -4.0640001297))
            make_face()
        # OneSide extrude, distance=0.762
        extrude(amount=0.762)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.2193543947, perimeter: 2.349439494
            with BuildLine():
                Line((-4.9529999401, 0.7619999908), (-4.4449999463, 1.1937999856))
                Line((-3.9369999524, 0.7619999908), (-4.9529999401, 0.7619999908))
                Line((-4.4449999463, 1.1937999856), (-3.9369999524, 0.7619999908))
            make_face()
        # OneSide extrude, distance=1.016
        extrude(amount=1.016)
    return part.part


def model_41941_79d46bb4_0003():
    """Model: Big House"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.7096644283, perimeter: 10.6680003405
            with BuildLine():
                Line((19.8120006323, -16.0020005107), (16.5100005269, -16.0020005107))
                Line((19.8120006323, -13.9700004458), (19.8120006323, -16.0020005107))
                Line((16.5100005269, -13.9700004458), (19.8120006323, -13.9700004458))
                Line((16.5100005269, -16.0020005107), (16.5100005269, -13.9700004458))
            make_face()
        # OneSide extrude, distance=2.286
        extrude(amount=2.286)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.4084013632, perimeter: 5.9120801584
            with BuildLine():
                Line((-13.7160004377, 2.286000073), (-14.9860004783, 3.3949774889))
                Line((-14.9860004783, 3.3949774889), (-16.2560005188, 2.286000073))
                Line((-16.2560005188, 2.286000073), (-13.7160004377, 2.286000073))
            make_face()
        # OneSide extrude, distance=3.556
        extrude(amount=3.556)
    return part.part


def model_41941_79d46bb4_0010():
    """Model: chance cards (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 63.970948002, perimeter: 32.8502395956
            with BuildLine():
                Line((-12.7832530475, -31.1611754559), (-22.8599996567, -31.1611754559))
                Line((-12.7832530475, -24.8128022673), (-12.7832530475, -31.1611754559))
                Line((-22.8599996567, -24.8128022673), (-12.7832530475, -24.8128022673))
                Line((-22.8599996567, -31.1611754559), (-22.8599996567, -24.8128022673))
            make_face()
        # OneSide extrude, distance=3.81
        extrude(amount=3.81)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.1005418328, perimeter: 15.2957031596
            with BuildLine():
                Line((-10.1181097776, -31.1905226093), (-11.3882410155, -31.1905226093))
                Line((-10.1181097776, -24.8128022673), (-10.1181097776, -31.1905226093))
                Line((-11.3882410155, -24.8128022673), (-10.1181097776, -24.8128022673))
                Line((-11.3882410155, -31.1905226093), (-11.3882410155, -24.8128022673))
            make_face()
        # OneSide extrude, distance=4.064
        extrude(amount=4.064)
    return part.part


def model_41942_29c07f06_0003():
    """Model: Component69"""
    with BuildPart() as part:
        # Sketch1 -> 拉伸1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.0000000023, 0.0000000015, 6.5850913586), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 38.735107648, perimeter: 43.9275282877
            with BuildLine():
                Line((-68.2225209998, -13.5921385951), (-56.694808826, -29.136502133))
                Line((-54.9201614039, -27.7786156347), (-56.694808826, -29.136502133))
                Line((-66.6786365316, -12.4471926644), (-54.9201614039, -27.7786156347))
                CenterArc((-67.4505787657, -13.0196656297), 0.9610515641, -143.4393394831, 179.9999999998)
            make_face()
            # Profile area: 1.4474228403, perimeter: 10.635304759
            with BuildLine():
                CenterArc((-67.4505787657, -13.0196656297), 0.9610515641, -143.4393394831, 179.9999999998)
                Line((-66.6975374643, -12.422548466), (-66.6786365316, -12.4471926644))
                CenterArc((-67.4505787657, -13.0196656297), 0.9610515641, 38.4123338315, 178.1483266855)
            make_face()
            with BuildLine():
                Line((-67.0097232336, -13.6656271551), (-66.7000009962, -12.8000001922))
                Line((-67.9286928322, -13.6385572454), (-67.0097232336, -13.6656271551))
                Line((-68.1869250414, -12.7562001582), (-67.9286928322, -13.6385572454))
                Line((-67.4275517251, -12.2379433978), (-68.1869250414, -12.7562001582))
                Line((-66.7000009962, -12.8000001922), (-67.4275517251, -12.2379433978))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> 拉伸2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.0000000023, 0.0000000015, 7.0850913586), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.9608365273, perimeter: 5.7445818552
            with BuildLine():
                Line((-56.694808826, -29.136502133), (-54.9201614039, -27.7786156347))
                CenterArc((-55.8074851149, -28.4575588839), 1.1172767355, -142.5782843018, 180)
            make_face()
            # Profile area: 1.9608337028, perimeter: 5.7445805912
            with BuildLine():
                CenterArc((-55.8074851149, -28.4575588839), 1.1172767355, 37.5238987743, 178.175706562)
                Line((-56.7148116377, -29.1095296537), (-56.694808826, -29.136502133))
                Line((-56.694808826, -29.136502133), (-54.9201614039, -27.7786156347))
                CenterArc((-55.8074851149, -28.4575588839), 1.1172767355, 37.4217156982, 0.1021830762)
            make_face()
        # OneSide extrude, distance=10
        extrude(amount=10, mode=Mode.ADD)
    return part.part


def model_41942_29c07f06_0014():
    """Model: Component66"""
    with BuildPart() as part:
        # Sketch1 -> 拉伸1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 6.6350913586), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.2265180109, perimeter: 2.9474266807
            with BuildLine():
                CenterArc((-66.2341384708, -6.5807466241), 0.9167377583, 61.9021104142, 58.9516635453)
                CenterArc((-65.5321107376, -5.4771655787), 0.4, 161.9512344948, 65.54350785)
                CenterArc((-66.212418691, -4.5073628329), 0.8974932901, -127.786599689, 57.3137778821)
                CenterArc((-67.0074216806, -5.5327696225), 0.4, -40.7259974996, 92.9393978105)
            make_face()
            # Profile area: 0.5018365573, perimeter: 2.512692077
            with BuildLine():
                CenterArc((-65.5321107376, -5.4771655787), 0.4, 161.9512344948, 65.54350785)
                CenterArc((-66.2341384708, -6.5807466241), 0.9167377583, 53.1740659638, 8.7280444504)
                CenterArc((-65.5321107376, -5.4771655787), 0.4, -112.4185659667, 274.3698004615)
            make_face()
            # Profile area: 0.001705084, perimeter: 0.3576490743
            with BuildLine():
                CenterArc((-67.0074216806, -5.5327696225), 0.4, -66.4281168454, 25.7021193458)
                CenterArc((-66.2341384708, -6.5807466241), 0.9167377583, 120.8537739595, 11.138337736)
            make_face()
            # Profile area: 0.0008182673, perimeter: 0.2798810788
            with BuildLine():
                CenterArc((-66.2341384708, -6.5807466241), 0.9167377583, 53.1740659638, 8.7280444504)
                CenterArc((-65.5321107376, -5.4771655787), 0.4, -132.5052576553, 20.0866916885)
            make_face()
            # Profile area: 0.4832782819, perimeter: 2.9832928094
            with BuildLine():
                CenterArc((-67.0074216806, -5.5327696225), 0.4, -120.0098926922, 53.5817758468)
                CenterArc((-66.2341384708, -6.5807466241), 0.9167377583, 120.8537739595, 11.138337736)
                CenterArc((-67.0074216806, -5.5327696225), 0.4, -40.7259974996, 92.9393978105)
                CenterArc((-67.0074216806, -5.5327696225), 0.4, 52.213400311, 69.802092566)
                CenterArc((-67.0074216806, -5.5327696225), 0.4, 122.015492877, 117.9746144308)
            make_face()
            with BuildLine():
                CenterArc((-67.0074216806, -5.5327696225), 0.075, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)

        # Sketch2 -> 拉伸2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 6.6850913586), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0176714587, perimeter: 0.471238898
            with Locations((-65.5321107376, -5.4771655787)):
                Circle(0.075)
        # OneSide extrude, distance=-0.05
        extrude(amount=-0.05, mode=Mode.SUBTRACT)
    return part.part


def model_41970_24ba0c1b_0001():
    """Model: Top Plate"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 11 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 24.5514382511, perimeter: 24.0685838133
            with BuildLine():
                Line((6.000000149, 3.0000000447), (1.5, 3.0000000447))
                CenterArc((1.5, 1.5000000447), 1.5, 90, 180)
                Line((1.5, 0), (8.500000149, 0))
                CenterArc((8.500000149, 1.5), 1.5, -90, 90)
                Line((10.000000149, 1.5), (10.000000149, 2))
                Line((6.000000149, 2), (10.000000149, 2))
                Line((6.000000149, 3.0000000447), (6.000000149, 2))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((5.500000082, -2.5000000373)):
                Circle(0.25)
            # Profile area: 0.4417864669, perimeter: 2.3561944902
            with Locations((1.5000000224, -0.75)):
                Circle(0.375)
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)
    return part.part


def model_41970_24ba0c1b_0002():
    """Model: File"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.6013274466, perimeter: 12.4128315763
            with BuildLine():
                CenterArc((0, 0), 0.400000006, 90, 180)
                Line((0, -0.400000006), (4.5, -0.4))
                Line((4.5, -0.4), (4.5, -0.099999994))
                CenterArc((4, -0.099999994), 0.5, 0, 90)
                Line((4, 0.400000006), (0, 0.400000006))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0400000005, perimeter: 1.70000002
            with BuildLine():
                Line((-3.95, -0.400000006), (-3.95, 0.400000004))
                Line((-3.95, 0.400000004), (-4, 0.400000004))
                Line((-4, 0.400000004), (-4, -0.400000006))
                Line((-4, -0.400000006), (-3.95, -0.400000006))
            make_face()
        # OneSide extrude, distance=-0.02
        extrude(amount=-0.02, mode=Mode.SUBTRACT)
    return part.part


def model_41970_24ba0c1b_0011():
    """Model: Saw"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 10.2800481495, perimeter: 23.0928916725
            with BuildLine():
                CenterArc((8.7000001341, 0.4898333913), 0.3, 0, 91.9091524804)
                Line((0, 0.5), (8.6900056848, 0.7896668634))
                CenterArc((0, 0), 0.5, 90, 180)
                Line((9.0000001341, -0.5000000075), (0, -0.5))
                Line((9.0000001341, 0.4898333913), (9.0000001341, -0.5000000075))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.375, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0169931086, perimeter: 0.5550378488
            with BuildLine():
                Line((-8.9000001341, 0.5000000074), (-8.8393808752, 0.3950043711))
                CenterArc((-8.796079605, 0.4200043711), 0.05, -150, 120)
                Line((-8.7527783348, 0.3950043711), (-8.692159076, 0.5000000074))
                Line((-8.692159076, 0.5000000074), (-8.9000001341, 0.5000000074))
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)
    return part.part


def model_41973_0e5cd44c_0001():
    """Model: Base"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 120, perimeter: 44
            with BuildLine():
                Line((10, -12), (0, -12))
                Line((10, 0), (10, -12))
                Line((0, 0), (10, 0))
                Line((0, -12), (0, 0))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -1, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 80, perimeter: 36
            with BuildLine():
                Line((9, 1), (1, 1))
                Line((9, 11), (9, 1))
                Line((1, 11), (9, 11))
                Line((1, 1), (1, 11))
            make_face()
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.SUBTRACT)
    return part.part


def model_41978_0c8a92df_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            Circle(0.1)
        # OneSide extrude, distance=0.03
        extrude(amount=0.03)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.03), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0020555269, perimeter: 0.1607187391
            Circle(0.0255791818)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)
    return part.part


def model_41978_4adb96a6_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=1.7
        extrude(amount=1.7, mode=Mode.ADD)
    return part.part


def model_41978_4e426020_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 15 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.8626548246, perimeter: 5.3132741229
            with BuildLine():
                CenterArc((-0.1, -0.6), 0.4, 180, 90)
                Line((0.1, -1), (-0.1, -1))
                CenterArc((0.1, -0.6), 0.4, -90, 90)
                Line((0.5, 0.6), (0.5, -0.6))
                CenterArc((0.1, 0.6), 0.4, 0, 90)
                Line((-0.1, 1), (0.1, 1))
                CenterArc((-0.1, 0.6), 0.4, 90, 90)
                Line((-0.5, -0.6), (-0.5, 0.6))
            make_face()
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-0.400000006, 0)):
                Circle(0.2)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)
    return part.part


def model_41978_f3c5934a_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 185.1577613878, perimeter: 102.483188863
            with BuildLine():
                Line((-7, 0), (-7, -4))
                Line((-7, -4), (39.952, -4))
                CenterArc((41.5768403361, -2), 2.5768403361, 129.0911035965, 101.8177928071)
                Line((-7, 0), (39.952, 0))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4, perimeter: 8.2
            with BuildLine():
                Line((3.4, 0), (3.4, 4))
                Line((3.3, 4), (3.4, 4))
                Line((3.3, 0), (3.3, 4))
                Line((3.4, 0), (3.3, 0))
            make_face()
        # OneSide extrude, distance=0.05
        extrude(amount=0.05, mode=Mode.ADD)
    return part.part


def model_41982_f75ceb8f_0000():
    """Model: chest top v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 7.9521564044, perimeter: 11.5685834706
            with BuildLine():
                CenterArc((0, 0), 2.25, 0, 180)
                Line((-2.25, 0), (2.25, 0))
            make_face()
        # OneSide extrude, distance=9
        extrude(amount=9)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(9, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0764379874, perimeter: 2.2706476199
            with BuildLine():
                CenterArc((0, 0), 2.25, 153.6128069395, 26.3871930605)
                Line((-2.25, 1), (-2.0155750294, 0.9999786502))
                Line((-2.25, 0), (-2.25, 1))
            make_face()
        # OneSide extrude, distance=-9
        extrude(amount=-9, mode=Mode.ADD)
    return part.part


def model_41982_f75ceb8f_0002():
    """Model: bottom and back v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 202.5, perimeter: 63
            with BuildLine():
                Line((16, -4), (-6.5, -4))
                Line((16, 5), (16, -4))
                Line((-6.5, 5), (16, 5))
                Line((-6.5, -4), (-6.5, 5))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.2, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.8, perimeter: 18.4
            with BuildLine():
                Line((-6.3, 5), (-6.3, -4))
                Line((-6.5, 5), (-6.3, 5))
                Line((-6.5, -4), (-6.5, 5))
                Line((-6.3, -4), (-6.5, -4))
            make_face()
        # OneSide extrude, distance=15
        extrude(amount=15, mode=Mode.ADD)
    return part.part


def model_41982_f75ceb8f_0006():
    """Model: chair v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 21.5, perimeter: 22.2
            with BuildLine():
                Line((-7, 2.5), (-7, 0))
                Line((-7, 0), (1.6, 0))
                Line((1.6, 0), (1.6, 2.5))
                Line((1.6, 2.5), (-7, 2.5))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.72, perimeter: 17.6
            with BuildLine():
                Line((0, -1.6), (0, 7))
                Line((0, 7), (-0.2, 7))
                Line((-0.2, 7), (-0.2, -1.6))
                Line((-0.2, -1.6), (0, -1.6))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.ADD)
    return part.part


def model_41982_f75ceb8f_0021():
    """Model: top v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 72, perimeter: 34
            with BuildLine():
                Line((1, -3.5), (-7, -3.5))
                Line((1, 5.5), (1, -3.5))
                Line((-7, 5.5), (1, 5.5))
                Line((-7, -3.5), (-7, 5.5))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -1), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.8835729338, perimeter: 3.8561944902
            with BuildLine():
                Line((0, 5.5), (0, 4))
                CenterArc((0, 4.75), 0.75, -90, 180)
            make_face()
            # Profile area: 0.8835729338, perimeter: 3.8561944902
            with BuildLine():
                Line((0, 4), (0, 2.5))
                CenterArc((0, 3.25), 0.75, -90, 180)
            make_face()
            # Profile area: 0.8835729338, perimeter: 3.8561944902
            with BuildLine():
                Line((0, 2.5), (0, 1))
                CenterArc((0, 1.75), 0.75, -90, 180)
            make_face()
            # Profile area: 0.8835729338, perimeter: 3.8561944902
            with BuildLine():
                Line((0, 1), (0, -0.5))
                CenterArc((0, 0.25), 0.75, -90, 180)
            make_face()
            # Profile area: 0.8835729338, perimeter: 3.8561944902
            with BuildLine():
                Line((0, -0.5), (0, -2))
                CenterArc((0, -1.25), 0.75, -90, 180)
            make_face()
            # Profile area: 0.8835729338, perimeter: 3.8561944902
            with BuildLine():
                Line((0, -2), (0, -3.5))
                CenterArc((0, -2.75), 0.75, -90, 180)
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.ADD)
    return part.part


def model_41982_f75ceb8f_0023():
    """Model: bottom frame 2 v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.5446900494, perimeter: 5.6548667765
            Circle(0.9)
        # OneSide extrude, distance=20
        extrude(amount=20)
    return part.part


def model_42015_efbcca8b_0000():
    """Model: 5/32nd Allen"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(13.7160004377, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.4092223751, perimeter: 2.38125
            with BuildLine():
                Line((2.3883580937, 3.1954157332), (2.7320619258, 3.3938532332))
                Line((2.7320619258, 3.3938532332), (2.7320619258, 3.7907282332))
                Line((2.7320619258, 3.7907282332), (2.3883580937, 3.9891657332))
                Line((2.3883580937, 3.9891657332), (2.0446542615, 3.7907282332))
                Line((2.0446542615, 3.7907282332), (2.0446542615, 3.3938532332))
                Line((2.0446542615, 3.3938532332), (2.3883580937, 3.1954157332))
            make_face()
        # OneSide extrude, distance=-10.16
        extrude(amount=-10.16)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -2.7320619258), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 1.9457425139, perimeter: 11.3877130744
            with BuildLine():
                CenterArc((-13.9700004458, 2.507650238), 1.2515497166, 94.8831666834, 266.0740812404)
                Line((-13.084043632, 2.5285590666), (-12.7186253966, 2.5285590666))
                CenterArc((-13.9700004458, 2.507650238), 0.8862035066, 91.8104794681, 269.5414659923)
                CenterArc((-13.9700004458, 2.507650238), 0.8862035066, 88.3690817915, 3.4413976765)
                Line((-13.7160004377, 3.3938532332), (-13.9447781646, 3.3934947456))
                Line((-13.7160004377, 3.7907282332), (-13.7160004377, 3.3938532332))
                Line((-13.7160004377, 3.7907282332), (-14.0765376097, 3.7546572651))
            make_face()
        # OneSide extrude, distance=-0.6858
        extrude(amount=-0.6858, mode=Mode.ADD)
    return part.part


def model_42015_efbcca8b_0004():
    """Model: 1/4th Allen"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(13.7160004377, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.0476092803, perimeter: 3.81
            with BuildLine():
                Line((4.4902457943, 3.1954157332), (5.0401719257, 3.5129157332))
                Line((5.0401719257, 3.5129157332), (5.0401719257, 4.1479157332))
                Line((5.0401719257, 4.1479157332), (4.4902457943, 4.4654157332))
                Line((4.4902457943, 4.4654157332), (3.9403196629, 4.1479157332))
                Line((3.9403196629, 4.1479157332), (3.9403196629, 3.5129157332))
                Line((3.9403196629, 3.5129157332), (4.4902457943, 3.1954157332))
            make_face()
        # OneSide extrude, distance=-10.16
        extrude(amount=-10.16)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -5.0401719257), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 3.6936585305, perimeter: 14.1624856063
            with BuildLine():
                CenterArc((-13.9700004458, 2.507650238), 1.6082174332, 95.521193445, 265.2237440004)
                Line((-12.9289855089, 2.5285590666), (-12.3619189387, 2.5285590666))
                CenterArc((-13.9700004458, 2.507650238), 1.0412248931, 97.642652035, 263.5079813878)
                Line((-13.7160004377, 3.5922907332), (-14.1084773515, 3.5396257341))
                Line((-13.7160004377, 4.1479157332), (-13.7160004377, 3.5922907332))
                Line((-13.7160004377, 4.1479157332), (-14.1247333789, 4.1084066317))
            make_face()
        # OneSide extrude, distance=-1.09728
        extrude(amount=-1.09728, mode=Mode.ADD)
    return part.part


def model_42015_efbcca8b_0005():
    """Model: 5/16"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(13.7160004377, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.6368895005, perimeter: 4.7625
            with BuildLine():
                Line((5.9434705081, 3.1954157332), (6.6308781724, 3.5922907332))
                Line((6.6308781724, 3.5922907332), (6.6308781724, 4.3860407332))
                Line((6.6308781724, 4.3860407332), (5.9434705081, 4.7829157332))
                Line((5.9434705081, 4.7829157332), (5.2560628439, 4.3860407332))
                Line((5.2560628439, 4.3860407332), (5.2560628439, 3.5922907332))
                Line((5.2560628439, 3.5922907332), (5.9434705081, 3.1954157332))
            make_face()
        # OneSide extrude, distance=-10.16
        extrude(amount=-10.16)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -6.6308781724), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 5.2185401378, perimeter: 15.238792598
            with BuildLine():
                Line((-13.7160004377, 4.3860407332), (-13.7160004377, 3.5922907332))
                Line((-13.7160004377, 4.3860407332), (-14.2659794704, 4.2931916333))
                CenterArc((-13.9700004458, 2.5400000811), 1.7780000567, 99.5824886118, 260.4175113882)
                Line((-12.9540004134, 2.5400000811), (-12.1920003891, 2.5400000811))
                CenterArc((-13.9700004458, 2.5400000811), 1.0160000324, 96.618842173, 263.381157827)
                Line((-13.7160004377, 3.5922907332), (-14.0871084936, 3.5492283858))
            make_face()
        # OneSide extrude, distance=-1.3843
        extrude(amount=-1.3843, mode=Mode.ADD)
    return part.part


def model_42044_ee2c1949_0005():
    """Model: 2mm Bolt"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1385640687, perimeter: 1.3856406667
            with BuildLine():
                Line((1.1000000164, 38.9154706337), (1.1000000164, 38.6845305226))
                Line((1.1000000164, 38.6845305226), (1.3000000194, 38.569060467))
                Line((1.3000000194, 38.569060467), (1.5000000224, 38.6845305226))
                Line((1.5000000224, 38.6845305226), (1.5000000224, 38.9154706337))
                Line((1.5000000224, 38.9154706337), (1.3000000194, 39.0309406893))
                Line((1.3000000194, 39.0309406893), (1.1000000164, 38.9154706337))
            make_face()
        # OneSide extrude, distance=0.15
        extrude(amount=0.15)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.15, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((1.3000000194, 38.8000005782)):
                Circle(0.1)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7, mode=Mode.ADD)
    return part.part


def model_42143_51b31600_0007():
    """Model: Spindle"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 7.74192, perimeter: 17.272
            with BuildLine():
                Line((-31.3646530439, 1.0075427064), (-31.3646530439, -0.0084572936))
                Line((-31.3646530439, -0.0084572936), (-23.7446530439, -0.0084572936))
                Line((-23.7446530439, 1.0075427064), (-23.7446530439, -0.0084572936))
                Line((-23.7446530439, 1.0075427064), (-31.3646530439, 1.0075427064))
            make_face()
        # OneSide extrude, distance=0.1778
        extrude(amount=0.1778)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.4196855303, perimeter: 2.722174448
            with BuildLine():
                Line((31.115000993, 0.2899128287), (30.2260009646, 0.2899128287))
                Line((31.115000993, 0.7620000243), (31.115000993, 0.2899128287))
                Line((30.2260009646, 0.7620000243), (31.115000993, 0.7620000243))
                Line((30.2260009646, 0.2899128287), (30.2260009646, 0.7620000243))
            make_face()
        # OneSide extrude, distance=-76.2
        extrude(amount=-76.2, mode=Mode.SUBTRACT)
    return part.part


def model_42329_df7f540f_0054():
    """Model: Arm head Suport"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7788404981, perimeter: 4.7933074684
            with BuildLine():
                Line((0.8689930295, 0.0608965522), (0.723584121, 1.018760731))
                CenterArc((0.6, 1), 0.125, 8.6319015847, 158.4492639419)
                CenterArc((-0.0166573368, 1.0997224561), 0.5, -10.118615973, 1.8651620934)
                CenterArc((-0.0166573368, 1.0997224561), 0.5, -88.0908565493, 77.9722405763)
                Line((0, 0.6), (0, 0))
                CenterArc((0.0068213871, -0.4999534665), 0.5, 40.5183458907, 50.2633517404)
                CenterArc((0.0068213871, -0.4999534665), 0.5, 39.7325777027, 0.785768188)
                CenterArc((0.6, 0), 0.2758, -139.1622627594, 151.9182692259)
            make_face()
            with BuildLine():
                CenterArc((0.6, 0), 0.08, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.6, 1), 0.08, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides extrude (symmetric), distance=0.35
        extrude(amount=0.35, both=True)

        # Sketch1 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7788404981, perimeter: 4.7933074684
            with BuildLine():
                Line((0.8689930295, 0.0608965522), (0.723584121, 1.018760731))
                CenterArc((0.6, 1), 0.125, 8.6319015847, 158.4492639419)
                CenterArc((-0.0166573368, 1.0997224561), 0.5, -10.118615973, 1.8651620934)
                CenterArc((-0.0166573368, 1.0997224561), 0.5, -88.0908565493, 77.9722405763)
                Line((0, 0.6), (0, 0))
                CenterArc((0.0068213871, -0.4999534665), 0.5, 40.5183458907, 50.2633517404)
                CenterArc((0.0068213871, -0.4999534665), 0.5, 39.7325777027, 0.785768188)
                CenterArc((0.6, 0), 0.2758, -139.1622627594, 151.9182692259)
            make_face()
            with BuildLine():
                CenterArc((0.6, 0), 0.08, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.6, 1), 0.08, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides extrude (symmetric), distance=0.25
        extrude(amount=0.25, both=True, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.36, perimeter: 2.4
            with BuildLine():
                Line((0, -0.35), (-0.6, -0.35))
                Line((0, 0.25), (0, -0.35))
                Line((-0.6, 0.25), (0, 0.25))
                Line((-0.6, -0.35), (-0.6, 0.25))
            make_face()
            # Profile area: 0.06, perimeter: 1.4
            with BuildLine():
                Line((0, 0.35), (0, 0.25))
                Line((-0.6, 0.35), (0, 0.35))
                Line((-0.6, 0.25), (-0.6, 0.35))
                Line((-0.6, 0.25), (0, 0.25))
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.ADD)
    return part.part


def model_42429_967ff817_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6384903279, perimeter: 5.2931051482
            with BuildLine():
                Line((0, 0), (0.635, 0))
                Line((0.6347379892, 0.9654615636), (0.635, 0))
                CenterArc((0.3175, 0.9525655095), 0.3175, 2.3278513188, 177.6721486812)
                Line((0, 0), (0, 0.9525655095))
            make_face()
            with BuildLine():
                CenterArc((0.3175, 0.9525655095), 0.15748, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.3175, 0.3194069092), 0.12192, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XY construction plane
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0791730436, perimeter: 0.9974556675
            with Locations((0.3175, 0.3175)):
                Circle(0.15875)
        # OneSide extrude, distance=-0.9906
        extrude(amount=-0.9906, mode=Mode.SUBTRACT)
    return part.part


def model_42429_deca15fc_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 146.6963395762, perimeter: 44.546063709
            with BuildLine():
                CenterArc((0, 0), 6.8357262346, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-0.9525, 3.1000000462), 0.127, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.9525, 3.1000000462), 0.127, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0506707479, perimeter: 0.797964534
            with Locations((-0.9525, 3.1000000462)):
                Circle(0.127)
            # Profile area: 0.0506707479, perimeter: 0.797964534
            with Locations((0.9525, 3.1000000462)):
                Circle(0.127)
        # OneSide extrude, distance=1.8
        extrude(amount=1.8)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 1.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0506707479, perimeter: 0.797964534
            with Locations((0.9525, -3.1000000462)):
                Circle(0.127)
            # Profile area: 0.0506707479, perimeter: 0.797964534
            with Locations((-0.9525, -3.1000000462)):
                Circle(0.127)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)
    return part.part


def model_42535_9efbd860_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 875, perimeter: 120
            with BuildLine():
                Line((-25, -35), (-25, 0))
                Line((0, -35), (-25, -35))
                Line((0, 0), (0, -35))
                Line((-25, 0), (0, 0))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            with Locations((13, 17)):
                Circle(2.5)
        # OneSide extrude, distance=60
        extrude(amount=60, mode=Mode.ADD)
    return part.part


def model_42540_6eb6c3bc_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 61274.2312808923, perimeter: 1093.8029070363
            with BuildLine():
                Line((0, 100), (0, 0))
                Line((0, 0), (350, 0))
                Line((350, 0), (350, 216.7743612484))
                Line((350, 216.7743612484), (150, 216.7743612484))
                Line((150, 216.7743612484), (100, 100))
                Line((100, 100), (0, 100))
            make_face()
        # OneSide extrude, distance=400
        extrude(amount=400)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 216.7743612484, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1963.4954084936, perimeter: 157.0796326795
            with Locations((-200, -250)):
                Circle(25)
        # OneSide extrude, distance=100
        extrude(amount=100, mode=Mode.ADD)
    return part.part


def model_42542_483aa73d_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # OneSide extrude, distance=10
        extrude(amount=10)
    return part.part


def model_42545_7e4c4d38_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.2732934641, perimeter: 34.8097025096
            with BuildLine():
                CenterArc((0, 0), 4, -35.0583732, 250.1167464001)
                Line((-3.274269028, -2.2976427774), (-2.9636696286, -2.2976427774))
                CenterArc((0, 0), 3.75, -37.7853313199, 255.5706626398)
                Line((2.9636696286, -2.2976427774), (3.274269028, -2.2976427774))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)
    return part.part


def model_42577_2275594e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 396.251241829, perimeter: 92.4513887461
            with BuildLine():
                Line((-0.0606186546, -6.4997173307), (1.2323171684, -6.3821151977))
                Line((1.2323171684, -6.3821151977), (30.3396881322, -3.7345832395))
                CenterArc((30, 0), 3.75, -84.8028235921, 169.6053888889)
                Line((1.23102034, 6.3823654645), (30.3397049681, 3.7345817081))
                Line((-0.0592393516, 6.4997300482), (1.23102034, 6.3823654645))
                CenterArc((0, 0), 6.5, 90.5221864331, 178.9434684263)
            make_face()
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 13 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 35.2821542029, perimeter: 22.2545615661
            with BuildLine():
                CenterArc((0, 0), 3.7511290267, 136.7322118415, 37.9567654346)
                Line((-3.7350250893, 0.3472125529), (-3.7350250893, -0.3472125529))
                CenterArc((0, 0), 3.7511290267, -174.6889772762, 37.9567654346)
                Line((-2.7314154033, -2.571057928), (2.7314154033, -2.571057928))
                CenterArc((0, 0), 3.7511290267, -43.2677881585, 37.9567654346)
                Line((3.7350250893, -0.3472125529), (3.7350250893, 0.3472125529))
                CenterArc((0, 0), 3.7511290267, 5.3110227238, 37.9567654346)
                Line((2.7314154033, 2.571057928), (-2.7314154033, 2.571057928))
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)
    return part.part


def model_42586_517832f9_0020():
    """Model: Door1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1341.9328, perimeter: 147.32
            with BuildLine():
                Line((21.1436869591, -17.9360284583), (21.1436869591, 15.0839715417))
                Line((21.1436869591, 15.0839715417), (-19.4963130409, 15.0839715417))
                Line((-19.4963130409, 15.0839715417), (-19.4963130409, -17.9360284583))
                Line((-19.4963130409, -17.9360284583), (21.1436869591, -17.9360284583))
            make_face()
        # OneSide extrude, distance=0.508
        extrude(amount=0.508)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.508, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2026830046, perimeter: 1.595929119
            with Locations((15.6863130409, 16.6660284583)):
                Circle(0.2540000081)
            # Profile area: 0.2026829916, perimeter: 1.595929068
            with Locations((11.8763130409, 16.6660284583)):
                Circle(0.254)
            # Profile area: 0.2026830046, perimeter: 1.595929119
            with Locations((-13.5236869591, 16.6660284583)):
                Circle(0.2540000081)
            # Profile area: 0.2026830046, perimeter: 1.595929119
            with Locations((-17.3336869591, 16.6660284583)):
                Circle(0.2540000081)
        # OneSide extrude, distance=-1.27
        extrude(amount=-1.27, mode=Mode.SUBTRACT)
    return part.part


def model_42601_bfe96b47_0007():
    """Model: Bottom Stalk v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 18.020175461, perimeter: 60.0672515366
            with BuildLine():
                CenterArc((0, 0), 5.08, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 4.48, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=350
        extrude(amount=350)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 3.1730871199, perimeter: 6.3146012337
            with Locations((10, 0)):
                Circle(1.005)
        # TwoSides extrude, along=12, against=-11
        extrude(amount=12, mode=Mode.SUBTRACT)
        extrude(sk.sketch, amount=-11, mode=Mode.SUBTRACT)
    return part.part


def model_42811_4743cfd2_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1385640646, perimeter: 1.3856406461
            with BuildLine():
                Line((0.1154700538, 0.2), (-0.1154700538, 0.2))
                Line((-0.1154700538, 0.2), (-0.2309401077, 0))
                Line((-0.2309401077, 0), (-0.1154700538, -0.2))
                Line((-0.1154700538, -0.2), (0.1154700538, -0.2))
                Line((0.1154700538, -0.2), (0.2309401077, 0))
                Line((0.2309401077, 0), (0.1154700538, 0.2))
            make_face()
        # OneSide extrude, distance=5.7
        extrude(amount=5.7)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.9258372741, perimeter: 8.7214702797
            with BuildLine():
                CenterArc((0, 0), 0.4, 106.778654881, 326.4426902381)
                Line((-0.1154700538, 0.8925618559), (-0.1154700538, 0.3829708431))
                CenterArc((0, 0), 0.9, 97.3713703032, 345.2572593936)
                Line((0.1154700538, 0.3829708431), (0.1154700538, 0.8925618559))
            make_face()
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4, mode=Mode.ADD)
    return part.part


def model_42811_75f8e8a3_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.8660254038, perimeter: 3.4641016151
            with BuildLine():
                Line((0.2886751346, 0.5), (-0.2886751346, 0.5))
                Line((-0.2886751346, 0.5), (-0.5773502692, 0))
                Line((-0.5773502692, 0), (-0.2886751346, -0.5))
                Line((-0.2886751346, -0.5), (0.2886751346, -0.5))
                Line((0.2886751346, -0.5), (0.5773502692, 0))
                Line((0.5773502692, 0), (0.2886751346, 0.5))
            make_face()
        # OneSide extrude, distance=5.7
        extrude(amount=5.7)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.7404010555, perimeter: 8.086532387
            with BuildLine():
                CenterArc((0, 0), 0.4, 136.1940077316, 267.6119845367)
                Line((-0.2886751346, 0.8524474568), (-0.2886751346, 0.2768874621))
                CenterArc((0, 0), 0.9, 108.7082968086, 322.5834063828)
                Line((0.2886751346, 0.2768874621), (0.2886751346, 0.8524474568))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.ADD)
    return part.part


def model_42811_a0527cb1_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5542562584, perimeter: 2.7712812921
            with BuildLine():
                Line((0.2309401077, -0.4), (0.4618802154, 0))
                Line((0.4618802154, 0), (0.2309401077, 0.4))
                Line((0.2309401077, 0.4), (-0.2309401077, 0.4))
                Line((-0.2309401077, 0.4), (-0.4618802154, 0))
                Line((-0.4618802154, 0), (-0.2309401077, -0.4))
                Line((-0.2309401077, -0.4), (0.2309401077, -0.4))
            make_face()
        # OneSide extrude, distance=5.7
        extrude(amount=5.7)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.4), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.804852437, perimeter: 8.2951864427
            with BuildLine():
                CenterArc((0, 0), 0.4, 125.2643896828, 289.4712206345)
                Line((-0.2309401077, 0.86986589), (-0.2309401077, 0.3265986324))
                CenterArc((0, 0), 0.9, 104.8684204642, 330.2631590717)
                Line((0.2309401077, 0.3265986324), (0.2309401077, 0.86986589))
            make_face()
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.ADD)
    return part.part


def model_42937_fd3c1e0b_0003():
    """Model: 06_CARROCERIA 2"""
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
        # Sketch5 -> Extrude6 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 9 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0686699975, perimeter: 1.1512389142
            with BuildLine():
                Line((-1.0011365665, 0.2749913908), (-0.9988672497, 0.2749914481))
                CenterArc((-1.0000000149, 0.200000003), 0.075, 90.8682947349, 179.1317052651)
                Line((-0.6599999851, 0.125000003), (-1.0000000149, 0.125000003))
                CenterArc((-0.6599999851, 0.200000003), 0.075, -90, 180.0014464634)
                Line((-0.9988672497, 0.2749914481), (-0.6600018785, 0.275000003))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


def model_43009_6aa4e085_0011():
    """Model: housing's gasket  (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 27 constraints, 20 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 7.2738360038, perimeter: 26.2544830604
            with BuildLine():
                CenterArc((0, -3.81), 2.2225, 141.8749484373, 256.2501031254)
                CenterArc((0, 0), 3, -134.092733222, 8.4458737327)
                CenterArc((-2.4, -1.905), 0.4, -115.4984091729, 76.881577514)
                CenterArc((0, -3.81), 3, 149.025689264, 30.974310736)
                CenterArc((0, -3.81), 3, -180, 33.5216590455)
                CenterArc((-2.1213203436, -5.9313203436), 0.6, -39.2608295227, 168.5216590455)
                CenterArc((0, -3.81), 3, -123.5216590455, 22.0433180909)
                CenterArc((0, -6.81), 0.6, 5.7391704773, 168.5216590455)
                CenterArc((0, -3.81), 3, -78.5216590455, 22.0433180909)
                CenterArc((2.1213203436, -5.9313203436), 0.6, 50.7391704773, 168.5216590455)
                CenterArc((0, -3.81), 3, -33.5216590455, 33.5216590455)
                CenterArc((0, -3.81), 3, 0, 30.9743103299)
                CenterArc((2.4000000492, -1.905), 0.4, -141.3831732647, 76.8815763707)
                CenterArc((0, 0), 3, -54.3531405107, 8.4458744699)
            make_face()
            # Profile area: 0.6179205185, perimeter: 7.9542343414
            with BuildLine():
                Line((-3, 0), (-3, -3.81))
                CenterArc((0, -3.81), 3, 149.025689264, 30.974310736)
                CenterArc((-2.4, -1.905), 0.4, 115.4984091729, 129.0031816543)
                CenterArc((0, 0), 3, -180, 30.974310736)
            make_face()
            # Profile area: 0.4348433861, perimeter: 2.6850723564
            with BuildLine():
                CenterArc((-2.4, -1.905), 0.4, -38.6168316588, 77.2336633177)
                CenterArc((0, 0), 3, -134.092733222, 8.4458737327)
                CenterArc((0, -3.81), 2.2225, 132.4475991631, 9.4273492742)
                Line((-1.5, -1.6399714174), (-1.5, -2.1700285826))
                CenterArc((0, 0), 2.2225, -141.8749484373, 9.4273492742)
                CenterArc((0, -3.81), 3, 125.6468594893, 8.4458737327)
            make_face()
            # Profile area: 0.4494190784, perimeter: 3.4462993765
            with BuildLine():
                CenterArc((2.1213203436, 2.1213203436), 0.6, -50.7391704773, 191.4783409545)
                CenterArc((0, 0), 3, 52.2708027909, 4.2075381636)
                CenterArc((2.0152543264, 2.0152543264), 0.4, -26.6577195745, 143.315439149)
                CenterArc((0, 0), 3, 33.5216590455, 4.2075381636)
            make_face()
            # Profile area: 0.1788994523, perimeter: 3.7181106629
            with BuildLine():
                CenterArc((0, -6.81), 0.6, 5.7391704773, 168.5216590455)
                CenterArc((0, -3.81), 3, -101.4783409545, 4.2075381636)
                CenterArc((0, -6.66), 0.4, -18.3422804255, 216.684560851)
                CenterArc((0, -3.81), 3, -82.7291972091, 4.2075381636)
            make_face()
            # Profile area: 0.4494190784, perimeter: 3.4462993765
            with BuildLine():
                CenterArc((0, -3.81), 3, -82.7291972091, 4.2075381636)
                CenterArc((0, -6.66), 0.4, -161.6577195745, 143.315439149)
                CenterArc((0, -3.81), 3, -101.4783409545, 4.2075381636)
                CenterArc((0, -6.81), 0.6, 174.2608295227, 191.4783409545)
            make_face()
            # Profile area: 0.1788994523, perimeter: 3.7181106629
            with BuildLine():
                CenterArc((0, 0), 3, 78.5216590455, 4.2075381636)
                CenterArc((0, 2.85), 0.4, 161.6577195745, 216.684560851)
                CenterArc((0, 0), 3, 97.2708027909, 4.2075381636)
                CenterArc((0, 3), 0.6, -174.2608295227, 168.5216590455)
            make_face()
            # Profile area: 0.4494190784, perimeter: 3.4462993765
            with BuildLine():
                CenterArc((0, -3.81), 3, -37.7291972091, 4.2075381636)
                CenterArc((2.0152543264, -5.8252543264), 0.4, -116.6577195745, 143.315439149)
                CenterArc((0, -3.81), 3, -56.4783409545, 4.2075381636)
                CenterArc((2.1213203436, -5.9313203436), 0.6, -140.7391704773, 191.4783409545)
            make_face()
            # Profile area: 0.4494190784, perimeter: 3.4462993765
            with BuildLine():
                CenterArc((0, 3), 0.6, -5.7391704773, 191.4783409545)
                CenterArc((0, 0), 3, 97.2708027909, 4.2075381636)
                CenterArc((0, 2.85), 0.4, 18.3422804255, 143.315439149)
                CenterArc((0, 0), 3, 78.5216590455, 4.2075381636)
            make_face()
            # Profile area: 0.4494190784, perimeter: 3.4462993765
            with BuildLine():
                CenterArc((0, -3.81), 3, -127.7291972091, 4.2075381636)
                CenterArc((-2.0152543264, -5.8252543264), 0.4, 153.3422804255, 143.315439149)
                CenterArc((0, -3.81), 3, -146.4783409545, 4.2075381636)
                CenterArc((-2.1213203436, -5.9313203436), 0.6, 129.2608295227, 191.4783409545)
            make_face()
            # Profile area: 0.1788994523, perimeter: 3.7181106629
            with BuildLine():
                CenterArc((0, 0), 3, 33.5216590455, 4.2075381636)
                CenterArc((2.0152543264, 2.0152543264), 0.4, 116.6577195745, 216.684560851)
                CenterArc((0, 0), 3, 52.2708027909, 4.2075381636)
                CenterArc((2.1213203436, 2.1213203436), 0.6, 140.7391704773, 168.5216590455)
            make_face()
            # Profile area: 0.4494190784, perimeter: 3.4462993765
            with BuildLine():
                CenterArc((-2.1213203436, 2.1213203436), 0.6, 39.2608295227, 191.4783409545)
                CenterArc((0, 0), 3, 142.2708027909, 4.2075381636)
                CenterArc((-2.0152543264, 2.0152543264), 0.4, 63.3422804255, 143.315439149)
                CenterArc((0, 0), 3, 123.5216590455, 4.2075381636)
            make_face()
            # Profile area: 0.1788994523, perimeter: 3.7181106629
            with BuildLine():
                CenterArc((0, 0), 3, 123.5216590455, 4.2075381636)
                CenterArc((-2.0152543264, 2.0152543264), 0.4, -153.3422804255, 216.684560851)
                CenterArc((0, 0), 3, 142.2708027909, 4.2075381636)
                CenterArc((-2.1213203436, 2.1213203436), 0.6, -129.2608295227, 168.5216590455)
            make_face()
            # Profile area: 0.617920483, perimeter: 7.9542343836
            with BuildLine():
                CenterArc((2.4000000492, -1.905), 0.4, -64.501596894, 129.0031937881)
                CenterArc((0, -3.81), 3, 0, 30.9743103299)
                Line((3, 0), (3, -3.81))
                CenterArc((0, 0), 3, -30.9743103299, 30.9743103299)
            make_face()
            # Profile area: 0.1788994523, perimeter: 3.7181106629
            with BuildLine():
                CenterArc((-2.1213203436, -5.9313203436), 0.6, -39.2608295227, 168.5216590455)
                CenterArc((0, -3.81), 3, -146.4783409545, 4.2075381636)
                CenterArc((-2.0152543264, -5.8252543264), 0.4, -63.3422804255, 216.684560851)
                CenterArc((0, -3.81), 3, -127.7291972091, 4.2075381636)
            make_face()
            # Profile area: 1.1430001874, perimeter: 8.2200000983
            with BuildLine():
                Line((3, 0), (3, -3.81))
                Line((3.3000000492, -3.81), (3, -3.81))
                Line((3.3000000492, 0), (3.3000000492, -3.81))
                Line((3, 0), (3.3000000492, 0))
            make_face()
            # Profile area: 7.2738360038, perimeter: 26.2544830604
            with BuildLine():
                CenterArc((0, 0), 2.2225, -38.1250515627, 256.2501031254)
                CenterArc((0, -3.81), 3, 45.9072660408, 8.4458744699)
                CenterArc((2.4000000492, -1.905), 0.4, 64.501596894, 76.8815763707)
                CenterArc((0, 0), 3, -30.9743103299, 30.9743103299)
                CenterArc((0, 0), 3, 0, 33.5216590455)
                CenterArc((2.1213203436, 2.1213203436), 0.6, 140.7391704773, 168.5216590455)
                CenterArc((0, 0), 3, 56.4783409545, 22.0433180909)
                CenterArc((0, 3), 0.6, -174.2608295227, 168.5216590455)
                CenterArc((0, 0), 3, 101.4783409545, 22.0433180909)
                CenterArc((-2.1213203436, 2.1213203436), 0.6, -129.2608295227, 168.5216590455)
                CenterArc((0, 0), 3, 146.4783409545, 33.5216590455)
                CenterArc((0, 0), 3, -180, 30.974310736)
                CenterArc((-2.4, -1.905), 0.4, 38.6168316588, 76.881577514)
                CenterArc((0, -3.81), 3, 125.6468594893, 8.4458737327)
            make_face()
            # Profile area: 0.4348433846, perimeter: 2.6850723215
            with BuildLine():
                CenterArc((0, 0), 2.2225, -47.5523991189, 9.4273475562)
                Line((1.5000000492, -1.6399713725), (1.5000000492, -2.1700286275))
                CenterArc((0, -3.81), 2.2225, 38.1250515627, 9.4273475562)
                CenterArc((0, 0), 3, -54.3531405107, 8.4458744699)
                CenterArc((2.4000000492, -1.905), 0.4, 141.3831732647, 77.2336534705)
                CenterArc((0, -3.81), 3, 45.9072660408, 8.4458744699)
            make_face()
            # Profile area: 1.143, perimeter: 8.22
            with BuildLine():
                Line((-3, 0), (-3.3, 0))
                Line((-3.3, 0), (-3.3, -3.81))
                Line((-3.3, -3.81), (-3, -3.81))
                Line((-3, 0), (-3, -3.81))
            make_face()
            # Profile area: 0.1788994523, perimeter: 3.7181106629
            with BuildLine():
                CenterArc((2.1213203436, -5.9313203436), 0.6, 50.7391704773, 168.5216590455)
                CenterArc((0, -3.81), 3, -56.4783409545, 4.2075381636)
                CenterArc((2.0152543264, -5.8252543264), 0.4, 26.6577195745, 216.684560851)
                CenterArc((0, -3.81), 3, -37.7291972091, 4.2075381636)
            make_face()
        # OneSide extrude, distance=0.15
        extrude(amount=0.15)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.15), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 14.535264872, perimeter: 13.9243792102
            with BuildLine():
                CenterArc((0, -3.81), 2.2225, -179.7421299109, 179.4844006944)
                CenterArc((0.0000000246, -3.83), 2.2225, 0.2578700891, 59.755462862)
                CenterArc((0.0000000246, 0.02), 2.2225, -119.9866670489, 59.9733340977)
                CenterArc((0.0000000246, -3.83), 2.2225, 119.9866670489, 59.7556037346)
            make_face()
            # Profile area: 0.0888997, perimeter: 13.9643793452
            with BuildLine():
                CenterArc((0.0000000246, -3.83), 2.2225, 179.7422707834, 180.5155993057)
                CenterArc((0, -3.81), 2.2225, -179.7421299109, 179.4844006944)
            make_face()
            # Profile area: 0.1313834854, perimeter: 8.8749834772
            with BuildLine():
                CenterArc((0.0000000246, 0.02), 2.2225, -60.0133329511, 59.755462862)
                CenterArc((0.0000000246, -3.83), 2.2225, 0.2578700891, 59.755462862)
                CenterArc((0, -3.81), 2.2225, -0.2577292165, 47.8101283354)
                Line((1.5000000492, -1.6399713725), (1.5000000492, -2.1700286275))
                CenterArc((0, 0), 2.2225, -47.5523991189, 47.8101283354)
            make_face()
            # Profile area: 0.0888997, perimeter: 13.9643793452
            with BuildLine():
                CenterArc((0, 0), 2.2225, 0.2577292165, 179.4844006943)
                CenterArc((0.0000000246, 0.02), 2.2225, -0.2578700891, 180.5155993056)
            make_face()
            # Profile area: 14.535264872, perimeter: 13.9243792102
            with BuildLine():
                CenterArc((0.0000000246, 0.02), 2.2225, -179.7422707835, 59.7556037347)
                CenterArc((0.0000000246, -3.83), 2.2225, 60.0133329511, 59.9733340977)
                CenterArc((0.0000000246, 0.02), 2.2225, -60.0133329511, 59.755462862)
                CenterArc((0, 0), 2.2225, 0.2577292165, 179.4844006943)
            make_face()
            # Profile area: 0.8937519754, perimeter: 4.6527243774
            with BuildLine():
                CenterArc((0.0000000246, 0.02), 2.2225, -119.9866670489, 59.9733340977)
                CenterArc((0.0000000246, -3.83), 2.2225, 60.0133329511, 59.9733340977)
            make_face()
            # Profile area: 0.1313836477, perimeter: 8.8750053782
            with BuildLine():
                CenterArc((0.0000000246, -3.83), 2.2225, 119.9866670489, 59.7556037346)
                CenterArc((0.0000000246, 0.02), 2.2225, -179.7422707835, 59.7556037347)
                CenterArc((0, 0), 2.2225, 179.7421299108, 47.810270926)
                Line((-1.5, -2.1700285826), (-1.5, -1.6399714174))
                CenterArc((0, -3.81), 2.2225, 132.4475991631, 47.8102709259)
            make_face()
        # OneSide extrude, distance=-0.15
        extrude(amount=-0.15, mode=Mode.SUBTRACT)
    return part.part


def model_43441_e1ab0873_0000():
    """Model: gear mount v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=-5
        extrude(amount=-5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -5), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.16, perimeter: 1.6
            with BuildLine():
                Line((0.2, -0.2), (0.2, 0.2))
                Line((0.2, 0.2), (-0.2, 0.2))
                Line((-0.2, 0.2), (-0.2, -0.2))
                Line((-0.2, -0.2), (0.2, -0.2))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)
    return part.part


def model_43529_4804941b_0018():
    """Model: Solid74_tornillo mediano (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.022710006, perimeter: 1.4312393053
            with BuildLine():
                CenterArc((0, 0), 0.65, -120.0002438954, 60.0002444809)
                Line((-0.3250023962, -0.562915129), (0, -0.7505553499))
                Line((0, -0.7505553499), (0.3250000058, -0.5629165091))
            make_face()
            # Profile area: 0.022710006, perimeter: 1.431241773
            with BuildLine():
                Line((-0.3249965295, 0.5629185161), (-0.65, 0.375277675))
                Line((-0.65, 0.375277675), (-0.65, 0))
                CenterArc((0, 0), 0.65, 119.9996467615, 60.0003532385)
            make_face()
            # Profile area: 0.022710006, perimeter: 1.4312257363
            with BuildLine():
                Line((0.3249999969, 0.5629165143), (0, 0.7505553499))
                Line((0, 0.7505553499), (-0.3249965295, 0.5629185161))
                CenterArc((0, 0), 0.65, 60.0000003172, 59.9996464442)
            make_face()
            # Profile area: 0.022710006, perimeter: 1.4312337824
            with BuildLine():
                Line((0.65, -0.0000000085), (0.65, 0.375277675))
                Line((0.65, 0.375277675), (0.3249999969, 0.5629165143))
                CenterArc((0, 0), 0.65, -0.0000007488, 60.000001066)
            make_face()
            # Profile area: 0.022710006, perimeter: 1.4312282244
            with BuildLine():
                CenterArc((0, 0), 0.65, -180, 59.9997561046)
                Line((-0.65, 0), (-0.65, -0.375277675))
                Line((-0.65, -0.375277675), (-0.3250023962, -0.562915129))
            make_face()
            # Profile area: 0.022710006, perimeter: 1.431233728
            with BuildLine():
                Line((0.3250000058, -0.5629165091), (0.65, -0.375277675))
                Line((0.65, -0.375277675), (0.65, -0.0000000085))
                CenterArc((0, 0), 0.65, -59.9999994145, 59.9999986657)
            make_face()
            # Profile area: 1.3273228961, perimeter: 4.0840704497
            with BuildLine():
                CenterArc((0, 0), 0.65, -59.9999994145, 59.9999986657)
                CenterArc((0, 0), 0.65, -0.0000007488, 60.000001066)
                CenterArc((0, 0), 0.65, 60.0000003172, 59.9996464442)
                CenterArc((0, 0), 0.65, 119.9996467615, 60.0003532385)
                CenterArc((0, 0), 0.65, -180, 59.9997561046)
                CenterArc((0, 0), 0.65, -120.0002438954, 60.0002444809)
            make_face()
        # OneSide extrude, distance=0.53
        extrude(amount=0.53)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.53, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=4.5
        extrude(amount=4.5, mode=Mode.ADD)
    return part.part


def model_43529_4804941b_0021():
    """Model: Sol1_tuerca"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.0685834706, perimeter: 15.7079632679
            with BuildLine():
                CenterArc((0, 0), 1.7, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.1
        extrude(amount=1.1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.8246680716, perimeter: 10.9955742876
            with BuildLine():
                CenterArc((0, 0), 0.95, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)
    return part.part


def model_43529_4804941b_0055():
    """Model: Solid35_Palanca"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 14 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 17.76, perimeter: 59.2
            with BuildLine():
                Line((-4, 4), (4, 4))
                Line((-4, -4), (-4, 4))
                Line((4, -4), (-4, -4))
                Line((4, 4), (4, -4))
            make_face()
            with BuildLine():
                Line((-3.4, -3.4), (3.4, -3.4))
                Line((-3.4, 3.4), (-3.4, -3.4))
                Line((3.4, 3.4), (-3.4, 3.4))
                Line((3.4, -3.4), (3.4, 3.4))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=80
        extrude(amount=80)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -4), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((0, 2)):
                Circle(0.5)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


def model_43628_a95b7e66_0013():
    """Model: 07A_axis support (front) v1 (1)"""
    with BuildPart() as part:
        # Sketch3 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # TwoSides extrude (symmetric), distance=0.6
        extrude(amount=0.6, both=True)

        # Sketch5 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # TwoSides extrude, along=0.2, against=-1.35
        extrude(amount=0.2, mode=Mode.SUBTRACT)
        extrude(sk.sketch, amount=-1.35, mode=Mode.SUBTRACT)
    return part.part


def model_43628_a95b7e66_0029():
    """Model: brush contact v7 (1)"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.7130063182, perimeter: 2.9933094803
            Circle(0.4764)
        # OneSide extrude, distance=1.6
        extrude(amount=1.6)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.6), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=-1.9
        extrude(amount=-1.9, mode=Mode.SUBTRACT)
    return part.part


def model_43628_a95b7e66_0030():
    """Model: brush v3 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4.5238934212, perimeter: 7.5398223686
            with Locations((-2.35, 0)):
                Circle(1.2)
        # Symmetric extrude, each_side=0.8
        extrude(amount=0.8, both=True, mode=Mode.SUBTRACT)
    return part.part


def model_43628_a95b7e66_0034():
    """Model: 07B_axis support (rear) v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # Symmetric extrude, each_side=0.4
        extrude(amount=0.4, both=True)

        # Sketch4 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # TwoSides extrude, along=0.15, against=-0.9
        extrude(amount=0.15, mode=Mode.SUBTRACT)
        extrude(sk.sketch, amount=-0.9, mode=Mode.SUBTRACT)
    return part.part


def model_43928_6ca53538_0003():
    """Model: Plasric Crankshaft spacer v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.2271846303, perimeter: 3.926990817
            Circle(0.625)
        # OneSide extrude, distance=0.625
        extrude(amount=0.625)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 9 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.625), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.4577330095, perimeter: 2.4688121525
            with BuildLine():
                CenterArc((0, 0), 0.405, -142.1970502185, 104.394100437)
                Line((0.32, -0.2482438317), (0.32, 0.2482438317))
                CenterArc((0, 0), 0.405, 37.8029497815, 104.394100437)
                Line((-0.32, 0.2482438317), (-0.32, -0.2482438317))
            make_face()
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.SUBTRACT)
    return part.part


def model_43928_6ca53538_0005():
    """Model: Drag Sprocket Pin v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1104466167, perimeter: 1.1780972451
            Circle(0.1875)
        # OneSide extrude, distance=0.175
        extrude(amount=0.175)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.175), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0176714587, perimeter: 0.471238898
            Circle(0.075)
        # OneSide extrude, distance=-0.325
        extrude(amount=-0.325, mode=Mode.ADD)
    return part.part


def model_43928_6ca53538_0016():
    """Model: Plastic Bushing v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 13 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2343318502, perimeter: 3.0304803876
            with BuildLine():
                CenterArc((0, 0), 0.245, 146.1705751042, 247.6588497916)
                Line((-0.2035211736, 0.1363969644), (-0.4112576277, 0.1072015097))
                CenterArc((0, 0), 0.425, 165.3899647752, 209.2200704496)
                Line((0.2035211736, 0.1363969644), (0.4112576277, 0.1072015097))
            make_face()
        # Symmetric extrude, each_side=0.15
        extrude(amount=0.15, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.5807706037, perimeter: 5.0806991285
            with BuildLine():
                CenterArc((0, 0), 0.5186183807, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.29, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.08
        extrude(amount=0.08, both=True, mode=Mode.SUBTRACT)
    return part.part


def model_43928_6ca53538_0020():
    """Model: Crank shaft spacer tension spring v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 10 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.6732403458, perimeter: 6.2387233368
            with BuildLine():
                CenterArc((0, 0), 0.6, 0, 360)
            make_face()
            with BuildLine():
                Line((-0.2482438317, -0.32), (0.2482438317, -0.32))
                CenterArc((0, 0), 0.405, 127.8029497815, 104.394100437)
                Line((0.2482438317, 0.32), (-0.2482438317, 0.32))
                CenterArc((0, 0), 0.405, -52.1970502185, 104.394100437)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.625
        extrude(amount=0.625)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.6409014745, perimeter: 18.1633933942
            with BuildLine():
                CenterArc((0.675, 0), 1.590793842, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0.675, 0), 1.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 4.1547562844, perimeter: 7.2256631033
            with Locations((0.675, 0)):
                Circle(1.15)
        # Symmetric extrude, each_side=-0.7
        extrude(amount=-0.7, both=True, mode=Mode.SUBTRACT)
    return part.part


def model_43928_6ca53538_0024():
    """Model: Main bearing cover v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            Circle(0.75)
        # OneSide extrude, distance=0.9
        extrude(amount=0.9)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 1.5393804003, perimeter: 4.398229715
            Circle(0.7)
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.SUBTRACT)
    return part.part


def model_43928_6ca53538_0031():
    """Model: Foot v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2775588538, perimeter: 4.0053979428
            with BuildLine():
                CenterArc((0, 0), 0.7375, 98.960258096, 162.0794838081)
                Line((-0.1148651383, -0.5761616527), (-0.1148651383, -0.7285))
                CenterArc((0, 0), 0.5875, 101.2748175617, 157.4503648765)
                Line((-0.1148651383, 0.7285), (-0.1148651383, 0.5761616527))
            make_face()
        # Symmetric extrude, each_side=3.1
        extrude(amount=3.1, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 44 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4.1797072527, perimeter: 11.3151862538
            with BuildLine():
                Line((1.9, 0.7285), (2.8390427282, 0.629392712))
                CenterArc((2.8085, 0.34), 0.291, -3.0123684576, 86.9876315424)
                Line((3.0990979002, 0.3247075049), (3.0994999273, -0.3397977088))
                CenterArc((2.8085, -0.34), 0.291, -83.9752630849, 84.0150927494)
                Line((1.9, -0.7285), (2.8390427282, -0.629392712))
                Line((2.6000000387, -1.9000000283), (1.9, -0.7285))
                Line((4.1000000611, -1.8000000268), (2.6000000387, -1.9000000283))
                Line((4.2000000626, -0.400000006), (4.1000000611, -1.8000000268))
                Line((3.1000000462, 1.5000000224), (4.2000000626, -0.400000006))
                Line((1.9, 0.7285), (3.1000000462, 1.5000000224))
            make_face()
            # Profile area: 3.361513125, perimeter: 12.0929987539
            with BuildLine():
                Line((-3.6000000536, 1.6000000238), (-4.0000000596, -2.3000000343))
                Line((-4.0000000596, -2.3000000343), (-1.9, -0.7285))
                Line((-1.9, -0.7285), (-3.1, -0.7285))
                Line((-3.0996869915, -0.3630605441), (-3.1, -0.7285))
                Line((-3.0990979002, 0.3247075049), (-3.0996869915, -0.3630605441))
                CenterArc((-2.8085, 0.34), 0.291, 166.7584937146, 16.253874743)
                CenterArc((-2.8085, 0.34), 0.291, 96.0247369151, 70.7337567994)
                Line((-1.9, 0.7285), (-2.8390427282, 0.629392712))
                Line((-1.9, 0.7285), (-3.6000000536, 1.6000000238))
            make_face()
            # Profile area: 0.0902111173, perimeter: 2.9528746023
            with BuildLine():
                Line((-1.9, -0.7285), (-2.8390427282, -0.629392712))
                CenterArc((-2.8085, -0.34), 0.291, -179.3711769655, 83.3464400504)
                Line((-3.0994824745, -0.3431936703), (-3.0996869915, -0.3630605441))
                Line((-3.0996869915, -0.3630605441), (-3.1, -0.7285))
                Line((-1.9, -0.7285), (-3.1, -0.7285))
            make_face()
        # OneSide extrude, distance=-4.6
        extrude(amount=-4.6, mode=Mode.SUBTRACT)
    return part.part


def model_43931_bb001c04_0002():
    """Model: ring v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 863.9379797372, perimeter: 345.5751918949
            with BuildLine():
                CenterArc((0, 0), 30, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=1.5
        extrude(amount=1.5, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 4.9087385212, perimeter: 7.853981634
            with Locations((0, 27.5)):
                Circle(1.25)
        # OneSide extrude, distance=-16
        extrude(amount=-16, mode=Mode.SUBTRACT)
    return part.part


def model_43931_bb001c04_0010():
    """Model: seridina_jet v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1884.9555921539, perimeter: 376.9911184308
            with BuildLine():
                CenterArc((0, 0), 35, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=25
        extrude(amount=25, both=True)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 25, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            with Locations((-0.386927566, -30.1220149942)):
                Circle(2)
        # OneSide extrude, distance=-70
        extrude(amount=-70, mode=Mode.SUBTRACT)
    return part.part


def model_43932_4bfdfe7b_0007():
    """Model: 9 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 14 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 24.7988653774, perimeter: 50.7085897275
            with BuildLine():
                Line((2.1, -5.2885737159), (2.1, 5.2885737159))
                Line((2.1, 5.2885737159), (-2.1, 5.2885737159))
                Line((-2.1, 5.2885737159), (-2.1, -5.2885737159))
                Line((-2.1, -5.2885737159), (2.1, -5.2885737159))
            make_face()
            with BuildLine():
                Line((-1.2, -4.0885737159), (1.2, -4.0885737159))
                Line((-1.2, 4.0885737159), (-1.2, -4.0885737159))
                Line((1.2, 4.0885737159), (-1.2, 4.0885737159))
                Line((1.2, -4.0885737159), (1.2, 4.0885737159))
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=1.4
        extrude(amount=1.4, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5.2885737159, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # OneSide extrude, distance=2.5
        extrude(amount=2.5, mode=Mode.ADD)
    return part.part


def model_43933_3b763a09_0002():
    """Model: 4 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 7.7942286341, perimeter: 10.3923048454
            with BuildLine():
                Line((0.8660254038, 1.5), (-0.8660254038, 1.5))
                Line((-0.8660254038, 1.5), (-1.7320508076, 0))
                Line((-1.7320508076, 0), (-0.8660254038, -1.5))
                Line((-0.8660254038, -1.5), (0.8660254038, -1.5))
                Line((0.8660254038, -1.5), (1.7320508076, 0))
                Line((1.7320508076, 0), (0.8660254038, 1.5))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_43933_3b763a09_0003():
    """Model: 2 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.5393804003, perimeter: 4.398229715
            Circle(0.7)
        # OneSide extrude, distance=1.4
        extrude(amount=1.4)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.6361725124, perimeter: 2.8274333882
            Circle(0.45)
        # OneSide extrude, distance=-1.2
        extrude(amount=-1.2, mode=Mode.SUBTRACT)
    return part.part


def model_43934_912ff891_0007():
    """Model: Crankshaft Center Rod v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # Symmetric extrude, each_side=1.25
        extrude(amount=1.25, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            with Locations((-0.9, 0)):
                Circle(0.125)
        # Symmetric extrude, each_side=0.8
        extrude(amount=0.8, both=True, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            with Locations((0.9, 0)):
                Circle(0.125)
        # Symmetric extrude, each_side=1.1
        extrude(amount=1.1, both=True, mode=Mode.SUBTRACT)
    return part.part


def model_43934_912ff891_0015():
    """Model: Crankshaft Outer Rod v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=5.2
        extrude(amount=5.2)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            with Locations((-4.85, 0)):
                Circle(0.125)
        # Symmetric extrude, each_side=1
        extrude(amount=1, both=True, mode=Mode.SUBTRACT)
    return part.part


def model_43934_912ff891_0017():
    """Model: Connecting Rod v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 11 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.9486725877, perimeter: 5.6566370614
            with BuildLine():
                Line((-0.4, 0.3), (-1, 0.3))
                Line((-1, 0.3), (-1, -0.3))
                Line((-1, -0.3), (1, -0.3))
                Line((1, -0.3), (1, 0.3))
                Line((1, 0.3), (0.4, 0.3))
                CenterArc((0, 0.3), 0.4, 180, 180)
            make_face()
        # Symmetric extrude, each_side=0.5
        extrude(amount=0.5, both=True)

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
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


def model_43934_912ff891_0019():
    """Model: Piston Ring v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.133738672, perimeter: 17.9070781255
            with BuildLine():
                CenterArc((0, 0), 1.6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2924712895, perimeter: 3.5247128948
            with BuildLine():
                Line((-0.6756431502, 0.5177807641), (0.7407946827, -0.3))
                Line((-0.7756431502, 0.3445756833), (-0.6756431502, 0.5177807641))
                Line((0.3407946827, -0.3), (-0.7756431502, 0.3445756833))
                Line((0.7407946827, -0.3), (0.3407946827, -0.3))
            make_face()
            # Profile area: 0.0986140867, perimeter: 1.5861408668
            with BuildLine():
                Line((0.7407946827, -0.3), (0.3407946827, -0.3))
                Line((0.9178062038, -0.6331377571), (0.3407946827, -0.3))
                Line((1.0178062038, -0.4599326763), (0.9178062038, -0.6331377571))
                Line((0.7407946827, -0.3), (1.0178062038, -0.4599326763))
            make_face()
        # OneSide extrude, distance=2.6
        extrude(amount=2.6, mode=Mode.SUBTRACT)
    return part.part


def model_43934_912ff891_0023():
    """Model: Piston Rod v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=1.3
        extrude(amount=1.3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.086393798, perimeter: 3.4557519189
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=5.3
        extrude(amount=5.3, mode=Mode.ADD)
    return part.part


def model_43934_912ff891_0024():
    """Model: Lower Cylinder Ream v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.4636059006, perimeter: 6.5973445725
            Circle(1.05)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.3273228961, perimeter: 4.0840704497
            Circle(0.65)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7, mode=Mode.ADD)
    return part.part


def model_43936_666b7568_0003():
    """Model: Light v1 (1)"""
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
            # Profile area: 226.9800692219, perimeter: 53.407075111
            Circle(8.5)
        # OneSide extrude, distance=190
        extrude(amount=190)
    return part.part


def model_44206_ff45fbf0_0006():
    """Model: manivela"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0204908739, perimeter: 1.1926990817
            with BuildLine():
                CenterArc((-0.4, 0), 0.025, 90, 180)
                Line((0, -0.025), (-0.4, -0.025))
                CenterArc((0, 0), 0.025, -90, 180)
                Line((-0.4, 0.025), (0, 0.025))
            make_face()
            with BuildLine():
                CenterArc((-0.05, 0), 0.0125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-0.4, 0), 0.0125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0), 0.0125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0004908739, perimeter: 0.0785398163
            with Locations((-0.4, 0)):
                Circle(0.0125)
        # OneSide extrude, distance=0.025
        extrude(amount=0.025)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.025, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0031309292, perimeter: 0.281681409
            with BuildLine():
                CenterArc((0.3, 0), 0.013, 90, 180)
                Line((0.3, -0.013), (0.4, -0.013))
                CenterArc((0.4, 0), 0.013, -90, 180)
                Line((0.3, 0.013), (0.4, 0.013))
            make_face()
        # OneSide extrude, distance=-0.009
        extrude(amount=-0.009, mode=Mode.SUBTRACT)
    return part.part


def model_44209_972a6882_0000():
    """Model: Component1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 64.9519052838, perimeter: 30
            with BuildLine():
                Line((-0.0339294466, -4.9998848779), (4.313062597, -2.5293262017))
                Line((4.313062597, -2.5293262017), (4.3469920436, 2.4705586763))
                Line((4.3469920436, 2.4705586763), (0.0339294466, 4.9998848779))
                Line((0.0339294466, 4.9998848779), (-4.313062597, 2.5293262017))
                Line((-4.313062597, 2.5293262017), (-4.3469920436, -2.4705586763))
                Line((-4.3469920436, -2.4705586763), (-0.0339294466, -4.9998848779))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


def model_44210_a155c2d1_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 22 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 11.1580253384, perimeter: 54.178265104
            with BuildLine():
                CenterArc((-4, 6.5), 1, 90, 90)
                Line((-5, 6.5), (-5, 3.5))
                CenterArc((-4, 3.5), 1, 180, 90)
                Line((-4, 2.5), (4, 2.5))
                CenterArc((4, 3.5), 1, -90, 90)
                Line((5, 3.5), (5, 6.5))
                CenterArc((4, 6.5), 1, 0, 90)
                Line((4, 7.5), (-4, 7.5))
            make_face()
            with BuildLine():
                Line((4.0658913266, 7.0658913266), (-4.1790695919, 7.0658913266))
                CenterArc((4.0658913266, 6.5658913266), 0.5, 0, 90)
                Line((4.5658913266, 3.4341086734), (4.5658913266, 6.5658913266))
                CenterArc((4.0658913266, 3.4341086734), 0.5, -90, 90)
                Line((-4.1790695919, 2.9341086734), (4.0658913266, 2.9341086734))
                CenterArc((-4.1790695919, 3.4341086734), 0.5, 180, 90)
                Line((-4.6790695919, 6.5658913266), (-4.6790695919, 3.4341086734))
                CenterArc((-4.1790695919, 6.5658913266), 0.5, 90, 90)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=5
        extrude(amount=5, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.5, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((3.5, 2.5)):
                Circle(0.5)
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((3.5, -2.5)):
                Circle(0.5)
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-3.5, -2.5)):
                Circle(0.5)
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-3.5, 2.5)):
                Circle(0.5)
        # OneSide extrude, distance=4.5
        extrude(amount=4.5, mode=Mode.ADD)
    return part.part


def model_44212_042d1bc2_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 30.6305283725, perimeter: 40.8407044967
            with BuildLine():
                CenterArc((0, 0), 4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=10
        extrude(amount=10)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 10, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 108.3622274502, perimeter: 72.6921240235
            with BuildLine():
                Line((-0.0426765958, 3.999772332), (-15.9999429307, 3.9999999996))
                CenterArc((-16, 0), 4, 89.9991825423, 180.0008174574)
                Line((-16, -4), (-0.0316130724, -3.9998750748))
                CenterArc((0, 0), 4, 90.6113088041, 178.9358625753)
            make_face()
            with BuildLine():
                CenterArc((-16, 0), 2.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-10
        extrude(amount=-10, mode=Mode.ADD)
    return part.part


def model_44323_3bf3f9ca_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 28.2743338823, perimeter: 18.8495559215
            Circle(3)
        # OneSide extrude, distance=12
        extrude(amount=12)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 12), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 20.4203522483, perimeter: 16.0190422444
            Circle(2.5495097568)
        # OneSide extrude, distance=-12
        extrude(amount=-12, mode=Mode.SUBTRACT)
    return part.part


def model_44354_07805a0e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> 拉伸1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 12 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 104.6062842556, perimeter: 39.187880883
            with BuildLine():
                Line((-7.4861237507, 1.4343304307), (-7.4861237507, -1.4343304307))
                Line((-2.8486505257, -4.4172685285), (-7.4861237507, -1.4343304307))
                Line((2.8486505257, -4.4172685285), (-2.8486505257, -4.4172685285))
                Line((7.4861237507, -1.4343304307), (2.8486505257, -4.4172685285))
                Line((7.4861237507, 1.4343304307), (7.4861237507, -1.4343304307))
                Line((2.8486505257, 4.4172685285), (7.4861237507, 1.4343304307))
                Line((-2.8486505257, 4.4172685285), (2.8486505257, 4.4172685285))
                Line((-7.4861237507, 1.4343304307), (-2.8486505257, 4.4172685285))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch2 -> 拉伸2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 23.7582944428, perimeter: 17.2787595947
            Circle(2.75)
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)
    return part.part


def model_44375_f48f985a_0000():
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
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 78.5398163397, perimeter: 31.4159265359
            Circle(5)
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch3 -> Extrude3 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 15 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.1914255761, perimeter: 5.5141695673
            with BuildLine():
                Line((14.9284936144, -10.8899802261), (16.2273678896, -10.8899802261))
                CenterArc((27.4941272199, -0.0101541037), 15.6623906943, -141.6987254457, 5.6977862964)
                _nurbs_edge([(14, -10), (14.0300991287, -10.0170574896), (14.1770457248, -10.0944698781), (14.4348512107, -10.1779793767), (14.6803043828, -10.157813541), (14.9124561254, -10.0314560384), (15.1078053283, -9.8361332281), (15.2028690388, -9.7176488674)], [1, 1, 1, 1, 1, 1, 1, 1], [0.9097555383, 0.9097555383, 0.9097555383, 0.9097555383, 0.9097555383, 0.9097555383, 0.92, 0.96, 1, 1, 1, 1, 1, 1], 5)
                Line((14, -10), (14.9284936144, -10.8899802261))
            make_face()
            # Profile area: 217.0188448165, perimeter: 158.8823174769
            with BuildLine():
                _nurbs_edge([(14, -10), (14.0300991287, -10.0170574896), (14.1770457248, -10.0944698781), (14.4348512107, -10.1779793767), (14.6803043828, -10.157813541), (14.9124561254, -10.0314560384), (15.1078053283, -9.8361332281), (15.2028690388, -9.7176488674)], [1, 1, 1, 1, 1, 1, 1, 1], [0.9097555383, 0.9097555383, 0.9097555383, 0.9097555383, 0.9097555383, 0.9097555383, 0.92, 0.96, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((27.4941272199, -0.0101541037), 15.6623906943, -46.5877168447, 264.888991399)
                Line((38.4446441206, -11.3877431554), (38.2579996472, -11.3877431554))
                Line((38.7209146734, -11.4427273602), (38.4446441206, -11.3877431554))
                _nurbs_edge([(34.1874981742, 19.0016523667), (34.5411651298, 18.7712358134), (35.2334893197, 18.3092832362), (36.2269463692, 17.6129959922), (37.4612629654, 16.6778784381), (38.8526014528, 15.4974162956), (40.0915881338, 14.3045378772), (41.17846273, 13.0976822949), (42.1154253684, 11.8743460008), (42.9073726459, 10.6309202133), (43.5633166195, 9.3623483279), (44.0958331388, 8.0623687067), (44.5174645476, 6.7246581474), (44.8378784671, 5.3437721245), (45.0607964995, 3.9161879953), (45.1809052933, 2.4413452191), (45.181036715, 0.9227263183), (45.0392339865, -0.6311976349), (44.7353759404, -2.2059907749), (44.258198067, -3.7801490839), (43.6119047177, -5.3241043561), (42.8241052163, -6.7987609755), (41.9507497055, -8.1551331846), (41.062732345, -9.3406928295), (40.2349632479, -10.3048522673), (39.5343435576, -11.0049993447), (39.113814853, -11.330701126), (38.8841392275, -11.4393184804), (38.7689932793, -11.4516114872), (38.7209146734, -11.4427273602)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.04, 0.08, 0.12, 0.16, 0.2, 0.24, 0.28, 0.32, 0.36, 0.4, 0.44, 0.48, 0.52, 0.56, 0.6, 0.64, 0.68, 0.72, 0.76, 0.8, 0.84, 0.88, 0.92, 0.96, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((27.4941272199, -0.0101541037), 20.1556443707, 70.6046733846, 41.9053806743)
                _nurbs_edge([(19.7776285547, 18.609879418), (19.468123856, 18.4185358127), (18.8610535675, 18.0284620007), (17.9862654649, 17.4211913989), (16.8917028393, 16.5670625519), (15.6443133388, 15.4252643154), (14.519162551, 14.2102892109), (13.5176365765, 12.9249555715), (12.6406586321, 11.5748960823), (11.8882962956, 10.1693270146), (11.2591422413, 8.7224252437), (10.7502399352, 7.2529056382), (10.357949755, 5.7805292257), (10.0785162733, 4.3234651643), (9.9087543659, 2.8950541416), (9.8465112121, 1.5013551965), (9.8914897774, 0.1368682293), (10.0447878228, -1.2140568206), (10.3065461905, -2.567369225), (10.6740444003, -3.9316635961), (11.1394546737, -5.2992857536), (11.687846588, -6.6385074818), (12.2944229469, -7.883140165), (12.8962238959, -8.8915870272), (13.3689241674, -9.4962813207), (13.7049015864, -9.8091192586), (13.9125756141, -9.9504556904), (14, -10)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.04, 0.08, 0.12, 0.16, 0.2, 0.24, 0.28, 0.32, 0.36, 0.4, 0.44, 0.48, 0.52, 0.56, 0.6, 0.64, 0.68, 0.72, 0.76, 0.8, 0.84, 0.88, 0.9097555383, 0.9097555383, 0.9097555383, 0.9097555383, 0.9097555383, 0.9097555383], 5)
            make_face()
            # Profile area: 0.0194610473, perimeter: 1.0698910693
            with BuildLine():
                Line((38.7209146734, -11.4427273602), (38.4446441206, -11.3877431554))
                Line((38.4446441206, -11.3877431554), (38.2579996472, -11.3877431554))
                CenterArc((27.4941272199, -0.0101541037), 15.6623906943, -46.8811919065, 0.2934750619)
                Line((38.7209146734, -11.4427273602), (38.1995814837, -11.4427273602))
            make_face()
        # OneSide extrude, distance=-3.9409
        extrude(amount=-3.9409)
    return part.part


def model_44519_90af0df6_0000():
    """Model: Component45"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.3694974853, perimeter: 2.1548184011
            with Locations((-100, 37.5)):
                Circle(0.34295)
        # OneSide extrude, distance=7
        extrude(amount=7)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(7, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.3233195031, perimeter: 5.2531976217
            with BuildLine():
                Line((-99.484531106, 37.469061311), (-99.7154718623, 37.9309398126))
                Line((-99.7154718623, 37.9309398126), (-100.2309407564, 37.9618785016))
                Line((-100.2309407564, 37.9618785016), (-100.515468894, 37.530938689))
                Line((-100.515468894, 37.530938689), (-100.2845281377, 37.0690601874))
                Line((-100.2845281377, 37.0690601874), (-99.7690592436, 37.0381214984))
                Line((-99.7690592436, 37.0381214984), (-99.484531106, 37.469061311))
            make_face()
            with BuildLine():
                CenterArc((-100, 37.5), 0.34295, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.ADD)
    return part.part


def model_44519_90af0df6_0002():
    """Model: Component52"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((20, -15)):
                Circle(0.25)
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(2.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1500610956, perimeter: 3.7616880586
            with BuildLine():
                Line((20.3577352012, -15.0732054774), (20.2422654038, -14.7267949666))
                Line((20.2422654038, -14.7267949666), (19.8845302025, -14.6535894892))
                Line((19.8845302025, -14.6535894892), (19.6422647988, -14.9267945226))
                Line((19.6422647988, -14.9267945226), (19.7577345962, -15.2732050334))
                Line((19.7577345962, -15.2732050334), (20.1154697975, -15.3464105108))
                Line((20.1154697975, -15.3464105108), (20.3577352012, -15.0732054774))
            make_face()
            with BuildLine():
                CenterArc((20, -15), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.ADD)
    return part.part


def model_44519_90af0df6_0005():
    """Model: Component27"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.9760782022, perimeter: 7.0685834706
            with Locations((100, 75)):
                Circle(1.125)
        # OneSide extrude, distance=19
        extrude(amount=19)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(19, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.9521250281, perimeter: 16.8665424417
            with BuildLine():
                Line((101.5773502692, 75.4226497308), (100.4226497308, 76.5773502692))
                Line((100.4226497308, 76.5773502692), (98.8452994616, 76.1547005384))
                Line((98.8452994616, 76.1547005384), (98.4226497308, 74.5773502692))
                Line((98.4226497308, 74.5773502692), (99.5773502692, 73.4226497308))
                Line((99.5773502692, 73.4226497308), (101.1547005384, 73.8452994616))
                Line((101.1547005384, 73.8452994616), (101.5773502692, 75.4226497308))
            make_face()
            with BuildLine():
                CenterArc((100, 75), 1.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.ADD)
    return part.part


def model_44519_90af0df6_0014():
    """Model: Component20"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((-45, 50)):
                Circle(0.4)
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(3, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.5019333833, perimeter: 6.2442234034
            with BuildLine():
                Line((-44.3845301774, 49.9113259963), (-44.6154711488, 50.4886754998))
                Line((-44.6154711488, 50.4886754998), (-45.2309409714, 50.5773495035))
                Line((-45.2309409714, 50.5773495035), (-45.6154698226, 50.0886740037))
                Line((-45.6154698226, 50.0886740037), (-45.3845288512, 49.5113245002))
                Line((-45.3845288512, 49.5113245002), (-44.7690590286, 49.4226504965))
                Line((-44.7690590286, 49.4226504965), (-44.3845301774, 49.9113259963))
            make_face()
            with BuildLine():
                CenterArc((-45, 50), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((-45, 50)):
                Circle(0.4)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


def model_44519_90af0df6_0017():
    """Model: Component63"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((-70, 17.5)):
                Circle(1)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.2, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.7399196947, perimeter: 4.6759465056
            with Locations((-70, 17.5)):
                Circle(0.7442)
        # OneSide extrude, distance=-3.5
        extrude(amount=-3.5, mode=Mode.SUBTRACT)
    return part.part


def model_45007_990d2758_0004():
    """Model: 14. Rótula empujador volante"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 12 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.8959292489, perimeter: 10.798229715
            with BuildLine():
                CenterArc((-2.0929780582, 7.9925846452), 0.4, 0, 90)
                Line((-2.0929780582, 8.3925846452), (-2.7929780582, 8.3925846452))
                CenterArc((-2.7929780582, 7.9925846452), 0.4, 90, 90)
                Line((-3.1929780582, 7.9925846452), (-3.1929780582, 5.8925846452))
                Line((-3.1929780582, 5.8925846452), (-1.6929780582, 5.8925846452))
                Line((-1.6929780582, 5.8925846452), (-1.6929780582, 7.9925846452))
            make_face()
            with BuildLine():
                CenterArc((-2.4429780582, 7.6925846452), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5.8925846452, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((0.5000000075, 2.5000000373)):
                Circle(0.3)
        # OneSide extrude, distance=-1.2
        extrude(amount=-1.2, mode=Mode.SUBTRACT)
    return part.part


def model_45097_af426930_0000():
    """Model: resistor_0805 v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 29 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.002825254, perimeter: 0.3011173565
            with BuildLine():
                Line((0.094, -0.0674976613), (0.094, 0.0674972259))
                Line((0.094, 0.0674972259), (0.0792841413, 0.0674972251))
                CenterArc((0.32, 0), 0.25, 164.3363936286, 31.3272127428)
                Line((0.0792841413, -0.0674972251), (0.094, -0.0674976613))
            make_face()
            # Profile area: 0.0007992404, perimeter: 0.2776979669
            with BuildLine():
                Line((0.094, -0.0674976613), (0.095, -0.0674976909))
                CenterArc((0.095, -0.0624976909), 0.005, -90.0000000014, 90.0000000014)
                Line((0.1, -0.0624976909), (0.1, 0.0624976909))
                CenterArc((0.095000465, 0.0624976909), 0.004999535, 0, 89.9999999987)
                Line((0.095000465, 0.0674972259), (0.094, 0.0674972259))
                Line((0.094, -0.0674976613), (0.094, 0.0674972259))
            make_face()
        # OneSide extrude, distance=0.045
        extrude(amount=0.045)
    return part.part


def model_45097_af426930_0002():
    """Model: cap0805_03 v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 27 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0047840903, perimeter: 0.3123514225
            with BuildLine():
                Line((0.0574309377, -0.0605000009), (0.092, -0.0605000014))
                Line((0.092, -0.0605000014), (0.092, 0.0605))
                Line((0.092, 0.0605), (0.0574309379, 0.0605))
                CenterArc((0.3, -0.0000000009), 0.25, 165.9953877008, 28.0092243938)
            make_face()
            # Profile area: 0.0011265368, perimeter: 0.3990958389
            with BuildLine():
                Line((0.0579385409, -0.0625000009), (0.0949999999, -0.0625000014))
                CenterArc((0.095, -0.0575000014), 0.005, -90.0000008491, 90.0000008491)
                Line((0.1, -0.0575000014), (0.1, 0.0575))
                CenterArc((0.0950000014, 0.0575), 0.0049999986, 0, 89.9999991509)
                Line((0.0950000015, 0.0624999986), (0.0579385409, 0.0624999991))
                CenterArc((0.3, -0.0000000009), 0.25, 165.5224878141, 0.4728998867)
                Line((0.092, 0.0605), (0.0574309379, 0.0605))
                Line((0.092, -0.0605000014), (0.092, 0.0605))
                Line((0.0574309377, -0.0605000009), (0.092, -0.0605000014))
                CenterArc((0.3, -0.0000000009), 0.25, -165.9953879054, 0.4729000913)
            make_face()
        # OneSide extrude, distance=0.08
        extrude(amount=0.08)
    return part.part


def model_45241_7a955ec1_0010():
    """Model: cap0402 v2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 27 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0003606485, perimeter: 0.1790997568
            with BuildLine():
                Line((0.0262531407, -0.025), (0.045, -0.025))
                CenterArc((0.045, -0.02), 0.005, -89.9999999515, 89.9999999515)
                Line((0.05, -0.02), (0.05, 0.02))
                CenterArc((0.045, 0.02), 0.005, 0, 90.0000000485)
                Line((0.045, 0.025), (0.0262531407, 0.025))
                CenterArc((0.275, 0), 0.25, 174.2608295227, 0.4604943791)
                Line((0.044, 0.023), (0.0260602483, 0.023))
                Line((0.044, -0.023), (0.044, 0.023))
                Line((0.0260602483, -0.023), (0.044, -0.023))
                CenterArc((0.275, 0), 0.25, -174.7213238966, 0.4604943739)
            make_face()
            # Profile area: 0.0008577567, perimeter: 0.1279446425
            with BuildLine():
                Line((0.0260602483, -0.023), (0.044, -0.023))
                Line((0.044, -0.023), (0.044, 0.023))
                Line((0.044, 0.023), (0.0260602483, 0.023))
                CenterArc((0.275, 0), 0.25, 174.7213239018, 10.5573522016)
            make_face()
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)
    return part.part


def model_45285_dc1f2b6f_0003():
    """Model: paddle link v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 58.9732061909, perimeter: 53.4650599243
            with BuildLine():
                CenterArc((-14.5536527254, -16.8798953365), 1.829359149, 43.5987999085, 174.1567213465)
                Line((-16, -18), (-3.503984544, -29.8602981653))
                CenterArc((-2.5462485235, -28.8512270655), 1.3912162913, -133.5048784298, 174.0525862986)
                Line((-13.2288558814, -15.6183612631), (-1.4891120495, -27.9468238123))
            make_face()
            with BuildLine():
                CenterArc((-14.5536527254, -16.8798953365), 0.9340550331, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-2.5462485235, -28.8512270655), 0.5661455957, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


MODELS = {
    "model_41753_9b4f8d8a_0001": {"func": model_41753_9b4f8d8a_0001, "volume": 320.5995323633, "area": 781.3141137891},
    "model_41753_9b4f8d8a_0006": {"func": model_41753_9b4f8d8a_0006, "volume": 11.0916057828, "area": 97.1734639411},
    "model_41754_fb582b36_0000": {"func": model_41754_fb582b36_0000, "volume": 48.0663675999, "area": 78.2256570744},
    "model_41757_c1173a7e_0000": {"func": model_41757_c1173a7e_0000, "volume": 58.6071438898, "area": 148.7861804777},
    "model_41757_c1173a7e_0002": {"func": model_41757_c1173a7e_0002, "volume": 308.8888699797, "area": 283.7561834242},
    "model_41757_c1173a7e_0006": {"func": model_41757_c1173a7e_0006, "volume": 173.9044390222, "area": 594.0638484939},
    "model_41757_c1173a7e_0024": {"func": model_41757_c1173a7e_0024, "volume": 7.5789913144, "area": 44.3874140727},
    "model_41759_fb1f25f1_0000": {"func": model_41759_fb1f25f1_0000, "volume": 0.0120733071, "area": 0.3735999886},
    "model_41762_1fb3760e_0000": {"func": model_41762_1fb3760e_0000, "volume": 466.85928, "area": 3208.34552},
    "model_41762_228d379c_0000": {"func": model_41762_228d379c_0000, "volume": 16.3999997139, "area": 213.9999977469},
    "model_41762_67992d19_0000": {"func": model_41762_67992d19_0000, "volume": 9.8331850062, "area": 25.8395995805},
    "model_41762_942c9cc2_0000": {"func": model_41762_942c9cc2_0000, "volume": 84, "area": 857.6},
    "model_41762_d2d9e84d_0000": {"func": model_41762_d2d9e84d_0000, "volume": 27.4499995306, "area": 263.3999978542},
    "model_41762_e0b6edc5_0000": {"func": model_41762_e0b6edc5_0000, "volume": 53.4786005029, "area": 519.3871053644},
    "model_41776_50aabc9d_0003": {"func": model_41776_50aabc9d_0003, "volume": 2.8071988795, "area": 40.3859006085},
    "model_41776_50aabc9d_0006": {"func": model_41776_50aabc9d_0006, "volume": 1.1329173809, "area": 25.1281298709},
    "model_41778_3d8cc892_0008": {"func": model_41778_3d8cc892_0008, "volume": 144.791657803, "area": 554.7398712719},
    "model_41785_5fecc307_0000": {"func": model_41785_5fecc307_0000, "volume": 38.7784247168, "area": 574.2009153133},
    "model_41785_a4e25fe9_0000": {"func": model_41785_a4e25fe9_0000, "volume": 1.7946571853, "area": 9.4219086203},
    "model_41785_d82bdc46_0000": {"func": model_41785_d82bdc46_0000, "volume": 7.4680321746, "area": 79.173043609},
    "model_41789_6056d5cf_0008": {"func": model_41789_6056d5cf_0008, "volume": 7706.016846, "area": 12491.9105},
    "model_41789_6056d5cf_0010": {"func": model_41789_6056d5cf_0010, "volume": 2882.074881, "area": 4772.5711},
    "model_41789_6056d5cf_0013": {"func": model_41789_6056d5cf_0013, "volume": 5101.5299292585, "area": 8300.3928445949},
    "model_41789_6056d5cf_0014": {"func": model_41789_6056d5cf_0014, "volume": 3725.0165188033, "area": 6093.945588203},
    "model_41845_866e0992_0007": {"func": model_41845_866e0992_0007, "volume": 0.00002025, "area": 0.00585},
    "model_41845_a5180a74_0001": {"func": model_41845_a5180a74_0001, "volume": 0.0071667582, "area": 0.3259402378},
    "model_41845_a5180a74_0006": {"func": model_41845_a5180a74_0006, "volume": 0.1025926351, "area": 1.566869336},
    "model_41859_173a686e_0002": {"func": model_41859_173a686e_0002, "volume": 0.3169651652, "area": 4.7317900586},
    "model_41859_173a686e_0003": {"func": model_41859_173a686e_0003, "volume": 0.1734315487, "area": 2.9537967677},
    "model_41859_173a686e_0005": {"func": model_41859_173a686e_0005, "volume": 0.3090161564, "area": 3.5424628644},
    "model_41859_173a686e_0009": {"func": model_41859_173a686e_0009, "volume": 0.1814780923, "area": 3.1067902732},
    "model_41878_3aeaed3d_0000": {"func": model_41878_3aeaed3d_0000, "volume": 3, "area": 15},
    "model_41892_7b3433f9_0000": {"func": model_41892_7b3433f9_0000, "volume": 47.4455114562, "area": 196.9047910768},
    "model_41896_7d8659e6_0005": {"func": model_41896_7d8659e6_0005, "volume": 26.4309578936, "area": 130.1622512133},
    "model_41896_7d8659e6_0008": {"func": model_41896_7d8659e6_0008, "volume": 3.5130634352, "area": 26.0880926566},
    "model_41896_7d8659e6_0020": {"func": model_41896_7d8659e6_0020, "volume": 3.7507848421, "area": 38.8230725775},
    "model_41902_43d78d0f_0008": {"func": model_41902_43d78d0f_0008, "volume": 977.8172880321, "area": 980.8102178631},
    "model_41902_43d78d0f_0013": {"func": model_41902_43d78d0f_0013, "volume": 918.4050118984, "area": 1207.4643020752},
    "model_41902_43d78d0f_0016": {"func": model_41902_43d78d0f_0016, "volume": 398.6310928793, "area": 613.0460227328},
    "model_41902_43d78d0f_0025": {"func": model_41902_43d78d0f_0025, "volume": 5029.7166097065, "area": 8040.9208247105},
    "model_41907_7bcecdb1_0000": {"func": model_41907_7bcecdb1_0000, "volume": 0.5415191275, "area": 12.370408958},
    "model_41920_1455d829_0000": {"func": model_41920_1455d829_0000, "volume": 6164.5267557917, "area": 2786.0413503962},
    "model_41941_79d46bb4_0002": {"func": model_41941_79d46bb4_0002, "volume": 0.6653148213, "area": 6.3096034636},
    "model_41941_79d46bb4_0003": {"func": model_41941_79d46bb4_0003, "volume": 20.3465681305, "area": 61.6465374044},
    "model_41941_79d46bb4_0010": {"func": model_41941_79d46bb4_0010, "volume": 276.649913896, "area": 331.4641301693},
    "model_41942_29c07f06_0003": {"func": model_41942_29c07f06_0003, "volume": 59.3079675454, "area": 178.7494730651},
    "model_41942_29c07f06_0014": {"func": model_41942_29c07f06_0014, "volume": 0.0598242371, "area": 2.7281501811},
    "model_41970_24ba0c1b_0001": {"func": model_41970_24ba0c1b_0001, "volume": 4.8464740182, "area": 54.3092923466},
    "model_41970_24ba0c1b_0002": {"func": model_41970_24ba0c1b_0002, "volume": 0.7194654917, "area": 9.7152212091},
    "model_41970_24ba0c1b_0011": {"func": model_41970_24ba0c1b_0011, "volume": 2.0526110083, "area": 25.1725595629},
    "model_41973_0e5cd44c_0001": {"func": model_41973_0e5cd44c_0001, "volume": 56, "area": 312.8},
    "model_41978_0c8a92df_0000": {"func": model_41978_0c8a92df_0000, "volume": 0.0017646886, "area": 0.1459689046},
    "model_41978_4adb96a6_0000": {"func": model_41978_4adb96a6_0000, "volume": 0.2332632545, "area": 2.6860617188},
    "model_41978_4e426020_0000": {"func": model_41978_4e426020_0000, "volume": 1.4272920066, "area": 8.6042474782},
    "model_41978_f3c5934a_0000": {"func": model_41978_f3c5934a_0000, "volume": 92.5988806939, "area": 421.9671172071},
    "model_41982_f75ceb8f_0000": {"func": model_41982_f75ceb8f_0000, "volume": 72.2573495266, "area": 121.9582609281},
    "model_41982_f75ceb8f_0002": {"func": model_41982_f75ceb8f_0002, "volume": 67.5, "area": 693.6},
    "model_41982_f75ceb8f_0006": {"func": model_41982_f75ceb8f_0006, "volume": 69.66, "area": 162.4},
    "model_41982_f75ceb8f_0021": {"func": model_41982_f75ceb8f_0021, "volume": 15.4602875206, "area": 162.4303085941},
    "model_41982_f75ceb8f_0023": {"func": model_41982_f75ceb8f_0023, "volume": 50.8938009882, "area": 118.186715628},
    "model_42015_efbcca8b_0000": {"func": model_42015_efbcca8b_0000, "volume": 5.4920895473, "area": 36.1687696544},
    "model_42015_efbcca8b_0004": {"func": model_42015_efbcca8b_0004, "volume": 14.6966879204, "area": 62.5129954277},
    "model_42015_efbcca8b_0005": {"func": model_42015_efbcca8b_0005, "volume": 23.8548224378, "area": 81.0104005359},
    "model_42044_ee2c1949_0005": {"func": model_42044_ee2c1949_0005, "volume": 0.0427757589, "area": 0.924797209},
    "model_42143_51b31600_0007": {"func": model_42143_51b31600_0007, "volume": 1.3018932887, "area": 18.1994331563},
    "model_42329_df7f540f_0054": {"func": model_42329_df7f540f_0054, "volume": 0.1857681843, "area": 4.6540250943},
    "model_42429_967ff817_0000": {"func": model_42429_967ff817_0000, "volume": 0.3541880539, "area": 5.0052928111},
    "model_42429_deca15fc_0000": {"func": model_42429_deca15fc_0000, "volume": 264.2054234808, "area": 371.3843832182},
    "model_42535_9efbd860_0000": {"func": model_42535_9efbd860_0000, "volume": 2053.0972450962, "area": 2812.4777960769},
    "model_42540_6eb6c3bc_0000": {"func": model_42540_6eb6c3bc_0000, "volume": 24706042.0532062873, "area": 575777.588644235},
    "model_42542_483aa73d_0000": {"func": model_42542_483aa73d_0000, "volume": 31.4159265359, "area": 69.115038379},
    "model_42545_7e4c4d38_0000": {"func": model_42545_7e4c4d38_0000, "volume": 12.8198803924, "area": 112.975694457},
    "model_42577_2275594e_0000": {"func": model_42577_2275594e_0000, "volume": 920.0637961666, "area": 1068.1400786554},
    "model_42586_517832f9_0020": {"func": model_42586_517832f9_0020, "volume": 681.2900105413, "area": 2760.3256239331},
    "model_42601_bfe96b47_0007": {"func": model_42601_bfe96b47_0007, "volume": 6303.2322238984, "area": 21054.4374121933},
    "model_42811_4743cfd2_0000": {"func": model_42811_4743cfd2_0000, "volume": 1.5362096915, "area": 14.5267625426},
    "model_42811_75f8e8a3_0000": {"func": model_42811_75f8e8a3_0000, "volume": 6.4787080599, "area": 29.3682431025},
    "model_42811_a0527cb1_0000": {"func": model_42811_a0527cb1_0000, "volume": 4.4907018596, "area": 24.5341253435},
    "model_42937_fd3c1e0b_0003": {"func": model_42937_fd3c1e0b_0003, "volume": 0.3433499873, "area": 5.8935345661},
    "model_43009_6aa4e085_0011": {"func": model_43009_6aa4e085_0011, "volume": 3.3796967627, "area": 56.3242255781},
    "model_43441_e1ab0873_0000": {"func": model_43441_e1ab0873_0000, "volume": 2.7532741229, "area": 15.9716802635},
    "model_43529_4804941b_0018": {"func": model_43529_4804941b_0018, "volume": 3.0376456648, "area": 16.6236654305},
    "model_43529_4804941b_0021": {"func": model_43529_4804941b_0021, "volume": 8.1053090463, "area": 35.8141562509},
    "model_43529_4804941b_0055": {"func": model_43529_4804941b_0055, "volume": 1420.328761102, "area": 4771.8341592654},
    "model_43628_a95b7e66_0013": {"func": model_43628_a95b7e66_0013, "volume": 0.3392920066, "area": 7.3513268094},
    "model_43628_a95b7e66_0029": {"func": model_43628_a95b7e66_0029, "volume": 0.688420767, "area": 8.6657500748},
    "model_43628_a95b7e66_0030": {"func": model_43628_a95b7e66_0030, "volume": 0.3246040961, "area": 2.7712154674},
    "model_43628_a95b7e66_0034": {"func": model_43628_a95b7e66_0034, "volume": 0.1759291886, "area": 3.9584067435},
    "model_43928_6ca53538_0003": {"func": model_43928_6ca53538_0003, "volume": 0.480907263, "area": 5.5362800976},
    "model_43928_6ca53538_0005": {"func": model_43928_6ca53538_0005, "volume": 0.0219788767, "area": 0.4977460861},
    "model_43928_6ca53538_0016": {"func": model_43928_6ca53538_0016, "volume": 0.0408525761, "area": 1.6370644779},
    "model_43928_6ca53538_0020": {"func": model_43928_6ca53538_0020, "volume": 0.1059070509, "area": 2.3965297201},
    "model_43928_6ca53538_0024": {"func": model_43928_6ca53538_0024, "volume": 0.3589269607, "area": 11.2940255897},
    "model_43928_6ca53538_0031": {"func": model_43928_6ca53538_0031, "volume": 1.6611952084, "area": 24.6288530377},
    "model_43931_bb001c04_0002": {"func": model_43931_bb001c04_0002, "volume": 2577.0877236479, "area": 2778.3460030185},
    "model_43931_bb001c04_0010": {"func": model_43931_bb001c04_0010, "volume": 93619.4610769758, "area": 23222.6528953358},
    "model_43932_4bfdfe7b_0007": {"func": model_43932_4bfdfe7b_0007, "volume": 77.2908046906, "area": 207.2897452596},
    "model_43933_3b763a09_0002": {"func": model_43933_3b763a09_0002, "volume": 7.7942286341, "area": 25.9807621135},
    "model_43933_3b763a09_0003": {"func": model_43933_3b763a09_0003, "volume": 1.3917255455, "area": 12.6292024674},
    "model_43934_912ff891_0007": {"func": model_43934_912ff891_0007, "volume": 1.1790610646, "area": 8.3150269152},
    "model_43934_912ff891_0015": {"func": model_43934_912ff891_0015, "volume": 2.5750430666, "area": 14.5876010675},
    "model_43934_912ff891_0017": {"func": model_43934_912ff891_0017, "volume": 0.8332190577, "area": 8.4886060513},
    "model_43934_912ff891_0019": {"func": model_43934_912ff891_0019, "volume": 0.8967947185, "area": 11.5357330644},
    "model_43934_912ff891_0023": {"func": model_43934_912ff891_0023, "volume": 1.7537940989, "area": 12.5977865409},
    "model_43934_912ff891_0024": {"func": model_43934_912ff891_0024, "volume": 1.9682077975, "area": 11.7652644877},
    "model_43936_666b7568_0003": {"func": model_43936_666b7568_0003, "volume": 43126.2131521539, "area": 10601.3044095388},
    "model_44206_ff45fbf0_0006": {"func": model_44206_ff45fbf0_0006, "volume": 0.0004963653, "area": 0.0723526097},
    "model_44209_972a6882_0000": {"func": model_44209_972a6882_0000, "volume": 129.9038105677, "area": 189.9038105677},
    "model_44210_a155c2d1_0000": {"func": model_44210_a155c2d1_0000, "volume": 125.7174203249, "area": 620.6473694809},
    "model_44212_042d1bc2_0000": {"func": model_44212_042d1bc2_0000, "volume": 1389.927558228, "area": 1163.4722007006},
    "model_44323_3bf3f9ca_0000": {"func": model_44323_3bf3f9ca_0000, "volume": 94.2477796077, "area": 434.1311412594},
    "model_44354_07805a0e_0000": {"func": model_44354_07805a0e_0000, "volume": 256.7291573968, "area": 322.1458494666},
    "model_44375_f48f985a_0000": {"func": model_44375_f48f985a_0000, "volume": 1017.1012928192, "area": 1293.9559149602},
    "model_44519_90af0df6_0000": {"func": model_44519_90af0df6_0000, "volume": 2.6834782482, "area": 16.7524310304},
    "model_44519_90af0df6_0002": {"func": model_44519_90af0df6_0002, "volume": 0.5208860712, "area": 4.7438311708},
    "model_44519_90af0df6_0005": {"func": model_44519_90af0df6_0005, "volume": 78.4976108699, "area": 150.8888679021},
    "model_44519_90af0df6_0014": {"func": model_44519_90af0df6_0014, "volume": 1.7088821153, "area": 10.2951886404},
    "model_44519_90af0df6_0017": {"func": model_44519_90af0df6_0017, "volume": 0.2803345918, "area": 4.9951722803},
    "model_45007_990d2758_0004": {"func": model_45007_990d2758_0004, "volume": 2.5566372423, "area": 18.8520349234},
    "model_45097_af426930_0000": {"func": model_45097_af426930_0000, "volume": 0.0001631022, "area": 0.0211461384},
    "model_45097_af426930_0002": {"func": model_45097_af426930_0002, "volume": 0.0004728502, "area": 0.0383149349},
    "model_45241_7a955ec1_0010": {"func": model_45241_7a955ec1_0010, "volume": 0.0000609203, "area": 0.00960108},
    "model_45285_dc1f2b6f_0003": {"func": model_45285_dc1f2b6f_0003, "volume": 117.9464123817, "area": 224.8765322303},
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
