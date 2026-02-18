"""Batch 004 - passing/02_3ops
140 models bundled from Fusion360 Gallery reconstructions.
"""

from build123d import *
from build123d import Edge, BuildLine
from collections import Counter
from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
from OCP.Geom import Geom_BSplineCurve
from OCP.TColStd import TColStd_Array1OfReal, TColStd_Array1OfInteger
from OCP.TColgp import TColgp_Array1OfPnt
from OCP.gp import gp_Pnt


# Description: This is a knurled adjustment knob featuring a cylindrical body with a textured knurled grip surface on one side and a smooth face, with a small protruding tab or pointer on the edge for precise rotational positioning.
def model_25168_05818e21_0012():
    """Model: Component13"""
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
            # Profile area: 10.0847305842, perimeter: 11.2573736754
            with BuildLine():
                CenterArc((0, 0), 1.7916666667, 4.5891664191, 350.8216671617)
                CenterArc((0, 0), 1.7916666667, -4.5891664191, 9.1783328383)
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0932862261, perimeter: 1.1999661518
            with BuildLine():
                Line((1.7859226277, 0.1433520568), (1.873321096, 0.1503673384))
                CenterArc((0, 0), 1.7916666667, -4.5891664191, 9.1783328383)
                Line((1.7859226277, -0.1433520568), (1.873321096, -0.1503673384))
                _nurbs_edge([(1.873321096, -0.1503673384), (1.8840515482, -0.1501598943), (1.9056991975, -0.149741396), (1.9380713753, -0.1445259229), (1.9705909849, -0.1375540875), (2.0031880832, -0.1285521551), (2.0358248951, -0.1178657654), (2.0684686661, -0.1055788629), (2.1010738025, -0.0917652701), (2.1336607453, -0.0765824856), (2.155065017, -0.0654206287), (2.1658461857, -0.0597984863)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0321598718, 0.0648794303, 0.0981385152, 0.1319348281, 0.1662674235, 0.2011357411, 0.236539382, 0.2724780318, 0.308951428, 0.308951428, 0.308951428, 0.308951428], 3)
                CenterArc((-0.0128673003, 0), 2.179533967, -1.5721851245, 3.144370249)
                _nurbs_edge([(1.873321096, 0.1503673384), (1.8840515482, 0.1501598943), (1.9056991975, 0.149741396), (1.9380713753, 0.1445259229), (1.9705909849, 0.1375540875), (2.0031880832, 0.1285521551), (2.0358248951, 0.1178657654), (2.0684686661, 0.1055788629), (2.1010738025, 0.0917652701), (2.1336607453, 0.0765824856), (2.155065017, 0.0654206287), (2.1658461857, 0.0597984863)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0321598718, 0.0648794303, 0.0981385152, 0.1319348281, 0.1662674235, 0.2011357411, 0.236539382, 0.2724780318, 0.308951428, 0.308951428, 0.308951428, 0.308951428], 3)
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical connector or coupling with a rounded, bulbous body featuring a protruding nozzle or spout on one side and a mesh or perforated textured section on the top surface.
def model_25168_05818e21_0016():
    """Model: Component46"""
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
            # Profile area: 10.0847305842, perimeter: 11.2573736754
            with BuildLine():
                CenterArc((0, 0), 1.7916666667, 4.5891664191, 350.8216671617)
                CenterArc((0, 0), 1.7916666667, -4.5891664191, 9.1783328383)
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0932862261, perimeter: 1.1999661518
            with BuildLine():
                Line((1.7859226277, 0.1433520568), (1.873321096, 0.1503673384))
                CenterArc((0, 0), 1.7916666667, -4.5891664191, 9.1783328383)
                Line((1.7859226277, -0.1433520568), (1.873321096, -0.1503673384))
                _nurbs_edge([(1.873321096, -0.1503673384), (1.8840515482, -0.1501598943), (1.9056991975, -0.149741396), (1.9380713753, -0.1445259229), (1.9705909849, -0.1375540875), (2.0031880832, -0.1285521551), (2.0358248951, -0.1178657654), (2.0684686661, -0.1055788629), (2.1010738025, -0.0917652701), (2.1336607453, -0.0765824856), (2.155065017, -0.0654206287), (2.1658461857, -0.0597984863)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0321598718, 0.0648794303, 0.0981385152, 0.1319348281, 0.1662674235, 0.2011357411, 0.236539382, 0.2724780318, 0.308951428, 0.308951428, 0.308951428, 0.308951428], 3)
                CenterArc((-0.0128673003, 0), 2.179533967, -1.5721851245, 3.144370249)
                _nurbs_edge([(1.873321096, 0.1503673384), (1.8840515482, 0.1501598943), (1.9056991975, 0.149741396), (1.9380713753, 0.1445259229), (1.9705909849, 0.1375540875), (2.0031880832, 0.1285521551), (2.0358248951, 0.1178657654), (2.0684686661, 0.1055788629), (2.1010738025, 0.0917652701), (2.1336607453, 0.0765824856), (2.155065017, 0.0654206287), (2.1658461857, 0.0597984863)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0321598718, 0.0648794303, 0.0981385152, 0.1319348281, 0.1662674235, 0.2011357411, 0.236539382, 0.2724780318, 0.308951428, 0.308951428, 0.308951428, 0.308951428], 3)
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)
    return part.part


# Description: A circular, dome-shaped lens cap with a ribbed or textured rim around the perimeter and a small tether loop or attachment point on one side for securing to a camera lens.
def model_25168_05818e21_0018():
    """Model: Component33"""
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
            # Profile area: 10.0847305842, perimeter: 11.2573736754
            with BuildLine():
                CenterArc((0, 0), 1.7916666667, 4.5891664191, 350.8216671617)
                CenterArc((0, 0), 1.7916666667, -4.5891664191, 9.1783328383)
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0932862261, perimeter: 1.1999661518
            with BuildLine():
                Line((1.7859226277, 0.1433520568), (1.873321096, 0.1503673384))
                CenterArc((0, 0), 1.7916666667, -4.5891664191, 9.1783328383)
                Line((1.7859226277, -0.1433520568), (1.873321096, -0.1503673384))
                _nurbs_edge([(1.873321096, -0.1503673384), (1.8840515482, -0.1501598943), (1.9056991975, -0.149741396), (1.9380713753, -0.1445259229), (1.9705909849, -0.1375540875), (2.0031880832, -0.1285521551), (2.0358248951, -0.1178657654), (2.0684686661, -0.1055788629), (2.1010738025, -0.0917652701), (2.1336607453, -0.0765824856), (2.155065017, -0.0654206287), (2.1658461857, -0.0597984863)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0321598718, 0.0648794303, 0.0981385152, 0.1319348281, 0.1662674235, 0.2011357411, 0.236539382, 0.2724780318, 0.308951428, 0.308951428, 0.308951428, 0.308951428], 3)
                CenterArc((-0.0128673003, 0), 2.179533967, -1.5721851245, 3.144370249)
                _nurbs_edge([(1.873321096, 0.1503673384), (1.8840515482, 0.1501598943), (1.9056991975, 0.149741396), (1.9380713753, 0.1445259229), (1.9705909849, 0.1375540875), (2.0031880832, 0.1285521551), (2.0358248951, 0.1178657654), (2.0684686661, 0.1055788629), (2.1010738025, 0.0917652701), (2.1336607453, 0.0765824856), (2.155065017, 0.0654206287), (2.1658461857, 0.0597984863)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0321598718, 0.0648794303, 0.0981385152, 0.1319348281, 0.1662674235, 0.2011357411, 0.236539382, 0.2724780318, 0.308951428, 0.308951428, 0.308951428, 0.308951428], 3)
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)
    return part.part


# Description: This is a circular disc or wheel with a textured/ribbed rim and a small protruding lug or tab feature on the right side, appearing to be a knob, pulley, or mechanical component with radial surface patterns.
def model_25168_05818e21_0019():
    """Model: Component31"""
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
            # Profile area: 10.0847305842, perimeter: 11.2573736754
            with BuildLine():
                CenterArc((0, 0), 1.7916666667, 4.5891664191, 350.8216671617)
                CenterArc((0, 0), 1.7916666667, -4.5891664191, 9.1783328383)
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0932862261, perimeter: 1.1999661518
            with BuildLine():
                Line((1.7859226277, 0.1433520568), (1.873321096, 0.1503673384))
                CenterArc((0, 0), 1.7916666667, -4.5891664191, 9.1783328383)
                Line((1.7859226277, -0.1433520568), (1.873321096, -0.1503673384))
                _nurbs_edge([(1.873321096, -0.1503673384), (1.8840515482, -0.1501598943), (1.9056991975, -0.149741396), (1.9380713753, -0.1445259229), (1.9705909849, -0.1375540875), (2.0031880832, -0.1285521551), (2.0358248951, -0.1178657654), (2.0684686661, -0.1055788629), (2.1010738025, -0.0917652701), (2.1336607453, -0.0765824856), (2.155065017, -0.0654206287), (2.1658461857, -0.0597984863)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0321598718, 0.0648794303, 0.0981385152, 0.1319348281, 0.1662674235, 0.2011357411, 0.236539382, 0.2724780318, 0.308951428, 0.308951428, 0.308951428, 0.308951428], 3)
                CenterArc((-0.0128673003, 0), 2.179533967, -1.5721851245, 3.144370249)
                _nurbs_edge([(1.873321096, 0.1503673384), (1.8840515482, 0.1501598943), (1.9056991975, 0.149741396), (1.9380713753, 0.1445259229), (1.9705909849, 0.1375540875), (2.0031880832, 0.1285521551), (2.0358248951, 0.1178657654), (2.0684686661, 0.1055788629), (2.1010738025, 0.0917652701), (2.1336607453, 0.0765824856), (2.155065017, 0.0654206287), (2.1658461857, 0.0597984863)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0321598718, 0.0648794303, 0.0981385152, 0.1319348281, 0.1662674235, 0.2011357411, 0.236539382, 0.2724780318, 0.308951428, 0.308951428, 0.308951428, 0.308951428], 3)
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


# Description: This is a sheet metal bin or chute component with a trapezoidal wedge shape, featuring angled side walls, an open top with a light blue interior surface, and a protruding outlet or spout on the lower left side.
def model_25199_d7aff7a5_0024():
    """Model: Part 24 - Cover A v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 7.8093291422, perimeter: 12.3210937397
            with BuildLine():
                Line((0, 0), (3.8, 0))
                Line((3.8, 0), (3.8, 2.8))
                Line((0, 1.5), (3.8, 2.8))
                CenterArc((-0.6389428447, 0.75), 0.9852654256, -49.5715327263, 99.1430654527)
            make_face()
        # OneSide extrude, distance=1.15
        extrude(amount=1.15)
    return part.part


# Description: This is a truncated octahedron or rounded polyhedron featuring a symmetrical geometric shape with multiple faceted surfaces, prominent corner vertices, and a central horizontal division creating upper and lower mirrored sections with angular planes and edges throughout.
def model_25365_4fb79251_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.5542562584, perimeter: 2.7712812921
            with BuildLine():
                Line((-0.2309401077, 0.4), (-0.4618802154, 0))
                Line((-0.4618802154, 0), (-0.2309401077, -0.4))
                Line((-0.2309401077, -0.4), (0.2309401077, -0.4))
                Line((0.2309401077, -0.4), (0.4618802154, 0))
                Line((0.4618802154, 0), (0.2309401077, 0.4))
                Line((0.2309401077, 0.4), (-0.2309401077, 0.4))
            make_face()
        # OneSide extrude, distance=0.9
        extrude(amount=0.9)
    return part.part


# Description: This is a cylindrical mesh filter or strainer basket with an open top, featuring a perforated or mesh upper section (shown in light blue) and a solid lower cylindrical wall (shown in dark gray), designed to contain and filter materials while allowing liquid or air to pass through.
def model_25365_769ce017_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.9864765163, perimeter: 6.1261056745
            Circle(0.975)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)
    return part.part


# Description: This is a cylindrical sleeve or spacer with a hollow bore through its center and visible surface texturing or knurling along its length.
def model_25365_befea608_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0942477796, perimeter: 3.7699111843
            with BuildLine():
                CenterArc((0, 0), 0.325, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.275, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.55
        extrude(amount=0.55, both=True)
    return part.part


# Description: This is an elliptical or oval-shaped cylindrical shell with a ribbed or finned interior surface and a solid outer wall, resembling a heat exchanger or cooling component with internal structural ribs for reinforcement and thermal performance.
def model_25365_e20900f9_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.3411494795, perimeter: 11.9380520836
            Circle(1.9)
        # OneSide extrude, distance=0.95
        extrude(amount=0.95)
    return part.part


# Description: This is a cylindrical mesh filter or strainer with a solid dark body and perforated mesh openings on the top and bottom ends, designed for fluid or air filtration applications.
def model_25365_eb01787e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=0.75
        extrude(amount=0.75)
    return part.part


# Description: This is a curved pipe or hose connector with flanged end fittings, featuring a smooth S-shaped or serpentine bend with cylindrical sections at both ends for attachment points.
def model_25416_e5f43085_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 28 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0910276471, perimeter: 1.9163715187
            with BuildLine():
                CenterArc((-0.0000007102, 1.8), 0.2, -95.3745859066, 302.3034415415)
                CenterArc((-0.0000007102, 1.8), 0.2, -153.0711443651, 57.6965584585)
            make_face()
            with BuildLine():
                CenterArc((-0.0000007102, 1.8), 0.105, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2150726901, perimeter: 3.3440774713
            with BuildLine():
                CenterArc((-0.0000007102, 1.8), 0.2, -153.0711443651, 57.6965584585)
                CenterArc((-0.7020196698, 2.2888479933), 0.7810249792, -140.0123090609, 92.1207246786)
                CenterArc((-1.5000007102, 1.8), 0.2, -47.8282963397, 44.0851825786)
                CenterArc((-0.7020196698, 2.2888479933), 0.9199869427, -136.1730239002, 74.8883974111)
                CenterArc((-0.2284451025, 1.4243970795), 0.0656845305, -26.0992194906, 144.8145930015)
                CenterArc((-0.1242686848, 0.8115159727), 0.5857305146, 79.6199834737, 14.8048215655)
                Line((-0.0187340528, 1.6008792781), (-0.0187340528, 1.3876606396))
            make_face()
            # Profile area: 0.2934640862, perimeter: 3.4053016181
            with BuildLine():
                CenterArc((-0.1242686848, 0.8115159727), 0.5857305146, 94.4248050392, 99.3520367689)
                CenterArc((-0.9683900806, 0.6045416023), 0.2833950924, -48.9572232504, 62.7340650585)
                CenterArc((-0.7049665452, 0.3019640319), 0.1177845994, 131.0427767496, 192.0102916275)
                CenterArc((-1.0699050372, 0.5764353292), 0.574418584, -36.9469316229, 50.8707739624)
                CenterArc((-0.1242686848, 0.8115159727), 0.4, 74.7021663412, 119.3108860572)
                Line((-0.0187340528, 1.3876606396), (-0.0187340528, 1.1973429306))
                CenterArc((-0.1242686848, 0.8115159727), 0.5857305146, 79.6199834737, 14.8048215655)
            make_face()
            # Profile area: 0.0910276471, perimeter: 1.9163715187
            with BuildLine():
                CenterArc((-1.5000007102, 1.8), 0.2, -3.7431137611, 224.6563067142)
                CenterArc((-1.5000007102, 1.8), 0.2, -139.0868070469, 17.939468836)
                CenterArc((-1.5000007102, 1.8), 0.2, -121.1473382109, 73.3190418713)
                CenterArc((-1.5000007102, 1.8), 0.2, -47.8282963397, 44.0851825786)
            make_face()
            with BuildLine():
                CenterArc((-1.5000007102, 1.8), 0.105, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.6462670743, perimeter: 8.2692311326
            with BuildLine():
                CenterArc((-1.5000007102, 1.8), 0.2, -121.1473382109, 73.3190418713)
                CenterArc((-3.5, 0), 2.5, 13.5540809606, 27.1031872255)
                CenterArc((-3.5, 0), 2.5, -47.9265413631, 61.4806223238)
                Line((-1.8247929038, -1.8557158147), (-1.7218062792, -1.9697995649))
                CenterArc((-3.5, 0), 2.6536923775, -47.9265413631, 60.698240372)
                CenterArc((-0.6193859056, 0.6529633221), 0.3, 162.5174290391, 30.2542699698)
                CenterArc((-3.5, 0), 2.6987890975, 15.9823527782, 21.7549597171)
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 28 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0910276471, perimeter: 1.9163715187
            with BuildLine():
                CenterArc((-0.0000007102, 1.8), 0.2, -95.3745859066, 302.3034415415)
                CenterArc((-0.0000007102, 1.8), 0.2, -153.0711443651, 57.6965584585)
            make_face()
            with BuildLine():
                CenterArc((-0.0000007102, 1.8), 0.105, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2934640862, perimeter: 3.4053016181
            with BuildLine():
                CenterArc((-0.1242686848, 0.8115159727), 0.5857305146, 94.4248050392, 99.3520367689)
                CenterArc((-0.9683900806, 0.6045416023), 0.2833950924, -48.9572232504, 62.7340650585)
                CenterArc((-0.7049665452, 0.3019640319), 0.1177845994, 131.0427767496, 192.0102916275)
                CenterArc((-1.0699050372, 0.5764353292), 0.574418584, -36.9469316229, 50.8707739624)
                CenterArc((-0.1242686848, 0.8115159727), 0.4, 74.7021663412, 119.3108860572)
                Line((-0.0187340528, 1.3876606396), (-0.0187340528, 1.1973429306))
                CenterArc((-0.1242686848, 0.8115159727), 0.5857305146, 79.6199834737, 14.8048215655)
            make_face()
            # Profile area: 0.0910276471, perimeter: 1.9163715187
            with BuildLine():
                CenterArc((-1.5000007102, 1.8), 0.2, -3.7431137611, 224.6563067142)
                CenterArc((-1.5000007102, 1.8), 0.2, -139.0868070469, 17.939468836)
                CenterArc((-1.5000007102, 1.8), 0.2, -121.1473382109, 73.3190418713)
                CenterArc((-1.5000007102, 1.8), 0.2, -47.8282963397, 44.0851825786)
            make_face()
            with BuildLine():
                CenterArc((-1.5000007102, 1.8), 0.105, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.ADD)
    return part.part


# Description: This is a mesh or perforated cylindrical container with an elliptical/oval footprint, featuring ventilation holes or mesh panels on the upper surfaces and solid walls on the lower portion.
def model_25436_61a7f978_0003():
    """Model: Gate Hinge"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 13 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0321577695, perimeter: 0.9625884389
            with BuildLine():
                Line((0.235, 0.125), (0.125, 0.125))
                CenterArc((0.125, 0), 0.125, 90, 90)
                Line((0, 0), (0.075, 0))
                CenterArc((0.125, 0), 0.05, 0, 180)
                Line((0.175, 0), (0.1975, 0))
                CenterArc((0.235, 0), 0.0375, 0, 180)
                Line((0.36, 0), (0.2725, 0))
                CenterArc((0.235, 0), 0.125, 0, 90)
            make_face()
            # Profile area: 0.0321577695, perimeter: 0.9625884389
            with BuildLine():
                Line((0.36, 0), (0.2725, 0))
                CenterArc((0.235, 0), 0.0375, -180, 180)
                Line((0.175, 0), (0.1975, 0))
                CenterArc((0.125, 0), 0.05, -180, 180)
                Line((0, 0), (0.075, 0))
                CenterArc((0.125, 0), 0.125, -180, 90)
                Line((0.125, -0.125), (0.235, -0.125))
                CenterArc((0.235, 0), 0.125, -90, 90)
            make_face()
            # Profile area: 0.0022089323, perimeter: 0.1928097245
            with BuildLine():
                Line((0.2725, 0), (0.1975, 0))
                CenterArc((0.235, 0), 0.0375, 0, 180)
            make_face()
            # Profile area: 0.0022089323, perimeter: 0.1928097245
            with BuildLine():
                CenterArc((0.235, 0), 0.0375, -180, 180)
                Line((0.2725, 0), (0.1975, 0))
            make_face()
        # OneSide extrude, distance=0.075
        extrude(amount=0.075)

        # Sketch1 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 13 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0022089323, perimeter: 0.1928097245
            with BuildLine():
                CenterArc((0.235, 0), 0.0375, -180, 180)
                Line((0.2725, 0), (0.1975, 0))
            make_face()
            # Profile area: 0.0022089323, perimeter: 0.1928097245
            with BuildLine():
                Line((0.2725, 0), (0.1975, 0))
                CenterArc((0.235, 0), 0.0375, 0, 180)
            make_face()
        # OneSide extrude, distance=0.0375
        extrude(amount=0.0375, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a polyhedron-shaped enclosure or housing with an irregular geometric form featuring multiple flat faceted surfaces, triangular and trapezoidal faces, and what appears to be a central slot or opening running through its body.
def model_25438_f75175e2_0004():
    """Model: nakrętka M8 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.9609281078, perimeter: 7.0166062226
            with BuildLine():
                Line((0.65, -0.375277675), (0.65, 0.375277675))
                Line((0.65, 0.375277675), (0, 0.7505553499))
                Line((0, 0.7505553499), (-0.65, 0.375277675))
                Line((-0.65, 0.375277675), (-0.65, -0.375277675))
                Line((-0.65, -0.375277675), (0, -0.7505553499))
                Line((0, -0.7505553499), (0.65, -0.375277675))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.65
        extrude(amount=0.65)
    return part.part


# Description: This is a dual-slot bracket or cable management clip with a rectangular body featuring two parallel vertical slots and curved mounting tabs at the top and bottom for attachment.
def model_25448_3e4b4ae7_0000():
    """Model: zatrzask bloku cpu v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 61 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 44.2752252061, perimeter: 37.9856836215
            with BuildLine():
                Line((4.5128658893, 9.8784851925), (3.1178352769, 8.4401290963))
                CenterArc((2.4, 9.1363420776), 1, -135.8760448803, 91.7520897606)
                Line((0.2871341107, 9.8784851925), (1.6821647231, 8.4401290963))
                CenterArc((0, 9.6), 0.4, -148.7948701278, 192.9188252475)
                Line((-0.3421271505, 9.3927585637), (0.223460034, 8.4590517954))
                CenterArc((-0.2041989041, 8.2), 0.5, -90, 121.2051298722)
                Line((-0.5, 7.7), (-0.2041989041, 7.7))
                Line((-0.5, 1.9), (-0.5, 7.7))
                Line((-0.2041989041, 1.9), (-0.5, 1.9))
                CenterArc((-0.2041989041, 1.4), 0.5, -31.2051298722, 121.2051298722)
                Line((-0.3421271505, 0.2072414363), (0.223460034, 1.1409482046))
                CenterArc((0, 0), 0.4, -44.1239551197, 192.9188252475)
                Line((0.2871341107, -0.2784851925), (1.6821647231, 1.1598709037))
                CenterArc((2.4, 0.4636579224), 1, 44.1239551197, 91.7520897606)
                Line((4.5128658893, -0.2784851925), (3.1178352769, 1.1598709037))
                CenterArc((4.8, 0), 0.4, 31.2051298722, 192.9188252475)
                Line((5.1421271505, 0.2072414363), (4.576539966, 1.1409482046))
                CenterArc((5.0041989041, 1.4), 0.5, 90, 121.2051298722)
                Line((5.3, 1.9), (5.0041989041, 1.9))
                Line((5.3, 7.7), (5.3, 1.9))
                Line((5.0041989041, 7.7), (5.3, 7.7))
                CenterArc((5.0041989041, 8.2), 0.5, 148.7948701278, 121.2051298722)
                Line((5.1421271505, 9.3927585637), (4.576539966, 8.4590517954))
                CenterArc((4.8, 9.6), 0.4, 135.8760448803, 192.9188252475)
            make_face()
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with BuildLine():
                CenterArc((4.8, 9.6), 0.4, 135.8760448803, 192.9188252475)
                CenterArc((4.8, 9.6), 0.4, -31.2051298722, 167.0811747525)
            make_face()
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with BuildLine():
                CenterArc((4.8, 0), 0.4, 31.2051298722, 192.9188252475)
                CenterArc((4.8, 0), 0.4, -135.8760448803, 167.0811747525)
            make_face()
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with BuildLine():
                CenterArc((0, 0), 0.4, -44.1239551197, 192.9188252475)
                CenterArc((0, 0), 0.4, 148.7948701278, 167.0811747525)
            make_face()
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with BuildLine():
                CenterArc((0, 9.6), 0.4, -148.7948701278, 192.9188252475)
                CenterArc((0, 9.6), 0.4, 44.1239551197, 167.0811747525)
            make_face()
        # OneSide extrude, distance=0.15
        extrude(amount=0.15)
    return part.part


# Description: This is a flexible hose or tube assembly with an elongated oval/elliptical loop shape, featuring a textured outer surface and what appears to be a quick-disconnect coupling or connector integrated at one end.
def model_25474_5422a377_0017():
    """Model: PODKLADKA_LOZYSKOWA v4 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.229546641, perimeter: 18.2531730663
            with BuildLine():
                CenterArc((0, 0), 1.6, 0, 360)
            make_face()
            with BuildLine():
                Line((1.05, 0.25), (1.05, -0.25))
                Line((1.05, -0.25), (1.2247448714, -0.25))
                CenterArc((0, 0), 1.25, 11.5369590328, 336.9260819344)
                Line((1.2247448714, 0.25), (1.05, 0.25))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.125
        extrude(amount=0.125)
    return part.part


# Description: This is a linear rail or guide block with a rectangular, elongated body featuring a recessed central channel running its length and two protruding flanges or mounting feet at each end.
def model_25475_70092bfb_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 20 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 352, perimeter: 128
            with BuildLine():
                Line((-2, -5), (0, -5))
                Line((-2, -3), (-2, -5))
                Line((-4, -3), (-2, -3))
                Line((-4, -9), (-4, -3))
                Line((-2, -9), (-4, -9))
                Line((-2, -7), (-2, -9))
                Line((0, -7), (-2, -7))
                Line((0, -10), (0, -7))
                Line((40, -10), (0, -10))
                Line((40, -7), (40, -10))
                Line((42, -7), (40, -7))
                Line((42, -9), (42, -7))
                Line((44, -9), (42, -9))
                Line((44, -3), (44, -9))
                Line((42, -3), (44, -3))
                Line((42, -5), (42, -3))
                Line((40, -5), (42, -5))
                Line((40, -2), (40, -5))
                Line((0, -2), (40, -2))
                Line((0, -5), (0, -2))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a mounting bracket or clamp with an elongated, angled body featuring two rectangular slots or cutouts and a forked top end for securing or gripping components.
def model_26261_5deaf75a_0000():
    """Model: Secondary Side Support"""
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
        # Sketch on XY construction plane
        # Sketch has 15 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 589.3685299906, perimeter: 193.5589502498
            with BuildLine():
                Line((0, 0), (11.6584339857, -6.731))
                _nurbs_edge([(11.6584339857, -6.731), (12.086720669, -6.2675629644), (12.8959968417, -5.3386183487), (13.968023111, -3.9389901423), (15.1115210098, -2.0603032045), (16.0600201709, 0.3082220151), (16.5358122084, 2.6939075772), (16.574175806, 5.0898020107), (16.2509160365, 7.483577347), (15.7049123639, 9.8551327709), (15.1196061157, 12.1790073692), (14.6931771389, 14.4282005641), (14.6132725978, 16.5776097046), (15.0297277158, 18.6078355359), (16.0252829558, 20.5094403105), (17.6351232044, 22.2797108251), (19.419237365, 23.5916925112), (21.0331343187, 24.5180825462), (22.2307617798, 25.1102627967), (22.8599996567, 25.3999996185)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9333333333, 1, 1, 1, 1, 1, 1], 5)
                Line((22.8599996567, 25.3999996185), (24.7466759131, 28.8925))
                Line((21.3726851487, 30.8404744761), (24.7466759131, 28.8925))
                _nurbs_edge([(21.3726851487, 30.8404744761), (21.1369406757, 30.6609190642), (20.6802917154, 30.3425185866), (20.0398388666, 29.987049851), (19.2753009659, 29.7583443808), (18.4645353057, 29.8764582043), (17.7824684955, 30.3737115876), (17.1937268653, 31.1922795429), (16.6355367664, 32.2264054895), (16.0315997029, 33.3439284718), (15.3062363202, 34.4081727122), (14.3991636088, 35.3004806255), (13.2785825232, 35.9402395738), (11.9599339319, 36.3128441523), (10.501668534, 36.4649987214), (8.9885598196, 36.4823670457), (7.5197647138, 36.4739349269), (6.1947441485, 36.5535545918), (5.1014756373, 36.8245414442), (4.300164586, 37.3588354756), (3.8214971449, 38.1940044873), (3.7066076415, 39.1157244103), (3.7717162805, 39.9507533436), (3.8820918931, 40.5710752733), (3.9540216148, 40.8971445563)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1, 1, 1, 1, 1], 5)
                Line((0, 43.18), (3.9540216148, 40.8971445563))
                Line((0, 0), (0, 43.18))
            make_face()
            with BuildLine():
                Line((10.6869235661, 6.8171800148), (10.6869235661, 0))
                Line((2.5399999619, 0), (10.6869235661, 0))
                Line((2.5399999619, 6.8171800148), (2.5399999619, 0))
                Line((10.6869235661, 6.8171800148), (2.5399999619, 6.8171800148))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((13.8464576416, 31.9719320773), (1.2083213397, 31.9719320773))
                Line((10.6869235661, 25.3999996185), (13.8464576416, 31.9719320773))
                Line((5.0799999237, 25.3999996185), (10.6869235661, 25.3999996185))
                Line((1.2083213397, 31.9719320773), (5.0799999237, 25.3999996185))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.905
        extrude(amount=1.905)
    return part.part


# Description: This is a cylindrical sleeve or tube with a rounded hemispherical end cap on one side and a flat end on the other, featuring a mesh or perforated pattern across its curved surface.
def model_26566_3009b7a9_0001():
    """Model: Motor"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            with Locations((0.8635999896, 0.0761999991)):
                Circle(0.635)
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)
    return part.part


# Description: This is a geometric polyhedron with a truncated octahedron or cuboctahedron-like shape, featuring multiple flat faceted surfaces (both triangular and square faces), internal curved cylindrical or organic forms visible through transparent sections, and a symmetrical multi-sided structure with both sharp edges and smooth curved internal geometry.
def model_26768_c4df841f_0006():
    """Model: Tuerca"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 23 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.0331505181, perimeter: 9.1439195775
            with BuildLine():
                CenterArc((0, 0), 0.95, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5053, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 23 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.2912609256, perimeter: 12.5510260418
            with BuildLine():
                Line((-0.5485, 0.950029868), (-1.097, 0))
                Line((-1.097, 0), (-0.5485, -0.950029868))
                Line((0.5485, -0.950029868), (-0.5485, -0.950029868))
                Line((0.5485, -0.950029868), (1.097, 0))
                Line((1.097, 0), (0.5485, 0.950029868))
                Line((0.5485, 0.950029868), (-0.5485, 0.950029868))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.95, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


# Description: This is an elongated rectangular duct or channel with a peaked/triangular top profile, featuring a longitudinal slot or opening along one side and internal ribbing or structural reinforcement details.
def model_26768_c4df841f_0015():
    """Model: Pieza 4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 17 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 36.2238308035, perimeter: 42.3829746035
            with BuildLine():
                Line((1.65, 0), (1.65, 1.0050125629))
                CenterArc((1.75, 2), 1, 95.7391704773, 168.5216590455)
                Line((1.65, 2.9949874371), (1.65, 3.5))
                Line((1.85, 3.5), (1.65, 3.5))
                Line((1.85, 2.9949874371), (1.85, 3.5))
                CenterArc((1.75, 2), 1, -84.2608295227, 168.5216590455)
                Line((1.85, 0), (1.85, 1.0050125629))
                Line((3.5, 0), (1.85, 0))
                Line((3.5, 9.1643590902), (3.5, 0))
                Line((3, 12), (3.5, 9.1643590902))
                Line((0.5, 12), (3, 12))
                Line((0.5, 12), (0, 9.1643590902))
                Line((0, 0), (0, 9.1643590902))
                Line((1.65, 0), (0, 0))
            make_face()
            with BuildLine():
                CenterArc((1.75, 10.5), 0.54, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


# Description: This is a tall, rectangular tower or enclosure with a sloped pyramidal top, featuring vertical ribbing/fins along its sides and an open framework structure, likely designed as a cooling tower or ventilation unit.
def model_26768_c4df841f_0018():
    """Model: Pieza 3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 11 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 53.341838201, perimeter: 53.2012381604
            with BuildLine():
                Line((-0.8687380383, 14.2232607303), (-0.8687380383, 12.7182481674))
                CenterArc((-0.9687380383, 11.7232607303), 1, -84.2608295227, 168.5216590455)
                Line((-0.8687380383, 10.7282732932), (-0.8687380383, 10.2232607303))
                Line((-1.0687380383, 10.2232607303), (-0.8687380383, 10.2232607303))
                Line((-1.0687380383, 10.7282732932), (-1.0687380383, 10.2232607303))
                CenterArc((-0.9687380383, 11.7232607303), 1, 95.7391704773, 168.5216590455)
                Line((-1.0687380383, 14.2232607303), (-1.0687380383, 12.7182481674))
                Line((-2.7187380383, 14.2232607303), (-1.0687380383, 14.2232607303))
                Line((-2.7187380383, -2.2767392697), (-2.7187380383, 14.2232607303))
                Line((0.7812619617, -2.2767392697), (-2.7187380383, -2.2767392697))
                Line((0.7812619617, 14.2232607303), (0.7812619617, -2.2767392697))
                Line((-0.8687380383, 14.2232607303), (0.7812619617, 14.2232607303))
            make_face()
            with BuildLine():
                CenterArc((-0.9687380383, -0.2767392697), 0.525, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3
        extrude(amount=3)
    return part.part


# Description: This is a knurled adjustable knob with a cylindrical body featuring a textured knurled grip surface on one half and a smooth flat face on the opposite side, with a small protruding tab or pointer for directional indication.
def model_26777_9c5b07d6_0000():
    """Model: Component8"""
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
            # Profile area: 40.3389223367, perimeter: 22.5147473507
            with BuildLine():
                CenterArc((0, 0), 3.5833333333, 4.5891664191, 350.8216671617)
                CenterArc((0, 0), 3.5833333333, -4.5891664191, 9.1783328383)
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.3731449044, perimeter: 2.3999323036
            with BuildLine():
                Line((3.5718452555, 0.2867041136), (3.7466421919, 0.3007346768))
                CenterArc((0, 0), 3.5833333333, -4.5891664191, 9.1783328383)
                Line((3.5718452555, -0.2867041136), (3.7466421919, -0.3007346768))
                _nurbs_edge([(3.7466421919, -0.3007346768), (3.7681030964, -0.3003197887), (3.8113983951, -0.299482792), (3.8761427506, -0.2890518458), (3.9411819698, -0.275108175), (4.0063761664, -0.2571043103), (4.0716497901, -0.2357315308), (4.1369373323, -0.2111577258), (4.202147605, -0.1835305401), (4.2673214906, -0.1531649712), (4.3101300341, -0.1308412573), (4.3316923715, -0.1195969727)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0643197435, 0.1297588607, 0.1962770304, 0.2638696562, 0.332534847, 0.4022714823, 0.4730787641, 0.5449560637, 0.617902856, 0.617902856, 0.617902856, 0.617902856], 3)
                CenterArc((-0.0257346007, 0), 4.359067934, -1.5721851245, 3.144370249)
                _nurbs_edge([(3.7466421919, 0.3007346768), (3.7681030964, 0.3003197887), (3.8113983951, 0.299482792), (3.8761427506, 0.2890518458), (3.9411819698, 0.275108175), (4.0063761664, 0.2571043103), (4.0716497901, 0.2357315308), (4.1369373323, 0.2111577258), (4.202147605, 0.1835305401), (4.2673214906, 0.1531649712), (4.3101300341, 0.1308412573), (4.3316923715, 0.1195969727)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0643197435, 0.1297588607, 0.1962770304, 0.2638696562, 0.332534847, 0.4022714823, 0.4730787641, 0.5449560637, 0.617902856, 0.617902856, 0.617902856, 0.617902856], 3)
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical filter or strainer component with a mesh or perforated surface on the upper portion and a solid base, featuring a small protruding lug or bracket on one end for mounting or attachment.
def model_26777_9c5b07d6_0001():
    """Model: Component4"""
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
            # Profile area: 0.4922373906, perimeter: 2.4870941841
            with BuildLine():
                CenterArc((0, 0), 0.3958333333, 8.2665492276, 343.4669015447)
                CenterArc((0, 0), 0.3958333333, -8.2665492276, 16.5330984553)
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0213848597, perimeter: 0.5679945652
            with BuildLine():
                Line((0.3917205852, 0.0569123092), (0.4648609605, 0.0675387297))
                CenterArc((0, 0), 0.3958333333, -8.2665492276, 16.5330984553)
                Line((0.3917205852, -0.0569123092), (0.4648609605, -0.0675387297))
                _nurbs_edge([(0.4648609605, -0.0675387297), (0.4691208061, -0.0676271271), (0.4777555477, -0.0678063093), (0.4907469663, -0.0657895952), (0.5038596081, -0.0628718281), (0.5170482465, -0.0588977312), (0.5302733508, -0.0540292003), (0.543504319, -0.0482980628), (0.5567016748, -0.0417335556), (0.5698685647, -0.0344103123), (0.5784324486, -0.0289658232), (0.5827597447, -0.0262147448)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0127593836, 0.0258633743, 0.0392971853, 0.0530581874, 0.067144904, 0.0815562586, 0.0962913826, 0.1113495424, 0.1267301078, 0.1267301078, 0.1267301078, 0.1267301078], 3)
                CenterArc((-0.0160002634, 0), 0.5993335968, -2.5069069843, 5.0138139687)
                _nurbs_edge([(0.4648609605, 0.0675387297), (0.4691208061, 0.0676271271), (0.4777555477, 0.0678063093), (0.4907469663, 0.0657895952), (0.5038596081, 0.0628718281), (0.5170482465, 0.0588977312), (0.5302733508, 0.0540292003), (0.543504319, 0.0482980628), (0.5567016748, 0.0417335556), (0.5698685647, 0.0344103123), (0.5784324486, 0.0289658232), (0.5827597447, 0.0262147448)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0127593836, 0.0258633743, 0.0392971853, 0.0530581874, 0.067144904, 0.0815562586, 0.0962913826, 0.1113495424, 0.1267301078, 0.1267301078, 0.1267301078, 0.1267301078], 3)
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)
    return part.part


# Description: This is a rectangular bar or structural beam with a long, slender parallelogram profile, featuring a uniform cross-section and smooth surfaces with no visible holes, slots, or protrusions.
def model_26942_279de65e_0011():
    """Model: Body Frame - 3 v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY) as sk:
            # Profile area: 1694, perimeter: 262.2099463491
            with BuildLine():
                Line((-15, 0), (0, 0))
                Line((0, 0), (0, 118))
                Line((0, 118), (-11, 118))
                Line((-11, 118), (-15, 80))
                Line((-15, 80), (-15, 0))
            make_face()
        # TwoSides offset extrude, full=85.5, trim=83
        extrude(amount=85.5)
        extrude(sk.sketch, amount=83, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a rectangular prism or box-shaped component with a tapered pyramidal top and reinforcing ribs or flanges along its sides and interior surfaces.
def model_26942_279de65e_0017():
    """Model: Steering Wheel v5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 13 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 352.8643563256, perimeter: 104.2160890814
            with BuildLine():
                CenterArc((10, 5.3205080757), 10, 150, 30)
                Line((0, 0), (0, 5.3205080757))
                Line((0, 0), (8, 0))
                Line((8, 0), (8, 5.3205080757))
                CenterArc((10, 5.3205080757), 2, 150, 30)
                Line((8.2679491924, 6.3205080757), (20.4803250565, 27.4729635533))
                CenterArc((22.212375864, 26.4729635533), 2, 130, 20)
                Line((20.9268006447, 28.0050524396), (27.9183327554, 33.871644455))
                Line((22.7760318779, 40), (27.9183327554, 33.871644455))
                Line((15.7844997672, 34.1334079845), (22.7760318779, 40))
                CenterArc((22.212375864, 26.4729635533), 10, 130, 20)
                Line((1.3397459622, 10.3205080757), (13.5521218262, 31.4729635533))
            make_face()
        # Symmetric extrude, each_side=11
        extrude(amount=11, both=True)
    return part.part


# Description: This is a long, tapered rectangular duct or channel with a trapezoidal cross-section that narrows toward one end, featuring a open top with internal ribbing or structural reinforcement lines running lengthwise along its surfaces.
def model_27070_53448c4a_0003():
    """Model: Klapka"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.5517702968, perimeter: 9.2578281867
            with BuildLine():
                Line((32.367560461, 12.4126562166), (28.3011079184, 12.4126562166))
                Line((28.3011079184, 12.4126562166), (28.3011079184, 11.7126562166))
                Line((28.8011079184, 11.7126562166), (28.3011079184, 11.7126562166))
                CenterArc((31.1319296384, 6.307732844), 5.8860790476, 77.8820859336, 35.4455749475)
                Line((32.367560461, 12.4126562166), (32.367560461, 12.0626562166))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


# Description: This is a straight cylindrical rod or tube with a uniform diameter, tapered slightly at both ends, rendered in dark gray.
def model_27450_ee1980ca_0000():
    """Model: rura"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 31.4159265359, perimeter: 31.4159265359
            with BuildLine():
                CenterArc((52.5, 0), 3.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((52.5, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            with Locations((52.5, 0)):
                Circle(1.5)
        # OneSide extrude, distance=30
        extrude(amount=30)

        # Sketch1 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 31.4159265359, perimeter: 31.4159265359
            with BuildLine():
                CenterArc((52.5, 0), 3.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((52.5, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=33
        extrude(amount=33, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a trapezoidal sheet metal tray or bracket with a sloped top surface, reinforcing ribs, and a dark structural flange or lip along the bottom edge that provides stiffness and support.
def model_27577_8520e14a_0010():
    """Model: Platform"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 30 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 103.2256, perimeter: 40.64
            with BuildLine():
                Line((50.8, 60.96), (50.8, 50.8))
                Line((50.8, 50.8), (60.96, 50.8))
                Line((60.96, 50.8), (60.96, 60.96))
                Line((60.96, 60.96), (50.8, 60.96))
            make_face()
            # Profile area: 1279.9975516211, perimeter: 268.2240018311
            with BuildLine():
                Line((-50.8, 60.96), (-50.8, 50.8))
                Line((-50.8, 50.8), (-60.96, 50.8))
                Line((-60.96, 50.8), (-60.96, -50.8))
                Line((-50.8, -50.8), (-60.96, -50.8))
                Line((-50.8, -60.96), (-50.8, -50.8))
                Line((-50.8, -60.96), (-48.7679990845, -60.96))
                Line((-48.7679990845, 60.96), (-48.7679990845, -60.96))
                Line((-48.7679990845, 60.96), (-50.8, 60.96))
            make_face()
            # Profile area: 103.2256, perimeter: 40.64
            with BuildLine():
                Line((-60.96, 60.96), (-60.96, 50.8))
                Line((-50.8, 50.8), (-60.96, 50.8))
                Line((-50.8, 60.96), (-50.8, 50.8))
                Line((-50.8, 60.96), (-60.96, 60.96))
            make_face()
            # Profile area: 1498.1585278593, perimeter: 268.4160913363
            with BuildLine():
                Line((24.3840009155, 60.96), (24.3840009155, -60.96))
                Line((24.3840009155, -60.96), (36.6720465837, -60.96))
                Line((36.6720465837, 60.96), (36.6720465837, -60.96))
                Line((36.6720465837, 60.96), (24.3840009155, 60.96))
            make_face()
            # Profile area: 1498.1585278592, perimeter: 268.4160913363
            with BuildLine():
                Line((-24.3839990845, 60.96), (-24.3839990845, -60.96))
                Line((-24.3839990845, -60.96), (-12.0959534163, -60.96))
                Line((-12.0959534163, 60.96), (-12.0959534163, -60.96))
                Line((-12.0959534163, 60.96), (-24.3839990845, 60.96))
            make_face()
            # Profile area: 51.6128, perimeter: 34.6884097937
            with BuildLine():
                Line((-60.96, -60.96), (-50.8, -50.8))
                Line((-50.8, -50.8), (-60.96, -50.8))
                Line((-60.96, -50.8), (-60.96, -60.96))
            make_face()
            # Profile area: 51.6128, perimeter: 34.6884097937
            with BuildLine():
                Line((-50.8, -60.96), (-50.8, -50.8))
                Line((-60.96, -60.96), (-50.8, -50.8))
                Line((-60.96, -60.96), (-50.8, -60.96))
            make_face()
            # Profile area: 1474.7387521408, perimeter: 268.0319086637
            with BuildLine():
                Line((-12.0959534163, 60.96), (-12.0959534163, -60.96))
                Line((-12.0959534163, -60.96), (0.0000009155, -60.96))
                Line((0.0000009155, 60.96), (0.0000009155, -60.96))
                Line((0.0000009155, 60.96), (-12.0959534163, 60.96))
            make_face()
            # Profile area: 103.2256, perimeter: 40.64
            with BuildLine():
                Line((50.8, -50.8), (60.96, -50.8))
                Line((50.8, -60.96), (50.8, -50.8))
                Line((60.96, -60.96), (50.8, -60.96))
                Line((60.96, -50.8), (60.96, -60.96))
            make_face()
            # Profile area: 1498.1585278593, perimeter: 268.4160913363
            with BuildLine():
                Line((-48.7679990845, 60.96), (-48.7679990845, -60.96))
                Line((-48.7679990845, -60.96), (-36.4799534163, -60.96))
                Line((-36.4799534163, 60.96), (-36.4799534163, -60.96))
                Line((-36.4799534163, 60.96), (-48.7679990845, 60.96))
            make_face()
            # Profile area: 1474.7387521407, perimeter: 268.0319086637
            with BuildLine():
                Line((-36.4799534163, 60.96), (-36.4799534163, -60.96))
                Line((-36.4799534163, -60.96), (-24.3839990845, -60.96))
                Line((-24.3839990845, 60.96), (-24.3839990845, -60.96))
                Line((-24.3839990845, 60.96), (-36.4799534163, 60.96))
            make_face()
            # Profile area: 1486.44864, perimeter: 268.224
            with BuildLine():
                Line((36.6720465837, 60.96), (36.6720465837, -60.96))
                Line((36.6720465837, -60.96), (48.8640465837, -60.96))
                Line((48.8640465837, 60.96), (48.8640465837, -60.96))
                Line((48.8640465837, 60.96), (36.6720465837, 60.96))
            make_face()
            # Profile area: 1268.2874405197, perimeter: 268.0319068327
            with BuildLine():
                Line((48.8640465837, 60.96), (48.8640465837, -60.96))
                Line((48.8640465837, -60.96), (50.8, -60.96))
                Line((50.8, -60.96), (50.8, -50.8))
                Line((50.8, -50.8), (60.96, -50.8))
                Line((60.96, -50.8), (60.96, 50.8))
                Line((50.8, 50.8), (60.96, 50.8))
                Line((50.8, 60.96), (50.8, 50.8))
                Line((50.8, 60.96), (48.8640465837, 60.96))
            make_face()
            # Profile area: 1474.7387521408, perimeter: 268.0319086637
            with BuildLine():
                Line((12.2880465837, 60.96), (12.2880465837, -60.96))
                Line((12.2880465837, -60.96), (24.3840009155, -60.96))
                Line((24.3840009155, 60.96), (24.3840009155, -60.96))
                Line((24.3840009155, 60.96), (12.2880465837, 60.96))
            make_face()
            # Profile area: 1498.1585278592, perimeter: 268.4160913363
            with BuildLine():
                Line((0.0000009155, 60.96), (0.0000009155, -60.96))
                Line((0.0000009155, -60.96), (12.2880465837, -60.96))
                Line((12.2880465837, 60.96), (12.2880465837, -60.96))
                Line((12.2880465837, 60.96), (0.0000009155, 60.96))
            make_face()
        # OneSide extrude, distance=13.97
        extrude(amount=13.97)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 30 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 103.2256, perimeter: 40.64
            with BuildLine():
                Line((-60.96, 60.96), (-60.96, 50.8))
                Line((-50.8, 50.8), (-60.96, 50.8))
                Line((-50.8, 60.96), (-50.8, 50.8))
                Line((-50.8, 60.96), (-60.96, 60.96))
            make_face()
            # Profile area: 51.6128, perimeter: 34.6884097937
            with BuildLine():
                Line((-60.96, -60.96), (-50.8, -50.8))
                Line((-50.8, -50.8), (-60.96, -50.8))
                Line((-60.96, -50.8), (-60.96, -60.96))
            make_face()
            # Profile area: 51.6128, perimeter: 34.6884097937
            with BuildLine():
                Line((-50.8, -60.96), (-50.8, -50.8))
                Line((-60.96, -60.96), (-50.8, -50.8))
                Line((-60.96, -60.96), (-50.8, -60.96))
            make_face()
            # Profile area: 103.2256, perimeter: 40.64
            with BuildLine():
                Line((50.8, 60.96), (50.8, 50.8))
                Line((50.8, 50.8), (60.96, 50.8))
                Line((60.96, 50.8), (60.96, 60.96))
                Line((60.96, 60.96), (50.8, 60.96))
            make_face()
            # Profile area: 103.2256, perimeter: 40.64
            with BuildLine():
                Line((50.8, -50.8), (60.96, -50.8))
                Line((50.8, -60.96), (50.8, -50.8))
                Line((60.96, -60.96), (50.8, -60.96))
                Line((60.96, -50.8), (60.96, -60.96))
            make_face()
        # OneSide extrude, distance=-6.35
        extrude(amount=-6.35, mode=Mode.ADD)
    return part.part


# Description: This is a boat hull or ship bow component with a blue trapezoidal main body, dark gray reinforcing ribs or supports extending upward from the sides, and internal structural webbing, designed to provide hydrodynamic shape and structural rigidity.
def model_27663_023746a1_0020():
    """Model: Base v8"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 20 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 35.2089539672, perimeter: 27.4601280479
            with BuildLine():
                CenterArc((8.001, 3.937), 0.38, -86.9453175501, 86.9453175501)
                CenterArc((8.001, 3.937), 0.38, 176.9453175501, 96.1093648998)
                CenterArc((8.001, 3.937), 0.38, 89.9999974467, 86.9453201034)
                Line((8.0010000169, 4.317), (0, 4.317))
                Line((0, 4.317), (0, 0.381))
                CenterArc((0.381, 0.381), 0.381, 93.1896851042, 86.8103148958)
                CenterArc((0.381, 0.381), 0.381, -3.1896851042, 96.3793702084)
                CenterArc((0.381, 0.381), 0.381, -90, 86.8103148958)
                Line((0.381, 0), (8.381, 0))
                Line((8.381, 0), (8.381, 3.937))
            make_face()
            # Profile area: 0.0499592885, perimeter: 1.2088555933
            with BuildLine():
                Line((0.359800491, 0.7614097538), (0.7614097538, 0.359800491))
                CenterArc((0.381, 0.381), 0.381, -3.1896851042, 96.3793702084)
            make_face()
            # Profile area: 0.3445022267, perimeter: 3.2006064844
            with BuildLine():
                CenterArc((0.381, 0.381), 0.381, -90, 86.8103148958)
                Line((0.359800491, 0.7614097538), (0.7614097538, 0.359800491))
                CenterArc((0.381, 0.381), 0.381, 93.1896851042, 86.8103148958)
                CenterArc((0.381, 0.381), 0.381, -180, 90)
            make_face()
            with BuildLine():
                CenterArc((0.381, 0.381), 0.14, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0493201303, perimeter: 1.2026966008
            with BuildLine():
                Line((7.6215399302, 3.957249825), (8.021249825, 3.5575399302))
                CenterArc((8.001, 3.937), 0.38, 176.9453175501, 96.1093648998)
            make_face()
            # Profile area: 0.3427506329, perimeter: 3.1951100674
            with BuildLine():
                CenterArc((8.001, 3.937), 0.38, 0, 89.9999974467)
                CenterArc((8.001, 3.937), 0.38, 89.9999974467, 86.9453201034)
                Line((7.6215399302, 3.957249825), (8.021249825, 3.5575399302))
                CenterArc((8.001, 3.937), 0.38, -86.9453175501, 86.9453175501)
            make_face()
            with BuildLine():
                CenterArc((8.001, 3.937), 0.14, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.254
        extrude(amount=-0.254)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 20 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3427506329, perimeter: 3.1951100674
            with BuildLine():
                CenterArc((8.001, 3.937), 0.38, 0, 89.9999974467)
                CenterArc((8.001, 3.937), 0.38, 89.9999974467, 86.9453201034)
                Line((7.6215399302, 3.957249825), (8.021249825, 3.5575399302))
                CenterArc((8.001, 3.937), 0.38, -86.9453175501, 86.9453175501)
            make_face()
            with BuildLine():
                CenterArc((8.001, 3.937), 0.14, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.3445022267, perimeter: 3.2006064844
            with BuildLine():
                CenterArc((0.381, 0.381), 0.381, -90, 86.8103148958)
                Line((0.359800491, 0.7614097538), (0.7614097538, 0.359800491))
                CenterArc((0.381, 0.381), 0.381, 93.1896851042, 86.8103148958)
                CenterArc((0.381, 0.381), 0.381, -180, 90)
            make_face()
            with BuildLine():
                CenterArc((0.381, 0.381), 0.14, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.524
        extrude(amount=1.524, mode=Mode.ADD)
    return part.part


# Description: This is a linear bearing or rail component with an elongated rectangular body, featuring a central cylindrical shaft, mounting flanges at both ends, and internal guide mechanisms for smooth linear motion.
def model_27679_501db761_0024():
    """Model: 17_19"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 17.7948745629, perimeter: 28.4671470697
            with BuildLine():
                CenterArc((1.25, 10), 1, 95.7391704773, 168.5216590455)
                Line((1.15, 10.9949874371), (1.15, 12))
                Line((1.15, 12), (-0.2428786102, 12))
                Line((-0.4726126277, 11.835081471), (-0.2428786102, 12))
                Line((-0.4726126277, 2.870681471), (-0.4726126277, 11.835081471))
                Line((-0.4726126277, 2.870681471), (0, 0))
                Line((0, 0), (1.25, 0))
                Line((1.25, 0), (1.25, 0.96))
                CenterArc((1.25, 1.5), 0.54, 90, 180)
                Line((1.25, 2.04), (1.25, 8.5000125629))
                Line((1.15, 8.5000125629), (1.25, 8.5000125629))
                Line((1.15, 9.0050125629), (1.15, 8.5000125629))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


# Description: This is a rectangular box-shaped component with an open top, featuring angled side walls and what appears to be internal ribbing or structural supports, designed as a containment or mounting structure.
def model_27682_04277f62_0002():
    """Model: pedal"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 23 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.3519071315, perimeter: 6.3519071315
            with BuildLine():
                Line((7.3, 2), (7.3, 0))
                Line((6.1240464343, 2), (7.3, 2))
                Line((6.1240464343, 1), (6.1240464343, 2))
                Line((6.1240464343, 0), (6.1240464343, 1))
                Line((7.3, 0), (6.1240464343, 0))
            make_face()
            # Profile area: 10.95, perimeter: 17.6
            with BuildLine():
                Line((7.3, 3.5), (7.3, 2))
                Line((0, 3.5), (7.3, 3.5))
                Line((0, 3.5), (0, 2.5))
                Line((0, 2.5), (0, 2))
                Line((0, 2), (6.1240464343, 2))
                Line((6.1240464343, 2), (7.3, 2))
            make_face()
            # Profile area: 6.1240464343, perimeter: 14.2480928685
            with BuildLine():
                Line((0, 1), (6.1240464343, 1))
                Line((0, 0), (0, 1))
                Line((6.1240464343, 0), (0, 0))
                Line((6.1240464343, 0), (6.1240464343, 1))
            make_face()
        # Symmetric extrude, each_side=1.25
        extrude(amount=1.25, both=True)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 23 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1, perimeter: 5
            with BuildLine():
                Line((0, 0), (0, 1))
                Line((0, 1), (0, 2))
                Line((0, 2), (-0.5, 2))
                Line((-0.5, 2), (-0.5, 0))
                Line((-0.5, 0), (0, 0))
            make_face()
            # Profile area: 0.1963495408, perimeter: 1.7853981634
            with BuildLine():
                CenterArc((0, 2), 0.5, 90, 90)
                Line((0, 2), (-0.5, 2))
                Line((0, 2.5), (0, 2))
            make_face()
            # Profile area: 3.5707963268, perimeter: 9.1415926536
            with BuildLine():
                Line((-0.5, 2), (-0.5, 0))
                CenterArc((0, 2), 0.5, 90, 90)
                Line((0, 3.5), (0, 2.5))
                CenterArc((0, 2), 1.5, 90, 90)
                Line((-1.5, 2), (-1.5, 0))
                Line((-1.5, 0), (-0.5, 0))
            make_face()
        # Symmetric extrude, each_side=1.25
        extrude(amount=1.25, both=True, mode=Mode.ADD)
    return part.part


# Description: This is a linear shaft or rod with a cylindrical body featuring blue striped texture patterns on both ends and a dark gray central section, designed for rotational or sliding motion in mechanical assemblies.
def model_27725_5cceaeb7_0000():
    """Model: Front Cover"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 13.8227298146, perimeter: 18.1641088073
            with BuildLine():
                Line((2.54, 0), (3.556, 0))
                CenterArc((0, 0), 2.54, 0, 180.252726285)
                Line((-2.5399752908, -0.0112036643), (-3.5559752908, -0.0112036643))
                Line((-3.5559752908, -0.0112036643), (-3.5559752908, -0.52024407))
                Line((3.556, -0.52024407), (-3.5559752908, -0.52024407))
                Line((3.556, 0), (3.556, -0.52024407))
            make_face()
        # Symmetric extrude, each_side=14.986
        extrude(amount=14.986, both=True)
    return part.part


# Description: This is a toroidal (doughnut-shaped) mesh or perforated component featuring a hollow center ring with a latticed or mesh surface pattern throughout its outer and inner surfaces.
def model_27733_626709f1_0001():
    """Model: Xtreme Solid V Wheel"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.4756535508, perimeter: 12.5349546878
            with BuildLine():
                CenterArc((0, 0), 1.195, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.5115
        extrude(amount=0.5115, both=True)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2434734307, perimeter: 9.7389372261
            with BuildLine():
                CenterArc((0, 0), 0.8, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.05
        extrude(amount=0.05, both=True, mode=Mode.ADD)
    return part.part


# Description: This is a hexagonal hollow spacer or bushing with a central oval aperture and internal curved/ribbed surfaces, featuring a symmetric design with tapered side walls.
def model_27839_4a077326_0016():
    """Model: Nakretka przeciwwagi"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.9609281078, perimeter: 7.0166062226
            with BuildLine():
                Line((5.6516775163, 16.2218320722), (6.3033420516, 15.8494523377))
                Line((6.3033420516, 15.8494523377), (6.9516646293, 16.2276205129))
                Line((6.9516646293, 16.2276205129), (6.9483226715, 16.9781684225))
                Line((6.9483226715, 16.9781684225), (6.2966581361, 17.350548157))
                Line((6.2966581361, 17.350548157), (5.6483355585, 16.9723799819))
                Line((5.6483355585, 16.9723799819), (5.6516775163, 16.2218320722))
            make_face()
            with BuildLine():
                CenterArc((6.3000000939, 16.6000002474), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.55
        extrude(amount=0.55)
    return part.part


# Description: This is a flat parallelogram plate or panel with a trapezoidal top surface, featuring a uniform thickness and beveled or angled edges that create a 3D wedge-like appearance.
def model_28119_f4fb1c4c_0004():
    """Model: Component5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.2, perimeter: 16.8
            with BuildLine():
                Line((-4.0153118696, 14.0019218359), (3.9846881304, 14.0019218359))
                Line((3.9846881304, 14.4019218359), (3.9846881304, 14.0019218359))
                Line((-4.0153118696, 14.4019218359), (3.9846881304, 14.4019218359))
                Line((-4.0153118696, 14.0019218359), (-4.0153118696, 14.4019218359))
            make_face()
        # Symmetric extrude, each_side=3
        extrude(amount=3, both=True)
    return part.part


# Description: This is a flat, rectangular base plate or platform with a trapezoidal top surface and beveled edges, featuring a shallow, dish-like depression across its upper face.
def model_28382_90b7cc0c_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 240, perimeter: 64
            with BuildLine():
                Line((10, -6), (10, 6))
                Line((10, 6), (-10, 6))
                Line((-10, 6), (-10, -6))
                Line((-10, -6), (10, -6))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a roof truss or structural frame component with a triangular peaked shape, featuring a solid dark base supporting an upper latticed or wireframe triangular structure that tapers to a point.
def model_28458_00521a97_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch11 -> 押し出し1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.1887902048, perimeter: 10.0943951024
            with BuildLine():
                Line((0, 0), (3.4641016151, 2))
                Line((0, 0), (4, 0))
                CenterArc((0, 0), 4, 0, 30)
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a toroidal (donut-shaped) component with a curved arrow or directional flange extending from the top, featuring a large central hole and textured or mesh-patterned surfaces on the inner walls.
def model_28940_05ead503_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.926990817, perimeter: 15.7079632679
            with BuildLine():
                CenterArc((-5, 3), 1.5, 64.6654186272, 34.603422281)
                CenterArc((-5, 3), 1.5, 99.2688409082, 325.396577719)
            make_face()
            with BuildLine():
                CenterArc((-5, 3), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1288769997, perimeter: 2.6842300014
            with BuildLine():
                Line((-4.3581448212, 4.3557366741), (-5.5123998655, 4.9022031022))
                Line((-5.5123998655, 4.9022031022), (-5.2416006751, 4.4804151829))
                CenterArc((-5, 3), 1.5, 64.6654186272, 34.603422281)
            make_face()
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)
    return part.part


# Description: This is an oval/elliptical shell or cover with a wireframe surface texture, featuring a smoothly curved outer perimeter and internal ribbed or linear structural elements running diagonally across its face.
def model_29122_80d91b52_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch18 -> Extrude11 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 50.2654824574, perimeter: 25.1327412287
            with Locations((30, 0)):
                Circle(4)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a cylindrical mesh filter or strainer with a closed bottom and open top featuring a perforated mesh screen, designed for liquid or particle filtration applications.
def model_29592_d1e941d1_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0349070782, perimeter: 0.6623105632
            Circle(0.10541)
        # OneSide extrude, distance=0.508
        extrude(amount=0.508)
    return part.part


# Description: This is a polyhedral geometric solid with an irregular, faceted shape featuring multiple triangular and quadrilateral faces in varying shades of blue and dark gray, resembling a truncated or distorted polyhedron with no obvious holes, slots, or curved surfaces.
def model_29746_74549e58_0008():
    """Model: Pieza 8 v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
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
        # OneSide extrude, distance=0.35
        extrude(amount=0.35)
    return part.part


# Description: This is a tapered wedge or shim with a elongated rectangular profile, featuring a pointed end and a flat base, commonly used for alignment, spacing, or securing purposes.
def model_30274_ca0d10b2_0006():
    """Model: ArmD"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 12 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0040000254, perimeter: 0.4400025524
            with BuildLine():
                Line((-1.1899999739, -0.2999987117), (-1.209999973, -0.2999987117))
                Line((-1.209999973, -0.2999987117), (-1.209999973, -0.4999999888))
                Line((-1.1899999739, -0.4999999888), (-1.209999973, -0.4999999888))
                Line((-1.1899999739, -0.4999999888), (-1.1899999739, -0.2999987117))
            make_face()
            # Profile area: 0.2878924186, perimeter: 3.1383596154
            with BuildLine():
                Line((-1.1899999739, 0.849999981), (-1.4092229018, 0.8499859778))
                Line((-1.4091494446, -0.2999987117), (-1.4092229018, 0.8499859778))
                Line((-1.4091494446, -0.2999987117), (-1.3891494446, -0.2999974342))
                Line((-1.3891494446, -0.2999974342), (-1.3891494446, -0.4999999888))
                Line((-1.209999973, -0.4999999888), (-1.3891494446, -0.4999999888))
                Line((-1.209999973, -0.2999987117), (-1.209999973, -0.4999999888))
                Line((-1.1899999739, -0.2999987117), (-1.209999973, -0.2999987117))
                Line((-1.1899999739, -0.2999987117), (-1.1899999739, 0.849999981))
            make_face()
            # Profile area: 0.0039987608, perimeter: 0.4399910567
            with BuildLine():
                Line((-1.3891494446, -0.2999974342), (-1.3891494446, -0.4999999888))
                Line((-1.4091494446, -0.2999987117), (-1.3891494446, -0.2999974342))
                Line((-1.4091366692, -0.4999999888), (-1.4091494446, -0.2999987117))
                Line((-1.3891494446, -0.4999999888), (-1.4091366692, -0.4999999888))
            make_face()
        # OneSide extrude, distance=0.02
        extrude(amount=0.02)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 12 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0040000254, perimeter: 0.4400025524
            with BuildLine():
                Line((-1.1899999739, -0.2999987117), (-1.209999973, -0.2999987117))
                Line((-1.209999973, -0.2999987117), (-1.209999973, -0.4999999888))
                Line((-1.1899999739, -0.4999999888), (-1.209999973, -0.4999999888))
                Line((-1.1899999739, -0.4999999888), (-1.1899999739, -0.2999987117))
            make_face()
            # Profile area: 0.0039987608, perimeter: 0.4399910567
            with BuildLine():
                Line((-1.3891494446, -0.2999974342), (-1.3891494446, -0.4999999888))
                Line((-1.4091494446, -0.2999987117), (-1.3891494446, -0.2999974342))
                Line((-1.4091366692, -0.4999999888), (-1.4091494446, -0.2999987117))
                Line((-1.3891494446, -0.4999999888), (-1.4091366692, -0.4999999888))
            make_face()
        # OneSide extrude, distance=-0.05
        extrude(amount=-0.05, mode=Mode.ADD)
    return part.part


# Description: This is a reinforced rubber or composite ring/band with an elliptical or oval cross-section, featuring a mesh or woven reinforcement pattern on the outer surface and a solid inner band, designed as a flexible coupling or sealing component.
def model_30400_8824ce97_0021():
    """Model: 18-03-001100-1part1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.931215544, perimeter: 11.5296450387
            with BuildLine():
                CenterArc((0, 0), 1.085, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3085
        extrude(amount=0.3085)
    return part.part


# Description: This is a cylindrical rod or shaft with a long, slender tapered form and a textured or knurled surface, commonly used as a stylus, pen, or tool component.
def model_30400_8824ce97_0034():
    """Model: 18-03-001300-1_18-03-001301-1-solid1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.2082300165, perimeter: 15.2274333882
            with BuildLine():
                CenterArc((5.6, 1.2), 1.2, -90, 90)
                Line((6.8, 1.2), (6.8, 4))
                Line((6.8, 4), (6.2, 4))
                Line((6.2, 1.2), (6.2, 4))
                CenterArc((5.6, 1.2), 0.6, -90, 90)
                Line((2.8, 0.6), (5.6, 0.6))
                Line((2.8, 0), (2.8, 0.6))
                Line((2.8, 0), (5.6, 0))
            make_face()
        # OneSide extrude, distance=80
        extrude(amount=80)
    return part.part


# Description: This is a thin, elongated rectangular plate or trim strip with a shallow curved underside and tapered ends, featuring a streamlined aerodynamic profile typical of automotive body trim or weatherstripping components.
def model_30417_0010bc7c_0008():
    """Model: Tube guide cover"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 19 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 45.9071273292, perimeter: 41.0464999281
            with BuildLine():
                Line((-8.8962482023, 1.25), (8.8962482023, 1.25))
                Line((-8.8962482023, 1.25), (-9.25, 0.7653767797))
                Line((-9.25, -0.7653767797), (-9.25, 0.7653767797))
                Line((-8.8962482023, -1.25), (-9.25, -0.7653767797))
                Line((8.8962482023, -1.25), (-8.8962482023, -1.25))
                Line((8.8962482023, -1.25), (9.25, -0.7653767797))
                Line((9.25, 0.7653767797), (9.25, -0.7653767797))
                Line((8.8962482023, 1.25), (9.25, 0.7653767797))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is a hexagonal prism or shaft component with a pointed/tapered nose cone on one end, featuring parallel grooves or flutes running along its length, and a flat base or mounting surface.
def model_30417_0010bc7c_0013():
    """Model: Gear (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 17 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(3.9869511092, -0.4792480899, 0.8455524673), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0563639425, perimeter: 1.0893646862
            with BuildLine():
                CenterArc((-0.8370471281, 2.5696027622), 0.9833083092, 10.6837604658, 15.2495618249)
                CenterArc((0, 0), 3, 89.0976388824, 1.8047222352)
                CenterArc((0.8370471281, 2.5696027622), 0.9833083092, 154.0666777093, 15.2495618249)
                CenterArc((-0.175892512, 2.7607023589), 0.0475, -86.3544439599, 75.6706834941)
                CenterArc((0, 0), 2.7188, 86.3544439599, 7.2911120802)
                CenterArc((0.175892512, 2.7607023589), 0.0475, -169.3162395342, 75.6706834941)
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a cylindrical manifold or pipe component featuring a rounded body with a tapered nozzle or spout on the left end and a flat or slightly curved surface on the right end, designed for fluid or gas flow applications.
def model_30417_0010bc7c_0014():
    """Model: Shaft_2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 21 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0202778338, perimeter: 0.6339807151
            with BuildLine():
                CenterArc((-0.0976575538, 0.4405047584), 0.1641697351, -12.0713607185, 58.6760325636)
                CenterArc((0, 0), 0.56, 88.4516290022, 3.0967419956)
                CenterArc((0.0976575538, 0.4405047584), 0.1641697351, 133.3953281549, 58.6760325636)
                CenterArc((-0.0926098344, 0.3998144302), 0.0304, -76.9584559908, 89.0298167092)
                CenterArc((0, 0), 0.38, 76.9584559908, 26.0830880185)
                CenterArc((0.0926098344, 0.3998144302), 0.0304, 167.9286392815, 89.0298167092)
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a pencil or stylus with a hexagonal body, featuring a pointed conical tip on the left end and a flat rectangular back end, with a wireframe mesh surface indicating a 3D solid model.
def model_30417_0010bc7c_0016():
    """Model: Gear"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 17 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0231281301, perimeter: 0.6982398356
            with BuildLine():
                CenterArc((-0.5614572909, 1.7152459738), 0.6566789404, 11.0515678228, 14.6240780034)
                CenterArc((0, 0), 2, 89.1295861691, 1.7408276618)
                CenterArc((0.5614572909, 1.7152459738), 0.6566789404, 154.3243541738, 14.6240780034)
                CenterArc((-0.1128798066, 1.8469537919), 0.0304, -86.5026185821, 75.4510507593)
                CenterArc((0, 0), 1.82, 86.5026185821, 6.9947628358)
                CenterArc((0.1128798066, 1.8469537919), 0.0304, -168.9484321772, 75.4510507593)
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a shoe sole or insole component featuring an elongated, curved footprint shape with textured upper surface, reinforced dark edges/flanges along the perimeter, and internal ribbed or structural reinforcement patterns visible through the semi-transparent mesh design.
def model_30418_de83ae84_0009():
    """Model: Part4 Junta:1 (1)"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 23 constraints, 17 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0116387077, perimeter: 0.9257317737
            with BuildLine():
                Line((0.0567, -0.075), (0.0567, -0.1))
                CenterArc((0.0817, -0.1), 0.025, 180, 50.3083045263)
                Line((0.0657335927, -0.1192373033), (0.1004335927, -0.1480373033))
                CenterArc((0.1164, -0.1288), 0.025, -129.6916954737, 125.282619515)
                Line((0.1413260147, -0.1307219241), (0.1451359054, -0.0835116771))
                CenterArc((0.1206, -0.079), 0.024947262, -10.4191914622, 50.5984253841)
                Line((0.1396604545, -0.0629045051), (0.0951075805, -0.0101445227))
                CenterArc((0.075, -0.025), 0.025, 36.4569828115, 53.5430171885)
                Line((0, 0), (0.075, 0))
                CenterArc((0, -0.025), 0.025, 90, 180)
                Line((0, -0.05), (0.0317, -0.05))
                CenterArc((0.0317, -0.075), 0.025, 0, 90)
            make_face()
            with BuildLine():
                CenterArc((0.1164, -0.1288), 0.0125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.1206, -0.079), 0.0125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.075, -0.025), 0.0125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.0817, -0.1), 0.0125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, -0.025), 0.0125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.0125
        extrude(amount=0.0125)
    return part.part


# Description: This is an elongated, boat-shaped channel or tray with a tapered design, featuring a curved bottom surface, raised flanged edges along the sides, and a streamlined profile that narrows toward one end.
def model_30419_d55a0a22_0003():
    """Model: crank"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.0360283014, perimeter: 6.9729122859
            with BuildLine():
                CenterArc((0, 0), 1.25, 76.5851512438, 26.8296975125)
                Line((-0.29, 1.2158947323), (-0.925, -0.840758586))
                CenterArc((0, 0), 1.25, -137.7314155704, 95.4628311409)
                Line((0.29, 1.2158947323), (0.925, -0.840758586))
            make_face()
        # OneSide extrude, distance=0.22
        extrude(amount=0.22)
    return part.part


# Description: This is a tapered cylindrical pin or punch with a elongated cone-shaped body that gradually narrows from a wider base to a sharp pointed tip, commonly used as a mechanical fastener, alignment pin, or drift punch.
def model_30419_d55a0a22_0004():
    """Model: tumbler plate"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 18 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.5132078094, perimeter: 14.9049084099
            with BuildLine():
                Line((0.275, -0.6), (0.275, 0.6))
                Line((0.275, 0.6), (0.4329275987, 0.6))
                Line((0.4329275987, 0.6), (0.275156094, 2.85))
                Line((0.145156094, 2.85), (0.275156094, 2.85))
                Line((0.145156094, 2.85), (0.145156094, 3.4035428908))
                CenterArc((0, 3.2), 0.25, 54.5055301019, 121.4834169154)
                Line((-0.475, 0), (-0.2493876437, 3.2174872284))
                Line((-0.475, 0), (-0.2493876437, -3.2174872284))
                CenterArc((0, -3.2), 0.25, -175.9889470173, 121.4834169154)
                Line((0.145156094, -2.85), (0.145156094, -3.4035428908))
                Line((0.145156094, -2.85), (0.275156094, -2.85))
                Line((0.4329275987, -0.6), (0.275156094, -2.85))
                Line((0.275, -0.6), (0.4329275987, -0.6))
            make_face()
        # OneSide extrude, distance=0.16
        extrude(amount=0.16)
    return part.part


# Description: This is a tapered needle or stylus with a sharp pointed tip, featuring a long slender shaft that gradually reduces in diameter toward the fine point at the end.
def model_30421_211edb5e_0003():
    """Model: Long cutter"""
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
        # Sketch has 8 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 39.5781716615, perimeter: 80.0602992252
            with BuildLine():
                _nurbs_edge([(16.2370154727, 2.5698497506), (16.2338178728, 2.5693621868), (16.2109157503, 2.5658630383), (16.1159880886, 2.5512661919), (15.7936201003, 2.5010487162), (14.9412365575, 2.3648067581), (13.314124978, 2.0936851398), (11.2182609629, 1.7264362106), (8.8801688206, 1.2892999026), (6.5588366872, 0.8156309219), (4.4973815555, 0.3400215459), (2.8772371829, -0.1072724605), (1.7663329554, -0.5064961161), (1.0813514346, -0.8531220545), (0.657007613, -1.1518957915), (0.3007320188, -1.4122793811), (-0.1422826856, -1.6430561924), (-0.6238412359, -1.8073924155), (-1.0674507728, -1.9199666275), (-1.3996696111, -1.9902780144), (-1.5749026044, -2.0242494554)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.3913768453, 0.3913768453, 0.3913768453, 0.3913768453, 0.3913768453, 0.3913768453, 0.4, 0.44, 0.48, 0.52, 0.56, 0.6, 0.64, 0.68, 0.72, 0.76, 0.8, 0.84, 0.88, 0.92, 0.96, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(33.7096327454, 5.4791296937), (32.6852070308, 5.310542605), (30.7136968488, 4.9859755142), (27.9884543671, 4.5369459961), (24.8200622856, 4.0140807903), (21.6355069127, 3.487004108), (19.2161065556, 3.084741978), (17.5303911519, 2.8023027386), (16.5171707582, 2.6299352773), (16.074217896, 2.551330941), (16.0538445119, 2.5435730152), (16.1494398527, 2.5568355437), (16.2123169306, 2.5661418762), (16.2330630894, 2.5692544927), (16.2370154727, 2.5698497506)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.04, 0.08, 0.12, 0.16, 0.2, 0.24, 0.28, 0.32, 0.36, 0.3728185939, 0.3728185939, 0.3728185939, 0.3728185939, 0.3728185939, 0.3728185939], 5)
                _nurbs_edge([(34.2961325751, 6.2848310763), (34.3224894577, 6.2606114584), (34.3716884613, 6.2129202287), (34.4349422504, 6.1436274942), (34.4978479722, 6.0557984476), (34.538523472, 5.954090015), (34.5385320013, 5.8610362637), (34.4956936007, 5.7771011291), (34.41073363, 5.7021302414), (34.2869229706, 5.6354274967), (34.1279917386, 5.5761990575), (33.9754034998, 5.5342310996), (33.8476210912, 5.5055943908), (33.756600907, 5.48774439), (33.7096327454, 5.4791296937)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                Line((5.3711448866, 1.8968957145), (34.2961325751, 6.2848310763))
                _nurbs_edge([(-1.0742149834, 0.2296626265), (-1.0662815511, 0.2583360567), (-1.0461058146, 0.3159751814), (-1.0029158298, 0.4033104706), (-0.9193688653, 0.5215195711), (-0.7719142612, 0.6714297308), (-0.5832393311, 0.8210724013), (-0.357905622, 0.965458943), (-0.1020839562, 1.0983591479), (0.1777393922, 1.2138305669), (0.4758514384, 1.3075266063), (0.7887269803, 1.3785148797), (1.1152656766, 1.4294275837), (1.4559506207, 1.465076147), (1.8123110061, 1.4915383004), (2.18627908, 1.5151172117), (2.5795532616, 1.5413273856), (2.9930335243, 1.5740110005), (3.42708445, 1.6157362813), (3.881689329, 1.6680430175), (4.3566170469, 1.7317196984), (4.7525682135, 1.7919771195), (5.0584156998, 1.8424078606), (5.2662464226, 1.8783467033), (5.3711448866, 1.8968957145)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(-1.7185439575, -0.9184144547), (-1.7184533492, -0.9184150762), (-1.6946566458, -0.9185693041), (-1.647865893, -0.9141545449), (-1.5801189726, -0.893353256), (-1.4954711815, -0.8385976689), (-1.4005884617, -0.7336264758), (-1.3173811724, -0.6031748339), (-1.2462668791, -0.458910789), (-1.1873622383, -0.3106799886), (-1.1405971139, -0.1647269575), (-1.105798167, -0.0247306891), (-1.0873710549, 0.0811195713), (-1.0787711255, 0.1568191595), (-1.0753485743, 0.2056534967), (-1.0742149834, 0.2296626265)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.4998089032, 0.4998089032, 0.4998089032, 0.4998089032, 0.4998089032, 0.4998089032, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(-1.7185439575, -0.9184144547), (-1.6864014553, -0.9338701869), (-1.624704933, -0.9653707181), (-1.5399255301, -1.0143887007), (-1.4426731609, -1.0833386573), (-1.3491763347, -1.1759137475), (-1.2861442268, -1.2754217642), (-1.2558890134, -1.3823888948), (-1.2593488918, -1.497028647), (-1.2948327945, -1.6189561806), (-1.3597718528, -1.7475868923), (-1.4332786718, -1.8553969132), (-1.4997517553, -1.9388357747), (-1.5490258328, -1.9955901426), (-1.5749026044, -2.0242494554)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on YZ construction plane
        # Sketch has 8 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.6391094823, perimeter: 5.5543711742
            with BuildLine():
                _nurbs_edge([(-1.5749026044, -2.0242494554), (-1.6165009637, -2.0226128098), (-1.6981126572, -2.017772146), (-1.8157753433, -2.0058092509), (-1.9629908549, -1.980298327), (-2.1297886858, -1.9313799095), (-2.2777706422, -1.8638551693), (-2.4053128154, -1.7761182829), (-2.5113729401, -1.6671385929), (-2.5965912559, -1.5375492084), (-2.662454917, -1.3888207213), (-2.7008886089, -1.255739477), (-2.7221975057, -1.1484958813), (-2.7331170663, -1.0737503803), (-2.7377552439, -1.0355651773)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(-1.7185439575, -0.9184144547), (-1.6864014553, -0.9338701869), (-1.624704933, -0.9653707181), (-1.5399255301, -1.0143887007), (-1.4426731609, -1.0833386573), (-1.3491763347, -1.1759137475), (-1.2861442268, -1.2754217642), (-1.2558890134, -1.3823888948), (-1.2593488918, -1.497028647), (-1.2948327945, -1.6189561806), (-1.3597718528, -1.7475868923), (-1.4332786718, -1.8553969132), (-1.4997517553, -1.9388357747), (-1.5490258328, -1.9955901426), (-1.5749026044, -2.0242494554)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(-2.7377552439, 0), (-2.7280460101, -0.0094610399), (-2.7072898658, -0.0304490012), (-2.6721425126, -0.0681290853), (-2.6172212643, -0.1308117777), (-2.5351530431, -0.2293420811), (-2.4400667399, -0.3457537551), (-2.3329997969, -0.4751602457), (-2.2160246311, -0.6086249563), (-2.092208472, -0.7336962731), (-1.9652450541, -0.8368117691), (-1.8641323658, -0.8917745214), (-1.7901886989, -0.9132591345), (-1.7421608016, -0.9182524623), (-1.7185439575, -0.9184144547)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.4998089032, 0.4998089032, 0.4998089032, 0.4998089032, 0.4998089032, 0.4998089032], 5)
                Line((-2.7377552439, -1.0355651773), (-2.7377552439, 0))
            make_face()
        # Symmetric extrude, each_side=1
        extrude(amount=1, both=True, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical rod or pin with a slightly rounded, tapered end at the top and a flat or blunt end at the bottom, featuring a smooth, elongated rectangular profile when viewed from this angle.
def model_30426_2cde26de_0009():
    """Model: raggio1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            Circle(0.75)
        # Symmetric extrude, each_side=17.5
        extrude(amount=17.5, both=True)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 10.7992247467, perimeter: 17.2787595947
            with BuildLine():
                CenterArc((0, 0), 2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=16.5
        extrude(amount=16.5, both=True, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical housing or adapter with a geometric, multi-faceted head section featuring triangular flanges and internal cavities, designed for mechanical assembly or mounting purposes.
def model_30447_4ed3b778_0010():
    """Model: Valve Rod Packing Gland"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1662816935, perimeter: 3.7158371402
            with BuildLine():
                Line((0.1833087105, -0.3175), (0.3666174209, 0))
                Line((0.3666174209, 0), (0.1833087105, 0.3175))
                Line((0.1833087105, 0.3175), (-0.1833087105, 0.3175))
                Line((-0.1833087105, 0.3175), (-0.3666174209, 0))
                Line((-0.3666174209, 0), (-0.1833087105, -0.3175))
                Line((-0.1833087105, -0.3175), (0.1833087105, -0.3175))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2413, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1390962701, perimeter: 2.2582396313
            with BuildLine():
                CenterArc((0, 0), 0.2413, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.11811, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.15875
        extrude(amount=0.15875)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1390962701, perimeter: 2.2582396313
            with BuildLine():
                CenterArc((0, 0), 0.2413, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.11811, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.47498
        extrude(amount=-0.47498, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical tube or pipe with a hollow interior, featuring a slightly textured or roughened top end and a smooth cylindrical body, oriented at an angle.
def model_30713_06b3d0ec_0006():
    """Model: Cuerpo"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            Circle(1.5)
        # Symmetric extrude, each_side=10
        extrude(amount=10, both=True)
    return part.part


# Description: This is a cylindrical sleeve or bushing with an elongated oval shape, featuring a central hollow core and a mesh or perforated pattern on the upper outer surface, suggesting it may serve as a filter, spacer, or structural component.
def model_30713_06b3d0ec_0011():
    """Model: Rueda (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 30.6305283725, perimeter: 40.8407044967
            with BuildLine():
                CenterArc((0, 0), 4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=1
        extrude(amount=1, both=True)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.5663706144, perimeter: 25.1327412287
            with BuildLine():
                CenterArc((0, 0), 2.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.5
        extrude(amount=0.5, both=True, mode=Mode.ADD)
    return part.part


# Description: This is a dual-chamber housing or bracket component with an angular, asymmetrical design featuring two dark box-like chambers connected by a curved central section, with internal slots and openings visible on the upper surfaces.
def model_30713_06b3d0ec_0017():
    """Model: Fijación"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 32 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 53.2582280506, perimeter: 42.5116529373
            with BuildLine():
                Line((-3.5672686263, 1.8095840814), (-5.3041560267, -1.6143761504))
                CenterArc((-10.6550589662, 1.0999999717), 6, -90, 63.1024856426)
                Line((-14.970868935, -4.9000000283), (-10.6550589662, -4.9000000283))
                CenterArc((-14.970868935, -6.4000000283), 1.5, 90, 180)
                Line((-7.7000001147, -7.9000000283), (-14.970868935, -7.9000000283))
                CenterArc((-7.7000001147, -1.9000000283), 6, -90, 47.2714247458)
                CenterArc((4.0532204237, -12.7564178065), 10, 118.1973846169, 19.0740401289)
                CenterArc((0, 0), 4, 153.1024856426, 107.2276312165)
            make_face()
            # Profile area: 43.1968989869, perimeter: 37.0575191895
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
                Line((-1.3377257349, 0.6785940305), (-3.5672686263, 1.8095840814))
                CenterArc((0, 0), 4, 153.1024856426, 107.2276312165)
                CenterArc((0, 0), 4, -99.6698831409, 19.0413556406)
                CenterArc((0, 0), 4, -80.6285275004, 107.2276312165)
                CenterArc((0, 0), 4, 26.5991037161, 126.5033819265)
            make_face()
            # Profile area: 53.2582280506, perimeter: 42.5116529373
            with BuildLine():
                CenterArc((-4.1196037402, -12.73513471), 10, 42.4301646129, 19.0740401289)
                CenterArc((7.6900000534, -1.9400775894), 6, -137.5698353871, 47.2714247458)
                Line((7.6587507054, -7.939996212), (14.9295209117, -7.9778645303))
                CenterArc((14.9373332487, -6.4778848747), 1.5, -90.2984106413, 180)
                Line((14.9451455857, -4.977905219), (10.6293941517, -4.9554275111))
                CenterArc((10.6606434997, 1.0444911116), 6, -153.4008962839, 63.1024856426)
                Line((3.5766449643, 1.7909804017), (5.2956760533, -1.6419794911))
                CenterArc((0, 0), 4, -80.6285275004, 107.2276312165)
            make_face()
        # Symmetric extrude, each_side=2.5
        extrude(amount=2.5, both=True)
    return part.part


# Description: This is a rectangular hollow tube or channel with a closed top end and an open bottom end, featuring a uniform extruded prismatic shape with straight walls and sharp edges.
def model_31008_8fa25b35_0001():
    """Model: 6 v5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 16, perimeter: 20
            with BuildLine():
                Line((1, -4), (1, 4))
                Line((1, 4), (-1, 4))
                Line((-1, 4), (-1, -4))
                Line((-1, -4), (1, -4))
            make_face()
        # Symmetric extrude, each_side=0.5
        extrude(amount=0.5, both=True)
    return part.part


# Description: This is an elongated rectangular prism or beam with a beveled or chamfered edge along its length, featuring a slight diagonal orientation and uniform cross-section throughout.
def model_31008_8fa25b35_0003():
    """Model: pad v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 14.24, perimeter: 21
            with BuildLine():
                Line((0.8, -4.45), (0.8, 4.45))
                Line((0.8, 4.45), (-0.8, 4.45))
                Line((-0.8, 4.45), (-0.8, -4.45))
                Line((-0.8, -4.45), (0.8, -4.45))
            make_face()
        # OneSide extrude, distance=0.478
        extrude(amount=0.478)
    return part.part


# Description: This is a rectangular extruded beam or rail with a uniform prismatic shape, featuring a slightly tapered or beveled top edge and a flat base, designed for structural support or linear guidance applications.
def model_31008_8fa25b35_0004():
    """Model: END PLATE v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 9 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.3213248654, perimeter: 9.0773502692
            with BuildLine():
                Line((-0.475, 0.9), (-0.475, -1.9))
                Line((-0.475, -1.9), (0.475, -1.9))
                Line((0.475, -1.9), (0.475, 1.9))
                Line((0.475, 1.9), (0.1023502692, 1.9))
                Line((-0.475, 0.9), (0.1023502692, 1.9))
            make_face()
        # Symmetric extrude, each_side=9.4
        extrude(amount=9.4, both=True)
    return part.part


# Description: This is a mesh trucker cap/baseball hat featuring a solid front panel with a curved bill/visor and a ventilated mesh back panel for breathability.
def model_31259_72b86045_0000():
    """Model: Drive Gear"""
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
            # Profile area: 0.7608559925, perimeter: 3.0921187535
            with BuildLine():
                CenterArc((0, 0), 0.4921259843, 9.71137289, 340.5772542201)
                CenterArc((0, 0), 0.4921259843, -9.71137289, 19.4227457799)
            make_face()
        # OneSide extrude, distance=0.490000036
        extrude(amount=0.490000036)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0516108416, perimeter: 0.8809829901
            with BuildLine():
                Line((0.4850738216, 0.0830142878), (0.6074996668, 0.1039659325))
                CenterArc((0, 0), 0.4921259843, -9.71137289, 19.4227457799)
                Line((0.4850738216, -0.0830142878), (0.6074996668, -0.1039659325))
                _nurbs_edge([(0.6074996668, -0.1039659325), (0.6139204293, -0.1042109142), (0.6269593392, -0.1047084089), (0.6466440241, -0.1017775566), (0.6665552608, -0.0973812119), (0.6866134285, -0.0912572892), (0.7067403328, -0.0836595266), (0.7268764822, -0.0746328889), (0.7469463921, -0.0642197357), (0.766949108, -0.0525384587), (0.7799043912, -0.0438166686), (0.7864574112, -0.0394050271)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0192373039, 0.0390659946, 0.0594578937, 0.0804070194, 0.1019097437, 0.1239633258, 0.1465655208, 0.1697144309, 0.1934084382, 0.1934084382, 0.1934084382, 0.1934084382], 3)
                CenterArc((-0.0353623959, 0), 0.8227639707, -2.7451442316, 5.4902884632)
                _nurbs_edge([(0.6074996668, 0.1039659325), (0.6139204293, 0.1042109142), (0.6269593392, 0.1047084089), (0.6466440241, 0.1017775566), (0.6665552608, 0.0973812119), (0.6866134285, 0.0912572892), (0.7067403328, 0.0836595266), (0.7268764822, 0.0746328889), (0.7469463921, 0.0642197357), (0.766949108, 0.0525384587), (0.7799043912, 0.0438166686), (0.7864574112, 0.0394050271)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0192373039, 0.0390659946, 0.0594578937, 0.0804070194, 0.1019097437, 0.1239633258, 0.1465655208, 0.1697144309, 0.1934084382, 0.1934084382, 0.1934084382, 0.1934084382], 3)
            make_face()
        # OneSide extrude, distance=0.490000036
        extrude(amount=0.490000036, mode=Mode.ADD)
    return part.part


# Description: This is a gear or sprocket with a circular disk body, featuring teeth around its circumference and a protruding hub or shaft mounting point on one side.
def model_31259_72b86045_0001():
    """Model: Large Gear"""
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
            # Profile area: 15.179922446, perimeter: 13.8114637658
            with BuildLine():
                CenterArc((0, 0), 2.1981627297, 3.348226589, 353.303546822)
                CenterArc((0, 0), 2.1981627297, -3.348226589, 6.696453178)
            make_face()
        # OneSide extrude, distance=0.500000016
        extrude(amount=0.500000016)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0602372629, perimeter: 0.9799057679
            with BuildLine():
                Line((2.1944104892, 0.1283822072), (2.2159442846, 0.1296420245))
                CenterArc((0, 0), 2.1981627297, -3.348226589, 6.696453178)
                Line((2.1944104892, -0.1283822072), (2.2159442846, -0.1296420245))
                _nurbs_edge([(2.2159442846, -0.1296420245), (2.2261472167, -0.1293252718), (2.2466970407, -0.1286872973), (2.277393291, -0.1238181728), (2.3081876722, -0.1174673121), (2.3390267266, -0.1094120769), (2.3698889459, -0.0999530678), (2.4007536716, -0.0891677868), (2.4315906608, -0.0771237047), (2.462419884, -0.0639579538), (2.4827311891, -0.0543187543), (2.4929491373, -0.0494695908)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0305946271, 0.061620934, 0.0930638115, 0.1249217059, 0.1571940478, 0.189880536, 0.2229809756, 0.2564952243, 0.290423169, 0.290423169, 0.290423169, 0.290423169], 3)
                CenterArc((-0.0081612253, 0), 2.5015995455, -1.13310843, 2.2662168599)
                _nurbs_edge([(2.2159442846, 0.1296420245), (2.2261472167, 0.1293252718), (2.2466970407, 0.1286872973), (2.277393291, 0.1238181728), (2.3081876722, 0.1174673121), (2.3390267266, 0.1094120769), (2.3698889459, 0.0999530678), (2.4007536716, 0.0891677868), (2.4315906608, 0.0771237047), (2.462419884, 0.0639579538), (2.4827311891, 0.0543187543), (2.4929491373, 0.0494695908)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0305946271, 0.061620934, 0.0930638115, 0.1249217059, 0.1571940478, 0.189880536, 0.2229809756, 0.2564952243, 0.290423169, 0.290423169, 0.290423169, 0.290423169], 3)
            make_face()
        # OneSide extrude, distance=0.500000016
        extrude(amount=0.500000016, mode=Mode.ADD)
    return part.part


# Description: This is a toroidal (donut-shaped) ring or spacer with a smooth, rounded outer surface and a central hollow opening, featuring a subtle textured or mesh-like finish on the top surface.
def model_31277_b1263495_0006():
    """Model: 7-8 PLAIN WASHER"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.059681195, perimeter: 21.4492866742
            with BuildLine():
                CenterArc((0, 0), 2.2225, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.19126, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.44958
        extrude(amount=0.44958)
    return part.part


# Description: This is a cylindrical container or tube with an open top featuring a blue mesh or perforated circular cover, and a solid dark gray body with vertical ribbing or fluting along its sides.
def model_31347_386f6298_0002():
    """Model: Handle Plug"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0506707479, perimeter: 0.797964534
            with Locations((7.6312789617, -16.5195275371)):
                Circle(0.127)
        # OneSide extrude, distance=0.2667
        extrude(amount=0.2667)
    return part.part


# Description: This is a rounded rectangular plate or panel with a parallelogram-like trapezoidal shape, featuring uniformly rounded corners and a slight 3D perspective suggesting a flat, thin component.
def model_31347_386f6298_0004():
    """Model: On/Off Button"""
    with BuildPart() as part:
        # Sketch3 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 15 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.27, 12.446), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 16.2423709967, perimeter: 15.4426533741
            with BuildLine():
                CenterArc((-1.778, 6.5384505692), 0.762, 90, 90)
                Line((-2.54, 4.7670174842), (-2.54, 6.5384505692))
                CenterArc((-1.778, 4.7670174842), 0.762, 180, 90)
                Line((1.778, 4.0050174842), (-1.778, 4.0050174842))
                CenterArc((1.778, 4.7670174842), 0.762, -90, 90)
                Line((2.54, 6.5384505692), (2.54, 4.7670174842))
                CenterArc((1.778, 6.5384505692), 0.762, 0, 90)
                Line((-1.778, 7.3004505692), (1.778, 7.3004505692))
            make_face()
        # OneSide extrude, distance=0.0127
        extrude(amount=0.0127)
    return part.part


# Description: This is a parallelogram-shaped flat plate or shim with a trapezoidal profile, featuring a diagonal internal line that suggests it may be divided into two triangular sections or indicates a fold/bend feature.
def model_31462_84375249_0003():
    """Model: Grill v3"""
    with BuildPart() as part:
        # Sketch5 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 560, perimeter: 108
            with BuildLine():
                Line((20, -7), (20, 7))
                Line((20, 7), (-20, 7))
                Line((-20, 7), (-20, -7))
                Line((-20, -7), (20, -7))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a cylindrical container or sleeve with a flat bottom and an angled or offset circular top surface, featuring a smooth curved sidewall and a recessed upper opening.
def model_31462_84375249_0009():
    """Model: legs v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            Circle(2.5)
        # OneSide extrude, distance=3
        extrude(amount=3)
    return part.part


# Description: This is a dodecahedron-shaped housing or bracket with a pentagonal geometric form featuring a large cylindrical hole through its center and triangular apertures on its faces.
def model_31627_68422558_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.7174152535, perimeter: 9.0305653993
            with BuildLine():
                Line((0.85, -0.4907477288), (0.85, 0.4907477288))
                Line((0.85, 0.4907477288), (0, 0.9814954576))
                Line((0, 0.9814954576), (-0.85, 0.4907477288))
                Line((-0.85, 0.4907477288), (-0.85, -0.4907477288))
                Line((-0.85, -0.4907477288), (0, -0.9814954576))
                Line((0, -0.9814954576), (0.85, -0.4907477288))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)
    return part.part


# Description: This is a pentagonal or irregular polyhedral 3D solid featuring a pyramidal top section (shown in lighter blue) and a larger geometric base body (shown in darker blue), with angular faceted surfaces throughout and no prominent holes or slots.
def model_31627_92333106_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.374901931, perimeter: 4.3647680351
            with BuildLine():
                Line((0.6314136634, -0.3612710695), (0.6285767556, 0.366184738))
                Line((0.6285767556, 0.366184738), (-0.0028369078, 0.7274558076))
                Line((-0.0028369078, 0.7274558076), (-0.6314136634, 0.3612710695))
                Line((-0.6314136634, 0.3612710695), (-0.6285767556, -0.366184738))
                Line((-0.6285767556, -0.366184738), (0.0028369078, -0.7274558076))
                Line((0.0028369078, -0.7274558076), (0.6314136634, -0.3612710695))
            make_face()
        # OneSide extrude, distance=-0.51
        extrude(amount=-0.51)
    return part.part


# Description: This is a cubic or dodecahedral housing with a large central cylindrical void featuring pyramidal protrusions on top and geometric cutouts/openings on its sides, designed as a structural frame or mounting component with internal cavity access.
def model_31627_e8252310_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.583282065, perimeter: 5.3490572073
            with BuildLine():
                Line((0.5, -0.2886751346), (0.5, 0.2886751346))
                Line((0.5, 0.2886751346), (0, 0.5773502692))
                Line((0, 0.5773502692), (-0.5, 0.2886751346))
                Line((-0.5, 0.2886751346), (-0.5, -0.2886751346))
                Line((-0.5, -0.2886751346), (0, -0.5773502692))
                Line((0, -0.5773502692), (0.5, -0.2886751346))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5)
    return part.part


# Description: This is a hexagonal or dodecahedral geometric solid with a large cylindrical bore through its center and triangular faceted surfaces forming a complex polyhedral structure with internal void geometry.
def model_31627_ec4c9f84_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.859602196, perimeter: 6.9094580845
            with BuildLine():
                Line((0.63, -0.3637306696), (0.63, 0.3637306696))
                Line((0.63, 0.3637306696), (0, 0.7274613392))
                Line((0, 0.7274613392), (-0.63, 0.3637306696))
                Line((-0.63, 0.3637306696), (-0.63, -0.3637306696))
                Line((-0.63, -0.3637306696), (0, -0.7274613392))
                Line((0, -0.7274613392), (0.63, -0.3637306696))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.405, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.65
        extrude(amount=-0.65)
    return part.part


# Description: This is a curved brake pad or friction material component with a concave crescent shape, featuring a textured surface and designed to wrap around a cylindrical form, commonly used in automotive or industrial braking systems.
def model_31748_5c7af877_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> 押し出し1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 16.5722596811, perimeter: 21.8853215912
            with BuildLine():
                CenterArc((0, 16.5368261331), 3.1, -19.5677063587, 61.5718208852)
                Line((1.9769293828, 18.6988275706), (2.303599993, 18.6112964444))
                Line((1.439715396, 16.6939176773), (1.9769293828, 18.6988275706))
                CenterArc((0.5176380902, 18.4686777857), 2, -147.4541502044, 84.9083004088)
                Line((-1.168284335, 17.3927290991), (-0.6310703482, 19.3976389924))
                Line((-0.9577409585, 19.4851701186), (-0.6310703482, 19.3976389924))
                CenterArc((0, 16.5368261331), 3.1, 107.9958854736, 61.5718208852)
                CenterArc((0.4141104722, 18.0823074552), 3.6, -164.1347437454, 118.2694874908)
            make_face()
        # OneSide extrude, distance=0.65
        extrude(amount=0.65)

        # Sketch1 -> 押し出し2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 20.8013421114, perimeter: 24.7282672272
            with BuildLine():
                CenterArc((-0.4658742812, -1.7386664873), 4, 14.03977488, 121.92045024)
                CenterArc((0, 0), 3.5, 162.6802514048, 61.3170294613)
                Line((-2.5178046828, -2.4311848098), (-2.2253458747, -2.5095489112))
                Line((-2.2253458747, -2.5095489112), (-1.6017608053, -0.1822977491))
                CenterArc((-0.5694018992, -2.1250368178), 2.2, 32.0141139198, 85.9717721604)
                Line((0.6724316041, -3.2860060465), (1.2960166736, -0.9587548844))
                Line((0.6724316041, -3.2860060465), (0.9648904122, -3.364370148))
                CenterArc((0, 0), 3.5, -73.9972808661, 61.3170294613)
            make_face()
        # OneSide extrude, distance=0.65
        extrude(amount=0.65)
    return part.part


# Description: This is a pulley or drive wheel featuring a circular ring with a grooved or ribbed outer surface for belt traction, a centered hub, and a hollow interior opening.
def model_31831_12689eab_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.3561944902, perimeter: 21.2617616649
            with BuildLine():
                CenterArc((-7.5, 0), 1.8027756377, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-7.5, 0), 1.5811388301, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.3062638932, perimeter: 1.9617914229
            with Locations((-7.5, 0)):
                Circle(0.3122288023)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a toroidal (doughnut-shaped) ring or torus with a smooth, rounded cross-section and a large central circular opening, featuring a textured or ribbed surface finish.
def model_31962_e5291336_0004():
    """Model: Component9"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 10.7756628018, perimeter: 30.7876080052
            with BuildLine():
                CenterArc((19.0644690181, 1.4890159362), 2.8, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((19.0644690181, 1.4890159362), 2.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a circular brake rotor or disc with an oval overall shape, featuring a central mounting hole, ventilation slots radiating outward, and curved braking surfaces with a mesh-textured finish.
def model_31962_e5291336_0024():
    """Model: DIN rotator"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.1056395521, perimeter: 10.6311495397
            with BuildLine():
                CenterArc((4.900000073, 1.1000000164), 0.95, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((4.900000073, 1.1000000164), 0.742, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.5279886277, perimeter: 5.0768137282
            with BuildLine():
                CenterArc((4.900000073, 1.1000000164), 0.508, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((4.900000073, 1.1000000164), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)
    return part.part


# Description: This is a wedge-shaped or truncated rectangular prism with a sloped top surface, featuring a solid body with angular facets and no holes or slots—essentially a flat-based box that tapers to a pointed or chamfered ridge along its top edge.
def model_32049_632b3378_0002():
    """Model: AE_P002 v5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.6774, perimeter: 12.7
            with BuildLine():
                Line((1.905, -1.27), (1.905, 1.27))
                Line((1.905, 1.27), (-1.905, 1.27))
                Line((-1.905, 1.27), (-1.905, -1.27))
                Line((-1.905, -1.27), (1.905, -1.27))
            make_face()
        # Symmetric extrude, each_side=0.53975
        extrude(amount=0.53975, both=True)
    return part.part


# Description: This is a flat parallelogram-shaped plate or panel with a simple rectangular form, featuring clean edges and a slight 3D perspective that suggests it is a thin, flat component with beveled or chamfered edges.
def model_32155_86984ce9_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 100, perimeter: 40
            with BuildLine():
                Line((-3, 6), (-3, -4))
                Line((-3, -4), (7, -4))
                Line((7, -4), (7, 6))
                Line((7, 6), (-3, 6))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a flat, elongated rectangular base or platform with a sloped or beveled top surface that features multiple triangulated facets, resembling a low-profile tray or mounting base with a complex geometric upper face.
def model_32163_0baf5480_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 63.9838968159, perimeter: 33.1590273201
            with BuildLine():
                Line((0, 0), (8, 0))
                Line((0, -8), (0, 0))
                Line((8, -8), (0, -8))
                Line((8, 0), (8, -8))
            make_face()
            with BuildLine():
                Line((7.5265625202, -4), (7.4972972187, -4))
                Line((7.5265625202, -4.5502483586), (7.5265625202, -4))
                Line((7.4972972187, -4.5502483586), (7.5265625202, -4.5502483586))
                Line((7.4972972187, -4), (7.4972972187, -4.5502483586))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


# Description: This is a cylindrical mesh or perforated sleeve with a wide, open-ended tubular shape featuring vertical ridges or corrugations along its surface and a continuous slot or opening running lengthwise down one side.
def model_32220_1fd19c5e_0014():
    """Model: 1 KOLO v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.0498887936, perimeter: 27.3318562828
            with BuildLine():
                CenterArc((0, 0), 2.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.1000000313, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


# Description: This is a rubber or elastomer drive belt with an elongated oval/elliptical toroidal shape, featuring a textured outer surface with a continuous ribbed or grooved pattern around its circumference for enhanced grip and power transmission.
def model_32220_1fd19c5e_0021():
    """Model: Zewnetrzne srebrne v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.157521601, perimeter: 30.7876080052
            with BuildLine():
                CenterArc((0, 0), 2.65, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)
    return part.part


# Description: A compact folding knife featuring a dark handle with textured grip and a curved blade that folds into the handle for safe, portable storage.
def model_32551_6c2e4a8d_0000():
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
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 15.5405198179, perimeter: 26.4821837992
            with BuildLine():
                _nurbs_edge([(0.9531825458, 0.215941312), (0.936346316, 0.2177963434), (0.8917461328, 0.2169136726), (0.8298306039, 0.1854119441), (0.7730033618, 0.0614454819), (0.7513109527, -0.2482067445), (0.7748172225, -0.7511084597), (0.8231395881, -1.375169971), (0.8741888685, -2.0724063681), (0.9134683963, -2.8031510405), (0.9328309198, -3.5354131254), (0.9293088908, -4.2443670964), (0.9039175999, -4.911796111), (0.8604760283, -5.5255558857), (0.8044122226, -6.0790384205), (0.7415981506, -6.5706255339), (0.6771214995, -7.0031796836), (0.6142029084, -7.3834502069), (0.5527610599, -7.7216904218), (0.4891363663, -8.0305887226), (0.4176526812, -8.3231583521), (0.3317861441, -8.6107892593), (0.225416664, -8.9014057998), (0.094223013, -9.1971686597), (-0.0635612243, -9.4936921342), (-0.2480988981, -9.7831413063), (-0.4164749202, -10.0018932233), (-0.5539526679, -10.1554288223), (-0.6505013947, -10.252663333), (-0.700000003, -10.299999997)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.7953309003, 0.7953309003, 0.7953309003, 0.7953309003, 0.7953309003, 0.7953309003, 0.8, 0.8083333333, 0.8166666667, 0.825, 0.8333333333, 0.8416666667, 0.85, 0.8583333333, 0.8666666667, 0.875, 0.8833333333, 0.8916666667, 0.9, 0.9083333333, 0.9166666667, 0.925, 0.9333333333, 0.9416666667, 0.95, 0.9583333333, 0.9666666667, 0.975, 0.9833333333, 0.9916666667, 1, 1, 1, 1, 1, 1], 5)
                Line((-0.9321874803, 0.5382776423), (0.9531825458, 0.215941312))
                _nurbs_edge([(-1.7799918518, -11.3328211826), (-1.7586847991, -11.2761985619), (-1.7161853139, -11.1589880677), (-1.6527799408, -10.9712765297), (-1.5689272776, -10.6972005288), (-1.4653155034, -10.3153403275), (-1.3630808872, -9.895422336), (-1.2625675865, -9.4398711153), (-1.1643520339, -8.9527696013), (-1.0692914214, -8.4402093018), (-0.9786030367, -7.9108610822), (-0.8938471613, -7.375856699), (-0.8166921778, -6.8471156459), (-0.7487259849, -6.3360005754), (-0.691244491, -5.8518141994), (-0.6450599632, -5.4004260579), (-0.61027699, -4.9826958632), (-0.5861373104, -4.5933236956), (-0.5706975909, -4.2186666303), (-0.561136585, -3.8384481511), (-0.5546257006, -3.4309617725), (-0.5490516191, -2.9773418661), (-0.5437805583, -2.4661302295), (-0.5404495011, -1.8979196185), (-0.5436439245, -1.2895022467), (-0.5618723308, -0.6793582518), (-0.6076625639, -0.1291661142), (-0.6855963656, 0.2581409463), (-0.7766196672, 0.4463917636), (-0.8575279676, 0.5159901417), (-0.9119772109, 0.5345921712), (-0.9321874803, 0.5382776423)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0083333333, 0.0166666667, 0.025, 0.0333333333, 0.0416666667, 0.05, 0.0583333333, 0.0666666667, 0.075, 0.0833333333, 0.0916666667, 0.1, 0.1083333333, 0.1166666667, 0.125, 0.1333333333, 0.1416666667, 0.15, 0.1583333333, 0.1666666667, 0.175, 0.1833333333, 0.1916666667, 0.2, 0.2083333333, 0.2166666667, 0.2213492574, 0.2213492574, 0.2213492574, 0.2213492574, 0.2213492574, 0.2213492574], 5)
                Line((-0.700000003, -10.299999997), (-1.7799918518, -11.3328211826))
            make_face()
        # Symmetric extrude, each_side=0.15
        extrude(amount=0.15, both=True)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.5760410999, perimeter: 21.9722753982
            with BuildLine():
                _nurbs_edge([(-0.9321874803, 0.5382776423), (-0.9479442476, 0.5411509891), (-1.0009085154, 0.544583676), (-1.0972487302, 0.5176848948), (-1.2452862422, 0.4093451584), (-1.4399255704, 0.1963366136), (-1.6219378212, -0.0056488792), (-1.7273669627, -0.049856602), (-1.731744127, 0.1188490873), (-1.6378837428, 0.4408527928), (-1.4672495692, 0.7972258292), (-1.2520667433, 1.0641033702), (-1.0275277348, 1.160593357), (-0.823016995, 1.116519135), (-0.6590568277, 1.0405385837), (-0.547108123, 1.0507738561), (-0.4878886841, 1.2057575257), (-0.4735924718, 1.5034970284), (-0.4912832366, 1.9099502679), (-0.525823751, 2.3766736808), (-0.5632267007, 2.8652734254), (-0.5917699077, 3.3486429242), (-0.6027148285, 3.8088218477), (-0.5911724791, 4.2359691889), (-0.5568850164, 4.6268727686), (-0.5051018507, 4.9836677775), (-0.4472849675, 5.3124525041), (-0.4022520405, 5.6219933249), (-0.3894830449, 5.9214613004), (-0.4218282975, 6.218093987), (-0.4985768236, 6.5149178286), (-0.5980310705, 6.8083637149), (-0.6712385589, 7.0861506132), (-0.6618029953, 7.3311923942), (-0.5243762896, 7.5252260623), (-0.2441910365, 7.6526123458), (0.1453466069, 7.7038745367), (0.5813318448, 7.674917329), (0.9880189066, 7.5664308912), (1.2950192972, 7.3832382398), (1.4530388272, 7.1336452922), (1.4552367784, 6.8288509317), (1.3335922737, 6.4820379931), (1.1416556852, 6.1072823689), (0.9415992697, 5.7185237089), (0.789317428, 5.3285007514), (0.7207714068, 4.9477246859), (0.7366876003, 4.5833721692), (0.8128309302, 4.2396647699), (0.9114215082, 3.9183277175), (0.9926389284, 3.6190283742), (1.0249369352, 3.3398001195), (0.9987348486, 3.0775280586), (0.926149418, 2.8281219058), (0.8296124132, 2.5862692418), (0.734438348, 2.3455861073), (0.6581128258, 2.0979636673), (0.6069514271, 1.8356650875), (0.5822827868, 1.558153281), (0.5840204097, 1.2765683674), (0.615999094, 1.0217890485), (0.6884778127, 0.8434887326), (0.8092635731, 0.7738505011), (0.9756009682, 0.7890699792), (1.1674618376, 0.788545588), (1.3541971823, 0.6726335194), (1.4990529054, 0.4243495525), (1.5661553579, 0.1463739202), (1.5329833833, -0.0353079879), (1.4009416447, -0.0381050923), (1.2304612314, 0.0748896887), (1.0960369179, 0.1672031414), (1.0113118738, 0.2053389409), (0.9663953453, 0.2144855134), (0.9531825458, 0.215941312)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.2213492574, 0.2213492574, 0.2213492574, 0.2213492574, 0.2213492574, 0.2213492574, 0.225, 0.2333333333, 0.2416666667, 0.25, 0.2583333333, 0.2666666667, 0.275, 0.2833333333, 0.2916666667, 0.3, 0.3083333333, 0.3166666667, 0.325, 0.3333333333, 0.3416666667, 0.35, 0.3583333333, 0.3666666667, 0.375, 0.3833333333, 0.3916666667, 0.4, 0.4083333333, 0.4166666667, 0.425, 0.4333333333, 0.4416666667, 0.45, 0.4583333333, 0.4666666667, 0.475, 0.4833333333, 0.4916666667, 0.5, 0.5083333333, 0.5166666667, 0.525, 0.5333333333, 0.5416666667, 0.55, 0.5583333333, 0.5666666667, 0.575, 0.5833333333, 0.5916666667, 0.6, 0.6083333333, 0.6166666667, 0.625, 0.6333333333, 0.6416666667, 0.65, 0.6583333333, 0.6666666667, 0.675, 0.6833333333, 0.6916666667, 0.7, 0.7083333333, 0.7166666667, 0.725, 0.7333333333, 0.7416666667, 0.75, 0.7583333333, 0.7666666667, 0.775, 0.7833333333, 0.7916666667, 0.7953309003, 0.7953309003, 0.7953309003, 0.7953309003, 0.7953309003, 0.7953309003], 5)
                Line((-0.9321874803, 0.5382776423), (0.9531825458, 0.215941312))
            make_face()
        # Symmetric extrude, each_side=0.5
        extrude(amount=0.5, both=True, mode=Mode.ADD)
    return part.part


# Description: This is a microphone featuring a spherical mesh head at the top, a cylindrical handle with vertical ribbing in the middle section, and a tapered base at the bottom.
def model_32743_f4c47bbc_0008():
    """Model: 43-ECCENTRIC ROD AND STRAP"""
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
        # Sketch has 14 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 1.8372340634, perimeter: 9.2418187134
            with BuildLine():
                CenterArc((0, 0), 0.25, -36.8698976458, 73.7397952917)
                Line((4.3514718626, -0.3), (0.2, -0.15))
                CenterArc((5.2, 0), 0.9, 160.5287793655, 38.942441269)
                Line((0.2, 0.15), (4.3514718626, 0.3))
            make_face()
            # Profile area: 0.0706858347, perimeter: 2.8274333882
            with BuildLine():
                CenterArc((0, 0), 0.25, 36.8698976458, 286.2602047083)
                CenterArc((0, 0), 0.25, -36.8698976458, 73.7397952917)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.5340707511, perimeter: 10.6814150222
            with BuildLine():
                CenterArc((5.2, 0), 0.9, -160.5287793655, 321.057558731)
                CenterArc((5.2, 0), 0.9, 160.5287793655, 38.942441269)
            make_face()
            with BuildLine():
                CenterArc((5.2, 0), 0.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0549778714, perimeter: 2.1991148575
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
            # Profile area: 0.471238898, perimeter: 9.4247779608
            with BuildLine():
                CenterArc((5.2, 0), 0.8, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((5.2, 0), 0.7, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.5393804003, perimeter: 4.398229715
            with Locations((5.2, 0)):
                Circle(0.7)
        # Symmetric extrude, each_side=0.2
        extrude(amount=0.2, both=True)
    return part.part


# Description: This is a wiper blade assembly consisting of a curved black rubber or polymer blade body with a blue-gray metal backing strip and a mounting bracket at the upper end for vehicle windshield attachment.
def model_32871_04ff3d41_0002():
    """Model: CT001"""
    with BuildPart() as part:
        # Sketch3 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 16 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 49.5622037162, perimeter: 42.0411291103
            with BuildLine():
                Line((-6.7999941256, -9.7999482773), (-5.3999941256, -9.7999482773))
                CenterArc((-5.3999941256, -8.9999482773), 0.8, -90, 90)
                Line((-4.5999941256, -8.9999482773), (-4.5999941256, -0.2000517227))
                CenterArc((-3.8, -0.2), 0.7999941273, 90, 90.0037043927)
                Line((-3.8, 0.5999941273), (-1.6, 0.5999941273))
                Line((-1.6, 0.5999941273), (-1.6, 0))
                Line((0, 0), (-1.6, 0))
                Line((0, 3.8000517227), (0, 0))
                Line((-6.2999941256, 3.8000517227), (0, 3.8000517227))
                CenterArc((-6.2999941256, 3.0000517227), 0.8, 90, 90)
                Line((-7.0999941256, -10.0999482773), (-7.0999941256, 3.0000517227))
                CenterArc((-6.7999941256, -10.0999482773), 0.3, 90, 90)
            make_face()
        # OneSide extrude, distance=0.9
        extrude(amount=0.9)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 16 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 47.9262865697, perimeter: 59.3249965952
            with BuildLine():
                CenterArc((-6.7999941256, -10.0999482773), 0.3, 90, 90)
                Line((-7.0999941256, -12.2702482773), (-7.0999941256, -10.0999482773))
                CenterArc((-6.1, -12.2702482773), 0.9999941256, 180, 20.3632280108)
                CenterArc((-1.6, -10.6), 5.7999659284, -159.6367719892, 120.9423292861)
                CenterArc((1.6, -13.1631738734), 1.6999829646, -38.6944427031, 179.9988408445)
                CenterArc((-1.6, -10.6), 2.4, 180, 141.3063777524)
                Line((-4, -0.2), (-4, -10.6))
                CenterArc((-3.8, -0.2), 0.2, 90, 90)
                Line((-1.6, 0), (-3.8, 0))
                Line((-1.6, 0.5999941273), (-1.6, 0))
                Line((-3.8, 0.5999941273), (-1.6, 0.5999941273))
                CenterArc((-3.8, -0.2), 0.7999941273, 90, 90.0037043927)
                Line((-4.5999941256, -8.9999482773), (-4.5999941256, -0.2000517227))
                CenterArc((-5.3999941256, -8.9999482773), 0.8, -90, 90)
                Line((-6.7999941256, -9.7999482773), (-5.3999941256, -9.7999482773))
            make_face()
            with BuildLine():
                CenterArc((-4.0042, -13.0042), 0.35, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.8042, -13.0042), 0.35, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.6
        extrude(amount=1.6, mode=Mode.ADD)
    return part.part


# Description: This is a coffin-shaped box or enclosure with a tapered, elongated rectangular body featuring angled side panels, internal structural ribbing or bracing, and ventilation slots or mesh openings along the sides.
def model_32871_04ff3d41_0015():
    """Model: CT006 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.0746903509, perimeter: 17.8265482457
            with BuildLine():
                Line((3.4, -3.6), (0.6, -3.6))
                Line((3.4, 0), (3.4, -3.6))
                Line((3.4, 0), (0.6, 0))
                Line((0.6, 0), (0.6, -3.6))
            make_face()
            with BuildLine():
                CenterArc((2.4, -2.7), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.4, -0.9), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.16, perimeter: 8.4
            with BuildLine():
                Line((0.6, -3.6), (0, -3.6))
                Line((0.6, 0), (0.6, -3.6))
                Line((0, 0), (0.6, 0))
                Line((0, -3.6), (0, 0))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


# Description: This is a truncated octahedron or rounded polyhedron housing with multiple angular faceted surfaces, featuring rectangular openings or slots across its sides and a complex geometric structure with both convex and concave surfaces.
def model_32879_49552f2f_0011():
    """Model: Pieza 12"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.5302947995, perimeter: 7.0358085532
            with BuildLine():
                CenterArc((0, 0), 0.6, 90, 180)
                Line((0, 1.2701705922), (0, 0.6))
                Line((0, 1.2701705922), (-1.1, 0.6350852961))
                Line((-1.1, 0.6350852961), (-1.1, -0.6350852961))
                Line((-1.1, -0.6350852961), (0, -1.2701705922))
                Line((0, -0.6), (0, -1.2701705922))
            make_face()
            # Profile area: 1.5302947995, perimeter: 7.0358085532
            with BuildLine():
                CenterArc((0, 0), 0.6, -90, 180)
                Line((0, -0.6), (0, -1.2701705922))
                Line((0, -1.2701705922), (1.1, -0.6350852961))
                Line((1.1, -0.6350852961), (1.1, 0.6350852961))
                Line((1.1, 0.6350852961), (0, 1.2701705922))
                Line((0, 1.2701705922), (0, 0.6))
            make_face()
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)
    return part.part


# Description: This is a circular disc or plate with a slightly curved or dished surface, featuring a textured or knurled edge around its circumference.
def model_33147_d7173b68_0006():
    """Model: Component33"""
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
            # Profile area: 7.4264305088, perimeter: 9.6603974098
            with BuildLine():
                CenterArc((0, 0), 1.5375, -2.0767736338, 4.1535472676)
                CenterArc((0, 0), 1.5375, 2.0767736338, 355.8464527324)
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0090322913, perimeter: 0.389405981
            with BuildLine():
                _nurbs_edge([(1.536490118, -0.0557168496), (1.5414944405, -0.0548247562), (1.55200185, -0.052745821), (1.5679405405, -0.0488547393), (1.5843620611, -0.044195778), (1.6007827749, -0.0389245486), (1.617191755, -0.0330749591), (1.6335991457, -0.0267133033), (1.6444365159, -0.0220739142), (1.649882121, -0.0197426954)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.0343644345, 0.0343644345, 0.0343644345, 0.0343644345, 0.0496077279, 0.0664986025, 0.0835653922, 0.1008079962, 0.1182263556, 0.135820431, 0.1535901936, 0.1535901936, 0.1535901936, 0.1535901936], 3)
                CenterArc((-0.0033388269, 0), 1.6533388269, -0.6841912796, 1.3683825592)
                _nurbs_edge([(1.536490118, 0.0557168496), (1.5414944405, 0.0548247562), (1.55200185, 0.052745821), (1.5679405405, 0.0488547393), (1.5843620611, 0.044195778), (1.6007827749, 0.0389245486), (1.617191755, 0.0330749591), (1.6335991457, 0.0267133033), (1.6444365159, 0.0220739142), (1.649882121, 0.0197426954)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.0343644345, 0.0343644345, 0.0343644345, 0.0343644345, 0.0496077279, 0.0664986025, 0.0835653922, 0.1008079962, 0.1182263556, 0.135820431, 0.1535901936, 0.1535901936, 0.1535901936, 0.1535901936], 3)
                CenterArc((0, 0), 1.5375, -2.0767736338, 4.1535472676)
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical knob or dial with a circular body, a small protruding shaft or pin on one side, and a textured mesh or knurled section on the upper portion for grip.
def model_33147_d7173b68_0012():
    """Model: Component12"""
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
            # Profile area: 1.0843403393, perimeter: 3.691371368
            with BuildLine():
                CenterArc((0, 0), 0.5875, 4.303307559, 351.3933848821)
                CenterArc((0, 0), 0.5875, -4.303307559, 8.6066151179)
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0084697552, perimeter: 0.3624106808
            with BuildLine():
                Line((0.5858437221, 0.0440838215), (0.6090684735, 0.0458314477))
                CenterArc((0, 0), 0.5875, -4.303307559, 8.6066151179)
                Line((0.5858437221, -0.0440838215), (0.6090684735, -0.0458314477))
                _nurbs_edge([(0.6090684735, -0.0458314477), (0.6123987734, -0.0457577433), (0.6191148133, -0.0456091077), (0.6291550264, -0.04399478), (0.639237705, -0.0418490708), (0.6493421353, -0.0390898461), (0.659457758, -0.0358224126), (0.6695752504, -0.0320727108), (0.6796815079, -0.0278634967), (0.6897829651, -0.0232427586), (0.6964226876, -0.0198488922), (0.6997661331, -0.0181399041)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0099822114, 0.0201305988, 0.0304392233, 0.0409074261, 0.0515349435, 0.0623216232, 0.0732673589, 0.084372068, 0.0956356818, 0.0956356818, 0.0956356818, 0.0956356818], 3)
                CenterArc((-0.0036285663, 0), 0.7036285663, -1.4772781512, 2.9545563024)
                _nurbs_edge([(0.6090684735, 0.0458314477), (0.6123987734, 0.0457577433), (0.6191148133, 0.0456091077), (0.6291550264, 0.04399478), (0.639237705, 0.0418490708), (0.6493421353, 0.0390898461), (0.659457758, 0.0358224126), (0.6695752504, 0.0320727108), (0.6796815079, 0.0278634967), (0.6897829651, 0.0232427586), (0.6964226876, 0.0198488922), (0.6997661331, 0.0181399041)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0099822114, 0.0201305988, 0.0304392233, 0.0409074261, 0.0515349435, 0.0623216232, 0.0732673589, 0.084372068, 0.0956356818, 0.0956356818, 0.0956356818, 0.0956356818], 3)
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)
    return part.part


# Description: This is an elongated rectangular tray or pan with a tapered wedge shape, featuring a recessed top surface with parallel slots or ribs, dark side walls, and a small rectangular opening or handle feature at the upper left end.
def model_33165_cec42ec5_0000():
    """Model: table"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 11 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0399999774, perimeter: 0.9656851515
            with BuildLine():
                Line((-4, 7.6000001132), (-4, 8))
                Line((-3.8000000566, 7.8000001162), (-4, 7.6000001132))
                Line((-4, 8), (-3.8000000566, 7.8000001162))
            make_face()
            # Profile area: 143.5307963494, perimeter: 49.3072780316
            with BuildLine():
                Line((-4, 8), (-3.8000000566, 7.8000001162))
                Line((-3.8000000566, 7.8000001162), (-4, 7.6000001132))
                Line((-4, -8), (-4, 7.6000001132))
                Line((4, -8), (-4, -8))
                CenterArc((4, -7), 1, -90, 90)
                Line((5, 7), (5, -7))
                CenterArc((4, 7), 1, 0, 90)
                Line((-4, 8), (4, 8))
            make_face()
        # OneSide extrude, distance=-1.2
        extrude(amount=-1.2)

        # Sketch1 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 11 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0399999774, perimeter: 0.9656851515
            with BuildLine():
                Line((-4, 7.6000001132), (-4, 8))
                Line((-3.8000000566, 7.8000001162), (-4, 7.6000001132))
                Line((-4, 8), (-3.8000000566, 7.8000001162))
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical rod or tube with a slightly tapered, rounded end at the top and a flat or blunt end at the bottom, featuring a uniform dark gray finish with subtle shading that emphasizes its three-dimensional cylindrical geometry.
def model_33607_c6f31fa6_0004():
    """Model: Shaft-Inventor"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.067074791, perimeter: 7.9796453401
            Circle(1.27)
        # OneSide extrude, distance=30.48
        extrude(amount=30.48)
    return part.part


# Description: This is a long, slender rectangular prism or bar stock with a parallelogram cross-section, featuring tapered or beveled edges along its length and a slight twist, commonly used as a structural support or reinforcement component.
def model_33628_296ae2b8_0001():
    """Model: Component1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2000000045, perimeter: 2.4000000447
            with BuildLine():
                Line((2, -1.8), (3.0000000447, -1.8))
                Line((2, -2), (2, -1.8))
                Line((3, -2), (2, -2))
                Line((3.0000000447, -1.8), (3, -2))
            make_face()
        # OneSide extrude, distance=4.6
        extrude(amount=4.6)
    return part.part


# Description: This is a cam follower or lever arm with an elongated teardrop shape, featuring a circular hole at one end and a tapered, curved body that extends to a pointed or rounded terminus, with internal ribbed reinforcement visible along its length.
def model_34063_0ca1585e_0009():
    """Model: Blade Grip"""
    with BuildPart() as part:
        # Sketch1 -> Extrude12 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 10 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.0467265996, perimeter: 8.7029406619
            with BuildLine():
                CenterArc((0, 0.0000001657), 0.7999999755, 107.4923270373, 145.0153494932)
                CenterArc((-2.6, 8.2499989039), 7.8499988211, -90, 17.4923270373)
                CenterArc((-2.6, 0.0000000829), 0.4, 90, 180)
                CenterArc((-2.6, -8.2499987382), 7.8499988211, 72.5076729627, 17.4923270373)
            make_face()
            with BuildLine():
                CenterArc((-2.6, 0.0000000829), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.2252210117, perimeter: 8.1681407453
            with BuildLine():
                CenterArc((0, 0.0000001657), 0.7999999755, 107.4923270373, 145.0153494932)
                CenterArc((0, 0.0000001657), 0.7999999755, -107.4923234695, 214.9846505068)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((-2.6, 0.0000000829)):
                Circle(0.1)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)
    return part.part


# Description: This is a dark metal bracket or arm with a bent, angular shape featuring two flat rectangular end plates connected by a curved or twisted central section, with visible geometric mesh lines indicating a 3D surface structure.
def model_34180_21cf3c28_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch16 -> Extrude4 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.2437215117, perimeter: 39.7945875473
            with BuildLine():
                Line((-19.6043322495, 9.000000149), (-20, 9))
                Line((-20, 9), (-20, 6.5))
                Line((-20, 6.5), (-22.5, 4))
                Line((-22.5, 4), (-22.5, -3.5))
                Line((-22.5, -3.5), (-20.1, -5.9))
                Line((-20.1, -5.9), (-20.1, -8.5))
                Line((-20.1, -8.5), (-19.800000295, -8.5))
                Line((-19.800000295, -8.5), (-19.800000295, -5.8000001475))
                Line((-19.800000295, -5.8000001475), (-22.2000003308, -3.4000001118))
                Line((-22.2000003308, -3.4000001118), (-22.2000003308, 3.8000000715))
                Line((-22.2000003308, 3.8000000715), (-19.6043322495, 6.3956681528))
                Line((-19.6043322495, 6.3956681528), (-19.6043322495, 9.000000149))
            make_face()
        # OneSide extrude, distance=4
        extrude(amount=4)
    return part.part


# Description: This is a cylindrical bolt or fastener with a hexagonal head at one end and a threaded shaft extending diagonally across the image.
def model_34226_dbed877f_0006():
    """Model: pindozawiasu v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 2.5132741229
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2)
    return part.part


# Description: This is a cylindrical suppressor or silencer with a elongated tubular body, featuring a slightly tapered rounded end cap and textured surface markings along its length.
def model_34234_04351713_0003():
    """Model: Peg"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=-3
        extrude(amount=-3)
    return part.part


# Description: This is a dark blue composite or reinforced polymer structural beam or duct with an elongated hexagonal cross-section, featuring a tapered profile that narrows toward one end and internal ribbing or reinforcement structures visible through its translucent sections.
def model_34343_6d3253e1_0015():
    """Model: Longboard Press .65" Lower v5 (1)"""
    with BuildPart() as part:
        # Sketch2 -> Extrude4 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 104.6366188797, perimeter: 65.5945143995
            with BuildLine():
                Line((0, 0), (-2.159, 0))
                Line((0, 30.48), (0, 0))
                Line((0, 30.48), (-2.159, 30.48))
                CenterArc((57.8485, 15.24), 61.9125, 165.7499673022, 28.5000653956)
            make_face()
        # OneSide extrude, distance=3.81
        extrude(amount=3.81)
    return part.part


# Description: This is a long, tapered hollow tube or duct with a polygonal cross-section, featuring a narrow pointed end that gradually widens toward the opposite end, with a textured or mesh-like surface pattern along its length.
def model_34343_6d3253e1_0019():
    """Model: Longboard Press .60" Lower v2"""
    with BuildPart() as part:
        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 108.5075788797, perimeter: 65.8485143995
            with BuildLine():
                Line((0, 0), (-2.286, 0))
                Line((0, 30.48), (0, 0))
                Line((-2.286, 30.48), (0, 30.48))
                CenterArc((57.7215, 15.24), 61.9125, 165.7499673022, 28.5000653956)
            make_face()
        # OneSide extrude, distance=3.81
        extrude(amount=3.81)
    return part.part


# Description: This is a long, narrow rectangular duct or channel with a tapered hexagonal cross-section, featuring internal ribbed reinforcement structures and a sloped top surface, designed for structural rigidity and efficient material use.
def model_34343_6d3253e1_0027():
    """Model: Longboard Press .70” Upper v6"""
    with BuildPart() as part:
        # Sketch2 -> Extrude3 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 171.4661209161, perimeter: 75.2899697103
            with BuildLine():
                Line((-8.89, 30.48), (-1.905, 30.48))
                Line((-8.89, 0), (-8.89, 30.48))
                Line((-1.905, 0), (-8.89, 0))
                CenterArc((54.229, 15.24), 58.166, 164.8107132628, 30.3785734744)
            make_face()
        # OneSide extrude, distance=3.81
        extrude(amount=3.81)
    return part.part


# Description: This is a long, tapered structural beam or duct with a hexagonal cross-section that narrows toward one end, featuring triangulated internal bracing and reinforcement ribs along its length.
def model_34343_6d3253e1_0028():
    """Model: Longboard Press .60" Upper v2 (1)"""
    with BuildPart() as part:
        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 162.4596211203, perimeter: 74.4845143995
            with BuildLine():
                Line((-8.89, 30.48), (-2.286, 30.48))
                Line((-8.89, 0), (-8.89, 30.48))
                Line((-2.286, 0), (-8.89, 0))
                CenterArc((57.7215, 15.24), 61.9125, 165.7499673022, 28.5000653956)
            make_face()
        # OneSide extrude, distance=3.81
        extrude(amount=3.81)
    return part.part


# Description: This is a hexagonal or octagonal block with a large cylindrical hole running through its center and a rectangular slot or opening cut through one side, creating a complex geometric part with both subtractive features.
def model_34436_ffc43a58_0000():
    """Model: tuerca"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.4011523849), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0394784314, perimeter: 1.7344650184
            with BuildLine():
                Line((0.8366025488, 1.6500000048), (0.663397468, 1.6500000145))
                Line((0.663397468, 1.6500000145), (0.5767949192, 1.5000000194))
                Line((0.5767949192, 1.5000000194), (0.6633974512, 1.3500000145))
                Line((0.6633974512, 1.3500000145), (0.836602532, 1.3500000048))
                Line((0.836602532, 1.3500000048), (0.9232050808, 1.5))
                Line((0.9232050808, 1.5), (0.8366025488, 1.6500000048))
            make_face()
            with BuildLine():
                CenterArc((0.75, 1.5000000097), 0.1106500127, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0144110362, perimeter: 1.2450132482
            with BuildLine():
                CenterArc((0.75, 1.5000000097), 0.1106500127, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0.75, 1.5000000097), 0.0875, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.18
        extrude(amount=0.18)
    return part.part


# Description: This is a rounded rectangular bar or spacer with a elongated cylindrical shape featuring semi-circular ends and a flat top surface, commonly used as a fastener, spacer, or connector in mechanical assemblies.
def model_34770_6bba5bd4_0003():
    """Model: Cylinder (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.5542113053, perimeter: 6.9821896726
            with BuildLine():
                CenterArc((0.6613728508, 7.6608003465), 0.635, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0.6613728508, 7.6608003465), 0.47625, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=8.89
        extrude(amount=8.89)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.6333843489, perimeter: 3.9898226701
            with BuildLine():
                CenterArc((0.6613728508, 7.6608003465), 0.47625, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0.6613728508, 7.6608003465), 0.15875, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3175
        extrude(amount=0.3175, mode=Mode.ADD)
    return part.part


# Description: This is a sculptural or decorative mounting bracket featuring a curved, loop-shaped upper section with an oval aperture, supported by an angular base with faceted geometric surfaces and a diagonal stripe pattern.
def model_34770_6bba5bd4_0008():
    """Model: Mounting bracket"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 16 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.016125, perimeter: 7.62
            with BuildLine():
                Line((-3.175, 0.635), (0, 0.635))
                Line((-3.175, 0), (-3.175, 0.635))
                Line((0, 0), (-3.175, 0))
                Line((0, 0.635), (0, 0))
            make_face()
        # Symmetric extrude, each_side=1.27
        extrude(amount=1.27, both=True)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 16 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4.7080084827, perimeter: 13.4221010076
            with BuildLine():
                Line((0, 0.635), (0, 1.27))
                CenterArc((-1.5875, 1.27), 1.5875, 0, 180)
                Line((-3.175, 1.27), (-3.175, 0.635))
                Line((-3.175, 0.635), (0, 0.635))
            make_face()
            with BuildLine():
                CenterArc((-1.5875, 2.16154), 0.635, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.3175
        extrude(amount=0.3175, both=True, mode=Mode.ADD)
    return part.part


# Description: This is a simple flat rectangular plate or bar with a clean, minimalist design featuring a horizontal linear form and uniform thickness throughout.
def model_34781_4f8a4759_0017():
    """Model: Cu4 v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            Circle(0.05)
        # OneSide extrude, distance=55.8
        extrude(amount=55.8)
    return part.part


# Description: This is a curved, elongated component with a streamlined, crescent-like shape featuring a textured upper surface and a smooth lower profile, resembling an aerodynamic guard or deflector with a gradual taper toward one end.
def model_34785_dc3b83fa_0011():
    """Model: Ramie v14"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 19 constraints, 13 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 6359.5276778821, perimeter: 639.6211975246
            with BuildLine():
                CenterArc((-177.9613507239, -115.8784411294), 150, 80.3758047465, 35.3430784767)
                Line((-243.0547556686, 19.2616662877), (-264.3395603296, 9.0093404945))
                CenterArc((-260, 0), 10, 115.7188832232, 172.3061556238)
                Line((-224.7796850443, 0.94467657), (-256.9056741363, -9.5092138187))
                CenterArc((-222.4589406466, -6.187233794), 7.5, 40.3663968462, 67.6586420007)
                Line((-216.7445534747, -1.3296851066), (-214.5715097375, -3.8860389499))
                CenterArc((-210, 0), 6, -139.6336031538, 67.5344095714)
                Line((-188.5507757482, 0.623008069), (-208.1557799333, -5.7095404671))
                CenterArc((-165.498024914, -70.7462477698), 75, 86.3994129487, 21.501393469)
                Line((-160.7879690176, 4.1057086071), (-0.3768044717, -5.9881565102))
                CenterArc((0, 0), 6, -93.6005870513, 173.9763917978)
                Line((-152.8835849765, 32.0103876073), (1.0031106299, 5.9155531495))
            make_face()
            with BuildLine():
                CenterArc((-210, 0), 3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0), 3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-260, 0), 3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=20
        extrude(amount=20)
    return part.part


# Description: This is a bent or folded sheet metal bracket with two rectangular flanges joined at an angle, featuring triangulated internal ribbing or bracing for structural reinforcement.
def model_35145_a3d7363c_0006():
    """Model: Connecting part 1"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 13 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.480000006, perimeter: 25.2
            with BuildLine():
                Line((2.2, -2.1), (2.2, 2.1))
                Line((2.2, 2.1), (-2.2, 2.1))
                Line((-2.2, 2.1), (-2.2, -2.1))
                Line((-2.2, -2.1), (-2, -2.1000000015))
                Line((-2, 1.8999999985), (-2, -2.1000000015))
                Line((2, 1.8999999985), (-2, 1.8999999985))
                Line((2, -2.1000000015), (2, 1.8999999985))
                Line((2, -2.1000000015), (2.2, -2.1))
            make_face()
        # Symmetric extrude, each_side=4.4
        extrude(amount=4.4, both=True)
    return part.part


# Description: This is a cylindrical sleeve or bushing with a hollow interior and a mesh or perforated section on the upper outer surface, featuring an overall drum-like shape with angled sides.
def model_35166_562b126c_0005():
    """Model: Button Extension Bushing"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.4909998734, perimeter: 7.0999993971
            with BuildLine():
                CenterArc((0, 0), 0.775, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.355, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.706
        extrude(amount=0.706)
    return part.part


# Description: This is a curved black arm or bracket with a gradual arc shape, featuring adjustable slot holes along its length and a circular mounting point or pad at one end, designed for articulated positioning or adjustment purposes.
def model_35941_9352b107_0000():
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
        # Sketch7 -> Extrude3 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 5.1664930055, perimeter: 23.072021472
            with BuildLine():
                CenterArc((5.813760897, 3.0817044813), 0.0270713029, -1.903164604, 77.1857819041)
                _nurbs_edge([(-1.1253528232, -0.6975776984), (-1.1145144473, -0.695954994), (-1.0886823773, -0.690852678), (-1.0463303038, -0.6780527409), (-0.9849407671, -0.6505719796), (-0.9015008149, -0.5998720721), (-0.8087424837, -0.5323539048), (-0.7134380709, -0.4562797114), (-0.6183477982, -0.3775790665), (-0.5264134369, -0.3013743529), (-0.440460645, -0.2308594984), (-0.362905396, -0.1657657229), (-0.2954902453, -0.1023235288), (-0.2390716119, -0.0362257832), (-0.1934175777, 0.0352933699), (-0.1569477477, 0.1105411126), (-0.1266549568, 0.1823012444), (-0.0986692778, 0.2432367276), (-0.0687172821, 0.2898429999), (-0.0326179999, 0.3279492573), (0.0131508129, 0.3684030159), (0.0708046318, 0.4206709553), (0.140761973, 0.4880078083), (0.2222301073, 0.5695120256), (0.3137013605, 0.6616303268), (0.4134484784, 0.7597666555), (0.5201001392, 0.8600759653), (0.6328984996, 0.9603618015), (0.7514543875, 1.0595169195), (0.8756207697, 1.1573112296), (1.0053222253, 1.2540452968), (1.1403956609, 1.3502524189), (1.2804441502, 1.4464037431), (1.4246386834, 1.5425525068), (1.5717930056, 1.6383294298), (1.7205598999, 1.7330971789), (1.8695894981, 1.826053953), (2.0177005521, 1.9163565738), (2.1640526583, 2.0032382457), (2.3083038157, 2.0861213587), (2.4508105321, 2.1647503869), (2.5926989147, 2.2392609416), (2.7355397284, 2.3100510695), (2.8810916987, 2.3776869916), (3.0310210802, 2.4427964973), (3.1866250022, 2.5059657632), (3.3485673604, 2.5676394279), (3.5165731512, 2.6280077898), (3.6892465857, 2.686933713), (3.8644159599, 2.7440490239), (4.0393995768, 2.7988255295), (4.2113039755, 2.8506564749), (4.377302282, 2.8989315704), (4.5349341148, 2.9431190243), (4.682366245, 2.9828347147), (4.8187480195, 3.0179422885), (4.9441534531, 3.0485182713), (5.059293445, 3.0747428382), (5.165295176, 3.096810876), (5.2634647581, 3.1148409034), (5.3550332157, 3.1287701717), (5.4409867971, 3.1383018441), (5.5222343688, 3.1430507417), (5.5996947246, 3.1426447428), (5.6744683782, 3.1368688991), (5.7331261215, 3.1279371949), (5.7769114323, 3.1188392725), (5.8060683154, 3.1117147092), (5.8206383991, 3.1078875943)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.0192861771, 0.0192861771, 0.0192861771, 0.0192861771, 0.0192861771, 0.0192861771, 0.0307692308, 0.0461538462, 0.0615384615, 0.0769230769, 0.0923076923, 0.1076923077, 0.1230769231, 0.1384615385, 0.1538461538, 0.1692307692, 0.1846153846, 0.2, 0.2153846154, 0.2307692308, 0.2461538462, 0.2615384615, 0.2769230769, 0.2923076923, 0.3076923077, 0.3230769231, 0.3384615385, 0.3538461538, 0.3692307692, 0.3846153846, 0.4, 0.4153846154, 0.4307692308, 0.4461538462, 0.4615384615, 0.4769230769, 0.4923076923, 0.5076923077, 0.5230769231, 0.5384615385, 0.5538461538, 0.5692307692, 0.5846153846, 0.6, 0.6153846154, 0.6307692308, 0.6461538462, 0.6615384615, 0.6769230769, 0.6923076923, 0.7076923077, 0.7230769231, 0.7384615385, 0.7538461538, 0.7692307692, 0.7846153846, 0.8, 0.8153846154, 0.8307692308, 0.8461538462, 0.8615384615, 0.8769230769, 0.8923076923, 0.9076923077, 0.9230769231, 0.9384615385, 0.9538461538, 0.9692307692, 0.9846153846, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((-1.1786699878, -1.1098287137), 0.4156845194, 82.6307400237, 287.9439551006)
                _nurbs_edge([(5.7870944266, 2.4130148383), (5.7826605921, 2.4031574988), (5.7736856022, 2.3842441059), (5.7599026662, 2.3582752057), (5.7408711591, 2.328477198), (5.7154342704, 2.2999992596), (5.6864201477, 2.282908933), (5.6507579147, 2.2810126815), (5.6069929977, 2.2938292069), (5.556473029, 2.3143532054), (5.5013363557, 2.3337793766), (5.4426258086, 2.3459266178), (5.3794359347, 2.3494595736), (5.3102416239, 2.3454584895), (5.2336620622, 2.3361572623), (5.1495710841, 2.3230532972), (5.0588064811, 2.3069634733), (4.9627218336, 2.2882609787), (4.862791348, 2.2670543506), (4.7601936769, 2.2433898032), (4.6554024787, 2.217444167), (4.548400823, 2.1894824633), (4.4388982849, 2.1598129242), (4.3265482606, 2.1287429157), (4.2111610545, 2.0965350644), (4.092928378, 2.0633619339), (3.9726165258, 2.0292650235), (3.8513366702, 1.9941745737), (3.7303391813, 1.9579254789), (3.6108039912, 1.9202745827), (3.4936215839, 1.8809171919), (3.379203444, 1.8395040372), (3.2672152587, 1.7956574987), (3.1566065098, 1.7489901088), (3.0458987846, 1.6991249775), (2.9334011839, 1.6457157342), (2.8174544016, 1.5884666658), (2.6966644088, 1.5271529965), (2.5701363347, 1.4616409047), (2.4377213949, 1.3919086802), (2.2998981004, 1.3180424414), (2.1576367317, 1.240230848), (2.0122710535, 1.1587602805), (1.8653667811, 1.0740101527), (1.7185936834, 0.986447959), (1.5735920919, 0.896625448), (1.4318517677, 0.8051724457), (1.2945605878, 0.712796817), (1.1625685825, 0.6202611177), (1.0364505159, 0.528339258), (0.9165400306, 0.437778924), (0.802975561, 0.3492614201), (0.695739725, 0.2633629721), (0.5947038757, 0.1805142304), (0.4996640134, 0.1009627437), (0.4103961546, 0.0247277213), (0.3266075404, -0.0484054185), (0.2478488316, -0.1188763863), (0.1734398548, -0.187345611), (0.1023871036, -0.2546899091), (0.033309624, -0.3219948885), (-0.0356533688, -0.3905584904), (-0.1064422937, -0.4615810996), (-0.1806753143, -0.535857369), (-0.2592200451, -0.6134439074), (-0.3418361511, -0.6933885822), (-0.4266368917, -0.7733032753), (-0.5102085956, -0.8495044406), (-0.5883990767, -0.9177298496), (-0.6569415025, -0.9737151685), (-0.7121096618, -1.0137938822), (-0.7435774894, -1.0312131347), (-0.7597150732, -1.035710857), (-0.7671548688, -1.0349006311), (-0.7700452692, -1.0335434929)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 0.9999999383, 0.9999999383, 0.9999999383, 0.9999999383, 0.9999999383, 0.9999999383], 5)
                Line((5.8408172669, 3.0808054331), (5.7870944266, 2.4130148383))
            make_face()
            with BuildLine():
                CenterArc((4.1513517931, 2.4416527111), 0.135, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.6609643414, 2.5625777225), 0.135, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.431175004, 0.4243486913), 0.135, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.0704189939, 0.0936819968), 0.135, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.5940375856, 2.5911176717), 0.085, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.2227141636, -1.1164188881), 0.085, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.16
        extrude(amount=0.16)
    return part.part


# Description: This is a cylindrical sleeve or bushing with an oval/elliptical cross-section, featuring two prominent horizontal grooves or channels running along its length and mesh-textured end surfaces.
def model_35968_5488b3e5_0001():
    """Model: ster"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.3432518436, perimeter: 24.8185819634
            with BuildLine():
                CenterArc((0, 0), 2.15, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.1129420437, perimeter: 29.2168116784
            with BuildLine():
                CenterArc((0, 0), 2.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


# Description: This is a truncated octahedron, a polyhedron with 14 faces (8 hexagonal and 6 square), 24 vertices, and 36 edges, characterized by its symmetrical geometric form with flattened corners.
def model_35968_5488b3e5_0006():
    """Model: nakretka do kola"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4.9883065983, perimeter: 8.3138441035
            with BuildLine():
                Line((-0.3071796729, 2.2000000414), (-1.6928203569, 2.2000000242))
                Line((-1.6928203569, 2.2000000242), (-2.3856406839, 0.9999999828))
                Line((-2.3856406839, 0.9999999828), (-1.6928203271, -0.2000000414))
                Line((-1.6928203271, -0.2000000414), (-0.3071796431, -0.2000000242))
                Line((-0.3071796431, -0.2000000242), (0.3856406839, 1.0000000172))
                Line((0.3856406839, 1.0000000172), (-0.3071796729, 2.2000000414))
            make_face()
        # OneSide extrude, distance=1.48
        extrude(amount=1.48)
    return part.part


# Description: This is a composite or layered blade/fin assembly with an elongated parallelogram shape, featuring multiple parallel slots or laminations running across its length, designed as an aerodynamic or structural component.
def model_35968_5488b3e5_0008():
    """Model: mata"""
    with BuildPart() as part:
        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 635.5801806545, perimeter: 135.4946436428
            with BuildLine():
                Line((-21, 24), (-21, 35.3006906012))
                Line((-27, 24), (-21, 24))
                Line((-27, 35.3006906012), (-27, 24))
                Line((-33.5, 35.3006906012), (-27, 35.3006906012))
                Line((-33.5, -2.575149019), (-33.5, 35.3006906012))
                Line((-14.9292084, -2.575149019), (-33.5, -2.575149019))
                Line((-14.9292084, 35.3006906012), (-14.9292084, -2.575149019))
                Line((-21, 35.3006906012), (-14.9292084, 35.3006906012))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is a flat rectangular plate or panel with a parallelogram shape, featuring beveled or chamfered edges along its perimeter and a slightly recessed or stepped surface detail.
def model_36268_3c96c142_0009():
    """Model: speaker grille v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 14 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 12.499975, perimeter: 78.74
            with BuildLine():
                Line((6.985, -3.175), (6.985, 3.175))
                Line((6.985, 3.175), (-6.985, 3.175))
                Line((-6.985, 3.175), (-6.985, -3.175))
                Line((-6.985, -3.175), (6.985, -3.175))
            make_face()
            with BuildLine():
                Line((-6.6675, -2.8575), (6.6675, -2.8575))
                Line((-6.6675, 2.8575), (-6.6675, -2.8575))
                Line((6.6675, 2.8575), (-6.6675, 2.8575))
                Line((6.6675, -2.8575), (6.6675, 2.8575))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 76.209525, perimeter: 38.1
            with BuildLine():
                Line((6.6675, -2.8575), (6.6675, 2.8575))
                Line((6.6675, 2.8575), (-6.6675, 2.8575))
                Line((-6.6675, 2.8575), (-6.6675, -2.8575))
                Line((-6.6675, -2.8575), (6.6675, -2.8575))
            make_face()
        # OneSide extrude, distance=0.15875
        extrude(amount=0.15875)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 14 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 12.499975, perimeter: 78.74
            with BuildLine():
                Line((6.985, -3.175), (6.985, 3.175))
                Line((6.985, 3.175), (-6.985, 3.175))
                Line((-6.985, 3.175), (-6.985, -3.175))
                Line((-6.985, -3.175), (6.985, -3.175))
            make_face()
            with BuildLine():
                Line((-6.6675, -2.8575), (6.6675, -2.8575))
                Line((-6.6675, 2.8575), (-6.6675, -2.8575))
                Line((6.6675, 2.8575), (-6.6675, 2.8575))
                Line((6.6675, -2.8575), (6.6675, 2.8575))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.3175
        extrude(amount=-0.3175, mode=Mode.ADD)
    return part.part


# Description: This is a chisel or cutting tool featuring a long, tapered cylindrical shaft with a textured grip section and a flat, angled cutting head at the end.
def model_36344_ecda4926_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 23 constraints, 19 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.0983537059, perimeter: 21.712183812
            with BuildLine():
                CenterArc((0, 0), 0.9, -86.5685676193, 69.1159753249)
                Line((0.0538685978, -0.8983864281), (0.0538685978, -1.8983864281))
                CenterArc((-9.2508845956, -8.4552391247), 11.382914797, -7.7996041161, 42.9711059862)
                Line((2.0267243315, -10), (2.9345045959, -10))
                CenterArc((-9.2508845956, -8.4552391247), 12.282914797, -7.2249361515, 36.8592160352)
                CenterArc((4.6254684857, -1.0470785195), 3.4672512552, 177.3592260907, 25.2815478185)
                Line((1.0750752419, -0.3949249145), (1.1618993307, -0.887328791))
                Line((0.858568891, -0.2699249145), (1.0750752419, -0.3949249145))
            make_face()
            # Profile area: 2.5446900494, perimeter: 5.6548667765
            with BuildLine():
                CenterArc((0, 0), 0.9, 92.7795266401, 68.3144326408)
                CenterArc((0, 0), 0.9, 161.0939592808, 112.3374730998)
                CenterArc((0, 0), 0.9, -86.5685676193, 69.1159753249)
                CenterArc((0, 0), 0.9, -17.4525922944, 110.2321189345)
            make_face()
            # Profile area: 3.2037760717, perimeter: 12.0803659031
            with BuildLine():
                Line((-0.15, 5.9), (-1.0498700799, 1.0263435542))
                Line((-1.0484076331, 0.3263450819), (-1.0498700799, 1.0263435542))
                Line((-0.8514460825, 0.2916154463), (-1.0484076331, 0.3263450819))
                CenterArc((0, 0), 0.9, 92.7795266401, 68.3144326408)
                Line((0, 5.9), (-0.0436435792, 0.898941176))
                Line((0, 5.9), (-0.15, 5.9))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a cylindrical tube or barrel with hemispherical end caps, featuring a series of parallel slots or grooves running longitudinally across its body surface.
def model_36436_362a4413_0030():
    """Model: Resistant v1"""
    with BuildPart() as part:
        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # Symmetric extrude, each_side=0.4
        extrude(amount=0.4, both=True)
    return part.part


# Description: This is a rectangular prism or box-shaped solid block with a tapered or wedge-like top surface, featuring clean edges and flat faces with no visible holes, slots, or curves.
def model_36445_67816b83_0006():
    """Model: Magnet"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.212, perimeter: 1.86
            with BuildLine():
                Line((0.1200000063, -0.2000000074), (-0.2799999937, -0.2000000074))
                Line((0.1200000063, 0.3299999926), (0.1200000063, -0.2000000074))
                Line((-0.2799999937, 0.3299999926), (0.1200000063, 0.3299999926))
                Line((-0.2799999937, -0.2000000074), (-0.2799999937, 0.3299999926))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a curved handle or grip component with a tubular, arc-shaped profile featuring a textured or knurled surface finish, designed for ergonomic gripping or carrying applications.
def model_36445_67816b83_0007():
    """Model: clip"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0191434774, perimeter: 1.5814795901
            with BuildLine():
                Line((0.0000323414, -0.1499999959), (0.000014359, -0.1749999758))
                CenterArc((0, 0), 0.1749999764, -89.9952987843, 269.9952987843)
                Line((-0.175, 0), (-0.15, 0))
                CenterArc((0, 0), 0.1499999993, -89.9876464962, 269.9876464962)
            make_face()
        # OneSide extrude, distance=0.01
        extrude(amount=0.01)
    return part.part


# Description: This is a dark gray metal or plastic connector plate with an elongated oval shape featuring two circular mounting holes aligned vertically and textured surfaces on the outer edges.
def model_36451_1a7f9437_0008():
    """Model: Housing"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 54 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 21.4710727317, perimeter: 95.2877938885
            with BuildLine():
                CenterArc((-9.6, 0), 5.8, -22.6198649481, 45.2397298961)
                CenterArc((0, -4), 4.6, 157.3801350519, 225.2397298961)
                CenterArc((9.6, 0), 5.8, 157.3801350519, 45.2397298961)
                CenterArc((0, 4), 4.6, -22.6198649481, 225.2397298961)
            make_face()
            with BuildLine():
                CenterArc((3, 0), 0.8, 126.8698976458, 106.2602047083)
                CenterArc((0, -4), 4.2, 126.8698976458, 286.2602047083)
                CenterArc((-3, 0), 0.8, -53.1301023542, 106.2602047083)
                CenterArc((0, 4), 4.2, -53.1301023542, 286.2602047083)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3, 0), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-3, 0), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.8
        extrude(amount=1.8)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 54 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 96.8085648802, perimeter: 63.7848385717
            with BuildLine():
                CenterArc((0, 4), 4.2, -53.1301023542, 286.2602047083)
                CenterArc((-3, 0), 0.8, -53.1301023542, 106.2602047083)
                CenterArc((0, -4), 4.2, 126.8698976458, 286.2602047083)
                CenterArc((3, 0), 0.8, 126.8698976458, 106.2602047083)
            make_face()
            with BuildLine():
                CenterArc((0, 4), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, -4), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


# Description: This is a circular disk or wheel with a textured rim, featuring a flat face, beveled or knurled edge on one side, and a small protruding pin or post on the lower right.
def model_36658_c1f72bb7_0000():
    """Model: Hand_Gear"""
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
            # Profile area: 30.5187792549, perimeter: 19.5834187724
            with BuildLine():
                CenterArc((0, 0), 3.1167979003, -2.5887690372, 5.1775380744)
                CenterArc((0, 0), 3.1167979003, 2.5887690372, 354.8224619256)
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0615671359, perimeter: 1.0086932663
            with BuildLine():
                _nurbs_edge([(3.1136170289, -0.1407769461), (3.1145362126, -0.1406967832), (3.1277999326, -0.1394855714), (3.1534067471, -0.1354956041), (3.190318255, -0.1281150211), (3.2272660813, -0.1188492088), (3.2642326017, -0.1080373572), (3.3011990788, -0.0957697336), (3.3381369368, -0.0821245374), (3.3750695959, -0.0672567502), (3.399442115, -0.0563982496), (3.4116941244, -0.0509397063)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.0339884809, 0.0339884809, 0.0339884809, 0.0339884809, 0.0367579437, 0.0739660331, 0.1116086742, 0.1496843263, 0.1881924538, 0.22713279, 0.266505173, 0.3063094911, 0.34654566, 0.34654566, 0.34654566, 0.34654566], 3)
                CenterArc((-0.0080994048, 0), 3.4201728956, -0.8533890489, 1.7067780978)
                _nurbs_edge([(3.1136170289, 0.1407769461), (3.1145362126, 0.1406967832), (3.1277999326, 0.1394855714), (3.1534067471, 0.1354956041), (3.190318255, 0.1281150211), (3.2272660813, 0.1188492088), (3.2642326017, 0.1080373572), (3.3011990788, 0.0957697336), (3.3381369368, 0.0821245374), (3.3750695959, 0.0672567502), (3.399442115, 0.0563982496), (3.4116941244, 0.0509397063)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.0339884809, 0.0339884809, 0.0339884809, 0.0339884809, 0.0367579437, 0.0739660331, 0.1116086742, 0.1496843263, 0.1881924538, 0.22713279, 0.266505173, 0.3063094911, 0.34654566, 0.34654566, 0.34654566, 0.34654566], 3)
                CenterArc((0, 0), 3.1167979003, -2.5887690372, 5.1775380744)
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


# Description: This is a circular disc or wheel with a knurled (textured) rim featuring a smooth, flat face and a raised, cross-hatched edge band that provides grip or aesthetic detailing.
def model_36658_c1f72bb7_0002():
    """Model: Gear_2"""
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
            # Profile area: 65.3355494718, perimeter: 28.6536337827
            with BuildLine():
                CenterArc((0, 0), 4.5603674541, -1.862837854, 3.7256757081)
                CenterArc((0, 0), 4.5603674541, 1.862837854, 356.2743242919)
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0624772106, perimeter: 1.0270647622
            with BuildLine():
                _nurbs_edge([(4.5579573465, -0.1482435285), (4.5639575033, -0.147045957), (4.5855825241, -0.1425416661), (4.6227542785, -0.133571788), (4.6693673991, -0.1205186101), (4.7159773346, -0.1057670561), (4.7625549762, -0.0894123291), (4.8091287484, -0.0716395774), (4.839902533, -0.0586860831), (4.8553632213, -0.0521782734)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.1224847322, 0.1224847322, 0.1224847322, 0.1224847322, 0.1408412985, 0.1887588803, 0.2371574357, 0.2860366966, 0.3353965075, 0.3852367663, 0.4355573993, 0.4355573993, 0.4355573993, 0.4355573993], 3)
                CenterArc((-0.0093018309, 0), 4.8649448756, -0.614529505, 1.22905901)
                _nurbs_edge([(4.5579573465, 0.1482435285), (4.5639575033, 0.147045957), (4.5855825241, 0.1425416661), (4.6227542785, 0.133571788), (4.6693673991, 0.1205186101), (4.7159773346, 0.1057670561), (4.7625549762, 0.0894123291), (4.8091287484, 0.0716395774), (4.839902533, 0.0586860831), (4.8553632213, 0.0521782734)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.1224847322, 0.1224847322, 0.1224847322, 0.1224847322, 0.1408412985, 0.1887588803, 0.2371574357, 0.2860366966, 0.3353965075, 0.3852367663, 0.4355573993, 0.4355573993, 0.4355573993, 0.4355573993], 3)
                CenterArc((0, 0), 4.5603674541, -1.862837854, 3.7256757081)
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical drum or wheel component with a solid flat face on one side and a perforated or mesh-textured curved surface on the opposite side, suggesting it may function as a filter, strainer, or ventilated drum.
def model_36658_c1f72bb7_0003():
    """Model: Component7"""
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
            # Profile area: 527.6113610237, perimeter: 81.425793843
            with BuildLine():
                CenterArc((0, 0), 12.9593175853, -0.697757675, 1.3955153501)
                CenterArc((0, 0), 12.9593175853, 0.697757675, 358.6044846499)
            make_face()
        # OneSide extrude, distance=10
        extrude(amount=10)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.063723501, perimeter: 1.0515638442
            with BuildLine():
                _nurbs_edge([(12.9583566133, -0.1578168562), (12.9886550008, -0.148435403), (13.053388216, -0.1275376131), (13.1522026652, -0.0931792406), (13.2203009965, -0.0671922617), (13.2544827759, -0.0541481655)], [1, 1, 1, 1, 1, 1], [0.6432576008, 0.6432576008, 0.6432576008, 0.6432576008, 0.7384083592, 0.8473100704, 0.9570633933, 0.9570633933, 0.9570633933, 0.9570633933], 3)
                CenterArc((-0.0245583082, 0), 13.279151484, -0.233634653, 0.467269306)
                _nurbs_edge([(12.9583566133, 0.1578168562), (12.9886550008, 0.148435403), (13.053388216, 0.1275376131), (13.1522026652, 0.0931792406), (13.2203009965, 0.0671922617), (13.2544827759, 0.0541481655)], [1, 1, 1, 1, 1, 1], [0.6432576008, 0.6432576008, 0.6432576008, 0.6432576008, 0.7384083592, 0.8473100704, 0.9570633933, 0.9570633933, 0.9570633933, 0.9570633933], 3)
                CenterArc((0, 0), 12.9593175853, -0.697757675, 1.3955153501)
            make_face()
        # OneSide extrude, distance=10
        extrude(amount=10, mode=Mode.ADD)
    return part.part


# Description: This is a triangular prism or wedge-shaped component with a flat base, sloped top surface, and a vertical face, featuring clean edges and uniform thickness throughout.
def model_36847_d0238124_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch3 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 253.5214620201, perimeter: 72.5902516619
            with BuildLine():
                Line((12.0894100822, -7.0005058781), (0.0179105017, 13.9699885187))
                Line((0.0179105017, 13.9699885187), (-12.1073205856, -6.9694839781))
                Line((-12.1073205856, -6.9694839781), (12.0894100822, -7.0005058781))
            make_face()
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)
    return part.part


# Description: This is a curved bracket or support rail with decorative scroll-end flanges at both ends, featuring a horizontal rectangular profile with upturned curled terminals on the left and right sides.
def model_36953_bdaf025b_0002():
    """Model: rurka do kosza"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 11 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 25.4101927683, perimeter: 170.0012851222
            with BuildLine():
                Line((-47.5523431781, 19), (-43.320399655, 19))
                CenterArc((-43.320399655, 18.5), 0.5, 20.7628214648, 69.2371785352)
                CenterArc((-45.3928571429, 17.7142857143), 2.7163995528, -140.869600443, 161.6324219079)
                Line((-47.5, 16), (-47.7327135036, 15.8106737598))
                CenterArc((-45.3928571429, 17.7142857143), 3.0163995528, -140.869600443, 161.6324219079)
                CenterArc((-43.320399655, 18.5), 0.8, 20.7628214648, 69.2371785352)
                Line((-47.5523431781, 19.3), (-43.320399655, 19.3))
                CenterArc((-47.5523431781, 18), 1.3, 90, 50.2081805004)
                CenterArc((-42.75, 14), 7.55, 140.2081805004, 74.6417240786)
                CenterArc((-47.0584219849, 11), 2.3, -145.150095421, 55.150095421)
                Line((-47.0584219849, 8.7), (-14, 8.7))
                CenterArc((-14, 11), 2.3, -90, 55.150095421)
                CenterArc((-18.3084219849, 14), 7.55, -34.849904579, 74.6417240786)
                CenterArc((-13.5060788068, 18), 1.3, 39.7918194996, 50.2081805004)
                Line((-13.5060788068, 19.3), (-17.7380223299, 19.3))
                CenterArc((-17.7380223299, 18.5), 0.8, 90, 69.2371785352)
                CenterArc((-15.665564842, 17.7142857143), 3.0163995528, 159.2371785352, 161.6324219079)
                Line((-13.5584219849, 16), (-13.3257084813, 15.8106737598))
                CenterArc((-15.665564842, 17.7142857143), 2.7163995528, 159.2371785352, 161.6324219079)
                CenterArc((-17.7380223299, 18.5), 0.5, 90, 69.2371785352)
                Line((-13.5060788068, 19), (-17.7380223299, 19))
                CenterArc((-13.5060788068, 18), 1, 39.7918194996, 50.2081805004)
                CenterArc((-18.3084219849, 14), 7.25, -34.849904579, 74.6417240786)
                CenterArc((-14, 11), 2, -90, 55.150095421)
                Line((-47.0584219849, 9), (-14, 9))
                CenterArc((-47.0584219849, 11), 2, -145.150095421, 55.150095421)
                CenterArc((-42.75, 14), 7.25, 140.2081805004, 74.6417240786)
                CenterArc((-47.5523431781, 18), 1, 90, 50.2081805004)
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)
    return part.part


# Description: This is a tapered metal pin or punch with a long, slender conical shape that gradually narrows from a blunt end to a sharp point, commonly used for alignment, fastening, or tool applications.
def model_36953_bdaf025b_0003():
    """Model: poprzeczne blaszki"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 5.32, perimeter: 53.6
            with BuildLine():
                Line((-18.609996558, -8.7928942569), (7.990003442, -8.7928942569))
                Line((-18.609996558, -8.7928942569), (-18.609996558, -8.9928942569))
                Line((-18.609996558, -8.9928942569), (7.990003442, -8.9928942569))
                Line((7.990003442, -8.7928942569), (7.990003442, -8.9928942569))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a triangular prism or wedge-shaped structural component featuring a tapered pentagonal profile with a flat base, sloped top surfaces, and internal reinforcing ribs or webs for structural support.
def model_37040_ecbcd25e_0002():
    """Model: podstawa v5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 363.2712640027, perimeter: 72.6542528005
            with BuildLine():
                Line((-7.2654252801, -10), (7.2654252801, -10))
                Line((7.2654252801, -10), (11.7557050458, 3.8196601125))
                Line((11.7557050458, 3.8196601125), (0, 12.360679775))
                Line((0, 12.360679775), (-11.7557050458, 3.8196601125))
                Line((-11.7557050458, 3.8196601125), (-7.2654252801, -10))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a hexagonal or elongated diamond-shaped frame with a hollow center and uniform wall thickness, featuring beveled edges and a flat, planar design typical of a structural bracket or mounting frame component.
def model_37040_ecbcd25e_0023():
    """Model: strop v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 76.2869654406, perimeter: 152.5739308811
            with BuildLine():
                Line((7.9919678081, -11), (12.9312755504, 4.2016261238))
                Line((12.9312755504, 4.2016261238), (0, 13.5967477525))
                Line((0, 13.5967477525), (-12.9312755504, 4.2016261238))
                Line((-12.9312755504, 4.2016261238), (-7.9919678081, -11))
                Line((-7.9919678081, -11), (7.9919678081, -11))
            make_face()
            with BuildLine():
                Line((-11.7557050458, 3.8196601125), (-7.2654252801, -10))
                Line((0, 12.360679775), (-11.7557050458, 3.8196601125))
                Line((11.7557050458, 3.8196601125), (0, 12.360679775))
                Line((7.2654252801, -10), (11.7557050458, 3.8196601125))
                Line((-7.2654252801, -10), (7.2654252801, -10))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 69.0215401605, perimeter: 138.043080321
            with BuildLine():
                Line((-7.2654252801, -10), (7.2654252801, -10))
                Line((7.2654252801, -10), (11.7557050458, 3.8196601125))
                Line((11.7557050458, 3.8196601125), (0, 12.360679775))
                Line((0, 12.360679775), (-11.7557050458, 3.8196601125))
                Line((-11.7557050458, 3.8196601125), (-7.2654252801, -10))
            make_face()
            with BuildLine():
                Line((-6.538882752, -9), (6.538882752, -9))
                Line((-10.5801345413, 3.4376941013), (-6.538882752, -9))
                Line((0, 11.1246117975), (-10.5801345413, 3.4376941013))
                Line((10.5801345413, 3.4376941013), (0, 11.1246117975))
                Line((6.538882752, -9), (10.5801345413, 3.4376941013))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a blue anodized aluminum aerospace or automotive component with an elongated, tapered hexagonal profile featuring central cutout slots and ribbed reinforcement patterns along its length.
def model_37040_ecbcd25e_0032():
    """Model: rolka v3 (2)"""
    with BuildPart() as part:
        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6536504688, perimeter: 5.4299223889
            with BuildLine():
                Line((0.4, -1), (1.3000000194, -0.5000000075))
                Line((1.3000000194, -0.5000000075), (0.4, 0))
                Line((0, 0), (0.4, 0))
                Line((0, -1), (0, 0))
                Line((0.4, -1), (0, -1))
            make_face()
            with BuildLine():
                CenterArc((0.5000000075, -0.5000000075), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is an aerodynamic boat hull or aircraft fuselage featuring a sleek, elongated spindle shape with a pointed nose cone, tapered body, and fine stern, characterized by smooth curves and a streamlined profile optimized for hydrodynamic or aerodynamic performance.
def model_37117_89aac9d4_0005():
    """Model: arduino_mount"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.4059880228, 5.5134782561, -2.1711939584), x_dir=(0, 0, -1), z_dir=(0.2377664048, 0.971322365, 0))):
            # Profile area: 30.5126057772, perimeter: 22.6143977186
            with BuildLine():
                Line((-13.2080004215, -2.6628013677), (-13.2080004215, -7.112000227))
                Line((-13.2080004215, -7.112000227), (-6.3500004215, -7.112000227))
                Line((-6.3500004215, -7.112000227), (-6.3500004215, -2.6628013677))
                Line((-6.3500004215, -2.6628013677), (-13.2080004215, -2.6628013677))
            make_face()
            # Profile area: 6.0679662228, perimeter: 15.4856022814
            with BuildLine():
                Line((-6.3500004215, -2.6628013677), (-13.2080004215, -2.6628013677))
                Line((-6.3500004215, -2.6628013677), (-6.3500004215, -1.778000227))
                Line((-6.3500004215, -1.778000227), (-13.2080004215, -1.778000227))
                Line((-13.2080004215, -1.778000227), (-13.2080004215, -2.6628013677))
            make_face()
        # OneSide extrude, distance=0.3175
        extrude(amount=0.3175)
    return part.part


# Description: A cylindrical rod or shaft with a long, slender, tapered design, featuring a slightly textured or knurled surface along its length.
def model_37267_b2be4b50_0024():
    """Model: pivot (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.6858403578, perimeter: 8.3955646226
            with BuildLine():
                CenterArc((80, 5), 1.5, 90, 210)
                Line((80, 6.5), (80.75, 3.7009618943))
            make_face()
            # Profile area: 2.3827431127, perimeter: 6.8247682959
            with BuildLine():
                Line((80, 6.5), (80.75, 3.7009618943))
                CenterArc((80, 5), 1.5, -60, 150)
            make_face()
        # OneSide extrude, distance=-4
        extrude(amount=-4)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.6858403578, perimeter: 8.3955646226
            with BuildLine():
                CenterArc((80, 5), 1.5, 90, 210)
                Line((80, 6.5), (80.75, 3.7009618943))
            make_face()
        # OneSide extrude, distance=70
        extrude(amount=70, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical container or housing with an oval/elliptical shape, featuring a recessed top surface with a mesh or perforated pattern and a central slot or opening, likely designed as a filter housing, air duct component, or ventilation element.
def model_37377_90529181_0004():
    """Model: kolo wewn v2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.1233403578, perimeter: 10.9955742876
            with BuildLine():
                CenterArc((-6, 3.5), 1.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-6, 3.5), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 90.1244392499, perimeter: 42.4115008235
            with BuildLine():
                CenterArc((-6, 3.5), 5.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-6, 3.5), 1.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.5
        extrude(amount=2.5, mode=Mode.ADD)
    return part.part


# Description: This is a gear with a large flat circular face and a textured rim featuring evenly-spaced teeth around its outer edge, designed for power transmission in mechanical systems.
def model_37524_6004c446_0001():
    """Model: Gear"""
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
            # Profile area: 110.7534128853, perimeter: 37.3064127614
            with BuildLine():
                CenterArc((0, 0), 5.9375, -2.5887690372, 5.1775380744)
                CenterArc((0, 0), 5.9375, 2.5887690372, 354.8224619256)
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.2234286755, perimeter: 1.9215606724
            with BuildLine():
                _nurbs_edge([(5.93144044, -0.2681800824), (5.9331914849, -0.268027372), (5.9584588716, -0.2657200136), (6.0072398531, -0.2581191258), (6.0775562759, -0.2440591152), (6.1479418848, -0.2264077428), (6.2183631062, -0.2058111655), (6.2887842452, -0.1824413426), (6.3591508646, -0.1564472438), (6.4295075802, -0.1281241091), (6.4759372291, -0.1074386654), (6.4992773069, -0.0970401404)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.0647480561, 0.0647480561, 0.0647480561, 0.0647480561, 0.0700238827, 0.1409052931, 0.2126145243, 0.2851486416, 0.3585066244, 0.4326879649, 0.5076923546, 0.5835195806, 0.6601694824, 0.6601694824, 0.6601694824, 0.6601694824], 3)
                CenterArc((-0.0154293661, 0), 6.5154293661, -0.8533890489, 1.7067780978)
                _nurbs_edge([(5.93144044, 0.2681800824), (5.9331914849, 0.268027372), (5.9584588716, 0.2657200136), (6.0072398531, 0.2581191258), (6.0775562759, 0.2440591152), (6.1479418848, 0.2264077428), (6.2183631062, 0.2058111655), (6.2887842452, 0.1824413426), (6.3591508646, 0.1564472438), (6.4295075802, 0.1281241091), (6.4759372291, 0.1074386654), (6.4992773069, 0.0970401404)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.0647480561, 0.0647480561, 0.0647480561, 0.0647480561, 0.0700238827, 0.1409052931, 0.2126145243, 0.2851486416, 0.3585066244, 0.4326879649, 0.5076923546, 0.5835195806, 0.6601694824, 0.6601694824, 0.6601694824, 0.6601694824], 3)
                CenterArc((0, 0), 5.9375, -2.5887690372, 5.1775380744)
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)
    return part.part


# Description: This is a circular disc or pulley with an overall flat, disc-like shape featuring a toothed or gear-tooth pattern around its outer edge and what appears to be a central hub or axle mount on one side.
def model_37524_6004c446_0002():
    """Model: Gear (1)"""
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
            # Profile area: 144.6575188707, perimeter: 42.6359002987
            with BuildLine():
                CenterArc((0, 0), 6.7857142857, -2.5887690372, 5.1775380744)
                CenterArc((0, 0), 6.7857142857, 2.5887690372, 354.8224619256)
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.2918252088, perimeter: 2.1960693399
            with BuildLine():
                _nurbs_edge([(6.7787890743, -0.3064915227), (6.7807902685, -0.3063169965), (6.8096672818, -0.3036800155), (6.865416975, -0.2949932866), (6.945778601, -0.2789247031), (7.0262192969, -0.258751706), (7.1067006928, -0.2352127606), (7.1871819945, -0.2085043915), (7.2676009881, -0.1787968501), (7.3480086631, -0.1464275532), (7.401071119, -0.1227870462), (7.4277454936, -0.1109030176)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.0739977785, 0.0739977785, 0.0739977785, 0.0739977785, 0.0800272945, 0.1610346207, 0.2429880278, 0.3258841619, 0.4097218565, 0.4945005313, 0.5802198338, 0.6668795207, 0.7544794084, 0.7544794084, 0.7544794084, 0.7544794084], 3)
                CenterArc((-0.0176335613, 0), 7.4462049899, -0.8533890489, 1.7067780978)
                _nurbs_edge([(6.7787890743, 0.3064915227), (6.7807902685, 0.3063169965), (6.8096672818, 0.3036800155), (6.865416975, 0.2949932866), (6.945778601, 0.2789247031), (7.0262192969, 0.258751706), (7.1067006928, 0.2352127606), (7.1871819945, 0.2085043915), (7.2676009881, 0.1787968501), (7.3480086631, 0.1464275532), (7.401071119, 0.1227870462), (7.4277454936, 0.1109030176)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.0739977785, 0.0739977785, 0.0739977785, 0.0739977785, 0.0800272945, 0.1610346207, 0.2429880278, 0.3258841619, 0.4097218565, 0.4945005313, 0.5802198338, 0.6668795207, 0.7544794084, 0.7544794084, 0.7544794084, 0.7544794084], 3)
                CenterArc((0, 0), 6.7857142857, -2.5887690372, 5.1775380744)
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical housing or connector body with a curved front face, a protruding nozzle or spout on the lower right side, and a mesh or perforated section visible on the upper curved surface.
def model_37596_8efba003_0001():
    """Model: Component2"""
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
            # Profile area: 1.2207511702, perimeter: 3.9166837545
            with BuildLine():
                CenterArc((0, 0), 0.6233595801, 8.2665492276, 343.4669015447)
                CenterArc((0, 0), 0.6233595801, -8.2665492276, 16.5330984553)
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.053034558, perimeter: 0.8944796302
            with BuildLine():
                Line((0.6168828113, 0.0896256838), (0.7320645047, 0.1063602043))
                CenterArc((0, 0), 0.6233595801, -8.2665492276, 16.5330984553)
                Line((0.6168828113, -0.0896256838), (0.7320645047, -0.1063602043))
                _nurbs_edge([(0.7320645047, -0.1063602043), (0.738772923, -0.1064994128), (0.7523709413, -0.1067815894), (0.7728298681, -0.1036056618), (0.7934796978, -0.0990107529), (0.8142492071, -0.0927523326), (0.835076143, -0.0850853548), (0.8559123134, -0.0760599414), (0.8766955508, -0.0657221348), (0.8974308106, -0.0541894681), (0.9109172419, -0.0456154696), (0.9177318815, -0.0412830627)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0200935175, 0.0407297233, 0.0618853311, 0.0835562007, 0.1057400062, 0.128435053, 0.1516399726, 0.17535361, 0.1995749729, 0.1995749729, 0.1995749729, 0.1995749729], 3)
                CenterArc((-0.0251972653, 0), 0.9438324359, -2.5069069843, 5.0138139687)
                _nurbs_edge([(0.7320645047, 0.1063602043), (0.738772923, 0.1064994128), (0.7523709413, 0.1067815894), (0.7728298681, 0.1036056618), (0.7934796978, 0.0990107529), (0.8142492071, 0.0927523326), (0.835076143, 0.0850853548), (0.8559123134, 0.0760599414), (0.8766955508, 0.0657221348), (0.8974308106, 0.0541894681), (0.9109172419, 0.0456154696), (0.9177318815, 0.0412830627)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0200935175, 0.0407297233, 0.0618853311, 0.0835562007, 0.1057400062, 0.128435053, 0.1516399726, 0.17535361, 0.1995749729, 0.1995749729, 0.1995749729, 0.1995749729], 3)
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


# Description: This is a hexagonal or multi-faceted structural component with an irregular polyhedron shape, featuring hollow interior cavities, mesh-patterned cutouts or perforations on its faces, and angled planar surfaces that create a complex geometric form.
def model_37615_8399c412_0009():
    """Model: Component8"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7729158594, perimeter: 5.6693921498
            with BuildLine():
                Line((0.55, -0.3175426481), (0.55, 0.3175426481))
                Line((0.55, 0.3175426481), (0, 0.6350852961))
                Line((0, 0.6350852961), (-0.55, 0.3175426481))
                Line((-0.55, 0.3175426481), (-0.55, -0.3175426481))
                Line((-0.55, -0.3175426481), (0, -0.6350852961))
                Line((0, -0.6350852961), (0.55, -0.3175426481))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.29585, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides extrude (symmetric), distance=0.275
        extrude(amount=0.275, both=True)
    return part.part


# Description: This is a circular disc or washer with a flat, disc-shaped body and a slightly beveled or curved edge around its perimeter.
def model_37840_de7298de_0000():
    """Model: Sun2"""
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
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 136.8477759904, perimeter: 41.4690230274
            with BuildLine():
                CenterArc((0, 0), 6.6, 0.9812688636, 358.0374622728)
                CenterArc((0, 0), 6.6, -0.9812688636, 1.9625377272)
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0579473217, perimeter: 0.941119224
            with BuildLine():
                Line((6.599032092, 0.113028533), (6.6659449382, 0.1183994791))
                CenterArc((0, 0), 6.6, -0.9812688636, 1.9625377272)
                Line((6.599032092, -0.113028533), (6.6659449382, -0.1183994791))
                _nurbs_edge([(6.6659449382, -0.1183994791), (6.666971792, -0.1184154506), (6.6690259748, -0.1184351684), (6.6721086746, -0.1184280686), (6.6762217944, -0.118345191), (6.6813679113, -0.1181194671), (6.686518605, -0.1177728966), (6.6916735789, -0.1173084768), (6.6968323186, -0.1167316539), (6.7019940451, -0.1160508941), (6.7071578316, -0.1152762853), (6.7123227105, -0.1144182588), (6.7174877807, -0.1134863142), (6.7226523226, -0.1124876465), (6.7278158868, -0.1114260999), (6.7329782064, -0.110303242), (6.7381391294, -0.1091192125), (6.7432985456, -0.1078736261), (6.7484563103, -0.1065665241), (6.7536121874, -0.1051990906), (6.758765887, -0.103773178), (6.7639170919, -0.1022909942), (6.7690654861, -0.100754744), (6.7742107855, -0.0991662604), (6.7793527602, -0.097526741), (6.7844912144, -0.0958369629), (6.7896259738, -0.0940974285), (6.7947568706, -0.0923085336), (6.799883728, -0.0904707429), (6.8050063501, -0.0885847181), (6.8101245317, -0.0866512267), (6.8152380665, -0.0846710842), (6.820346755, -0.0826450882), (6.8254504141, -0.0805739522), (6.8305488831, -0.0784582571), (6.8356420116, -0.0762984914), (6.8407296492, -0.0740950806), (6.8458116367, -0.0718484209), (6.8508877943, -0.0695589164), (6.8559579154, -0.0672270085), (6.8610217856, -0.0648531524), (6.8660791991, -0.0624378007), (6.8711299765, -0.0599813862), (6.876173983, -0.0574843067), (6.8812111441, -0.0549469102), (6.8862414287, -0.0523694843), (6.8902601529, -0.0502756933), (6.8932711049, -0.0486874956), (6.8952770334, -0.0476207682), (6.8962796545, -0.0470854223)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0222222222, 0.0444444444, 0.0666666667, 0.0888888889, 0.1111111111, 0.1333333333, 0.1555555556, 0.1777777778, 0.2, 0.2222222222, 0.2444444444, 0.2666666667, 0.2888888889, 0.3111111111, 0.3333333333, 0.3555555556, 0.3777777778, 0.4, 0.4222222222, 0.4444444444, 0.4666666667, 0.4888888889, 0.5111111111, 0.5333333333, 0.5555555556, 0.5777777778, 0.6, 0.6222222222, 0.6444444444, 0.6666666667, 0.6888888889, 0.7111111111, 0.7333333333, 0.7555555556, 0.7777777778, 0.8, 0.8222222222, 0.8444444444, 0.8666666667, 0.8888888889, 0.9111111111, 0.9333333333, 0.9555555556, 0.9777777778, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((5.1807572246, 0), 1.716168478, -1.5721851245, 3.144370249)
                _nurbs_edge([(6.6659449382, 0.1183994791), (6.666971792, 0.1184154506), (6.6690259748, 0.1184351684), (6.6721086746, 0.1184280686), (6.6762217944, 0.118345191), (6.6813679113, 0.1181194671), (6.686518605, 0.1177728966), (6.6916735789, 0.1173084768), (6.6968323186, 0.1167316539), (6.7019940451, 0.1160508941), (6.7071578316, 0.1152762853), (6.7123227105, 0.1144182588), (6.7174877807, 0.1134863142), (6.7226523226, 0.1124876465), (6.7278158868, 0.1114260999), (6.7329782064, 0.110303242), (6.7381391294, 0.1091192125), (6.7432985456, 0.1078736261), (6.7484563103, 0.1065665241), (6.7536121874, 0.1051990906), (6.758765887, 0.103773178), (6.7639170919, 0.1022909942), (6.7690654861, 0.100754744), (6.7742107855, 0.0991662604), (6.7793527602, 0.097526741), (6.7844912144, 0.0958369629), (6.7896259738, 0.0940974285), (6.7947568706, 0.0923085336), (6.799883728, 0.0904707429), (6.8050063501, 0.0885847181), (6.8101245317, 0.0866512267), (6.8152380665, 0.0846710842), (6.820346755, 0.0826450882), (6.8254504141, 0.0805739522), (6.8305488831, 0.0784582571), (6.8356420116, 0.0762984914), (6.8407296492, 0.0740950806), (6.8458116367, 0.0718484209), (6.8508877943, 0.0695589164), (6.8559579154, 0.0672270085), (6.8610217856, 0.0648531524), (6.8660791991, 0.0624378007), (6.8711299765, 0.0599813862), (6.876173983, 0.0574843067), (6.8812111441, 0.0549469102), (6.8862414287, 0.0523694843), (6.8902601529, 0.0502756933), (6.8932711049, 0.0486874956), (6.8952770334, 0.0476207682), (6.8962796545, 0.0470854223)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0222222222, 0.0444444444, 0.0666666667, 0.0888888889, 0.1111111111, 0.1333333333, 0.1555555556, 0.1777777778, 0.2, 0.2222222222, 0.2444444444, 0.2666666667, 0.2888888889, 0.3111111111, 0.3333333333, 0.3555555556, 0.3777777778, 0.4, 0.4222222222, 0.4444444444, 0.4666666667, 0.4888888889, 0.5111111111, 0.5333333333, 0.5555555556, 0.5777777778, 0.6, 0.6222222222, 0.6444444444, 0.6666666667, 0.6888888889, 0.7111111111, 0.7333333333, 0.7555555556, 0.7777777778, 0.8, 0.8222222222, 0.8444444444, 0.8666666667, 0.8888888889, 0.9111111111, 0.9333333333, 0.9555555556, 0.9777777778, 1, 1, 1, 1, 1, 1], 5)
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)
    return part.part


# Description: This is a spherical or hemispherical enclosure with a mesh or perforated curved panel on the upper portion, featuring a solid base and a small protruding nozzle or connector on the side—likely designed as a fan shroud, acoustic cover, or ventilated housing component.
def model_37840_de7298de_0002():
    """Model: Planet1"""
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
            # Profile area: 6.2525454673, perimeter: 8.8640737601
            with BuildLine():
                CenterArc((0, 0), 1.4107611549, 4.5891664191, 350.8216671617)
                CenterArc((0, 0), 1.4107611549, -4.5891664191, 9.1783328383)
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0578375759, perimeter: 0.9448552377
            with BuildLine():
                Line((1.4062382896, 0.1128756353), (1.4750559811, 0.1183994791))
                CenterArc((0, 0), 1.4107611549, -4.5891664191, 9.1783328383)
                Line((1.4062382896, -0.1128756353), (1.4750559811, -0.1183994791))
                _nurbs_edge([(1.4750559811, -0.1183994791), (1.483505156, -0.1182361373), (1.5005505492, -0.117906611), (1.526040453, -0.1137999393), (1.5516464448, -0.1083103051), (1.5773134514, -0.1012221694), (1.6030117284, -0.0928076893), (1.6287154851, -0.0831329629), (1.6543888208, -0.0722561182), (1.680047831, -0.0603011698), (1.6969015882, -0.051512306), (1.7053906974, -0.0470854223)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0253227337, 0.0510861656, 0.0772744214, 0.1038856914, 0.1309192311, 0.1583745993, 0.1862514819, 0.2145496314, 0.2432688409, 0.2432688409, 0.2432688409, 0.2432688409], 3)
                CenterArc((-0.0101317325, 0), 1.716168478, -1.5721851245, 3.144370249)
                _nurbs_edge([(1.4750559811, 0.1183994791), (1.483505156, 0.1182361373), (1.5005505492, 0.117906611), (1.526040453, 0.1137999393), (1.5516464448, 0.1083103051), (1.5773134514, 0.1012221694), (1.6030117284, 0.0928076893), (1.6287154851, 0.0831329629), (1.6543888208, 0.0722561182), (1.680047831, 0.0603011698), (1.6969015882, 0.051512306), (1.7053906974, 0.0470854223)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0253227337, 0.0510861656, 0.0772744214, 0.1038856914, 0.1309192311, 0.1583745993, 0.1862514819, 0.2145496314, 0.2432688409, 0.2432688409, 0.2432688409, 0.2432688409], 3)
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical filter or strainer component with a mesh or perforated surface on the curved sides and solid end caps, featuring what appears to be a small outlet or connection point at the bottom.
def model_37840_de7298de_0003():
    """Model: Planet2"""
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
            # Profile area: 6.2525454673, perimeter: 8.8640737601
            with BuildLine():
                CenterArc((0, 0), 1.4107611549, 4.5891664191, 350.8216671617)
                CenterArc((0, 0), 1.4107611549, -4.5891664191, 9.1783328383)
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0578375759, perimeter: 0.9448552377
            with BuildLine():
                Line((1.4062382896, 0.1128756353), (1.4750559811, 0.1183994791))
                CenterArc((0, 0), 1.4107611549, -4.5891664191, 9.1783328383)
                Line((1.4062382896, -0.1128756353), (1.4750559811, -0.1183994791))
                _nurbs_edge([(1.4750559811, -0.1183994791), (1.483505156, -0.1182361373), (1.5005505492, -0.117906611), (1.526040453, -0.1137999393), (1.5516464448, -0.1083103051), (1.5773134514, -0.1012221694), (1.6030117284, -0.0928076893), (1.6287154851, -0.0831329629), (1.6543888208, -0.0722561182), (1.680047831, -0.0603011698), (1.6969015882, -0.051512306), (1.7053906974, -0.0470854223)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0253227337, 0.0510861656, 0.0772744214, 0.1038856914, 0.1309192311, 0.1583745993, 0.1862514819, 0.2145496314, 0.2432688409, 0.2432688409, 0.2432688409, 0.2432688409], 3)
                CenterArc((-0.0101317325, 0), 1.716168478, -1.5721851245, 3.144370249)
                _nurbs_edge([(1.4750559811, 0.1183994791), (1.483505156, 0.1182361373), (1.5005505492, 0.117906611), (1.526040453, 0.1137999393), (1.5516464448, 0.1083103051), (1.5773134514, 0.1012221694), (1.6030117284, 0.0928076893), (1.6287154851, 0.0831329629), (1.6543888208, 0.0722561182), (1.680047831, 0.0603011698), (1.6969015882, 0.051512306), (1.7053906974, 0.0470854223)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0253227337, 0.0510861656, 0.0772744214, 0.1038856914, 0.1309192311, 0.1583745993, 0.1862514819, 0.2145496314, 0.2432688409, 0.2432688409, 0.2432688409, 0.2432688409], 3)
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.ADD)
    return part.part


# Description: This is a circular disc or pulley with a flat face and a textured or ribbed rim around its outer edge, featuring a central bore for shaft mounting.
def model_37840_de7298de_0004():
    """Model: Inputshaft_sun"""
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
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 38.4845100065, perimeter: 21.9911485751
            with BuildLine():
                CenterArc((0, 0), 3.5, 1.8506650967, 356.2986698066)
                CenterArc((0, 0), 3.5, -1.8506650967, 3.7013301934)
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0578109789, perimeter: 0.9410898131
            with BuildLine():
                Line((3.4981743787, 0.1130310409), (3.5650559811, 0.1183994791))
                CenterArc((0, 0), 3.5, -1.8506650967, 3.7013301934)
                Line((3.4981743787, -0.1130310409), (3.5650559811, -0.1183994791))
                _nurbs_edge([(3.5650559811, -0.1183994791), (3.5660828349, -0.1184154506), (3.5681370177, -0.1184351684), (3.5712197174, -0.1184280686), (3.5753328373, -0.118345191), (3.5804789541, -0.1181194671), (3.5856296479, -0.1177728966), (3.5907846217, -0.1173084768), (3.5959433615, -0.1167316539), (3.601105088, -0.1160508941), (3.6062688745, -0.1152762853), (3.6114337534, -0.1144182588), (3.6165988236, -0.1134863142), (3.6217633655, -0.1124876465), (3.6269269296, -0.1114260999), (3.6320892493, -0.110303242), (3.6372501723, -0.1091192125), (3.6424095885, -0.1078736261), (3.6475673532, -0.1065665241), (3.6527232302, -0.1051990906), (3.6578769299, -0.103773178), (3.6630281348, -0.1022909942), (3.668176529, -0.100754744), (3.6733218284, -0.0991662604), (3.6784638031, -0.097526741), (3.6836022573, -0.0958369629), (3.6887370167, -0.0940974285), (3.6938679135, -0.0923085336), (3.6989947709, -0.0904707429), (3.704117393, -0.0885847181), (3.7092355746, -0.0866512267), (3.7143491094, -0.0846710842), (3.7194577979, -0.0826450882), (3.724561457, -0.0805739522), (3.729659926, -0.0784582571), (3.7347530544, -0.0762984914), (3.7398406921, -0.0740950806), (3.7449226796, -0.0718484209), (3.7499988372, -0.0695589164), (3.7550689583, -0.0672270085), (3.7601328285, -0.0648531524), (3.765190242, -0.0624378007), (3.7702410194, -0.0599813862), (3.7752850259, -0.0574843067), (3.780322187, -0.0549469102), (3.7853524716, -0.0523694843), (3.7893711957, -0.0502756933), (3.7923821477, -0.0486874956), (3.7943880763, -0.0476207682), (3.7953906974, -0.0470854223)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0222222222, 0.0444444444, 0.0666666667, 0.0888888889, 0.1111111111, 0.1333333333, 0.1555555556, 0.1777777778, 0.2, 0.2222222222, 0.2444444444, 0.2666666667, 0.2888888889, 0.3111111111, 0.3333333333, 0.3555555556, 0.3777777778, 0.4, 0.4222222222, 0.4444444444, 0.4666666667, 0.4888888889, 0.5111111111, 0.5333333333, 0.5555555556, 0.5777777778, 0.6, 0.6222222222, 0.6444444444, 0.6666666667, 0.6888888889, 0.7111111111, 0.7333333333, 0.7555555556, 0.7777777778, 0.8, 0.8222222222, 0.8444444444, 0.8666666667, 0.8888888889, 0.9111111111, 0.9333333333, 0.9555555556, 0.9777777778, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((2.0798682675, 0), 1.716168478, -1.5721851245, 3.144370249)
                _nurbs_edge([(3.5650559811, 0.1183994791), (3.5660828349, 0.1184154506), (3.5681370177, 0.1184351684), (3.5712197174, 0.1184280686), (3.5753328373, 0.118345191), (3.5804789541, 0.1181194671), (3.5856296479, 0.1177728966), (3.5907846217, 0.1173084768), (3.5959433615, 0.1167316539), (3.601105088, 0.1160508941), (3.6062688745, 0.1152762853), (3.6114337534, 0.1144182588), (3.6165988236, 0.1134863142), (3.6217633655, 0.1124876465), (3.6269269296, 0.1114260999), (3.6320892493, 0.110303242), (3.6372501723, 0.1091192125), (3.6424095885, 0.1078736261), (3.6475673532, 0.1065665241), (3.6527232302, 0.1051990906), (3.6578769299, 0.103773178), (3.6630281348, 0.1022909942), (3.668176529, 0.100754744), (3.6733218284, 0.0991662604), (3.6784638031, 0.097526741), (3.6836022573, 0.0958369629), (3.6887370167, 0.0940974285), (3.6938679135, 0.0923085336), (3.6989947709, 0.0904707429), (3.704117393, 0.0885847181), (3.7092355746, 0.0866512267), (3.7143491094, 0.0846710842), (3.7194577979, 0.0826450882), (3.724561457, 0.0805739522), (3.729659926, 0.0784582571), (3.7347530544, 0.0762984914), (3.7398406921, 0.0740950806), (3.7449226796, 0.0718484209), (3.7499988372, 0.0695589164), (3.7550689583, 0.0672270085), (3.7601328285, 0.0648531524), (3.765190242, 0.0624378007), (3.7702410194, 0.0599813862), (3.7752850259, 0.0574843067), (3.780322187, 0.0549469102), (3.7853524716, 0.0523694843), (3.7893711957, 0.0502756933), (3.7923821477, 0.0486874956), (3.7943880763, 0.0476207682), (3.7953906974, 0.0470854223)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0222222222, 0.0444444444, 0.0666666667, 0.0888888889, 0.1111111111, 0.1333333333, 0.1555555556, 0.1777777778, 0.2, 0.2222222222, 0.2444444444, 0.2666666667, 0.2888888889, 0.3111111111, 0.3333333333, 0.3555555556, 0.3777777778, 0.4, 0.4222222222, 0.4444444444, 0.4666666667, 0.4888888889, 0.5111111111, 0.5333333333, 0.5555555556, 0.5777777778, 0.6, 0.6222222222, 0.6444444444, 0.6666666667, 0.6888888889, 0.7111111111, 0.7333333333, 0.7555555556, 0.7777777778, 0.8, 0.8222222222, 0.8444444444, 0.8666666667, 0.8888888889, 0.9111111111, 0.9333333333, 0.9555555556, 0.9777777778, 1, 1, 1, 1, 1, 1], 5)
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)
    return part.part


# Description: This is a circular disc or plate with a beveled or knurled edge rim, featuring a flat, slightly curved face and a raised perimeter that suggests it could be a lens cap, dial, or mechanical component with improved grip.
def model_38120_b4f25309_0003():
    """Model: Component7"""
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
            # Profile area: 1803.2796373145, perimeter: 150.5346479845
            with BuildLine():
                CenterArc((0, 0), 23.9583333333, 1.5122042087, 356.9755915825)
                CenterArc((0, 0), 23.9583333333, -1.5122042087, 3.0244084175)
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 2.3366861306, perimeter: 6.0681715903
            with BuildLine():
                Line((23.949989281, 0.632257502), (24.8961877014, 0.6572362627))
                CenterArc((0, 0), 23.9583333333, -1.5122042087, 3.0244084175)
                Line((23.949989281, -0.632257502), (24.8961877014, -0.6572362627))
                _nurbs_edge([(24.8961877014, -0.6572362627), (24.9306394842, -0.6564511113), (24.9996912345, -0.6548774314), (25.1031021115, -0.6453280548), (25.2066146931, -0.6331562197), (25.3101823615, -0.6180093563), (25.4137964681, -0.6004708854), (25.5174470544, -0.5807159168), (25.6211154424, -0.558893463), (25.7248302429, -0.5352747497), (25.793768786, -0.5180729593), (25.8283070903, -0.5094548388)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.1033525861, 0.2071497145, 0.311376123, 0.4160303597, 0.5211119479, 0.6266206686, 0.7325564012, 0.8389190712, 0.9457086282, 0.9457086282, 0.9457086282, 0.9457086282], 3)
                CenterArc((0.0119103525, 0), 25.8214229808, -1.1305150086, 2.2610300172)
                _nurbs_edge([(24.8961877014, 0.6572362627), (24.9306394842, 0.6564511113), (24.9996912345, 0.6548774314), (25.1031021115, 0.6453280548), (25.2066146931, 0.6331562197), (25.3101823615, 0.6180093563), (25.4137964681, 0.6004708854), (25.5174470544, 0.5807159168), (25.6211154424, 0.558893463), (25.7248302429, 0.5352747497), (25.793768786, 0.5180729593), (25.8283070903, 0.5094548388)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.1033525861, 0.2071497145, 0.311376123, 0.4160303597, 0.5211119479, 0.6266206686, 0.7325564012, 0.8389190712, 0.9457086282, 0.9457086282, 0.9457086282, 0.9457086282], 3)
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.ADD)
    return part.part


# Description: This is a knurled adjustable knob or dial featuring a circular face with a small protruding pointer/pin on the side and a textured knurled grip band around its circumference for improved grip and tactile feedback.
def model_38120_b4f25309_0004():
    """Model: Component15"""
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
            # Profile area: 99.401955055, perimeter: 35.3429173529
            with BuildLine():
                CenterArc((0, 0), 5.625, 5.6106354489, 348.7787291022)
                CenterArc((0, 0), 5.625, -5.6106354489, 11.2212708978)
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 2.2017709594, perimeter: 5.8129463399
            with BuildLine():
                Line((5.598052139, 0.5499429512), (6.6091735149, 0.6492737648))
                CenterArc((0, 0), 5.625, -5.6106354489, 11.2212708978)
                Line((5.598052139, -0.5499429512), (6.6091735149, -0.6492737648))
                _nurbs_edge([(6.6091735149, -0.6492737648), (6.6412102952, -0.6494933519), (6.7057550492, -0.6499357559), (6.8026376593, -0.6380870334), (6.9000242613, -0.6215052072), (6.9977642233, -0.5994661182), (7.0957472569, -0.5729235031), (7.1938935145, -0.5421187113), (7.2920929495, -0.5072605049), (7.3903915776, -0.46878796), (7.4552328784, -0.4403380537), (7.4878587045, -0.4260230772)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0960185923, 0.1934494159, 0.2922394742, 0.3923820559, 0.4938741797, 0.5967139793, 0.7009000752, 0.8064313507, 0.9133068528, 0.9133068528, 0.9133068528, 0.9133068528], 3)
                CenterArc((0.0196173323, 0), 7.4803826677, -3.2648782956, 6.5297565913)
                _nurbs_edge([(6.6091735149, 0.6492737648), (6.6412102952, 0.6494933519), (6.7057550492, 0.6499357559), (6.8026376593, 0.6380870334), (6.9000242613, 0.6215052072), (6.9977642233, 0.5994661182), (7.0957472569, 0.5729235031), (7.1938935145, 0.5421187113), (7.2920929495, 0.5072605049), (7.3903915776, 0.46878796), (7.4552328784, 0.4403380537), (7.4878587045, 0.4260230772)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0960185923, 0.1934494159, 0.2922394742, 0.3923820559, 0.4938741797, 0.5967139793, 0.7009000752, 0.8064313507, 0.9133068528, 0.9133068528, 0.9133068528, 0.9133068528], 3)
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.ADD)
    return part.part


# Description: This is a circular disk or plate with an eccentric cylindrical protrusion featuring a smooth, curved elliptical profile tilted in 3D space, with a small rounded knob or post extending from one edge.
def model_38197_7b9c2c15_0005():
    """Model: Motion gear"""
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
            # Profile area: 4.1424381814, perimeter: 7.2149437582
            with BuildLine():
                CenterArc((0, 0), 1.1482939633, 5.3307352527, 349.3385294947)
                CenterArc((0, 0), 1.1482939633, -5.3307352527, 10.6614705053)
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0566396131, perimeter: 0.9310686359
            with BuildLine():
                Line((1.143327597, 0.10668192), (1.2278123261, 0.1145650439))
                CenterArc((0, 0), 1.1482939633, -5.3307352527, 10.6614705053)
                Line((1.143327597, -0.10668192), (1.2278123261, -0.1145650439))
                _nurbs_edge([(1.2278123261, -0.1145650439), (1.2356789866, -0.114472024), (1.2515645864, -0.1142841836), (1.2753416896, -0.1104479586), (1.2992478766, -0.1052425051), (1.3232256903, -0.0984498642), (1.3472397741, -0.09033464), (1.3712605928, -0.0809586976), (1.3952479157, -0.0703768234), (1.4192158406, -0.058709642), (1.4349292483, -0.0501121797), (1.4428495317, -0.0457786616)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0235710746, 0.0475984255, 0.0720652147, 0.0969693663, 0.1223099618, 0.1480864233, 0.1742983216, 0.2009453092, 0.2280270908, 0.2280270908, 0.2280270908, 0.2280270908], 3)
                CenterArc((-0.0120830954, 0), 1.4556526492, -1.8021858831, 3.6043717662)
                _nurbs_edge([(1.2278123261, 0.1145650439), (1.2356789866, 0.114472024), (1.2515645864, 0.1142841836), (1.2753416896, 0.1104479586), (1.2992478766, 0.1052425051), (1.3232256903, 0.0984498642), (1.3472397741, 0.09033464), (1.3712605928, 0.0809586976), (1.3952479157, 0.0703768234), (1.4192158406, 0.058709642), (1.4349292483, 0.0501121797), (1.4428495317, 0.0457786616)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0235710746, 0.0475984255, 0.0720652147, 0.0969693663, 0.1223099618, 0.1480864233, 0.1742983216, 0.2009453092, 0.2280270908, 0.2280270908, 0.2280270908, 0.2280270908], 3)
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical knob or grip with a rounded, bulbous body featuring a textured mesh pattern on one side and a smooth dark surface, with a small protruding nub or pin on one end for attachment or rotation purposes.
def model_38197_7b9c2c15_0006():
    """Model: Motion gear (2)"""
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
            # Profile area: 4.1424381814, perimeter: 7.2149437582
            with BuildLine():
                CenterArc((0, 0), 1.1482939633, 5.3307352527, 349.3385294947)
                CenterArc((0, 0), 1.1482939633, -5.3307352527, 10.6614705053)
            make_face()
        # OneSide extrude, distance=0.9
        extrude(amount=0.9)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0566396131, perimeter: 0.9310686359
            with BuildLine():
                Line((1.143327597, 0.10668192), (1.2278123261, 0.1145650439))
                CenterArc((0, 0), 1.1482939633, -5.3307352527, 10.6614705053)
                Line((1.143327597, -0.10668192), (1.2278123261, -0.1145650439))
                _nurbs_edge([(1.2278123261, -0.1145650439), (1.2356789866, -0.114472024), (1.2515645864, -0.1142841836), (1.2753416896, -0.1104479586), (1.2992478766, -0.1052425051), (1.3232256903, -0.0984498642), (1.3472397741, -0.09033464), (1.3712605928, -0.0809586976), (1.3952479157, -0.0703768234), (1.4192158406, -0.058709642), (1.4349292483, -0.0501121797), (1.4428495317, -0.0457786616)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0235710746, 0.0475984255, 0.0720652147, 0.0969693663, 0.1223099618, 0.1480864233, 0.1742983216, 0.2009453092, 0.2280270908, 0.2280270908, 0.2280270908, 0.2280270908], 3)
                CenterArc((-0.0120830954, 0), 1.4556526492, -1.8021858831, 3.6043717662)
                _nurbs_edge([(1.2278123261, 0.1145650439), (1.2356789866, 0.114472024), (1.2515645864, 0.1142841836), (1.2753416896, 0.1104479586), (1.2992478766, 0.1052425051), (1.3232256903, 0.0984498642), (1.3472397741, 0.09033464), (1.3712605928, 0.0809586976), (1.3952479157, 0.0703768234), (1.4192158406, 0.058709642), (1.4349292483, 0.0501121797), (1.4428495317, 0.0457786616)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0235710746, 0.0475984255, 0.0720652147, 0.0969693663, 0.1223099618, 0.1480864233, 0.1742983216, 0.2009453092, 0.2280270908, 0.2280270908, 0.2280270908, 0.2280270908], 3)
            make_face()
        # OneSide extrude, distance=0.9
        extrude(amount=0.9, mode=Mode.ADD)
    return part.part


# Description: This is a hexagonal or octagonal ring-shaped component with a large central elliptical or oval hole running through its center, featuring a faceted outer geometry with flat faces and edges.
def model_38276_c9ef069a_0009():
    """Model: Piece 14"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.6650481113, perimeter: 10.0969910934
            with BuildLine():
                Line((0.5773503311, 7.2000001073), (-0.5773503311, 7.2000001073))
                Line((-0.5773503311, 7.2000001073), (-1.1547006623, 6.2))
                Line((-1.1547006623, 6.2), (-0.5773503311, 5.1999998927))
                Line((-0.5773503311, 5.1999998927), (0.5773503311, 5.1999998927))
                Line((0.5773503311, 5.1999998927), (1.1547006623, 6.2))
                Line((1.1547006623, 6.2), (0.5773503311, 7.2000001073))
            make_face()
            with BuildLine():
                CenterArc((0, 6.2), 0.5043281337, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)
    return part.part


MODELS = {
    "model_25168_05818e21_0012": {"func": model_25168_05818e21_0012, "volume": 10.1780604921, "area": 32.239347738},
    "model_25168_05818e21_0016": {"func": model_25168_05818e21_0016, "volume": 20.3561209841, "area": 44.1226618554},
    "model_25168_05818e21_0018": {"func": model_25168_05818e21_0018, "volume": 3.0534181476, "area": 23.9210278558},
    "model_25168_05818e21_0019": {"func": model_25168_05818e21_0019, "volume": 5.089030246, "area": 26.2976906793},
    "model_25199_d7aff7a5_0024": {"func": model_25199_d7aff7a5_0024, "volume": 8.9807285135, "area": 29.787916085},
    "model_25365_4fb79251_0000": {"func": model_25365_4fb79251_0000, "volume": 0.4988306326, "area": 3.6026656797},
    "model_25365_769ce017_0000": {"func": model_25365_769ce017_0000, "volume": 2.0905335614, "area": 10.2612270048},
    "model_25365_befea608_0000": {"func": model_25365_befea608_0000, "volume": 0.1036725576, "area": 4.335397862},
    "model_25365_e20900f9_0000": {"func": model_25365_e20900f9_0000, "volume": 10.7740920055, "area": 34.0234484384},
    "model_25365_eb01787e_0000": {"func": model_25365_eb01787e_0000, "volume": 0.0942477796, "area": 1.1938052084},
    "model_25416_e5f43085_0000": {"func": model_25416_e5f43085_0000, "volume": 0.4486096815, "area": 8.5953893537},
    "model_25436_61a7f978_0003": {"func": model_25436_61a7f978_0003, "volume": 0.0049893353, "area": 0.2452693437},
    "model_25438_f75175e2_0004": {"func": model_25438_f75175e2_0004, "volume": 0.6246032701, "area": 6.4826502603},
    "model_25448_3e4b4ae7_0000": {"func": model_25448_3e4b4ae7_0000, "volume": 6.9428766757, "area": 98.1613130548},
    "model_25474_5422a377_0017": {"func": model_25474_5422a377_0017, "volume": 0.4036933301, "area": 8.7407399154},
    "model_25475_70092bfb_0000": {"func": model_25475_70092bfb_0000, "volume": 704, "area": 960},
    "model_26261_5deaf75a_0000": {"func": model_26261_5deaf75a_0000, "volume": 1122.7470203888, "area": 1547.4668622367},
    "model_26566_3009b7a9_0001": {"func": model_26566_3009b7a9_0001, "volume": 3.2175924923, "area": 12.6676869774},
    "model_26768_c4df841f_0006": {"func": model_26768_c4df841f_0006, "volume": 2.3244114436, "area": 14.405716423},
    "model_26768_c4df841f_0015": {"func": model_26768_c4df841f_0015, "volume": 54.3357462052, "area": 136.0221235122},
    "model_26768_c4df841f_0018": {"func": model_26768_c4df841f_0018, "volume": 160.025514603, "area": 266.2873908831},
    "model_26777_9c5b07d6_0000": {"func": model_26777_9c5b07d6_0000, "volume": 81.4244839366, "area": 128.9573909518},
    "model_26777_9c5b07d6_0001": {"func": model_26777_9c5b07d6_0001, "volume": 1.0272444375, "area": 6.6805383451},
    "model_26942_279de65e_0011": {"func": model_26942_279de65e_0011, "volume": 4235, "area": 4043.5248658727},
    "model_26942_279de65e_0017": {"func": model_26942_279de65e_0017, "volume": 7763.0158391624, "area": 2998.4826724417},
    "model_27070_53448c4a_0003": {"func": model_27070_53448c4a_0003, "volume": 2.3276554452, "area": 16.9902828736},
    "model_27450_ee1980ca_0000": {"func": model_27450_ee1980ca_0000, "volume": 212.0575041173, "area": 296.8805057642},
    "model_27577_8520e14a_0010": {"func": model_27577_8520e14a_0010, "volume": 210278.805248, "area": 37574.1184},
    "model_27663_023746a1_0020": {"func": model_27663_023746a1_0020, "volume": 10.1902268644, "area": 88.5525261602},
    "model_27679_501db761_0024": {"func": model_27679_501db761_0024, "volume": 26.6923118443, "area": 78.2904697302},
    "model_27682_04277f62_0002": {"func": model_27682_04277f62_0002, "volume": 60.4827485834, "area": 143.8969172636},
    "model_27725_5cceaeb7_0000": {"func": model_27725_5cceaeb7_0000, "volume": 414.2948580019, "area": 572.0601288001},
    "model_27733_626709f1_0001": {"func": model_27733_626709f1_0001, "volume": 2.5569409256, "area": 18.2300966821},
    "model_27839_4a077326_0016": {"func": model_27839_4a077326_0016, "volume": 0.5285104593, "area": 5.780989638},
    "model_28119_f4fb1c4c_0004": {"func": model_28119_f4fb1c4c_0004, "volume": 19.2, "area": 107.2},
    "model_28382_90b7cc0c_0000": {"func": model_28382_90b7cc0c_0000, "volume": 480, "area": 608},
    "model_28458_00521a97_0000": {"func": model_28458_00521a97_0000, "volume": 2.0943951024, "area": 13.4247779608},
    "model_28940_05ead503_0000": {"func": model_28940_05ead503_0000, "volume": 2.8391074717, "area": 19.7179892542},
    "model_29122_80d91b52_0000": {"func": model_29122_80d91b52_0000, "volume": 25.1327412287, "area": 113.0973355292},
    "model_29592_d1e941d1_0000": {"func": model_29592_d1e941d1_0000, "volume": 0.0177327957, "area": 0.4062679226},
    "model_29746_74549e58_0008": {"func": model_29746_74549e58_0008, "volume": 0.1939896904, "area": 2.0784609691},
    "model_30274_ca0d10b2_0006": {"func": model_30274_ca0d10b2_0006, "volume": 0.0063177634, "area": 0.6985490011},
    "model_30400_8824ce97_0021": {"func": model_30400_8824ce97_0021, "volume": 0.5957799953, "area": 7.4193265824},
    "model_30400_8824ce97_0034": {"func": model_30400_8824ce97_0034, "volume": 336.6584013175, "area": 1226.6111310914},
    "model_30417_0010bc7c_0008": {"func": model_30417_0010bc7c_0008, "volume": 9.1814254658, "area": 100.0235546441},
    "model_30417_0010bc7c_0013": {"func": model_30417_0010bc7c_0013, "volume": 0.0563639425, "area": 1.2020925711},
    "model_30417_0010bc7c_0014": {"func": model_30417_0010bc7c_0014, "volume": 0.0101389169, "area": 0.3575460251},
    "model_30417_0010bc7c_0016": {"func": model_30417_0010bc7c_0016, "volume": 0.011564065, "area": 0.395376178},
    "model_30418_de83ae84_0009": {"func": model_30418_de83ae84_0009, "volume": 0.0001454838, "area": 0.0348490625},
    "model_30419_d55a0a22_0003": {"func": model_30419_d55a0a22_0003, "volume": 0.6679262263, "area": 7.6060973056},
    "model_30419_d55a0a22_0004": {"func": model_30419_d55a0a22_0004, "volume": 0.7221132495, "area": 11.4112009644},
    "model_30421_211edb5e_0003": {"func": model_30421_211edb5e_0003, "volume": 30.9829327915, "area": 147.6093697957},
    "model_30426_2cde26de_0009": {"func": model_30426_2cde26de_0009, "volume": 418.2245220091, "area": 449.2477494633},
    "model_30447_4ed3b778_0010": {"func": model_30447_4ed3b778_0010, "volume": 0.1145466981, "area": 2.1503871695},
    "model_30713_06b3d0ec_0006": {"func": model_30713_06b3d0ec_0006, "volume": 141.3716694115, "area": 202.6327261565},
    "model_30713_06b3d0ec_0011": {"func": model_30713_06b3d0ec_0011, "volume": 73.8274273594, "area": 161.7920216599},
    "model_30713_06b3d0ec_0017": {"func": model_30713_06b3d0ec_0017, "volume": 748.5667754407, "area": 747.6128183891},
    "model_31008_8fa25b35_0001": {"func": model_31008_8fa25b35_0001, "volume": 16, "area": 52},
    "model_31008_8fa25b35_0003": {"func": model_31008_8fa25b35_0003, "volume": 6.80672, "area": 38.518},
    "model_31008_8fa25b35_0004": {"func": model_31008_8fa25b35_0004, "volume": 62.4409074696, "area": 177.2968347916},
    "model_31259_72b86045_0000": {"func": model_31259_72b86045_0000, "volume": 0.3981081072, "area": 3.4082636769},
    "model_31259_72b86045_0001": {"func": model_31259_72b86045_0001, "volume": 7.6201069977, "area": 37.6190920767},
    "model_31277_b1263495_0006": {"func": model_31277_b1263495_0006, "volume": 4.9722114716, "area": 31.7625326929},
    "model_31347_386f6298_0002": {"func": model_31347_386f6298_0002, "volume": 0.0135138885, "area": 0.314158637},
    "model_31347_386f6298_0004": {"func": model_31347_386f6298_0004, "volume": 0.2062781117, "area": 32.6808636912},
    "model_31462_84375249_0003": {"func": model_31462_84375249_0003, "volume": 56, "area": 1130.8},
    "model_31462_84375249_0009": {"func": model_31462_84375249_0009, "volume": 58.9048622548, "area": 86.3937979737},
    "model_31627_68422558_0000": {"func": model_31627_68422558_0000, "volume": 1.3739322028, "area": 10.6592828265},
    "model_31627_92333106_0000": {"func": model_31627_92333106_0000, "volume": 0.7011999848, "area": 4.97583556},
    "model_31627_e8252310_0000": {"func": model_31627_e8252310_0000, "volume": 0.2916410325, "area": 3.8410927336},
    "model_31627_ec4c9f84_0000": {"func": model_31627_ec4c9f84_0000, "volume": 0.5587414274, "area": 6.210352147},
    "model_31748_5c7af877_0000": {"func": model_31748_5c7af877_0000, "volume": 24.2928411651, "area": 105.0460363168},
    "model_31831_12689eab_0000": {"func": model_31831_12689eab_0000, "volume": 1.3312291917, "area": 16.9366933106},
    "model_31962_e5291336_0004": {"func": model_31962_e5291336_0004, "volume": 5.3878314009, "area": 36.9451296062},
    "model_31962_e5291336_0024": {"func": model_31962_e5291336_0024, "volume": 0.9801769079, "area": 12.6920343205},
    "model_32049_632b3378_0002": {"func": model_32049_632b3378_0002, "volume": 10.4467533, "area": 33.06445},
    "model_32155_86984ce9_0000": {"func": model_32155_86984ce9_0000, "volume": 50, "area": 220},
    "model_32163_0baf5480_0000": {"func": model_32163_0baf5480_0000, "volume": 95.9758452238, "area": 177.7063346119},
    "model_32220_1fd19c5e_0014": {"func": model_32220_1fd19c5e_0014, "volume": 3.0748331904, "area": 45.0975620114},
    "model_32220_1fd19c5e_0021": {"func": model_32220_1fd19c5e_0021, "volume": 2.4630086404, "area": 24.6300864041},
    "model_32551_6c2e4a8d_0000": {"func": model_32551_6c2e4a8d_0000, "volume": 16.2381866282, "area": 83.002482353},
    "model_32743_f4c47bbc_0008": {"func": model_32743_f4c47bbc_0008, "volume": 1.8313094615, "area": 14.9967744409},
    "model_32871_04ff3d41_0002": {"func": model_32871_04ff3d41_0002, "volume": 121.2880418216, "area": 298.9619881875},
    "model_32871_04ff3d41_0015": {"func": model_32871_04ff3d41_0015, "volume": 7.6048142105, "area": 37.2453096491},
    "model_32879_49552f2f_0011": {"func": model_32879_49552f2f_0011, "volume": 2.4484716792, "area": 15.2339269881},
    "model_33147_d7173b68_0006": {"func": model_33147_d7173b68_0006, "volume": 1.4870928279, "area": 16.8363030695},
    "model_33147_d7173b68_0012": {"func": model_33147_d7173b68_0012, "volume": 0.4371258559, "area": 3.7365320534},
    "model_33165_cec42ec5_0000": {"func": model_33165_cec42ec5_0000, "volume": 172.2369556193, "area": 346.2303263368},
    "model_33607_c6f31fa6_0004": {"func": model_33607_c6f31fa6_0004, "volume": 154.4444396289, "area": 253.3537395487},
    "model_33628_296ae2b8_0001": {"func": model_33628_296ae2b8_0001, "volume": 0.9200000206, "area": 11.4400002146},
    "model_34063_0ca1585e_0009": {"func": model_34063_0ca1585e_0009, "volume": 1.3213453778, "area": 11.4839952746},
    "model_34180_21cf3c28_0000": {"func": model_34180_21cf3c28_0000, "volume": 24.9748860469, "area": 171.6657932127},
    "model_34226_dbed877f_0006": {"func": model_34226_dbed877f_0006, "volume": 0.3785619148, "area": 5.6077428867},
    "model_34234_04351713_0003": {"func": model_34234_04351713_0003, "volume": 0.8482300165, "area": 6.2203534541},
    "model_34343_6d3253e1_0015": {"func": model_34343_6d3253e1_0015, "volume": 398.6655179316, "area": 459.1883376215},
    "model_34343_6d3253e1_0019": {"func": model_34343_6d3253e1_0019, "volume": 413.4138755316, "area": 467.8979976215},
    "model_34343_6d3253e1_0027": {"func": model_34343_6d3253e1_0027, "volume": 653.2859206904, "area": 629.7870264284},
    "model_34343_6d3253e1_0028": {"func": model_34343_6d3253e1_0028, "volume": 618.9711564684, "area": 608.7052421027},
    "model_34436_ffc43a58_0000": {"func": model_34436_ffc43a58_0000, "volume": 0.0097001042, "area": 0.393800591},
    "model_34770_6bba5bd4_0003": {"func": model_34770_6bba5bd4_0003, "volume": 5.1280380346, "area": 63.8134731488},
    "model_34770_6bba5bd4_0008": {"func": model_34770_6bba5bd4_0008, "volume": 8.1105428865, "area": 37.2938511053},
    "model_34781_4f8a4759_0017": {"func": model_34781_4f8a4759_0017, "volume": 0.4382521752, "area": 17.5457949703},
    "model_34785_dc3b83fa_0011": {"func": model_34785_dc3b83fa_0011, "volume": 127190.5535576423, "area": 25511.4793062565},
    "model_35145_a3d7363c_0006": {"func": model_35145_a3d7363c_0006, "volume": 21.8240000551, "area": 226.72},
    "model_35166_562b126c_0005": {"func": model_35166_562b126c_0005, "volume": 1.0526459106, "area": 7.9945993211},
    "model_35941_9352b107_0000": {"func": model_35941_9352b107_0000, "volume": 0.8266358221, "area": 14.0244420524},
    "model_35968_5488b3e5_0001": {"func": model_35968_5488b3e5_0001, "volume": 13.7994457309, "area": 70.7486665588},
    "model_35968_5488b3e5_0006": {"func": model_35968_5488b3e5_0006, "volume": 7.3826937656, "area": 22.2811024698},
    "model_35968_5488b3e5_0008": {"func": model_35968_5488b3e5_0008, "volume": 127.1160361309, "area": 1298.2592900375},
    "model_36268_3c96c142_0009": {"func": model_36268_3c96c142_0009, "volume": 18.0513751875, "area": 208.87055},
    "model_36344_ecda4926_0000": {"func": model_36344_ecda4926_0000, "volume": 14.8468198271, "area": 64.8235525452},
    "model_36436_362a4413_0030": {"func": model_36436_362a4413_0030, "volume": 0.0565486678, "area": 0.8953539063},
    "model_36445_67816b83_0006": {"func": model_36445_67816b83_0006, "volume": 0.0212, "area": 0.61},
    "model_36445_67816b83_0007": {"func": model_36445_67816b83_0007, "volume": 0.0001914348, "area": 0.0541017508},
    "model_36451_1a7f9437_0008": {"func": model_36451_1a7f9437_0008, "volume": 58.0096438932, "area": 402.8601588775},
    "model_36658_c1f72bb7_0000": {"func": model_36658_c1f72bb7_0000, "volume": 30.5803443937, "area": 81.1895056736},
    "model_36658_c1f72bb7_0002": {"func": model_36658_c1f72bb7_0002, "volume": 130.7960448251, "area": 188.9712924419},
    "model_36658_c1f72bb7_0003": {"func": model_36658_c1f72bb7_0003, "volume": 5276.7508247614, "area": 1873.8109155493},
    "model_36847_d0238124_0000": {"func": model_36847_d0238124_0000, "volume": 643.944513531, "area": 691.4221632613},
    "model_36953_bdaf025b_0002": {"func": model_36953_bdaf025b_0002, "volume": 15.246115661, "area": 152.82115661},
    "model_36953_bdaf025b_0003": {"func": model_36953_bdaf025b_0003, "volume": 5.32, "area": 64.24},
    "model_37040_ecbcd25e_0002": {"func": model_37040_ecbcd25e_0002, "volume": 363.2712640027, "area": 799.1967808059},
    "model_37040_ecbcd25e_0023": {"func": model_37040_ecbcd25e_0023, "volume": 145.3085056011, "area": 435.9255168032},
    "model_37040_ecbcd25e_0032": {"func": model_37040_ecbcd25e_0032, "volume": 0.0653650469, "area": 1.8502931766},
    "model_37117_89aac9d4_0005": {"func": model_37117_89aac9d4_0005, "volume": 11.61433161, "area": 80.903064},
    "model_37267_b2be4b50_0024": {"func": model_37267_b2be4b50_0024, "volume": 356.2831589309, "area": 639.5258023697},
    "model_37377_90529181_0004": {"func": model_37377_90529181_0004, "volume": 233.5577788403, "area": 285.0995333133},
    "model_37524_6004c446_0001": {"func": model_37524_6004c446_0001, "volume": 221.9536686266, "area": 298.2634602401},
    "model_37524_6004c446_0002": {"func": model_37524_6004c446_0002, "volume": 289.8986692266, "area": 377.1098620085},
    "model_37596_8efba003_0001": {"func": model_37596_8efba003_0001, "volume": 1.2737878501, "area": 6.9989839325},
    "model_37615_8399c412_0009": {"func": model_37615_8399c412_0009, "volume": 0.4251037227, "area": 4.6639974011},
    "model_37840_de7298de_0000": {"func": model_37840_de7298de_0000, "volume": 205.358589712, "area": 336.7484554627},
    "model_37840_de7298de_0002": {"func": model_37840_de7298de_0002, "volume": 9.4656151889, "area": 26.6561764612},
    "model_37840_de7298de_0003": {"func": model_37840_de7298de_0003, "volume": 18.931149011, "area": 40.691586836},
    "model_37840_de7298de_0004": {"func": model_37840_de7298de_0004, "volume": 57.8134840253, "area": 110.8046951813},
    "model_38120_b4f25309_0003": {"func": model_38120_b4f25309_0003, "volume": 5416.853296406, "area": 4073.4531228948},
    "model_38120_b4f25309_0004": {"func": model_38120_b4f25309_0004, "volume": 304.8126554925, "area": 320.0651358838},
    "model_38197_7b9c2c15_0005": {"func": model_38197_7b9c2c15_0005, "volume": 0.4199096532, "area": 9.1700221496},
    "model_38197_7b9c2c15_0006": {"func": model_38197_7b9c2c15_0006, "volume": 3.7791868788, "area": 15.3449546348},
    "model_38276_c9ef069a_0009": {"func": model_38276_c9ef069a_0009, "volume": 1.5990288668, "area": 11.3882908787},
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
