"""Batch 005 - passing/01_2ops
145 models bundled from Fusion360 Gallery reconstructions.
"""

from build123d import *
from build123d import Edge, BuildLine
from collections import Counter
from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
from OCP.Geom import Geom_BSplineCurve
from OCP.TColStd import TColStd_Array1OfReal, TColStd_Array1OfInteger
from OCP.TColgp import TColgp_Array1OfPnt
from OCP.gp import gp_Pnt


# Description: This is a cylindrical flange coupling with a large central hole, featuring radial ridging or ribbing around its outer surface and a tapered conical protrusion extending from one side, designed to connect two shafts or provide mechanical alignment.
def model_139925_2aab35d1_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 17.5852881156, perimeter: 24.1748319571
            with BuildLine():
                CenterArc((0, 0), 10, 79.8173355963, 20.3653288073)
                Line((0, 20), (1.7678695081, 9.8424914225))
                Line((-1.7678695081, 9.8424914225), (0, 20))
            make_face()
            # Profile area: 294.524311274, perimeter: 78.5398163397
            with BuildLine():
                CenterArc((0, 0), 10, 100.1826644037, 339.6346711927)
                CenterArc((0, 0), 10, 79.8173355963, 20.3653288073)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)
    return part.part


# Description: This is a shoe sole or footwear insole featuring an elongated curved shape with a textured tread pattern on the bottom surface and blue linear grip markings concentrated on the heel and forefoot areas.
def model_139978_a15b18af_0000():
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
        # Sketch has 13 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 19.6014992539, perimeter: 25.8264593469
            with BuildLine():
                _nurbs_edge([(2.4101662286, -1.4752081853), (2.4034748641, -1.4754171658), (2.3738529658, -1.4762968598), (2.3197959492, -1.4775499185), (2.2382162409, -1.4785633753), (2.1244041425, -1.4783773055), (1.9815303381, -1.4759218101), (1.8290662474, -1.4710862041), (1.6687644161, -1.4637111225), (1.503509598, -1.4536318906), (1.3367725584, -1.4406801618), (1.1722441923, -1.4246944709), (1.0133950525, -1.4055394499), (0.8631087817, -1.3831271315), (0.7231291478, -1.3574633326), (0.5942044237, -1.3286226535), (0.5000495901, -1.3030819186), (0.4344350476, -1.2825725849), (0.3928991221, -1.2683023411), (0.3726829221, -1.2610178815)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.0470426499, 0.0470426499, 0.0470426499, 0.0470426499, 0.0470426499, 0.0470426499, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9333333333, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((-0.512222314, -2.4721919908), 1.5, 53.8474748271, 252.3050503459)
                _nurbs_edge([(2.4101662286, -3.4691757963), (2.4034748641, -3.4689668158), (2.3738529658, -3.4680871218), (2.3197959492, -3.4668340631), (2.2382162409, -3.4658206063), (2.1244041425, -3.4660066762), (1.9815303381, -3.4684621716), (1.8290662474, -3.4732977775), (1.6687644161, -3.4806728591), (1.503509598, -3.490752091), (1.3367725584, -3.5037038198), (1.1722441923, -3.5196895107), (1.0133950525, -3.5388445317), (0.8631087817, -3.5612568501), (0.7231291478, -3.586920649), (0.5942044237, -3.6157613282), (0.5000495901, -3.641302063), (0.4344350476, -3.6618113967), (0.3928991221, -3.6760816405), (0.3726829221, -3.6833661002)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.0470426499, 0.0470426499, 0.0470426499, 0.0470426499, 0.0470426499, 0.0470426499, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9333333333, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(2.487777686, -3.4721919908), (2.4727729071, -3.4714866657), (2.4575095712, -3.4708323375), (2.441987674, -3.4702290061), (2.4262067528, -3.469676764), (2.4101662286, -3.4691757963)], [1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0470426499, 0.0470426499, 0.0470426499, 0.0470426499, 0.0470426499, 0.0470426499], 5)
                _nurbs_edge([(2.487777686, -3.4721919908), (2.5027823507, -3.471486671), (2.5180455685, -3.4708323474), (2.5335673437, -3.4702290199), (2.5493481389, -3.4696767808), (2.5653885331, -3.4691758154)], [1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0470422919, 0.0470422919, 0.0470422919, 0.0470422919, 0.0470422919, 0.0470422919], 5)
                _nurbs_edge([(2.5653885344, -3.4691758154), (2.5720800174, -3.4689668304), (2.6017020275, -3.4680871306), (2.6557591575, -3.4668340664), (2.7373389891, -3.4658206061), (2.8511512294, -3.4660066762), (2.9940250339, -3.4684621716), (3.1464891246, -3.4732977775), (3.3067909559, -3.4806728591), (3.472045774, -3.490752091), (3.6387828136, -3.5037038198), (3.8033111796, -3.5196895107), (3.9621603194, -3.5388445317), (4.1124465903, -3.5612568501), (4.2524262242, -3.586920649), (4.3813509483, -3.6157613282), (4.4755057819, -3.641302063), (4.5411203243, -3.6618113967), (4.5826562499, -3.6760816405), (4.6028724499, -3.6833661002)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.0470422927, 0.0470422927, 0.0470422927, 0.0470422927, 0.0470422927, 0.0470422927, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9333333333, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((5.487777686, -2.4721919908), 1.5, -126.1525251729, 252.3050503459)
                _nurbs_edge([(2.5653888449, -1.4752081759), (2.5720802675, -1.4754171586), (2.6017022206, -1.4762968555), (2.6557592927, -1.4775499169), (2.7373390615, -1.4785633754), (2.8511512294, -1.4783773055), (2.9940250339, -1.4759218101), (3.1464891246, -1.4710862041), (3.3067909559, -1.4637111225), (3.472045774, -1.4536318906), (3.6387828136, -1.4406801618), (3.8033111796, -1.4246944709), (3.9621603194, -1.4055394499), (4.1124465903, -1.3831271315), (4.2524262242, -1.3574633326), (4.3813509483, -1.3286226535), (4.4755057819, -1.3030819186), (4.5411203243, -1.2825725849), (4.5826562499, -1.2683023411), (4.6028724499, -1.2610178815)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.0470424748, 0.0470424748, 0.0470424748, 0.0470424748, 0.0470424748, 0.0470424748, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9333333333, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(2.487777686, -1.4721919908), (2.5027824091, -1.4728973133), (2.5180456872, -1.4735516393), (2.5335675247, -1.4741549688), (2.5493483842, -1.4747072094), (2.5653888449, -1.4752081759)], [1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0470424748, 0.0470424748, 0.0470424748, 0.0470424748, 0.0470424748, 0.0470424748], 5)
                _nurbs_edge([(2.487777686, -1.4721919908), (2.4727729072, -1.4728973159), (2.4575095714, -1.4735516441), (2.4419876744, -1.4741549755), (2.4262067533, -1.4747072176), (2.4101662292, -1.4752081852)], [1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0470426495, 0.0470426495, 0.0470426495, 0.0470426495, 0.0470426495, 0.0470426495], 5)
            make_face()
            with BuildLine():
                CenterArc((2.487777686, -2.4721919908), 0.6485, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a parallelogram-shaped flat plate or panel with a skewed rectangular geometry, featuring a diagonal internal line or edge that divides the surface, and characterized by a clean, minimalist design with no holes, slots, or additional features.
def model_140192_eaef8e46_0003():
    """Model: LCD v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 45.7792, perimeter: 27.16
            with BuildLine():
                Line((3.11, -3.68), (3.11, 3.68))
                Line((3.11, 3.68), (-3.11, 3.68))
                Line((-3.11, 3.68), (-3.11, -3.68))
                Line((-3.11, -3.68), (3.11, -3.68))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is a flat parallelogram-shaped panel or frame with a hollow interior, featuring small mounting holes or attachment points along its edges, typical of a structural bracket, trim ring, or gasket component.
def model_140192_eaef8e46_0004():
    """Model: LCD Mask v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.0504521859, perimeter: 90.6588803158
            with BuildLine():
                Line((-2.4837929463, 4.2545863483), (-2.85, 3.925))
                Line((-2.85, 3.925), (-6.3, 3.925))
                CenterArc((-6.3, 3.725), 0.2, 90, 90)
                Line((-6.5, 3.725), (-6.5, 2.865))
                Line((-6.5, 2.865), (-6.8295863483, 2.4987929463))
                CenterArc((-6.6809275191, 2.365), 0.2, 138.0127875042, 41.9872090348)
                CenterArc((-6.6809275191, 2.365), 0.2, 179.999996539, 41.9872159568)
                Line((-6.8295863483, 2.2312070537), (-6.5, 1.865))
                Line((-6.5, 1.865), (-6.5, -2.205))
                Line((-6.5, -2.205), (-6.8295863483, -2.5712070537))
                CenterArc((-6.6809275191, -2.705), 0.2, 138.0127875042, 41.9872124958)
                CenterArc((-6.6809275191, -2.705), 0.2, 180, 41.9872124958)
                Line((-6.8295863483, -2.8387929463), (-6.5, -3.205))
                Line((-6.5, -3.205), (-6.5, -3.725))
                CenterArc((-6.3, -3.725), 0.2, -180, 90)
                Line((-6.3, -3.925), (-3.55, -3.925))
                Line((-3.55, -3.925), (-3.1837929463, -4.2545863483))
                CenterArc((-3.05, -4.1059275191), 0.2, -131.9872124958, 41.9872124958)
                CenterArc((-3.05, -4.1059275191), 0.2, -90, 41.9872124958)
                Line((-2.9162070537, -4.2545863483), (-2.55, -3.925))
                Line((-2.55, -3.925), (2.55, -3.925))
                Line((2.55, -3.925), (2.9162070537, -4.2545863483))
                CenterArc((3.05, -4.1059275191), 0.2, -131.9872124958, 41.9872124958)
                CenterArc((3.05, -4.1059275191), 0.2, -90, 41.9872124958)
                Line((3.1837929463, -4.2545863483), (3.55, -3.925))
                Line((3.55, -3.925), (6.3, -3.925))
                CenterArc((6.3, -3.725), 0.2, -90, 90)
                Line((6.5, -3.725), (6.5, -3.205))
                Line((6.5, -3.205), (6.8295863483, -2.8387929463))
                CenterArc((6.6809275191, -2.705), 0.2, -41.9872124958, 41.9872124958)
                CenterArc((6.6809275191, -2.705), 0.2, 0, 41.9872124958)
                Line((6.8295863483, -2.5712070537), (6.5, -2.205))
                Line((6.5, -2.205), (6.5, 1.865))
                Line((6.5, 1.865), (6.8295863483, 2.2312070537))
                CenterArc((6.6809275191, 2.365), 0.2, -41.9872124958, 41.9872086776)
                CenterArc((6.6809275191, 2.365), 0.2, -0.0000038182, 41.987216314)
                Line((6.8295863483, 2.4987929463), (6.5, 2.865))
                Line((6.5, 2.865), (6.5, 3.725))
                CenterArc((6.3, 3.725), 0.2, 0, 90)
                Line((6.3, 3.925), (1.8, 3.925))
                Line((1.8, 3.925), (1.4337929463, 4.2545863483))
                CenterArc((1.3, 4.1059275191), 0.2, 48.0127875042, 41.9872124958)
                CenterArc((1.3, 4.1059275191), 0.2, 90, 41.9872124958)
                Line((1.1662070537, 4.2545863483), (0.8, 3.925))
                Line((0.8, 3.925), (-1.85, 3.925))
                Line((-1.85, 3.925), (-2.2162070537, 4.2545863483))
                CenterArc((-2.35, 4.1059275191), 0.2, 48.0127875042, 41.9872124958)
                CenterArc((-2.35, 4.1059275191), 0.2, 90, 41.9872124958)
            make_face()
            with BuildLine():
                CenterArc((-6.6809275191, 2.365), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.6809275191, -2.705), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-6.6809275191, -2.705), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.6809275191, 2.365), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-2.35, 4.1059275191), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.05, -4.1059275191), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-3.05, -4.1059275191), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.3, 4.1059275191), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-6.41, -3.725), (-6.41, 3.725))
                CenterArc((-6.3, 3.725), 0.11, 90, 90)
                Line((-6.3, 3.835), (6.3, 3.835))
                CenterArc((6.3, 3.725), 0.11, 0, 90)
                Line((6.41, 3.725), (6.41, -3.725))
                CenterArc((6.3, -3.725), 0.11, -90, 90)
                Line((6.3, -3.835), (-6.3, -3.835))
                CenterArc((-6.3, -3.725), 0.11, -180, 90)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 8.0256132711, perimeter: 80.1711503838
            with BuildLine():
                CenterArc((-6.3, -3.725), 0.11, -180, 90)
                Line((6.3, -3.835), (-6.3, -3.835))
                CenterArc((6.3, -3.725), 0.11, -90, 90)
                Line((6.41, 3.725), (6.41, -3.725))
                CenterArc((6.3, 3.725), 0.11, 0, 90)
                Line((-6.3, 3.835), (6.3, 3.835))
                CenterArc((-6.3, 3.725), 0.11, 90, 90)
                Line((-6.41, -3.725), (-6.41, 3.725))
            make_face()
            with BuildLine():
                Line((-6.21, -3.635), (-6.21, 3.635))
                Line((-6.21, 3.635), (6.21, 3.635))
                Line((6.21, 3.635), (6.21, -3.635))
                Line((6.21, -3.635), (-6.21, -3.635))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.115
        extrude(amount=0.115)
    return part.part


# Description: This is a long, slender cylindrical rod or shaft with a slightly tapered or rounded end, featuring a smooth, streamlined profile with a subtle ridge or groove running along its length.
def model_140194_b0abb2bf_0002():
    """Model: Head top Trim"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1290.3199321747, perimeter: 419.0999880981
            with BuildLine():
                Line((-10.1599971008, 1.2699999237), (193.0399971008, 1.2699999237))
                Line((-10.1599971008, -5.0799999237), (-10.1599971008, 1.2699999237))
                Line((193.0399971008, -5.0799999237), (-10.1599971008, -5.0799999237))
                Line((193.0399971008, 1.2699999237), (193.0399971008, -5.0799999237))
            make_face()
        # OneSide extrude, distance=1.905
        extrude(amount=1.905)
    return part.part


# Description: This is a long, slender rectangular tube or extrusion with a hollow square or rectangular cross-section, featuring vertical grooves or ribs running along its length for structural reinforcement.
def model_140194_b0abb2bf_0010():
    """Model: Left Arm support (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3.81), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 283.06395, perimeter: 156.21
            with BuildLine():
                Line((-3.81, -48.26), (-7.62, -48.26))
                Line((-7.62, -48.26), (-7.62, -122.555))
                Line((-7.62, -122.555), (-3.81, -122.555))
                Line((-3.81, -122.555), (-3.81, -48.26))
            make_face()
        # OneSide extrude, distance=7.62
        extrude(amount=7.62)
    return part.part


# Description: This is a tapered steel wedge or shim with a flat top surface and a pointed tip, featuring a gradually decreasing thickness from the blunt end to the sharp end.
def model_140194_b0abb2bf_0012():
    """Model: Left Arm Top Support"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3.81), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 7.25805, perimeter: 11.43
            with BuildLine():
                Line((-7.62, -46.355), (-7.62, -48.26))
                Line((-11.43, -46.355), (-7.62, -46.355))
                Line((-11.43, -48.26), (-11.43, -46.355))
                Line((-7.62, -48.26), (-11.43, -48.26))
            make_face()
            # Profile area: 7.25805, perimeter: 11.43
            with BuildLine():
                Line((-3.81, -48.26), (-7.62, -48.26))
                Line((-3.81, -46.355), (-3.81, -48.26))
                Line((-7.62, -46.355), (-3.81, -46.355))
                Line((-7.62, -46.355), (-7.62, -48.26))
            make_face()
        # OneSide extrude, distance=99.06
        extrude(amount=99.06)
    return part.part


# Description: This is a geometric solid featuring two identical octahedrons with a diamond-like shape, characterized by eight triangular faces meeting at pointed vertices with internal edge definitions visible throughout.
def model_140194_b0abb2bf_0016():
    """Model: Middle partitions"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -120.65, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 58.0644, perimeter: 64.77
            with BuildLine():
                Line((-122.555, 100.965), (-124.46, 100.965))
                Line((-124.46, 100.965), (-124.46, 70.485))
                Line((-124.46, 70.485), (-122.555, 70.485))
                Line((-122.555, 70.485), (-122.555, 100.965))
            make_face()
            # Profile area: 58.0644, perimeter: 64.77
            with BuildLine():
                Line((-60.325, 70.485), (-60.325, 100.965))
                Line((-58.42, 70.485), (-60.325, 70.485))
                Line((-58.42, 100.965), (-58.42, 70.485))
                Line((-60.325, 100.965), (-58.42, 100.965))
            make_face()
        # OneSide extrude, distance=34.29
        extrude(amount=34.29)
    return part.part


# Description: This is a flat parallelogram-shaped plate or panel with a slightly beveled edge border, rendered in dark blue-gray with a 3D perspective view.
def model_140265_1d92f548_0000():
    """Model: top (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 38 constraints, 40 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 70.8439403657, perimeter: 85.5843807451
            with BuildLine():
                Line((-6, 3.5), (6, 3.5))
                Line((-6, -3.5), (-6, 3.5))
                Line((6, -3.5), (-6, -3.5))
                Line((6, 3.5), (6, -3.5))
            make_face()
            with BuildLine():
                CenterArc((-5.6, 3.1), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.6, 3.1), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-5.6, -3.1), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.6, -3.1), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-4.2, -2.5754947997), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-4.07, 2.2545052003), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.01, 0.7345052003), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.01, -2.0554947997), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-3.7881415491, -1.4362718189), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-3.7881415491, 1.3637281811), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.6118584509, -0.1362718189), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.6118584509, 1.3637281811), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.489010232, -2.0305835227), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.5122589423, 1.9914433592), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-0.4770964771, -2.0498539447), (-2.5327173189, -2.0498539447))
                CenterArc((-0.4770964771, -2.4498539447), 0.4, -90, 180)
                Line((-2.5327173189, -2.8498539447), (-0.4770964771, -2.8498539447))
                CenterArc((-2.5327173189, -2.4498539447), 0.4, 90, 180)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-0.4770964771, 2.8565049662), (-2.5327173189, 2.8565049662))
                CenterArc((-0.4770964771, 2.4565049662), 0.4, -90, 180)
                Line((-2.5327173189, 2.0565049662), (-0.4770964771, 2.0565049662))
                CenterArc((-2.5327173189, 2.4565049662), 0.4, 90, 180)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((3.68, -1.1446970163), (3.68, 1.1753029837))
                Line((3.68, 1.1753029837), (5, 1.1753029837))
                Line((5, 1.1753029837), (5, -1.1446970163))
                Line((5, -1.1446970163), (3.68, -1.1446970163))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.34, 1.4003029837), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.34, -1.3696970163), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-2, 0.538551694), (-4.5321002787, 0.538551694))
                CenterArc((-2, 0.038551694), 0.5, -90, 180)
                Line((-4.5321002787, -0.461448306), (-2, -0.461448306))
                CenterArc((-4.5321002787, 0.038551694), 0.5, 90, 180)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-4.2, -2.5754947997)):
                Circle(0.15)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-4.07, 2.2545052003)):
                Circle(0.15)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((1.01, 0.7345052003)):
                Circle(0.15)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((1.01, -2.0554947997)):
                Circle(0.15)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-3.7881415491, -1.4362718189)):
                Circle(0.15)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-3.7881415491, 1.3637281811)):
                Circle(0.15)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((0.6118584509, -0.1362718189)):
                Circle(0.15)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((0.6118584509, 1.3637281811)):
                Circle(0.15)
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((2.489010232, -2.0305835227)):
                Circle(0.5)
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((2.5122589423, 1.9914433592)):
                Circle(0.5)
            # Profile area: 2.147151498, perimeter: 6.6245158063
            with BuildLine():
                CenterArc((-2.5327173189, -2.4498539447), 0.4, 90, 180)
                Line((-2.5327173189, -2.8498539447), (-0.4770964771, -2.8498539447))
                CenterArc((-0.4770964771, -2.4498539447), 0.4, -90, 180)
                Line((-0.4770964771, -2.0498539447), (-2.5327173189, -2.0498539447))
            make_face()
            # Profile area: 2.147151498, perimeter: 6.6245158063
            with BuildLine():
                CenterArc((-2.5327173189, 2.4565049662), 0.4, 90, 180)
                Line((-2.5327173189, 2.0565049662), (-0.4770964771, 2.0565049662))
                CenterArc((-0.4770964771, 2.4565049662), 0.4, -90, 180)
                Line((-0.4770964771, 2.8565049662), (-2.5327173189, 2.8565049662))
            make_face()
            # Profile area: 3.0624, perimeter: 7.28
            with BuildLine():
                Line((5, -1.1446970163), (3.68, -1.1446970163))
                Line((5, 1.1753029837), (5, -1.1446970163))
                Line((3.68, 1.1753029837), (5, 1.1753029837))
                Line((3.68, -1.1446970163), (3.68, 1.1753029837))
            make_face()
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((4.34, 1.4003029837)):
                Circle(0.1)
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((4.34, -1.3696970163)):
                Circle(0.1)
            # Profile area: 3.3174984421, perimeter: 8.2057932109
            with BuildLine():
                CenterArc((-4.5321002787, 0.038551694), 0.5, 90, 180)
                Line((-4.5321002787, -0.461448306), (-2, -0.461448306))
                CenterArc((-2, 0.038551694), 0.5, -90, 180)
                Line((-2, 0.538551694), (-4.5321002787, 0.538551694))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: A tilted ladder with a parallelogram frame featuring two vertical side rails and five equally-spaced horizontal rungs for climbing.
def model_140391_46e0f895_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # subframe -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 38 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1264.514141246, perimeter: 508.0000043488
            with BuildLine():
                Line((144.7799978256, 0), (144.7799978256, -5.0799999237))
                Line((144.7799978256, -5.0799999237), (144.7799978256, -49.4819661417))
                Line((144.7799978256, -54.5619661417), (144.7799978256, -49.4819661417))
                Line((144.7799978256, -54.5619661417), (144.7799978256, -98.2499661417))
                Line((144.7799978256, -98.2499661417), (144.7799978256, -103.3299661417))
                Line((144.7799978256, -103.3299661417), (144.7799978256, -147.0179661417))
                Line((144.7799978256, -147.0179661417), (144.7799978256, -152.0979661417))
                Line((144.7799978256, -152.0979661417), (144.7799978256, -195.7859661417))
                Line((144.7799978256, -195.7859661417), (144.7799978256, -200.8659661417))
                Line((144.7799978256, -200.8659661417), (144.7799978256, -244.5539661417))
                Line((144.7799978256, -244.5539661417), (144.7799978256, -248.92))
                Line((144.7799978256, -248.92), (149.86, -248.92))
                Line((149.86, 0), (149.86, -248.92))
                Line((149.86, 0), (144.7799978256, 0))
            make_face()
            # Profile area: 377.0506745101, perimeter: 181.4520633679
            with BuildLine():
                Line((144.7799978256, -248.92), (58.42, -248.92))
                Line((144.7799978256, -244.5539661417), (144.7799978256, -248.92))
                Line((58.42, -244.5539661417), (144.7799978256, -244.5539661417))
                Line((58.42, -248.92), (58.42, -244.5539661417))
            make_face()
            # Profile area: 438.7087889542, perimeter: 182.8799956512
            with BuildLine():
                Line((58.42, -200.8659661417), (144.7799978256, -200.8659661417))
                Line((144.7799978256, -195.7859661417), (144.7799978256, -200.8659661417))
                Line((58.42, -195.7859661417), (144.7799978256, -195.7859661417))
                Line((58.42, -200.8659661417), (58.42, -195.7859661417))
            make_face()
            # Profile area: 1264.5136, perimeter: 508
            with BuildLine():
                Line((53.34, 0), (53.34, -248.92))
                Line((58.42, -248.92), (53.34, -248.92))
                Line((58.42, -248.92), (58.42, -244.5539661417))
                Line((58.42, -244.5539661417), (58.42, -243.8399963379))
                Line((58.42, -200.8659661417), (58.42, -243.8399963379))
                Line((58.42, -200.8659661417), (58.42, -195.7859661417))
                Line((58.42, -152.0979661417), (58.42, -195.7859661417))
                Line((58.42, -152.0979661417), (58.42, -147.0179661417))
                Line((58.42, -103.3299661417), (58.42, -147.0179661417))
                Line((58.42, -103.3299661417), (58.42, -98.2499661417))
                Line((58.42, -54.5619661417), (58.42, -98.2499661417))
                Line((58.42, -49.4819661417), (58.42, -54.5619661417))
                Line((58.42, -5.0799999237), (58.42, -49.4819661417))
                Line((58.42, 0), (58.42, -5.0799999237))
                Line((53.34, 0), (58.42, 0))
            make_face()
            # Profile area: 438.7087889542, perimeter: 182.8799956512
            with BuildLine():
                Line((58.42, -152.0979661417), (144.7799978256, -152.0979661417))
                Line((144.7799978256, -147.0179661417), (144.7799978256, -152.0979661417))
                Line((58.42, -147.0179661417), (144.7799978256, -147.0179661417))
                Line((58.42, -152.0979661417), (58.42, -147.0179661417))
            make_face()
            # Profile area: 438.7087889542, perimeter: 182.8799956512
            with BuildLine():
                Line((58.42, -103.3299661417), (144.7799978256, -103.3299661417))
                Line((144.7799978256, -98.2499661417), (144.7799978256, -103.3299661417))
                Line((58.42, -98.2499661417), (144.7799978256, -98.2499661417))
                Line((58.42, -103.3299661417), (58.42, -98.2499661417))
            make_face()
            # Profile area: 438.7087889542, perimeter: 182.8799956512
            with BuildLine():
                Line((58.42, -54.5619661417), (144.7799978256, -54.5619661417))
                Line((144.7799978256, -54.5619661417), (144.7799978256, -49.4819661417))
                Line((144.7799978256, -49.4819661417), (58.42, -49.4819661417))
                Line((58.42, -49.4819661417), (58.42, -54.5619661417))
            make_face()
            # Profile area: 438.7087823654, perimeter: 182.8799954987
            with BuildLine():
                Line((144.7799978256, -5.0799999237), (58.42, -5.0799999237))
                Line((144.7799978256, 0), (144.7799978256, -5.0799999237))
                Line((58.42, 0), (144.7799978256, 0))
                Line((58.42, 0), (58.42, -5.0799999237))
            make_face()
        # OneSide extrude, distance=7.62
        extrude(amount=7.62)
    return part.part


# Description: This is a cylindrical mesh or perforated filter sleeve with a closed bottom end and an open top end, featuring a fine mesh or screen pattern on its surface.
def model_140400_0aab1cd3_0006():
    """Model: small skew v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)
    return part.part


# Description: This is a robotic arm or manipulator joint featuring an angled cylindrical shaft with a hexagonal connector at the top and a spherical ball joint at the bottom, with blue and dark gray material sections indicating different components or joint types.
def model_140558_461ff76a_0000():
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
        # Sketch has 55 constraints, 14 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.0286187858, perimeter: 1.5072014303
            with BuildLine():
                Line((2.7479884064, 3.0169258905), (2.6494106951, 3.0564444418))
                _nurbs_edge([(2.0200390019, 2.8680379409), (2.0696267907, 2.8888130217), (2.1851772753, 2.9337617429), (2.3076055493, 2.9738688816), (2.4366127717, 3.0093448052), (2.5718803026, 3.0404138187), (2.6494106951, 3.0564444418)], [1, 1, 1, 1, 1, 1, 1], [0.5365680912, 0.5365680912, 0.5365680912, 0.5365680912, 0.5365680912, 0.5365680912, 0.6, 0.6804348205, 0.6804348205, 0.6804348205, 0.6804348205, 0.6804348205, 0.6804348205], 5)
                Line((2.0200390019, 2.8680379409), (2.7479884064, 3.0169258905))
            make_face()
            # Profile area: 2.3301096686, perimeter: 8.8996593149
            with BuildLine():
                Line((2.0200390019, 2.8680379409), (2.7479884064, 3.0169258905))
                _nurbs_edge([(1.6317634301, 2.6583359155), (1.6779221567, 2.6903476353), (1.7499307897, 2.7362628504), (1.8262371409, 2.7791527099), (1.9067795237, 2.8190606381), (1.9914519576, 2.8560612392), (2.0200390019, 2.8680379409)], [1, 1, 1, 1, 1, 1, 1], [0.4265173793, 0.4265173793, 0.4265173793, 0.4265173793, 0.4265173793, 0.4265173793, 0.5, 0.5365680912, 0.5365680912, 0.5365680912, 0.5365680912, 0.5365680912, 0.5365680912], 5)
                CenterArc((1.2883255021, 3.0449517066), 0.5171280115, -59.0007930923, 10.6160684175)
                _nurbs_edge([(1.528419637, 2.5808292156), (1.5328899891, 2.5844557089), (1.5381054748, 2.5886493623), (1.5433495664, 2.5928228786), (1.548622271, 2.5969762531), (1.5539235926, 2.6011094827), (1.5546599819, 2.6016827982)], [1, 1, 1, 1, 1, 1, 1], [0.3922839166, 0.3922839166, 0.3922839166, 0.3922839166, 0.3922839166, 0.3922839166, 0.4, 0.4012436333, 0.4012436333, 0.4012436333, 0.4012436333, 0.4012436333, 0.4012436333], 5)
                Line((1.528419637, 2.5808292156), (1.8436173162, 2.6899426566))
                CenterArc((1.9090429373, 2.5009466563), 0.2, 68.1547782276, 40.9397773329)
                Line((3.6885440771, 2.0030398332), (1.9834630462, 2.6865851421))
                Line((5.5400888966, 2.6769470349), (3.6885440771, 2.0030398332))
                Line((5.5382787105, 2.6819204803), (5.5400888966, 2.6769470349))
                Line((5.3657073755, 3.1560563265), (5.5382787105, 2.6819204803))
                CenterArc((5.1777688513, 3.0876522979), 0.2, 20, 87.105311078)
                Line((3.577077787, 2.8043092968), (5.1189430669, 3.2788054487))
                CenterArc((3.430013326, 3.282192174), 0.5, -75.3078226773, 2.4131337552)
                CenterArc((3.430013326, 3.282192174), 0.5, -94.0444313088, 18.7366086316)
                CenterArc((3.430013326, 3.282192174), 0.5, -111.8452217724, 17.8007904636)
                Line((3.2439630537, 2.8180959597), (2.9035553912, 2.954561064))
                Line((2.9035553912, 2.954561064), (2.7479884064, 3.0169258905))
            make_face()
            # Profile area: 0.7142817323, perimeter: 4.5057233212
            with BuildLine():
                CenterArc((1.2883255021, 3.0449517066), 0.5171280115, -48.3847246748, 21.7226507628)
                CenterArc((1.2883255021, 3.0449517066), 0.5171280115, -26.662073912, 79.3343048397)
                CenterArc((1.2883255021, 3.0449517066), 0.5171280115, 52.6722309276, 15.4825473)
                CenterArc((1.2883255021, 3.0449517066), 0.5171280115, 68.1547782276, 220.9397773329)
                CenterArc((1.2883255021, 3.0449517066), 0.5171280115, -70.9054444395, 11.9046513472)
                _nurbs_edge([(1.5546599819, 2.6016827982), (1.5696252597, 2.6133340064), (1.5848182483, 2.6248249187), (1.600239032, 2.6361554759), (1.6158875138, 2.6473257464), (1.6317634301, 2.6583359155)], [1, 1, 1, 1, 1, 1], [0.4012436333, 0.4012436333, 0.4012436333, 0.4012436333, 0.4012436333, 0.4012436333, 0.4265173793, 0.4265173793, 0.4265173793, 0.4265173793, 0.4265173793, 0.4265173793], 5)
            make_face()
            with BuildLine():
                CenterArc((1.2883255021, 3.0449517066), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2648762865, perimeter: 2.7758283914
            with BuildLine():
                _nurbs_edge([(2.0200390019, 2.8680379409), (2.0696267907, 2.8888130217), (2.1851772753, 2.9337617429), (2.3076055493, 2.9738688816), (2.4366127717, 3.0093448052), (2.5718803026, 3.0404138187), (2.6494106951, 3.0564444418)], [1, 1, 1, 1, 1, 1, 1], [0.5365680912, 0.5365680912, 0.5365680912, 0.5365680912, 0.5365680912, 0.5365680912, 0.6, 0.6804348205, 0.6804348205, 0.6804348205, 0.6804348205, 0.6804348205, 0.6804348205], 5)
                Line((2.6494106951, 3.0564444418), (1.6352925377, 3.4629915188))
                Line((1.601898413, 3.4561613975), (1.6352925377, 3.4629915188))
                CenterArc((1.2883255021, 3.0449517066), 0.5171280115, -26.662073912, 79.3343048397)
                Line((1.7504665747, 2.8129021228), (2.0200390019, 2.8680379409))
            make_face()
            # Profile area: 0.0129495267, perimeter: 0.9133085861
            with BuildLine():
                Line((1.7504665747, 2.8129021228), (2.0200390019, 2.8680379409))
                CenterArc((1.2883255021, 3.0449517066), 0.5171280115, -48.3847246748, 21.7226507628)
                _nurbs_edge([(1.6317634301, 2.6583359155), (1.6779221567, 2.6903476353), (1.7499307897, 2.7362628504), (1.8262371409, 2.7791527099), (1.9067795237, 2.8190606381), (1.9914519576, 2.8560612392), (2.0200390019, 2.8680379409)], [1, 1, 1, 1, 1, 1, 1], [0.4265173793, 0.4265173793, 0.4265173793, 0.4265173793, 0.4265173793, 0.4265173793, 0.5, 0.5365680912, 0.5365680912, 0.5365680912, 0.5365680912, 0.5365680912, 0.5365680912], 5)
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a blue anodized aluminum bracket or arm with an elongated shaft extending from a vertical angular flange, featuring cutouts and a handle-like opening for gripping or mounting purposes.
def model_140636_00af4387_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 51 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 74.9977204688, perimeter: 68.467299096
            with BuildLine():
                Line((11.4300000919, -0.6399999081), (11.4300002729, -1.900000173))
                CenterArc((12.0700002729, -1.9000000811), 0.64, -179.9999917715, 89.9999917715)
                Line((12.0700002729, -2.5400000811), (18.4099996352, -2.5400000811))
                CenterArc((18.4099996352, -1.9000000811), 0.64, -90, 90)
                Line((19.0499996352, -1.9000000811), (19.0499996352, 4.4400000811))
                CenterArc((18.4099996352, 4.4400000811), 0.64, 0, 90)
                Line((18.4099996352, 5.0800000811), (12.0700002729, 5.0800000811))
                CenterArc((12.0700002729, 4.4400000811), 0.64, 90, 89.9999917715)
                Line((11.4300002729, 4.440000173), (11.4300000919, 3.1799999081))
                CenterArc((10.7900000919, 3.18), 0.64, -90, 89.9999917715)
                Line((10.7900000919, 2.54), (0.64, 2.54))
                CenterArc((0.64, 1.9), 0.64, 90, 90)
                Line((0, 1.9), (0, 0.64))
                CenterArc((0.64, 0.64), 0.64, -180, 90)
                Line((0.64, 0), (10.7900000919, 0))
                CenterArc((10.7900000919, -0.64), 0.64, 0.0000082285, 89.9999917715)
            make_face()
            with BuildLine():
                CenterArc((1.2700000405, 1.27), 0.3175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.3500000405, 1.27), 0.3175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((16.906875, 2.936875), (13.573125, 2.936875))
                Line((16.906875, -0.396875), (16.906875, 2.936875))
                Line((13.573125, -0.396875), (16.906875, -0.396875))
                Line((13.573125, 2.936875), (13.573125, -0.396875))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


# Description: This is a 3D bent metal bracket or angle iron with an L-shaped profile, featuring a vertical leg and a horizontal leg connected at a right angle with a sharp internal corner.
def model_140763_e14274f8_0004():
    """Model: Tabletop"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 10 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2123.5996077559, perimeter: 242.1001584427
            with BuildLine():
                Line((0, 0), (19.9906637612, 0))
                Line((0, -9.9906637612), (0, 0))
                Line((0, -9.9906637612), (70, -79.9906637612))
                Line((84.9906637612, -65), (70, -79.9906637612))
                Line((84.9906637612, -65), (19.9906637612, 0))
            make_face()
            # Profile area: 8288.1068555249, perimeter: 411.9425540319
            with BuildLine():
                Line((19.9906637612, 0), (180, 0))
                Line((84.9906637612, -65), (19.9906637612, 0))
                Line((180, -65), (84.9906637612, -65))
                Line((180, 0), (180, -65))
            make_face()
            # Profile area: 11550.6535367192, perimeter: 499.0136218438
            with BuildLine():
                Line((0, -9.9906637612), (70, -79.9906637612))
                Line((0, -210), (0, -9.9906637612))
                Line((70, -210), (0, -210))
                Line((70, -79.9906637612), (70, -210))
            make_face()
        # Start offset: 75.5 (not directly supported, may affect result)
        # OneSide extrude, distance=-2.5
        extrude(amount=-2.5)
    return part.part


# Description: This is a hexagonal tool steel bar or punch with a tapered, beveled point at one end and a flat end at the other, featuring a long prismatic body.
def model_140984_0596e640_0005():
    """Model: Sitzen Raum 2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 298.0570924398, perimeter: 99.1591692685
            with BuildLine():
                Line((1.9870719221, -42.5795846343), (-5.0129280779, -42.5795846343))
                Line((1.9870719221, 0), (1.9870719221, -42.5795846343))
                Line((-5.0129280779, 0), (1.9870719221, 0))
                Line((-5.0129280779, -42.5795846343), (-5.0129280779, 0))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


# Description: This is a complex polyhedron or irregular hexahedron with an asymmetrical shape featuring multiple faceted surfaces, angular edges, and what appears to be concave and convex geometric features, resembling an abstract geometric solid or potentially an aerodynamic component.
def model_141032_6b0fa18c_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1860.5, perimeter: 183
            with BuildLine():
                Line((0, 30.5), (0, 0))
                Line((0, 0), (61, 0))
                Line((61, 0), (61, 30.5))
                Line((61, 30.5), (0, 30.5))
            make_face()
        # OneSide extrude, distance=20.3
        extrude(amount=20.3)
    return part.part


# Description: This is a cylindrical sleeve or tube with a smooth, tapered rounded end on one side and a flat or slightly recessed end on the other, featuring a uniform hollow or solid tubular geometry typical of a mechanical spacer, connector, or barrel component.
def model_141118_cb31cb8f_0000():
    """Model: Pistone"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 1.02), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))) as sk:
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # TwoSides extrude, along=0.6, against=-1.5
        extrude(amount=0.6)
        extrude(sk.sketch, amount=-1.5)
    return part.part


# Description: This is a toroidal or ring-shaped bearing component with a large central hole, featuring a curved mesh or textured surface on the outer edge and a smooth solid body, designed for rotational applications.
def model_141118_cb31cb8f_0001():
    """Model: PinExtender"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.62), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.6946061357, perimeter: 4.2097341558
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.17, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2)
    return part.part


# Description: This is a curved duct or cable management component featuring a U-shaped arch with two solid rectangular base flanges at each end and a perforated or mesh-textured curved upper section for routing and organizing cables or airflow.
def model_141119_b9c79872_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 31 constraints, 16 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 46.6706845872, perimeter: 59.7155732707
            with BuildLine():
                Line((3.4925002432, 5.715), (3.4925259308, 0.8989335671))
                Line((3.4925259308, 0.8989335671), (4.3905515429, 0.000907955))
                Line((4.3905515429, 0.000907955), (7.6200002432, -0.0000049997))
                Line((7.6200002432, -0.0000049997), (7.6200002432, 3.1749950003))
                CenterArc((6.9850002432, 3.1749950003), 0.635, 0, 90)
                Line((6.9850002432, 3.8099950003), (5.7150002432, 3.8099950003))
                CenterArc((5.7150002432, 5.0799950003), 1.27, -180, 90)
                Line((4.4450002432, 5.0799950003), (4.4450002432, 5.715))
                CenterArc((0.0000002432, 5.715), 4.445, 0, 89.9998711006)
                Line((0.0000102432, 10.16), (0.0000002432, 10.16))
                CenterArc((0.0000002432, 5.715), 4.445, 90, 90)
                Line((-4.4449997568, 5.715), (-4.4449997568, 5.0799950003))
                CenterArc((-5.7149997568, 5.0799950003), 1.27, -90, 90)
                Line((-5.7149997568, 3.8099950003), (-6.9849998379, 3.8099950003))
                CenterArc((-6.9849998379, 3.1749950003), 0.635, 90, 89.9999926858)
                Line((-7.6199998379, 3.1749950814), (-7.6200002432, -0.0000049997))
                Line((-7.6200002432, -0.0000049997), (-4.3863122752, -0.0000049997))
                Line((-4.3863122752, -0.0000049997), (-3.4924997568, 0.8938075187))
                Line((-3.4924997568, 0.8938075187), (-3.4924997568, 5.715))
                CenterArc((0.0000002432, 5.715), 3.4925, 0, 180)
            make_face()
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)
    return part.part


# Description: This is a utility knife or craft knife blade featuring an elongated pointed tip, a narrow shaft with adjustment slots or notches along its length, and a handle grip section on the right end.
def model_141270_b5c7f8b7_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 55 constraints, 22 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 88.0691773363, perimeter: 92.2412067589
            with BuildLine():
                Line((25.5624269936, 3.0562426994), (69.2574257426, 7.4257425743))
                Line((69.2574257426, 7.4257425743), (69.0584183045, 9.4158169547))
                Line((24.9952391887, 5.0094990431), (69.0584183045, 9.4158169547))
                CenterArc((20, 2.5), 5.5901699437, 5.7105931375, 20.9633608692)
            make_face()
            # Profile area: 2.0564015809, perimeter: 6.203693882
            with BuildLine():
                CenterArc((20, 2.5), 4.59, 5.7105931375, 25.8317443023)
                Line((24.5672207031, 2.9567220703), (25.5624269936, 3.0562426994))
                CenterArc((20, 2.5), 5.5901699437, 5.7105931375, 20.9633608692)
                Line((23.9118451391, 4.9011596381), (24.9952391887, 5.0094990431))
            make_face()
            # Profile area: 6.0447936894, perimeter: 10.4445531287
            with BuildLine():
                Line((84.5875636319, 4.938369575), (84.5875636319, 2.938369575))
                Line((80.9728448177, 4.938369575), (84.5875636319, 4.938369575))
                CenterArc((74.975185951, 0.4975185951), 7.4627789266, 19.0910315716, 17.4263531888)
                Line((82.0275129288, 2.938369575), (84.5875636319, 2.938369575))
            make_face()
            # Profile area: 2.3244819346, perimeter: 7.0326258458
            with BuildLine():
                CenterArc((74.975185951, 0.4975185951), 7.4627789266, 19.0910315716, 17.4263531888)
                Line((79.6708447519, 4.938369575), (80.9728448177, 4.938369575))
                CenterArc((74.975185951, 0.4975185951), 6.463, 22.1891421424, 21.2133518373)
                Line((80.9595502025, 2.938369575), (82.0275129288, 2.938369575))
            make_face()
            # Profile area: 19.482457106, perimeter: 23.6637243179
            with BuildLine():
                Line((69.2574257426, 7.4257425743), (74.2326125824, 7.9232612582))
                Line((74.2326125824, 7.9232612582), (79.2076979291, 8.4207697929))
                CenterArc((83.9838764421, 10.9083627684), 5.3851648071, -174.2894068625, 21.8014094864)
                Line((69.0584183045, 9.4158169547), (78.6254371836, 10.3725188426))
                Line((69.2574257426, 7.4257425743), (69.0584183045, 9.4158169547))
            make_face()
            # Profile area: 8.5, perimeter: 17
            with BuildLine():
                Line((4.1231056256, -1.0307764064), (8.2462112512, 0))
                Line((4.1231056256, 1.0307764064), (8.2462112512, 0))
                Line((0, 0), (4.1231056256, 1.0307764064))
                Line((0, 0), (4.1231056256, -1.0307764064))
            make_face()
            # Profile area: 18.2843134708, perimeter: 23.4904467019
            with BuildLine():
                CenterArc((83.9838764421, 10.9083627684), 5.3851648071, -152.4879973761, 113.7720976939)
                Line((84.320696531, 7.5401618796), (88.1856882861, 7.5401618796))
                CenterArc((83.9838764421, 10.9083627684), 3.385, -174.2894068625, 90)
                Line((79.008690491, 10.4108441733), (80.6156755532, 10.5715426795))
                Line((79.2076979291, 8.4207697929), (79.008690491, 10.4108441733))
            make_face()
            # Profile area: 5.0927503866, perimeter: 11.8040521445
            with BuildLine():
                Line((87.0800436416, 9.5401618796), (89.1923336347, 9.5401618796))
                CenterArc((83.9838764421, 10.9083627684), 3.385, -84.2894068625, 60.4487002691)
                Line((84.320696531, 7.5401618796), (88.1856882861, 7.5401618796))
                CenterArc((83.9838764421, 10.9083627684), 5.3851648071, -38.7158996822, 23.997501677)
            make_face()
            # Profile area: 17.0239959382, perimeter: 23.4907368623
            with BuildLine():
                Line((4.1231056256, 1.0307764064), (14.5255153748, 3.6313788437))
                Line((4.1231056256, 1.0307764064), (8.2462112512, 0))
                Line((8.2462112512, 0), (14.4892968127, 1.5607713904))
                CenterArc((20, 2.5), 5.5901699437, 168.3234091702, 21.3489783597)
            make_face()
            # Profile area: 0.6418141191, perimeter: 4.5874000431
            with BuildLine():
                Line((20, -5), (20.4826767813, -3.0692928748))
                CenterArc((20, 2.5), 5.5901699437, -91.9611966626, 6.9145024611)
                Line((20, -5), (19.8086895409, -3.0868954087))
            make_face()
            # Profile area: 3.4797964793, perimeter: 7.9183435575
            with BuildLine():
                Line((110, 6), (110.4153919612, 4.043613147))
                Line((107.5189402363, 5.4732062937), (110, 6))
                CenterArc((110.2076959806, 7.2718065735), 3.2348679137, -146.2200876901, 59.9013181652)
            make_face()
            # Profile area: 5.2903348366, perimeter: 11.7575065077
            with BuildLine():
                Line((105, 7.5401618796), (105, 9.5401618796))
                Line((105, 7.5401618796), (107.0409022801, 7.9319490413))
                CenterArc((110.2076959806, 7.2718065735), 3.2348679137, 108.0522420805, 60.1726409809)
                Line((105, 9.5401618796), (109.2052620568, 10.3474360453))
            make_face()
            # Profile area: 27.5612101243, perimeter: 34.5482085379
            with BuildLine():
                Line((8.2462112512, 0), (16.9280685084, -2.1704643143))
                Line((4.1231056256, -1.0307764064), (8.2462112512, 0))
                Line((4.1231056256, -1.0307764064), (20, -5))
                Line((20, -5), (19.8086895409, -3.0868954087))
                CenterArc((20, 2.5), 5.5901699437, -123.3343505457, 31.373153883)
            make_face()
            # Profile area: 5.5412240428, perimeter: 12.875480369
            with BuildLine():
                Line((75.419271049, 4.938369575), (79.6708447519, 4.938369575))
                CenterArc((74.975185951, 0.4975185951), 4.463, 33.1551551842, 51.1342516783)
                Line((78.7115766552, 2.938369575), (80.9595502025, 2.938369575))
                CenterArc((74.975185951, 0.4975185951), 6.463, 22.1891421424, 21.2133518373)
            make_face()
            # Profile area: 2.0282896816, perimeter: 6.1019372179
            with BuildLine():
                CenterArc((74.975185951, 0.4975185951), 7.4627789266, 170.1655005964, 15.5450925411)
                Line((67.5494433768, -0.2450556623), (68.5442605907, -0.1455739409))
                CenterArc((74.975185951, 0.4975185951), 6.463, 167.6842752581, 18.0263178794)
                Line((68.6609185062, 1.8760669748), (67.62207083, 1.7721822072))
            make_face()
            # Profile area: 20.7097610088, perimeter: 28.4011243528
            with BuildLine():
                Line((69.5925159421, 4.0748405788), (69.800992562, 1.9900743804))
                Line((70, 0), (69.800992562, 1.9900743804))
                Line((70, 0), (70.5343349711, 0.0534334971))
                CenterArc((74.975185951, 0.4975185951), 4.463, 95.7105931375, 90)
                CenterArc((74.975185951, 0.4975185951), 4.463, 84.2894068625, 11.421186275)
                Line((75.419271049, 4.938369575), (79.6708447519, 4.938369575))
                CenterArc((74.975185951, 0.4975185951), 6.463, 43.4024939797, 102.9894974678)
            make_face()
            # Profile area: 94.9283727959, perimeter: 99.197769584
            with BuildLine():
                CenterArc((20, 2.5), 5.5901699437, -85.0466942015, 13.0125531283)
                Line((20, -5), (20.4826767813, -3.0692928748))
                Line((20, -5), (67.5494433768, -0.2450556623))
                CenterArc((74.975185951, 0.4975185951), 7.4627789266, 170.1655005964, 15.5450925411)
                Line((67.62207083, 1.7721822072), (21.7242892025, -2.8175959555))
            make_face()
            # Profile area: 2.412557607, perimeter: 6.8440651684
            with BuildLine():
                CenterArc((83.9838764421, 10.9083627684), 5.3851648071, -38.7158996822, 23.997501677)
                Line((88.1856882861, 7.5401618796), (89.9832946721, 7.5401618796))
                Line((89.9832946721, 7.5401618796), (89.9832946721, 9.5401618796))
                Line((89.1923336347, 9.5401618796), (89.9832946721, 9.5401618796))
            make_face()
            # Profile area: 11.0878787386, perimeter: 15.1036665985
            with BuildLine():
                Line((15.4630435747, 1.8042080809), (17.4182838055, 2.2930181386))
                CenterArc((20, 2.5), 4.59, -171.2809974207, 86.9915905582)
                Line((20.2577146323, -0.0771463226), (20.4567220703, -2.0672207031))
                CenterArc((20, 2.5), 2.59, -175.4162754088, 91.1268685463)
            make_face()
            # Profile area: 7.0470589866, perimeter: 13.4840960299
            with BuildLine():
                CenterArc((110.2076959806, 7.2718065735), 3.2348679137, -146.2200876901, 59.9013181652)
                Line((105, 4.938369575), (107.5189402363, 5.4732062937))
                Line((105, 4.938369575), (105, 2.938369575))
                Line((110.4153919612, 4.043613147), (105, 2.938369575))
            make_face()
            # Profile area: 2.1038337571, perimeter: 6.3557634879
            with BuildLine():
                Line((14.5255153748, 3.6313788437), (15.6312266727, 3.9078066682))
                CenterArc((20, 2.5), 5.5901699437, 168.3234091702, 21.3489783597)
                Line((14.4892968127, 1.5607713904), (15.4630435747, 1.8042080809))
                CenterArc((20, 2.5), 4.59, 162.1388269013, 26.580175678)
            make_face()
            # Profile area: 11.2783176264, perimeter: 15.2783176264
            with BuildLine():
                Line((20.2577146323, -0.0771463226), (20.4567220703, -2.0672207031))
                CenterArc((20, 2.5), 4.59, -84.2894068625, 90)
                Line((22.5771463226, 2.7577146323), (24.5672207031, 2.9567220703))
                CenterArc((20, 2.5), 2.59, -84.2894068625, 90)
            make_face()
            # Profile area: 4.7026095737, perimeter: 9.2225076953
            with BuildLine():
                CenterArc((110.2076959806, 7.2718065735), 3.2348679137, 108.0522420805, 60.1726409809)
                Line((107.0409022801, 7.9319490413), (109.5371381259, 8.4111455058))
                CenterArc((110, 7.25), 1.25, 90, 21.7334725556)
                Line((110, 8.5), (110, 10.5))
                Line((109.2052620568, 10.3474360453), (110, 10.5))
            make_face()
            # Profile area: 1.3776913303, perimeter: 5.6427073637
            with BuildLine():
                Line((69.800992562, 1.9900743804), (68.6609185062, 1.8760669748))
                Line((69.5925159421, 4.0748405788), (69.800992562, 1.9900743804))
                CenterArc((74.975185951, 0.4975185951), 6.463, 146.3919914475, 21.2922838107)
            make_face()
            # Profile area: 40.8248727362, perimeter: 44.8248727362
            with BuildLine():
                Line((105, 4.938369575), (105, 2.938369575))
                Line((84.5875636319, 4.938369575), (105, 4.938369575))
                Line((84.5875636319, 4.938369575), (84.5875636319, 2.938369575))
                Line((84.5875636319, 2.938369575), (105, 2.938369575))
            make_face()
            # Profile area: 2.7166277333, perimeter: 6.6421402513
            with BuildLine():
                CenterArc((74.975185951, 0.4975185951), 6.463, 167.6842752581, 18.0263178794)
                Line((68.5442605907, -0.1455739409), (70, 0))
                Line((70, 0), (69.800992562, 1.9900743804))
                Line((69.800992562, 1.9900743804), (68.6609185062, 1.8760669748))
            make_face()
            # Profile area: 4.5691128633, perimeter: 9.8455585885
            with BuildLine():
                Line((15.6312266727, 3.9078066682), (18.5301901473, 4.6325475368))
                CenterArc((20, 2.5), 4.59, 162.1388269013, 26.580175678)
                Line((15.4630435747, 1.8042080809), (17.4182838055, 2.2930181386))
                CenterArc((20, 2.5), 2.59, 124.5756695305, 60.0080550607)
            make_face()
            # Profile area: 0.5173424681, perimeter: 4.4342543581
            with BuildLine():
                CenterArc((83.9838764421, 10.9083627684), 5.3851648071, -174.2894068625, 21.8014094864)
                Line((79.2076979291, 8.4207697929), (79.008690491, 10.4108441733))
                Line((78.6254371836, 10.3725188426), (79.008690491, 10.4108441733))
            make_face()
            # Profile area: 14.9176572689, perimeter: 18.0896280901
            with BuildLine():
                Line((110, 8.5), (110, 10.5))
                CenterArc((110, 7.25), 1.25, -90, 180)
                Line((110, 6), (110.4153919612, 4.043613147))
                CenterArc((110.2076959806, 7.2718065735), 3.2348679137, -86.3187695249, 180)
            make_face()
            # Profile area: 4.2757206099, perimeter: 8.8402728205
            with BuildLine():
                CenterArc((20, 2.5), 2.59, 5.7105931375, 50.5519296988)
                Line((22.5771463226, 2.7577146323), (24.5672207031, 2.9567220703))
                CenterArc((20, 2.5), 4.59, 5.7105931375, 25.8317443023)
                Line((21.4384561886, 4.6538207431), (23.9118451391, 4.9011596381))
            make_face()
            # Profile area: 30.0334106558, perimeter: 34.0334106558
            with BuildLine():
                Line((89.9832946721, 7.5401618796), (89.9832946721, 9.5401618796))
                Line((89.9832946721, 7.5401618796), (105, 7.5401618796))
                Line((105, 7.5401618796), (105, 9.5401618796))
                Line((89.9832946721, 9.5401618796), (105, 9.5401618796))
            make_face()
        # OneSide extrude, distance=0.8125
        extrude(amount=0.8125)
    return part.part


# Description: This is a tapered cylindrical rod or pin with a pointed tip, featuring a gradually decreasing diameter from a thicker rounded end to a sharp conical point at the opposite end.
def model_141323_f85efdd4_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # base -> Extrude3 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.5, perimeter: 31
            with BuildLine():
                Line((14.508482519, -7.5), (14.508482519, 7.5))
                Line((14.508482519, 7.5), (14.008482519, 7.5))
                Line((14.008482519, 7.5), (14.008482519, -7.5))
                Line((14.008482519, -7.5), (14.508482519, -7.5))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is a triangular pyramidal or tetrahedral 3D part with a dark blue surface finish, featuring a divided face with an internal diagonal ridge or reinforcement running across its surface.
def model_141638_a21f336f_0006():
    """Model: Chip board (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.5, 0, 0), x_dir=(0, -1, 0), z_dir=(-1, 0, 0))):
            # Profile area: 3.8, perimeter: 7.8
            with BuildLine():
                Line((-1.9, 2), (0, 2))
                Line((-1.9, 0), (-1.9, 2))
                Line((0, 0), (-1.9, 0))
                Line((0, 2), (0, 0))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a dark gray mounting bracket or handle with an overall curved, organic shape featuring two large oval apertures on opposite sides, multiple small circular mounting holes, and a contoured body designed for ergonomic gripping or component attachment.
def model_141638_a21f336f_0016():
    """Model: Bottom Plate (1) (4)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 102 constraints, 31 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 40.7966523969, perimeter: 59.1049301546
            with BuildLine():
                CenterArc((-2.1000009092, 0.994440159), 3.9956917255, -88.5658982867, 8.6165160124)
                CenterArc((2.1707530556, -20.5279276304), 17.9473385864, 84.4722259829, 17.0124934561)
                CenterArc((3.9959171678, -1.6687013613), 1, -95.5277740171, 95.5277740171)
                Line((4.9959171678, 1.6687013613), (4.9959171678, -1.6687013613))
                CenterArc((3.9959171678, 1.6687013613), 1, 0, 95.5277740171)
                CenterArc((2.1707530556, 20.5279276304), 17.9473385864, -88.6762139509, 4.203987968)
                Line((2.3666726189, 2.3666726189), (2.5853791054, 2.5853791054))
                CenterArc((2.25, 2.25), 0.165, -135, 180)
                Line((1.1767766953, 1.1767766953), (2.1333273811, 2.1333273811))
                CenterArc((1, 1), 0.25, -135, 180)
                CenterArc((1, 1), 0.25, 45, 180)
                CenterArc((2.25, 2.25), 0.165, 45, 180)
                CenterArc((2.1707530556, 20.5279276304), 17.9473385864, -101.484719439, 12.8085054881)
                CenterArc((-2.1000009092, -0.994440159), 3.9956917255, 79.9493822743, 8.6165160124)
                CenterArc((-2, 0), 3, 90, 90)
                CenterArc((-2, 0), 3, 180, 90)
            make_face()
            with BuildLine():
                CenterArc((-1, 1), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1, -1), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1, -1), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.25, -2.25), 0.165, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-2.25, -2.25), 0.165, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-2.25, 2.25), 0.165, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.25, 2.1981422235), 0.165, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.25, -2.1981422235), 0.165, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-2, 1.4142135624), (-2, -1.4142135624))
                CenterArc((-2.5, -1.4142135624), 0.5, -109.4712206345, 109.4712206345)
                CenterArc((-2, 0), 2, 180, 70.5287793655)
                CenterArc((-2, 0), 2, 109.4712206345, 70.5287793655)
                CenterArc((-2.5, 1.4142135624), 0.5, 0, 109.4712206345)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-4.5000000671, 0), 0.165, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.6000000536, 0), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.04276493, perimeter: 0.8483627878
            with BuildLine():
                Line((2.1333273811, 2.1333273811), (2.3666726189, 2.3666726189))
                CenterArc((2.25, 2.25), 0.165, -135, 180)
            make_face()
            # Profile area: 0.04276493, perimeter: 0.8483627878
            with BuildLine():
                CenterArc((2.25, 2.25), 0.165, 45, 180)
                Line((2.1333273811, 2.1333273811), (2.3666726189, 2.3666726189))
            make_face()
            # Profile area: 0.08552986, perimeter: 1.0367255757
            with Locations((2.25, -2.25)):
                Circle(0.165)
        # OneSide extrude, distance=0.32
        extrude(amount=0.32)
    return part.part


# Description: This is a metal mounting bracket with an angular, hook-like shape featuring two small holes at the top, one large oval slot at the bottom, and a flat upper flange for attachment.
def model_141760_ccfda5bc_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 24 constraints, 13 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 19.3294551137, perimeter: 33.2805857173
            with BuildLine():
                Line((1.2700000405, 1.7462500811), (1.606595734, -0.4042375588))
                CenterArc((3.1750000405, -0.1587499189), 1.5875, -171.1042047135, 162.208409427)
                Line((5.0800000405, 1.7462500811), (4.743404347, -0.4042375588))
                CenterArc((5.7150000405, 1.7462500811), 0.635, 90, 90)
                Line((5.7150000405, 2.3812500811), (7.1437500405, 2.3812500811))
                CenterArc((7.1437500405, 2.5400000811), 0.15875, -90, 90)
                Line((7.3025000405, 2.5400000811), (7.3025000405, 3.6512500811))
                CenterArc((7.1437500405, 3.6512500811), 0.15875, 0, 90)
                Line((7.1437500405, 3.8100000811), (5.0800000405, 3.8100000811))
                Line((1.2700000405, 3.8100000811), (5.0800000405, 3.8100000811))
                Line((0.7775785159, 3.8100000811), (1.2700000405, 3.8100000811))
                CenterArc((0.7775785159, 3.4925000811), 0.3175, 90, 48.3664606634)
                Line((0.09374916, 3.2010928405), (0.5402760573, 3.7034355999))
                CenterArc((0.2124003894, 3.0956250811), 0.15875, 138.3664606634, 83.2670786731)
                Line((0.09374916, 2.9901573216), (0.5513673854, 2.4753368181))
                CenterArc((0.7886698441, 2.6862723369), 0.3175, -138.3664606634, 39.0821765129)
                CenterArc((0.6350000405, 1.7462500811), 0.635, 0, 80.7157158495)
            make_face()
            with BuildLine():
                CenterArc((3.1750000405, -0.1587499189), 0.9525, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.5875000405, 3.0956250811), 0.41021, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.7625000405, 3.0956250811), 0.39751, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3175
        extrude(amount=0.3175)
    return part.part


# Description: This is a rectangular prism or block with a slight trapezoidal profile, featuring a long, slender elongated shape with a narrow slot or groove running along one of its side faces.
def model_141848_34f575d3_0004():
    """Model: lcd cover"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 1.9075), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.14, perimeter: 5
            with BuildLine():
                Line((1.15, 0.9462500097), (1.15, -0.9537499903))
                Line((0.55, 0.9462500097), (1.15, 0.9462500097))
                Line((0.55, -0.9537499903), (0.55, 0.9462500097))
                Line((1.15, -0.9537499903), (0.55, -0.9537499903))
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2)
    return part.part


# Description: This is a parallelogram-shaped flat plate or panel with a slight 3D depth, featuring a beveled or chamfered edge on the left side and a clean, simple geometric form suitable for structural or assembly applications.
def model_142315_5c796497_0000():
    """Model: Lenovo HDD case_hard drive v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 69.77598948, perimeter: 33.9598
            with BuildLine():
                Line((0, 6.9723), (0, 0))
                Line((0, 0), (10.0076, 0))
                Line((10.0076, 0), (10.0076, 6.9723))
                Line((10.0076, 6.9723), (0, 6.9723))
            make_face()
        # OneSide extrude, distance=0.6858
        extrude(amount=0.6858)
    return part.part


# Description: This is a dark blue molded plastic shoulder or arm support brace featuring an L-shaped design with a curved upper section for shoulder placement, a protruding lower arm sleeve, and multiple drainage or mounting holes along its surface.
def model_142385_63969402_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 12 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0090380738, perimeter: 0.6203459847
            with BuildLine():
                CenterArc((0, 0), 0.032, 90, 180)
                Line((0.055, -0.032), (0, -0.032))
                CenterArc((0.075, -0.032), 0.02, 0, 180)
                Line((0.095, -0.032), (0.1233383416, -0.0615563657))
                CenterArc((0.1035837439, 0.0669339292), 0.13, -81.2595616485, 17.6997661969)
                Line((0.08, 0.032), (0.1614680108, -0.0494680108))
                Line((0, 0.032), (0.08, 0.032))
            make_face()
            with BuildLine():
                CenterArc((0.03, 0.0181777145), 0.005, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.0137895819, 0), 0.005, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.0437895819, 0), 0.005, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.03, -0.0218222855), 0.005, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=0.01
        extrude(amount=0.005, both=True)
    return part.part


# Description: This is a clamp or bracket with an angular L-shaped profile, featuring a C-shaped clamping head at the top and a rectangular base with four circular holes along its length for mounting or securing purposes.
def model_142408_d8a5427b_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 27 constraints, 14 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 111.3404516544, perimeter: 118.8560509146
            with BuildLine():
                CenterArc((2.3101308193, 5.608217553), 1.905, 90, 101.5369590328)
                CenterArc((0.7547048326, 5.290717553), 0.3175, -168.4630409672, 78.4630409672)
                Line((0.7547048326, 4.973217553), (5.1676308193, 4.973217553))
                Line((5.1676308193, 4.973217553), (5.1676308193, -0.106782447))
                Line((5.1676308193, -0.106782447), (0.0876308193, -0.106782447))
                Line((0.0876308193, -0.106782447), (0.0876308193, 4.3061435397))
                CenterArc((-0.2298691807, 4.3061435397), 0.3175, 0, 78.4630409672)
                CenterArc((-0.5473691807, 2.750717553), 1.905, 78.4630409672, 101.5369590328)
                Line((-2.4523691807, -0.1065128362), (-2.4523691807, 2.750717553))
                CenterArc((0.0876308193, -0.1065128362), 2.54, 180, 90)
                Line((0.5670035127, -2.6465128362), (0.0876308193, -2.6465128362))
                CenterArc((0.5670035127, -5.1865128362), 2.54, 67.5392299975, 22.4607700025)
                Line((1.5374124665, -2.8391938416), (17.6483623849, -9.4996477855))
                CenterArc((18.0122657426, -8.6194031625), 0.9525, -112.4607700025, 90)
                Line((20.1049360192, -6.0505741344), (18.8925103656, -8.9833065202))
                CenterArc((19.2246913962, -5.6866707768), 0.9525, -22.4607700025, 89.9879949716)
                Line((8.2965842707, -0.1354071648), (19.5887791811, -4.8065024208))
                CenterArc((8.6606720557, 0.7447611912), 0.9525, 180, 67.527224969)
                Line((7.7081720557, 4.973217553), (7.7081720557, 0.7447611912))
                CenterArc((5.1681720557, 4.973217553), 2.54, 0, 90)
                Line((2.3101308193, 7.513217553), (5.1681720557, 7.513217553))
            make_face()
            with BuildLine():
                CenterArc((17.1514041978, -6.5465313735), 1.905, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((13.3370108315, -4.9696168236), 1.5875, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((10.109447214, -3.6353045121), 1.27, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((7.4687133451, -2.5435944391), 0.9525, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.9525
        extrude(amount=0.9525)
    return part.part


# Description: A flat, parallelogram-shaped plate with a slightly beveled or chamfered edge on the left side and diagonal surface lines suggesting a 3D depth or thickness to the part.
def model_142411_e422dd79_0000():
    """Model: Component15"""
    with BuildPart() as part:
        # Sketch1 -> 拉伸1 (NewBody)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 10.2000013046, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 86.1064613088, perimeter: 37.5992470937
            with BuildLine():
                Line((5.4499058979, 1.3500942034), (-5.4499058979, 1.3500942034))
                Line((5.4499058979, 9.2499059545), (5.4499058979, 1.3500942034))
                Line((-5.4499058979, 9.2499059545), (5.4499058979, 9.2499059545))
                Line((-5.4499058979, 1.3500942034), (-5.4499058979, 9.2499059545))
            make_face()
        # OneSide extrude, distance=0.299
        extrude(amount=0.299)
    return part.part


# Description: This is a dual-arm bracket or support assembly with an elongated base featuring two upright cylindrical/tubular arms extending upward at angles, designed to provide structural support or mounting points.
def model_142460_c5e6d8b8_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 22 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 55.9060976856, perimeter: 55.7026810688
            with BuildLine():
                Line((-4.5721651413, 2.6000667969), (-7.4863787036, 5.5142803593))
                Line((-7.4863787036, 5.5142803593), (-8.5470388754, 4.4536201875))
                Line((-8.5470388754, 4.4536201875), (-5.1934854848, 1.1000667969))
                CenterArc((-3.7792719224, 2.5142803593), 2, -135, 45)
                Line((-3.7792719224, 0.5142803593), (11.4529611246, 0.5142803593))
                Line((11.4529611246, 0.5142803593), (11.4529611246, 2.0142803593))
                Line((11.4529611246, 2.0142803593), (7.4529611246, 2.0142803593))
                CenterArc((7.4529611246, 2.5142803593), 0.5, 180, 90)
                Line((6.9529611246, 2.5142803593), (6.9529611246, 6.5142803593))
                CenterArc((4.9529611246, 6.5142803593), 2, 0, 180)
                Line((2.9529611246, 6.5142803593), (2.9529611246, 2.5142803593))
                CenterArc((2.4529611246, 2.5142803593), 0.5, -90, 90)
                Line((2.4529611246, 2.0142803593), (-3.1579515789, 2.0142803593))
                CenterArc((-3.1579515789, 4.0142803593), 2, -135, 45)
            make_face()
        # Symmetric extrude, full_length=True, total=2
        extrude(amount=1, both=True)
    return part.part


# Description: This is a dark gray curved bracket or mounting plate with an organic, rounded shape featuring a rectangular slot opening, a small circular hole, and a curved cutout at the bottom.
def model_142461_5238e16d_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 50 constraints, 15 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 183.0359872539, perimeter: 107.4948720902
            with BuildLine():
                CenterArc((3.4532544255, -10.4298825799), 0.5, -170.6252776943, 98.9445903889)
                CenterArc((0, 0), 11.4866927125, -71.6806873054, 69.018066001)
                CenterArc((10.9748314105, -0.510384433), 0.5, -2.6626213043, 59.8825584605)
                Line((11.2455392537, -0.0900069078), (7.9998952322, 2.0000698452))
                Line((7.9998952322, 2.0000698452), (4, 3.5))
                Line((4, 3.5), (0, 4))
                Line((-4, 3.5), (0, 4))
                Line((-7.9998952322, 2.0000698452), (-4, 3.5))
                Line((-10.7739965201, 0.1506689866), (-7.9998952322, 2.0000698452))
                CenterArc((-10.496646422, -0.2653561606), 0.5, 123.690067526, 57.7580664657)
                CenterArc((0, 0), 11, -178.5518660083, 70.0028663949)
                CenterArc((-3.3402132856, -9.9545454545), 0.5, -108.5489996134, 91.1693828056)
                CenterArc((0, -11), 3, 9.3747223057, 153.2456608865)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, -7), 2, 24.9742400599, 130.0515198802)
                CenterArc((-2.266244257, -5.9444731328), 0.5, -90, 65.0257599401)
                Line((-2.266244257, -6.4444731328), (-6.5, -6.4444731328))
                CenterArc((-6.5, -5.9444731328), 0.5, 180, 90)
                Line((-7, -5.9444731328), (-7, -2.9444731328))
                CenterArc((-6.5, -2.9444731328), 0.5, 90, 90)
                Line((-6.5, -2.4444731328), (6.5, -2.4444731328))
                CenterArc((6.5, -2.9444731328), 0.5, 0, 90)
                Line((7, -2.9444731328), (7, -5.9444731328))
                CenterArc((6.5, -5.9444731328), 0.5, -90, 90)
                Line((6.5, -6.4444731328), (2.266244257, -6.4444731328))
                CenterArc((2.266244257, -5.9444731328), 0.5, -155.0257599401, 65.0257599401)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=0.2
        extrude(amount=0.1, both=True)
    return part.part


# Description: This is a cylindrical suppressor or silencer with a long tubular body, rounded end caps, and a slightly tapered design, featuring a smooth exterior surface with subtle surface details or markings along its length.
def model_142581_460e171c_0001():
    """Model: Zitstok 5 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=3.5
        extrude(amount=3.5)
    return part.part


# Description: This is a dark blue angled bracket or support component with a trapezoidal profile, featuring a central oval hole and a vertical slot on its side, designed for structural mounting or assembly purposes.
def model_142680_cd829f9e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 9 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 180.737279468, perimeter: 66.1157216133
            with BuildLine():
                Line((-6.25, -11.5), (6.25, -11.5))
                Line((6.25, -11.5), (6.25, 0.5))
                Line((0, 6.75), (6.25, 0.5))
                Line((-6.25, 0.5), (0, 6.75))
                Line((-6.25, -11.5), (-6.25, 0.5))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, -2.8), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.7
        extrude(amount=1.7)
    return part.part


# Description: This is a wedge-shaped bracket or support block featuring a trapezoidal profile with angled top and bottom faces, a flat vertical back surface, and a recessed slot or channel along its left edge.
def model_142680_cd829f9e_0002():
    """Model: Back"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 181.0200228068, perimeter: 64.2307660212
            with BuildLine():
                Line((-6.25, -11.75), (6.25, -11.75))
                Line((6.25, -11.75), (6.25, 0.25))
                Line((0, 6.5), (6.25, 0.25))
                Line((-6.25, 0.25), (0, 6.5))
                Line((-6.25, -11.75), (-6.25, 0.25))
            make_face()
            with BuildLine():
                CenterArc((0, -0.25), 1.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 8.0424771932, perimeter: 10.0530964915
            with Locations((0, -0.25)):
                Circle(1.6)
        # OneSide extrude, distance=1.7
        extrude(amount=1.7)
    return part.part


# Description: This is a geometric solid composed of two square pyramids joined at their bases, forming an octahedron with eight triangular faces, a square cross-section at the center, and symmetrical pointed vertices at the top and bottom.
def model_142680_cd829f9e_0003():
    """Model: RoofL"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.7), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 22.95, perimeter: 30.4
            with BuildLine():
                Line((-1.3413548656, 21.665197531), (-0.0056930258, 20.6135286431))
                Line((-9.6928430929, 11.0584711562), (-1.3413548656, 21.665197531))
                Line((-8.3571812531, 10.0068022683), (-9.6928430929, 11.0584711562))
                Line((-0.0056930258, 20.6135286431), (-8.3571812531, 10.0068022683))
            make_face()
        # OneSide extrude, distance=18
        extrude(amount=18)
    return part.part


# Description: This is a thin, elongated wedge or blade-shaped component with a pointed upper edge, a flat bottom surface, and a tapered profile that gradually widens along its length.
def model_142680_cd829f9e_0004():
    """Model: RoofR"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.7), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 20.06, perimeter: 27
            with BuildLine():
                Line((13.3640288931, 21.4553083355), (21.2578127262, 12.6844374098))
                Line((21.2578127262, 12.6844374098), (22.5214127748, 13.8216774536))
                Line((22.5214127748, 13.8216774536), (14.6276289417, 22.5925483793))
                Line((14.6276289417, 22.5925483793), (13.3640288931, 21.4553083355))
            make_face()
        # OneSide extrude, distance=18
        extrude(amount=18)
    return part.part


# Description: This is a parallelepiped or wedge-shaped block with a slanted top surface, featuring a rectangular base and angled sides that taper upward, creating an asymmetrical geometric form.
def model_142680_cd829f9e_0005():
    """Model: Side"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 21.845, perimeter: 29.804163056
            with BuildLine():
                Line((-1.7, 0), (-1.7, 12))
                Line((0, 0), (-1.7, 0))
                Line((0, 13.7), (0, 0))
                Line((-1.7, 12), (0, 13.7))
            make_face()
        # OneSide extrude, distance=12.5
        extrude(amount=12.5)
    return part.part


# Description: This is a thin, elongated rectangular plate or blade with a tapered wedge-shaped profile, featuring a sloped top surface that gradually rises from one end to the other, creating an aerodynamic or streamlined form.
def model_142680_cd829f9e_0006():
    """Model: Bottom"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 262.5, perimeter: 67
            with BuildLine():
                Line((-6.25, 10.5), (-6.25, -10.5))
                Line((-6.25, -10.5), (6.25, -10.5))
                Line((6.25, -10.5), (6.25, 10.5))
                Line((6.25, 10.5), (-6.25, 10.5))
            make_face()
        # OneSide extrude, distance=1.7
        extrude(amount=1.7)
    return part.part


# Description: This is a polyhedron or geometric solid with an irregular, blocky shape featuring multiple faceted surfaces in dark navy and blue tones, with visible edge lines defining its angular geometry and complex three-dimensional structure.
def model_142680_cd829f9e_0007():
    """Model: Light for pictures"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1, perimeter: 4
            with BuildLine():
                Line((-3.3854660553, -11.8894235811), (-4.3854660553, -11.8894235811))
                Line((-3.3854660553, -10.8894235811), (-3.3854660553, -11.8894235811))
                Line((-4.3854660553, -10.8894235811), (-3.3854660553, -10.8894235811))
                Line((-4.3854660553, -11.8894235811), (-4.3854660553, -10.8894235811))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a rectangular hollow channel or tube with an elongated prismatic shape, featuring a longitudinal slot or open groove running along one side, and appears to be tilted at an angle in the isometric view.
def model_142852_00b5fde9_0001():
    """Model: Support - Vert"""
    with BuildPart() as part:
        # profile -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.635), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 22.5806, perimeter: 23.9121024484
            with BuildLine():
                Line((1.5875, 0), (1.5875, -10.16))
                Line((1.5875, -10.16), (4.1275, -10.16))
                Line((4.1275, -10.16), (4.1275, -2.54))
                Line((1.5875, 0), (4.1275, -2.54))
            make_face()
            # Profile area: 3.2258, perimeter: 8.6721024484
            with BuildLine():
                Line((1.5875, 0), (4.1275, -2.54))
                Line((4.1275, -2.54), (4.1275, 0))
                Line((4.1275, 0), (1.5875, 0))
            make_face()
            # Profile area: 6.4516, perimeter: 21.59
            with BuildLine():
                Line((0.9525, -10.16), (1.5875, -10.16))
                Line((1.5875, 0), (1.5875, -10.16))
                Line((1.5875, 0), (0.9525, 0))
                Line((0.9525, 0), (0.9525, -2.54))
                Line((0.9525, -2.54), (0.9525, -10.16))
            make_face()
        # OneSide extrude, distance=-1.27
        extrude(amount=-1.27)
    return part.part


# Description: This is a flat, elongated parallelogram-shaped plate or panel with a trapezoidal profile, featuring a thin depth and internal diagonal reinforcement ribs or stiffeners running across its upper surface.
def model_142961_244ceb90_0002():
    """Model: 工作桌面 v1"""
    with BuildPart() as part:
        # Sketch1 -> 拉伸1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 10000, perimeter: 400
            with BuildLine():
                Line((55, -62.2170201767), (-45, -62.2170201767))
                Line((55, 37.7829798233), (55, -62.2170201767))
                Line((-45, 37.7829798233), (55, 37.7829798233))
                Line((-45, -62.2170201767), (-45, 37.7829798233))
            make_face()
        # OneSide extrude, distance=-10
        extrude(amount=-10)
    return part.part


# Description: This is a cylindrical mesh or perforated container with an elliptical cross-section, featuring a solid dark base section and an open mesh top, commonly used as a filter, strainer, or ventilation component.
def model_142999_171240b6_0007():
    """Model: DC fan 5v v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.2698006922, perimeter: 5.3407075111
            Circle(0.85)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)
    return part.part


# Description: This is a mesh-topped cylindrical container or basket with an elliptical cross-section, featuring a solid dark base band and a perforated or mesh upper section that curves inward at the top.
def model_142999_171240b6_0009():
    """Model: m3 25 screw black v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2471812954, perimeter: 1.7624334787
            Circle(0.2805)
        # OneSide extrude, distance=0.163
        extrude(amount=0.163)
    return part.part


# Description: This is a hexagonal or polygonal prism-like component with a complex faceted geometry, featuring multiple planar surfaces in varying shades that suggest internal voids or cutouts, and an overall angular, geometric form typical of structural or mechanical parts.
def model_143017_21d96cc2_0005():
    """Model: active chamber v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 225.806, perimeter: 60.96
            with BuildLine():
                Line((8.89, -6.35), (-8.89, -6.35))
                Line((8.89, 6.35), (8.89, -6.35))
                Line((-8.89, 6.35), (8.89, 6.35))
                Line((-8.89, -6.35), (-8.89, 6.35))
            make_face()
        # OneSide extrude, distance=8.89
        extrude(amount=8.89)
    return part.part


# Description: This is a rectangular tower or column structure with a tapered hexagonal profile, featuring multiple rectangular apertures (windows or openings) arranged vertically along its sides and triangular cutouts or vents between them.
def model_143019_54c55d14_0006():
    """Model: cable combs v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 18 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.261179434, perimeter: 4.010530784
            with BuildLine():
                CenterArc((0, -0.43), 0.075, 90, 90)
                Line((0, -0.355), (0, -0.05))
                CenterArc((0, 0), 0.05, 90, 180)
                Line((0, 0.05), (0, 0.355))
                CenterArc((0, 0.43), 0.075, 180, 90)
                Line((-0.075, 0.43), (-0.355, 0.43))
                CenterArc((-0.43, 0.43), 0.075, -90, 90)
                Line((-0.43, 0.05), (-0.43, 0.355))
                CenterArc((-0.43, 0), 0.05, -90, 180)
                Line((-0.43, -0.355), (-0.43, -0.05))
                CenterArc((-0.43, -0.43), 0.075, 0, 90)
                Line((-0.355, -0.43), (-0.075, -0.43))
            make_face()
            with BuildLine():
                CenterArc((-0.215, 0.215), 0.115, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-0.215, -0.215), 0.115, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)
    return part.part


# Description: This is a polyhedron-shaped structural component with an irregular faceted geometry featuring multiple angular surfaces, internal mesh/lattice reinforcement patterns, and hollow cavities, designed for lightweight strength in applications requiring complex 3D geometry.
def model_143293_fc5b0ff7_0015():
    """Model: nut_L v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.8622314814, perimeter: 6.3560367957
            with BuildLine():
                Line((0.6, 0.3464101615), (0, 0.692820323))
                Line((0, 0.692820323), (-0.6, 0.3464101615))
                Line((-0.6, 0.3464101615), (-0.6, -0.3464101615))
                Line((-0.6, -0.3464101615), (0, -0.692820323))
                Line((0, -0.692820323), (0.6, -0.3464101615))
                Line((0.6, -0.3464101615), (0.6, 0.3464101615))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.35, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)
    return part.part


# Description: This is a torus (donut-shaped) component with a smooth, curved surface featuring a central hole and characterized by its symmetrical, rounded geometry throughout.
def model_143293_fc5b0ff7_0019():
    """Model: washer_L v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.638937829, perimeter: 8.7964594301
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a toroidal (donut-shaped) disk or washer with a smooth outer rim and a central hole, featuring a textured or mesh-patterned surface on the top face and a solid dark base, designed as a mechanical component or spacer.
def model_143293_fc5b0ff7_0022():
    """Model: washer_S v1 (7)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.0445795573, perimeter: 5.9690260418
            with BuildLine():
                CenterArc((0, 0), 0.65, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.07
        extrude(amount=0.07)
    return part.part


# Description: This is a complex polyhedral geometric solid featuring multiple angled facets and triangular faces arranged in an irregular, faceted three-dimensional form with a mix of flat surfaces and linear edge details.
def model_143293_fc5b0ff7_0026():
    """Model: nut_S v1 (5)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5051310362, perimeter: 4.6884877804
            with BuildLine():
                Line((0.45, 0.2598076211), (0, 0.5196152423))
                Line((0, 0.5196152423), (-0.45, 0.2598076211))
                Line((-0.45, 0.2598076211), (-0.45, -0.2598076211))
                Line((-0.45, -0.2598076211), (0, -0.5196152423))
                Line((0, -0.5196152423), (0.45, -0.2598076211))
                Line((0.45, -0.2598076211), (0.45, 0.2598076211))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a stamped or formed metal bracket with a U-shaped channel profile, featuring two rectangular flanges with triangulated reinforcement ribs on the upper surfaces and cutout openings on the sides.
def model_143346_3c91017f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 14 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 18.5, perimeter: 24.6055512755
            with BuildLine():
                Line((1, 1), (1, 0))
                Line((2.5, 0), (1, 1))
                Line((4.5, 0), (2.5, 0))
                Line((6, 1), (4.5, 0))
                Line((6, 0), (6, 1))
                Line((7, 0), (6, 0))
                Line((7, 3), (7, 0))
                Line((4, 3), (7, 3))
                Line((4, 2), (4, 3))
                Line((3, 2), (4, 2))
                Line((3, 3), (3, 2))
                Line((0, 3), (3, 3))
                Line((0, 0), (0, 3))
                Line((1, 0), (0, 0))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a hexagonal prism or wedge-shaped structural component with a tapered top surface featuring triangulated facets and internal geometric divisions, appearing to be designed for structural support or load distribution.
def model_143754_92a6452a_0002():
    """Model: wood spacer"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 80), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 4.28625, perimeter: 9.87
            with BuildLine():
                Line((-93.2, 0), (-92.075, 0))
                Line((-93.2, -3.81), (-93.2, 0))
                Line((-92.075, -3.81), (-93.2, -3.81))
                Line((-92.075, 0), (-92.075, -3.81))
            make_face()
            # Profile area: 24.1935, perimeter: 20.32
            with BuildLine():
                Line((-92.075, 0), (-92.075, -3.81))
                Line((-85.725, -3.81), (-92.075, -3.81))
                Line((-85.725, -3.81), (-85.725, 0))
                Line((-92.075, 0), (-85.725, 0))
            make_face()
            # Profile area: 4.28625, perimeter: 9.87
            with BuildLine():
                Line((-85.725, -3.81), (-85.725, 0))
                Line((-84.6, -3.81), (-85.725, -3.81))
                Line((-84.6, 0), (-84.6, -3.81))
                Line((-85.725, 0), (-84.6, 0))
            make_face()
        # OneSide extrude, distance=10
        extrude(amount=10)
    return part.part


# Description: This is an extruded angular channel or corner bead with a long, tapered V-shaped profile featuring two parallel flanges that form a sharp interior corner, commonly used as trim or reinforcement in construction or manufacturing applications.
def model_143754_92a6452a_0003():
    """Model: metal channel"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 12 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 90), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.5785000238, perimeter: 31.7700000089
            with BuildLine():
                Line((-88.9, 0), (-84.6, 0))
                Line((-84.6, 0), (-84.2825, 0))
                Line((-84.2825, 0), (-84.2825, -3.175))
                Line((-84.1824999985, -3.175), (-84.2825, -3.175))
                Line((-84.1824999985, 0.1000000015), (-84.1824999985, -3.175))
                Line((-88.9, 0.1000000015), (-84.1824999985, 0.1000000015))
                Line((-88.9, 0.1000000015), (-93.6175000015, 0.1000000015))
                Line((-93.6175000015, 0.1000000015), (-93.6175000015, -3.175))
                Line((-93.6175000015, -3.175), (-93.5175, -3.175))
                Line((-93.5175, 0), (-93.5175, -3.175))
                Line((-93.2, 0), (-93.5175, 0))
                Line((-88.9, 0), (-93.2, 0))
            make_face()
        # OneSide extrude, distance=-44.45
        extrude(amount=-44.45)
    return part.part


# Description: This is a long, narrow rectangular tray or channel with a shallow depth, featuring a flat base and angled side walls that slope outward, creating a trapezoidal cross-section profile.
def model_143754_92a6452a_0004():
    """Model: horiz spacer"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 169.3545, perimeter: 85.09
            with BuildLine():
                Line((0, -4.445), (0, 0))
                Line((0, 0), (-38.1, 0))
                Line((-38.1, 0), (-38.1, -4.445))
                Line((-38.1, -4.445), (0, -4.445))
            make_face()
        # OneSide extrude, distance=1.11125
        extrude(amount=1.11125)
    return part.part


# Description: This is a long, flat rectangular bar or rail with a slightly tapered trapezoidal profile, featuring a subtle curved or beveled top edge running along its entire length.
def model_143754_92a6452a_0006():
    """Model: L channel"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 6 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.97425, perimeter: 19.685
            with BuildLine():
                Line((-0.1, 0.1), (-2.8575, 0.1))
                Line((-2.8575, 0), (-2.8575, 0.1))
                Line((0, 0), (-2.8575, 0))
                Line((0, 0), (0, 6.985))
                Line((-0.1, 6.985), (0, 6.985))
                Line((-0.1, 0.1), (-0.1, 6.985))
            make_face()
        # OneSide extrude, distance=152.4
        extrude(amount=152.4)
    return part.part


# Description: This is a hook or cable clamp with a curved body featuring a lightning bolt strike symbol on top, designed to secure and hang objects or electrical conduits.
def model_143812_9f085870_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 41 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 15.204278521, perimeter: 18.2384289984
            with BuildLine():
                Line((0, 0), (0, 5.4098360656))
                Line((-5.4546387058, 0.4917191997), (0, 5.4098360656))
                CenterArc((0, 30.5), 30.5, -100.3022360965, 10.3022360965)
            make_face()
            # Profile area: 0.6628834862, perimeter: 6.4534439155
            with BuildLine():
                CenterArc((0, 85.5), 24.5, 90, 0.6957662528)
                CenterArc((-161.8053278688, 100.75), 161.772388, 2.2139517795, 1.0633164753)
                CenterArc((0, 85.5), 21.5, 90, 0.4095926764)
                Line((0, 107), (0, 110))
            make_face()
            # Profile area: 93.8828873759, perimeter: 44.9894999459
            with BuildLine():
                CenterArc((0, 30.5), 30.5, -133.7716720265, 28.8415913665)
                Line((-7.8580233999, 1.0296510328), (-2.2324162294, 6.1019197932))
                CenterArc((0, 30.5), 24.5, -132.7431662645, 37.5151789517)
                Line((-21.0994802953, 8.4758784223), (-16.6284723511, 12.5071150932))
            make_face()
            # Profile area: 7.1005050431, perimeter: 12.8570568706
            with BuildLine():
                CenterArc((0, 30.5), 21.5, -87.3126637306, 9.429788007)
                Line((0, 8.1147540984), (1.0080419293, 9.0236443625))
                Line((0, 6), (0, 8.1147540984))
                CenterArc((0, 30.5), 24.5, -90, 1.5542932529)
                Line((0.6645430891, 6.0090142607), (4.5130819529, 9.4790083182))
            make_face()
            # Profile area: 23.8118828427, perimeter: 19.4735405428
            with BuildLine():
                Line((0, 58), (0, 61))
                CenterArc((0, 30.5), 30.5, 90, 8.0971148938)
                CenterArc((-161.8053278688, 100.75), 162.5223880785, -16.1525058401, 1.8848128075)
                CenterArc((0, 85.5), 30.5, -100.7683372268, 4.8464649584)
                Line((-3.1467536318, 55.1627631189), (0, 58))
            make_face()
            # Profile area: 49.1072392346, perimeter: 40.1925651992
            with BuildLine():
                CenterArc((0, 30.5), 24.5, -0.6938849556, 37.5151789517)
                Line((17.37382327, 43.1649226205), (19.612462864, 45.1833681561))
                CenterArc((0, 30.5), 21.5, -8.6092085377, 44.6999771849)
                Line((21.2577452038, 27.2815735444), (24.4982033625, 30.2032981137))
            make_face()
            # Profile area: 93.8828873759, perimeter: 44.9894999459
            with BuildLine():
                CenterArc((0, 30.5), 30.5, 9.0082083917, 28.8415913665)
                Line((19.612462864, 45.1833681561), (24.0834708082, 49.214604827))
                CenterArc((0, 30.5), 24.5, -0.6938849556, 37.5151789517)
                Line((24.4982033625, 30.2032981137), (30.1238105331, 35.2755668741))
            make_face()
            # Profile area: 2.25227254, perimeter: 7.5082217093
            with BuildLine():
                CenterArc((0, 85.5), 24.5, 94.2045883532, 1.7548881225)
                CenterArc((-161.8053278688, 100.75), 159.522388, 2.1970842814, 1.0794737627)
                CenterArc((0, 85.5), 21.5, 94.4078071263, 2.0019212254)
                CenterArc((-161.8053278688, 100.75), 160.272388, 2.2121291117, 1.0728804879)
            make_face()
            # Profile area: 64.4530011677, perimeter: 48.9829659162
            with BuildLine():
                CenterArc((0, 30.5), 24.5, 36.8212939961, 53.1787060039)
                Line((0, 52), (0, 55))
                CenterArc((0, 30.5), 21.5, 36.0907686471, 53.9092313529)
                Line((17.37382327, 43.1649226205), (19.612462864, 45.1833681561))
            make_face()
            # Profile area: 15.8422720907, perimeter: 21.1775449951
            with BuildLine():
                CenterArc((0, 30.5), 30.5, 4.3803638282, 4.6278445635)
                Line((24.4982033625, 30.2032981137), (30.1238105331, 35.2755668741))
                CenterArc((0, 30.5), 24.5, -7.4761655212, 6.7822805656)
                Line((24.2917272933, 27.3122131333), (30.4109090882, 32.8295081943))
            make_face()
            # Profile area: 0.4422083269, perimeter: 3.2509452735
            with BuildLine():
                CenterArc((0, 30.5), 21.5, -90, 2.6873362694)
                Line((0, 8.1147540984), (0, 9))
                Line((0, 8.1147540984), (1.0080419293, 9.0236443625))
            make_face()
            # Profile area: 22.5086347988, perimeter: 25.1286049973
            with BuildLine():
                Line((0, 0), (8.2358293836, 7.4257478049))
                CenterArc((0, 30.5), 24.5, -88.4457067471, 18.0885741228)
                Line((0, 5.4098360656), (0.6645430891, 6.0090142607))
                Line((0, 0), (0, 5.4098360656))
            make_face()
            # Profile area: 41.5592679566, perimeter: 43.9054087761
            with BuildLine():
                Line((4.5130819529, 9.4790083182), (20.4431884295, 23.8422190758))
                CenterArc((0, 30.5), 21.5, -77.8828757236, 59.8438791788)
            make_face()
            # Profile area: 37.7129133198, perimeter: 32.5473618645
            with BuildLine():
                Line((24.2917272933, 27.3122131333), (30.4109090882, 32.8295081943))
                CenterArc((0, 30.5), 24.5, -25.5647396439, 18.0885741228)
                Line((22.1014074975, 19.9274985633), (30.3372368811, 27.3532463682))
                CenterArc((0, 30.5), 30.5, -5.9218722683, 10.3022360965)
            make_face()
            # Profile area: 1.4731930285, perimeter: 12.4755566094
            with BuildLine():
                Line((0, 110), (0, 116))
                CenterArc((0, 85.5), 24.5, 88.9385564053, 1.0614435947)
                CenterArc((-161.8053278688, 100.75), 162.5223880785, 3.261281424, 2.1228871894)
            make_face()
            # Profile area: 4.8056756528, perimeter: 10.3893398513
            with BuildLine():
                CenterArc((0, 30.5), 30.5, 84.0781277317, 5.9218722683)
                Line((0, 58), (0, 61))
                Line((0, 58), (3.1467536318, 60.8372368811))
            make_face()
            # Profile area: 0.9198335054, perimeter: 9.1363328988
            with BuildLine():
                CenterArc((0, 85.5), 24.5, -99.7068936321, 9.7068936321)
                CenterArc((-161.8053278688, 100.75), 162.5223880785, -14.2676930326, 0.2380743819)
                CenterArc((0, 30.5), 30.5, 90, 8.0971148938)
            make_face()
            # Profile area: 17.3307565898, perimeter: 19.3641051554
            with BuildLine():
                CenterArc((0, 30.5), 24.5, 90, 8.5125048455)
                Line((-6.8112314344, 51.8587257559), (-3.6266188954, 54.7300977172))
                CenterArc((-161.8053278688, 100.75), 162.5223880785, -17.9089340157, 0.4015964761)
                CenterArc((0, 30.5), 21.5, 90, 19.4459446856)
                Line((0, 52), (0, 55))
            make_face()
            # Profile area: 48.4998134884, perimeter: 31.3669350523
            with BuildLine():
                CenterArc((0, 30.5), 30.5, 64.3743954473, 19.7037322844)
                Line((0, 58), (3.1467536318, 60.8372368811))
                Line((0, 55), (0, 58))
                CenterArc((0, 85.5), 30.5, -90, 25.6256045527)
            make_face()
            # Profile area: 9.4989951752, perimeter: 15.9836780797
            with BuildLine():
                CenterArc((0, 30.5), 24.5, -7.4761655212, 6.7822805656)
                Line((21.2577452038, 27.2815735444), (24.4982033625, 30.2032981137))
                CenterArc((0, 30.5), 21.5, -18.0389965447, 9.429788007)
                Line((20.4431884295, 23.8422190758), (24.2917272933, 27.3122131333))
            make_face()
            # Profile area: 3.0384505971, perimeter: 13.0601645085
            with BuildLine():
                CenterArc((0, 85.5), 30.5, 90, 1.4136782911)
                CenterArc((-161.8053278688, 100.75), 161.772388, 3.2772682548, 2.1286337687)
                CenterArc((0, 85.5), 24.5, 90, 0.6957662528)
                Line((0, 110), (0, 116))
            make_face()
            # Profile area: 77.2756746218, perimeter: 55.2268224817
            with BuildLine():
                Line((0, 55), (18.1659021246, 55))
                CenterArc((0, 30.5), 24.5, 36.8212939961, 53.1787060039)
                Line((19.612462864, 45.1833681561), (24.0834708082, 49.214604827))
                CenterArc((0, 30.5), 30.5, 37.8497997582, 15.5945448472)
            make_face()
            # Profile area: 9.0056260101, perimeter: 15.0125638637
            with BuildLine():
                CenterArc((0, 85.5), 30.5, 91.4136782911, 2.8210000194)
                CenterArc((-161.8053278688, 100.75), 160.272388, 3.2850095997, 2.1450715458)
                CenterArc((0, 85.5), 24.5, 90.6957662528, 3.5088221004)
                CenterArc((-161.8053278688, 100.75), 161.772388, 3.2772682548, 2.1286337687)
            make_face()
            # Profile area: 62.987867339, perimeter: 66.9589626474
            with BuildLine():
                Line((20.4431884295, 23.8422190758), (24.2917272933, 27.3122131333))
                CenterArc((0, 30.5), 21.5, -77.8828757236, 59.8438791788)
                Line((0.6645430891, 6.0090142607), (4.5130819529, 9.4790083182))
                CenterArc((0, 30.5), 24.5, -88.4457067471, 18.0885741228)
                Line((8.2358293836, 7.4257478049), (22.1014074975, 19.9274985633))
                CenterArc((0, 30.5), 24.5, -25.5647396439, 18.0885741228)
            make_face()
            # Profile area: 3.9060052023, perimeter: 11.9773767327
            with BuildLine():
                CenterArc((0, 30.5), 30.5, 98.0971148938, 1.5327744648)
                CenterArc((-161.8053278688, 100.75), 161.772388, -16.1742392502, 1.7930256974)
                CenterArc((0, 85.5), 30.5, -102.1820155178, 1.4136782911)
                CenterArc((-161.8053278688, 100.75), 162.5223880785, -16.1525058401, 1.8848128075)
            make_face()
            # Profile area: 0.195096141, perimeter: 2.1495689721
            with BuildLine():
                CenterArc((0, 30.5), 24.5, -90, 1.5542932529)
                Line((0, 5.4098360656), (0, 6))
                Line((0, 5.4098360656), (0.6645430891, 6.0090142607))
            make_face()
            # Profile area: 0.1152328131, perimeter: 2.1728689727
            with BuildLine():
                Line((-8.6882666474, 50.1663169573), (-7.9176991576, 50.8610909235))
                CenterArc((0, 30.5), 21.5, 112.0086901754, 1.8263904635)
                CenterArc((-161.8053278688, 100.75), 161.772388, -18.1215760446, 0.1593737838)
            make_face()
            # Profile area: 1.5905866657, perimeter: 7.058664667
            with BuildLine():
                CenterArc((0, 85.5), 24.5, 88.9385564053, 1.0614435947)
                Line((0, 107), (0, 110))
                CenterArc((0, 85.5), 21.5, 88.408414377, 1.591585623)
                CenterArc((-161.8053278688, 100.75), 162.5223880785, 2.2009973674, 1.0602840566)
            make_face()
            # Profile area: 15.6471759497, perimeter: 20.2083038919
            with BuildLine():
                Line((-5.4546387058, 0.4917191997), (0, 5.4098360656))
                Line((0, 5.4098360656), (0, 6))
                CenterArc((0, 30.5), 24.5, -95.2279873127, 5.2279873127)
                Line((-7.8580233999, 1.0296510328), (-2.2324162294, 6.1019197932))
                CenterArc((0, 30.5), 30.5, -104.93008066, 4.6278445635)
            make_face()
            # Profile area: 48.6650309077, perimeter: 38.712111729
            with BuildLine():
                CenterArc((0, 30.5), 24.5, -132.7431662645, 37.5151789517)
                Line((-2.2324162294, 6.1019197932), (0, 8.1147540984))
                Line((0, 8.1147540984), (0, 9))
                CenterArc((0, 30.5), 21.5, -132.0126409155, 42.0126409155)
                Line((-16.6284723511, 12.5071150932), (-14.3898327571, 14.5255606288))
            make_face()
            # Profile area: 2.7796175615, perimeter: 9.2781549393
            with BuildLine():
                CenterArc((0, 30.5), 24.5, 98.5125048455, 5.8616076095)
                CenterArc((-161.8053278688, 100.75), 162.5223880785, -17.5073375396, 0.8756219486)
                Line((-6.8112314344, 51.8587257559), (-3.6266188954, 54.7300977172))
            make_face()
            # Profile area: 4.8056756528, perimeter: 10.3893398513
            with BuildLine():
                Line((0, 55), (0, 58))
                Line((-3.1467536318, 55.1627631189), (0, 58))
                CenterArc((0, 85.5), 30.5, -95.9218722683, 5.9218722683)
            make_face()
            # Profile area: 2.3984901321, perimeter: 7.3561294059
            with BuildLine():
                CenterArc((0, 30.5), 24.5, -95.2279873127, 5.2279873127)
                Line((0, 6), (0, 8.1147540984))
                Line((-2.2324162294, 6.1019197932), (0, 8.1147540984))
            make_face()
            # Profile area: 20.9196561908, perimeter: 37.6254068038
            with BuildLine():
                CenterArc((0, 85.5), 30.5, -90, 25.6256045527)
                Line((0, 55), (18.1659021246, 55))
                CenterArc((0, 30.5), 30.5, 53.4443446054, 10.9300508419)
            make_face()
            # Profile area: 0.5934630567, perimeter: 4.0406079938
            with BuildLine():
                Line((-7.9176991576, 50.8610909235), (-6.8112314344, 51.8587257559))
                CenterArc((-161.8053278688, 100.75), 161.772388, -18.1215760446, 0.1593737838)
                CenterArc((0, 30.5), 21.5, 109.4459446856, 2.5627454898)
                CenterArc((-161.8053278688, 100.75), 162.5223880785, -17.9089340157, 0.4015964761)
            make_face()
            # Profile area: 2.1652537714, perimeter: 8.1459402693
            with BuildLine():
                CenterArc((-161.8053278688, 100.75), 162.5223880785, -17.5073375396, 0.8756219486)
                CenterArc((0, 30.5), 24.5, 104.3741124549, 2.0711529865)
                CenterArc((-161.8053278688, 100.75), 161.772388, -17.9622022607, 1.1640831966)
                Line((-7.9176991576, 50.8610909235), (-6.8112314344, 51.8587257559))
            make_face()
            # Profile area: 49.2746950915, perimeter: 55.7916293584
            with BuildLine():
                CenterArc((0, 30.5), 21.5, -18.0389965447, 9.429788007)
                Line((1.0080419293, 9.0236443625), (21.2577452038, 27.2815735444))
                CenterArc((0, 30.5), 21.5, -87.3126637306, 9.429788007)
                Line((4.5130819529, 9.4790083182), (20.4431884295, 23.8422190758))
            make_face()
            # Profile area: 37.6392791548, perimeter: 33.6122699991
            with BuildLine():
                Line((7.0780667065, 76.5), (11.5581050771, 76.5))
                Line((0, 70.1181365761), (7.0780667065, 76.5))
                Line((0, 66.0787577174), (0, 70.1181365761))
                Line((0, 66.0787577174), (11.5581050771, 76.5))
            make_face()
            # Profile area: 1.2269359755, perimeter: 5.1081429708
            with BuildLine():
                CenterArc((-161.8053278688, 100.75), 160.272388, -14.6381223534, 0.584775527)
                CenterArc((0, 30.5), 30.5, 102.0772482753, 0.6802849598)
                Line((-6.3815234177, 60.3249251276), (-5.0494345617, 61.5259888503))
                CenterArc((0, 85.5), 24.5, -104.97292558, 3.079062897)
            make_face()
            # Profile area: 13.4401151117, perimeter: 17.9201534822
            with BuildLine():
                Line((7.0780667065, 76.5), (10.4053394338, 79.5))
                Line((7.0780667065, 76.5), (11.5581050771, 76.5))
                Line((11.5581050771, 76.5), (14.8853778043, 79.5))
                Line((10.4053394338, 79.5), (14.8853778043, 79.5))
            make_face()
            # Profile area: 26.2251092105, perimeter: 24.9634445109
            with BuildLine():
                Line((0, 79.5), (10.4053394338, 79.5))
                Line((0, 76.5), (0, 79.5))
                Line((0, 76.5), (7.0780667065, 76.5))
                Line((7.0780667065, 76.5), (10.4053394338, 79.5))
            make_face()
            # Profile area: 0.5262928822, perimeter: 3.6296562913
            with BuildLine():
                CenterArc((-161.8053278688, 100.75), 160.272388, -14.7547802445, 0.116657891)
                CenterArc((0, 30.5), 30.5, 102.7575332352, 1.5997355981)
                CenterArc((-161.8053278688, 100.75), 159.522388, -15.1686235972, 0.3859912304)
                Line((-7.8407110003, 59.0092641925), (-6.8179709302, 59.9314068787))
            make_face()
            # Profile area: 31.7216892106, perimeter: 86.0271111644
            with BuildLine():
                CenterArc((0, 85.5), 21.5, 94.4078071263, 2.0019212254)
                CenterArc((-161.8053278688, 100.75), 159.522388, -12.9654215081, 15.1625057895)
                CenterArc((0, 85.5), 21.5, -107.1780655785, 1.3135519107)
                Line((-5.8773154326, 64.8189177434), (-5.5435990853, 65.119809532))
                CenterArc((-161.8053278688, 100.75), 160.272388, -12.8447598935, 15.0568890053)
            make_face()
            # Profile area: 0.5992047345, perimeter: 3.6777535161
            with BuildLine():
                CenterArc((-161.8053278688, 100.75), 162.5223880785, -14.0296186507, 0.4678283364)
                Line((-4.8053273037, 61.7460855583), (-3.8144544885, 62.6394954737))
                CenterArc((-161.8053278688, 100.75), 161.772388, -14.0456054816, 0.0939172098)
                CenterArc((0, 85.5), 24.5, -101.4641034796, 1.7572098475)
            make_face()
            # Profile area: 5.6979123395, perimeter: 11.5713054027
            with BuildLine():
                CenterArc((-161.8053278688, 100.75), 161.772388, -17.9622022607, 1.1640831966)
                CenterArc((0, 30.5), 24.5, 106.4452654415, 4.3147837838)
                CenterArc((-161.8053278688, 100.75), 160.272388, -18.6213740857, 1.4412538471)
                CenterArc((0, 30.5), 21.5, 113.8350806389, 3.6520231154)
                Line((-8.6882666474, 50.1663169573), (-7.9176991576, 50.8610909235))
            make_face()
            # Profile area: 4.5009353826, perimeter: 9.0040858116
            with BuildLine():
                CenterArc((0, 85.5), 24.5, 90.6957662528, 3.5088221004)
                CenterArc((-161.8053278688, 100.75), 160.272388, 2.2121291117, 1.0728804879)
                CenterArc((0, 85.5), 21.5, 90.4095926764, 3.9982144499)
                CenterArc((-161.8053278688, 100.75), 161.772388, 2.2139517795, 1.0633164753)
            make_face()
            # Profile area: 1.0409178287, perimeter: 5.13547143
            with BuildLine():
                CenterArc((0, 85.5), 21.5, -99.1767516038, 3.3508793693)
                CenterArc((-161.8053278688, 100.75), 162.5223880785, -13.5617903143, 0.5924557202)
                Line((-3.8144544885, 62.6394954737), (-2.1823689143, 64.1110480406))
            make_face()
            # Profile area: 2.2564155522, perimeter: 8.0367033158
            with BuildLine():
                CenterArc((-161.8053278688, 100.75), 161.772388, -12.9822890063, 0.8860548694)
                CenterArc((0, 85.5), 21.5, -101.1779299032, 2.0011782994)
                CenterArc((-161.8053278688, 100.75), 162.5223880785, -12.9693345942, 1.2372385836)
                Line((-3.6247702284, 66.8499011242), (-2.6781853485, 67.7033792947))
            make_face()
            # Profile area: 4.500695565, perimeter: 13.5030597505
            with BuildLine():
                CenterArc((0, 85.5), 30.5, 94.2346783105, 1.4090000724)
                CenterArc((-161.8053278688, 100.75), 159.522388, 3.276558044, 2.1558311548)
                CenterArc((0, 85.5), 24.5, 94.2045883532, 1.7548881225)
                CenterArc((-161.8053278688, 100.75), 160.272388, 3.2850095997, 2.1450715458)
            make_face()
            # Profile area: 1.380509749, perimeter: 5.2917623384
            with BuildLine():
                CenterArc((-161.8053278688, 100.75), 159.522388, -14.7826323668, 0.737737096)
                CenterArc((0, 30.5), 30.5, 102.7575332352, 1.5997355981)
                CenterArc((-161.8053278688, 100.75), 160.272388, -14.6381223534, 0.584775527)
                CenterArc((0, 85.5), 24.5, -106.7278137025, 1.7548881225)
            make_face()
            # Profile area: 2.0719614824, perimeter: 7.1403674441
            with BuildLine():
                Line((-6.516572589, 64.2425383401), (-5.8773154326, 64.8189177434))
                CenterArc((-161.8053278688, 100.75), 159.522388, -14.0448952708, 0.8152377905)
                CenterArc((0, 85.5), 24.5, -106.7278137025, 1.7548881225)
                CenterArc((-161.8053278688, 100.75), 160.272388, -14.0533468264, 1.0728804879)
                CenterArc((0, 85.5), 21.5, -105.8645136677, 0.6883693146)
            make_face()
            # Profile area: 2.5938929338, perimeter: 9.0389573864
            with BuildLine():
                CenterArc((-161.8053278688, 100.75), 160.272388, -16.1984183722, 1.4436381278)
                Line((-7.8407110003, 59.0092641925), (-6.8179709302, 59.9314068787))
                CenterArc((-161.8053278688, 100.75), 159.522388, -16.2007264255, 1.0321028283)
                CenterArc((0, 85.5), 30.5, -106.4120156096, 1.4090000724)
            make_face()
            # Profile area: 2.656424213, perimeter: 7.8103348443
            with BuildLine():
                Line((-1.1022970115, 76.5), (0, 76.5))
                Line((0, 76.5), (0, 79.5))
                Line((-0.6781603063, 79.5), (0, 79.5))
                CenterArc((-161.8053278688, 100.75), 162.5223880785, -8.5811599804, 1.0681555739)
            make_face()
            # Profile area: 3.0942836772, perimeter: 10.3410513861
            with BuildLine():
                CenterArc((0, 30.5), 24.5, 110.7600492253, 2.2628614483)
                CenterArc((-161.8053278688, 100.75), 159.522388, -18.9171636306, 1.5180069434)
                CenterArc((0, 30.5), 21.5, 117.4871037543, 2.9725212214)
                CenterArc((-161.8053278688, 100.75), 160.272388, -18.6213740857, 1.4412538471)
            make_face()
            # Profile area: 4.476559741, perimeter: 8.8838273454
            with BuildLine():
                CenterArc((-161.8053278688, 100.75), 160.272388, -14.0533468264, 1.0728804879)
                CenterArc((0, 85.5), 24.5, -104.97292558, 3.079062897)
                Line((-5.0494345617, 61.5259888503), (-4.8053273037, 61.7460855583))
                CenterArc((-161.8053278688, 100.75), 161.772388, -13.9516882718, 0.9693992655)
                CenterArc((0, 85.5), 21.5, -105.1761443531, 3.9982144499)
            make_face()
            # Profile area: 0.6862932723, perimeter: 4.2277389295
            with BuildLine():
                CenterArc((-161.8053278688, 100.75), 161.772388, -14.3812135529, 0.3356080713)
                CenterArc((0, 85.5), 24.5, -101.8938626831, 0.4297592035)
                Line((-6.3815234177, 60.3249251276), (-5.0494345617, 61.5259888503))
                CenterArc((0, 30.5), 30.5, 99.6298893586, 2.4473589168)
            make_face()
            # Profile area: 1.6542654173, perimeter: 6.5026955342
            with BuildLine():
                CenterArc((-161.8053278688, 100.75), 162.5223880785, -13.5617903143, 0.5924557202)
                CenterArc((0, 85.5), 21.5, -101.1779299032, 2.0011782994)
                CenterArc((-161.8053278688, 100.75), 161.772388, -13.9516882718, 0.9693992655)
                Line((-4.8053273037, 61.7460855583), (-3.8144544885, 62.6394954737))
            make_face()
            # Profile area: 0.0243756417, perimeter: 0.7776195976
            with BuildLine():
                CenterArc((-161.8053278688, 100.75), 161.772388, -14.0456054816, 0.0939172098)
                Line((-5.0494345617, 61.5259888503), (-4.8053273037, 61.7460855583))
                CenterArc((0, 85.5), 24.5, -101.8938626831, 0.4297592035)
            make_face()
            # Profile area: 0.1803110577, perimeter: 2.0893221602
            with BuildLine():
                CenterArc((-161.8053278688, 100.75), 159.522388, -13.2296574802, 0.2642359721)
                Line((-6.516572589, 64.2425383401), (-5.8773154326, 64.8189177434))
                CenterArc((0, 85.5), 21.5, -107.1780655785, 1.3135519107)
            make_face()
            # Profile area: 13.028109411, perimeter: 20.0280189154
            with BuildLine():
                Line((-2.6781853485, 67.7033792947), (0, 70.1181365761))
                Line((0, 70.1181365761), (0, 76.5))
                Line((-1.1022970115, 76.5), (0, 76.5))
                CenterArc((-161.8053278688, 100.75), 162.5223880785, -11.7320960106, 3.1509360302)
            make_face()
            # Profile area: 0.6056384234, perimeter: 3.1902140123
            with BuildLine():
                CenterArc((-161.8053278688, 100.75), 162.5223880785, -14.2676930326, 0.2380743819)
                CenterArc((0, 85.5), 24.5, -101.4641034796, 1.7572098475)
                CenterArc((-161.8053278688, 100.75), 161.772388, -14.3812135529, 0.3356080713)
                CenterArc((0, 30.5), 30.5, 98.0971148938, 1.5327744648)
            make_face()
            # Profile area: 0.0527044238, perimeter: 1.2761168168
            with BuildLine():
                CenterArc((0, 30.5), 30.5, 102.0772482753, 0.6802849598)
                CenterArc((-161.8053278688, 100.75), 160.272388, -14.7547802445, 0.116657891)
                Line((-6.8179709302, 59.9314068787), (-6.3815234177, 60.3249251276))
            make_face()
            # Profile area: 12.0005194211, perimeter: 15.3508123451
            with BuildLine():
                CenterArc((-161.8053278688, 100.75), 162.5223880785, -12.9693345942, 1.2372385836)
                CenterArc((0, 85.5), 21.5, -99.1767516038, 3.3508793693)
                Line((-2.1823689143, 64.1110480406), (0, 66.0787577174))
                Line((0, 66.0787577174), (0, 70.1181365761))
                Line((-2.6781853485, 67.7033792947), (0, 70.1181365761))
            make_face()
            # Profile area: 7.0396923386, perimeter: 12.4929394505
            with BuildLine():
                CenterArc((0, 30.5), 30.5, 99.6298893586, 2.4473589168)
                Line((-6.8179709302, 59.9314068787), (-6.3815234177, 60.3249251276))
                CenterArc((-161.8053278688, 100.75), 160.272388, -16.1984183722, 1.4436381278)
                CenterArc((0, 85.5), 30.5, -105.0030155372, 2.8210000194)
                CenterArc((-161.8053278688, 100.75), 161.772388, -16.1742392502, 1.7930256974)
            make_face()
            # Profile area: 11.5228896545, perimeter: 43.6129442837
            with BuildLine():
                CenterArc((0, 85.5), 21.5, 88.408414377, 1.591585623)
                Line((0, 85.5), (0, 107))
                CenterArc((-161.8053278688, 100.75), 162.5223880785, -5.3841686134, 7.5851659808)
            make_face()
            # Profile area: 18.4505082214, perimeter: 81.3387037661
            with BuildLine():
                CenterArc((0, 85.5), 21.5, 90, 0.4095926764)
                CenterArc((-161.8053278688, 100.75), 161.772388, -12.0962341369, 14.3101859165)
                Line((-3.6247702284, 66.8499011242), (-2.6781853485, 67.7033792947))
                CenterArc((-161.8053278688, 100.75), 162.5223880785, -11.7320960106, 3.1509360302)
                CenterArc((-161.8053278688, 100.75), 162.5223880785, -8.5811599804, 1.0681555739)
                CenterArc((-161.8053278688, 100.75), 162.5223880785, -7.5130044065, 2.1288357931)
                Line((0, 85.5), (0, 107))
            make_face()
            # Profile area: 22.5856275131, perimeter: 22.9902611353
            with BuildLine():
                Line((0, 70.1181365761), (7.0780667065, 76.5))
                Line((0, 76.5), (7.0780667065, 76.5))
                Line((0, 70.1181365761), (0, 76.5))
            make_face()
            # Profile area: 0.0490721345, perimeter: 1.0872523154
            with BuildLine():
                Line((-5.8773154326, 64.8189177434), (-5.5435990853, 65.119809532))
                CenterArc((0, 85.5), 21.5, -105.8645136677, 0.6883693146)
                CenterArc((-161.8053278688, 100.75), 160.272388, -12.9804663385, 0.135706445)
            make_face()
            # Profile area: 2.1789166812, perimeter: 6.9652889503
            with BuildLine():
                Line((-5.5435990853, 65.119809532), (-3.6247702284, 66.8499011242))
                CenterArc((-161.8053278688, 100.75), 160.272388, -12.9804663385, 0.135706445)
                CenterArc((0, 85.5), 21.5, -105.1761443531, 3.9982144499)
                CenterArc((-161.8053278688, 100.75), 161.772388, -12.9822890063, 0.8860548694)
            make_face()
            # Profile area: 61.9002163279, perimeter: 86.6065354054
            with BuildLine():
                CenterArc((0, 85.5), 21.5, 90.4095926764, 3.9982144499)
                CenterArc((-161.8053278688, 100.75), 160.272388, -12.8447598935, 15.0568890053)
                Line((-5.5435990853, 65.119809532), (-3.6247702284, 66.8499011242))
                CenterArc((-161.8053278688, 100.75), 161.772388, -12.0962341369, 14.3101859165)
            make_face()
        # OneSide extrude, distance=0.83
        extrude(amount=0.83)
    return part.part


# Description: This is a cylindrical mesh or perforated sleeve with an oval or elliptical cross-section, featuring a solid outer band and an open mesh or latticed upper surface, commonly used as a filter, strainer, or ventilation component.
def model_143967_d7e408c9_0001():
    """Model: collar"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.8357293382, perimeter: 23.5619449019
            with BuildLine():
                CenterArc((12.5, -5), 2.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((12.5, -5), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


# Description: This is a cylindrical sleeve or bushing with a hollow core, featuring a rectangular slot or opening cut through the upper portion and a slightly flared or curved rim at the top.
def model_143967_d7e408c9_0004():
    """Model: eye end"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 21.2057504117, perimeter: 28.2743338823
            with BuildLine():
                CenterArc((0, -10), 3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, -10), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3.6
        extrude(amount=3.6)
    return part.part


# Description: This is a elongated cylindrical sleeve or tube with a longitudinal slot running along its length, featuring a curved/rounded bottom section and an open top channel design, likely used as a guide, conduit, or mounting bracket.
def model_144130_cd731033_0000():
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
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.8565449711, perimeter: 5.3366071595
            with BuildLine():
                _nurbs_edge([(5, -7.5), (5.0113402376, -7.5429084344), (5.0378059101, -7.6245241163), (5.0888588863, -7.7343453262), (5.1800219033, -7.8551433927), (5.334530288, -7.961129448), (5.5317340558, -8.0197279372), (5.7719267208, -8.0306130892), (6.0520547129, -7.9971740587), (6.3679768618, -7.9240071268), (6.7155343623, -7.8157281475), (7.0162423895, -7.7039524015), (7.2535976227, -7.6069969092), (7.4170042287, -7.5366219759), (7.5, -7.5)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                Line((7.5, -7.5), (5, -7.5))
            make_face()
            # Profile area: 1.25, perimeter: 5.7169892001
            with BuildLine():
                Line((5, -5.5), (5, -5))
                Line((5, -7.5), (5, -5.5))
                Line((6, -6.5), (5, -7.5))
                Line((6, -6.5), (5, -5))
            make_face()
            # Profile area: 4.375, perimeter: 13.8250475511
            with BuildLine():
                Line((5, -2.5), (5, -5))
                Line((6, -6.5), (5, -5))
                Line((6, -6.5), (5, -7.5))
                Line((7.5, -7.5), (5, -7.5))
                Line((6, -5), (7.5, -7.5))
                Line((5, -2.5), (6, -5))
            make_face()
        # OneSide extrude, distance=1.3
        extrude(amount=1.3)
    return part.part


# Description: This is a kayak or canoe hull with a streamlined, tapered design featuring a blue interior deck panel and black structural frame/gunwales, designed for water transportation.
def model_144304_edb09673_0002():
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
        # Sketch on XZ construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.112650758, perimeter: 27.7503707736
            with BuildLine():
                Line((-9.3055668157, -1.8113162137), (-5.024851198, 0.0569412479))
                Line((-5.024851198, 0.0569412479), (-5.5248393555, 1.2025580372))
                Line((-5.5248393555, 1.2025580372), (-12.3981670371, 2.5755744497))
                _nurbs_edge([(-12.3981670371, 2.5755744497), (-12.6462521617, 2.6251319513), (-13.0623749797, 2.6665502003), (-13.446632942, 2.5557430208), (-13.5453192083, 2.1098430679), (-13.2111086153, 1.2252599967), (-12.7210486951, 0.3576013343), (-12.2699154392, -0.3527418746), (-11.9354808768, -0.8497129445), (-11.7614720082, -1.1017942373)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.2, 0.4, 0.6, 0.8, 0.9959785896, 0.9959785896, 0.9959785896, 0.9959785896, 0.9959785896, 0.9959785896], 5)
                CenterArc((-10.1060926983, 0.0229190125), 2.0013147064, -66.4218215218, 280.6151591485)
            make_face()
            # Profile area: 4.0594320886, perimeter: 22.9239788978
            with BuildLine():
                CenterArc((-10.1060926983, 0.0229190125), 2.0013147064, -66.4218215218, 280.6151591485)
                _nurbs_edge([(-11.7614720082, -1.1017942373), (-11.7579014086, -1.106966855), (-11.7543272343, -1.1121420493), (-11.7507494854, -1.1173198202), (-11.747168162, -1.1225001675), (-11.7435832639, -1.1276830913)], [1, 1, 1, 1, 1, 1], [0.9959785896, 0.9959785896, 0.9959785896, 0.9959785896, 0.9959785896, 0.9959785896, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((-10.1060926983, 0.0229190125), 2.0013147064, -144.9057512744, 78.4839297526)
            make_face()
            with BuildLine():
                CenterArc((-10.1060926983, 0.0229190125), 1.647149902, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0000012201, perimeter: 0.0629364813
            with BuildLine():
                _nurbs_edge([(-11.7614720082, -1.1017942373), (-11.7579014086, -1.106966855), (-11.7543272343, -1.1121420493), (-11.7507494854, -1.1173198202), (-11.747168162, -1.1225001675), (-11.7435832639, -1.1276830913)], [1, 1, 1, 1, 1, 1], [0.9959785896, 0.9959785896, 0.9959785896, 0.9959785896, 0.9959785896, 0.9959785896, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((-10.1060926983, 0.0229190125), 2.0013147064, -145.8066623733, 0.9009110989)
            make_face()
            # Profile area: 8.5234638234, perimeter: 10.3493480627
            with Locations((-10.1060926983, 0.0229190125)):
                Circle(1.647149902)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a cylindrical mechanical component with a smooth, rounded body featuring vertical ribbed or fluted detailing along one side, and a slightly tapered or domed top end.
def model_144406_b7cbbc5a_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.1309733553, perimeter: 5.6548667765
            with BuildLine():
                CenterArc((0, 0), 0.65, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3.5
        extrude(amount=3.5)
    return part.part


# Description: This is a cylindrical capsule or rounded rectangular tube featuring two hemispherical ends connected by a straight cylindrical body, with a smooth, continuous surface and no visible holes or protrusions.
def model_144613_4ddef66b_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 8.0424771932, perimeter: 10.0530964915
            with Locations((-2.0682484335, 0.5134961628)):
                Circle(1.6)
        # OneSide extrude, distance=2.6
        extrude(amount=2.6)
    return part.part


# Description: This is a cylindrical capsule or rounded rectangular tube with hemispherical end caps, featuring a hollow interior core and a mesh/wireframe visualization showing its internal structure.
def model_144653_e3eccdf1_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # Symmetric extrude, each_side=2
        extrude(amount=2, both=True)
    return part.part


# Description: This is a 3D wedge or tapered plate with a parallelogram shape, featuring a diagonal internal division line and sharp edges that suggest a beveled or sloped geometric form.
def model_144781_a0ee9ef1_0001():
    """Model: screen v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 121.146548029, perimeter: 45.8610716
            with BuildLine():
                Line((-7.3377679, 4.1275), (7.3377679, 4.1275))
                Line((-7.3377679, -4.1275), (-7.3377679, 4.1275))
                Line((7.3377679, -4.1275), (-7.3377679, -4.1275))
                Line((7.3377679, 4.1275), (7.3377679, -4.1275))
            make_face()
        # OneSide extrude, distance=0.1524
        extrude(amount=0.1524)
    return part.part


# Description: This is an elongated cylindrical or capsule-shaped component with a ribbed or textured finish on both circular end caps and a smooth curved body featuring internal geometric divisions or reinforcing ribs running along its length.
def model_144781_a0ee9ef1_0004():
    """Model: Home Btn v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 24 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.8645865598, perimeter: 5.2674652292
            with BuildLine():
                CenterArc((0.0254, 0.5334), 0.4826, 0, 90)
                Line((0.0254, 1.016), (-0.0254, 1.016))
                CenterArc((-0.0254, 0.5334), 0.4826, 90, 90)
                Line((-0.508, 0.5334), (-0.508, -0.5334))
                CenterArc((-0.0254, -0.5334), 0.4826, 180, 90)
                Line((-0.0254, -1.016), (0.0254, -1.016))
                CenterArc((0.0254, -0.5334), 0.4826, -90, 90)
                Line((0.508, -0.5334), (0.508, 0.5334))
            make_face()
        # OneSide extrude, distance=0.1778
        extrude(amount=0.1778)
    return part.part


# Description: This is a cylindrical rod or shaft with rounded ends and a slightly elongated rectangular profile, featuring what appears to be shallow slots or grooves along its top surface.
def model_144963_acf119c2_0001():
    """Model: Piston Pin"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.5026548246, perimeter: 5.0265482457
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=6.8
        extrude(amount=6.8)
    return part.part


# Description: This is a parallelogram-shaped prism or wedge component with a slanted rectangular profile, featuring flat faces and sharp edges typical of a geometric structural part or bracket.
def model_145210_6e676ea8_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 403.2, perimeter: 81.6
            with BuildLine():
                Line((-24, 16.8), (0, 16.8))
                Line((-24, 0), (-24, 16.8))
                Line((0, 0), (-24, 0))
                Line((0, 16.8), (0, 0))
            make_face()
        # OneSide extrude, distance=5.4
        extrude(amount=5.4)
    return part.part


# Description: This is a curved, elongated duct or channel component with a streamlined aerodynamic shape, tapering toward one end and featuring a flange or mounting point at the opposite end.
def model_145461_30637b22_0000():
    """Model: File_MultiTool v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.0949198547, perimeter: 9.167382561
            with BuildLine():
                Line((0, 0), (0, 0.6))
                Line((0, 0), (3.2, 0))
                CenterArc((3.7223218971, -0.8803758827), 1.0236610079, 62.1837825021, 58.4966273641)
                CenterArc((2.4338247539, -2.4), 3, 53.9334117402, 36.0665882598)
                Line((0, 0.6), (2.4338247539, 0.6))
            make_face()
        # OneSide extrude, distance=0.16
        extrude(amount=0.16)
    return part.part


# Description: This is a cylindrical tube or rod with a slightly tapered, rounded end at the top and a flat or beveled end at the bottom, featuring a uniform hollow or solid cylindrical shaft.
def model_145461_30637b22_0013():
    """Model: Pin1_MultiTool v1 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            Circle(0.1)
        # OneSide extrude, distance=1.58
        extrude(amount=1.58)
    return part.part


# Description: This is a curved duct or air channel component with an elongated, tapered shape that features a longitudinal slot or opening along its upper surface and ribbed or textured detailing on the exterior.
def model_145461_30637b22_0014():
    """Model: SmallKnife_MultiTool v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.948538254, perimeter: 9.1401655914
            with BuildLine():
                CenterArc((2.5416876048, -2.4), 3, 56.4426902381, 33.5573097619)
                Line((0, 0.6), (2.5416876048, 0.6))
                Line((0, 0), (0, 0.6))
                Line((1.1, 0), (0, 0))
                Line((1.2, 0.1), (1.1, 0))
                Line((4.2, 0.1), (1.2, 0.1))
            make_face()
        # OneSide extrude, distance=0.16
        extrude(amount=0.16)
    return part.part


# Description: This is a parallelogram-shaped structural frame or bracket with a hollow, diamond-like geometric structure featuring internal ribbing, a central slot or opening, and triangulated support elements for lightweight rigidity.
def model_145487_b3a696c4_0000():
    """Model: CommonSide"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 29 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 49.0136397272, perimeter: 94.821405227
            with BuildLine():
                Line((-12.15, -9), (-21.85, -9))
                Line((-12.15, 1), (-12.15, -9))
                Line((-21.85, 1), (-12.15, 1))
                Line((-21.85, -9), (-21.85, 1))
            make_face()
            with BuildLine():
                Line((-16.0901305616, -3.5851053084), (-13.6525126266, -1.1474873734))
                Line((-13.6525126266, -1.1474873734), (-13, -1.8))
                Line((-13, -4), (-13, -1.8))
                Line((-13, -4), (-13, -6.2))
                Line((-13.6525126266, -6.8525126266), (-13, -6.2))
                Line((-16.0901305616, -4.4148946916), (-13.6525126266, -6.8525126266))
                CenterArc((-17, -4), 1, -65.4873151147, 40.9746302294)
                Line((-16.5851053084, -4.9098694384), (-14.1474873734, -7.3474873734))
                Line((-14.1474873734, -7.3474873734), (-14.8, -8))
                Line((-17, -8), (-14.8, -8))
                Line((-17, -8), (-19.2, -8))
                Line((-19.8525126266, -7.3474873734), (-19.2, -8))
                Line((-17.4148946916, -4.9098694384), (-19.8525126266, -7.3474873734))
                CenterArc((-17, -4), 1, -155.4873151147, 40.9746302294)
                Line((-17.9098694384, -4.4148946916), (-20.3474873734, -6.8525126266))
                Line((-20.3474873734, -6.8525126266), (-21, -6.2))
                Line((-21, -4), (-21, -6.2))
                Line((-21, -4), (-21, -1.8))
                Line((-20.3474873734, -1.1474873734), (-21, -1.8))
                Line((-17.9098694384, -3.5851053084), (-20.3474873734, -1.1474873734))
                CenterArc((-17, -4), 1, 114.5126848853, 40.9746302294)
                Line((-17.4148946916, -3.0901305616), (-19.8525126266, -0.6525126266))
                Line((-19.8525126266, -0.6525126266), (-19.2, 0))
                Line((-17, 0), (-19.2, 0))
                Line((-17, 0), (-14.8, 0))
                Line((-14.1474873734, -0.6525126266), (-14.8, 0))
                Line((-16.5851053084, -3.0901305616), (-14.1474873734, -0.6525126266))
                CenterArc((-17, -4), 1, 24.5126848853, 40.9746302294)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 2.3561944902, perimeter: 9.4247779608
            with BuildLine():
                CenterArc((-17, -4), 1, 24.5126848853, 40.9746302294)
                CenterArc((-17, -4), 1, 65.4873151147, 49.0253697706)
                CenterArc((-17, -4), 1, 114.5126848853, 40.9746302294)
                CenterArc((-17, -4), 1, 155.4873151147, 24.5126848853)
                CenterArc((-17, -4), 1, 180, 24.5126848853)
                CenterArc((-17, -4), 1, -155.4873151147, 40.9746302294)
                CenterArc((-17, -4), 1, -114.5126848853, 49.0253697706)
                CenterArc((-17, -4), 1, -65.4873151147, 40.9746302294)
                CenterArc((-17, -4), 1, -24.5126848853, 49.0253697706)
            make_face()
            with BuildLine():
                CenterArc((-17, -4), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.125
        extrude(amount=-0.125)
    return part.part


# Description: This is a wedge-shaped or trapezoidal prism component with an angled top surface, featuring a rectangular base with what appears to be a hollow or recessed interior cavity, designed as a structural or mounting bracket element.
def model_145500_552cada5_0005():
    """Model: Forside"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 12 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 22.1955525149, perimeter: 110.9777625746
            with BuildLine():
                Line((0, 0), (16, 0))
                Line((16, 0), (20.5, 0))
                Line((20.5, 0), (20.5, 11))
                Line((20.5, 11), (17.325340324, 11))
                CenterArc((17.325340324, 5.05), 5.95, 90, 25.1148348861)
                Line((0.5180095114, 3.7428169585), (14.7999587604, 10.437480669))
                CenterArc((0.9, 2.9279039161), 0.9, 115.1148348861, 64.8851651139)
                Line((0, 0), (0, 2.9279039161))
            make_face()
            with BuildLine():
                Line((0.4, 0.4), (16, 0.4))
                Line((0.4, 0.4), (0.4, 2.9279039161))
                CenterArc((0.9, 2.9279039161), 0.5, 115.1148348861, 64.8851651139)
                Line((0.6877830619, 3.3806333841), (14.9697323109, 10.0752970946))
                CenterArc((17.325340324, 5.05), 5.55, 90, 25.1148348861)
                Line((20.1, 10.6), (17.325340324, 10.6))
                Line((20.1, 0.4), (20.1, 10.6))
                Line((16, 0.4), (20.1, 0.4))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=14
        extrude(amount=14)
    return part.part


# Description: This is a cylindrical disk or pulley with a solid flat face and a ribbed or finned curved back surface, featuring a uniform circular geometry with radial ridges on one side.
def model_145532_70f82e64_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 20.2682991639, perimeter: 15.9592906802
            Circle(2.54)
        # OneSide extrude, distance=1.778
        extrude(amount=1.778)
    return part.part


# Description: This is a truncated polyhedron or chamfered cube with a predominantly dark navy blue finish, featuring multiple flat faceted surfaces and edges with subtle geometric segmentation lines, creating an angular, modernist geometric form.
def model_145532_a003c07c_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 27.77817025, perimeter: 21.082
            with BuildLine():
                Line((2.63525, -2.63525), (2.63525, 2.63525))
                Line((2.63525, 2.63525), (-2.63525, 2.63525))
                Line((-2.63525, 2.63525), (-2.63525, -2.63525))
                Line((-2.63525, -2.63525), (2.63525, -2.63525))
            make_face()
        # OneSide extrude, distance=5.2705
        extrude(amount=5.2705)
    return part.part


# Description: This is a parallelogram-shaped plate or panel with a trapezoidal profile, featuring a flat main face with recessed or beveled edges on the top and bottom, creating a hollow or box-like 3D geometry.
def model_145540_a4f54d5f_0010():
    """Model: Foot Break v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 51.6128, perimeter: 30.48
            with BuildLine():
                Line((0, 5.08), (0, 0))
                Line((0, 0), (10.16, 0))
                Line((10.16, 0), (10.16, 5.08))
                Line((10.16, 5.08), (0, 5.08))
            make_face()
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)
    return part.part


# Description: This is a horseshoe magnet with a U-shaped curved body, textured magnetic surfaces on both inner arms, and flat rectangular pole pieces at the open ends.
def model_145619_8e3238eb_0004():
    """Model: c-ring"""
    with BuildPart() as part:
        # Sketch1 -> 押し出し1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 14 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0314287592, perimeter: 1.8917119457
            with BuildLine():
                CenterArc((0, 0), 0.16, -71.4199210014, 322.8398420028)
                Line((-0.0509807621, -0.1516606801), (-0.0659807621, -0.1776414422))
                Line((-0.0659807621, -0.1776414422), (-0.04, -0.1926414422))
                Line((-0.04, -0.1926414422), (-0.0283685725, -0.1724952188))
                CenterArc((-0.0630095886, -0.1524952188), 0.04, -30, 97.5500468175)
                CenterArc((0, 0), 0.125, -67.5500468175, 315.100093635)
                CenterArc((0.0630095886, -0.1524952188), 0.04, 112.4499531825, 97.5500468175)
                Line((0.04, -0.1926414422), (0.0283685725, -0.1724952188))
                Line((0.0659807621, -0.1776414422), (0.04, -0.1926414422))
                Line((0.0509807621, -0.1516606801), (0.0659807621, -0.1776414422))
            make_face()
        # OneSide extrude, distance=-0.03
        extrude(amount=-0.03)
    return part.part


# Description: This is a multi-chambered industrial enclosure or manifold block with a rectangular overall shape, featuring multiple internal compartments separated by walls, internal structural ribbing for reinforcement, and open top sections with flanged edges for mounting or connection purposes.
def model_145643_0b6cfcf1_0000():
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
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.8842179217, perimeter: 28.3857544846
            with BuildLine():
                Line((0.5027083333, 0), (0.5027083333, -0.1190625))
                Line((0.5027083333, -0.1190625), (0.5027083333, -0.238125))
                Line((0.5027083333, -0.238125), (0.2645833333, -0.238125))
                Line((0.2645833333, -0.238125), (0.0264583333, -0.238125))
                Line((0.0264583333, -0.238125), (0.0264583333, -0.4365625))
                Line((0.0264583333, -0.4365625), (0.0264583333, -0.635))
                Line((0.0264583333, -0.635), (0.1058333333, -0.635))
                Line((0.1058333333, -0.635), (0.1852083333, -0.635))
                Line((0.1852083333, -0.635), (0.1852083333, -0.9525))
                Line((0.1852083333, -0.9525), (0.1852083333, -1.27))
                Line((0.1852083333, -1.27), (0.1058333333, -1.27))
                Line((0.1058333333, -1.27), (0.0264583333, -1.27))
                Line((0.0264583333, -1.27), (0.0264583333, -1.4684375))
                Line((0.0264583333, -1.4684375), (0.0264583333, -1.666875))
                Line((0.0264583333, -1.666875), (0.2645833333, -1.666875))
                Line((0.2645833333, -1.666875), (0.5027083333, -1.666875))
                Line((0.5027083333, -1.666875), (0.5027083333, -1.7594791667))
                Line((0.5027083333, -1.7594791667), (0.5027083333, -1.8520833333))
                Line((0.5027083333, -1.8520833333), (0.873125, -1.8520833333))
                Line((0.873125, -1.8520833333), (1.2435416667, -1.8520833333))
                Line((1.2435416667, -1.8520833333), (1.2435416667, -1.7012708333))
                Line((1.2435416667, -1.7012708333), (1.2435416667, -1.5531041667))
                Line((1.2435416667, -1.5531041667), (1.3096875, -1.6139583333))
                Line((1.3096875, -1.6139583333), (1.3758333333, -1.6748125))
                Line((1.3758333333, -1.6748125), (1.4419791667, -1.6139583333))
                Line((1.4419791667, -1.6139583333), (1.508125, -1.5531041667))
                Line((1.508125, -1.5531041667), (1.508125, -1.7012708333))
                Line((1.508125, -1.7012708333), (1.508125, -1.8520833333))
                Line((1.508125, -1.8520833333), (1.8785416667, -1.8520833333))
                Line((1.8785416667, -1.8520833333), (2.2489583333, -1.8520833333))
                Line((2.2489583333, -1.8520833333), (2.2489583333, -1.7594791667))
                Line((2.2489583333, -1.7594791667), (2.2489583333, -1.666875))
                Line((2.2489583333, -1.666875), (2.4870833333, -1.666875))
                Line((2.4870833333, -1.666875), (2.7252083333, -1.666875))
                Line((2.7252083333, -1.666875), (2.7252083333, -1.4710833333))
                _nurbs_edge([(2.7252083333, -1.4710833333), (2.7252083333, -1.2752916667), (2.7252083333, -1.2726458333), (2.6537708333, -1.2647083333)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                Line((2.6537708333, -1.2647083333), (2.5796875, -1.2567708333))
                Line((2.5796875, -1.2567708333), (2.57175, -0.9445625))
                Line((2.57175, -0.9445625), (2.5638125, -0.635))
                Line((2.5638125, -0.635), (2.6458333333, -0.635))
                Line((2.6458333333, -0.635), (2.7252083333, -0.635))
                Line((2.7252083333, -0.635), (2.7252083333, -0.4365625))
                Line((2.7252083333, -0.4365625), (2.7252083333, -0.238125))
                Line((2.7252083333, -0.238125), (2.4870833333, -0.238125))
                Line((2.4870833333, -0.238125), (2.2489583333, -0.238125))
                Line((2.2489583333, -0.238125), (2.2489583333, -0.1190625))
                Line((2.2489583333, -0.1190625), (2.2489583333, 0))
                Line((2.2489583333, 0), (2.00025, 0))
                Line((2.00025, 0), (1.7515416667, 0))
                Line((1.7515416667, 0), (1.5610416667, -0.2037291667))
                Line((1.5610416667, -0.2037291667), (1.3731875, -0.4101041667))
                Line((1.3731875, -0.4101041667), (1.1773958333, -0.2037291667))
                Line((1.1773958333, -0.2037291667), (0.98425, 0))
                Line((0.98425, 0), (0.7434791667, 0))
                Line((0.7434791667, 0), (0.5027083333, 0))
            make_face()
            with BuildLine():
                Line((0.9128125, -0.1058333333), (1.1456458333, -0.3360208333))
                Line((1.1456458333, -0.3360208333), (1.3784791667, -0.5688541667))
                Line((1.3784791667, -0.5688541667), (1.6007291667, -0.3360208333))
                Line((1.6007291667, -0.3360208333), (1.8229791667, -0.1058333333))
                Line((1.8229791667, -0.1058333333), (1.9711458333, -0.1058333333))
                _nurbs_edge([(1.9711458333, -0.1058333333), (2.1140208333, -0.1058333333), (2.1166666667, -0.1058333333), (2.1166666667, -0.1852083333)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(2.1166666667, -0.1852083333), (2.1166666667, -0.2566458333), (2.1087291667, -0.2645833333), (2.0372916667, -0.2645833333)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                Line((2.0372916667, -0.2645833333), (1.9579166667, -0.2645833333))
                Line((1.9579166667, -0.2645833333), (1.9579166667, -0.4550833333))
                Line((1.9579166667, -0.4550833333), (1.9579166667, -0.6455833333))
                Line((1.9579166667, -0.6455833333), (2.111375, -0.4947708333))
                Line((2.111375, -0.4947708333), (2.2648333333, -0.3439583333))
                Line((2.2648333333, -0.3439583333), (2.4421041667, -0.3439583333))
                Line((2.4421041667, -0.3439583333), (2.619375, -0.3439583333))
                Line((2.619375, -0.3439583333), (2.619375, -0.4233333333))
                _nurbs_edge([(2.619375, -0.4233333333), (2.619375, -0.4947708333), (2.6114375, -0.5027083333), (2.54, -0.5027083333)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                Line((2.54, -0.5027083333), (2.460625, -0.5027083333))
                Line((2.460625, -0.5027083333), (2.460625, -0.9392708333))
                Line((2.460625, -0.9392708333), (2.460625, -1.3758333333))
                Line((2.460625, -1.3758333333), (2.54, -1.3758333333))
                _nurbs_edge([(2.54, -1.3758333333), (2.6114375, -1.3758333333), (2.619375, -1.3837708333), (2.619375, -1.4552083333)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                Line((2.619375, -1.4552083333), (2.619375, -1.5345833333))
                Line((2.619375, -1.5345833333), (2.3415625, -1.5345833333))
                Line((2.3415625, -1.5345833333), (2.06375, -1.5345833333))
                Line((2.06375, -1.5345833333), (2.06375, -1.4552083333))
                _nurbs_edge([(2.06375, -1.4552083333), (2.06375, -1.381125), (2.0690416667, -1.3758333333), (2.1695833333, -1.3758333333)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                Line((2.1695833333, -1.3758333333), (2.2754166667, -1.3758333333))
                Line((2.2754166667, -1.3758333333), (2.2754166667, -0.9868958333))
                Line((2.2754166667, -0.9868958333), (2.2754166667, -0.6006041667))
                Line((2.2754166667, -0.6006041667), (2.2039791667, -0.6641041667))
                _nurbs_edge([(2.2039791667, -0.6641041667), (2.1616458333, -0.6985), (2.0902083333, -0.762), (2.0452291667, -0.8043333333)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                Line((2.0452291667, -0.8043333333), (1.9579166667, -0.8837083333))
                Line((1.9579166667, -0.8837083333), (1.9579166667, -1.2620625))
                Line((1.9579166667, -1.2620625), (1.9579166667, -1.6404166667))
                Line((1.9579166667, -1.6404166667), (2.0372916667, -1.6404166667))
                _nurbs_edge([(2.0372916667, -1.6404166667), (2.1087291667, -1.6404166667), (2.1166666667, -1.6483541667), (2.1166666667, -1.7197916667)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                Line((2.1166666667, -1.7197916667), (2.1166666667, -1.7991666667))
                Line((2.1166666667, -1.7991666667), (1.8653125, -1.7991666667))
                Line((1.8653125, -1.7991666667), (1.6139583333, -1.7991666667))
                Line((1.6139583333, -1.7991666667), (1.6139583333, -1.7197916667))
                _nurbs_edge([(1.6139583333, -1.7197916667), (1.6139583333, -1.6483541667), (1.6218958333, -1.6404166667), (1.6933333333, -1.6404166667)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                Line((1.6933333333, -1.6404166667), (1.7727083333, -1.6404166667))
                Line((1.7727083333, -1.6404166667), (1.7727083333, -1.3678958333))
                Line((1.7727083333, -1.3678958333), (1.7700625, -1.0980208333))
                Line((1.7700625, -1.0980208333), (1.571625, -1.3043958333))
                Line((1.571625, -1.3043958333), (1.3731875, -1.5107708333))
                Line((1.3731875, -1.5107708333), (1.1773958333, -1.3043958333))
                Line((1.1773958333, -1.3043958333), (0.9816041667, -1.0980208333))
                Line((0.9816041667, -1.0980208333), (0.9789583333, -1.3678958333))
                Line((0.9789583333, -1.3678958333), (0.9789583333, -1.6404166667))
                Line((0.9789583333, -1.6404166667), (1.0583333333, -1.6404166667))
                _nurbs_edge([(1.0583333333, -1.6404166667), (1.1297708333, -1.6404166667), (1.1377083333, -1.6483541667), (1.1377083333, -1.7197916667)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                Line((1.1377083333, -1.7197916667), (1.1377083333, -1.7991666667))
                Line((1.1377083333, -1.7991666667), (0.889, -1.7991666667))
                _nurbs_edge([(0.889, -1.7991666667), (0.7514166667, -1.7991666667), (0.6323541667, -1.7885833333), (0.6244166667, -1.778)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(0.6244166667, -1.778), (0.6164791667, -1.7647708333), (0.619125, -1.730375), (0.6270625, -1.698625)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(0.6270625, -1.698625), (0.6376458333, -1.6562916667), (0.6614583333, -1.6404166667), (0.7170208333, -1.6404166667)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                Line((0.7170208333, -1.6404166667), (0.79375, -1.6404166667))
                Line((0.79375, -1.6404166667), (0.79375, -1.2752916667))
                Line((0.79375, -1.2752916667), (0.7911041667, -0.9128125))
                Line((0.7911041667, -0.9128125), (0.6482291667, -0.7567083333))
                Line((0.6482291667, -0.7567083333), (0.5027083333, -0.60325))
                Line((0.5027083333, -0.60325), (0.5027083333, -0.9895416667))
                Line((0.5027083333, -0.9895416667), (0.5027083333, -1.3758333333))
                Line((0.5027083333, -1.3758333333), (0.5688541667, -1.3758333333))
                _nurbs_edge([(0.5688541667, -1.3758333333), (0.6244166667, -1.3758333333), (0.635, -1.3890625), (0.635, -1.4552083333)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                Line((0.635, -1.4552083333), (0.635, -1.5345833333))
                Line((0.635, -1.5345833333), (0.3836458333, -1.5345833333))
                Line((0.3836458333, -1.5345833333), (0.1322916667, -1.5345833333))
                Line((0.1322916667, -1.5345833333), (0.1322916667, -1.4552083333))
                _nurbs_edge([(0.1322916667, -1.4552083333), (0.1322916667, -1.3837708333), (0.1402291667, -1.3758333333), (0.2116666667, -1.3758333333)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                Line((0.2116666667, -1.3758333333), (0.2910416667, -1.3758333333))
                Line((0.2910416667, -1.3758333333), (0.2910416667, -0.9392708333))
                Line((0.2910416667, -0.9392708333), (0.2910416667, -0.5027083333))
                Line((0.2910416667, -0.5027083333), (0.2090208333, -0.5027083333))
                _nurbs_edge([(0.2090208333, -0.5027083333), (0.1375833333, -0.5027083333), (0.1296458333, -0.4947708333), (0.1375833333, -0.428625)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(0.1375833333, -0.428625), (0.1455208333, -0.3598333333), (0.1508125, -0.3571875), (0.3148541667, -0.34925)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                Line((0.3148541667, -0.34925), (0.4841875, -0.3413125))
                Line((0.4841875, -0.3413125), (0.6402916667, -0.4947708333))
                Line((0.6402916667, -0.4947708333), (0.79375, -0.6455833333))
                Line((0.79375, -0.6455833333), (0.79375, -0.4577291667))
                Line((0.79375, -0.4577291667), (0.79375, -0.2672291667))
                Line((0.79375, -0.2672291667), (0.7090833333, -0.2592916667))
                _nurbs_edge([(0.7090833333, -0.2592916667), (0.635, -0.254), (0.619125, -0.238125), (0.6138333333, -0.1772708333)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(0.6138333333, -0.1772708333), (0.6058958333, -0.1058333333), (0.6058958333, -0.1058333333), (0.7593541667, -0.1058333333)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                Line((0.7593541667, -0.1058333333), (0.9128125, -0.1058333333))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a flat rectangular plate with a central pyramidal or star-shaped void feature and multiple internal triangular reinforcing ribs or webbing that extend from a central hub to the outer edges.
def model_145864_5361be41_0000():
    """Model: Base Plate"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 145.0912614788, perimeter: 57.853981634
            with BuildLine():
                Line((7.5, -5), (-7.5, -5))
                Line((7.5, 5), (7.5, -5))
                Line((-7.5, 5), (7.5, 5))
                Line((-7.5, -5), (-7.5, 5))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a U-shaped or loop-shaped bracket with two parallel cylindrical rails connected by curved end caps, featuring a hollow rectangular passage running through its center length.
def model_145896_aefbc211_0002():
    """Model: Pin"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 15 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 8.2964600329, perimeter: 55.3097335529
            with BuildLine():
                CenterArc((0, 5.5), 1.05, 0, 180)
                Line((-1.05, 5.5), (-1.05, -5.5))
                CenterArc((0, -5.5), 1.05, 180, 180)
                Line((1.05, -5.5), (1.05, 5.5))
            make_face()
            with BuildLine():
                Line((0.75, -5.5), (0.75, 5.5))
                CenterArc((0, -5.5), 0.75, 180, 180)
                Line((-0.75, 5.5), (-0.75, -5.5))
                CenterArc((0, 5.5), 0.75, 0, 180)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


# Description: A horizontal bar or rod with three circular holes evenly spaced along its length, designed to connect chain links or serve as a mounting bracket with bolt holes at each end and center position.
def model_145983_487afb94_0003():
    """Model: Component2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 22 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.6649181731, perimeter: 8.5118352716
            with BuildLine():
                CenterArc((-4.5398, 0), 0.44, -30.754703633, 61.5094072661)
                Line((-4.1616796488, -0.225), (-0.3781203512, -0.225))
                CenterArc((0, 0), 0.44, 149.245296367, 61.5094072661)
                Line((-4.1616796488, 0.225), (-0.3781203512, 0.225))
            make_face()
            # Profile area: 0.4118627969, perimeter: 4.335397862
            with BuildLine():
                CenterArc((0, 0), 0.44, 149.245296367, 61.5094072661)
                CenterArc((0, 0), 0.44, -149.245296367, 118.4905927339)
                CenterArc((0, 0), 0.44, -30.754703633, 61.5094072661)
                CenterArc((0, 0), 0.44, 30.754703633, 118.4905927339)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.4118627969, perimeter: 4.335397862
            with BuildLine():
                CenterArc((4.5398, 0), 0.44, 149.245296367, 61.5094072661)
                CenterArc((4.5398, 0), 0.44, -149.245296367, 298.4905927339)
            make_face()
            with BuildLine():
                CenterArc((4.5398, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.6649181731, perimeter: 8.5118352716
            with BuildLine():
                CenterArc((0, 0), 0.44, -30.754703633, 61.5094072661)
                Line((0.3781203512, -0.225), (4.1616796488, -0.225))
                CenterArc((4.5398, 0), 0.44, 149.245296367, 61.5094072661)
                Line((0.3781203512, 0.225), (4.1616796488, 0.225))
            make_face()
            # Profile area: 0.4118627969, perimeter: 4.335397862
            with BuildLine():
                CenterArc((-4.5398, 0), 0.44, 30.754703633, 298.4905927339)
                CenterArc((-4.5398, 0), 0.44, -30.754703633, 61.5094072661)
            make_face()
            with BuildLine():
                CenterArc((-4.5398, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is a boat-shaped 3D part with a tapered, wedge-like profile featuring a pointed bow at one end, a wider stern section, and a concave underside with internal ribbing or structural reinforcement.
def model_145989_582f32c0_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2625, perimeter: 250
            with BuildLine():
                Line((0, 0), (32.5, 0))
                Line((55, 30), (32.5, 0))
                Line((-55, 30), (55, 30))
                Line((-32.5, 0), (-55, 30))
                Line((0, 0), (-32.5, 0))
            make_face()
        # OneSide extrude, distance=40
        extrude(amount=40)
    return part.part


# Description: This is a oval or elliptical ring/band with a smooth, curved outer surface and an open-top design featuring internal ribbed or segmented reinforcement structures visible through the transparent upper section.
def model_145991_2218b12c_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 314.159265359, perimeter: 62.8318530718
            Circle(10)
        # OneSide extrude, distance=4.5
        extrude(amount=4.5)
    return part.part


# Description: This is a cylindrical roller or spindle with a rounded hemispherical end cap and a flat circular end, featuring a textured or knurled surface along its length.
def model_146102_93e433ac_0002():
    """Model: bolt v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=3.4
        extrude(amount=3.4)
    return part.part


# Description: This is a folded metal bracket or duct component with an angular, bent sheet metal design featuring multiple planar surfaces, internal ribbing or bracing elements, and a complex geometric form that appears designed for structural support or fluid/air channeling.
def model_146170_5c8504dd_0000():
    """Model: Part"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 28.75, perimeter: 24.8994949366
            with BuildLine():
                Line((3, -4), (0, -4))
                Line((4.5, -2.5), (3, -4))
                Line((6, -4), (4.5, -2.5))
                Line((9, -1), (6, -4))
                Line((8, 0), (9, -1))
                Line((0, 0), (8, 0))
                Line((0, -4), (0, 0))
            make_face()
        # Symmetric extrude, full_length=True, total=1
        extrude(amount=0.5, both=True)
    return part.part


# Description: This is a flat, elongated parallelogram-shaped plate or tray with a slightly curved or beveled top surface and a dark edge flange on one side, designed as a shallow container or base component.
def model_146191_0fd44744_0001():
    """Model: fdsffdf v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.96, perimeter: 11.96
            with BuildLine():
                Line((1.48, -1), (-2.5, -1))
                Line((1.48, 1), (1.48, -1))
                Line((-2.5, 1), (1.48, 1))
                Line((-2.5, -1), (-2.5, 1))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: This is a U-shaped bracket or clamp with a curved base, two parallel vertical flanges, and a top opening designed to grip or secure cylindrical objects or components.
def model_146197_0222a249_0000():
    """Model: Part"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 15 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 73.5159399611, perimeter: 53.4683580751
            with BuildLine():
                CenterArc((0, 0), 4, 180, 180)
                Line((4, 10), (4, 0))
                Line((4, 10), (-4, 5.3811978465))
                Line((-4, 0), (-4, 5.3811978465))
            make_face()
            with BuildLine():
                Line((-1, 5), (-1, 0))
                CenterArc((0, 5), 1, 0, 180)
                Line((1, 0), (1, 5))
                CenterArc((0, 0), 1, -180, 180)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5)
    return part.part


# Description: This is a curved aerodynamic fairing or deflector with a streamlined, elongated parallelogram-like shape featuring a smooth curved leading edge on the left side and a flat trailing edge on the right, with a divided surface panel design in blue and dark gray tones.
def model_146291_6b0c8db3_0001():
    """Model: СТОЛ В КУПЕ v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.2913274508, perimeter: 4.6566371308
            with BuildLine():
                CenterArc((-0.5000000075, 0.400000006), 0.400000006, 90, 180)
                Line((-0.5000000075, 0), (0.8000000119, 0))
                Line((0.8000000119, 0.8000000119), (0.8000000119, 0))
                Line((-0.5000000075, 0.8000000119), (0.8000000119, 0.8000000119))
            make_face()
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)
    return part.part


# Description: This appears to be a collection of rounded rectangular pads or buttons distributed across a surface, featuring uniform rounded corners and a uniform depth, likely representing mounting points, connectors, or interface elements on a larger component.
def model_146321_0dbae658_0006():
    """Model: Поворотная платформа"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(11.2, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.5890486225, perimeter: 4.7123889804
            with BuildLine():
                CenterArc((3.5, 12), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((3.5, 12), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.5890486225, perimeter: 4.7123889804
            with BuildLine():
                CenterArc((3.5, 3), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((3.5, 3), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.5890486225, perimeter: 4.7123889804
            with BuildLine():
                CenterArc((12.5, 3), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((12.5, 3), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.5890480842, perimeter: 4.7123879037
            with BuildLine():
                CenterArc((12.5, 12), 0.4999998286, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((12.5, 12), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a streamlined aerodynamic fairing or duct component with an elongated wedge shape, featuring a tapered profile that transitions from a wider base to a pointed nose, with a curved upper surface and flat bottom designed for fluid flow direction.
def model_146373_341af1db_0000():
    """Model: broze surf fin"""
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
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 30.1275625982, perimeter: 32.3073405763
            with BuildLine():
                _nurbs_edge([(5.9481820055, -3.9615730928), (5.9889305735, -3.9726114964), (6.0695229863, -3.9936713272), (6.1876542022, -4.0222771687), (6.3419025899, -4.0509298382), (6.5326447043, -4.0627750261), (6.7197448986, -4.0445239917), (6.87155942, -4.0283481842), (6.9991757732, -3.9655708359), (7.1282534191, -3.7827320809), (7.2324211301, -3.5023206868), (7.2812984305, -3.165609108), (7.2672122009, -2.7822883515), (7.1889257966, -2.3561585754), (7.0535266483, -1.8794560205), (6.8709907434, -1.340480049), (6.6960010956, -0.8484675836), (6.5523686211, -0.4401411466), (6.4516217314, -0.1497434749), (6.4000000954, 0.0000000373)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9333333333, 1, 1, 1, 1, 1, 1], 5)
                Line((6.4000000954, 0.0000000373), (-7.0644705224, -0.0990035136))
                CenterArc((-7.0643234674, -0.119002973), 0.02, 90.4212852891, 163.211393505)
                Line((-7.0699593527, -0.1381924701), (5.9481820055, -3.9615730928))
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)
    return part.part


# Description: This is a hollow cylindrical sleeve or tube with a uniform circular cross-section, smooth curved outer surface, and open ends on both sides.
def model_146477_bee264e8_0000():
    """Model: pijp"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 9.6211275016, perimeter: 76.9690200129
            with BuildLine():
                CenterArc((0, 0), 6.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=16
        extrude(amount=16)
    return part.part


# Description: This is a flat parallelogram-shaped plate or panel with a uniform dark gray color and slight 3D beveled edges, featuring no holes, slots, or other cutouts.
def model_146498_a1bffd0b_0001():
    """Model: BASE"""
    with BuildPart() as part:
        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1584000.0000000002, perimeter: 5320
            with BuildLine():
                Line((0, 1760), (0, 0))
                Line((0, 0), (900, 0))
                Line((900, 0), (900, 1760))
                Line((900, 1760), (0, 1760))
            make_face()
        # OneSide extrude, distance=30
        extrude(amount=30)
    return part.part


# Description: This is a C-shaped or channel-shaped bracket with a rectangular slot cut through the center, featuring flat mounting flanges on the sides and a hollow interior cavity design typical of structural support or mounting components.
def model_146544_67c41937_0001():
    """Model: Matcher"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on BRepFace
        # Sketch has 15 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 117.9314165294, perimeter: 69.4247779608
            with BuildLine():
                Line((-7.5, -2.5), (-2.5, -2.5))
                Line((-7.5, -5), (-7.5, -2.5))
                Line((7.5, -5), (-7.5, -5))
                Line((7.5, 5), (7.5, -5))
                Line((-7.5, 5), (7.5, 5))
                Line((-7.5, 2.5), (-7.5, 5))
                Line((-2.5, 2.5), (-7.5, 2.5))
                Line((-2.5, -2.5), (-2.5, 2.5))
            make_face()
            with BuildLine():
                CenterArc((3.75, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3
        extrude(amount=3)
    return part.part


# Description: This is a parallelogram-shaped flat plate or panel with two diagonal cross-braces or reinforcing ribs running across its interior surface.
def model_146545_f266050f_0001():
    """Model: Platform"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 239.2146018366, perimeter: 67.1415926536
            with BuildLine():
                Line((10, -6), (10, 6))
                Line((10, 6), (-10, 6))
                Line((-10, 6), (-10, -6))
                Line((-10, -6), (10, -6))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=0.5
        extrude(amount=0.25, both=True)
    return part.part


# Description: This is a hexagonal prism or box-like solid with a pentagonal or trapezoidal top face, featuring internal triangulated geometry and no apparent holes or slots—essentially a geometric polyhedron with a roughly rectangular body and angled upper surfaces.
def model_146580_1c2df42f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 100, perimeter: 40
            with BuildLine():
                Line((7.5, -7.5), (-2.5, -7.5))
                Line((7.5, 2.5), (7.5, -7.5))
                Line((-2.5, 2.5), (7.5, 2.5))
                Line((-2.5, -7.5), (-2.5, 2.5))
            make_face()
        # OneSide extrude, distance=15
        extrude(amount=15)
    return part.part


# Description: This is a ring or washer-shaped component with a toroidal (donut-like) geometry, featuring a hollow central opening and a textured or knurled outer surface for grip or friction purposes.
def model_146617_2c247f85_0034():
    """Model: Подкладка"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.8246680716, perimeter: 6.5973445725
            with BuildLine():
                CenterArc((-9.5, -5.5), 0.65, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-9.5, -5.5), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a cylindrical sleeve or bushing with a rounded, capsule-like overall shape featuring a hollow interior bore and a mesh-textured surface that suggests it may have internal ribbing or structural reinforcement.
def model_146624_359752bb_0000():
    """Model: Tyre"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0144468798, perimeter: 0.4260807967
            Circle(0.067812865)
        # OneSide extrude, distance=0.0866
        extrude(amount=0.0866)
    return part.part


# Description: This is a curved rod or hook with a gentle S-shaped bend, featuring a slight curve at the bottom and a more pronounced hook or curl at the top end.
def model_146717_3e6a84c1_0010():
    """Model: 长灯笼 v0"""
    with BuildPart() as part:
        # Sketch1 -> 拉伸1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 20 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0677146009, perimeter: 13.5629199658
            with BuildLine():
                CenterArc((0.4, 1.7000000253), 1.1100000164, -90, 90)
                Line((1.5100000164, 1.7000000253), (1.5100000164, 5.0000000745))
                CenterArc((0.4, 5.0000000745), 1.1100000164, 0, 90)
                Line((0.4, 6.1000000909), (0.4, 6.1100000909))
                CenterArc((0.4, 5.0000000745), 1.1000000164, 0, 90)
                Line((1.5000000164, 1.7000000253), (1.5000000164, 5.0000000745))
                CenterArc((0.4, 1.7000000253), 1.1000000164, -90, 90)
                Line((0.4, 0.6000000089), (0.4, 0.5900000089))
            make_face()
        # Symmetric extrude, each_side=0.02
        extrude(amount=0.02, both=True)
    return part.part


# Description: This is a hexagonal prism or truncated wedge-shaped solid body with a flat top surface, angled side faces, and a rectangular base, featuring clean edges and a compact geometric form.
def model_146827_44b163c8_0003():
    """Model: MOTOR"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 31), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 116.25, perimeter: 46
            with BuildLine():
                Line((0, 1.5), (-15.5, 1.5))
                Line((0, 9), (0, 1.5))
                Line((-15.5, 9), (0, 9))
                Line((-15.5, 1.5), (-15.5, 9))
            make_face()
        # OneSide extrude, distance=-10.5
        extrude(amount=-10.5)
    return part.part


# Description: This is a hexagonal or cubic housing component with a recessed or open cavity on one face and a textured/mesh panel or vent section on the upper portion, designed for electronic enclosure or ventilation purposes.
def model_146849_d0676b7e_0005():
    """Model: часть 6 v8"""
    with BuildPart() as part:
        # Sketch3 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.0313274123, perimeter: 5.8566370614
            with BuildLine():
                Line((0.5, 5.6), (0.5, 3.9))
                CenterArc((0.1, 5.6), 0.4, 0, 90)
                Line((-0.1, 6), (0.1, 6))
                CenterArc((-0.1, 5.6), 0.4, 90, 90)
                Line((-0.5, 3.9), (-0.5, 5.6))
                Line((0.5, 3.9), (-0.5, 3.9))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


# Description: This is a tapered cylindrical rod or pin with a slightly conical shape, featuring a uniform diameter that gradually reduces toward one end, commonly used as a mechanical fastener, alignment pin, or dowel.
def model_146857_25b972d7_0002():
    """Model: Rear Axle v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=23.5
        extrude(amount=23.5)
    return part.part


# Description: This is a cylindrical roller or drum with a textured mesh or perforated surface pattern covering the curved body, featuring flat circular end caps on both sides.
def model_146857_25b972d7_0009():
    """Model: Rear Spacer v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 6.8722339297, perimeter: 10.9955742876
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


# Description: This is a tapered cylindrical rod or pin with a uniform diameter that gradually reduces to a sharp point at one end, featuring a simple conical tip design.
def model_146857_25b972d7_0010():
    """Model: Front  Axle v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=13
        extrude(amount=13)
    return part.part


# Description: This is a mobile device stand with an L-shaped profile featuring a tall angled back panel and a horizontal base arm with a notched support slot for holding phones or tablets at a tilted viewing angle.
def model_147021_113e7fda_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 10 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 54.7237023567, perimeter: 108.0673932923
            with BuildLine():
                Line((-5.7761176723, 0.11811834), (-11, 0.11811834))
                Line((-11, 0.11811834), (-11, -1.5520339828))
                CenterArc((-9.5, -1.5520339828), 1.5, -180, 90)
                Line((-9.5, -3.0520339828), (20, -3.0520339828))
                Line((20, -2), (20, -3.0520339828))
                Line((-9.029723065, -2), (20, -2))
                CenterArc((-9.029723065, -1.0170261563), 0.9829738437, 170.7809910869, 99.2190089131)
                Line((-5.5659416199, -0.8595452151), (-10, -0.8595452151))
                CenterArc((-7.8171846211, 9.6124291651), 10.7112250686, -77.8673304396, 90.0550580766)
                Line((1.6751604682, 11.6626186778), (2.6526216044, 11.8737341137))
                CenterArc((-7.8171846211, 9.6124291651), 9.7112250686, -77.8673304396, 90.0550580766)
            make_face()
        # OneSide extrude, distance=10
        extrude(amount=10)
    return part.part


# Description: This is a hollow cylindrical ring or bushing with a rounded, toroidal outer profile and a large central bore, featuring a smooth curved cross-section and what appears to be a slightly tapered or chamfered inner and outer geometry.
def model_147133_92c04b84_0001():
    """Model: Уплотнитель-кольцо"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.0681415022, perimeter: 10.6814150222
            with BuildLine():
                CenterArc((0, 0), 0.95, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=1.2
        extrude(amount=0.6, both=True)
    return part.part


# Description: This is a dark blue/navy molded plastic component with a curved, wing-like or fin shape featuring a central circular hole and radiating surface ribs or ridges that provide structural reinforcement across its curved body.
def model_147133_92c04b84_0003():
    """Model: Стекло"""
    with BuildPart() as part:
        # 08.05.13.01.22076.000 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints, 15 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 93.7400816748, perimeter: 57.0892379496
            with BuildLine():
                CenterArc((9.2929708956, 5.5), 5.5, -133.7486128832, 43.7486128832)
                Line((9.2929708956, 0), (12.7679708956, 0))
                Line((12.7679708956, 0), (12.7679708956, 1))
                Line((12.7679708956, 1), (12.2470263626, 3.954423259))
                Line((12.2470263626, 3.954423259), (12.7679708956, 6.0083005525))
                Line((12.7679708956, 7.0083005525), (12.7679708956, 6.0083005525))
                Line((9.9650871907, 7.5292450855), (12.7679708956, 7.0083005525))
                Line((7.0106639317, 7.0083005525), (9.9650871907, 7.5292450855))
                Line((4.0562406727, 7.5292450855), (7.0106639317, 7.0083005525))
                Line((1.1018174136, 7.0083005525), (4.0562406727, 7.5292450855))
                Line((-1.8526058454, 7.5292450855), (1.1018174136, 7.0083005525))
                Line((-4.8070291044, 7.0083005525), (-1.8526058454, 7.5292450855))
                Line((-6.8070291044, 7.0083005525), (-4.8070291044, 7.0083005525))
                Line((-6.8070291044, 7.0083005525), (-6.8070291044, 3.7))
                Line((-6.8070291044, 3.7), (-0.0070291044, 3.7))
                CenterArc((0, -4.3207282473), 8.0207313273, 46.8080657738, 43.2421463644)
            make_face()
            with BuildLine():
                CenterArc((7.7929708956, 3.6), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=1.2
        extrude(amount=0.6, both=True)
    return part.part


# Description: This is a cylindrical sleeve or tube with a curved top opening and vertical ribbed or fluted detailing along its exterior surface.
def model_147134_273aac81_0005():
    """Model: Уплотнитель_цилиндр"""
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
        # Symmetric extrude, full_length=True, total=1.8
        extrude(amount=0.9, both=True)
    return part.part


# Description: This is a curved cylindrical bowl or basket-like container with an oval/elliptical opening at the top, a smooth curved body, and an internal ribbed or latticed structure visible through the transparent top surface.
def model_147134_273aac81_0006():
    """Model: Таблетка"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            Circle(0.75)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)
    return part.part


# Description: This is a narrow, elongated rectangular compass card or pointer with a central circular hole and diagonal shading lines indicating directional orientation, tilted at an angle in 3D space.
def model_147134_273aac81_0007():
    """Model: Уплотнитель_пластина"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 10 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 64.4606195997, perimeter: 40.798229715
            with BuildLine():
                Line((2.5, -6.6), (2.5, 6.6))
                Line((2.5, 6.6), (-2.5, 6.6))
                Line((-2.5, 6.6), (-2.5, -6.6))
                Line((-2.5, -6.6), (2.5, -6.6))
            make_face()
            with BuildLine():
                CenterArc((0, 0.6), 0.7, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=0.1
        extrude(amount=0.05, both=True)
    return part.part


# Description: This is a flat parallelogram-shaped plate or panel with a 3D beveled or chamfered edge on the left side, featuring a trapezoidal profile when viewed from an angle.
def model_147140_f824fffe_0002():
    """Model: Крышка"""
    with BuildPart() as part:
        # 815E10N_del -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.6099993711, perimeter: 19.9000004679
            with BuildLine():
                Line((9.3879103661, 1.804999914), (2.037910372, 1.804999914))
                Line((2.037910372, 1.804999914), (2.037910372, 1.2050000019))
                Line((2.6499999687, 1.2050000019), (2.037910372, 1.2050000019))
                Line((9.3879103661, 1.2050000019), (2.6499999687, 1.2050000019))
                Line((10.6499999762, 1.2050000019), (9.3879103661, 1.2050000019))
                Line((11.3879106939, 1.2050000019), (10.6499999762, 1.2050000019))
                Line((11.3879106939, 1.804999914), (11.3879106939, 1.2050000019))
                Line((9.3879103661, 1.804999914), (11.3879106939, 1.804999914))
            make_face()
        # Symmetric extrude, full_length=True, total=5.4
        extrude(amount=2.7, both=True)
    return part.part


# Description: This is a set of five identical rectangular magazine bodies with a slightly tapered, parallelogram-like profile, featuring a curved feed lip at the top and a pronounced ribbed or fluted pattern along the sides for structural reinforcement and grip.
def model_147178_2016d56d_0001():
    """Model: 外部"""
    with BuildPart() as part:
        # Sketch1 -> 押し出し1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 22 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.295, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.00035, perimeter: 0.09
            with BuildLine():
                Line((-0.1125, 0.0729487835), (-0.1125, 0.0829487835))
                Line((-0.1125, 0.0829487835), (-0.1475, 0.0829487835))
                Line((-0.1475, 0.0829487835), (-0.1475, 0.0729487835))
                Line((-0.1475, 0.0729487835), (-0.1125, 0.0729487835))
            make_face()
            # Profile area: 0.00035, perimeter: 0.09
            with BuildLine():
                Line((-0.0475, 0.073), (-0.0475, 0.083))
                Line((-0.0475, 0.083), (-0.0825, 0.083))
                Line((-0.0825, 0.083), (-0.0825, 0.073))
                Line((-0.0825, 0.073), (-0.0475, 0.073))
            make_face()
            # Profile area: 0.000175, perimeter: 0.055
            with BuildLine():
                Line((0, 0.073), (0.0175, 0.073))
                Line((0.0175, 0.073), (0.0175, 0.083))
                Line((0.0175, 0.083), (0, 0.083))
                Line((0, 0.083), (0, 0.073))
            make_face()
            # Profile area: 0.000175, perimeter: 0.055
            with BuildLine():
                Line((0, 0.083), (0, 0.073))
                Line((0, 0.083), (-0.0175, 0.083))
                Line((-0.0175, 0.083), (-0.0175, 0.073))
                Line((-0.0175, 0.073), (0, 0.073))
            make_face()
            # Profile area: 0.00035, perimeter: 0.09
            with BuildLine():
                Line((0.0825, 0.083), (0.0825, 0.073))
                Line((0.0475, 0.083), (0.0825, 0.083))
                Line((0.0475, 0.073), (0.0475, 0.083))
                Line((0.0825, 0.073), (0.0475, 0.073))
            make_face()
            # Profile area: 0.00035, perimeter: 0.09
            with BuildLine():
                Line((0.1125, 0.0829487835), (0.1475, 0.0829487835))
                Line((0.1125, 0.0729487835), (0.1125, 0.0829487835))
                Line((0.1475, 0.0729487835), (0.1125, 0.0729487835))
                Line((0.1475, 0.0829487835), (0.1475, 0.0729487835))
            make_face()
        # OneSide extrude, distance=0.11
        extrude(amount=0.11)
    return part.part


# Description: This is a cylindrical bushing or spacer with a central axial hole, featuring a curved outer surface and mesh-textured details, designed for mechanical assembly or bearing applications.
def model_147292_7cfe4450_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.5079644737, perimeter: 7.5398223686
            with BuildLine():
                CenterArc((0, 0), 0.8, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.25
        extrude(amount=1.25)
    return part.part


# Description: This is a simple flat rectangular bar or plate with a horizontal linear profile and no visible holes, slots, or other features—essentially a basic structural or spacer component with a uniform rectangular cross-section.
def model_147546_ede0f31c_0002():
    """Model: Shaft"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            Circle(0.6)
        # OneSide extrude, distance=210
        extrude(amount=210)
    return part.part


# Description: This is a curved duct or flexible connector component with a ribbed/corrugated cylindrical body and two rectangular flanged end pieces designed for attachment or mounting.
def model_147759_44dc68e3_0001():
    """Model: KajakHandgreep v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 20 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.7531499493, perimeter: 7.9314994394
            with BuildLine():
                CenterArc((1.3000000045, -0.3357142737), 1.1548478927, 25.2719817487, 129.4560365025)
                CenterArc((0.1652518179, 0.2), 0.0999999985, -90, 64.7280182513)
                Line((0, 0.1000000015), (0.1652518179, 0.1000000015))
                Line((0, 0.1000000015), (-0.3, 0.1000000015))
                Line((-0.3, 0.1000000015), (-0.3, -0.1))
                Line((-0.3, -0.1), (0, -0.1))
                Line((0, -0.1), (0.1652518179, -0.1))
                CenterArc((0.1652518179, 0.2), 0.3, -90, 64.7280182513)
                CenterArc((1.3000000045, -0.3357142737), 0.9548478912, 25.2719817487, 129.4560365025)
                CenterArc((2.4347481911, 0.2), 0.3, -154.7280182513, 64.7280182513)
                Line((2.4347481911, -0.1), (2.6000000089, -0.1))
                Line((2.9000000089, -0.1), (2.6000000089, -0.1))
                Line((2.9000000089, 0.1000000015), (2.9000000089, -0.1))
                Line((2.6000000089, 0.1000000015), (2.9000000089, 0.1000000015))
                Line((2.4347481911, 0.1000000015), (2.6000000089, 0.1000000015))
                CenterArc((2.4347481911, 0.2), 0.0999999985, -154.7280182513, 64.7280182513)
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a conical or tapered washer/spacer with a flattened ring shape featuring radial ribbing or grooves across its surface for structural reinforcement and a central hole.
def model_148051_66cb4858_0004():
    """Model: Exit baffle"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.6505356632, perimeter: 13.9643793452
            with BuildLine():
                CenterArc((0, 0), 1.5875, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.635, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is an inhaler device with an L-shaped body featuring a cylindrical lower chamber, a rectangular upper dosage cartridge, and a curved mouthpiece section at the base, designed for handheld respiratory medication delivery.
def model_148051_66cb4858_0008():
    """Model: collector"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 25 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 1.5608605912, perimeter: 5.9182054185
            with BuildLine():
                CenterArc((0.21625, -0.4325), 0.15875, -90, 90)
                Line((0.375, -0.4325), (0.375, 0))
                Line((0.375, 0), (0, 0))
                Line((0, 0), (0, 0.15875))
                Line((0, 0.15875), (-1.245651363, 0.15875))
                CenterArc((-1.245651363, -0.14125), 0.3, 90, 65.5)
                Line((-1.5186397443, -0.0168420272), (-1.8093710477, -0.6547936482))
                CenterArc((-1.664914696, -0.7206262005), 0.15875, 155.5, 90)
                Line((-1.7307472482, -0.8650825523), (-1.5983544034, -0.9254174477))
                CenterArc((-1.5325218511, -0.780961096), 0.15875, -114.5, 90)
                Line((-1.3880654993, -0.8467936482), (-1.2716075494, -0.59125))
                Line((-1.2716075494, -0.59125), (0.21625, -0.59125))
            make_face()
        # Symmetric extrude, full_length=True, total=0.15875
        extrude(amount=0.079375, both=True)
    return part.part


# Description: This is a flat parallelogram-shaped plate or shim with a uniform thickness, featuring a simple rectangular geometry with angled sides and no holes or additional features.
def model_148051_66cb4858_0009():
    """Model: Main deck"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 44 constraints, 19 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 52.5061151359, perimeter: 32.0074778338
            with BuildLine():
                CenterArc((2.201875, 11.43), 0.079375, 0, 90)
                Line((-2.201875, 11.509375), (2.201875, 11.509375))
                CenterArc((-2.201875, 11.43), 0.079375, 90, 90)
                Line((-2.28125, 10.795), (-2.28125, 11.43))
                Line((-2.28125, 0.635), (-2.28125, 10.795))
                Line((-2.28125, 0.079375), (-2.28125, 0.635))
                CenterArc((-2.201875, 0.079375), 0.079375, 180, 90)
                Line((2.201875, 0), (-2.201875, 0))
                CenterArc((2.201875, 0.079375), 0.079375, -90, 90)
                Line((2.28125, 0.635), (2.28125, 0.079375))
                Line((2.28125, 10.795), (2.28125, 0.635))
                Line((2.28125, 11.43), (2.28125, 10.795))
            make_face()
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)
    return part.part


# Description: This is a multi-segment composite shaft or tool holder featuring a tapered cylindrical body with three stacked angular/faceted sections that progressively increase in diameter toward the top, terminating in a pointed or wedge-shaped head, designed for applications requiring modular assembly or angular load distribution.
def model_148051_66cb4858_0011():
    """Model: Gyro-Magnetic stabilizer"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 65 constraints, 29 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 4.1672538065, perimeter: 11.8040291742
            with BuildLine():
                Line((3.396914, 4.29097), (3.1241361016, 4.29097))
                CenterArc((3.1241361016, 4.608470019), 0.317500019, -148.15932424, 58.15932424)
                Line((2.854414, 4.440970019), (2.2044140247, 4.4409700037))
                CenterArc((1.9346919432, 4.60847), 0.3175, -90, 58.1593228931)
                Line((1.3589271098, 4.29097), (1.9346919432, 4.29097))
                CenterArc((1.815344161, 3.777440168), 0.6870439673, 131.6301790932, 51.4126672347)
                Line((1.9346919432, 3.74097), (1.1292688224, 3.74097))
                CenterArc((1.9346919432, 3.42347), 0.3175, 31.840677891, 58.159322109)
                Line((2.8544140224, 3.59097), (2.2044140224, 3.59097))
                CenterArc((3.1241361016, 3.42347), 0.3175, 90, 58.159322109)
                Line((3.396914, 3.74097), (3.1241361016, 3.74097))
                CenterArc((3.396914, 3.42347), 0.3175, 0, 90)
                Line((3.714414, 3.3225645412), (3.714414, 3.42347))
                Line((3.714414, 3.3225645412), (4.739414, 3.3225645412))
                CenterArc((5.0441571914, 3.23347), 0.3175, 90, 73.7032223629)
                Line((6.0025161792, 3.55097), (5.0441571914, 3.55097))
                CenterArc((5.3899997937, 3.4493573926), 0.6208876263, 9.4192258635, 11.3495836272)
                CenterArc((12.5156733497, 6.151708985), 7, -166.1915311388, 6.9603406295)
                Line((5.7179802672, 4.48097), (5.0441572075, 4.48097))
                CenterArc((5.0441572075, 4.7984700215), 0.3175000215, -163.703219457, 73.703219457)
                Line((4.385664, 4.7093754588), (4.739414, 4.7093754588))
                Line((4.068164, 4.7093754588), (4.385664, 4.7093754588))
                Line((4.068164, 4.7093754588), (3.714414, 4.7093754588))
                Line((3.714414, 4.7093754588), (3.714414, 4.60847))
                CenterArc((3.396914, 4.60847), 0.3175, -90, 90)
            make_face()
        # Symmetric extrude, full_length=True, total=0.15875
        extrude(amount=0.079375, both=True)
    return part.part


# Description: This is a antenna or communications spike featuring a tapered conical shaft that extends upward from a pyramidal base, with the base having a square or rectangular footprint and angled mounting surfaces.
def model_148051_66cb4858_0013():
    """Model: Fin"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 20 constraints, 15 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 79.8166956062, perimeter: 59.3071149731
            with BuildLine():
                Line((6.6133026557, 7.0815842153), (6.3680966625, 11.114577524))
                CenterArc((6.1304105772, 11.10012621), 0.238125, 3.4793003722, 102.7809043362)
                Line((6.0637355772, 11.32872621), (3.2052185695, 10.4949920828))
                CenterArc((3.5608185695, 9.2757920828), 1.27, 106.2602047083, 57.2354339099)
                Line((2.3431449664, 9.6365842615), (0, 1.72847))
                Line((0, 1.72847), (11, 1.72847))
                Line((11, 1.72847), (11, 2.6620425))
                Line((11, 2.6620425), (23.319, 2.6620425))
                CenterArc((22.7307622092, 2.5705369038), 0.5953125, 8.8419990459, 72.7580009541)
                Line((22.8177272622, 3.1594630895), (8.2365031688, 5.3126309329))
                CenterArc((8.5147913382, 7.1971947272), 1.905, -176.5206996278, 78.1206996278)
            make_face()
        # Symmetric extrude, full_length=True, total=0.15875
        extrude(amount=0.079375, both=True)
    return part.part


# Description: This is a cylindrical spacer or sleeve with a hollow center, featuring a mesh or perforated band around the upper portion and a solid ribbed lower section, designed for structural support or as a component in an assembly.
def model_148051_66cb4858_0014():
    """Model: Thin ring"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.1840004435, perimeter: 9.7017407691
            with BuildLine():
                CenterArc((0, 0), 0.89408, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.65, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.47625
        extrude(amount=0.47625)
    return part.part


# Description: This is a rectangular electronic enclosure or housing with a sloped top face, rounded bottom edges, and a protruding flange or connector block on the upper right side.
def model_148051_66cb4858_0016():
    """Model: Goniometer"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 23 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 2.3527219702, perimeter: 6.1455917506
            with BuildLine():
                Line((1.5875, 1.27), (0.15875, 1.27))
                CenterArc((0.15875, 1.11125), 0.15875, 90, 90)
                Line((0, 1.11125), (0, 0.15875))
                CenterArc((0.15875, 0.15875), 0.15875, 180, 90)
                Line((0.15875, 0), (1.74625, 0))
                CenterArc((1.74625, 0.15875), 0.15875, -90, 90)
                Line((1.905, 0.15875), (1.905, 1.11125))
                Line((1.5875, 1.11125), (1.905, 1.11125))
                Line((1.5875, 1.27), (1.5875, 1.11125))
            make_face()
        # Symmetric extrude, full_length=True, total=0.15875
        extrude(amount=0.079375, both=True)
    return part.part


# Description: This is a circular disc or wheel with a large flat face, a textured or knurled rim edge, and a central axial hole, featuring an overall thin, disc-like profile suitable for rotational applications.
def model_148051_66cb4858_0017():
    """Model: Satellite dish (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.8056947329, perimeter: 6.7328257557
            with BuildLine():
                CenterArc((0, 0), 0.9525, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1190625, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.15875
        extrude(amount=0.15875)
    return part.part


# Description: This is a retractable awning or shade canopy with a trapezoidal fabric panel stretched across a folding metal frame, featuring an angled support arm mechanism and a dark mounting bracket or hardware assembly on the right side.
def model_148051_66cb4858_0019():
    """Model: Partition 1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 18 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.6660072758, perimeter: 6.0437389169
            with BuildLine():
                Line((-0.5159375, -0.7540625), (-0.5159375, -0.8334375))
                Line((-0.5159375, -0.8334375), (0.5159375, -0.8334375))
                Line((0.5159375, -0.7540625), (0.5159375, -0.8334375))
                CenterArc((0.5953125, -0.7540625), 0.079375, 90, 90)
                Line((1.11125, -0.6746875), (0.5953125, -0.6746875))
                Line((1.11125, -0.6746875), (1.11125, 0))
                Line((1.11125, 0), (-1.11125, 0))
                Line((-1.11125, 0), (-1.11125, -0.6746875))
                Line((-1.11125, -0.6746875), (-0.5953125, -0.6746875))
                CenterArc((-0.5953125, -0.7540625), 0.079375, 0, 90)
            make_face()
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)
    return part.part


# Description: This is a dark gray cylindrical rod or shaft with rounded ends, appearing to be a smooth, uniform hollow or solid tube with no visible holes, slots, or flanges.
def model_148051_66cb4858_0021():
    """Model: BT-56 x 7 in"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5703499385, perimeter: 21.3854495115
            with BuildLine():
                CenterArc((0, 0), 1.72847, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.67513, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=17.78
        extrude(amount=17.78)
    return part.part


# Description: A long, slender pry bar or lever tool with a flat, angled head at one end and a flat chisel-like tip at the opposite end, featuring a slightly curved shaft for structural rigidity.
def model_148051_66cb4858_0023():
    """Model: Engine hook"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 23 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.5780329804, perimeter: 15.5642128107
            with BuildLine():
                Line((0.91, -0.47625), (0.635, -0.47625))
                Line((0.635, -0.47625), (0.635, -0.55125))
                Line((0.635, -0.55125), (0.91, -0.55125))
                CenterArc((0.91, -0.45125), 0.1, -90, 90)
                Line((1.01, -0.45125), (1.01, 6.5095068645))
                CenterArc((0.91, 6.5095068645), 0.1, 0, 90)
                Line((0.91, 6.6095068645), (0.635, 6.6095068645))
                Line((0.635, 6.6095068645), (0.635, 6.5345068645))
                Line((0.635, 6.5345068645), (0.91, 6.5345068645))
                CenterArc((0.91, 6.5095068645), 0.025, 0, 90)
                Line((0.935, 6.5095068645), (0.935, 0))
                Line((0.935, 0), (0.935, -0.45125))
                CenterArc((0.91, -0.45125), 0.025, -90, 90)
            make_face()
        # Symmetric extrude, full_length=True, total=0.5
        extrude(amount=0.25, both=True)
    return part.part


# Description: This is a cylindrical pipe nipple or connector with a smooth elongated body and threaded ends on both sides for screwing into fittings.
def model_148051_66cb4858_0024():
    """Model: Engine mount tube"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2017687882, perimeter: 11.5296450387
            with BuildLine():
                CenterArc((0, 0), 0.935, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.9, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=7.62
        extrude(amount=7.62)
    return part.part


# Description: This is a cylindrical tube or pipe with a slightly tapered or rounded end, featuring a smooth, hollow cylindrical body oriented at an angle.
def model_148051_66cb4858_0025():
    """Model: BT-56 x 6.25 in"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5703499385, perimeter: 21.3854495115
            with BuildLine():
                CenterArc((0, 0), 1.72847, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.67513, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=15.875
        extrude(amount=15.875)
    return part.part


# Description: This is a flat, annular (ring-shaped) washer or spacer with a circular hole in the center and a slightly tilted or beveled outer edge.
def model_148051_66cb4858_0026():
    """Model: Centering ring (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 5.9060164848, perimeter: 16.5400401116
            with BuildLine():
                CenterArc((0, 0), 1.6637, 0, 360)
            make_face()
            with BuildLine():
                Line((0.25, 0.9009578237), (0.25, 1.01))
                CenterArc((0, 0), 0.935, 105.5084018038, 328.9831963925)
                Line((-0.25, 1.01), (-0.25, 0.9009578237))
                Line((0.25, 1.01), (-0.25, 1.01))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.075
        extrude(amount=0.075)
    return part.part


# Description: This is a streamlined, elongated aerodynamic fairing or cowling with a pointed nose cone at the top, a tapered body with subtle curves and ridges running along its length, and a flared or flanged base, designed to reduce drag or channel airflow around another component.
def model_148051_66cb4858_0027():
    """Model: Component53"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 6 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 2.2807884599, perimeter: 8.5291129299
            with BuildLine():
                CenterArc((-0.272849221, -0.0343264123), 0.275, 7.1705527125, 37.8294472875)
                Line((-0.0783948562, 0.1601279525), (-0.9379020452, 1.0196351415))
                CenterArc((-1.218535049, 0.7390021377), 0.396875, 45, 69)
                Line((-1.3799586542, 1.1015654912), (-3.1911944108, 0.2951513766))
                CenterArc((-2.9452155838, -0.2573261145), 0.6047619048, 114, 40.8176920708)
                Line((-3.4925, 0), (0, 0))
            make_face()
            with BuildLine():
                CenterArc((-1.16, 0.635), 0.1190625, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=0.15875
        extrude(amount=0.079375, both=True)
    return part.part


# Description: This is a TIE Fighter wing panel (or similar spacecraft component) featuring a tapered, curved aerodynamic design with a pointed apex at the top, internal ribbed reinforcement structure, and a mounting hole for assembly.
def model_148051_66cb4858_0028():
    """Model: Component54"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 10 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 1.9465950785, perimeter: 7.4229388272
            with BuildLine():
                Line((-0.3832180919, 0.4501615893), (-0.5384990235, 0.4171556084))
                Line((-0.5384990235, 0.4171556084), (-0.3683118778, -0.3835119618))
                CenterArc((-0.0577500145, -0.3175), 0.3175, -168, 78)
                Line((-0.0577500145, -0.635), (1.1675432448, -0.635))
                CenterArc((0.9198440175, -0.739909927), 0.269, 22.954482516, 10.245517484)
                Line((1.1449336178, -0.5926154199), (-0.1167291732, 1.3354074162))
                CenterArc((-0.5158657507, 1.0742197586), 0.477, 33.2, 68.8)
                Line((-0.6150396272, 1.5407961642), (-0.3832180919, 0.4501615893))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1190625, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=0.15875
        extrude(amount=0.079375, both=True)
    return part.part


# Description: This is a ladder rung or step with a rectangular profile, featuring small notches or indentations along one edge for gripping or attachment purposes.
def model_148051_66cb4858_0032():
    """Model: Partition 2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 19 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4.0637519531, perimeter: 12.779375
            with BuildLine():
                Line((-0.8334375, 0), (0, 0))
                Line((0, 0), (0, 5.23875))
                Line((0, 5.23875), (-0.6746875, 5.23875))
                Line((-0.6746875, 5.23875), (-0.6746875, 4.60375))
                Line((-0.6746875, 4.60375), (-0.8334375, 4.60375))
                Line((-0.8334375, 4.60375), (-0.8334375, 3.889375))
                Line((-0.8334375, 3.889375), (-0.6746875, 3.889375))
                Line((-0.6746875, 3.889375), (-0.6746875, 3.254375))
                Line((-0.6746875, 3.254375), (-0.8334375, 3.254375))
                Line((-0.8334375, 3.254375), (-0.8334375, 1.905))
                Line((-0.8334375, 1.905), (-0.6746875, 1.905))
                Line((-0.6746875, 1.905), (-0.6746875, 1.27))
                Line((-0.6746875, 1.27), (-0.8334375, 1.27))
                Line((-0.8334375, 1.27), (-0.8334375, 0))
            make_face()
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)
    return part.part


# Description: This is a hollow cylindrical sleeve or bushing with a uniform bore throughout, featuring a slightly rounded or domed top end and an open bottom end, with mesh-like surface texturing visible in the rendering.
def model_148051_66cb4858_0033():
    """Model: Satellite body"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1781393481, perimeter: 4.4885505038
            with BuildLine():
                CenterArc((0, 0), 0.396875, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


# Description: This is a black plastic or composite mounting bracket with an elongated, angled design featuring a series of adjustment holes along the upper arm and two rectangular slots in the middle section for fastening or alignment purposes.
def model_148051_66cb4858_0035():
    """Model: Top fin"""
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
        # Sketch has 50 constraints, 33 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 51.0851658834, perimeter: 78.646002699
            with BuildLine():
                Line((5.08, 1.72847), (5.08, 1.77847))
                Line((5.08, 1.72847), (16.0019999879, 1.72847))
                Line((16.0019999879, 1.72847), (16.0019999865, 1.92847))
                Line((16.0019999865, 1.92847), (18.5419999865, 1.92847))
                Line((18.5419999865, 1.92847), (18.5419999765, 3.35153))
                Line((18.5419999765, 3.35153), (12.0419999765, 3.35153))
                _nurbs_edge([(12.0419999765, 3.35153), (11.8463275925, 3.3515299986), (11.4730032308, 3.3703148186), (10.9670759965, 3.4548426902), (10.3994989051, 3.6745594848), (9.8651154686, 4.0966547098), (9.50506228, 4.6274845502), (9.3220494415, 5.2270082353), (9.3207664733, 5.8592455477), (9.5055808719, 6.4960889607), (9.8835432579, 7.115918934), (10.3481243898, 7.5856492734), (10.7923615034, 7.9187648468), (11.1318810049, 8.1318172418), (11.3124816793, 8.2360870915)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                Line((12.8281585338, 9.1111635314), (11.3124816793, 8.2360870915))
                Line((12.4989957725, 9.8334452902), (12.8281585338, 9.1111635314))
                Line((12.4989957725, 9.8334452902), (0.409004489, 4.3237188331))
                Line((0.409004489, 4.3237188331), (0.2, 4.22847))
                _nurbs_edge([(-0.0047809951, 1.77847), (-0.0437685921, 1.8267110996), (-0.1189061832, 1.9246512132), (-0.2231003278, 2.0759347353), (-0.3436754479, 2.286168692), (-0.4561541358, 2.5613821972), (-0.5207211508, 2.8457200518), (-0.5286632108, 3.1337725042), (-0.4752628946, 3.4173819492), (-0.3652086713, 3.6843824196), (-0.2092161492, 3.9202593503), (-0.0572197065, 4.0725713155), (0.0676614523, 4.1611274992), (0.155177014, 4.2080429884), (0.2, 4.22847)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                Line((5.08, 1.77847), (-0.0047809951, 1.77847))
            make_face()
            with BuildLine():
                CenterArc((15.8419999822, 2.5400140851), 0.3175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((10.6419999822, 2.5399747982), 0.3175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((11.9419999822, 2.5399846199), 0.3175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((17.1419999822, 2.5400239069), 0.3175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((13.2419999822, 2.5399944417), 0.3175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((14.5419999822, 2.5400042634), 0.3175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((15.0556733898, 6.1517090203), 7, -174.7115821705, 15.4803920372)
                CenterArc((7.93, 3.4493574375), 0.6208874375, -90, 110.7688098666)
                Line((5.8140533441, 2.82847), (7.93, 2.82847))
                CenterArc((5.8140533441, 3.1125233441), 0.2840533441, 180, 90)
                Line((5.53, 3.35347), (5.53, 3.1125233441))
                Line((5.53, 3.35347), (3.8031477847, 3.35347))
                CenterArc((4.3484576779, 3.7714012544), 0.6870439673, 113.8790789939, 103.5878572763)
                Line((4.6662820998, 4.6634617522), (4.07033697, 4.399635514))
                CenterArc((4.7372585537, 4.503136258), 0.175333742, 90, 23.8790789939)
                Line((5.53, 4.67847), (4.7372585537, 4.67847))
                Line((5.53, 4.67847), (5.53, 4.9014943688))
                CenterArc((5.68875, 4.9014943688), 0.15875, 114.5, 65.5)
                Line((5.6229174477, 5.0459507205), (7.4465028384, 5.8770064623))
                CenterArc((7.634370439, 5.464768637), 0.4530278799, 5.2884178295, 109.2115821705)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=0.15875
        extrude(amount=0.079375, both=True)
    return part.part


# Description: This is a cylindrical sleeve or tube with a ribbed or corrugated surface texture running along its length, featuring a slightly tapered or threaded end at the top.
def model_148051_66cb4858_0036():
    """Model: Centuri ST20 x 18 in"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.8602068848, perimeter: 32.2537264648
            with BuildLine():
                CenterArc((0, 0), 2.59334, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.54, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=12.7
        extrude(amount=12.7)
    return part.part


# Description: This is a curved aerodynamic fairing or spoiler with a swept, blade-like shape featuring a hollow underside cavity and textured surface treatment, designed for airflow management or aesthetic purposes on a vehicle or aircraft.
def model_148051_66cb4858_0037():
    """Model: Deck brace"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 16 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.631825667, perimeter: 12.3731110383
            with BuildLine():
                CenterArc((0, 0), 1.72847, -84.2324135944, 174.2324129827)
                Line((2.30505, -1.7197200002), (0.1736999191, -1.7197200002))
                Line((2.30505, -1.7197200002), (2.3720857749, -1.7197200002))
                CenterArc((0, -0.81153), 2.54, -20.9501231696, 110.9501227533)
            make_face()
        # OneSide extrude, distance=0.15875
        extrude(amount=0.15875)
    return part.part


# Description: This is a triangular pyramidal antenna or fin-shaped component with a tall, pointed apex and a broad rectangular base, featuring a hollow or recessed interior cavity and a metallic reinforcement strip along one edge.
def model_148051_66cb4858_0039():
    """Model: Fin forward"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 15 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 5.8771517827, perimeter: 12.8795307486
            with BuildLine():
                Line((0, 1.72847), (5, 1.72847))
                CenterArc((4.5313460462, 1.6035257434), 0.485023294, 14.9279779754, 63.0720220246)
                Line((2.6101187985, 2.5077541968), (4.6321880593, 2.0779501147))
                CenterArc((2.6828878568, 2.8501058642), 0.35, -153, 51.0000056067)
                Line((1.7453083048, 3.9192680999), (2.3710355733, 2.6912091893))
                CenterArc((1.567107, 3.82847), 0.2, 27, 63)
                Line((0.708281845, 4.02847), (1.567107, 4.02847))
                CenterArc((0.708281845, 3.7343066274), 0.2941633726, 90, 78.5)
                Line((0, 1.72847), (0.420023889, 3.7929533714))
            make_face()
        # Symmetric extrude, full_length=True, total=0.15875
        extrude(amount=0.079375, both=True)
    return part.part


# Description: This is a rectangular protective case or enclosure with a dark navy blue finish, featuring a slightly curved top surface and rounded edges, designed for portable device storage or transportation.
def model_148051_66cb4858_0040():
    """Model: Ringnet support"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 12 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.9972458968, perimeter: 3.9912278338
            with BuildLine():
                CenterArc((1.11125, 0.15875), 0.15875, -90, 90)
                Line((1.27, 0.15875), (1.27, 0.635))
                CenterArc((1.11125, 0.635), 0.15875, 0, 90)
                Line((1.11125, 0.79375), (0, 0.79375))
                Line((0, 0.79375), (0, 0))
                Line((0, 0), (1.11125, 0))
            make_face()
        # Symmetric extrude, full_length=True, total=0.15875
        extrude(amount=0.079375, both=True)
    return part.part


# Description: This is a cylindrical rod or tube with rounded ends, featuring a smooth, tapered appearance and a slight diagonal orientation.
def model_148051_66cb4858_0042():
    """Model: BT-56 x 8 in"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5703499385, perimeter: 21.3854495115
            with BuildLine():
                CenterArc((0, 0), 1.72847, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.67513, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=20.32
        extrude(amount=20.32)
    return part.part


# Description: This is a cylindrical sleeve or barrel component with an open top, featuring vertical ribbed or fluted texturing on its exterior surface and a slightly tapered or curved profile.
def model_148051_66cb4858_0043():
    """Model: Baffle assembly v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7783026879, perimeter: 20.4278920707
            with BuildLine():
                CenterArc((0, 0), 1.6637, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.5875, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3.81
        extrude(amount=3.81)
    return part.part


# Description: This is a cylindrical roller or shaft with a knurled or textured surface around its middle section, featuring smooth rounded ends and a dark metallic finish.
def model_148051_66cb4858_0044():
    """Model: antenae"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.044534837, perimeter: 0.7480917506
            Circle(0.1190625)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


# Description: This is a claw hammer featuring a long handle with a head that has a striking face on one end and a curved claw for nail removal on the other end.
def model_148051_66cb4858_0045():
    """Model: Wing brace"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 38 constraints, 23 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 14.1714130734, perimeter: 30.6266091543
            with BuildLine():
                CenterArc((2.3591388279, -0.3500000005), 0.3757423721, -86.3977359034, 86.3977359034)
                Line((0, -0.3500000005), (2.7348812, -0.3500000005))
                Line((0, -0.3500000005), (0, 0))
                Line((0, 0), (-1.1924599014, -0.0000000027))
                CenterArc((-1.1924599, -0.6350000027), 0.635, 90.0000001301, 70.699097837)
                CenterArc((-2.9903908, -0.0053417789), 1.27, -90, 70.6990979671)
                Line((-3.1491157, -1.2753417789), (-2.9903908, -1.2753417789))
                CenterArc((-3.1491157, -1.5134667789), 0.238125, 90, 90)
                Line((-3.3872407, -1.5875000005), (-3.3872407, -1.5134667789))
                CenterArc((-3.1491157, -1.5875000005), 0.238125, 180, 90)
                Line((-1.3162129206, -1.8256250005), (-3.1491157, -1.8256250005))
                CenterArc((-1.3162129206, -2.4606250005), 0.635, -0.0000004796, 90.0000004796)
                Line((-0.6812129707, -8.4472473995), (-0.6812129206, -2.4606250058))
                CenterArc((-1.2368379707, -8.4472473949), 0.555625, -76.8634363953, 76.8634359157)
                CenterArc((-1.0384003992, -9.2975237005), 0.3175, 103.1365636047, 76.8634363953)
                Line((-1.3559003992, -9.2975237005), (-1.3559004, -9.5250000005))
                CenterArc((-1.1177754, -9.5250000005), 0.238125, 180, 90)
                Line((-0.0462129, -9.7631250005), (-1.1177754, -9.7631250005))
                CenterArc((-0.0462129, -9.4456250005), 0.3175, -90, 90)
                Line((0.2712871, -1.9038493311), (0.2712871, -9.4456250005))
                CenterArc((1.3851269077, -1.9038493311), 1.1138398077, 93.6022640966, 86.3977359034)
                Line((2.3827467052, -0.7249999982), (1.3151444, -0.7922101964))
            make_face()
        # Symmetric extrude, full_length=True, total=0.15875
        extrude(amount=0.079375, both=True)
    return part.part


# Description: This is a cylindrical tube or pipe with rounded ends, tilted at an angle, featuring a uniform hollow circular cross-section.
def model_148051_a453e5db_0000():
    """Model: BT-5 x 2.5 in"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1272345025, perimeter: 8.4823001647
            with BuildLine():
                CenterArc((0, 0), 0.69, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.66, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=6.35
        extrude(amount=6.35)
    return part.part


# Description: A cylindrical sleeve or tube with a slightly tapered top edge and vertical ribbing or fluting along its exterior surface.
def model_148051_a453e5db_0002():
    """Model: Launch Lug 1/8"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0294524311, perimeter: 2.3561944902
            with BuildLine():
                CenterArc((0, 0.88707), 0.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0.88707), 0.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


# Description: This is a cylindrical tube or sleeve with a smooth exterior wall and a textured or ribbed top rim, designed as a hollow cylindrical component with open ends.
def model_148051_ad8f6d60_0002():
    """Model: Launch Lug 1/8"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0294524311, perimeter: 2.3561944902
            with BuildLine():
                CenterArc((0, 1.13472), 0.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 1.13472), 0.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.9525
        extrude(amount=0.9525)
    return part.part


# Description: This is an elongated cylindrical rod or shaft with a slight bend at the top end, featuring a hook-like or curved terminal that appears designed for hanging or securing purposes.
def model_148051_ad8f6d60_0004():
    """Model: Engine hook"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 20 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.2478539816, perimeter: 10.0141592654
            with BuildLine():
                CenterArc((4.1575, 0.665), 0.075, 0, 90)
                Line((-0.2925, 0.74), (4.1575, 0.74))
                CenterArc((-0.2925, 0.665), 0.075, 90, 90)
                Line((-0.3675, 0.49), (-0.3675, 0.665))
                Line((-0.3175, 0.49), (-0.3675, 0.49))
                Line((-0.3175, 0.665), (-0.3175, 0.49))
                CenterArc((-0.2925, 0.665), 0.025, 90, 90)
                Line((4.1575, 0.69), (-0.2925, 0.69))
                CenterArc((4.1575, 0.665), 0.025, 0, 90)
                Line((4.1825, 0.49), (4.1825, 0.665))
                Line((4.2325, 0.49), (4.1825, 0.49))
                Line((4.2325, 0.665), (4.2325, 0.49))
            make_face()
        # Symmetric extrude, full_length=True, total=0.3175
        extrude(amount=0.15875, both=True)
    return part.part


# Description: This is a cylindrical tube or pipe with a uniform circular cross-section, featuring rounded ends and a slight taper or bevel at the top, commonly used as a structural component, connector, or spacer.
def model_148051_ad8f6d60_0005():
    """Model: BT-5 x 3in"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1272345025, perimeter: 8.4823001647
            with BuildLine():
                CenterArc((0, 0), 0.69, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.66, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=7.62
        extrude(amount=7.62)
    return part.part


# Description: This is a reinforced rubber or elastomer ring/sleeve with an elongated oval shape, featuring a mesh or fabric reinforcement layer on its outer surface and a hollow center opening, designed for applications requiring flexibility and structural support such as vibration damping or mechanical sealing.
def model_148051_ad8f6d60_0006():
    """Model: Centering ring slot"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 14 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0458001488, perimeter: 0.9061341956
            with BuildLine():
                Line((0.15875, -0.74), (0.15875, -0.8747110594))
                Line((-0.1433733503, -0.74), (0.15875, -0.74))
                Line((-0.15875, -0.74), (-0.1433733503, -0.74))
                Line((-0.15875, -0.8747110594), (-0.15875, -0.74))
                CenterArc((0, 0), 0.889, -100.2865606115, 20.5731212229)
            make_face()
            # Profile area: 0.9235308642, perimeter: 9.6880102539
            with BuildLine():
                CenterArc((0, 0), 0.889, -79.7134393885, 339.4268787771)
                Line((-0.15875, -0.8747110594), (-0.15875, -0.74))
                Line((-0.15875, -0.74), (-0.15875, -0.6714897151))
                CenterArc((0, 0), 0.69, -76.6986619719, 333.3973239437)
                Line((0.15875, -0.6714897151), (0.15875, -0.74))
                Line((0.15875, -0.74), (0.15875, -0.8747110594))
            make_face()
        # OneSide extrude, distance=0.15875
        extrude(amount=0.15875)
    return part.part


MODELS = {
    "model_139925_2aab35d1_0000": {"func": model_139925_2aab35d1_0000, "volume": 249.6876795117, "area": 700.7038447617},
    "model_139978_a15b18af_0000": {"func": model_139978_a15b18af_0000, "volume": 19.6014981278, "area": 65.0294544194},
    "model_140192_eaef8e46_0003": {"func": model_140192_eaef8e46_0003, "volume": 9.15584, "area": 96.9904},
    "model_140192_eaef8e46_0004": {"func": model_140192_eaef8e46_0004, "volume": 1.5037475276, "area": 36.4156198562},
    "model_140194_b0abb2bf_0002": {"func": model_140194_b0abb2bf_0002, "volume": 2458.0594707928, "area": 3379.0253416763},
    "model_140194_b0abb2bf_0010": {"func": model_140194_b0abb2bf_0010, "volume": 2156.947299, "area": 1756.4481},
    "model_140194_b0abb2bf_0012": {"func": model_140194_b0abb2bf_0012, "volume": 1437.964866, "area": 1916.1252},
    "model_140194_b0abb2bf_0016": {"func": model_140194_b0abb2bf_0016, "volume": 3982.056552, "area": 4674.1842},
    "model_140265_1d92f548_0000": {"func": model_140265_1d92f548_0000, "volume": 25.1151769984, "area": 179.9654866776},
    "model_140391_46e0f895_0000": {"func": model_140391_46e0f895_0000, "volume": 38859.1223370094, "area": 25384.288587351},
    "model_140400_0aab1cd3_0006": {"func": model_140400_0aab1cd3_0006, "volume": 1.9634954085, "area": 9.4247779608},
    "model_140558_461ff76a_0000": {"func": model_140558_461ff76a_0000, "volume": 1.6754179999, "area": 12.9721878379},
    "model_140636_00af4387_0000": {"func": model_140636_00af4387_0000, "volume": 47.6235524977, "area": 193.4721758635},
    "model_140763_e14274f8_0004": {"func": model_140763_e14274f8_0004, "volume": 54905.9, "area": 45852.7666811942},
    "model_140984_0596e640_0005": {"func": model_140984_0596e640_0005, "volume": 1490.285462199, "area": 1091.9100312222},
    "model_141032_6b0fa18c_0000": {"func": model_141032_6b0fa18c_0000, "volume": 37768.15, "area": 7435.9},
    "model_141118_cb31cb8f_0000": {"func": model_141118_cb31cb8f_0000, "volume": 0.1484402529, "area": 2.1205750412},
    "model_141118_cb31cb8f_0001": {"func": model_141118_cb31cb8f_0001, "volume": 0.1389212271, "area": 2.2311591026},
    "model_141119_b9c79872_0000": {"func": model_141119_b9c79872_0000, "volume": 118.5435388515, "area": 245.0189252819},
    "model_141270_b5c7f8b7_0000": {"func": model_141270_b5c7f8b7_0000, "volume": 377.7506415202, "area": 1309.7445819006},
    "model_141323_f85efdd4_0000": {"func": model_141323_f85efdd4_0000, "volume": 1.5, "area": 21.2},
    "model_141638_a21f336f_0006": {"func": model_141638_a21f336f_0006, "volume": 0.38, "area": 8.38},
    "model_141638_a21f336f_0016": {"func": model_141638_a21f336f_0016, "volume": 13.1096678774, "area": 99.6536368325},
    "model_141760_ccfda5bc_0000": {"func": model_141760_ccfda5bc_0000, "volume": 6.1371019986, "area": 49.2254961926},
    "model_141848_34f575d3_0004": {"func": model_141848_34f575d3_0004, "volume": 0.228, "area": 3.28},
    "model_142315_5c796497_0000": {"func": model_142315_5c796497_0000, "volume": 47.8523735854, "area": 162.8416098},
    "model_142385_63969402_0000": {"func": model_142385_63969402_0000, "volume": 0.0000903807, "area": 0.0242796074},
    "model_142408_d8a5427b_0000": {"func": model_142408_d8a5427b_0000, "volume": 106.0517802008, "area": 335.8912918049},
    "model_142411_e422dd79_0000": {"func": model_142411_e422dd79_0000, "volume": 25.7458319313, "area": 183.4550974985},
    "model_142460_c5e6d8b8_0000": {"func": model_142460_c5e6d8b8_0000, "volume": 111.8121953712, "area": 223.2175575087},
    "model_142461_5238e16d_0000": {"func": model_142461_5238e16d_0000, "volume": 36.6071974508, "area": 387.5709489259},
    "model_142581_460e171c_0001": {"func": model_142581_460e171c_0001, "volume": 0.687223393, "area": 5.8904862255},
    "model_142680_cd829f9e_0000": {"func": model_142680_cd829f9e_0000, "volume": 307.2533750956, "area": 473.8712856786},
    "model_142680_cd829f9e_0002": {"func": model_142680_cd829f9e_0002, "volume": 321.40625, "area": 470.2270382004},
    "model_142680_cd829f9e_0003": {"func": model_142680_cd829f9e_0003, "volume": 413.1, "area": 593.1},
    "model_142680_cd829f9e_0004": {"func": model_142680_cd829f9e_0004, "volume": 361.08, "area": 526.12},
    "model_142680_cd829f9e_0005": {"func": model_142680_cd829f9e_0005, "volume": 273.0625, "area": 416.2420382004},
    "model_142680_cd829f9e_0006": {"func": model_142680_cd829f9e_0006, "volume": 446.25, "area": 638.9},
    "model_142680_cd829f9e_0007": {"func": model_142680_cd829f9e_0007, "volume": 1, "area": 6},
    "model_142852_00b5fde9_0001": {"func": model_142852_00b5fde9_0001, "volume": 40.96766, "area": 98.3869},
    "model_142961_244ceb90_0002": {"func": model_142961_244ceb90_0002, "volume": 100000, "area": 24000},
    "model_142999_171240b6_0007": {"func": model_142999_171240b6_0007, "volume": 1.3618804153, "area": 7.7440258911},
    "model_142999_171240b6_0009": {"func": model_142999_171240b6_0009, "volume": 0.0402905511, "area": 0.7816392478},
    "model_143017_21d96cc2_0005": {"func": model_143017_21d96cc2_0005, "volume": 2007.41534, "area": 993.5464},
    "model_143019_54c55d14_0006": {"func": model_143019_54c55d14_0006, "volume": 0.1044717736, "area": 2.1265711816},
    "model_143293_fc5b0ff7_0015": {"func": model_143293_fc5b0ff7_0015, "volume": 0.5173388888, "area": 5.5380850402},
    "model_143293_fc5b0ff7_0019": {"func": model_143293_fc5b0ff7_0019, "volume": 0.2638937829, "area": 6.157521601},
    "model_143293_fc5b0ff7_0022": {"func": model_143293_fc5b0ff7_0022, "volume": 0.073120569, "area": 2.5069909376},
    "model_143293_fc5b0ff7_0026": {"func": model_143293_fc5b0ff7_0026, "volume": 0.2525655181, "area": 3.3545059626},
    "model_143346_3c91017f_0000": {"func": model_143346_3c91017f_0000, "volume": 18.5, "area": 61.6055512755},
    "model_143754_92a6452a_0002": {"func": model_143754_92a6452a_0002, "volume": 327.66, "area": 313.732},
    "model_143754_92a6452a_0003": {"func": model_143754_92a6452a_0003, "volume": 70.1643260588, "area": 1415.3335004451},
    "model_143754_92a6452a_0004": {"func": model_143754_92a6452a_0004, "volume": 188.195188125, "area": 433.2652625},
    "model_143754_92a6452a_0006": {"func": model_143754_92a6452a_0006, "volume": 148.4757, "area": 3001.9425},
    "model_143812_9f085870_0000": {"func": model_143812_9f085870_0000, "volume": 957.7563173433, "area": 2627.863003241},
    "model_143967_d7e408c9_0001": {"func": model_143967_d7e408c9_0001, "volume": 13.2535940073, "area": 53.0143760293},
    "model_143967_d7e408c9_0004": {"func": model_143967_d7e408c9_0004, "volume": 76.3407014822, "area": 144.1991027998},
    "model_144130_cd731033_0000": {"func": model_144130_cd731033_0000, "volume": 8.4260090018, "area": 30.441153674},
    "model_144304_edb09673_0002": {"func": model_144304_edb09673_0002, "volume": 11.8477741943, "area": 57.7518367811},
    "model_144406_b7cbbc5a_0000": {"func": model_144406_b7cbbc5a_0000, "volume": 3.9584067435, "area": 22.0539804282},
    "model_144613_4ddef66b_0000": {"func": model_144613_4ddef66b_0000, "volume": 20.9104407023, "area": 42.2230052642},
    "model_144653_e3eccdf1_0000": {"func": model_144653_e3eccdf1_0000, "volume": 12.5663706144, "area": 31.4159265359},
    "model_144781_a0ee9ef1_0001": {"func": model_144781_a0ee9ef1_0001, "volume": 18.4627339196, "area": 249.2823233698},
    "model_144781_a0ee9ef1_0004": {"func": model_144781_a0ee9ef1_0004, "volume": 0.3315234903, "area": 4.6657284374},
    "model_144963_acf119c2_0001": {"func": model_144963_acf119c2_0001, "volume": 3.4180528071, "area": 35.1858377202},
    "model_145210_6e676ea8_0000": {"func": model_145210_6e676ea8_0000, "volume": 2177.28, "area": 1247.04},
    "model_145461_30637b22_0000": {"func": model_145461_30637b22_0000, "volume": 0.3351871768, "area": 5.6566209192},
    "model_145461_30637b22_0013": {"func": model_145461_30637b22_0013, "volume": 0.0496371639, "area": 1.0555751316},
    "model_145461_30637b22_0014": {"func": model_145461_30637b22_0014, "volume": 0.3117661206, "area": 5.3595030026},
    "model_145487_b3a696c4_0000": {"func": model_145487_b3a696c4_0000, "volume": 6.4212292772, "area": 115.0552991259},
    "model_145500_552cada5_0005": {"func": model_145500_552cada5_0005, "volume": 310.7377352088, "area": 1598.0797810741},
    "model_145532_70f82e64_0000": {"func": model_145532_70f82e64_0000, "volume": 36.0370359134, "area": 68.9122171573},
    "model_145532_a003c07c_0000": {"func": model_145532_a003c07c_0000, "volume": 146.4048463026, "area": 166.6690215},
    "model_145540_a4f54d5f_0010": {"func": model_145540_a4f54d5f_0010, "volume": 65.548256, "area": 141.9352},
    "model_145619_8e3238eb_0004": {"func": model_145619_8e3238eb_0004, "volume": 0.0009428628, "area": 0.1196088768},
    "model_145643_0b6cfcf1_0000": {"func": model_145643_0b6cfcf1_0000, "volume": 1.8842179217, "area": 32.1541903065},
    "model_145864_5361be41_0000": {"func": model_145864_5361be41_0000, "volume": 145.0912614788, "area": 348.0365045915},
    "model_145896_aefbc211_0002": {"func": model_145896_aefbc211_0002, "volume": 12.4446900494, "area": 99.5575203953},
    "model_145983_487afb94_0003": {"func": model_145983_487afb94_0003, "volume": 0.9130849474, "area": 14.3810489586},
    "model_145989_582f32c0_0000": {"func": model_145989_582f32c0_0000, "volume": 105000, "area": 15250},
    "model_145991_2218b12c_0000": {"func": model_145991_2218b12c_0000, "volume": 1413.7166941154, "area": 911.061869541},
    "model_146102_93e433ac_0002": {"func": model_146102_93e433ac_0002, "volume": 2.6703537556, "area": 12.252211349},
    "model_146170_5c8504dd_0000": {"func": model_146170_5c8504dd_0000, "volume": 28.75, "area": 82.3994949366},
    "model_146191_0fd44744_0001": {"func": model_146191_0fd44744_0001, "volume": 2.388, "area": 19.508},
    "model_146197_0222a249_0000": {"func": model_146197_0222a249_0000, "volume": 110.2739099416, "area": 227.2344170347},
    "model_146291_6b0c8db3_0001": {"func": model_146291_6b0c8db3_0001, "volume": 0.0645663725, "area": 2.8154867581},
    "model_146321_0dbae658_0006": {"func": model_146321_0dbae658_0006, "volume": 2.3561939518, "area": 23.5619427485},
    "model_146373_341af1db_0000": {"func": model_146373_341af1db_0000, "volume": 18.0765394674, "area": 79.6395292137},
    "model_146477_bee264e8_0000": {"func": model_146477_bee264e8_0000, "volume": 153.9380400259, "area": 1250.7465752104},
    "model_146498_a1bffd0b_0001": {"func": model_146498_a1bffd0b_0001, "volume": 47520000.0000000075, "area": 3327600.0000000005},
    "model_146544_67c41937_0001": {"func": model_146544_67c41937_0001, "volume": 353.7942495883, "area": 444.1371669412},
    "model_146545_f266050f_0001": {"func": model_146545_f266050f_0001, "volume": 119.6073009183, "area": 512},
    "model_146580_1c2df42f_0000": {"func": model_146580_1c2df42f_0000, "volume": 1500, "area": 800},
    "model_146617_2c247f85_0034": {"func": model_146617_2c247f85_0034, "volume": 0.0824668072, "area": 2.3090706004},
    "model_146624_359752bb_0000": {"func": model_146624_359752bb_0000, "volume": 0.0012510998, "area": 0.0657923565},
    "model_146717_3e6a84c1_0010": {"func": model_146717_3e6a84c1_0010, "volume": 0.002708584, "area": 0.6779460005},
    "model_146827_44b163c8_0003": {"func": model_146827_44b163c8_0003, "volume": 1220.625, "area": 715.5},
    "model_146849_d0676b7e_0005": {"func": model_146849_d0676b7e_0005, "volume": 3.0469911184, "area": 12.8476104167},
    "model_146857_25b972d7_0002": {"func": model_146857_25b972d7_0002, "volume": 4.61421421, "area": 37.3064127614},
    "model_146857_25b972d7_0009": {"func": model_146857_25b972d7_0009, "volume": 34.3611696486, "area": 68.7223392973},
    "model_146857_25b972d7_0010": {"func": model_146857_25b972d7_0010, "volume": 2.552544031, "area": 20.81305133},
    "model_147021_113e7fda_0000": {"func": model_147021_113e7fda_0000, "volume": 547.2370235666, "area": 1190.121337636},
    "model_147133_92c04b84_0001": {"func": model_147133_92c04b84_0001, "volume": 1.2817698027, "area": 14.9539810311},
    "model_147133_92c04b84_0003": {"func": model_147133_92c04b84_0003, "volume": 112.4880980097, "area": 255.987248889},
    "model_147134_273aac81_0005": {"func": model_147134_273aac81_0005, "volume": 0.6220353454, "area": 13.131857292},
    "model_147134_273aac81_0006": {"func": model_147134_273aac81_0006, "volume": 0.7068583471, "area": 5.4192473274},
    "model_147134_273aac81_0007": {"func": model_147134_273aac81_0007, "volume": 6.44606196, "area": 133.001062171},
    "model_147140_f824fffe_0002": {"func": model_147140_f824fffe_0002, "volume": 30.2939966038, "area": 118.6800012688},
    "model_147178_2016d56d_0001": {"func": model_147178_2016d56d_0001, "volume": 0.0001925, "area": 0.053},
    "model_147292_7cfe4450_0000": {"func": model_147292_7cfe4450_0000, "volume": 1.8849555922, "area": 12.4407069082},
    "model_147546_ede0f31c_0002": {"func": model_147546_ede0f31c_0002, "volume": 237.5044046114, "area": 793.9432954152},
    "model_147759_44dc68e3_0001": {"func": model_147759_44dc68e3_0001, "volume": 0.3765749746, "area": 5.4720496182},
    "model_148051_66cb4858_0004": {"func": model_148051_66cb4858_0004, "volume": 0.6650535663, "area": 14.6975092608},
    "model_148051_66cb4858_0008": {"func": model_148051_66cb4858_0008, "volume": 0.2477866189, "area": 4.0612362926},
    "model_148051_66cb4858_0009": {"func": model_148051_66cb4858_0009, "volume": 2.6253057568, "area": 106.6126041635},
    "model_148051_66cb4858_0011": {"func": model_148051_66cb4858_0011, "volume": 0.6615515396, "area": 10.2083972444},
    "model_148051_66cb4858_0013": {"func": model_148051_66cb4858_0013, "volume": 12.6709004275, "area": 169.0483957143},
    "model_148051_66cb4858_0014": {"func": model_148051_66cb4858_0014, "volume": 0.5638802112, "area": 6.9884549282},
    "model_148051_66cb4858_0016": {"func": model_148051_66cb4858_0016, "volume": 0.3734946128, "area": 5.6810566308},
    "model_148051_66cb4858_0017": {"func": model_148051_66cb4858_0017, "volume": 0.4454040388, "area": 6.6802255545},
    "model_148051_66cb4858_0019": {"func": model_148051_66cb4858_0019, "volume": 0.0833003638, "area": 3.6342014974},
    "model_148051_66cb4858_0021": {"func": model_148051_66cb4858_0021, "volume": 10.140821906, "area": 381.3739921917},
    "model_148051_66cb4858_0023": {"func": model_148051_66cb4858_0023, "volume": 0.2890164902, "area": 8.9381723661},
    "model_148051_66cb4858_0024": {"func": model_148051_66cb4858_0024, "volume": 1.5374781659, "area": 88.2594327711},
    "model_148051_66cb4858_0025": {"func": model_148051_66cb4858_0025, "volume": 9.0543052732, "area": 340.6347108723},
    "model_148051_66cb4858_0026": {"func": model_148051_66cb4858_0026, "volume": 0.4429512364, "area": 13.0525359781},
    "model_148051_66cb4858_0027": {"func": model_148051_66cb4858_0027, "volume": 0.362075168, "area": 5.9155735973},
    "model_148051_66cb4858_0028": {"func": model_148051_66cb4858_0028, "volume": 0.3090219687, "area": 5.0715816959},
    "model_148051_66cb4858_0032": {"func": model_148051_66cb4858_0032, "volume": 0.2031875977, "area": 8.7664726563},
    "model_148051_66cb4858_0033": {"func": model_148051_66cb4858_0033, "volume": 0.1131184861, "area": 3.2065082662},
    "model_148051_66cb4858_0035": {"func": model_148051_66cb4858_0035, "volume": 8.1097703558, "area": 114.6553846934},
    "model_148051_66cb4858_0036": {"func": model_148051_66cb4858_0036, "volume": 10.9246274372, "area": 411.342739872},
    "model_148051_66cb4858_0037": {"func": model_148051_66cb4858_0037, "volume": 0.4178023246, "area": 7.2278827113},
    "model_148051_66cb4858_0039": {"func": model_148051_66cb4858_0039, "volume": 0.9329978455, "area": 13.7989290718},
    "model_148051_66cb4858_0040": {"func": model_148051_66cb4858_0040, "volume": 0.1583127861, "area": 2.6280992122},
    "model_148051_66cb4858_0042": {"func": model_148051_66cb4858_0042, "volume": 11.5895107498, "area": 435.693033951},
    "model_148051_66cb4858_0043": {"func": model_148051_66cb4858_0043, "volume": 2.9653332409, "area": 79.3868741652},
    "model_148051_66cb4858_0044": {"func": model_148051_66cb4858_0044, "volume": 0.0282796215, "area": 0.5641079357},
    "model_148051_66cb4858_0045": {"func": model_148051_66cb4858_0045, "volume": 2.2497118254, "area": 33.2048003501},
    "model_148051_a453e5db_0000": {"func": model_148051_a453e5db_0000, "volume": 0.8079390907, "area": 54.1170750507},
    "model_148051_a453e5db_0002": {"func": model_148051_a453e5db_0002, "volume": 0.0187022938, "area": 1.5550883635},
    "model_148051_ad8f6d60_0002": {"func": model_148051_ad8f6d60_0002, "volume": 0.0280534406, "area": 2.3031801142},
    "model_148051_ad8f6d60_0004": {"func": model_148051_ad8f6d60_0004, "volume": 0.0786936392, "area": 3.67520353},
    "model_148051_ad8f6d60_0005": {"func": model_148051_ad8f6d60_0005, "volume": 0.9695269088, "area": 64.8895962599},
    "model_148051_ad8f6d60_0006": {"func": model_148051_ad8f6d60_0006, "volume": 0.1538812983, "area": 3.5349409346},
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
