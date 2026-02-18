"""Batch 003 - passing/05_8to10ops
54 models bundled from Fusion360 Gallery reconstructions.
"""

from build123d import *
from build123d import Edge, BuildLine
from collections import Counter
from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
from OCP.Geom import Geom_BSplineCurve
from OCP.TColStd import TColStd_Array1OfReal, TColStd_Array1OfInteger
from OCP.TColgp import TColgp_Array1OfPnt
from OCP.gp import gp_Pnt


# Description: This is a parallelogram-shaped box or duct component with a rectangular cross-section, featuring flat side panels and open or beveled edges at the ends.
def model_141790_1137bb2a_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 425, perimeter: 84
            with BuildLine():
                Line((8.5, -12.5), (8.5, 12.5))
                Line((8.5, 12.5), (-8.5, 12.5))
                Line((-8.5, 12.5), (-8.5, -12.5))
                Line((-8.5, -12.5), (8.5, -12.5))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.2), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 3.4, perimeter: 34.4
            with BuildLine():
                Line((-8.5, -12.3), (8.5, -12.3))
                Line((-8.5, -12.5), (-8.5, -12.3))
                Line((8.5, -12.5), (-8.5, -12.5))
                Line((8.5, -12.3), (8.5, -12.5))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.2), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 3.4, perimeter: 34.4
            with BuildLine():
                Line((8.5, 12.3), (-8.5, 12.3))
                Line((8.5, 12.5), (8.5, 12.3))
                Line((-8.5, 12.5), (8.5, 12.5))
                Line((-8.5, 12.3), (-8.5, 12.5))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.2), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 4.9200000367, perimeter: 49.6000003666
            with BuildLine():
                Line((8.3, -12.3), (8.3, 12.3000001833))
                Line((8.5, -12.3), (8.3, -12.3))
                Line((8.5, 12.3000001833), (8.5, -12.3))
                Line((8.3, 12.3000001833), (8.5, 12.3000001833))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.2), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 4.9200000059, perimeter: 49.6000000586
            with BuildLine():
                Line((-8.5, 12.3000000293), (-8.5, -12.3))
                Line((-8.5, -12.3), (-8.3, -12.3))
                Line((-8.3, -12.3), (-8.3, 12.3000000293))
                Line((-8.3, 12.3000000293), (-8.5, 12.3000000293))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.ADD)
    return part.part


# Description: This is a roof tile or curved panel with a dual-slope design, featuring a central valley, textured side flanges, and blue-highlighted upper edges that suggest mounting surfaces or structural ridges.
def model_142182_3b1414ce_0000():
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
        # Sketch13 -> Extrude11 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.0994111946, perimeter: 14.4799929578
            with BuildLine():
                Line((-20.4925875438, 22.9915634326), (-19.3767762092, 22.9915634326))
                CenterArc((-19.3767762092, 24.8211566925), 1.8295932599, -90, 62.4020185775)
                Line((-22.1752776872, 24.7380978098), (-17.7553542516, 23.9735705128))
                Line((-23.7521152372, 24.3558341613), (-22.1752776872, 24.7380978098))
                CenterArc((-23, 23.8865256797), 0.8865256797, 148.0364632853, 121.9635367147)
                Line((-23, 23), (-22, 23))
                CenterArc((-21.2462701634, 23), 0.7537298366, -0.6413303244, 180.6413303244)
            make_face()
        # Symmetric extrude, full_length=True, total=3
        extrude(amount=1.5, both=True)
    return part.part


# Description: This is an open-frame buggy or ATV chassis featuring a rectangular tube steel frame with an open cabin design, large cylindrical wheels at each corner, and exposed structural bracing with diagonal support members throughout the frame.
def model_142226_ba437656_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 12.81, perimeter: 16.4
            with BuildLine():
                Line((6.1, -2.1), (0, -2.1))
                Line((6.1, 0), (6.1, -2.1))
                Line((0, 0), (6.1, 0))
                Line((0, -2.1), (0, 0))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 18 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.053014376, perimeter: 1.0068583471
            with BuildLine():
                CenterArc((5.7, 1.7000000253), 0.15, -90, 270)
                Line((5.55, 1.7000000253), (5.7, 1.7000000253))
                Line((5.7, 1.7000000253), (5.7, 1.5500000253))
            make_face()
            # Profile area: 0.0176714587, perimeter: 0.535619449
            with BuildLine():
                Line((5.7, 1.7000000253), (5.7, 1.5500000253))
                Line((5.55, 1.7000000253), (5.7, 1.7000000253))
                CenterArc((5.7, 1.7000000253), 0.15, 180, 90)
            make_face()
            # Profile area: 0.0176714587, perimeter: 0.535619449
            with BuildLine():
                Line((5.7, 0.25), (5.7, 0.4))
                Line((5.7, 0.4), (5.55, 0.4))
                CenterArc((5.7, 0.4), 0.15, 180, 90)
            make_face()
            # Profile area: 0.0176714587, perimeter: 0.535619449
            with BuildLine():
                Line((5.7, 0.4), (5.55, 0.4))
                Line((5.7, 0.55), (5.7, 0.4))
                CenterArc((5.7, 0.4), 0.15, 90, 90)
            make_face()
            # Profile area: 0.0176714587, perimeter: 0.535619449
            with BuildLine():
                CenterArc((5.7, 0.4), 0.15, -90, 90)
                Line((5.7, 0.4), (5.85, 0.4))
                Line((5.7, 0.25), (5.7, 0.4))
            make_face()
            # Profile area: 0.0176714587, perimeter: 0.535619449
            with BuildLine():
                Line((5.7, 0.55), (5.7, 0.4))
                Line((5.7, 0.4), (5.85, 0.4))
                CenterArc((5.7, 0.4), 0.15, 0, 90)
            make_face()
            # Profile area: 0.0176714587, perimeter: 0.535619449
            with BuildLine():
                Line((0.550000006, 0.4), (0.400000006, 0.4))
                CenterArc((0.400000006, 0.4), 0.15, 0, 90)
                Line((0.400000006, 0.4), (0.400000006, 0.55))
            make_face()
            # Profile area: 0.053014376, perimeter: 1.0068583471
            with BuildLine():
                Line((0.400000006, 0.4), (0.400000006, 0.55))
                CenterArc((0.400000006, 0.4), 0.15, 90, 270)
                Line((0.550000006, 0.4), (0.400000006, 0.4))
            make_face()
            # Profile area: 0.0176714587, perimeter: 0.535619449
            with BuildLine():
                Line((0.400000006, 1.7000000253), (0.250000006, 1.7000000253))
                Line((0.400000006, 1.8500000253), (0.400000006, 1.7000000253))
                CenterArc((0.400000006, 1.7000000253), 0.15, 90, 90)
            make_face()
            # Profile area: 0.0176714587, perimeter: 0.535619449
            with BuildLine():
                CenterArc((0.400000006, 1.7000000253), 0.15, 0, 90)
                Line((0.400000006, 1.8500000253), (0.400000006, 1.7000000253))
                Line((0.400000006, 1.7000000253), (0.550000006, 1.7000000253))
            make_face()
            # Profile area: 0.0176714587, perimeter: 0.535619449
            with BuildLine():
                Line((0.400000006, 1.5500000253), (0.400000006, 1.7000000253))
                Line((0.400000006, 1.7000000253), (0.250000006, 1.7000000253))
                CenterArc((0.400000006, 1.7000000253), 0.15, 180, 90)
            make_face()
            # Profile area: 0.0176714587, perimeter: 0.535619449
            with BuildLine():
                CenterArc((0.400000006, 1.7000000253), 0.15, -90, 90)
                Line((0.400000006, 1.7000000253), (0.550000006, 1.7000000253))
                Line((0.400000006, 1.5500000253), (0.400000006, 1.7000000253))
            make_face()
        # OneSide extrude, distance=-1.3
        extrude(amount=-1.3, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.246642622, perimeter: 3.6461873918
            with BuildLine():
                Line((0, 1.2527864045), (0, 2.1))
                CenterArc((-0.4, 1.7), 0.6, -48.1896851042, 186.3793702084)
                Line((0, 2.1), (-0.8472135955, 2.1))
            make_face()
            # Profile area: 0.246642622, perimeter: 3.6461873918
            with BuildLine():
                CenterArc((-5.7, 1.7), 0.6, 41.8103148958, 186.3793702084)
                Line((-6.1, 2.1), (-6.1, 1.2527864045))
                Line((-5.2527864045, 2.1), (-6.1, 2.1))
            make_face()
            # Profile area: 0.246642622, perimeter: 3.6461873918
            with BuildLine():
                CenterArc((-0.4, 0.4), 0.6, -138.1896851042, 186.3793702084)
                Line((0, 0), (0, 0.8472135955))
                Line((-0.8472135955, 0), (0, 0))
            make_face()
            # Profile area: 0.246642622, perimeter: 3.6461873918
            with BuildLine():
                CenterArc((-5.7, 0.4), 0.6, 131.8103148958, 186.3793702084)
                Line((-6.1, 0), (-5.2527864045, 0))
                Line((-6.1, 0.8472135955), (-6.1, 0))
            make_face()
        # OneSide extrude, distance=-0.7
        extrude(amount=-0.7, mode=Mode.ADD)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 18 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1256637061, perimeter: 1.4283185307
            with BuildLine():
                Line((-0.4, 0), (-0.4, 0.4))
                Line((-0.4, 0.4), (-0.8, 0.4))
                CenterArc((-0.4, 0.4), 0.4, -180, 90)
            make_face()
            # Profile area: 0.1256637061, perimeter: 1.4283185307
            with BuildLine():
                Line((-0.4, 0.4), (0, 0.4))
                Line((-0.4, 0), (-0.4, 0.4))
                CenterArc((-0.4, 0.4), 0.4, -90, 90)
            make_face()
            # Profile area: 0.1256637061, perimeter: 1.4283185307
            with BuildLine():
                CenterArc((-0.4, 0.4), 0.4, 90, 90)
                Line((-0.4, 0.4), (-0.8, 0.4))
                Line((-0.4, 0.8), (-0.4, 0.4))
            make_face()
            # Profile area: 0.1256637061, perimeter: 1.4283185307
            with BuildLine():
                CenterArc((-0.4, 0.4), 0.4, 0, 90)
                Line((-0.4, 0.8), (-0.4, 0.4))
                Line((-0.4, 0.4), (0, 0.4))
            make_face()
            # Profile area: 0.1256637061, perimeter: 1.4283185307
            with BuildLine():
                Line((-0.4, 1.7), (-0.4, 1.3))
                Line((-0.8, 1.7), (-0.4, 1.7))
                CenterArc((-0.4, 1.7), 0.4, 180, 90)
            make_face()
            # Profile area: 0.3769911184, perimeter: 2.6849555922
            with BuildLine():
                CenterArc((-0.4, 1.7), 0.4, 0, 90)
                CenterArc((-0.4, 1.7), 0.4, 90, 90)
                Line((-0.8, 1.7), (-0.4, 1.7))
                Line((-0.4, 1.7), (-0.4, 1.3))
                CenterArc((-0.4, 1.7), 0.4, -90, 90)
            make_face()
            # Profile area: 0.3769911184, perimeter: 2.6849555922
            with BuildLine():
                CenterArc((-5.7, 0.4), 0.4, -89.9999986674, 89.9999986674)
                Line((-5.3, 0.4), (-5.7, 0.4))
                Line((-5.7, 0.4), (-5.7, 0.8))
                CenterArc((-5.7, 0.4), 0.4, 90, 90)
                CenterArc((-5.7, 0.4), 0.4, -180, 90.0000013326)
            make_face()
            # Profile area: 0.1256637061, perimeter: 1.4283185307
            with BuildLine():
                CenterArc((-5.7, 0.4), 0.4, 0, 90)
                Line((-5.7, 0.4), (-5.7, 0.8))
                Line((-5.3, 0.4), (-5.7, 0.4))
            make_face()
            # Profile area: 0.1256637061, perimeter: 1.4283185307
            with BuildLine():
                CenterArc((-5.7, 1.7), 0.4, -90, 90)
                Line((-5.7, 1.7), (-5.3, 1.7))
                Line((-5.7, 1.3), (-5.7, 1.7))
            make_face()
            # Profile area: 0.1256637037, perimeter: 1.4283185185
            with BuildLine():
                Line((-5.6999999878, 2.1), (-5.7, 1.7))
                Line((-5.7, 1.7), (-5.3, 1.7))
                CenterArc((-5.7, 1.7), 0.4, 0, 89.9999982546)
            make_face()
            # Profile area: 0.1256637061, perimeter: 1.4283185307
            with BuildLine():
                CenterArc((-5.7, 1.7), 0.4, 180, 90)
                Line((-5.7, 1.3), (-5.7, 1.7))
                Line((-5.7, 1.7), (-6.1, 1.7))
            make_face()
            # Profile area: 0.1256637086, perimeter: 1.4283185429
            with BuildLine():
                Line((-5.7, 1.7), (-6.1, 1.7))
                Line((-5.6999999878, 2.1), (-5.7, 1.7))
                CenterArc((-5.7, 1.7), 0.4, 89.9999982546, 90.0000017454)
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a curved duct or conduit assembly with a serpentine shape featuring a large circular opening on the left side, angular rectangular sections in the middle, and a tapered rounded end on the right, designed for fluid or air flow applications.
def model_142246_0851be5e_0012():
    """Model: Component33"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 13.1587608005, perimeter: 19.8814150222
            with BuildLine():
                Line((-1.8, -2.8), (-1.8, 0))
                CenterArc((0, -2.8), 1.8, 180, 180)
                Line((1.8, 0), (1.8, -2.8))
                Line((-1.8, 0), (1.8, 0))
            make_face()
            with BuildLine():
                CenterArc((0, -2.8), 0.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.8), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 2, perimeter: 6
            with BuildLine():
                Line((-1.8, 2), (-1.8, 0))
                Line((-1.8, 0), (-0.8, 0))
                Line((-0.8, 0), (-0.8, 2))
                Line((-0.8, 2), (-1.8, 2))
            make_face()
        # OneSide extrude, distance=3.2
        extrude(amount=3.2, mode=Mode.ADD)

        # Sketch5 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 4), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 5.6, perimeter: 9.9388269481
            with BuildLine():
                Line((-1.8, 2), (-5, 1.5))
                Line((-5, 1.5), (-5, 0))
                Line((-5, 0), (-1.8, 0))
                Line((-1.8, 2), (-1.8, 0))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.ADD)

        # Sketch6 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3), x_dir=(1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 3.5342917688, perimeter: 7.7123890251
            with BuildLine():
                Line((3.5000000522, 0), (6.5000000969, 0))
                CenterArc((5, 0), 1.5, 0, 180)
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.ADD)
    return part.part


# Description: This is a dark blue molded or cast housing component with an irregular, roughly cubic shape featuring a large mesh-textured opening on the upper surface and a smaller rectangular cutout on the front face.
def model_142764_e4f86a3b_0000():
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
        # Sketch has 13 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 255.189691386, perimeter: 78.175103885
            with BuildLine():
                Line((-1.4762340947, 2.6288231709), (-5.7110249315, 2.5810713307))
                CenterArc((-5.7076423226, 2.2810904013), 0.3, 90.6460444129, 124.4761192973)
                Line((-5.9530204907, 2.1084938933), (-3.0599884507, -2.0044914166))
                CenterArc((-2.2420612236, -1.429169723), 1, -144.8778362899, 54.7320973911)
                _nurbs_edge([(-2.2446048445, -2.429166488), (-1.9767250232, -2.4300613449), (-1.4588011459, -2.4316130835), (-0.7354195833, -2.4332269087), (0.1267644601, -2.4353655903), (1.0589155374, -2.4464001513), (1.8762719591, -2.4770778212), (2.6100793653, -2.5395618431), (3.2882736082, -2.6449029734), (3.9322772434, -2.8000517855), (4.5551517532, -3.0057231125), (5.0421686516, -3.2092375591), (5.4022974072, -3.3827485996), (5.6401401146, -3.5075515329), (5.7585005816, -3.5722351534)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                Line((5.7585005816, -3.5722351534), (9.7433748058, -3.5722351534))
                _nurbs_edge([(9.7433748058, -3.5722351534), (9.7885367172, -3.5399970407), (9.8794180663, -3.476373743), (10.0174126377, -3.3834975327), (10.2048057936, -3.2648646561), (10.4450957527, -3.1258268403), (10.6919612525, -2.9968485718), (10.9459178962, -2.8787186434), (11.207208299, -2.7718082181), (11.4754974851, -2.6756048354), (11.7502385271, -2.5892717819), (11.974759973, -2.5274393757), (12.1456404456, -2.484873445), (12.2606490549, -2.4581610776), (12.3184254443, -2.4452211411)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(12.3184254443, -2.4452211411), (12.3375129227, -2.4153573355), (12.3756615055, -2.3560635017), (12.4328052634, -2.2684240025), (12.5088360619, -2.1542173562), (12.6035876101, -2.0161786002), (12.6980243168, -1.8833181375), (12.7921167328, -1.7561203278), (12.8858426081, -1.6349511235), (12.9792068648, -1.5197295697), (13.0722328829, -1.4100711263), (13.1464033127, -1.3264625252), (13.2018989533, -1.2659301068), (13.2388382464, -1.2265258255), (13.257293443, -1.207061347)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                Line((13.257293443, -1.207061347), (13.257293443, 2.4050761829))
                _nurbs_edge([(11.7798183326, 10.0809114783), (11.8195952959, 10.0829568314), (11.895744879, 10.0797501818), (11.9997563619, 10.0530483636), (12.1179580451, 9.9735460476), (12.232108002, 9.801831765), (12.3147787802, 9.5614126509), (12.3707013375, 9.2605592885), (12.4062277024, 8.9107652736), (12.4283206078, 8.5252883915), (12.4435270387, 8.1177100282), (12.4570633743, 7.7006107134), (12.4716043165, 7.2839640437), (12.4870248518, 6.8744694865), (12.501647239, 6.4763596867), (12.5131099445, 6.0918321014), (12.519392995, 5.7216068469), (12.5197458278, 5.3654000337), (12.5157466, 5.0224294927), (12.512106487, 4.6918484784), (12.5154569313, 4.3727750496), (12.533351858, 4.064353737), (12.5731865275, 3.7658002327), (12.6411749154, 3.4764480119), (12.7412104494, 3.1957932111), (12.8753639069, 2.9234805122), (13.0106370542, 2.7121227908), (13.127852154, 2.5572035181), (13.2129819502, 2.4555193955), (13.257293443, 2.4050761829)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.04, 0.08, 0.12, 0.16, 0.2, 0.24, 0.28, 0.32, 0.36, 0.4, 0.44, 0.48, 0.52, 0.56, 0.6, 0.64, 0.68, 0.72, 0.76, 0.8, 0.84, 0.88, 0.92, 0.96, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(-8.8077198183, 10.1946085658), (-8.6560342853, 10.2155034742), (-8.3470655422, 10.2564526912), (-7.8668192031, 10.3153547698), (-7.1927689205, 10.3888263528), (-6.2936334111, 10.4719965371), (-5.3382688867, 10.5460150171), (-4.3284238826, 10.610093349), (-3.2682562095, 10.6630354827), (-2.1642624877, 10.7033783642), (-1.0246712344, 10.7296591588), (0.1409186583, 10.7406622481), (1.3219388999, 10.7356758951), (2.5071729194, 10.7148087599), (3.6851146306, 10.6791890204), (4.8445224081, 10.6305766653), (5.9749347985, 10.5710885688), (7.06726918, 10.5028914051), (8.1143410495, 10.4279467199), (9.1117218361, 10.3476836826), (10.0574438806, 10.2629757275), (10.7722994198, 10.1920367168), (11.2850996543, 10.1371324091), (11.6166341419, 10.0997771865), (11.7798183326, 10.0809114783)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1, 1, 1, 1, 1], 5)
                Line((-8.8077198183, 10.1946085658), (-11.2388872253, 5.5534457311))
                CenterArc((-10.7959746786, 5.3214360848), 0.5, 152.3532292009, 117.6467707991)
                Line((-10.7959746786, 4.8214360848), (-1.4818717763, 4.8214360848))
                CenterArc((-1.4818717763, 4.3214360848), 0.5, 0, 90)
                Line((-0.9818717763, 4.3214360848), (-0.9818717763, 3.1287913865))
                CenterArc((-1.4818717763, 3.1287913865), 0.5, -89.3539555871, 89.3539555871)
            make_face()
        # Symmetric extrude, each_side=7
        extrude(amount=7, both=True)
    return part.part


# Description: This is a cutting tool or lathe bit with an elongated hexagonal body, a tapered nose cone, and longitudinal flutes or grooves along its top surface for chip evacuation and cutting geometry.
def model_142852_65dcbe39_0000():
    """Model: Rail"""
    with BuildPart() as part:
        # profile -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 58.1238801901, perimeter: 38.1312231969
            with BuildLine():
                Line((1.905, -13.3506115984), (-1.905, -13.3506115984))
                Line((1.905, 1.905), (1.905, -13.3506115984))
                Line((-1.905, 1.905), (1.905, 1.905))
                Line((-1.905, -13.3506115984), (-1.905, 1.905))
            make_face()
        # OneSide extrude, distance=1.905
        extrude(amount=1.905)

        # miter cut -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.905, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 10.887075, perimeter: 16.8181536726
            with BuildLine():
                Line((-1.905, -1.905), (1.905, -1.905))
                Line((1.905, -1.905), (1.905, 1.905))
                Line((0, 0), (1.905, 1.905))
                Line((0, 0), (-1.905, 1.905))
                Line((-1.905, 1.905), (-1.905, -1.905))
            make_face()
        # OneSide extrude, distance=-1.905
        extrude(amount=-1.905, mode=Mode.SUBTRACT)

        # slated notch -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-1.905, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 2.872978125, perimeter: 6.8848790542
            with BuildLine():
                Line((1.905, 0), (1.905, 1.27))
                Line((0, 1.74625), (1.905, 1.27))
                Line((0, 1.74625), (0, 0))
                Line((0, 0), (1.905, 0))
            make_face()
        # OneSide extrude, distance=-3.81
        extrude(amount=-3.81, mode=Mode.SUBTRACT)

        # tenon -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.905), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 1.209675, perimeter: 5.08
            with BuildLine():
                Line((-0.9525, 0.635), (-0.9525, 1.27))
                Line((0.9525, 0.635), (-0.9525, 0.635))
                Line((0.9525, 1.27), (0.9525, 0.635))
                Line((0.9525, 1.27), (-0.9525, 1.27))
            make_face()
        # OneSide extrude, distance=3.81
        extrude(amount=3.81, mode=Mode.ADD)

        # coping -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 13.3506115984), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0503681315, perimeter: 3.8915393464
            with BuildLine():
                Line((-1.905, 1.905), (-1.905, 1.825625))
                CenterArc((0, -20.9946874925), 22.8996874926, 90.0000497275, 4.7718383348)
                Line((-0.0000198748, 1.905), (-1.905, 1.905))
            make_face()
            # Profile area: 0.0503681315, perimeter: 3.8916188458
            with BuildLine():
                CenterArc((0, -20.9946874925), 22.8996874926, 85.2281119377, 4.7719377898)
                Line((1.905, 1.825625), (1.905, 1.905))
                Line((1.905, 1.905), (-0.0000198748, 1.905))
            make_face()
        # OneSide extrude, distance=-15.25524
        extrude(amount=-15.25524, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a curved duct or channel component with an elongated, horizontal profile featuring a tapered design, an open top surface with a blue-tinted interior, dark outer walls, and a connector or attachment point on the right end.
def model_142852_c569311a_0003():
    """Model: Short Frame"""
    with BuildPart() as part:
        # profile -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 45.1612, perimeter: 42.7442048969
            with BuildLine():
                Line((7.62, 17.78), (-7.62, 17.78))
                Line((10.16, 20.32), (7.62, 17.78))
                Line((-10.16, 20.32), (10.16, 20.32))
                Line((-10.16, 20.32), (-7.62, 17.78))
            make_face()
        # OneSide extrude, distance=1.905
        extrude(amount=1.905)

        # notch -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.905, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.2258, perimeter: 8.6721024484
            with BuildLine():
                Line((-7.62, -17.78), (-7.62, -20.32))
                Line((-7.62, -17.78), (-10.16, -20.32))
                Line((-10.16, -20.32), (-7.62, -20.32))
            make_face()
        # OneSide extrude, distance=-1.27
        extrude(amount=-1.27, mode=Mode.SUBTRACT)

        # tenon -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(7.62, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.80645, perimeter: 3.81
            with BuildLine():
                Line((19.685, 0.9525), (18.415, 0.9525))
                Line((19.685, 1.5875), (19.685, 0.9525))
                Line((18.415, 1.5875), (19.685, 1.5875))
                Line((18.415, 0.9525), (18.415, 1.5875))
            make_face()
        # OneSide extrude, distance=2.54
        extrude(amount=2.54, mode=Mode.ADD)

        # panel slot -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -17.78), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.30241875, perimeter: 2.2225
            with BuildLine():
                Line((-7.62, 1.031875), (-7.62, 0.555625))
                Line((-8.255, 1.031875), (-7.62, 1.031875))
                Line((-8.255, 0.555625), (-8.255, 1.031875))
                Line((-7.62, 0.555625), (-8.255, 0.555625))
            make_face()
            # Profile area: 7.25805, perimeter: 31.4325
            with BuildLine():
                Line((7.62, 0.555625), (-7.62, 0.555625))
                Line((7.62, 0.555625), (7.62, 0.635))
                Line((7.62, 0.635), (7.62, 1.031875))
                Line((-7.62, 1.031875), (7.62, 1.031875))
                Line((-7.62, 1.031875), (-7.62, 0.555625))
            make_face()
            # Profile area: 0.30241875, perimeter: 2.2225
            with BuildLine():
                Line((8.255, 0.555625), (7.62, 0.555625))
                Line((8.255, 1.031875), (8.255, 0.555625))
                Line((7.62, 1.031875), (8.255, 1.031875))
                Line((7.62, 0.635), (7.62, 1.031875))
                Line((7.62, 0.555625), (7.62, 0.635))
            make_face()
        # OneSide extrude, distance=-0.47625
        extrude(amount=-0.47625, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a fastener or anchor bolt with a cylindrical shaft and a large, flat, circular head featuring a textured or knurled surface for grip.
def model_142868_bcc940c6_0000():
    """Model: Button"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-2.5664, -1.866)):
                Circle(0.3)
        # OneSide extrude, distance=0.075
        extrude(amount=0.075)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.075, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.0445795573, perimeter: 5.9690260418
            with BuildLine():
                CenterArc((-2.5664, -1.866), 0.65, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-2.5664, -1.866), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-2.5664, -1.866)):
                Circle(0.3)
        # OneSide extrude, distance=0.15
        extrude(amount=0.15, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((2.5664, -1.866)):
                Circle(0.3)
        # OneSide extrude, distance=1.97
        extrude(amount=1.97, mode=Mode.ADD)

        # Sketch5 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -1.97, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0907920277, perimeter: 1.0681415022
            with Locations((2.5664, -1.866)):
                Circle(0.17)
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a blue anodized aluminum extrusion or channel component featuring a long, horizontal L-shaped or bent profile with a hollow rectangular cross-section, a mounting flange on one end, and what appears to be slots or grooves along its length for attachment or alignment purposes.
def model_143019_77f4e3fa_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude3 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints, 25 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.7612708, perimeter: 38.2524
            with BuildLine():
                Line((5.5334, 2.0174), (5.5334, -0.5226))
                Line((5.5334, -0.5226), (-1.985, -0.5226))
                Line((-1.985, -1.1068), (-1.985, -0.5226))
                Line((6.016, -1.1068), (-1.985, -1.1068))
                Line((6.016, 2.5), (6.016, -1.1068))
                Line((-1.985, 2.5), (6.016, 2.5))
                Line((-1.985, 2.0174), (-1.985, 2.5))
                Line((-1.985, 2.0174), (5.5334, 2.0174))
            make_face()
            # Profile area: 17.5585147414, perimeter: 54.0781730177
            with BuildLine():
                Line((-1.985, 2.0174), (-1.985, 2.5))
                Line((-1.985, 2.5), (6.016, 2.5))
                Line((6.016, 2.5), (6.016, -1.1068))
                Line((6.016, -1.1068), (-1.985, -1.1068))
                Line((-1.985, -1.1068), (-1.985, -0.5226))
                Line((-1.985, -0.5226), (-2.747, -0.5226))
                Line((-2.747, -1.8688), (-2.747, -0.5226))
                Line((6.778, -1.8688), (-2.747, -1.8688))
                Line((6.778, 3.262), (6.778, -1.8688))
                Line((-2.747, 3.262), (6.778, 3.262))
                Line((-2.747, 2.0174), (-2.747, 3.262))
                Line((-2.747, 2.0174), (-1.985, 2.0174))
            make_face()
            with BuildLine():
                CenterArc((6.397, 2.881), 0.2032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.397, -1.4878), 0.2032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-2.366, -1.4878), 0.2032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-2.366, 2.881), 0.2032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)

        # Sketch2 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.635, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.6516096, perimeter: 8.9408
            with BuildLine():
                Line((-1.19, 1.1068), (-1.19, 0.7004))
                Line((-5.254, 1.1068), (-1.19, 1.1068))
                Line((-5.254, 0.7004), (-5.254, 1.1068))
                Line((-1.19, 0.7004), (-5.254, 0.7004))
            make_face()
        # OneSide extrude, distance=-0.4572
        extrude(amount=-0.4572, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude5 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.2354414454, perimeter: 5.9503432544
            with BuildLine():
                Line((-1.6739011807, 3.5907027108), (-2.8423011807, 3.5907027108))
                Line((-1.6739011807, 4.7591027108), (-1.6739011807, 3.5907027108))
                Line((-2.8423011807, 4.7591027108), (-1.6739011807, 4.7591027108))
                Line((-2.8423011807, 3.5907027108), (-2.8423011807, 4.7591027108))
            make_face()
            with BuildLine():
                CenterArc((-2.4613011807, 4.3527027108), 0.2032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.4572
        extrude(amount=0.4572)

        # Sketch4 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.4572, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.16516096, perimeter: 1.6256
            with BuildLine():
                Line((2.0803011807, -3.5907027108), (2.0803011807, -3.9971027108))
                Line((1.6739011807, -3.5907027108), (2.0803011807, -3.5907027108))
                Line((1.6739011807, -3.9971027108), (1.6739011807, -3.5907027108))
                Line((2.0803011807, -3.9971027108), (1.6739011807, -3.9971027108))
            make_face()
        # OneSide extrude, distance=-0.0762
        extrude(amount=-0.0762, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical sleeve or bushing with a hollow circular bore, featuring two opposing oval slots or cutouts on opposite sides of the outer surface.
def model_143324_6d184340_0000():
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
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 7.283920012, perimeter: 45.8829607057
            with BuildLine():
                CenterArc((0, 0), 3.81, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3.4925, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=2.54
        extrude(amount=2.54, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 1.9793260902, perimeter: 13.1031958439
            with BuildLine():
                CenterArc((0, 0), 3.81, 45.1083094731, 90)
                Line((2.688979259, 2.6991647865), (2.9130608639, 2.9240951854))
                CenterArc((0, 0), 4.1275, 45.1083094731, 90)
                Line((-2.6991647865, 2.688979259), (-2.9240951854, 2.9130608639))
            make_face()
        # Symmetric extrude, each_side=2.286
        extrude(amount=2.286, both=True, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            with Locations((0, 3.81)):
                Circle(0.635)
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            with Locations((-0.0119999405, -3.8099811025)):
                Circle(0.635)
        # Symmetric extrude, each_side=3.81
        extrude(amount=3.81, both=True, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.2005095857, perimeter: 4.4356863493
            with BuildLine():
                Line((-1.0656374763, 0.0963684298), (-1.0656374763, -0.2265886091))
                Line((-0.9540163646, 0.0963684298), (-1.0656374763, 0.0963684298))
                _nurbs_edge([(-0.9004382561, 0.0928957439), (-0.9076215964, 0.0938997211), (-0.9253832544, 0.0963821734), (-0.9433286301, 0.0963735598), (-0.9540163646, 0.0963684298)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0217366688, 0.0537464834, 0.0537464834, 0.0537464834, 0.0537464834], 3)
                _nurbs_edge([(-0.8565339516, 0.0735480763), (-0.86364756, 0.0777992281), (-0.8774852695, 0.0860687589), (-0.8929321952, 0.0906631907), (-0.9004382561, 0.0928957439)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0247504317, 0.0481456475, 0.0481456475, 0.0481456475, 0.0481456475], 3)
                _nurbs_edge([(-0.8076687227, 0.0249309517), (-0.8158783305, 0.0351911789), (-0.8303433601, 0.0532693249), (-0.8486271163, 0.067426002), (-0.8565339516, 0.0735480763)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0392424042, 0.0691436849, 0.0691436849, 0.0691436849, 0.0691436849], 3)
                _nurbs_edge([(-0.7382156025, -0.075280013), (-0.7507925938, -0.0558484943), (-0.7728891384, -0.0217092154), (-0.7971966491, 0.0108876769), (-0.8076687227, 0.0249309517)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0694149749, 0.121955326, 0.121955326, 0.121955326, 0.121955326], 3)
                Line((-0.6419733535, -0.2265886091), (-0.7382156025, -0.075280013))
                Line((-0.5209265123, -0.2265886091), (-0.6419733535, -0.2265886091))
                Line((-0.6474303971, -0.0286471867), (-0.5209265123, -0.2265886091))
                _nurbs_edge([(-0.7273015152, 0.0680910922), (-0.7131586714, 0.0539616074), (-0.6834485198, 0.0242795195), (-0.6598141574, -0.0104499129), (-0.6474303971, -0.0286471867)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0598355881, 0.1256978026, 0.1256978026, 0.1256978026, 0.1256978026], 3)
                _nurbs_edge([(-0.7853444885, 0.1043059207), (-0.7738793502, 0.0986408775), (-0.7533176506, 0.0884811293), (-0.7352809909, 0.0743449728), (-0.7273015152, 0.0680910922)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0382366453, 0.0685740022, 0.0685740022, 0.0685740022, 0.0685740022], 3)
                _nurbs_edge([(-0.6305632363, 0.1717746831), (-0.651000929, 0.1555266518), (-0.69639068, 0.1194416539), (-0.7537902729, 0.1096749566), (-0.7853444885, 0.1043059207)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0771238024, 0.1712830429, 0.1712830429, 0.1712830429, 0.1712830429], 3)
                _nurbs_edge([(-0.5804577242, 0.3022473432), (-0.5824061463, 0.277612673), (-0.5862405718, 0.2291325187), (-0.6159502247, 0.1906853403), (-0.6305632363, 0.1717746831)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0724052302, 0.1424909165, 0.1424909165, 0.1424909165, 0.1424909165], 3)
                _nurbs_edge([(-0.6107194792, 0.4118840672), (-0.6018933181, 0.3948290697), (-0.5840881816, 0.3604237878), (-0.5816747811, 0.3217501316), (-0.5804577242, 0.3022473432)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0569333703, 0.1148524742, 0.1148524742, 0.1148524742, 0.1148524742], 3)
                _nurbs_edge([(-0.6915827761, 0.4810891725), (-0.6754734948, 0.4731580474), (-0.6426459412, 0.4569959712), (-0.6214924409, 0.427106199), (-0.6107194792, 0.4118840672)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.052972876, 0.1079483247, 0.1079483247, 0.1079483247, 0.1079483247], 3)
                _nurbs_edge([(-0.8394187163, 0.5006848551), (-0.8106878861, 0.5004637773), (-0.7605149478, 0.5000777071), (-0.7122216105, 0.4867744891), (-0.6915827761, 0.4810891725)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0857162548, 0.1496871597, 0.1496871597, 0.1496871597, 0.1496871597], 3)
                Line((-1.1618796582, 0.5006848551), (-0.8394187163, 0.5006848551))
                Line((-1.1618796582, -0.2265886091), (-1.1618796582, 0.5006848551))
                Line((-1.0656374763, -0.2265886091), (-1.1618796582, -0.2265886091))
            make_face()
            with BuildLine():
                Line((-0.8354499708, 0.4203176476), (-1.0656374763, 0.4203176476))
                _nurbs_edge([(-0.7171315919, 0.3870793558), (-0.7328222558, 0.3967328622), (-0.7688630266, 0.4189065455), (-0.8114203495, 0.4198084149), (-0.8354499708, 0.4203176476)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0543600859, 0.1248627473, 0.1248627473, 0.1248627473, 0.1248627473], 3)
                _nurbs_edge([(-0.6796765099, 0.3022473432), (-0.6811831544, 0.3186322257), (-0.684170935, 0.3511245865), (-0.7062074186, 0.3751628417), (-0.7171315919, 0.3870793558)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0479284759, 0.0950454989, 0.0950454989, 0.0950454989, 0.0950454989], 3)
                _nurbs_edge([(-0.6990241776, 0.2370110131), (-0.6933811294, 0.2472110441), (-0.6821360611, 0.267536946), (-0.6804943637, 0.2907053878), (-0.6796765099, 0.3022473432)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0345144738, 0.0687780083, 0.0687780083, 0.0687780083, 0.0687780083], 3)
                _nurbs_edge([(-0.7555788825, 0.1933547534), (-0.7440179058, 0.1984365796), (-0.7215288508, 0.2083220307), (-0.7063836608, 0.2276291358), (-0.6990241776, 0.2370110131)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0372369691, 0.0724354234, 0.0724354234, 0.0724354234, 0.0724354234], 3)
                _nurbs_edge([(-0.858766384, 0.179712174), (-0.8390386558, 0.1799270163), (-0.8040462322, 0.1803080967), (-0.7702999677, 0.1893920662), (-0.7555788825, 0.1933547534)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0588859614, 0.1044500659, 0.1044500659, 0.1044500659, 0.1044500659], 3)
                Line((-1.0656374763, 0.179712174), (-0.858766384, 0.179712174))
                Line((-1.0656374763, 0.4203176476), (-1.0656374763, 0.179712174))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.135951839, perimeter: 3.3629027622
            with BuildLine():
                Line((0.5218625893, -0.2265886091), (0.4285969366, -0.2265886091))
                _nurbs_edge([(0.4992904295, -0.1633366369), (0.5016813471, -0.1742629744), (0.5065053279, -0.1963082529), (0.5167137727, -0.2164365386), (0.5218625893, -0.2265886091)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0334063782, 0.0674016261, 0.0674016261, 0.0674016261, 0.0674016261], 3)
                _nurbs_edge([(0.4935853113, -0.0058268928), (0.4933800421, -0.0397367642), (0.4930616119, -0.0923405037), (0.4976572654, -0.1447218139), (0.4992904295, -0.1633366369)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.1016471908, 0.1576833566, 0.1576833566, 0.1576833566, 0.1576833566], 3)
                Line((0.4935853113, 0.1132355906), (0.4935853113, -0.0058268928))
                _nurbs_edge([(0.4891204466, 0.1955871857), (0.4904078605, 0.1849320014), (0.4937106958, 0.1575963342), (0.4936328274, 0.1300466616), (0.4935853113, 0.1132355906)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0321728054, 0.0825387042, 0.0825387042, 0.0825387042, 0.0825387042], 3)
                _nurbs_edge([(0.4613391985, 0.2563586808), (0.467513524, 0.2475405189), (0.4804895415, 0.2290081913), (0.4861522183, 0.2070809022), (0.4891204466, 0.1955871857)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0320249975, 0.06730402, 0.06730402, 0.06730402, 0.06730402], 3)
                _nurbs_edge([(0.3993274798, 0.2962942101), (0.4120514448, 0.2911189376), (0.4352790525, 0.281671474), (0.4532242767, 0.264240883), (0.4613391985, 0.2563586808)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0407402414, 0.074371341, 0.074371341, 0.074371341, 0.074371341], 3)
                _nurbs_edge([(0.2896906962, 0.3121691919), (0.3102223844, 0.3118234582), (0.347486214, 0.3111959715), (0.3832630332, 0.300911932), (0.3993274798, 0.2962942101)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0612723041, 0.1112056974, 0.1112056974, 0.1112056974, 0.1112056974], 3)
                _nurbs_edge([(0.1701321234, 0.2935656882), (0.1885706124, 0.2989873177), (0.227578126, 0.3104570364), (0.268246097, 0.3115780638), (0.2896906962, 0.3121691919)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0574078285, 0.1214490325, 0.1214490325, 0.1214490325, 0.1214490325], 3)
                _nurbs_edge([(0.0912532439, 0.2404836989), (0.1018136695, 0.2514716348), (0.1242418902, 0.2748078014), (0.1542522647, 0.2870747081), (0.1701321234, 0.2935656882)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0452093292, 0.0960155254, 0.0960155254, 0.0960155254, 0.0960155254], 3)
                _nurbs_edge([(0.0520618786, 0.1499465681), (0.0563205241, 0.1672730426), (0.0642918047, 0.1997045256), (0.0826860831, 0.2275258693), (0.0912532439, 0.2404836989)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0530555348, 0.0993087005, 0.0993087005, 0.0993087005, 0.0993087005], 3)
                Line((0.1393743386, 0.1380403019), (0.0520618786, 0.1499465681))
                _nurbs_edge([(0.1837746729, 0.2161750771), (0.1742142263, 0.2064953413), (0.1525350927, 0.1845457095), (0.1440933132, 0.1547154741), (0.1393743386, 0.1380403019)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0402021032, 0.091161721, 0.091161721, 0.091161721, 0.091161721], 3)
                _nurbs_edge([(0.276792251, 0.2382512666), (0.2581371981, 0.2379608669), (0.2253503108, 0.2374504797), (0.1962971801, 0.22258319), (0.1837746729, 0.2161750771)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0550338415, 0.0967238402, 0.0967238402, 0.0967238402, 0.0967238402], 3)
                _nurbs_edge([(0.3784916033, 0.2079895414), (0.3647054474, 0.2167902881), (0.3338664136, 0.2364771773), (0.2971146539, 0.2376195664), (0.276792251, 0.2382512666)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0482159648, 0.1078570257, 0.1078570257, 0.1078570257, 0.1078570257], 3)
                _nurbs_edge([(0.4037923445, 0.1310950495), (0.4034360678, 0.1472310175), (0.4028078676, 0.1756825573), (0.3858374438, 0.1982297383), (0.3784916033, 0.2079895414)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0469369384, 0.0827609582, 0.0827609582, 0.0827609582, 0.0827609582], 3)
                _nurbs_edge([(0.4032961954, 0.1077786065), (0.403436154, 0.1127805708), (0.4036535955, 0.1205516846), (0.4037558922, 0.1283250851), (0.4037923445, 0.1310950495)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0150114545, 0.023321982, 0.023321982, 0.023321982, 0.023321982], 3)
                _nurbs_edge([(0.2440501084, 0.0770207621), (0.2755275329, 0.0808314583), (0.3293637271, 0.0873489349), (0.381601336, 0.1017836916), (0.4032961954, 0.1077786065)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0949444173, 0.1623845079, 0.1623845079, 0.1623845079, 0.1623845079], 3)
                _nurbs_edge([(0.1646750798, 0.0636262871), (0.1756464018, 0.0660460699), (0.2018749814, 0.0718309211), (0.2285393506, 0.0751120928), (0.2440501084, 0.0770207621)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0336880427, 0.0805362838, 0.0805362838, 0.0805362838, 0.0805362838], 3)
                _nurbs_edge([(0.1004309286, 0.034356711), (0.110345824, 0.0404425099), (0.1305505332, 0.052844234), (0.1531603815, 0.0599880823), (0.1646750798, 0.0636262871)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0347597397, 0.0708338724, 0.0708338724, 0.0708338724, 0.0708338724], 3)
                _nurbs_edge([(0.054294311, -0.016988995), (0.0605456717, -0.0069005282), (0.0728623983, 0.0129762462), (0.0913344004, 0.0273020005), (0.1004309286, 0.034356711)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0352871891, 0.0695244891, 0.0695244891, 0.0695244891, 0.0695244891], 3)
                _nurbs_edge([(0.0366829266, -0.0876823687), (0.0373712455, -0.0751462787), (0.0387273607, -0.0504478681), (0.049157944, -0.0280288612), (0.054294311, -0.016988995)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0372819224, 0.0734522671, 0.0734522671, 0.0734522671, 0.0734522671], 3)
                _nurbs_edge([(0.0833156933, -0.1960788392), (0.0697151179, -0.1808187112), (0.0421557192, -0.1498964935), (0.0385229318, -0.1085993524), (0.0366829266, -0.0876823687)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0596389036, 0.1208487344, 0.1208487344, 0.1208487344, 0.1208487344], 3)
                _nurbs_edge([(0.2167650093, -0.2384948753), (0.1903419375, -0.2374373629), (0.1417587492, -0.2354929513), (0.1016227957, -0.2084251852), (0.0833156933, -0.1960788392)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0774994225, 0.1424955078, 0.1424955078, 0.1424955078, 0.1424955078], 3)
                _nurbs_edge([(0.3152396311, -0.2211315655), (0.2995140054, -0.2261953865), (0.2674941971, -0.2365061099), (0.2338737315, -0.2378241523), (0.2167650093, -0.2384948753)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0493134703, 0.1004098589, 0.1004098589, 0.1004098589, 0.1004098589], 3)
                _nurbs_edge([(0.4107375969, -0.1616003536), (0.3949920856, -0.1743713357), (0.3656110054, -0.1982019526), (0.3312065267, -0.213863256), (0.3152396311, -0.2211315655)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0605249955, 0.112939473, 0.112939473, 0.112939473, 0.112939473], 3)
                _nurbs_edge([(0.4285969366, -0.2265886091), (0.4243533478, -0.21666572), (0.4154425379, -0.1958293519), (0.4123548417, -0.1733659994), (0.4107375969, -0.1616003536)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0322252884, 0.0676675881, 0.0676675881, 0.0676675881, 0.0676675881], 3)
            make_face()
            with BuildLine():
                _nurbs_edge([(0.3889095415, -0.0842096828), (0.3930843073, -0.0718267878), (0.4028249245, -0.0429348576), (0.4031248284, -0.0123749396), (0.4032961954, 0.0050871945)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0389783226, 0.0909447241, 0.0909447241, 0.0909447241, 0.0909447241], 3)
                _nurbs_edge([(0.3298743595, -0.1459733867), (0.3423291205, -0.1378613768), (0.3668569321, -0.1218859717), (0.3816353339, -0.0966374705), (0.3889095415, -0.0842096828)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0439191242, 0.0864922267, 0.0864922267, 0.0864922267, 0.0864922267], 3)
                _nurbs_edge([(0.2380970349, -0.168545606), (0.2546083893, -0.1677215161), (0.2866819128, -0.1661207107), (0.3157637605, -0.1525553433), (0.3298743595, -0.1459733867)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0490668004, 0.0953129061, 0.0953129061, 0.0953129061, 0.0953129061], 3)
                _nurbs_edge([(0.1589700808, -0.1447331332), (0.1697573798, -0.1516602894), (0.1937370054, -0.1670590109), (0.2223536595, -0.1680180134), (0.2380970349, -0.168545606)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.037787097, 0.083998825, 0.083998825, 0.083998825, 0.083998825], 3)
                _nurbs_edge([(0.1319329371, -0.0852018618), (0.1330705287, -0.0966217846), (0.1353513528, -0.1195182578), (0.1510842013, -0.1363143281), (0.1589700808, -0.1447331332)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0334325911, 0.0670309627, 0.0670309627, 0.0670309627, 0.0670309627], 3)
                _nurbs_edge([(0.1443352331, -0.0427858852), (0.1407179669, -0.0493522193), (0.1334377629, -0.0625677937), (0.1324366391, -0.0776256844), (0.1319329371, -0.0852018618)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0221967882, 0.0446738325, 0.0446738325, 0.0446738325, 0.0446738325], 3)
                _nurbs_edge([(0.1795578827, -0.0137643837), (0.1724368967, -0.0173757223), (0.1585234719, -0.0244317802), (0.1489896028, -0.0367649272), (0.1443352331, -0.0427858852)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0236202296, 0.0461506723, 0.0461506723, 0.0461506723, 0.0461506723], 3)
                _nurbs_edge([(0.2574447026, 0.004094956), (0.2416441806, 0.001831401), (0.2151606566, -0.0019625821), (0.1897914059, -0.0103721196), (0.1795578827, -0.0137643837)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0477555179, 0.0800438371, 0.0800438371, 0.0800438371, 0.0800438371], 3)
                _nurbs_edge([(0.4032961954, 0.0378293968), (0.3831589825, 0.0312124784), (0.3355964137, 0.0155838193), (0.286027151, 0.0082967814), (0.2574447026, 0.004094956)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0634829148, 0.1499418273, 0.1499418273, 0.1499418273, 0.1499418273], 3)
                Line((0.4032961954, 0.0050871945), (0.4032961954, 0.0378293968))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1131435141, perimeter: 2.8993037276
            with BuildLine():
                _nurbs_edge([(-0.31405542, -0.4198170923), (-0.3250550445, -0.4258195335), (-0.3479199032, -0.4382967747), (-0.3739628696, -0.439684752), (-0.3874773155, -0.4404050135)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0371002848, 0.0771201573, 0.0771201573, 0.0771201573, 0.0771201573], 3)
                _nurbs_edge([(-0.2594851027, -0.3550769114), (-0.2672428386, -0.3684825889), (-0.2816249642, -0.3933354765), (-0.3038284988, -0.4114661336), (-0.31405542, -0.4198170923)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0460072011, 0.0852930999, 0.0852930999, 0.0852930999, 0.0852930999], 3)
                _nurbs_edge([(-0.2093797098, -0.2355183386), (-0.2184781214, -0.2601435853), (-0.2334720975, -0.3007254335), (-0.2521435651, -0.3397375294), (-0.2594851027, -0.3550769114)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0786977933, 0.1296921789, 0.1296921789, 0.1296921789, 0.1296921789], 3)
                Line((-0.0089577804, 0.3002629853), (-0.2093797098, -0.2355183386))
                Line((-0.0982545982, 0.3002629853), (-0.0089577804, 0.3002629853))
                Line((-0.2108679186, -0.0068190717), (-0.0982545982, 0.3002629853))
                _nurbs_edge([(-0.2475788961, -0.1268737935), (-0.242220335, -0.1065359311), (-0.2315501585, -0.0660383841), (-0.2177417475, -0.0265008579), (-0.2108679186, -0.0068190717)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0630687887, 0.1255850391, 0.1255850391, 0.1255850391, 0.1255850391], 3)
                _nurbs_edge([(-0.2857780824, -0.0048347138), (-0.2788073843, -0.0246057212), (-0.2646250394, -0.0648311389), (-0.2533249376, -0.1059599914), (-0.2475788961, -0.1268737935)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.062870114, 0.1279133914, 0.1279133914, 0.1279133914, 0.1279133914], 3)
                Line((-0.3954148064, 0.3002629853), (-0.2857780824, -0.0048347138))
                Line((-0.4916569958, 0.3002629853), (-0.3954148064, 0.3002629853))
                Line((-0.2917312155, -0.227580788), (-0.4916569958, 0.3002629853))
                _nurbs_edge([(-0.2996687065, -0.2494089626), (-0.2986058035, -0.2463453635), (-0.2960678588, -0.2390302601), (-0.2933252229, -0.2317892371), (-0.2917312155, -0.227580788)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0097278057, 0.0232275506, 0.0232275506, 0.0232275506, 0.0232275506], 3)
                _nurbs_edge([(-0.3269538651, -0.3158855461), (-0.3231579202, -0.3081628529), (-0.3125760667, -0.2866345086), (-0.3047118529, -0.2639536778), (-0.2996687065, -0.2494089626)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.025797169, 0.0719140747, 0.0719140747, 0.0719140747, 0.0719140747], 3)
                _nurbs_edge([(-0.3562233816, -0.3436667942), (-0.3505211401, -0.3400006878), (-0.3390061716, -0.3325974412), (-0.3309969167, -0.3214916974), (-0.3269538651, -0.3158855461)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0201426237, 0.0406755265, 0.0406755265, 0.0406755265, 0.0406755265], 3)
                _nurbs_edge([(-0.4038483868, -0.3535885834), (-0.394785833, -0.353362495), (-0.3782704624, -0.3529504771), (-0.3630788375, -0.3465535201), (-0.3562233816, -0.3436667942)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0269036531, 0.0490285415, 0.0490285415, 0.0490285415, 0.0490285415], 3)
                _nurbs_edge([(-0.4549460779, -0.345651152), (-0.4458584957, -0.3479613254), (-0.4290689965, -0.3522294193), (-0.4117796164, -0.3531611614), (-0.4038483868, -0.3535885834)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0280482282, 0.0518196917, 0.0518196917, 0.0518196917, 0.0518196917], 3)
                Line((-0.4450241695, -0.4294909262), (-0.4549460779, -0.345651152))
                _nurbs_edge([(-0.3874773155, -0.4404050135), (-0.3966357404, -0.4398401343), (-0.4162645445, -0.4386294563), (-0.4350197725, -0.4326698787), (-0.4450241695, -0.4294909262)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0274211804, 0.058770475, 0.058770475, 0.058770475, 0.058770475], 3)
            make_face()
            # Profile area: 0.1109777183, perimeter: 2.7738482819
            with BuildLine():
                Line((0.7212922205, 0.0611457802), (0.7212922205, -0.2265886091))
                _nurbs_edge([(0.7627160181, 0.1985637523), (0.750717445, 0.1816353816), (0.7218764957, 0.1409446865), (0.7215076291, 0.090565775), (0.7212922205, 0.0611457802)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0609710134, 0.1465559192, 0.1465559192, 0.1465559192, 0.1465559192], 3)
                _nurbs_edge([(0.8611907591, 0.2347785808), (0.8428953636, 0.2333307284), (0.8066658556, 0.2304636147), (0.7772682457, 0.2091261134), (0.7627160181, 0.1985637523)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0539096654, 0.1067547652, 0.1067547652, 0.1067547652, 0.1067547652], 3)
                _nurbs_edge([(0.9234504332, 0.2186555542), (0.9140158666, 0.2233563323), (0.8944230642, 0.2331184572), (0.8725376436, 0.2342117459), (0.8611907591, 0.2347785808)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.031268149, 0.0649346913, 0.0649346913, 0.0649346913, 0.0649346913], 3)
                _nurbs_edge([(0.9604096045, 0.1754953838), (0.9561845902, 0.184101306), (0.9475727715, 0.2016427), (0.9315912938, 0.2129140181), (0.9234504332, 0.2186555542)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0282785752, 0.0576400323, 0.0576400323, 0.0576400323, 0.0576400323], 3)
                _nurbs_edge([(0.9708275427, 0.0938879229), (0.9707417602, 0.1098942446), (0.9705934548, 0.1375668308), (0.9634297103, 0.1642473549), (0.9604096045, 0.1754953838)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0477581242, 0.0825668026, 0.0825668026, 0.0825668026, 0.0825668026], 3)
                Line((0.9708275427, -0.2265886091), (0.9708275427, 0.0938879229))
                Line((1.0601243605, -0.2265886091), (0.9708275427, -0.2265886091))
                Line((1.0601243605, 0.0973606087), (1.0601243605, -0.2265886091))
                _nurbs_edge([(1.0551633467, 0.1841770388), (1.0565950321, 0.1728208787), (1.0602268771, 0.144013005), (1.0601630355, 0.114960512), (1.0601243605, 0.0973606087)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0343088461, 0.0870333726, 0.0870333726, 0.0870333726, 0.0870333726], 3)
                _nurbs_edge([(1.0273820986, 0.250157503), (1.0335419341, 0.2402575092), (1.0463006512, 0.2197518935), (1.0521421105, 0.1963042792), (1.0551633467, 0.1841770388)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0347533288, 0.0719837225, 0.0719837225, 0.0719837225, 0.0719837225], 3)
                _nurbs_edge([(0.9676029314, 0.2950539566), (0.9798322697, 0.2892339146), (1.0028328164, 0.2782877665), (1.0195523179, 0.2591294066), (1.0273820986, 0.250157503)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.040127163, 0.0754698796, 0.0754698796, 0.0754698796, 0.0754698796], 3)
                _nurbs_edge([(0.8800422777, 0.3121691919), (0.8954315373, 0.3115259548), (0.9254991164, 0.3102691962), (0.9537913136, 0.3000451213), (0.9676029314, 0.2950539566)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0459025556, 0.0896845437, 0.0896845437, 0.0896845437, 0.0896845437], 3)
                _nurbs_edge([(0.7123626103, 0.2253528214), (0.7341197233, 0.2506727533), (0.7782780137, 0.3020621495), (0.8457926149, 0.3087675774), (0.8800422777, 0.3121691919)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0962926935, 0.1954358886, 0.1954358886, 0.1954358886, 0.1954358886], 3)
                Line((0.7123626103, 0.3002629853), (0.7123626103, 0.2253528214))
                Line((0.6319954027, 0.3002629853), (0.7123626103, 0.3002629853))
                Line((0.6319954027, -0.2265886091), (0.6319954027, 0.3002629853))
                Line((0.7212922205, -0.2265886091), (0.6319954027, -0.2265886091))
            make_face()
        # OneSide extrude, distance=-3.556
        extrude(amount=-3.556, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a mounting bracket or support base with a rectangular foundation block featuring angular geometric surfaces and a cylindrical curved loop or clamp mechanism extending upward from the top, designed to hold or secure a round component.
def model_143346_3ed36a3d_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 60, perimeter: 32
            with BuildLine():
                Line((10, -6), (0, -6))
                Line((10, 0), (10, -6))
                Line((0, 0), (10, 0))
                Line((0, -6), (0, 0))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 20, perimeter: 24
            with BuildLine():
                Line((-10, 2), (0, 2))
                Line((-10, 0), (-10, 2))
                Line((0, 0), (-10, 0))
                Line((0, 2), (0, 0))
            make_face()
        # OneSide extrude, distance=2.5
        extrude(amount=2.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 9.8174770425, perimeter: 12.853981634
            with BuildLine():
                CenterArc((5, 4.5), 2.5, -90, 90)
                Line((7.5, 4.5), (2.5, 4.5))
                CenterArc((5, 4.5), 2.5, 180, 90)
            make_face()
            # Profile area: 9.8174770425, perimeter: 12.853981634
            with BuildLine():
                CenterArc((5, 4.5), 2.5, 0, 180)
                Line((7.5, 4.5), (2.5, 4.5))
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            with Locations((5, 4.5)):
                Circle(2)
        # OneSide extrude, distance=-2.6201
        extrude(amount=-2.6201, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a flat metal bar or trim piece with a parallelogram shape, featuring a brushed or striated surface texture and beveled edges along its perimeter.
def model_144142_88858328_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch14 -> Extrude11 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.5673917111, perimeter: 8.8600988548
            with BuildLine():
                CenterArc((9.6235460163, -1.9579730675), 2.8884435629, 137.323015584, 8.217330687)
                Line((7.2477362081, -0.4759783248), (7.2419525684, -0.3236172723))
                Line((7.7522737159, -0.3236172723), (7.2477362081, -0.4759783248))
                CenterArc((11.5, -21.8625234979), 21.8625234979, 90, 9.8705307922)
                Line((11.4000001699, 0), (11.5, 0))
                Line((7.5, 0), (11.4000001699, 0))
            make_face()
            # Profile area: 1.565087677, perimeter: 9.3949888688
            with BuildLine():
                CenterArc((10.9834237582, -11.6173900654), 12.1283961434, 87.558902737, 19.1322272239)
                Line((7.5, 0), (11.4000001699, 0))
                Line((11.7304089152, 0.2547536533), (11.4000001699, 0))
                Line((12.0534331558, 0.5859652762), (11.7304089152, 0.2547536533))
                Line((11.8964260966, 0.5285101215), (12.0534331558, 0.5859652762))
                Line((11.7304089152, 0.5087463438), (11.8964260966, 0.5285101215))
                CenterArc((11.5610285468, 1.9315538489), 1.4328541118, -92.441097263, 9.2300131707)
            make_face()
        # OneSide extrude, distance=23
        extrude(amount=23)
    return part.part


# Description: This is a hexahedron or irregular polyhedron with a hollow rectangular chamber running through its center, featuring six quadrilateral faces with two larger rectangular openings on opposite ends and tapered or angled side walls.
def model_144225_66a62553_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 600, perimeter: 100
            with BuildLine():
                Line((15, -10), (-15, -10))
                Line((15, 10), (15, -10))
                Line((-15, 10), (15, 10))
                Line((-15, -10), (-15, 10))
            make_face()
        # OneSide extrude, distance=10
        extrude(amount=10)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 10), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 551, perimeter: 96
            with BuildLine():
                Line((-14.5, 9.5), (14.5, 9.5))
                Line((-14.5, -9.5), (-14.5, 9.5))
                Line((14.5, -9.5), (-14.5, -9.5))
                Line((14.5, 9.5), (14.5, -9.5))
            make_face()
        # OneSide extrude, distance=-9
        extrude(amount=-9, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 10), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 14.5, perimeter: 59
            with BuildLine():
                Line((-14.5, -10), (-14.5, -9.5))
                Line((14.5, -10), (-14.5, -10))
                Line((14.5, -9.5), (14.5, -10))
                Line((-14.5, -9.5), (14.5, -9.5))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 10), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 14.5, perimeter: 59
            with BuildLine():
                Line((-14.5, 9.5), (-14.5, 10))
                Line((14.5, 9.5), (-14.5, 9.5))
                Line((14.5, 10), (14.5, 9.5))
                Line((-14.5, 10), (14.5, 10))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a dual-chamber speaker or acoustic enclosure assembly featuring two rectangular, angled boxes mounted on a common base platform with support legs and internal bracing elements.
def model_144279_136348c1_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 70 constraints, 17 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3906961121, perimeter: 3.6479343253
            with BuildLine():
                CenterArc((0.1524, -0.1524), 0.1524, 90, 90)
                Line((0, -0.4826), (0, -0.1524))
                CenterArc((0.1524, -0.4826), 0.1524, 180, 90)
                Line((0.7556499762, -0.635), (0.1524, -0.635))
                Line((0.7556499762, 0), (0.7556499762, -0.635))
                Line((0.1524, 0), (0.7556499762, 0))
            make_face()
            with BuildLine():
                CenterArc((0.3174999952, -0.3175), 0.1587499976, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3175
        extrude(amount=0.3175)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 70 constraints, 17 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2206447245, perimeter: 2.3876000143
            with BuildLine():
                Line((0.7556499762, 0), (0.7556499762, -0.635))
                Line((0.7556499762, -0.635), (1.1112499833, -0.635))
                Line((1.1112499833, -0.635), (1.1112499833, 0))
                Line((1.1112499833, 0), (0.7556499762, 0))
            make_face()
            with BuildLine():
                Line((0.9524999762, -0.4191), (0.9524999762, -0.4699))
                Line((0.9524999762, -0.4699), (0.9016999762, -0.4699))
                Line((0.9016999762, -0.4699), (0.9016999762, -0.4191))
                Line((0.9016999762, -0.4191), (0.9524999762, -0.4191))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((0.9524999762, -0.1651), (0.9524999762, -0.2159))
                Line((0.9524999762, -0.2159), (0.9016999762, -0.2159))
                Line((0.9016999762, -0.2159), (0.9016999762, -0.1651))
                Line((0.9016999762, -0.1651), (0.9524999762, -0.1651))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2206447245, perimeter: 2.3876000143
            with BuildLine():
                Line((2.063749969, 0), (2.063749969, -0.635))
                Line((2.063749969, -0.635), (2.4193499762, -0.635))
                Line((2.4193499762, -0.635), (2.4193499762, 0))
                Line((2.4193499762, 0), (2.063749969, 0))
            make_face()
            with BuildLine():
                Line((2.2732999762, -0.2159), (2.2224999762, -0.2159))
                Line((2.2224999762, -0.2159), (2.2224999762, -0.1651))
                Line((2.2224999762, -0.1651), (2.2732999762, -0.1651))
                Line((2.2732999762, -0.1651), (2.2732999762, -0.2159))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((2.2732999762, -0.4699), (2.2224999762, -0.4699))
                Line((2.2224999762, -0.4699), (2.2224999762, -0.4191))
                Line((2.2224999762, -0.4191), (2.2732999762, -0.4191))
                Line((2.2732999762, -0.4191), (2.2732999762, -0.4699))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.3906961424, perimeter: 3.6479344206
            with BuildLine():
                Line((2.4193499762, -0.635), (2.4193499762, 0))
                Line((3.0226, -0.635), (2.4193499762, -0.635))
                CenterArc((3.0226, -0.4826), 0.1524, -90, 90)
                Line((3.175, -0.1524), (3.175, -0.4826))
                CenterArc((3.0226, -0.1524), 0.1524, 0, 90)
                Line((2.4193499762, 0), (3.0226, 0))
            make_face()
            with BuildLine():
                CenterArc((2.8574999571, -0.3175), 0.1587499976, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.5921698039, perimeter: 3.5739822384
            with BuildLine():
                Line((1.1112499833, -0.635), (1.1112499833, 0))
                Line((2.063749969, -0.635), (1.1112499833, -0.635))
                Line((2.063749969, 0), (2.063749969, -0.635))
                Line((1.1112499833, 0), (2.063749969, 0))
            make_face()
            with BuildLine():
                CenterArc((1.5874999762, -0.3175), 0.0635, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.012667687, perimeter: 0.398982267
            with Locations((1.5874999762, -0.3175)):
                Circle(0.0635)
            # Profile area: 0.00258064, perimeter: 0.2032
            with BuildLine():
                Line((0.9016999762, -0.4191), (0.9524999762, -0.4191))
                Line((0.9016999762, -0.4699), (0.9016999762, -0.4191))
                Line((0.9524999762, -0.4699), (0.9016999762, -0.4699))
                Line((0.9524999762, -0.4191), (0.9524999762, -0.4699))
            make_face()
            # Profile area: 0.00258064, perimeter: 0.2032
            with BuildLine():
                Line((0.9016999762, -0.1651), (0.9524999762, -0.1651))
                Line((0.9016999762, -0.2159), (0.9016999762, -0.1651))
                Line((0.9524999762, -0.2159), (0.9016999762, -0.2159))
                Line((0.9524999762, -0.1651), (0.9524999762, -0.2159))
            make_face()
            # Profile area: 0.00258064, perimeter: 0.2032
            with BuildLine():
                Line((2.2732999762, -0.1651), (2.2732999762, -0.2159))
                Line((2.2224999762, -0.1651), (2.2732999762, -0.1651))
                Line((2.2224999762, -0.2159), (2.2224999762, -0.1651))
                Line((2.2732999762, -0.2159), (2.2224999762, -0.2159))
            make_face()
            # Profile area: 0.00258064, perimeter: 0.2032
            with BuildLine():
                Line((2.2732999762, -0.4191), (2.2732999762, -0.4699))
                Line((2.2224999762, -0.4191), (2.2732999762, -0.4191))
                Line((2.2224999762, -0.4699), (2.2224999762, -0.4191))
                Line((2.2732999762, -0.4699), (2.2224999762, -0.4699))
            make_face()
        # OneSide extrude, distance=0.3175
        extrude(amount=0.3175, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 70 constraints, 17 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2206447245, perimeter: 2.3876000143
            with BuildLine():
                Line((0.7556499762, 0), (0.7556499762, -0.635))
                Line((0.7556499762, -0.635), (1.1112499833, -0.635))
                Line((1.1112499833, -0.635), (1.1112499833, 0))
                Line((1.1112499833, 0), (0.7556499762, 0))
            make_face()
            with BuildLine():
                Line((0.9524999762, -0.4191), (0.9524999762, -0.4699))
                Line((0.9524999762, -0.4699), (0.9016999762, -0.4699))
                Line((0.9016999762, -0.4699), (0.9016999762, -0.4191))
                Line((0.9016999762, -0.4191), (0.9524999762, -0.4191))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((0.9524999762, -0.1651), (0.9524999762, -0.2159))
                Line((0.9524999762, -0.2159), (0.9016999762, -0.2159))
                Line((0.9016999762, -0.2159), (0.9016999762, -0.1651))
                Line((0.9016999762, -0.1651), (0.9524999762, -0.1651))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2206447245, perimeter: 2.3876000143
            with BuildLine():
                Line((2.063749969, 0), (2.063749969, -0.635))
                Line((2.063749969, -0.635), (2.4193499762, -0.635))
                Line((2.4193499762, -0.635), (2.4193499762, 0))
                Line((2.4193499762, 0), (2.063749969, 0))
            make_face()
            with BuildLine():
                Line((2.2732999762, -0.2159), (2.2224999762, -0.2159))
                Line((2.2224999762, -0.2159), (2.2224999762, -0.1651))
                Line((2.2224999762, -0.1651), (2.2732999762, -0.1651))
                Line((2.2732999762, -0.1651), (2.2732999762, -0.2159))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((2.2732999762, -0.4699), (2.2224999762, -0.4699))
                Line((2.2224999762, -0.4699), (2.2224999762, -0.4191))
                Line((2.2224999762, -0.4191), (2.2732999762, -0.4191))
                Line((2.2732999762, -0.4191), (2.2732999762, -0.4699))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.00258064, perimeter: 0.2032
            with BuildLine():
                Line((0.9016999762, -0.4191), (0.9524999762, -0.4191))
                Line((0.9016999762, -0.4699), (0.9016999762, -0.4191))
                Line((0.9524999762, -0.4699), (0.9016999762, -0.4699))
                Line((0.9524999762, -0.4191), (0.9524999762, -0.4699))
            make_face()
            # Profile area: 0.00258064, perimeter: 0.2032
            with BuildLine():
                Line((0.9016999762, -0.1651), (0.9524999762, -0.1651))
                Line((0.9016999762, -0.2159), (0.9016999762, -0.1651))
                Line((0.9524999762, -0.2159), (0.9016999762, -0.2159))
                Line((0.9524999762, -0.1651), (0.9524999762, -0.2159))
            make_face()
            # Profile area: 0.00258064, perimeter: 0.2032
            with BuildLine():
                Line((2.2732999762, -0.1651), (2.2732999762, -0.2159))
                Line((2.2224999762, -0.1651), (2.2732999762, -0.1651))
                Line((2.2224999762, -0.2159), (2.2224999762, -0.1651))
                Line((2.2732999762, -0.2159), (2.2224999762, -0.2159))
            make_face()
            # Profile area: 0.00258064, perimeter: 0.2032
            with BuildLine():
                Line((2.2732999762, -0.4191), (2.2732999762, -0.4699))
                Line((2.2224999762, -0.4191), (2.2732999762, -0.4191))
                Line((2.2224999762, -0.4699), (2.2224999762, -0.4191))
                Line((2.2732999762, -0.4699), (2.2224999762, -0.4699))
            make_face()
        # OneSide extrude, distance=1.4097
        extrude(amount=1.4097, mode=Mode.SUBTRACT)

        # Sketch1 -> Extrude4 (Join)
        # Sketch on XZ construction plane
        # Sketch has 70 constraints, 17 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2206447245, perimeter: 2.3876000143
            with BuildLine():
                Line((0.7556499762, 0), (0.7556499762, -0.635))
                Line((0.7556499762, -0.635), (1.1112499833, -0.635))
                Line((1.1112499833, -0.635), (1.1112499833, 0))
                Line((1.1112499833, 0), (0.7556499762, 0))
            make_face()
            with BuildLine():
                Line((0.9524999762, -0.4191), (0.9524999762, -0.4699))
                Line((0.9524999762, -0.4699), (0.9016999762, -0.4699))
                Line((0.9016999762, -0.4699), (0.9016999762, -0.4191))
                Line((0.9016999762, -0.4191), (0.9524999762, -0.4191))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((0.9524999762, -0.1651), (0.9524999762, -0.2159))
                Line((0.9524999762, -0.2159), (0.9016999762, -0.2159))
                Line((0.9016999762, -0.2159), (0.9016999762, -0.1651))
                Line((0.9016999762, -0.1651), (0.9524999762, -0.1651))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2206447245, perimeter: 2.3876000143
            with BuildLine():
                Line((2.063749969, 0), (2.063749969, -0.635))
                Line((2.063749969, -0.635), (2.4193499762, -0.635))
                Line((2.4193499762, -0.635), (2.4193499762, 0))
                Line((2.4193499762, 0), (2.063749969, 0))
            make_face()
            with BuildLine():
                Line((2.2732999762, -0.2159), (2.2224999762, -0.2159))
                Line((2.2224999762, -0.2159), (2.2224999762, -0.1651))
                Line((2.2224999762, -0.1651), (2.2732999762, -0.1651))
                Line((2.2732999762, -0.1651), (2.2732999762, -0.2159))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((2.2732999762, -0.4699), (2.2224999762, -0.4699))
                Line((2.2224999762, -0.4699), (2.2224999762, -0.4191))
                Line((2.2224999762, -0.4191), (2.2732999762, -0.4191))
                Line((2.2732999762, -0.4191), (2.2732999762, -0.4699))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.00258064, perimeter: 0.2032
            with BuildLine():
                Line((0.9016999762, -0.4191), (0.9524999762, -0.4191))
                Line((0.9016999762, -0.4699), (0.9016999762, -0.4191))
                Line((0.9524999762, -0.4699), (0.9016999762, -0.4699))
                Line((0.9524999762, -0.4191), (0.9524999762, -0.4699))
            make_face()
            # Profile area: 0.00258064, perimeter: 0.2032
            with BuildLine():
                Line((0.9016999762, -0.1651), (0.9524999762, -0.1651))
                Line((0.9016999762, -0.2159), (0.9016999762, -0.1651))
                Line((0.9524999762, -0.2159), (0.9016999762, -0.2159))
                Line((0.9524999762, -0.1651), (0.9524999762, -0.2159))
            make_face()
            # Profile area: 0.00258064, perimeter: 0.2032
            with BuildLine():
                Line((2.2732999762, -0.1651), (2.2732999762, -0.2159))
                Line((2.2224999762, -0.1651), (2.2732999762, -0.1651))
                Line((2.2224999762, -0.2159), (2.2224999762, -0.1651))
                Line((2.2732999762, -0.2159), (2.2224999762, -0.2159))
            make_face()
            # Profile area: 0.00258064, perimeter: 0.2032
            with BuildLine():
                Line((2.2732999762, -0.4191), (2.2732999762, -0.4699))
                Line((2.2224999762, -0.4191), (2.2732999762, -0.4191))
                Line((2.2224999762, -0.4699), (2.2224999762, -0.4191))
                Line((2.2732999762, -0.4699), (2.2224999762, -0.4699))
            make_face()
        # OneSide extrude, distance=1.4097
        extrude(amount=1.4097, mode=Mode.ADD)

        # Sketch1 -> Extrude5 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 70 constraints, 17 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.012667687, perimeter: 0.398982267
            with Locations((1.5874999762, -0.3175)):
                Circle(0.0635)
        # OneSide extrude, distance=0.254
        extrude(amount=0.254, mode=Mode.SUBTRACT)

        # Sketch1 -> Extrude6 (Join)
        # Sketch on XZ construction plane
        # Sketch has 70 constraints, 17 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.00258064, perimeter: 0.2032
            with BuildLine():
                Line((2.2732999762, -0.4191), (2.2732999762, -0.4699))
                Line((2.2224999762, -0.4191), (2.2732999762, -0.4191))
                Line((2.2224999762, -0.4699), (2.2224999762, -0.4191))
                Line((2.2732999762, -0.4699), (2.2224999762, -0.4699))
            make_face()
            # Profile area: 0.00258064, perimeter: 0.2032
            with BuildLine():
                Line((2.2732999762, -0.1651), (2.2732999762, -0.2159))
                Line((2.2224999762, -0.1651), (2.2732999762, -0.1651))
                Line((2.2224999762, -0.2159), (2.2224999762, -0.1651))
                Line((2.2732999762, -0.2159), (2.2224999762, -0.2159))
            make_face()
            # Profile area: 0.00258064, perimeter: 0.2032
            with BuildLine():
                Line((0.9016999762, -0.4191), (0.9524999762, -0.4191))
                Line((0.9016999762, -0.4699), (0.9016999762, -0.4191))
                Line((0.9524999762, -0.4699), (0.9016999762, -0.4699))
                Line((0.9524999762, -0.4191), (0.9524999762, -0.4699))
            make_face()
            # Profile area: 0.00258064, perimeter: 0.2032
            with BuildLine():
                Line((0.9016999762, -0.1651), (0.9524999762, -0.1651))
                Line((0.9016999762, -0.2159), (0.9016999762, -0.1651))
                Line((0.9524999762, -0.2159), (0.9016999762, -0.2159))
                Line((0.9524999762, -0.1651), (0.9524999762, -0.2159))
            make_face()
        # OneSide extrude, distance=-0.254
        extrude(amount=-0.254, mode=Mode.ADD)

        # Sketch1 -> Extrude7 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 70 constraints, 17 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2206447245, perimeter: 2.3876000143
            with BuildLine():
                Line((0.7556499762, 0), (0.7556499762, -0.635))
                Line((0.7556499762, -0.635), (1.1112499833, -0.635))
                Line((1.1112499833, -0.635), (1.1112499833, 0))
                Line((1.1112499833, 0), (0.7556499762, 0))
            make_face()
            with BuildLine():
                Line((0.9524999762, -0.4191), (0.9524999762, -0.4699))
                Line((0.9524999762, -0.4699), (0.9016999762, -0.4699))
                Line((0.9016999762, -0.4699), (0.9016999762, -0.4191))
                Line((0.9016999762, -0.4191), (0.9524999762, -0.4191))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((0.9524999762, -0.1651), (0.9524999762, -0.2159))
                Line((0.9524999762, -0.2159), (0.9016999762, -0.2159))
                Line((0.9016999762, -0.2159), (0.9016999762, -0.1651))
                Line((0.9016999762, -0.1651), (0.9524999762, -0.1651))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.5921698039, perimeter: 3.5739822384
            with BuildLine():
                Line((1.1112499833, -0.635), (1.1112499833, 0))
                Line((2.063749969, -0.635), (1.1112499833, -0.635))
                Line((2.063749969, 0), (2.063749969, -0.635))
                Line((1.1112499833, 0), (2.063749969, 0))
            make_face()
            with BuildLine():
                CenterArc((1.5874999762, -0.3175), 0.0635, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2206447245, perimeter: 2.3876000143
            with BuildLine():
                Line((2.063749969, 0), (2.063749969, -0.635))
                Line((2.063749969, -0.635), (2.4193499762, -0.635))
                Line((2.4193499762, -0.635), (2.4193499762, 0))
                Line((2.4193499762, 0), (2.063749969, 0))
            make_face()
            with BuildLine():
                Line((2.2732999762, -0.2159), (2.2224999762, -0.2159))
                Line((2.2224999762, -0.2159), (2.2224999762, -0.1651))
                Line((2.2224999762, -0.1651), (2.2732999762, -0.1651))
                Line((2.2732999762, -0.1651), (2.2732999762, -0.2159))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((2.2732999762, -0.4699), (2.2224999762, -0.4699))
                Line((2.2224999762, -0.4699), (2.2224999762, -0.4191))
                Line((2.2224999762, -0.4191), (2.2732999762, -0.4191))
                Line((2.2732999762, -0.4191), (2.2732999762, -0.4699))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.0381
        extrude(amount=0.0381, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a rectangular prism or box-shaped component with cylindrical flanges or mounting bosses protruding from both ends, featuring an internal truss or ribbed structure visible through the blue-shaded surfaces.
def model_144433_e54699d3_0000():
    """Model: box (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 28.22, perimeter: 23.4
            with BuildLine():
                Line((4.15, -1.7), (-4.15, -1.7))
                Line((4.15, 1.7), (4.15, -1.7))
                Line((-4.15, 1.7), (4.15, 1.7))
                Line((-4.15, -1.7), (-4.15, 1.7))
            make_face()
        # OneSide extrude, distance=3.8
        extrude(amount=3.8)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3.8), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 19.5, perimeter: 20.2
            with BuildLine():
                Line((3.75, -1.3), (3.75, 1.3))
                Line((3.75, 1.3), (-3.75, 1.3))
                Line((-3.75, 1.3), (-3.75, -1.3))
                Line((-3.75, -1.3), (3.75, -1.3))
            make_face()
        # OneSide extrude, distance=-3.4
        extrude(amount=-3.4, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-4.15, 0, 0), x_dir=(0, -1, 0), z_dir=(-1, 0, 0))) as sk:
            # Profile area: 6.157521601, perimeter: 8.7964594301
            with Locations((0, 1.6)):
                Circle(1.4)
        # TwoSides extrude, along=1.8, against=-0.4
        extrude(amount=1.8, mode=Mode.ADD)
        extrude(sk.sketch, amount=-0.4, mode=Mode.ADD)

        # Sketch7 -> Extrude7 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3.8), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.5872298071, perimeter: 2.8988283119
            with BuildLine():
                CenterArc((-4.35, 0), 0.5, 66.4218215218, 227.1563569564)
                Line((-4.15, 0.4582575695), (-4.15, -0.4582575695))
            make_face()
        # OneSide extrude, distance=-2.1
        extrude(amount=-2.1, mode=Mode.ADD)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-5.95, 0, 0), x_dir=(0, -1, 0), z_dir=(-1, 0, 0))):
            # Profile area: 3.8013271108, perimeter: 6.9115038379
            with Locations((0, 1.6)):
                Circle(1.1)
        # OneSide extrude, distance=-4.1
        extrude(amount=-4.1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a flat rectangular frame or mounting bracket with a parallelogram shape, featuring a hollow center and beveled or angled edges on all sides, creating a shallow tray-like structure with a recessed interior.
def model_144648_0fd6ca79_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 10307.5, perimeter: 421
            with BuildLine():
                Line((66.5, -38.75), (66.5, 38.75))
                Line((66.5, 38.75), (-66.5, 38.75))
                Line((-66.5, 38.75), (-66.5, -38.75))
                Line((-66.5, -38.75), (66.5, -38.75))
            make_face()
        # OneSide extrude, distance=7.7
        extrude(amount=7.7)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 8687.5, perimeter: 389
            with BuildLine():
                Line((62.5, 34.75), (-62.5, 34.75))
                Line((-62.5, 34.75), (-62.5, -34.75))
                Line((-62.5, -34.75), (62.5, -34.75))
                Line((62.5, -34.75), (62.5, 34.75))
            make_face()
        # OneSide extrude, distance=-70
        extrude(amount=-70, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 38.75), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 492.1, perimeter: 273.4
            with BuildLine():
                Line((-66.5, -4), (66.5, -4))
                Line((-66.5, -7.7), (-66.5, -4))
                Line((66.5, -7.7), (-66.5, -7.7))
                Line((66.5, -4), (66.5, -7.7))
            make_face()
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 12 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-66.5, 0, 0), x_dir=(0, -1, 0), z_dir=(-1, 0, 0))):
            # Profile area: 30.8, perimeter: 23.4
            with BuildLine():
                Line((0, 42.75), (0, 38.75))
                Line((-7.7, 42.75), (0, 42.75))
                Line((-7.7, 38.75), (-7.7, 42.75))
                Line((0, 38.75), (-7.7, 38.75))
            make_face()
            # Profile area: 30.8, perimeter: 23.4
            with BuildLine():
                Line((-7.7, -38.75), (0, -38.75))
                Line((-7.7, -42.75), (-7.7, -38.75))
                Line((0, -42.75), (-7.7, -42.75))
                Line((0, -38.75), (0, -42.75))
            make_face()
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4, mode=Mode.ADD)
    return part.part


# Description: This is a drive belt or serpentine belt featuring a long, flat rectangular body with multiple parallel grooves running along its length and two curved, raised flanges or edges on opposite ends that form a loop shape.
def model_144709_642fc665_0001():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 24.7744792076, perimeter: 47.6730788822
            with BuildLine():
                CenterArc((0, 0), 3.005, -105.6520109426, 210.9870569279)
                Line((-7.7701562375, 0.985156944), (-0.7947112829, 2.8980094853))
                CenterArc((-7.5056932482, 0.0207611087), 1, 105.3350459853, 149.0129430721)
                Line((-0.8107310669, -2.8935687545), (-7.7754872805, -0.9421569461))
            make_face()
            with BuildLine():
                CenterArc((-7.5056932482, 0.0207611087), 0.505, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0), 2.605, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.6053538094, perimeter: 32.107076188
            with BuildLine():
                CenterArc((0, 0), 2.6049999418, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.5049999418, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.7278303226, perimeter: 35.7974831413
            with BuildLine():
                Line((3.5754609763, -0.0098898971), (3.5760141838, 0.1901093378))
                Line((3.5760141838, 0.1901093378), (2.8571136939, 0.1920978512))
                CenterArc((0, 0), 2.8635642553, 3.8464888706, 351.9900573014)
                Line((3.5749077688, -0.209889132), (2.8560072789, -0.2079006186))
                Line((3.5754609763, -0.0098898971), (3.5749077688, -0.209889132))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.605, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6, mode=Mode.ADD)
    return part.part


# Description: This is a bracket or support arm assembly with a horizontal main beam featuring a blue metallic top surface, two vertical flanges at each end with mounting holes, and a diagonal brace member extending downward to provide structural reinforcement.
def model_144780_918f74e1_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 105.3205313116, perimeter: 112.6789140795
            with BuildLine():
                Line((21.55, -2), (35, -2))
                Line((35, -2), (35, 0))
                Line((21.55, 0), (35, 0))
                Line((21.55, 0), (13.45, 0))
                Line((0, 0), (13.45, 0))
                Line((0, 0), (0, -2))
                Line((0, -2), (13.45, -2))
                Line((13.45, -2), (16.5, -5.05))
                Line((16.5, -17), (16.5, -5.05))
                Line((16.5, -17), (18.5, -17))
                Line((18.5, -5.05), (18.5, -17))
                Line((21.55, -2), (18.5, -5.05))
            make_face()
            with BuildLine():
                CenterArc((17.5, -8.5), 0.65, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((17.5, -12), 0.65, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((17.5, -15.5), 0.65, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.2
        extrude(amount=2.2)

        # Sketch4 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 9 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 21.2453352646, perimeter: 16.3394233913
            with Locations((34.1, 1)):
                Circle(2.6005)
            # Profile area: 21.2453352646, perimeter: 16.3394233913
            with Locations((0.9, 1)):
                Circle(2.6005)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2, mode=Mode.ADD)

        # Sketch7 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-0.9, 1)):
                Circle(0.3)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-34.1, 1)):
                Circle(0.3)
        # OneSide extrude, distance=-8
        extrude(amount=-8, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a rectangular channel or tray with a long, shallow box-like shape featuring angled end caps on both sides and a recessed central channel running along its length.
def model_145041_025cf3fe_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 57.6, perimeter: 44.4
            with BuildLine():
                Line((0, 3), (0, 0))
                Line((0, 0), (19.2, 0))
                Line((19.2, 0), (19.2, 3))
                Line((19.2, 3), (0, 3))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.4), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 20.2, perimeter: 82.8
            with BuildLine():
                Line((-19.2, -3), (0, -3))
                Line((0, -3), (0, 0))
                Line((0, 0), (-19.2, 0))
                Line((-19.2, 0), (-19.2, -3))
            make_face()
            with BuildLine():
                Line((-18.1000000164, -2.600000006), (-1.1000000164, -2.600000006))
                Line((-18.1000000164, -0.400000006), (-18.1000000164, -2.600000006))
                Line((-1.1000000164, -0.400000006), (-18.1000000164, -0.400000006))
                Line((-1.1000000164, -2.600000006), (-1.1000000164, -0.400000006))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.2), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 19.8073009183, perimeter: 85.9415926536
            with BuildLine():
                Line((-19.2, 0), (-19.2, -3))
                Line((-19.2, -3), (0, -3))
                Line((0, -3), (0, 0))
                Line((0, 0), (-19.2, 0))
            make_face()
            with BuildLine():
                CenterArc((-18.6500002779, -1.5000000224), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-0.550625235, -1.5), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-18.1000000164, -0.400000006), (-1.1000000164, -0.400000006))
                Line((-1.1000000164, -0.400000006), (-1.1000000164, -2.600000006))
                Line((-1.1000000164, -2.600000006), (-18.1000000164, -2.600000006))
                Line((-18.1000000164, -2.600000006), (-18.1000000164, -0.400000006))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.4), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 3.84, perimeter: 38.8
            with BuildLine():
                Line((-19.2, -2.8), (0, -2.8))
                Line((-19.2, -3), (-19.2, -2.8))
                Line((0, -3), (-19.2, -3))
                Line((0, -2.8), (0, -3))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.4), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 3.84, perimeter: 38.8
            with BuildLine():
                Line((0, -0.2), (-19.2, -0.2))
                Line((0, 0), (0, -0.2))
                Line((-19.2, 0), (0, 0))
                Line((-19.2, -0.2), (-19.2, 0))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


# Description: This is a complex molded or cast component featuring a bulbous main body with multiple angular fins or blade-like protrusions on top, a cylindrical side extension, and what appears to be internal cavities or passages, suggesting it may be a pump housing, compressor casing, or fluid dynamics component.
def model_145257_89235edd_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 9.12, perimeter: 14.6
            with BuildLine():
                Line((0, 5.7), (1.6, 5.7))
                Line((0, 0), (0, 5.7))
                Line((1.6, 0), (0, 0))
                Line((1.6, 5.7), (1.6, 0))
            make_face()
            # Profile area: 13.3401667134, perimeter: 20.9473342574
            with BuildLine():
                Line((1.6, 5.7), (1.6, 0))
                Line((1.6, 0), (4.1275105345, 0.9870108905))
                CenterArc((3.4, 2.85), 2, -68.6690002146, 137.3380004293)
                Line((1.6, 5.7), (4.1275105345, 4.7129891095))
            make_face()
            with BuildLine():
                CenterArc((3.4, 2.85), 0.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 2.0106192983, perimeter: 5.0265482457
            with Locations((3.4, 2.85)):
                Circle(0.8)
        # OneSide extrude, distance=-8.4
        extrude(amount=-8.4)

        # Sketch1 -> Extrude2 (Cut)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.0106192983, perimeter: 5.0265482457
            with Locations((3.4, 2.85)):
                Circle(0.8)
        # OneSide extrude, distance=-11.5
        extrude(amount=-11.5, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 31.6235749403, perimeter: 22.5030716969
            with BuildLine():
                Line((7.4053255458, 1.4), (7.0888083615, 7))
                Line((7.0888083615, 7), (1.6, 7))
                Line((1.6, 7), (1.6, 1.4))
                Line((7.4053255458, 1.4), (1.6, 1.4))
            make_face()
        # OneSide extrude, distance=8
        extrude(amount=8, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 18.4490028582, perimeter: 27.3318560862
            with BuildLine():
                CenterArc((-4.2, 2.85), 2.85, 90, 180)
                CenterArc((-4.2, 2.85), 2.85, -90, 180)
            make_face()
            with BuildLine():
                CenterArc((-4.2, 2.85), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3.8
        extrude(amount=3.8, mode=Mode.ADD)

        # Sketch3 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            with Locations((-4.2, 2.85)):
                Circle(1.5)
        # OneSide extrude, distance=-9.5
        extrude(amount=-9.5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude6 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.2533739975, perimeter: 2.3159324177
            with BuildLine():
                CenterArc((4.2, 2.85), 1.5, 74.0946682472, 30.9320199068)
                Line((4.6110965877, 4.6487077469), (4.6110730709, 4.2925737175))
                Line((3.8110965877, 4.6487077469), (4.6110965877, 4.6487077469))
                Line((3.8110965877, 4.2987077469), (3.8110965877, 4.6487077469))
            make_face()
        # OneSide extrude, distance=-13.2
        extrude(amount=-13.2, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a complex multi-faceted industrial component with an irregular polygonal shape featuring angular surfaces, internal cavities with cross-hatched detail, and protruding flanges or ears, resembling a casting or bracket with multiple functional surfaces and recessed pockets.
def model_145985_e6210d7a_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.64, perimeter: 12
            with BuildLine():
                Line((1.2, -1.8), (-1.2, -1.8))
                Line((1.2, 1.8), (1.2, -1.8))
                Line((-1.2, 1.8), (1.2, 1.8))
                Line((-1.2, -1.8), (-1.2, 1.8))
            make_face()
        # OneSide extrude, distance=3.5
        extrude(amount=3.5)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.0893800988, perimeter: 9.2548667765
            with BuildLine():
                CenterArc((1.2, 0), 1.8, -90, 180)
                Line((1.2, 1.8), (1.2, -1.8))
            make_face()
        # OneSide extrude, distance=1.4
        extrude(amount=1.4, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1.2, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.21, perimeter: 8.2453624047
            with BuildLine():
                Line((-1.8, 1.4), (-0.8, 2.3))
                Line((0.5, 2.3), (-0.8, 2.3))
                Line((0.5, 3.5), (0.5, 2.3))
                Line((0.5, 3.5), (-1.8, 3.5))
                Line((-1.8, 1.4), (-1.8, 3.5))
            make_face()
        # OneSide extrude, distance=-1.4
        extrude(amount=-1.4, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-1.2, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 2.4138940946, perimeter: 7.5126513579
            with BuildLine():
                Line((-0.4989467796, 3.5), (1.8000000268, 1.4000000209))
                Line((1.8000000268, 1.4000000209), (1.8, 3.5))
                Line((-0.4989467796, 3.5), (1.8, 3.5))
            make_face()
        # OneSide extrude, distance=-2.4
        extrude(amount=-2.4, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.6595130102, 1.515901663), x_dir=(1, 0, 0), z_dir=(0, 0.7383316988, 0.6744377677))):
            # Profile area: 1.0153324579, perimeter: 4.8936168622
            with BuildLine():
                Line((-0.2, 1.9203727151), (-1.2, 2.7289204103))
                Line((-1.2, 2.7289204103), (-0.2, 0.9605415066))
                Line((-0.2, 0.9605415066), (-0.2, 1.9203727151))
            make_face()
        # OneSide extrude, distance=1.3
        extrude(amount=1.3, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a 3D connector or coupling part featuring two cylindrical shafts intersecting at an angle, with rounded ends and a cross-shaped overall geometry, commonly used for mechanical linkage or rotational power transmission applications.
def model_146109_4a58cccf_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # Symmetric extrude, each_side=2
        extrude(amount=2, both=True)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # Symmetric extrude, each_side=2
        extrude(amount=2, both=True, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -2), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.096211275, perimeter: 1.0995574288
            Circle(0.175)
        # OneSide extrude, distance=-8.9
        extrude(amount=-8.9, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(2, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.096211275, perimeter: 1.0995574288
            Circle(0.175)
        # OneSide extrude, distance=-4.8
        extrude(amount=-4.8, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a curved cylindrical bracket or housing with a split design, featuring two elongated slots on opposite sides, a central rectangular opening, and ribbed reinforcement patterns throughout its structure.
def model_146317_3eafabf0_0004():
    """Model: rPi_camera_rotator v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.5637441664, perimeter: 25.9181393921
            with BuildLine():
                CenterArc((0, 0), 2.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.925, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=4.08
        extrude(amount=4.08)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 8.45, perimeter: 11.7
            with BuildLine():
                Line((1.625, 0.7340000966), (1.625, 3.3340000966))
                Line((1.625, 3.3340000966), (-1.625, 3.3340000966))
                Line((-1.625, 3.3340000966), (-1.625, 0.7340000966))
                Line((-1.625, 0.7340000966), (1.625, 0.7340000966))
            make_face()
        # OneSide extrude, distance=4.4
        extrude(amount=4.4, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude7 (Join)
        # Sketch on YZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.5199999558, perimeter: 5.6793687969
            with BuildLine():
                CenterArc((1.6845822379, 2.0333779371), 4.3845872386, -179.9134658792, 17.1520468771)
                Line((-2.5030450713, 0.7340000966), (-2.3030450713, 0.7340000966))
                CenterArc((1.8845822379, 2.0333779371), 4.3845872386, 162.7443932464, 34.4941877515)
                Line((-2.3026587691, 3.3340000966), (-2.5026587691, 3.3340000966))
                CenterArc((1.6845822379, 2.0333779371), 4.3845872386, 162.7443932464, 17.1690726328)
                Line((-2.7, 2.0267558741), (-2.7, 2.04))
            make_face()
        # Symmetric extrude, each_side=1.625
        extrude(amount=1.625, both=True, mode=Mode.ADD)

        # Sketch8 -> Extrude8 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 7.6529129114, perimeter: 11.7133277361
            with BuildLine():
                Line((-3.0000000447, 3.9855984601), (-3.0000000447, 0.0969462647))
                Line((-1.031988372, 0.0969462647), (-3.0000000447, 0.0969462647))
                Line((-1.031988372, 3.9855984601), (-1.031988372, 0.0969462647))
                Line((-3.0000000447, 3.9855984601), (-1.031988372, 3.9855984601))
            make_face()
        # Symmetric extrude, each_side=0.85
        extrude(amount=0.85, both=True, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical connector or adapter housing with a dark gray main body, featuring a protruding circular end cap, angular mounting flanges on the sides with rectangular cutouts, and blue accent panels or internal components visible through the structure.
def model_146317_9562bd6f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.5446900494, perimeter: 5.6548667765
            Circle(0.9)
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 15, perimeter: 16
            with BuildLine():
                Line((-2.0265859981, 0.4040636478), (2.8030431334, 1.6981588733))
                Line((2.8030431334, 1.6981588733), (2.0265859981, 4.5959363522))
                Line((2.0265859981, 4.5959363522), (-2.8030431334, 3.3018411267))
                Line((-2.8030431334, 3.3018411267), (-2.0265859981, 0.4040636478))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 8.2346903509, perimeter: 11.8288229509
            with BuildLine():
                Line((1.1973331241, 3.9596282421), (-1.7667350233, 3.1654085757))
                CenterArc((-2.3131451848, 3.0189984142), 0.5656854249, -75, 90)
                Line((-2.1667350233, 2.4725882527), (-1.8901534471, 1.4403717579))
                CenterArc((-1.7437432856, 0.8939615964), 0.5656854249, 15, 90)
                Line((-1.1973331241, 1.0403717579), (1.7667350233, 1.8345914243))
                CenterArc((2.3131451848, 1.9810015858), 0.5656854249, 105, 90)
                Line((2.1667350233, 2.5274117473), (1.8901534471, 3.5596282421))
                CenterArc((1.7437432856, 4.1060384036), 0.5656854249, -165, 90)
            make_face()
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.5393804003, perimeter: 4.398229715
            Circle(0.7)
        # OneSide extrude, distance=-4.7
        extrude(amount=-4.7, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.08552986, perimeter: 1.0367255757
            with Locations((-2.3131451848, 3.0189984142)):
                Circle(0.165)
            # Profile area: 0.08552986, perimeter: 1.0367255757
            with Locations((-1.7437432856, 0.8939615964)):
                Circle(0.165)
            # Profile area: 0.08552986, perimeter: 1.0367255757
            with Locations((1.7437432856, 4.1060384036)):
                Circle(0.165)
            # Profile area: 0.08552986, perimeter: 1.0367255757
            with Locations((2.3131451848, 1.9810015858)):
                Circle(0.165)
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a protective cover or housing component with a curved, rounded rectangular shape featuring a large open cavity on top, ventilation slots on the side, and mounting holes for assembly.
def model_146317_fc36685c_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1472621556, perimeter: 2.3561944902
            with BuildLine():
                CenterArc((-1.0875, 0.625), 0.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-1.0875, 0.625), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1472621556, perimeter: 2.3561944902
            with BuildLine():
                CenterArc((-1.0875, -0.675), 0.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-1.0875, -0.675), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1472621556, perimeter: 2.3561944902
            with BuildLine():
                CenterArc((1.0125, 0.625), 0.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((1.0125, 0.625), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1472621556, perimeter: 2.3561944902
            with BuildLine():
                CenterArc((1.0125, -0.675), 0.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((1.0125, -0.675), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 5.6797151136, perimeter: 13.2971232869
            with BuildLine():
                CenterArc((-1.125, 0.5), 0.475, 90, 90)
                Line((-1.6, -0.55), (-1.6, 0.5))
                CenterArc((-1.125, -0.55), 0.475, 180, 90)
                Line((0.975, -1.025), (-1.125, -1.025))
                CenterArc((0.975, -0.475), 0.55, -90, 90)
                Line((1.525, 0.425), (1.525, -0.475))
                CenterArc((0.975, 0.425), 0.55, 0, 90)
                Line((-1.125, 0.975), (0.975, 0.975))
            make_face()
            with BuildLine():
                CenterArc((-1.0875, 0.625), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.0125, 0.625), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.0875, -0.675), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.0125, -0.675), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1472621556, perimeter: 2.3561944902
            with BuildLine():
                CenterArc((-1.0875, 0.625), 0.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-1.0875, 0.625), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.1), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.3646337547, perimeter: 3.8734824888
            with BuildLine():
                Line((1.375, 0.9038873605), (1.375, -0.9538873605))
                CenterArc((1.125, -0.55), 0.475, -58.2431361407, 58.2431361407)
                Line((1.6, -0.55), (1.6, 0.5))
                CenterArc((1.125, 0.5), 0.475, 0, 58.2431361407)
            make_face()
            # Profile area: 0.3422253718, perimeter: 3.719884077
            with BuildLine():
                Line((-1.3000000194, -0.9187059695), (-1.3000000194, 0.8687059695))
                CenterArc((-0.975, 0.425), 0.55, 126.2215491213, 53.7784508787)
                Line((-1.525, 0.425), (-1.525, -0.475))
                CenterArc((-0.975, -0.475), 0.55, -180, 53.7784508787)
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(1.525, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.5632001966, perimeter: 4.1778793821
            with BuildLine():
                Line((-0.0567341743, 0.9094848011), (1.2482595404, 0.2228018259))
                CenterArc((1.1160206874, -0.028509009), 0.2839793126, 0, 62.2468169893)
                Line((1.4000000209, 0.9094848011), (1.4000000209, -0.028509009))
                Line((-0.0567341743, 0.9094848011), (1.4000000209, 0.9094848011))
            make_face()
            # Profile area: 0.5686432669, perimeter: 4.1966950673
            with BuildLine():
                CenterArc((1.1160206874, -0.028509009), 0.2839793126, -62.2468169893, 62.2468169893)
                Line((-0.0638178896, -0.9702302449), (1.2482595404, -0.2798198439))
                Line((1.4000000209, -0.9702302449), (-0.0638178896, -0.9702302449))
                Line((1.4000000209, -0.028509009), (1.4000000209, -0.9702302449))
            make_face()
        # OneSide extrude, distance=-3.2
        extrude(amount=-3.2, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1.525, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0530929158, perimeter: 0.8168140899
            with Locations((1.1160206874, -0.028509009)):
                Circle(0.13)
        # OneSide extrude, distance=-3.2
        extrude(amount=-3.2, mode=Mode.SUBTRACT)
    return part.part


# Description: A rectangular frame or mounting bracket with two vertical parallel rails connected by horizontal supports at top and bottom, featuring mounting flanges with holes at the corners and a large open rectangular passage through the center.
def model_146380_f1665a64_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 58.8, perimeter: 33.8
            with BuildLine():
                Line((-4.9, 12), (0, 12))
                Line((-4.9, 0), (-4.9, 12))
                Line((0, 0), (-4.9, 0))
                Line((0, 12), (0, 0))
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.6, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 20.01, perimeter: 19.6
            with BuildLine():
                Line((-3.9, 10.4), (-3.9, 3.5))
                Line((-3.9, 3.5), (-1, 3.5))
                Line((-1, 3.5), (-1, 10.4))
                Line((-1, 10.4), (-3.9, 10.4))
            make_face()
        # OneSide extrude, distance=-20
        extrude(amount=-20, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 23 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.5, perimeter: 3
            with BuildLine():
                Line((0, 10.5), (0, 11.5))
                Line((0.5, 10.5), (0, 10.5))
                Line((0.5, 11.5), (0.5, 10.5))
                Line((0, 11.5), (0.5, 11.5))
            make_face()
            # Profile area: 0.5, perimeter: 3
            with BuildLine():
                Line((4.9, 10.5), (4.9, 11.5))
                Line((4.9, 11.5), (4.4, 11.5))
                Line((4.4, 11.5), (4.4, 10.5))
                Line((4.4, 10.5), (4.9, 10.5))
            make_face()
            # Profile area: 0.5, perimeter: 3
            with BuildLine():
                Line((4.9, 2), (4.9, 1))
                Line((4.4, 2), (4.9, 2))
                Line((4.4, 1), (4.4, 2))
                Line((4.9, 1), (4.4, 1))
            make_face()
            # Profile area: 0.5, perimeter: 3
            with BuildLine():
                Line((0, 2), (0, 1))
                Line((0, 1), (0.5, 1))
                Line((0.5, 1), (0.5, 2))
                Line((0.5, 2), (0, 2))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 4.9), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-0.5, 11)):
                Circle(0.15)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-0.5, 1.5)):
                Circle(0.15)
        # OneSide extrude, distance=-20
        extrude(amount=-20, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a dark blue polyhedron or geometric box-like component with an irregular, faceted shape featuring multiple angular surfaces, cutouts on the sides, and internal cavity details visible through translucent sections.
def model_146499_eb4d211f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrusion2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 84, perimeter: 38
            with BuildLine():
                Line((0, 7), (0, 0))
                Line((0, 0), (12, 0))
                Line((12, 0), (12, 7))
                Line((12, 7), (0, 7))
            make_face()
        # OneSide extrude, distance=4
        extrude(amount=4)

        # Sketch6 -> Extrusion6 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, -1, 0), z_dir=(-1, 0, 0))):
            # Profile area: 3.2685129968, perimeter: 6.4088490133
            with Locations((-4.98, 2.02)):
                Circle(1.02)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrusion7 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(12, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 3.2685129968, perimeter: 6.4088490133
            with Locations((4.98, 2.02)):
                Circle(1.02)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch11 -> Extrusion12 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, -1, 0), z_dir=(-1, 0, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((-1, 2.64)):
                Circle(0.4)
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a grenade-shaped pressure vessel or container featuring an ovoid main body with a flat rectangular fuze well or arming lever attachment on the top, designed for secure handling and detonation initiation.
def model_147672_3e42908e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 12 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 21.0551029732, perimeter: 18.5012918912
            with BuildLine():
                Line((-13.5037605485, 0.4488527649), (-13.9554304242, 0.0103752985))
                Line((-11.4554304242, 0.0103752985), (-13.9554304242, 0.0103752985))
                Line((-11.4554304242, 0.0103752985), (-11.3072581875, 0.0103752985))
                Line((-11.3072581875, 0.0103752985), (-8.9554304242, 0.0103752985))
                Line((-9.3209197639, 0.3868610642), (-8.9554304242, 0.0103752985))
                CenterArc((-8.9621659404, 0.7351363778), 0.5, 143.7449795375, 80.4059317731)
                CenterArc((-11.3813443059, 2.5092773068), 2.5, -36.2550204625, 250.8118635463)
                CenterArc((-13.8520358621, 0.8076065885), 0.5, -45.8490886893, 80.4059317731)
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 68 constraints, 23 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 1.4554543826, perimeter: 5.7561637914
            with BuildLine():
                Line((-11.7049823473, 3.4967088291), (-11.7049823473, 3.5032912752))
                CenterArc((-10.7000001594, 3.5000000522), 1.0049875771, -179.8123623297, 113.6491530725)
                CenterArc((-10.3039551078, 2.6036050676), 0.025, -66.1632092572, 99.1070573372)
                Line((-10.3724273698, 2.7552410309), (-10.2829750096, 2.6172004888))
                Line((-10.2986041916, 2.8691630283), (-10.3724273698, 2.7552410309))
                CenterArc((-10.3195842898, 2.8827584494), 0.025, -32.94384808, 130.4060297824)
                CenterArc((-10.4000001624, 3.4967088291), 0.5941944616, -180, 97.4621817024)
                Line((-10.994194624, 3.4967088291), (-10.994194624, 4.2967088291))
                CenterArc((-11.3495884857, 3.7488563683), 0.6530291844, 57.0283802187, 65.9432395626)
                Line((-11.7049823473, 3.5032912752), (-11.7049823473, 4.2967088291))
            make_face()
            # Profile area: 0.1184266067, perimeter: 1.7733689143
            with BuildLine():
                CenterArc((-11.8844762285, 3.9400046169), 1.0032794782, 28.1658528976, 29.8120666658)
                CenterArc((-10.8370027292, 3.9554265427), 0.9814741091, 121.6829651881, 30.4902971628)
                CenterArc((-11.3524912556, 3.6787248616), 0.8150209736, 64.3741058633, 51.2517882733)
            make_face()
            # Profile area: 0.3834044614, perimeter: 2.4349010007
            with BuildLine():
                Line((-10.4000001624, 4.1500000641), (-10.4000001624, 3.4967088291))
                CenterArc((-10.5500001624, 4.1500000641), 0.15, 0, 90)
                Line((-10.9000001624, 4.3000000641), (-10.5500001624, 4.3000000641))
                Line((-10.9000001624, 3.7467088291), (-10.9000001624, 4.3000000641))
                CenterArc((-10.6500001624, 3.7467088291), 0.25, 180, 90)
                Line((-10.4000001624, 3.4967088291), (-10.6500001624, 3.4967088291))
            make_face()
            # Profile area: 0.3817588558, perimeter: 2.4283185695
            with BuildLine():
                CenterArc((-12.1500001833, 4.1500000641), 0.15, 90, 90)
                Line((-12.3000001833, 4.1500000641), (-12.3000001833, 3.5000000522))
                Line((-12.3000001833, 3.5000000522), (-12.0500001758, 3.5000000522))
                CenterArc((-12.0500001758, 3.7500000522), 0.25, -90, 90)
                Line((-11.8000001758, 3.7500000522), (-11.8000001758, 4.3000000641))
                Line((-11.8000001758, 4.3000000641), (-12.1500001833, 4.3000000641))
            make_face()
            # Profile area: 0.2504409197, perimeter: 2.0937762117
            with BuildLine():
                Line((-12.5000001863, 3.3828427581), (-12.5000001863, 3.1000000462))
                CenterArc((-12.6000001878, 3.1000000462), 0.3, 70.5287790637, 306.4383723706)
                Line((-12.5000001863, 3.1000000462), (-12.3130585217, 3.1875470639))
            make_face()
            # Profile area: 0.9402618385, perimeter: 3.8536931505
            with BuildLine():
                CenterArc((-11.3813443059, 2.5092773068), 1, 113.1615284789, 104.6542707541)
                CenterArc((-12.4000001848, 2.9000000432), 1.0295630294, -77.167368102, 64.6635108121)
                CenterArc((-10.7000001594, 3.5000000522), 1.0770329775, -176.2029897485, 46.0254451412)
            make_face()
            # Profile area: 1.0349357049, perimeter: 4.4541798742
            with BuildLine():
                CenterArc((-11.3813443059, 2.5092773068), 1, -135.0659160945, 132.8698869157)
                CenterArc((-10.7000001594, 3.5000000522), 1.0770329775, -123.7728197996, 50.9413088483)
                CenterArc((-12.4000001848, 2.9000000432), 1.1401754421, -74.1849157544, 59.1754119885)
            make_face()
            # Profile area: 0.7440566538, perimeter: 3.4396414874
            with BuildLine():
                CenterArc((-9.9271305085, 2.1414971666), 0.4, -27.1831866881, 192.9903157517)
                CenterArc((-11.3813443059, 2.5092773068), 1.1, -53.7436935497, 39.5508226133)
                CenterArc((-10.326986294, 2.3967112253), 0.873410183, -117.538746741, 87.444491227)
            make_face()
            # Profile area: 0.7742484631, perimeter: 3.9005031517
            with BuildLine():
                CenterArc((-12.087965523, 3.0249897147), 1.5562521177, -131.573184119, 2.6927013679)
                CenterArc((-12.087965523, 3.0249897147), 1.5562521177, -128.880482751, 49.3227014499)
                CenterArc((-11.3813443059, 2.5092773068), 1.1, -165.7973061511, 53.0937236)
                CenterArc((-12.8354950288, 2.1412478585), 0.4, 14.2026938489, 210.3254795536)
            make_face()
            # Profile area: 0.1410393265, perimeter: 1.8193994833
            with BuildLine():
                CenterArc((-10.3055458988, 1.2474835967), 0.06, -126.1982270145, 19.2036892195)
                CenterArc((-10.2560571891, 1.4094090824), 0.2293192113, -106.9945377951, 32.8875667299)
                CenterArc((-10.198736755, 1.2080911744), 0.02, -74.1069710653, 114.1099025421)
                CenterArc((-10.2049469286, 1.2028796786), 0.028107154, 40.0029314766, 34.1859242812)
                CenterArc((-10.1991959173, 1.2231882437), 0.007, 74.1888557994, 12.021207088)
                CenterArc((-10.1908481507, 1.3492045873), 0.1192925337, 174.8424562605, 91.3676066393)
                CenterArc((-10.3584691897, 1.3707652588), 0.05, -12.5175312073, 90.906442831)
                CenterArc((-10.0964373397, 2.6460318654), 1.2519084486, -119.2361419455, 17.6250535693)
                CenterArc((-10.7274186006, 1.518694255), 0.04, 60.7638580545, 16.0231191071)
                CenterArc((-10.7526902234, 1.4110581914), 0.1505630005, 76.7869771616, 219.270593324)
                CenterArc((-10.6206607032, 1.1410464822), 0.15, 89.6898902453, 26.3676802403)
                CenterArc((-10.6224281826, 0.8144907485), 0.476560517, 53.8017729856, 35.8881172597)
            make_face()
            # Profile area: 0.1665280566, perimeter: 1.8380570588
            with BuildLine():
                CenterArc((-12.4515600924, 1.1567175745), 0.074587694, 85.696708649, 137.0316668071)
                CenterArc((-12.4923936256, 1.1190000151), 0.019, -137.2716245439, 47.2716147611)
                Line((-12.4923936288, 1.1000000151), (-12.259999726, 1.0999999754))
                CenterArc((-12.2042040034, 1.9799603715), 0.8817275437, -93.6281012856, 25.2014558009)
                CenterArc((-11.9453864152, 1.3253440734), 0.1778035129, -68.4232737488, 60.5956281513)
                Line((-11.8000001758, 1.4000000209), (-11.7692396324, 1.3011283731))
                CenterArc((-12.0560986609, 2.935035597), 1.5562521177, -98.0186932583, 17.4904292781)
                CenterArc((-12.2766772867, 1.3692439986), 0.025, 81.9813067417, 90.2292802757)
                CenterArc((-12.4649152752, 1.3949939615), 0.1649910549, -83.4040746833, 75.6146617007)
            make_face()
            # Profile area: 0.15946818, perimeter: 1.6643517896
            with BuildLine():
                CenterArc((-10.000000149, 3.1000000462), 0.3, 179.8285812747, 180.1714187253)
                CenterArc((-9.7750001457, 3.0562967163), 0.0868042696, 30.229829627, 119.5403422316)
                CenterArc((-9.9250001479, 3.0552110052), 0.0873559291, 30.8451084743, 118.3097830514)
                CenterArc((-10.0750001501, 3.0553172191), 0.0873015189, 30.7852602717, 118.4294794566)
                CenterArc((-10.2252800342, 3.05356211), 0.0884507925, 31.6692099655, 115.9759082263)
            make_face()
            # Profile area: 0.1058251135, perimeter: 1.659036704
            with BuildLine():
                CenterArc((-10.000000149, 3.1000000462), 0.3, 8.1672006347, 63.5826358696)
                CenterArc((-9.8804749034, 3.5000000522), 0.1178979517, -110.745044597, 8.2164190975)
                CenterArc((-9.8804749034, 3.5000000522), 0.1178979517, 180, 69.254955403)
                CenterArc((-10.1162708068, 3.5000000522), 0.1178979517, -66.4588943953, 66.4588943953)
                CenterArc((-10.1162708068, 3.5000000522), 0.1178979517, -81.1252782961, 14.6663839008)
                CenterArc((-10.000000149, 3.1000000462), 0.3, 109.0831530246, 62.8668263483)
                CenterArc((-10.2235220786, 3.0761998247), 0.0986743462, 41.8325966447, 96.3348067105)
                CenterArc((-10.0739110828, 3.0735630508), 0.1023460393, 42.4329925425, 95.5930662575)
                CenterArc((-9.9241865009, 3.0766105947), 0.0993010077, 41.6614485945, 96.677102811)
                CenterArc((-9.7765214902, 3.0783809232), 0.0975992306, 41.1611800379, 97.6776399243)
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch3 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1.5, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.0113097336, perimeter: 0.3769911184
            with Locations((-11.3000001684, 1.8000000268)):
                Circle(0.06)
            # Profile area: 0.0113097336, perimeter: 0.3769911184
            with Locations((-11.5849823473, 3.9000000581)):
                Circle(0.06)
            # Profile area: 0.0113097336, perimeter: 0.3769911184
            with Locations((-11.114194624, 3.9000000581)):
                Circle(0.06)
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 1.8947730692, perimeter: 30.3163691071
            with BuildLine():
                CenterArc((-11.3813443059, 2.5092773068), 2.475, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-11.3813443059, 2.5092773068), 2.35, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


# Description: This is a blue rectangular bridge or connector component with two cylindrical support legs on each end and a small raised feature or handle on top, designed to span between two mounting points.
def model_147739_796beb31_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> 押し出し1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 15, perimeter: 16
            with BuildLine():
                Line((-2.5, 1.5), (2.5, 1.5))
                Line((-2.5, -1.5), (-2.5, 1.5))
                Line((2.5, -1.5), (-2.5, -1.5))
                Line((2.5, 1.5), (2.5, -1.5))
            make_face()
        # OneSide extrude, distance=6.5
        extrude(amount=6.5)

        # Sketch2 -> 押し出し2 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(2.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4.5, perimeter: 9
            with BuildLine():
                Line((1.5, 5), (-1.5, 5))
                Line((1.5, 6.5), (1.5, 5))
                Line((-1.5, 6.5), (1.5, 6.5))
                Line((-1.5, 5), (-1.5, 6.5))
            make_face()
        # OneSide extrude, distance=12
        extrude(amount=12, mode=Mode.ADD)

        # Sketch4 -> 押し出し3 (Join)
        # Sketch on Profile plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 32.5, perimeter: 23
            with BuildLine():
                Line((19.5, 0), (14.5, 0))
                Line((19.5, 6.5), (19.5, 0))
                Line((14.5, 6.5), (19.5, 6.5))
                Line((14.5, 0), (14.5, 6.5))
            make_face()
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.ADD)

        # Sketch5 -> 押し出し4 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -1.5), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 2.653870517, perimeter: 7.1237949867
            with BuildLine():
                Line((-18.4387094509, 6.5), (-19.5, 6.5))
                CenterArc((-19.5, 6.5), 1.0612905491, 0, 270)
                Line((-19.5, 6.5), (-19.5, 5.4387094509))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a rectangular insert or cutting tool with an elongated prismatic shape, featuring a tapered or wedge-like profile with angular faceted surfaces and a dark metallic finish, commonly used as a lathe or milling insert for machining operations.
def model_20203_7e31e92a_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 123.7711270804, perimeter: 58.7990667337
            with BuildLine():
                Line((-5, 20), (-5, 0))
                Line((-5, 0), (-3.634854036, -5.0947940974))
                CenterArc((-2.4551922321, -4.7787046697), 1.2212757665, -165, 150)
                Line((-1.2755304282, -5.0947940974), (0.2745189732, 0))
                Line((0, 20), (0.2745189732, 0))
                Line((0, 20), (-5, 20))
            make_face()
        # OneSide extrude, distance=6
        extrude(amount=6)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XY construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.6219868529, perimeter: 6.467492429
            with BuildLine():
                CenterArc((-2.5554200835, 4.441093189), 0.5550730285, 0, 180)
                Line((-3.110493112, 4.441093189), (-3.110493112, 2.951160323))
                CenterArc((-2.5554200835, 2.951160323), 0.5550730285, 180, 180)
                Line((-2.000347055, 2.951160323), (-2.000347055, 4.441093189))
            make_face()
        # OneSide extrude, distance=7.5
        extrude(amount=7.5, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.2512614399, 0, 0.0764442364), x_dir=(0.291068791, 0, -0.9567021265), z_dir=(0.9567021265, 0, 0.291068791))):
            # Profile area: 5.5408430108, perimeter: 9.4173691756
            with BuildLine():
                Line((-4.8086845878, 5), (-4.8086845878, 2.6))
                Line((-4.8086845878, 2.6), (-2.5, 2.6))
                Line((-2.5, 2.6), (-2.5, 5))
                Line((-2.5, 5), (-4.8086845878, 5))
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-4.6650635095, 0, 1.25), x_dir=(0.2588190451, 0, 0.9659258263), z_dir=(-0.9659258263, 0, 0.2588190451))):
            # Profile area: 7.5, perimeter: 11
            with BuildLine():
                Line((3.5, 2.5), (3.5, 5))
                Line((3.5, 5), (0.5, 5))
                Line((0.5, 5), (0.5, 2.5))
                Line((0.5, 2.5), (3.5, 2.5))
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a horizontal mounting bracket or channel with a long rectangular profile, featuring two circular mounting holes at each end and a central slot or groove running lengthwise along the top surface.
def model_20440_27177360_0003():
    """Model: trave v5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 128.8, perimeter: 80.6
            with BuildLine():
                Line((0, -3.5), (0, 0))
                Line((0, 0), (-36.8, 0))
                Line((-36.8, 0), (-36.8, -3.5))
                Line((-36.8, -3.5), (0, -3.5))
            make_face()
        # OneSide extrude, distance=2.8
        extrude(amount=2.8)

        # Sketch5 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.8), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 18.9, perimeter: 17.8
            with BuildLine():
                Line((-5.4, -3.5), (0, -3.5))
                Line((0, -3.5), (0, 0))
                Line((0, 0), (-5.4, 0))
                Line((-5.4, -3.5), (-5.4, 0))
            make_face()
            # Profile area: 18.9, perimeter: 17.8
            with BuildLine():
                Line((-31.4, 0), (-36.8, 0))
                Line((-36.8, 0), (-36.8, -3.5))
                Line((-36.8, -3.5), (-31.4, -3.5))
                Line((-31.4, 0), (-31.4, -3.5))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude3 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 18.9, perimeter: 17.8
            with BuildLine():
                Line((31.4, 0), (31.4, -3.5))
                Line((31.4, -3.5), (36.8, -3.5))
                Line((36.8, -3.5), (36.8, 0))
                Line((36.8, 0), (31.4, 0))
            make_face()
            # Profile area: 18.9, perimeter: 17.8
            with BuildLine():
                Line((0, 0), (0, -3.5))
                Line((0, -3.5), (5.4, -3.5))
                Line((5.4, -3.5), (5.4, 0))
                Line((5.4, 0), (0, 0))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 12 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 2.89, perimeter: 6.8
            with BuildLine():
                Line((33.4, -0.9), (35.1, -0.9))
                Line((33.4, -2.6), (33.4, -0.9))
                Line((35.1, -2.6), (33.4, -2.6))
                Line((35.1, -0.9), (35.1, -2.6))
            make_face()
            # Profile area: 2.89, perimeter: 6.8
            with BuildLine():
                Line((1.7, -0.9), (3.4, -0.9))
                Line((1.7, -2.6), (1.7, -0.9))
                Line((3.4, -2.6), (1.7, -2.6))
                Line((3.4, -0.9), (3.4, -2.6))
            make_face()
        # OneSide extrude, distance=-11
        extrude(amount=-11, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a sheet metal channel or tray with a trapezoidal cross-section, featuring a central web, outward-flaring side flanges, and small mounting tabs or lugs extending from the ends.
def model_20945_8b57f672_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 148620.48, perimeter: 1706.8
            with BuildLine():
                Line((121.9, 609.6), (-121.9, 609.6))
                Line((-121.9, 609.6), (-121.9, 0))
                Line((-121.9, 0), (121.9, 0))
                Line((121.9, 0), (121.9, 609.6))
            make_face()
            # Profile area: 148620.48, perimeter: 1706.8
            with BuildLine():
                Line((-121.9, 0), (121.9, 0))
                Line((-121.9, 0), (-121.9, -609.6))
                Line((-121.9, -609.6), (121.9, -609.6))
                Line((121.9, -609.6), (121.9, 0))
            make_face()
        # OneSide extrude, distance=259.1
        extrude(amount=259.1)

        # Sketch5 -> Extrude4 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 410520, perimeter: 4393.6
            with BuildLine():
                Line((364.4, -732.1), (-121.9, -732.1))
                Line((364.4, 732.1), (364.4, -732.1))
                Line((-121.9, 732.1), (364.4, 732.1))
                Line((-121.9, 612.1), (-121.9, 732.1))
                Line((124.4, 612.1), (-121.9, 612.1))
                Line((124.4, -612.1), (124.4, 612.1))
                Line((-121.9, -612.1), (124.4, -612.1))
                Line((-121.9, -732.1), (-121.9, -612.1))
            make_face()
        # OneSide extrude, distance=20
        extrude(amount=20)

        # Sketch6 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 13 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-117.6, 10.3, 609.6), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 16368.8053217759, perimeter: 1671.5598789104
            with BuildLine():
                Line((15.7, 300.5497732705), (219.5, 318.3799628971))
                Line((219.5, 318.3799628971), (219.5, 249.8))
                Line((219.5, 249.8), (239.5, 249.8))
                Line((239.5, 249.8), (239.5, 320.1297361676))
                Line((239.5, 320.1297361676), (489.5, 342.0019020491))
                Line((489.5, 342.0019020491), (487.7502267295, 362.0019020491))
                Line((487.7502267295, 362.0019020491), (-206.0497732705, 301.3022672948))
                Line((-206.0497732705, 301.3022672948), (-204.3, 281.3022672948))
                Line((-204.3, 281.3022672948), (-4.3, 298.8))
                Line((-4.3, 298.8), (-4.3, 249.8))
                Line((-4.3, 249.8), (15.7, 249.8))
                Line((15.7, 300.5497732705), (15.7, 249.8))
            make_face()
        # OneSide extrude, distance=-20
        extrude(amount=-20, mode=Mode.ADD)
    return part.part


# Description: This is a U-shaped mounting bracket or channel with two vertical flanges on each end and a cylindrical boss or pivot point on the left side, designed to hold or support components in a fixed assembly.
def model_21231_eb9826e5_0004():
    """Model: Y6 v7"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.2671, perimeter: 9.98
            with BuildLine():
                Line((2.38, -0.77), (0, -0.77))
                Line((2.38, 0), (2.38, -0.77))
                Line((0, 0), (2.38, 0))
                Line((0, -0.77), (0, 0))
            make_face()
            with BuildLine():
                Line((0.465, -0.58), (0.465, -0.19))
                Line((0.465, -0.19), (1.915, -0.19))
                Line((1.915, -0.19), (1.915, -0.58))
                Line((1.915, -0.58), (0.465, -0.58))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.31
        extrude(amount=0.31)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.31, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1463, perimeter: 1.92
            with BuildLine():
                Line((-2.19, 0), (-2.19, 0.77))
                Line((-2.19, 0.77), (-2.38, 0.77))
                Line((-2.38, 0.77), (-2.38, 0))
                Line((-2.38, 0), (-2.19, 0))
            make_face()
            # Profile area: 0.1463, perimeter: 1.92
            with BuildLine():
                Line((-0.19, 0.77), (-0.19, 0))
                Line((-0.19, 0), (0, 0))
                Line((0, 0), (0, 0.77))
                Line((0, 0.77), (-0.19, 0.77))
            make_face()
        # OneSide extrude, distance=1.1
        extrude(amount=1.1, mode=Mode.ADD)

        # Sketch8 -> Extrude7 (Join)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((0.4238902781, 0.91)):
                Circle(0.15)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch9 -> Extrude8 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.3, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.2120575041, perimeter: 2.8274333882
            with BuildLine():
                CenterArc((0.4238902781, 0.91), 0.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0.4238902781, 0.91), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((0.4238902781, 0.91)):
                Circle(0.15)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


# Description: This is a hydraulic or pneumatic actuator assembly featuring a cylindrical barrel body with an angled trapezoidal mounting bracket, a protruding rod or shaft on one side, and internal structural framing visible through semi-transparent rendering.
def model_21231_eb9826e5_0009():
    """Model: Y5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 13 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.012038023, perimeter: 0.5357024274
            with BuildLine():
                CenterArc((0, 0), 0.14, 120, 120)
                Line((-0.07, 0.1212435565), (-0.07, -0.1212435565))
            make_face()
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            with BuildLine():
                CenterArc((-1.2800000608, 0), 0.125, 104.7125580804, 150.585988521)
                CenterArc((-1.2800000608, 0), 0.125, -104.7014533986, 209.414011479)
            make_face()
            # Profile area: 0.5745972963, perimeter: 3.7070793312
            with BuildLine():
                CenterArc((0, 0), 0.45, 104.7087831014, 150.5824347671)
                CenterArc((0, 0), 0.45, -104.7087821314, 209.4175652329)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.14, 120, 120)
                CenterArc((0, 0), 0.14, -120, 240)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.4172244449, perimeter: 4.1156403822
            with BuildLine():
                CenterArc((-1.2800000608, 0), 0.125, -104.7014533986, 209.414011479)
                Line((-1.3117228712, -0.1209076654), (-0.1142577907, -0.4352529808))
                CenterArc((0, 0), 0.45, 104.7087831014, 150.5824347671)
                Line((-1.3117463039, 0.1209015141), (-0.1142577981, 0.4352529788))
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2211681228, perimeter: 2.7646015352
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.14, 60, 240)
                CenterArc((0, 0), 0.14, -60, 120)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.049537193, perimeter: 0.8289177417
            with BuildLine():
                Line((0.07, 0.1212435565), (0.07, -0.1212435565))
                CenterArc((0, 0), 0.14, 60, 240)
            make_face()
            # Profile area: 0.012038023, perimeter: 0.5357024274
            with BuildLine():
                CenterArc((0, 0), 0.14, -60, 120)
                Line((0.07, 0.1212435565), (0.07, -0.1212435565))
            make_face()
        # OneSide extrude, distance=0.63
        extrude(amount=0.63, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 16 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1155028229, perimeter: 1.5806805784
            with BuildLine():
                Line((0.9200000608, 0.2237384138), (0.6200000608, 0.2237384138))
                Line((0.6200000608, 0.2237384138), (0.6200000608, 0.1437384138))
                Line((0.6200000608, 0.1437384138), (0.6999999844, 0.0905146277))
                Line((0.6999999844, 0.0905146277), (0.6999999844, -0.0905146277))
                Line((0.6200000608, -0.1437384138), (0.6999999844, -0.0905146277))
                Line((0.6200000608, -0.1437384138), (0.6200000608, -0.2237384138))
                Line((0.6200000608, -0.2237384138), (0.9200000608, -0.2237384138))
                Line((0.9200000608, -0.2237384138), (0.9200000608, 0.2237384138))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 0.0176714587, perimeter: 0.471238898
            with Locations((1.2800000608, 0)):
                Circle(0.075)
        # TwoSides extrude, along=0.42, against=-0.62
        extrude(amount=0.42, mode=Mode.ADD)
        extrude(sk.sketch, amount=-0.62, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.63, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.061575216, perimeter: 0.879645943
            Circle(0.14)
        # OneSide extrude, distance=-0.63
        extrude(amount=-0.63, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a trapezoidal/wedge-shaped housing or duct component with a tapered box form, featuring a cylindrical projection on the right side, internal ribbing/bracing visible through transparent surfaces, and multiple rectangular apertures or slots on the lower face.
def model_21231_eb9826e5_0012():
    """Model: Y7"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.8032, perimeter: 10.04
            with BuildLine():
                Line((2, -0.83), (0, -0.83))
                Line((2, 0), (2, -0.83))
                Line((0, 0), (2, 0))
                Line((0, -0.83), (0, 0))
            make_face()
            with BuildLine():
                Line((0.16, -0.67), (0.16, -0.16))
                Line((0.16, -0.16), (1.84, -0.16))
                Line((1.84, -0.16), (1.84, -0.67))
                Line((1.84, -0.67), (0.16, -0.67))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(2, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with BuildLine():
                CenterArc((-0.415, 0.35), 0.15, 90, 180)
                CenterArc((-0.415, 0.35), 0.15, -90, 180)
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(2.3, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.2120575041, perimeter: 2.8274333882
            with BuildLine():
                CenterArc((-0.415, 0.35), 0.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-0.415, 0.35), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-0.415, 0.35)):
                Circle(0.15)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 25 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.83), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.030787608, perimeter: 0.7198229715
            with BuildLine():
                Line((1, 0.49), (1, 0.21))
                CenterArc((1, 0.35), 0.14, -90, 90)
                CenterArc((1, 0.35), 0.14, 0, 90)
            make_face()
            # Profile area: 0.0322662244, perimeter: 0.8947226842
            with BuildLine():
                Line((0.9999999963, 0.7), (1, 0.49))
                CenterArc((1, 0.35), 0.14, 0, 90)
                Line((1.14, 0.35), (1.14, 0.6707802986))
                CenterArc((1, 0.35), 0.35, 66.4218215218, 23.5781790852)
            make_face()
            # Profile area: 0.0322662231, perimeter: 0.8947226768
            with BuildLine():
                CenterArc((1, 0.35), 0.35, 90.000000607, 23.5781778712)
                Line((0.86, 0.35), (0.86, 0.6707802986))
                CenterArc((1, 0.35), 0.14, 90, 90)
                Line((0.9999999963, 0.7), (1, 0.49))
            make_face()
            # Profile area: 0.0013399722, perimeter: 0.3132506012
            with BuildLine():
                CenterArc((1, 0.35), 0.35, 66.4218215218, 23.5781790852)
                Line((1.14, 0.6707802986), (1.14, 0.7))
                Line((1.14, 0.7), (0.9999999963, 0.7))
            make_face()
            # Profile area: 0.0013399723, perimeter: 0.3132505901
            with BuildLine():
                Line((0.86, 0.6707802986), (0.86, 0.7))
                CenterArc((1, 0.35), 0.35, 90.000000607, 23.5781778712)
                Line((0.9999999963, 0.7), (0.86, 0.7))
            make_face()
            # Profile area: 0.030787608, perimeter: 0.7198229715
            with BuildLine():
                CenterArc((1, 0.35), 0.14, 90, 90)
                CenterArc((1, 0.35), 0.14, 180, 90)
                Line((1, 0.49), (1, 0.21))
            make_face()
        # OneSide extrude, distance=-0.17
        extrude(amount=-0.17, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude7 (Join)
        # Sketch on BRepFace
        # Sketch has 25 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.83), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0971024946, perimeter: 1.4530562338
            with BuildLine():
                Line((1.14, 0.35), (1.14, 0.6707802986))
                Line((1.14, 0.35), (1.14, 0.0292197014))
                CenterArc((1, 0.35), 0.35, -66.4218215218, 66.4218215218)
                CenterArc((1, 0.35), 0.35, 0, 66.4218215218)
            make_face()
            # Profile area: 0.0322662244, perimeter: 0.8947226842
            with BuildLine():
                Line((0.9999999963, 0.7), (1, 0.49))
                CenterArc((1, 0.35), 0.14, 0, 90)
                Line((1.14, 0.35), (1.14, 0.6707802986))
                CenterArc((1, 0.35), 0.35, 66.4218215218, 23.5781790852)
            make_face()
            # Profile area: 0.0249487527, perimeter: 0.9949675196
            with BuildLine():
                Line((0.86, 0.0292197014), (0.86, 0))
                CenterArc((1, 0.35), 0.35, -180, 66.4218215218)
                Line((0.65, 0.35), (0.65, 0))
                Line((0.65, 0), (0.86, 0))
            make_face()
            # Profile area: 0.0971024946, perimeter: 1.4530562338
            with BuildLine():
                CenterArc((1, 0.35), 0.35, -180, 66.4218215218)
                Line((0.86, 0.35), (0.86, 0.0292197014))
                Line((0.86, 0.35), (0.86, 0.6707802986))
                CenterArc((1, 0.35), 0.35, 113.5781784782, 66.4218215218)
            make_face()
            # Profile area: 0.0322662231, perimeter: 0.8947226768
            with BuildLine():
                CenterArc((1, 0.35), 0.35, 90.000000607, 23.5781778712)
                Line((0.86, 0.35), (0.86, 0.6707802986))
                CenterArc((1, 0.35), 0.14, 90, 90)
                Line((0.9999999963, 0.7), (1, 0.49))
            make_face()
            # Profile area: 0.0249487527, perimeter: 0.9949675196
            with BuildLine():
                Line((1.35, 0.35), (1.35, 0))
                CenterArc((1, 0.35), 0.35, -66.4218215218, 66.4218215218)
                Line((1.14, 0.0292197014), (1.14, 0))
                Line((1.14, 0), (1.35, 0))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical coupling or connector component with two coaxial barrel sections of different diameters, featuring mesh-textured openings at the top ends and a stepped design for joining two shaft or tube assemblies.
def model_21233_05d745b4_0005():
    """Model: LegCrank v1 (7)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6156736203, perimeter: 6.3146012337
            with BuildLine():
                CenterArc((0, 0), 0.6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.405, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.84
        extrude(amount=0.84)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.84, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.515299735, perimeter: 2.5446900494
            Circle(0.405)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.84, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.255025, perimeter: 2.02
            with BuildLine():
                Line((-0.2525, 0.2525), (-0.2525, -0.2525))
                Line((-0.2525, -0.2525), (0.2525, -0.2525))
                Line((0.2525, -0.2525), (0.2525, 0.2525))
                Line((0.2525, 0.2525), (-0.2525, 0.2525))
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.84, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1106375859, perimeter: 2.4915901574
            with BuildLine():
                Line((0, -0.6), (1.1, -0.6))
                CenterArc((1.1, 0), 0.6, -156.4435356909, 66.4435356909)
                CenterArc((0, 0), 0.6, -90, 66.4435356909)
            make_face()
            # Profile area: 1.0987248282, perimeter: 3.7699111843
            with BuildLine():
                CenterArc((1.1, 0), 0.6, -156.4435356909, 66.4435356909)
                CenterArc((1.1, 0), 0.6, -90, 180)
                CenterArc((1.1, 0), 0.6, 90, 66.4435356909)
                CenterArc((0, 0), 0.6, -23.5564643091, 47.1129286182)
            make_face()
            # Profile area: 0.1106375859, perimeter: 2.4915901574
            with BuildLine():
                CenterArc((1.1, 0), 0.6, 90, 66.4435356909)
                Line((0, 0.6), (1.1, 0.6))
                CenterArc((0, 0), 0.6, 23.5564643091, 66.4435356909)
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.84, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5654866776, perimeter: 3.0849555922
            with BuildLine():
                Line((1.1, -0.6), (1.1, 0.6))
                CenterArc((1.1, 0), 0.6, -90, 180)
            make_face()
            # Profile area: 0.5654866776, perimeter: 3.0849555922
            with BuildLine():
                CenterArc((1.1, 0), 0.6, 90, 180)
                Line((1.1, -0.6), (1.1, 0.6))
            make_face()
        # OneSide extrude, distance=0.67
        extrude(amount=0.67, mode=Mode.ADD)
    return part.part


# Description: This is a angular bracket or mounting component with a complex folded/bent geometry featuring multiple planar faces, internal cutouts or slots at the base, and a triangulated surface structure typical of structural reinforcement ribs.
def model_21234_8b71bd47_0002():
    """Model: 2 Sliding Jaw v6"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 59.274075, perimeter: 31.115
            with BuildLine():
                Line((0, 8.89), (0, 0))
                Line((0, 0), (6.6675, 0))
                Line((6.6675, 0), (6.6675, 8.89))
                Line((6.6675, 8.89), (0, 8.89))
            make_face()
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)

        # Sketch6 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2016125, perimeter: 2.8575
            with BuildLine():
                Line((6.50875, 1.27), (6.6675, 1.27))
                Line((6.6675, 1.27), (6.6675, 2.54))
                Line((6.6675, 2.54), (6.50875, 2.54))
                Line((6.50875, 2.54), (6.50875, 1.27))
            make_face()
        # OneSide extrude, distance=-9.652
        extrude(amount=-9.652, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 9 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(6.6675, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.764109375, perimeter: 22.5425
            with BuildLine():
                Line((8.73125, 1.27), (8.89, 1.27))
                Line((8.89, 1.27), (8.89, 2.54))
                Line((8.89, 2.54), (0, 2.54))
                Line((0, 2.54), (0, 1.27))
                Line((0, 1.27), (0.15875, 1.27))
                Line((0.15875, 2.38125), (0.15875, 1.27))
                Line((8.73125, 2.38125), (0.15875, 2.38125))
                Line((8.73125, 1.27), (8.73125, 2.38125))
            make_face()
        # OneSide extrude, distance=-5.715
        extrude(amount=-5.715, mode=Mode.SUBTRACT)

        # Sketch9 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.70564375, perimeter: 5.08
            with BuildLine():
                Line((0, -3.33375), (0, -5.55625))
                Line((0, -3.33375), (-0.3175, -3.33375))
                Line((-0.3175, -3.33375), (-0.3175, -5.55625))
                Line((-0.3175, -5.55625), (0, -5.55625))
            make_face()
            # Profile area: 14.81851875, perimeter: 17.78
            with BuildLine():
                Line((6.6675, -3.33375), (0, -3.33375))
                Line((0, -3.33375), (0, -5.55625))
                Line((0, -5.55625), (6.6675, -5.55625))
                Line((6.6675, -5.55625), (6.6675, -3.33375))
            make_face()
        # OneSide extrude, distance=1.74625
        extrude(amount=1.74625, mode=Mode.ADD)

        # Sketch11 -> Extrude9 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -1.74625, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            with Locations((1.27, -4.445)):
                Circle(0.635)
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            with Locations((5.08, -4.445)):
                Circle(0.635)
        # OneSide extrude, distance=-1.11125
        extrude(amount=-1.11125, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a ball screw assembly consisting of a dark gray cylindrical shaft with a blue cubic nut block attached at its midpoint, designed for linear motion conversion in mechanical systems.
def model_21236_b696e901_0022():
    """Model: Gray Gear Rod v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6495190528, perimeter: 3
            with BuildLine():
                Line((-0.4330127019, -0.25), (0, -0.5))
                Line((0, -0.5), (0.4330127019, -0.25))
                Line((0.4330127019, -0.25), (0.4330127019, 0.25))
                Line((0.4330127019, 0.25), (0, 0.5))
                Line((0, 0.5), (-0.4330127019, 0.25))
                Line((-0.4330127019, 0.25), (-0.4330127019, -0.25))
            make_face()
        # OneSide extrude, distance=0.509
        extrude(amount=0.509)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.509, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1339645793, perimeter: 1.2974777659
            Circle(0.2065)
        # OneSide extrude, distance=0.651
        extrude(amount=0.651, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.16, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0564104377, perimeter: 0.8419468312
            Circle(0.134)
        # OneSide extrude, distance=1.759
        extrude(amount=1.759, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0564104377, perimeter: 0.8419468312
            Circle(0.134)
        # OneSide extrude, distance=0.552
        extrude(amount=0.552, mode=Mode.ADD)
    return part.part


# Description: This is a dual-cylinder connector or coupling assembly featuring two parallel cylindrical bodies connected by a central bridge mechanism, with textured end caps and what appears to be an internal channel or slot linking the two cylinders.
def model_21236_b696e901_0032():
    """Model: Right A6 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.9185085723, perimeter: 6.8001356528
            with BuildLine():
                CenterArc((1.474, -0.79), 0.448, 131.3543710535, 277.291257893)
                Line((1.77, -0.4537144071), (1.77, 0))
                CenterArc((1.474, 0), 0.296, 0, 90)
                Line((1.474, 0.296), (0.6322855929, 0.296))
                CenterArc((0.296, 0), 0.448, 41.3543710535, 277.291257893)
                Line((0.6322855929, -0.296), (1.178, -0.296))
                Line((1.178, -0.296), (1.178, -0.4537144071))
            make_face()
        # OneSide extrude, distance=0.209
        extrude(amount=0.209)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.209, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6305302119, perimeter: 2.8148670176
            with BuildLine():
                CenterArc((-1.474, 0.79), 0.448, -131.3543710535, 82.708742107)
                CenterArc((-1.474, 0.79), 0.448, -48.6456289465, 277.291257893)
            make_face()
        # OneSide extrude, distance=0.279
        extrude(amount=0.279, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.488, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2780505848, perimeter: 1.8692476289
            with Locations((-1.474, 0.79)):
                Circle(0.2975)
        # OneSide extrude, distance=0.683
        extrude(amount=0.683, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.209, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2780505848, perimeter: 1.8692476289
            with Locations((-0.296, 0)):
                Circle(0.2975)
        # OneSide extrude, distance=0.515
        extrude(amount=0.515, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.209, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2642079422, perimeter: 1.8221237391
            with Locations((-1.474, 0)):
                Circle(0.29)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical sleeve or spacer with a hollow interior, featuring notched or slotted cutouts along both the top and bottom edges of the circular ends.
def model_21237_7887a24b_0002():
    """Model: Follower Guide Pin Retainer v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.4417864669, perimeter: 2.3561944902
            Circle(0.375)
        # OneSide extrude, distance=1.58
        extrude(amount=1.58)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.58), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=-2.8
        extrude(amount=-2.8, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.58), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1570796327, perimeter: 3.1415926536
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.975
        extrude(amount=-0.975, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.58), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0490873852, perimeter: 3.926990817
            with BuildLine():
                CenterArc((0, 0), 0.325, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0284168143, perimeter: 0.6919744666
            with BuildLine():
                Line((0.08, 0.366367302), (0.08, 0.1833030278))
                CenterArc((0, 0), 0.375, 77.6822340172, 24.6355319657)
                Line((-0.08, 0.1833030278), (-0.08, 0.366367302))
                CenterArc((0, 0), 0.2, 66.4218215218, 47.1563569564)
            make_face()
            # Profile area: 0.0284168143, perimeter: 0.6919744666
            with BuildLine():
                CenterArc((0, 0), 0.2, -113.5781784782, 47.1563569564)
                Line((-0.08, -0.366367302), (-0.08, -0.1833030278))
                CenterArc((0, 0), 0.375, -102.3177659828, 24.6355319657)
                Line((0.08, -0.1833030278), (0.08, -0.366367302))
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a flanged bushing or coupling adapter with a cylindrical body featuring a central bore, a radial flange on one end, and multiple rectangular slots or cutouts around its circumference for fastening or alignment purposes.
def model_21237_7887a24b_0015():
    """Model: Line Guide Head Bushing v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.5541769441, perimeter: 2.638937829
            Circle(0.42)
        # OneSide extrude, distance=0.53
        extrude(amount=0.53)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.53), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.2714336053, perimeter: 4.5238934212
            with BuildLine():
                CenterArc((0, 0), 0.42, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.08
        extrude(amount=-0.08, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.2714336053, perimeter: 4.5238934212
            with BuildLine():
                CenterArc((0, 0), 0.42, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.325
        extrude(amount=-0.325, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.53), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.101787602, perimeter: 1.1309733553
            Circle(0.18)
        # OneSide extrude, distance=-1.25
        extrude(amount=-1.25, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a mounting bracket or clamp assembly with a U-shaped upper frame featuring two cylindrical posts, a rectangular slot opening in the center, and a lower box-like base component with flanged edges for attachment.
def model_21256_433456a3_0014():
    """Model: Slider v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 14 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.9033822877, perimeter: 8.1094615923
            with BuildLine():
                Line((0.9, 0), (0.9, -0.305))
                Line((0.525, 0), (0.9, 0))
                CenterArc((0.4025, 0), 0.1225, -149.0502769211, 149.0502769211)
                Line((0.2974416829, -0.063), (-0.5224416829, -0.063))
                CenterArc((-0.6275, 0), 0.1225, 30.9497230789, 298.1005538423)
                Line((-0.5224416829, 0.063), (0.2974416829, 0.063))
                CenterArc((0.4025, 0), 0.1225, 0, 149.0502769211)
                Line((0.9, 0.305), (0.9, 0))
                Line((-0.9, 0.305), (0.9, 0.305))
                Line((-0.9, -0.305), (-0.9, 0.305))
                Line((0.9, -0.305), (-0.9, -0.305))
            make_face()
            # Profile area: 0.0235717624, perimeter: 0.6298451001
            with BuildLine():
                Line((0.28, 0), (0.525, 0))
                CenterArc((0.4025, 0), 0.1225, -180, 30.9497230789)
                CenterArc((0.4025, 0), 0.1225, -149.0502769211, 149.0502769211)
            make_face()
            # Profile area: 0.0235717624, perimeter: 0.6298451001
            with BuildLine():
                CenterArc((0.4025, 0), 0.1225, 0, 149.0502769211)
                CenterArc((0.4025, 0), 0.1225, 149.0502769211, 30.9497230789)
                Line((0.28, 0), (0.525, 0))
            make_face()
            # Profile area: 0.1003306627, perimeter: 1.9044522709
            with BuildLine():
                CenterArc((0.4025, 0), 0.1225, -180, 30.9497230789)
                CenterArc((0.4025, 0), 0.1225, 149.0502769211, 30.9497230789)
                Line((-0.5224416829, 0.063), (0.2974416829, 0.063))
                CenterArc((-0.6275, 0), 0.1225, -30.9497230789, 61.8994461577)
                Line((0.2974416829, -0.063), (-0.5224416829, -0.063))
            make_face()
            # Profile area: 0.0471435248, perimeter: 0.7696902001
            with BuildLine():
                CenterArc((-0.6275, 0), 0.1225, -30.9497230789, 61.8994461577)
                CenterArc((-0.6275, 0), 0.1225, 30.9497230789, 298.1005538423)
            make_face()
        # OneSide extrude, distance=0.33
        extrude(amount=0.33)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 14 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1003306627, perimeter: 1.9044522709
            with BuildLine():
                CenterArc((0.4025, 0), 0.1225, -180, 30.9497230789)
                CenterArc((0.4025, 0), 0.1225, 149.0502769211, 30.9497230789)
                Line((-0.5224416829, 0.063), (0.2974416829, 0.063))
                CenterArc((-0.6275, 0), 0.1225, -30.9497230789, 61.8994461577)
                Line((0.2974416829, -0.063), (-0.5224416829, -0.063))
            make_face()
        # OneSide extrude, distance=-0.65
        extrude(amount=-0.65, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 14 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0471435248, perimeter: 0.7696902001
            with BuildLine():
                CenterArc((-0.6275, 0), 0.1225, -30.9497230789, 61.8994461577)
                CenterArc((-0.6275, 0), 0.1225, 30.9497230789, 298.1005538423)
            make_face()
            # Profile area: 0.0235717624, perimeter: 0.6298451001
            with BuildLine():
                Line((0.28, 0), (0.525, 0))
                CenterArc((0.4025, 0), 0.1225, -180, 30.9497230789)
                CenterArc((0.4025, 0), 0.1225, -149.0502769211, 149.0502769211)
            make_face()
            # Profile area: 0.0235717624, perimeter: 0.6298451001
            with BuildLine():
                CenterArc((0.4025, 0), 0.1225, 0, 149.0502769211)
                CenterArc((0.4025, 0), 0.1225, 149.0502769211, 30.9497230789)
                Line((0.28, 0), (0.525, 0))
            make_face()
        # OneSide extrude, distance=0.825
        extrude(amount=0.825, mode=Mode.ADD)

        # Sketch1 -> Extrude4 (Join)
        # Sketch on XZ construction plane
        # Sketch has 14 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0471435248, perimeter: 0.7696902001
            with BuildLine():
                CenterArc((-0.6275, 0), 0.1225, -30.9497230789, 61.8994461577)
                CenterArc((-0.6275, 0), 0.1225, 30.9497230789, 298.1005538423)
            make_face()
            # Profile area: 0.0235717624, perimeter: 0.6298451001
            with BuildLine():
                Line((0.28, 0), (0.525, 0))
                CenterArc((0.4025, 0), 0.1225, -180, 30.9497230789)
                CenterArc((0.4025, 0), 0.1225, -149.0502769211, 149.0502769211)
            make_face()
            # Profile area: 0.0235717624, perimeter: 0.6298451001
            with BuildLine():
                CenterArc((0.4025, 0), 0.1225, 0, 149.0502769211)
                CenterArc((0.4025, 0), 0.1225, 149.0502769211, 30.9497230789)
                Line((0.28, 0), (0.525, 0))
            make_face()
        # OneSide extrude, distance=-0.65
        extrude(amount=-0.65, mode=Mode.ADD)

        # Sketch2 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.825, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0084281077, perimeter: 1.605353846
            with BuildLine():
                CenterArc((0.6275, 0), 0.133, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0.6275, 0), 0.1225, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0084281077, perimeter: 1.605353846
            with BuildLine():
                CenterArc((-0.4025, 0), 0.133, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-0.4025, 0), 0.1225, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0471435248, perimeter: 0.7696902001
            with Locations((0.6275, 0)):
                Circle(0.1225)
            # Profile area: 0.0471435248, perimeter: 0.7696902001
            with Locations((-0.4025, 0)):
                Circle(0.1225)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch2 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.825, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.660206276, perimeter: 5.5421236185
            with BuildLine():
                CenterArc((0.7005, 0), 0.25, -90, 180)
                Line((0.7005, 0.25), (-0.4495, 0.25))
                CenterArc((-0.4495, 0), 0.25, 90, 180)
                Line((-0.4495, -0.25), (0.7005, -0.25))
            make_face()
            with BuildLine():
                CenterArc((-0.4025, 0), 0.133, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.6275, 0), 0.133, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.125
        extrude(amount=0.125, mode=Mode.ADD)
    return part.part


# Description: This is a boat hull or marine vessel with an elongated horizontal body featuring a dark textured bow section on the left, a blue-shaded mid-section, and a raised cabin structure with windows on the right stern.
def model_21557_53eafe15_0039():
    """Model: Part 11 - Finger v1"""
    with BuildPart() as part:
        # Sketch5 -> Extrude3 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 26.8015536881, perimeter: 33.993810472
            with BuildLine():
                Line((0, 0), (12.954, 0))
                CenterArc((12.954, 1.27), 1.27, -90, 90)
                Line((14.224, 1.27), (14.224, 2.032))
                Line((13.6933755159, 3.2035920352), (14.224, 2.032))
                CenterArc((13.462, 3.0988), 0.254, 24.3661963094, 155.6338036906)
                Line((13.208, 1.8288), (13.208, 3.0988))
                Line((0, 1.8288), (13.208, 1.8288))
                Line((0, 0), (0, 1.8288))
            make_face()
        # TwoSides extrude (symmetric), distance=1.27
        extrude(amount=1.27, both=True)

        # Sketch6 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 9 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.27, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.3380912785, perimeter: 17.2390023743
            with BuildLine():
                CenterArc((-13.8338818102, -0.762), 0.254, 61.0449756281, 88.9550243719)
                CenterArc((-13.5879473678, -0.3175), 0.254, -118.9550243719, 33.0457998254)
                Line((-5.588, 0), (-13.5698278062, -0.5708528794))
                Line((-5.588, 0), (-12.954, 0))
                CenterArc((-12.954, -1.27), 1.27, 90, 60)
            make_face()
        # OneSide extrude, distance=-0.889
        extrude(amount=-0.889, mode=Mode.SUBTRACT)

        # Sketch8 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 9 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -1.27, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 2.3380912785, perimeter: 17.2390023743
            with BuildLine():
                Line((5.588, 0), (13.5698278062, -0.5708528794))
                CenterArc((13.5879473678, -0.3175), 0.254, -94.0907754535, 33.0457998254)
                CenterArc((13.8338818102, -0.762), 0.254, 30, 88.9550243719)
                CenterArc((12.954, -1.27), 1.27, 30, 60)
                Line((5.588, 0), (12.954, 0))
            make_face()
        # OneSide extrude, distance=-0.889
        extrude(amount=-0.889, mode=Mode.SUBTRACT)

        # Sketch9 -> Extrude6 (Cut)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.4932493285, perimeter: 2.4896493461
            with Locations((4.3180001378, 0)):
                Circle(0.39624)
            # Profile area: 0.4932493285, perimeter: 2.4896493461
            with Locations((1.2700000405, 0)):
                Circle(0.39624)
            # Profile area: 5.032248, perimeter: 28.9709282739
            with BuildLine():
                Line((0, -0.762), (5.588, -0.762))
                Line((0, -1.27), (0, -0.762))
                Line((14.224, -1.27), (0, -1.27))
                Line((5.588, -0.762), (14.224, -1.27))
            make_face()
            # Profile area: 2.838704, perimeter: 12.192
            with BuildLine():
                Line((0, 0.762), (5.588, 0.762))
                Line((5.588, 0.762), (5.588, 1.27))
                Line((5.588, 1.27), (0, 1.27))
                Line((0, 0.762), (0, 1.27))
            make_face()
            # Profile area: 2.193544, perimeter: 17.7949282739
            with BuildLine():
                Line((5.588, 0.762), (5.588, 1.27))
                Line((5.588, 0.762), (14.224, 1.27))
                Line((14.224, 1.27), (5.588, 1.27))
            make_face()
        # OneSide extrude, distance=-5.08
        extrude(amount=-5.08, mode=Mode.SUBTRACT)

        # Sketch10 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 76 constraints, 17 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.762, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.01161288, perimeter: 0.5203261469
            with BuildLine():
                Line((-1.4930032088, -1.8288), (-1.2774770619, -1.8288))
                Line((-1.3852401353, -1.7210369265), (-1.2774770619, -1.8288))
                Line((-1.4930032088, -1.8288), (-1.3852401353, -1.7210369265))
            make_face()
            # Profile area: 0.01161288, perimeter: 0.5203261469
            with BuildLine():
                Line((-1.7085293557, -1.8288), (-1.4930032088, -1.8288))
                Line((-1.6007662822, -1.7210369265), (-1.4930032088, -1.8288))
                Line((-1.7085293557, -1.8288), (-1.6007662822, -1.7210369265))
            make_face()
            # Profile area: 0.01161288, perimeter: 0.5203261469
            with BuildLine():
                Line((-1.9240555026, -1.8288), (-1.7085293557, -1.8288))
                Line((-1.8162924292, -1.7210369265), (-1.7085293557, -1.8288))
                Line((-1.9240555026, -1.8288), (-1.8162924292, -1.7210369265))
            make_face()
            # Profile area: 0.01161288, perimeter: 0.5203261469
            with BuildLine():
                Line((-2.1395816495, -1.8288), (-1.9240555026, -1.8288))
                Line((-2.0318185761, -1.7210369265), (-1.9240555026, -1.8288))
                Line((-2.1395816495, -1.8288), (-2.0318185761, -1.7210369265))
            make_face()
            # Profile area: 0.01161288, perimeter: 0.5203261469
            with BuildLine():
                Line((-2.3551077964, -1.8288), (-2.1395816495, -1.8288))
                Line((-2.1395816495, -1.8288), (-2.247344723, -1.7210369265))
                Line((-2.247344723, -1.7210369265), (-2.3551077964, -1.8288))
            make_face()
            # Profile area: 0.01161288, perimeter: 0.5203261469
            with BuildLine():
                Line((-2.5706339433, -1.8288), (-2.3551077964, -1.8288))
                Line((-2.3551077964, -1.8288), (-2.4628708699, -1.7210369265))
                Line((-2.4628708699, -1.7210369265), (-2.5706339433, -1.8288))
            make_face()
            # Profile area: 0.01161288, perimeter: 0.5203261469
            with BuildLine():
                Line((-2.7861600902, -1.8288), (-2.5706339433, -1.8288))
                Line((-2.5706339433, -1.8288), (-2.6783970168, -1.7210369265))
                Line((-2.6783970168, -1.7210369265), (-2.7861600902, -1.8288))
            make_face()
            # Profile area: 0.01161288, perimeter: 0.5203261469
            with BuildLine():
                Line((-3.0016862371, -1.8288), (-2.7861600902, -1.8288))
                Line((-2.7861600902, -1.8288), (-2.8939231637, -1.7210369265))
                Line((-2.8939231637, -1.7210369265), (-3.0016862371, -1.8288))
            make_face()
            # Profile area: 0.01161288, perimeter: 0.5203261469
            with BuildLine():
                Line((-3.217212384, -1.8288), (-3.0016862371, -1.8288))
                Line((-3.1094493106, -1.7210369265), (-3.0016862371, -1.8288))
                Line((-3.217212384, -1.8288), (-3.1094493106, -1.7210369265))
            make_face()
            # Profile area: 0.01161288, perimeter: 0.5203261469
            with BuildLine():
                Line((-3.4327385309, -1.8288), (-3.217212384, -1.8288))
                Line((-3.3249754575, -1.7210369265), (-3.217212384, -1.8288))
                Line((-3.4327385309, -1.8288), (-3.3249754575, -1.7210369265))
            make_face()
            # Profile area: 0.01161288, perimeter: 0.5203261469
            with BuildLine():
                Line((-3.6482646778, -1.8288), (-3.4327385309, -1.8288))
                Line((-3.5405016044, -1.7210369265), (-3.4327385309, -1.8288))
                Line((-3.6482646778, -1.8288), (-3.5405016044, -1.7210369265))
            make_face()
            # Profile area: 0.01161288, perimeter: 0.5203261469
            with BuildLine():
                Line((-3.8637908248, -1.8288), (-3.6482646778, -1.8288))
                Line((-3.7560277513, -1.7210369265), (-3.6482646778, -1.8288))
                Line((-3.8637908248, -1.8288), (-3.7560277513, -1.7210369265))
            make_face()
            # Profile area: 0.01161288, perimeter: 0.5203261469
            with BuildLine():
                Line((-4.0793169717, -1.8288), (-3.8637908248, -1.8288))
                Line((-3.8637908248, -1.8288), (-3.9715538982, -1.7210369265))
                Line((-3.9715538982, -1.7210369265), (-4.0793169717, -1.8288))
            make_face()
            # Profile area: 0.01161288, perimeter: 0.5203261469
            with BuildLine():
                Line((-4.2948431186, -1.8288), (-4.0793169717, -1.8288))
                Line((-4.0793169717, -1.8288), (-4.1870800451, -1.7210369265))
                Line((-4.1870800451, -1.7210369265), (-4.2948431186, -1.8288))
            make_face()
            # Profile area: 0.01161288, perimeter: 0.5203261469
            with BuildLine():
                Line((-4.5103692655, -1.8288), (-4.2948431186, -1.8288))
                Line((-4.2948431186, -1.8288), (-4.402606192, -1.7210369265))
                Line((-4.402606192, -1.7210369265), (-4.5103692655, -1.8288))
            make_face()
            # Profile area: 0.01161288, perimeter: 0.5203261469
            with BuildLine():
                Line((-4.7258954124, -1.8288), (-4.5103692655, -1.8288))
                Line((-4.5103692655, -1.8288), (-4.6181323389, -1.7210369265))
                Line((-4.6181323389, -1.7210369265), (-4.7258954124, -1.8288))
            make_face()
            # Profile area: 0.01161288, perimeter: 0.5203261469
            with BuildLine():
                Line((-4.9414215593, -1.8288), (-4.7258954124, -1.8288))
                Line((-4.8336584858, -1.7210369265), (-4.7258954124, -1.8288))
                Line((-4.9414215593, -1.8288), (-4.8336584858, -1.7210369265))
            make_face()
            # Profile area: 0.01161288, perimeter: 0.5203261469
            with BuildLine():
                Line((-5.1569477062, -1.8288), (-4.9414215593, -1.8288))
                Line((-5.0491846327, -1.7210369265), (-4.9414215593, -1.8288))
                Line((-5.1569477062, -1.8288), (-5.0491846327, -1.7210369265))
            make_face()
            # Profile area: 0.01161288, perimeter: 0.5203261469
            with BuildLine():
                Line((-5.3724738531, -1.8288), (-5.1569477062, -1.8288))
                Line((-5.2647107796, -1.7210369265), (-5.1569477062, -1.8288))
                Line((-5.3724738531, -1.8288), (-5.2647107796, -1.7210369265))
            make_face()
            # Profile area: 0.01161288, perimeter: 0.5203261469
            with BuildLine():
                Line((-5.588, -1.8288), (-5.3724738531, -1.8288))
                Line((-5.4802369265, -1.7210369265), (-5.3724738531, -1.8288))
                Line((-5.588, -1.8288), (-5.4802369265, -1.7210369265))
            make_face()
            # Profile area: 0.0114899516, perimeter: 0.4981515334
            with BuildLine():
                Line((-0.1998463274, -1.8288), (0, -1.8288))
                Line((0, -1.8288), (0, -1.8131201805))
                Line((-0.0920832539, -1.7210369265), (0, -1.8131201805))
                Line((-0.1998463274, -1.8288), (-0.0920832539, -1.7210369265))
            make_face()
            # Profile area: 0.01161288, perimeter: 0.5203261469
            with BuildLine():
                Line((-0.4153724743, -1.8288), (-0.1998463274, -1.8288))
                Line((-0.3076094008, -1.7210369265), (-0.1998463274, -1.8288))
                Line((-0.4153724743, -1.8288), (-0.3076094008, -1.7210369265))
            make_face()
            # Profile area: 0.01161288, perimeter: 0.5203261469
            with BuildLine():
                Line((-0.6308986212, -1.8288), (-0.4153724743, -1.8288))
                Line((-0.4153724743, -1.8288), (-0.5231355477, -1.7210369265))
                Line((-0.5231355477, -1.7210369265), (-0.6308986212, -1.8288))
            make_face()
            # Profile area: 0.01161288, perimeter: 0.5203261469
            with BuildLine():
                Line((-0.8464247681, -1.8288), (-0.6308986212, -1.8288))
                Line((-0.6308986212, -1.8288), (-0.7386616946, -1.7210369265))
                Line((-0.7386616946, -1.7210369265), (-0.8464247681, -1.8288))
            make_face()
            # Profile area: 0.01161288, perimeter: 0.5203261469
            with BuildLine():
                Line((-1.061950915, -1.8288), (-0.8464247681, -1.8288))
                Line((-0.8464247681, -1.8288), (-0.9541878415, -1.7210369265))
                Line((-0.9541878415, -1.7210369265), (-1.061950915, -1.8288))
            make_face()
            # Profile area: 0.01161288, perimeter: 0.5203261469
            with BuildLine():
                Line((-1.1697139884, -1.7210369265), (-1.2774770619, -1.8288))
                Line((-1.2774770619, -1.8288), (-1.061950915, -1.8288))
                Line((-1.061950915, -1.8288), (-1.1697139884, -1.7210369265))
            make_face()
            # Profile area: 0.0114899516, perimeter: 0.4981515334
            with BuildLine():
                Line((0, -0.0156798195), (0, 0))
                Line((0, 0), (-0.1998463274, 0))
                Line((-0.1998463274, 0), (-0.0920832539, -0.1077630735))
                Line((-0.0920832539, -0.1077630735), (0, -0.0156798195))
            make_face()
            # Profile area: 0.01161288, perimeter: 0.5203261469
            with BuildLine():
                Line((-5.3724738531, 0), (-5.588, 0))
                Line((-5.588, 0), (-5.4802369265, -0.1077630735))
                Line((-5.4802369265, -0.1077630735), (-5.3724738531, 0))
            make_face()
            # Profile area: 0.01161288, perimeter: 0.5203261469
            with BuildLine():
                Line((-5.1569477062, 0), (-5.3724738531, 0))
                Line((-5.3724738531, 0), (-5.2647107796, -0.1077630735))
                Line((-5.2647107796, -0.1077630735), (-5.1569477062, 0))
            make_face()
            # Profile area: 0.01161288, perimeter: 0.5203261469
            with BuildLine():
                Line((-4.9414215593, 0), (-5.1569477062, 0))
                Line((-5.1569477062, 0), (-5.0491846327, -0.1077630735))
                Line((-5.0491846327, -0.1077630735), (-4.9414215593, 0))
            make_face()
            # Profile area: 0.01161288, perimeter: 0.5203261469
            with BuildLine():
                Line((-4.7258954124, 0), (-4.9414215593, 0))
                Line((-4.9414215593, 0), (-4.8336584858, -0.1077630735))
                Line((-4.8336584858, -0.1077630735), (-4.7258954124, 0))
            make_face()
            # Profile area: 0.01161288, perimeter: 0.5203261469
            with BuildLine():
                Line((-4.5103692655, 0), (-4.7258954124, 0))
                Line((-4.6181323389, -0.1077630735), (-4.7258954124, 0))
                Line((-4.5103692655, 0), (-4.6181323389, -0.1077630735))
            make_face()
            # Profile area: 0.01161288, perimeter: 0.5203261469
            with BuildLine():
                Line((-4.2948431186, 0), (-4.5103692655, 0))
                Line((-4.402606192, -0.1077630735), (-4.5103692655, 0))
                Line((-4.2948431186, 0), (-4.402606192, -0.1077630735))
            make_face()
            # Profile area: 0.01161288, perimeter: 0.5203261469
            with BuildLine():
                Line((-4.0793169717, 0), (-4.2948431186, 0))
                Line((-4.1870800451, -0.1077630735), (-4.2948431186, 0))
                Line((-4.0793169717, 0), (-4.1870800451, -0.1077630735))
            make_face()
            # Profile area: 0.01161288, perimeter: 0.5203261469
            with BuildLine():
                Line((-3.8637908248, 0), (-4.0793169717, 0))
                Line((-3.9715538982, -0.1077630735), (-4.0793169717, 0))
                Line((-3.8637908248, 0), (-3.9715538982, -0.1077630735))
            make_face()
            # Profile area: 0.01161288, perimeter: 0.5203261469
            with BuildLine():
                Line((-3.6482646778, 0), (-3.8637908248, 0))
                Line((-3.8637908248, 0), (-3.7560277513, -0.1077630735))
                Line((-3.7560277513, -0.1077630735), (-3.6482646778, 0))
            make_face()
            # Profile area: 0.01161288, perimeter: 0.5203261469
            with BuildLine():
                Line((-3.4327385309, 0), (-3.6482646778, 0))
                Line((-3.6482646778, 0), (-3.5405016044, -0.1077630735))
                Line((-3.5405016044, -0.1077630735), (-3.4327385309, 0))
            make_face()
            # Profile area: 0.01161288, perimeter: 0.5203261469
            with BuildLine():
                Line((-3.217212384, 0), (-3.4327385309, 0))
                Line((-3.4327385309, 0), (-3.3249754575, -0.1077630735))
                Line((-3.3249754575, -0.1077630735), (-3.217212384, 0))
            make_face()
            # Profile area: 0.01161288, perimeter: 0.5203261469
            with BuildLine():
                Line((-3.0016862371, 0), (-3.217212384, 0))
                Line((-3.217212384, 0), (-3.1094493106, -0.1077630735))
                Line((-3.1094493106, -0.1077630735), (-3.0016862371, 0))
            make_face()
            # Profile area: 0.01161288, perimeter: 0.5203261469
            with BuildLine():
                Line((-2.7861600902, 0), (-3.0016862371, 0))
                Line((-2.8939231637, -0.1077630735), (-3.0016862371, 0))
                Line((-2.7861600902, 0), (-2.8939231637, -0.1077630735))
            make_face()
            # Profile area: 0.01161288, perimeter: 0.5203261469
            with BuildLine():
                Line((-2.5706339433, 0), (-2.7861600902, 0))
                Line((-2.6783970168, -0.1077630735), (-2.7861600902, 0))
                Line((-2.5706339433, 0), (-2.6783970168, -0.1077630735))
            make_face()
            # Profile area: 0.01161288, perimeter: 0.5203261469
            with BuildLine():
                Line((-2.3551077964, 0), (-2.5706339433, 0))
                Line((-2.4628708699, -0.1077630735), (-2.5706339433, 0))
                Line((-2.3551077964, 0), (-2.4628708699, -0.1077630735))
            make_face()
            # Profile area: 0.01161288, perimeter: 0.5203261469
            with BuildLine():
                Line((-2.1395816495, 0), (-2.3551077964, 0))
                Line((-2.247344723, -0.1077630735), (-2.3551077964, 0))
                Line((-2.1395816495, 0), (-2.247344723, -0.1077630735))
            make_face()
            # Profile area: 0.01161288, perimeter: 0.5203261469
            with BuildLine():
                Line((-1.9240555026, 0), (-2.1395816495, 0))
                Line((-2.1395816495, 0), (-2.0318185761, -0.1077630735))
                Line((-2.0318185761, -0.1077630735), (-1.9240555026, 0))
            make_face()
            # Profile area: 0.01161288, perimeter: 0.5203261469
            with BuildLine():
                Line((-1.7085293557, 0), (-1.9240555026, 0))
                Line((-1.9240555026, 0), (-1.8162924292, -0.1077630735))
                Line((-1.8162924292, -0.1077630735), (-1.7085293557, 0))
            make_face()
            # Profile area: 0.01161288, perimeter: 0.5203261469
            with BuildLine():
                Line((-1.4930032088, 0), (-1.7085293557, 0))
                Line((-1.7085293557, 0), (-1.6007662822, -0.1077630735))
                Line((-1.6007662822, -0.1077630735), (-1.4930032088, 0))
            make_face()
            # Profile area: 0.01161288, perimeter: 0.5203261469
            with BuildLine():
                Line((-1.2774770619, 0), (-1.4930032088, 0))
                Line((-1.4930032088, 0), (-1.3852401353, -0.1077630735))
                Line((-1.3852401353, -0.1077630735), (-1.2774770619, 0))
            make_face()
            # Profile area: 0.01161288, perimeter: 0.5203261469
            with BuildLine():
                Line((-1.061950915, 0), (-1.2774770619, 0))
                Line((-1.1697139884, -0.1077630735), (-1.2774770619, 0))
                Line((-1.061950915, 0), (-1.1697139884, -0.1077630735))
            make_face()
            # Profile area: 0.01161288, perimeter: 0.5203261469
            with BuildLine():
                Line((-0.8464247681, 0), (-1.061950915, 0))
                Line((-0.9541878415, -0.1077630735), (-1.061950915, 0))
                Line((-0.8464247681, 0), (-0.9541878415, -0.1077630735))
            make_face()
            # Profile area: 0.01161288, perimeter: 0.5203261469
            with BuildLine():
                Line((-0.6308986212, 0), (-0.8464247681, 0))
                Line((-0.7386616946, -0.1077630735), (-0.8464247681, 0))
                Line((-0.6308986212, 0), (-0.7386616946, -0.1077630735))
            make_face()
            # Profile area: 0.01161288, perimeter: 0.5203261469
            with BuildLine():
                Line((-0.4153724743, 0), (-0.6308986212, 0))
                Line((-0.5231355477, -0.1077630735), (-0.6308986212, 0))
                Line((-0.4153724743, 0), (-0.5231355477, -0.1077630735))
            make_face()
            # Profile area: 0.01161288, perimeter: 0.5203261469
            with BuildLine():
                Line((-0.1998463274, 0), (-0.4153724743, 0))
                Line((-0.4153724743, 0), (-0.3076094008, -0.1077630735))
                Line((-0.3076094008, -0.1077630735), (-0.1998463274, 0))
            make_face()
        # OneSide extrude, distance=-5.08
        extrude(amount=-5.08, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a tapered cylindrical sleeve or cone-shaped housing with a rounded top end, featuring a vertical slot or opening running along one side and a flange or lip at the base, likely designed as a protective cover or connector component.
def model_21626_b34008e6_0003():
    """Model: Flywheel Post v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 10 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 32.0415095631, perimeter: 22.8245823579
            with BuildLine():
                Line((-3.2, 0), (3.2, 0))
                Line((3.2, 0), (3.2, 0.6))
                Line((3.2, 0.6), (1.6781610859, 5.7462613925))
                CenterArc((0, 5.25), 1.75, 16.4738638733, 147.0522722534)
                Line((-3.2, 0.6), (-1.6781610859, 5.7462613925))
                Line((-3.2, 0), (-3.2, 0.6))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch4 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.0104624736, perimeter: 4.3106860415
            with BuildLine():
                CenterArc((-0.5809475019, 5.85), 0.3, -43.4325463736, 180.0000796347)
                CenterArc((0, 5.3), 1.1, 136.5674824844, 86.8650349772)
                CenterArc((-0.5809475019, 4.75), 0.3, -136.5675334618, 180.0000723696)
                CenterArc((0, 5.3), 0.5, 136.5674693317, 86.8650658161)
            make_face()
        # OneSide extrude, distance=-0.25
        extrude(amount=-0.25, mode=Mode.SUBTRACT)
    return part.part


# Description: A symmetrical dumbbell consisting of a long cylindrical bar with enlarged rounded grip sections at each end.
def model_21638_0a984848_0029():
    """Model: connecting rod v1 (10)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5890486225, perimeter: 4.7123889804
            with BuildLine():
                CenterArc((0, 0), 0.5, 53.1301023542, 253.7397952917)
                CenterArc((0, 0), 0.5, -53.1301023542, 106.2602047083)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 4.096352391, perimeter: 12.654590436
            with BuildLine():
                CenterArc((0, 0), 0.5, -53.1301023542, 106.2602047083)
                Line((0.3, -0.4), (5.7, -0.4))
                CenterArc((6, 0), 0.5, 126.8698976458, 106.2602047083)
                Line((0.3, 0.4), (5.7, 0.4))
            make_face()
            # Profile area: 0.5890486225, perimeter: 4.7123889804
            with BuildLine():
                CenterArc((6, 0), 0.5, 126.8698976458, 106.2602047083)
                CenterArc((6, 0), 0.5, -126.8698976458, 253.7397952917)
            make_face()
            with BuildLine():
                CenterArc((6, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.4), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.62, perimeter: 11.4
            with BuildLine():
                Line((5.7, 0.7), (5.7, 1))
                Line((5.7, 1), (0.3, 1))
                Line((0.3, 0.7), (0.3, 1))
                Line((0.3, 0.7), (5.7, 0.7))
            make_face()
            # Profile area: 1.62, perimeter: 11.4
            with BuildLine():
                Line((0.3, 0), (0.3, 0.3))
                Line((0.3, 0), (5.7, 0))
                Line((5.7, 0), (5.7, 0.3))
                Line((0.3, 0.3), (5.7, 0.3))
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1118238045, perimeter: 1.727295218
            with BuildLine():
                Line((-5.7, -0.4), (-5.7, 0.4))
                CenterArc((-6, 0), 0.5, -53.1301023542, 106.2602047083)
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1118238045, perimeter: 1.727295218
            with BuildLine():
                Line((-0.3, 0.4), (-0.3, -0.4))
                CenterArc((0, 0), 0.5, 126.8698976458, 106.2602047083)
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.ADD)
    return part.part


# Description: This is a hexagonal or polygonal speaker enclosure with a dark blue/navy finish, featuring a circular speaker driver mounted on one angled face and a wireframe-textured top surface, designed as a compact directional audio device.
def model_21642_b79d233e_0012():
    """Model: Carburetor Housing v2"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.37970556, perimeter: 7.361
            with BuildLine():
                Line((0.87885, -0.9614), (0.87885, 0.9614))
                Line((0.87885, 0.9614), (-0.87885, 0.9614))
                Line((-0.87885, 0.9614), (-0.87885, -0.9614))
                Line((-0.87885, -0.9614), (0.87885, -0.9614))
            make_face()
        # OneSide extrude, distance=1.3157
        extrude(amount=1.3157)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.87885, 0, 0), x_dir=(0, -1, 0), z_dir=(-1, 0, 0))):
            # Profile area: 1.0260826452, perimeter: 3.5908404031
            with Locations((0, 0.65785)):
                Circle(0.5715)
        # OneSide extrude, distance=0.16
        extrude(amount=0.16, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-1.03885, 0, 0), x_dir=(0, -1, 0), z_dir=(-1, 0, 0))):
            # Profile area: 0.4955364547, perimeter: 7.9636232176
            with BuildLine():
                CenterArc((0, 0.65785), 0.69595, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0.65785), 0.5715, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.0260826452, perimeter: 3.5908404031
            with Locations((0, 0.65785)):
                Circle(0.5715)
        # OneSide extrude, distance=0.0686
        extrude(amount=0.0686, mode=Mode.ADD)
    return part.part


# Description: This is a trapezoidal box-shaped component with an open top, featuring internal ribbing and structural reinforcements, and angled side walls that taper toward one end.
def model_21644_aa203dc5_0011():
    """Model: PT-201-P-016 v2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 10.5, perimeter: 13
            with BuildLine():
                Line((-1.75, 1.5), (1.75, 1.5))
                Line((-1.75, -1.5), (-1.75, 1.5))
                Line((1.75, -1.5), (-1.75, -1.5))
                Line((1.75, 1.5), (1.75, -1.5))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.1963703568, perimeter: 9.3979265327
            with BuildLine():
                Line((1.75, 0.3), (-1.75, 0.3020740818))
                Line((1.75, 1.5), (1.75, 0.3))
                Line((1.75, 1.5), (-1.75, 1.5))
                Line((-1.75, 1.5), (-1.75, 0.3020740818))
            make_face()
        # OneSide extrude, distance=0.45
        extrude(amount=0.45, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.072033409, perimeter: 1.1601670798
            with BuildLine():
                Line((1.503, 0.95), (1.3228329551, 0.95))
                Line((1.323, 0.55), (1.3228329551, 0.95))
                Line((1.503, 0.55), (1.323, 0.55))
                Line((1.503, 0.95), (1.503, 0.55))
            make_face()
            # Profile area: 0.072, perimeter: 1.16
            with BuildLine():
                Line((-0.7327893525, 0.55), (-0.7327893525, 0.95))
                Line((-0.5527893525, 0.55), (-0.7327893525, 0.55))
                Line((-0.5527893525, 0.95), (-0.5527893525, 0.55))
                Line((-0.7327893525, 0.95), (-0.5527893525, 0.95))
            make_face()
        # OneSide extrude, distance=-1.7
        extrude(amount=-1.7, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.0509348792, perimeter: 7.6005342575
            with BuildLine():
                Line((-1.75, -1.5), (1.75, -1.5))
                Line((1.75, -1.5), (1.75, -1.2))
                Line((1.75, -1.2), (-1.75, -1.1994657833))
                Line((-1.75, -1.1994657833), (-1.75, -1.5))
            make_face()
        # OneSide extrude, distance=0.05
        extrude(amount=0.05, mode=Mode.ADD)
    return part.part


# Description: This is a rectangular hollow structural frame or enclosure with an open interior channel, featuring multiple rectangular window/slot openings on its sides and a peaked roof-like top section.
def model_21734_7cf58bd0_0000():
    """Model: STEAM CHEST v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 9 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 17.695, perimeter: 30.8
            with BuildLine():
                Line((-3.8, 6.35), (0, 6.35))
                Line((-3.8, 0), (-3.8, 6.35))
                Line((0, 0), (-3.8, 0))
                Line((0, 6.35), (0, 0))
            make_face()
            with BuildLine():
                Line((-0.925, 4.825), (-0.925, 1.525))
                Line((-0.925, 1.525), (-2.875, 1.525))
                Line((-2.875, 1.525), (-2.875, 4.825))
                Line((-2.875, 4.825), (-0.925, 4.825))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.7
        extrude(amount=1.7)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 20 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1.7, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1590431281, perimeter: 1.4137166941
            with Locations((-3.3375, 5.725)):
                Circle(0.225)
            # Profile area: 0.1590431281, perimeter: 1.4137166941
            with Locations((-3.3375, 4.025)):
                Circle(0.225)
            # Profile area: 0.1590431281, perimeter: 1.4137166941
            with Locations((-3.3375, 2.325)):
                Circle(0.225)
            # Profile area: 0.1590431281, perimeter: 1.4137166941
            with Locations((-3.3375, 0.625)):
                Circle(0.225)
            # Profile area: 0.1590431281, perimeter: 1.4137166941
            with Locations((-0.4625, 0.625)):
                Circle(0.225)
            # Profile area: 0.1590431281, perimeter: 1.4137166941
            with Locations((-0.4624991494, 2.325)):
                Circle(0.225)
            # Profile area: 0.1590431281, perimeter: 1.4137166941
            with Locations((-0.4624983688, 4.025)):
                Circle(0.225)
            # Profile area: 0.1590431281, perimeter: 1.4137166941
            with Locations((-0.4624994355, 5.725)):
                Circle(0.225)
        # OneSide extrude, distance=-4.6
        extrude(amount=-4.6, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 6.35, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2042820623, perimeter: 1.6022122533
            with Locations((-0.85, 1.9)):
                Circle(0.255)
        # OneSide extrude, distance=-3.9
        extrude(amount=-3.9, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a shaft collar or coupling connector with a cylindrical body featuring a horizontal through-hole and a central square or rectangular slot, designed to mount onto and secure a shaft or rod.
def model_21734_7cf58bd0_0004():
    """Model: PISTON ROD v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.2004085081, perimeter: 6.5061009831
            with BuildLine():
                CenterArc((-2.1847915983, 0.17186056), 1.25, 68.8998039759, 42.2003920482)
                Line((-2.6347915983, 1.338050939), (-2.6347915983, -0.994329819))
                CenterArc((-2.1847915983, 0.17186056), 1.25, -111.1001960241, 42.2003920482)
                Line((-1.7347915983, -0.994329819), (-1.7347915983, 1.338050939))
            make_face()
        # OneSide extrude, distance=2.3
        extrude(amount=2.3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(2.3, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-2.1847915983, 0.17186056)):
                Circle(0.3)
        # OneSide extrude, distance=7.65
        extrude(amount=7.65, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((2.1847915983, 0.17186056)):
                Circle(0.3)
        # OneSide extrude, distance=7.55
        extrude(amount=7.55, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(9.95, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-2.1847915983, 0.17186056)):
                Circle(0.25)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)

        # Sketch6 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 13 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.6347915983), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 2.0902659527, perimeter: 6.28225567
            with BuildLine():
                CenterArc((0.5, -0.42813944), 0.15, 90, 180)
                Line((0.5, -0.57813944), (1.8, -0.57813944))
                CenterArc((1.8, -0.42813944), 0.15, -90, 180)
                Line((1.8, -0.27813944), (1.8, 0.62186056))
                CenterArc((1.8, 0.77186056), 0.15, -90, 180)
                Line((1.8, 0.92186056), (0.5, 0.92186056))
                CenterArc((0.5, 0.7742256086), 0.1476349514, 90, 180)
                Line((0.5, 0.6265906572), (0.5, -0.27813944))
            make_face()
        # OneSide extrude, distance=-2.5
        extrude(amount=-2.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a dark gray/blue molded enclosure or housing component with a rounded, organic blob-like shape featuring multiple circular holes or ports distributed across its surface and mesh or perforated areas on the top.
def model_21773_01f6bc23_0016():
    """Model: Gland v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 11 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 32.161565366, perimeter: 21.9696570441
            with BuildLine():
                CenterArc((-1.2360525946, 0.1402808362), 1.0000000002, 119.2303384669, 121.8790959443)
                Line((0.9595297831, -2.2133504254), (-1.719190816, -0.7352632571))
                CenterArc((2.2639320222, 0.1506577807), 2.7, -118.8888457712, 58.1179817233)
                Line((6.2522198238, -0.711639326), (3.582351453, -2.2055616922))
                CenterArc((5.7639166394, 0.1610347255), 1, -60.7708843009, 121.8801778696)
                Line((3.5683824818, 2.5146393795), (6.247057013, 1.036577631))
                CenterArc((2.2639320222, 0.1506577807), 2.7000000002, 61.1099855178, 58.1198726729)
                Line((-1.724374403, 1.0129444666), (0.9454828903, 2.5068606343))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((5.7639166394, 0.1610347255)):
                Circle(0.5)
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-1.2360525946, 0.1402808362)):
                Circle(0.5)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((2.2639320222, 0.1506577807)):
                Circle(1)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 10.7128309487, perimeter: 19.4778744523
            with BuildLine():
                CenterArc((2.2639320222, 0.1506577807), 2.1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((2.2639320222, 0.1506577807), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


# Description: This is a motorcycle or ATV seat cover featuring an elongated, curved body with blue and black color panels, ribbed surface texturing, and a contoured design that wraps around the seat base with tapered ends.
def model_21783_c6677b21_0002():
    """Model: Support Plate (2) v8 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 11 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 84.8015085986, perimeter: 36.1638712303
            with BuildLine():
                CenterArc((0.0219524062, 9.4311460017), 1.8859946157, 25.7328957912, 128.6956999315)
                Line((-5.3618027531, 2.6154442559), (-1.6793053847, 10.245208419))
                CenterArc((-3.7806917552, 1.7559957152), 1.7996010063, 151.4727109283, 118.5152405537)
                Line((3.8189298115, -0.0437734794), (-3.7810701866, -0.0436052513))
                CenterArc((3.7287073552, 1.8098604682), 1.8558283604, -87.2134252635, 112.9463210547)
                Line((1.7209089599, 10.2500002739), (5.4004893047, 2.6156172656))
            make_face()
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with Locations((0.0216350872, 9.6563098615)):
                Circle(0.75)
        # OneSide extrude, distance=6
        extrude(amount=6, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((0, 1.3999999992)):
                Circle(0.3)
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with Locations((3.8188927862, 1.7562265206)):
                Circle(0.75)
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with Locations((-3.7806917552, 1.7559957152)):
                Circle(0.75)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-1.5999292913, 4.1173917536)):
                Circle(0.3)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((1.6000707087, 4.1999999992)):
                Circle(0.3)
        # OneSide extrude, distance=3.5
        extrude(amount=3.5, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.7, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.9087385212, perimeter: 7.853981634
            with Locations((-0.0000708329, -3.1999999992)):
                Circle(1.25)
        # OneSide extrude, distance=-5
        extrude(amount=-5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cross-shaped connector or junction piece featuring a horizontal bar intersected by a diagonal bar at approximately 45 degrees, with rounded ends and a cylindrical form suggesting it functions as a joining or mounting component.
def model_21799_0d47cdac_0002():
    """Model: Guide v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 11 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 69.4247779608, perimeter: 138.8495559215
            with BuildLine():
                CenterArc((0, 15), 2, 0, 180)
                Line((-2, 15), (-2, -15))
                CenterArc((0, -15), 2, 180, 180)
                Line((2, -15), (2, 15))
            make_face()
            with BuildLine():
                Line((1, -15), (1, 15))
                CenterArc((0, -15), 1, 180, 180)
                Line((-1, 15), (-1, -15))
                CenterArc((0, 15), 1, 0, 180)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.75
        extrude(amount=0.75, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4.5, perimeter: 9
            with BuildLine():
                Line((-0.75, 1.5), (-0.75, -1.5))
                Line((-0.75, -1.5), (0.75, -1.5))
                Line((0.75, -1.5), (0.75, 1.5))
                Line((0.75, 1.5), (-0.75, 1.5))
            make_face()
        # Symmetric extrude, each_side=4
        extrude(amount=4, both=True, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 0.75), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 6, perimeter: 10
            with BuildLine():
                Line((-1, 1.5), (1, 1.5))
                Line((-1, -1.5), (-1, 1.5))
                Line((1, -1.5), (-1, -1.5))
                Line((1, 1.5), (1, -1.5))
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-4, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with BuildLine():
                CenterArc((0, 0), 0.75, 0, 180)
                CenterArc((0, 0), 0.75, -180, 180)
            make_face()
        # OneSide extrude, distance=30
        extrude(amount=30, mode=Mode.ADD)

        # Sketch6 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(4, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with BuildLine():
                CenterArc((0, 0), 0.75, 0, 180)
                CenterArc((0, 0), 0.75, -180, 180)
            make_face()
        # OneSide extrude, distance=30
        extrude(amount=30, mode=Mode.ADD)
    return part.part


# Description: This is a tire and wheel assembly consisting of a large oval/circular tire with a textured tread pattern surrounding a central hub, featuring a single spoke connecting the rim to the center hub.
def model_21803_8a36dcda_0017():
    """Model: Flywheel_V2 v5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 68.3296402156, perimeter: 91.1061869541
            with BuildLine():
                CenterArc((0, 0), 8, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 6.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=1.3
        extrude(amount=1.3, both=True)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 5.3092915846, perimeter: 8.1681408993
            Circle(1.3)
        # Symmetric extrude, each_side=1.8
        extrude(amount=1.8, both=True)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 11.9694680102, perimeter: 79.7964534012
            with BuildLine():
                CenterArc((0, 0), 6.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 6.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.2959069696, perimeter: 17.2787595947
            with BuildLine():
                CenterArc((0, 0), 1.45, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.5
        extrude(amount=0.5, both=True, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.3777738874, perimeter: 10.5360212132
            with BuildLine():
                Line((-0.2566763312, 1.4271009989), (-0.2566763312, 6.1946845974))
                CenterArc((0, 0), 1.45, 80.3395211491, 19.856602814)
                Line((0.2433236688, 1.4294382086), (0.2433236688, 6.1952234497))
                CenterArc((0, 0), 6.2, 87.7508063566, 4.6218831037)
            make_face()
        # Symmetric extrude, each_side=0.5
        extrude(amount=0.5, both=True, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            Circle(0.6)
        # Symmetric extrude, each_side=3.6
        extrude(amount=3.6, both=True, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a dark gray/blue structural chassis or skid frame with a long rectangular base, featuring two raised triangular end caps on either side, central mounting slots, and reinforcing ribs or flanges running along its length.
def model_21822_7d3db422_0007():
    """Model: Rocker Bearing"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.32, perimeter: 15.2
            with BuildLine():
                Line((7.3, -13.4), (7.3, -15))
                Line((6.3, -13.4), (7.3, -13.4))
                Line((6.3, -14.6), (6.3, -13.4))
                Line((3.5, -14.6), (6.3, -14.6))
                Line((3.5, -13.4), (3.5, -14.6))
                Line((2.5, -13.4), (3.5, -13.4))
                Line((2.5, -15), (2.5, -13.4))
                Line((7.3, -15), (2.5, -15))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(7.3, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-14, 0.5)):
                Circle(0.2)
        # OneSide extrude, distance=-1.4
        extrude(amount=-1.4, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(2.5, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((14.0000002086, 0.5)):
                Circle(0.4)
        # OneSide extrude, distance=-1.2
        extrude(amount=-1.2, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 14.6), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.1590431281, perimeter: 1.4137166941
            with Locations((-4.0000000596, 0.5000000075)):
                Circle(0.225)
            # Profile area: 0.1590431281, perimeter: 1.4137166941
            with Locations((-5.800000073, 0.5000000075)):
                Circle(0.225)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)
    return part.part


MODELS = {
    "model_141790_1137bb2a_0000": {"func": model_141790_1137bb2a_0000, "volume": 134.9200004889, "area": 1366.0000009778},
    "model_142182_3b1414ce_0000": {"func": model_142182_3b1414ce_0000, "volume": 21.2982335839, "area": 57.6388012627},
    "model_142226_ba437656_0000": {"func": model_142226_ba437656_0000, "volume": 24.9377233521, "area": 71.0411061889},
    "model_142246_0851be5e_0012": {"func": model_142246_0851be5e_0012, "volume": 27.8284468945, "area": 92.1643560969},
    "model_142764_e4f86a3b_0000": {"func": model_142764_e4f86a3b_0000, "volume": 3572.6565176743, "area": 1604.8309595297},
    "model_142852_65dcbe39_0000": {"func": model_142852_65dcbe39_0000, "volume": 88.2090590286, "area": 169.7754143852},
    "model_142852_c569311a_0003": {"func": model_142852_c569311a_0003, "volume": 80.4640449058, "area": 191.3098348585},
    "model_142868_bcc940c6_0000": {"func": model_142868_bcc940c6_0000, "volume": 0.6411205208, "area": 8.724202799},
    "model_143019_77f4e3fa_0000": {"func": model_143019_77f4e3fa_0000, "volume": 17.1452064733, "area": 96.2905865357},
    "model_143324_6d184340_0000": {"func": model_143324_6d184340_0000, "volume": 43.55790624, "area": 249.4161085649},
    "model_143346_3ed36a3d_0000": {"func": model_143346_3ed36a3d_0000, "volume": 164.5022128562, "area": 269.3429173529},
    "model_144142_88858328_0000": {"func": model_144142_88858328_0000, "volume": 49.0470259251, "area": 244.7319686052},
    "model_144225_66a62553_0000": {"func": model_144225_66a62553_0000, "volume": 1026.5, "area": 3007},
    "model_144279_136348c1_0000": {"func": model_144279_136348c1_0000, "volume": 1.0367949336, "area": 11.2182518586},
    "model_144433_e54699d3_0000": {"func": model_144433_e54699d3_0000, "volume": 44.8898018329, "area": 240.8889166811},
    "model_144648_0fd6ca79_0000": {"func": model_144648_0fd6ca79_0000, "volume": 12498.64, "area": 9606.6},
    "model_144709_642fc665_0001": {"func": model_144709_642fc665_0001, "volume": 15.5450087498, "area": 97.9490334865},
    "model_144780_918f74e1_0000": {"func": model_144780_918f74e1_0000, "volume": 280.7713188164, "area": 566.9380977843},
    "model_145041_025cf3fe_0000": {"func": model_145041_025cf3fe_0000, "volume": 44.6974601837, "area": 231.9083185307},
    "model_145257_89235edd_0000": {"func": model_145257_89235edd_0000, "volume": 171.7941229153, "area": 328.4228091402},
    "model_145985_e6210d7a_0000": {"func": model_145985_e6210d7a_0000, "volume": 30.1942837447, "area": 65.4276590028},
    "model_146109_4a58cccf_0000": {"func": model_146109_4a58cccf_0000, "volume": 0.7463561267, "area": 20.2733831077},
    "model_146317_3eafabf0_0004": {"func": model_146317_3eafabf0_0004, "volume": 12.0441925824, "area": 104.8571179551},
    "model_146317_9562bd6f_0000": {"func": model_146317_9562bd6f_0000, "volume": 10.730913344, "area": 87.792192197},
    "model_146317_fc36685c_0000": {"func": model_146317_fc36685c_0000, "volume": 1.9252698806, "area": 22.6694206945},
    "model_146380_f1665a64_0000": {"func": model_146380_f1665a64_0000, "volume": 25.1326283306, "area": 122.9394689145},
    "model_146499_eb4d211f_0000": {"func": model_146499_eb4d211f_0000, "volume": 330.3432482679, "area": 333.3831847043},
    "model_147672_3e42908e_0000": {"func": model_147672_3e42908e_0000, "volume": 24.7585889508, "area": 85.3455645864},
    "model_147739_796beb31_0000": {"func": model_147739_796beb31_0000, "volume": 254.3077410339, "area": 386.5553310074},
    "model_20203_7e31e92a_0000": {"func": model_20203_7e31e92a_0000, "volume": 724.4019950475, "area": 642.461046872},
    "model_20440_27177360_0003": {"func": model_20440_27177360_0003, "volume": 312.436, "area": 474.6},
    "model_20945_8b57f672_0000": {"func": model_20945_8b57f672_0000, "volume": 85552908.8424355388, "area": 2327689.3282217598},
    "model_21231_eb9826e5_0004": {"func": model_21231_eb9826e5_0004, "volume": 0.7924154182, "area": 10.9358494655},
    "model_21231_eb9826e5_0009": {"func": model_21231_eb9826e5_0009, "volume": 0.4802721954, "area": 6.8797755831},
    "model_21231_eb9826e5_0012": {"func": model_21231_eb9826e5_0012, "volume": 0.6811153893, "area": 10.3991868999},
    "model_21233_05d745b4_0005": {"func": model_21233_05d745b4_0005, "volume": 1.7490004096, "area": 12.7245952256},
    "model_21234_8b71bd47_0002": {"func": model_21234_8b71bd47_0002, "volume": 163.255657995, "area": 237.8487777592},
    "model_21236_b696e901_0022": {"func": model_21236_b696e901_0022, "volume": 0.5481806605, "area": 5.6164352581},
    "model_21236_b696e901_0032": {"func": model_21236_b696e901_0032, "volume": 1.3063027346, "area": 11.016137662},
    "model_21237_7887a24b_0002": {"func": model_21237_7887a24b_0002, "volume": 0.3259117417, "area": 7.0083103564},
    "model_21237_7887a24b_0015": {"func": model_21237_7887a24b_0015, "volume": 0.1298357412, "area": 2.597468806},
    "model_21256_433456a3_0014": {"func": model_21256_433456a3_0014, "volume": 0.64026804, "area": 8.4063174035},
    "model_21557_53eafe15_0039": {"func": model_21557_53eafe15_0039, "volume": 43.7192690934, "area": 129.0823328766},
    "model_21626_b34008e6_0003": {"func": model_21626_b34008e6_0003, "volume": 31.7888939447, "area": 87.9852729945},
    "model_21638_0a984848_0029": {"func": model_21638_0a984848_0029, "volume": 2.8166382015, "area": 23.5518410586},
    "model_21642_b79d233e_0012": {"func": model_21642_b79d233e_0012, "volume": 4.7152348988, "area": 18.309859095},
    "model_21644_aa203dc5_0011": {"func": model_21644_aa203dc5_0011, "volume": 7.0182555709, "area": 33.7388023175},
    "model_21734_7cf58bd0_0000": {"func": model_21734_7cf58bd0_0000, "volume": 27.606983313, "area": 106.4666665523},
    "model_21734_7cf58bd0_0004": {"func": model_21734_7cf58bd0_0004, "volume": 7.7719232725, "area": 51.8458669657},
    "model_21773_01f6bc23_0016": {"func": model_21773_01f6bc23_0016, "volume": 38.1620073345, "area": 108.9122548821},
    "model_21783_c6677b21_0002": {"func": model_21783_c6677b21_0002, "volume": 51.6201717204, "area": 192.1531255232},
    "model_21799_0d47cdac_0002": {"func": model_21799_0d47cdac_0002, "volume": 228.1659189998, "area": 665.8672286269},
    "model_21803_8a36dcda_0017": {"func": model_21803_8a36dcda_0017, "volume": 208.3421590531, "area": 463.7435268759},
    "model_21822_7d3db422_0007": {"func": model_21822_7d3db422_0007, "volume": 3.5644469668, "area": 26.8480749658},
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
