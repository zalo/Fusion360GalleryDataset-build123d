"""Batch 011 - passing/04_6to7ops
49 models bundled from Fusion360 Gallery reconstructions.
"""

from build123d import *
from build123d import Edge, BuildLine
from collections import Counter
from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
from OCP.Geom import Geom_BSplineCurve
from OCP.TColStd import TColStd_Array1OfReal, TColStd_Array1OfInteger
from OCP.TColgp import TColgp_Array1OfPnt
from OCP.gp import gp_Pnt


def model_83100_215c1f32_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 42.2187384345, perimeter: 24.1867732449
            with BuildLine():
                Line((0.0179491924, -4.0310889132), (3.5, -2))
                Line((3.5, -2), (3.4820508076, 2.0310889132))
                Line((3.4820508076, 2.0310889132), (-0.0179491924, 4.0310889132))
                Line((-0.0179491924, 4.0310889132), (-3.5, 2))
                Line((-3.5, 2), (-3.4820508076, -2.0310889132))
                Line((-3.4820508076, -2.0310889132), (0.0179491924, -4.0310889132))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.4977871438, perimeter: 29.0366120824
            with BuildLine():
                CenterArc((0, 0), 2.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.1213203436, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 14.1371669412, perimeter: 13.3286488145
            Circle(2.1213203436)
        # OneSide extrude, distance=-9.5
        extrude(amount=-9.5, mode=Mode.SUBTRACT)
    return part.part


def model_83113_d57d4ccf_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 44.125, perimeter: 45
            with BuildLine():
                Line((17.5, 1.75), (17.5, 0))
                Line((4, 1.75), (17.5, 1.75))
                Line((4, 5.5), (4, 1.75))
                Line((1.5, 5.5), (4, 5.5))
                Line((0, 3.5), (1.5, 5.5))
                Line((0, 0), (0, 3.5))
                Line((17.5, 0), (0, 0))
            make_face()
        # OneSide extrude, distance=6
        extrude(amount=6)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(17.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 14.2206568476, perimeter: 20.8626866932
            with BuildLine():
                Line((-1.9375014484, 5.9529050706), (-1.8753843521, 5.7631840032))
                CenterArc((-3, 5.5), 1.1550005087, 23.0868146383, 133.8263707234)
                Line((-4.0624985516, 5.9529050706), (-4.1246156479, 5.7631840032))
                Line((-4.1246156479, 5.7631840032), (-5.4385832572, 1.75))
                Line((-5.4385832572, 1.75), (-0.5614167428, 1.75))
                Line((-1.8753843521, 5.7631840032), (-0.5614167428, 1.75))
            make_face()
            with BuildLine():
                CenterArc((-3, 5.5), 0.7071067812, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(17.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4.2135750847, perimeter: 9.5
            with BuildLine():
                Line((-1.5, 0), (-1.5, 1))
                Line((-1.5, 1), (-2.1909499435, 1))
                Line((-2.1909499435, 1), (-2.1909499435, 1.75))
                Line((-3.8090500565, 1.75), (-2.1909499435, 1.75))
                Line((-3.8090500565, 1), (-3.8090500565, 1.75))
                Line((-4.5, 1), (-3.8090500565, 1))
                Line((-4.5, 0), (-4.5, 1))
                Line((-4.5, 0), (-1.5, 0))
            make_face()
        # OneSide extrude, distance=-20
        extrude(amount=-20, mode=Mode.SUBTRACT)
    return part.part


def model_83210_07c13a64_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 32 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 6.5098672286, perimeter: 43.1407075111
            with BuildLine():
                CenterArc((4.5, -0.5), 0.5, 0, 90)
                Line((0, 0), (4.5, 0))
                Line((0, 0), (0, -0.3))
                Line((0, -0.3), (4.5, -0.3))
                CenterArc((4.5, -0.5), 0.2, 0, 90)
                Line((4.7, -0.5), (4.7, -3.3))
                CenterArc((5.2, -3.3), 0.5, 180, 90)
                Line((5.2, -3.8), (9.8, -3.8))
                CenterArc((9.8, -3.3), 0.5, -90, 90)
                Line((10.3, -3.3), (10.3, -0.5))
                CenterArc((10.5, -0.5), 0.2, 90, 90)
                Line((10.5, -0.3), (15, -0.3))
                Line((15, 0), (15, -0.3))
                Line((10.5, 0), (15, 0))
                CenterArc((10.5, -0.5), 0.5, 90, 90)
                Line((10, -3), (10, -0.5))
                CenterArc((9.5, -3), 0.5, -90, 90)
                Line((5.5, -3.5), (9.5, -3.5))
                CenterArc((5.5, -3), 0.5, 180, 90)
                Line((5, -0.5), (5, -3))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -3.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.0053311702, perimeter: 17.6639822061
            with BuildLine():
                CenterArc((-7.5, 2.5), 1.5757939792, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-7.5, 2.5), 1.2355161036, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -3.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853985379, perimeter: 3.1415934026
            with Locations((-7.5, 2.5)):
                Circle(0.5000001192)
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)
    return part.part


def model_83236_24c6e9d2_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 31.12, perimeter: 38.2627416998
            with BuildLine():
                Line((-11.8, 1.6), (0, 1.6))
                Line((-11.8, 5.2), (-11.8, 1.6))
                Line((-12.8, 5.2), (-11.8, 5.2))
                Line((-14.4, 3.6), (-12.8, 5.2))
                Line((-14.4, 0), (-14.4, 3.6))
                Line((0, 0), (-14.4, 0))
                Line((0, 1.6), (0, 0))
            make_face()
        # OneSide extrude, distance=6.4
        extrude(amount=6.4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 11.0389302469, perimeter: 19.9849004274
            with BuildLine():
                CenterArc((-3.189817914, 3.5999856007), 1.6, 25, 129.6758937044)
                Line((-4.6360621789, 4.2843667271), (-5.9063385555, 1.6))
                Line((-5.9063385555, 1.6), (-0.4918046419, 1.6))
                Line((-1.7397254547, 4.2761748195), (-0.4918046419, 1.6))
            make_face()
            with BuildLine():
                CenterArc((-3.189817914, 3.5999856007), 0.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-2.2
        extrude(amount=-2.2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 3.68, perimeter: 9.6
            with BuildLine():
                Line((-1.6, 0), (-1.6, 0.7))
                Line((-1.6, 0.7), (-2.4, 0.7))
                Line((-2.4, 0.7), (-2.4, 1.6))
                Line((-2.4, 1.6), (-4, 1.6))
                Line((-4, 0.7), (-4, 1.6))
                Line((-4.8, 0.7), (-4, 0.7))
                Line((-4.8, 0), (-4.8, 0.7))
                Line((-4.8, 0), (-1.6, 0))
            make_face()
        # OneSide extrude, distance=-20
        extrude(amount=-20, mode=Mode.SUBTRACT)
    return part.part


def model_83362_2bb27f28_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with Locations((1.6287539262, -1.3864131398)):
                Circle(0.75)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.9940754664, perimeter: 3.5343911399
            with Locations((-1.6287539262, 1.3864131398)):
                Circle(0.5625158207)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)
    return part.part


def model_83409_4e6ef323_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch3 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.1962448351, perimeter: 12.362448351
            with BuildLine():
                Line((5, -0.2), (6.3737034184, -0.2))
                Line((6.3737034184, -0.2), (4.2307910637, 3.014368532))
                Line((4.2307910637, 3.014368532), (4.6788854382, 3.9105572809))
                Line((4.5, 4), (4.6788854382, 3.9105572809))
                Line((4, 3), (4.5, 4))
                Line((6, 0), (4, 3))
                Line((5, 0), (6, 0))
                Line((5, -0.2), (5, 0))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


def model_83423_7ea0c866_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 12.5457651055, perimeter: 15.5897256042
            with BuildLine():
                Line((2.7617665016, -1.1356648995), (2.7617665016, 1.1356648995))
                Line((2.7617665016, 1.1356648995), (-2.7617665016, 1.1356648995))
                Line((-2.7617665016, 1.1356648995), (-2.7617665016, -1.1356648995))
                Line((-2.7617665016, -1.1356648995), (2.7617665016, -1.1356648995))
            make_face()
        # Symmetric extrude, each_side=0.15
        extrude(amount=0.15, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.15, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0903339279, perimeter: 1.2269742245
            with BuildLine():
                CenterArc((2.4000000358, 0), 0.15, 112.6175276227, 314.7649447547)
                CenterArc((2.4000000358, 0.200000003), 0.0843471613, -46.8493174565, 273.698634913)
            make_face()
        # Symmetric extrude, each_side=0.1
        extrude(amount=0.1, both=True, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.15, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.3200000095, perimeter: 3.6000000536
            with BuildLine():
                Line((-2.5000000373, 0.8000000119), (-2.3000000343, 0.8000000119))
                Line((-2.5000000373, -0.8000000119), (-2.5000000373, 0.8000000119))
                Line((-2.3000000343, -0.8000000119), (-2.5000000373, -0.8000000119))
                Line((-2.3000000343, 0.8000000119), (-2.3000000343, -0.8000000119))
            make_face()
        # Symmetric extrude, each_side=0.1
        extrude(amount=0.1, both=True, mode=Mode.SUBTRACT)
    return part.part


def model_85541_199004a0_0002():
    """Model: Component2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 175.8200110274, perimeter: 64.3422751482
            with BuildLine():
                Line((5.8736974182, 7), (7.1079862832, 0))
                Line((7.1079862832, 0), (31.6079862832, 0))
                Line((31.6079862832, 0), (31.6079862832, 7))
                Line((31.6079862832, 7), (5.8736974182, 7))
            make_face()
        # OneSide extrude, distance=7
        extrude(amount=7)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 7, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 180.1400220547, perimeter: 65.4685777299
            with BuildLine():
                Line((-31.6079862832, 7), (-31.6079862832, 0))
                Line((-31.6079862832, 0), (-5.8736974182, 0))
                Line((-5.8736974182, 0), (-5.8736974182, 7))
                Line((-5.8736974182, 7), (-31.6079862832, 7))
            make_face()
        # OneSide extrude, distance=-0.7
        extrude(amount=-0.7, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 6.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.5362703988, perimeter: 9.5621778265
            with BuildLine():
                Line((-31.6079862832, 3.5), (-29.587260341, 7))
                Line((-29.587260341, 7), (-31.6079862832, 7))
                Line((-31.6079862832, 7), (-31.6079862832, 3.5))
            make_face()
            # Profile area: 3.5362703988, perimeter: 9.5621778265
            with BuildLine():
                Line((-31.6079862832, 3.5), (-29.587260341, 0))
                Line((-31.6079862832, 3.5), (-31.6079862832, 0))
                Line((-31.6079862832, 0), (-29.587260341, 0))
            make_face()
        # OneSide extrude, distance=-8.87
        extrude(amount=-8.87, mode=Mode.SUBTRACT)
    return part.part


def model_85552_3669d6cf_0000():
    """Model: Horquilla"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1710508806, perimeter: 1.8853981634
            with BuildLine():
                Line((3.9000000581, 0.000000003), (4.1000000581, 0.000000003))
                Line((4.1000000581, 0.000000003), (4.1000000581, 0.600000003))
                Line((4.1000000581, 0.600000003), (3.9000000581, 0.600000003))
                CenterArc((3.9000000581, 0.500000003), 0.1, 90, 180)
                Line((3.9000000581, 0.300000003), (3.9000000581, 0.400000003))
                CenterArc((3.9000000581, 0.150000003), 0.15, 90, 180)
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(4.1000000581, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.096211275, perimeter: 1.0995574288
            with Locations((0.300000003, 0.4)):
                Circle(0.175)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(4.8000000581, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.0090560296, perimeter: 0.5284610337
            with BuildLine():
                Line((0.175000003, 0.5224744871), (0.425000003, 0.5224744871))
                CenterArc((0.300000003, 0.4), 0.175, 44.4153085972, 91.1693828056)
            make_face()
        # OneSide extrude, distance=-0.35
        extrude(amount=-0.35, mode=Mode.SUBTRACT)
    return part.part


def model_86099_c101852f_0001():
    """Model: lamp part v1"""
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
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.4977871438, perimeter: 21.9911485751
            with BuildLine():
                CenterArc((0, 0), 2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.0685834706, perimeter: 28.2743338823
            with BuildLine():
                CenterArc((0, 0), 2.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 5.4977871438, perimeter: 21.9911485751
            with BuildLine():
                CenterArc((0, 0), 2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            Circle(1.5)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


def model_86303_87045e9c_0000():
    """Model: Typical bordeaux v1"""
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
        # Sketch3 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 108.9983717624, perimeter: 42.1076399805
            with BuildLine():
                Line((6.3836825082, -7.8133088642), (6.3836825082, 1.3654682433))
                Line((6.3836825082, 1.3654682433), (-5.4913603745, 1.3654682433))
                Line((-5.4913603745, 1.3654682433), (-5.4913603745, -7.8133088642))
                Line((-5.4913603745, -7.8133088642), (6.3836825082, -7.8133088642))
            make_face()
        # Symmetric extrude, each_side=-7.5
        extrude(amount=-7.5, both=True)

        # Sketch4 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 22.5, perimeter: 19
            with BuildLine():
                Line((3, 9), (3, 14))
                Line((3, 14), (-1.5, 14))
                Line((-1.5, 14), (-1.5, 9))
                Line((-1.5, 9), (3, 9))
            make_face()
        # Symmetric extrude, each_side=3
        extrude(amount=3, both=True)
    return part.part


def model_86378_fb294b8e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 25 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.5, perimeter: 15
            with BuildLine():
                Line((2.5, 2), (2.5, 0))
                Line((-3, 2), (2.5, 2))
                Line((-3, 2), (-3, 1.5))
                Line((2, 1.5), (-3, 1.5))
                Line((2, 0), (2, 1.5))
                Line((2, 0), (2.5, 0))
            make_face()
            # Profile area: 18, perimeter: 72.5
            with BuildLine():
                Line((2, 0), (2.5, 0))
                Line((-3, 0), (2, 0))
                Line((-3, 0), (-3, -0.5))
                Line((-3, -0.5), (5, -0.5))
                Line((5, -0.5), (5, -1))
                Line((5, -1), (5.5, -1))
                Line((5.5, -1), (5.5, 7.5))
                Line((5.5, 7.5), (6.5, 7.5))
                Line((6.5, 7.5), (6.5, 8))
                Line((6.5, 8), (-4.5, 8))
                Line((-4.5, 8), (-4.5, 7.5))
                Line((-4.5, 7.5), (-3.5, 7.5))
                Line((-3.5, 7.5), (-3.5, -1))
                Line((-3.5, -1), (-3, -1))
                Line((-3, -1), (-3, -0.5))
                Line((-3, 1.5), (-3, 0))
                Line((-3, 2), (-3, 1.5))
                Line((-3, 7.5), (-3, 2))
                Line((-3, 7.5), (5, 7.5))
                Line((5, 7.5), (5, 0))
                Line((2.5, 0), (5, 0))
            make_face()
        # OneSide extrude, distance=7
        extrude(amount=7)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(7, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 5.5, perimeter: 23
            with BuildLine():
                Line((-3, 7.5), (-3.5, 7.5))
                Line((5, 7.5), (-3, 7.5))
                Line((5.5, 7.5), (5, 7.5))
                Line((6.5, 7.5), (5.5, 7.5))
                Line((6.5, 8), (6.5, 7.5))
                Line((-4.5, 8), (6.5, 8))
                Line((-4.5, 7.5), (-4.5, 8))
                Line((-3.5, 7.5), (-4.5, 7.5))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 10 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 14.283504205, perimeter: 54.8497719636
            with BuildLine():
                Line((-8.5, 4), (-0.5769199178, 4))
                Line((-0.5769199178, 4), (-0.5769199178, -6))
                Line((-0.5769199178, -6), (-8.5, -5.9963890237))
                Line((-8.5, -5.9963890237), (-8.5, -6.5))
                Line((-8.5, -6.5), (0, -6.5))
                Line((0, -6.5), (0, 4.5))
                Line((0, 4.5), (-8.5, 4.5))
                Line((-8.5, 4.5), (-8.5, 4))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch3 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 10 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2447698388, perimeter: 1.7538154149
            with Locations((-2.4749929871, 1.9866830033)):
                Circle(0.2791283926)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


def model_86386_ce62c3a1_0000():
    """Model: Component1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 78.5398163397, perimeter: 31.4159265359
            with Locations((-30, 0)):
                Circle(5)
        # OneSide extrude, distance=7.5
        extrude(amount=7.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 7.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2297.2896279375, perimeter: 204.2035224833
            with BuildLine():
                CenterArc((30, 0), 27.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((30, 0), 5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 78.5398163397, perimeter: 31.4159265359
            with Locations((30, 0)):
                Circle(5)
        # OneSide extrude, distance=2.5
        extrude(amount=2.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 39 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 10, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 26.4984567107, perimeter: 54.9907971115
            with BuildLine():
                Line((30.5, 0), (30.5, -0.5))
                Line((30.5, -0.5), (56.9953699734, -0.5))
                CenterArc((30, 0), 27, -1.0610936076, 2.1221872152)
                Line((30.5, 0.5), (56.9953699734, 0.5))
                Line((30.5, 0), (30.5, 0.5))
            make_face()
            # Profile area: 21.4020999526, perimeter: 86.6083998103
            with BuildLine():
                CenterArc((30, 0), 27, 135, 43.9389063924)
                Line((10.908116908, 19.091883092), (10.5545635174, 19.4454364826))
                CenterArc((30, 0), 27.5, 135, 90)
                Line((10.908116908, -19.091883092), (10.5545635174, -19.4454364826))
                CenterArc((30, 0), 27, -178.9389063924, 43.9389063924)
                CenterArc((30, 0), 27, 178.9389063924, 2.1221872152)
            make_face()
            # Profile area: 0.25, perimeter: 2
            with BuildLine():
                Line((30, 0), (30.5, 0))
                Line((30, -0.5), (30, 0))
                Line((30, -0.5), (30.5, -0.5))
                Line((30.5, 0), (30.5, -0.5))
            make_face()
            # Profile area: 0.25, perimeter: 2
            with BuildLine():
                Line((30.5, 0), (30.5, 0.5))
                Line((30, 0.5), (30.5, 0.5))
                Line((30, 0.5), (30, 0))
                Line((30, 0), (30.5, 0))
            make_face()
            # Profile area: 26.4984567107, perimeter: 54.9907971115
            with BuildLine():
                Line((30, -0.5), (29.5, -0.5))
                Line((29.5, -0.5), (29.5, -26.9953699734))
                CenterArc((30, 0), 27, -91.0610936076, 2.1221872152)
                Line((30.5, -0.5), (30.5, -26.9953699734))
                Line((30, -0.5), (30.5, -0.5))
            make_face()
            # Profile area: 21.402181684, perimeter: 86.6087268408
            with BuildLine():
                CenterArc((30, 0), 27, -45, 43.9389063924)
                Line((49.091883092, -19.091883092), (49.4454364826, -19.4454364826))
                CenterArc((30, 0), 27.5, -45, 90.0006811438)
                Line((49.091883092, 19.091883092), (49.44520531, 19.4456676525))
                CenterArc((30, 0), 27, 1.0610936076, 43.9389063924)
                CenterArc((30, 0), 27, -1.0610936076, 2.1221872152)
            make_face()
            # Profile area: 26.4984567107, perimeter: 54.9907971115
            with BuildLine():
                Line((30.5, 0.5), (30.5, 26.9953699734))
                CenterArc((30, 0), 27, 88.9389063924, 2.1221872152)
                Line((29.5, 0.5), (29.5, 26.9953699734))
                Line((30, 0.5), (29.5, 0.5))
                Line((30, 0.5), (30.5, 0.5))
            make_face()
            # Profile area: 0.5, perimeter: 3
            with BuildLine():
                Line((30, 0.5), (30, 0))
                Line((30, 0.5), (29.5, 0.5))
                Line((29.5, -0.5), (29.5, 0.5))
                Line((30, -0.5), (29.5, -0.5))
                Line((30, -0.5), (30, 0))
            make_face()
            # Profile area: 26.4984567107, perimeter: 54.9907971115
            with BuildLine():
                Line((29.5, 0.5), (3.0046300266, 0.5))
                CenterArc((30, 0), 27, 178.9389063924, 2.1221872152)
                Line((29.5, -0.5), (3.0046300266, -0.5))
                Line((29.5, -0.5), (29.5, 0.5))
            make_face()
        # OneSide extrude, distance=55
        extrude(amount=55, mode=Mode.ADD)
    return part.part


def model_86704_3f8f3bfe_0003():
    """Model: Handrail"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 105.2683160093), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 5.067074791, perimeter: 7.9796453401
            with Locations((-6.3499999046, 25.3999996185)):
                Circle(1.27)
        # OneSide extrude, distance=-121.92
        extrude(amount=-121.92)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 105.2683160093), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 3.4002051697, perimeter: 6.5366840468
            with Locations((-6.3499999046, 25.3999996185)):
                Circle(1.0403455775)
        # OneSide extrude, distance=-121.92
        extrude(amount=-121.92, mode=Mode.SUBTRACT)
    return part.part


def model_86905_949d0ba4_0000():
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
        # OneSide extrude, distance=1.4
        extrude(amount=1.4)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 12 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.8588505205, perimeter: 51.9380520836
            with BuildLine():
                Line((-3.5, -3.5), (3.5, -3.5))
                Line((3.5, -3.5), (3.5, 3.5))
                Line((3.5, 3.5), (-3.5, 3.5))
                Line((-3.5, 3.5), (-3.5, -3.5))
            make_face()
            with BuildLine():
                CenterArc((1.5, -1.5), 1.9, -90, 90)
                Line((-1.5, -3.4), (1.5, -3.4))
                CenterArc((-1.5, -1.5), 1.9, -180, 90)
                Line((-3.4, 1.5), (-3.4, -1.5))
                CenterArc((-1.5, 1.5), 1.9, 90, 90)
                Line((1.5, 3.4), (-1.5, 3.4))
                CenterArc((1.5, 1.5), 1.9, 0, 90)
                Line((3.4, -1.5), (3.4, 1.5))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude6 (Cut)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1239269908, perimeter: 2.6570796327
            with BuildLine():
                CenterArc((0, 0.3), 0.05, 180, 180)
                Line((0.05, 0.3), (0.05, 1.5))
                Line((0.05, 1.5), (-0.05, 1.5))
                Line((-0.05, 0.3), (-0.05, 1.5))
            make_face()
        # OneSide extrude, distance=3.4
        extrude(amount=3.4, mode=Mode.SUBTRACT)
    return part.part


def model_87466_a6bedea0_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            Circle(2)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.3962634016, perimeter: 5.3962634016
            with BuildLine():
                Line((0, 0), (-1.9906682492, 0.1929764796))
                CenterArc((0, 0), 2, 174.4630167792, 40)
                Line((0, 0), (-1.6489832405, -1.1317483257))
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1745329252, perimeter: 1.8962634016
            with BuildLine():
                Line((-0.2488335311, 0.02412206), (0, 0))
                Line((0, 0), (-0.2061229051, -0.1414685407))
                CenterArc((0, 0), 0.25, -145.5369832208, 320)
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)
    return part.part


def model_88056_e0bff7c9_0000():
    """Model: Cylinder in Box Puzzle Assembled v3 v3"""
    with BuildPart() as part:
        # Sketch9 -> Extrude4 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 167.7416, perimeter: 53.34
            with BuildLine():
                Line((16.51, -15.16), (0, -15.16))
                Line((16.51, -5), (16.51, -15.16))
                Line((0, -5), (16.51, -5))
                Line((0, -15.16), (0, -5))
            make_face()
        # OneSide extrude, distance=3.81
        extrude(amount=3.81)
    return part.part


def model_88396_5f13c951_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 8.0424771932, perimeter: 10.0530964915
            Circle(1.6)
        # OneSide extrude, distance=-7.2
        extrude(amount=-7.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.4493933113, perimeter: 8.2557986795
            with BuildLine():
                CenterArc((0, 0), 1.6, -110.1055097879, 40.2110195758)
                Line((0.55, 1.5024979201), (0.55, -1.5024979201))
                CenterArc((0, 0), 1.6, 69.8944902121, 40.2110195758)
                Line((-0.55, -1.5024979201), (-0.55, 1.5024979201))
            make_face()
        # OneSide extrude, distance=2.5
        extrude(amount=2.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.55, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((-1.6838962679, 0)):
                Circle(0.4)
        # OneSide extrude, distance=-5
        extrude(amount=-5, mode=Mode.SUBTRACT)
    return part.part


def model_89253_e57586a5_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 20.2682991639, perimeter: 15.9592906802
            Circle(2.54)
        # OneSide extrude, distance=1.905
        extrude(amount=1.905)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1.905, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 11.4009182797, perimeter: 11.9694680102
            Circle(1.905)
        # OneSide extrude, distance=3.81
        extrude(amount=3.81, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 11.4009182797, perimeter: 11.9694680102
            Circle(1.905)
        # OneSide extrude, distance=3.81
        extrude(amount=3.81, mode=Mode.ADD)
    return part.part


def model_89681_0c77b7fc_0006():
    """Model: Cap Screw"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 2.5446900494, perimeter: 5.6548667765
            Circle(0.9)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1.2, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            Circle(0.6)
        # OneSide extrude, distance=7.5
        extrude(amount=7.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.8660254038, perimeter: 3.4641016151
            with BuildLine():
                Line((0.2886751346, 0.5), (-0.2886751346, 0.5))
                Line((-0.2886751346, 0.5), (-0.5773502692, 0))
                Line((-0.5773502692, 0), (-0.2886751346, -0.5))
                Line((-0.2886751346, -0.5), (0.2886751346, -0.5))
                Line((0.2886751346, -0.5), (0.5773502692, 0))
                Line((0.5773502692, 0), (0.2886751346, 0.5))
            make_face()
        # OneSide extrude, distance=-0.6
        extrude(amount=-0.6, mode=Mode.SUBTRACT)
    return part.part


def model_89681_0c77b7fc_0007():
    """Model: Head (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            Circle(2)
        # OneSide extrude, distance=8.5
        extrude(amount=8.5)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            Circle(0.6)
        # OneSide extrude, distance=-2.5
        extrude(amount=-2.5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 8.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            Circle(0.6)
        # OneSide extrude, distance=-2.5
        extrude(amount=-2.5, mode=Mode.SUBTRACT)
    return part.part


def model_90077_e7a99c92_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 50.2654824574, perimeter: 25.1327412287
            Circle(4)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.0868357663, perimeter: 48.6946861306
            with BuildLine():
                CenterArc((0, 0), 4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=10
        extrude(amount=10, mode=Mode.ADD)
    return part.part


def model_90104_558cd746_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 19 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 13.2042444083, perimeter: 44.686390968
            with BuildLine():
                CenterArc((-0.25, 2.25), 2.8504385627, 37.8749836511, 104.2500326978)
                Line((-2.5, 4), (-2.5, 0.5))
                Line((-2.5, 0.5), (2, 0.5))
                Line((2, 0.5), (2, 4))
            make_face()
            with BuildLine():
                Line((-2, 1), (-2, 4))
                Line((-2, 4), (-1.5, 4))
                Line((-1.5, 4), (-1.5, 1))
                Line((-1.5, 1), (-2, 1))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-1, 1), (-1, 4))
                Line((-1, 4), (-0.5, 4))
                Line((-0.5, 4), (-0.5, 1))
                Line((-0.5, 1), (-1, 1))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((0, 1), (0, 4))
                Line((0, 4), (0.5, 4))
                Line((0.5, 4), (0.5, 1))
                Line((0.5, 1), (0, 1))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((1, 1), (1, 4))
                Line((1, 4), (1.5, 4))
                Line((1.5, 4), (1.5, 1))
                Line((1.5, 1), (1, 1))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.2, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.6190621924, perimeter: 10.0260749437
            with BuildLine():
                Line((-2.5, 0), (2, 0))
                Line((2, 0), (2, 0.5))
                CenterArc((-0.25, 12.4516139208), 12.1615613847, -100.6616652184, 21.3233304368)
                Line((-2.5, 0.5), (-2.5, 0))
            make_face()
        # OneSide extrude, distance=4.5
        extrude(amount=4.5)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 20 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.4, perimeter: 2.6
            with BuildLine():
                Line((0.2, 2.5), (1, 2.5))
                Line((0.2, 2), (0.2, 2.5))
                Line((1, 2), (0.2, 2))
                Line((1, 2.5), (1, 2))
            make_face()
            # Profile area: 0.35, perimeter: 2.4
            with BuildLine():
                Line((4.7, 2), (4.7, 2.5))
                Line((4.7, 2.5), (4, 2.5))
                Line((4, 2.5), (4, 2))
                Line((4, 2), (4.7, 2))
            make_face()
            # Profile area: 0.4, perimeter: 2.6
            with BuildLine():
                Line((0.2, -1.5), (0.2, -2))
                Line((0.2, -2), (1, -2))
                Line((1, -2), (1, -1.5))
                Line((1, -1.5), (0.2, -1.5))
            make_face()
            # Profile area: 0.35, perimeter: 2.4
            with BuildLine():
                Line((4, -2), (4, -1.5))
                Line((4.7, -2), (4, -2))
                Line((4.7, -1.5), (4.7, -2))
                Line((4, -1.5), (4.7, -1.5))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.ADD)
    return part.part


def model_90114_99894f36_0000():
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
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 78.5398163397, perimeter: 31.4159265359
            Circle(5)
        # OneSide extrude, distance=10
        extrude(amount=10)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 11.1567726208, perimeter: 23.9343885759
            with BuildLine():
                Line((5, 9.5), (5, 8.5))
                _nurbs_edge([(5, 8.5), (5.1250904241, 8.5538491698), (5.3682255578, 8.6489637147), (5.7117911841, 8.7538833211), (6.1272966743, 8.8177299447), (6.5734435949, 8.7689503737), (6.9427947836, 8.5920274706), (7.2308201033, 8.2923440609), (7.4325813683, 7.884500884), (7.5431523361, 7.3898690089), (7.5582450356, 6.832206702), (7.4749106454, 6.2345800857), (7.2929667267, 5.6153937328), (7.0150736388, 4.9870745012), (6.6450677208, 4.3577318699), (6.1870796659, 3.7319805475), (5.753155476, 3.2359986657), (5.3908207807, 2.8668885659), (5.1329865598, 2.6220846253), (5, 2.5)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9333333333, 1, 1, 1, 1, 1, 1], 5)
                Line((5, 2.5), (5, 1))
                _nurbs_edge([(5, 9.5), (5.1143238954, 9.5660787119), (5.3416406027, 9.6804094239), (5.678620547, 9.7984286663), (6.1198952191, 9.848027636), (6.6550408298, 9.728688089), (7.1654157037, 9.43055367), (7.6341417485, 8.966444635), (8.0350774967, 8.361823744), (8.3378624606, 7.6483312883), (8.5121322307, 6.8595463857), (8.5317676246, 6.0267134777), (8.3810437099, 5.1738906459), (8.0545962634, 4.3171396155), (7.5529589172, 3.4667508359), (6.8801500513, 2.628423115), (6.2089522105, 1.9694564597), (5.6326304529, 1.4820827606), (5.216239554, 1.1601903674), (5, 1)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9333333333, 1, 1, 1, 1, 1, 1], 5)
            make_face()
        # Symmetric extrude, each_side=0.5
        extrude(amount=0.5, both=True)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 10, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 50.2654824574, perimeter: 25.1327412287
            Circle(4)
        # OneSide extrude, distance=-9.5
        extrude(amount=-9.5, mode=Mode.SUBTRACT)
    return part.part


def model_90205_97363b6d_0001():
    """Model: Eraser v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3578470382, perimeter: 2.1205750412
            Circle(0.3375)
        # OneSide extrude, distance=3.5
        extrude(amount=3.5)

        # Sketch4 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.188574099, perimeter: 1.5393804003
            Circle(0.245)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch5 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3.7, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0490088454, perimeter: 3.2672563597
            with BuildLine():
                CenterArc((0, 0), 0.275, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.245, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.188574099, perimeter: 1.5393804003
            Circle(0.245)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)
    return part.part


def model_90205_97363b6d_0010():
    """Model: Eraser Guide v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=4
        extrude(amount=4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4476769531, perimeter: 5.9690260418
            with BuildLine():
                CenterArc((0, 0), 0.55, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 4.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            Circle(0.35)
        # OneSide extrude, distance=-4.1
        extrude(amount=-4.1, mode=Mode.SUBTRACT)
    return part.part


def model_90615_6b438630_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> 拉伸1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 64, perimeter: 40
            with BuildLine():
                Line((-1, -5), (-5, -5))
                Line((-1, 1), (-1, -5))
                Line((-1, 1), (5, 1))
                Line((5, 5), (5, 1))
                Line((-5, 5), (5, 5))
                Line((-5, -5), (-5, 5))
            make_face()
        # OneSide extrude, distance=6
        extrude(amount=6)

        # Sketch2 -> 拉伸2 (Cut)
        # Sketch on XY construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane.XY) as sk:
            # Profile area: 16.5, perimeter: 17
            with BuildLine():
                Line((-1.5, 0), (-1.5, 5.5))
                Line((-1.5, 5.5), (-4.5, 5.5))
                Line((-4.5, 5.5), (-4.5, 0))
                Line((-1.5, 0), (-4.5, 0))
            make_face()
        # TwoSides extrude, along=5, against=-4.5
        extrude(amount=5, mode=Mode.SUBTRACT)
        extrude(sk.sketch, amount=-4.5, mode=Mode.SUBTRACT)

        # Sketch3 -> 拉伸3 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))) as sk:
            # Profile area: 16.5, perimeter: 17
            with BuildLine():
                Line((1.5, 5.5), (1.5, 0))
                Line((1.5, 0), (4.5, 0))
                Line((4.5, 0), (4.5, 5.5))
                Line((4.5, 5.5), (1.5, 5.5))
            make_face()
        # TwoSides extrude, along=5, against=-4.5
        extrude(amount=5, mode=Mode.SUBTRACT)
        extrude(sk.sketch, amount=-4.5, mode=Mode.SUBTRACT)
    return part.part


def model_90628_b8795213_0013():
    """Model: Coil (1) (1)"""
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
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.3), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.158732126, perimeter: 6.5860506843
            with BuildLine():
                CenterArc((0, 0), 0.5482025219, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.8), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.1868430659, perimeter: 7.214369215
            with BuildLine():
                CenterArc((0, 0), 0.6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5482025219, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.158732126, perimeter: 6.5860506843
            with BuildLine():
                CenterArc((0, 0), 0.5482025219, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


def model_90721_ee6f6982_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrusion1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4.8835382907, perimeter: 17.4784609691
            with BuildLine():
                Line((0, -0.6), (5.1392304845, -0.6))
                Line((5.1392304845, -0.6), (7.5980762114, -2.0196152423))
                Line((7.8980762114, -1.5), (7.5980762114, -2.0196152423))
                Line((5.3, 0), (7.8980762114, -1.5))
                Line((0, 0), (5.3, 0))
                Line((0, -0.6), (0, 0))
            make_face()
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)

        # Sketch2 -> Extrusion2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.8), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((5.5830127019, -0.5098076211)):
                Circle(0.15)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((7.3150635095, -1.5098076211)):
                Circle(0.15)
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrusion3 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -0.6, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((4.5320508076, 0.400000006)):
                Circle(0.15)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((3.9320508076, 0.400000006)):
                Circle(0.15)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((1.55, 0.4000000022)):
                Circle(0.15)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((0.65, 0.4000000008)):
                Circle(0.15)
        # OneSide extrude, distance=-0.6
        extrude(amount=-0.6, mode=Mode.SUBTRACT)
    return part.part


def model_91208_3ef96086_0000():
    """Model: heavy guy"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 380.1327110844, perimeter: 69.115038379
            Circle(11)
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 103.6725575685, perimeter: 69.115038379
            with BuildLine():
                CenterArc((0, 0), 7, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 103.6725575685, perimeter: 69.115038379
            with BuildLine():
                CenterArc((0, 0), 7, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)
    return part.part


def model_91299_4f533c5d_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 90, perimeter: 42
            with BuildLine():
                Line((3, -7.5), (3, 7.5))
                Line((3, 7.5), (-3, 7.5))
                Line((-3, 7.5), (-3, -7.5))
                Line((-3, -7.5), (3, -7.5))
            make_face()
        # Symmetric extrude, each_side=-4
        extrude(amount=-4, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(4, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 21.7653519932, perimeter: 21.7029348606
            Ellipse(5, 1.3856253431, rotation=90)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            Circle(2.5)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


def model_91391_c2de97c9_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 961, perimeter: 124
            with BuildLine():
                Line((0, 31), (0, 0))
                Line((0, 0), (31, 0))
                Line((31, 0), (31, 31))
                Line((31, 31), (0, 31))
            make_face()
        # OneSide extrude, distance=25
        extrude(amount=25)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 25), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 63, perimeter: 252
            with BuildLine():
                Line((-31.5, -31.5), (-31.5, 0.5))
                Line((0.5, -31.5), (-31.5, -31.5))
                Line((0.5, 0.5), (0.5, -31.5))
                Line((-31.5, 0.5), (0.5, 0.5))
            make_face()
            with BuildLine():
                Line((-31, 0), (-31, -31))
                Line((0, 0), (-31, 0))
                Line((0, -31), (0, 0))
                Line((-31, -31), (0, -31))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 961, perimeter: 124
            with BuildLine():
                Line((-31, -31), (0, -31))
                Line((0, -31), (0, 0))
                Line((0, 0), (-31, 0))
                Line((-31, 0), (-31, -31))
            make_face()
        # OneSide extrude, distance=22
        extrude(amount=22, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 47), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 4.4296456416, perimeter: 29.5309709437
            with BuildLine():
                CenterArc((-15.5, -15.5), 2.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-15.5, -15.5), 2.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=5
        extrude(amount=5, mode=Mode.ADD)
    return part.part


def model_91410_a5189a65_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch10 -> Extrude3 (NewBody)
        # Sketch on YZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.3219579864, perimeter: 2.0114281941
            with Locations((-2.2781699348, 0.8415579053)):
                Circle(0.3201287398)
            # Profile area: 0.339340104, perimeter: 2.0650117462
            with Locations((-4.3380058263, 0.8415579053)):
                Circle(0.3286568269)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3)
    return part.part


def model_91431_cc01fc10_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 13 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 58, perimeter: 29.6568542495
            with BuildLine():
                Line((4, -3), (-4, -3))
                Line((4, -3), (5, -2))
                Line((5, 2), (5, -2))
                Line((4, 3), (5, 2))
                Line((-4, 3), (4, 3))
                Line((-4, 3), (-5, 2))
                Line((-5, -2), (-5, 2))
                Line((-4, -3), (-5, -2))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4.3739696962, perimeter: 58.3195959493
            with BuildLine():
                Line((-5, -2), (-4, -3))
                Line((-4, -3), (4, -3))
                Line((4, -3), (5, -2))
                Line((5, -2), (5, 2))
                Line((5, 2), (4, 3))
                Line((4, 3), (-4, 3))
                Line((-4, 3), (-5, 2))
                Line((-5, 2), (-5, -2))
            make_face()
            with BuildLine():
                Line((3.9378679656, 2.85), (-3.9378679656, 2.85))
                Line((4.85, 1.9378679656), (3.9378679656, 2.85))
                Line((4.85, -1.9378679656), (4.85, 1.9378679656))
                Line((3.9378679656, -2.85), (4.85, -1.9378679656))
                Line((-3.9378679656, -2.85), (3.9378679656, -2.85))
                Line((-4.85, -1.9378679656), (-3.9378679656, -2.85))
                Line((-4.85, 1.9378679656), (-4.85, -1.9378679656))
                Line((-3.9378679656, 2.85), (-4.85, 1.9378679656))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.9927409851, perimeter: 10.3907206209
            with BuildLine():
                Line((0.4883500303, 1.2117992209), (1.5116499697, 1.2117992209))
                Line((0.4883500303, -1.2117992209), (0.4883500303, 1.2117992209))
                Line((1.5116499697, -1.2117992209), (0.4883500303, -1.2117992209))
                Line((1.5116499697, 1.2117992209), (1.5116499697, -1.2117992209))
            make_face()
            with BuildLine():
                CenterArc((1, 0.7058843989), 0.2893575802, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1, -0.7228186534), 0.2671951375, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)
    return part.part


def model_91433_d1a5d966_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 36.572066703, perimeter: 32.4586958407
            with BuildLine():
                Line((0, 13.5253917293), (0, 0))
                Line((0, 0), (2.7039561911, 0))
                Line((2.7039561911, 0), (2.7039561911, 13.5253917293))
                Line((2.7039561911, 13.5253917293), (0, 13.5253917293))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 7.7853981634, perimeter: 17.1415926536
            with BuildLine():
                CenterArc((1.5, 5), 0.5, -180, 180)
                Line((2, 5), (2, 12))
                CenterArc((1.5, 12), 0.5, 0, 180)
                Line((1, 12), (1, 5))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude3 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.3835007986, perimeter: 2.1952706363
            with Locations((1.5, 3.1534546731)):
                Circle(0.3493881732)
            # Profile area: 0.3835007986, perimeter: 2.1952706363
            with Locations((1.5, 1.6288517356)):
                Circle(0.3493881732)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


def model_91434_7c784ac3_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.1078965197, perimeter: 16.1922179827
            with BuildLine():
                CenterArc((2.25, -2.9940322929), 1.2500142453, -179.726462533, 179.4529250659)
                CenterArc((7, -1), 4.0311288741, 150.2551187031, 59.4897625939)
                CenterArc((2.25, 1), 1.25, 0, 180)
                CenterArc((-2.75, -1), 4.25, -28.0724869359, 56.1449738717)
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0019634954, perimeter: 0.1570796327
            with Locations((-2.25, -1)):
                Circle(0.025)
            # Profile area: 0.0019634954, perimeter: 0.1570796327
            with Locations((-2.2000000328, -1.0500000156)):
                Circle(0.025)
            # Profile area: 0.0019634954, perimeter: 0.1570796327
            with Locations((-2.1498138591, -1.1001861603)):
                Circle(0.025)
            # Profile area: 0.0019634954, perimeter: 0.1570796327
            with Locations((-2.0989503672, -1.151049662)):
                Circle(0.025)
            # Profile area: 0.0019634954, perimeter: 0.1570796327
            with Locations((-2.0496599722, -1.2003400666)):
                Circle(0.025)
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 16 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0800000024, perimeter: 1.2000000179
            with BuildLine():
                Line((-2.8000000417, 2.5000000373), (-2.4000000358, 2.5000000373))
                Line((-2.8000000417, 2.3000000343), (-2.8000000417, 2.5000000373))
                Line((-2.4000000358, 2.3000000343), (-2.8000000417, 2.3000000343))
                Line((-2.4000000358, 2.5000000373), (-2.4000000358, 2.3000000343))
            make_face()
            # Profile area: 0.0800000024, perimeter: 1.2000000179
            with BuildLine():
                Line((-2.2000000328, 2.5000000373), (-1.8000000268, 2.5000000373))
                Line((-2.2000000328, 2.3000000343), (-2.2000000328, 2.5000000373))
                Line((-1.8000000268, 2.3000000343), (-2.2000000328, 2.3000000343))
                Line((-1.8000000268, 2.5000000373), (-1.8000000268, 2.3000000343))
            make_face()
            # Profile area: 0.0800000024, perimeter: 1.2000000179
            with BuildLine():
                Line((-2.2000000328, 2.9000000432), (-1.8000000268, 2.9000000432))
                Line((-2.2000000328, 2.7000000402), (-2.2000000328, 2.9000000432))
                Line((-1.8000000268, 2.7000000402), (-2.2000000328, 2.7000000402))
                Line((-1.8000000268, 2.9000000432), (-1.8000000268, 2.7000000402))
            make_face()
            # Profile area: 0.0800000024, perimeter: 1.2000000179
            with BuildLine():
                Line((-2.8000000417, 2.9000000432), (-2.4000000358, 2.9000000432))
                Line((-2.8000000417, 2.7000000402), (-2.8000000417, 2.9000000432))
                Line((-2.4000000358, 2.7000000402), (-2.8000000417, 2.7000000402))
                Line((-2.4000000358, 2.9000000432), (-2.4000000358, 2.7000000402))
            make_face()
        # OneSide extrude, distance=0.05
        extrude(amount=0.05, mode=Mode.ADD)
    return part.part


def model_91457_9b6cdf83_0001():
    """Model: spigot"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.5446900494, perimeter: 5.6548667765
            Circle(0.9)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.4), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.5393804003, perimeter: 4.398229715
            Circle(0.7)
        # OneSide extrude, distance=3.2
        extrude(amount=3.2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


def model_91673_a331a9ee_0000():
    """Model: Bracket"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 336 constraints, 88 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 24.1646785886, perimeter: 83.003978921
            with BuildLine():
                Line((0, -4.4), (0, 0))
                Line((0, 0), (-7.9, 0))
                Line((-7.9, 0), (-7.9, -4.4))
                Line((-7.9, -4.4), (0, -4.4))
            make_face()
            with BuildLine():
                Line((-6.4, -2.375), (-6.575, -2.375))
                Line((-6.575, -2.025), (-6.575, -2.375))
                Line((-6.4, -2.025), (-6.575, -2.025))
                Line((-6.4, -2.025), (-6.05, -2.025))
                Line((-6.05, -2.025), (-5.875, -2.025))
                Line((-5.875, -2.025), (-5.875, -2.375))
                Line((-6.05, -2.375), (-5.875, -2.375))
                Line((-6.05, -2.375), (-6.4, -2.375))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-1.1, -2.375), (-1.275, -2.375))
                Line((-1.275, -2.375), (-1.275, -2.025))
                Line((-1.1, -2.025), (-1.275, -2.025))
                Line((-1.1, -2.025), (-0.75, -2.025))
                Line((-0.75, -2.025), (-0.575, -2.025))
                Line((-0.575, -2.375), (-0.575, -2.025))
                Line((-0.75, -2.375), (-0.575, -2.375))
                Line((-0.75, -2.375), (-1.1, -2.375))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-7.315, -2.2), 0.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-7.3887734957, -3.835), 0.265, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-6.855, -0.6), 0.265, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-3.21, -0.6), 0.265, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-3.7140570083, -3.835), 0.265, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-2.45, -1.3), (-2.45, -1.7))
                CenterArc((-2.15, -1.3), 0.3, 0, 180)
                Line((-1.85, -1.3), (-1.85, -1.7))
                CenterArc((-2.15, -1.7), 0.3, 180, 180)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-5.95, -0.6), 0.3, 90, 180)
                Line((-5.95, -0.3), (-5.55, -0.3))
                CenterArc((-5.55, -0.6), 0.3, -90, 180)
                Line((-5.55, -0.9), (-5.95, -0.9))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-4.65, -0.3), (-4.25, -0.3))
                CenterArc((-4.25, -0.6), 0.3, -90, 180)
                Line((-4.25, -0.9), (-4.65, -0.9))
                CenterArc((-4.65, -0.6), 0.3, 90, 180)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-6.35, -1.2), (-5.95, -1.2))
                CenterArc((-5.95, -1.5), 0.3, -90, 180)
                Line((-5.95, -1.8), (-6.35, -1.8))
                CenterArc((-6.35, -1.5), 0.3, 90, 180)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-6.325, -3.5), (-5.925, -3.5))
                CenterArc((-5.925, -3.8), 0.3, -90, 180)
                Line((-5.925, -4.1), (-6.325, -4.1))
                CenterArc((-6.325, -3.8), 0.3, 180, 90)
                CenterArc((-6.325, -3.8), 0.3, 90, 90)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-6.325, -2.6), (-5.925, -2.6))
                CenterArc((-5.925, -2.9), 0.3, -90, 180)
                Line((-5.925, -3.2), (-6.325, -3.2))
                CenterArc((-6.325, -2.9), 0.3, 90, 180)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-4.625, -4.1), (-5.025, -4.1))
                CenterArc((-5.025, -3.8), 0.3, 90, 180)
                Line((-5.025, -3.5), (-4.625, -3.5))
                CenterArc((-4.625, -3.8), 0.3, -90, 180)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-3.75, -1.2), (-3.35, -1.2))
                CenterArc((-3.35, -1.5), 0.3, -90, 180)
                Line((-3.35, -1.8), (-3.75, -1.8))
                CenterArc((-3.75, -1.5), 0.3, 90, 180)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-4.65, -1.8), (-5.05, -1.8))
                CenterArc((-5.05, -1.5), 0.3, 90, 180)
                Line((-5.05, -1.2), (-4.65, -1.2))
                CenterArc((-4.65, -1.5), 0.3, -90, 180)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-5.05, -2.65), 0.3, 90, 180)
                Line((-5.05, -2.35), (-4.65, -2.35))
                CenterArc((-4.65, -2.65), 0.3, -90, 180)
                Line((-4.65, -2.95), (-5.05, -2.95))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-3.35, -2.95), (-3.75, -2.95))
                CenterArc((-3.75, -2.65), 0.3, 90, 180)
                Line((-3.75, -2.35), (-3.35, -2.35))
                CenterArc((-3.35, -2.65), 0.3, -90, 180)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-2.4, -2.35), (-2, -2.35))
                CenterArc((-2, -2.65), 0.3, -90, 180)
                Line((-2, -2.95), (-2.4, -2.95))
                CenterArc((-2.4, -2.65), 0.3, 90, 180)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-2.5, -3.5), (-2.1, -3.5))
                CenterArc((-2.1, -3.8), 0.3, -90, 180)
                Line((-2.1, -4.1), (-2.5, -4.1))
                CenterArc((-2.5, -3.8), 0.3, 90, 180)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-1.1, -2.6), (-0.7, -2.6))
                CenterArc((-0.7, -2.9), 0.3, -90, 180)
                Line((-0.7, -3.2), (-1.1, -3.2))
                CenterArc((-1.1, -2.9), 0.3, 90, 180)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-1.1, -3.5), (-0.7, -3.5))
                CenterArc((-0.7, -3.8), 0.3, -90, 180)
                Line((-0.7, -4.1), (-1.1, -4.1))
                CenterArc((-1.1, -3.8), 0.3, 90, 180)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-1.1, -1.2), (-0.7, -1.2))
                CenterArc((-0.7, -1.5), 0.3, -90, 180)
                Line((-0.7, -1.8), (-1.1, -1.8))
                CenterArc((-1.1, -1.5), 0.3, 90, 180)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.5, -0.6), 0.3, 90, 180)
                Line((-0.7, -0.3), (-1.5, -0.3))
                CenterArc((-0.7, -0.6), 0.3, -90, 180)
                Line((-0.7, -0.9), (-1.5, -0.9))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.06125, perimeter: 1.05
            with BuildLine():
                Line((-1.1, -2.375), (-1.1, -2.025))
                Line((-1.1, -2.025), (-1.275, -2.025))
                Line((-1.275, -2.375), (-1.275, -2.025))
                Line((-1.1, -2.375), (-1.275, -2.375))
            make_face()
            # Profile area: 0.06125, perimeter: 1.05
            with BuildLine():
                Line((-6.05, -2.375), (-5.875, -2.375))
                Line((-5.875, -2.025), (-5.875, -2.375))
                Line((-6.05, -2.025), (-5.875, -2.025))
                Line((-6.05, -2.025), (-6.05, -2.375))
            make_face()
            # Profile area: 0.06125, perimeter: 1.05
            with BuildLine():
                Line((-0.75, -2.375), (-0.575, -2.375))
                Line((-0.575, -2.375), (-0.575, -2.025))
                Line((-0.75, -2.025), (-0.575, -2.025))
                Line((-0.75, -2.025), (-0.75, -2.375))
            make_face()
            # Profile area: 0.06125, perimeter: 1.05
            with BuildLine():
                Line((-6.4, -2.375), (-6.4, -2.025))
                Line((-6.4, -2.025), (-6.575, -2.025))
                Line((-6.575, -2.025), (-6.575, -2.375))
                Line((-6.4, -2.375), (-6.575, -2.375))
            make_face()
        # OneSide extrude, distance=0.17
        extrude(amount=0.17)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 336 constraints, 88 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.54, perimeter: 9.5
            with BuildLine():
                Line((-7.9, 0), (-7.9, -4.4))
                Line((-7.9, 0), (-8.25, 0))
                Line((-8.25, 0), (-8.25, -4.4))
                Line((-8.25, -4.4), (-7.9, -4.4))
            make_face()
        # OneSide extrude, distance=1.86
        extrude(amount=1.86, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 336 constraints, 88 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1225, perimeter: 1.4
            with BuildLine():
                Line((-0.75, -2.375), (-1.1, -2.375))
                Line((-0.75, -2.025), (-0.75, -2.375))
                Line((-1.1, -2.025), (-0.75, -2.025))
                Line((-1.1, -2.375), (-1.1, -2.025))
            make_face()
            # Profile area: 0.06125, perimeter: 1.05
            with BuildLine():
                Line((-1.1, -2.375), (-1.1, -2.025))
                Line((-1.1, -2.025), (-1.275, -2.025))
                Line((-1.275, -2.375), (-1.275, -2.025))
                Line((-1.1, -2.375), (-1.275, -2.375))
            make_face()
            # Profile area: 0.06125, perimeter: 1.05
            with BuildLine():
                Line((-0.75, -2.375), (-0.575, -2.375))
                Line((-0.575, -2.375), (-0.575, -2.025))
                Line((-0.75, -2.025), (-0.575, -2.025))
                Line((-0.75, -2.025), (-0.75, -2.375))
            make_face()
            # Profile area: 0.1225, perimeter: 1.4
            with BuildLine():
                Line((-6.05, -2.375), (-6.4, -2.375))
                Line((-6.05, -2.025), (-6.05, -2.375))
                Line((-6.4, -2.025), (-6.05, -2.025))
                Line((-6.4, -2.375), (-6.4, -2.025))
            make_face()
            # Profile area: 0.06125, perimeter: 1.05
            with BuildLine():
                Line((-6.05, -2.375), (-5.875, -2.375))
                Line((-5.875, -2.025), (-5.875, -2.375))
                Line((-6.05, -2.025), (-5.875, -2.025))
                Line((-6.05, -2.025), (-6.05, -2.375))
            make_face()
            # Profile area: 0.06125, perimeter: 1.05
            with BuildLine():
                Line((-6.4, -2.375), (-6.4, -2.025))
                Line((-6.4, -2.025), (-6.575, -2.025))
                Line((-6.575, -2.025), (-6.575, -2.375))
                Line((-6.4, -2.375), (-6.575, -2.375))
            make_face()
        # OneSide extrude, distance=-0.13
        extrude(amount=-0.13)

        # Sketch3 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 50 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-8.25, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.096211275, perimeter: 1.0995574288
            with Locations((2.2, 0.975)):
                Circle(0.175)
            # Profile area: 0.0619496416, perimeter: 1.0092824047
            with BuildLine():
                CenterArc((0.6, 1.13), 0.3, -138.1896851042, 96.3793702084)
                CenterArc((0.6, 0.73), 0.3, 41.8103148958, 96.3793702084)
            make_face()
            # Profile area: 0.0096031514, perimeter: 0.8378369119
            with BuildLine():
                CenterArc((0.6, 1.13), 0.3, -41.8103148958, 41.8103148958)
                CenterArc((0.6, 0.73), 0.3, -0.0000303825, 41.8103452782)
                Line((0.9, 0.7299998409), (0.9, 1.13))
            make_face()
            # Profile area: 0.2207936972, perimeter: 1.8849555922
            with BuildLine():
                CenterArc((0.6, 0.73), 0.3, 180, 179.9999696175)
                CenterArc((0.6, 0.73), 0.3, -0.0000303825, 41.8103452782)
                CenterArc((0.6, 1.13), 0.3, -138.1896851042, 96.3793702084)
                CenterArc((0.6, 0.73), 0.3, 138.1896851042, 41.8103148958)
            make_face()
            # Profile area: 0.0096031514, perimeter: 0.8378362313
            with BuildLine():
                Line((0.3, 0.7300003624), (0.3, 1.13))
                CenterArc((0.6, 0.73), 0.3, 138.1896851042, 41.8103148958)
                CenterArc((0.6, 1.13), 0.3, 180, 41.8103148958)
            make_face()
            # Profile area: 0.2207936972, perimeter: 1.8849555922
            with BuildLine():
                CenterArc((0.6, 1.13), 0.3, 180, 41.8103148958)
                CenterArc((0.6, 0.73), 0.3, 41.8103148958, 96.3793702084)
                CenterArc((0.6, 1.13), 0.3, -41.8103148958, 41.8103148958)
                CenterArc((0.6, 1.13), 0.3, 0, 180)
            make_face()
            # Profile area: 0.0096031514, perimeter: 0.8378369119
            with BuildLine():
                Line((4.1, 0.7299998409), (4.1, 1.13))
                CenterArc((3.8, 1.13), 0.3, -41.8103148958, 41.8103148958)
                CenterArc((3.8, 0.73), 0.3, -0.0000303825, 41.8103452782)
            make_face()
            # Profile area: 0.0619496416, perimeter: 1.0092824047
            with BuildLine():
                CenterArc((3.8, 1.13), 0.3, -138.1896851042, 96.3793702084)
                CenterArc((3.8, 0.73), 0.3, 41.8103148958, 96.3793702084)
            make_face()
            # Profile area: 0.2207936972, perimeter: 1.8849555922
            with BuildLine():
                CenterArc((3.8, 0.73), 0.3, 138.1896851042, 41.8103148958)
                CenterArc((3.8, 0.73), 0.3, 180, 179.9999696175)
                CenterArc((3.8, 0.73), 0.3, -0.0000303825, 41.8103452782)
                CenterArc((3.8, 1.13), 0.3, -138.1896851042, 96.3793702084)
            make_face()
            # Profile area: 0.2207936972, perimeter: 1.8849555922
            with BuildLine():
                CenterArc((3.8, 0.73), 0.3, 41.8103148958, 96.3793702084)
                CenterArc((3.8, 1.13), 0.3, -41.8103148958, 41.8103148958)
                CenterArc((3.8, 1.13), 0.3, 0, 180)
                CenterArc((3.8, 1.13), 0.3, 180, 41.8103148958)
            make_face()
            # Profile area: 0.0096031514, perimeter: 0.8378362313
            with BuildLine():
                CenterArc((3.8, 1.13), 0.3, 180, 41.8103148958)
                Line((3.5, 0.7300003624), (3.5, 1.13))
                CenterArc((3.8, 0.73), 0.3, 138.1896851042, 41.8103148958)
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


def model_92286_2ab17805_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.0106192983, perimeter: 5.0265482457
            Circle(0.8)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.3), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1, perimeter: 4
            with BuildLine():
                Line((0.5, -0.5), (0.5, 0.5))
                Line((0.5, 0.5), (-0.5, 0.5))
                Line((-0.5, 0.5), (-0.5, -0.5))
                Line((-0.5, -0.5), (0.5, -0.5))
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.8602498879, perimeter: 4.0151998508
            with BuildLine():
                Line((0.5291502622, -0.6), (-0.5291502622, -0.6))
                CenterArc((0, 0), 0.8, -48.5903778907, 48.5903778907)
                Line((-0.8, 0), (0.8, 0))
                CenterArc((0, 0), 0.8, -180, 48.5903778907)
            make_face()
            # Profile area: 0.0498750561, perimeter: 1.549299401
            with BuildLine():
                Line((0.8, -0.6), (0.5291502622, -0.6))
                Line((0.8, 0), (0.8, -0.6))
                CenterArc((0, 0), 0.8, -48.5903778907, 48.5903778907)
            make_face()
            # Profile area: 0.0498750561, perimeter: 1.549299401
            with BuildLine():
                CenterArc((0, 0), 0.8, -180, 48.5903778907)
                Line((-0.8, -0.6), (-0.8, 0))
                Line((-0.5291502622, -0.6), (-0.8, -0.6))
            make_face()
        # OneSide extrude, distance=1.1
        extrude(amount=1.1, mode=Mode.ADD)
    return part.part


def model_92355_a1f4144c_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 17 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.3171017275, perimeter: 28.4699113898
            with BuildLine():
                CenterArc((0, 0.3), 0.3, -90, 180)
                Line((0, 0.6), (-0.75, 0.6))
                CenterArc((-0.75, 0), 0.6, 90, 90)
                Line((-1.35, 0), (-1.35, -1.15))
                CenterArc((-0.75, -1.15), 0.6, 180, 90)
                Line((-0.75, -1.75), (2.45, -1.75))
                CenterArc((2.45, -1.15), 0.6, -90, 90)
                Line((3.05, -1.15), (3.05, 3.2000000477))
                Line((3.05, 3.2000000477), (5.0000000671, 3.2000000477))
                Line((5.0000000671, 3.2000000477), (5.0000000671, 3.8500000714))
                Line((5.0000000671, 3.8500000714), (2.45, 3.85))
                Line((2.45, -1.15), (2.45, 3.85))
                Line((-0.75, -1.15), (2.45, -1.15))
                Line((-0.75, 0), (-0.75, -1.15))
                Line((0, 0), (-0.75, 0))
            make_face()
        # OneSide extrude, distance=0.95
        extrude(amount=0.95)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -3.2000000477), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.7088218425, perimeter: 2.9845130209
            with BuildLine():
                CenterArc((-4.0000000335, -0.475), 0.475, 89.9999994601, 179.9999999135)
                CenterArc((-4.0000000335, -0.475), 0.475, -90.0000006263, 180.0000000865)
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


def model_92553_3ba197ab_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.1694480478, perimeter: 8.4568356156
            with BuildLine():
                CenterArc((-0.1, -1), 1.4, 0, 180)
                Line((-1.2025, -1), (-1.5, -1))
                CenterArc((-0.1, -1), 1.1025, 0, 180)
                Line((1.3, -1), (1.0025, -1))
            make_face()
            # Profile area: 1.1694480478, perimeter: 8.4568356156
            with BuildLine():
                Line((1.0025, 2), (1.3, 2))
                CenterArc((-0.1, 2), 1.4, 0, 180)
                Line((-1.5, 2), (-1.2025, 2))
                CenterArc((-0.1, 2), 1.1025, 0, 180)
            make_face()
            # Profile area: 2.242478399, perimeter: 14.7964594301
            with BuildLine():
                CenterArc((-0.1, 2), 1.4, -180, 180)
                Line((-1.5, -1), (-1.5, 2))
                CenterArc((-0.1, -1), 1.4, 0, 180)
                Line((1.3, 2), (1.3, -1))
            make_face()
            # Profile area: 1.1694480478, perimeter: 8.4568356156
            with BuildLine():
                CenterArc((-0.1, 2), 1.1025, -180, 180)
                Line((-1.5, 2), (-1.2025, 2))
                CenterArc((-0.1, 2), 1.4, -180, 180)
                Line((1.0025, 2), (1.3, 2))
            make_face()
            # Profile area: 1.1694480478, perimeter: 8.4568356156
            with BuildLine():
                Line((1.3, -1), (1.0025, -1))
                CenterArc((-0.1, -1), 1.1025, -180, 180)
                Line((-1.2025, -1), (-1.5, -1))
                CenterArc((-0.1, -1), 1.4, -180, 180)
            make_face()
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.8509953331, perimeter: 10.3672557568
            with BuildLine():
                CenterArc((7.5, 1.5), 1.1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((7.5, 1.5), 0.55, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.25
        extrude(amount=0.25)

        # Sketch2 -> Extrude3 (Join)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.4286506826, perimeter: 6.0161499316
            with BuildLine():
                CenterArc((7.5, 1.5), 0.55, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((7.5, 1.5), 0.4075, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch2 -> Extrude4 (Join)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.5216810951, perimeter: 2.5603980127
            with Locations((7.5, 1.5)):
                Circle(0.4075)
        # OneSide extrude, distance=0.55
        extrude(amount=0.55, mode=Mode.ADD)
    return part.part


def model_92738_0c72fe82_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 21.5454, perimeter: 20.42
            with BuildLine():
                Line((3.615, -1.49), (3.615, 1.49))
                Line((3.615, 1.49), (-3.615, 1.49))
                Line((-3.615, 1.49), (-3.615, -1.49))
                Line((-3.615, -1.49), (3.615, -1.49))
            make_face()
        # OneSide extrude, distance=0.79
        extrude(amount=0.79)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.79, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.31, perimeter: 7.54
            with BuildLine():
                Line((-1.5, 0.385), (-1.5, -0.385))
                Line((-1.5, -0.385), (1.5, -0.385))
                Line((1.5, -0.385), (1.5, 0.385))
                Line((1.5, 0.385), (-1.5, 0.385))
            make_face()
        # OneSide extrude, distance=6.4
        extrude(amount=6.4, mode=Mode.ADD)
    return part.part


def model_93181_b95f586d_0000():
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
        # Sketch4 -> Extrude3 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 13.8544236023, perimeter: 13.1946891451
            with Locations((20.0381021005, -0.1176447947)):
                Circle(2.1)
        # OneSide extrude, distance=6
        extrude(amount=6)

        # Sketch5 -> Extrude4 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 13.8544236023, perimeter: 13.1946891451
            with Locations((15.0535032457, -6.888402052)):
                Circle(2.1)
        # OneSide extrude, distance=-3
        extrude(amount=-3)
    return part.part


def model_94163_9b899ce2_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0118492105, perimeter: 2.3801381368
            with BuildLine():
                Line((-0.0099999956, -0.1399490512), (-0.0100082975, -0.359949051))
                Line((-0.0100082975, -0.359949051), (0.2599916955, -0.3600101886))
                Line((0.2599916955, -0.3600101886), (0.2599924505, -0.3400101886))
                Line((0.2599924505, -0.3400101886), (0.304419285, -0.3400118656))
                Line((0.304419285, -0.3400118656), (0.4038124564, -0.2291374757))
                Line((0.4038124564, -0.2291374757), (0.3040497926, -0.1400798362))
                Line((-0.0099999956, -0.1399490512), (0.3040497926, -0.1400798362))
            make_face()
            with BuildLine():
                Line((0.3000075495, -0.1500048858), (0.3000062458, -0.2300048858))
                Line((0.3000075495, -0.1500048858), (0.3899554736, -0.2300086832))
                Line((0.3, -0.3299999966), (0.3899554736, -0.2300086832))
                Line((0.2499999944, -0.3299999966), (0.3, -0.3299999966))
                Line((0.2499999998, -0.3500094336), (0.2499999944, -0.3299999966))
                Line((0, -0.3499999966), (0.2499999998, -0.3500094336))
                Line((0.0000075495, -0.1499999968), (0, -0.3499999966))
                Line((0.0000075495, -0.1499999968), (0.2900011342, -0.1500047227))
                Line((0.2899999935, -0.2199999951), (0.2900011342, -0.1500047227))
                Line((0.3000062458, -0.2300048858), (0.2899999935, -0.2199999951))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.27
        extrude(amount=0.27)

        # Sketch14 -> Extrude5 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0020021249, perimeter: 0.2402136137
            with BuildLine():
                Line((0.4302124776, -0.5000000075), (0.4302124776, -0.4800000075))
                Line((0.4302124776, -0.4800000075), (0.3302124776, -0.4800000075))
                Line((0.3299999926, -0.5000000075), (0.3302124776, -0.4800000075))
                Line((0.4302124776, -0.5000000075), (0.3299999926, -0.5000000075))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


def model_98408_4a172cb9_0000():
    """Model: vleugel heli"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.8693293485, perimeter: 21.8384626574
            with BuildLine():
                Line((0, 0), (9.6818821779, 0))
                Line((9.6818821779, 0), (10.374029685, 0.6895347167))
                Line((1.7221858468, 1.7592172277), (10.374029685, 0.6895347167))
                Line((0, 0), (1.7221858468, 1.7592172277))
            make_face()
        # OneSide extrude, distance=0.075
        extrude(amount=0.075)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.075, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7194523689, perimeter: 4.0958255526
            with BuildLine():
                Line((-0.8302567826, -0.8481094175), (-1.6966027121, 0))
                Line((0, 0), (-0.8302567826, -0.8481094175))
                Line((-1.6966027121, 0), (0, 0))
            make_face()
        # OneSide extrude, distance=0.025
        extrude(amount=0.025, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0794446585, perimeter: 0.9991651625
            with Locations((-0.7055412149, -0.3004611395)):
                Circle(0.1590220746)
        # OneSide extrude, distance=-0.8788
        extrude(amount=-0.8788, mode=Mode.SUBTRACT)
    return part.part


def model_98416_af704f6f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 120, perimeter: 46
            with BuildLine():
                Line((7.5, -4), (7.5, 4))
                Line((7.5, 4), (-7.5, 4))
                Line((-7.5, 4), (-7.5, -4))
                Line((-7.5, -4), (7.5, -4))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 33 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.5), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 80.8334882862, perimeter: 36.5454286204
            with BuildLine():
                CenterArc((5.3040841439, 2.8), 0.4, 8.1946115538, 81.8053884462)
                Line((5.3040841439, 3.2), (-5.3040841439, 3.2))
                CenterArc((-5.3040841439, 2.8), 0.4, 90, 81.8053884462)
                CenterArc((-6.4918317122, 2.9710430181), 0.8, -74.537203167, 66.3425916132)
                CenterArc((-6.1718965713, 1.8144784909), 0.4, 105.462796833, 74.537203167)
                Line((-6.5718965713, 1.8144784909), (-6.5718965713, -1.8144784909))
                CenterArc((-6.1718965713, -1.8144784909), 0.4, -180, 74.537203167)
                CenterArc((-6.4918317122, -2.9710430181), 0.8, 8.1946115538, 66.3425916132)
                CenterArc((-5.3040841439, -2.8), 0.4, -171.8053884462, 81.8053884462)
                Line((-5.3040841439, -3.2), (5.3040841439, -3.2))
                CenterArc((5.3040841439, -2.8), 0.4, -90, 81.8053884462)
                CenterArc((6.4918317122, -2.9710430181), 0.8, 105.462796833, 66.3425916132)
                CenterArc((6.1718965713, -1.8144784909), 0.4, -74.537203167, 74.537203167)
                Line((6.5718965713, -1.8144784909), (6.5718965713, 1.8144784909))
                CenterArc((6.1718965713, 1.8144784909), 0.4, 0, 74.537203167)
                CenterArc((6.4918317122, 2.9710430181), 0.8, -171.8053884462, 66.3425916132)
            make_face()
        # OneSide extrude, distance=-0.7
        extrude(amount=-0.7, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 14 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.5), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((6.5, 3)):
                Circle(0.4)
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((6.5, -3)):
                Circle(0.4)
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((-6.5, 3)):
                Circle(0.4)
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((-6.5, -3)):
                Circle(0.4)
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.SUBTRACT)
    return part.part


def model_98883_3f3088e4_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 16 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 161.29, perimeter: 61.3210244843
            with BuildLine():
                Line((-12.7, 8.89), (0, -3.81))
                Line((0, -3.81), (12.7, 8.89))
                Line((12.7, 8.89), (-12.7, 8.89))
            make_face()
            # Profile area: 470.9668, perimeter: 117.2010244843
            with BuildLine():
                Line((-12.7, 8.89), (-17.78, 8.89))
                Line((-17.78, 8.89), (-17.78, -8.89))
                Line((-17.78, -8.89), (17.78, -8.89))
                Line((17.78, -8.89), (17.78, 8.89))
                Line((17.78, 8.89), (12.7, 8.89))
                Line((0, -3.81), (12.7, 8.89))
                Line((-12.7, 8.89), (0, -3.81))
            make_face()
        # OneSide extrude, distance=-12.7
        extrude(amount=-12.7)

        # Sketch4 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -12.7), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 361.2896, perimeter: 91.44
            with BuildLine():
                Line((-17.78, 1.27), (-17.78, -8.89))
                Line((17.78, -8.89), (-17.78, -8.89))
                Line((17.78, -8.89), (17.78, 1.27))
                Line((-17.78, 1.27), (17.78, 1.27))
            make_face()
        # OneSide extrude, distance=5.08
        extrude(amount=5.08, mode=Mode.ADD)
    return part.part


def model_99079_80299be5_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch6 -> Extrude6 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 48.387, perimeter: 33.02
            with BuildLine():
                Line((-6.35, 1.905), (6.35, 1.905))
                Line((-6.35, -1.905), (-6.35, 1.905))
                Line((6.35, -1.905), (-6.35, -1.905))
                Line((6.35, 1.905), (6.35, -1.905))
            make_face()
        # Symmetric extrude, each_side=3.81
        extrude(amount=3.81, both=True)

        # Sketch7 -> Extrude7 (Cut)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 11.741912, perimeter: 19.3548
            with BuildLine():
                Line((-4.1275, -1.905), (0, -1.905))
                Line((0, -1.905), (4.1275, -1.905))
                Line((4.1275, -1.905), (4.1275, -0.4826))
                Line((4.1275, -0.4826), (-4.1275, -0.4826))
                Line((-4.1275, -0.4826), (-4.1275, -1.905))
            make_face()
        # Symmetric extrude, each_side=3.81
        extrude(amount=3.81, both=True, mode=Mode.SUBTRACT)

        # Sketch8 -> Extrude8 (Join)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 14.7741644715, perimeter: 16.7132001621
            with BuildLine():
                Line((-1.2700000405, 1.905), (0, 1.905))
                Line((0, 1.905), (1.2700000405, 1.905))
                Line((1.2700000405, 1.905), (1.2700000405, 7.7216))
                Line((1.2700000405, 7.7216), (-1.2700000405, 7.7216))
                Line((-1.2700000405, 7.7216), (-1.2700000405, 1.905))
            make_face()
        # Symmetric extrude, each_side=3.81
        extrude(amount=3.81, both=True, mode=Mode.ADD)
    return part.part


def model_99732_6f03d7fc_0001():
    """Model: 001.001.002.001"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 28.2743338823, perimeter: 56.5486677646
            with BuildLine():
                CenterArc((0, 0), 5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=40
        extrude(amount=20, both=True)

        # Sketch4 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 20), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 34.5575191895, perimeter: 69.115038379
            with BuildLine():
                CenterArc((0, 0), 6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-4
        extrude(amount=-4, mode=Mode.ADD)

        # Sketch5 -> Extrude4 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, -20), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 34.5575191895, perimeter: 69.115038379
            with BuildLine():
                CenterArc((0, 0), 6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-4
        extrude(amount=-4, mode=Mode.ADD)
    return part.part


MODELS = {
    "model_83100_215c1f32_0000": {"func": model_83100_215c1f32_0000, "volume": 100.7380759114, "area": 255.8192454121},
    "model_83113_d57d4ccf_0000": {"func": model_83113_d57d4ccf_0000, "volume": 219.4537497127, "area": 424.5145682564},
    "model_83210_07c13a64_0000": {"func": model_83210_07c13a64_0000, "volume": 38.3243789221, "area": 263.42291737},
    "model_83236_24c6e9d2_0000": {"func": model_83236_24c6e9d2_0000, "volume": 170.4616465433, "area": 357.3422390928},
    "model_83362_2bb27f28_0000": {"func": model_83362_2bb27f28_0000, "volume": 0.6847578405, "area": 6.5973644535},
    "model_83409_4e6ef323_0000": {"func": model_83409_4e6ef323_0000, "volume": 1.1817267631, "area": 13.0331202397},
    "model_83423_7ea0c866_0000": {"func": model_83423_7ea0c866_0000, "volume": 3.7226961379, "area": 30.25114532},
    "model_85541_199004a0_0002": {"func": model_85541_199004a0_0002, "volume": 1060.3874555004, "area": 722.5708165738},
    "model_85552_3669d6cf_0000": {"func": model_85552_3669d6cf_0000, "volume": 0.2352291628, "area": 2.987228763},
    "model_86099_c101852f_0001": {"func": model_86099_c101852f_0001, "volume": 18.0641577581, "area": 80.1106126665},
    "model_86303_87045e9c_0000": {"func": model_86303_87045e9c_0000, "volume": 1769.9755764365, "area": 1008.6113432317},
    "model_86378_fb294b8e_0000": {"func": model_86378_fb294b8e_0000, "volume": 165.7693671831, "area": 700.3122540116},
    "model_86386_ce62c3a1_0000": {"func": model_86386_ce62c3a1_0000, "volume": 14767.5181996122, "area": 26604.1520815448},
    "model_86704_3f8f3bfe_0003": {"func": model_86704_3f8f3bfe_0003, "volume": 203.2247442262, "area": 1773.1646180917},
    "model_86905_949d0ba4_0000": {"func": model_86905_949d0ba4_0000, "volume": 65.283222971, "area": 142.9709507746},
    "model_87466_a6bedea0_0000": {"func": model_87466_a6bedea0_0000, "volume": 3.2986722863, "area": 26.8110597594},
    "model_88056_e0bff7c9_0000": {"func": model_88056_e0bff7c9_0000, "volume": 639.095496, "area": 538.7086},
    "model_88396_5f13c951_0000": {"func": model_88396_5f13c951_0000, "volume": 65.9763987623, "area": 110.8660377099},
    "model_89253_e57586a5_0000": {"func": model_89253_e57586a5_0000, "volume": 125.4861071985, "area": 162.1463933112},
    "model_89681_0c77b7fc_0006": {"func": model_89681_0c77b7fc_0006, "volume": 11.0163129817, "area": 42.228015082},
    "model_89681_0c77b7fc_0007": {"func": model_89681_0c77b7fc_0007, "volume": 101.1592834456, "area": 150.7964473723},
    "model_90077_e7a99c92_0000": {"func": model_90077_e7a99c92_0000, "volume": 80.9745506463, "area": 597.5309227128},
    "model_90104_558cd746_0000": {"func": model_90104_558cd746_0000, "volume": 14.4266287473, "area": 113.7012286414},
    "model_90114_99894f36_0000": {"func": model_90114_99894f36_0000, "volume": 319.0328480463, "area": 756.2478449869},
    "model_90205_97363b6d_0001": {"func": model_90205_97363b6d_0001, "volume": 1.3614543368, "area": 9.0619632792},
    "model_90205_97363b6d_0010": {"func": model_90205_97363b6d_0010, "volume": 0.5277875658, "area": 20.5460159545},
    "model_90615_6b438630_0000": {"func": model_90615_6b438630_0000, "volume": 120, "area": 511},
    "model_90628_b8795213_0013": {"func": model_90628_b8795213_0013, "volume": 0.252153659, "area": 7.8136137766},
    "model_90721_ee6f6982_0000": {"func": model_90721_ee6f6982_0000, "volume": 3.6240872938, "area": 26.6715265246},
    "model_91208_3ef96086_0000": {"func": model_91208_3ef96086_0000, "volume": 1078.194598712, "area": 1009.079560333},
    "model_91299_4f533c5d_0000": {"func": model_91299_4f533c5d_0000, "volume": 751.5828290357, "area": 545.556916357},
    "model_91391_c2de97c9_0000": {"func": model_91391_c2de97c9_0000, "volume": 46575.1482282078, "area": 8111.6548547187},
    "model_91410_a5189a65_0000": {"func": model_91410_a5189a65_0000, "volume": 0.1983894271, "area": 2.545528163},
    "model_91431_cc01fc10_0000": {"func": model_91431_cc01fc10_0000, "volume": 291.6718903333, "area": 280.1044786857},
    "model_91433_d1a5d966_0000": {"func": model_91433_d1a5d966_0000, "volume": 32.8327679407, "area": 115.051733828},
    "model_91434_7c784ac3_0000": {"func": model_91434_7c784ac3_0000, "volume": 6.0689665126, "area": 32.6304418507},
    "model_91457_9b6cdf83_0001": {"func": model_91457_9b6cdf83_0001, "volume": 6.729291464, "area": 24.5672545511},
    "model_91673_a331a9ee_0000": {"func": model_91673_a331a9ee_0000, "volume": 6.6781510766, "area": 83.452951703},
    "model_92286_2ab17805_0000": {"func": model_92286_2ab17805_0000, "volume": 1.4591857895, "area": 11.3687032946},
    "model_92355_a1f4144c_0000": {"func": model_92355_a1f4144c_0000, "volume": 8.6100684836, "area": 46.6651322961},
    "model_92553_3ba197ab_0000": {"func": model_92553_3ba197ab_0000, "volume": 5.9724580535, "area": 44.0395765834},
    "model_92738_0c72fe82_0000": {"func": model_92738_0c72fe82_0000, "volume": 31.804866, "area": 107.4786},
    "model_93181_b95f586d_0000": {"func": model_93181_b95f586d_0000, "volume": 124.689812421, "area": 174.169896715},
    "model_94163_9b899ce2_0000": {"func": model_94163_9b899ce2_0000, "volume": 0.0033994993, "area": 0.6943613291},
    "model_98408_4a172cb9_0000": {"func": model_98408_4a172cb9_0000, "volume": 0.9002415445, "area": 25.4199662344},
    "model_98416_af704f6f_0000": {"func": model_98416_af704f6f_0000, "volume": 120.4006292522, "area": 345.6402061749},
    "model_98883_3f3088e4_0000": {"func": model_98883_3f3088e4_0000, "volume": 9865.012528, "area": 3083.8648},
    "model_99079_80299be5_0000": {"func": model_99079_80299be5_0000, "volume": 391.8147038329, "area": 464.773264943},
    "model_99732_6f03d7fc_0001": {"func": model_99732_6f03d7fc_0001, "volume": 1407.4335088082, "area": 2506.9909375647},
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
