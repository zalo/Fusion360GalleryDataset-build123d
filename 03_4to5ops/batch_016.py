"""Batch 016 - passing/03_4to5ops
50 models bundled from Fusion360 Gallery reconstructions.
"""

from build123d import *
from build123d import Edge, BuildLine
from collections import Counter
from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
from OCP.Geom import Geom_BSplineCurve
from OCP.TColStd import TColStd_Array1OfReal, TColStd_Array1OfInteger
from OCP.TColgp import TColgp_Array1OfPnt
from OCP.gp import gp_Pnt


# Description: This is a rectangular storage or display box with a hinged lid that opens upward, featuring a flat base and internal compartment with a light blue interior surface.
def model_87358_854d47fe_0004():
    """Model: угольник 10 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 20.64, perimeter: 29.2
            with BuildLine():
                Line((0, 0), (0, 5.8))
                Line((0, 5.8), (-0.8, 5.8))
                Line((-0.8, 5.8), (-0.8, 2))
                Line((-0.8, 2), (-8.8, 2))
                Line((-8.8, 0), (-8.8, 2))
                Line((0, 0), (-8.8, 0))
            make_face()
        # OneSide extrude, distance=29
        extrude(amount=29)
    return part.part


# Description: This is a thin-walled, wedge-shaped structural component with a tapered triangular profile, featuring a pointed leading edge and a rectangular base, likely designed as an aerodynamic or hydrodynamic element such as a fin, strut, or blade.
def model_87373_a5e91136_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch12 -> Extrude3 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 37.5, perimeter: 25.8309518948
            with BuildLine():
                Line((15, -4), (10, -4))
                Line((15, 2), (15, -4))
                Line((10, 5), (15, 2))
                Line((10, -4), (10, 5))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a U-shaped metal bracket or channel with two parallel vertical arms connected by a curved or angled base, featuring hexagonal head openings at each end for bolt attachment.
def model_87757_eb92dadf_0000():
    """Model: partV"""
    with BuildPart() as part:
        # Sketch1 -> 押し出し1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 19 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(3.4156152415, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0120925597, perimeter: 0.4415525766
            with BuildLine():
                Line((2.7828913942, 0.9232663918), (2.681348733, 0.9232663918))
                Line((2.7828913942, 0.9232663918), (2.7828913942, 1.0432663918))
                Line((2.7828913942, 1.0432663918), (2.6828913942, 1.0432663918))
                Line((2.6828913942, 1.0432663918), (2.681348733, 0.9232663918))
            make_face()
            # Profile area: 0.0120925597, perimeter: 0.4415525766
            with BuildLine():
                Line((2.1733407631, 0.9232663918), (2.071798102, 0.9232663918))
                Line((2.171798102, 1.0432663918), (2.1733407631, 0.9232663918))
                Line((2.071798102, 1.0432663918), (2.171798102, 1.0432663918))
                Line((2.071798102, 0.9232663918), (2.071798102, 1.0432663918))
            make_face()
            # Profile area: 0.215919983, perimeter: 4.5214849823
            with BuildLine():
                Line((2.243434785, -0.0501336082), (2.071798102, 0.9232663918))
                Line((2.6112547112, -0.0501336082), (2.243434785, -0.0501336082))
                Line((2.6112547112, -0.0501336082), (2.7828913942, 0.9232663918))
                Line((2.7828913942, 0.9232663918), (2.681348733, 0.9232663918))
                Line((2.681348733, 0.9232663918), (2.5273447481, 0.0498663918))
                Line((2.3273447481, 0.0498663918), (2.5273447481, 0.0498663918))
                Line((2.1733407631, 0.9232663918), (2.3273447481, 0.0498663918))
                Line((2.1733407631, 0.9232663918), (2.071798102, 0.9232663918))
            make_face()
        # OneSide extrude, distance=0.08
        extrude(amount=0.08)

        # Sketch2 -> 押し出し2 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(3.4156152415, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0120925597, perimeter: 0.4415525766
            with BuildLine():
                Line((-2.071798102, 0.9232663918), (-2.1733407631, 0.9232663918))
                Line((-2.071798102, 0.9232663918), (-2.071798102, 1.0432663918))
                Line((-2.071798102, 1.0432663918), (-2.171798102, 1.0432663918))
                Line((-2.171798102, 1.0432663918), (-2.1733407631, 0.9232663918))
            make_face()
            # Profile area: 0.0120925597, perimeter: 0.4415525766
            with BuildLine():
                Line((-2.681348733, 0.9232663918), (-2.7828913942, 0.9232663918))
                Line((-2.681348733, 0.9232663918), (-2.6828913942, 1.0432663918))
                Line((-2.6828913942, 1.0432663918), (-2.7828913942, 1.0432663918))
                Line((-2.7828913942, 1.0432663918), (-2.7828913942, 0.9232663918))
            make_face()
        # OneSide extrude, distance=0.18
        extrude(amount=0.18, mode=Mode.ADD)
    return part.part


# Description: This is a hexagonal prism or column with a elongated rectangular slot or opening cut along one side, featuring angled top surfaces that form a peaked roof-like profile.
def model_87951_500b1dcd_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch7 -> 拉伸1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 21 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3578.5398163397, perimeter: 231.4159265359
            with BuildLine():
                CenterArc((-25, -25), 5, 180, 90)
                Line((25, -30), (-25, -30))
                CenterArc((25, -25), 5, -90, 90)
                Line((30, 25), (30, -25))
                CenterArc((25, 25), 5, 0, 90)
                Line((-25, 30), (25, 30))
                CenterArc((-25, 25), 5, 90, 90)
                Line((-30, -25), (-30, 25))
            make_face()
        # OneSide extrude, distance=200
        extrude(amount=200)
    return part.part


# Description: This is a cylindrical ring or collar component with an elliptical or oval cross-section, featuring a hollow center cavity and mesh or perforated sections on the upper portions, likely designed for ventilation, filtration, or structural lightweighting.
def model_88060_389bdff4_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 572.5552611167, perimeter: 84.8230016469
            Circle(13.5)
        # OneSide extrude, distance=6
        extrude(amount=6)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 176.7145867644, perimeter: 47.1238898038
            Circle(7.5)
        # OneSide extrude, distance=-6
        extrude(amount=-6, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a dark blue plastic or metal bracket or mount with an elongated rectangular body, featuring a central slot or channel running lengthwise and a raised flange or extension on the right end.
def model_88219_05eb53c9_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 13 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 32.1240244336, perimeter: 46.405756381
            with BuildLine():
                Line((12, 1.0278882225), (10, 1.0278882225))
                CenterArc((12, 1.3278882225), 0.3, -90, 90)
                Line((12.3, 4.7278882225), (12.3, 1.3278882225))
                CenterArc((12, 4.7278882225), 0.3, 0, 90)
                Line((10, 5.0278882225), (12, 5.0278882225))
                CenterArc((9.5, 5.0278882225), 0.5, -90, 90)
                Line((9.5, 4.5278882225), (1, 4.5278882225))
                Line((1, 1.5278882225), (1, 4.5278882225))
                Line((9.5, 1.5278882225), (1, 1.5278882225))
                CenterArc((9.5, 1.0278882225), 0.5, 0, 90)
            make_face()
            with BuildLine():
                Line((3.0102555766, 3.3026969254), (8.9999912172, 3.3028882224))
                CenterArc((9, 3.0278882225), 0.275, -90.0018298825, 180.0036597649)
                Line((3.0102555766, 2.7530795197), (8.9999912172, 2.7528882227))
                CenterArc((3, 3.0278882225), 0.275, 87.8627725718, 184.2744548564)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((11, 3.0278882225), 0.44, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5278882225, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.3117691454, perimeter: 2.8392304845
            with BuildLine():
                Line((1, 0.2), (2.0392304845, 0.8))
                Line((1, 0.8), (2.0392304845, 0.8))
                Line((1, 0.2), (1, 0.8))
            make_face()
        # OneSide extrude, distance=-4.9
        extrude(amount=-4.9, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a toothed drive belt or pulley ring with a circular profile, featuring evenly-spaced internal teeth around its inner circumference for power transmission, and a smooth outer diameter surface.
def model_88317_a9fa6cf2_0000():
    """Model: ELICHE v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude3 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 177.7969938993, perimeter: 402.8610561314
            with BuildLine():
                CenterArc((0, 0), 32.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 31.6173284625, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=6.2252
        extrude(amount=6.2252)

        # Sketch2 -> Extrude4 (NewBody)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.5468669595, perimeter: 9.0703007985
            with Locations((0, -2.9107577085)):
                Circle(1.4435832074)
        # OneSide extrude, distance=-3.6073
        extrude(amount=-3.6073)
    return part.part


# Description: This is a cylindrical sleeve or tube with a closed bottom and open top, featuring vertical ribbed or fluted patterns running along its curved surface for structural reinforcement.
def model_89527_b3bf425d_0004():
    """Model: bush1 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3455751919, perimeter: 6.9115038379
            with BuildLine():
                CenterArc((0, 0), 0.6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.3
        extrude(amount=2.3)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((0, 1.15)):
                Circle(0.2)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical flashlight or torch body with a textured grip section on the lower half and a flat, perforated mesh lens cap on the top end.
def model_89527_b3bf425d_0018():
    """Model: m3*5 v1 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical dome or cover with an oval footprint, featuring multiple rectangular slots or openings distributed across its curved surface for ventilation or access.
def model_89527_b3bf425d_0027():
    """Model: 10 v0"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.9087385212, perimeter: 7.853981634
            Circle(1.25)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((0, -0.8)):
                Circle(0.25)
            # Profile area: 0.0314159275, perimeter: 0.6283185401
            with Locations((-0.86, 0.4)):
                Circle(0.1000000015)
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((0, 0.95)):
                Circle(0.1)
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((0.86, 0.4)):
                Circle(0.1)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical rod or shaft with a slightly tapered design, featuring rounded ends and a smooth, uniform surface with no holes or protrusions.
def model_89527_b3bf425d_0032():
    """Model: 09 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=-5.2
        extrude(amount=-5.2)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on XY construction plane
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((0, -1.7)):
                Circle(0.15)
        # TwoSides extrude (symmetric), distance=0.8
        extrude(amount=0.8, both=True, mode=Mode.SUBTRACT)
    return part.part


# Description: This is an elliptical or oblong bowl-shaped component with a curved, streamlined form featuring a recessed center cavity, reinforced rim flanges on the sides, and a dark base section with light blue upper surfaces.
def model_89824_94d89a7c_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4212291057, perimeter: 2.3544101917
            with BuildLine():
                Line((0.3388415118, -2.1561028978), (0.3388415118, -1.8792492732))
                CenterArc((0.1356415118, -1.8792492732), 0.2032, 0, 90)
                Line((0.1356415118, -1.6760492732), (-0.1263383323, -1.6760492732))
                CenterArc((-0.1263383323, -1.8792492732), 0.2032, 90, 90)
                Line((-0.3295383323, -1.8792492732), (-0.3295383323, -2.1561028978))
                CenterArc((-0.1263383323, -2.1561028978), 0.2032, 180, 90)
                Line((-0.1263383323, -2.3593028978), (0.1356415118, -2.3593028978))
                CenterArc((0.1356415118, -2.1561028978), 0.2032, -90, 90)
            make_face()
        # OneSide extrude, distance=-0.127
        extrude(amount=-0.127)
    return part.part


# Description: This is a round mirror or reflective disc featuring a circular flat face with a small mounting bracket or tab protruding from the edge.
def model_89934_c31d503d_0000():
    """Model: Spur Gear (30 teeth)"""
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
            # Profile area: 963.1476305118, perimeter: 114.0770097823
            with BuildLine():
                CenterArc((0, 0), 17.52092, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.635, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 5.4822937629, perimeter: 9.2185109945
            with BuildLine():
                _nurbs_edge([(17.8606629998, -1.2031994705), (17.9509086818, -1.2007835147), (18.1328017491, -1.1959140782), (18.4045894821, -1.1521961422), (18.6773902334, -1.0946271662), (18.950683809, -1.0210934605), (19.2242325788, -0.9343716916), (19.4978187509, -0.8351607162), (19.7711299757, -0.7240721561), (20.0443455408, -0.6023697611), (20.2241168539, -0.5131277117), (20.3146051329, -0.4682075333)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.2705518054, 0.5453058436, 0.8241182245, 1.1069754237, 1.3938730688, 1.6848091924, 1.9797827401, 2.2787930809, 2.5818398071, 2.5818398071, 2.5818398071, 2.5818398071], 3)
                CenterArc((0, 0), 20.32, -1.320309544, 2.6406190879)
                _nurbs_edge([(17.8606629998, 1.2031994705), (17.9509086818, 1.2007835147), (18.1328017491, 1.1959140782), (18.4045894821, 1.1521961422), (18.6773902334, 1.0946271662), (18.950683809, 1.0210934605), (19.2242325788, 0.9343716916), (19.4978187509, 0.8351607162), (19.7711299757, 0.7240721561), (20.0443455408, 0.6023697611), (20.2241168539, 0.5131277117), (20.3146051329, 0.4682075333)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.2705518054, 0.5453058436, 0.8241182245, 1.1069754237, 1.3938730688, 1.6848091924, 1.9797827401, 2.2787930809, 2.5818398071, 2.5818398071, 2.5818398071, 2.5818398071], 3)
                Line((17.4803006701, 1.177643237), (17.8606629998, 1.2031994705))
                Line((17.4803006701, -1.177643237), (17.4803006701, 1.177643237))
                Line((17.4803006701, -1.177643237), (17.8606629998, -1.2031994705))
            make_face()
        # OneSide extrude, distance=1.27
        extrude(amount=1.27, mode=Mode.ADD)
    return part.part


# Description: This is an electric motor rotor consisting of a cylindrical core with axial copper or aluminum windings (shown in blue) and a large radial cooling fan blade attached to one end for air circulation.
def model_90628_b8795213_0011():
    """Model: Pole piece (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.2548321522, perimeter: 9.1639096089
            with BuildLine():
                CenterArc((0, 0), 0.9752964516, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.4831850607, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.7334607343, perimeter: 3.0359412738
            Circle(0.4831850607)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.7334607343, perimeter: 3.0359412738
            Circle(0.4831850607)
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-2, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0497908663, perimeter: 0.7910059915
            Circle(0.1258925136)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a rectangular base plate or chassis component with a trapezoidal profile, featuring multiple internal ribs and mounting bosses, with a sloped top surface and recessed central cavity for structural support and component mounting.
def model_90721_92ea8254_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrusion1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 25.327, perimeter: 28.6
            with BuildLine():
                Line((0, 2), (0, -2))
                Line((0, -2), (7, -2))
                Line((7, -2), (7, -0.405))
                Line((7, -0.405), (3.7, -0.405))
                Line((3.7, -0.405), (3.7, 0.405))
                Line((7, 0.405), (3.7, 0.405))
                Line((7, 2), (7, 0.405))
                Line((0, 2), (7, 2))
            make_face()
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)

        # Sketch2 -> Extrusion2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((6.6, 0.3)):
                Circle(0.15)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((4.6, 0.3)):
                Circle(0.15)
        # OneSide extrude, distance=-4
        extrude(amount=-4, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a dual-chamber air intake or plenum component with two symmetrical curved cylindrical sections connected by a central bridge, featuring internal ribbing/bracing and multiple port openings for fluid or air flow distribution.
def model_90917_39defb9c_0000():
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
        # Sketch has 43 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 20.6837536801, perimeter: 75.7203719112
            with BuildLine():
                CenterArc((-4.7970332319, 2.399999994), 0.4, 90, 90)
                Line((-5.1970332319, 2.399999994), (-5.1970332319, -2.400000006))
                CenterArc((-4.7970332319, -2.400000006), 0.4, 180, 90)
                Line((-4.7970332319, -2.800000006), (0.8, -2.8059334827))
                CenterArc((0.8, -2.4), 0.4059334827, -90, 90)
                Line((1.2059334827, -2.4), (1.2000000536, 2.3999999881))
                CenterArc((0.8, 2.3999999881), 0.4000000536, 0, 89.9999982925)
                Line((-4.7970332319, 2.799999994), (0.8000000119, 2.8000000417))
            make_face()
            with BuildLine():
                Line((0.9999999911, -2.4), (0.9999999911, 2.3999999881))
                CenterArc((0.8, -2.4), 0.1999999911, 180, 180)
                Line((0.6000000089, -2.4), (0.6000000089, 2.3999999881))
                CenterArc((0.8, 2.3999999881), 0.1999999911, 0, 180)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-1, -0.8), (-1, -2.4))
                Line((-1, -0.8), (-0.9999999911, 0.8000000119))
                Line((-0.9999999911, 2.3999999881), (-0.9999999911, 0.8000000119))
                CenterArc((-0.8, 2.3999999881), 0.1999999911, 0, 180)
                Line((-0.6000000089, 0.8000000119), (-0.6000000089, 2.3999999881))
                Line((-0.6, -0.8), (-0.6000000089, 0.8000000119))
                Line((-0.6, -2.4), (-0.6, -0.8))
                CenterArc((-0.8, -2.4), 0.2, 180, 180)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-4.4536974739, 2.2446589576), (-3.2835696323, 0.4835614491))
                CenterArc((-4.3704066023, 2.2999999977), 0.1, 90.0000004881, 123.6012962845)
                Line((-2.0274579088, 2.4000000176), (-4.3704066032, 2.3999999977))
                CenterArc((-2.0274579079, 2.3000000176), 0.1, -33.6620352505, 123.6620357387)
                Line((-3.1170466023, 0.4834731847), (-1.9442257494, 2.2445707132))
                CenterArc((-3.2002787608, 0.5389024892), 0.1, -146.3987032273, 112.7366679768)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-1.784390612, 1.7629378158), (-2.9234876016, 0.0524797453))
                CenterArc((-1.7011584535, 1.7075085114), 0.1, -0.0607398654, 146.3987046148)
                Line((-1.6047834502, -1.711994479), (-1.6011585097, 1.7074025003))
                CenterArc((-1.704783394, -1.7118884679), 0.1, -146.3987032273, 146.3379633619)
                Line((-2.9235463146, -0.0582905992), (-1.7880742655, -1.767229508))
                CenterArc((-2.8402554431, -0.0029495592), 0.1, 146.3379647495, 67.2633320232)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-3.1175620968, -0.4890786072), (-1.9491528918, -2.2475894868))
                CenterArc((-2.0324437633, -2.3029305269), 0.1, -90.0607358303, 123.6620326029)
                Line((-4.3704068219, -2.4004522473), (-2.0325497673, -2.4029304707))
                CenterArc((-4.3703008179, -2.3004523035), 0.1, 146.3379647495, 123.6012994203)
                Line((-3.2840851269, -0.4889903428), (-4.4535329764, -2.245022999))
                CenterArc((-3.2008529684, -0.5444196473), 0.1, 33.6012967727, 112.7366679768)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-3.4775854145, 0.0527734411), (-4.6137423603, 1.7627431516))
                CenterArc((-3.560876286, -0.0025675989), 0.1, -33.6620352505, 67.2633320232)
                Line((-3.4776441276, -0.0579969034), (-4.6138010734, -1.7640402299))
                CenterArc((-4.6970332319, -1.7086109254), 0.1, 180, 146.3379647495)
                Line((-4.7970332319, 1.7074021116), (-4.7970332319, -1.7086109254))
                CenterArc((-4.6970332319, 1.7074021116), 0.1, 33.6012967727, 146.3987032273)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)

        # Sketch1 -> Extrude5 (Join)
        # Sketch on XZ construction plane
        # Sketch has 43 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1719153653, perimeter: 10.1862687264
            with BuildLine():
                _nurbs_edge([(1.2059334827, -2.4), (1.2816676926, -2.3039616747), (1.4265112669, -2.1118883713), (1.6239026978, -1.8237884578), (1.8442262481, -1.4439136576), (2.0082802984, -1.0640672882), (2.0966812326, -0.7802592033), (2.1394122991, -0.5924742532), (2.1564571613, -0.5007023412)], [1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.3955867113, 0.3955867113, 0.3955867113, 0.3955867113, 0.3955867113, 0.3955867113], 5)
                Line((2.2029661717, -0.50064485), (2.1564571613, -0.5007023412))
                Line((2.2029661717, -0.50064485), (2.2029656701, -0.0066217456))
                Line((2.2029656701, -0.0066217456), (2.2029656691, 0.0008784854))
                Line((2.2029656691, 0.0008784854), (2.2029661717, 0.5000000075))
                Line((2.2029661717, 0.5000000075), (2.1555050652, 0.4999413392))
                _nurbs_edge([(2.1555050652, 0.4999413392), (2.1382205269, 0.5920407126), (2.0950223634, 0.7801270526), (2.0058838288, 1.0641902404), (1.8407896637, 1.4442151105), (1.6193417811, 1.8242115071), (1.4212601929, 2.1121116032), (1.2759609727, 2.3040383085), (1.2000000536, 2.3999999881)], [1, 1, 1, 1, 1, 1, 1, 1, 1], [0.6040541152, 0.6040541152, 0.6040541152, 0.6040541152, 0.6040541152, 0.6040541152, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                Line((1.2059334827, -2.4), (1.2000000536, 2.3999999881))
            make_face()
            # Profile area: 3.1718859862, perimeter: 10.1861545061
            with BuildLine():
                _nurbs_edge([(-5.1970332319, 2.399999994), (-5.272880841, 2.303999994), (-5.4179523239, 2.111999994), (-5.6156889504, 1.823999994), (-5.8366120007, 1.4439999967), (-6.0012043361, 1.0639999994), (-6.0899785321, 0.7800000021), (-6.1329414765, 0.5920000048), (-6.1501072407, 0.5000000075)], [1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.3958333305, 0.3958333305, 0.3958333305, 0.3958333305, 0.3958333305, 0.3958333305], 5)
                Line((-6.1970332319, 0.5000000075), (-6.1501072407, 0.5000000075))
                Line((-6.1970332319, -0.5000000075), (-6.1970332319, 0.5000000075))
                Line((-6.1970332319, -0.5000000075), (-6.1501072429, -0.5000000075))
                _nurbs_edge([(-6.1501072429, -0.5000000075), (-6.1329414787, -0.5920000072), (-6.0899785343, -0.7800000069), (-6.0012043382, -1.0640000066), (-5.8366120021, -1.4440000063), (-5.6156889504, -1.824000006), (-5.4179523239, -2.112000006), (-5.272880841, -2.304000006), (-5.1970332319, -2.400000006)], [1, 1, 1, 1, 1, 1, 1, 1, 1], [0.604166667, 0.604166667, 0.604166667, 0.604166667, 0.604166667, 0.604166667, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                Line((-5.1970332319, 2.399999994), (-5.1970332319, -2.400000006))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5, mode=Mode.ADD)

        # Sketch3 -> Extrude6 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 14 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 13.2710454052, perimeter: 25.7767608605
            with BuildLine():
                _nurbs_edge([(-2.8006036078, 0.7978845763), (-2.6886404968, 1.1013420858), (-2.4647110564, 1.6817658366), (-2.1288072406, 2.4729301052), (-1.680915856, 3.366237026), (-1.1210166872, 4.1952942392), (-0.5610794574, 4.7110673283), (-0.0011010589, 4.8879785552), (0.5589202072, 4.7120438191), (1.118982648, 4.1971963952), (1.6790831582, 3.368996827), (2.1271915241, 2.4763154132), (2.4632875253, 1.6855867792), (2.6873579646, 1.1054387467), (2.799394794, 0.8021154237)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                Line((2.7956172517, 5.8021139967), (2.799394794, 0.8021154237))
                Line((-2.8043811501, 5.7978831494), (2.7956172517, 5.8021139967))
                Line((-2.8006036078, 0.7978845763), (-2.8043811501, 5.7978831494))
            make_face()
            # Profile area: 0.2228318531, perimeter: 2.6283185307
            with BuildLine():
                Line((-0.0006044069, 1.8), (-0.0006044069, 3))
                CenterArc((-0.0006044069, 2), 0.2, -90, 90)
                Line((0.1993955931, 2), (0.1993955931, 2.8))
                CenterArc((-0.0006044069, 2.8), 0.2, 0, 90)
            make_face()
            # Profile area: 0.2228318531, perimeter: 2.6283185307
            with BuildLine():
                Line((-0.0006044069, 1.8), (-0.0006044069, 3))
                CenterArc((-0.0006044069, 2.8), 0.2, 90, 90)
                Line((-0.2006044069, 2.8), (-0.2006044069, 2))
                CenterArc((-0.0006044069, 2), 0.2, 180, 90)
            make_face()
            # Profile area: 0.2228318531, perimeter: 2.6283185307
            with BuildLine():
                Line((-0.0006044069, 3.4), (-0.0006044069, 4.6))
                CenterArc((-0.0006044069, 4.4), 0.2, 90, 90)
                Line((-0.2006044069, 4.4), (-0.2006044069, 3.6))
                CenterArc((-0.0006044069, 3.6), 0.2, 180, 90)
            make_face()
            # Profile area: 0.2228318531, perimeter: 2.6283185307
            with BuildLine():
                CenterArc((-0.0006044069, 3.6), 0.2, -90, 90)
                Line((0.1993955931, 3.6), (0.1993955931, 4.4))
                CenterArc((-0.0006044069, 4.4), 0.2, 0, 90)
                Line((-0.0006044069, 3.4), (-0.0006044069, 4.6))
            make_face()
        # Symmetric extrude, each_side=7
        extrude(amount=7, both=True, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a dark gray/charcoal plastic or metal enclosure housing with an irregular polygonal shape featuring multiple internal compartments, ventilation slots, and mounting features visible through transparent or cutaway sections on its sides.
def model_90917_3d2d21a9_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.9773316292, perimeter: 24.3401921039
            with BuildLine():
                Line((0.6069703162, -0.7501342148), (-0.5930248268, -0.7467200091))
                Line((-0.5930248268, -0.7467200091), (-0.5930248268, -1.6834637583))
                Line((-0.8069703043, -1.8498657942), (-0.5930248268, -1.6834637583))
                CenterArc((-0.5, -2.2445419048), 0.5, 127.8749832899, 52.1250167101)
                Line((-1, -2.2445419048), (-1, -3.2))
                Line((-1, -3.2), (1, -3.2))
                Line((1, -3.2), (1.0000000035, -2.9184315072))
                CenterArc((1.5000000035, -2.9184315134), 0.5, 115.0168935326, 64.9831057559)
                Line((1.2885572704, -2.4653399436), (3.7114427331, -1.3346600582))
                CenterArc((3.5, -0.8815684884), 0.5, -64.9831064674, 64.9831064674)
                Line((4, -0.8815684884), (4, 0))
                Line((4, 0), (0.8000000119, 0))
                Line((0.8000000119, 0), (0.8000000119, -0.3554581042))
                CenterArc((0.3000000119, -0.3554581042), 0.5, -52.1250167101, 52.1250167101)
            make_face()
            with BuildLine():
                CenterArc((1.2000000039, -1.6000000027), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((2.85, -0.75), (3.55, -0.75))
                CenterArc((2.85, -0.6), 0.15, 90, 180)
                Line((3.55, -0.45), (2.85, -0.45))
                CenterArc((3.55, -0.6), 0.15, -90, 180)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((1.95, -0.45), (1.25, -0.45))
                CenterArc((1.95, -0.6), 0.15, -90, 180)
                Line((1.25, -0.75), (1.95, -0.75))
                CenterArc((1.25, -0.6), 0.15, 90, 180)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((0.3500000047, -2.4500000022), (-0.3499999953, -2.4499999978))
                CenterArc((0.3500000037, -2.6000000022), 0.15, -90.0000003557, 180)
                Line((-0.3499999972, -2.7499999978), (0.3500000028, -2.7500000022))
                CenterArc((-0.3499999963, -2.5999999978), 0.15, 89.9999996443, 180)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.4
        extrude(amount=2.4)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((3.2, 2)):
                Circle(0.2)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((1.6, 2)):
                Circle(0.2)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((3.2, 0.4)):
                Circle(0.2)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((1.6, 0.4)):
                Circle(0.2)
        # OneSide extrude, distance=0.75
        extrude(amount=0.75, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((0, 0.4)):
                Circle(0.2)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((0, 2)):
                Circle(0.2)
        # OneSide extrude, distance=10
        extrude(amount=10, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a VR headset mount or controller holder featuring an ergonomic arm-like shape with a curved ring at the top for device placement, a textured grip surface, and a flanged base for stable mounting or hand-holding.
def model_90917_4670b560_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.937345179, perimeter: 16.7964594479
            with BuildLine():
                CenterArc((-2, 0.8), 0.4, 90, 90)
                Line((-2.4, 0.8), (-2.4, -0.8))
                CenterArc((-2, -0.8), 0.4, 180, 90)
                Line((-0.4, -1.2), (-2, -1.2))
                Line((0, -1.2000000179), (-0.4, -1.2))
                Line((0, 1.2), (0, -1.2000000179))
                Line((-2, 1.2), (0, 1.2))
            make_face()
            with BuildLine():
                CenterArc((-2, 0.8), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-2, -0.8), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.2, 0.8), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.2, -0.8), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-2.0000000298, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.2000000179, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.9058053623, perimeter: 14.9915952444
            with BuildLine():
                Line((1.0198039089, 1.5000000201), (0.7348469342, 1.5000000201))
                CenterArc((0, 1.3500000201), 1.0307764125, 8.3674719704, 171.6325280296)
                Line((-1.2000000179, 0.3), (-1.0307764125, 1.3500000201))
                Line((-1.2000000179, 0.3), (1.2, 0.3))
                Line((1.2, 0.3), (1.0549512103, 1.2000000201))
                Line((0.7348469342, 1.2000000201), (1.0549512103, 1.2000000201))
                CenterArc((0, 1.3500000201), 0.7500000112, 11.5369588585, 336.9260822829)
            make_face()
            with BuildLine():
                CenterArc((-0.8, 0.7000000104), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.8, 0.7000000104), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.ADD)
    return part.part


# Description: This is a trapezoidal or wedge-shaped housing/enclosure with a sloped top surface, featuring a recessed rectangular cavity or opening on the front face and a solid vertical flange or wall on the right side.
def model_90999_1320f1ab_0021():
    """Model: Adafruit MicroUSB Micro Lipo.f56d000c-bc30-413b-99dd-dae2f263bd51 v1_C0805-NO v1 (16) (5)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 27 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
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
            # Profile area: 0.0047840903, perimeter: 0.3123514225
            with BuildLine():
                Line((0.0574309377, -0.0605000009), (0.092, -0.0605000014))
                Line((0.092, -0.0605000014), (0.092, 0.0605))
                Line((0.092, 0.0605), (0.0574309379, 0.0605))
                CenterArc((0.3, -0.0000000009), 0.25, 165.9953877008, 28.0092243938)
            make_face()
        # OneSide extrude, distance=0.125
        extrude(amount=0.125)
    return part.part


# Description: This is a pulley or idler wheel featuring a large circular disc with a grooved rim around its outer edge and a central axle hole, designed to guide and support a belt or cable.
def model_91100_df680fe7_0002():
    """Model: Mirror plug"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.8013271108, perimeter: 6.9115038379
            Circle(1.1)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.2), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.2714159265, perimeter: 3.0283185307
            with BuildLine():
                CenterArc((0.6, 0), 0.1, -90, 180)
                Line((0.6, 0.1), (-0.6, 0.1))
                CenterArc((-0.6, 0), 0.1, 90, 180)
                Line((-0.6, -0.1), (0.6, -0.1))
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical rod or shaft with a uniform circular cross-section, featuring a slightly tapered or rounded end on one side and a textured surface, appearing to be a simple mechanical component such as a pin, dowel, or drive shaft.
def model_91208_3ef96086_0001():
    """Model: handle"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4.9087385212, perimeter: 7.853981634
            Circle(1.25)
        # OneSide extrude, distance=35
        extrude(amount=35)
    return part.part


# Description: This is a hexagonal prism or column with internal curved/twisted surface features, characterized by a six-sided polygonal base and top with prominent diagonal ribbing or twisted internal geometry visible through cutaway sections on the sides.
def model_91292_7f12120b_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 91, perimeter: 40
            with BuildLine():
                Line((0, 13), (0, 0))
                Line((0, 0), (7, 0))
                Line((7, 0), (7, 13))
                Line((7, 13), (0, 13))
            make_face()
        # OneSide extrude, distance=4.5
        extrude(amount=4.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 3.926990817, perimeter: 7.024814731
            with Locations((-4, 9.5)):
                Circle(1.1180339887)
            # Profile area: 14.1371669412, perimeter: 13.3286488145
            with Locations((-3.5, 3.5)):
                Circle(2.1213203436)
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical housing or barrel with rounded ends (capsule shape), featuring a central axial bore or cavity running through its length and radial ports or openings on the side.
def model_91411_4c4628c8_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # Symmetric extrude, each_side=0.3
        extrude(amount=0.3, both=True)

        # Sketch7 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.3, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            Circle(0.1)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)
    return part.part


# Description: This is a hexagonal or polygonal geometric solid with an irregular, faceted form featuring multiple planar surfaces, internal geometric divisions, and a complex three-dimensional structure with sharp edges and angular faces.
def model_91412_b926c9f0_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 144, perimeter: 48
            with BuildLine():
                Line((-12, 12), (0, 12))
                Line((-12, 0), (-12, 12))
                Line((0, 0), (-12, 0))
                Line((0, 12), (0, 0))
            make_face()
        # OneSide extrude, distance=8
        extrude(amount=8)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            with Locations((6, -8)):
                Circle(2)
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)
    return part.part


# Description: This is an L-shaped bracket or angle iron featuring a vertical rectangular post mounted at an angle on a wider rectangular base plate, commonly used for structural support or mounting applications.
def model_91426_d0eb0ffa_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 15, perimeter: 16
            with BuildLine():
                Line((2.5, -1.5), (-2.5, -1.5))
                Line((2.5, 1.5), (2.5, -1.5))
                Line((-2.5, 1.5), (2.5, 1.5))
                Line((-2.5, -1.5), (-2.5, 1.5))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2, perimeter: 6
            with BuildLine():
                Line((-1, 0.5), (1, 0.5))
                Line((-1, -0.5), (-1, 0.5))
                Line((1, -0.5), (-1, -0.5))
                Line((1, 0.5), (1, -0.5))
            make_face()
        # OneSide extrude, distance=11
        extrude(amount=11, mode=Mode.ADD)
    return part.part


# Description: This is a sheet metal bracket or deflector with a trapezoidal base and an angled flange extending upward from the right side, featuring a bent profile with internal reinforcement lines suggesting a hollow or formed construction.
def model_91466_9983a0f3_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 448, perimeter: 452
            with BuildLine():
                Line((0, -60), (0, 2))
                Line((0, -60), (52, -60))
                Line((52, -60), (52, -58))
                Line((2, -58), (52, -58))
                Line((2, 0), (2, -58))
                Line((2, 0), (50, 0))
                Line((50, 0), (50, -25))
                Line((50, -25), (15, -25))
                Line((15, -27), (15, -25))
                Line((52, -27), (15, -27))
                Line((52, 2), (52, -27))
                Line((0, 2), (52, 2))
            make_face()
        # OneSide extrude, distance=25
        extrude(amount=25)

        # Sketch1 -> Extrude3 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 448, perimeter: 452
            with BuildLine():
                Line((0, -60), (0, 2))
                Line((0, -60), (52, -60))
                Line((52, -60), (52, -58))
                Line((2, -58), (52, -58))
                Line((2, 0), (2, -58))
                Line((2, 0), (50, 0))
                Line((50, 0), (50, -25))
                Line((50, -25), (15, -25))
                Line((15, -27), (15, -25))
                Line((52, -27), (15, -27))
                Line((52, 2), (52, -27))
                Line((0, 2), (52, 2))
            make_face()
        # OneSide extrude, distance=0.25
        extrude(amount=0.25)

        # Sketch3 -> Extrude4 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 8 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 2430.5135861806, perimeter: 1223.2567930903
            with BuildLine():
                Line((-320.0622470067, -4.1050173658), (73.008630349, -4.1050173658))
                CenterArc((73.008630349, 19.8949826342), 24, -90, 90)
                Line((97.008630349, 19.8949826342), (97.008630349, 199.8949826342))
                Line((93.008630349, 199.8949826342), (97.008630349, 199.8949826342))
                Line((93.008630349, 19.8949826342), (93.008630349, 199.8949826342))
                CenterArc((73.008630349, 19.8949826342), 20, -90, 90)
                Line((-320.0622470067, -0.1050173658), (73.008630349, -0.1050173658))
                Line((-320.0622470067, -4.1050173658), (-320.0622470067, -0.1050173658))
            make_face()
        # OneSide extrude, distance=800
        extrude(amount=800)
    return part.part


# Description: This is a cylindrical connector or coupling with an elongated capsule shape, featuring a mesh-textured cylindrical section on one end and a smooth, rounded body with what appears to be a central slot or opening along its length.
def model_91542_02495a22_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 46.5663706144, perimeter: 29.5663706144
            with BuildLine():
                CenterArc((9, 2), 2, -90, 180)
                Line((9, 4), (0.5, 4))
                CenterArc((0.5, 2), 2, 90, 180)
                Line((0.5, 0), (9, 0))
            make_face()
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)
    return part.part


# Description: This is a futuristic spacecraft or drone component featuring a dual-thruster design with two cylindrical engine pods connected to a central body, characterized by angular armor plating, blue accent panels, and curved intake vents.
def model_91555_fecd461a_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.7853981634, perimeter: 7.1415926536
            with BuildLine():
                CenterArc((-3.5, 0.5), 0.5, 90, 180)
                Line((-1.5, 0), (-3.5, 0))
                CenterArc((-1.5, 0.5), 0.5, -90, 180)
                Line((-3.5, 1), (-1.5, 1))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1)

        # Sketch3 -> Extrude3 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 12 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.2853981634, perimeter: 6.1415926536
            with BuildLine():
                CenterArc((1, 0.5), 0.5, 90, 180)
                Line((2.5, 0), (1, 0))
                CenterArc((2.5, 0.5), 0.5, -90, 180)
                Line((1, 1), (2.5, 1))
            make_face()
            # Profile area: 1.9292291743, perimeter: 6.0479531393
            with BuildLine():
                CenterArc((4.2633364098, 1.4036053), 0.4036053, -90, 180)
                Line((2.5073232855, 1.8072106), (4.2633364098, 1.8072106))
                CenterArc((2.5073232855, 1.4036053), 0.4036053, 90, 180)
                Line((4, 1), (2.5073232855, 1))
                Line((4.2633364098, 1), (4, 1))
            make_face()
            # Profile area: 2.3666016907, perimeter: 6.3034053687
            with BuildLine():
                CenterArc((5.5724527795, 0.5), 0.5052221346, -98.2450875143, 196.4901750287)
                Line((4.2633364098, 1), (5.5, 1))
                Line((4.2633364098, 1), (4, 1))
                CenterArc((4, 0.5), 0.5, 90, 180)
                Line((5.5, 0), (4, 0))
            make_face()
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)
    return part.part


# Description: This is a rectangular bracket or mounting block with a tall, elongated box shape featuring a protruding cylindrical knob or pivot pin on one end and internal slot details along its length.
def model_91604_bfe95003_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((4, 2)):
                Circle(1)
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5)

        # Sketch9 -> Extrude2 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 26.25, perimeter: 22.0663729752
            with BuildLine():
                Line((-2.5, 6), (-6.5, 6))
                Line((-6.5, 6), (-5.5, -1.5))
                Line((-5.5, -1.5), (-2.5, -1.5))
                Line((-2.5, 6), (-2.5, -1.5))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a tweezers or forceps tool featuring a symmetrical pincer design with two parallel curved handles that converge toward a flat, textured gripping head with a shell-like or radial pattern detail.
def model_91694_4d2b7754_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 11 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.1390196852, perimeter: 7.9392452425
            with BuildLine():
                CenterArc((-0.6000000089, -3.4913212228), 0.1003759054, -175.0398259003, 170.0796518006)
                Line((-0.5000000075, -3.5000000522), (-0.3995513125, -1.3810592333))
                CenterArc((0, -1.4000000209), 0.400000006, 90, 87.285917169)
                CenterArc((0, 0), 1, -175.0398259003, 85.0398259003)
                Line((-0.7000000104, -3.5000000522), (-0.9962550388, -0.0864632737))
            make_face()
            # Profile area: 1.1397279738, perimeter: 7.946311888
            with BuildLine():
                CenterArc((0, 0), 1, -90, 85.0398259003)
                CenterArc((0, -1.4000000209), 0.400000006, 2.714082831, 87.285917169)
                Line((0.5000000075, -3.5000000522), (0.3995513125, -1.3810592333))
                CenterArc((0.6000000089, -3.4952595377), 0.1001123008, -177.285917169, 174.5718343381)
                Line((0.7000000104, -3.5000000522), (0.9962550388, -0.0864632737))
            make_face()
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with BuildLine():
                CenterArc((0, 0), 1, -175.0398259003, 85.0398259003)
                CenterArc((0, 0), 1, -90, 85.0398259003)
                CenterArc((0, 0), 1, -4.9601740997, 189.9203481994)
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.0106193582, perimeter: 5.0265483206
            Circle(0.8000000119)
        # OneSide extrude, distance=-0.08
        extrude(amount=-0.08, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a centrifugal blower or fan housing featuring a rectangular inlet duct on the left, a cylindrical impeller chamber with visible internal fan blades in the center, and a curved outlet port on the right side.
def model_92030_4f061297_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 99, perimeter: 40
            with BuildLine():
                Line((-4.5, 5.5), (4.5, 5.5))
                Line((-4.5, -5.5), (-4.5, 5.5))
                Line((4.5, -5.5), (-4.5, -5.5))
                Line((4.5, 5.5), (4.5, -5.5))
            make_face()
        # OneSide extrude, distance=4
        extrude(amount=4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 4), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 18.741797286, perimeter: 33.6552139423
            with BuildLine():
                CenterArc((0, 0), 3.2350733162, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.1213203436, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=4
        extrude(amount=4, mode=Mode.ADD)
    return part.part


# Description: This is a rectangular frame or bezel with a parallelogram shape, featuring a hollow center opening and small notches or slots at the corners, likely designed as a mounting bracket or trim ring.
def model_92043_9b7b2ecc_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 56 constraints, 14 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 28.0717527707, perimeter: 108.1844189278
            with BuildLine():
                CenterArc((-8.7086226602, -4.0011385982), 0.5, 180, 90)
                Line((8.6992947296, -4.5011385982), (-8.7086226602, -4.5011385982))
                CenterArc((8.6992947296, -4.0011385982), 0.5, -90, 90)
                Line((9.1992947296, 3.9988614018), (9.1992947296, -4.0011385982))
                CenterArc((8.6992947296, 3.9988614018), 0.5, 0, 90)
                Line((-8.7086226602, 4.4988614018), (8.6992947296, 4.4988614018))
                CenterArc((-8.7086226602, 3.9988614018), 0.5, 90, 90)
                Line((-9.2086226602, -4.0011385982), (-9.2086226602, 3.9988614018))
            make_face()
            with BuildLine():
                CenterArc((0.4411438247, 4.088837638), 0.1, -168.6140488433, 78.6140488433)
                Line((0.4411438247, 3.988837638), (8.0727455481, 3.988837638))
                CenterArc((8.0727455481, 4.088837638), 0.1, -90, 76.7838876693)
                CenterArc((8.5108271402, 3.9859565481), 0.35, -77.3181549001, 244.1020425694)
                CenterArc((8.6096188274, 3.5469346778), 0.1, 102.6818450999, 77.3181549001)
                Line((8.5096188274, 3.5469346778), (8.5096188274, -3.5484251232))
                CenterArc((8.6096188274, -3.5484251232), 0.1, 180, 77.2812903678)
                CenterArc((8.5105446907, -3.9873833392), 0.35, -166.8737169465, 244.1550073143)
                CenterArc((8.0723023384, -4.0895774714), 0.1, 13.1262830535, 76.8737169465)
                Line((8.0723023384, -3.9895774714), (0.4409941911, -3.9895774714))
                CenterArc((0.4409941911, -4.0895774714), 0.1, 90, 78.5179429709)
                CenterArc((0, -4), 0.35, -168.5179429709, 157.0358859417)
                CenterArc((-0.4409941911, -4.0895774714), 0.1, 11.4820570291, 78.5179429709)
                Line((-0.4409941911, -3.9895774714), (-8.0767463045, -3.9895774714))
                CenterArc((-8.0767463045, -4.0895774714), 0.1, 90, 76.6528872788)
                CenterArc((-8.5145915257, -3.9856950267), 0.35, 102.6663247435, 243.9865625353)
                CenterArc((-8.6132642864, -3.5466464118), 0.1, -77.3336752565, 77.3336752565)
                Line((-8.5132642864, -3.5466464118), (-8.5132642864, 3.5443735462))
                CenterArc((-8.6132642864, 3.5443735462), 0.1, 0, 77.3548971815)
                CenterArc((-8.5147541527, 3.9834586786), 0.35, 13.5430242693, 243.8118729122)
                CenterArc((-8.0772666959, 4.088837638), 0.1, -166.4569757307, 76.4569757307)
                Line((-8.0772666959, 3.988837638), (-0.4411438247, 3.988837638))
                CenterArc((-0.4411438247, 4.088837638), 0.1, -90, 78.6140488433)
                CenterArc((0, 4), 0.35, 11.3859511567, 157.2280976867)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)
    return part.part


# Description: A rounded rectangular bar or connector with a horizontal slot or groove running along its length, featuring curved ends and a dark metallic finish.
def model_92286_045b32ee_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 9 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 7.7309733553, perimeter: 14.7699111843
            with BuildLine():
                CenterArc((-2.75, 0), 0.6, 90, 180)
                Line((-2.75, -0.6), (2.75, -0.6))
                CenterArc((2.75, 0), 0.6, -90, 180)
                Line((2.75, 0.6), (-2.75, 0.6))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.1570796327, perimeter: 3.1415926536
            with BuildLine():
                CenterArc((-2.75, 0), 0.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-2.75, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)
    return part.part


# Description: This is a circular fan or impeller shroud with an overall disc-like shape, featuring a mesh or perforated section on the upper portion and a solid curved surface on the lower half, designed to direct or contain airflow.
def model_92286_d48d120d_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 26.4207942167, perimeter: 18.2212373908
            Circle(2.9)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.2), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 21.2371663383, perimeter: 16.3362817987
            Circle(2.6)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7, mode=Mode.ADD)
    return part.part


# Description: This is a fish-shaped protective mesh or guard featuring a large circular/oval main body with a tapered snout extension, designed with a mesh or perforated surface pattern on the upper portions and smooth surfaces on the lower sections.
def model_92461_da2a8a13_0001():
    """Model: Spur Gear (10 teeth)"""
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
            # Profile area: 3.4797977234, perimeter: 7.8235989424
            with BuildLine():
                CenterArc((0, 0), 1.0673644444, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1778, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.254
        extrude(amount=0.254)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2423571876, perimeter: 1.8868787925
            with BuildLine():
                _nurbs_edge([(1.3064482835, -0.2269300648), (1.3075385014, -0.2271187063), (1.3097209779, -0.2274582893), (1.3130008152, -0.2278545659), (1.317386011, -0.2281681328), (1.3228865621, -0.2282679702), (1.3284045952, -0.2281589158), (1.3339381992, -0.2279224893), (1.3394852928, -0.2276172356), (1.3450437768, -0.227263782), (1.3506116219, -0.2268584177), (1.3561869705, -0.2263830588), (1.3617682232, -0.2258159181), (1.3673541545, -0.2251434805), (1.3729439417, -0.2243664928), (1.3785370306, -0.2234937955), (1.3841330328, -0.2225386515), (1.3897316184, -0.2215144274), (1.3953323911, -0.2204297157), (1.4009348479, -0.2192868971), (1.4065384372, -0.2180847688), (1.4121425915, -0.2168201556), (1.4177467677, -0.2154897765), (1.4233504925, -0.2140923881), (1.4289533672, -0.2126291175), (1.4345550419, -0.2111023991), (1.4401551973, -0.2095152979), (1.4457535253, -0.2078707394), (1.4513497064, -0.2061706193), (1.4569434075, -0.204415765), (1.4625342914, -0.2026063763), (1.4681220231, -0.2007423266), (1.4737062763, -0.1988234955), (1.4792867421, -0.1968501553), (1.4848631281, -0.1948229697), (1.4904351538, -0.1927428151), (1.4960025477, -0.1906106553), (1.5015650435, -0.188427405), (1.507122376, -0.1861937711), (1.5126742812, -0.1839102588), (1.5182204968, -0.1815772487), (1.5237607634, -0.1791950527), (1.5292948254, -0.1767639742), (1.5348224317, -0.1742843795), (1.540343336, -0.1717566976), (1.5458572967, -0.1691813876), (1.5513640768, -0.1665589164), (1.5568634439, -0.1638897345), (1.5623551701, -0.1611742471), (1.5678390313, -0.1584128141), (1.5733148055, -0.1556057651), (1.5787822714, -0.1527534107), (1.5842412068, -0.1498560545), (1.5896913873, -0.1469140079), (1.5951325873, -0.1439275918), (1.6005645835, -0.1408971276), (1.6059871592, -0.1378229315), (1.6114001063, -0.1347053087), (1.616803231, -0.1315445458), (1.6221963514, -0.1283409108), (1.6275792877, -0.1250946617), (1.6329518545, -0.1218060524), (1.6383138532, -0.1184753401), (1.6436650615, -0.1151027944), (1.6490052331, -0.1116886984), (1.6543341187, -0.1082333358), (1.6596514827, -0.1047369804), (1.6649571205, -0.1011998855), (1.6702508777, -0.0976222725), (1.6755326634, -0.0940043224), (1.6808024324, -0.0903461764), (1.6850086235, -0.0873875832), (1.6881578547, -0.0851506224), (1.6902549377, -0.0836513108), (1.691302878, -0.0828996539)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((0, 0), 1.6933333333, -2.806121858, 5.6122437161)
                _nurbs_edge([(1.3064482835, 0.2269300648), (1.3075385014, 0.2271187063), (1.3097209779, 0.2274582893), (1.3130008152, 0.2278545659), (1.317386011, 0.2281681328), (1.3228865621, 0.2282679702), (1.3284045952, 0.2281589158), (1.3339381992, 0.2279224893), (1.3394852928, 0.2276172356), (1.3450437768, 0.227263782), (1.3506116219, 0.2268584177), (1.3561869705, 0.2263830588), (1.3617682232, 0.2258159181), (1.3673541545, 0.2251434805), (1.3729439417, 0.2243664928), (1.3785370306, 0.2234937955), (1.3841330328, 0.2225386515), (1.3897316184, 0.2215144274), (1.3953323911, 0.2204297157), (1.4009348479, 0.2192868971), (1.4065384372, 0.2180847688), (1.4121425915, 0.2168201556), (1.4177467677, 0.2154897765), (1.4233504925, 0.2140923881), (1.4289533672, 0.2126291175), (1.4345550419, 0.2111023991), (1.4401551973, 0.2095152979), (1.4457535253, 0.2078707394), (1.4513497064, 0.2061706193), (1.4569434075, 0.204415765), (1.4625342914, 0.2026063763), (1.4681220231, 0.2007423266), (1.4737062763, 0.1988234955), (1.4792867421, 0.1968501553), (1.4848631281, 0.1948229697), (1.4904351538, 0.1927428151), (1.4960025477, 0.1906106553), (1.5015650435, 0.188427405), (1.507122376, 0.1861937711), (1.5126742812, 0.1839102588), (1.5182204968, 0.1815772487), (1.5237607634, 0.1791950527), (1.5292948254, 0.1767639742), (1.5348224317, 0.1742843795), (1.540343336, 0.1717566976), (1.5458572967, 0.1691813876), (1.5513640768, 0.1665589164), (1.5568634439, 0.1638897345), (1.5623551701, 0.1611742471), (1.5678390313, 0.1584128141), (1.5733148055, 0.1556057651), (1.5787822714, 0.1527534107), (1.5842412068, 0.1498560545), (1.5896913873, 0.1469140079), (1.5951325873, 0.1439275918), (1.6005645835, 0.1408971276), (1.6059871592, 0.1378229315), (1.6114001063, 0.1347053087), (1.616803231, 0.1315445458), (1.6221963514, 0.1283409108), (1.6275792877, 0.1250946617), (1.6329518545, 0.1218060524), (1.6383138532, 0.1184753401), (1.6436650615, 0.1151027944), (1.6490052331, 0.1116886984), (1.6543341187, 0.1082333358), (1.6596514827, 0.1047369804), (1.6649571205, 0.1011998855), (1.6702508777, 0.0976222725), (1.6755326634, 0.0940043224), (1.6808024324, 0.0903461764), (1.6850086235, 0.0873875832), (1.6881578547, 0.0851506224), (1.6902549377, 0.0836513108), (1.691302878, 0.0828996539)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                Line((1.0506325476, 0.1826660093), (1.3064482835, 0.2269300648))
                Line((1.0506325476, -0.1826660093), (1.0506325476, 0.1826660093))
                Line((1.0506325476, -0.1826660093), (1.3064482835, -0.2269300648))
            make_face()
        # OneSide extrude, distance=0.254
        extrude(amount=0.254, mode=Mode.ADD)
    return part.part


# Description: This is a polyhedron-shaped structural component with an irregular, angular geometry featuring multiple faceted surfaces, internal ribbing or bracing elements, and what appears to be a complex recessed cavity or cutout section on one face.
def model_92644_539a4676_0001():
    """Model: body"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 5.32, perimeter: 9.4
            with BuildLine():
                Line((1.3999999791, -1.9), (-1.4000000209, -1.9))
                Line((1.3999999791, 0), (1.3999999791, -1.9))
                Line((-1.4000000209, 0), (1.3999999791, 0))
                Line((-1.4000000209, -1.9), (-1.4000000209, 0))
            make_face()
        # OneSide extrude, distance=1.54
        extrude(amount=1.54)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 54 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -1.9, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.101690828, perimeter: 2.1625220532
            with BuildLine():
                Line((1.035, 1.3000000209), (0.505, 1.3000000209))
                Line((0.505, 1.3000000209), (0.505, 0.9000000209))
                CenterArc((0.77, 0.9000000209), 0.265, 0, 180)
                Line((1.035, 0.9000000209), (1.035, 1.3000000209))
            make_face()
            # Profile area: 0.110309172, perimeter: 1.3625220532
            with BuildLine():
                CenterArc((0.77, 0.9000000209), 0.265, 0, 180)
                Line((0.505, 0.9000000209), (1.035, 0.9000000209))
            make_face()
            # Profile area: 0.110309172, perimeter: 1.3625220532
            with BuildLine():
                Line((0.505, 0.9000000209), (1.035, 0.9000000209))
                CenterArc((0.77, 0.9000000209), 0.265, 180, 180)
            make_face()
            # Profile area: 0.110309172, perimeter: 1.3625220532
            with BuildLine():
                CenterArc((0.77, 0.0000000209), 0.265, 90, 180)
                Line((0.77, -0.2649999791), (0.77, 0.2650000209))
            make_face()
            # Profile area: 0.101690828, perimeter: 2.1625220532
            with BuildLine():
                CenterArc((0.77, 0.0000000209), 0.265, 90, 180)
                Line((0.77, 0.2650000209), (0.37, 0.2650000209))
                Line((0.37, 0.2650000209), (0.37, -0.2649999791))
                Line((0.37, -0.2649999791), (0.77, -0.2649999791))
            make_face()
            # Profile area: 0.110309172, perimeter: 1.3625220532
            with BuildLine():
                Line((0.77, -0.2649999791), (0.77, 0.2650000209))
                CenterArc((0.77, 0.0000000209), 0.265, -90, 180)
            make_face()
            # Profile area: 0.2206183441, perimeter: 1.6650441064
            with BuildLine():
                CenterArc((0.77, -0.8999999791), 0.265, 0, 180)
                CenterArc((0.77, -0.8999999791), 0.265, 180, 180)
            make_face()
            # Profile area: 0.101690828, perimeter: 2.1625220532
            with BuildLine():
                CenterArc((0.77, -0.8999999791), 0.265, 180, 180)
                Line((0.505, -1.2999999791), (0.505, -0.8999999791))
                Line((1.035, -1.2999999791), (0.505, -1.2999999791))
                Line((1.035, -0.8999999791), (1.035, -1.2999999791))
            make_face()
            # Profile area: 0.06125, perimeter: 1.05
            with BuildLine():
                Line((1.365, 0.7500000209), (1.365, 0.4000000209))
                Line((1.365, 0.7500000209), (1.19, 0.7500000209))
                Line((1.19, 0.7500000209), (1.19, 0.4000000209))
                Line((1.19, 0.4000000209), (1.365, 0.4000000209))
            make_face()
            # Profile area: 0.021, perimeter: 0.59
            with BuildLine():
                Line((1.54, 0.7500000209), (1.365, 0.7500000209))
                Line((1.54, 0.7500000209), (1.54, 0.8700000209))
                Line((1.54, 0.8700000209), (1.365, 0.8700000209))
                Line((1.365, 0.8700000209), (1.365, 0.7500000209))
            make_face()
            # Profile area: 0.06125, perimeter: 1.05
            with BuildLine():
                Line((1.54, -0.7499999791), (1.365, -0.7499999791))
                Line((1.54, -0.7499999791), (1.54, -0.3999999791))
                Line((1.365, -0.3999999791), (1.54, -0.3999999791))
                Line((1.365, -0.3999999791), (1.365, -0.7499999791))
            make_face()
            # Profile area: 0.06125, perimeter: 1.05
            with BuildLine():
                Line((1.365, -0.3999999791), (1.365, -0.7499999791))
                Line((1.19, -0.3999999791), (1.365, -0.3999999791))
                Line((1.19, -0.7499999791), (1.19, -0.3999999791))
                Line((1.365, -0.7499999791), (1.19, -0.7499999791))
            make_face()
            # Profile area: 0.06125, perimeter: 1.05
            with BuildLine():
                Line((1.365, 0.4000000209), (1.54, 0.4000000209))
                Line((1.54, 0.4000000209), (1.54, 0.7500000209))
                Line((1.54, 0.7500000209), (1.365, 0.7500000209))
                Line((1.365, 0.7500000209), (1.365, 0.4000000209))
            make_face()
            # Profile area: 0.0385, perimeter: 0.79
            with BuildLine():
                Line((1.54, -0.9699999791), (1.54, -0.7499999791))
                Line((1.54, -0.7499999791), (1.365, -0.7499999791))
                Line((1.365, -0.7499999791), (1.365, -0.9699999791))
                Line((1.365, -0.9699999791), (1.54, -0.9699999791))
            make_face()
            # Profile area: 0.06125, perimeter: 1.05
            with BuildLine():
                Line((0.175, -0.3999999791), (0.175, -0.7499999791))
                Line((0.175, -0.3999999791), (0, -0.3999999791))
                Line((0, -0.7499999791), (0, -0.3999999791))
                Line((0, -0.7499999791), (0.175, -0.7499999791))
            make_face()
            # Profile area: 0.0385, perimeter: 0.79
            with BuildLine():
                Line((0.175, -0.9699999791), (0, -0.9699999791))
                Line((0.175, -0.7499999791), (0.175, -0.9699999791))
                Line((0, -0.7499999791), (0.175, -0.7499999791))
                Line((0, -0.9699999791), (0, -0.7499999791))
            make_face()
            # Profile area: 0.06125, perimeter: 1.05
            with BuildLine():
                Line((0.175, 0.7500000209), (0.175, 0.4000000209))
                Line((0.35, 0.4000000209), (0.175, 0.4000000209))
                Line((0.35, 0.7500000209), (0.35, 0.4000000209))
                Line((0.175, 0.7500000209), (0.35, 0.7500000209))
            make_face()
            # Profile area: 0.06125, perimeter: 1.05
            with BuildLine():
                Line((0.175, -0.7499999791), (0.35, -0.7499999791))
                Line((0.35, -0.7499999791), (0.35, -0.3999999791))
                Line((0.35, -0.3999999791), (0.175, -0.3999999791))
                Line((0.175, -0.3999999791), (0.175, -0.7499999791))
            make_face()
            # Profile area: 0.021, perimeter: 0.59
            with BuildLine():
                Line((0, 0.7500000209), (0, 0.8700000209))
                Line((0, 0.7500000209), (0.175, 0.7500000209))
                Line((0.175, 0.8700000209), (0.175, 0.7500000209))
                Line((0, 0.8700000209), (0.175, 0.8700000209))
            make_face()
            # Profile area: 0.06125, perimeter: 1.05
            with BuildLine():
                Line((0, 0.7500000209), (0.175, 0.7500000209))
                Line((0, 0.4000000209), (0, 0.7500000209))
                Line((0.175, 0.4000000209), (0, 0.4000000209))
                Line((0.175, 0.7500000209), (0.175, 0.4000000209))
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)
    return part.part


# Description: A long, slender cylindrical rod or shaft with a slight taper, oriented at an angle, featuring a smooth uniform surface with no visible holes, slots, or flanges.
def model_93197_ce30c6aa_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 21 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.0649551315, perimeter: 10.4705921022
            with BuildLine():
                Line((0.9772253777, 0.200000003), (0.9772253777, 0.080000003))
                Line((0.9772253777, 0.080000003), (0.4772253777, 0.080000003))
                Line((0.4772253777, 0.080000003), (0.4772253777, 0.200000003))
                Line((-0.4500000075, 0.200000003), (0.4772253777, 0.200000003))
                CenterArc((-0.4500000075, 0.150000003), 0.05, 90, 90)
                Line((-0.5000000075, 0.150000003), (-0.5000000075, 0.080000003))
                Line((-0.5000000075, 0.080000003), (-0.2200000075, 0.080000003))
                Line((-0.2200000075, 0.080000003), (-0.2200000075, -0.1000000015))
                Line((-0.2200000075, -0.1000000015), (-0.0200000075, -0.1000000015))
                Line((-0.0200000075, -0.1000000015), (-0.0200000075, 0.0299999985))
                Line((-0.0200000075, 0.0299999985), (0.2799999925, 0.0299999985))
                Line((0.2799999925, 0.0299999985), (0.2799999925, -0.1000000015))
                Line((0.2799999925, -0.1000000015), (0.5399999925, -0.1000000015))
                Line((0.5399999925, -0.1000000015), (0.5399999925, -0.5000000015))
                Line((0.5399999925, -0.5000000015), (0.3000000045, -0.5000000015))
                Line((0.3000000045, -0.5000000015), (0.3000000045, -0.6300000015))
                Line((0.3000000045, -0.6300000015), (0, -0.6300000015))
                Line((0, -0.6300000015), (0, -0.5000000015))
                Line((0, -0.5000000015), (-0.200000003, -0.5000000015))
                Line((-0.200000003, -0.5000000015), (-0.200000003, -0.8000000119))
                Line((-0.200000003, -0.8000000119), (1.259999997, -0.8000000119))
                Line((1.259999997, -0.8000000119), (1.259999997, -0.6800000119))
                Line((1.259999997, -0.6800000119), (1.059999997, -0.6800000119))
                Line((1.059999997, -0.6800000119), (1.059999997, -0.5400000119))
                Line((1.059999997, -0.5400000119), (1.259999997, -0.5400000119))
                Line((1.259999997, -0.5400000119), (1.259999997, -0.3600000045))
                Line((1.259999997, -0.3600000045), (1.1311486622, -0.3600000045))
                CenterArc((0.9772253777, -0.3005641356), 0.165, 21.534126699, 317.3523261851)
                Line((1.259999997, -0.2400000045), (1.1307082303, -0.2400000045))
                Line((1.259999997, -0.2400000045), (1.259999997, 0.000000003))
                Line((1.9000000283, 0.000000003), (1.259999997, 0.000000003))
                Line((1.9000000283, 0.200000003), (1.9000000283, 0.000000003))
                Line((1.3899999925, 0.200000003), (1.9000000283, 0.200000003))
                Line((0.9772253777, 0.200000003), (1.3899999925, 0.200000003))
            make_face()
        # OneSide extrude, distance=42.7
        extrude(amount=42.7)
    return part.part


# Description: This is a flat parallelogram-shaped panel or plate with an internal triangular lattice/truss structure that provides structural reinforcement while minimizing weight.
def model_95620_940f6521_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> 拉伸1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 270 constraints, 101 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 226.8458049838, perimeter: 419.14629323
            with BuildLine():
                CenterArc((-4, 0), 1, 90, 90)
                Line((-5, 0), (-5, -18))
                CenterArc((-4, -18), 1, 180, 90)
                Line((14, -19), (-4, -19))
                CenterArc((14, -18), 1, -90, 90)
                Line((15, 0), (15, -18))
                CenterArc((14, 0), 1, 0, 90)
                Line((-4, 1), (14, 1))
            make_face()
            with BuildLine():
                Line((-4.3292893219, -0.3778174593), (-1.2071067812, -3.5))
                Line((-4.5, -3.5), (-1.2071067812, -3.5))
                Line((-4.5, -0.4485281374), (-4.5, -3.5))
                CenterArc((-4.4, -0.4485281374), 0.1, 45, 135)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-0.5, 0.25), (-0.5, -2.5514718626))
                CenterArc((-0.6, -2.5514718626), 0.1, -135, 135)
                Line((-3.6221825407, 0.3292893219), (-0.6707106781, -2.6221825407))
                CenterArc((-3.5514718626, 0.4), 0.1, 90, 135)
                Line((-3.5514718626, 0.5), (-0.75, 0.5))
                CenterArc((-0.75, 0.25), 0.25, 0, 90)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((3.6221825407, 0.3292893219), (0.6707106781, -2.6221825407))
                CenterArc((0.6, -2.5514718626), 0.1, 180, 135)
                Line((0.5, 0.25), (0.5, -2.5514718626))
                CenterArc((0.75, 0.25), 0.25, 90, 90)
                Line((0.75, 0.5), (3.5514718626, 0.5))
                CenterArc((3.5514718626, 0.4), 0.1, -45, 135)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((4.5, -0.4485281374), (4.5, -3.25))
                CenterArc((4.25, -3.25), 0.25, -90, 90)
                Line((1.4485281374, -3.5), (4.25, -3.5))
                CenterArc((1.4485281374, -3.4), 0.1, 135, 135)
                Line((4.3292893219, -0.3778174593), (1.3778174593, -3.3292893219))
                CenterArc((4.4, -0.4485281374), 0.1, 0, 135)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((5.5, -0.4485281374), (5.5, -3.25))
                CenterArc((5.6, -0.4485281374), 0.1, 45, 135)
                Line((8.6221825407, -3.3292893219), (5.6707106781, -0.3778174593))
                CenterArc((8.5514718626, -3.4), 0.1, -90, 135)
                Line((5.75, -3.5), (8.5514718626, -3.5))
                CenterArc((5.75, -3.25), 0.25, 180, 90)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((9.5, 0.25), (9.5, -2.5514718626))
                CenterArc((9.4, -2.5514718626), 0.1, -135, 135)
                Line((9.3292893219, -2.6221825407), (6.3778174593, 0.3292893219))
                CenterArc((6.4485281374, 0.4), 0.1, 90, 135)
                Line((6.4485281374, 0.5), (9.25, 0.5))
                CenterArc((9.25, 0.25), 0.25, 0, 90)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((13.6221825407, 0.3292893219), (10.6707106781, -2.6221825407))
                CenterArc((10.6, -2.5514718626), 0.1, 180, 135)
                Line((10.5, 0.25), (10.5, -2.5514718626))
                CenterArc((10.75, 0.25), 0.25, 90, 90)
                Line((10.75, 0.5), (13.5514718626, 0.5))
                CenterArc((13.5514718626, 0.4), 0.1, -45, 135)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((14.5, -0.4485281374), (14.5, -3.25))
                CenterArc((14.25, -3.25), 0.25, -90, 90)
                Line((11.4485281374, -3.5), (14.25, -3.5))
                CenterArc((11.4485281374, -3.4), 0.1, 135, 135)
                Line((14.3292893219, -0.3778174593), (11.3778174593, -3.3292893219))
                CenterArc((14.4, -0.4485281374), 0.1, 0, 135)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((14.3292893219, -7.6221825407), (11.3778174593, -4.6707106781))
                CenterArc((11.4485281374, -4.6), 0.1, 90, 135)
                Line((11.4485281374, -4.5), (14.25, -4.5))
                CenterArc((14.25, -4.75), 0.25, 0, 90)
                Line((14.5, -4.75), (14.5, -7.5514718626))
                CenterArc((14.4, -7.5514718626), 0.1, -135, 135)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((10.5, -5.4485281374), (10.5, -8.25))
                CenterArc((10.6, -5.4485281374), 0.1, 45, 135)
                Line((13.6221825407, -8.3292893219), (10.6707106781, -5.3778174593))
                CenterArc((13.5514718626, -8.4), 0.1, -90, 135)
                Line((10.75, -8.5), (13.5514718626, -8.5))
                CenterArc((10.75, -8.25), 0.25, 180, 90)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((9.5, -5.4485281374), (9.5, -8.25))
                CenterArc((9.25, -8.25), 0.25, -90, 90)
                Line((6.4485281374, -8.5), (9.25, -8.5))
                CenterArc((6.4485281374, -8.4), 0.1, 135, 135)
                Line((9.3292893219, -5.3778174593), (6.3778174593, -8.3292893219))
                CenterArc((9.4, -5.4485281374), 0.1, 0, 135)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((5.75, -4.5), (8.5514718626, -4.5))
                CenterArc((8.5514718626, -4.6), 0.1, -45, 135)
                Line((8.6221825407, -4.6707106781), (5.6707106781, -7.6221825407))
                CenterArc((5.6, -7.5514718626), 0.1, -180, 135)
                Line((5.5, -4.75), (5.5, -7.5514718626))
                CenterArc((5.75, -4.75), 0.25, 90, 90)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((1.4485281374, -4.5), (4.25, -4.5))
                CenterArc((4.25, -4.75), 0.25, 0, 90)
                Line((4.5, -4.75), (4.5, -7.5514718626))
                CenterArc((4.4, -7.5514718626), 0.1, -135, 135)
                Line((1.3778174593, -4.6707106781), (4.3292893219, -7.6221825407))
                CenterArc((1.4485281374, -4.6), 0.1, 90, 135)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((0.6707106781, -5.3778174593), (3.6221825407, -8.3292893219))
                CenterArc((3.5514718626, -8.4), 0.1, -90, 135)
                Line((0.75, -8.5), (3.5514718626, -8.5))
                CenterArc((0.75, -8.25), 0.25, 180, 90)
                Line((0.5, -5.4485281374), (0.5, -8.25))
                CenterArc((0.6, -5.4485281374), 0.1, 45, 135)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-4.25, -4.5), (-1.4485281374, -4.5))
                CenterArc((-1.4485281374, -4.6), 0.1, -45, 135)
                Line((-1.3778174593, -4.6707106781), (-4.3292893219, -7.6221825407))
                CenterArc((-4.4, -7.5514718626), 0.1, 180, 135)
                Line((-4.5, -4.75), (-4.5, -7.5514718626))
                CenterArc((-4.25, -4.75), 0.25, 90, 90)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-0.5, -5.4485281374), (-0.5, -8.25))
                CenterArc((-0.75, -8.25), 0.25, -90, 90)
                Line((-3.5514718626, -8.5), (-0.75, -8.5))
                CenterArc((-3.5514718626, -8.4), 0.1, 135, 135)
                Line((-0.6707106781, -5.3778174593), (-3.6221825407, -8.3292893219))
                CenterArc((-0.6, -5.4485281374), 0.1, 0, 135)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-4.3292893219, -10.3778174593), (-1.3778174593, -13.3292893219))
                CenterArc((-1.4485281374, -13.4), 0.1, -90, 135)
                Line((-4.25, -13.5), (-1.4485281374, -13.5))
                CenterArc((-4.25, -13.25), 0.25, 180, 90)
                Line((-4.5, -10.4485281374), (-4.5, -13.25))
                CenterArc((-4.4, -10.4485281374), 0.1, 45, 135)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-0.5, -9.75), (-0.5, -12.5514718626))
                CenterArc((-0.6, -12.5514718626), 0.1, -135, 135)
                Line((-3.6221825407, -9.6707106781), (-0.6707106781, -12.6221825407))
                CenterArc((-3.5514718626, -9.6), 0.1, 90, 135)
                Line((-3.5514718626, -9.5), (-0.75, -9.5))
                CenterArc((-0.75, -9.75), 0.25, 0, 90)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((3.6221825407, -9.6707106781), (0.6707106781, -12.6221825407))
                CenterArc((0.6, -12.5514718626), 0.1, 180, 135)
                Line((0.5, -9.75), (0.5, -12.5514718626))
                CenterArc((0.75, -9.75), 0.25, 90, 90)
                Line((0.75, -9.5), (3.5514718626, -9.5))
                CenterArc((3.5514718626, -9.6), 0.1, -45, 135)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((4.5, -10.4485281374), (4.5, -13.25))
                CenterArc((4.25, -13.25), 0.25, -90, 90)
                Line((1.4485281374, -13.5), (4.25, -13.5))
                CenterArc((1.4485281374, -13.4), 0.1, 135, 135)
                Line((4.3292893219, -10.3778174593), (1.3778174593, -13.3292893219))
                CenterArc((4.4, -10.4485281374), 0.1, 0, 135)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((5.6707106781, -10.3778174593), (8.6221825407, -13.3292893219))
                CenterArc((8.5514718626, -13.4), 0.1, -90, 135)
                Line((5.75, -13.5), (8.5514718626, -13.5))
                CenterArc((5.75, -13.25), 0.25, 180, 90)
                Line((5.5, -10.4485281374), (5.5, -13.25))
                CenterArc((5.6, -10.4485281374), 0.1, 45, 135)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((9.5, -9.75), (9.5, -12.5514718626))
                CenterArc((9.4, -12.5514718626), 0.1, -135, 135)
                Line((6.3778174593, -9.6707106781), (9.3292893219, -12.6221825407))
                CenterArc((6.4485281374, -9.6), 0.1, 90, 135)
                Line((6.4485281374, -9.5), (9.25, -9.5))
                CenterArc((9.25, -9.75), 0.25, 0, 90)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((10.75, -9.5), (13.5514718626, -9.5))
                CenterArc((13.5514718626, -9.6), 0.1, -45, 135)
                Line((10.6707106781, -12.6221825407), (13.6221825407, -9.6707106781))
                CenterArc((10.6, -12.5514718626), 0.1, 180, 135)
                Line((10.5, -9.75), (10.5, -12.5514718626))
                CenterArc((10.75, -9.75), 0.25, 90, 90)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((14.5, -10.4485281374), (14.5, -13.25))
                CenterArc((14.25, -13.25), 0.25, -90, 90)
                Line((11.4485281374, -13.5), (14.25, -13.5))
                CenterArc((11.4485281374, -13.4), 0.1, 135, 135)
                Line((11.3778174593, -13.3292893219), (14.3292893219, -10.3778174593))
                CenterArc((14.4, -10.4485281374), 0.1, 0, 135)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((11.4485281374, -14.5), (14.25, -14.5))
                CenterArc((14.25, -14.75), 0.25, 0, 90)
                Line((14.5, -14.75), (14.5, -17.5514718626))
                CenterArc((14.4, -17.5514718626), 0.1, -135, 135)
                Line((11.3778174593, -14.6707106781), (14.3292893219, -17.6221825407))
                CenterArc((11.4485281374, -14.6), 0.1, 90, 135)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((10.6707106781, -15.3778174593), (13.6221825407, -18.3292893219))
                CenterArc((13.5514718626, -18.4), 0.1, -90, 135)
                Line((10.75, -18.5), (13.5514718626, -18.5))
                CenterArc((10.75, -18.25), 0.25, 180, 90)
                Line((10.5, -15.4485281374), (10.5, -18.25))
                CenterArc((10.6, -15.4485281374), 0.1, 45, 135)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((6.3778174593, -18.3292893219), (9.3292893219, -15.3778174593))
                CenterArc((9.4, -15.4485281374), 0.1, 0, 135)
                Line((9.5, -15.4485281374), (9.5, -18.25))
                CenterArc((9.25, -18.25), 0.25, -90, 90)
                Line((6.4485281374, -18.5), (9.25, -18.5))
                CenterArc((6.4485281374, -18.4), 0.1, 135, 135)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((5.75, -14.5), (8.5514718626, -14.5))
                CenterArc((8.5514718626, -14.6), 0.1, -45, 135)
                Line((5.6707106781, -17.6221825407), (8.6221825407, -14.6707106781))
                CenterArc((5.6, -17.5514718626), 0.1, 180, 135)
                Line((5.5, -14.75), (5.5, -17.5514718626))
                CenterArc((5.75, -14.75), 0.25, 90, 90)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((1.4485281374, -14.5), (4.25, -14.5))
                CenterArc((4.25, -14.75), 0.25, 0, 90)
                Line((4.5, -14.75), (4.5, -17.5514718626))
                CenterArc((4.4, -17.5514718626), 0.1, -135, 135)
                Line((1.3778174593, -14.6707106781), (4.3292893219, -17.6221825407))
                CenterArc((1.4485281374, -14.6), 0.1, 90, 135)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((0.6707106781, -15.3778174593), (3.6221825407, -18.3292893219))
                CenterArc((3.5514718626, -18.4), 0.1, -90, 135)
                Line((0.75, -18.5), (3.5514718626, -18.5))
                CenterArc((0.75, -18.25), 0.25, 180, 90)
                Line((0.5, -15.4485281374), (0.5, -18.25))
                CenterArc((0.6, -15.4485281374), 0.1, 45, 135)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-0.5, -15.4485281374), (-0.5, -18.25))
                CenterArc((-0.75, -18.25), 0.25, -90, 90)
                Line((-3.5514718626, -18.5), (-0.75, -18.5))
                CenterArc((-3.5514718626, -18.4), 0.1, 135, 135)
                Line((-0.6707106781, -15.3778174593), (-3.6221825407, -18.3292893219))
                CenterArc((-0.6, -15.4485281374), 0.1, 0, 135)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-4.25, -14.5), (-1.4485281374, -14.5))
                CenterArc((-1.4485281374, -14.6), 0.1, -45, 135)
                Line((-1.3778174593, -14.6707106781), (-4.3292893219, -17.6221825407))
                CenterArc((-4.4, -17.5514718626), 0.1, 180, 135)
                Line((-4.5, -14.75), (-4.5, -17.5514718626))
                CenterArc((-4.25, -14.75), 0.25, 90, 90)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.02
        extrude(amount=0.02)

        # Sketch1 -> 拉伸2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 270 constraints, 101 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.3834379341, perimeter: 10.6408932419
            with BuildLine():
                CenterArc((4.4, -10.4485281374), 0.1, 0, 135)
                Line((4.3292893219, -10.3778174593), (1.3778174593, -13.3292893219))
                CenterArc((1.4485281374, -13.4), 0.1, 135, 135)
                Line((1.4485281374, -13.5), (4.25, -13.5))
                CenterArc((4.25, -13.25), 0.25, -90, 90)
                Line((4.5, -10.4485281374), (4.5, -13.25))
            make_face()
            # Profile area: 5.3834379341, perimeter: 10.6408932419
            with BuildLine():
                CenterArc((11.4485281374, -14.6), 0.1, 90, 135)
                Line((11.3778174593, -14.6707106781), (14.3292893219, -17.6221825407))
                CenterArc((14.4, -17.5514718626), 0.1, -135, 135)
                Line((14.5, -14.75), (14.5, -17.5514718626))
                CenterArc((14.25, -14.75), 0.25, 0, 90)
                Line((11.4485281374, -14.5), (14.25, -14.5))
            make_face()
            # Profile area: 5.3834379341, perimeter: 10.6408932419
            with BuildLine():
                CenterArc((5.75, -14.75), 0.25, 90, 90)
                Line((5.5, -14.75), (5.5, -17.5514718626))
                CenterArc((5.6, -17.5514718626), 0.1, 180, 135)
                Line((5.6707106781, -17.6221825407), (8.6221825407, -14.6707106781))
                CenterArc((8.5514718626, -14.6), 0.1, -45, 135)
                Line((5.75, -14.5), (8.5514718626, -14.5))
            make_face()
            # Profile area: 5.3834379341, perimeter: 10.6408932419
            with BuildLine():
                CenterArc((1.4485281374, -14.6), 0.1, 90, 135)
                Line((1.3778174593, -14.6707106781), (4.3292893219, -17.6221825407))
                CenterArc((4.4, -17.5514718626), 0.1, -135, 135)
                Line((4.5, -14.75), (4.5, -17.5514718626))
                CenterArc((4.25, -14.75), 0.25, 0, 90)
                Line((1.4485281374, -14.5), (4.25, -14.5))
            make_face()
            # Profile area: 5.3834379341, perimeter: 10.6408932419
            with BuildLine():
                CenterArc((-4.25, -14.75), 0.25, 90, 90)
                Line((-4.5, -14.75), (-4.5, -17.5514718626))
                CenterArc((-4.4, -17.5514718626), 0.1, 180, 135)
                Line((-1.3778174593, -14.6707106781), (-4.3292893219, -17.6221825407))
                CenterArc((-1.4485281374, -14.6), 0.1, -45, 135)
                Line((-4.25, -14.5), (-1.4485281374, -14.5))
            make_face()
            # Profile area: 5.3834379341, perimeter: 10.6408932419
            with BuildLine():
                CenterArc((4.4, -0.4485281374), 0.1, 0, 135)
                Line((4.3292893219, -0.3778174593), (1.3778174593, -3.3292893219))
                CenterArc((1.4485281374, -3.4), 0.1, 135, 135)
                Line((1.4485281374, -3.5), (4.25, -3.5))
                CenterArc((4.25, -3.25), 0.25, -90, 90)
                Line((4.5, -0.4485281374), (4.5, -3.25))
            make_face()
            # Profile area: 5.3834379341, perimeter: 10.6408932419
            with BuildLine():
                CenterArc((1.4485281374, -4.6), 0.1, 90, 135)
                Line((1.3778174593, -4.6707106781), (4.3292893219, -7.6221825407))
                CenterArc((4.4, -7.5514718626), 0.1, -135, 135)
                Line((4.5, -4.75), (4.5, -7.5514718626))
                CenterArc((4.25, -4.75), 0.25, 0, 90)
                Line((1.4485281374, -4.5), (4.25, -4.5))
            make_face()
            # Profile area: 5.3834379341, perimeter: 10.6408932419
            with BuildLine():
                CenterArc((-0.75, -9.75), 0.25, 0, 90)
                Line((-3.5514718626, -9.5), (-0.75, -9.5))
                CenterArc((-3.5514718626, -9.6), 0.1, 90, 135)
                Line((-3.6221825407, -9.6707106781), (-0.6707106781, -12.6221825407))
                CenterArc((-0.6, -12.5514718626), 0.1, -135, 135)
                Line((-0.5, -9.75), (-0.5, -12.5514718626))
            make_face()
            # Profile area: 5.3834379341, perimeter: 10.6408932419
            with BuildLine():
                CenterArc((0.6, -15.4485281374), 0.1, 45, 135)
                Line((0.5, -15.4485281374), (0.5, -18.25))
                CenterArc((0.75, -18.25), 0.25, 180, 90)
                Line((0.75, -18.5), (3.5514718626, -18.5))
                CenterArc((3.5514718626, -18.4), 0.1, -90, 135)
                Line((0.6707106781, -15.3778174593), (3.6221825407, -18.3292893219))
            make_face()
            # Profile area: 5.3834379341, perimeter: 10.6408932419
            with BuildLine():
                CenterArc((-4.4, -10.4485281374), 0.1, 45, 135)
                Line((-4.5, -10.4485281374), (-4.5, -13.25))
                CenterArc((-4.25, -13.25), 0.25, 180, 90)
                Line((-4.25, -13.5), (-1.4485281374, -13.5))
                CenterArc((-1.4485281374, -13.4), 0.1, -90, 135)
                Line((-4.3292893219, -10.3778174593), (-1.3778174593, -13.3292893219))
            make_face()
            # Profile area: 5.3834379341, perimeter: 10.6408932419
            with BuildLine():
                CenterArc((0.6, -5.4485281374), 0.1, 45, 135)
                Line((0.5, -5.4485281374), (0.5, -8.25))
                CenterArc((0.75, -8.25), 0.25, 180, 90)
                Line((0.75, -8.5), (3.5514718626, -8.5))
                CenterArc((3.5514718626, -8.4), 0.1, -90, 135)
                Line((0.6707106781, -5.3778174593), (3.6221825407, -8.3292893219))
            make_face()
            # Profile area: 5.3834379341, perimeter: 10.6408932419
            with BuildLine():
                CenterArc((-0.6, -15.4485281374), 0.1, 0, 135)
                Line((-0.6707106781, -15.3778174593), (-3.6221825407, -18.3292893219))
                CenterArc((-3.5514718626, -18.4), 0.1, 135, 135)
                Line((-3.5514718626, -18.5), (-0.75, -18.5))
                CenterArc((-0.75, -18.25), 0.25, -90, 90)
                Line((-0.5, -15.4485281374), (-0.5, -18.25))
            make_face()
            # Profile area: 5.3834379341, perimeter: 10.6408932419
            with BuildLine():
                CenterArc((3.5514718626, -9.6), 0.1, -45, 135)
                Line((0.75, -9.5), (3.5514718626, -9.5))
                CenterArc((0.75, -9.75), 0.25, 90, 90)
                Line((0.5, -9.75), (0.5, -12.5514718626))
                CenterArc((0.6, -12.5514718626), 0.1, 180, 135)
                Line((3.6221825407, -9.6707106781), (0.6707106781, -12.6221825407))
            make_face()
            # Profile area: 5.3834379341, perimeter: 10.6408932419
            with BuildLine():
                CenterArc((3.5514718626, 0.4), 0.1, -45, 135)
                Line((0.75, 0.5), (3.5514718626, 0.5))
                CenterArc((0.75, 0.25), 0.25, 90, 90)
                Line((0.5, 0.25), (0.5, -2.5514718626))
                CenterArc((0.6, -2.5514718626), 0.1, 180, 135)
                Line((3.6221825407, 0.3292893219), (0.6707106781, -2.6221825407))
            make_face()
            # Profile area: 5.3834379341, perimeter: 10.6408932419
            with BuildLine():
                CenterArc((10.6, -15.4485281374), 0.1, 45, 135)
                Line((10.5, -15.4485281374), (10.5, -18.25))
                CenterArc((10.75, -18.25), 0.25, 180, 90)
                Line((10.75, -18.5), (13.5514718626, -18.5))
                CenterArc((13.5514718626, -18.4), 0.1, -90, 135)
                Line((10.6707106781, -15.3778174593), (13.6221825407, -18.3292893219))
            make_face()
            # Profile area: 5.3834379341, perimeter: 10.6408932419
            with BuildLine():
                CenterArc((6.4485281374, -18.4), 0.1, 135, 135)
                Line((6.4485281374, -18.5), (9.25, -18.5))
                CenterArc((9.25, -18.25), 0.25, -90, 90)
                Line((9.5, -15.4485281374), (9.5, -18.25))
                CenterArc((9.4, -15.4485281374), 0.1, 0, 135)
                Line((6.3778174593, -18.3292893219), (9.3292893219, -15.3778174593))
            make_face()
            # Profile area: 5.3834379341, perimeter: 10.6408932419
            with BuildLine():
                CenterArc((-0.6, -5.4485281374), 0.1, 0, 135)
                Line((-0.6707106781, -5.3778174593), (-3.6221825407, -8.3292893219))
                CenterArc((-3.5514718626, -8.4), 0.1, 135, 135)
                Line((-3.5514718626, -8.5), (-0.75, -8.5))
                CenterArc((-0.75, -8.25), 0.25, -90, 90)
                Line((-0.5, -5.4485281374), (-0.5, -8.25))
            make_face()
            # Profile area: 5.3834379341, perimeter: 10.6408932419
            with BuildLine():
                CenterArc((-0.75, 0.25), 0.25, 0, 90)
                Line((-3.5514718626, 0.5), (-0.75, 0.5))
                CenterArc((-3.5514718626, 0.4), 0.1, 90, 135)
                Line((-3.6221825407, 0.3292893219), (-0.6707106781, -2.6221825407))
                CenterArc((-0.6, -2.5514718626), 0.1, -135, 135)
                Line((-0.5, 0.25), (-0.5, -2.5514718626))
            make_face()
            # Profile area: 5.3834379341, perimeter: 10.6408932419
            with BuildLine():
                CenterArc((9.4, -5.4485281374), 0.1, 0, 135)
                Line((9.3292893219, -5.3778174593), (6.3778174593, -8.3292893219))
                CenterArc((6.4485281374, -8.4), 0.1, 135, 135)
                Line((6.4485281374, -8.5), (9.25, -8.5))
                CenterArc((9.25, -8.25), 0.25, -90, 90)
                Line((9.5, -5.4485281374), (9.5, -8.25))
            make_face()
            # Profile area: 5.3834379341, perimeter: 10.6408932419
            with BuildLine():
                CenterArc((14.4, -0.4485281374), 0.1, 0, 135)
                Line((14.3292893219, -0.3778174593), (11.3778174593, -3.3292893219))
                CenterArc((11.4485281374, -3.4), 0.1, 135, 135)
                Line((11.4485281374, -3.5), (14.25, -3.5))
                CenterArc((14.25, -3.25), 0.25, -90, 90)
                Line((14.5, -0.4485281374), (14.5, -3.25))
            make_face()
            # Profile area: 5.4092117121, perimeter: 10.9954174237
            with BuildLine():
                CenterArc((-4.4, -0.4485281374), 0.1, 45, 135)
                Line((-4.5, -0.4485281374), (-4.5, -3.5))
                Line((-4.5, -3.5), (-1.2071067812, -3.5))
                Line((-4.3292893219, -0.3778174593), (-1.2071067812, -3.5))
            make_face()
            # Profile area: 5.3834379341, perimeter: 10.6408932419
            with BuildLine():
                CenterArc((-4.25, -4.75), 0.25, 90, 90)
                Line((-4.5, -4.75), (-4.5, -7.5514718626))
                CenterArc((-4.4, -7.5514718626), 0.1, 180, 135)
                Line((-1.3778174593, -4.6707106781), (-4.3292893219, -7.6221825407))
                CenterArc((-1.4485281374, -4.6), 0.1, -45, 135)
                Line((-4.25, -4.5), (-1.4485281374, -4.5))
            make_face()
            # Profile area: 5.3834379341, perimeter: 10.6408932419
            with BuildLine():
                CenterArc((13.5514718626, 0.4), 0.1, -45, 135)
                Line((10.75, 0.5), (13.5514718626, 0.5))
                CenterArc((10.75, 0.25), 0.25, 90, 90)
                Line((10.5, 0.25), (10.5, -2.5514718626))
                CenterArc((10.6, -2.5514718626), 0.1, 180, 135)
                Line((13.6221825407, 0.3292893219), (10.6707106781, -2.6221825407))
            make_face()
            # Profile area: 5.3834379341, perimeter: 10.6408932419
            with BuildLine():
                CenterArc((5.75, -4.75), 0.25, 90, 90)
                Line((5.5, -4.75), (5.5, -7.5514718626))
                CenterArc((5.6, -7.5514718626), 0.1, -180, 135)
                Line((8.6221825407, -4.6707106781), (5.6707106781, -7.6221825407))
                CenterArc((8.5514718626, -4.6), 0.1, -45, 135)
                Line((5.75, -4.5), (8.5514718626, -4.5))
            make_face()
            # Profile area: 5.3834379341, perimeter: 10.6408932419
            with BuildLine():
                CenterArc((14.4, -10.4485281374), 0.1, 0, 135)
                Line((11.3778174593, -13.3292893219), (14.3292893219, -10.3778174593))
                CenterArc((11.4485281374, -13.4), 0.1, 135, 135)
                Line((11.4485281374, -13.5), (14.25, -13.5))
                CenterArc((14.25, -13.25), 0.25, -90, 90)
                Line((14.5, -10.4485281374), (14.5, -13.25))
            make_face()
            # Profile area: 5.3834379341, perimeter: 10.6408932419
            with BuildLine():
                CenterArc((5.6, -10.4485281374), 0.1, 45, 135)
                Line((5.5, -10.4485281374), (5.5, -13.25))
                CenterArc((5.75, -13.25), 0.25, 180, 90)
                Line((5.75, -13.5), (8.5514718626, -13.5))
                CenterArc((8.5514718626, -13.4), 0.1, -90, 135)
                Line((5.6707106781, -10.3778174593), (8.6221825407, -13.3292893219))
            make_face()
            # Profile area: 5.3834379341, perimeter: 10.6408932419
            with BuildLine():
                CenterArc((9.25, -9.75), 0.25, 0, 90)
                Line((6.4485281374, -9.5), (9.25, -9.5))
                CenterArc((6.4485281374, -9.6), 0.1, 90, 135)
                Line((6.3778174593, -9.6707106781), (9.3292893219, -12.6221825407))
                CenterArc((9.4, -12.5514718626), 0.1, -135, 135)
                Line((9.5, -9.75), (9.5, -12.5514718626))
            make_face()
            # Profile area: 5.3834379341, perimeter: 10.6408932419
            with BuildLine():
                CenterArc((10.75, -9.75), 0.25, 90, 90)
                Line((10.5, -9.75), (10.5, -12.5514718626))
                CenterArc((10.6, -12.5514718626), 0.1, 180, 135)
                Line((10.6707106781, -12.6221825407), (13.6221825407, -9.6707106781))
                CenterArc((13.5514718626, -9.6), 0.1, -45, 135)
                Line((10.75, -9.5), (13.5514718626, -9.5))
            make_face()
            # Profile area: 5.3834379341, perimeter: 10.6408932419
            with BuildLine():
                CenterArc((5.75, -3.25), 0.25, 180, 90)
                Line((5.75, -3.5), (8.5514718626, -3.5))
                CenterArc((8.5514718626, -3.4), 0.1, -90, 135)
                Line((8.6221825407, -3.3292893219), (5.6707106781, -0.3778174593))
                CenterArc((5.6, -0.4485281374), 0.1, 45, 135)
                Line((5.5, -0.4485281374), (5.5, -3.25))
            make_face()
            # Profile area: 5.3834379341, perimeter: 10.6408932419
            with BuildLine():
                CenterArc((9.25, 0.25), 0.25, 0, 90)
                Line((6.4485281374, 0.5), (9.25, 0.5))
                CenterArc((6.4485281374, 0.4), 0.1, 90, 135)
                Line((9.3292893219, -2.6221825407), (6.3778174593, 0.3292893219))
                CenterArc((9.4, -2.5514718626), 0.1, -135, 135)
                Line((9.5, 0.25), (9.5, -2.5514718626))
            make_face()
            # Profile area: 5.3834379341, perimeter: 10.6408932419
            with BuildLine():
                CenterArc((10.75, -8.25), 0.25, 180, 90)
                Line((10.75, -8.5), (13.5514718626, -8.5))
                CenterArc((13.5514718626, -8.4), 0.1, -90, 135)
                Line((13.6221825407, -8.3292893219), (10.6707106781, -5.3778174593))
                CenterArc((10.6, -5.4485281374), 0.1, 45, 135)
                Line((10.5, -5.4485281374), (10.5, -8.25))
            make_face()
            # Profile area: 5.3834379341, perimeter: 10.6408932419
            with BuildLine():
                CenterArc((14.4, -7.5514718626), 0.1, -135, 135)
                Line((14.5, -4.75), (14.5, -7.5514718626))
                CenterArc((14.25, -4.75), 0.25, 0, 90)
                Line((11.4485281374, -4.5), (14.25, -4.5))
                CenterArc((11.4485281374, -4.6), 0.1, 90, 135)
                Line((14.3292893219, -7.6221825407), (11.3778174593, -4.6707106781))
            make_face()
        # OneSide extrude, distance=-0.01
        extrude(amount=-0.01)
    return part.part


# Description: These are two parallel strut bars or tie rods with elongated hexagonal bodies, featuring mounting flanges at each end and a central reinforced beam, designed for structural support or suspension bracing applications.
def model_96000_16f93834_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 28 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 46.105203484, perimeter: 31.857102048
            with BuildLine():
                CenterArc((38.1, -6.65), 1.6, -176.4166783015, 86.4166783015)
                Line((38.1, -8.25), (43.37456939, -8.25))
                CenterArc((43.37456939, -6.65), 1.6, -90, 90)
                Line((44.97456939, -6.65), (44.97456939, -3.85))
                CenterArc((43.37456939, -3.85), 1.6, 0, 90)
                Line((43.37456939, -2.25), (40.5, -2.25))
                Line((40.5, -2.25), (38.1, -2.25))
                CenterArc((38.1, -3.85), 1.6, 90, 86.4166783015)
                CenterArc((38.1, -3.85), 1.6, 176.4166783015, 3.5833216985)
                Line((36.5, -3.85), (36.5, -6.65))
                CenterArc((38.1, -6.65), 1.6, 180, 3.5833216985)
            make_face()
            with BuildLine():
                CenterArc((41.97456939, -5.75), 0.9, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 46.105203484, perimeter: 31.857102048
            with BuildLine():
                CenterArc((8.4, -6.65), 1.6, -3.5833216985, 3.5833216985)
                Line((10, -3.85), (10, -6.65))
                CenterArc((8.4, -3.85), 1.6, 0, 3.5833216985)
                CenterArc((8.4, -3.85), 1.6, 3.5833216985, 86.4166783015)
                Line((6, -2.25), (8.4, -2.25))
                Line((4.52543061, -2.25), (6, -2.25))
                Line((3.12543061, -2.25), (4.52543061, -2.25))
                CenterArc((3.12543061, -3.85), 1.6, 90, 90)
                Line((1.52543061, -6.65), (1.52543061, -3.85))
                CenterArc((3.12543061, -6.65), 1.6, 180, 90)
                Line((8.4, -8.25), (3.12543061, -8.25))
                CenterArc((8.4, -6.65), 1.6, -90, 86.4166783015)
            make_face()
            with BuildLine():
                CenterArc((4.52543061, -5.75), 0.9, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 46.105203484, perimeter: 31.857102048
            with BuildLine():
                Line((10, 12.85), (10, 15.65))
                CenterArc((8.4, 15.65), 1.6, 0, 3.5833216985)
                CenterArc((8.4, 15.65), 1.6, 3.5833216985, 86.4166783015)
                Line((8.4, 17.25), (3.12543061, 17.25))
                CenterArc((3.12543061, 15.65), 1.6, 90, 90)
                Line((1.52543061, 15.65), (1.52543061, 12.85))
                CenterArc((3.12543061, 12.85), 1.6, -180, 90)
                Line((3.12543061, 11.25), (4.52543061, 11.25))
                Line((4.52543061, 11.25), (6, 11.25))
                Line((6, 11.25), (8.4, 11.25))
                CenterArc((8.4, 12.85), 1.6, -90, 86.4166783015)
                CenterArc((8.4, 12.85), 1.6, -3.5833216985, 3.5833216985)
            make_face()
            with BuildLine():
                CenterArc((4.52543061, 14.75), 0.9, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 46.105203484, perimeter: 31.857102048
            with BuildLine():
                CenterArc((38.1, 15.65), 1.6, 176.4166783015, 3.5833216985)
                Line((36.5, 12.85), (36.5, 15.65))
                CenterArc((38.1, 12.85), 1.6, 180, 3.5833216985)
                CenterArc((38.1, 12.85), 1.6, -176.4166783015, 86.4166783015)
                Line((40.5, 11.25), (38.1, 11.25))
                Line((43.37456939, 11.25), (40.5, 11.25))
                CenterArc((43.37456939, 12.85), 1.6, -90, 90)
                Line((44.97456939, 15.65), (44.97456939, 12.85))
                CenterArc((43.37456939, 15.65), 1.6, 0, 90)
                Line((38.1, 17.25), (43.37456939, 17.25))
                CenterArc((38.1, 15.65), 1.6, 90, 86.4166783015)
            make_face()
            with BuildLine():
                CenterArc((41.97456939, 14.75), 0.9, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.2
        extrude(amount=2.2)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 28 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 21, perimeter: 20
            with BuildLine():
                Line((28, 12.75), (28, 15.75))
                Line((35, 12.75), (28, 12.75))
                Line((35, 12.75), (35, 15.75))
                Line((35, 15.75), (28, 15.75))
            make_face()
            # Profile area: 28.5, perimeter: 25
            with BuildLine():
                Line((18.5, 12.75), (18.5, 15.75))
                Line((28, 12.75), (18.5, 12.75))
                Line((28, 12.75), (28, 15.75))
                Line((28, 15.75), (18.5, 15.75))
            make_face()
            # Profile area: 4.5002084556, perimeter: 9.0063865532
            with BuildLine():
                Line((35, 12.75), (35, 15.75))
                Line((36.5031280577, 12.75), (35, 12.75))
                CenterArc((38.1, 12.85), 1.6, 180, 3.5833216985)
                Line((36.5, 12.85), (36.5, 15.65))
                CenterArc((38.1, 15.65), 1.6, 176.4166783015, 3.5833216985)
                Line((36.5031280577, 15.75), (35, 15.75))
            make_face()
            # Profile area: 4.5002084556, perimeter: 9.0063865532
            with BuildLine():
                CenterArc((8.4, 12.85), 1.6, -3.5833216985, 3.5833216985)
                Line((11.5, 12.75), (9.9968719423, 12.75))
                Line((11.5, 12.75), (11.5, 15.75))
                Line((11.5, 15.75), (9.9968719423, 15.75))
                CenterArc((8.4, 15.65), 1.6, 0, 3.5833216985)
                Line((10, 12.85), (10, 15.65))
            make_face()
            # Profile area: 21, perimeter: 20
            with BuildLine():
                Line((18.5, 12.75), (11.5, 12.75))
                Line((18.5, 12.75), (18.5, 15.75))
                Line((18.5, 15.75), (11.5, 15.75))
                Line((11.5, 12.75), (11.5, 15.75))
            make_face()
            # Profile area: 4.5002084556, perimeter: 9.0063865532
            with BuildLine():
                CenterArc((38.1, -6.65), 1.6, 180, 3.5833216985)
                Line((36.5, -3.85), (36.5, -6.65))
                CenterArc((38.1, -3.85), 1.6, 176.4166783015, 3.5833216985)
                Line((36.5031280577, -3.75), (35, -3.75))
                Line((35, -3.75), (35, -6.75))
                Line((36.5031280577, -6.75), (35, -6.75))
            make_face()
            # Profile area: 21, perimeter: 20
            with BuildLine():
                Line((35, -3.75), (28, -3.75))
                Line((28, -3.75), (28, -6.75))
                Line((35, -6.75), (28, -6.75))
                Line((35, -3.75), (35, -6.75))
            make_face()
            # Profile area: 4.5002084556, perimeter: 9.0063865532
            with BuildLine():
                Line((11.5, -3.75), (11.5, -6.75))
                Line((11.5, -3.75), (9.9968719423, -3.75))
                CenterArc((8.4, -3.85), 1.6, 0, 3.5833216985)
                Line((10, -3.85), (10, -6.65))
                CenterArc((8.4, -6.65), 1.6, -3.5833216985, 3.5833216985)
                Line((11.5, -6.75), (9.9968719423, -6.75))
            make_face()
            # Profile area: 21, perimeter: 20
            with BuildLine():
                Line((18.5, -3.75), (18.5, -6.75))
                Line((18.5, -3.75), (11.5, -3.75))
                Line((11.5, -3.75), (11.5, -6.75))
                Line((18.5, -6.75), (11.5, -6.75))
            make_face()
            # Profile area: 28.5, perimeter: 25
            with BuildLine():
                Line((28, -3.75), (28, -6.75))
                Line((28, -3.75), (18.5, -3.75))
                Line((18.5, -3.75), (18.5, -6.75))
                Line((28, -6.75), (18.5, -6.75))
            make_face()
        # TwoSides offset extrude, full=2.2, trim=0.5
        extrude(amount=2.2, mode=Mode.ADD)
        extrude(sk.sketch, amount=0.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is an elongated hexagonal or wedge-shaped structural component with a tapered profile, featuring internal diagonal bracing ribs and recessed slots along its length for lightweight reinforcement.
def model_96151_49bcd93d_0003():
    """Model: Component4"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 935.4143466935, perimeter: 124.8331477355
            with BuildLine():
                Line((-45.8198199688, 0.3005973047), (-45.8198199688, -37.115976563))
                Line((-45.8198199688, -37.115976563), (-20.8198199688, -37.115976563))
                Line((-20.8198199688, -37.115976563), (-20.8198199688, 0.3005973047))
                Line((-20.8198199688, 0.3005973047), (-45.8198199688, 0.3005973047))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 757.1646250903, perimeter: 112.8331477355
            with BuildLine():
                Line((-44.3198199688, 1.1994026953), (-22.3198199688, 1.1994026953))
                Line((-22.3198199688, 1.1994026953), (-22.3198199688, 35.615976563))
                Line((-22.3198199688, 35.615976563), (-44.3198199688, 35.615976563))
                Line((-44.3198199688, 35.615976563), (-44.3198199688, 1.1994026953))
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a trapezoidal prism or wedge-shaped structural component with a tapered profile, featuring a large flat face and an angled side surface with visible internal geometry and edge details.
def model_97732_4959b064_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 9 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 575.7241516806, perimeter: 101.6128926473
            with BuildLine():
                Line((0.2606390817, 41.9220190609), (0.2606390817, 37.9220190609))
                Line((0.2606390817, 37.9220190609), (7.6981318329, 14.7814655355))
                Line((7.6981318329, 14.7814655355), (7.7128784692, 10.7814927185))
                Line((7.7128784692, 10.7814927185), (18.7128784692, 10.8220462439))
                Line((18.7128784692, 10.8220462439), (18.6981318329, 14.8220190609))
                Line((18.6981318329, 14.8220190609), (26.2606390817, 37.9220190609))
                Line((26.2606390817, 41.9220190609), (26.2606390817, 37.9220190609))
                Line((0.2606390817, 41.9220190609), (26.2606390817, 41.9220190609))
            make_face()
        # OneSide extrude, distance=6
        extrude(amount=6)

        # Sketch5 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(18.7525210578, 0.0691346218, 0), x_dir=(0, 0, -1), z_dir=(0.9999932042, 0.0036866591, 0))):
            # Profile area: 1.5, perimeter: 7
            with BuildLine():
                Line((-4.5000000671, 14.7529846968), (-4.5000000671, 14.2529846968))
                Line((-4.5000000671, 14.2529846968), (-1.5000000671, 14.2529846968))
                Line((-1.5000000671, 14.2529846968), (-1.5000000671, 14.7529846968))
                Line((-1.5000000671, 14.7529846968), (-4.5000000671, 14.7529846968))
            make_face()
        # OneSide extrude, distance=-15
        extrude(amount=-15, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a mummy sleeping bag with a tapered, elongated pod-like shape, featuring a dark outer shell, blue interior lining, and a contoured hood section at the head end for thermal insulation and comfort.
def model_97733_4ac743c3_0000():
    """Model: BracePlate1"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.5), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.5028223913, perimeter: 7.0567854033
            with BuildLine():
                Line((-1.9422616568, 2.1463497875), (-1.9422616568, 2.6463497875))
                Line((-1.9422616568, 2.6463497875), (-4.8214969462, 2.6463497875))
                CenterArc((0, 0), 5.5, 151.2391681474, 5.7910610968)
                Line((-1.9422616568, 2.1463497875), (-5.0639098125, 2.1463497875))
            make_face()
            # Profile area: 2.2760467803, perimeter: 10.1704951996
            with BuildLine():
                CenterArc((0, 0), 5.5, 151.2391681474, 5.7910610968)
                Line((-4.8214969462, 2.6463497875), (-9.5, 2.6463497875))
                Line((-9.5, 2.1463497875), (-9.5, 2.6463497875))
                Line((-5.0639098125, 2.1463497875), (-9.5, 2.1463497875))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch4 -> Extrude2 (Intersect)
        # Sketch on BRepFace
        # Sketch has 14 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -2.6463497875, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 17.5898283079, perimeter: 22.4611495805
            with BuildLine():
                CenterArc((9, 1), 0.5, -90, 90)
                Line((9.5, 2.0000000186), (9.5, 1))
                CenterArc((8, 2.0000000186), 1.5, 0, 89.9999992885)
                Line((5.5752551904, 3.5000000487), (8.0000000186, 3.5000000186))
                CenterArc((5.575255178, 2.5000000487), 1, 89.9999992885, 30.7796789842)
                Line((2.430523481, 1.7908278177), (5.0635170021, 3.3591415035))
                CenterArc((2.9422616568, 0.9316863629), 1, 120.7796782727, 59.2203217273)
                Line((1.9422616568, 0.5), (1.9422616568, 0.9316863629))
                Line((9, 0.5), (1.9422616568, 0.5))
            make_face()
            with BuildLine():
                CenterArc((8, 2.0000000186), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.INTERSECT)
    return part.part


# Description: This image shows two cylindrical components: a larger oval or elliptical ring with internal geometric ribbing/mesh pattern on the left, and a smaller solid cylindrical cap or plug on the right, appearing to be assembly parts for a mechanical or engineering application.
def model_98114_3ee5d793_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            Circle(2.5)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch3 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.3407112858, perimeter: 8.9263502047
            with Locations((6.978264213, -0.0822354369)):
                Circle(1.4206727588)
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a cylindrical roller or spacer with a smooth, rounded body featuring a textured or mesh-patterned surface on the upper portion, tapering slightly toward rounded ends.
def model_98199_1b94ba49_0000():
    """Model: Piston"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 11.611), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))) as sk:
            # Profile area: 4.9087385212, perimeter: 7.853981634
            Circle(1.25)
        # TwoSides extrude, along=3.97, against=-2
        extrude(amount=3.97)
        extrude(sk.sketch, amount=-2)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 15.581), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=-1.3
        extrude(amount=-1.3, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 15.581), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 2.2619467106, perimeter: 7.5398223686
            with BuildLine():
                CenterArc((0, 0), 0.9, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.32
        extrude(amount=-0.32, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a four-pointed ninja throwing star (shuriken) featuring a central circular hole, symmetrical blade-shaped points with sharp edges, and ribbed or fluted surface details along the arms.
def model_98277_baf4f456_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 59.8515400673, perimeter: 43.2845707968
            with BuildLine():
                Line((-6.0621778265, -3.5), (6.0621778265, -3.5))
                Line((6.0621778265, -3.5), (0, 7))
                Line((0, 7), (-6.0621778265, -3.5))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.7, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.7247647842, perimeter: 5.5097562611
            with BuildLine():
                Line((-1.2311061285, 1.7578723952), (-3.0265437838, 1.7578723952))
                Line((-3.0265437838, 1.7578723952), (-3.0356340427, 1.7421276048))
                Line((-3.0356340427, 1.7421276048), (-2.1379152151, 0.1872329844))
                CenterArc((-3.0310889132, 1.75), 1.8, -60.2505869201, 60.5011738403)
            make_face()
            # Profile area: 1.6823076573, perimeter: 5.4634305682
            with BuildLine():
                Line((-3.0356340427, 1.7421276048), (-2.1379152151, 0.1872329844))
                Line((-3.0356340427, 1.7421276048), (-3.9310889132, 0.1911542732))
                CenterArc((-3.0310889132, 1.75), 1.8, -120, 59.7494130799)
            make_face()
            # Profile area: 1.6823076573, perimeter: 5.4634305682
            with BuildLine():
                CenterArc((-3.0310889132, 1.75), 1.8, 0.2505869201, 59.7494130799)
                Line((-2.1310889132, 3.3088457268), (-3.0265437838, 1.7578723952))
                Line((-1.2311061285, 1.7578723952), (-3.0265437838, 1.7578723952))
            make_face()
            # Profile area: 1.7300444739, perimeter: 5.5182142305
            with BuildLine():
                Line((0.0090902589, -3.5), (0.9081969187, -1.9427015839))
                CenterArc((0, -3.5), 1.8027756377, 59.7497988977, 60.5004022047)
                Line((-0.9081969187, -1.9427015839), (-0.0090902589, -3.5))
                Line((-0.0090902589, -3.5), (0.0090902589, -3.5))
            make_face()
            # Profile area: 1.6875217941, perimeter: 5.4718885113
            with BuildLine():
                Line((0.0090902589, -3.5), (1.8027756377, -3.5))
                CenterArc((0, -3.5), 1.8027756377, 0, 59.7497988977)
                Line((0.0090902589, -3.5), (0.9081969187, -1.9427015839))
            make_face()
            # Profile area: 1.6875217941, perimeter: 5.4718885113
            with BuildLine():
                Line((-0.9081969187, -1.9427015839), (-0.0090902589, -3.5))
                CenterArc((0, -3.5), 1.8027756377, 120.2502011023, 59.7497988977)
                Line((-1.8027756377, -3.5), (-0.0090902589, -3.5))
            make_face()
            # Profile area: 1.7534370542, perimeter: 5.5707314145
            with BuildLine():
                CenterArc((3.0538185047, 1.7106311927), 1.8, -121.0026131033, 61.0026131033)
                Line((3.9538185047, 0.1517854659), (3.0356340427, 1.7421276048))
                Line((2.1266796034, 0.1677723341), (3.0356340427, 1.7421276048))
            make_face()
            # Profile area: 1.7238631678, perimeter: 5.5088988436
            with BuildLine():
                Line((2.1266796034, 0.1677723341), (3.0356340427, 1.7421276048))
                Line((3.0356340427, 1.7421276048), (3.0265437838, 1.7578723952))
                Line((3.0265437838, 1.7578723952), (1.2544385369, 1.7578723952))
                CenterArc((3.0538185047, 1.7106311927), 1.8, 178.4960931383, 60.5012937584)
            make_face()
            # Profile area: 1.6120798768, perimeter: 5.3552647697
            with BuildLine():
                Line((3.0265437838, 1.7578723952), (1.2544385369, 1.7578723952))
                Line((3.0265437838, 1.7578723952), (2.1538185047, 3.2694769195))
                CenterArc((3.0538185047, 1.7106311927), 1.8, 120, 58.4960931383)
            make_face()
        # OneSide extrude, distance=-2.5
        extrude(amount=-2.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical mesh or perforated filter/strainer component with a rounded cap-like top, solid base, and ventilated mesh sections along the sides, featuring a small protruding nozzle or connector at the bottom.
def model_98300_5afcf0f2_0000():
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
            # Profile area: 0.898093403, perimeter: 3.3594306882
            Circle(0.53467)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0208000255, perimeter: 0.5581023896
            with BuildLine():
                _nurbs_edge([(0.5928938767, -0.0673311686), (0.5932367562, -0.0673694895), (0.593922607, -0.0674365486), (0.5949516583, -0.0675083893), (0.596324387, -0.0675494304), (0.5980420086, -0.0675254677), (0.5997620717, -0.0674466491), (0.6014852157, -0.0673332275), (0.6032117674, -0.067200513), (0.6049415485, -0.0670546412), (0.6066740537, -0.0668954578), (0.6084086085, -0.0667189729), (0.6101445293, -0.0665199055), (0.6118812925, -0.0662943431), (0.6136186695, -0.0660418939), (0.6153566252, -0.0657643889), (0.6170952415, -0.0654649505), (0.6188346349, -0.0651469603), (0.6205748692, -0.0648129813), (0.622315892, -0.0644639705), (0.6240575798, -0.0640998702), (0.625799769, -0.0637200089), (0.6275422898, -0.0633235553), (0.6292850035, -0.062909997), (0.6310278262, -0.0624794621), (0.6327707084, -0.0620324618), (0.6345136219, -0.0615697273), (0.6362565446, -0.0610920184), (0.6379994435, -0.0605999231), (0.6397422655, -0.0600937311), (0.6414849452, -0.0595735479), (0.6432274109, -0.0590393658), (0.6449695906, -0.0584911474), (0.6467114189, -0.0579289147), (0.648452841, -0.0573528025), (0.6501938088, -0.05676301), (0.6519342785, -0.0561597717), (0.6536742079, -0.0555433226), (0.6554135532, -0.0549138615), (0.6571522674, -0.0542715292), (0.6588903018, -0.0536164298), (0.6606276068, -0.0529486436), (0.6623641332, -0.0522682429), (0.664099833, -0.0515753083), (0.6658346605, -0.0508699386), (0.6675685714, -0.0501522425), (0.6693015227, -0.0494223324), (0.6710334722, -0.0486803188), (0.6727643782, -0.0479263033), (0.674494199, -0.047160375), (0.6762228928, -0.0463826138), (0.6779504179, -0.0455930939), (0.6796767322, -0.0447918862), (0.6814017933, -0.0439790618), (0.6831255586, -0.0431546947), (0.6848479856, -0.0423188588), (0.6865690329, -0.0414716277), (0.6882886604, -0.0406130723), (0.6900068306, -0.0397432597), (0.6917235082, -0.0388622524), (0.6934386587, -0.0379701096), (0.6951522466, -0.0370668891), (0.6968642341, -0.036152648), (0.6985745792, -0.0352274452), (0.7002832344, -0.034291342), (0.7019901511, -0.0333443998), (0.7036952827, -0.0323866783), (0.7053985882, -0.0314182333), (0.7071000355, -0.0304391147), (0.7087996054, -0.0294493646), (0.7104972875, -0.0284490168), (0.7118539202, -0.0276402804), (0.7128705436, -0.0270289771), (0.7135479143, -0.0266193309), (0.7138865052, -0.02641398)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((0, 0), 0.714375, -2.1189916072, 4.2379832145)
                _nurbs_edge([(0.5928938767, 0.0673311686), (0.5932367562, 0.0673694895), (0.593922607, 0.0674365486), (0.5949516583, 0.0675083893), (0.596324387, 0.0675494304), (0.5980420086, 0.0675254677), (0.5997620717, 0.0674466491), (0.6014852157, 0.0673332275), (0.6032117674, 0.067200513), (0.6049415485, 0.0670546412), (0.6066740537, 0.0668954578), (0.6084086085, 0.0667189729), (0.6101445293, 0.0665199055), (0.6118812925, 0.0662943431), (0.6136186695, 0.0660418939), (0.6153566252, 0.0657643889), (0.6170952415, 0.0654649505), (0.6188346349, 0.0651469603), (0.6205748692, 0.0648129813), (0.622315892, 0.0644639705), (0.6240575798, 0.0640998702), (0.625799769, 0.0637200089), (0.6275422898, 0.0633235553), (0.6292850035, 0.062909997), (0.6310278262, 0.0624794621), (0.6327707084, 0.0620324618), (0.6345136219, 0.0615697273), (0.6362565446, 0.0610920184), (0.6379994435, 0.0605999231), (0.6397422655, 0.0600937311), (0.6414849452, 0.0595735479), (0.6432274109, 0.0590393658), (0.6449695906, 0.0584911474), (0.6467114189, 0.0579289147), (0.648452841, 0.0573528025), (0.6501938088, 0.05676301), (0.6519342785, 0.0561597717), (0.6536742079, 0.0555433226), (0.6554135532, 0.0549138615), (0.6571522674, 0.0542715292), (0.6588903018, 0.0536164298), (0.6606276068, 0.0529486436), (0.6623641332, 0.0522682429), (0.664099833, 0.0515753083), (0.6658346605, 0.0508699386), (0.6675685714, 0.0501522425), (0.6693015227, 0.0494223324), (0.6710334722, 0.0486803188), (0.6727643782, 0.0479263033), (0.674494199, 0.047160375), (0.6762228928, 0.0463826138), (0.6779504179, 0.0455930939), (0.6796767322, 0.0447918862), (0.6814017933, 0.0439790618), (0.6831255586, 0.0431546947), (0.6848479856, 0.0423188588), (0.6865690329, 0.0414716277), (0.6882886604, 0.0406130723), (0.6900068306, 0.0397432597), (0.6917235082, 0.0388622524), (0.6934386587, 0.0379701096), (0.6951522466, 0.0370668891), (0.6968642341, 0.036152648), (0.6985745792, 0.0352274452), (0.7002832344, 0.034291342), (0.7019901511, 0.0333443998), (0.7036952827, 0.0323866783), (0.7053985882, 0.0314182333), (0.7071000355, 0.0304391147), (0.7087996054, 0.0294493646), (0.7104972875, 0.0284490168), (0.7118539202, 0.0276402804), (0.7128705436, 0.0270289771), (0.7135479143, 0.0266193309), (0.7138865052, 0.02641398)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                Line((0.530261643, 0.0603312644), (0.5928938767, 0.0673311686))
                Line((0.530261643, -0.0603312644), (0.530261643, 0.0603312644))
                Line((0.530261643, -0.0603312644), (0.5928938767, -0.0673311686))
            make_face()
        # OneSide extrude, distance=0.8
        extrude(amount=0.8, mode=Mode.ADD)
    return part.part


# Description: This is a curved hose or conduit component with a serpentine S-shape, featuring a small flanged elbow on one end and a tapered outlet on the other, designed to route flexible tubing or cables in a confined space.
def model_98404_8bfd7519_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 19 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.8258497583, perimeter: 11.6200157504
            with BuildLine():
                CenterArc((0.2743493376, 3.8493932876), 3.6609011086, 69.2254828708, 25.0723140912)
                Line((0, 7.5), (0, 7.394619229))
                CenterArc((0.2743493376, 3.8493932876), 3.5558254364, 65.1826184913, 29.242429073)
                CenterArc((2.0606360984, 7.7121940531), 0.7, -114.8173815087, 22.4696834321)
                CenterArc((1.9985449793, 6.1977029487), 0.8157633761, 2.5788922494, 85.073409674)
                CenterArc((3.9664755229, 6.320647324), 1.1562140284, -175.7224777358, 53.0322856915)
                CenterArc((3.6120567793, 5.7683754659), 0.5, -122.6901920443, 44.2244075197)
                CenterArc((3.7655092231, 5.0164313499), 0.2674422493, -58.8609607661, 160.3951762415)
                Line((3.9038080599, 4.7875235334), (3.9581444382, 4.6975876958))
                CenterArc((3.7655092231, 5.0164313499), 0.3725179216, -58.8609607661, 154.7165208451)
                CenterArc((3.6662919804, 5.9838749124), 0.6, -131.7123527583, 47.5679128373)
                CenterArc((3.9664755229, 6.320647324), 1.0511383562, -138.7377584062, 7.0254056479)
                CenterArc((3.6273553092, 6.0231186749), 0.6, 173.8821009416, 47.3801406522)
                CenterArc((1.9985449793, 6.1977029487), 1.0381400304, -6.1178990584, 101.9766344595)
                CenterArc((1.8211223853, 7.9267639623), 0.7, -110.7745171292, 26.6332525303)
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)
    return part.part


# Description: This is a composite mechanical part featuring a cylindrical lower section with a rectangular upper box section, designed with multiple internal passages and geometric complexity, likely serving as a manifold, adapter, or junction component in a hydraulic or pneumatic system.
def model_98960_2725c9ae_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 136.925, perimeter: 47.9865007051
            with BuildLine():
                Line((3.8, -13.9), (12.7, -5))
                Line((12.7, 0), (12.7, -5))
                Line((12.7, 0), (0, 0))
                Line((0, -13.9), (0, 0))
                Line((0, -13.9), (3.8, -13.9))
            make_face()
        # Symmetric extrude, full_length=True, total=7.6
        extrude(amount=3.8, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 61.4422989589, perimeter: 29.7380520836
            with BuildLine():
                Line((7.6, 3.8), (0, 3.8))
                Line((7.6, 8.9), (7.6, 3.8))
                CenterArc((3.8, 8.9), 3.8, 0, 180)
                Line((0, 8.9), (0, 3.8))
            make_face()
        # OneSide extrude, distance=-2.6
        extrude(amount=-2.6, mode=Mode.ADD)
    return part.part


# Description: This is a bent or folded sheet metal bracket with an angular, asymmetrical shape featuring multiple planar faces, internal cavities, and sharp edges designed to function as a mounting or structural component.
def model_99101_b40b79b1_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 70.1666235604, perimeter: 48.5148882821
            with BuildLine():
                Line((15, 0), (15, 2))
                Line((15, 2), (13.1801488287, 7))
                Line((13.1801488287, 7), (9.0922744052, 7))
                Line((9.0922744052, 7), (9.0922744052, 0.9930747045))
                Line((9.0922744052, 0.9930747045), (8.0922744052, 0.9930747045))
                Line((8.0922744052, 0.9930747045), (8.0922744052, 4))
                Line((8.0922744052, 4), (0, 4))
                Line((0, 4), (0, 0))
                Line((0, 0), (15, 0))
            make_face()
        # Symmetric extrude, full_length=True, total=7
        extrude(amount=3.5, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 42.5536464315, perimeter: 26.1845488105
            with BuildLine():
                Line((-0.5, -3), (-0.5, 3))
                Line((-0.5, 3), (-7.5922744052, 3))
                Line((-7.5922744052, 3), (-7.5922744052, -3))
                Line((-7.5922744052, -3), (-0.5, -3))
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a dark gray dual-chamber enclosure or housing with a rounded, pill-shaped overall form, featuring multiple circular ventilation holes and mesh openings on the top and sides for cooling or airflow management.
def model_99549_61e3db73_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0002873816, perimeter: 0.3485482271
            with BuildLine():
                Line((-4.1023649465, 2.3635919367), (-3.9298264721, 2.3393922918))
                CenterArc((-4.2289688242, 0.8337507301), 1.5350708971, 78.7627530932, 6.5064448141)
            make_face()
            # Profile area: 3.8476399149, perimeter: 14.0122947299
            with BuildLine():
                CenterArc((-4.2289688242, 0.8337507301), 1.5350708971, -79.3554168075, 158.1181699008)
                Line((-3.9454164536, -0.6749045361), (-0.6930756124, -0.2329335086))
                CenterArc((-0.6454231143, 0.8268009127), 1.0608052622, 92.8962803927, 174.5290659953)
                Line((-3.9298264721, 2.3393922918), (-0.6990235926, 1.8862511442))
            make_face()
            # Profile area: 2.6859855042, perimeter: 9.9320819349
            with BuildLine():
                CenterArc((-0.6454231143, 0.8268009127), 1.0608052622, 92.8962803927, 174.5290659953)
                CenterArc((-0.6454231143, 0.8268009127), 1.0608052622, -92.5746536121, 185.4709340047)
            make_face()
            with BuildLine():
                CenterArc((-0.6454231143, 0.8268009127), 0.519934673, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 5.0017744369, perimeter: 15.1375413659
            with BuildLine():
                CenterArc((-4.2289688242, 0.8337507301), 1.5350708971, 85.2691979073, 189.5636244909)
                Line((-4.0996411284, -0.6958626217), (-3.9454164536, -0.6749045361))
                CenterArc((-4.2289688242, 0.8337507301), 1.5350708971, -79.3554168075, 158.1181699008)
                Line((-4.1023649465, 2.3635919367), (-3.9298264721, 2.3393922918))
            make_face()
            with BuildLine():
                CenterArc((-4.2289688242, 0.8337507301), 0.8741691652, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.8492732267, perimeter: 3.2668458978
            with Locations((-0.6454231143, 0.8268009127)):
                Circle(0.519934673)
            # Profile area: 2.4007162914, perimeter: 5.492566855
            with Locations((-4.2289688242, 0.8337507301)):
                Circle(0.8741691652)
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.6859855042, perimeter: 9.9320819349
            with BuildLine():
                CenterArc((-0.6454231143, 0.8268009127), 1.0608052622, 92.8962803927, 174.5290659953)
                CenterArc((-0.6454231143, 0.8268009127), 1.0608052622, -92.5746536121, 185.4709340047)
            make_face()
            with BuildLine():
                CenterArc((-0.6454231143, 0.8268009127), 0.519934673, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XY construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 5.0017744369, perimeter: 15.1375413659
            with BuildLine():
                CenterArc((-4.2289688242, 0.8337507301), 1.5350708971, 85.2691979073, 189.5636244909)
                Line((-4.0996411284, -0.6958626217), (-3.9454164536, -0.6749045361))
                CenterArc((-4.2289688242, 0.8337507301), 1.5350708971, -79.3554168075, 158.1181699008)
                Line((-4.1023649465, 2.3635919367), (-3.9298264721, 2.3393922918))
            make_face()
            with BuildLine():
                CenterArc((-4.2289688242, 0.8337507301), 0.8741691652, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=4
        extrude(amount=4, mode=Mode.ADD)

        # Sketch1 -> Extrude4 (Cut)
        # Sketch on XY construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.4007162914, perimeter: 5.492566855
            with Locations((-4.2289688242, 0.8337507301)):
                Circle(0.8741691652)
            # Profile area: 0.8492732267, perimeter: 3.2668458978
            with Locations((-0.6454231143, 0.8268009127)):
                Circle(0.519934673)
        # OneSide extrude, distance=6
        extrude(amount=6, mode=Mode.SUBTRACT)
    return part.part


MODELS = {
    "model_87358_854d47fe_0004": {"func": model_87358_854d47fe_0004, "volume": 598.56, "area": 888.08},
    "model_87373_a5e91136_0000": {"func": model_87373_a5e91136_0000, "volume": 18.75, "area": 87.9154759474},
    "model_87757_eb92dadf_0000": {"func": model_87757_eb92dadf_0000, "volume": 0.0235617297, "area": 1.0390426915},
    "model_87951_500b1dcd_0000": {"func": model_87951_500b1dcd_0000, "volume": 715707.9632679494, "area": 53440.2649398591},
    "model_88060_389bdff4_0000": {"func": model_88060_389bdff4_0000, "volume": 2375.0440461139, "area": 1583.3626974093},
    "model_88219_05eb53c9_0000": {"func": model_88219_05eb53c9_0000, "volume": 24.7639121108, "area": 99.4314242277},
    "model_88317_a9fa6cf2_0000": {"func": model_88317_a9fa6cf2_0000, "volume": 1130.4383596051, "area": 2909.2976644176},
    "model_89527_b3bf425d_0004": {"func": model_89527_b3bf425d_0004, "volume": 0.7820374275, "area": 16.4622011147},
    "model_89527_b3bf425d_0018": {"func": model_89527_b3bf425d_0018, "volume": 0.0604756586, "area": 0.9738937226},
    "model_89527_b3bf425d_0027": {"func": model_89527_b3bf425d_0027, "volume": 1.3265374977, "area": 12.7077422847},
    "model_89527_b3bf425d_0032": {"func": model_89527_b3bf425d_0032, "volume": 1.4292370856, "area": 10.7492742111},
    "model_89824_94d89a7c_0000": {"func": model_89824_94d89a7c_0000, "volume": 0.0534960964, "area": 1.1414683058},
    "model_89934_c31d503d_0000": {"func": model_89934_c31d503d_0000, "volume": 1230.0827404345, "area": 2087.7285812731},
    "model_90628_b8795213_0011": {"func": model_90628_b8795213_0011, "volume": 1.7508134973, "area": 12.8985669515},
    "model_90721_92ea8254_0000": {"func": model_90721_92ea8254_0000, "volume": 19.8106243746, "area": 78.9815216613},
    "model_90917_39defb9c_0000": {"func": model_90917_39defb9c_0000, "volume": 41.3673079998, "area": 186.4301457142},
    "model_90917_3d2d21a9_0000": {"func": model_90917_3d2d21a9_0000, "volume": 20.7786470067, "area": 82.029993026},
    "model_90917_4670b560_0000": {"func": model_90917_4670b560_0000, "volume": 3.0058478489, "area": 26.878515094},
    "model_90999_1320f1ab_0021": {"func": model_90999_1320f1ab_0021, "volume": 0.0007388284, "area": 0.0532176303},
    "model_91100_df680fe7_0002": {"func": model_91100_df680fe7_0002, "volume": 0.7331238295, "area": 9.2877868423},
    "model_91208_3ef96086_0001": {"func": model_91208_3ef96086_0001, "volume": 171.8058482432, "area": 284.7068342316},
    "model_91292_7f12120b_0000": {"func": model_91292_7f12120b_0000, "volume": 355.3075267256, "area": 423.0603906365},
    "model_91411_4c4628c8_0000": {"func": model_91411_4c4628c8_0000, "volume": 0.1209513172, "area": 1.3980087308},
    "model_91412_b926c9f0_0000": {"func": model_91412_b926c9f0_0000, "volume": 1114.3008881569, "area": 709.6991118431},
    "model_91426_d0eb0ffa_0000": {"func": model_91426_d0eb0ffa_0000, "volume": 29.5, "area": 104},
    "model_91466_9983a0f3_0000": {"func": model_91466_9983a0f3_0000, "volume": 1955722.8689445716, "area": 996671.461644613},
    "model_91542_02495a22_0000": {"func": model_91542_02495a22_0000, "volume": 116.4159265359, "area": 167.0486677646},
    "model_91555_fecd461a_0000": {"func": model_91555_fecd461a_0000, "volume": 8.0503813862, "area": 40.247869711},
    "model_91604_bfe95003_0000": {"func": model_91604_bfe95003_0000, "volume": 30.9623889804, "area": 90.2743362432},
    "model_91694_4d2b7754_0000": {"func": model_91694_4d2b7754_0000, "volume": 0.9232185139, "area": 14.4891730126},
    "model_92030_4f061297_0000": {"func": model_92030_4f061297_0000, "volume": 470.967189144, "area": 492.6208557691},
    "model_92043_9b7b2ecc_0000": {"func": model_92043_9b7b2ecc_0000, "volume": 19.6502269395, "area": 131.8725987909},
    "model_92286_045b32ee_0000": {"func": model_92286_045b32ee_0000, "volume": 1.5933185609, "area": 19.3584067435},
    "model_92286_d48d120d_0000": {"func": model_92286_d48d120d_0000, "volume": 20.1501752801, "area": 67.9212331706},
    "model_92461_da2a8a13_0001": {"func": model_92461_da2a8a13_0001, "volume": 0.9443620089, "area": 9.7157425304},
    "model_92644_539a4676_0001": {"func": model_92644_539a4676_0001, "volume": 7.8776144968, "area": 26.9735132319},
    "model_93197_ce30c6aa_0000": {"func": model_93197_ce30c6aa_0000, "volume": 45.4735841171, "area": 449.2241930254},
    "model_95620_940f6521_0000": {"func": model_95620_940f6521_0000, "volume": 6.2598739764, "area": 810.074742251},
    "model_96000_16f93834_0000": {"func": model_96000_16f93834_0000, "volume": 676.0272081573, "area": 1127.0274481479},
    "model_96151_49bcd93d_0003": {"func": model_96151_49bcd93d_0003, "volume": 4449.9223459403, "area": 2528.844376385},
    "model_97732_4959b064_0000": {"func": model_97732_4959b064_0000, "volume": 3437.8447979531, "area": 1835.1261825215},
    "model_97733_4ac743c3_0000": {"func": model_97733_4ac743c3_0000, "volume": 8.7949141948, "area": 46.4102312428},
    "model_98114_3ee5d793_0000": {"func": model_98114_3ee5d793_0000, "volume": 32.3163766566, "area": 85.5119944188},
    "model_98199_1b94ba49_0000": {"func": model_98199_1b94ba49_0000, "volume": 28.2137796839, "area": 60.3625612461},
    "model_98277_baf4f456_0000": {"func": model_98277_baf4f456_0000, "volume": 31.1973842653, "area": 123.7520214569},
    "model_98300_5afcf0f2_0000": {"func": model_98300_5afcf0f2_0000, "volume": 0.7347994585, "area": 4.7760009171},
    "model_98404_8bfd7519_0000": {"func": model_98404_8bfd7519_0000, "volume": 0.3303399033, "area": 6.2997058169},
    "model_98960_2725c9ae_0000": {"func": model_98960_2725c9ae_0000, "volume": 1200.3799772932, "area": 799.2309386942},
    "model_99101_b40b79b1_0000": {"func": model_99101_b40b79b1_0000, "volume": 406.0590720601, "area": 532.3065627163},
    "model_99549_61e3db73_0000": {"func": model_99549_61e3db73_0000, "volume": 35.760908853, "area": 111.5720236155},
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
